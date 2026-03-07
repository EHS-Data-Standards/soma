# Examples

This page provides comprehensive examples of using the SOMA.
All examples use the `Container` class as the root element and demonstrate real-world
use cases for environmental health research data.

## Quick Start

The simplest way to get started is to pick an example that matches your assay type
and adapt it to your data. Each example shows:

- Required fields for the assay type
- Named measurement slots inside `has_specified_output` (e.g., `beat_frequency_hz`, not generic `observation_type`)
- Study subject with `cell_type` on the subject (not the assay) and appropriate detail level
- Protocols via `follows_protocols` with `protocol_type` designator (ImagingProtocol, MolecularAssayProtocol, etc.)
- Exposure conditions via `has_exposure_condition` (agent, concentration, duration, timing)

## Download Example Data Files

All example data files are available for download. These are the same files used for schema validation testing:

| Assay Type | Download |
|---|---|
| Ciliary Function | [`Container-ciliary_function.yaml`](examples/Container-ciliary_function.yaml) |
| Airway Surface Liquid | [`Container-asl.yaml`](examples/Container-asl.yaml) |
| Mucociliary Clearance | [`Container-mcc.yaml`](examples/Container-mcc.yaml) |
| Oxidative Stress | [`Container-oxidative_stress.yaml`](examples/Container-oxidative_stress.yaml) |
| CFTR Function | [`Container-cftr.yaml`](examples/Container-cftr.yaml) |
| EGFR Signaling | [`Container-egfr.yaml`](examples/Container-egfr.yaml) |
| Goblet Cell / Mucin | [`Container-goblet_cell_mucin.yaml`](examples/Container-goblet_cell_mucin.yaml) |
| FoxJ Expression | [`Container-foxj.yaml`](examples/Container-foxj.yaml) |
| Gene Expression | [`Container-gene_expression.yaml`](examples/Container-gene_expression.yaml) |
| Lung Function | [`Container-lung_function.yaml`](examples/Container-lung_function.yaml) |
| BALF / Sputum | [`Container-balf_sputum.yaml`](examples/Container-balf_sputum.yaml) |
| Protocol (base) | [`Container-protocol.yaml`](examples/Container-protocol.yaml) |
| Comprehensive AOP | [`Container-comprehensive_aop_lung.yaml`](examples/Container-comprehensive_aop_lung.yaml) |

---

## In Vitro Assays

These examples demonstrate assays performed on cell culture systems. The `study_subject`
slot captures the biological model (including `cell_type`), and `follows_protocols` captures domain-specific protocol details.

### Ciliary Function Assay

Measuring ciliary beat frequency (CBF) in primary human bronchial epithelial cells.
This assay supports both in vitro and in vivo contexts (`supported_contexts: in_vitro_or_in_vivo`).

