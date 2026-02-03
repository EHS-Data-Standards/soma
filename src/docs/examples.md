# Examples

This page provides comprehensive examples of using the Outcomes Working Group Data Model.
All examples use the `Container` class as the root element and demonstrate real-world
use cases for environmental health research data.

## Quick Start

The simplest way to get started is to pick an example that matches your measurement type
and adapt it to your data. Each example shows:

- Required fields for the measurement type
- Proper use of ontology-backed units
- Context for in vitro (cell culture) or in vivo (human/animal) settings

---

## In Vitro Measurements

These examples demonstrate measurements performed on cell culture systems, using the
`InVitroContext` mixin which provides the `cell_culture_system` slot for detailed
culture system specification.

### Ciliary Function Measurement

Measuring ciliary beat frequency (CBF) in primary human bronchial epithelial cells
cultured at air-liquid interface:

```yaml
ciliary_measurements:
  - id: "CILIARY:001"
    name: "CBF measurement after ozone exposure"
    observation_type: ciliary_beat_frequency
    quantity_measured:
      value: "8.5"
      unit:
        id: "UO:0000106"
        name: "hertz"
    measurement_date: "2024-01-15"
    cell_culture_system:
      id: "owg:culture-001"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21
```

**Key points:**

- `observation_type` uses the `CiliaryObservationTypeEnum` (e.g., `ciliary_beat_frequency`, `ciliary_beat_pattern`, `percent_motile_cilia`)
- `cell_culture_system` is a structured object with culture details
- `days_at_differentiation` indicates maturation time at ALI

---

### Airway Surface Liquid (ASL) Measurement

Measuring ASL height using micro-optical coherence tomography:

```yaml
asl_measurements:
  - id: "ASL:001"
    name: "Airway surface liquid height"
    observation_type: asl_height
    quantity_measured:
      value: "7.2"
      unit:
        id: "UO:0000017"
        name: "micrometer"
    measurement_date: "2024-02-10"
    cell_culture_system:
      id: "owg:culture-002"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 28
```

---

### Mucociliary Clearance (MCC) Measurement

Tracking fluorescent microsphere transport rate:

```yaml
mcc_measurements:
  - id: "MCC:001"
    name: "Mucociliary transport rate"
    observation_type: mucociliary_transport_rate
    quantity_measured:
      value: "45.3"
      unit:
        id: "UO:0000103"
        name: "micrometer per second"
    measurement_date: "2024-03-05"
    cell_culture_system:
      id: "owg:culture-007"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21
```

---

### Oxidative Stress Measurement

Measuring reactive oxygen species (ROS) after PM2.5 exposure:

```yaml
oxidative_stress_measurements:
  - id: "OX:001"
    name: "ROS level after PM2.5 exposure"
    observation_type: reactive_oxygen_species
    quantity_measured:
      value: "2.5"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_date: "2024-01-20"
    cell_culture_system:
      id: "owg:culture-003"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21
```

---

### CFTR Function Measurement

Measuring CFTR-mediated chloride secretion using Ussing chambers:

```yaml
cftr_measurements:
  - id: "CFTR:001"
    name: "CFTR chloride secretion"
    observation_type: cftr_chloride_secretion
    quantity_measured:
      value: "15.2"
      unit:
        id: "UO:0000274"
        name: "microampere per square centimeter"
    measurement_date: "2024-04-12"
    cell_culture_system:
      id: "owg:culture-006"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 28
```

---

### EGFR Phosphorylation Measurement

Measuring EGFR phosphorylation after smoke exposure:

```yaml
egfr_phosphorylation_measurements:
  - id: "EGFR:001"
    name: "EGFR phosphorylation after smoke exposure"
    observation_type: egfr_phosphorylation
    quantity_measured:
      value: "3.2"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_date: "2024-05-08"
    cell_culture_system:
      id: "owg:culture-005"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21
```

---

### Goblet Cell / Mucin Measurement

Measuring MUC5AC expression in goblet cells:

```yaml
goblet_cell_mucin_measurements:
  - id: "GCM:001"
    name: "MUC5AC expression"
    observation_type: muc5ac_expression
    quantity_measured:
      value: "4.8"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_date: "2024-06-15"
    cell_culture_system:
      id: "owg:culture-004"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 28
```

---

### FoxJ Measurement

Measuring FoxJ1 transcription factor expression (master regulator of ciliogenesis):

