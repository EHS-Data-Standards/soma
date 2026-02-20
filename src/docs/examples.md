# Examples

This page provides comprehensive examples of using the Outcomes Working Group Data Model.
All examples use the `Container` class as the root element and demonstrate real-world
use cases for environmental health research data.

## Quick Start

The simplest way to get started is to pick an example that matches your assay type
and adapt it to your data. Each example shows:

- Required fields for the assay type
- Named measurement slots (e.g., `beat_frequency_hz`, not generic `observation_type`)
- Study subject with appropriate detail level
- Typed protocols with `protocol_type` designator (ImagingProtocol, MolecularAssayProtocol, etc.)

---

## In Vitro Assays

These examples demonstrate assays performed on cell culture systems. The `study_subject`
slot captures the biological model, and typed protocols capture domain-specific details.

### Ciliary Function Assay

Measuring ciliary beat frequency (CBF) in primary human bronchial epithelial cells:

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
    percentage_ciliated_cells:
      value: "65"
      unit:
        id: "UO:0000187"
        name: "percent"
    assay_date: "2024-01-15"
    cell_type:
      id: "CL:0002328"
      name: "bronchial epithelial cell"
    tissue_context:
      id: "UBERON:0002031"
      name: "bronchus"
    study_subject:
      subject_type: TwoDCellCulture
      id: "owg:culture-001"
      name: "Primary HBE ALI culture"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
      primary_cell:
        id: "CL:0002328"
        name: "bronchial epithelial cell"
      anatomical_origin:
        id: "UBERON:0002031"
        name: "bronchus"
      cell_culture_growth_mode: air_liquid_interface
      days_at_differentiation: 21
      donor_info: "Healthy non-smoker, male, age 35, no respiratory disease"
      replicates_per_donor: 3
      substrate_type: transwell_insert
      passage_number: 2
      seeding_density:
        value: "200000"
        unit:
          id: "UO:0000210"
          name: "cells per square centimeter"
      culture_conditions:
        id: "owg:conditions-001"
        name: "Standard ALI culture conditions"
        days_at_air_liquid_interface: 21
        substrate_type: transwell_insert
        cell_culture_growth_mode: air_liquid_interface
        replicates_per_donor: 3
      culture_media:
        id: "owg:media-001"
        name: "PneumaCult-ALI medium"
        base_medium: "PneumaCult-ALI"
        manufacturer: "STEMCELL Technologies"
        supplements:
          - id: "owg:supp-001"
            name: "Hydrocortisone"
            supplement_type: hormone
            concentration:
              value: "0.48"
              unit:
                id: "UO:0000064"
                name: "micrograms per milliliter"
          - id: "owg:supp-002"
            name: "Heparin"
            supplement_type: growth_factor
            concentration:
              value: "4"
              unit:
                id: "UO:0000064"
                name: "micrograms per milliliter"
    imaging_protocol:
      protocol_type: ImagingProtocol
      id: "PROTOCOL:cbf-001"
      name: "High-speed video microscopy for CBF"
      imaging_frame_rate:
        value: "200"
        unit:
          id: "UO:0000105"
          name: "hertz"
      imaging_duration:
        value: "5"
        unit:
          id: "UO:0000010"
          name: "second"
      temperature_control:
        value: "37"
        unit:
          id: "UO:0000027"
          name: "degree Celsius"
