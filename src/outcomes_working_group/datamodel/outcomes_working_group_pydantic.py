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
                  'NCBIGENE': {'prefix_prefix': 'NCBIGENE',
                               'prefix_reference': 'https://www.ncbi.nlm.nih.gov/gene/'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'NHANES': {'prefix_prefix': 'NHANES',
                             'prefix_reference': 'https://wwwn.cdc.gov/Nchs/Nhanes/'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
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
                          'prefix_reference': 'https://w3id.org/diatomsRcool/exposome-schema/'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/vocab/unit/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://EHS-Data-Standards.github.io/outcomes-working-group'],
     'source_file': 'src/outcomes_working_group/schema/outcomes_working_group.yaml',
     'title': 'Outcome Measurement Data Model'} )

class ExposureRouteEnum(str, Enum):
    """
    Routes of exposure to chemicals or environmental factors
    """
    Oral = "Oral"
    """
    Oral ingestion
    """
    Dermal = "Dermal"
    """
    Dermal contact
    """
    Inhalation = "Inhalation"
    """
    Inhalation
    """
    Injection = "Injection"
    """
    Injection
    """
    Unknown = "Unknown"
    """
    Unknown route
    """


class ExposureMediumEnum(str, Enum):
    """
    Medium through which exposure occurs
    """
    Air = "Air"
    """
    Air
    """
    Water = "Water"
    """
    Water
    """
    Food = "Food"
    """
    Food
    """
    Soil = "Soil"
    """
    Soil
    """
    Dust = "Dust"
    """
    Dust
    """
    ConsumerProduct = "ConsumerProduct"
    """
    Consumer product
    """
    Unknown = "Unknown"
    """
    Unknown medium
    """


class ExpressionAssayMethodEnum(str, Enum):
    """
    Methods used to measure gene or protein expression. Includes transcriptomic, proteomic, and imaging-based approaches.
    """
    qRT_PCR = "qRT_PCR"
    """
    Quantitative real-time polymerase chain reaction
    """
    RNA_Seq = "RNA_Seq"
    """
    RNA sequencing (bulk)
    """
    Single_Cell_RNA_Seq = "Single_Cell_RNA_Seq"
    """
    Single-cell RNA sequencing
    """
    Microarray = "Microarray"
    """
    Gene expression microarray
    """
    NanoString = "NanoString"
    """
    NanoString nCounter gene expression assay
    """
    Northern_Blot = "Northern_Blot"
    """
    Northern blot for RNA detection
    """
    In_Situ_Hybridization = "In_Situ_Hybridization"
    """
    In situ hybridization (ISH, FISH, RNAscope)
    """
    Western_Blot = "Western_Blot"
    """
    Western blot (immunoblot) for protein detection
    """
    ELISA = "ELISA"
    """
    Enzyme-linked immunosorbent assay
    """
    Immunohistochemistry = "Immunohistochemistry"
    """
    Immunohistochemistry on tissue sections
    """
    Immunofluorescence = "Immunofluorescence"
    """
    Immunofluorescence staining
    """
    Flow_Cytometry = "Flow_Cytometry"
    """
    Flow cytometry for protein expression
    """
    Mass_Spectrometry = "Mass_Spectrometry"
    """
    Mass spectrometry-based proteomics
    """
    Immunoprecipitation = "Immunoprecipitation"
    """
    Immunoprecipitation followed by detection
    """
    Luminex = "Luminex"
    """
    Luminex multiplex bead-based assay
    """
    Other = "Other"
    """
    Other assay method not listed
    """


class BiologicalOrganizationLevelEnum(str, Enum):
    """
    Levels of biological organization
    """
    Molecular = "Molecular"
    """
    Molecular level
    """
    Cellular = "Cellular"
    """
    Cellular level
    """
    Tissue = "Tissue"
    """
    Tissue level
    """
    Organ = "Organ"
    """
    Organ level
    """
    Organism = "Organism"
    """
    Organism level
    """
    Population = "Population"
    """
    Population level
    """


class StudyTypeEnum(str, Enum):
    """
    Types of research studies
    """
    Cohort = "Cohort"
    """
    Cohort study
    """
    CrossSectional = "CrossSectional"
    """
    Cross-sectional study
    """
    CaseControl = "CaseControl"
    """
    Case-control study
    """
    RandomizedControlledTrial = "RandomizedControlledTrial"
    """
    Randomized controlled trial
    """
    Survey = "Survey"
    """
    Survey
    """
    Gwas = "Gwas"
    """
    Genome-wide association study
    """
    Other = "Other"
    """
    Other study type
    """