```yaml
ciliary_function_assays:
  # Example 1: In vitro context using ALI culture
  - id: "CILIARY:001"
    name: "CBF measurement after ozone exposure (in vitro)"
    has_specified_output:
      id: "CILIARY:001-output"
      name: "CILIARY:001 measurement results"
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
      cilia_length:
        value: "7.2"
        unit:
          id: "UO:0000017"
          name: "micrometer"
      cilia_per_cell:
        value: "150"
        unit:
          id: "UO:0000189"
          name: "count"
      ciliary_motion_patterns: coordinated
      ciliary_beat_amplitude:
        value: "4.5"
        unit:
          id: "UO:0000017"
          name: "micrometer"
    assay_date: "2024-01-15"
    informs_on_key_event:
      id: "KE:ke3-impaired-ciliary"
      name: "Decreased ciliary function"
      biological_action: decreased
      level_of_biological_organization: cellular
    has_exposure_condition:
      - id: "EXPOSURE:ozone-200ppb-4h"
        name: "Ozone 200 ppb for 4 hours"
        exposure_agent:
          id: "CHEBI:25812"
          name: "ozone"
        exposure_concentration:
          value: "200"
          unit:
            id: "UO:0000169"
            name: "parts per billion"
        exposure_duration:
          value: "4"
          unit:
            id: "UO:0000032"
            name: "hour"
        timing_post_exposure:
          value: "2"
          unit:
            id: "UO:0000032"
            name: "hour"
    study_subject:
      subject_type: CellularSystem
      id: "soma:culture-001"
      name: "Primary HBE ALI culture"
      cell_type:
        id: "CL:0002328"
        name: "bronchial epithelial cell"
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
        id: "soma:conditions-001"
        name: "Standard ALI culture conditions"
        days_at_air_liquid_interface: 21
        substrate_type: transwell_insert
        cell_culture_growth_mode: air_liquid_interface
        replicates_per_donor: 3
      culture_media:
        id: "soma:media-001"
        name: "PneumaCult-ALI medium"
        base_medium: "PneumaCult-ALI"
        manufacturer: "STEMCELL Technologies"
        supplements:
          - id: "soma:supp-001"
            name: "Hydrocortisone"
            supplement_type: hormone
            concentration:
              value: "0.48"
              unit:
                id: "UO:0000064"
                name: "micrograms per milliliter"
          - id: "soma:supp-002"
            name: "Heparin"
            supplement_type: growth_factor
            concentration:
              value: "4"
              unit:
                id: "UO:0000064"
                name: "micrograms per milliliter"
    follows_protocols:
      - protocol_type: ImagingProtocol
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

  # Example 2: In vivo context using OCT-based measurement
  - id: "CILIARY:002"
    name: "In vivo OCT-based ciliary function assessment"
    has_specified_output:
      id: "CILIARY:002-output"
      name: "CILIARY:002 measurement results"
      beat_frequency_hz:
        value: "11.2"
        unit:
          id: "UO:0000106"
          name: "hertz"
      active_area_percentage:
        value: "85"
        unit:
          id: "UO:0000187"
          name: "percent"
    assay_date: "2024-03-10"
    informs_on_key_event:
      id: "KE:ke3-impaired-ciliary"
      name: "Decreased ciliary function"
      biological_action: decreased
      level_of_biological_organization: cellular
    study_subject:
      subject_type: InVivoSubject
      id: "SUBJECT:003"
      name: "Subject C"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
      age:
        value: "38"
        unit:
          id: "UO:0000036"
          name: "year"
      sex: "female"
      subject_characteristics: "Non-smoker, no respiratory disease, healthy volunteer"
      sample_collection_method: "In vivo OCT imaging of nasal epithelium"
      clinical_context: "Baseline assessment, no active respiratory symptoms"
    follows_protocols:
      - protocol_type: ImagingProtocol
        id: "PROTOCOL:oct-001"
        name: "In vivo OCT for ciliary function"
        imaging_frame_rate:
          value: "100"
          unit:
            id: "UO:0000105"
            name: "hertz"
        imaging_duration:
          value: "10"
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

- Named measurement slots inside `has_specified_output`: `beat_frequency_hz`, `active_area_percentage`, `percentage_ciliated_cells`, `cilia_length`, `cilia_per_cell`, `ciliary_motion_patterns`, `ciliary_beat_amplitude`
- `cell_type` is on the `study_subject`, NOT on the assay — this is where cell identity belongs
- `informs_on_key_event` links the assay to AOP Key Event: "Decreased ciliary function"
- `has_exposure_condition` captures the exposure agent, concentration, duration, and timing post-exposure
- `study_subject` captures the full biological model including:
  - `cell_type`, `primary_cell` and `anatomical_origin` for cell provenance
  - Culture details: `cell_culture_growth_mode`, `days_at_differentiation`, `passage_number`, `seeding_density`
  - `donor_info` for subject demographics and health status
  - `culture_conditions` with ALI-specific parameters
  - `culture_media` with base medium, manufacturer, and detailed `supplements` (type, concentration)
- `follows_protocols` references protocols with `protocol_type: ImagingProtocol` for polymorphic dispatch
- Example 2 shows the same assay in an **in vivo** context with `InVivoSubject`

**See [`Container-ciliary_function.yaml`](examples/Container-ciliary_function.yaml) for the full data file.**

---

### Airway Surface Liquid (ASL) Assay

Measuring ASL height using confocal microscopy:

```yaml
asl_assays:
  - id: "ASL:001"
    name: "Airway surface liquid height"
    has_specified_output:
      id: "ASL:001-output"
      name: "ASL:001 measurement results"
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
      mucus_layer_thickness:
        value: "35"
        unit:
          id: "UO:0000017"
          name: "micrometer"
      ion_composition: "Cl- 125 mM, Na+ 140 mM, K+ 15 mM"
      asl_ph:
        value: "7.1"
        unit:
          id: "UO:0000196"
          name: "pH"
    assay_date: "2024-02-10"
    informs_on_key_event:
      id: "KE:ke-decreased-asl"
      name: "Decreased ASL height"
      biological_action: decreased
      level_of_biological_organization: cellular
    study_subject:
      subject_type: CellularSystem
      id: "soma:culture-002"
      name: "Primary HBE ALI culture"
      cell_type:
        id: "CL:0002328"
        name: "bronchial epithelial cell"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    follows_protocols:
      - protocol_type: ImagingProtocol
        id: "PROTOCOL:asl-001"
        name: "Confocal microscopy for ASL height"
        spatial_resolution:
          value: "1.5"
          unit:
            id: "UO:0000017"
            name: "micrometer"
        fluorescent_labeling: "Texas Red-dextran"
        temperature_control:
          value: "37"
          unit:
            id: "UO:0000027"
            name: "degree Celsius"