```

**Key points:**

- Named measurement slots: `beat_frequency_hz`, `active_area_percentage`, `percentage_ciliated_cells`
- `tissue_context` links the assay to the anatomical site (bronchus)
- `study_subject` captures the full biological model including:
  - `primary_cell` and `anatomical_origin` for cell provenance
  - Culture details: `cell_culture_growth_mode`, `days_at_differentiation`, `passage_number`, `seeding_density`
  - `donor_info` for subject demographics and health status
  - `culture_conditions` with ALI-specific parameters
  - `culture_media` with base medium, manufacturer, and detailed `supplements` (type, concentration)
- `protocol_type: ImagingProtocol` designates the concrete Protocol subclass for polymorphic dispatch
- `imaging_protocol` (ImagingProtocol) with frame rate, duration, and temperature

---

### Airway Surface Liquid (ASL) Assay

Measuring ASL height using confocal microscopy:

```yaml
asl_assays:
  - id: "ASL:001"
    name: "Airway surface liquid height"
    asl_height_um:
      value: "7.2"
      unit:
        id: "UO:0000017"
        name: "micrometer"
    periciliary_layer_depth:
      value: "5.1"
      unit:
        id: "UO:0000017"
        name: "micrometer"
    assay_date: "2024-02-10"
    cell_type:
      id: "CL:0002328"
      name: "bronchial epithelial cell"
    study_subject:
      subject_type: TwoDCellCulture
      id: "owg:culture-002"
      name: "Primary HBE ALI culture"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    imaging_protocol:
      protocol_type: ImagingProtocol
      id: "PROTOCOL:asl-001"
      name: "Confocal microscopy for ASL height"
      spatial_resolution:
        value: "1.5"
        unit:
          id: "UO:0000017"
          name: "micrometer"
      fluorescent_labeling: "Texas Red-dextran"
```

---

### Mucociliary Clearance (MCC) Assay

Tracking fluorescent microsphere transport rate:

```yaml
mcc_assays:
  - id: "MCC:001"
    name: "Mucociliary transport rate"
    transport_rate:
      value: "45.3"
      unit:
        id: "UO:0000103"
        name: "micrometer per second"
    transport_directionality: normal
    assay_date: "2024-03-05"
    cell_type:
      id: "CL:0002328"
      name: "bronchial epithelial cell"
    study_subject:
      subject_type: TwoDCellCulture
      id: "owg:culture-007"
      name: "Primary HBE ALI culture"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    imaging_protocol:
      protocol_type: ImagingProtocol
      id: "PROTOCOL:mcc-001"
      name: "Fluorescent microsphere tracking for MCC"
      fluorescent_tracer: "1-um fluorescent microspheres"
      particle_tracking_method: "automated particle tracking"
```

---

### Oxidative Stress Assay

Measuring reactive oxygen species (ROS) after PM2.5 exposure:

```yaml
oxidative_stress_assays:
  - id: "OX:001"
    name: "ROS level after PM2.5 exposure"
    reactive_oxygen_species:
      value: "2.5"
      unit:
        id: "UO:0000193"
        name: "fold change"
    ros_probe_type: "DCFDA"
    assay_date: "2024-01-20"
    cell_type:
      id: "CL:0002328"
      name: "bronchial epithelial cell"
    study_subject:
      subject_type: TwoDCellCulture
      id: "owg:culture-003"
      name: "Primary HBE ALI culture"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    molecular_protocol:
      protocol_type: MolecularAssayProtocol
      id: "PROTOCOL:ros-001"
      name: "DCFDA ROS detection in ALI cultures"
      detection_method: "fluorescence plate reader"
      normalization_method: "cell count normalization"
```

---

### CFTR Function Assay

Measuring CFTR-mediated chloride secretion using Ussing chambers:

```yaml
cftr_assays:
  - id: "CFTR:001"
    name: "CFTR chloride secretion"
    cftr_chloride_secretion:
      value: "15.2"
      unit:
        id: "UO:0000274"
        name: "microampere per square centimeter"
    stimulation_agent: "forskolin 10 uM"
    inhibitor_used: "CFTRinh-172"
    assay_date: "2024-04-12"
    cell_type:
      id: "CL:0002328"
      name: "bronchial epithelial cell"
    study_subject:
      subject_type: TwoDCellCulture
      id: "owg:culture-006"
      name: "Primary HBE ALI culture"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    follows_protocols:
      - id: "PROTOCOL:cftr-001"
        name: "Ussing chamber short-circuit current protocol"
      - id: "PROTOCOL:cftr-prep-001"
        name: "Tissue mounting and equilibration protocol"
        description: "Pre-assay protocol for mounting tissue in Ussing chamber and equilibrating"
