-- # Class: Container Description: Root container for outcomes research data. Organized around ASSAYS that inform on Key Events in Adverse Outcome Pathways (AOPs).The schema is assay-centric: each assay class contains named slots for its specific measurements, with an explicit connection to the Key Event it informs via the informs_on_key_event slot.
--     * Slot: id
-- # Class: NamedThing Description: A generic entity with an identifier and name. Base class for all named entities in the schema.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
-- # Class: KeyEvent Description: A measurable change in biological state that is a step in an Adverse Outcome Pathway. Key Events represent the biological perturbations that assays measure to provide evidence for AOP-based mechanistic understanding. Key events can be Molecular Initiating Events (MIEs), intermediate Key Events, or Adverse Outcomes at the organism/population level.
--     * Slot: biological_process Description: The biological process affected by this key event. Should reference a GO biological process term.
--     * Slot: biological_object Description: The biological entity affected (protein, cell, tissue, organ).
--     * Slot: biological_action Description: The type of change (increased, decreased, altered, impaired).
--     * Slot: level_of_biological_organization Description: The level of biological organization at which this key event occurs.
--     * Slot: occurs_in_cell_type Description: The cell type in which this key event occurs. Should reference a Cell Ontology (CL) term.
--     * Slot: occurs_in_anatomy Description: The anatomical location where this key event occurs. Should reference a UBERON anatomy term.
--     * Slot: aopwiki_id Description: The AOP-Wiki identifier for this entity (e.g., "AOP:411" for an AOP, "KE:1234" for a key event).
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: KeyEvent_id Description: Autocreated FK slot
--     * Slot: AdverseOutcomePathway_id Description: Autocreated FK slot
--     * Slot: MolecularInitiatingEvent_id Description: Autocreated FK slot
-- # Class: KeyEventRelationship Description: A directional relationship between two key events in an AOP. Represents the causal linkage between an upstream event and a downstream event with supporting evidence.
--     * Slot: relationship_type Description: The type of causal relationship (directly leads to, indirectly leads to).
--     * Slot: evidence_support Description: Level of evidence supporting this key event relationship.
--     * Slot: quantitative_understanding Description: Level of quantitative understanding of the relationship.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: AdverseOutcomePathway_id Description: Autocreated FK slot
--     * Slot: upstream_event_id Description: The upstream key event in this relationship (cause).
--     * Slot: downstream_event_id Description: The downstream key event in this relationship (effect).
-- # Class: AdverseOutcome Description: An adverse health outcome at the organism or population level that represents the apical endpoint of an Adverse Outcome Pathway. This is the final, clinically or ecologically relevant effect.
--     * Slot: outcome_level Description: The level at which the adverse outcome manifests (individual, population).
--     * Slot: biological_process Description: The biological process affected by this key event. Should reference a GO biological process term.
--     * Slot: occurs_in_anatomy Description: The anatomical location where this key event occurs. Should reference a UBERON anatomy term.
--     * Slot: aopwiki_id Description: The AOP-Wiki identifier for this entity (e.g., "AOP:411" for an AOP, "KE:1234" for a key event).
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
-- # Class: AdverseOutcomePathway Description: A sequence of causally linked events at different levels of biological organization that lead from a molecular initiating event through intermediate key events to an adverse health outcome. AOPs provide a structured framework for organizing mechanistic evidence.
--     * Slot: aopwiki_id Description: The AOP-Wiki identifier for this entity (e.g., "AOP:411" for an AOP, "KE:1234" for a key event).
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: molecular_initiating_event_id Description: The molecular initiating event that starts this AOP.
--     * Slot: adverse_outcome_id Description: The adverse outcome that is the apical endpoint of this AOP.
-- # Class: MolecularInitiatingEvent Description: The initial molecular-level perturbation that starts an Adverse Outcome Pathway. The MIE is the direct interaction between a stressor and a biological target (e.g., receptor binding, enzyme inhibition).
--     * Slot: target_molecule Description: The molecular target of the stressor in the MIE (e.g., receptor, enzyme).
--     * Slot: biological_process Description: The biological process affected by this key event. Should reference a GO biological process term.
--     * Slot: biological_object Description: The biological entity affected (protein, cell, tissue, organ).
--     * Slot: biological_action Description: The type of change (increased, decreased, altered, impaired).
--     * Slot: level_of_biological_organization Description: The level of biological organization at which this key event occurs.
--     * Slot: occurs_in_cell_type Description: The cell type in which this key event occurs. Should reference a Cell Ontology (CL) term.
--     * Slot: occurs_in_anatomy Description: The anatomical location where this key event occurs. Should reference a UBERON anatomy term.
--     * Slot: aopwiki_id Description: The AOP-Wiki identifier for this entity (e.g., "AOP:411" for an AOP, "KE:1234" for a key event).
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
-- # Abstract Class: Assay Description: A planned process with the objective to produce information about biological state relevant to a Key Event in an Adverse Outcome Pathway. Assays are organized by the functional domain they assess (e.g., ciliary function, oxidative stress), and each domain-specific assay class contains named slots for the specific measurements it can produce. Assays inform on key events and contain the measurement data as named slots.
--     * Slot: assay_date Description: Date when the assay was performed.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: informs_on_key_event_id Description: The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.
--     * Slot: study_subject_id Description: The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.
--     * Slot: has_specified_output_id Description: The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).
-- # Abstract Class: AssayOutputMeasurement Description: The measurement results produced by an assay. The specified output of a planned process. Each domain-specific assay class has a corresponding AssayOutputMeasurement subclass containing the named measurement slots for that assay type. This class represents the "output" in the Input/Process/Output model: what was measured and what values were obtained.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
-- # Class: StudySubject Description: The subject of a study — what the assay is performed on. Subclasses capture different experimental contexts (model systems, living subjects, populations) with context-appropriate slots. The type of subject determines which slots are available, replacing the old mixin pattern.
--     * Slot: subject_type Description: The specific type of study subject. Used to designate which concrete class (e.g., CellularSystem, InVivoSubject) is instantiated for polymorphic study_subject slots.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: model_species_id Description: The species of origin for the cells or organism being studied. Reference to NCBITaxon term.
-- # Class: ModelSystem Description: An in vitro or ex vivo model system used to study biological processes. Parent class for cell-based and other model systems.
--     * Slot: subject_type Description: The specific type of study subject. Used to designate which concrete class (e.g., CellularSystem, InVivoSubject) is instantiated for polymorphic study_subject slots.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: model_species_id Description: The species of origin for the cells or organism being studied. Reference to NCBITaxon term.
-- # Class: InVivoSubject Description: A living human or animal subject from whom measurements are taken. Used for clinical assays (lung function, BALF/sputum) and any assay performed on living subjects.
--     * Slot: sex Description: Biological sex of the subject.
--     * Slot: subject_characteristics Description: Relevant subject characteristics (disease state, medications, etc.). TIER 1 for LungFunctionAssay per user feedback.
--     * Slot: disease_state
--     * Slot: sample_type Description: Type of biological sample (e.g., sputum, BALF, blood).
--     * Slot: collection_site Description: Anatomical site of sample collection.
--     * Slot: collection_date Description: Date when the sample was collected.
--     * Slot: sample_collection_method Description: Method used for sample collection in vivo (e.g., bronchoscopy, induced sputum, spirometry).
--     * Slot: clinical_context Description: Clinical context for in vivo measurements (e.g., routine screening, post-exposure assessment, disease monitoring, baseline spirometry).
--     * Slot: subject_type Description: The specific type of study subject. Used to designate which concrete class (e.g., CellularSystem, InVivoSubject) is instantiated for polymorphic study_subject slots.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: PopulationSubject_id Description: Autocreated FK slot
--     * Slot: age_id Description: Age of the subject.
--     * Slot: model_species_id Description: The species of origin for the cells or organism being studied. Reference to NCBITaxon term.
-- # Class: PopulationSubject Description: A population or cohort of subjects studied in aggregate. Used for epidemiological or population-level analyses. Can optionally hold references to individual InVivoSubject members.
--     * Slot: cohort_size Description: Number of subjects in the cohort or population.
--     * Slot: inclusion_criteria Description: Criteria for inclusion in the study population.
--     * Slot: subject_type Description: The specific type of study subject. Used to designate which concrete class (e.g., CellularSystem, InVivoSubject) is instantiated for polymorphic study_subject slots.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: age_range_id Description: Age range of the study population.
--     * Slot: model_species_id Description: The species of origin for the cells or organism being studied. Reference to NCBITaxon term.
-- # Class: Protocol Description: A detailed set of steps for how to perform a specific assay. Protocols ensure reproducibility across laboratories. Contains universal slots; domain-specific details are in protocol subclasses (ImagingProtocol, StainingProtocol, etc.). Protocols can reference other protocols via sub_protocols to represent composite workflows (e.g., sample preparation, wash steps, or post-processing protocols that are shared across assays).
--     * Slot: protocol_type Description: The specific type of protocol. Used to designate which concrete class (e.g., ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is instantiated for polymorphic protocol slots.
--     * Slot: protocol_version Description: Version of the protocol.
--     * Slot: quality_control_criteria Description: Quality control acceptance criteria.
--     * Slot: replicate_requirements Description: Number of replicates required.
--     * Slot: protocol_author Description: Author of the protocol.
--     * Slot: institution Description: Institution where protocol was developed.
--     * Slot: publication_reference Description: Reference to protocol publication.
--     * Slot: last_updated Description: Date protocol was last updated.
--     * Slot: validation_status Description: Validation status of the protocol.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: Assay_id Description: Autocreated FK slot
--     * Slot: Protocol_id Description: Autocreated FK slot
--     * Slot: ImagingProtocol_id Description: Autocreated FK slot
--     * Slot: StainingProtocol_id Description: Autocreated FK slot
--     * Slot: SpirometryProtocol_id Description: Autocreated FK slot
--     * Slot: MolecularAssayProtocol_id Description: Autocreated FK slot
--     * Slot: CiliaryFunctionAssay_id Description: Autocreated FK slot
--     * Slot: ASLAssay_id Description: Autocreated FK slot
--     * Slot: MucociliaryClearanceAssay_id Description: Autocreated FK slot
--     * Slot: OxidativeStressAssay_id Description: Autocreated FK slot
--     * Slot: CFTRFunctionAssay_id Description: Autocreated FK slot
--     * Slot: EGFRSignalingAssay_id Description: Autocreated FK slot
--     * Slot: GobletCellAssay_id Description: Autocreated FK slot
--     * Slot: BALFSputumAssay_id Description: Autocreated FK slot
--     * Slot: LungFunctionAssay_id Description: Autocreated FK slot
--     * Slot: FoxJExpressionAssay_id Description: Autocreated FK slot
--     * Slot: GeneExpressionAssay_id Description: Autocreated FK slot
-- # Class: ImagingProtocol Description: Protocol for imaging-based assays (CBF, ASL, MCC). Captures frame rate, duration, resolution, and tracer/labeling details.
--     * Slot: fluorescent_labeling Description: Fluorescent label or tracer used.
--     * Slot: fluorescent_tracer Description: Fluorescent tracer used for tracking (MCC assays).
--     * Slot: evaporation_prevention Description: Method used to prevent evaporation (e.g., perfluorocarbon overlay).
--     * Slot: particle_tracking_method Description: Method used for tracking particles or mucus.
--     * Slot: protocol_type Description: The specific type of protocol. Used to designate which concrete class (e.g., ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is instantiated for polymorphic protocol slots.
--     * Slot: protocol_version Description: Version of the protocol.
--     * Slot: quality_control_criteria Description: Quality control acceptance criteria.
--     * Slot: replicate_requirements Description: Number of replicates required.
--     * Slot: protocol_author Description: Author of the protocol.
--     * Slot: institution Description: Institution where protocol was developed.
--     * Slot: publication_reference Description: Reference to protocol publication.
--     * Slot: last_updated Description: Date protocol was last updated.
--     * Slot: validation_status Description: Validation status of the protocol.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: imaging_frame_rate_id Description: Frame rate for video/imaging acquisition (e.g., 200 fps).
--     * Slot: imaging_duration_id Description: Duration of imaging session.
--     * Slot: spatial_resolution_id Description: Spatial resolution of imaging (e.g., 1-2 um axial resolution).
--     * Slot: temperature_control_id Description: Temperature conditions during the procedure (e.g., 37C).
--     * Slot: humidity_control_id Description: Humidity conditions during the procedure.
--     * Slot: particle_size_id Description: Size of tracking particles.
-- # Class: StainingProtocol Description: Protocol for staining-based assays (goblet cell, immunofluorescence). Captures staining type, antibodies, fixation, and detection details.
--     * Slot: staining_type Description: Type of staining used (e.g., immunofluorescence, AB-PAS).
--     * Slot: detection_method Description: Detection method used (e.g., flow cytometry, plate reader).
--     * Slot: normalization_method Description: Method used for data normalization.
--     * Slot: fixation_method Description: Fixation method used for tissue/cell preparation.
--     * Slot: counterstain Description: Counterstain used (e.g., hematoxylin, DAPI).
--     * Slot: protocol_type Description: The specific type of protocol. Used to designate which concrete class (e.g., ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is instantiated for polymorphic protocol slots.
--     * Slot: protocol_version Description: Version of the protocol.
--     * Slot: quality_control_criteria Description: Quality control acceptance criteria.
--     * Slot: replicate_requirements Description: Number of replicates required.
--     * Slot: protocol_author Description: Author of the protocol.
--     * Slot: institution Description: Institution where protocol was developed.
--     * Slot: publication_reference Description: Reference to protocol publication.
--     * Slot: last_updated Description: Date protocol was last updated.
--     * Slot: validation_status Description: Validation status of the protocol.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
-- # Class: SpirometryProtocol Description: Protocol for lung function / spirometry assays. Captures spirometry standards, bronchodilator details, and plethysmography method.
--     * Slot: spirometry_standard Description: Spirometry standard followed (e.g., ATS/ERS 2019).
--     * Slot: bronchodilator_agent Description: Bronchodilator agent used (e.g., albuterol).
--     * Slot: plethysmography_method Description: Method for plethysmography measurement.
--     * Slot: protocol_type Description: The specific type of protocol. Used to designate which concrete class (e.g., ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is instantiated for polymorphic protocol slots.
--     * Slot: protocol_version Description: Version of the protocol.
--     * Slot: quality_control_criteria Description: Quality control acceptance criteria.
--     * Slot: replicate_requirements Description: Number of replicates required.
--     * Slot: protocol_author Description: Author of the protocol.
--     * Slot: institution Description: Institution where protocol was developed.
--     * Slot: publication_reference Description: Reference to protocol publication.
--     * Slot: last_updated Description: Date protocol was last updated.
--     * Slot: validation_status Description: Validation status of the protocol.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: bronchodilator_dose_id Description: Dose of bronchodilator administered.
-- # Class: MolecularAssayProtocol Description: Protocol for molecular biology assays (qRT-PCR, Western blot, ELISA). Captures detection method, normalization, primers, and platform details.
--     * Slot: detection_method Description: Detection method used (e.g., flow cytometry, plate reader).
--     * Slot: normalization_method Description: Method used for data normalization.
--     * Slot: reference_gene Description: Reference/housekeeping gene used for normalization.
--     * Slot: lysis_buffer Description: Lysis buffer used for sample preparation.
--     * Slot: platform Description: Assay platform or instrument used (e.g., QuantStudio, Illumina).
--     * Slot: protocol_type Description: The specific type of protocol. Used to designate which concrete class (e.g., ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is instantiated for polymorphic protocol slots.
--     * Slot: protocol_version Description: Version of the protocol.
--     * Slot: quality_control_criteria Description: Quality control acceptance criteria.
--     * Slot: replicate_requirements Description: Number of replicates required.
--     * Slot: protocol_author Description: Author of the protocol.
--     * Slot: institution Description: Institution where protocol was developed.
--     * Slot: publication_reference Description: Reference to protocol publication.
--     * Slot: last_updated Description: Date protocol was last updated.
--     * Slot: validation_status Description: Validation status of the protocol.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
-- # Class: QuantityValue Description: A quantity with a numeric value and unit of measurement. Used for all measurement values in assays.
--     * Slot: id
--     * Slot: value Description: The numeric value of the quantity.
--     * Slot: unit_id Description: The unit of measurement.
-- # Class: Unit Description: A unit of measurement from a standard ontology (UO, UCUM, QUDT).
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
-- # Class: NamedEntity Description: A reference to an entity with an identifier and name. Used for cell_type, tissue_context, participant references, etc.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
-- # Class: ExposureCondition Description: A structured description of an exposure or treatment applied to a biological system. Captures what agent was applied, at what concentration, for how long, and when the measurement was taken relative to exposure.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: Assay_id Description: Autocreated FK slot
--     * Slot: CiliaryFunctionAssay_id Description: Autocreated FK slot
--     * Slot: ASLAssay_id Description: Autocreated FK slot
--     * Slot: MucociliaryClearanceAssay_id Description: Autocreated FK slot
--     * Slot: OxidativeStressAssay_id Description: Autocreated FK slot
--     * Slot: CFTRFunctionAssay_id Description: Autocreated FK slot
--     * Slot: EGFRSignalingAssay_id Description: Autocreated FK slot
--     * Slot: GobletCellAssay_id Description: Autocreated FK slot
--     * Slot: BALFSputumAssay_id Description: Autocreated FK slot
--     * Slot: LungFunctionAssay_id Description: Autocreated FK slot
--     * Slot: FoxJExpressionAssay_id Description: Autocreated FK slot
--     * Slot: GeneExpressionAssay_id Description: Autocreated FK slot
--     * Slot: exposure_agent_id Description: The chemical, biological, or environmental agent used for exposure or treatment. Reference to a CHEBI or ECTO ontology term.
--     * Slot: exposure_concentration_id Description: Concentration of the exposure agent applied.
--     * Slot: exposure_duration_id Description: Duration of exposure or treatment.
--     * Slot: timing_post_exposure_id Description: Time after exposure when the measurement was taken. Used to capture the temporal relationship between exposure and assay readout.
-- # Class: CellularSystem Description: Cell-based model systems that use living cells to model biological processes.
--     * Slot: cell_culture_growth_mode
--     * Slot: substrate_type
--     * Slot: passage_number
--     * Slot: coating
--     * Slot: matrix_composition
--     * Slot: organoid_type
--     * Slot: days_at_differentiation Description: Days at air-liquid interface or differentiation stage.
--     * Slot: donor_info Description: Information about cell donor (e.g., healthy non-smoker, CF patient, age, anatomical region).
--     * Slot: replicates_per_donor Description: Number of biological replicates per donor.
--     * Slot: subject_type Description: The specific type of study subject. Used to designate which concrete class (e.g., CellularSystem, InVivoSubject) is instantiated for polymorphic study_subject slots.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: cell_line_id
--     * Slot: primary_cell_id
--     * Slot: cell_type_id Description: The cell type being studied. Reference to a Cell Ontology (CL) term. Used on CellularSystem and CellLine to describe the cell identity.
--     * Slot: anatomical_origin_id
--     * Slot: confluence_level_id
--     * Slot: seeding_density_id
--     * Slot: size_range_id
--     * Slot: culture_conditions_id
--     * Slot: culture_media_id
--     * Slot: model_species_id Description: The species of origin for the cells or organism being studied. Reference to NCBITaxon term.
-- # Class: CellLine Description: A cell line - a genetically stable cultured cell population.
--     * Slot: tissue_origin
--     * Slot: disease_state
--     * Slot: supplier
--     * Slot: catalog_number
--     * Slot: authentication_method
--     * Slot: mycoplasma_status
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: cell_type_id Description: The cell type being studied. Reference to a Cell Ontology (CL) term. Used on CellularSystem and CellLine to describe the cell identity.
--     * Slot: model_species_id Description: The species of origin for the cells or organism being studied. Reference to NCBITaxon term.
-- # Class: CellCultureConditions Description: Detailed cell culture parameters including medium, environment, and timing.
--     * Slot: days_at_air_liquid_interface
--     * Slot: passage_number
--     * Slot: substrate_type
--     * Slot: cell_culture_growth_mode
--     * Slot: donor_count
--     * Slot: replicates_per_donor Description: Number of biological replicates per donor.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: culture_media_id
-- # Class: CellCultureMedium Description: Detailed formulation of cell culture medium including base medium and supplements.
--     * Slot: base_medium
--     * Slot: serum_type
--     * Slot: manufacturer
--     * Slot: catalog_number
--     * Slot: lot_number
--     * Slot: preparation_date
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: serum_concentration_id
--     * Slot: osmolality_id
-- # Class: MediumSupplement Description: Supplement or additive to cell culture medium.
--     * Slot: supplement_type
--     * Slot: manufacturer
--     * Slot: catalog_number
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: CellCultureMedium_id Description: Autocreated FK slot
--     * Slot: concentration_id
-- # Class: QuantityRange Description: A range of quantity values with minimum and maximum bounds.
--     * Slot: id
--     * Slot: min_value_id
--     * Slot: max_value_id
--     * Slot: unit_id Description: The unit of measurement.
-- # Class: CiliaryFunctionAssay Description: Assay for measuring ciliary function including beat frequency, active area, cilia morphology, and ciliated cell populations. Informs on Key Event: "Decreased ciliary function" in respiratory AOPs.CONTEXT: Can be performed in vitro (tissue slices, spheroids) or in vivo (often using optical coherence tomography).TIER 1 slots (critical): beat_frequency_hz, active_area_percentage, cilia_length, cilia_per_cell, percentage_ciliated_cells, cell_type_ratios,
--     * Slot: analysis_software Description: Software used for analysis (e.g., SAVA, Cilia FA).
--     * Slot: airway_region Description: Region of airway from which cells originated.
--     * Slot: assay_date Description: Date when the assay was performed.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: informs_on_key_event_id Description: The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.
--     * Slot: study_subject_id Description: Can be ModelSystem (in vitro - ALI cultures, tissue slices, spheroids) or InVivoSubject (in vivo - OCT measurements)
--     * Slot: has_specified_output_id Description: The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).
-- # Class: CiliaryFunctionOutput Description: Measurement results from a ciliary function assay. Contains the measured values for ciliary beat frequency, active area, cilia morphology, and ciliated cell populations.
--     * Slot: ciliary_motion_patterns Description: Patterns of ciliary motion (coordinated, dyskinetic, immotile). TIER 2 - supporting information.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: beat_frequency_hz_id Description: Ciliary beat frequency measured in Hz. TIER 1 - critical for assessing ciliary function.
--     * Slot: active_area_percentage_id Description: Percentage of epithelial surface with actively beating cilia. TIER 1 - critical for assessing ciliary coverage.
--     * Slot: cilia_length_id Description: Length of cilia measured in micrometers. TIER 1 - morphological assessment of cilia.
--     * Slot: cilia_per_cell_id Description: Number of cilia per ciliated cell. TIER 1.
--     * Slot: percentage_ciliated_cells_id Description: Percentage of cells that are ciliated. TIER 1 - critical for understanding ciliated cell populations.
--     * Slot: ciliary_beat_amplitude_id Description: Amplitude of ciliary beat. TIER 2.
-- # Class: ASLAssay Description: Assay for measuring airway surface liquid properties including ASL height, periciliary layer depth, and ion composition. Informs on Key Event: "Decreased ASL height" or "Altered airway hydration" in CF-related AOPs.
--     * Slot: assay_date Description: Date when the assay was performed.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: informs_on_key_event_id Description: The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.
--     * Slot: study_subject_id Description: The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.
--     * Slot: has_specified_output_id Description: The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).
-- # Class: ASLOutput Description: Measurement results from an airway surface liquid assay. Contains the measured values for ASL height, periciliary layer depth, and ion composition.
--     * Slot: ion_composition Description: Ionic composition (Cl-, Na+, K+). TIER 3 - not critical for comparison but relevant for mechanism.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: asl_height_um_id Description: Airway surface liquid height in micrometers. TIER 1 - primary measurement for ASL assays.
--     * Slot: periciliary_layer_depth_id Description: Depth of the periciliary layer in micrometers. TIER 1 - helps give confidence to the outcome.
--     * Slot: mucus_layer_thickness_id Description: Thickness of the mucus gel layer in micrometers. TIER 2.
--     * Slot: asl_ph_id Description: pH of airway surface liquid. TIER 3.
-- # Class: MucociliaryClearanceAssay Description: Assay for measuring mucociliary clearance and transport. Informs on Key Event: "Impaired mucociliary clearance" in respiratory AOPs. TIER 1 slots (critical): transport_rate, directionality.
--     * Slot: mucus_composition Description: Composition of mucus. TIER 2 per feedback.
--     * Slot: assay_date Description: Date when the assay was performed.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: informs_on_key_event_id Description: The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.
--     * Slot: study_subject_id Description: The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.
--     * Slot: has_specified_output_id Description: The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).
-- # Class: MucociliaryClearanceOutput Description: Measurement results from a mucociliary clearance assay. Contains the measured values for transport rate, directionality, and clearance metrics.
--     * Slot: transport_directionality Description: Directionality of mucociliary transport. TIER 1.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: transport_rate_id Description: Mucociliary transport rate. TIER 1 - primary outcome measure for MCC assays.
--     * Slot: mucus_layer_thickness_id Description: Thickness of the mucus gel layer in micrometers. TIER 2.
--     * Slot: percentage_active_transport_id Description: Percentage of area showing active transport. TIER 2.
--     * Slot: particle_clearance_time_id Description: Time for particle clearance. TIER 2.
-- # Class: OxidativeStressAssay Description: Assay for measuring oxidative stress markers. Informs on Key Event: "Increased oxidative stress" - often a Molecular Initiating Event (MIE) in respiratory toxicology AOPs. TIER 1 slots (critical): All surrogate markers for oxidative stress. Multiple detection methods expected - no single "best" for lung function.
--     * Slot: ros_probe_type Description: Type of ROS probe used (DCFDA, DHE, MitoSOX, etc.). TIER 1 - varies by method.
--     * Slot: assay_date Description: Date when the assay was performed.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: informs_on_key_event_id Description: The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.
--     * Slot: study_subject_id Description: The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.
--     * Slot: has_specified_output_id Description: The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).
-- # Class: OxidativeStressOutput Description: Measurement results from an oxidative stress assay. Contains all surrogate markers for oxidative stress including ROS levels, lipid peroxidation, protein oxidation, DNA damage, and antioxidant capacity.
--     * Slot: antioxidant_enzyme_activities Description: Antioxidant enzyme activities (SOD, catalase, GPx). TIER 1.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: reactive_oxygen_species_id Description: ROS level as fold change or fluorescence intensity. TIER 1.
--     * Slot: lipid_peroxidation_id Description: Lipid peroxidation level. TIER 1 - surrogate marker for OS.
--     * Slot: malondialdehyde_level_id Description: MDA level - lipid peroxidation marker.
--     * Slot: four_hydroxynonenal_level_id Description: 4-HNE level - lipid peroxidation marker.
--     * Slot: eight_isoprostane_level_id Description: 8-isoprostane level.
--     * Slot: protein_carbonyl_content_id Description: Protein carbonyl content. TIER 1.
--     * Slot: nitrotyrosine_level_id Description: Nitrotyrosine level. TIER 1.
--     * Slot: dna_damage_markers_id Description: DNA damage markers (8-OHdG). TIER 1 - surrogate for OS.
--     * Slot: eight_ohdg_level_id Description: 8-OHdG level (DNA oxidation marker). TIER 1.
--     * Slot: antioxidant_capacity_id Description: Total antioxidant capacity or GSH/GSSG ratio. TIER 1.
--     * Slot: glutathione_ratio_id Description: GSH/GSSG ratio indicating antioxidant status. TIER 1.
--     * Slot: superoxide_dismutase_activity_id Description: SOD activity. TIER 1.
--     * Slot: catalase_activity_id Description: Catalase activity. TIER 1.
--     * Slot: glutathione_peroxidase_activity_id Description: GPx activity. TIER 1.
--     * Slot: total_antioxidant_capacity_id Description: Total antioxidant capacity. TIER 1.
--     * Slot: nrf2_activation_id Description: Nrf2 activation level. TIER 1.
-- # Class: CFTRFunctionAssay Description: Assay for measuring CFTR (Cystic Fibrosis Transmembrane Conductance Regulator) function. Informs on Key Event: "Decreased CFTR function" in cystic fibrosis-related AOPs.
--     * Slot: stimulation_agent Description: Stimulation agent used (e.g., forskolin concentration).
--     * Slot: inhibitor_used Description: Inhibitor used (e.g., CFTRinh-172).
--     * Slot: assay_date Description: Date when the assay was performed.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: informs_on_key_event_id Description: The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.
--     * Slot: study_subject_id Description: The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.
--     * Slot: has_specified_output_id Description: The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).
-- # Class: CFTRFunctionOutput Description: Measurement results from a CFTR function assay. Contains the measured values for CFTR-mediated chloride secretion, forskolin response, and related electrophysiology measurements.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: cftr_chloride_secretion_id Description: CFTR-mediated chloride secretion in uA/cm2.
--     * Slot: cftr_forskolin_response_id Description: Forskolin-stimulated CFTR response.
--     * Slot: inhibitor_sensitive_current_id Description: Inhibitor-sensitive current measurement.
--     * Slot: cftr_specific_current_id Description: CFTR-specific chloride secretory current.
--     * Slot: sweat_chloride_concentration_id Description: Sweat chloride concentration in mEq/L (CF diagnostic).
--     * Slot: nasal_potential_difference_id Description: Nasal potential difference in mV.
-- # Class: EGFRSignalingAssay Description: Assay for measuring EGFR phosphorylation and downstream signaling. Informs on Key Event: "EGFR activation" in mucus hypersecretion AOPs.IMPORTANT: EGFR phosphorylation is the MOST SPECIFIC evidence for activation. Downstream kinase data alone is insufficient - needs phosphorylation measure OR inhibitor reversal for strong evidence. Cell type matters due to receptor location in ALI cultures.TIER 1 slots (critical): egfr_phosphorylation with site specification.
--     * Slot: normalization_reference Description: Normalization reference (beta-actin, GAPDH, total EGFR).
--     * Slot: phosphorylation_site Description: Specific phosphorylation site being measured.
--     * Slot: assay_date Description: Date when the assay was performed.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: informs_on_key_event_id Description: The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.
--     * Slot: study_subject_id Description: The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.
--     * Slot: has_specified_output_id Description: The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).
-- # Class: EGFRSignalingOutput Description: Measurement results from an EGFR signaling assay. Contains the measured values for EGFR phosphorylation, total protein, and downstream kinase activation.
--     * Slot: downstream_kinase_activation Description: Activation levels of downstream kinases. TIER 2 - not specific to EGFR alone without phosphorylation data.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: egfr_phosphorylation_y1068_id Description: EGFR phosphorylation at Y1068 residue (fold change). TIER 1 - MOST SPECIFIC evidence for EGFR activation.
--     * Slot: egfr_phosphorylation_y1173_id Description: EGFR phosphorylation at Y1173 residue (fold change). TIER 1.
--     * Slot: total_egfr_protein_id Description: Total EGFR protein level (loading control). TIER 1.
--     * Slot: erk_phosphorylation_id Description: ERK phosphorylation level. TIER 2.
--     * Slot: akt_phosphorylation_id Description: AKT phosphorylation level. TIER 2.
--     * Slot: egfr_ligand_expression_id Description: Expression of EGFR ligands (EGF, TGF-alpha, amphiregulin).
--     * Slot: egfr_membrane_localization_id Description: EGFR membrane localization percentage.
-- # Class: GobletCellAssay Description: Assay for measuring goblet cell populations and mucin production. Informs on Key Event: "Goblet cell hyperplasia" or "Mucin hypersecretion".IMPORTANT per domain feedback: Need BOTH cell counts AND mucin secretion measurements - cells may stay same but secretion changes. AB-PAS staining common for visualizing goblet cells. Some secreted mucins not tethered to goblet cells.
--     * Slot: assay_date Description: Date when the assay was performed.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: informs_on_key_event_id Description: The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.
--     * Slot: study_subject_id Description: The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.
--     * Slot: has_specified_output_id Description: The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).
-- # Class: GobletCellOutput Description: Measurement results from a goblet cell assay. Contains the measured values for goblet cell counts, mucin expression, and mucus properties.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: goblet_cell_count_id Description: Number of goblet cells (raw count). TIER 1 - want both raw and relative information.
--     * Slot: goblet_cell_percentage_id Description: Percentage of goblet cells. TIER 1.
--     * Slot: muc5ac_mrna_expression_id Description: MUC5AC mRNA expression level (fold change). TIER 1.
--     * Slot: muc5ac_protein_expression_id Description: MUC5AC protein expression level. TIER 1.
--     * Slot: muc5b_mrna_expression_id Description: MUC5B mRNA expression level (fold change). TIER 1.
--     * Slot: muc5b_protein_expression_id Description: MUC5B protein expression level. TIER 1.
--     * Slot: muc5ac_muc5b_ratio_id Description: MUC5AC to MUC5B ratio. TIER 1 - important for disease state.
--     * Slot: mucin_protein_concentration_id Description: Total mucin protein concentration. TIER 1 - want both direct and comparative measures.
--     * Slot: mucin_secretion_rate_id Description: Mucin secretion rate. TIER 1.
--     * Slot: percent_solids_id Description: Percent solids in apical secretion (overall secretion). TIER 1.
--     * Slot: goblet_to_ciliated_ratio_id Description: Ratio of goblet cells to ciliated cells. TIER 2 - related to transdifferentiation but not critical for outcome.
--     * Slot: mucus_viscosity_id Description: Mucus viscosity in centipoise. TIER 2.
-- # Class: BALFSputumAssay Description: Assay for measuring bronchoalveolar lavage fluid (BALF) or sputum composition. Informs on Key Event: "Airway inflammation" and provides evidence for inflammatory cell populations and cytokine levels.This assay is IN VIVO ONLY - requires samples from human or animal subjects.
--     * Slot: assay_date Description: Date when the assay was performed.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: target_cell_type_id Description: The specific cell type that is the primary focus of this assay's analysis, when the assay examines multiple cell populations in a sample (e.g., neutrophils in a BALF differential).
--     * Slot: informs_on_key_event_id Description: The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.
--     * Slot: study_subject_id Description: The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.
--     * Slot: has_specified_output_id Description: The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).
-- # Class: BALFSputumOutput Description: Measurement results from a BALF/sputum assay. Contains inflammatory cell differentials, cytokine concentrations, and microbiome metrics.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: neutrophil_percentage_id Description: Neutrophil percentage in BALF/sputum.
--     * Slot: eosinophil_percentage_id Description: Eosinophil percentage in BALF/sputum.
--     * Slot: macrophage_percentage_id Description: Macrophage percentage in BALF/sputum.
--     * Slot: lymphocyte_percentage_id Description: Lymphocyte percentage in BALF/sputum.
--     * Slot: total_cell_count_id Description: Total cell count in BALF/sputum.
--     * Slot: il6_concentration_id Description: IL-6 concentration.
--     * Slot: il8_concentration_id Description: IL-8 concentration.
--     * Slot: tnf_alpha_concentration_id Description: TNF-alpha concentration.
--     * Slot: il1_beta_concentration_id Description: IL-1 beta concentration.
--     * Slot: total_protein_concentration_id Description: Total protein concentration.
--     * Slot: alpha_diversity_id Description: Alpha diversity (microbiome).
--     * Slot: beta_diversity_id Description: Beta diversity (microbiome).
--     * Slot: bacterial_load_id Description: Bacterial load (16S copies or CFU).
--     * Slot: cell_free_dna_id Description: Cell-free DNA concentration.
-- # Class: LungFunctionAssay Description: Clinical assay for measuring lung function. Informs on Adverse Outcome: "Decreased lung function" - the composite clinical outcome.IMPORTANT per domain feedback: - Subject characteristics (sex, species, age, height) are critical -  often reported as % of predicted baseline- Reference dataset (GLI-2012 for humans) is essential for interpretation - Hemoglobin levels pair with DLCO measurements - Recent respiratory illness affects spirometry resultsTIER 1 slots (critical): fev1, fvc, subject_characteristics, reference_dataset. This assay is IN VIVO ONLY.
--     * Slot: reference_dataset Description: Reference dataset for interpretation (GLI-2012 for humans). TIER 1 - essential for interpretation.
--     * Slot: recent_respiratory_illness Description: Recent respiratory illness (affects spirometry). TIER 2.
--     * Slot: assay_date Description: Date when the assay was performed.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: hemoglobin_level_id Description: Hemoglobin level. TIER 2 - pairs with DLCO.
--     * Slot: informs_on_key_event_id Description: The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.
--     * Slot: study_subject_id Description: The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.
--     * Slot: has_specified_output_id Description: The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).
-- # Class: LungFunctionOutput Description: Measurement results from a lung function assay. Contains spirometry measurements, diffusing capacity, and related clinical metrics.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: fev1_id Description: Forced expiratory volume in 1 second. TIER 1 - primary spirometry measurement.
--     * Slot: fvc_id Description: Forced vital capacity. TIER 1 - primary spirometry measurement.
--     * Slot: fev1_fvc_ratio_id Description: Ratio of FEV1 to FVC (Tiffeneau-Pinelli index). TIER 2 - can be calculated from FEV1 and FVC.
--     * Slot: feno_id Description: Fractional exhaled nitric oxide in ppb. TIER 2 - marker for airway inflammation.
--     * Slot: decline_rate_id Description: Longitudinal decline rate in mL/year. TIER 2 - useful for pre/post comparisons.
--     * Slot: bronchodilator_response_id Description: Response to bronchodilator (% change in FEV1). TIER 2 - informs reversibility.
--     * Slot: dlco_id Description: Diffusing capacity for carbon monoxide. TIER 2 - measure of fibrosis, needs hemoglobin level.
--     * Slot: peak_expiratory_flow_id Description: Peak expiratory flow. TIER 2.
--     * Slot: fef25_75_id Description: Forced expiratory flow 25-75%. TIER 3 - more variable than FEV1, FVC.
--     * Slot: total_lung_capacity_id Description: Total lung capacity. TIER 3 - requires more equipment.
--     * Slot: functional_residual_capacity_id Description: Functional residual capacity. TIER 3 - requires more equipment.
--     * Slot: residual_volume_id Description: Residual volume. TIER 3 - requires more equipment.
--     * Slot: lung_compliance_id Description: Lung compliance. TIER 3 - most often reported for animals, difficult to relate to human exposure.
--     * Slot: lung_elastance_id Description: Lung elastance. TIER 3 - most often reported for animals.
--     * Slot: lung_resistance_id Description: Lung resistance. TIER 3 - most often reported for animals.
-- # Class: FoxJExpressionAssay Description: Assay for measuring FoxJ1 expression related to ciliogenesis. Informs on Key Event: "Altered ciliogenesis" in respiratory AOPs. FoxJ1 is a master transcription factor for motile cilia.This assay is primarily IN VITRO focused.
--     * Slot: assay_date Description: Date when the assay was performed.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: informs_on_key_event_id Description: The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.
--     * Slot: study_subject_id Description: The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.
--     * Slot: has_specified_output_id Description: The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).
-- # Class: FoxJExpressionOutput Description: Measurement results from a FoxJ1 expression assay. Contains the measured values for FoxJ1 mRNA, protein, and cellular localization.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: foxj1_mrna_expression_id Description: FoxJ1 mRNA expression level.
--     * Slot: foxj1_protein_expression_id Description: FoxJ1 protein expression level.
--     * Slot: foxj1_positive_cell_percentage_id Description: Percentage of FoxJ1-positive cells.
--     * Slot: foxj1_nuclear_localization_id Description: FoxJ1 nuclear localization.
-- # Class: GeneExpressionAssay Description: General assay for gene expression measurements. Renamed from TranscriptionFactorExpressionMeasurement per domain feedback - gene expression is more commonly the primary output.
--     * Slot: target_gene Description: Target gene being measured.
--     * Slot: gene_expression_method Description: Method used for gene expression (qRT-PCR, RNA-seq, etc.).
--     * Slot: normalization_reference Description: Normalization reference (beta-actin, GAPDH, total EGFR).
--     * Slot: assay_date Description: Date when the assay was performed.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: informs_on_key_event_id Description: The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.
--     * Slot: study_subject_id Description: The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.
--     * Slot: has_specified_output_id Description: The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).
-- # Class: GeneExpressionOutput Description: Measurement results from a gene expression assay. Contains the measured values for mRNA level, protein level, and positive cell percentage.
--     * Slot: id Description: A unique identifier for the entity.
--     * Slot: name Description: A human-readable name for the entity.
--     * Slot: description Description: A detailed description of the entity.
--     * Slot: mrna_level_id Description: mRNA expression level.
--     * Slot: protein_level_id Description: Protein expression level.
--     * Slot: percentage_positive_cells_id Description: Percentage of positive cells (IHC, flow cytometry).
-- # Class: AdverseOutcomePathway_stressors
--     * Slot: AdverseOutcomePathway_id Description: Autocreated FK slot
--     * Slot: stressors Description: Chemical or physical stressors that can trigger this AOP.
-- # Class: Protocol_equipment_required
--     * Slot: Protocol_id Description: Autocreated FK slot
--     * Slot: equipment_required Description: Equipment required for this protocol.
-- # Class: ImagingProtocol_equipment_required
--     * Slot: ImagingProtocol_id Description: Autocreated FK slot
--     * Slot: equipment_required Description: Equipment required for this protocol.
-- # Class: StainingProtocol_antibodies_used
--     * Slot: StainingProtocol_id Description: Autocreated FK slot
--     * Slot: antibodies_used Description: Antibodies used in staining or detection.
-- # Class: StainingProtocol_equipment_required
--     * Slot: StainingProtocol_id Description: Autocreated FK slot
--     * Slot: equipment_required Description: Equipment required for this protocol.
-- # Class: SpirometryProtocol_equipment_required
--     * Slot: SpirometryProtocol_id Description: Autocreated FK slot
--     * Slot: equipment_required Description: Equipment required for this protocol.
-- # Class: MolecularAssayProtocol_antibodies_used
--     * Slot: MolecularAssayProtocol_id Description: Autocreated FK slot
--     * Slot: antibodies_used Description: Antibodies used in staining or detection.
-- # Class: MolecularAssayProtocol_primer_sequences
--     * Slot: MolecularAssayProtocol_id Description: Autocreated FK slot
--     * Slot: primer_sequences Description: Primer sequences used for PCR-based methods.
-- # Class: MolecularAssayProtocol_equipment_required
--     * Slot: MolecularAssayProtocol_id Description: Autocreated FK slot
--     * Slot: equipment_required Description: Equipment required for this protocol.
-- # Class: CellularSystem_cell_type_ratios
--     * Slot: CellularSystem_id Description: Autocreated FK slot
--     * Slot: cell_type_ratios
-- # Class: CiliaryFunctionOutput_cell_type_ratios
--     * Slot: CiliaryFunctionOutput_id Description: Autocreated FK slot
--     * Slot: cell_type_ratios
-- # Class: OxidativeStressOutput_protein_oxidation_markers
--     * Slot: OxidativeStressOutput_id Description: Autocreated FK slot
--     * Slot: protein_oxidation_markers Description: Protein oxidation markers (carbonyls, nitrotyrosine). TIER 1.
-- # Class: EGFRSignalingOutput_pathway_biomarkers
--     * Slot: EGFRSignalingOutput_id Description: Autocreated FK slot
--     * Slot: pathway_biomarkers Description: Pathway-specific biomarker signatures. TIER 2 - relationship to outcome needs further investigation.

