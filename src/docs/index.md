# Outcomes Working Group Data Model

The Outcomes Working Group Data Model is a [LinkML](https://linkml.io/) schema for representing 
Key Event and Outcome measurements, assays, and experimental protocols in the context of environmental 
health sciences (EHS) outcomes research.

## Purpose

This data model provides a standardized way to capture and exchange data about airway biology 
measurements relevant to respiratory health outcomes, including:

- **Ciliary function** - Beat frequency, active area, morphology
- **Airway surface liquid** - ASL height, periciliary layer depth, ion composition
- **Mucociliary clearance** - Transport rates, directionality, clearance efficiency
- **Oxidative stress** - ROS, lipid peroxidation, antioxidant capacity
- **Ion channel function** - CFTR chloride secretion, sweat chloride
- **Signaling pathways** - EGFR phosphorylation, downstream kinases
- **Mucin biology** - Goblet cells, MUC5AC/MUC5B expression
- **Inflammatory markers** - BALF/sputum cell counts, cytokines
- **Lung function** - Spirometry outcomes (FEV1, FVC)
- **Exposure biomarkers** - Cotinine, metals, PAH metabolites

## Microschema Architecture

The schema uses a **microschema architecture** where domain-specific measurement types 
inherit from a common base and can incorporate context mixins for in vitro or in vivo settings.

### Measurement Microschemas

| Microschema | Container Slot | Description |
|-------------|----------------|-------------|
| CiliaryFunctionMeasurement | `ciliary_measurements` | Ciliary beat frequency, active area, morphology |
| ASLMeasurement | `asl_measurements` | Airway surface liquid height, PCL depth, ions |
| MCCMeasurement | `mcc_measurements` | Mucociliary transport and clearance |
| OxidativeStressMeasurement | `oxidative_stress_measurements` | ROS, MDA, 4-HNE, antioxidant enzymes |
| CFTRMeasurement | `cftr_measurements` | CFTR chloride secretion, sweat chloride |
| EGFRMeasurement | `egfr_measurements` | EGFR/ERK/AKT phosphorylation |
| GobletCellMucinMeasurement | `goblet_cell_mucin_measurements` | Goblet cells, MUC5AC/5B expression |
| BALFSputumMeasurement | `balf_sputum_measurements` | Cell differentials, cytokines |
| LungFunctionMeasurement | `lung_function_measurements` | FEV1, FVC, FeNO |
| FoxJMeasurement | `foxj_measurements` | FoxJ1 expression, ciliogenesis |

### Context Mixins

Each measurement can include context about the experimental setting:

| Mixin | Use Case | Key Slots |
|-------|----------|-----------|
| InVitroContext | Cell culture experiments | `cell_culture_system`, `days_at_differentiation`, `passage_number`, `donor_info` |
| InVivoContext | Human/animal samples | `participant`, `sample_type`, `collection_site`, `collection_date` |

### Supporting Entities

| Entity | Container Slot | Description |
|--------|----------------|-------------|
| Protocol | `protocols` | Detailed experimental procedures |
| Method | `methods` | General measurement techniques |
| Assay | `assays` | Specific test definitions |

## Key Features

The schema integrates with major biomedical ontologies:

| Domain | Ontologies |
|--------|-----------|
| Biological Processes | GO (Gene Ontology) |
| Chemicals | ChEBI |
| Phenotypes | HP (Human Phenotype Ontology) |
| Cell Types | CL (Cell Ontology) |
| Environment | ENVO |
| Units | UO, UCUM, QUDT |
| Assays | OBI |

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

All data uses the `Container` class as the root element. Here are examples for each measurement type:

### Ciliary Function Measurement

```yaml
ciliary_measurements:
  CILIARY:001:
    id: "CILIARY:001"
    name: "CBF measurement after ozone exposure"
    observation_type: ciliary_beat_frequency
    quantity_measured:
      value: "8.5"
      unit:
        id: "UO:0000106"
        name: "hertz"
    measurement_method: "high-speed video microscopy"
    measurement_date: "2024-01-15"
    cell_culture_system: "ALI"
    days_at_differentiation: 21
```

### Oxidative Stress Measurement

```yaml
oxidative_stress_measurements:
  OX:001:
    id: "OX:001"
    name: "ROS level after PM2.5 exposure"
    observation_type: reactive_oxygen_species
    quantity_measured:
      value: "2.5"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_method: "DCFDA fluorescence assay"
    cell_culture_system: "ALI"
    days_at_differentiation: 21
```

### Lung Function Measurement (In Vivo)

```yaml
lung_function_measurements:
  LF:001:
    id: "LF:001"
    name: "FEV1 measurement"
    observation_type: fev1
    quantity_measured:
      value: "82.5"
      unit:
        id: "UO:0000187"
        name: "percent predicted"
    measurement_method: "Spirometry"
    participant:
      id: "PARTICIPANT:001"
      name: "Subject A"
```

### Protocol Definition

```yaml
protocols:
  PROTOCOL:001:
    id: "PROTOCOL:001"
    name: "High-speed video microscopy for CBF"
    study_context: in_vitro
    imaging_frame_rate:
      value: "200"
      unit:
        id: "UO:0000106"
        name: "hertz"
    temperature_control:
      value: "37"
      unit:
        id: "UO:0000027"
        name: "degree Celsius"
    replicate_count: 3
```

## Resources

- [GitHub Repository](https://github.com/EHS-Data-Standards/outcomes-working-group)
- [LinkML Documentation](https://linkml.io/linkml/)
- [About This Project](about.md)