```

**Key points:**

- `follows_protocols` is multivalued — an assay can reference multiple protocols (e.g., the main assay protocol plus a preparation protocol)

---

### EGFR Signaling Assay

Measuring EGFR phosphorylation after smoke exposure:

```yaml
egfr_signaling_assays:
  - id: "EGFR:001"
    name: "EGFR phosphorylation after smoke exposure"
    egfr_phosphorylation_y1068:
      value: "3.2"
      unit:
        id: "UO:0000193"
        name: "fold change"
    total_egfr_protein:
      value: "1.0"
      unit:
        id: "UO:0000193"
        name: "fold change"
    normalization_reference: "beta-actin"
    assay_date: "2024-05-08"
    cell_type:
      id: "CL:0002328"
      name: "bronchial epithelial cell"
    study_subject:
      subject_type: TwoDCellCulture
      id: "owg:culture-005"
      name: "Primary HBE ALI culture"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    molecular_protocol:
      protocol_type: MolecularAssayProtocol
      id: "PROTOCOL:wb-001"
      name: "Western blot for phospho-EGFR"
      detection_method: "chemiluminescence"
      antibodies_used:
        - "anti-pEGFR Y1068 (Cell Signaling #3777)"
        - "anti-total EGFR (Cell Signaling #4267)"
      normalization_method: "total protein normalization"
```

---

### Goblet Cell Assay

Measuring MUC5AC expression and goblet cell quantification:

```yaml
goblet_cell_assays:
  - id: "GCM:001"
    name: "MUC5AC expression and goblet cell quantification"
    muc5ac_mrna_expression:
      value: "4.8"
      unit:
        id: "UO:0000193"
        name: "fold change"
    goblet_cell_percentage:
      value: "28"
      unit:
        id: "UO:0000187"
        name: "percent"
    assay_date: "2024-06-15"
    cell_type:
      id: "CL:0002328"
      name: "bronchial epithelial cell"
    study_subject:
      subject_type: TwoDCellCulture
      id: "owg:culture-004"
      name: "Primary HBE ALI culture"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    staining_protocol:
      protocol_type: StainingProtocol
      id: "PROTOCOL:stain-001"
      name: "AB-PAS staining for goblet cells"
      staining_type: "AB-PAS"
      fixation_method: "4% paraformaldehyde"
      counterstain: "hematoxylin"
```

---

### FoxJ Expression Assay

Measuring FoxJ1 transcription factor expression (master regulator of ciliogenesis):

```yaml
foxj_assays:
  - id: "FOXJ:001"
    name: "FoxJ1 mRNA expression"
    foxj1_mrna_expression:
      value: "0.65"
      unit:
        id: "UO:0000193"
        name: "fold change"
    foxj1_positive_cell_percentage:
      value: "42"
      unit:
        id: "UO:0000187"
        name: "percent"
    assay_date: "2024-09-05"
    cell_type:
      id: "CL:0002328"
      name: "bronchial epithelial cell"
    study_subject:
      subject_type: TwoDCellCulture
      id: "owg:culture-008"
      name: "Primary HBE ALI culture"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    molecular_protocol:
      protocol_type: MolecularAssayProtocol
      id: "PROTOCOL:qpcr-001"
      name: "qRT-PCR for FoxJ1"
      detection_method: "SYBR Green qPCR"
      reference_gene: "GAPDH"
```

---

### Gene Expression Assay

Measuring target gene mRNA expression:

```yaml
gene_expression_assays:
  - id: "GE:001"
    name: "IL-8 gene expression after exposure"
    target_gene: "PR:000006689"
    mrna_level:
      value: "3.5"
      unit:
        id: "UO:0000193"
        name: "fold change"
    gene_expression_method: "qRT-PCR"
    normalization_reference: "GAPDH"
    assay_date: "2024-10-01"
    cell_type:
      id: "CL:0002328"
      name: "bronchial epithelial cell"
    study_subject:
      subject_type: TwoDCellCulture
      id: "owg:culture-009"
      name: "Primary HBE ALI culture"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    molecular_protocol:
      protocol_type: MolecularAssayProtocol
      id: "PROTOCOL:qpcr-002"
      name: "qRT-PCR for cytokine expression"
      detection_method: "TaqMan qPCR"
      reference_gene: "GAPDH"
      platform: "QuantStudio 6"