CREATE TABLE "Container" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Container_id" ON "Container" (id);
CREATE TABLE "NamedThing" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_NamedThing_id" ON "NamedThing" (id);
CREATE TABLE "AdverseOutcome" (
	outcome_level VARCHAR(10),
	biological_process TEXT,
	occurs_in_anatomy TEXT,
	aopwiki_id TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_AdverseOutcome_id" ON "AdverseOutcome" (id);
CREATE TABLE "MolecularInitiatingEvent" (
	target_molecule TEXT,
	biological_process TEXT,
	biological_object TEXT,
	biological_action VARCHAR(9),
	level_of_biological_organization VARCHAR(10),
	occurs_in_cell_type TEXT,
	occurs_in_anatomy TEXT,
	aopwiki_id TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MolecularInitiatingEvent_id" ON "MolecularInitiatingEvent" (id);
CREATE TABLE "AssayOutputMeasurement" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_AssayOutputMeasurement_id" ON "AssayOutputMeasurement" (id);
CREATE TABLE "StainingProtocol" (
	staining_type TEXT,
	detection_method TEXT,
	normalization_method TEXT,
	fixation_method TEXT,
	counterstain TEXT,
	protocol_type TEXT,
	protocol_version TEXT,
	quality_control_criteria TEXT,
	replicate_requirements INTEGER,
	protocol_author TEXT,
	institution TEXT,
	publication_reference TEXT,
	last_updated DATE,
	validation_status TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_StainingProtocol_id" ON "StainingProtocol" (id);
CREATE TABLE "MolecularAssayProtocol" (
	detection_method TEXT,
	normalization_method TEXT,
	reference_gene TEXT,
	lysis_buffer TEXT,
	platform TEXT,
	protocol_type TEXT,
	protocol_version TEXT,
	quality_control_criteria TEXT,
	replicate_requirements INTEGER,
	protocol_author TEXT,
	institution TEXT,
	publication_reference TEXT,
	last_updated DATE,
	validation_status TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MolecularAssayProtocol_id" ON "MolecularAssayProtocol" (id);
CREATE TABLE "Unit" (
	id TEXT NOT NULL,
	name TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Unit_id" ON "Unit" (id);
CREATE TABLE "NamedEntity" (
	id TEXT NOT NULL,
	name TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_NamedEntity_id" ON "NamedEntity" (id);
CREATE TABLE "AdverseOutcomePathway" (
	aopwiki_id TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	molecular_initiating_event_id TEXT,
	adverse_outcome_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY(molecular_initiating_event_id) REFERENCES "MolecularInitiatingEvent" (id),
	FOREIGN KEY(adverse_outcome_id) REFERENCES "AdverseOutcome" (id)
);CREATE INDEX "ix_AdverseOutcomePathway_id" ON "AdverseOutcomePathway" (id);
CREATE TABLE "StudySubject" (
	subject_type TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	model_species_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(model_species_id) REFERENCES "NamedEntity" (id)
);CREATE INDEX "ix_StudySubject_id" ON "StudySubject" (id);
CREATE TABLE "ModelSystem" (
	subject_type TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	model_species_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(model_species_id) REFERENCES "NamedEntity" (id)
);CREATE INDEX "ix_ModelSystem_id" ON "ModelSystem" (id);
CREATE TABLE "QuantityValue" (
	id INTEGER NOT NULL,
	value TEXT,
	unit_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(unit_id) REFERENCES "Unit" (id)
);CREATE INDEX "ix_QuantityValue_id" ON "QuantityValue" (id);
CREATE TABLE "CellLine" (
	tissue_origin TEXT,
	disease_state TEXT,
	supplier TEXT,
	catalog_number TEXT,
	authentication_method TEXT,
	mycoplasma_status TEXT,
	id TEXT NOT NULL,
	name TEXT,
	cell_type_id TEXT,
	model_species_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(cell_type_id) REFERENCES "NamedEntity" (id),
	FOREIGN KEY(model_species_id) REFERENCES "NamedEntity" (id)
);CREATE INDEX "ix_CellLine_id" ON "CellLine" (id);
CREATE TABLE "StainingProtocol_antibodies_used" (
	"StainingProtocol_id" TEXT,
	antibodies_used TEXT,
	PRIMARY KEY ("StainingProtocol_id", antibodies_used),
	FOREIGN KEY("StainingProtocol_id") REFERENCES "StainingProtocol" (id)
);CREATE INDEX "ix_StainingProtocol_antibodies_used_StainingProtocol_id" ON "StainingProtocol_antibodies_used" ("StainingProtocol_id");CREATE INDEX "ix_StainingProtocol_antibodies_used_antibodies_used" ON "StainingProtocol_antibodies_used" (antibodies_used);
CREATE TABLE "StainingProtocol_equipment_required" (
	"StainingProtocol_id" TEXT,
	equipment_required TEXT,
	PRIMARY KEY ("StainingProtocol_id", equipment_required),
	FOREIGN KEY("StainingProtocol_id") REFERENCES "StainingProtocol" (id)
);CREATE INDEX "ix_StainingProtocol_equipment_required_StainingProtocol_id" ON "StainingProtocol_equipment_required" ("StainingProtocol_id");CREATE INDEX "ix_StainingProtocol_equipment_required_equipment_required" ON "StainingProtocol_equipment_required" (equipment_required);
CREATE TABLE "MolecularAssayProtocol_antibodies_used" (
	"MolecularAssayProtocol_id" TEXT,
	antibodies_used TEXT,
	PRIMARY KEY ("MolecularAssayProtocol_id", antibodies_used),
	FOREIGN KEY("MolecularAssayProtocol_id") REFERENCES "MolecularAssayProtocol" (id)
);CREATE INDEX "ix_MolecularAssayProtocol_antibodies_used_MolecularAssayProtocol_id" ON "MolecularAssayProtocol_antibodies_used" ("MolecularAssayProtocol_id");CREATE INDEX "ix_MolecularAssayProtocol_antibodies_used_antibodies_used" ON "MolecularAssayProtocol_antibodies_used" (antibodies_used);
CREATE TABLE "MolecularAssayProtocol_primer_sequences" (
	"MolecularAssayProtocol_id" TEXT,
	primer_sequences TEXT,
	PRIMARY KEY ("MolecularAssayProtocol_id", primer_sequences),
	FOREIGN KEY("MolecularAssayProtocol_id") REFERENCES "MolecularAssayProtocol" (id)
);CREATE INDEX "ix_MolecularAssayProtocol_primer_sequences_primer_sequences" ON "MolecularAssayProtocol_primer_sequences" (primer_sequences);CREATE INDEX "ix_MolecularAssayProtocol_primer_sequences_MolecularAssayProtocol_id" ON "MolecularAssayProtocol_primer_sequences" ("MolecularAssayProtocol_id");
CREATE TABLE "MolecularAssayProtocol_equipment_required" (
	"MolecularAssayProtocol_id" TEXT,
	equipment_required TEXT,
	PRIMARY KEY ("MolecularAssayProtocol_id", equipment_required),
	FOREIGN KEY("MolecularAssayProtocol_id") REFERENCES "MolecularAssayProtocol" (id)
);CREATE INDEX "ix_MolecularAssayProtocol_equipment_required_MolecularAssayProtocol_id" ON "MolecularAssayProtocol_equipment_required" ("MolecularAssayProtocol_id");CREATE INDEX "ix_MolecularAssayProtocol_equipment_required_equipment_required" ON "MolecularAssayProtocol_equipment_required" (equipment_required);
CREATE TABLE "KeyEvent" (
	biological_process TEXT,
	biological_object TEXT,
	biological_action VARCHAR(9),
	level_of_biological_organization VARCHAR(10),
	occurs_in_cell_type TEXT,
	occurs_in_anatomy TEXT,
	aopwiki_id TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	"KeyEvent_id" TEXT,
	"AdverseOutcomePathway_id" TEXT,
	"MolecularInitiatingEvent_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY("KeyEvent_id") REFERENCES "KeyEvent" (id),
	FOREIGN KEY("AdverseOutcomePathway_id") REFERENCES "AdverseOutcomePathway" (id),
	FOREIGN KEY("MolecularInitiatingEvent_id") REFERENCES "MolecularInitiatingEvent" (id)
);CREATE INDEX "ix_KeyEvent_id" ON "KeyEvent" (id);
CREATE TABLE "ImagingProtocol" (
	fluorescent_labeling TEXT,
	fluorescent_tracer TEXT,
	evaporation_prevention TEXT,
	particle_tracking_method TEXT,
	protocol_type TEXT,
	protocol_version TEXT,
	quality_control_criteria TEXT,
	replicate_requirements INTEGER,
	protocol_author TEXT,
	institution TEXT,
	publication_reference TEXT,
	last_updated DATE,
	validation_status TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	imaging_frame_rate_id INTEGER,
	imaging_duration_id INTEGER,
	spatial_resolution_id INTEGER,
	temperature_control_id INTEGER,
	humidity_control_id INTEGER,
	particle_size_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(imaging_frame_rate_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(imaging_duration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(spatial_resolution_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(temperature_control_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(humidity_control_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(particle_size_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_ImagingProtocol_id" ON "ImagingProtocol" (id);
CREATE TABLE "SpirometryProtocol" (
	spirometry_standard TEXT,
	bronchodilator_agent TEXT,
	plethysmography_method TEXT,
	protocol_type TEXT,
	protocol_version TEXT,
	quality_control_criteria TEXT,
	replicate_requirements INTEGER,
	protocol_author TEXT,
	institution TEXT,
	publication_reference TEXT,
	last_updated DATE,
	validation_status TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	bronchodilator_dose_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(bronchodilator_dose_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_SpirometryProtocol_id" ON "SpirometryProtocol" (id);
CREATE TABLE "CellCultureMedium" (
	base_medium TEXT,
	serum_type TEXT,
	manufacturer TEXT,
	catalog_number TEXT,
	lot_number TEXT,
	preparation_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	serum_concentration_id INTEGER,
	osmolality_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(serum_concentration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(osmolality_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_CellCultureMedium_id" ON "CellCultureMedium" (id);
CREATE TABLE "QuantityRange" (
	id INTEGER NOT NULL,
	min_value_id INTEGER,
	max_value_id INTEGER,
	unit_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(min_value_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(max_value_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(unit_id) REFERENCES "Unit" (id)
);CREATE INDEX "ix_QuantityRange_id" ON "QuantityRange" (id);
CREATE TABLE "CiliaryFunctionOutput" (
	ciliary_motion_patterns VARCHAR(11),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	beat_frequency_hz_id INTEGER,
	active_area_percentage_id INTEGER,
	cilia_length_id INTEGER,
	cilia_per_cell_id INTEGER,
	percentage_ciliated_cells_id INTEGER,
	ciliary_beat_amplitude_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(beat_frequency_hz_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(active_area_percentage_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cilia_length_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cilia_per_cell_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(percentage_ciliated_cells_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(ciliary_beat_amplitude_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_CiliaryFunctionOutput_id" ON "CiliaryFunctionOutput" (id);
CREATE TABLE "ASLOutput" (
	ion_composition TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	asl_height_um_id INTEGER,
	periciliary_layer_depth_id INTEGER,
	mucus_layer_thickness_id INTEGER,
	asl_ph_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(asl_height_um_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(periciliary_layer_depth_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(mucus_layer_thickness_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(asl_ph_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_ASLOutput_id" ON "ASLOutput" (id);
CREATE TABLE "MucociliaryClearanceOutput" (
	transport_directionality VARCHAR(8),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	transport_rate_id INTEGER,
	mucus_layer_thickness_id INTEGER,
	percentage_active_transport_id INTEGER,
	particle_clearance_time_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(transport_rate_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(mucus_layer_thickness_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(percentage_active_transport_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(particle_clearance_time_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_MucociliaryClearanceOutput_id" ON "MucociliaryClearanceOutput" (id);
CREATE TABLE "OxidativeStressOutput" (
	antioxidant_enzyme_activities TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	reactive_oxygen_species_id INTEGER,
	lipid_peroxidation_id INTEGER,
	malondialdehyde_level_id INTEGER,
	four_hydroxynonenal_level_id INTEGER,
	eight_isoprostane_level_id INTEGER,
	protein_carbonyl_content_id INTEGER,
	nitrotyrosine_level_id INTEGER,
	dna_damage_markers_id INTEGER,
	eight_ohdg_level_id INTEGER,
	antioxidant_capacity_id INTEGER,
	glutathione_ratio_id INTEGER,
	superoxide_dismutase_activity_id INTEGER,
	catalase_activity_id INTEGER,
	glutathione_peroxidase_activity_id INTEGER,
	total_antioxidant_capacity_id INTEGER,
	nrf2_activation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(reactive_oxygen_species_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(lipid_peroxidation_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(malondialdehyde_level_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(four_hydroxynonenal_level_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(eight_isoprostane_level_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(protein_carbonyl_content_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(nitrotyrosine_level_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dna_damage_markers_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(eight_ohdg_level_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(antioxidant_capacity_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(glutathione_ratio_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(superoxide_dismutase_activity_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(catalase_activity_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(glutathione_peroxidase_activity_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(total_antioxidant_capacity_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(nrf2_activation_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_OxidativeStressOutput_id" ON "OxidativeStressOutput" (id);
CREATE TABLE "CFTRFunctionOutput" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	cftr_chloride_secretion_id INTEGER,
	cftr_forskolin_response_id INTEGER,
	inhibitor_sensitive_current_id INTEGER,
	cftr_specific_current_id INTEGER,
	sweat_chloride_concentration_id INTEGER,
	nasal_potential_difference_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(cftr_chloride_secretion_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cftr_forskolin_response_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(inhibitor_sensitive_current_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cftr_specific_current_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(sweat_chloride_concentration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(nasal_potential_difference_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_CFTRFunctionOutput_id" ON "CFTRFunctionOutput" (id);
CREATE TABLE "EGFRSignalingOutput" (
	downstream_kinase_activation TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	egfr_phosphorylation_y1068_id INTEGER,
	egfr_phosphorylation_y1173_id INTEGER,
	total_egfr_protein_id INTEGER,
	erk_phosphorylation_id INTEGER,
	akt_phosphorylation_id INTEGER,
	egfr_ligand_expression_id INTEGER,
	egfr_membrane_localization_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(egfr_phosphorylation_y1068_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(egfr_phosphorylation_y1173_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(total_egfr_protein_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(erk_phosphorylation_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(akt_phosphorylation_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(egfr_ligand_expression_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(egfr_membrane_localization_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_EGFRSignalingOutput_id" ON "EGFRSignalingOutput" (id);
CREATE TABLE "GobletCellOutput" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	goblet_cell_count_id INTEGER,
	goblet_cell_percentage_id INTEGER,
	muc5ac_mrna_expression_id INTEGER,
	muc5ac_protein_expression_id INTEGER,
	muc5b_mrna_expression_id INTEGER,
	muc5b_protein_expression_id INTEGER,
	muc5ac_muc5b_ratio_id INTEGER,
	mucin_protein_concentration_id INTEGER,
	mucin_secretion_rate_id INTEGER,
	percent_solids_id INTEGER,
	goblet_to_ciliated_ratio_id INTEGER,
	mucus_viscosity_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(goblet_cell_count_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(goblet_cell_percentage_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(muc5ac_mrna_expression_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(muc5ac_protein_expression_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(muc5b_mrna_expression_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(muc5b_protein_expression_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(muc5ac_muc5b_ratio_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(mucin_protein_concentration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(mucin_secretion_rate_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(percent_solids_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(goblet_to_ciliated_ratio_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(mucus_viscosity_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_GobletCellOutput_id" ON "GobletCellOutput" (id);
CREATE TABLE "BALFSputumOutput" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	neutrophil_percentage_id INTEGER,
	eosinophil_percentage_id INTEGER,
	macrophage_percentage_id INTEGER,
	lymphocyte_percentage_id INTEGER,
	total_cell_count_id INTEGER,
	il6_concentration_id INTEGER,
	il8_concentration_id INTEGER,
	tnf_alpha_concentration_id INTEGER,
	il1_beta_concentration_id INTEGER,
	total_protein_concentration_id INTEGER,
	alpha_diversity_id INTEGER,
	beta_diversity_id INTEGER,
	bacterial_load_id INTEGER,
	cell_free_dna_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(neutrophil_percentage_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(eosinophil_percentage_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(macrophage_percentage_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(lymphocyte_percentage_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(total_cell_count_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(il6_concentration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(il8_concentration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(tnf_alpha_concentration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(il1_beta_concentration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(total_protein_concentration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(alpha_diversity_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beta_diversity_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(bacterial_load_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cell_free_dna_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_BALFSputumOutput_id" ON "BALFSputumOutput" (id);
CREATE TABLE "LungFunctionOutput" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	fev1_id INTEGER,
	fvc_id INTEGER,
	fev1_fvc_ratio_id INTEGER,
	feno_id INTEGER,
	decline_rate_id INTEGER,
	bronchodilator_response_id INTEGER,
	dlco_id INTEGER,
	peak_expiratory_flow_id INTEGER,
	fef25_75_id INTEGER,
	total_lung_capacity_id INTEGER,
	functional_residual_capacity_id INTEGER,
	residual_volume_id INTEGER,
	lung_compliance_id INTEGER,
	lung_elastance_id INTEGER,
	lung_resistance_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(fev1_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(fvc_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(fev1_fvc_ratio_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(feno_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(decline_rate_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(bronchodilator_response_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dlco_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(peak_expiratory_flow_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(fef25_75_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(total_lung_capacity_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(functional_residual_capacity_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(residual_volume_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(lung_compliance_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(lung_elastance_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(lung_resistance_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_LungFunctionOutput_id" ON "LungFunctionOutput" (id);
CREATE TABLE "FoxJExpressionOutput" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	foxj1_mrna_expression_id INTEGER,
	foxj1_protein_expression_id INTEGER,
	foxj1_positive_cell_percentage_id INTEGER,
	foxj1_nuclear_localization_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(foxj1_mrna_expression_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(foxj1_protein_expression_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(foxj1_positive_cell_percentage_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(foxj1_nuclear_localization_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_FoxJExpressionOutput_id" ON "FoxJExpressionOutput" (id);
CREATE TABLE "GeneExpressionOutput" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	mrna_level_id INTEGER,
	protein_level_id INTEGER,
	percentage_positive_cells_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(mrna_level_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(protein_level_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(percentage_positive_cells_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_GeneExpressionOutput_id" ON "GeneExpressionOutput" (id);
CREATE TABLE "AdverseOutcomePathway_stressors" (
	"AdverseOutcomePathway_id" TEXT,
	stressors TEXT,
	PRIMARY KEY ("AdverseOutcomePathway_id", stressors),
	FOREIGN KEY("AdverseOutcomePathway_id") REFERENCES "AdverseOutcomePathway" (id)
);CREATE INDEX "ix_AdverseOutcomePathway_stressors_stressors" ON "AdverseOutcomePathway_stressors" (stressors);CREATE INDEX "ix_AdverseOutcomePathway_stressors_AdverseOutcomePathway_id" ON "AdverseOutcomePathway_stressors" ("AdverseOutcomePathway_id");
CREATE TABLE "KeyEventRelationship" (
	relationship_type TEXT,
	evidence_support VARCHAR(13),
	quantitative_understanding VARCHAR(13),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"AdverseOutcomePathway_id" TEXT,
	upstream_event_id TEXT,
	downstream_event_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AdverseOutcomePathway_id") REFERENCES "AdverseOutcomePathway" (id),
	FOREIGN KEY(upstream_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(downstream_event_id) REFERENCES "KeyEvent" (id)
);CREATE INDEX "ix_KeyEventRelationship_id" ON "KeyEventRelationship" (id);
CREATE TABLE "Assay" (
	assay_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	informs_on_key_event_id TEXT,
	study_subject_id TEXT,
	has_specified_output_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(informs_on_key_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(study_subject_id) REFERENCES "StudySubject" (id),
	FOREIGN KEY(has_specified_output_id) REFERENCES "AssayOutputMeasurement" (id)
);CREATE INDEX "ix_Assay_id" ON "Assay" (id);
CREATE TABLE "PopulationSubject" (
	cohort_size INTEGER,
	inclusion_criteria TEXT,
	subject_type TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	age_range_id INTEGER,
	model_species_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(age_range_id) REFERENCES "QuantityRange" (id),
	FOREIGN KEY(model_species_id) REFERENCES "NamedEntity" (id)
);CREATE INDEX "ix_PopulationSubject_id" ON "PopulationSubject" (id);
CREATE TABLE "CellCultureConditions" (
	days_at_air_liquid_interface INTEGER,
	passage_number INTEGER,
	substrate_type VARCHAR(18),
	cell_culture_growth_mode VARCHAR(20),
	donor_count INTEGER,
	replicates_per_donor INTEGER,
	id TEXT NOT NULL,
	name TEXT,
	culture_media_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(culture_media_id) REFERENCES "CellCultureMedium" (id)
);CREATE INDEX "ix_CellCultureConditions_id" ON "CellCultureConditions" (id);
CREATE TABLE "MediumSupplement" (
	supplement_type VARCHAR(22),
	manufacturer TEXT,
	catalog_number TEXT,
	id TEXT NOT NULL,
	name TEXT,
	"CellCultureMedium_id" TEXT,
	concentration_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CellCultureMedium_id") REFERENCES "CellCultureMedium" (id),
	FOREIGN KEY(concentration_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_MediumSupplement_id" ON "MediumSupplement" (id);
CREATE TABLE "CiliaryFunctionAssay" (
	analysis_software TEXT,
	airway_region TEXT,
	assay_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	informs_on_key_event_id TEXT,
	study_subject_id TEXT,
	has_specified_output_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY(informs_on_key_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(study_subject_id) REFERENCES "StudySubject" (id),
	FOREIGN KEY(has_specified_output_id) REFERENCES "CiliaryFunctionOutput" (id)
);CREATE INDEX "ix_CiliaryFunctionAssay_id" ON "CiliaryFunctionAssay" (id);
CREATE TABLE "ASLAssay" (
	assay_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	informs_on_key_event_id TEXT,
	study_subject_id TEXT,
	has_specified_output_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY(informs_on_key_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(study_subject_id) REFERENCES "StudySubject" (id),
	FOREIGN KEY(has_specified_output_id) REFERENCES "ASLOutput" (id)
);CREATE INDEX "ix_ASLAssay_id" ON "ASLAssay" (id);
CREATE TABLE "MucociliaryClearanceAssay" (
	mucus_composition TEXT,
	assay_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	informs_on_key_event_id TEXT,
	study_subject_id TEXT,
	has_specified_output_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY(informs_on_key_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(study_subject_id) REFERENCES "StudySubject" (id),
	FOREIGN KEY(has_specified_output_id) REFERENCES "MucociliaryClearanceOutput" (id)
);CREATE INDEX "ix_MucociliaryClearanceAssay_id" ON "MucociliaryClearanceAssay" (id);
CREATE TABLE "OxidativeStressAssay" (
	ros_probe_type TEXT,
	assay_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	informs_on_key_event_id TEXT,
	study_subject_id TEXT,
	has_specified_output_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY(informs_on_key_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(study_subject_id) REFERENCES "StudySubject" (id),
	FOREIGN KEY(has_specified_output_id) REFERENCES "OxidativeStressOutput" (id)
);CREATE INDEX "ix_OxidativeStressAssay_id" ON "OxidativeStressAssay" (id);
CREATE TABLE "CFTRFunctionAssay" (
	stimulation_agent TEXT,
	inhibitor_used TEXT,
	assay_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	informs_on_key_event_id TEXT,
	study_subject_id TEXT,
	has_specified_output_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY(informs_on_key_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(study_subject_id) REFERENCES "StudySubject" (id),
	FOREIGN KEY(has_specified_output_id) REFERENCES "CFTRFunctionOutput" (id)
);CREATE INDEX "ix_CFTRFunctionAssay_id" ON "CFTRFunctionAssay" (id);
CREATE TABLE "EGFRSignalingAssay" (
	normalization_reference TEXT,
	phosphorylation_site TEXT,
	assay_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	informs_on_key_event_id TEXT,
	study_subject_id TEXT,
	has_specified_output_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY(informs_on_key_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(study_subject_id) REFERENCES "StudySubject" (id),
	FOREIGN KEY(has_specified_output_id) REFERENCES "EGFRSignalingOutput" (id)
);CREATE INDEX "ix_EGFRSignalingAssay_id" ON "EGFRSignalingAssay" (id);
CREATE TABLE "GobletCellAssay" (
	assay_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	informs_on_key_event_id TEXT,
	study_subject_id TEXT,
	has_specified_output_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY(informs_on_key_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(study_subject_id) REFERENCES "StudySubject" (id),
	FOREIGN KEY(has_specified_output_id) REFERENCES "GobletCellOutput" (id)
);CREATE INDEX "ix_GobletCellAssay_id" ON "GobletCellAssay" (id);
CREATE TABLE "FoxJExpressionAssay" (
	assay_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	informs_on_key_event_id TEXT,
	study_subject_id TEXT,
	has_specified_output_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY(informs_on_key_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(study_subject_id) REFERENCES "StudySubject" (id),
	FOREIGN KEY(has_specified_output_id) REFERENCES "FoxJExpressionOutput" (id)
);CREATE INDEX "ix_FoxJExpressionAssay_id" ON "FoxJExpressionAssay" (id);
CREATE TABLE "GeneExpressionAssay" (
	target_gene TEXT,
	gene_expression_method TEXT,
	normalization_reference TEXT,
	assay_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	informs_on_key_event_id TEXT,
	study_subject_id TEXT,
	has_specified_output_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY(informs_on_key_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(study_subject_id) REFERENCES "StudySubject" (id),
	FOREIGN KEY(has_specified_output_id) REFERENCES "GeneExpressionOutput" (id)
);CREATE INDEX "ix_GeneExpressionAssay_id" ON "GeneExpressionAssay" (id);
CREATE TABLE "ImagingProtocol_equipment_required" (
	"ImagingProtocol_id" TEXT,
	equipment_required TEXT,
	PRIMARY KEY ("ImagingProtocol_id", equipment_required),
	FOREIGN KEY("ImagingProtocol_id") REFERENCES "ImagingProtocol" (id)
);CREATE INDEX "ix_ImagingProtocol_equipment_required_ImagingProtocol_id" ON "ImagingProtocol_equipment_required" ("ImagingProtocol_id");CREATE INDEX "ix_ImagingProtocol_equipment_required_equipment_required" ON "ImagingProtocol_equipment_required" (equipment_required);
CREATE TABLE "SpirometryProtocol_equipment_required" (
	"SpirometryProtocol_id" TEXT,
	equipment_required TEXT,
	PRIMARY KEY ("SpirometryProtocol_id", equipment_required),
	FOREIGN KEY("SpirometryProtocol_id") REFERENCES "SpirometryProtocol" (id)
);CREATE INDEX "ix_SpirometryProtocol_equipment_required_SpirometryProtocol_id" ON "SpirometryProtocol_equipment_required" ("SpirometryProtocol_id");CREATE INDEX "ix_SpirometryProtocol_equipment_required_equipment_required" ON "SpirometryProtocol_equipment_required" (equipment_required);
CREATE TABLE "CiliaryFunctionOutput_cell_type_ratios" (
	"CiliaryFunctionOutput_id" TEXT,
	cell_type_ratios TEXT,
	PRIMARY KEY ("CiliaryFunctionOutput_id", cell_type_ratios),
	FOREIGN KEY("CiliaryFunctionOutput_id") REFERENCES "CiliaryFunctionOutput" (id)
);CREATE INDEX "ix_CiliaryFunctionOutput_cell_type_ratios_CiliaryFunctionOutput_id" ON "CiliaryFunctionOutput_cell_type_ratios" ("CiliaryFunctionOutput_id");CREATE INDEX "ix_CiliaryFunctionOutput_cell_type_ratios_cell_type_ratios" ON "CiliaryFunctionOutput_cell_type_ratios" (cell_type_ratios);
CREATE TABLE "OxidativeStressOutput_protein_oxidation_markers" (
	"OxidativeStressOutput_id" TEXT,
	protein_oxidation_markers TEXT,
	PRIMARY KEY ("OxidativeStressOutput_id", protein_oxidation_markers),
	FOREIGN KEY("OxidativeStressOutput_id") REFERENCES "OxidativeStressOutput" (id)
);CREATE INDEX "ix_OxidativeStressOutput_protein_oxidation_markers_OxidativeStressOutput_id" ON "OxidativeStressOutput_protein_oxidation_markers" ("OxidativeStressOutput_id");CREATE INDEX "ix_OxidativeStressOutput_protein_oxidation_markers_protein_oxidation_markers" ON "OxidativeStressOutput_protein_oxidation_markers" (protein_oxidation_markers);
CREATE TABLE "EGFRSignalingOutput_pathway_biomarkers" (
	"EGFRSignalingOutput_id" TEXT,
	pathway_biomarkers TEXT,
	PRIMARY KEY ("EGFRSignalingOutput_id", pathway_biomarkers),
	FOREIGN KEY("EGFRSignalingOutput_id") REFERENCES "EGFRSignalingOutput" (id)
);CREATE INDEX "ix_EGFRSignalingOutput_pathway_biomarkers_EGFRSignalingOutput_id" ON "EGFRSignalingOutput_pathway_biomarkers" ("EGFRSignalingOutput_id");CREATE INDEX "ix_EGFRSignalingOutput_pathway_biomarkers_pathway_biomarkers" ON "EGFRSignalingOutput_pathway_biomarkers" (pathway_biomarkers);
CREATE TABLE "InVivoSubject" (
	sex TEXT,
	subject_characteristics TEXT,
	disease_state TEXT,
	sample_type VARCHAR(25),
	collection_site TEXT,
	collection_date DATE,
	sample_collection_method TEXT,
	clinical_context TEXT,
	subject_type TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"PopulationSubject_id" TEXT,
	age_id INTEGER,
	model_species_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PopulationSubject_id") REFERENCES "PopulationSubject" (id),
	FOREIGN KEY(age_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(model_species_id) REFERENCES "NamedEntity" (id)
);CREATE INDEX "ix_InVivoSubject_id" ON "InVivoSubject" (id);
CREATE TABLE "CellularSystem" (
	cell_culture_growth_mode VARCHAR(20),
	substrate_type VARCHAR(18),
	passage_number INTEGER,
	coating TEXT,
	matrix_composition TEXT,
	organoid_type TEXT,
	days_at_differentiation INTEGER,
	donor_info TEXT,
	replicates_per_donor INTEGER,
	subject_type TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	cell_line_id TEXT,
	primary_cell_id TEXT,
	cell_type_id TEXT,
	anatomical_origin_id TEXT,
	confluence_level_id INTEGER,
	seeding_density_id INTEGER,
	size_range_id INTEGER,
	culture_conditions_id TEXT,
	culture_media_id TEXT,
	model_species_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(cell_line_id) REFERENCES "CellLine" (id),
	FOREIGN KEY(primary_cell_id) REFERENCES "NamedEntity" (id),
	FOREIGN KEY(cell_type_id) REFERENCES "NamedEntity" (id),
	FOREIGN KEY(anatomical_origin_id) REFERENCES "NamedEntity" (id),
	FOREIGN KEY(confluence_level_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(seeding_density_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(size_range_id) REFERENCES "QuantityRange" (id),
	FOREIGN KEY(culture_conditions_id) REFERENCES "CellCultureConditions" (id),
	FOREIGN KEY(culture_media_id) REFERENCES "CellCultureMedium" (id),
	FOREIGN KEY(model_species_id) REFERENCES "NamedEntity" (id)
);CREATE INDEX "ix_CellularSystem_id" ON "CellularSystem" (id);
CREATE TABLE "BALFSputumAssay" (
	assay_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	target_cell_type_id TEXT,
	informs_on_key_event_id TEXT,
	study_subject_id TEXT,
	has_specified_output_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY(target_cell_type_id) REFERENCES "NamedEntity" (id),
	FOREIGN KEY(informs_on_key_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(study_subject_id) REFERENCES "InVivoSubject" (id),
	FOREIGN KEY(has_specified_output_id) REFERENCES "BALFSputumOutput" (id)
);CREATE INDEX "ix_BALFSputumAssay_id" ON "BALFSputumAssay" (id);
CREATE TABLE "LungFunctionAssay" (
	reference_dataset TEXT,
	recent_respiratory_illness TEXT,
	assay_date DATE,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	hemoglobin_level_id INTEGER,
	informs_on_key_event_id TEXT,
	study_subject_id TEXT,
	has_specified_output_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY(hemoglobin_level_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(informs_on_key_event_id) REFERENCES "KeyEvent" (id),
	FOREIGN KEY(study_subject_id) REFERENCES "InVivoSubject" (id),
	FOREIGN KEY(has_specified_output_id) REFERENCES "LungFunctionOutput" (id)
);CREATE INDEX "ix_LungFunctionAssay_id" ON "LungFunctionAssay" (id);
CREATE TABLE "CellularSystem_cell_type_ratios" (
	"CellularSystem_id" TEXT,
	cell_type_ratios TEXT,
	PRIMARY KEY ("CellularSystem_id", cell_type_ratios),
	FOREIGN KEY("CellularSystem_id") REFERENCES "CellularSystem" (id)
);CREATE INDEX "ix_CellularSystem_cell_type_ratios_CellularSystem_id" ON "CellularSystem_cell_type_ratios" ("CellularSystem_id");CREATE INDEX "ix_CellularSystem_cell_type_ratios_cell_type_ratios" ON "CellularSystem_cell_type_ratios" (cell_type_ratios);
CREATE TABLE "Protocol" (
	protocol_type TEXT,
	protocol_version TEXT,
	quality_control_criteria TEXT,
	replicate_requirements INTEGER,
	protocol_author TEXT,
	institution TEXT,
	publication_reference TEXT,
	last_updated DATE,
	validation_status TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"Container_id" INTEGER,
	"Assay_id" TEXT,
	"Protocol_id" TEXT,
	"ImagingProtocol_id" TEXT,
	"StainingProtocol_id" TEXT,
	"SpirometryProtocol_id" TEXT,
	"MolecularAssayProtocol_id" TEXT,
	"CiliaryFunctionAssay_id" TEXT,
	"ASLAssay_id" TEXT,
	"MucociliaryClearanceAssay_id" TEXT,
	"OxidativeStressAssay_id" TEXT,
	"CFTRFunctionAssay_id" TEXT,
	"EGFRSignalingAssay_id" TEXT,
	"GobletCellAssay_id" TEXT,
	"BALFSputumAssay_id" TEXT,
	"LungFunctionAssay_id" TEXT,
	"FoxJExpressionAssay_id" TEXT,
	"GeneExpressionAssay_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Container_id") REFERENCES "Container" (id),
	FOREIGN KEY("Assay_id") REFERENCES "Assay" (id),
	FOREIGN KEY("Protocol_id") REFERENCES "Protocol" (id),
	FOREIGN KEY("ImagingProtocol_id") REFERENCES "ImagingProtocol" (id),
	FOREIGN KEY("StainingProtocol_id") REFERENCES "StainingProtocol" (id),
	FOREIGN KEY("SpirometryProtocol_id") REFERENCES "SpirometryProtocol" (id),
	FOREIGN KEY("MolecularAssayProtocol_id") REFERENCES "MolecularAssayProtocol" (id),
	FOREIGN KEY("CiliaryFunctionAssay_id") REFERENCES "CiliaryFunctionAssay" (id),
	FOREIGN KEY("ASLAssay_id") REFERENCES "ASLAssay" (id),
	FOREIGN KEY("MucociliaryClearanceAssay_id") REFERENCES "MucociliaryClearanceAssay" (id),
	FOREIGN KEY("OxidativeStressAssay_id") REFERENCES "OxidativeStressAssay" (id),
	FOREIGN KEY("CFTRFunctionAssay_id") REFERENCES "CFTRFunctionAssay" (id),
	FOREIGN KEY("EGFRSignalingAssay_id") REFERENCES "EGFRSignalingAssay" (id),
	FOREIGN KEY("GobletCellAssay_id") REFERENCES "GobletCellAssay" (id),
	FOREIGN KEY("BALFSputumAssay_id") REFERENCES "BALFSputumAssay" (id),
	FOREIGN KEY("LungFunctionAssay_id") REFERENCES "LungFunctionAssay" (id),
	FOREIGN KEY("FoxJExpressionAssay_id") REFERENCES "FoxJExpressionAssay" (id),
	FOREIGN KEY("GeneExpressionAssay_id") REFERENCES "GeneExpressionAssay" (id)
);CREATE INDEX "ix_Protocol_id" ON "Protocol" (id);
CREATE TABLE "ExposureCondition" (
	id TEXT NOT NULL,
	name TEXT,
	"Assay_id" TEXT,
	"CiliaryFunctionAssay_id" TEXT,
	"ASLAssay_id" TEXT,
	"MucociliaryClearanceAssay_id" TEXT,
	"OxidativeStressAssay_id" TEXT,
	"CFTRFunctionAssay_id" TEXT,
	"EGFRSignalingAssay_id" TEXT,
	"GobletCellAssay_id" TEXT,
	"BALFSputumAssay_id" TEXT,
	"LungFunctionAssay_id" TEXT,
	"FoxJExpressionAssay_id" TEXT,
	"GeneExpressionAssay_id" TEXT,
	exposure_agent_id TEXT,
	exposure_concentration_id INTEGER,
	exposure_duration_id INTEGER,
	timing_post_exposure_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Assay_id") REFERENCES "Assay" (id),
	FOREIGN KEY("CiliaryFunctionAssay_id") REFERENCES "CiliaryFunctionAssay" (id),
	FOREIGN KEY("ASLAssay_id") REFERENCES "ASLAssay" (id),
	FOREIGN KEY("MucociliaryClearanceAssay_id") REFERENCES "MucociliaryClearanceAssay" (id),
	FOREIGN KEY("OxidativeStressAssay_id") REFERENCES "OxidativeStressAssay" (id),
	FOREIGN KEY("CFTRFunctionAssay_id") REFERENCES "CFTRFunctionAssay" (id),
	FOREIGN KEY("EGFRSignalingAssay_id") REFERENCES "EGFRSignalingAssay" (id),
	FOREIGN KEY("GobletCellAssay_id") REFERENCES "GobletCellAssay" (id),
	FOREIGN KEY("BALFSputumAssay_id") REFERENCES "BALFSputumAssay" (id),
	FOREIGN KEY("LungFunctionAssay_id") REFERENCES "LungFunctionAssay" (id),
	FOREIGN KEY("FoxJExpressionAssay_id") REFERENCES "FoxJExpressionAssay" (id),
	FOREIGN KEY("GeneExpressionAssay_id") REFERENCES "GeneExpressionAssay" (id),
	FOREIGN KEY(exposure_agent_id) REFERENCES "NamedEntity" (id),
	FOREIGN KEY(exposure_concentration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(exposure_duration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(timing_post_exposure_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_ExposureCondition_id" ON "ExposureCondition" (id);
CREATE TABLE "Protocol_equipment_required" (
	"Protocol_id" TEXT,
	equipment_required TEXT,
	PRIMARY KEY ("Protocol_id", equipment_required),
	FOREIGN KEY("Protocol_id") REFERENCES "Protocol" (id)
);CREATE INDEX "ix_Protocol_equipment_required_equipment_required" ON "Protocol_equipment_required" (equipment_required);CREATE INDEX "ix_Protocol_equipment_required_Protocol_id" ON "Protocol_equipment_required" ("Protocol_id");
