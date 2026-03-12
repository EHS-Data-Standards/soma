"""Auto-generate FlatteningSpec YAML files by introspecting the LinkML schema.

Uses SchemaView to walk each assay class hierarchy, identify QuantityValue-typed
slots, multivalued inlined slots, polymorphic slots, and generate declarative
flattening specs per assay type.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml
from linkml_runtime.utils.schemaview import SchemaView

# Mapping from Container slot name to assay class name
ASSAY_COLLECTION_SLOTS = {
    "ciliary_function_assays": "CiliaryFunctionAssay",
    "asl_assays": "ASLAssay",
    "mcc_assays": "MucociliaryClearanceAssay",
    "oxidative_stress_assays": "OxidativeStressAssay",
    "cftr_assays": "CFTRFunctionAssay",
    "egfr_signaling_assays": "EGFRSignalingAssay",
    "goblet_cell_assays": "GobletCellAssay",
    "balf_sputum_assays": "BALFSputumAssay",
    "lung_function_assays": "LungFunctionAssay",
    "foxj_assays": "FoxJExpressionAssay",
    "gene_expression_assays": "GeneExpressionAssay",
}

# Classes that are QuantityValue-like (value + unit)
QV_CLASS = "QuantityValue"

# Known polymorphic base classes and their concrete subclasses
STUDY_SUBJECT_SUBCLASSES = ["CellularSystem", "InVivoSubject", "PopulationSubject"]
PROTOCOL_SUBCLASSES = [
    "ImagingProtocol",
    "StainingProtocol",
    "SpirometryProtocol",
    "MolecularAssayProtocol",
]


def _is_quantity_value(sv: SchemaView, range_name: str | None) -> bool:
    """Check if a range is QuantityValue."""
    if range_name is None:
        return False
    if range_name == QV_CLASS:
        return True
    ancestors = sv.class_ancestors(range_name) if range_name in sv.all_classes() else []
    return QV_CLASS in ancestors


def _is_named_entity_like(sv: SchemaView, range_name: str | None) -> bool:
    """Check if a range is a NamedEntity subclass (has id + name slots)."""
    if range_name is None:
        return False
    if range_name not in sv.all_classes():
        return False
    cls_slots = [s.name for s in sv.class_induced_slots(range_name)]
    return "id" in cls_slots and "name" in cls_slots


def _get_output_class(sv: SchemaView, assay_class: str) -> str | None:
    """Get the output measurement class for an assay by checking has_specified_output range."""
    for slot in sv.class_induced_slots(assay_class):
        if slot.name == "has_specified_output":
            return slot.range
    return None


def _get_output_slots(sv: SchemaView, output_class: str) -> list[dict[str, Any]]:
    """Get measurement slots from an output class, categorized by type."""
    quantity_values = []
    scalars = []
    enum_slots = []

    # Get slots defined directly on this output class (not inherited from base)
    base_slots = set()
    for ancestor in sv.class_ancestors(output_class):
        if ancestor == output_class:
            continue
        for s in sv.class_induced_slots(ancestor):
            base_slots.add(s.name)

    for slot in sv.class_induced_slots(output_class):
        if slot.name in base_slots:
            continue  # skip inherited id, name, description
        if slot.name in ("id", "name", "description"):
            continue

        if _is_quantity_value(sv, slot.range):
            quantity_values.append({
                "path": f"has_specified_output.{slot.name}",
                "prefix": slot.name,
            })
        elif slot.range and slot.range in sv.all_enums():
            enum_slots.append(slot.name)
        elif slot.multivalued:
            scalars.append(slot.name)  # multivalued strings go as scalars (delimited)
        else:
            scalars.append(slot.name)

    return quantity_values, scalars, enum_slots


def _get_assay_own_slots(sv: SchemaView, assay_class: str) -> list[str]:
    """Get slots defined directly on an assay subclass (not on Assay base)."""
    base_slots = set()
    for ancestor in sv.class_ancestors(assay_class):
        if ancestor == assay_class:
            continue
        for s in sv.class_induced_slots(ancestor):
            base_slots.add(s.name)

    own_slots = []
    for slot in sv.class_induced_slots(assay_class):
        if slot.name not in base_slots and slot.name not in ("id", "name", "description"):
            own_slots.append(slot.name)
    return own_slots


def _build_polymorphic_subject_rules(sv: SchemaView) -> list[dict[str, Any]]:
    """Build polymorphic flattening rules for study_subject."""
    variants = {}

    for subclass_name in STUDY_SUBJECT_SUBCLASSES:
        if subclass_name not in sv.all_classes():
            continue

        # Get slots specific to this subclass
        base_slots = set()
        for ancestor in sv.class_ancestors(subclass_name):
            if ancestor == subclass_name:
                continue
            for s in sv.class_induced_slots(ancestor):
                base_slots.add(s.name)

        scalars = []
        qvs = []
        inlined = []

        for slot in sv.class_induced_slots(subclass_name):
            if slot.name in base_slots or slot.name in ("id", "name", "description", "subject_type", "model_species"):
                continue

            if _is_quantity_value(sv, slot.range):
                qvs.append({"path": slot.name, "prefix": slot.name})
            elif slot.range and slot.range in sv.all_classes() and _is_named_entity_like(sv, slot.range):
                if not slot.multivalued:
                    inlined.append({
                        "path": slot.name,
                        "columns": [
                            {"slot": "id", "column": f"{slot.name}_id"},
                            {"slot": "name", "column": f"{slot.name}_name"},
                        ],
                    })
                # Skip multivalued inlined for now (like culture_media.supplements)
            elif slot.range and slot.range in sv.all_enums():
                scalars.append(slot.name)
            elif not slot.multivalued:
                scalars.append(slot.name)

        variant_spec: dict[str, Any] = {}
        if scalars:
            variant_spec["scalars"] = scalars
        if qvs:
            variant_spec["quantity_values"] = qvs
        if inlined:
            variant_spec["inlined_objects"] = inlined

        if variant_spec:
            variants[subclass_name] = variant_spec

    if not variants:
        return []

    return [{
        "path": "study_subject",
        "discriminator": "subject_type",
        "variants": variants,
    }]


def _build_exposure_rules() -> list[dict[str, Any]]:
    """Build multivalued rules for exposure conditions (row expansion)."""
    return [{
        "path": "has_exposure_condition",
        "strategy": "expand_rows",
        "per_item": [
            {"slot": "id", "column": "exposure_id"},
            {"slot": "name", "column": "exposure_name"},
            {"slot": "exposure_agent.name", "column": "exposure_agent"},
            {"slot": "exposure_agent.id", "column": "exposure_agent_id"},
            {"slot": "exposure_concentration", "type": "quantity_value", "prefix": "exposure_concentration"},
            {"slot": "exposure_duration", "type": "quantity_value", "prefix": "exposure_duration"},
            {"slot": "timing_post_exposure", "type": "quantity_value", "prefix": "timing_post_exposure"},
        ],
    }]


def _build_protocol_rules() -> list[dict[str, Any]]:
    """Build multivalued rules for protocols (delimited)."""
    return [{
        "path": "follows_protocols",
        "strategy": "delimited",
        "delimiter": " | ",
        "slot": "name",
    }]


def _build_supplement_rules() -> list[dict[str, Any]]:
    """Build rules for culture media supplements (delimited)."""
    return [{
        "path": "study_subject.culture_media.supplements",
        "strategy": "delimited",
        "delimiter": " | ",
        "slot": "name",
    }]


def generate_flattening_spec(
    sv: SchemaView,
    assay_class: str,
    container_slot: str,
) -> dict[str, Any]:
    """Generate a FlatteningSpec dict for a single assay type.

    Args:
        sv: SchemaView of the merged schema
        assay_class: Name of the assay class (e.g. 'CiliaryFunctionAssay')
        container_slot: Name of the Container slot (e.g. 'ciliary_function_assays')

    Returns:
        A dict representing the flattening spec YAML
    """
    output_class = _get_output_class(sv, assay_class)

    # Build flatten rules
    rules: dict[str, Any] = {}

    # 1. Scalar assay-level slots
    assay_scalars = ["id", "name", "assay_date"]
    # Add assay-specific scalars
    own_slots = _get_assay_own_slots(sv, assay_class)
    for s in own_slots:
        slot_def = sv.get_slot(s)
        if slot_def and slot_def.range and not _is_quantity_value(sv, slot_def.range):
            if slot_def.range not in sv.all_classes() or slot_def.range in sv.all_enums():
                assay_scalars.append(s)
            elif slot_def.range == "string" or slot_def.range in ("integer", "float", "date", "boolean", "uriorcurie"):
                assay_scalars.append(s)

    rules["scalars"] = assay_scalars

    # 2. QuantityValue slots from output class
    if output_class:
        qvs, output_scalars, output_enums = _get_output_slots(sv, output_class)
        if qvs:
            rules["quantity_values"] = qvs
        # Output scalars (enum values, strings)
        if output_scalars or output_enums:
            all_output_scalars = output_scalars + output_enums
            rules["output_scalars"] = [
                {"path": f"has_specified_output.{s}", "column": s}
                for s in all_output_scalars
            ]

    # 3. Inlined object: informs_on_key_event
    rules["inlined_objects"] = [{
        "path": "informs_on_key_event",
        "columns": [
            {"slot": "id", "column": "key_event_id"},
            {"slot": "name", "column": "key_event_name"},
        ],
    }]

    # 4. Study subject common fields + polymorphic dispatch
    rules["study_subject_common"] = {
        "scalars": ["id", "name"],
        "inlined_objects": [
            {
                "path": "model_species",
                "columns": [
                    {"slot": "id", "column": "model_species_id"},
                    {"slot": "name", "column": "model_species_name"},
                ],
            },
        ],
    }

    # 5. Polymorphic subject rules
    polymorphic = _build_polymorphic_subject_rules(sv)
    if polymorphic:
        rules["polymorphic"] = polymorphic

    # 6. Multivalued: exposures (row expansion)
    multivalued = _build_exposure_rules()
    # Add protocols (delimited)
    multivalued.extend(_build_protocol_rules())
    # Add supplements (delimited) — only relevant for CellularSystem subjects
    multivalued.extend(_build_supplement_rules())
    rules["multivalued"] = multivalued

    spec = {
        "source_class": assay_class,
        "container_slot": container_slot,
        "target_sheet": assay_class,
        "flatten_rules": rules,
    }

    return spec


def _to_plain(obj: Any) -> Any:
    """Recursively convert LinkML runtime objects (SlotDefinitionName etc.) to plain Python types."""
    if isinstance(obj, dict):
        return {str(k): _to_plain(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_to_plain(v) for v in obj]
    if isinstance(obj, str):
        return str(obj)  # converts SlotDefinitionName -> str
    return obj


def introspect_schema(
    schema_path: str | Path,
    assay_types: list[str] | None = None,
    output_dir: str | Path | None = None,
) -> dict[str, dict[str, Any]]:
    """Introspect the SOMA schema and generate flattening specs.

    Args:
        schema_path: Path to the main soma.yaml schema file
        assay_types: Optional list of assay class names to generate specs for.
                     If None, generates for all 11 assay types.
        output_dir: Optional directory to write spec YAML files to.

    Returns:
        Dict mapping assay class name to its FlatteningSpec dict
    """
    sv = SchemaView(str(schema_path))

    specs = {}
    for slot_name, class_name in ASSAY_COLLECTION_SLOTS.items():
        if assay_types and class_name not in assay_types:
            continue

        spec = _to_plain(generate_flattening_spec(sv, class_name, slot_name))
        specs[class_name] = spec

        if output_dir:
            out_path = Path(output_dir)
            out_path.mkdir(parents=True, exist_ok=True)
            # Convert CamelCase to snake_case for filename
            # Handle consecutive capitals (e.g. CFTR -> cftr, EGFR -> egfr)
            snake_name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", class_name)
            snake_name = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", snake_name).lower()
            spec_file = out_path / f"{snake_name}.flat.yaml"
            with open(spec_file, "w") as f:
                yaml.dump(spec, f, default_flow_style=False, sort_keys=False)

    return specs