```

**See [`Container-asl.yaml`](examples/Container-asl.yaml) for the full data file.**

---

### Mucociliary Clearance (MCC) Assay

Tracking fluorescent microsphere transport rate:

```yaml
mcc_assays:
  - id: "MCC:001"
    name: "Mucociliary transport rate"
    has_specified_output:
      id: "MCC:001-output"
      name: "MCC:001 measurement results"
      transport_rate:
        value: "45.3"
        unit:
          id: "UO:0000103"
          name: "micrometer per second"
      transport_directionality: normal
      mucus_layer_thickness:
        value: "28"
        unit:
          id: "UO:0000017"
          name: "micrometer"
      percentage_active_transport:
        value: "82"
        unit:
          id: "UO:0000187"
          name: "percent"
      particle_clearance_time:
        value: "120"
        unit:
          id: "UO:0000010"
          name: "second"
    assay_date: "2024-03-05"
    informs_on_key_event:
      id: "KE:ke3-impaired-mcc"
      name: "Impaired mucociliary clearance"
      biological_action: impaired
      level_of_biological_organization: tissue
    study_subject:
      subject_type: CellularSystem
      id: "soma:culture-007"
      name: "Primary HBE ALI culture"
      cell_type:
        id: "CL:0002328"
        name: "bronchial epithelial cell"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    follows_protocols:
      - protocol_type: ImagingProtocol
        id: "PROTOCOL:mcc-001"
        name: "Fluorescent microsphere tracking for MCC"
        fluorescent_tracer: "1-um fluorescent microspheres"
        particle_tracking_method: "automated particle tracking"
        particle_size:
          value: "1"
          unit:
            id: "UO:0000017"
            name: "micrometer"
        imaging_frame_rate:
          value: "30"
          unit:
            id: "UO:0000105"
            name: "hertz"
