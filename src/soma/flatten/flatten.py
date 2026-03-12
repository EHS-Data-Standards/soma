"""Flatten nested SOMA YAML data into flat rows using FlatteningSpec.

Reads nested YAML + FlatteningSpec -> produces flat rows (list of dicts).
Handles: scalar pass-through, QV decomposition, dot-path extraction,
row expansion for multivalued, polymorphic dispatch.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def _resolve_dot_path(obj: dict[str, Any], path: str) -> Any:
    """Resolve a dot-separated path against a nested dict.

    Returns None if any segment is missing.
    """
    parts = path.split(".")
    current = obj
    for part in parts:
        if not isinstance(current, dict):
            return None
        current = current.get(part)
        if current is None:
            return None
    return current


def _extract_quantity_value(obj: dict[str, Any] | None) -> tuple[str | None, str | None]:
    """Extract (value, unit_name) from a QuantityValue dict."""
    if obj is None or not isinstance(obj, dict):
        return None, None
    value = obj.get("value")
    unit_obj = obj.get("unit")
    unit_name = None
    if isinstance(unit_obj, dict):
        unit_name = unit_obj.get("name")
    elif isinstance(unit_obj, str):
        unit_name = unit_obj
    return value, unit_name


def _flatten_scalars(assay: dict[str, Any], scalar_names: list[str]) -> dict[str, Any]:
    """Extract scalar fields from an assay dict."""
    row = {}
    for name in scalar_names:
        row[name] = assay.get(name)
    return row


def _flatten_quantity_values(
    assay: dict[str, Any],
    qv_specs: list[dict[str, Any]],
) -> dict[str, Any]:
    """Extract QuantityValue fields, producing {prefix}_value and {prefix}_unit columns."""
    row = {}
    for qv_spec in qv_specs:
        path = qv_spec["path"]
        prefix = qv_spec["prefix"]
        qv_obj = _resolve_dot_path(assay, path)
        val, unit = _extract_quantity_value(qv_obj)
        row[f"{prefix}_value"] = val
        row[f"{prefix}_unit"] = unit
    return row


def _flatten_output_scalars(
    assay: dict[str, Any],
    output_scalar_specs: list[dict[str, Any]],
) -> dict[str, Any]:
    """Extract non-QV scalar fields from the output object."""
    row = {}
    for spec in output_scalar_specs:
        path = spec["path"]
        column = spec["column"]
        row[column] = _resolve_dot_path(assay, path)
    return row


def _flatten_inlined_objects(
    assay: dict[str, Any],
    inlined_specs: list[dict[str, Any]],
    path_prefix: str = "",
) -> dict[str, Any]:
    """Extract inlined object fields (e.g., key_event_id, key_event_name)."""
    row = {}
    for spec in inlined_specs:
        path = spec["path"]
        full_path = f"{path_prefix}.{path}" if path_prefix else path
        obj = _resolve_dot_path(assay, full_path)
        if obj is None:
            obj = {}
        for col_spec in spec["columns"]:
            slot = col_spec["slot"]
            column = col_spec["column"]
            if isinstance(obj, dict):
                row[column] = obj.get(slot)
            else:
                row[column] = None
    return row


def _flatten_study_subject_common(
    assay: dict[str, Any],
    common_spec: dict[str, Any],
) -> dict[str, Any]:
    """Extract common study_subject fields."""
    row = {}
    subject = assay.get("study_subject", {})
    if not isinstance(subject, dict):
        subject = {}

    # Subject type discriminator
    row["subject_type"] = subject.get("subject_type")

    # Common scalars
    for name in common_spec.get("scalars", []):
        row[f"subject_{name}"] = subject.get(name)

    # Common inlined objects
    for spec in common_spec.get("inlined_objects", []):
        path = spec["path"]
        obj = subject.get(path, {})
        if not isinstance(obj, dict):
            obj = {}
        for col_spec in spec["columns"]:
            row[col_spec["column"]] = obj.get(col_spec["slot"])

    return row


def _flatten_polymorphic_subject(
    assay: dict[str, Any],
    poly_specs: list[dict[str, Any]],
) -> dict[str, Any]:
    """Apply polymorphic flattening based on discriminator."""
    row = {}
    subject = assay.get("study_subject", {})
    if not isinstance(subject, dict):
        return row

    for poly_spec in poly_specs:
        discriminator = poly_spec["discriminator"]
        disc_value = subject.get(discriminator)
        variants = poly_spec.get("variants", {})

        if disc_value and disc_value in variants:
            variant = variants[disc_value]

            # Scalars
            for name in variant.get("scalars", []):
                row[name] = subject.get(name)

            # Quantity values
            for qv_spec in variant.get("quantity_values", []):
                qv_obj = subject.get(qv_spec["path"])
                val, unit = _extract_quantity_value(qv_obj)
                prefix = qv_spec["prefix"]
                row[f"{prefix}_value"] = val
                row[f"{prefix}_unit"] = unit

            # Inlined objects
            for inl_spec in variant.get("inlined_objects", []):
                obj = subject.get(inl_spec["path"], {})
                if not isinstance(obj, dict):
                    obj = {}
                for col_spec in inl_spec["columns"]:
                    row[col_spec["column"]] = obj.get(col_spec["slot"])

    return row


def _expand_exposure_rows(
    base_row: dict[str, Any],
    assay: dict[str, Any],
    mv_spec: dict[str, Any],
) -> list[dict[str, Any]]:
    """Expand multivalued items into separate rows (one row per item)."""
    path = mv_spec["path"]
    items = _resolve_dot_path(assay, path)
    per_item_specs = mv_spec.get("per_item", [])

    if not items or not isinstance(items, list):
        # No items: return single row with blank exposure columns
        row = dict(base_row)
        for item_spec in per_item_specs:
            if item_spec.get("type") == "quantity_value":
                prefix = item_spec["prefix"]
                row[f"{prefix}_value"] = None
                row[f"{prefix}_unit"] = None
            else:
                row[item_spec["column"]] = None
        return [row]

    rows = []
    for item in items:
        if not isinstance(item, dict):
            continue
        row = dict(base_row)
        for item_spec in per_item_specs:
            if item_spec.get("type") == "quantity_value":
                prefix = item_spec["prefix"]
                qv_obj = _resolve_dot_path(item, item_spec["slot"])
                val, unit = _extract_quantity_value(qv_obj)
                row[f"{prefix}_value"] = val
                row[f"{prefix}_unit"] = unit
            else:
                slot_path = item_spec["slot"]
                column = item_spec["column"]
                row[column] = _resolve_dot_path(item, slot_path)
        rows.append(row)

    return rows


def _flatten_delimited(
    assay: dict[str, Any],
    mv_spec: dict[str, Any],
) -> dict[str, Any]:
    """Join multivalued items into a delimited string."""
    path = mv_spec["path"]
    slot = mv_spec["slot"]
    delimiter = mv_spec.get("delimiter", " | ")

    items = _resolve_dot_path(assay, path)
    if not items or not isinstance(items, list):
        # Use last segment of path as column name
        col_name = path.replace(".", "_")
        return {col_name: None}

    values = []
    for item in items:
        if isinstance(item, dict):
            val = item.get(slot)
            if val is not None:
                values.append(str(val))
        elif isinstance(item, str):
            values.append(item)

    col_name = path.replace(".", "_")
    return {col_name: delimiter.join(values) if values else None}


def flatten_assay(
    assay: dict[str, Any],
    spec: dict[str, Any],
) -> list[dict[str, Any]]:
    """Flatten a single assay instance into one or more flat rows.

    Returns multiple rows if row-expanding multivalued fields are present.
    """
    rules = spec["flatten_rules"]

    # Build base row from non-expanding fields
    base_row: dict[str, Any] = {}

    # Scalars
    base_row.update(_flatten_scalars(assay, rules.get("scalars", [])))

    # QuantityValue output slots
    base_row.update(_flatten_quantity_values(assay, rules.get("quantity_values", [])))

    # Non-QV output scalars
    base_row.update(_flatten_output_scalars(assay, rules.get("output_scalars", [])))

    # Inlined objects (key event, etc.)
    base_row.update(_flatten_inlined_objects(assay, rules.get("inlined_objects", [])))

    # Study subject common fields
    if "study_subject_common" in rules:
        base_row.update(_flatten_study_subject_common(assay, rules["study_subject_common"]))

    # Polymorphic subject fields
    if "polymorphic" in rules:
        base_row.update(_flatten_polymorphic_subject(assay, rules["polymorphic"]))

    # Delimited multivalued fields (added to base row)
    for mv_spec in rules.get("multivalued", []):
        if mv_spec.get("strategy") == "delimited":
            base_row.update(_flatten_delimited(assay, mv_spec))

    # Row-expanding multivalued fields
    rows = [base_row]
    for mv_spec in rules.get("multivalued", []):
        if mv_spec.get("strategy") == "expand_rows":
            expanded = []
            for row in rows:
                expanded.extend(_expand_exposure_rows(row, assay, mv_spec))
            rows = expanded

    return rows


def flatten_container(
    data: dict[str, Any],
    spec: dict[str, Any],
) -> list[dict[str, Any]]:
    """Flatten all assays of a given type from a Container dict.

    Args:
        data: The parsed Container YAML dict
        spec: The FlatteningSpec for this assay type

    Returns:
        List of flat row dicts
    """
    container_slot = spec["container_slot"]
    assays = data.get(container_slot, [])
    if not assays:
        return []

    all_rows = []
    for assay in assays:
        all_rows.extend(flatten_assay(assay, spec))

    return all_rows


def flatten_yaml_file(
    yaml_path: str | Path,
    spec: dict[str, Any],
) -> list[dict[str, Any]]:
    """Load a YAML file and flatten using a spec.

    Args:
        yaml_path: Path to a Container YAML file
        spec: The FlatteningSpec dict

    Returns:
        List of flat row dicts
    """
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
    return flatten_container(data, spec)