class DataSourceEnum(str, Enum):
    """
    Data sources and repositories
    """
    Nhanes = "Nhanes"
    """
    National Health and Nutrition Examination Survey
    """
    Chear = "Chear"
    """
    Children's Health Exposure Analysis Resource
    """
    Hhear = "Hhear"
    """
    Human Health Exposure Analysis Resource
    """
    AopWiki = "AopWiki"
    """
    AOP Wiki
    """
    Ctd = "Ctd"
    """
    Comparative Toxicogenomics Database
    """
    ToxCast = "ToxCast"
    """
    ToxCast
    """
    Tox21 = "Tox21"
    """
    Tox21
    """
    ChemBl = "ChemBl"
    """
    ChEMBL
    """
    CompTox = "CompTox"
    """
    CompTox Dashboard
    """
    GwasCatalog = "GwasCatalog"
    """
    GWAS Catalog
    """
    GeneExpressionAtlas = "GeneExpressionAtlas"
    """
    Gene Expression Atlas
    """
    UsdaPesticide = "UsdaPesticide"
    """
    USDA Pesticide Data Program
    """
    Wweia = "Wweia"
    """
    What We Eat In America
    """
    Other = "Other"
    """
    Other data source
    """


class SexEnum(str, Enum):
    """
    Biological sex
    """
    Male = "Male"
    """
    Male
    """
    Female = "Female"
    """
    Female
    """
    Unknown = "Unknown"
    """
    Unknown
    """


class SampleTypeEnum(str, Enum):
    """
    Types of biological and environmental samples
    """
    Blood = "Blood"
    """
    Blood sample
    """
    Urine = "Urine"
    """
    Urine sample
    """
    Serum = "Serum"
    """
    Serum sample
    """
    Plasma = "Plasma"
    """
    Plasma sample
    """
    Tissue = "Tissue"
    """
    Tissue sample
    """
    Saliva = "Saliva"
    """
    Saliva sample
    """
    Hair = "Hair"
    """
    Hair sample
    """
    Nail = "Nail"
    """
    Nail sample
    """
    Air = "Air"
    """
    Air sample (environmental)
    """
    Water = "Water"
    """
    Water sample (environmental)
    """
    Soil = "Soil"
    """
    Soil sample (environmental)
    """
    Other = "Other"
    """
    Other sample type
    """