```

---

## In Vivo Assays

These examples demonstrate assays from human or animal subjects. The `study_subject`
slot uses InVivoSubject-level properties including `age`, `sex`, `sample_type`,
`collection_site`, and `subject_characteristics`.

### Lung Function Assay

Spirometry measurement from a human subject:

```yaml
lung_function_assays:
  - id: "LF:001"
    name: "FEV1 measurement"
    fev1:
      value: "82.5"
      unit:
        id: "UO:0000187"
        name: "percent predicted"
    fvc:
      value: "95.0"
      unit:
        id: "UO:0000187"
        name: "percent predicted"
    reference_dataset: "GLI-2012"
    assay_date: "2024-08-10"
    study_subject:
      subject_type: InVivoSubject
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
      subject_characteristics: "Non-smoker, no respiratory disease"
    spirometry_protocol:
      protocol_type: SpirometryProtocol
      id: "PROTOCOL:spiro-001"
      name: "Pre- and post-bronchodilator spirometry"
      spirometry_standard: "ATS/ERS 2019"
      bronchodilator_agent: "albuterol"
      bronchodilator_dose:
        value: "400"
        unit:
          id: "UO:0000022"
          name: "microgram"
```

**Key points:**

- `study_subject` includes InVivoSubject slots: `age`, `sex`, `subject_characteristics`
- `protocol_type: SpirometryProtocol` designates the concrete Protocol subclass
- `spirometry_protocol` (SpirometryProtocol) with standards and bronchodilator details

---

### BALF/Sputum Assay

Inflammatory cell differential from induced sputum:

```yaml
balf_sputum_assays:
  - id: "BALF:001"
    name: "Neutrophil percentage in induced sputum"
    neutrophil_percentage:
      value: "45.0"
      unit:
        id: "UO:0000187"
        name: "percent"
    il8_concentration:
      value: "250"
      unit:
        id: "UO:0000175"
        name: "picogram per milliliter"
    assay_date: "2024-07-22"
    cell_type:
      id: "CL:0000775"
      name: "neutrophil"
    study_subject:
      subject_type: InVivoSubject
      id: "SUBJECT:001"
      name: "Subject A"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
      age:
        value: "45"
        unit:
          id: "UO:0000036"
          name: "year"
      sex: "female"
      sample_type: sputum
      collection_site: "pulmonary clinic"
      subject_characteristics: "Non-smoker, mild asthma"
    molecular_protocol:
      protocol_type: MolecularAssayProtocol
      id: "PROTOCOL:balf-001"
      name: "Sputum cell differential protocol"
      detection_method: "cytospin and Diff-Quik staining"
```

---

## Protocols

The schema supports detailed documentation of experimental procedures through
typed Protocols (specific procedures).

**Key protocol features:**

- **`protocol_type`** (on Protocol): designates which concrete Protocol subclass is
  instantiated (e.g., `ImagingProtocol`, `StainingProtocol`, `SpirometryProtocol`,
  `MolecularAssayProtocol`). This enables polymorphic dispatch — when protocols are
  referenced via `follows_protocols` or `sub_protocols`, the `protocol_type` field
  tells the system which subclass to use for validation and deserialization.
- **`follows_protocols`** (on Assay): multivalued — an assay can reference multiple protocols
- **`sub_protocols`** (on Protocol): protocols can compose other protocols to represent
  composite workflows (e.g., sample prep, wash steps, post-processing)
- **`equipment_required`** (on Protocol): list of equipment needed for the protocol
- Any Protocol subclass (ImagingProtocol, MolecularAssayProtocol, StainingProtocol,
  SpirometryProtocol) is valid wherever Protocol is expected

### Protocol Definition (Base) with Sub-Protocols

A protocol using base Protocol slots, including `sub_protocols` to compose
reusable workflow steps:

```yaml
protocols:
  - id: "PROTOCOL:001"
    name: "High-speed video microscopy for CBF"
    description: "Protocol for measuring ciliary beat frequency using high-speed video microscopy"
    protocol_version: "2.1"
    temperature_control:
      value: "37"
      unit:
        id: "UO:0000027"
        name: "degree Celsius"
    quality_control_criteria: "Minimum 5 fields per insert, discard if >50% debris"
    replicate_requirements: 3
    sub_protocols:
      - id: "PROTOCOL:001a"
        name: "Sample preparation for CBF imaging"
        description: "Pre-imaging wash and equilibration steps"
        protocol_version: "1.0"
        temperature_control:
          value: "37"
          unit:
            id: "UO:0000027"
            name: "degree Celsius"
      - id: "PROTOCOL:001b"
        name: "Post-imaging data export"
        description: "Steps for exporting and archiving video files after acquisition"
        protocol_version: "1.0"
