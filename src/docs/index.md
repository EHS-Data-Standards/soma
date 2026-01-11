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

Navigate to the [Schema Overview](elements/index.md) to explore all classes, slots, and enumerations defined in the model.

### View Diagrams

Visual representations of the schema are available:

- [Mermaid ER Diagram](elements/mermaid_diagram.md) - Interactive entity-relationship diagram
- [SQL ER Diagram](elements/sql_er_diagram.png) - Database schema visualization

### Use the Schema

The schema can be used to:

1. **Validate data** - Ensure your data conforms to the model
2. **Generate code** - Create Python dataclasses, Pydantic models, JSON Schema
3. **Transform data** - Convert between JSON, YAML, RDF, and other formats

## Example Data

The repository includes several complete example datasets demonstrating different aspects
of the data model. Browse them on GitHub or download for local use.

### Complete Study Examples

| Example | Description |
|---------|-------------|
| [Comprehensive Asthma Study](https://github.com/EHS-Data-Standards/outcomes-working-group/blob/main/tests/data/valid/Container-comprehensive_asthma_study.yaml) | Full cohort study with participants, exposures, biomarkers, and phenotypes |
| [PM2.5 Cohort Exposure Study](https://github.com/EHS-Data-Standards/outcomes-working-group/blob/main/tests/data/valid/Container-pm25_cohort_exposure_study.yaml) | Air pollution exposure study with environmental measurements |
| [Synthetic Population Study](https://github.com/EHS-Data-Standards/outcomes-working-group/blob/main/tests/data/valid/Container-synthetic_population_study.yaml) | Geographic hierarchy with households, persons, and study linkage |

### In Vitro and Cell Culture Examples

| Example | Description |
|---------|-------------|
| [Cell Culture Toxicant Study](https://github.com/EHS-Data-Standards/outcomes-working-group/blob/main/tests/data/valid/Container-cell_culture_toxicant_study.yaml) | 2D, 3D, and organ-on-chip models with BaP exposure |
| [In Vitro Airway Measurements](https://github.com/EHS-Data-Standards/outcomes-working-group/blob/main/tests/data/valid/Container-in_vitro_airway_measurements.yaml) | ALI cultures with ciliary function and mucus measurements |

### Measurement Type Examples

| Example | Description |
|---------|-------------|
| [Exposure Measurements](https://github.com/EHS-Data-Standards/outcomes-working-group/blob/main/tests/data/valid/Container-exposure_measurements.yaml) | PM2.5, ozone, and cotinine exposure data |
| [Biomarker Measurements](https://github.com/EHS-Data-Standards/outcomes-working-group/blob/main/tests/data/valid/Container-biomarker_measurements.yaml) | Oxidative stress and inflammatory biomarkers |
| [Phenotype Measurements](https://github.com/EHS-Data-Standards/outcomes-working-group/blob/main/tests/data/valid/Container-phenotype_measurements.yaml) | Pulmonary function and clinical phenotypes |
| [Expression Measurements](https://github.com/EHS-Data-Standards/outcomes-working-group/blob/main/tests/data/valid/Container-expression_measurements.yaml) | Gene and protein expression data |

### Quick Example

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