```

**See [`Container-mcc.yaml`](examples/Container-mcc.yaml) for the full data file.**

---

### Oxidative Stress Assay

Measuring reactive oxygen species (ROS) after PM2.5 exposure:

```yaml
oxidative_stress_assays:
  - id: "OX:001"
    name: "ROS level after PM2.5 exposure"
    has_specified_output:
      id: "OX:001-output"
      name: "OX:001 measurement results"
      reactive_oxygen_species:
        value: "2.5"
        unit:
          id: "UO:0000193"
          name: "fold change"
      lipid_peroxidation:
        value: "1.8"
        unit:
          id: "UO:0000193"
          name: "fold change"
      malondialdehyde_level:
        value: "3.2"
        unit:
          id: "UO:0000063"
          name: "nanomole per milligram protein"
      protein_carbonyl_content:
        value: "2.1"
        unit:
          id: "UO:0000063"
          name: "nanomole per milligram protein"
      glutathione_ratio:
        value: "0.65"
        unit:
          id: "UO:0000190"
          name: "ratio"
      eight_ohdg_level:
        value: "12.5"
        unit:
          id: "UO:0000275"
          name: "nanogram per milligram creatinine"
      superoxide_dismutase_activity:
        value: "0.75"
        unit:
          id: "UO:0000193"
          name: "fold change"
      catalase_activity:
        value: "0.82"
        unit:
          id: "UO:0000193"
          name: "fold change"
      nrf2_activation:
        value: "2.8"
        unit:
          id: "UO:0000193"
          name: "fold change"
      protein_oxidation_markers:
        - "carbonyl"
        - "nitrotyrosine"
      antioxidant_enzyme_activities: "SOD, catalase, GPx measured"
    ros_probe_type: "DCFDA"
    assay_date: "2024-01-20"
    informs_on_key_event:
      id: "KE:mie-oxidative-stress"
      name: "Increased oxidative stress"
      biological_action: increased
      level_of_biological_organization: molecular
    has_exposure_condition:
      - id: "EXPOSURE:pm25-24h"
        name: "PM2.5 10 ug/cm2 for 24 hours"
        exposure_agent:
          id: "CHEBI:74481"
          name: "PM2.5"
        exposure_concentration:
          value: "10"
          unit:
            id: "UO:0000274"
            name: "microgram per square centimeter"
        exposure_duration:
          value: "24"
          unit:
            id: "UO:0000032"
            name: "hour"
        timing_post_exposure:
          value: "0"
          unit:
            id: "UO:0000032"
            name: "hour"
    study_subject:
      subject_type: CellularSystem
      id: "soma:culture-003"
      name: "Primary HBE ALI culture"
      cell_type:
        id: "CL:0002328"
        name: "bronchial epithelial cell"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    follows_protocols:
      - protocol_type: MolecularAssayProtocol
        id: "PROTOCOL:ros-001"
        name: "DCFDA ROS detection in ALI cultures"
        detection_method: "fluorescence plate reader"
        normalization_method: "cell count normalization"
```

**Key points:**

- Rich set of oxidative stress markers: `reactive_oxygen_species`, `lipid_peroxidation`, `malondialdehyde_level`, `glutathione_ratio`, `nrf2_activation`, and more
- `has_exposure_condition` captures PM2.5 exposure details including `timing_post_exposure`
- `cell_type` is on the `study_subject`, not the assay

**See [`Container-oxidative_stress.yaml`](examples/Container-oxidative_stress.yaml) for the full data file.**

---

### CFTR Function Assay

Measuring CFTR-mediated chloride secretion using Ussing chambers:

```yaml
cftr_assays:
  - id: "CFTR:001"
    name: "CFTR chloride secretion"
    has_specified_output:
      id: "CFTR:001-output"
      name: "CFTR:001 measurement results"
      cftr_chloride_secretion:
        value: "15.2"
        unit:
          id: "UO:0000274"
          name: "microampere per square centimeter"
      cftr_forskolin_response:
        value: "12.8"
        unit:
          id: "UO:0000274"
          name: "microampere per square centimeter"
      inhibitor_sensitive_current:
        value: "14.5"
        unit:
          id: "UO:0000274"
          name: "microampere per square centimeter"
      cftr_specific_current:
        value: "13.9"
        unit:
          id: "UO:0000274"
          name: "microampere per square centimeter"
      sweat_chloride_concentration:
        value: "25"
        unit:
          id: "UO:0000308"
          name: "milliequivalent per liter"
      nasal_potential_difference:
        value: "-18.5"
        unit:
          id: "UO:0000247"
          name: "millivolt"
    stimulation_agent: "forskolin 10 uM"
    inhibitor_used: "CFTRinh-172"
    assay_date: "2024-04-12"
    informs_on_key_event:
      id: "KE:ke-decreased-cftr"
      name: "Decreased CFTR function"
      biological_action: decreased
      level_of_biological_organization: molecular
    study_subject:
      subject_type: CellularSystem
      id: "soma:culture-006"
      name: "Primary HBE ALI culture"
      cell_type:
        id: "CL:0002328"
        name: "bronchial epithelial cell"
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
- Rich CFTR measurement outputs: `cftr_chloride_secretion`, `cftr_forskolin_response`, `inhibitor_sensitive_current`, `sweat_chloride_concentration`, `nasal_potential_difference`