```

**Key points:**

- `sub_protocols` allows a protocol to reference other protocols as part of its workflow
- Sub-protocols can be any Protocol subclass (e.g., an ImagingProtocol can include a
  StainingProtocol as a preparation step)
- This enables reuse of common steps (wash protocols, fixation, equilibration) across
  multiple parent protocols

---

### Typed Protocols on Assays

Assays reference typed protocols directly for domain-specific details.
The `protocol_type` field designates which concrete Protocol subclass is being used.
The base `follows_protocols` slot is also available for general protocol references:

```yaml
# ImagingProtocol on a CiliaryFunctionAssay
ciliary_function_assays:
  - id: "CILIARY:001"
    name: "CBF measurement"
    beat_frequency_hz:
      value: "12.5"
      unit:
        id: "UO:0000106"
        name: "hertz"
    assay_date: "2024-01-15"
    study_subject:
      subject_type: TwoDCellCulture
      id: "owg:culture-001"
      name: "Primary HBE ALI culture"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    imaging_protocol:
      protocol_type: ImagingProtocol
      id: "PROTOCOL:cbf-001"
      name: "CBF measurement by high-speed microscopy"
      imaging_frame_rate:
        value: "200"
        unit:
          id: "UO:0000105"
          name: "hertz"
      temperature_control:
        value: "37"
        unit:
          id: "UO:0000027"
          name: "degree Celsius"
```

---

## Comprehensive AOP Example: PM2.5 Exposure -> Impaired Lung Function

This comprehensive example demonstrates an Adverse Outcome Pathway (AOP) for particulate
matter (PM2.5) exposure leading to impaired lung function. The pathway includes:

- **MIE (Molecular Initiating Event)**: Oxidative stress
- **KE1 (Key Event 1)**: EGFR activation/phosphorylation
- **KE2 (Key Event 2)**: Goblet cell hyperplasia and mucin hypersecretion
- **KE3 (Key Event 3)**: Impaired mucociliary clearance
- **AO (Adverse Outcome)**: Reduced lung function

**Study Design:**

- In vitro: Primary human bronchial epithelial (HBE) cells at ALI
- In vivo: Clinical cohort with spirometry
- Exposure: PM2.5 (10 ug/cm2) vs. clean air control
- Timepoints: 4h (early), 24h (intermediate), 7d (late)

**See [`Container-comprehensive_aop_lung.yaml`](../examples/Container-comprehensive_aop_lung.yaml)
and [`assay_centric_example.yaml`](../examples/assay_centric_example.yaml) for the full data files.**

Key features demonstrated in the comprehensive example:

- **AOP linkage**: Each assay uses `informs_on_key_event` to connect to the biological pathway
- **Named measurement slots**: `reactive_oxygen_species`, `egfr_phosphorylation_y1068`, `beat_frequency_hz`, `fev1`
- **Typed protocols** with `protocol_type` designator: ImagingProtocol, MolecularAssayProtocol, StainingProtocol, SpirometryProtocol
- **In vitro study subjects**: StudySubject with `model_species` for cell culture assays
- **In vivo study subjects**: InVivoSubject with `age`, `sex`, `subject_characteristics` for clinical assays
- **Input samples**: `input_sample` with exposure conditions and duration
- **Time-course data**: Multiple timepoints per assay type showing dose-response

---

## Next Steps

- Browse the complete [Schema Documentation](elements/index.md) for all available classes and slots
- Read [About](about.md) to learn more about the project goals
- Visit the [GitHub Repository](https://github.com/EHS-Data-Standards/outcomes-working-group) to contribute