class SummaryStatisticEnum(str, Enum):
    """
    Types of summary statistics
    """
    Mean = "Mean"
    """
    Arithmetic mean
    """
    Median = "Median"
    """
    Median
    """
    Mode = "Mode"
    """
    Mode
    """
    Percentile = "Percentile"
    """
    Percentile
    """
    StandardDeviation = "StandardDeviation"
    """
    Standard deviation
    """
    Variance = "Variance"
    """
    Variance
    """
    Range = "Range"
    """
    Range
    """
    InterquartileRange = "InterquartileRange"
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
    FEV1_FVC_Ratio = "FEV1_FVC_Ratio"
    """
    Ratio of FEV1 to FVC (Tiffeneau-Pinelli index)
    """
    FEF25_75 = "FEF25_75"
    """
    Forced expiratory flow at 25-75% of FVC
    """
    PeakExpiratoryFlow = "PeakExpiratoryFlow"
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
    BronchodilatorResponse = "BronchodilatorResponse"
    """
    Change in lung function after bronchodilator administration
    """
    LungFunctionDeclineRate = "LungFunctionDeclineRate"
    """
    Rate of decline in lung function over time
    """
    CiliaryBeatFrequency = "CiliaryBeatFrequency"
    """
    Frequency of ciliary beating in Hz
    """
    CiliaryActiveAreaPercentage = "CiliaryActiveAreaPercentage"
    """
    Percentage of epithelial surface with active cilia
    """
    CiliaPerCell = "CiliaPerCell"
    """
    Number of cilia per epithelial cell
    """
    CiliaLength = "CiliaLength"
    """
    Length of cilia in micrometers
    """
    PercentageCiliatedCells = "PercentageCiliatedCells"
    """
    Percentage of cells that are ciliated
    """
    ASLHeight = "ASLHeight"
    """
    Airway surface liquid height in micrometers
    """
    PericiliaryLayerDepth = "PericiliaryLayerDepth"
    """
    Depth of periciliary liquid layer (reduced in disease)
    """
    MucusLayerThickness = "MucusLayerThickness"
    """
    Thickness of the mucus gel layer
    """
    MucociliaryTransportRate = "MucociliaryTransportRate"
    """
    Rate of mucociliary transport (mm/min)
    """
    MucociliaryDirectionality = "MucociliaryDirectionality"
    """
    Directionality and coordination of mucociliary transport
    """
    ParticleClearanceRate = "ParticleClearanceRate"
    """
    Rate of particle clearance from airways
    """
    GobletCellCount = "GobletCellCount"
    """
    Number or percentage of goblet cells
    """
    GobletToCiliatedRatio = "GobletToCiliatedRatio"
    """
    Ratio of goblet cells to ciliated cells
    """
    MucinProteinConcentration = "MucinProteinConcentration"
    """
    Concentration of secreted mucin protein
    """
    MucusViscosity = "MucusViscosity"
    """
    Viscosity of airway mucus
    """
    CFTRChlorideSecretion = "CFTRChlorideSecretion"
    """
    CFTR-mediated chloride secretory current
    """
    InhibitorSensitiveCurrent = "InhibitorSensitiveCurrent"
    """
    Current sensitive to CFTR inhibitors (e.g., CFTRinh-172)
    """
    SweatChlorideConcentration = "SweatChlorideConcentration"
    """
    Chloride concentration in sweat (CF diagnostic)
    """
    ReactiveOxygenSpecies = "ReactiveOxygenSpecies"
    """
    Reactive oxygen species (ROS) level
    """
    LipidPeroxidation = "LipidPeroxidation"
    """
    Lipid peroxidation markers (MDA, 8-isoprostane)
    """
    ProteinCarbonyls = "ProteinCarbonyls"
    """
    Protein carbonyl content (protein oxidation marker)
    """
    DNA_8OHdG = "DNA_8OHdG"
    """
    8-hydroxydeoxyguanosine (DNA oxidative damage marker)
    """
    GlutathioneRatio = "GlutathioneRatio"
    """
    GSH/GSSG ratio (antioxidant capacity)
    """
    SuperoxideDismutaseActivity = "SuperoxideDismutaseActivity"
    """
    Superoxide dismutase (SOD) enzyme activity
    """
    CatalaseActivity = "CatalaseActivity"
    """
    Catalase enzyme activity
    """
    GlutathionePeroxidaseActivity = "GlutathionePeroxidaseActivity"
    """
    Glutathione peroxidase (GPx) activity
    """
    TotalAntioxidantCapacity = "TotalAntioxidantCapacity"
    """
    Total antioxidant capacity of sample
    """
    TEER = "TEER"
    """
    Transepithelial electrical resistance
    """
    ParacellularPermeability = "ParacellularPermeability"
    """
    Paracellular permeability coefficient
    """
    IL6Level = "IL6Level"
    """
    Interleukin-6 concentration
    """
    IL8Level = "IL8Level"
    """
    Interleukin-8 (CXCL8) concentration
    """
    IL13Level = "IL13Level"
    """
    Interleukin-13 concentration
    """
    TNFAlphaLevel = "TNFAlphaLevel"
    """
    Tumor necrosis factor alpha concentration
    """
    NeutrophilPercentage = "NeutrophilPercentage"
    """
    Percentage of neutrophils in BALF or sputum
    """
    EosinophilPercentage = "EosinophilPercentage"
    """
    Percentage of eosinophils in BALF or sputum
    """
    MacrophagePercentage = "MacrophagePercentage"
    """
    Percentage of macrophages in BALF or sputum
    """
    TotalInflammatoryCell = "TotalInflammatoryCell"
    """
    Total inflammatory cell count
    """
    LDHRelease = "LDHRelease"
    """
    Lactate dehydrogenase release (cell damage marker)
    """
    CellViability = "CellViability"
    """
    Cell viability percentage
    """
    MTTReduction = "MTTReduction"
    """
    MTT assay result (metabolic activity)
    """
    ApoptosisRate = "ApoptosisRate"
    """
    Rate of apoptotic cell death
    """
    GeneExpression = "GeneExpression"
    """
    Gene expression level (mRNA). Use with GeneExpressionMeasurement class to specify target_gene, tissue_context, and assay_method.
    """
    ProteinExpression = "ProteinExpression"
    """
    Protein expression level. Use with ProteinExpressionMeasurement class to specify target_protein, tissue_context, and assay_method.
    """
    ProteinPhosphorylation = "ProteinPhosphorylation"
    """
    Protein phosphorylation level. Use with ProteinExpressionMeasurement class and specify phosphorylation_site (e.g., Y1068 for EGFR).
    """
    ProteinLocalization = "ProteinLocalization"
    """
    Protein subcellular localization (membrane, cytoplasm, nucleus). Use with ProteinExpressionMeasurement class.
    """
    ExpressionRatio = "ExpressionRatio"
    """
    Ratio of expression between two genes or proteins (e.g., MUC5AC/MUC5B ratio). Specify both targets in description.
    """
    PercentagePositiveCells = "PercentagePositiveCells"
    """
    Percentage of cells positive for a marker (IHC, flow cytometry)
    """
    BloodLeadLevel = "BloodLeadLevel"
    """
    Blood lead concentration
    """
    BloodCadmiumLevel = "BloodCadmiumLevel"
    """
    Blood cadmium concentration
    """
    BloodMercuryLevel = "BloodMercuryLevel"
    """
    Blood mercury concentration
    """
    UrinaryArsenicLevel = "UrinaryArsenicLevel"
    """
    Urinary arsenic concentration
    """
    UrinaryCotinineLevel = "UrinaryCotinineLevel"
    """
    Urinary cotinine (tobacco exposure biomarker)
    """
    UrinaryBPALevel = "UrinaryBPALevel"
    """
    Urinary bisphenol A concentration
    """
    UrinaryPhthalateMetabolites = "UrinaryPhthalateMetabolites"
    """
    Urinary phthalate metabolite concentrations
    """
    PM2_5Exposure = "PM2_5Exposure"
    """
    Fine particulate matter (PM2.5) exposure level
    """
    OzoneExposure = "OzoneExposure"
    """
    Ozone exposure concentration
    """
    NO2Exposure = "NO2Exposure"
    """
    Nitrogen dioxide exposure concentration
    """
    PolycyclicAromaticHydrocarbons = "PolycyclicAromaticHydrocarbons"
    """
    PAH metabolite levels
    """
    BodyMassIndex = "BodyMassIndex"
    """
    Body mass index (BMI)
    """
    BodyWeight = "BodyWeight"
    """
    Body weight measurement
    """
    Height = "Height"
    """
    Height measurement
    """
    AlphaDiversity = "AlphaDiversity"
    """
    Microbiome alpha diversity metric
    """
    BetaDiversity = "BetaDiversity"
    """
    Microbiome beta diversity metric
    """
    BacterialLoad = "BacterialLoad"
    """
    Total bacterial load (CFU or 16S copies)
    """
    Other = "Other"
    """
    Other measurement type not listed
    """