**See [`Container-cftr.yaml`](examples/Container-cftr.yaml) for the full data file.**

---

### EGFR Signaling Assay

Measuring EGFR phosphorylation after smoke exposure:

```yaml
egfr_signaling_assays:
  - id: "EGFR:001"
    name: "EGFR phosphorylation after smoke exposure"
    has_specified_output:
      id: "EGFR:001-output"
      name: "EGFR:001 measurement results"
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
      egfr_phosphorylation_y1173:
        value: "2.1"
        unit:
          id: "UO:0000193"
          name: "fold change"
      downstream_kinase_activation: "ERK1/2 and AKT activated"
      erk_phosphorylation:
        value: "2.8"
        unit:
          id: "UO:0000193"
          name: "fold change"
      akt_phosphorylation:
        value: "1.5"
        unit:
          id: "UO:0000193"
          name: "fold change"
      egfr_ligand_expression:
        value: "1.9"
        unit:
          id: "UO:0000193"
          name: "fold change"
      egfr_membrane_localization:
        value: "78"
        unit:
          id: "UO:0000187"
          name: "percent"
    normalization_reference: "beta-actin"
    assay_date: "2024-05-08"
    informs_on_key_event:
      id: "KE:ke1-egfr-activation"
      name: "EGFR activation"
      biological_action: activated
      level_of_biological_organization: molecular
    has_exposure_condition:
      - id: "EXPOSURE:cse-4h"
        name: "Cigarette smoke extract 5% for 4 hours"
        exposure_agent:
          id: "CHEBI:39188"
          name: "cigarette smoke extract"
        exposure_concentration:
          value: "5"
          unit:
            id: "UO:0000187"
            name: "percent"
        exposure_duration:
          value: "4"
          unit:
            id: "UO:0000032"
            name: "hour"
    study_subject:
      subject_type: CellularSystem
      id: "soma:culture-005"
      name: "Primary HBE ALI culture"
      cell_type:
        id: "CL:0002328"
        name: "bronchial epithelial cell"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    follows_protocols:
      - protocol_type: MolecularAssayProtocol
        id: "PROTOCOL:wb-001"
        name: "Western blot for phospho-EGFR"
        detection_method: "chemiluminescence"
        antibodies_used:
          - "anti-pEGFR Y1068 (Cell Signaling #3777)"
          - "anti-total EGFR (Cell Signaling #4267)"
        normalization_method: "total protein normalization"
```

**See [`Container-egfr.yaml`](examples/Container-egfr.yaml) for the full data file.**

---

### Goblet Cell Assay

Measuring MUC5AC expression and goblet cell quantification:

```yaml
goblet_cell_assays:
  - id: "GCM:001"
    name: "MUC5AC expression and goblet cell quantification"
    has_specified_output:
      id: "GCM:001-output"
      name: "GCM:001 measurement results"
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
      goblet_cell_count:
        value: "85"
        unit:
          id: "UO:0000189"
          name: "count"
      muc5ac_protein_expression:
        value: "3.2"
        unit:
          id: "UO:0000193"
          name: "fold change"
      muc5b_mrna_expression:
        value: "1.8"
        unit:
          id: "UO:0000193"
          name: "fold change"
      muc5b_protein_expression:
        value: "1.5"
        unit:
          id: "UO:0000193"
          name: "fold change"
      muc5ac_muc5b_ratio:
        value: "2.7"
        unit:
          id: "UO:0000190"
          name: "ratio"
      mucin_secretion_rate:
        value: "12.5"
        unit:
          id: "UO:0000298"
          name: "microgram per hour"
      percent_solids:
        value: "4.2"
        unit:
          id: "UO:0000187"
          name: "percent"
      goblet_to_ciliated_ratio:
        value: "0.45"
        unit:
          id: "UO:0000190"
          name: "ratio"
    assay_date: "2024-06-15"
    informs_on_key_event:
      id: "KE:ke2-goblet-hyperplasia"
      name: "Goblet cell hyperplasia"
      biological_action: increased
      level_of_biological_organization: cellular
    study_subject:
      subject_type: CellularSystem
      id: "soma:culture-004"
      name: "Primary HBE ALI culture"
      cell_type:
        id: "CL:0002328"
        name: "bronchial epithelial cell"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    follows_protocols:
      - protocol_type: StainingProtocol
        id: "PROTOCOL:stain-001"
        name: "AB-PAS staining for goblet cells"
        staining_type: "AB-PAS"
        fixation_method: "4% paraformaldehyde"
        counterstain: "hematoxylin"
```

