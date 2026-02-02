from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'outcomes_working_group',
     'default_range': 'string',
     'description': 'A LinkML data model for representing biological measurements, '
                    'assays, and experimental protocols in the context of outcomes '
                    'research. This is the main entry point that imports the '
                    'measurement base schema and domain-specific microschemas.',
     'id': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
     'imports': ['linkml:types', 'measurement_base', 'measurement_microschemas'],
     'license': 'MIT',
     'name': 'outcomes_working_group',
     'prefixes': {'CHEBI': {'prefix_prefix': 'CHEBI',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CL_'},
                  'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'UO': {'prefix_prefix': 'UO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/UO_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'measurement_base': {'prefix_prefix': 'measurement_base',
                                       'prefix_reference': 'https://w3id.org/EHS-Data-Standards/measurement_base/'},
                  'measurement_microschemas': {'prefix_prefix': 'measurement_microschemas',
                                               'prefix_reference': 'https://w3id.org/EHS-Data-Standards/measurement_microschemas/'},
                  'outcomes_working_group': {'prefix_prefix': 'outcomes_working_group',
                                             'prefix_reference': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://EHS-Data-Standards.github.io/outcomes-working-group'],
     'source_file': 'src/outcomes_working_group/schema/outcomes_working_group.yaml',
     'title': 'Outcomes Working Group Schema'} )

class StudyContextEnum(str, Enum):
    """
    The experimental context for a protocol or measurement.
    """
    in_vitro = "in_vitro"
    """
    Performed on cultured cells or tissues
    """
    in_vivo = "in_vivo"
    """
    Performed on living human or animal subjects
    """
    ex_vivo = "ex_vivo"
    """
    Performed on tissue removed from an organism
    """


class SampleTypeEnum(str, Enum):
    """
    Types of biological samples for in vivo measurements.
    """
    urine = "urine"
    """
    Urine sample
    """
    blood = "blood"
    """
    Blood sample (whole blood, serum, or plasma)
    """
    sputum = "sputum"
    """
    Induced or spontaneous sputum
    """
    balf = "balf"
    """
    Bronchoalveolar lavage fluid
    """
    nasal_epithelium = "nasal_epithelium"
    """
    Nasal epithelial sample
    """
    bronchial_epithelium = "bronchial_epithelium"
    """
    Bronchial epithelial sample
    """
    exhaled_breath_condensate = "exhaled_breath_condensate"
    """
    Exhaled breath condensate (EBC)
    """
    biopsy = "biopsy"
    """
    Tissue biopsy
    """
    sweat = "sweat"
    """
    Sweat sample (e.g., for sweat chloride test)
    """


class CiliaryFunctionObservationTypeEnum(str, Enum):
    """
    Observation types for ciliary function measurements.
    """
    ciliary_beat_frequency = "ciliary_beat_frequency"
    """
    Ciliary beat frequency (Hz)
    """
    ciliary_active_area_percentage = "ciliary_active_area_percentage"
    """
    Percentage of epithelial surface with actively beating cilia
    """
    cilia_length = "cilia_length"
    """
    Length of cilia (μm)
    """
    cilia_per_cell = "cilia_per_cell"
    """
    Number of cilia per cell
    """
    percentage_ciliated_cells = "percentage_ciliated_cells"
    """
    Percentage of cells that are ciliated
    """
    ciliary_motion_pattern = "ciliary_motion_pattern"
    """
    Pattern of ciliary motion (coordinated, dyskinetic, immotile)
    """
    ciliary_beat_amplitude = "ciliary_beat_amplitude"
    """
    Amplitude of ciliary beat stroke
    """


class ASLObservationTypeEnum(str, Enum):
    """
    Observation types for airway surface liquid measurements.
    """
    asl_height = "asl_height"
    """
    Airway surface liquid height/depth (μm)
    """
    periciliary_layer_depth = "periciliary_layer_depth"
    """
    Periciliary layer (PCL) depth (μm)
    """
    mucus_layer_thickness = "mucus_layer_thickness"
    """
    Thickness of the mucus gel layer (μm)
    """
    asl_chloride_concentration = "asl_chloride_concentration"
    """
    Chloride ion concentration in ASL
    """
    asl_sodium_concentration = "asl_sodium_concentration"
    """
    Sodium ion concentration in ASL
    """
    asl_potassium_concentration = "asl_potassium_concentration"
    """
    Potassium ion concentration in ASL
    """
    asl_ph = "asl_ph"
    """
    pH of airway surface liquid
    """


class MCCObservationTypeEnum(str, Enum):
    """
    Observation types for mucociliary clearance measurements.
    """
    mucociliary_transport_rate = "mucociliary_transport_rate"
    """
    Rate of mucus/particle transport (mm/min or μm/s)
    """
    transport_directionality = "transport_directionality"
    """
    Directionality of mucociliary transport
    """
    percentage_active_transport = "percentage_active_transport"
    """
    Percentage of surface with active mucociliary transport
    """
    particle_clearance_time = "particle_clearance_time"
    """
    Time to clear particles from a defined region
    """
    biofilm_clearance_rate = "biofilm_clearance_rate"
    """
    Rate of bacterial biofilm clearance
    """
    bacterial_load = "bacterial_load"
    """
    Bacterial load remaining after clearance (CFU)
    """


class OxidativeStressObservationTypeEnum(str, Enum):
    """
    Observation types for oxidative stress measurements.
    """
    reactive_oxygen_species = "reactive_oxygen_species"
    """
    Reactive oxygen species level (fluorescence intensity or fold change)
    """
    malondialdehyde = "malondialdehyde"
    """
    Malondialdehyde (MDA) level - lipid peroxidation marker
    """
    four_hydroxynonenal = "four_hydroxynonenal"
    """
    4-Hydroxynonenal (4-HNE) level - lipid peroxidation marker
    """
    eight_isoprostane = "eight_isoprostane"
    """
    8-Isoprostane level - lipid peroxidation marker
    """
    protein_carbonyl = "protein_carbonyl"
    """
    Protein carbonyl content - protein oxidation marker
    """
    nitrotyrosine = "nitrotyrosine"
    """
    Nitrotyrosine level - protein nitration marker
    """
    eight_ohdg = "eight_ohdg"
    """
    8-OHdG level - DNA oxidation marker
    """
    glutathione_ratio = "glutathione_ratio"
    """
    GSH/GSSG ratio - antioxidant capacity
    """
    superoxide_dismutase_activity = "superoxide_dismutase_activity"
    """
    Superoxide dismutase (SOD) enzyme activity
    """
    catalase_activity = "catalase_activity"
    """
    Catalase enzyme activity
    """
    glutathione_peroxidase_activity = "glutathione_peroxidase_activity"
    """
    Glutathione peroxidase (GPx) enzyme activity
    """
    total_antioxidant_capacity = "total_antioxidant_capacity"
    """
    Total antioxidant capacity of sample
    """
    nrf2_activation = "nrf2_activation"
    """
    NRF2 pathway activation level
    """


class CFTRObservationTypeEnum(str, Enum):
    """
    Observation types for CFTR function measurements.
    """
    cftr_chloride_secretion = "cftr_chloride_secretion"
    """
    CFTR-mediated chloride secretory current (μA/cm²)
    """
    cftr_forskolin_response = "cftr_forskolin_response"
    """
    CFTR response to forskolin stimulation
    """
    cftr_inhibitor_sensitive_current = "cftr_inhibitor_sensitive_current"
    """
    CFTRinh-172 sensitive current
    """
    sweat_chloride_concentration = "sweat_chloride_concentration"
    """
    Sweat chloride concentration (mEq/L) - CF diagnostic
    """
    nasal_potential_difference = "nasal_potential_difference"
    """
    Nasal potential difference measurement
    """


class EGFRObservationTypeEnum(str, Enum):
    """
    Observation types for EGFR signaling measurements.
    """
    egfr_phosphorylation = "egfr_phosphorylation"
    """
    EGFR phosphorylation level (specify site, e.g., Y1068, Y1173)
    """
    egfr_total_protein = "egfr_total_protein"
    """
    Total EGFR protein expression
    """
    erk_phosphorylation = "erk_phosphorylation"
    """
    ERK1/2 phosphorylation (downstream kinase)
    """
    akt_phosphorylation = "akt_phosphorylation"
    """
    AKT phosphorylation (downstream kinase)
    """
    egfr_ligand_expression = "egfr_ligand_expression"
    """
    EGFR ligand expression (EGF, TGF-α, amphiregulin)
    """
    egfr_membrane_localization = "egfr_membrane_localization"
    """
    EGFR membrane localization
    """


class GobletCellMucinObservationTypeEnum(str, Enum):
    """
    Observation types for goblet cell and mucin measurements.
    """
    goblet_cell_count = "goblet_cell_count"
    """
    Number or percentage of goblet cells
    """
    goblet_to_ciliated_ratio = "goblet_to_ciliated_ratio"
    """
    Ratio of goblet cells to ciliated cells
    """
    muc5ac_expression = "muc5ac_expression"
    """
    MUC5AC gene or protein expression
    """
    muc5b_expression = "muc5b_expression"
    """
    MUC5B gene or protein expression
    """
    muc5ac_muc5b_ratio = "muc5ac_muc5b_ratio"
    """
    Ratio of MUC5AC to MUC5B expression
    """
    mucin_protein_concentration = "mucin_protein_concentration"
    """
    Total mucin protein concentration
    """
    mucin_secretion_rate = "mucin_secretion_rate"
    """
    Rate of mucin secretion
    """
    mucus_viscosity = "mucus_viscosity"
    """
    Viscosity of airway mucus
    """
    percent_solids = "percent_solids"
    """
    Percent solids in mucus/secretions
    """


class BALFSputumObservationTypeEnum(str, Enum):
    """
    Observation types for BALF and sputum measurements.
    """
    neutrophil_percentage = "neutrophil_percentage"
    """
    Percentage of neutrophils in differential cell count
    """
    eosinophil_percentage = "eosinophil_percentage"
    """
    Percentage of eosinophils in differential cell count
    """
    macrophage_percentage = "macrophage_percentage"
    """
    Percentage of macrophages in differential cell count
    """
    lymphocyte_percentage = "lymphocyte_percentage"
    """
    Percentage of lymphocytes in differential cell count
    """
    total_cell_count = "total_cell_count"
    """
    Total cell count in sample
    """
    il6_concentration = "il6_concentration"
    """
    IL-6 cytokine concentration
    """
    il8_concentration = "il8_concentration"
    """
    IL-8 (CXCL8) cytokine concentration
    """
    tnf_alpha_concentration = "tnf_alpha_concentration"
    """
    TNF-α cytokine concentration
    """
    il1_beta_concentration = "il1_beta_concentration"
    """
    IL-1β cytokine concentration
    """
    total_protein_concentration = "total_protein_concentration"
    """
    Total protein concentration
    """
    alpha_diversity = "alpha_diversity"
    """
    Microbiome alpha diversity metric
    """
    beta_diversity = "beta_diversity"
    """
    Microbiome beta diversity metric
    """
    bacterial_load = "bacterial_load"
    """
    Total bacterial load (16S copies or CFU)
    """


class LungFunctionObservationTypeEnum(str, Enum):
    """
    Observation types for lung function measurements.
    """
    fev1 = "fev1"
    """
    Forced expiratory volume in 1 second (L or % predicted)
    """
    fvc = "fvc"
    """
    Forced vital capacity (L or % predicted)
    """
    fev1_fvc_ratio = "fev1_fvc_ratio"
    """
    Ratio of FEV1 to FVC
    """
    fef25_75 = "fef25_75"
    """
    Forced expiratory flow at 25-75% of FVC
    """
    pef = "pef"
    """
    Peak expiratory flow
    """
    dlco = "dlco"
    """
    Diffusing capacity for carbon monoxide
    """
    feno = "feno"
    """
    Fractional exhaled nitric oxide (ppb)
    """
    bronchodilator_response = "bronchodilator_response"
    """
    Change in FEV1 after bronchodilator administration
    """
    lung_function_decline_rate = "lung_function_decline_rate"
    """
    Rate of FEV1 decline over time (mL/year)
    """


class FoxJObservationTypeEnum(str, Enum):
    """
    Observation types for FoxJ1 and ciliogenesis measurements.
    """
    foxj1_mrna_expression = "foxj1_mrna_expression"
    """
    FoxJ1 mRNA expression level
    """
    foxj1_protein_expression = "foxj1_protein_expression"
    """
    FoxJ1 protein expression level
    """
    foxj1_positive_cell_percentage = "foxj1_positive_cell_percentage"
    """
    Percentage of FoxJ1-positive cells
    """
    foxj1_nuclear_localization = "foxj1_nuclear_localization"
    """
    FoxJ1 nuclear localization
    """


class ExposureBiomarkerObservationTypeEnum(str, Enum):
    """
    Observation types for exposure biomarker measurements.
    """
    urinary_cotinine = "urinary_cotinine"
    """
    Urinary cotinine level (tobacco smoke biomarker)
    """
    serum_cotinine = "serum_cotinine"
    """
    Serum cotinine level
    """
    urinary_1_hydroxypyrene = "urinary_1_hydroxypyrene"
    """
    Urinary 1-hydroxypyrene (PAH biomarker)
    """
    blood_lead = "blood_lead"
    """
    Blood lead concentration
    """
    urinary_arsenic = "urinary_arsenic"
    """
    Urinary arsenic species
    """
    urinary_cadmium = "urinary_cadmium"
    """
    Urinary cadmium concentration
    """
    exhaled_co = "exhaled_co"
    """
    Exhaled carbon monoxide (smoking biomarker)
    """



class Measurement(ConfiguredBaseModel):
    """
    The result of applying an assay to a specific sample at a specific time, producing a value (or values). This is the interface that domain-specific measurement microschemas implement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_base',
         'mixin': True})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    observation_type: Optional[str] = Field(default=None, description="""The type of observation being measured. Constrained by domain-specific enums in microschemas (e.g., CiliaryObservationTypeEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measured_entity: Optional[NamedEntity] = Field(default=None, description="""The biological or chemical entity being measured (e.g., Cilium, CFTR, ROS). Reference to an ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Brief description of the method used to obtain the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date when the measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    uses: Optional[Assay] = Field(default=None, description="""The Assay used to produce this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })


class Assay(ConfiguredBaseModel):
    """
    A test or experiment used to measure a specific biological or chemical activity; assays generate data on how a substance affects cells, tissues, or systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0000070',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_base'})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })


class Method(ConfiguredBaseModel):
    """
    A general approach or technique used to collect, measure, or analyze data (e.g., qPCR, RNA-Seq, high-speed video microscopy, ELISA).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_base'})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    implements: Optional[Assay] = Field(default=None, description="""The Assay that this Method implements or realizes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })


class Protocol(ConfiguredBaseModel):
    """
    A detailed set of steps for how to perform a test or collect data; protocols ensure consistency across laboratories or studies when generating exposure or biological data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0000272',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_base'})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    specified_by: Optional[Method] = Field(default=None, description="""The Method that this Protocol specifies in detail.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    follows: Optional[Assay] = Field(default=None, description="""The Assay that this Protocol provides detailed steps for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    study_context: Optional[StudyContextEnum] = Field(default=None, description="""The experimental context for this protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    imaging_frame_rate: Optional[QuantityValue] = Field(default=None, description="""Frame rate for video/imaging acquisition (e.g., 200 fps).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    imaging_duration: Optional[QuantityValue] = Field(default=None, description="""Duration of imaging session.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    spatial_resolution: Optional[QuantityValue] = Field(default=None, description="""Spatial resolution of imaging (e.g., 1-2 μm axial resolution).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    temperature_control: Optional[QuantityValue] = Field(default=None, description="""Temperature conditions during the procedure (e.g., 37°C).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    humidity_control: Optional[QuantityValue] = Field(default=None, description="""Humidity conditions during the procedure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    evaporation_control: Optional[str] = Field(default=None, description="""Method used to prevent evaporation (e.g., perfluorocarbon overlay, oil).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    detection_method: Optional[str] = Field(default=None, description="""Detection method used (e.g., flow cytometry, plate reader, microscopy).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    staining_type: Optional[str] = Field(default=None, description="""Type of staining used (e.g., immunofluorescence, histological, AB-PAS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    antibody_used: Optional[list[str]] = Field(default=[], description="""Antibodies used in staining or detection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    probe_type: Optional[str] = Field(default=None, description="""Type of probe used (e.g., DCFDA for ROS, Texas Red-dextran for ASL).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    normalization_method: Optional[str] = Field(default=None, description="""Method used for data normalization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    replicate_count: Optional[int] = Field(default=None, description="""Number of technical replicates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    quality_control_criteria: Optional[str] = Field(default=None, description="""Quality control acceptance criteria for the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })


class InVitroContext(ConfiguredBaseModel):
    """
    Context slots for in vitro measurements using cell culture systems. Mix this into microschemas that can be performed on cultured cells.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_base',
         'mixin': True})

    cell_culture_system: Optional[str] = Field(default=None, description="""Type of cell culture system (e.g., ALI, organoid, 2D monolayer, MucilAir, EpiAirway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    days_at_differentiation: Optional[int] = Field(default=None, description="""Days at air-liquid interface or differentiation stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    passage_number: Optional[int] = Field(default=None, description="""Cell passage number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    substrate_type: Optional[str] = Field(default=None, description="""Type of culture substrate (e.g., transwell, collagen-coated, Matrigel).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    donor_info: Optional[str] = Field(default=None, description="""Information about cell donor (e.g., healthy non-smoker, CF patient, age, anatomical region).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of replicate cultures per donor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    culture_medium: Optional[str] = Field(default=None, description="""Culture medium formulation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })


class InVivoContext(ConfiguredBaseModel):
    """
    Context slots for in vivo measurements from human or animal subjects. Mix this into microschemas that can be performed on living subjects.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_base',
         'mixin': True})

    participant: Optional[NamedEntity] = Field(default=None, description="""The study participant from whom the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample (e.g., urine, blood, sputum, nasal epithelium, exhaled breath condensate).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_site: Optional[str] = Field(default=None, description="""Anatomical site of sample collection (e.g., inferior turbinate, bronchus).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_date: Optional[date] = Field(default=None, description="""Date when the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    subject_characteristics: Optional[str] = Field(default=None, description="""Relevant subject characteristics (e.g., age, sex, disease state, medication use, smoking status).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })


class QuantityValue(ConfiguredBaseModel):
    """
    A quantity with a numeric value and unit of measurement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_base'})

    value: Optional[str] = Field(default=None, description="""The numeric value of the quantity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })
    unit: Optional[Unit] = Field(default=None, description="""The unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })


class Unit(ConfiguredBaseModel):
    """
    A unit of measurement from a standard ontology (UO, UCUM, QUDT).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_base',
         'id_prefixes': ['UO', 'UCUM', 'QUDT']})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })


class NamedEntity(ConfiguredBaseModel):
    """
    A reference to an entity with an identifier and name. Used for measured_entity, participant, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_base'})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })


class CiliaryFunctionMeasurement(InVivoContext, InVitroContext, Measurement):
    """
    Measurement of ciliary function including beat frequency, active area, cilia morphology, and ciliated cell populations. Can be performed in vitro on ALI cultures or in vivo via intranasal imaging (e.g., μOCT).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_microschemas',
         'implements': ['measurement_base:Measurement'],
         'mixins': ['Measurement', 'InVitroContext', 'InVivoContext'],
         'slot_usage': {'observation_type': {'name': 'observation_type',
                                             'range': 'CiliaryFunctionObservationTypeEnum'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    observation_type: Optional[CiliaryFunctionObservationTypeEnum] = Field(default=None, description="""The type of observation being measured. Constrained by domain-specific enums in microschemas (e.g., CiliaryObservationTypeEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measured_entity: Optional[NamedEntity] = Field(default=None, description="""The biological or chemical entity being measured (e.g., Cilium, CFTR, ROS). Reference to an ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Brief description of the method used to obtain the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date when the measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    uses: Optional[Assay] = Field(default=None, description="""The Assay used to produce this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    cell_culture_system: Optional[str] = Field(default=None, description="""Type of cell culture system (e.g., ALI, organoid, 2D monolayer, MucilAir, EpiAirway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    days_at_differentiation: Optional[int] = Field(default=None, description="""Days at air-liquid interface or differentiation stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    passage_number: Optional[int] = Field(default=None, description="""Cell passage number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    substrate_type: Optional[str] = Field(default=None, description="""Type of culture substrate (e.g., transwell, collagen-coated, Matrigel).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    donor_info: Optional[str] = Field(default=None, description="""Information about cell donor (e.g., healthy non-smoker, CF patient, age, anatomical region).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of replicate cultures per donor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    culture_medium: Optional[str] = Field(default=None, description="""Culture medium formulation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    participant: Optional[NamedEntity] = Field(default=None, description="""The study participant from whom the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample (e.g., urine, blood, sputum, nasal epithelium, exhaled breath condensate).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_site: Optional[str] = Field(default=None, description="""Anatomical site of sample collection (e.g., inferior turbinate, bronchus).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_date: Optional[date] = Field(default=None, description="""Date when the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    subject_characteristics: Optional[str] = Field(default=None, description="""Relevant subject characteristics (e.g., age, sex, disease state, medication use, smoking status).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })


class ASLMeasurement(InVivoContext, InVitroContext, Measurement):
    """
    Measurement of airway surface liquid properties including ASL height, periciliary layer depth, and ion composition. Critical for assessing airway hydration status in CF and other mucociliary disorders.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_microschemas',
         'implements': ['measurement_base:Measurement'],
         'mixins': ['Measurement', 'InVitroContext', 'InVivoContext'],
         'slot_usage': {'observation_type': {'name': 'observation_type',
                                             'range': 'ASLObservationTypeEnum'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    observation_type: Optional[ASLObservationTypeEnum] = Field(default=None, description="""The type of observation being measured. Constrained by domain-specific enums in microschemas (e.g., CiliaryObservationTypeEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measured_entity: Optional[NamedEntity] = Field(default=None, description="""The biological or chemical entity being measured (e.g., Cilium, CFTR, ROS). Reference to an ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Brief description of the method used to obtain the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date when the measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    uses: Optional[Assay] = Field(default=None, description="""The Assay used to produce this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    cell_culture_system: Optional[str] = Field(default=None, description="""Type of cell culture system (e.g., ALI, organoid, 2D monolayer, MucilAir, EpiAirway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    days_at_differentiation: Optional[int] = Field(default=None, description="""Days at air-liquid interface or differentiation stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    passage_number: Optional[int] = Field(default=None, description="""Cell passage number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    substrate_type: Optional[str] = Field(default=None, description="""Type of culture substrate (e.g., transwell, collagen-coated, Matrigel).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    donor_info: Optional[str] = Field(default=None, description="""Information about cell donor (e.g., healthy non-smoker, CF patient, age, anatomical region).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of replicate cultures per donor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    culture_medium: Optional[str] = Field(default=None, description="""Culture medium formulation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    participant: Optional[NamedEntity] = Field(default=None, description="""The study participant from whom the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample (e.g., urine, blood, sputum, nasal epithelium, exhaled breath condensate).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_site: Optional[str] = Field(default=None, description="""Anatomical site of sample collection (e.g., inferior turbinate, bronchus).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_date: Optional[date] = Field(default=None, description="""Date when the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    subject_characteristics: Optional[str] = Field(default=None, description="""Relevant subject characteristics (e.g., age, sex, disease state, medication use, smoking status).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })


class MCCMeasurement(InVivoContext, InVitroContext, Measurement):
    """
    Measurement of mucociliary clearance and transport including mucus transport rate, directionality, and clearance efficiency. Assesses the coordinated function of cilia and mucus for pathogen clearance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_microschemas',
         'implements': ['measurement_base:Measurement'],
         'mixins': ['Measurement', 'InVitroContext', 'InVivoContext'],
         'slot_usage': {'observation_type': {'name': 'observation_type',
                                             'range': 'MCCObservationTypeEnum'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    observation_type: Optional[MCCObservationTypeEnum] = Field(default=None, description="""The type of observation being measured. Constrained by domain-specific enums in microschemas (e.g., CiliaryObservationTypeEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measured_entity: Optional[NamedEntity] = Field(default=None, description="""The biological or chemical entity being measured (e.g., Cilium, CFTR, ROS). Reference to an ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Brief description of the method used to obtain the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date when the measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    uses: Optional[Assay] = Field(default=None, description="""The Assay used to produce this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    cell_culture_system: Optional[str] = Field(default=None, description="""Type of cell culture system (e.g., ALI, organoid, 2D monolayer, MucilAir, EpiAirway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    days_at_differentiation: Optional[int] = Field(default=None, description="""Days at air-liquid interface or differentiation stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    passage_number: Optional[int] = Field(default=None, description="""Cell passage number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    substrate_type: Optional[str] = Field(default=None, description="""Type of culture substrate (e.g., transwell, collagen-coated, Matrigel).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    donor_info: Optional[str] = Field(default=None, description="""Information about cell donor (e.g., healthy non-smoker, CF patient, age, anatomical region).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of replicate cultures per donor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    culture_medium: Optional[str] = Field(default=None, description="""Culture medium formulation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    participant: Optional[NamedEntity] = Field(default=None, description="""The study participant from whom the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample (e.g., urine, blood, sputum, nasal epithelium, exhaled breath condensate).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_site: Optional[str] = Field(default=None, description="""Anatomical site of sample collection (e.g., inferior turbinate, bronchus).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_date: Optional[date] = Field(default=None, description="""Date when the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    subject_characteristics: Optional[str] = Field(default=None, description="""Relevant subject characteristics (e.g., age, sex, disease state, medication use, smoking status).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })


class OxidativeStressMeasurement(InVivoContext, InVitroContext, Measurement):
    """
    Measurement of oxidative stress markers including reactive oxygen species, lipid peroxidation products, protein oxidation, DNA damage, and antioxidant capacity. Key molecular initiating event in respiratory toxicology AOPs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_microschemas',
         'implements': ['measurement_base:Measurement'],
         'mixins': ['Measurement', 'InVitroContext', 'InVivoContext'],
         'slot_usage': {'observation_type': {'name': 'observation_type',
                                             'range': 'OxidativeStressObservationTypeEnum'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    observation_type: Optional[OxidativeStressObservationTypeEnum] = Field(default=None, description="""The type of observation being measured. Constrained by domain-specific enums in microschemas (e.g., CiliaryObservationTypeEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measured_entity: Optional[NamedEntity] = Field(default=None, description="""The biological or chemical entity being measured (e.g., Cilium, CFTR, ROS). Reference to an ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Brief description of the method used to obtain the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date when the measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    uses: Optional[Assay] = Field(default=None, description="""The Assay used to produce this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    cell_culture_system: Optional[str] = Field(default=None, description="""Type of cell culture system (e.g., ALI, organoid, 2D monolayer, MucilAir, EpiAirway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    days_at_differentiation: Optional[int] = Field(default=None, description="""Days at air-liquid interface or differentiation stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    passage_number: Optional[int] = Field(default=None, description="""Cell passage number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    substrate_type: Optional[str] = Field(default=None, description="""Type of culture substrate (e.g., transwell, collagen-coated, Matrigel).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    donor_info: Optional[str] = Field(default=None, description="""Information about cell donor (e.g., healthy non-smoker, CF patient, age, anatomical region).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of replicate cultures per donor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    culture_medium: Optional[str] = Field(default=None, description="""Culture medium formulation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    participant: Optional[NamedEntity] = Field(default=None, description="""The study participant from whom the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample (e.g., urine, blood, sputum, nasal epithelium, exhaled breath condensate).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_site: Optional[str] = Field(default=None, description="""Anatomical site of sample collection (e.g., inferior turbinate, bronchus).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_date: Optional[date] = Field(default=None, description="""Date when the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    subject_characteristics: Optional[str] = Field(default=None, description="""Relevant subject characteristics (e.g., age, sex, disease state, medication use, smoking status).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })


class CFTRMeasurement(InVivoContext, InVitroContext, Measurement):
    """
    Measurement of CFTR (cystic fibrosis transmembrane conductance regulator) function including chloride secretion, CFTR-mediated current, and clinical indicators like sweat chloride concentration.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_microschemas',
         'implements': ['measurement_base:Measurement'],
         'mixins': ['Measurement', 'InVitroContext', 'InVivoContext'],
         'slot_usage': {'observation_type': {'name': 'observation_type',
                                             'range': 'CFTRObservationTypeEnum'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    observation_type: Optional[CFTRObservationTypeEnum] = Field(default=None, description="""The type of observation being measured. Constrained by domain-specific enums in microschemas (e.g., CiliaryObservationTypeEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measured_entity: Optional[NamedEntity] = Field(default=None, description="""The biological or chemical entity being measured (e.g., Cilium, CFTR, ROS). Reference to an ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Brief description of the method used to obtain the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date when the measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    uses: Optional[Assay] = Field(default=None, description="""The Assay used to produce this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    cell_culture_system: Optional[str] = Field(default=None, description="""Type of cell culture system (e.g., ALI, organoid, 2D monolayer, MucilAir, EpiAirway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    days_at_differentiation: Optional[int] = Field(default=None, description="""Days at air-liquid interface or differentiation stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    passage_number: Optional[int] = Field(default=None, description="""Cell passage number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    substrate_type: Optional[str] = Field(default=None, description="""Type of culture substrate (e.g., transwell, collagen-coated, Matrigel).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    donor_info: Optional[str] = Field(default=None, description="""Information about cell donor (e.g., healthy non-smoker, CF patient, age, anatomical region).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of replicate cultures per donor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    culture_medium: Optional[str] = Field(default=None, description="""Culture medium formulation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    participant: Optional[NamedEntity] = Field(default=None, description="""The study participant from whom the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample (e.g., urine, blood, sputum, nasal epithelium, exhaled breath condensate).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_site: Optional[str] = Field(default=None, description="""Anatomical site of sample collection (e.g., inferior turbinate, bronchus).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_date: Optional[date] = Field(default=None, description="""Date when the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    subject_characteristics: Optional[str] = Field(default=None, description="""Relevant subject characteristics (e.g., age, sex, disease state, medication use, smoking status).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })


class EGFRMeasurement(InVitroContext, Measurement):
    """
    Measurement of EGFR (epidermal growth factor receptor) pathway activation including receptor phosphorylation, downstream kinase activation, and ligand expression. Key signaling pathway in airway inflammation and mucin regulation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_microschemas',
         'implements': ['measurement_base:Measurement'],
         'mixins': ['Measurement', 'InVitroContext'],
         'slot_usage': {'observation_type': {'name': 'observation_type',
                                             'range': 'EGFRObservationTypeEnum'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    observation_type: Optional[EGFRObservationTypeEnum] = Field(default=None, description="""The type of observation being measured. Constrained by domain-specific enums in microschemas (e.g., CiliaryObservationTypeEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measured_entity: Optional[NamedEntity] = Field(default=None, description="""The biological or chemical entity being measured (e.g., Cilium, CFTR, ROS). Reference to an ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Brief description of the method used to obtain the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date when the measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    uses: Optional[Assay] = Field(default=None, description="""The Assay used to produce this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    cell_culture_system: Optional[str] = Field(default=None, description="""Type of cell culture system (e.g., ALI, organoid, 2D monolayer, MucilAir, EpiAirway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    days_at_differentiation: Optional[int] = Field(default=None, description="""Days at air-liquid interface or differentiation stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    passage_number: Optional[int] = Field(default=None, description="""Cell passage number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    substrate_type: Optional[str] = Field(default=None, description="""Type of culture substrate (e.g., transwell, collagen-coated, Matrigel).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    donor_info: Optional[str] = Field(default=None, description="""Information about cell donor (e.g., healthy non-smoker, CF patient, age, anatomical region).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of replicate cultures per donor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    culture_medium: Optional[str] = Field(default=None, description="""Culture medium formulation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })


class GobletCellMucinMeasurement(InVivoContext, InVitroContext, Measurement):
    """
    Measurement of goblet cell populations and mucin production including goblet cell counts, mucin gene/protein expression, and mucus properties. Assesses goblet cell hyperplasia and mucus hypersecretion phenotypes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_microschemas',
         'implements': ['measurement_base:Measurement'],
         'mixins': ['Measurement', 'InVitroContext', 'InVivoContext'],
         'slot_usage': {'observation_type': {'name': 'observation_type',
                                             'range': 'GobletCellMucinObservationTypeEnum'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    observation_type: Optional[GobletCellMucinObservationTypeEnum] = Field(default=None, description="""The type of observation being measured. Constrained by domain-specific enums in microschemas (e.g., CiliaryObservationTypeEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measured_entity: Optional[NamedEntity] = Field(default=None, description="""The biological or chemical entity being measured (e.g., Cilium, CFTR, ROS). Reference to an ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Brief description of the method used to obtain the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date when the measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    uses: Optional[Assay] = Field(default=None, description="""The Assay used to produce this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    cell_culture_system: Optional[str] = Field(default=None, description="""Type of cell culture system (e.g., ALI, organoid, 2D monolayer, MucilAir, EpiAirway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    days_at_differentiation: Optional[int] = Field(default=None, description="""Days at air-liquid interface or differentiation stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    passage_number: Optional[int] = Field(default=None, description="""Cell passage number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    substrate_type: Optional[str] = Field(default=None, description="""Type of culture substrate (e.g., transwell, collagen-coated, Matrigel).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    donor_info: Optional[str] = Field(default=None, description="""Information about cell donor (e.g., healthy non-smoker, CF patient, age, anatomical region).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of replicate cultures per donor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    culture_medium: Optional[str] = Field(default=None, description="""Culture medium formulation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    participant: Optional[NamedEntity] = Field(default=None, description="""The study participant from whom the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample (e.g., urine, blood, sputum, nasal epithelium, exhaled breath condensate).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_site: Optional[str] = Field(default=None, description="""Anatomical site of sample collection (e.g., inferior turbinate, bronchus).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_date: Optional[date] = Field(default=None, description="""Date when the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    subject_characteristics: Optional[str] = Field(default=None, description="""Relevant subject characteristics (e.g., age, sex, disease state, medication use, smoking status).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })


class BALFSputumMeasurement(InVivoContext, Measurement):
    """
    Measurement of bronchoalveolar lavage fluid (BALF) or sputum components including inflammatory cell profiles, cytokine levels, microbiome composition, and protein concentrations. Clinical assessment of airway inflammation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_microschemas',
         'implements': ['measurement_base:Measurement'],
         'mixins': ['Measurement', 'InVivoContext'],
         'slot_usage': {'observation_type': {'name': 'observation_type',
                                             'range': 'BALFSputumObservationTypeEnum'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    observation_type: Optional[BALFSputumObservationTypeEnum] = Field(default=None, description="""The type of observation being measured. Constrained by domain-specific enums in microschemas (e.g., CiliaryObservationTypeEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measured_entity: Optional[NamedEntity] = Field(default=None, description="""The biological or chemical entity being measured (e.g., Cilium, CFTR, ROS). Reference to an ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Brief description of the method used to obtain the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date when the measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    uses: Optional[Assay] = Field(default=None, description="""The Assay used to produce this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    participant: Optional[NamedEntity] = Field(default=None, description="""The study participant from whom the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample (e.g., urine, blood, sputum, nasal epithelium, exhaled breath condensate).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_site: Optional[str] = Field(default=None, description="""Anatomical site of sample collection (e.g., inferior turbinate, bronchus).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_date: Optional[date] = Field(default=None, description="""Date when the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    subject_characteristics: Optional[str] = Field(default=None, description="""Relevant subject characteristics (e.g., age, sex, disease state, medication use, smoking status).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })


class LungFunctionMeasurement(InVivoContext, Measurement):
    """
    Measurement of lung function parameters via spirometry and other pulmonary function tests including FEV1, FVC, FEV1/FVC ratio, and diffusing capacity. Clinical outcomes for respiratory health assessment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_microschemas',
         'implements': ['measurement_base:Measurement'],
         'mixins': ['Measurement', 'InVivoContext'],
         'slot_usage': {'observation_type': {'name': 'observation_type',
                                             'range': 'LungFunctionObservationTypeEnum'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    observation_type: Optional[LungFunctionObservationTypeEnum] = Field(default=None, description="""The type of observation being measured. Constrained by domain-specific enums in microschemas (e.g., CiliaryObservationTypeEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measured_entity: Optional[NamedEntity] = Field(default=None, description="""The biological or chemical entity being measured (e.g., Cilium, CFTR, ROS). Reference to an ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Brief description of the method used to obtain the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date when the measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    uses: Optional[Assay] = Field(default=None, description="""The Assay used to produce this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    participant: Optional[NamedEntity] = Field(default=None, description="""The study participant from whom the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample (e.g., urine, blood, sputum, nasal epithelium, exhaled breath condensate).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_site: Optional[str] = Field(default=None, description="""Anatomical site of sample collection (e.g., inferior turbinate, bronchus).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_date: Optional[date] = Field(default=None, description="""Date when the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    subject_characteristics: Optional[str] = Field(default=None, description="""Relevant subject characteristics (e.g., age, sex, disease state, medication use, smoking status).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })


class FoxJMeasurement(InVitroContext, Measurement):
    """
    Measurement of FoxJ1 expression and related ciliogenesis markers. FoxJ1 is a master regulator of multiciliogenesis, and its expression indicates ciliated cell differentiation status.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_microschemas',
         'implements': ['measurement_base:Measurement'],
         'mixins': ['Measurement', 'InVitroContext'],
         'slot_usage': {'observation_type': {'name': 'observation_type',
                                             'range': 'FoxJObservationTypeEnum'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    observation_type: Optional[FoxJObservationTypeEnum] = Field(default=None, description="""The type of observation being measured. Constrained by domain-specific enums in microschemas (e.g., CiliaryObservationTypeEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measured_entity: Optional[NamedEntity] = Field(default=None, description="""The biological or chemical entity being measured (e.g., Cilium, CFTR, ROS). Reference to an ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Brief description of the method used to obtain the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date when the measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    uses: Optional[Assay] = Field(default=None, description="""The Assay used to produce this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    cell_culture_system: Optional[str] = Field(default=None, description="""Type of cell culture system (e.g., ALI, organoid, 2D monolayer, MucilAir, EpiAirway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    days_at_differentiation: Optional[int] = Field(default=None, description="""Days at air-liquid interface or differentiation stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    passage_number: Optional[int] = Field(default=None, description="""Cell passage number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    substrate_type: Optional[str] = Field(default=None, description="""Type of culture substrate (e.g., transwell, collagen-coated, Matrigel).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    donor_info: Optional[str] = Field(default=None, description="""Information about cell donor (e.g., healthy non-smoker, CF patient, age, anatomical region).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of replicate cultures per donor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })
    culture_medium: Optional[str] = Field(default=None, description="""Culture medium formulation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroContext']} })


class ExposureBiomarkerMeasurement(InVivoContext, Measurement):
    """
    Measurement of biomarkers indicating exposure to environmental agents including urinary metabolites (e.g., cotinine for tobacco smoke), blood levels, and other exposure indicators.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/measurement_microschemas',
         'implements': ['measurement_base:Measurement'],
         'mixins': ['Measurement', 'InVivoContext'],
         'slot_usage': {'observation_type': {'name': 'observation_type',
                                             'range': 'ExposureBiomarkerObservationTypeEnum'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'Assay',
                       'Method',
                       'Protocol',
                       'Unit',
                       'NamedEntity'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'Assay', 'Method', 'Protocol'],
         'slot_uri': 'schema:description'} })
    observation_type: Optional[ExposureBiomarkerObservationTypeEnum] = Field(default=None, description="""The type of observation being measured. Constrained by domain-specific enums in microschemas (e.g., CiliaryObservationTypeEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of the reference range for this measurement type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measured_entity: Optional[NamedEntity] = Field(default=None, description="""The biological or chemical entity being measured (e.g., Cilium, CFTR, ROS). Reference to an ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Brief description of the method used to obtain the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date when the measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    uses: Optional[Assay] = Field(default=None, description="""The Assay used to produce this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    participant: Optional[NamedEntity] = Field(default=None, description="""The study participant from whom the measurement was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample (e.g., urine, blood, sputum, nasal epithelium, exhaled breath condensate).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_site: Optional[str] = Field(default=None, description="""Anatomical site of sample collection (e.g., inferior turbinate, bronchus).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    collection_date: Optional[date] = Field(default=None, description="""Date when the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })
    subject_characteristics: Optional[str] = Field(default=None, description="""Relevant subject characteristics (e.g., age, sex, disease state, medication use, smoking status).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoContext']} })


class Container(ConfiguredBaseModel):
    """
    A container for collections of measurements and related entities. Used as the root class for data validation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'tree_root': True})

    ciliary_measurements: Optional[list[CiliaryFunctionMeasurement]] = Field(default=[], description="""Collection of ciliary function measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    asl_measurements: Optional[list[ASLMeasurement]] = Field(default=[], description="""Collection of airway surface liquid measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    mcc_measurements: Optional[list[MCCMeasurement]] = Field(default=[], description="""Collection of mucociliary clearance measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    oxidative_stress_measurements: Optional[list[OxidativeStressMeasurement]] = Field(default=[], description="""Collection of oxidative stress measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    cftr_measurements: Optional[list[CFTRMeasurement]] = Field(default=[], description="""Collection of CFTR function measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    egfr_measurements: Optional[list[EGFRMeasurement]] = Field(default=[], description="""Collection of EGFR signaling measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    goblet_cell_mucin_measurements: Optional[list[GobletCellMucinMeasurement]] = Field(default=[], description="""Collection of goblet cell and mucin measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    balf_sputum_measurements: Optional[list[BALFSputumMeasurement]] = Field(default=[], description="""Collection of BALF and sputum measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    lung_function_measurements: Optional[list[LungFunctionMeasurement]] = Field(default=[], description="""Collection of lung function measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    foxj_measurements: Optional[list[FoxJMeasurement]] = Field(default=[], description="""Collection of FoxJ1/ciliogenesis measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    exposure_biomarker_measurements: Optional[list[ExposureBiomarkerMeasurement]] = Field(default=[], description="""Collection of exposure biomarker measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    protocols: Optional[list[Protocol]] = Field(default=[], description="""Collection of protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    methods: Optional[list[Method]] = Field(default=[], description="""Collection of methods.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    assays: Optional[list[Assay]] = Field(default=[], description="""Collection of assays.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Measurement.model_rebuild()
Assay.model_rebuild()
Method.model_rebuild()
Protocol.model_rebuild()
InVitroContext.model_rebuild()
InVivoContext.model_rebuild()
QuantityValue.model_rebuild()
Unit.model_rebuild()
NamedEntity.model_rebuild()
CiliaryFunctionMeasurement.model_rebuild()
ASLMeasurement.model_rebuild()
MCCMeasurement.model_rebuild()
OxidativeStressMeasurement.model_rebuild()
CFTRMeasurement.model_rebuild()
EGFRMeasurement.model_rebuild()
GobletCellMucinMeasurement.model_rebuild()
BALFSputumMeasurement.model_rebuild()
LungFunctionMeasurement.model_rebuild()
FoxJMeasurement.model_rebuild()
ExposureBiomarkerMeasurement.model_rebuild()
Container.model_rebuild()
