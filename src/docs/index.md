---
hide:
  - navigation
  - toc
title: SOMA
---

<style>
.md-content > .md-typeset > h1:first-child { display: none; }
</style>

<div class="aop-hero" markdown>

<div style="text-align: center;" markdown>
![SOMA Logo](soma-logo.svg){ style="width: 100%; max-width: 900px;" }
</div>

<p class="aop-subtitle">A <a href="https://linkml.io/">LinkML</a> schema for representing Key Event and Outcome measurements, assays, and experimental protocols in the context of environmental health sciences (EHS) outcomes research.</p>

</div>

<div class="aop-cards" markdown>

<div class="aop-card aop-card--green" markdown>

### Schema Overview

<a href="elements/" class="aop-btn aop-btn--green">Schema</a>
<a href="examples/" class="aop-btn aop-btn--green">Examples</a>

Browse the assay classes, slots, enumerations, and study subjects defined in the SOMA data model.

</div>

<div class="aop-card aop-card--orange" markdown>

### Contribute

<a href="https://github.com/EHS-Data-Standards/soma" class="aop-btn aop-btn--orange">GitHub Repository</a>
<a href="about/" class="aop-btn aop-btn--orange">About This Project</a>

Submit issues, propose schema changes, or contribute new assay definitions to the SOMA project.

</div>

<div class="aop-card aop-card--blue" markdown>

### Download Content

<a href="artifacts/" class="aop-btn aop-btn--blue">Artifacts</a>

Download generated artifacts: JSON Schema, Python dataclasses, Pydantic models, and Excel templates.

</div>

<div class="aop-card aop-card--purple" markdown>

### Data Entry

<a href="harmonizer.html" class="aop-btn aop-btn--outline">Data Harmonizer</a>

Use the browser-based Data Harmonizer to enter and validate SOMA data interactively.

</div>

</div>

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
any class in the StudySubject hierarchy. The hierarchy has exactly three
subclasses — one for each kind of thing a study can be performed on:

| Class | Use Case | Key Slots |
|-------|----------|-----------|
| StudySubject | Base class | `species` |
| ModelSystem | Laboratory model systems | (inherits from StudySubject) |
| CellularSystem | Cell-based experiments | `cell_type`, `cell_line`, `culture_conditions`, `days_at_differentiation`, `substrate_type`, `passage_number` |
| InVivoSubject | Human/animal samples | `age`, `sex`, `sample_type`, `collection_site`, `subject_characteristics` |
| PopulationSubject | Epidemiological cohorts | `cohort_name`, `sample_size`, `demographics` |

Every study subject records its species in the `species` slot — a human
cohort records *Homo sapiens* there just as a cell line records its species
of origin.

### Ontology Term References

Classes named `*Reference` are **not** study subjects or experimental
entities — they are small value holders (an ontology identifier plus its
label) used as the range of descriptive slots. They all inherit from
`NamedEntity`. The schema has two parallel root classes: `NamedThing`
(id, name, description) for first-class records such as assays, study
subjects, protocols, and key events, and `NamedEntity` (id, name) for
the descriptive value objects that live inside those records' slots.
Not every NamedEntity is an ontology-term pointer — some subclasses, like
`ExposureCondition` and `CellLine`, are things the schema itself defines,
optionally mapped to ontology terms — but the `*Reference` classes are
pure term pointers:

| Reference Class | Ontology | Used By (for example) |
|-----------------|----------|-----------------------|
| SpeciesReference | NCBI Taxonomy | `species` on StudySubject, CellLine |
| CellTypeReference | Cell Ontology (CL) | `cell_type`, `target_cell_type` |
| AnatomicalEntityReference | UBERON | `anatomical_origin` |
| ChemicalEntityReference | ChEBI / ECTO / ENVO | `exposure_agent` |

For example, `SpeciesReference` is how a study subject's `species` slot
points at an NCBI Taxonomy term; it is not a fourth kind of study subject.

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
| AdverseOutcome | `adverse_outcomes` | Outcomes, grounded to MONDO/HPO terms |
| AdverseOutcomePathway | `adverse_outcome_pathways` | Complete AOP definitions |

### From an Outcome to Relevant Assays

An `AdverseOutcome` is a specialized `KeyEvent`, so it inherits
`upstream_key_events`, and its `outcome_term` slot grounds it to a MONDO
disease or HPO phenotype term. This closes the Outcome ↔ Key Event ↔ Assay
traversal: to answer *"I am looking for data on this outcome — what assays
might be relevant?"*, find the outcome by its ontology term, walk its
`upstream_key_events`, and collect every assay whose `informs_on_key_event`
matches the outcome itself or any Key Event in the chain. No curated
`AdverseOutcomePathway` record is required. See
`Container-outcome_connection.yaml` in the examples for a worked traversal.

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
      id: "soma:culture-001"
      name: "Primary HBE ALI culture"
      species:
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
      species:
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

- [LinkML Documentation](https://linkml.io/linkml/)