**See [`Container-goblet_cell_mucin.yaml`](examples/Container-goblet_cell_mucin.yaml) for the full data file.**

---

### FoxJ Expression Assay

Measuring FoxJ1 transcription factor expression (master regulator of ciliogenesis).
This assay is **in vitro only** (`supported_contexts: in_vitro_only`).

```yaml
foxj_assays:
  - id: "FOXJ:001"
    name: "FoxJ1 mRNA expression"
    has_specified_output:
      id: "FOXJ:001-output"
      name: "FOXJ:001 measurement results"
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
      foxj1_protein_expression:
        value: "0.58"
        unit:
          id: "UO:0000193"
          name: "fold change"
      foxj1_nuclear_localization:
        value: "35"
        unit:
          id: "UO:0000187"
          name: "percent"
    assay_date: "2024-09-05"
    informs_on_key_event:
      id: "KE:ke-altered-ciliogenesis"
      name: "Altered ciliogenesis"
      biological_action: altered
      level_of_biological_organization: cellular
    study_subject:
      subject_type: CellularSystem
      id: "soma:culture-008"
      name: "Primary HBE ALI culture"
      cell_type:
        id: "CL:0002328"
        name: "bronchial epithelial cell"
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
      days_at_differentiation: 14
      donor_info: "Healthy donor, non-smoker"
      replicates_per_donor: 3
      substrate_type: transwell_insert
      passage_number: 2
    follows_protocols:
      - protocol_type: MolecularAssayProtocol
        id: "PROTOCOL:qpcr-001"
        name: "qRT-PCR for FoxJ1"
        detection_method: "SYBR Green qPCR"
        reference_gene: "GAPDH"
        primer_sequences:
          - "FOXJ1-F: 5'-CAGGCCCAGAACTTTCTCC-3'"
          - "FOXJ1-R: 5'-GGCCTTTGGTACTGTCTCAC-3'"
```

**See [`Container-foxj.yaml`](examples/Container-foxj.yaml) for the full data file.**

---

### Gene Expression Assay

Measuring target gene mRNA expression.
This assay is **in vitro only** (`supported_contexts: in_vitro_only`).

```yaml
gene_expression_assays:
  - id: "GE:001"
    name: "IL-8 gene expression after exposure"
    target_gene: "PR:000006689"
    has_specified_output:
      id: "GE:001-output"
      name: "GE:001 measurement results"
      mrna_level:
        value: "3.5"
        unit:
          id: "UO:0000193"
          name: "fold change"
      protein_level:
        value: "2.1"
        unit:
          id: "UO:0000193"
          name: "fold change"
      percentage_positive_cells:
        value: "45"
        unit:
          id: "UO:0000187"
          name: "percent"
    gene_expression_method: "qRT-PCR"
    normalization_reference: "GAPDH"
    assay_date: "2024-10-01"
    has_exposure_condition:
      - id: "EXPOSURE:lps-100ng-6h"
        name: "LPS 100 ng/mL for 6 hours"
        exposure_agent:
          id: "CHEBI:16412"
          name: "lipopolysaccharide"
        exposure_concentration:
          value: "100"
          unit:
            id: "UO:0000275"
            name: "nanogram per milliliter"
        exposure_duration:
          value: "6"
          unit:
            id: "UO:0000032"
            name: "hour"
    study_subject:
      subject_type: CellularSystem
      id: "soma:culture-009"
      name: "Primary HBE ALI culture"
      cell_type:
        id: "CL:0002328"
        name: "bronchial epithelial cell"
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
      donor_info: "Healthy donor, non-smoker, age 40"
      replicates_per_donor: 3
      substrate_type: transwell_insert
      passage_number: 2
    follows_protocols:
      - protocol_type: MolecularAssayProtocol
        id: "PROTOCOL:qpcr-002"
        name: "qRT-PCR for cytokine expression"
        detection_method: "TaqMan qPCR"
        reference_gene: "GAPDH"
        platform: "QuantStudio 6"
```