class Container(ConfiguredBaseModel):
    """
    A container for collections of measurements and related entities. Used as the root class for data validation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'tree_root': True})

    exposure_measurements: Optional[list[ExposureMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    biomarker_measurements: Optional[list[BiomarkerMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    phenotype_measurements: Optional[list[PhenotypeMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    gene_expression_measurements: Optional[list[GeneExpressionMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    protein_expression_measurements: Optional[list[ProteinExpressionMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    aggregated_measurements: Optional[list[AggregatedMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    studies: Optional[list[Study]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    cohorts: Optional[list[Cohort]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    participants: Optional[list[Participant]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    chemicals: Optional[list[ChemicalEntity]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    genes: Optional[list[Gene]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    proteins: Optional[list[Protein]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    ciliary_measurements: Optional[list[PhenotypeMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    asl_measurements: Optional[list[PhenotypeMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    mcc_measurements: Optional[list[PhenotypeMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    goblet_cell_measurements: Optional[list[PhenotypeMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    oxidative_stress_measurements: Optional[list[BiomarkerMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    barrier_measurements: Optional[list[BiomarkerMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    cytotoxicity_measurements: Optional[list[BiomarkerMeasurement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })


class NamedThing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity in the exposome
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class UnitConcept(ConfiguredBaseModel):
    """
    A unit of measurement from a standard ontology (UO, UCUM, QUDT)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group',
         'id_prefixes': ['UO', 'UCUM', 'qudt']})

    id: Optional[str] = Field(default=None, description="""The unit identifier (e.g., UO:0000009 for kilogram)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label for the unit (e.g., \"kg\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitConcept']} })


class Quantity(ConfiguredBaseModel):
    """
    A quantity with a numeric value and unit of measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fhir:Quantity',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    value: Optional[float] = Field(default=None, description="""The numeric value of the quantity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity']} })
    unit: Optional[str] = Field(default=None, description="""The unit identifier (e.g., UO:0000009 for kilogram)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity']} })
    unit_label: Optional[str] = Field(default=None, description="""Human-readable label for the unit (e.g., \"kg\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity']} })


class QuantityRange(ConfiguredBaseModel):
    """
    A range of quantities with lower and upper bounds
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fhir:Range',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    lower_bound: Optional[Quantity] = Field(default=None, description="""The lower bound of the range""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityRange']} })
    upper_bound: Optional[Quantity] = Field(default=None, description="""The upper bound of the range""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityRange']} })


class OntologyReference(ConfiguredBaseModel):
    """
    A reference to an ontology term with both identifier and human-readable name. Used for measured entities, phenotypes, and other ontology-backed concepts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: Optional[str] = Field(default=None, description="""The ontology term identifier (e.g., CHEBI:25016, GO:0005929)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference']} })
    name: Optional[str] = Field(default=None, description="""Human-readable name for the term (e.g., \"Lead\", \"Cilium\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference']} })


class GeneReference(ConfiguredBaseModel):
    """
    A reference to a gene with identifier, name, and symbol. Used for target_gene in expression measurements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: Optional[str] = Field(default=None, description="""The gene identifier (e.g., NCBIGENE:4586)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference']} })
    name: Optional[str] = Field(default=None, description="""Full gene name (e.g., \"Mucin 5AC, oligomeric mucus/gel-forming\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference']} })
    symbol: Optional[str] = Field(default=None, description="""Gene symbol (e.g., \"MUC5AC\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneReference', 'Gene']} })


class ProteinReference(ConfiguredBaseModel):
    """
    A reference to a protein with identifier, name, and encoding gene. Used for target_protein in expression measurements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: Optional[str] = Field(default=None, description="""The protein identifier (e.g., PR:000007223)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference']} })
    name: Optional[str] = Field(default=None, description="""Protein name (e.g., \"Epidermal growth factor receptor\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference']} })
    encoded_by_gene: Optional[GeneReference] = Field(default=None, description="""The gene that encodes this protein""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinReference', 'Protein']} })


class TissueReference(ConfiguredBaseModel):
    """
    A reference to an anatomical tissue or structure with identifier and name. Used for tissue_context in expression measurements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: Optional[str] = Field(default=None, description="""The anatomy identifier (e.g., UBERON:0002031)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference']} })
    name: Optional[str] = Field(default=None, description="""Tissue/anatomy name (e.g., \"bronchial epithelium\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference']} })


class CellTypeReference(ConfiguredBaseModel):
    """
    A reference to a cell type with identifier and name. Used for cell_type_context in expression measurements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: Optional[str] = Field(default=None, description="""The cell type identifier (e.g., CL:0000160)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference']} })
    name: Optional[str] = Field(default=None, description="""Cell type name (e.g., \"goblet cell\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference']} })


class ParticipantReference(ConfiguredBaseModel):
    """
    A reference to a study participant with identifier. Used when referring to participants in measurements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: Optional[str] = Field(default=None, description="""The participant identifier (e.g., owg:participant-001)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference']} })


class CohortReference(ConfiguredBaseModel):
    """
    A reference to a cohort with identifier. Used when referring to cohorts in aggregated measurements and participants.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: Optional[str] = Field(default=None, description="""The cohort identifier (e.g., owg:cohort-001)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference']} })


class StudyReference(ConfiguredBaseModel):
    """
    A reference to a study with identifier. Used when referring to studies in cohorts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: Optional[str] = Field(default=None, description="""The study identifier (e.g., owg:study-001)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference']} })


class BiologicalEntity(NamedThing):
    """
    Biological entities including genes, proteins, cells, and anatomical structures
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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

    exposed_to_chemical: Optional[str] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class BiologicalResponse(NamedThing):
    """
    A biological response at the molecular, cellular, or tissue level
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class HealthOutcome(NamedThing):
    """
    A health-related outcome including phenotypes and diseases
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class StudyEntity(NamedThing):
    """
    Entities related to studies, cohorts, and participants
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Measurement(NamedThing):
    """
    A measurement observation with a typed quantity value and optional reference ranges
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented (e.g., 'blood lead level', 'BMI'). This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[Quantity] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[Quantity] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[Quantity] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Association(NamedThing):
    """
    A relationship between two entities
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ChemicalExposure(ExposureEvent):
    """
    Exposure to a chemical substance
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:0000006',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    exposed_to_chemical: Optional[str] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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
    exposed_to_chemical: Optional[str] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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
    exposed_to_chemical: Optional[str] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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
    exposed_to_chemical: Optional[str] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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
    affected_anatomy: Optional[str] = Field(default=None, description="""Anatomical location affected""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class AdverseOutcome(HealthOutcome):
    """
    An adverse health outcome in the context of an Adverse Outcome Pathway
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    outcome_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""Level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcome']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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
    data_source: Optional[DataSourceEnum] = Field(default=None, description="""Source database or repository""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    principal_investigator: Optional[str] = Field(default=None, description="""Principal investigator name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    publications: Optional[list[str]] = Field(default=[], description="""Related publications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Cohort(StudyEntity):
    """
    A group of individuals in a study
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    part_of_study: Optional[StudyReference] = Field(default=None, description="""Study that this cohort is part of, with identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })
    cohort_size: Optional[int] = Field(default=None, description="""Number of participants in cohort""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })
    inclusion_criteria: Optional[str] = Field(default=None, description="""Criteria for cohort inclusion""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Participant(StudyEntity):
    """
    An individual participant in a study
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    part_of_cohort: Optional[CohortReference] = Field(default=None, description="""Cohort that this participant is part of, with identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant'], 'slot_uri': 'biolink:member_of'} })
    participant_id: Optional[str] = Field(default=None, description="""Participant identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    age: Optional[int] = Field(default=None, description="""Age in years""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    sex: Optional[SexEnum] = Field(default=None, description="""Biological sex""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    species: Optional[str] = Field(default=None, description="""Species name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant', 'Organism']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ExposureMeasurement(Measurement):
    """
    A measurement of exposure to a chemical or environmental factor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    measured_entity: Optional[OntologyReference] = Field(default=None, description="""The entity being measured, with both identifier and human-readable name. Examples: chemical compounds (CHEBI), cell types (CL), biological processes (GO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AggregatedMeasurement']} })
    participant: Optional[ParticipantReference] = Field(default=None, description="""The participant being measured, with identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
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
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement']} })
    source_database_record: Optional[str] = Field(default=None, description="""Link to original database record (URI or CURIE)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement']} })
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented (e.g., 'blood lead level', 'BMI'). This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[Quantity] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[Quantity] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[Quantity] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class BiomarkerMeasurement(Measurement):
    """
    A measurement of a biological marker
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    biomarker_type: Optional[str] = Field(default=None, description="""Type of biomarker""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiomarkerMeasurement']} })
    measured_entity: Optional[OntologyReference] = Field(default=None, description="""The entity being measured, with both identifier and human-readable name. Examples: chemical compounds (CHEBI), cell types (CL), biological processes (GO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AggregatedMeasurement']} })
    participant: Optional[ParticipantReference] = Field(default=None, description="""The participant being measured, with identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
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
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented (e.g., 'blood lead level', 'BMI'). This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[Quantity] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[Quantity] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[Quantity] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class PhenotypeMeasurement(Measurement):
    """
    A measurement of a phenotypic trait or functional assay
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    phenotype: Optional[OntologyReference] = Field(default=None, description="""The phenotype being measured, with identifier and name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeMeasurement',
                       'ExposureToPhenotypeAssociation',
                       'GeneticVariantToPhenotypeAssociation']} })
    measured_entity: Optional[OntologyReference] = Field(default=None, description="""The entity being measured, with both identifier and human-readable name. Examples: chemical compounds (CHEBI), cell types (CL), biological processes (GO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AggregatedMeasurement']} })
    participant: Optional[ParticipantReference] = Field(default=None, description="""The participant being measured, with identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
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
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented (e.g., 'blood lead level', 'BMI'). This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[Quantity] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[Quantity] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[Quantity] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class AggregatedMeasurement(Measurement):
    """
    An aggregated or summary measurement across a cohort or population
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    measured_entity: Optional[OntologyReference] = Field(default=None, description="""The entity being measured, with both identifier and human-readable name. Examples: chemical compounds (CHEBI), cell types (CL), biological processes (GO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AggregatedMeasurement']} })
    cohort: Optional[CohortReference] = Field(default=None, description="""The cohort for aggregated measurements, with identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    summary_statistic: Optional[SummaryStatisticEnum] = Field(default=None, description="""Type of summary statistic""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    sample_size: Optional[int] = Field(default=None, description="""Number of samples""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    stratification: Optional[str] = Field(default=None, description="""Stratification variables""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented (e.g., 'blood lead level', 'BMI'). This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[Quantity] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[Quantity] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[Quantity] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class GeneExpressionMeasurement(Measurement):
    """
    A measurement of gene expression (mRNA level) in a specific biological context. Captures the target gene, tissue/cell type context, and assay methodology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    target_gene: Optional[GeneReference] = Field(default=None, description="""The gene whose expression is being measured, with identifier, name, and symbol. Use this to specify the exact gene target (e.g., MUC5AC, EGFR, IL8).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement']} })
    tissue_context: Optional[TissueReference] = Field(default=None, description="""The anatomical tissue or structure where expression was measured, with identifier and name (e.g., bronchial epithelium, lung, nasal mucosa).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    cell_type_context: Optional[CellTypeReference] = Field(default=None, description="""The specific cell type where expression was measured, with identifier and name (e.g., goblet cell, ciliated cell, basal cell).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    assay_method: Optional[ExpressionAssayMethodEnum] = Field(default=None, description="""The experimental method used to measure expression. Captures whether this was qRT-PCR, RNA-seq, Western blot, IHC, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    normalization_reference: Optional[str] = Field(default=None, description="""The reference gene or protein used for normalization (e.g., GAPDH, beta-actin, 18S rRNA, total protein).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    participant: Optional[ParticipantReference] = Field(default=None, description="""The participant being measured, with identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented (e.g., 'blood lead level', 'BMI'). This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[Quantity] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[Quantity] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[Quantity] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ProteinExpressionMeasurement(Measurement):
    """
    A measurement of protein expression or post-translational modification (e.g., phosphorylation) in a specific biological context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    target_protein: Optional[ProteinReference] = Field(default=None, description="""The protein whose expression or modification is being measured, with identifier, name, and optionally the encoding gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinExpressionMeasurement']} })
    phosphorylation_site: Optional[str] = Field(default=None, description="""For protein phosphorylation measurements, the specific amino acid residue that is phosphorylated (e.g., Y1068, S473, T308).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinExpressionMeasurement']} })
    tissue_context: Optional[TissueReference] = Field(default=None, description="""The anatomical tissue or structure where expression was measured, with identifier and name (e.g., bronchial epithelium, lung, nasal mucosa).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    cell_type_context: Optional[CellTypeReference] = Field(default=None, description="""The specific cell type where expression was measured, with identifier and name (e.g., goblet cell, ciliated cell, basal cell).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    assay_method: Optional[ExpressionAssayMethodEnum] = Field(default=None, description="""The experimental method used to measure expression. Captures whether this was qRT-PCR, RNA-seq, Western blot, IHC, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    normalization_reference: Optional[str] = Field(default=None, description="""The reference gene or protein used for normalization (e.g., GAPDH, beta-actin, 18S rRNA, total protein).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionMeasurement', 'ProteinExpressionMeasurement']} })
    participant: Optional[ParticipantReference] = Field(default=None, description="""The participant being measured, with identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'GeneExpressionMeasurement',
                       'ProteinExpressionMeasurement']} })
    observation_type: Optional[MeasurementTypeEnum] = Field(default=None, description="""The type of observation being represented (e.g., 'blood lead level', 'BMI'). This field holds the key in the core key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quantity_measured: Optional[Quantity] = Field(default=None, description="""The measured quantity value with its unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_low: Optional[Quantity] = Field(default=None, description="""Lower bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    range_high: Optional[Quantity] = Field(default=None, description="""Upper bound of reference range (e.g., from a laboratory). Set to NULL if not provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Gene(BiologicalEntity):
    """
    A gene or genetic element
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    ncbigene_id: Optional[str] = Field(default=None, description="""NCBI Gene identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene']} })
    symbol: Optional[str] = Field(default=None, description="""Gene symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneReference', 'Gene']} })
    in_taxon: Optional[str] = Field(default=None, description="""Taxonomic group""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
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

    encoded_by_gene: Optional[str] = Field(default=None, description="""Gene that encodes this protein""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinReference', 'Protein']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class CellType(BiologicalEntity):
    """
    A type of cell
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CL:0000000',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    cl_id: Optional[str] = Field(default=None, description="""Cell Ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellType']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('cl_id')
    def pattern_cl_id(cls, v):
        pattern=re.compile(r"^CL:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid cl_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid cl_id format: {v}"
            raise ValueError(err_msg)
        return v


class AnatomicalEntity(BiologicalEntity):
    """
    An anatomical structure or system
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'UBERON:0001062',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    uberon_id: Optional[str] = Field(default=None, description="""UBERON anatomical identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalEntity']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('uberon_id')
    def pattern_uberon_id(cls, v):
        pattern=re.compile(r"^UBERON:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid uberon_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid uberon_id format: {v}"
            raise ValueError(err_msg)
        return v


class Organism(BiologicalEntity):
    """
    An individual organism
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    species: Optional[str] = Field(default=None, description="""Species name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant', 'Organism']} })
    taxon_id: Optional[str] = Field(default=None, description="""NCBI Taxonomy identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organism']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ExposureToPhenotypeAssociation(Association):
    """
    An association between an exposure and a phenotype
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    exposure: Optional[str] = Field(default=None, description="""Exposure in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation']} })
    phenotype: Optional[OntologyReference] = Field(default=None, description="""The phenotype being measured, with identifier and name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeMeasurement',
                       'ExposureToPhenotypeAssociation',
                       'GeneticVariantToPhenotypeAssociation']} })
    association_type: Optional[str] = Field(default=None, description="""Type of association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation', 'GeneToDiseaseAssociation']} })
    evidence: Optional[str] = Field(default=None, description="""Evidence for association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ChemicalToGeneAssociation(Association):
    """
    An association between a chemical and a gene
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    chemical: Optional[str] = Field(default=None, description="""Chemical in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation']} })
    gene: Optional[str] = Field(default=None, description="""Gene in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation', 'GeneToDiseaseAssociation']} })
    interaction_type: Optional[str] = Field(default=None, description="""Type of interaction""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class GeneToDiseaseAssociation(Association):
    """
    An association between a gene and a disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    gene: Optional[str] = Field(default=None, description="""Gene in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation', 'GeneToDiseaseAssociation']} })
    disease: Optional[str] = Field(default=None, description="""Disease in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneToDiseaseAssociation']} })
    association_type: Optional[str] = Field(default=None, description="""Type of association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation', 'GeneToDiseaseAssociation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class GeneticVariantToPhenotypeAssociation(Association):
    """
    An association between a genetic variant and a phenotype (e.g., from GWAS)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/outcomes_working_group'})

    genetic_variant: Optional[str] = Field(default=None, description="""Genetic variant identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticVariantToPhenotypeAssociation']} })
    phenotype: Optional[OntologyReference] = Field(default=None, description="""The phenotype being measured, with identifier and name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeMeasurement',
                       'ExposureToPhenotypeAssociation',
                       'GeneticVariantToPhenotypeAssociation']} })
    p_value: Optional[float] = Field(default=None, description="""Statistical p-value""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticVariantToPhenotypeAssociation']} })
    effect_size: Optional[float] = Field(default=None, description="""Effect size of association""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticVariantToPhenotypeAssociation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'UnitConcept',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference',
                       'ParticipantReference',
                       'CohortReference',
                       'StudyReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing',
                       'OntologyReference',
                       'GeneReference',
                       'ProteinReference',
                       'TissueReference',
                       'CellTypeReference'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Container.model_rebuild()
NamedThing.model_rebuild()
UnitConcept.model_rebuild()
Quantity.model_rebuild()
QuantityRange.model_rebuild()
OntologyReference.model_rebuild()
GeneReference.model_rebuild()
ProteinReference.model_rebuild()
TissueReference.model_rebuild()
CellTypeReference.model_rebuild()
ParticipantReference.model_rebuild()
CohortReference.model_rebuild()
StudyReference.model_rebuild()
BiologicalEntity.model_rebuild()
ChemicalEntity.model_rebuild()
ExposureEvent.model_rebuild()
BiologicalResponse.model_rebuild()
HealthOutcome.model_rebuild()
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
Gene.model_rebuild()
Protein.model_rebuild()
CellType.model_rebuild()
AnatomicalEntity.model_rebuild()
Organism.model_rebuild()
ExposureToPhenotypeAssociation.model_rebuild()
ChemicalToGeneAssociation.model_rebuild()
GeneToDiseaseAssociation.model_rebuild()
GeneticVariantToPhenotypeAssociation.model_rebuild()
