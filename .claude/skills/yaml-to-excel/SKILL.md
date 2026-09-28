---
name: yaml-to-excel
description: Convert validated SOMA YAML to a formatted Excel workbook
user_invocable: true
---

# /yaml-to-excel - YAML to Excel Spreadsheet

Use this skill to convert a validated SOMA YAML file into a formatted Excel workbook.

## Prerequisites

1. The YAML file should be validated first (use `/linkml-validate`)
2. The LinkML-generated Excel scaffold should be up to date at `project/excel/soma.xlsx` (regenerate via `just gen-project` if needed)

## Usage

### Convert a YAML file to Excel

```bash
uv run python scripts/yaml_to_excel.py --input <yaml-file> --output <xlsx-file>
```

### Examples

```bash
# Convert Liu 2024 data
uv run python scripts/yaml_to_excel.py \
  --input tests/data/valid/Container-liu2024-pm25-cftr.yaml \
  --output src/docs/Liu2024_PM25_CFTR_SOMA.xlsx

# Convert Montgomery 2020 data
uv run python scripts/yaml_to_excel.py \
  --input tests/data/valid/Container-montgomery2020-pm25-mucociliary.yaml \
  --output src/docs/Montgomery2020_PM25_Mucociliary_SOMA.xlsx
```

### Use a custom scaffold template

```bash
uv run python scripts/yaml_to_excel.py \
  --input <yaml-file> \
  --output <xlsx-file> \
  --template project/excel/soma.xlsx
```

## What the Script Does

1. Loads and validates the YAML against the SOMA schema
2. Reads the LinkML scaffold (`project/excel/soma.xlsx`) for canonical tab names and column headers
3. Creates tabs for each non-empty collection:
   - **Metadata** - paper-level information from YAML header comments
   - **Protocol** - all protocols
   - **ExposureCondition** - unique exposure conditions referenced by assays
   - **KeyEvent** - unique key events referenced by assays
   - **CellularSystem** - unique cellular study subjects
   - **InVivoSubject** - unique in vivo study subjects
   - Assay tabs (e.g., CFTRFunctionAssay, GeneExpressionAssay, etc.)
   - Output tabs (e.g., CFTRFunctionOutput, GeneExpressionOutput, etc.) -
     one row per output record, i.e. per experimental condition/group, with
     `experimental_group` and `measured_under` columns
   - **Responses** - long-format tab: one row per (output record x measurement)
     with value, unit, central tendency, variability, and sample size - the
     per-condition dose-response table for downstream analysis
   - **ResponseComparison** - analysis-layer changes vs. control (delta,
     change type/direction, p-value, derivation)
   - **KeyEventRelationship** - container-level KE network topology
4. Applies SOMA styling (blue headers, borders, auto-width columns, tab colors)

## Reference Files

| File | Purpose |
|------|---------|
| `scripts/yaml_to_excel.py` | The converter script |
| `scripts/generate_paper_excel.py` | Reference for styling and header definitions |
| `project/excel/soma.xlsx` | LinkML-generated scaffold (canonical structure) |

## Output Verification

After generating an Excel file, verify:
- All expected tabs are present
- Row counts match the number of assays/entities in the YAML
- No empty tabs for collections that have data
- Headers match the schema slot names
