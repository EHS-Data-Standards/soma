# Outcomes Working Group Data Model

The Outcomes Working Group Data Model is a [LinkML](https://linkml.io/) schema for representing
Key Event and Outcome measurements, assays, and experimental protocols in the context of environmental
health sciences (EHS) outcomes research.

## Purpose

This data model provides a standardized way to capture and exchange data about airway biology
assays relevant to respiratory health outcomes, including:

- **Ciliary function** - Beat frequency, active area, morphology
- **Airway surface liquid** - ASL height, periciliary layer depth, ion composition
- **Mucociliary clearance** - Transport rates, directionality, clearance efficiency
- **Oxidative stress** - ROS, lipid peroxidation, antioxidant capacity
- **Ion channel function** - CFTR chloride secretion, sweat chloride
- **Signaling pathways** - EGFR phosphorylation, downstream kinases
- **Mucin biology** - Goblet cells, MUC5AC/MUC5B expression
- **Inflammatory markers** - BALF/sputum cell counts, cytokines
- **Lung function** - Spirometry outcomes (FEV1, FVC)
- **Gene expression** - Target gene mRNA levels

## Assay-Centric Architecture

The schema uses an **assay-centric architecture** where domain-specific assay types
inherit from a common `Assay` base class. Each assay class has **named measurement slots**
(e.g., `beat_frequency_hz`, `asl_height_um`) instead of generic observation types.

### Assay Microschemas

| Assay Class | Container Slot | Description |
|-------------|----------------|-------------|
| CiliaryFunctionAssay | `ciliary_function_assays` | Ciliary beat frequency, active area, morphology |
| ASLAssay | `asl_assays` | Airway surface liquid height, PCL depth, ions |
| MucociliaryClearanceAssay | `mcc_assays` | Mucociliary transport and clearance |
| OxidativeStressAssay | `oxidative_stress_assays` | ROS, MDA, lipid peroxidation |
| CFTRFunctionAssay | `cftr_assays` | CFTR chloride secretion, sweat chloride |
| EGFRSignalingAssay | `egfr_signaling_assays` | EGFR/ERK/AKT phosphorylation |
| GobletCellAssay | `goblet_cell_assays` | Goblet cells, MUC5AC/5B expression |
| BALFSputumAssay | `balf_sputum_assays` | Cell differentials, cytokines |
| LungFunctionAssay | `lung_function_assays` | FEV1, FVC, FeNO |
| FoxJExpressionAssay | `foxj_assays` | FoxJ1 expression, ciliogenesis |
| GeneExpressionAssay | `gene_expression_assays` | Target gene mRNA expression |

### Study Subject Hierarchy

Each assay records its biological system via the `study_subject` slot, which accepts
any class in the StudySubject hierarchy:

| Class | Use Case | Key Slots |
|-------|----------|-----------|
| StudySubject | Base class | `model_species` |
| ModelSystem | Laboratory model systems | (inherits from StudySubject) |
| CellularSystem | Cell-based experiments | `cell_type`, `cell_line`, `culture_conditions`, `days_at_differentiation` |
| TwoDCellCulture | ALI / monolayer cultures | `substrate_type`, `passage_number`, `confluence_level` |
| ThreeDCellCulture | Organoids, spheroids | `scaffold_type`, `organoid_type` |
| InVivoSubject | Human/animal samples | `age`, `sex`, `sample_type`, `collection_site`, `subject_characteristics` |
| PopulationSubject | Epidemiological cohorts | `cohort_name`, `sample_size`, `demographics` |

### Protocol Hierarchy

Assays reference typed protocols for domain-specific procedural details:

| Protocol Class | Slot Name | Key Slots |
|---------------|-----------|-----------|
| Protocol | `follows_protocols` | `protocol_version`, `temperature_control`, `quality_control_criteria`, `sub_protocols` |
| ImagingProtocol | `imaging_protocol` | `imaging_frame_rate`, `imaging_duration`, `spatial_resolution` |
| MolecularAssayProtocol | `molecular_protocol` | `detection_method`, `antibodies_used`, `reference_gene` |
| StainingProtocol | `staining_protocol` | `staining_type`, `fixation_method`, `counterstain` |
| SpirometryProtocol | `spirometry_protocol` | `spirometry_standard`, `bronchodilator_agent` |

Assays reference protocols via `follows_protocols` (multivalued — an assay can follow multiple protocols).
Protocols can compose other protocols via `sub_protocols` (e.g., sample prep, wash steps, post-processing).
Any Protocol subclass is valid in both slots.

### Supporting Entities

| Entity | Container Slot | Description |
|--------|----------------|-------------|
| Protocol | `protocols` | Detailed experimental procedures |
| KeyEvent | `key_events` | AOP key events that assays inform on |
| AdverseOutcomePathway | `adverse_outcome_pathways` | Complete AOP definitions |

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

All data uses the `Container` class as the root element. Here's a quick example:

### Ciliary Function Assay (In Vitro)

```yaml
ciliary_function_assays:
  - id: "CILIARY:001"
    name: "CBF measurement after ozone exposure"
    beat_frequency_hz:
      value: "8.5"
      unit:
        id: "UO:0000106"
        name: "hertz"
    active_area_percentage:
      value: "72"
      unit:
        id: "UO:0000187"
        name: "percent"
    assay_date: "2024-01-15"
    cell_type:
      id: "CL:0002328"
      name: "bronchial epithelial cell"
    study_subject:
      id: "owg:culture-001"
      name: "Primary HBE ALI culture"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    imaging_protocol:
      id: "PROTOCOL:cbf-001"
      name: "High-speed video microscopy for CBF"
      imaging_frame_rate:
        value: "200"
        unit:
          id: "UO:0000105"
          name: "hertz"
```

### Lung Function Assay (In Vivo)

```yaml
lung_function_assays:
  - id: "LF:001"
    name: "FEV1 measurement"
    fev1:
      value: "82.5"
      unit:
        id: "UO:0000187"
        name: "percent predicted"
    reference_dataset: "GLI-2012"
    assay_date: "2024-08-10"
    study_subject:
      id: "SUBJECT:002"
      name: "Subject B"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
      age:
        value: "52"
        unit:
          id: "UO:0000036"
          name: "year"
      sex: "male"
    spirometry_protocol:
      id: "PROTOCOL:spiro-001"
      name: "Pre- and post-bronchodilator spirometry"
      spirometry_standard: "ATS/ERS 2019"
```

**See the [Examples](examples.md) page for comprehensive examples covering all assay types,
protocols, and study configurations.**

## Resources

- [Examples](examples.md) - Comprehensive examples for all assay types
- [Schema Documentation](elements/index.md) - Full schema reference
- [GitHub Repository](https://github.com/EHS-Data-Standards/outcomes-working-group)
- [LinkML Documentation](https://linkml.io/linkml/)
- [About This Project](about.md)
