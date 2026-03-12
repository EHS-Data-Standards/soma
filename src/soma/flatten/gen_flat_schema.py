"""Generate flat LinkML schemas from FlatteningSpecs.

Produces a flat LinkML schema where all slots are strings, suitable for
validating flat-form data before unflattening.

[Optional/later — placeholder for Phase 3]
"""

from __future__ import annotations

from typing import Any


def generate_flat_schema(specs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Generate a flat LinkML schema dict from flattening specs.

    All slots become string-typed for flat-form validation.
    """
    from soma.flatten.excel_io import _columns_from_spec

    classes = {}
    slots = {}

    for assay_class, spec in specs.items():
        columns = _columns_from_spec(spec)

        # Create a flat class with all columns as string slots
        class_def = {
            "description": f"Flat representation of {assay_class}",
            "slots": columns,
        }
        classes[f"Flat{assay_class}"] = class_def

        for col in columns:
            if col not in slots:
                slots[col] = {
                    "range": "string",
                    "description": f"Flat column: {col}",
                }

    schema = {
        "name": "soma_flat",
        "description": "Flat SOMA schema for spreadsheet validation",
        "id": "https://w3id.org/EHS-Data-Standards/soma_flat",
        "imports": ["linkml:types"],
        "prefixes": {
            "linkml": "https://w3id.org/linkml/",
            "soma_flat": "https://w3id.org/EHS-Data-Standards/soma_flat/",
        },
        "default_prefix": "soma_flat",
        "default_range": "string",
        "classes": classes,
        "slots": slots,
    }

    return schema
