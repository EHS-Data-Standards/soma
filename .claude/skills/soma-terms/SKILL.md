---
name: soma-terms
description: >
  Skill for adding and validating ontology term references in the text extracted from PDFs.
  This skill should be used when working with soma files that need ontology term
  annotations (HPO for phenotypes, CL for cell types, GO for biological processes, MONDO
  for diseases, UBERON for anatomical entities, UO for units). Use this skill when adding ontology terms to 
  structured data extracted from text.
---

# SOMA Ontology Terms Skill

## Overview

Add and validate ontology term references in text extracted to conform to the SOMA schema. This ensures
phenotypes, cell types, biological processes, and other entities are properly linked to
authoritative ontology terms with correct IDs and labels.

## When to Use

  - Adding `cell_type` / `target_cell_type` to assays or study subjects (uses CL - Cell Ontology)
  - Adding `species` to study subjects (uses NCBITaxon - NCBI Taxonomy)
  - Adding `exposure_agent` to exposure conditions (uses CHEBI - Chemical Entities of Biological Interest, or ECTO for environmental exposures)
  - Adding `anatomical_origin` / anatomical location slots (uses UBERON - Uber-anatomy Ontology)
  - Adding `unit` to measurement values, durations, or concentrations (uses UO - Units of Measurement)
  - Adding protein or gene targets to expression/signaling assays (uses PR - Protein Ontology, NCBIGene)
  - Adding `cell_line` references on CellularSystem subjects (uses CLO - Cell Line Ontology)
  - Adding `occurs_in_cell_type` / biological process terms to AOP key events (uses GO - Gene Ontology, CL)
  - Adding `assay_type` references to Assay instances (uses OBI - Ontology for Biomedical Investigations)
  - Validating existing ontology term references in Container YAML files
  - Fixing label mismatches between `preferred_term` and the canonical ontology label
  - Replacing overly general terms (e.g., CL:0000066 epithelial cell) with more specific ones (e.g., CL:0002202 epithelial cell of tracheobronchial tree)

## Term Object Structure

All term references follow this YAML structure:

```yaml
# For phenotypes:
phenotype_term:
  preferred_term: <Human readable name>
  term:
    id: HP:XXXXXXX
    label: <Exact HP label from ontology>

# For cell types:
cell_types:
- preferred_term: <Human readable name>
  term:
    id: CL:XXXXXXX
    label: <Exact CL label from ontology>

```

## Ontology Lookup with OAK

Use the Ontology Access Kit (OAK) to look up terms:

### Exact Match
```bash
uv run runoak -i sqlite:obo:hp info "seizure"
# Returns: HP:0001250 ! Seizure
```

### Fuzzy Search
```bash
uv run runoak -i sqlite:obo:hp info "l~cognitive impairment"
# Returns multiple matches - select the most appropriate
```

### Get Full Term Details
```bash
uv run runoak -i sqlite:obo:cl info CL:0000540 -O obo
# Returns complete term information including definition
```

### Common Ontology Prefixes

| Prefix | Ontology | Example |
|--------|----------|---------|
| CHEBI | Chemical Entities of Biological Interest | CHEBI:74481 (PM2.5) |
| CL | Cell Ontology | CL:0002603 (nasal epithelial cell) |
| UBERON | Uber-anatomy Ontology | UBERON:0001707 (nasal cavity) |
| NCBITaxon | NCBI Taxonomy | NCBITaxon:9606 (Homo sapiens) |
| UO | Units of Measurement | UO:0000032 (hour) |
| OBI | Ontology for Biomedical Investigations | OBI:0000070 (assay) |
| GO | Gene Ontology | GO:0005216 (ion channel activity) |
| ECTO | Environmental Conditions, Treatments, and Exposures | ECTO:0001018 |
| PR | Protein Ontology | PR:000003411 (CFTR) |
| HP | Human Phenotype Ontology | HP:0002110 (bronchiectasis) |
| PATO | Phenotypic Quality Ontology | PATO:0000001 (quality) |
| CLO | Cell Line Ontology | CLO:0003679 (Calu-3) |

## Specificity Guidelines

**Critical**: Always use the most specific term that accurately describes the entity:

| Incorrect (too general) | Correct (specific) |
|------------------------|-------------------|
| CL:0000066 epithelial cell | CL:0002202 epithelial cell of tracheobronchial tree |
| HP:0000001 All | HP:0001250 Seizure |
| CL:0000000 cell | CL:0000540 neuron |

When a fuzzy search returns multiple results:
1. Review all candidates
2. Check term definitions with `-O obo` flag
3. Select the term that most precisely matches the biological context
4. If no specific term exists, use the closest parent but note the limitation

## Validation

After adding terms, validate with:

```bash
just validate-terms
```

This checks:
- Term IDs exist in the ontology
- Labels match the canonical ontology labels exactly
- Required fields are present

### Fixing Label Mismatches

If validation reports a label mismatch:
```
LABEL MISMATCH: Cholera.yaml
  Term: HP:0003394
  Expected: Muscle cramps
  Actual: Muscle spasm
```

Update the `label` field to match the ontology's canonical label exactly.

## Batch Processing

To find entries missing term annotations:

```python
import yaml
import glob

for f in glob.glob("kb/disorders/*.yaml"):
    with open(f) as file:
        data = yaml.safe_load(file)
    for pheno in data.get('phenotypes', []):
        if 'phenotype_term' not in pheno:
            print(f"{f}: {pheno.get('name')} - missing phenotype_term")
```

## Common Patterns

### Adding HPO to a Phenotype
1. Look up term: `uv run runoak -i sqlite:obo:hp info "l~<phenotype name>"`
2. Verify specificity: `uv run runoak -i sqlite:obo:hp info <HP:ID> -O obo`
3. Add to YAML:
   ```yaml
   phenotype_term:
     preferred_term: <Original Name>
     term:
       id: <HP:ID>
       label: <Exact label from OAK>
   ```
4. Validate: `just validate-terms`

### Adding CL to Cell Types
1. Look up term: `uv run runoak -i sqlite:obo:cl info "l~<cell type>"`
2. Verify specificity
3. Add `term:` block under the cell_type entry
4. Validate
