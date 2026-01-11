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


linkml_meta = LinkMLMeta({'default_prefix': 'owg',
     'default_range': 'string',
     'description': 'A LinkML data model for representing biological measurements, '
                    'assays, and experimental protocols in the context of outcomes '
                    'research.',
     'id': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'outcomes_working_group',
     'prefixes': {'AOPWIKI': {'prefix_prefix': 'AOPWIKI',
                              'prefix_reference': 'https://aopwiki.org/aops/'},
                  'CHEBI': {'prefix_prefix': 'CHEBI',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'CHEMBL.COMPOUND': {'prefix_prefix': 'CHEMBL.COMPOUND',
                                      'prefix_reference': 'http://identifiers.org/chembl.compound/'},
                  'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CL_'},
                  'CLO': {'prefix_prefix': 'CLO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/CLO_'},
                  'CTD.CHEMICAL': {'prefix_prefix': 'CTD.CHEMICAL',
                                   'prefix_reference': 'http://ctdbase.org/detail.go?type=chem&acc='},
                  'CTD.GENE': {'prefix_prefix': 'CTD.GENE',
                               'prefix_reference': 'http://ctdbase.org/detail.go?type=gene&acc='},
                  'DTXSID': {'prefix_prefix': 'DTXSID',
                             'prefix_reference': 'https://comptox.epa.gov/dashboard/dsstoxdb/results?search='},
                  'ECTO': {'prefix_prefix': 'ECTO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ECTO_'},
                  'EFO': {'prefix_prefix': 'EFO',
                          'prefix_reference': 'http://identifiers.org/efo/'},
                  'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'FOODON': {'prefix_prefix': 'FOODON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/FOODON_'},
                  'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'GWAS': {'prefix_prefix': 'GWAS',
                           'prefix_reference': 'https://www.ebi.ac.uk/gwas/studies/'},
                  'GXA': {'prefix_prefix': 'GXA',
                          'prefix_reference': 'https://www.ebi.ac.uk/gxa/experiments/'},
                  'HHEAR': {'prefix_prefix': 'HHEAR',
                            'prefix_reference': 'http://hadatac.org/ont/hhear#'},
                  'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'MONDO': {'prefix_prefix': 'MONDO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'MP': {'prefix_prefix': 'MP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/MP_'},
                  'NAMO': {'prefix_prefix': 'NAMO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NAMO_'},
                  'NCBIGENE': {'prefix_prefix': 'NCBIGENE',
                               'prefix_reference': 'https://www.ncbi.nlm.nih.gov/gene/'},
                  'NCBITaxon': {'prefix_prefix': 'NCBITaxon',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'NHANES': {'prefix_prefix': 'NHANES',
                             'prefix_reference': 'https://wwwn.cdc.gov/Nchs/Nhanes/'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'OMRSE': {'prefix_prefix': 'OMRSE',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/OMRSE_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'PR': {'prefix_prefix': 'PR',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/PR_'},
                  'PUBCHEM.COMPOUND': {'prefix_prefix': 'PUBCHEM.COMPOUND',
                                       'prefix_reference': 'http://identifiers.org/pubchem.compound/'},
                  'RO': {'prefix_prefix': 'RO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/RO_'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'UCUM': {'prefix_prefix': 'UCUM',
                           'prefix_reference': 'http://unitsofmeasure.org/'},
                  'UO': {'prefix_prefix': 'UO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/UO_'},
                  'UPHENO': {'prefix_prefix': 'UPHENO',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UPHENO_'},
                  'USDA.PESTICIDE': {'prefix_prefix': 'USDA.PESTICIDE',
                                     'prefix_reference': 'https://www.ams.usda.gov/datasets/pdp/'},
                  'ZP': {'prefix_prefix': 'ZP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/ZP_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/vocab/'},
                  'chear': {'prefix_prefix': 'chear',
                            'prefix_reference': 'http://hadatac.org/ont/chear#'},
                  'fhir': {'prefix_prefix': 'fhir',
                           'prefix_reference': 'http://hl7.org/fhir/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'owg': {'prefix_prefix': 'owg',
                          'prefix_reference': 'https://w3id.org/EHS-Data-Standards/outcomes-working-group/'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/vocab/unit/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'wikidata': {'prefix_prefix': 'wikidata',
                               'prefix_reference': 'http://www.wikidata.org/entity/'}},
     'see_also': ['https://EHS-Data-Standards.github.io/outcomes-working-group'],
     'source_file': 'src/outcomes_working_group/schema/outcomes_working_group.yaml',
     'title': 'Outcome Measurement Data Model'} )

class ExposureRouteEnum(str, Enum):
    """
    Routes of exposure to chemicals or environmental factors
    """
    oral = "oral"
    """
    Oral ingestion
    """
    dermal = "dermal"
    """
    Dermal contact
    """
    inhalation = "inhalation"
    """
    Inhalation
    """
    injection = "injection"
    """
    Injection
    """
    unknown = "unknown"
    """
    Unknown route
    """


class ExposureMediumEnum(str, Enum):
    """
    Medium through which exposure occurs
    """
    air = "air"
    """
    Air
    """
    water = "water"
    """
    Water
    """
    food = "food"
    """
    Food
    """
    soil = "soil"
    """
    Soil
    """
    dust = "dust"
    """
    Dust
    """
    consumer_product = "consumer_product"
    """
    Consumer product
    """
    unknown = "unknown"
    """
    Unknown medium
    """


class ExpressionAssayMethodEnum(str, Enum):
    """
    Methods used to measure gene or protein expression. Includes transcriptomic, proteomic, and imaging-based approaches.
    """
    qrt_pcr = "qrt_pcr"
    """
    Quantitative real-time polymerase chain reaction
    """
    rna_seq = "rna_seq"
    """
    RNA sequencing (bulk)
    """
    single_cell_rna_seq = "single_cell_rna_seq"
    """
    Single-cell RNA sequencing
    """
    microarray = "microarray"
    """
    Gene expression microarray
    """
    nanostring = "nanostring"
    """
    NanoString nCounter gene expression assay
    """
    northern_blot = "northern_blot"
    """
    Northern blot for RNA detection
    """
    in_situ_hybridization = "in_situ_hybridization"
    """
    In situ hybridization (ISH, FISH, RNAscope)
    """
    western_blot = "western_blot"
    """
    Western blot (immunoblot) for protein detection
    """
    elisa = "elisa"
    """
    Enzyme-linked immunosorbent assay
    """
    immunohistochemistry = "immunohistochemistry"
    """
    Immunohistochemistry on tissue sections
    """
    immunofluorescence = "immunofluorescence"
    """
    Immunofluorescence staining
    """
    flow_cytometry = "flow_cytometry"
    """
    Flow cytometry for protein expression
    """
    mass_spectrometry = "mass_spectrometry"
    """
    Mass spectrometry-based proteomics
    """
    immunoprecipitation = "immunoprecipitation"
    """
    Immunoprecipitation followed by detection
    """
    luminex = "luminex"
    """
    Luminex multiplex bead-based assay
    """
    other = "other"
    """
    Other assay method not listed
    """


class BiologicalOrganizationLevelEnum(str, Enum):
    """
    Levels of biological organization
    """
    molecular = "molecular"
    """
    Molecular level
    """
    cellular = "cellular"
    """
    Cellular level
    """
    tissue = "tissue"
    """
    Tissue level
    """
    organ = "organ"
    """
    Organ level
    """
    organism = "organism"
    """
    Organism level
    """
    population = "population"
    """
    Population level
    """


class StudyTypeEnum(str, Enum):
    """
    Types of research studies
    """
    cohort = "cohort"
    """
    Cohort study
    """
    cross_sectional = "cross_sectional"
    """
    Cross-sectional study
    """
    case_control = "case_control"
    """
    Case-control study
    """
    randomized_controlled_trial = "randomized_controlled_trial"
    """
    Randomized controlled trial
    """
    survey = "survey"
    """
    Survey
    """
    gwas = "gwas"
    """
    Genome-wide association study
    """
    other = "other"
    """
    Other study type
    """


class SexEnum(str, Enum):
    """
    Biological sex
    """
    male = "male"
    """
    Male
    """
    female = "female"
    """
    Female
    """
    unknown = "unknown"
    """
    Unknown
    """


class SampleTypeEnum(str, Enum):
    """
    Types of biological and environmental samples
    """
    blood = "blood"
    """
    Blood sample
    """
    urine = "urine"
    """
    Urine sample
    """
    serum = "serum"
    """
    Serum sample
    """
    plasma = "plasma"
    """
    Plasma sample
    """
    tissue = "tissue"
    """
    Tissue sample
    """
    saliva = "saliva"
    """
    Saliva sample
    """
    hair = "hair"
    """
    Hair sample
    """
    nail = "nail"
    """
    Nail sample
    """
    air = "air"
    """
    Air sample (environmental)
    """
    water = "water"
    """
    Water sample (environmental)
    """
    soil = "soil"
    """
    Soil sample (environmental)
    """
    other = "other"
    """
    Other sample type
    """


class SummaryStatisticEnum(str, Enum):
    """
    Types of summary statistics
    """
    mean = "mean"
    """
    Arithmetic mean
    """
    median = "median"
    """
    Median
    """
    mode = "mode"
    """
    Mode
    """
    percentile = "percentile"
    """
    Percentile
    """
    standard_deviation = "standard_deviation"
    """
    Standard deviation
    """
    variance = "variance"
    """
    Variance
    """
    range = "range"
    """
    Range
    """
    interquartile_range = "interquartile_range"
    """
    Interquartile range
    """


class MeasurementTypeEnum(str, Enum):
    """
    Types of measurements and observations for outcomes research, with emphasis on respiratory health and environmental toxicant effects.
    """
    FEV1 = "FEV1"
    """
    Forced expiratory volume in 1 second
    """
    FVC = "FVC"
    """
    Forced vital capacity
    """
    FEV1_FEC_ratio = "FEV1_FEC_ratio"
    """
    Ratio of FEV1 to FVC (Tiffeneau-Pinelli index)
    """
    FEF25_75 = "FEF25_75"
    """
    Forced expiratory flow at 25-75% of FVC
    """
    peak_expiratory_flow = "peak_expiratory_flow"
    """
    Peak expiratory flow rate
    """
    DLCO = "DLCO"
    """
    Diffusing capacity of the lung for carbon monoxide
    """
    FeNO = "FeNO"
    """
    Fractional exhaled nitric oxide (airway inflammation marker)
    """
    bronchodilator_response = "bronchodilator_response"
    """
    Change in lung function after bronchodilator administration
    """
    lung_function_decline_rate = "lung_function_decline_rate"
    """
    Rate of decline in lung function over time
    """
    ciliary_beat_frequency = "ciliary_beat_frequency"
    """
    Frequency of ciliary beating in Hz
    """
    ciliary_active_area_percentage = "ciliary_active_area_percentage"
    """
    Percentage of epithelial surface with active cilia
    """
    cilia_per_cell = "cilia_per_cell"
    """
    Number of cilia per epithelial cell
    """
    cilia_length = "cilia_length"
    """
    Length of cilia in micrometers
    """
    percentage_ciliated_cells = "percentage_ciliated_cells"
    """
    Percentage of cells that are ciliated
    """
    asl_height = "asl_height"
    """
    Airway surface liquid height in micrometers
    """
    periciliary_layer_depth = "periciliary_layer_depth"
    """
    Depth of periciliary liquid layer (reduced in disease)
    """
    mucus_layer_thickness = "mucus_layer_thickness"
    """
    Thickness of the mucus gel layer
    """
    mucociliary_transport_rate = "mucociliary_transport_rate"
    """
    Rate of mucociliary transport (mm/min)
    """
    mucociliary_directionality = "mucociliary_directionality"
    """
    Directionality and coordination of mucociliary transport
    """
    particle_clearance_rate = "particle_clearance_rate"
    """
    Rate of particle clearance from airways
    """
    goblet_cell_count = "goblet_cell_count"
    """
    Number or percentage of goblet cells
    """
    goblet_to_ciliated_ratio = "goblet_to_ciliated_ratio"
    """
    Ratio of goblet cells to ciliated cells
    """
    mucin_protein_concentration = "mucin_protein_concentration"
    """
    Concentration of secreted mucin protein
    """
    mucus_viscosity = "mucus_viscosity"
    """
    Viscosity of airway mucus
    """
    CFTR_chloride_secretion = "CFTR_chloride_secretion"
    """
    CFTR-mediated chloride secretory current
    """
    inhibitor_sensitive_current = "inhibitor_sensitive_current"
    """
    Current sensitive to CFTR inhibitors (e.g., CFTRinh-172)
    """
    sweat_chloride_concentration = "sweat_chloride_concentration"
    """
    Chloride concentration in sweat (CF diagnostic)
    """
    reactive_oxygen_species = "reactive_oxygen_species"
    """
    Reactive oxygen species (ROS) level
    """
    lipid_peroxidation = "lipid_peroxidation"
    """
    Lipid peroxidation markers (MDA, 8-isoprostane)
    """
    protein_carbonyls = "protein_carbonyls"
    """
    Protein carbonyl content (protein oxidation marker)
    """
    DNA_8ohdg = "DNA_8ohdg"
    """
    8-hydroxydeoxyguanosine (DNA oxidative damage marker)
    """
    glutathione_ratio = "glutathione_ratio"
    """
    GSH/GSSG ratio (antioxidant capacity)
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
    Glutathione peroxidase (GPx) activity
    """
    total_antioxidant_capacity = "total_antioxidant_capacity"
    """
    Total antioxidant capacity of sample
    """
    TEER = "TEER"
    """
    Transepithelial electrical resistance
    """
    paracellular_permeability = "paracellular_permeability"
    """
    Paracellular permeability coefficient
    """
    IL6_level = "IL6_level"
    """
    Interleukin-6 concentration
    """
    IL8_level = "IL8_level"
    """
    Interleukin-8 (CXCL8) concentration
    """
    IL13_level = "IL13_level"
    """
    Interleukin-13 concentration
    """
    TNF_alpha_level = "TNF_alpha_level"
    """
    Tumor necrosis factor alpha concentration
    """
    neutrophil_percentage = "neutrophil_percentage"
    """
    Percentage of neutrophils in BALF or sputum
    """
    eosinophil_percentage = "eosinophil_percentage"
    """
    Percentage of eosinophils in BALF or sputum
    """
    macrophage_percentage = "macrophage_percentage"
    """
    Percentage of macrophages in BALF or sputum
    """
    total_inflammatory_cell = "total_inflammatory_cell"
    """
    Total inflammatory cell count
    """
    LDH_release = "LDH_release"
    """
    Lactate dehydrogenase release (cell damage marker)
    """
    cell_viability = "cell_viability"
    """
    Cell viability percentage
    """
    mtt_reduction = "mtt_reduction"
    """
    MTT assay result (metabolic activity)
    """
    apoptosis_rate = "apoptosis_rate"
    """
    Rate of apoptotic cell death
    """
    gene_expression = "gene_expression"
    """
    Gene expression level (mRNA). Use with GeneExpressionMeasurement class to specify target_gene, tissue_context, and assay_method.
    """
    protein_expression = "protein_expression"
    """
    Protein expression level. Use with ProteinExpressionMeasurement class to specify target_protein, tissue_context, and assay_method.
    """
    protein_phosphorylation = "protein_phosphorylation"
    """
    Protein phosphorylation level. Use with ProteinExpressionMeasurement class and specify phosphorylation_site (e.g., Y1068 for EGFR).
    """
    protein_localization = "protein_localization"
    """
    Protein subcellular localization (membrane, cytoplasm, nucleus). Use with ProteinExpressionMeasurement class.
    """
    expression_ratio = "expression_ratio"
    """
    Ratio of expression between two genes or proteins (e.g., MUC5AC/MUC5B ratio). Specify both targets in description.
    """
    percentage_positive_cells = "percentage_positive_cells"
    """
    Percentage of cells positive for a marker (IHC, flow cytometry)
    """
    urinary_arsenic_level = "urinary_arsenic_level"
    """
    Urinary arsenic concentration
    """
    urinary_cotinine_level = "urinary_cotinine_level"
    """
    Urinary cotinine (tobacco exposure biomarker)
    """
    urinary_bpa_level = "urinary_bpa_level"
    """
    Urinary bisphenol A concentration
    """
    urinary_phthalate_metabolites = "urinary_phthalate_metabolites"
    """
    Urinary phthalate metabolite concentrations
    """
    pm2_5_exposure = "pm2_5_exposure"
    """
    Fine particulate matter (PM2.5) exposure level
    """
    ozone_exposure = "ozone_exposure"
    """
    Ozone exposure concentration
    """
    NO2_exposure = "NO2_exposure"
    """
    Nitrogen dioxide exposure concentration
    """
    polycyclic_aromatic_hydrocarbons = "polycyclic_aromatic_hydrocarbons"
    """
    PAH metabolite levels
    """
    body_mass_index = "body_mass_index"
    """
    Body mass index (BMI)
    """
    body_weight = "body_weight"
    """
    Body weight measurement
    """
    height = "height"
    """
    Height measurement
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
    Total bacterial load (CFU or 16S copies)
    """
    co2_percentage = "co2_percentage"
    """
    Carbon dioxide percentage in incubator atmosphere
    """
    o2_percentage = "o2_percentage"
    """
    Oxygen percentage in incubator (for hypoxic cultures)
    """
    temperature = "temperature"
    """
    Incubator or culture temperature
    """
    humidity = "humidity"
    """
    Relative humidity in incubator
    """
    nitrogen_balance = "nitrogen_balance"
    """
    Nitrogen percentage in atmosphere
    """
    ph = "ph"
    """
    pH of culture medium
    """
    stretch_frequency = "stretch_frequency"
    """
    Frequency of cyclic mechanical stretch (Hz)
    """
    stretch_amplitude = "stretch_amplitude"
    """
    Amplitude of mechanical stretch as percentage
    """
    shear_stress = "shear_stress"
    """
    Fluid shear stress applied to cells (dyn/cm2 or Pa)
    """
    flow_rate = "flow_rate"
    """
    Fluid flow rate in microfluidic or perfusion systems
    """
    perfusion_rate = "perfusion_rate"
    """
    Media perfusion rate for continuous culture systems
    """
    pressure = "pressure"
    """
    Hydrostatic or pneumatic pressure
    """
    pore_size = "pore_size"
    """
    Diameter of membrane pores (typically in micrometers)
    """
    pore_density = "pore_density"
    """
    Number of pores per unit area
    """
    thickness = "thickness"
    """
    Membrane thickness
    """
    surface_area = "surface_area"
    """
    Total membrane surface area
    """
    teer = "teer"
    """
    Transepithelial electrical resistance (membrane property)
    """
    other = "other"
    """
    Other measurement type not listed
    """


class RelationshipToHouseholdHeadEnum(str, Enum):
    """
    Relationship of a person to the household head (householder) in census data. Based on PUMS RELP variable coding.
    """
    householder = "householder"
    """
    Reference person (head of household)
    """
    spouse = "spouse"
    """
    Husband or wife of the householder
    """
    child = "child"
    """
    Biological, adopted, or stepchild of the householder
    """
    other_relative = "other_relative"
    """
    Other relative of the householder (parent, sibling, grandchild, etc.)
    """
    nonrelative = "nonrelative"
    """
    Non-relative of the householder (roommate, boarder, etc.)
    """
    foster_child = "foster_child"
    """
    Foster child
    """
    foster_parent = "foster_parent"
    """
    Foster parent
    """
    other_nonrelative = "other_nonrelative"
    """
    Other non-relative
    """


class CellCultureGrowthModeEnum(str, Enum):
    """
    Cell culture growth modes including traditional and advanced systems. Based on CLO cell culture growth mode terms.
    """
    adherent = "adherent"
    """
    Cells grow attached to a surface
    """
    suspension = "suspension"
    """
    Cells grow suspended in culture medium
    """
    air_liquid_interface = "air_liquid_interface"
    """
    Cells cultured at interface between air and liquid medium (ALI)
    """
    three_dimensional = "three_dimensional"
    """
    Cells grown in 3D matrix or scaffold
    """
    organoid = "organoid"
    """
    Self-organizing 3D tissue culture from stem cells
    """
    spheroid = "spheroid"
    """
    Spherical cellular aggregates formed by self-aggregation
    """


class SubstrateTypeEnum(str, Enum):
    """
    Types of cell culture substrates and surfaces. Includes traditional and advanced substrate materials.
    """
    plastic = "plastic"
    """
    Standard tissue culture-treated plastic
    """
    collagen_coated = "collagen_coated"
    """
    Collagen-coated surface for enhanced cell attachment
    """
    matrigel = "matrigel"
    """
    Basement membrane matrix (Matrigel/Geltrex)
    """
    fibronectin_coated = "fibronectin_coated"
    """
    Fibronectin-coated surface
    """
    laminin_coated = "laminin_coated"
    """
    Laminin-coated surface
    """
    transwell_insert = "transwell_insert"
    """
    Permeable support for air-liquid interface culture
    """
    hydrogel = "hydrogel"
    """
    Three-dimensional hydrogel matrix
    """
    glass = "glass"
    """
    Glass surface or coverslip
    """
    pdms = "pdms"
    """
    Polydimethylsiloxane (for microfluidics/organ-on-chip)
    """


class SupplementTypeEnum(str, Enum):
    """
    Categories of cell culture medium supplements and additives.
    """
    growth_factor = "growth_factor"
    """
    Proteins that stimulate cell growth, proliferation, and differentiation
    """
    antibiotic = "antibiotic"
    """
    Antimicrobial substances used to prevent bacterial contamination
    """
    antifungal = "antifungal"
    """
    Antifungal agents to prevent fungal contamination
    """
    hormone = "hormone"
    """
    Signaling molecules that regulate cell physiology
    """
    vitamin = "vitamin"
    """
    Organic compounds essential for normal growth and nutrition
    """
    amino_acid = "amino_acid"
    """
    Amino acid supplements for protein synthesis
    """
    cytokine = "cytokine"
    """
    Small proteins important in cell signaling
    """
    buffer = "buffer"
    """
    pH buffering agents (HEPES, bicarbonate)
    """
    serum = "serum"
    """
    Serum supplements (FBS, human serum)
    """
    differentiation_factor = "differentiation_factor"
    """
    Factors that induce or maintain cell differentiation
    """


class CellLineModificationEnum(str, Enum):
    """
    Types of genetic or other modifications applied to cell lines.
    """
    none = "none"
    """
    Unmodified cell line
    """
    transfection = "transfection"
    """
    Transient or stable DNA/RNA transfection
    """
    viral_transduction = "viral_transduction"
    """
    Viral vector-mediated gene transfer (lentiviral, adenoviral, AAV)
    """
    crispr_knockout = "crispr_knockout"
    """
    CRISPR/Cas9-mediated gene knockout
    """
    crispr_knockin = "crispr_knockin"
    """
    CRISPR/Cas9-mediated gene knockin or base editing
    """
    rnai = "rnai"
    """
    RNA interference-mediated gene knockdown (siRNA, shRNA)
    """
    overexpression = "overexpression"
    """
    Stable or transient gene overexpression
    """
    reporter = "reporter"
    """
    Reporter gene insertion (GFP, luciferase, fluorescent proteins)
    """
    immortalization = "immortalization"
    """
    Immortalization of primary cells (hTERT, SV40, etc.)
    """


class ThreeDArchitectureEnum(str, Enum):
    """
    Types of three-dimensional cell culture architectures.
    """
    spheroid = "spheroid"
    """
    Spherical cellular aggregates formed by self-aggregation
    """
    organoid = "organoid"
    """
    Self-organizing 3D tissue derived from stem cells
    """
    scaffold_based = "scaffold_based"
    """
    Cells grown on/in synthetic or natural scaffolds
    """
    hydrogel_encapsulated = "hydrogel_encapsulated"
    """
    Cells encapsulated within hydrogel matrix
    """
    bioprinted = "bioprinted"
    """
    3D bioprinted tissue constructs
    """
    microcarrier = "microcarrier"
    """
    Cells grown on microcarrier beads in suspension
    """
    hanging_drop = "hanging_drop"
    """
    Spheroids formed using hanging drop method
    """


class CoCultureConfigurationEnum(str, Enum):
    """
    Physical configurations for co-culture systems combining multiple cell types.
    """
    direct_contact = "direct_contact"
    """
    Cell types in direct physical contact on same surface
    """
    transwell = "transwell"
    """
    Cell types separated by permeable membrane insert
    """
    conditioned_medium = "conditioned_medium"
    """
    One cell type exposed to conditioned medium from another
    """
    microfluidic = "microfluidic"
    """
    Cell types in separate microfluidic compartments with shared media
    """
    spheroid_core_shell = "spheroid_core_shell"
    """
    One cell type forms core, another forms surrounding shell
    """
    patterned = "patterned"
    """
    Cell types arranged in defined spatial patterns
    """


class ChemicalFormEnum(str, Enum):
    """
    Physical form of a test substance or chemical in an exposure experiment.
    """
    solid = "solid"
    """
    Solid form (powder, crystite, etc.)
    """
    solution = "solution"
    """
    Dissolved in liquid vehicle
    """
    suspension = "suspension"
    """
    Particles suspended in liquid
    """
    aerosol = "aerosol"
    """
    Fine particles or droplets suspended in air
    """
    vapor = "vapor"
    """
    Gaseous form of normally liquid or solid substance
    """
    gas = "gas"
    """
    Gaseous chemical substance
    """
    nanoparticle = "nanoparticle"
    """
    Nanoparticulate form (1-100 nm)
    """
    microparticle = "microparticle"
    """
    Microparticulate form (0.1-100 um)
    """
    emulsion = "emulsion"
    """
    Mixture of immiscible liquids
    """
    gel = "gel"
    """
    Semi-solid gel form
    """


class ExposureRegimentEnum(str, Enum):
    """
    Pattern or schedule of exposure events in an in vitro experiment.
    """
    single = "single"
    """
    Single exposure event
    """
    continuous = "continuous"
    """
    Continuous exposure throughout experiment duration
    """
    repeated = "repeated"
    """
    Multiple discrete exposure events
    """
    intermittent = "intermittent"
    """
    Alternating periods of exposure and recovery
    """
    continuous_perfusion = "continuous_perfusion"
    """
    Continuous exposure via perfusion system
    """
    acute = "acute"
    """
    Short-term exposure (minutes to hours)
    """
    subchronic = "subchronic"
    """
    Medium-term exposure (days)
    """
    chronic = "chronic"
    """
    Long-term exposure (weeks or longer)
    """


class ControlTypeEnum(str, Enum):
    """
    Types of experimental controls used in in vitro exposure studies.
    """
    untreated = "untreated"
    """
    No treatment applied (negative control)
    """
    vehicle = "vehicle"
    """
    Vehicle/solvent only control
    """
    positive = "positive"
    """
    Known positive control compound
    """
    historical = "historical"
    """
    Comparison to historical control data
    """
    air = "air"
    """
    Clean air exposure (for aerosol studies)
    """
    media_only = "media_only"
    """
    Culture medium only control
    """
    sham = "sham"
    """
    Sham exposure procedure
    """


class DoseNormalizationMethodEnum(str, Enum):
    """
    Methods for normalizing dose in exposure experiments.
    """
    per_surface_area = "per_surface_area"
    """
    Dose normalized to surface area (ug/cm2)
    """
    per_cell_count = "per_cell_count"
    """
    Dose normalized to cell number
    """
    per_protein = "per_protein"
    """
    Dose normalized to total protein content
    """
    per_well = "per_well"
    """
    Dose per well (absolute)
    """
    per_insert = "per_insert"
    """
    Dose per transwell insert
    """
    per_volume = "per_volume"
    """
    Concentration in volume (ug/mL)
    """
    deposited_fraction = "deposited_fraction"
    """
    Based on measured deposited fraction
    """
    isdd_modeled = "isdd_modeled"
    """
    Calculated using In Vitro Sedimentation, Diffusion, and Dosimetry model
    """


class AerosolGenerationMethodEnum(str, Enum):
    """
    Methods for generating aerosols in inhalation toxicology studies.
    """
    nebulization = "nebulization"
    """
    Liquid nebulization (jet, ultrasonic, vibrating mesh)
    """
    dry_powder_dispersion = "dry_powder_dispersion"
    """
    Aerosolization of dry powder
    """
    condensation = "condensation"
    """
    Condensation aerosol generation
    """
    electrospray = "electrospray"
    """
    Electrospray atomization
    """
    spark_discharge = "spark_discharge"
    """
    Spark discharge for nanoparticle generation
    """
    combustion = "combustion"
    """
    Combustion-generated aerosols
    """
    evaporation_condensation = "evaporation_condensation"
    """
    Evaporation-condensation method
    """
    atomization = "atomization"
    """
    Mechanical atomization
    """
    cloud_system = "cloud_system"
    """
    Cloud-based deposition system (e.g., Vitrocell Cloud)
    """
    alice = "alice"
    """
    Air-Liquid Interface Cell Exposure system
    """


class DataNormalizationMethodEnum(str, Enum):
    """
    Methods for normalizing measurement data in analysis.
    """
    per_area = "per_area"
    """
    Normalized to surface area
    """
    per_cell_count = "per_cell_count"
    """
    Normalized to cell number
    """
    per_baseline = "per_baseline"
    """
    Normalized to baseline/pre-exposure value
    """
    to_internal_control = "to_internal_control"
    """
    Normalized to internal control on same plate/experiment
    """
    to_vehicle_control = "to_vehicle_control"
    """
    Normalized to vehicle control
    """
    to_positive_control = "to_positive_control"
    """
    Normalized to positive control
    """
    to_historical_control = "to_historical_control"
    """
    Normalized to historical control values
    """
    per_protein = "per_protein"
    """
    Normalized to total protein
    """
    z_score = "z_score"
    """
    Z-score normalization
    """
    percent_of_control = "percent_of_control"
    """
    Expressed as percentage of control
    """
    fold_change = "fold_change"
    """
    Expressed as fold change from baseline
    """


class RawDataTypeEnum(str, Enum):
    """
    Types of raw data collected from measurements.
    """
    image_stack = "image_stack"
    """
    Z-stack of images
    """
    single_image = "single_image"
    """
    Single 2D image
    """
    video = "video"
    """
    Time-lapse video recording
    """
    fluorescence_intensity = "fluorescence_intensity"
    """
    Fluorescence intensity readings
    """
    absorbance = "absorbance"
    """
    Absorbance/optical density readings
    """
    luminescence = "luminescence"
    """
    Luminescence readings
    """
    electrical = "electrical"
    """
    Electrical measurements (TEER, patch clamp)
    """
    flow_cytometry = "flow_cytometry"
    """
    Flow cytometry data files
    """
    spectral = "spectral"
    """
    Spectral data (Raman, FTIR)
    """
    mass_spec = "mass_spec"
    """
    Mass spectrometry data
    """
    sequencing = "sequencing"
    """
    Sequencing reads
    """
    tabular = "tabular"
    """
    Tabular/numeric data
    """


class AutomationLevelEnum(str, Enum):
    """
    Level of automation in data processing and analysis.
    """
    manual = "manual"
    """
    Fully manual analysis
    """
    semi_automated = "semi_automated"
    """
    Partially automated with manual verification
    """
    fully_automated = "fully_automated"
    """
    Fully automated pipeline
    """
    ai_assisted = "ai_assisted"
    """
    AI/ML-assisted analysis with human oversight
    """


class DataTransformationEnum(str, Enum):
    """
    Mathematical transformations applied to data.
    """
    none = "none"
    """
    No transformation applied
    """
    log10 = "log10"
    """
    Log base 10 transformation
    """
    log2 = "log2"
    """
    Log base 2 transformation
    """
    natural_log = "natural_log"
    """
    Natural logarithm transformation
    """
    square_root = "square_root"
    """
    Square root transformation
    """
    arcsine = "arcsine"
    """
    Arcsine transformation (for proportions)
    """
    box_cox = "box_cox"
    """
    Box-Cox transformation
    """
    inverse = "inverse"
    """
    Inverse transformation
    """
    z_transform = "z_transform"
    """
    Z-score transformation
    """


class ReplicateCombinationMethodEnum(str, Enum):
    """
    Methods for combining replicate measurements.
    """
    mean = "mean"
    """
    Arithmetic mean of replicates
    """
    median = "median"
    """
    Median of replicates
    """
    weighted_mean = "weighted_mean"
    """
    Weighted mean based on quality scores
    """
    geometric_mean = "geometric_mean"
    """
    Geometric mean of replicates
    """
    fitted_model = "fitted_model"
    """
    Value from fitted statistical model
    """
    surface_fit = "surface_fit"
    """
    Fitted surface model for spatial data
    """
    best_replicate = "best_replicate"
    """
    Best quality replicate selected
    """
    sum = "sum"
    """
    Sum of replicate values
    """



class Container(ConfiguredBaseModel):
    """
    A container for collections of measurements and related entities. Used as the root class for data validation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'tree_root': True})

    studies: Optional[list[Study]] = Field(default=[], description="""Collection of research studies in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    cohorts: Optional[list[Cohort]] = Field(default=[], description="""Collection of study cohorts in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    participants: Optional[list[Participant]] = Field(default=[], description="""Collection of study participants in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    exposure_measurements: Optional[list[ExposureMeasurement]] = Field(default=[], description="""Collection of exposure measurements in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    biomarker_measurements: Optional[list[BiomarkerMeasurement]] = Field(default=[], description="""Collection of biomarker measurements in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    phenotype_measurements: Optional[list[PhenotypeMeasurement]] = Field(default=[], description="""Collection of phenotype measurements in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    aggregated_measurements: Optional[list[AggregatedMeasurement]] = Field(default=[], description="""Collection of aggregated or summary measurements in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    gene_expression_measurements: Optional[list[GeneExpressionMeasurement]] = Field(default=[], description="""Collection of gene expression measurements in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    protein_expression_measurements: Optional[list[ProteinExpressionMeasurement]] = Field(default=[], description="""Collection of protein expression measurements in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    chemical_exposures: Optional[list[ChemicalExposure]] = Field(default=[], description="""Collection of chemical exposure events in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    dietary_exposures: Optional[list[DietaryExposure]] = Field(default=[], description="""Collection of dietary exposure events in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    environmental_exposures: Optional[list[EnvironmentalExposure]] = Field(default=[], description="""Collection of environmental exposure events in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    occupational_exposures: Optional[list[OccupationalExposure]] = Field(default=[], description="""Collection of occupational exposure events in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    phenotypes: Optional[list[Phenotype]] = Field(default=[], description="""Collection of phenotypes in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    diseases: Optional[list[Disease]] = Field(default=[], description="""Collection of diseases in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    adverse_outcomes: Optional[list[AdverseOutcome]] = Field(default=[], description="""Collection of adverse outcomes in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    adverse_outcome_pathways: Optional[list[AdverseOutcomePathway]] = Field(default=[], description="""Collection of adverse outcome pathways in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    genes: Optional[list[Gene]] = Field(default=[], description="""Collection of genes in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    proteins: Optional[list[Protein]] = Field(default=[], description="""Collection of proteins in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    cell_types: Optional[list[CellType]] = Field(default=[], description="""Collection of cell types in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    anatomical_entities: Optional[list[AnatomicalEntity]] = Field(default=[], description="""Collection of anatomical entities in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    organisms: Optional[list[Organism]] = Field(default=[], description="""Collection of organisms in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    exposure_to_phenotype_associations: Optional[list[ExposureToPhenotypeAssociation]] = Field(default=[], description="""Collection of exposure-to-phenotype associations in the container.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    states: Optional[list[State]] = Field(default=[], description="""U.S. states or territories with their geographic hierarchies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    public_use_microdata_areas: Optional[list[PublicUseMicrodataArea]] = Field(default=[], description="""Public Use Microdata Areas (PUMAs) within a state. PUMAs are non-overlapping statistical geographic areas containing no fewer than 100,000 people each.""", json_schema_extra = { "linkml_meta": {'aliases': ['pumas'], 'domain_of': ['Container', 'State']} })
    counties: Optional[list[County]] = Field(default=[], description="""Counties within a state or geographic region.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'State']} })
    census_tracts: Optional[list[CensusTract]] = Field(default=[], description="""Census tracts within a county.""", json_schema_extra = { "linkml_meta": {'aliases': ['tracts'], 'domain_of': ['Container', 'County']} })
    block_groups: Optional[list[BlockGroup]] = Field(default=[], description="""Block groups within a census tract.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CensusTract']} })
    households: Optional[list[Household]] = Field(default=[], description="""Households within a block group or geographic area.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'BlockGroup']} })
    persons: Optional[list[Person]] = Field(default=[], description="""Persons (individuals) in the container. Can be used for top-level person collections or for linking persons to study participants.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    schools: Optional[list[School]] = Field(default=[], description="""Schools where synthetic population persons may be assigned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    cellular_systems: Optional[list[CellularSystem]] = Field(default=[], description="""Collection of cellular systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    two_d_cell_cultures: Optional[list[TwoDCellCulture]] = Field(default=[], description="""Collection of 2D cell cultures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    three_d_cell_cultures: Optional[list[ThreeDCellCulture]] = Field(default=[], description="""Collection of 3D cell cultures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    co_cultures: Optional[list[CoCulture]] = Field(default=[], description="""Collection of co-cultures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    cell_lines: Optional[list[CellLine]] = Field(default=[], description="""Collection of cell lines.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    environmental_measurements: Optional[list[EnvironmentalMeasurement]] = Field(default=[], description="""Collection of environmental condition measurements (CO2, O2, temperature, humidity, pH) for the culture system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CellCultureConditions', 'CellularSystem']} })
    mechanical_measurements: Optional[list[MechanicalMeasurement]] = Field(default=[], description="""Collection of mechanical stimulation measurements (stretch, shear, flow) for advanced culture systems like organ-on-chip.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CellularSystem']} })
    in_vitro_exposures: Optional[list[InVitroExposure]] = Field(default=[], description="""Collection of in vitro exposure events.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    exposure_materials: Optional[list[ExposureMaterial]] = Field(default=[], description="""Collection of exposure materials/test articles.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    particle_properties_collection: Optional[list[ParticleProperties]] = Field(default=[], description="""Collection of particle property characterizations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    aerosol_generations: Optional[list[AerosolGeneration]] = Field(default=[], description="""Collection of aerosol generation specifications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    sample_preparations: Optional[list[SamplePreparation]] = Field(default=[], description="""Collection of sample preparation protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    analyses: Optional[list[Analysis]] = Field(default=[], description="""Collection of data analysis specifications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })


class NamedThing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity in the exposome
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Unit(NamedThing):
    """
    A unit of measurement from a standard ontology (UO, UCUM, QUDT)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'id_prefixes': ['UO', 'UCUM', 'qudt']})

    unit_label: Optional[str] = Field(default=None, description="""A human-readable label for the unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class QuantityValue(ConfiguredBaseModel):
    """
    A quantity with a numeric value and unit of measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fhir:Quantity',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    unit: Optional[Unit] = Field(default=None, description="""The unit of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })
    value: Optional[str] = Field(default=None, description="""The numeric value of the quantity""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })


class QuantityRange(ConfiguredBaseModel):
    """
    A range of quantities with lower and upper bounds
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fhir:Range',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    lower_bound: Optional[QuantityValue] = Field(default=None, description="""The lower bound of the range""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityRange']} })
    upper_bound: Optional[QuantityValue] = Field(default=None, description="""The upper bound of the range""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityRange']} })


class OntologyTerm(NamedThing):
    """
    A reference to an ontology term with both identifier and human-readable name. Used for measured entities, phenotypes, and other ontology-backed concepts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Tissue(NamedThing):
    """
    A reference to an anatomical tissue or structure with identifier and name. Used for tissue_context in expression measurements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class BiologicalEntity(NamedThing):
    """
    Biological entities including genes, proteins, cells, and anatomical structures
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ChemicalEntity(NamedThing):
    """
    A chemical entity including compounds, drugs, and metabolites
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHEBI:24431',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    chebi_id: Optional[str] = Field(default=None, description="""ChEBI identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    dtxsid: Optional[str] = Field(default=None, description="""EPA CompTox Dashboard identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    chembl_id: Optional[str] = Field(default=None, description="""ChEMBL compound identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    pubchem_cid: Optional[int] = Field(default=None, description="""PubChem Compound identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    cas_number: Optional[str] = Field(default=None, description="""CAS Registry Number""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    inchi: Optional[str] = Field(default=None, description="""InChI chemical identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    smiles: Optional[str] = Field(default=None, description="""SMILES chemical structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    molecular_formula: Optional[str] = Field(default=None, description="""Molecular formula""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('chebi_id')
    def pattern_chebi_id(cls, v):
        pattern=re.compile(r"^CHEBI:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid chebi_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid chebi_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('dtxsid')
    def pattern_dtxsid(cls, v):
        pattern=re.compile(r"^DTXSID\d{7,9}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid dtxsid format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid dtxsid format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('chembl_id')
    def pattern_chembl_id(cls, v):
        pattern=re.compile(r"^CHEMBL\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid chembl_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid chembl_id format: {v}"
            raise ValueError(err_msg)
        return v


class ExposureEvent(NamedThing):
    """
    An event in which an organism is exposed to a chemical or environmental factor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    exposed_subject: Optional[ExposableSubject] = Field(default=None, description="""The subject being exposed to a substance or environmental factor. Can be either a model system (cell culture, organoid) or a study participant. This polymorphic slot enables unified exposure tracking across in vitro and population-based studies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposed_to_chemical: Optional[ChemicalEntity] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class BiologicalResponse(NamedThing):
    """
    A biological response at the molecular, cellular, or tissue level
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class HealthOutcome(NamedThing):
    """
    A health-related outcome including phenotypes and diseases
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ExposableSubject(NamedThing):
    """
    An entity that can be exposed to a substance or environmental factor. This abstract class provides a common parent for both biological model systems (cell cultures, organoids) and study participants, enabling polymorphic linking from ExposureEvent to any exposable subject.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class StudyEntity(NamedThing):
    """
    Entities related to studies, cohorts, and participants
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Measurement(NamedThing):
    """
    A measurement observation with a typed quantity value and optional reference ranges
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented. This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Association(NamedThing):
    """
    A relationship between two entities
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ChemicalExposure(ExposureEvent):
    """
    Exposure to a chemical substance
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:0000006',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    exposed_subject: Optional[ExposableSubject] = Field(default=None, description="""The subject being exposed to a substance or environmental factor. Can be either a model system (cell culture, organoid) or a study participant. This polymorphic slot enables unified exposure tracking across in vitro and population-based studies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposed_to_chemical: Optional[ChemicalEntity] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class DietaryExposure(ExposureEvent):
    """
    Exposure through dietary consumption
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'FOODON:00002403',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    food_item: Optional[str] = Field(default=None, description="""Food item consumed""", json_schema_extra = { "linkml_meta": {'domain_of': ['DietaryExposure']} })
    serving_size: Optional[str] = Field(default=None, description="""Serving size""", json_schema_extra = { "linkml_meta": {'domain_of': ['DietaryExposure']} })
    exposed_subject: Optional[ExposableSubject] = Field(default=None, description="""The subject being exposed to a substance or environmental factor. Can be either a model system (cell culture, organoid) or a study participant. This polymorphic slot enables unified exposure tracking across in vitro and population-based studies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposed_to_chemical: Optional[ChemicalEntity] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class EnvironmentalExposure(ExposureEvent):
    """
    Exposure to environmental factors
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:0000001',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    environmental_context: Optional[str] = Field(default=None, description="""Environmental context of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnvironmentalExposure']} })
    exposed_subject: Optional[ExposableSubject] = Field(default=None, description="""The subject being exposed to a substance or environmental factor. Can be either a model system (cell culture, organoid) or a study participant. This polymorphic slot enables unified exposure tracking across in vitro and population-based studies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposed_to_chemical: Optional[ChemicalEntity] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class OccupationalExposure(ExposureEvent):
    """
    Exposure in an occupational setting
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:0000002',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    occupation: Optional[str] = Field(default=None, description="""Occupation related to exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['OccupationalExposure']} })
    workplace: Optional[str] = Field(default=None, description="""Workplace where exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['OccupationalExposure']} })
    exposed_subject: Optional[ExposableSubject] = Field(default=None, description="""The subject being exposed to a substance or environmental factor. Can be either a model system (cell culture, organoid) or a study participant. This polymorphic slot enables unified exposure tracking across in vitro and population-based studies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposed_to_chemical: Optional[ChemicalEntity] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Phenotype(HealthOutcome):
    """
    An observable characteristic or trait
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'UPHENO:0001001',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'id_prefixes': ['HP', 'UPHENO', 'MP', 'ZP']})

    severity: Optional[str] = Field(default=None, description="""Severity of phenotype or disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    onset_age: Optional[str] = Field(default=None, description="""Age of onset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Disease(HealthOutcome):
    """
    A disease or medical condition
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'MONDO:0000001',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    disease_category: Optional[str] = Field(default=None, description="""Category of disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    affected_anatomy: Optional[AnatomicalEntity] = Field(default=None, description="""Anatomical location affected""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class AdverseOutcome(HealthOutcome):
    """
    An adverse health outcome in the context of an Adverse Outcome Pathway
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    outcome_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""Level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcome']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class AdverseOutcomePathway(NamedThing):
    """
    A sequence of causally linked events at different levels of biological organization that lead from exposure to adverse health outcomes
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    aopwiki_id: Optional[str] = Field(default=None, description="""AOP Wiki identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    molecular_initiating_event: Optional[str] = Field(default=None, description="""The molecular initiating event of an AOP""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    key_events: Optional[list[str]] = Field(default=[], description="""Key events in an AOP""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    key_event_relationships: Optional[list[str]] = Field(default=[], description="""Relationships between key events""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    adverse_outcome: Optional[str] = Field(default=None, description="""The adverse outcome of an AOP""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    stressors: Optional[list[str]] = Field(default=[], description="""Chemical stressors that trigger the AOP""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class MolecularInitiatingEvent(BiologicalResponse):
    """
    The initial molecular-level perturbation that starts an Adverse Outcome Pathway
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:3000000',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    biological_process: Optional[str] = Field(default=None, description="""Biological process involved""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    biological_object: Optional[str] = Field(default=None, description="""Biological object involved""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    biological_action: Optional[str] = Field(default=None, description="""Biological action or change""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    occurs_in_cell_type: Optional[str] = Field(default=None, description="""Cell type where event occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent'],
         'slot_uri': 'CL:0000000'} })
    occurs_in_anatomy: Optional[str] = Field(default=None, description="""Anatomical location where event occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent'],
         'slot_uri': 'UBERON:0001062'} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class KeyEvent(BiologicalResponse):
    """
    A measurable change in biological state that is a step in an Adverse Outcome Pathway
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:1000000',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    biological_process: Optional[str] = Field(default=None, description="""Biological process involved""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    biological_object: Optional[str] = Field(default=None, description="""Biological object involved""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    biological_action: Optional[str] = Field(default=None, description="""Biological action or change""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    level_of_biological_organization: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""Level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    occurs_in_cell_type: Optional[str] = Field(default=None, description="""Cell type where event occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent'],
         'slot_uri': 'CL:0000000'} })
    occurs_in_anatomy: Optional[str] = Field(default=None, description="""Anatomical location where event occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent'],
         'slot_uri': 'UBERON:0001062'} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class KeyEventRelationship(Association):
    """
    A directional relationship between two key events in an AOP
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    upstream_event: Optional[str] = Field(default=None, description="""Upstream key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    downstream_event: Optional[str] = Field(default=None, description="""Downstream key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    relationship_type: Optional[str] = Field(default=None, description="""Type of relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    evidence_support: Optional[str] = Field(default=None, description="""Evidence supporting the relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Study(StudyEntity):
    """
    A research study or survey
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'EFO:0001444',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    study_type: Optional[StudyTypeEnum] = Field(default=None, description="""Type of study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    population: Optional[str] = Field(default=None, description="""Study population description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    enrollment_period: Optional[str] = Field(default=None, description="""Time period of enrollment""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    geographic_location: Optional[str] = Field(default=None, description="""Geographic location of study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    principal_investigator: Optional[str] = Field(default=None, description="""Principal investigator name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    publications: Optional[list[str]] = Field(default=[], description="""Related publications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Cohort(StudyEntity):
    """
    A group of individuals in a study
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    part_of_study: Optional[Study] = Field(default=None, description="""Study that this cohort is part of.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })
    cohort_size: Optional[int] = Field(default=None, description="""Number of participants in cohort""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })
    inclusion_criteria: Optional[str] = Field(default=None, description="""Criteria for cohort inclusion""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Participant(StudyEntity, ExposableSubject):
    """
    A role representing an individual's participation in a study. Links a Person to a specific study cohort and captures study-specific identifiers and attributes. Age and sex are recorded at enrollment and may differ from the Person's current values or values in other study registrations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'mixins': ['ExposableSubject'],
         'slot_usage': {'age': {'description': 'Age of the participant in years at the '
                                               'time of study enrollment. This is a '
                                               'study-specific value that may differ '
                                               'from other study registrations or the '
                                               "person's current age.",
                                'name': 'age'},
                        'sex': {'description': 'Biological sex of the participant as '
                                               'recorded at study enrollment. This is '
                                               'the value captured during study '
                                               'registration and may be used for '
                                               'stratification or eligibility '
                                               'criteria.',
                                'name': 'sex'}}})

    person: Optional[str] = Field(default=None, description="""The person (individual) who is participating in this study. Links the study participation role to the actual individual.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    part_of_cohort: Optional[Cohort] = Field(default=None, description="""Cohort that this participant is part of.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant'], 'slot_uri': 'biolink:member_of'} })
    participant_id: Optional[str] = Field(default=None, description="""Participant identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    age: Optional[int] = Field(default=None, description="""Age of the participant in years at the time of study enrollment. This is a study-specific value that may differ from other study registrations or the person's current age.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant', 'Person']} })
    sex: Optional[SexEnum] = Field(default=None, description="""Biological sex of the participant as recorded at study enrollment. This is the value captured during study registration and may be used for stratification or eligibility criteria.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant', 'Person']} })
    enrollment_date: Optional[date] = Field(default=None, description="""Date when the person enrolled in the study as a participant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    withdrawal_date: Optional[date] = Field(default=None, description="""Date when the participant withdrew from or completed the study. Null if participant is still active.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    study_arm: Optional[str] = Field(default=None, description="""Study arm or group to which the participant was assigned (e.g., treatment, control, placebo).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ExposureMeasurement(Measurement):
    """
    A measurement of exposure to a chemical or environmental factor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    measured_entity: Optional[OntologyTerm] = Field(default=None, description="""The entity being measured, with both identifier and human-readable name. Examples: chemical compounds (CHEBI), cell types (CL), biological processes (GO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AggregatedMeasurement']} })
    participant: Optional[Participant] = Field(default=None, description="""The participant being measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Method used for measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement', 'BiomarkerMeasurement']} })
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented. This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class BiomarkerMeasurement(Measurement):
    """
    A measurement of a biological marker
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    biomarker_type: Optional[str] = Field(default=None, description="""Type of biomarker""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiomarkerMeasurement']} })
    measured_entity: Optional[OntologyTerm] = Field(default=None, description="""The entity being measured, with both identifier and human-readable name. Examples: chemical compounds (CHEBI), cell types (CL), biological processes (GO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AggregatedMeasurement']} })
    participant: Optional[Participant] = Field(default=None, description="""The participant being measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement', 'BiomarkerMeasurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Method used for measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented. This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class PhenotypeMeasurement(Measurement):
    """
    A measurement of a phenotypic trait or functional assay
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    phenotype: Optional[OntologyTerm] = Field(default=None, description="""The phenotype being measured, with identifier and name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeMeasurement', 'ExposureToPhenotypeAssociation']} })
    measured_entity: Optional[OntologyTerm] = Field(default=None, description="""The entity being measured, with both identifier and human-readable name. Examples: chemical compounds (CHEBI), cell types (CL), biological processes (GO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AggregatedMeasurement']} })
    participant: Optional[Participant] = Field(default=None, description="""The participant being measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Method used for measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented. This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class AggregatedMeasurement(Measurement):
    """
    An aggregated or summary measurement across a cohort or population
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    measured_entity: Optional[OntologyTerm] = Field(default=None, description="""The entity being measured, with both identifier and human-readable name. Examples: chemical compounds (CHEBI), cell types (CL), biological processes (GO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AggregatedMeasurement']} })
    cohort: Optional[Cohort] = Field(default=None, description="""The cohort for aggregated measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    summary_statistic: Optional[SummaryStatisticEnum] = Field(default=None, description="""Type of summary statistic""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    sample_size: Optional[int] = Field(default=None, description="""Number of samples""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    stratification: Optional[str] = Field(default=None, description="""Stratification variables""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented. This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class GeneExpressionMeasurement(Measurement):
    """
    A measurement of gene expression (mRNA level) in a specific biological context. Captures the target gene, tissue/cell type context, and assay methodology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    target_gene: Optional[Gene] = Field(default=None, description="""The gene whose expression is being measured, with identifier, name, and symbol. Use this to specify the exact gene target (e.g., MUC5AC, EGFR, IL8).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement']} })
    tissue_context: Optional[Tissue] = Field(default=None, description="""The anatomical tissue or structure where expression was measured, with identifier and name (e.g., bronchial epithelium, lung, nasal mucosa).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    cell_type_context: Optional[CellType] = Field(default=None, description="""The specific cell type where expression was measured, with identifier and name (e.g., goblet cell, ciliated cell, basal cell).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    assay_method: Optional[ExpressionAssayMethodEnum] = Field(default=None, description="""The experimental method used to measure expression. Captures whether this was qRT-PCR, RNA-seq, Western blot, IHC, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    normalization_reference: Optional[str] = Field(default=None, description="""The reference gene or protein used for normalization (e.g., GAPDH, beta-actin, 18S rRNA, total protein).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    participant: Optional[Participant] = Field(default=None, description="""The participant being measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented. This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ProteinExpressionMeasurement(Measurement):
    """
    A measurement of protein expression or post-translational modification (e.g., phosphorylation) in a specific biological context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    target_protein: Optional[Protein] = Field(default=None, description="""The protein whose expression or modification is being measured, with identifier, name, and optionally the encoding gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinExpressionMeasurement']} })
    phosphorylation_site: Optional[str] = Field(default=None, description="""For protein phosphorylation measurements, the specific amino acid residue that is phosphorylated (e.g., Y1068, S473, T308).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinExpressionMeasurement']} })
    tissue_context: Optional[Tissue] = Field(default=None, description="""The anatomical tissue or structure where expression was measured, with identifier and name (e.g., bronchial epithelium, lung, nasal mucosa).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    cell_type_context: Optional[CellType] = Field(default=None, description="""The specific cell type where expression was measured, with identifier and name (e.g., goblet cell, ciliated cell, basal cell).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    assay_method: Optional[ExpressionAssayMethodEnum] = Field(default=None, description="""The experimental method used to measure expression. Captures whether this was qRT-PCR, RNA-seq, Western blot, IHC, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    normalization_reference: Optional[str] = Field(default=None, description="""The reference gene or protein used for normalization (e.g., GAPDH, beta-actin, 18S rRNA, total protein).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    participant: Optional[Participant] = Field(default=None, description="""The participant being measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented. This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class EnvironmentalMeasurement(Measurement):
    """
    A measurement of environmental conditions for cell culture systems including temperature, CO2, O2 percentage, humidity, and pH. Used to document incubator and culture conditions. Valid observation_type values include: co2_percentage, o2_percentage, temperature, humidity, nitrogen_balance, ph.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented. This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class MechanicalMeasurement(Measurement):
    """
    A measurement of mechanical stimulation parameters for advanced culture systems like organ-on-chip and microphysiological systems. Includes stretch frequency/amplitude, shear stress, flow rate, and pressure. Valid observation_type values include: stretch_frequency, stretch_amplitude, shear_stress, flow_rate, perfusion_rate, pressure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented. This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class MembranePropertyMeasurement(Measurement):
    """
    A measurement of membrane properties for transwell, ALI, and organ-on-chip culture systems. Includes pore size, pore density, thickness, surface area, and TEER. Valid observation_type values include: pore_size, pore_density, thickness, surface_area, teer.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    membrane_material: Optional[str] = Field(default=None, description="""Material of the porous membrane (e.g., PET, polycarbonate, PDMS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MembranePropertyMeasurement']} })
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented. This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[QuantityValue] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[QuantityValue] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[QuantityValue] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class CellLine(NamedThing):
    """
    A cell line - a genetically stable cultured cell population that contains individual cell line cells. Reference to a specific cell line with identifiers from cell line repositories.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CLO:0000031',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'id_prefixes': ['CLO']})

    cell_culture_type: Optional[CellType] = Field(default=None, description="""The cell type being cultured, with ontology reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'CellularSystem'], 'slot_uri': 'EFO:0000324'} })
    model_species: Optional[Organism] = Field(default=None, description="""The species of origin for the cells in the model system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'ModelSystem']} })
    tissue_origin: Optional[AnatomicalEntity] = Field(default=None, description="""Tissue from which the cell line was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine']} })
    disease_state: Optional[Disease] = Field(default=None, description="""Disease state of the cell line donor (if applicable).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine']} })
    supplier: Optional[str] = Field(default=None, description="""Supplier or repository of the cell line (e.g., ATCC, Coriell).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine']} })
    catalog_number: Optional[str] = Field(default=None, description="""Catalog number from manufacturer.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine',
                       'CellCultureMedium',
                       'MediumSupplement',
                       'ExposureMaterial']} })
    authentication_method: Optional[str] = Field(default=None, description="""Method used to authenticate the cell line (e.g., STR profiling).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine']} })
    mycoplasma_status: Optional[str] = Field(default=None, description="""Mycoplasma testing status (positive, negative, not tested).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class CellCultureConditions(NamedThing):
    """
    Detailed cell culture parameters including medium, environment, and timing.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['CLO:0037334'],
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    culture_media: Optional[CellCultureMedium] = Field(default=None, description="""Cell culture medium formulation with supplements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'CellularSystem']} })
    days_at_air_liquid_interface: Optional[int] = Field(default=None, description="""Number of days cells have been cultured at air-liquid interface (ALI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions']} })
    passage_number: Optional[int] = Field(default=None, description="""Cell passage number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'TwoDCellCulture'],
         'exact_mappings': ['CLO:0000170']} })
    substrate_type: Optional[SubstrateTypeEnum] = Field(default=None, description="""Type of culture substrate or surface material.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions',
                       'TwoDCellCulture',
                       'ThreeDCellCulture',
                       'CoCulture']} })
    cell_culture_growth_mode: Optional[CellCultureGrowthModeEnum] = Field(default=None, description="""Mode of cell culture growth (adherent, suspension, ALI, 3D, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'CellularSystem'],
         'exact_mappings': ['CLO:0000030']} })
    environmental_measurements: Optional[list[EnvironmentalMeasurement]] = Field(default=[], description="""Collection of environmental condition measurements (CO2, O2, temperature, humidity, pH) for the culture system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CellCultureConditions', 'CellularSystem']} })
    donor_count: Optional[int] = Field(default=None, description="""Number of unique cell donors used in the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of biological replicates per donor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class CellCultureMedium(NamedThing):
    """
    Detailed formulation of cell culture medium including base medium and supplements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    base_medium: Optional[str] = Field(default=None, description="""Base medium type (e.g., DMEM, RPMI 1640, Ham's F-12, BEGM).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    serum_type: Optional[str] = Field(default=None, description="""Type of serum used (e.g., FBS, human serum, serum-free).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    serum_concentration: Optional[QuantityValue] = Field(default=None, description="""Serum concentration as percentage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    supplements: Optional[list[MediumSupplement]] = Field(default=[], description="""List of medium supplements with concentrations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    osmolality: Optional[QuantityValue] = Field(default=None, description="""Osmolality of the medium in mOsm/kg.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    manufacturer: Optional[str] = Field(default=None, description="""Manufacturer of the product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium', 'MediumSupplement', 'ExposureMaterial']} })
    catalog_number: Optional[str] = Field(default=None, description="""Catalog number from manufacturer.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine',
                       'CellCultureMedium',
                       'MediumSupplement',
                       'ExposureMaterial']} })
    lot_number: Optional[str] = Field(default=None, description="""Lot or batch number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    preparation_date: Optional[date] = Field(default=None, description="""Date when medium was prepared.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class MediumSupplement(NamedThing):
    """
    Supplement or additive to cell culture medium.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    supplement_type: Optional[SupplementTypeEnum] = Field(default=None, description="""Category of supplement (growth factor, antibiotic, hormone, vitamin, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MediumSupplement']} })
    supplement_entity: Optional[ChemicalEntity] = Field(default=None, description="""The chemical entity representing the supplement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MediumSupplement']} })
    concentration: Optional[QuantityValue] = Field(default=None, description="""Concentration of supplement or reagent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MediumSupplement']} })
    manufacturer: Optional[str] = Field(default=None, description="""Manufacturer of the product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium', 'MediumSupplement', 'ExposureMaterial']} })
    catalog_number: Optional[str] = Field(default=None, description="""Catalog number from manufacturer.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine',
                       'CellCultureMedium',
                       'MediumSupplement',
                       'ExposureMaterial']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ModelSystem(ExposableSubject):
    """
    Abstract base class for model systems used in biomedical research. Encompasses cellular systems, microphysiological systems, and in silico models.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'NAMO:0000000',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    model_species: Optional[Organism] = Field(default=None, description="""The species of origin for the cells in the model system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class CellularSystem(ModelSystem):
    """
    Cell-based model systems that use living cells to model biological processes. Includes 2D cultures, 3D systems, and co-cultures. Abstract base class for specific culture types.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'NAMO:0000001',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    cell_line: Optional[CellLine] = Field(default=None, description="""The cell line used in the culture system. References a genetically stable cultured cell population.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem'], 'slot_uri': 'CLO:0000031'} })
    cell_line_lineage: Optional[str] = Field(default=None, description="""The lineage or derivation history of the cell line, including original tissue source and passage history.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    primary_cultured_cell: Optional[CellType] = Field(default=None, description="""Primary cells directly isolated from tissue, not from an established cell line. Reference to Cell Ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    cell_culture_type: Optional[CellType] = Field(default=None, description="""The cell type being cultured, with ontology reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'CellularSystem'], 'slot_uri': 'EFO:0000324'} })
    anatomical_origin: Optional[AnatomicalEntity] = Field(default=None, description="""The anatomical location from which cells were derived (e.g., lung, intestine).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem'], 'slot_uri': 'UBERON:0001062'} })
    cell_culture_growth_mode: Optional[CellCultureGrowthModeEnum] = Field(default=None, description="""Mode of cell culture growth (adherent, suspension, ALI, 3D, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'CellularSystem'],
         'exact_mappings': ['CLO:0000030']} })
    cell_line_modification: Optional[CellLineModificationEnum] = Field(default=None, description="""Genetic or other modifications applied to the cell line (e.g., transfection, CRISPR editing, viral transduction).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    induced_pluripotent_stem_cell_line: Optional[bool] = Field(default=None, description="""Whether this is an induced pluripotent stem cell (iPSC) line.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem'], 'exact_mappings': ['CLO:0037307']} })
    culture_conditions: Optional[CellCultureConditions] = Field(default=None, description="""Detailed cell culture conditions including medium, environment, and timing.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    culture_media: Optional[CellCultureMedium] = Field(default=None, description="""Cell culture medium formulation with supplements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'CellularSystem']} })
    environmental_measurements: Optional[list[EnvironmentalMeasurement]] = Field(default=[], description="""Collection of environmental condition measurements (CO2, O2, temperature, humidity, pH) for the culture system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CellCultureConditions', 'CellularSystem']} })
    mechanical_measurements: Optional[list[MechanicalMeasurement]] = Field(default=[], description="""Collection of mechanical stimulation measurements (stretch, shear, flow) for advanced culture systems like organ-on-chip.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CellularSystem']} })
    membrane_properties: Optional[list[MembranePropertyMeasurement]] = Field(default=[], description="""Collection of membrane property measurements (pore size, TEER) for transwell and organ-on-chip systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    model_species: Optional[Organism] = Field(default=None, description="""The species of origin for the cells in the model system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class TwoDCellCulture(CellularSystem):
    """
    Conventional monolayer cell cultures grown on flat surfaces. Includes adherent and suspension cultures in standard tissue culture vessels.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'NAMO:0000002',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'id_prefixes': ['owg']})

    substrate_type: Optional[SubstrateTypeEnum] = Field(default=None, description="""Type of culture substrate or surface material.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions',
                       'TwoDCellCulture',
                       'ThreeDCellCulture',
                       'CoCulture']} })
    confluence_level: Optional[QuantityValue] = Field(default=None, description="""Confluence level of adherent culture as percentage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TwoDCellCulture']} })
    passage_number: Optional[int] = Field(default=None, description="""Cell passage number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'TwoDCellCulture'],
         'exact_mappings': ['CLO:0000170']} })
    seeding_density: Optional[QuantityValue] = Field(default=None, description="""Cell seeding density (cells per cm2 or per mL).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TwoDCellCulture']} })
    coating: Optional[str] = Field(default=None, description="""Surface coating applied to membrane or substrate.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TwoDCellCulture']} })
    cell_line: Optional[CellLine] = Field(default=None, description="""The cell line used in the culture system. References a genetically stable cultured cell population.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem'], 'slot_uri': 'CLO:0000031'} })
    cell_line_lineage: Optional[str] = Field(default=None, description="""The lineage or derivation history of the cell line, including original tissue source and passage history.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    primary_cultured_cell: Optional[CellType] = Field(default=None, description="""Primary cells directly isolated from tissue, not from an established cell line. Reference to Cell Ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    cell_culture_type: Optional[CellType] = Field(default=None, description="""The cell type being cultured, with ontology reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'CellularSystem'], 'slot_uri': 'EFO:0000324'} })
    anatomical_origin: Optional[AnatomicalEntity] = Field(default=None, description="""The anatomical location from which cells were derived (e.g., lung, intestine).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem'], 'slot_uri': 'UBERON:0001062'} })
    cell_culture_growth_mode: Optional[CellCultureGrowthModeEnum] = Field(default=None, description="""Mode of cell culture growth (adherent, suspension, ALI, 3D, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'CellularSystem'],
         'exact_mappings': ['CLO:0000030']} })
    cell_line_modification: Optional[CellLineModificationEnum] = Field(default=None, description="""Genetic or other modifications applied to the cell line (e.g., transfection, CRISPR editing, viral transduction).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    induced_pluripotent_stem_cell_line: Optional[bool] = Field(default=None, description="""Whether this is an induced pluripotent stem cell (iPSC) line.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem'], 'exact_mappings': ['CLO:0037307']} })
    culture_conditions: Optional[CellCultureConditions] = Field(default=None, description="""Detailed cell culture conditions including medium, environment, and timing.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    culture_media: Optional[CellCultureMedium] = Field(default=None, description="""Cell culture medium formulation with supplements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'CellularSystem']} })
    environmental_measurements: Optional[list[EnvironmentalMeasurement]] = Field(default=[], description="""Collection of environmental condition measurements (CO2, O2, temperature, humidity, pH) for the culture system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CellCultureConditions', 'CellularSystem']} })
    mechanical_measurements: Optional[list[MechanicalMeasurement]] = Field(default=[], description="""Collection of mechanical stimulation measurements (stretch, shear, flow) for advanced culture systems like organ-on-chip.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CellularSystem']} })
    membrane_properties: Optional[list[MembranePropertyMeasurement]] = Field(default=[], description="""Collection of membrane property measurements (pore size, TEER) for transwell and organ-on-chip systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    model_species: Optional[Organism] = Field(default=None, description="""The species of origin for the cells in the model system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ThreeDCellCulture(CellularSystem):
    """
    Three-dimensional cell culture systems including spheroids, organoids, and scaffold-based cultures. Provides enhanced physiological relevance with 3D architecture.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'NAMO:0000003',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'id_prefixes': ['owg']})

    three_d_architecture: Optional[ThreeDArchitectureEnum] = Field(default=None, description="""Type of 3D culture architecture (spheroid, organoid, scaffold-based, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThreeDCellCulture']} })
    matrix_composition: Optional[str] = Field(default=None, description="""Composition of the 3D matrix or scaffold material (e.g., Matrigel, collagen, alginate, synthetic hydrogel).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThreeDCellCulture']} })
    size_range: Optional[QuantityRange] = Field(default=None, description="""Size range of 3D structures (diameter for spheroids/organoids).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThreeDCellCulture']} })
    organoid_type: Optional[str] = Field(default=None, description="""Specific type of organoid (e.g., intestinal, cerebral, lung, liver).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThreeDCellCulture']} })
    substrate_type: Optional[SubstrateTypeEnum] = Field(default=None, description="""Type of culture substrate or surface material.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions',
                       'TwoDCellCulture',
                       'ThreeDCellCulture',
                       'CoCulture']} })
    cell_line: Optional[CellLine] = Field(default=None, description="""The cell line used in the culture system. References a genetically stable cultured cell population.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem'], 'slot_uri': 'CLO:0000031'} })
    cell_line_lineage: Optional[str] = Field(default=None, description="""The lineage or derivation history of the cell line, including original tissue source and passage history.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    primary_cultured_cell: Optional[CellType] = Field(default=None, description="""Primary cells directly isolated from tissue, not from an established cell line. Reference to Cell Ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    cell_culture_type: Optional[CellType] = Field(default=None, description="""The cell type being cultured, with ontology reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'CellularSystem'], 'slot_uri': 'EFO:0000324'} })
    anatomical_origin: Optional[AnatomicalEntity] = Field(default=None, description="""The anatomical location from which cells were derived (e.g., lung, intestine).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem'], 'slot_uri': 'UBERON:0001062'} })
    cell_culture_growth_mode: Optional[CellCultureGrowthModeEnum] = Field(default=None, description="""Mode of cell culture growth (adherent, suspension, ALI, 3D, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'CellularSystem'],
         'exact_mappings': ['CLO:0000030']} })
    cell_line_modification: Optional[CellLineModificationEnum] = Field(default=None, description="""Genetic or other modifications applied to the cell line (e.g., transfection, CRISPR editing, viral transduction).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    induced_pluripotent_stem_cell_line: Optional[bool] = Field(default=None, description="""Whether this is an induced pluripotent stem cell (iPSC) line.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem'], 'exact_mappings': ['CLO:0037307']} })
    culture_conditions: Optional[CellCultureConditions] = Field(default=None, description="""Detailed cell culture conditions including medium, environment, and timing.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    culture_media: Optional[CellCultureMedium] = Field(default=None, description="""Cell culture medium formulation with supplements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'CellularSystem']} })
    environmental_measurements: Optional[list[EnvironmentalMeasurement]] = Field(default=[], description="""Collection of environmental condition measurements (CO2, O2, temperature, humidity, pH) for the culture system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CellCultureConditions', 'CellularSystem']} })
    mechanical_measurements: Optional[list[MechanicalMeasurement]] = Field(default=[], description="""Collection of mechanical stimulation measurements (stretch, shear, flow) for advanced culture systems like organ-on-chip.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CellularSystem']} })
    membrane_properties: Optional[list[MembranePropertyMeasurement]] = Field(default=[], description="""Collection of membrane property measurements (pore size, TEER) for transwell and organ-on-chip systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    model_species: Optional[Organism] = Field(default=None, description="""The species of origin for the cells in the model system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class CoCulture(CellularSystem):
    """
    Co-culture systems combining multiple cell types to simulate tissue microenvironments and cell-cell interactions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'NAMO:0000004',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'id_prefixes': ['owg']})

    coculture_configuration: Optional[CoCultureConfigurationEnum] = Field(default=None, description="""Physical configuration of co-culture (direct contact, transwell, microfluidic).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoCulture']} })
    cell_type_ratios: Optional[list[str]] = Field(default=[], description="""Ratios between different cell types in co-culture (e.g., \"epithelial:stromal = 3:1\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoCulture']} })
    substrate_type: Optional[SubstrateTypeEnum] = Field(default=None, description="""Type of culture substrate or surface material.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions',
                       'TwoDCellCulture',
                       'ThreeDCellCulture',
                       'CoCulture']} })
    cell_line: Optional[CellLine] = Field(default=None, description="""The cell line used in the culture system. References a genetically stable cultured cell population.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem'], 'slot_uri': 'CLO:0000031'} })
    cell_line_lineage: Optional[str] = Field(default=None, description="""The lineage or derivation history of the cell line, including original tissue source and passage history.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    primary_cultured_cell: Optional[CellType] = Field(default=None, description="""Primary cells directly isolated from tissue, not from an established cell line. Reference to Cell Ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    cell_culture_type: Optional[CellType] = Field(default=None, description="""The cell type being cultured, with ontology reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'CellularSystem'], 'slot_uri': 'EFO:0000324'} })
    anatomical_origin: Optional[AnatomicalEntity] = Field(default=None, description="""The anatomical location from which cells were derived (e.g., lung, intestine).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem'], 'slot_uri': 'UBERON:0001062'} })
    cell_culture_growth_mode: Optional[CellCultureGrowthModeEnum] = Field(default=None, description="""Mode of cell culture growth (adherent, suspension, ALI, 3D, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'CellularSystem'],
         'exact_mappings': ['CLO:0000030']} })
    cell_line_modification: Optional[CellLineModificationEnum] = Field(default=None, description="""Genetic or other modifications applied to the cell line (e.g., transfection, CRISPR editing, viral transduction).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    induced_pluripotent_stem_cell_line: Optional[bool] = Field(default=None, description="""Whether this is an induced pluripotent stem cell (iPSC) line.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem'], 'exact_mappings': ['CLO:0037307']} })
    culture_conditions: Optional[CellCultureConditions] = Field(default=None, description="""Detailed cell culture conditions including medium, environment, and timing.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    culture_media: Optional[CellCultureMedium] = Field(default=None, description="""Cell culture medium formulation with supplements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions', 'CellularSystem']} })
    environmental_measurements: Optional[list[EnvironmentalMeasurement]] = Field(default=[], description="""Collection of environmental condition measurements (CO2, O2, temperature, humidity, pH) for the culture system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CellCultureConditions', 'CellularSystem']} })
    mechanical_measurements: Optional[list[MechanicalMeasurement]] = Field(default=[], description="""Collection of mechanical stimulation measurements (stretch, shear, flow) for advanced culture systems like organ-on-chip.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CellularSystem']} })
    membrane_properties: Optional[list[MembranePropertyMeasurement]] = Field(default=[], description="""Collection of membrane property measurements (pore size, TEER) for transwell and organ-on-chip systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    model_species: Optional[Organism] = Field(default=None, description="""The species of origin for the cells in the model system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'ModelSystem']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ExposureMaterial(NamedThing):
    """
    Detailed specification of the test article or substance used in an exposure experiment. Extends chemical entity information with physical form, purity, and particle properties relevant for toxicology studies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    test_substance: Optional[ChemicalEntity] = Field(default=None, description="""The chemical entity being tested, with full identifier information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMaterial']} })
    chemical_form: Optional[ChemicalFormEnum] = Field(default=None, description="""Physical form of the test substance (solid, aerosol, solution, vapor, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMaterial']} })
    nominal_concentration: Optional[QuantityValue] = Field(default=None, description="""Nominal or intended concentration of the test substance as prepared.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMaterial']} })
    applied_dose: Optional[QuantityValue] = Field(default=None, description="""The dose applied to cells or tissue (may differ from nominal concentration).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMaterial']} })
    purity: Optional[QuantityValue] = Field(default=None, description="""Purity of the test substance as percentage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMaterial']} })
    composition: Optional[str] = Field(default=None, description="""Detailed composition of the test material, especially for complex mixtures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMaterial']} })
    vehicle_solvent: Optional[str] = Field(default=None, description="""Vehicle or solvent used to deliver the test substance (e.g., DMSO, PBS, culture medium).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMaterial']} })
    particle_properties: Optional[ParticleProperties] = Field(default=None, description="""Physical properties of particulate test materials.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMaterial']} })
    source_lot_number: Optional[str] = Field(default=None, description="""Lot number from the source/manufacturer of the test article.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMaterial']} })
    manufacturer: Optional[str] = Field(default=None, description="""Manufacturer of the product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium', 'MediumSupplement', 'ExposureMaterial']} })
    catalog_number: Optional[str] = Field(default=None, description="""Catalog number from manufacturer.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine',
                       'CellCultureMedium',
                       'MediumSupplement',
                       'ExposureMaterial']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ParticleProperties(NamedThing):
    """
    Physical and chemical properties of particulate test materials including nanoparticles, aerosols, and other particle-based exposures. Essential for characterizing inhaled toxicants and nanomaterials.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    particle_size: Optional[QuantityValue] = Field(default=None, description="""Primary particle size (e.g., diameter) in nanometers or micrometers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParticleProperties']} })
    particle_size_distribution: Optional[str] = Field(default=None, description="""Description of particle size distribution (e.g., monodisperse, polydisperse, D10/D50/D90 values).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParticleProperties']} })
    surface_area: Optional[QuantityValue] = Field(default=None, description="""Specific surface area of particles (e.g., m2/g by BET method).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParticleProperties']} })
    zeta_potential: Optional[QuantityValue] = Field(default=None, description="""Zeta potential in mV, indicating surface charge in the vehicle/medium.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParticleProperties']} })
    hydrodynamic_diameter: Optional[QuantityValue] = Field(default=None, description="""Hydrodynamic diameter measured by dynamic light scattering (DLS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParticleProperties']} })
    polydispersity_index: Optional[float] = Field(default=None, description="""Polydispersity index (PDI) from DLS, indicating size distribution width.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParticleProperties']} })
    particle_morphology: Optional[str] = Field(default=None, description="""Particle shape and morphology (e.g., spherical, rod, fiber, agglomerate).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParticleProperties']} })
    particle_composition: Optional[str] = Field(default=None, description="""Chemical composition of particles if different from bulk material.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParticleProperties']} })
    agglomeration_state: Optional[str] = Field(default=None, description="""State of agglomeration/aggregation in the exposure medium.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParticleProperties']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class InVitroExposure(ExposureEvent):
    """
    An in vitro exposure event describing how cells or tissues were exposed to a test substance. Captures exposure timing, frequency, aerosol generation parameters, and other in vitro-specific details.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    exposure_material: Optional[ExposureMaterial] = Field(default=None, description="""The test material used for the exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    exposure_frequency: Optional[str] = Field(default=None, description="""Frequency of exposure (e.g., single, daily, twice daily).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    exposure_regiment: Optional[ExposureRegimentEnum] = Field(default=None, description="""Type of exposure regiment (continuous, repeated, intermittent, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    time_post_exposure: Optional[QuantityValue] = Field(default=None, description="""Time elapsed between end of exposure and measurement (recovery period).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    exposure_temperature: Optional[QuantityValue] = Field(default=None, description="""Temperature during exposure in degrees Celsius.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    control_description: Optional[str] = Field(default=None, description="""Description of control conditions used in the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    control_type: Optional[ControlTypeEnum] = Field(default=None, description="""Type of control used (vehicle, untreated, positive, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    number_of_replicates: Optional[int] = Field(default=None, description="""Number of replicate wells/inserts/samples per condition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    effective_deposition: Optional[QuantityValue] = Field(default=None, description="""Actual amount of material deposited on cells (measured or calculated).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    deposited_dose: Optional[QuantityValue] = Field(default=None, description="""Dose that reached the cell surface (may be calculated from ISDD or measured).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    baseline_teer: Optional[QuantityValue] = Field(default=None, description="""Baseline TEER measurement before exposure, used to assess barrier integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    aerosol_generation: Optional[AerosolGeneration] = Field(default=None, description="""Parameters for aerosol generation (for inhalation studies).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    sample_preparation: Optional[SamplePreparation] = Field(default=None, description="""Pre-exposure sample preparation procedures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure']} })
    dose_normalization_method: Optional[DoseNormalizationMethodEnum] = Field(default=None, description="""Method used to normalize dose (per area, per cell count, per protein, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure', 'Analysis']} })
    exposed_subject: Optional[ExposableSubject] = Field(default=None, description="""The subject being exposed to a substance or environmental factor. Can be either a model system (cell culture, organoid) or a study participant. This polymorphic slot enables unified exposure tracking across in vitro and population-based studies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposed_to_chemical: Optional[ChemicalEntity] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class AerosolGeneration(NamedThing):
    """
    Parameters describing aerosol generation for inhalation toxicology studies. Includes generation method, equipment, and characterization of the generated aerosol for air-liquid interface and other exposure systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    aerosol_generation_method: Optional[AerosolGenerationMethodEnum] = Field(default=None, description="""Method used to generate the aerosol (nebulization, condensation, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AerosolGeneration']} })
    aerosol_generation_equipment: Optional[str] = Field(default=None, description="""Equipment used for aerosol generation (e.g., Vitrocell Cloud, ALICE, nebulizer type).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AerosolGeneration']} })
    aerosol_concentration: Optional[QuantityValue] = Field(default=None, description="""Concentration of aerosol in the exposure chamber or at the ALI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AerosolGeneration']} })
    aerosol_flow_rate: Optional[QuantityValue] = Field(default=None, description="""Flow rate of aerosol delivery system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AerosolGeneration']} })
    aerosol_exposure_duration: Optional[QuantityValue] = Field(default=None, description="""Duration of aerosol exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AerosolGeneration']} })
    mass_median_aerodynamic_diameter: Optional[QuantityValue] = Field(default=None, description="""Mass median aerodynamic diameter of generated aerosol particles.""", json_schema_extra = { "linkml_meta": {'aliases': ['MMAD'], 'domain_of': ['AerosolGeneration']} })
    geometric_standard_deviation: Optional[float] = Field(default=None, description="""Geometric standard deviation of aerosol particle size distribution.""", json_schema_extra = { "linkml_meta": {'aliases': ['GSD'], 'domain_of': ['AerosolGeneration']} })
    aerosol_characterization_method: Optional[str] = Field(default=None, description="""Methods used to characterize aerosol (e.g., APS, SMPS, impactor, gravimetric).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AerosolGeneration']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class SamplePreparation(NamedThing):
    """
    Pre-exposure sample preparation procedures for in vitro systems. Includes ASL-specific preparations like mucus removal and other treatments applied before exposure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    mucus_removal_performed: Optional[bool] = Field(default=None, description="""Whether mucus was removed from the apical surface before exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SamplePreparation']} })
    mucus_removal_method: Optional[str] = Field(default=None, description="""Method used to remove mucus (e.g., PBS wash, mucolytic agent, aspiration).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SamplePreparation']} })
    debris_removal_performed: Optional[bool] = Field(default=None, description="""Whether debris was removed from the sample before exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SamplePreparation']} })
    debris_removal_method: Optional[str] = Field(default=None, description="""Method used to remove debris from samples.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SamplePreparation']} })
    wash_steps: Optional[str] = Field(default=None, description="""Description of wash steps performed before exposure (buffer, number, duration).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SamplePreparation']} })
    equilibration_time: Optional[QuantityValue] = Field(default=None, description="""Time allowed for sample equilibration before exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SamplePreparation']} })
    pre_exposure_treatment: Optional[str] = Field(default=None, description="""Any pre-treatment applied before exposure (e.g., cytokine priming).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SamplePreparation']} })
    surface_preparation: Optional[str] = Field(default=None, description="""Surface preparation procedures (e.g., coating, conditioning).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SamplePreparation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Analysis(NamedThing):
    """
    Data analysis and processing parameters describing how measurement data was acquired, processed, normalized, and quality controlled. Links to measurements to provide complete provenance of derived values.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    normalization_performed: Optional[bool] = Field(default=None, description="""Whether data normalization was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    data_normalization_method: Optional[DataNormalizationMethodEnum] = Field(default=None, description="""Method used for data normalization (per area, per cell count, baseline, control).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    viability_normalized: Optional[bool] = Field(default=None, description="""Whether data were normalized to account for cell viability/cytotoxicity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    baseline_definition: Optional[str] = Field(default=None, description="""How baseline is defined (e.g., response of solvent control, pre-exposure value).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    dose_normalization_method: Optional[DoseNormalizationMethodEnum] = Field(default=None, description="""Method used to normalize dose (per area, per cell count, per protein, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVitroExposure', 'Analysis']} })
    raw_data_type: Optional[RawDataTypeEnum] = Field(default=None, description="""Type of raw data collected (image stack, video, fluorescence intensity, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    analysis_software: Optional[str] = Field(default=None, description="""Software used for data analysis (e.g., CellProfiler, ImageJ, R, MATLAB).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    analysis_software_version: Optional[str] = Field(default=None, description="""Version of the analysis software used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    automation_level: Optional[AutomationLevelEnum] = Field(default=None, description="""Level of automation in data processing (manual, semi-automated, fully automated).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    algorithm_type: Optional[str] = Field(default=None, description="""Type of algorithm used for analysis (e.g., thresholding, segmentation, machine learning).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    pipeline_reference: Optional[str] = Field(default=None, description="""Reference to analysis pipeline (workflow name/version, GitHub URL, DOI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    data_transformation: Optional[DataTransformationEnum] = Field(default=None, description="""Mathematical transformation applied to data (log, square root, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    replicate_combination_method: Optional[ReplicateCombinationMethodEnum] = Field(default=None, description="""Method for combining replicate measurements (mean, median, fitted model).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    outlier_detection_method: Optional[str] = Field(default=None, description="""Method used for outlier detection (e.g., IQR, Grubbs test, ROUT).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    outlier_removal_performed: Optional[bool] = Field(default=None, description="""Whether outliers were removed from the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    imaging_magnification: Optional[str] = Field(default=None, description="""Microscope magnification used (e.g., 10x, 20x, 40x).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    pixel_size: Optional[QuantityValue] = Field(default=None, description="""Size of image pixels in micrometers or nanometers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    voxel_depth: Optional[QuantityValue] = Field(default=None, description="""Depth of voxels for 3D imaging in micrometers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    z_step_size: Optional[QuantityValue] = Field(default=None, description="""Z-step size for optical stacks (usually in micrometers).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    number_of_z_slices: Optional[int] = Field(default=None, description="""Number of Z-slices in an optical stack.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    temporal_resolution: Optional[QuantityValue] = Field(default=None, description="""Temporal resolution for video acquisition (fps or acquisition rate).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    acquisition_duration: Optional[QuantityValue] = Field(default=None, description="""Total duration of video or time-series acquisition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    motion_stabilization_applied: Optional[bool] = Field(default=None, description="""Whether motion stabilization/drift correction was applied to images or video.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    frame_rate: Optional[QuantityValue] = Field(default=None, description="""Frame rate of video acquisition in frames per second.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    flow_profile_during_imaging: Optional[str] = Field(default=None, description="""Flow conditions during imaging (for lung-on-chip or perfusion systems).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    measurements_per_replicate: Optional[int] = Field(default=None, description="""Number of images or individual measurements per replicate.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    qc_acceptance_criteria: Optional[str] = Field(default=None, description="""Criteria used to determine data validity (e.g., CV threshold, comparison to historical controls).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    qc_passed: Optional[bool] = Field(default=None, description="""Whether the data passed quality control criteria.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    comparison_to_historical_controls: Optional[str] = Field(default=None, description="""How data were compared to historical control values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    final_metric: Optional[str] = Field(default=None, description="""The final output metric reported (e.g., CBF in Hz, MCC rate in mm/min).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    final_metric_unit: Optional[Unit] = Field(default=None, description="""Unit of the final metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Gene(BiologicalEntity):
    """
    A gene or genetic element
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    ncbigene_id: Optional[str] = Field(default=None, description="""NCBI Gene identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene']} })
    symbol: Optional[str] = Field(default=None, description="""Gene symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'Protein']} })
    in_taxon: Optional[str] = Field(default=None, description="""Taxonomic group""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'Protein']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('ncbigene_id')
    def pattern_ncbigene_id(cls, v):
        pattern=re.compile(r"^\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ncbigene_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ncbigene_id format: {v}"
            raise ValueError(err_msg)
        return v


class Protein(BiologicalEntity):
    """
    A protein or polypeptide
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    encoded_by_gene: Optional[Gene] = Field(default=None, description="""Gene that encodes this protein""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protein']} })
    symbol: Optional[str] = Field(default=None, description="""Gene symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'Protein']} })
    in_taxon: Optional[str] = Field(default=None, description="""Taxonomic group""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'Protein']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class CellType(BiologicalEntity):
    """
    A type of cell
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CL:0000000',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'id_prefixes': ['CL']})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class AnatomicalEntity(BiologicalEntity):
    """
    An anatomical structure or system
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'UBERON:0001062',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'id_prefixes': ['UBERON']})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Organism(BiologicalEntity):
    """
    An individual organism
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    species: Optional[str] = Field(default=None, description="""Species name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organism', 'Person']} })
    taxon_id: Optional[str] = Field(default=None, description="""NCBI Taxonomy identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organism']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ExposureToPhenotypeAssociation(Association):
    """
    An association between an exposure and a phenotype
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    exposure: Optional[ExposureEvent] = Field(default=None, description="""Exposure in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation']} })
    phenotype: Optional[OntologyTerm] = Field(default=None, description="""The phenotype being measured, with identifier and name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeMeasurement', 'ExposureToPhenotypeAssociation']} })
    association_type: Optional[str] = Field(default=None, description="""Type of association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation', 'GeneToDiseaseAssociation']} })
    evidence: Optional[str] = Field(default=None, description="""Evidence for association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ChemicalToGeneAssociation(Association):
    """
    An association between a chemical and a gene
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    chemical: Optional[ChemicalEntity] = Field(default=None, description="""Chemical in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation']} })
    gene: Optional[Gene] = Field(default=None, description="""Gene in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation', 'GeneToDiseaseAssociation']} })
    interaction_type: Optional[str] = Field(default=None, description="""Type of interaction""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class GeneToDiseaseAssociation(Association):
    """
    An association between a gene and a disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    gene: Optional[Gene] = Field(default=None, description="""Gene in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation', 'GeneToDiseaseAssociation']} })
    disease: Optional[Disease] = Field(default=None, description="""Disease in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneToDiseaseAssociation']} })
    association_type: Optional[str] = Field(default=None, description="""Type of association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation', 'GeneToDiseaseAssociation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class GeographicEntity(NamedThing):
    """
    Abstract base class for geographic entities used in synthetic population modeling. Provides common geographic identifier infrastructure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""Federal Information Processing Standard (FIPS) code, a unique numeric identifier assigned to geographic areas like states and counties within the United States, used primarily by the Census Bureau to identify locations when analyzing population data.""", json_schema_extra = { "linkml_meta": {'aliases': ['fips_code'],
         'domain_of': ['GeographicEntity', 'School'],
         'exact_mappings': ['wikidata:Q917824']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class State(GeographicEntity):
    """
    A U.S. state or equivalent territory with associated geographic properties. Contains counties and public use microdata areas.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['wikidata:Q7275'],
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    abbreviation: Optional[str] = Field(default=None, description="""Standard two-letter abbreviation for a U.S. state or territory.""", json_schema_extra = { "linkml_meta": {'domain_of': ['State']} })
    counties: Optional[list[County]] = Field(default=[], description="""Counties within a state or geographic region.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'State']} })
    public_use_microdata_areas: Optional[list[PublicUseMicrodataArea]] = Field(default=[], description="""Public Use Microdata Areas (PUMAs) within a state. PUMAs are non-overlapping statistical geographic areas containing no fewer than 100,000 people each.""", json_schema_extra = { "linkml_meta": {'aliases': ['pumas'], 'domain_of': ['Container', 'State']} })
    federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""Federal Information Processing Standard (FIPS) code, a unique numeric identifier assigned to geographic areas like states and counties within the United States, used primarily by the Census Bureau to identify locations when analyzing population data.""", json_schema_extra = { "linkml_meta": {'aliases': ['fips_code'],
         'domain_of': ['GeographicEntity', 'School'],
         'exact_mappings': ['wikidata:Q917824']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class PublicUseMicrodataArea(GeographicEntity):
    """
    Public Use Microdata Areas (PUMAs) are non-overlapping, statistical geographic areas that partition each state or equivalent entity into geographic areas containing no fewer than 100,000 people each. They cover the entirety of the United States, Puerto Rico, and Guam.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['PUMA'],
         'exact_mappings': ['wikidata:Q7257651'],
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    state_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""State-level Federal Information Processing Standard (FIPS) code. A two-digit code uniquely identifying each U.S. state and territory.""", json_schema_extra = { "linkml_meta": {'aliases': ['state_fips_code'],
         'domain_of': ['PublicUseMicrodataArea',
                       'County',
                       'CensusTract',
                       'BlockGroup',
                       'School',
                       'Person'],
         'exact_mappings': ['wikidata:Q5440257'],
         'is_a': 'federal_information_processing_standard_code'} })
    federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""Federal Information Processing Standard (FIPS) code, a unique numeric identifier assigned to geographic areas like states and counties within the United States, used primarily by the Census Bureau to identify locations when analyzing population data.""", json_schema_extra = { "linkml_meta": {'aliases': ['fips_code'],
         'domain_of': ['GeographicEntity', 'School'],
         'exact_mappings': ['wikidata:Q917824']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class County(GeographicEntity):
    """
    A county or equivalent administrative subdivision with associated properties. Contains census tracts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['wikidata:Q28575', 'NCIT:C49292'],
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    state_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""State-level Federal Information Processing Standard (FIPS) code. A two-digit code uniquely identifying each U.S. state and territory.""", json_schema_extra = { "linkml_meta": {'aliases': ['state_fips_code'],
         'domain_of': ['PublicUseMicrodataArea',
                       'County',
                       'CensusTract',
                       'BlockGroup',
                       'School',
                       'Person'],
         'exact_mappings': ['wikidata:Q5440257'],
         'is_a': 'federal_information_processing_standard_code'} })
    census_tracts: Optional[list[CensusTract]] = Field(default=[], description="""Census tracts within a county.""", json_schema_extra = { "linkml_meta": {'aliases': ['tracts'], 'domain_of': ['Container', 'County']} })
    federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""Federal Information Processing Standard (FIPS) code, a unique numeric identifier assigned to geographic areas like states and counties within the United States, used primarily by the Census Bureau to identify locations when analyzing population data.""", json_schema_extra = { "linkml_meta": {'aliases': ['fips_code'],
         'domain_of': ['GeographicEntity', 'School'],
         'exact_mappings': ['wikidata:Q917824']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class CensusTract(GeographicEntity):
    """
    A census tract is a small, relatively permanent geographic area within a county, used to collect and present demographic data from the census, usually containing between 2,500 and 8,000 residents and designed to be as homogeneous as possible in terms of population characteristics and living conditions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['Tract'],
         'exact_mappings': ['wikidata:Q107738887', 'NCIT:C67490'],
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    state_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""State-level Federal Information Processing Standard (FIPS) code. A two-digit code uniquely identifying each U.S. state and territory.""", json_schema_extra = { "linkml_meta": {'aliases': ['state_fips_code'],
         'domain_of': ['PublicUseMicrodataArea',
                       'County',
                       'CensusTract',
                       'BlockGroup',
                       'School',
                       'Person'],
         'exact_mappings': ['wikidata:Q5440257'],
         'is_a': 'federal_information_processing_standard_code'} })
    county_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""County-level Federal Information Processing Standard (FIPS) code. A three-digit code uniquely identifying a county within a state.""", json_schema_extra = { "linkml_meta": {'aliases': ['county_fips_code'],
         'domain_of': ['CensusTract', 'BlockGroup', 'School', 'Person'],
         'exact_mappings': ['wikidata:P882'],
         'is_a': 'federal_information_processing_standard_code'} })
    block_groups: Optional[list[BlockGroup]] = Field(default=[], description="""Block groups within a census tract.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'CensusTract']} })
    federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""Federal Information Processing Standard (FIPS) code, a unique numeric identifier assigned to geographic areas like states and counties within the United States, used primarily by the Census Bureau to identify locations when analyzing population data.""", json_schema_extra = { "linkml_meta": {'aliases': ['fips_code'],
         'domain_of': ['GeographicEntity', 'School'],
         'exact_mappings': ['wikidata:Q917824']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class BlockGroup(GeographicEntity):
    """
    A statistical division within a census tract, typically containing between 600 and 3,000 people, which is used by the Census Bureau to present demographic data at a smaller, more localized level than the entire census tract.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['wikidata:Q5058963'],
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    census_tract_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""Census tract-level Federal Information Processing Standard (FIPS) code. Identifies a specific census tract within a county.""", json_schema_extra = { "linkml_meta": {'aliases': ['tract_fips_code'],
         'domain_of': ['BlockGroup', 'School', 'Person'],
         'is_a': 'federal_information_processing_standard_code'} })
    state_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""State-level Federal Information Processing Standard (FIPS) code. A two-digit code uniquely identifying each U.S. state and territory.""", json_schema_extra = { "linkml_meta": {'aliases': ['state_fips_code'],
         'domain_of': ['PublicUseMicrodataArea',
                       'County',
                       'CensusTract',
                       'BlockGroup',
                       'School',
                       'Person'],
         'exact_mappings': ['wikidata:Q5440257'],
         'is_a': 'federal_information_processing_standard_code'} })
    county_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""County-level Federal Information Processing Standard (FIPS) code. A three-digit code uniquely identifying a county within a state.""", json_schema_extra = { "linkml_meta": {'aliases': ['county_fips_code'],
         'domain_of': ['CensusTract', 'BlockGroup', 'School', 'Person'],
         'exact_mappings': ['wikidata:P882'],
         'is_a': 'federal_information_processing_standard_code'} })
    households: Optional[list[Household]] = Field(default=[], description="""Households within a block group or geographic area.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container', 'BlockGroup']} })
    federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""Federal Information Processing Standard (FIPS) code, a unique numeric identifier assigned to geographic areas like states and counties within the United States, used primarily by the Census Bureau to identify locations when analyzing population data.""", json_schema_extra = { "linkml_meta": {'aliases': ['fips_code'],
         'domain_of': ['GeographicEntity', 'School'],
         'exact_mappings': ['wikidata:Q917824']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class School(NamedThing):
    """
    A school entity representing an educational institution where synthetic population persons may be assigned for modeling purposes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""Federal Information Processing Standard (FIPS) code, a unique numeric identifier assigned to geographic areas like states and counties within the United States, used primarily by the Census Bureau to identify locations when analyzing population data.""", json_schema_extra = { "linkml_meta": {'aliases': ['fips_code'],
         'domain_of': ['GeographicEntity', 'School'],
         'exact_mappings': ['wikidata:Q917824']} })
    state_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""State-level Federal Information Processing Standard (FIPS) code. A two-digit code uniquely identifying each U.S. state and territory.""", json_schema_extra = { "linkml_meta": {'aliases': ['state_fips_code'],
         'domain_of': ['PublicUseMicrodataArea',
                       'County',
                       'CensusTract',
                       'BlockGroup',
                       'School',
                       'Person'],
         'exact_mappings': ['wikidata:Q5440257'],
         'is_a': 'federal_information_processing_standard_code'} })
    county_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""County-level Federal Information Processing Standard (FIPS) code. A three-digit code uniquely identifying a county within a state.""", json_schema_extra = { "linkml_meta": {'aliases': ['county_fips_code'],
         'domain_of': ['CensusTract', 'BlockGroup', 'School', 'Person'],
         'exact_mappings': ['wikidata:P882'],
         'is_a': 'federal_information_processing_standard_code'} })
    census_tract_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""Census tract-level Federal Information Processing Standard (FIPS) code. Identifies a specific census tract within a county.""", json_schema_extra = { "linkml_meta": {'aliases': ['tract_fips_code'],
         'domain_of': ['BlockGroup', 'School', 'Person'],
         'is_a': 'federal_information_processing_standard_code'} })
    block_group_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""Block group-level Federal Information Processing Standard (FIPS) code. Identifies a specific block group within a census tract.""", json_schema_extra = { "linkml_meta": {'aliases': ['block_group_fips_code'],
         'domain_of': ['School', 'Person'],
         'is_a': 'federal_information_processing_standard_code'} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Household(NamedThing):
    """
    A household entity representing a group of people living together in a single dwelling unit. Used in synthetic population modeling.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['wikidata:Q259059', 'OMRSE:00000076'],
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    serial_number: Optional[str] = Field(default=None, description="""Serial number linking to the original PUMS (Public Use Microdata Sample) record. Used to connect synthetic population records to source census microdata.""", json_schema_extra = { "linkml_meta": {'aliases': ['serialno'], 'domain_of': ['Household', 'Person']} })
    household_identifier: Optional[str] = Field(default=None, description="""Unique identifier for a household within the synthetic population.""", json_schema_extra = { "linkml_meta": {'aliases': ['hh_id'], 'domain_of': ['Household', 'Person']} })
    household_head_age: Optional[int] = Field(default=None, description="""Age of the household head (householder) in years. Used as one of the four matching variables in synthetic population generation.""", json_schema_extra = { "linkml_meta": {'aliases': ['hh_age'], 'domain_of': ['Household', 'Person']} })
    household_income: Optional[float] = Field(default=None, description="""Annual household income in dollars. Used as one of the four matching variables in synthetic population generation.""", json_schema_extra = { "linkml_meta": {'aliases': ['hh_income'], 'domain_of': ['Household', 'Person']} })
    household_head_race: Optional[str] = Field(default=None, description="""Race category of the household head. Used as one of the four matching variables in synthetic population generation.""", json_schema_extra = { "linkml_meta": {'aliases': ['hh_race'], 'domain_of': ['Household', 'Person']} })
    household_size: Optional[int] = Field(default=None, description="""Number of persons in the household. Used as one of the four matching variables in synthetic population generation.""", json_schema_extra = { "linkml_meta": {'aliases': ['size'], 'domain_of': ['Household', 'Person']} })
    household_persons: Optional[list[Person]] = Field(default=[], description="""Persons (individuals) within the household.""", json_schema_extra = { "linkml_meta": {'aliases': ['persons'], 'domain_of': ['Household']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Person(NamedThing):
    """
    A person (individual human being) with demographic and geographic attributes. Persons can participate in studies through the Participant role, which links a Person to a specific study cohort. In synthetic population contexts, persons are members of households within geographic hierarchies. Age and sex on Person represent current or snapshot values from the source data (e.g., census), distinct from study-specific values captured on Participant at enrollment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['schema:Person', 'NCIT:C25190'],
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'slot_usage': {'age': {'description': 'Age of the person in years as recorded '
                                               'in the source data (e.g., census or '
                                               'synthetic population). This represents '
                                               'a snapshot value at the time of data '
                                               'collection, distinct from '
                                               'study-specific age at enrollment.',
                                'name': 'age'},
                        'sex': {'description': 'Biological sex of the person as '
                                               'recorded in the source data (e.g., '
                                               'census or synthetic population). This '
                                               'represents the value from the original '
                                               'data source, distinct from '
                                               'study-specific sex recorded at '
                                               'enrollment.',
                                'name': 'sex'}}})

    age: Optional[int] = Field(default=None, description="""Age of the person in years as recorded in the source data (e.g., census or synthetic population). This represents a snapshot value at the time of data collection, distinct from study-specific age at enrollment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant', 'Person']} })
    sex: Optional[SexEnum] = Field(default=None, description="""Biological sex of the person as recorded in the source data (e.g., census or synthetic population). This represents the value from the original data source, distinct from study-specific sex recorded at enrollment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant', 'Person']} })
    race: Optional[str] = Field(default=None, description="""Race of the person. Derived from census race categories.""", json_schema_extra = { "linkml_meta": {'aliases': ['rac1p'], 'domain_of': ['Person']} })
    species: Optional[str] = Field(default=None, description="""Species name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organism', 'Person']} })
    state_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""State-level Federal Information Processing Standard (FIPS) code. A two-digit code uniquely identifying each U.S. state and territory.""", json_schema_extra = { "linkml_meta": {'aliases': ['state_fips_code'],
         'domain_of': ['PublicUseMicrodataArea',
                       'County',
                       'CensusTract',
                       'BlockGroup',
                       'School',
                       'Person'],
         'exact_mappings': ['wikidata:Q5440257'],
         'is_a': 'federal_information_processing_standard_code'} })
    county_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""County-level Federal Information Processing Standard (FIPS) code. A three-digit code uniquely identifying a county within a state.""", json_schema_extra = { "linkml_meta": {'aliases': ['county_fips_code'],
         'domain_of': ['CensusTract', 'BlockGroup', 'School', 'Person'],
         'exact_mappings': ['wikidata:P882'],
         'is_a': 'federal_information_processing_standard_code'} })
    census_tract_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""Census tract-level Federal Information Processing Standard (FIPS) code. Identifies a specific census tract within a county.""", json_schema_extra = { "linkml_meta": {'aliases': ['tract_fips_code'],
         'domain_of': ['BlockGroup', 'School', 'Person'],
         'is_a': 'federal_information_processing_standard_code'} })
    block_group_federal_information_processing_standard_code: Optional[str] = Field(default=None, description="""Block group-level Federal Information Processing Standard (FIPS) code. Identifies a specific block group within a census tract.""", json_schema_extra = { "linkml_meta": {'aliases': ['block_group_fips_code'],
         'domain_of': ['School', 'Person'],
         'is_a': 'federal_information_processing_standard_code'} })
    serial_number: Optional[str] = Field(default=None, description="""Serial number linking to the original PUMS (Public Use Microdata Sample) record. Used to connect synthetic population records to source census microdata.""", json_schema_extra = { "linkml_meta": {'aliases': ['serialno'], 'domain_of': ['Household', 'Person']} })
    household_identifier: Optional[str] = Field(default=None, description="""Unique identifier for a household within the synthetic population.""", json_schema_extra = { "linkml_meta": {'aliases': ['hh_id'], 'domain_of': ['Household', 'Person']} })
    household_head_age: Optional[int] = Field(default=None, description="""Age of the household head (householder) in years. Used as one of the four matching variables in synthetic population generation.""", json_schema_extra = { "linkml_meta": {'aliases': ['hh_age'], 'domain_of': ['Household', 'Person']} })
    household_income: Optional[float] = Field(default=None, description="""Annual household income in dollars. Used as one of the four matching variables in synthetic population generation.""", json_schema_extra = { "linkml_meta": {'aliases': ['hh_income'], 'domain_of': ['Household', 'Person']} })
    household_head_race: Optional[str] = Field(default=None, description="""Race category of the household head. Used as one of the four matching variables in synthetic population generation.""", json_schema_extra = { "linkml_meta": {'aliases': ['hh_race'], 'domain_of': ['Household', 'Person']} })
    household_size: Optional[int] = Field(default=None, description="""Number of persons in the household. Used as one of the four matching variables in synthetic population generation.""", json_schema_extra = { "linkml_meta": {'aliases': ['size'], 'domain_of': ['Household', 'Person']} })
    assigned_school: Optional[str] = Field(default=None, description="""School assigned to a person for modeling purposes. Assignment is based on school/grade capacity and proximity.""", json_schema_extra = { "linkml_meta": {'aliases': ['school'], 'domain_of': ['Person']} })
    person_order: Optional[int] = Field(default=None, description="""Person's order within the household, starting from 1. The householder is typically person 1.""", json_schema_extra = { "linkml_meta": {'aliases': ['sporder'], 'domain_of': ['Person']} })
    relationship_to_household_head: Optional[RelationshipToHouseholdHeadEnum] = Field(default=None, description="""Relationship of the person to the household head (householder). Values: 1=Householder, 2=Spouse, 3=Child, 4=Other relative, 5=Nonrelative, 6=Foster child, 7=Foster parent, 8=Other nonrelative.""", json_schema_extra = { "linkml_meta": {'aliases': ['relp'], 'domain_of': ['Person']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Container.model_rebuild()
NamedThing.model_rebuild()
Unit.model_rebuild()
QuantityValue.model_rebuild()
QuantityRange.model_rebuild()
OntologyTerm.model_rebuild()
Tissue.model_rebuild()
BiologicalEntity.model_rebuild()
ChemicalEntity.model_rebuild()
ExposureEvent.model_rebuild()
BiologicalResponse.model_rebuild()
HealthOutcome.model_rebuild()
ExposableSubject.model_rebuild()
StudyEntity.model_rebuild()
Measurement.model_rebuild()
Association.model_rebuild()
ChemicalExposure.model_rebuild()
DietaryExposure.model_rebuild()
EnvironmentalExposure.model_rebuild()
OccupationalExposure.model_rebuild()
Phenotype.model_rebuild()
Disease.model_rebuild()
AdverseOutcome.model_rebuild()
AdverseOutcomePathway.model_rebuild()
MolecularInitiatingEvent.model_rebuild()
KeyEvent.model_rebuild()
KeyEventRelationship.model_rebuild()
Study.model_rebuild()
Cohort.model_rebuild()
Participant.model_rebuild()
ExposureMeasurement.model_rebuild()
BiomarkerMeasurement.model_rebuild()
PhenotypeMeasurement.model_rebuild()
AggregatedMeasurement.model_rebuild()
GeneExpressionMeasurement.model_rebuild()
ProteinExpressionMeasurement.model_rebuild()
EnvironmentalMeasurement.model_rebuild()
MechanicalMeasurement.model_rebuild()
MembranePropertyMeasurement.model_rebuild()
CellLine.model_rebuild()
CellCultureConditions.model_rebuild()
CellCultureMedium.model_rebuild()
MediumSupplement.model_rebuild()
ModelSystem.model_rebuild()
CellularSystem.model_rebuild()
TwoDCellCulture.model_rebuild()
ThreeDCellCulture.model_rebuild()
CoCulture.model_rebuild()
ExposureMaterial.model_rebuild()
ParticleProperties.model_rebuild()
InVitroExposure.model_rebuild()
AerosolGeneration.model_rebuild()
SamplePreparation.model_rebuild()
Analysis.model_rebuild()
Gene.model_rebuild()
Protein.model_rebuild()
CellType.model_rebuild()
AnatomicalEntity.model_rebuild()
Organism.model_rebuild()
ExposureToPhenotypeAssociation.model_rebuild()
ChemicalToGeneAssociation.model_rebuild()
GeneToDiseaseAssociation.model_rebuild()
GeographicEntity.model_rebuild()
State.model_rebuild()
PublicUseMicrodataArea.model_rebuild()
County.model_rebuild()
CensusTract.model_rebuild()
BlockGroup.model_rebuild()
School.model_rebuild()
Household.model_rebuild()
Person.model_rebuild()
