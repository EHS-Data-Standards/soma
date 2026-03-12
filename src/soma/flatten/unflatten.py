"""Unflatten flat rows back to nested SOMA YAML structure.

Reverses the flattening: flat rows -> nested YAML conforming to the source schema.
Reconstructs QuantityValue objects, multivalued lists, polymorphic subclasses.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


def _build_quantity_value(value: Any, unit: Any) -> dict[str, Any] | None:
    """Reconstruct a QuantityValue dict from value and unit strings."""
    if value is None and unit is None:
        return None
    qv: dict[str, Any] = {}
    if value is not None:
        qv["value"] = str(value)
    if unit is not None:
        qv["unit"] = {"name": str(unit)}
    return qv


def _set_nested_path(obj: dict, path: str, value: Any) -> None:
    """Set a value at a dot-separated path in a nested dict, creating intermediate dicts."""
    parts = path.split(".")
    current = obj
    for part in parts[:-1]:
        if part not in current or not isinstance(current[part], dict):
            current[part] = {}
        current = current[part]
    current[parts[-1]] = value


def _group_rows_by_assay(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Group rows by assay id (for reassembling expanded rows)."""
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        assay_id = row.get("id", "")
        groups[assay_id].append(row)
    return dict(groups)


def unflatten_assay(
    rows: list[dict[str, Any]],
    spec: dict[str, Any],
) -> dict[str, Any]:
    """Unflatten one or more flat rows (sharing the same assay id) into a nested assay dict.

    If multiple rows exist, they represent expanded multivalued items.
    """
    rules = spec["flatten_rules"]
    # Use first row for non-expanded fields
    base = rows[0]
    assay: dict[str, Any] = {}

    # 1. Scalars
    for name in rules.get("scalars", []):
        val = base.get(name)
        if val is not None:
            assay[name] = val

    # 2. QuantityValue output slots
    output: dict[str, Any] = {}
    for qv_spec in rules.get("quantity_values", []):
        prefix = qv_spec["prefix"]
        path = qv_spec["path"]
        val = base.get(f"{prefix}_value")
        unit = base.get(f"{prefix}_unit")
        qv = _build_quantity_value(val, unit)
        if qv is not None:
            # path is like "has_specified_output.beat_frequency_hz"
            parts = path.split(".", 1)
            if len(parts) == 2:
                slot_name = parts[1]
                output[slot_name] = qv

    # 3. Non-QV output scalars
    for os_spec in rules.get("output_scalars", []):
        column = os_spec["column"]
        path = os_spec["path"]
        val = base.get(column)
        if val is not None:
            parts = path.split(".", 1)
            if len(parts) == 2:
                output[parts[1]] = val

    if output:
        # Need to add id/name if present (from base row with output_ prefix convention)
        # We'll reconstruct minimal output object
        assay["has_specified_output"] = output

    # 4. Inlined objects
    for inl_spec in rules.get("inlined_objects", []):
        path = inl_spec["path"]
        obj: dict[str, Any] = {}
        for col_spec in inl_spec["columns"]:
            val = base.get(col_spec["column"])
            if val is not None:
                obj[col_spec["slot"]] = val
        if obj:
            _set_nested_path(assay, path, obj)

    # 5. Study subject
    subject: dict[str, Any] = {}
    if "study_subject_common" in rules:
        common = rules["study_subject_common"]
        subject_type = base.get("subject_type")
        if subject_type:
            subject["subject_type"] = subject_type

        for name in common.get("scalars", []):
            val = base.get(f"subject_{name}")
            if val is not None:
                subject[name] = val

        for inl_spec in common.get("inlined_objects", []):
            obj = {}
            for col_spec in inl_spec["columns"]:
                val = base.get(col_spec["column"])
                if val is not None:
                    obj[col_spec["slot"]] = val
            if obj:
                subject[inl_spec["path"]] = obj

    # 6. Polymorphic subject fields
    if "polymorphic" in rules:
        subject_type = base.get("subject_type")
        for poly_spec in rules["polymorphic"]:
            variants = poly_spec.get("variants", {})
            if subject_type and subject_type in variants:
                variant = variants[subject_type]

                for name in variant.get("scalars", []):
                    val = base.get(name)
                    if val is not None:
                        subject[name] = val

                for qv_spec in variant.get("quantity_values", []):
                    prefix = qv_spec["prefix"]
                    val = base.get(f"{prefix}_value")
                    unit = base.get(f"{prefix}_unit")
                    qv = _build_quantity_value(val, unit)
                    if qv is not None:
                        subject[qv_spec["path"]] = qv

                for inl_spec in variant.get("inlined_objects", []):
                    obj = {}
                    for col_spec in inl_spec["columns"]:
                        val = base.get(col_spec["column"])
                        if val is not None:
                            obj[col_spec["slot"]] = val
                    if obj:
                        subject[inl_spec["path"]] = obj

    if subject:
        assay["study_subject"] = subject

    # 7. Multivalued: expand_rows -> reconstruct list
    for mv_spec in rules.get("multivalued", []):
        if mv_spec.get("strategy") == "expand_rows":
            path = mv_spec["path"]
            items = []
            for row in rows:
                item: dict[str, Any] = {}
                has_data = False
                for item_spec in mv_spec.get("per_item", []):
                    if item_spec.get("type") == "quantity_value":
                        prefix = item_spec["prefix"]
                        val = row.get(f"{prefix}_value")
                        unit = row.get(f"{prefix}_unit")
                        qv = _build_quantity_value(val, unit)
                        if qv is not None:
                            _set_nested_path(item, item_spec["slot"], qv)
                            has_data = True
                    else:
                        slot_path = item_spec["slot"]
                        column = item_spec["column"]
                        val = row.get(column)
                        if val is not None:
                            _set_nested_path(item, slot_path, val)
                            has_data = True
                if has_data:
                    items.append(item)
            if items:
                _set_nested_path(assay, path, items)

    # 8. Multivalued: delimited -> split back into list
    for mv_spec in rules.get("multivalued", []):
        if mv_spec.get("strategy") == "delimited":
            path = mv_spec["path"]
            slot = mv_spec["slot"]
            delimiter = mv_spec.get("delimiter", " | ")
            col_name = path.replace(".", "_")
            val = base.get(col_name)
            if val and isinstance(val, str):
                items = [
                    {slot: v.strip()}
                    for v in val.split(delimiter)
                    if v.strip()
                ]
                if items:
                    _set_nested_path(assay, path, items)

    return assay


def unflatten_rows(
    rows: list[dict[str, Any]],
    spec: dict[str, Any],
) -> list[dict[str, Any]]:
    """Unflatten a list of flat rows into a list of nested assay dicts.

    Groups rows by assay id to handle row-expanded multivalued fields.
    """
    grouped = _group_rows_by_assay(rows)
    assays = []
    for _assay_id, group_rows in grouped.items():
        assays.append(unflatten_assay(group_rows, spec))
    return assays


def unflatten_to_container(
    rows: list[dict[str, Any]],
    spec: dict[str, Any],
) -> dict[str, Any]:
    """Unflatten rows into a Container dict.

    Returns a dict with the appropriate container_slot populated.
    """
    container_slot = spec["container_slot"]
    assays = unflatten_rows(rows, spec)
    return {container_slot: assays}


def unflatten_to_yaml(
    rows: list[dict[str, Any]],
    spec: dict[str, Any],
    output_path: str | Path,
) -> Path:
    """Unflatten rows and write to a YAML file."""
    container = unflatten_to_container(rows, spec)
    output_path = Path(output_path)
    with open(output_path, "w") as f:
        yaml.dump(container, f, default_flow_style=False, sort_keys=False)
    return output_path