```yaml
foxj_measurements:
  - id: "FOXJ:001"
    name: "FoxJ1 mRNA expression"
    observation_type: foxj1_mrna_expression
    quantity_measured:
      value: "0.65"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_date: "2024-09-05"
    cell_culture_system:
      id: "owg:culture-008"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 14
```

---

## In Vivo Measurements

These examples demonstrate measurements from human or animal subjects, using the
`InVivoContext` mixin which provides participant and sample information.

### Lung Function Measurement

Spirometry measurement from a human subject:

```yaml
lung_function_measurements:
  - id: "LF:001"
    name: "FEV1 measurement"
    observation_type: fev1
    quantity_measured:
      value: "82.5"
      unit:
        id: "UO:0000187"
        name: "percent predicted"
    measurement_date: "2024-08-10"
    participant:
      id: "PARTICIPANT:002"
      name: "Subject B"
```

**Key points:**

- `participant` replaces `cell_culture_system` for in vivo context
- No `days_at_differentiation` since this is a human measurement

---

### BALF/Sputum Measurement

Inflammatory cell differential from induced sputum:

```yaml
balf_sputum_measurements:
  - id: "BALF:001"
    name: "Neutrophil percentage in induced sputum"
    observation_type: neutrophil_percentage
    quantity_measured:
      value: "45.0"
      unit:
        id: "UO:0000187"
        name: "percent"
    measurement_date: "2024-07-22"
    sample_type: sputum
    participant:
      id: "PARTICIPANT:001"
      name: "Subject A"
```

---

## Protocols, Methods, and Assays

