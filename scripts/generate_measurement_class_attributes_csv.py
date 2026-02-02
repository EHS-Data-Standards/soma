#!/usr/bin/env python3
"""
Generate a CSV file containing measurement class attributes from the LinkML schema.
This script extracts all measurement classes and their attributes, including
inherited slots and ranges.
"""

import csv
import sys
from pathlib import Path
from linkml_runtime.utils.schemaview import SchemaView

# Add the project root to sys.path to enable imports
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

def get_measurement_classes(schema_view):
    """Get all classes that are subclasses of Measurement."""
    measurement_classes = []

    # Get all classes
    for class_name in schema_view.all_classes():
        class_def = schema_view.get_class(class_name)

        # Check if this is a Measurement class (either ends with "Measurement" or is "Measurement")
        if class_name.endswith("Measurement"):
            measurement_classes.append(class_name)

    return sorted(measurement_classes)

def get_class_attributes(schema_view, class_name):
    """Get all attributes (slots) for a given class, including inherited ones."""
    attributes = []

    # Get all slots for this class (including inherited)
    class_slots = schema_view.class_slots(class_name)

    for slot_name in class_slots:
        slot_def = schema_view.get_slot(slot_name)

        # Get the range (type) of the slot
        range_type = slot_def.range if slot_def.range else "string"

        # Get description
        description = slot_def.description if slot_def.description else ""

        # Determine cardinality
        if slot_def.multivalued:
            cardinality = "multiple"
        else:
            cardinality = "single"

        attributes.append({
            'MeasurementClassName': class_name,
            'AttributeName': slot_name,
            'Cardinality': cardinality,
            'Range': range_type,
            'Description': description.replace('\n', ' ').strip()
        })

    return attributes

def main():
    # Path to the LinkML schema
    schema_path = project_root / "src" / "outcomes_working_group" / "schema" / "v2.yaml"

    if not schema_path.exists():
        print(f"Error: Schema file not found at {schema_path}")
        sys.exit(1)

    print(f"Loading schema from: {schema_path}")

    # Load the schema
    schema_view = SchemaView(str(schema_path))

    # Get all measurement classes
    measurement_classes = get_measurement_classes(schema_view)
    print(f"Found {len(measurement_classes)} measurement classes")

    # Collect all attributes for all measurement classes
    all_attributes = []

    for class_name in measurement_classes:
        print(f"Processing class: {class_name}")
        class_attributes = get_class_attributes(schema_view, class_name)
        all_attributes.extend(class_attributes)

    # Sort by class name and then by attribute name
    all_attributes.sort(key=lambda x: (x['MeasurementClassName'], x['AttributeName']))

    # Write to CSV
    output_path = project_root / "examples" / "measurement_class_attributes.csv"
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['MeasurementClassName', 'AttributeName', 'Cardinality', 'Range', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(all_attributes)

    print(f"\nCSV file generated: {output_path}")
    print(f"Total rows: {len(all_attributes)}")

    # Print summary
    class_summary = {}
    for attr in all_attributes:
        class_name = attr['MeasurementClassName']
        if class_name not in class_summary:
            class_summary[class_name] = 0
        class_summary[class_name] += 1

    print("\nSummary by class:")
    for class_name, count in sorted(class_summary.items()):
        print(f"  {class_name}: {count} attributes")

if __name__ == "__main__":
    main()
