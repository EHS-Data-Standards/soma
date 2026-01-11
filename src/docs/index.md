# Outcomes Working Group Data Model

The Outcomes Working Group Data Model is a [LinkML](https://linkml.io/) schema for representing biological measurements, assays, and experimental protocols in the context of environmental health sciences (EHS) outcomes research.

## Purpose

This data model provides a standardized way to capture and exchange data about:

- **Exposure events** - Chemical, dietary, environmental, and occupational exposures
- **Biological measurements** - Biomarkers, gene/protein expression, phenotypes
- **Health outcomes** - Diseases, adverse outcomes, and phenotypic traits
- **Study metadata** - Studies, cohorts, and participant information
- **Adverse Outcome Pathways (AOPs)** - Mechanistic links from exposure to outcome
- **Model systems** - Cell cultures, organoids, and in vitro exposure systems

## Key Features

The schema integrates with major biomedical ontologies including:

| Domain | Ontologies |
|--------|-----------|
| Chemicals | ChEBI, PubChem, ChEMBL, DSSTox |
| Phenotypes | HP, MP, ZP, UPHENO |
| Diseases | MONDO |
| Anatomy | UBERON |
| Cell Types | CL, CLO |
| Exposures | ECTO, ENVO |
| Units | UO, UCUM, QUDT |

### Flexible Measurement Framework

The model supports multiple measurement types:

- **ExposureMeasurement** - Quantified exposure levels
- **BiomarkerMeasurement** - Biological marker concentrations
- **PhenotypeMeasurement** - Observable trait measurements
- **GeneExpressionMeasurement** - mRNA expression levels
- **ProteinExpressionMeasurement** - Protein levels and modifications
- **AggregatedMeasurement** - Summary statistics across cohorts

### In Vitro Systems Support

Comprehensive support for cell-based model systems:

- 2D and 3D cell cultures
- Co-culture systems
- Air-liquid interface exposures
- Aerosol generation parameters
- Environmental and mechanical measurements

### Synthetic Population Modeling

Geographic hierarchy for population-level analysis:

- States, Counties, Census Tracts, Block Groups
- Households and Persons
- School assignments

## Getting Started

### Browse the Schema

Navigate to the [Schema Overview](elements/index.md) to explore all classes, slots,
and enumerations defined in the model.

### Use the Schema

The schema can be used to:

1. **Validate data** - Ensure your data conforms to the model
2. **Generate code** - Create Python dataclasses, Pydantic models, JSON Schema
3. **Transform data** - Convert between JSON, YAML, RDF, and other formats

## Example Data

The repository includes complete example datasets demonstrating different aspects
of the data model. Click any example to expand and view the full YAML.

### Measurement Type Examples

<details>
<summary><strong>Exposure Measurements</strong> - PM2.5, ozone, and cotinine exposure data</summary>

```yaml
# Example ExposureMeasurement data for environmental toxicant research
# Demonstrates the Quantity pattern with value + unit object
# and OntologyReference pattern with id + name for readability

exposure_measurements:
  - id: owg:exposure-003
    name: PM2.5 personal exposure - Participant P002
    description: 24-hour integrated personal PM2.5 exposure from wearable monitor
    observation_type: pm2_5_exposure
    quantity_measured:
      value: "18.5"
      unit:
        id: UO:0000301
        name: microgram per cubic meter
    measured_entity:
      id: ENVO:01000415
      name: Particulate matter with aerodynamic diameter less than or equal to 2.5 micrometers
    participant:
      id: owg:participant-002
      name: Participant 002
    measurement_method: Personal exposure monitor (RTI MicroPEM)
    measurement_date: "2024-03-16"
    sample_type: air

  - id: owg:exposure-004
    name: Urinary cotinine - Participant P003
    description: Urinary cotinine as biomarker of tobacco smoke exposure
    observation_type: urinary_cotinine_level
    quantity_measured:
      value: "125.0"
      unit:
        id: UO:0000271
        name: nanogram per milliliter
    range_low:
      value: "0.0"
      unit:
        id: UO:0000271
        name: nanogram per milliliter
    range_high:
      value: "10.0"
      unit:
        id: UO:0000271
        name: nanogram per milliliter
    measured_entity:
      id: CHEBI:68641
      name: Cotinine
    participant:
      id: owg:participant-003
      name: Participant 003
    measurement_method: LC-MS/MS
    measurement_date: "2024-03-17"
    sample_type: urine

  - id: owg:exposure-005
    name: Ozone exposure - Participant P004
    description: Ambient ozone concentration at participant residence
    observation_type: ozone_exposure
    quantity_measured:
      value: "0.065"
      unit:
        id: UO:0000170
        name: parts per million
    measured_entity:
      id: CHEBI:25812
      name: Ozone
    participant:
      id: owg:participant-004
      name: Participant 004
    measurement_method: UV photometric analyzer
    measurement_date: "2024-03-18"
    sample_type: air
```

</details>

<details>
<summary><strong>Biomarker Measurements</strong> - Oxidative stress and inflammatory biomarkers</summary>

```yaml
# Example BiomarkerMeasurement data for respiratory health research
# Includes oxidative stress markers, inflammatory cytokines, and CFTR function

biomarker_measurements:
  # Oxidative Stress Markers
  - id: owg:biomarker-001
    name: Exhaled breath condensate 8-isoprostane - Participant P001
    description: Lipid peroxidation marker in exhaled breath condensate
    observation_type: lipid_peroxidation
    quantity_measured:
      value: "45.2"
      unit:
        id: UO:0000274
        name: picogram per milliliter
    range_low:
      value: "10.0"
      unit:
        id: UO:0000274
        name: picogram per milliliter
    range_high:
      value: "35.0"
      unit:
        id: UO:0000274
        name: picogram per milliliter
    biomarker_type: Oxidative stress
    measured_entity:
      id: CHEBI:27894
      name: 8-isoprostane
    participant:
      id: owg:participant-001
      name: Participant 001
    measurement_method: ELISA
    measurement_date: "2024-03-15"

  # Inflammatory Cytokines
  - id: owg:biomarker-003
    name: Sputum IL-8 level - Participant P002
    description: Interleukin-8 concentration in induced sputum
    observation_type: IL8_level
    quantity_measured:
      value: "2450.0"
      unit:
        id: UO:0000274
        name: picogram per milliliter
    range_low:
      value: "100.0"
      unit:
        id: UO:0000274
        name: picogram per milliliter
    range_high:
      value: "1500.0"
      unit:
        id: UO:0000274
        name: picogram per milliliter
    biomarker_type: Pro-inflammatory cytokine
    measured_entity:
      id: PR:000001562
      name: Interleukin-8
    participant:
      id: owg:participant-002
      name: Participant 002
    measurement_method: Multiplex cytokine assay (Luminex)
    measurement_date: "2024-03-16"
```

</details>

<details>
<summary><strong>Phenotype Measurements</strong> - Pulmonary function and clinical phenotypes</summary>

```yaml
# Example PhenotypeMeasurement data for respiratory health outcomes
# Includes lung function tests, FeNO, and ciliary function measurements

phenotype_measurements:
  # Spirometry - Lung Function Tests
  - id: owg:phenotype-001
    name: FEV1 measurement - Participant P001
    description: Forced expiratory volume in 1 second, pre-bronchodilator
    observation_type: FEV1
    quantity_measured:
      value: "2.85"
      unit:
        id: UO:0000099
        name: liter
    range_low:
      value: "3.20"
      unit:
        id: UO:0000099
        name: liter
    range_high:
      value: "4.50"
      unit:
        id: UO:0000099
        name: liter
    phenotype:
      id: HP:0002094
      name: Dyspnea
    participant:
      id: owg:participant-001
      name: Participant 001
    measurement_date: "2024-03-15"

  # FeNO - Airway Inflammation Marker
  - id: owg:phenotype-005
    name: FeNO measurement - Participant P002
    description: Fractional exhaled nitric oxide at 50 mL/s flow rate
    observation_type: FeNO
    quantity_measured:
      value: "42.0"
      unit:
        id: UO:0000170
        name: parts per billion
    range_low:
      value: "0.0"
      unit:
        id: UO:0000170
        name: parts per billion
    range_high:
      value: "25.0"
      unit:
        id: UO:0000170
        name: parts per billion
    phenotype:
      id: HP:0002099
      name: Asthma
    participant:
      id: owg:participant-002
      name: Participant 002
    measurement_date: "2024-03-16"
```

</details>

<details>
<summary><strong>Gene Expression Measurements</strong> - mRNA expression with tissue context</summary>

```yaml
# Expression Measurement Examples
# Demonstrates GeneExpressionMeasurement with target specification and tissue/cell context

gene_expression_measurements:
  # MUC5AC gene expression in bronchial epithelium
  - id: owg:geneexp-001-muc5ac-control
    name: MUC5AC mRNA - Control ALI culture
    description: MUC5AC gene expression in untreated bronchial epithelial cells at ALI
    observation_type: gene_expression
    quantity_measured:
      value: "1.0"
      unit:
        id: UO:0000186
        name: dimensionless unit
    target_gene:
      id: NCBIGENE:4586
      name: Mucin 5AC, oligomeric mucus/gel-forming
      symbol: MUC5AC
    tissue_context:
      id: UBERON:0002031
      name: bronchial epithelium
    cell_type_context:
      id: CL:0000160
      name: goblet cell
    assay_method: qrt_pcr
    normalization_reference: GAPDH
    measurement_date: "2024-03-15"

  - id: owg:geneexp-002-muc5ac-il13
    name: MUC5AC mRNA - IL-13 stimulated
    description: MUC5AC upregulation after IL-13 stimulation (10 ng/mL, 14 days)
    observation_type: gene_expression
    quantity_measured:
      value: "8.5"
      unit:
        id: UO:0000186
        name: dimensionless unit
    target_gene:
      id: NCBIGENE:4586
      name: Mucin 5AC, oligomeric mucus/gel-forming
      symbol: MUC5AC
    tissue_context:
      id: UBERON:0002031
      name: bronchial epithelium
    cell_type_context:
      id: CL:0000160
      name: goblet cell
    assay_method: qrt_pcr
    normalization_reference: GAPDH
    measurement_date: "2024-03-15"
```

</details>

### Complete Study Examples

For larger examples showing complete study structures, see the
[examples directory on GitHub](https://github.com/EHS-Data-Standards/outcomes-working-group/tree/main/tests/data/valid):

- **Comprehensive Asthma Study** - Full cohort with participants, exposures, biomarkers, phenotypes
- **PM2.5 Cohort Exposure Study** - Air pollution exposure with environmental measurements
- **Synthetic Population Study** - Geographic hierarchy with households and study linkage
- **Cell Culture Toxicant Study** - 2D, 3D, and organ-on-chip models with BaP exposure
- **In Vitro Airway Measurements** - ALI cultures with ciliary function and mucus data

### Quick Reference

Here's a minimal example showing the core patterns:

```yaml
studies:
  - id: owg:study001
    name: "Example Exposure Study"
    study_type: "cohort study"
    population: "Adults aged 18-65"

participants:
  - id: owg:participant001
    participant_id: "P001"
    age: 45
    sex: female
    part_of_cohort: owg:cohort001

exposure_measurements:
  - id: owg:measurement001
    name: "Lead blood level"
    participant: owg:participant001
    measured_entity:
      id: CHEBI:25016
      name: "lead atom"
    quantity_measured:
      value: "3.5"
      unit:
        id: UO:0000274
        name: "microgram per deciliter"
```

## Resources

- [GitHub Repository](https://github.com/EHS-Data-Standards/outcomes-working-group)
- [LinkML Documentation](https://linkml.io/linkml/)
- [About This Project](about.md)