**Key points:**

- `target_gene` is an assay-level slot (not inside `has_specified_output`)
- Output includes `mrna_level`, `protein_level`, and `percentage_positive_cells`
- `has_exposure_condition` captures LPS exposure details

**See [`Container-gene_expression.yaml`](examples/Container-gene_expression.yaml) for the full data file.**

---

## In Vivo Assays

These examples demonstrate assays from human or animal subjects. The `study_subject`
slot uses InVivoSubject-level properties including `age`, `sex`, `sample_type`,
`collection_site`, and `subject_characteristics`.

### Lung Function Assay

Spirometry measurement from a human subject.
This assay is **in vivo only** (`supported_contexts: in_vivo_only`).

```yaml
lung_function_assays:
  - id: "LF:001"
    name: "FEV1 measurement"
    has_specified_output:
      id: "LF:001-output"
      name: "LF:001 measurement results"
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
      fev1_fvc_ratio:
        value: "86.8"
        unit:
          id: "UO:0000187"
          name: "percent"
      feno:
        value: "22"
        unit:
          id: "UO:0000170"
          name: "parts per billion"
      bronchodilator_response:
        value: "8.5"
        unit:
          id: "UO:0000187"
          name: "percent"
      dlco:
        value: "88"
        unit:
          id: "UO:0000187"
          name: "percent predicted"
      peak_expiratory_flow:
        value: "92"
        unit:
          id: "UO:0000187"
          name: "percent predicted"
    reference_dataset: "GLI-2012"
    assay_date: "2024-08-10"
    informs_on_key_event:
      id: "KE:ao-decreased-lung-function"
      name: "Decreased lung function"
      biological_action: decreased
      level_of_biological_organization: organ
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
      clinical_context: "Baseline spirometry, pre-bronchodilator"
    follows_protocols:
      - protocol_type: SpirometryProtocol
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

- `informs_on_key_event` links to AOP Adverse Outcome: "Decreased lung function"
- `study_subject` includes InVivoSubject slots: `age`, `sex`, `subject_characteristics`, `clinical_context`
- Rich lung function outputs: `fev1`, `fvc`, `fev1_fvc_ratio`, `feno`, `bronchodilator_response`, `dlco`, `peak_expiratory_flow`
- `follows_protocols` references a SpirometryProtocol with `protocol_type` designator for polymorphic dispatch

**See [`Container-lung_function.yaml`](examples/Container-lung_function.yaml) for the full data file.**

---

### BALF/Sputum Assay

Inflammatory cell differential from induced sputum.
This assay is **in vivo only** (`supported_contexts: in_vivo_only`).

```yaml
balf_sputum_assays:
  - id: "BALF:001"
    name: "Neutrophil percentage in induced sputum"
    has_specified_output:
      id: "BALF:001-output"
      name: "BALF:001 measurement results"
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
      eosinophil_percentage:
        value: "3.5"
        unit:
          id: "UO:0000187"
          name: "percent"
      macrophage_percentage:
        value: "38.0"
        unit:
          id: "UO:0000187"
          name: "percent"
      lymphocyte_percentage:
        value: "12.5"
        unit:
          id: "UO:0000187"
          name: "percent"
      total_cell_count:
        value: "2500000"
        unit:
          id: "UO:0000209"
          name: "cells per milliliter"
      il6_concentration:
        value: "85"
        unit:
          id: "UO:0000175"
          name: "picogram per milliliter"
      tnf_alpha_concentration:
        value: "120"
        unit:
          id: "UO:0000175"
          name: "picogram per milliliter"
      total_protein_concentration:
        value: "1.2"
        unit:
          id: "UO:0000176"
          name: "milligram per milliliter"
    assay_date: "2024-07-22"
    informs_on_key_event:
      id: "KE:ke-airway-inflammation"
      name: "Airway inflammation"
      biological_action: increased
      level_of_biological_organization: tissue
    target_cell_type:
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
      sample_collection_method: "Induced sputum with hypertonic saline nebulization"
      clinical_context: "Routine monitoring, stable asthma"
    follows_protocols:
      - protocol_type: MolecularAssayProtocol
        id: "PROTOCOL:balf-001"
        name: "Sputum cell differential protocol"
        detection_method: "cytospin and Diff-Quik staining"