The schema supports detailed documentation of experimental procedures through a
three-level hierarchy: Assays (what is measured), Methods (how it's measured),
and Protocols (specific procedures).

### Assay Definition

An assay type reference:

```yaml
assays:
  - id: "ASSAY:001"
    name: "Ciliary beat frequency assay"
    description: "Assay for measuring the frequency of ciliary beating in airway epithelial cells"
```

---

### Method Definition

A general measurement method that implements an assay:

```yaml
methods:
  - id: "METHOD:001"
    name: "High-speed video microscopy"
    description: "Video microscopy technique for measuring ciliary dynamics at frame rates above 100 Hz"
    implements_assay:
      id: "ASSAY:001"
      name: "Ciliary beat frequency assay"
```

---

### Protocol Definition

A detailed protocol that specifies a method:

```yaml
protocols:
  - id: "PROTOCOL:001"
    name: "High-speed video microscopy for CBF"
    description: "Protocol for measuring ciliary beat frequency using high-speed video microscopy"
    specified_by_method:
      id: "METHOD:001"
      name: "High-speed video microscopy"
```

---

### Linking Measurements to Protocols and Methods

Measurements can reference the protocol and method used:

```yaml
ciliary_measurements:
  - id: "CILIARY:001"
    name: "CBF - Control baseline"
    observation_type: ciliary_beat_frequency
    quantity_measured:
      value: "12.5"
      unit:
        id: "UO:0000106"
        name: "hertz"
    measurement_date: "2024-01-15"
    uses_method:
      id: "METHOD:001"
      name: "High-speed video microscopy"
    follows_protocol:
      id: "PROTOCOL:001"
      name: "CBF measurement by high-speed microscopy"
    cell_culture_system:
      id: "owg:culture-001"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21
```

---

## Comprehensive AOP Example: PM2.5 Exposure → Impaired Lung Function

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
- Exposure: PM2.5 (10 μg/cm²) vs. clean air control
- Timepoints: 4h (early), 24h (intermediate), 7d (late)

```yaml
# =============================================================================
# ASSAYS - The tests being performed
# =============================================================================

assays:
  - id: "ASSAY:001"
    name: "Reactive oxygen species assay"
    description: "Assay for measuring intracellular ROS levels using fluorescent probes"

  - id: "ASSAY:002"
    name: "Protein phosphorylation assay"
    description: "Assay for detecting phosphorylation of target proteins"

  - id: "ASSAY:003"
    name: "Gene expression assay"
    description: "Assay for measuring mRNA expression levels"

  - id: "ASSAY:004"
    name: "Ciliary beat frequency assay"
    description: "Assay for measuring the frequency of ciliary beating in airway epithelial cells"

  - id: "ASSAY:005"
    name: "Mucociliary transport assay"
    description: "Assay for measuring the rate and efficiency of mucus/particle transport"

  - id: "ASSAY:006"
    name: "Pulmonary function test"
    description: "Clinical assay for measuring lung volumes and airflow"

# =============================================================================
# METHODS - General techniques implementing the assays
# =============================================================================

methods:
  - id: "METHOD:001"
    name: "DCFDA fluorescence assay"
    description: "Measurement of intracellular ROS using 2',7'-dichlorofluorescein diacetate (DCFDA) probe with plate reader detection"
    implements_assay:
      id: "ASSAY:001"
      name: "Reactive oxygen species assay"

  - id: "METHOD:002"
    name: "Western blot"
    description: "Protein detection and semi-quantification by SDS-PAGE and immunoblotting"
    implements_assay:
      id: "ASSAY:002"
      name: "Protein phosphorylation assay"

  - id: "METHOD:003"
    name: "Quantitative RT-PCR"
    description: "Reverse transcription followed by quantitative PCR for mRNA quantification"
    implements_assay:
      id: "ASSAY:003"
      name: "Gene expression assay"

  - id: "METHOD:004"
    name: "High-speed video microscopy"
    description: "Video microscopy at frame rates >100 Hz for ciliary motion analysis"
    implements_assay:
      id: "ASSAY:004"
      name: "Ciliary beat frequency assay"

  - id: "METHOD:005"
    name: "Fluorescent microsphere tracking"
    description: "Tracking fluorescent particles to measure mucociliary transport rate"
    implements_assay:
      id: "ASSAY:005"
      name: "Mucociliary transport assay"

  - id: "METHOD:006"
    name: "Spirometry"
    description: "Standardized spirometry following ATS/ERS guidelines"
    implements_assay:
      id: "ASSAY:006"
      name: "Pulmonary function test"

# =============================================================================
# PROTOCOLS - Detailed procedures for each method
# =============================================================================

protocols:
  - id: "PROTOCOL:001"
    name: "DCFDA ROS detection in ALI cultures"
    description: "Protocol for measuring intracellular ROS in differentiated HBE cells using DCFDA"
    specified_by_method:
      id: "METHOD:001"
      name: "DCFDA fluorescence assay"

  - id: "PROTOCOL:002"
    name: "Western blot for phospho-EGFR"
    description: "Protocol for detecting EGFR phosphorylation at Y1068 by Western blot"
    specified_by_method:
      id: "METHOD:002"
      name: "Western blot"

  - id: "PROTOCOL:003"
    name: "qRT-PCR for MUC5AC"
    description: "Protocol for measuring MUC5AC mRNA expression by qRT-PCR with GAPDH normalization"
    specified_by_method:
      id: "METHOD:003"
      name: "Quantitative RT-PCR"

  - id: "PROTOCOL:004"
    name: "CBF measurement by high-speed microscopy"
    description: "Protocol for measuring ciliary beat frequency using high-speed video microscopy at 200 fps"
    specified_by_method:
      id: "METHOD:004"
      name: "High-speed video microscopy"

  - id: "PROTOCOL:005"
    name: "MCT rate by microsphere tracking"
    description: "Protocol for measuring mucociliary transport rate using 1-μm fluorescent microspheres"
    specified_by_method:
      id: "METHOD:005"
      name: "Fluorescent microsphere tracking"

  - id: "PROTOCOL:006"
    name: "Pre- and post-bronchodilator spirometry"
    description: "Clinical spirometry protocol following ATS/ERS 2019 guidelines with bronchodilator reversibility testing"
    specified_by_method:
      id: "METHOD:006"
      name: "Spirometry"

# =============================================================================
# OXIDATIVE STRESS MEASUREMENTS (MIE)
# =============================================================================

oxidative_stress_measurements:
  # Control - 4h
  - id: "OX:001"
    name: "ROS level - Control 4h"
    description: "Intracellular ROS in control HBE cells at 4 hours"
    observation_type: reactive_oxygen_species
    quantity_measured:
      value: "1.0"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_date: "2024-01-15"
    uses_method:
      id: "METHOD:001"
      name: "DCFDA fluorescence assay"
    follows_protocol:
      id: "PROTOCOL:001"
      name: "DCFDA ROS detection in ALI cultures"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
      cell_type:
        id: "CL:0002328"
        name: "bronchial epithelial cell"
      anatomical_origin:
        id: "UBERON:0002031"
        name: "bronchus"
      model_species:
        id: "NCBITaxon:9606"
        name: "Homo sapiens"
    days_at_differentiation: 21
    donor_info: "Healthy non-smoker, 35y female"
    replicates_per_donor: 3

  # PM2.5 exposed - 4h
  - id: "OX:002"
    name: "ROS level - PM2.5 4h"
    description: "Intracellular ROS in PM2.5-exposed HBE cells at 4 hours"
    observation_type: reactive_oxygen_species
    quantity_measured:
      value: "2.8"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_date: "2024-01-15"
    uses_method:
      id: "METHOD:001"
      name: "DCFDA fluorescence assay"
    follows_protocol:
      id: "PROTOCOL:001"
      name: "DCFDA ROS detection in ALI cultures"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21
    donor_info: "Healthy non-smoker, 35y female"
    replicates_per_donor: 3

  # Lipid peroxidation marker - PM2.5 24h
  - id: "OX:003"
    name: "MDA level - PM2.5 24h"
    description: "Malondialdehyde (lipid peroxidation marker) after PM2.5 exposure"
    observation_type: malondialdehyde
    quantity_measured:
      value: "1.9"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_date: "2024-01-16"
    uses_method:
      id: "METHOD:001"
      name: "DCFDA fluorescence assay"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21

# =============================================================================
# EGFR PHOSPHORYLATION MEASUREMENTS (KE1)
# =============================================================================

egfr_phosphorylation_measurements:
  # Control - 4h
  - id: "EGFR:001"
    name: "pEGFR Y1068 - Control 4h"
    description: "EGFR phosphorylation at Y1068 in control cells at 4 hours"
    observation_type: egfr_phosphorylation
    phosphorylation_site: "Y1068"
    quantity_measured:
      value: "1.0"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_date: "2024-01-15"
    uses_method:
      id: "METHOD:002"
      name: "Western blot"
    follows_protocol:
      id: "PROTOCOL:002"
      name: "Western blot for phospho-EGFR"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21

  # PM2.5 exposed - 4h
  - id: "EGFR:002"
    name: "pEGFR Y1068 - PM2.5 4h"
    description: "EGFR phosphorylation at Y1068 after PM2.5 exposure at 4 hours"
    observation_type: egfr_phosphorylation
    phosphorylation_site: "Y1068"
    quantity_measured:
      value: "3.5"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_date: "2024-01-15"
    uses_method:
      id: "METHOD:002"
      name: "Western blot"
    follows_protocol:
      id: "PROTOCOL:002"
      name: "Western blot for phospho-EGFR"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21

  # Total EGFR protein (normalization control)
  - id: "EGFR:003"
    name: "Total EGFR - PM2.5 4h"
    description: "Total EGFR protein expression (loading control)"
    observation_type: egfr_total_protein
    quantity_measured:
      value: "1.05"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_date: "2024-01-15"
    uses_method:
      id: "METHOD:002"
      name: "Western blot"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21

# =============================================================================
# GOBLET CELL / MUCIN MEASUREMENTS (KE2)
# =============================================================================

goblet_cell_mucin_measurements:
  # MUC5AC mRNA - Control 24h
  - id: "GCM:001"
    name: "MUC5AC mRNA - Control 24h"
    description: "MUC5AC mRNA expression in control cells at 24 hours"
    observation_type: muc5ac_expression
    quantity_measured:
      value: "1.0"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_date: "2024-01-16"
    uses_method:
      id: "METHOD:003"
      name: "Quantitative RT-PCR"
    follows_protocol:
      id: "PROTOCOL:003"
      name: "qRT-PCR for MUC5AC"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21

  # MUC5AC mRNA - PM2.5 24h
  - id: "GCM:002"
    name: "MUC5AC mRNA - PM2.5 24h"
    description: "MUC5AC mRNA expression after PM2.5 exposure at 24 hours"
    observation_type: muc5ac_expression
    quantity_measured:
      value: "4.2"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_date: "2024-01-16"
    uses_method:
      id: "METHOD:003"
      name: "Quantitative RT-PCR"
    follows_protocol:
      id: "PROTOCOL:003"
      name: "qRT-PCR for MUC5AC"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21

  # Goblet cell percentage - PM2.5 7d
  - id: "GCM:003"
    name: "Goblet cell percentage - PM2.5 7d"
    description: "Percentage of goblet cells after 7-day PM2.5 exposure"
    observation_type: goblet_cell_count
    quantity_measured:
      value: "32"
      unit:
        id: "UO:0000187"
        name: "percent"
    range_low:
      value: "10"
      unit:
        id: "UO:0000187"
        name: "percent"
    range_high:
      value: "20"
      unit:
        id: "UO:0000187"
        name: "percent"
    measurement_date: "2024-01-22"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 28

  # Mucus viscosity - PM2.5 7d
  - id: "GCM:004"
    name: "Mucus viscosity - PM2.5 7d"
    description: "Mucus viscosity after 7-day PM2.5 exposure showing hypersecretion phenotype"
    observation_type: mucus_viscosity
    quantity_measured:
      value: "185"
      unit:
        id: "UO:0000019"
        name: "centipoise"
    measurement_date: "2024-01-22"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 28

# =============================================================================
# CILIARY FUNCTION MEASUREMENTS (KE3 - part 1)
# =============================================================================

ciliary_measurements:
  # CBF - Control baseline
  - id: "CILIARY:001"
    name: "CBF - Control baseline"
    description: "Ciliary beat frequency in control HBE cells at baseline"
    observation_type: ciliary_beat_frequency
    quantity_measured:
      value: "12.5"
      unit:
        id: "UO:0000106"
        name: "hertz"
    range_low:
      value: "10"
      unit:
        id: "UO:0000106"
        name: "hertz"
    range_high:
      value: "15"
      unit:
        id: "UO:0000106"
        name: "hertz"
    measurement_date: "2024-01-15"
    uses_method:
      id: "METHOD:004"
      name: "High-speed video microscopy"
    follows_protocol:
      id: "PROTOCOL:004"
      name: "CBF measurement by high-speed microscopy"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21

  # CBF - PM2.5 24h
  - id: "CILIARY:002"
    name: "CBF - PM2.5 24h"
    description: "Ciliary beat frequency after PM2.5 exposure at 24 hours"
    observation_type: ciliary_beat_frequency
    quantity_measured:
      value: "9.8"
      unit:
        id: "UO:0000106"
        name: "hertz"
    measurement_date: "2024-01-16"
    uses_method:
      id: "METHOD:004"
      name: "High-speed video microscopy"
    follows_protocol:
      id: "PROTOCOL:004"
      name: "CBF measurement by high-speed microscopy"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21

  # CBF - PM2.5 7d
  - id: "CILIARY:003"
    name: "CBF - PM2.5 7d"
    description: "Ciliary beat frequency after 7-day PM2.5 exposure showing sustained impairment"
    observation_type: ciliary_beat_frequency
    quantity_measured:
      value: "7.2"
      unit:
        id: "UO:0000106"
        name: "hertz"
    measurement_date: "2024-01-22"
    uses_method:
      id: "METHOD:004"
      name: "High-speed video microscopy"
    follows_protocol:
      id: "PROTOCOL:004"
      name: "CBF measurement by high-speed microscopy"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 28

  # Ciliated cell percentage - PM2.5 7d
  - id: "CILIARY:004"
    name: "Ciliated cell percentage - PM2.5 7d"
    description: "Percentage of ciliated cells after 7-day PM2.5 exposure"
    observation_type: percentage_ciliated_cells
    quantity_measured:
      value: "45"
      unit:
        id: "UO:0000187"
        name: "percent"
    range_low:
      value: "60"
      unit:
        id: "UO:0000187"
        name: "percent"
    range_high:
      value: "80"
      unit:
        id: "UO:0000187"
        name: "percent"
    measurement_date: "2024-01-22"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 28

# =============================================================================
# MUCOCILIARY CLEARANCE MEASUREMENTS (KE3 - part 2)
# =============================================================================

mcc_measurements:
  # MCT rate - Control baseline
  - id: "MCC:001"
    name: "MCT rate - Control baseline"
    description: "Mucociliary transport rate in control HBE cells at baseline"
    observation_type: mucociliary_transport_rate
    quantity_measured:
      value: "52"
      unit:
        id: "UO:0000103"
        name: "micrometer per second"
    measurement_date: "2024-01-15"
    uses_method:
      id: "METHOD:005"
      name: "Fluorescent microsphere tracking"
    follows_protocol:
      id: "PROTOCOL:005"
      name: "MCT rate by microsphere tracking"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21

  # MCT rate - PM2.5 24h
  - id: "MCC:002"
    name: "MCT rate - PM2.5 24h"
    description: "Mucociliary transport rate after PM2.5 exposure at 24 hours"
    observation_type: mucociliary_transport_rate
    quantity_measured:
      value: "38"
      unit:
        id: "UO:0000103"
        name: "micrometer per second"
    measurement_date: "2024-01-16"
    uses_method:
      id: "METHOD:005"
      name: "Fluorescent microsphere tracking"
    follows_protocol:
      id: "PROTOCOL:005"
      name: "MCT rate by microsphere tracking"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21

  # MCT rate - PM2.5 7d (severely impaired)
  - id: "MCC:003"
    name: "MCT rate - PM2.5 7d"
    description: "Mucociliary transport rate after 7-day PM2.5 exposure showing severe impairment"
    observation_type: mucociliary_transport_rate
    quantity_measured:
      value: "18"
      unit:
        id: "UO:0000103"
        name: "micrometer per second"
    measurement_date: "2024-01-22"
    uses_method:
      id: "METHOD:005"
      name: "Fluorescent microsphere tracking"
    follows_protocol:
      id: "PROTOCOL:005"
      name: "MCT rate by microsphere tracking"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 28

  # Percentage active transport - PM2.5 7d
  - id: "MCC:004"
    name: "Active transport percentage - PM2.5 7d"
    description: "Percentage of surface with active mucociliary transport after 7-day PM2.5 exposure"
    observation_type: percentage_active_transport
    quantity_measured:
      value: "35"
      unit:
        id: "UO:0000187"
        name: "percent"
    measurement_date: "2024-01-22"
    cell_culture_system:
      id: "owg:culture-aop-001"
      name: "Primary HBE ALI culture - Donor 1"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 28

# =============================================================================
# LUNG FUNCTION MEASUREMENTS (Adverse Outcome - Clinical)
# =============================================================================

lung_function_measurements:
  # FEV1 - Subject 1 (PM2.5 exposed community)
  - id: "LF:001"
    name: "FEV1 - Subject 1 baseline"
    description: "FEV1 in subject from high PM2.5 exposure area at baseline"
    observation_type: fev1
    quantity_measured:
      value: "78"
      unit:
        id: "UO:0000187"
        name: "percent predicted"
    measurement_date: "2024-02-01"
    uses_method:
      id: "METHOD:006"
      name: "Spirometry"
    follows_protocol:
      id: "PROTOCOL:006"
      name: "Pre- and post-bronchodilator spirometry"
    participant:
      id: "PARTICIPANT:001"
      name: "Subject 1"
    sample_type: exhaled_breath_condensate
    collection_site: "pulmonary function laboratory"
    subject_characteristics: "52y male, non-smoker, high PM2.5 exposure area resident, 15 years"

  # FEV1 - Subject 1 follow-up
  - id: "LF:002"
    name: "FEV1 - Subject 1 1-year follow-up"
    description: "FEV1 decline after 1 year continued PM2.5 exposure"
    observation_type: fev1
    quantity_measured:
      value: "74"
      unit:
        id: "UO:0000187"
        name: "percent predicted"
    measurement_date: "2025-02-01"
    uses_method:
      id: "METHOD:006"
      name: "Spirometry"
    follows_protocol:
      id: "PROTOCOL:006"
      name: "Pre- and post-bronchodilator spirometry"
    participant:
      id: "PARTICIPANT:001"
      name: "Subject 1"
    sample_type: exhaled_breath_condensate
    subject_characteristics: "53y male, non-smoker, high PM2.5 exposure area resident, 16 years"

  # FEV1/FVC ratio - Subject 1
  - id: "LF:003"
    name: "FEV1/FVC ratio - Subject 1"
    description: "FEV1/FVC ratio indicating obstructive pattern"
    observation_type: fev1_fvc_ratio
    quantity_measured:
      value: "0.68"
      unit:
        id: "UO:0000196"
        name: "ratio"
    range_low:
      value: "0.70"
      unit:
        id: "UO:0000196"
        name: "ratio"
    measurement_date: "2025-02-01"
    uses_method:
      id: "METHOD:006"
      name: "Spirometry"
    participant:
      id: "PARTICIPANT:001"
      name: "Subject 1"

  # FEV1 decline rate - Subject 1
  - id: "LF:004"
    name: "FEV1 decline rate - Subject 1"
    description: "Rate of FEV1 decline over 1 year (accelerated compared to normal aging)"
    observation_type: lung_function_decline_rate
    quantity_measured:
      value: "65"
      unit:
        id: "UO:0000098"
        name: "milliliter per year"
    range_high:
      value: "30"
      unit:
        id: "UO:0000098"
        name: "milliliter per year"
    measurement_date: "2025-02-01"
    participant:
      id: "PARTICIPANT:001"
      name: "Subject 1"
    subject_characteristics: "Accelerated decline >2x normal (25-30 mL/year)"
```

---

## Next Steps

- Browse the complete [Schema Documentation](elements/index.md) for all available classes and slots
- Read [About](about.md) to learn more about the project goals
- Visit the [GitHub Repository](https://github.com/EHS-Data-Standards/outcomes-working-group) to contribute