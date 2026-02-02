# Example data for outcomes_working_group

This folder contains example data for testing and demonstrating the datamodel,
sorted in subfolders:

- `valid` - Data conforming to the datamodel. Used to verify the datamodel.
- `invalid` - Data not conforming to the datamodel. Used to verify validation.
- `problem` - Data which are not yet handled correctly in the current schema version,
   again separated into valid/invalid.
- `valid_bkup` - Backup of previous test data (pre-microschema refactor).

## Schema Structure

The schema uses a **microschema architecture** with domain-specific measurement types.
All data files use the `Container` class as the root element.

### Measurement Microschemas

| Microschema | Description | Container Slot |
|-------------|-------------|----------------|
| CiliaryFunctionMeasurement | Ciliary beat frequency, active area, morphology | `ciliary_measurements` |
| ASLMeasurement | Airway surface liquid height, PCL depth, ion composition | `asl_measurements` |
| MCCMeasurement | Mucociliary clearance and transport | `mcc_measurements` |
| OxidativeStressMeasurement | ROS, lipid peroxidation, antioxidant capacity | `oxidative_stress_measurements` |
| CFTRMeasurement | CFTR chloride secretion and function | `cftr_measurements` |
| EGFRMeasurement | EGFR signaling and phosphorylation | `egfr_measurements` |
| GobletCellMucinMeasurement | Goblet cells, MUC5AC/MUC5B expression | `goblet_cell_mucin_measurements` |
| BALFSputumMeasurement | BALF/sputum cell counts and cytokines | `balf_sputum_measurements` |
| LungFunctionMeasurement | FEV1, FVC, spirometry outcomes | `lung_function_measurements` |
| FoxJMeasurement | FoxJ1 expression and ciliogenesis | `foxj_measurements` |
| ExposureBiomarkerMeasurement | Cotinine, metals, PAH metabolites | `exposure_biomarker_measurements` |

### Supporting Entities

| Entity | Description | Container Slot |
|--------|-------------|----------------|
| Protocol | Detailed experimental procedures | `protocols` |
| Method | General measurement techniques | `methods` |
| Assay | Test/experiment definitions | `assays` |

## File Naming Convention

All example data files must conform to the scheme `Container-<descriptor>.yaml`
where `<descriptor>` is a descriptive name for the test case. The `Container` prefix
indicates the root class used for validation.