```

**Key points:**

- Uses `target_cell_type` (not `cell_type`) to indicate the cell population being analyzed (neutrophils)
- Rich inflammatory panel: `neutrophil_percentage`, `eosinophil_percentage`, `macrophage_percentage`, `lymphocyte_percentage`, `total_cell_count`
- Cytokine measurements: `il8_concentration`, `il6_concentration`, `tnf_alpha_concentration`
- InVivoSubject with `sample_type`, `collection_site`, `sample_collection_method`, `clinical_context`

**See [`Container-balf_sputum.yaml`](examples/Container-balf_sputum.yaml) for the full data file.**

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
    quality_control_criteria: "Minimum 5 fields per insert, discard if >50% debris"
    replicate_requirements: 3
    sub_protocols:
      - id: "PROTOCOL:001a"
        name: "Sample preparation for CBF imaging"
        description: "Pre-imaging wash and equilibration steps"
        protocol_version: "1.0"
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

**See [`Container-protocol.yaml`](examples/Container-protocol.yaml) for the full data file.**

---

### Protocols on Assays via `follows_protocols`

Assays reference protocols via the `follows_protocols` slot, which is multivalued.
The `protocol_type` field designates which concrete Protocol subclass is being used,
enabling polymorphic dispatch:

```yaml
# ImagingProtocol on a CiliaryFunctionAssay
ciliary_function_assays:
  - id: "CILIARY:001"
    name: "CBF measurement"
    has_specified_output:
      id: "CILIARY:001-output"
      name: "CILIARY:001 measurement results"
      beat_frequency_hz:
        value: "12.5"
        unit:
          id: "UO:0000106"
          name: "hertz"
    assay_date: "2024-01-15"
    study_subject:
      subject_type: CellularSystem
      id: "soma:culture-001"
      name: "Primary HBE ALI culture"
      cell_type:
        id: "CL:0002328"
        name: "bronchial epithelial cell"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    follows_protocols:
      - protocol_type: ImagingProtocol
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

**See [`Container-comprehensive_aop_lung.yaml`](examples/Container-comprehensive_aop_lung.yaml) for the full data file.**

Key features demonstrated in the comprehensive example:

- **AOP linkage**: Each assay uses `informs_on_key_event` to connect to the biological pathway
- **Output classes**: Measurements wrapped in `has_specified_output` using domain-specific output classes (e.g., `OxidativeStressOutput`, `CiliaryFunctionOutput`, `LungFunctionOutput`)
- **Named measurement slots**: `reactive_oxygen_species`, `egfr_phosphorylation_y1068`, `beat_frequency_hz`, `fev1` inside their output classes
- **Protocols via `follows_protocols`** with `protocol_type` designator: ImagingProtocol, MolecularAssayProtocol, StainingProtocol, SpirometryProtocol
- **In vitro study subjects**: `cell_type` on the StudySubject (CellularSystem) for cell culture assays
- **In vivo study subjects**: InVivoSubject with `age`, `sex`, `subject_characteristics` for clinical assays
- **Exposure conditions**: `has_exposure_condition` with agent, concentration, duration, and `timing_post_exposure`
- **Co-exposures**: Multivalued `has_exposure_condition` for PM2.5 + ozone co-exposure
- **Time-course data**: Multiple timepoints per assay type showing dose-response

---

## Next Steps

- Browse the complete [Schema Documentation](elements/index.md) for all available classes and slots
- Read [About](about.md) to learn more about the project goals
- Visit the [GitHub Repository](https://github.com/EHS-Data-Standards/soma) to contribute
