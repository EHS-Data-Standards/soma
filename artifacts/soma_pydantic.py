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


linkml_meta = LinkMLMeta({'default_prefix': 'soma',
     'default_range': 'string',
     'description': 'A LinkML data model for representing biological assays, '
                    'measurements, and experimental protocols in the context of '
                    'outcomes research. The schema is centered around ASSAYS that '
                    'inform on Key Events in Adverse Outcome Pathways (AOPs), with '
                    'named slots for specific measurements.\n'
                    'This is the main entry point that imports the AOP framework, '
                    'assay base schema, and domain-specific assay microschemas.',
     'id': 'https://w3id.org/EHS-Data-Standards/soma',
     'imports': ['linkml:types',
                 'aop_framework',
                 'assay_base',
                 'assay_microschemas'],
     'license': 'MIT',
     'name': 'soma',
     'prefixes': {'CHEBI': {'prefix_prefix': 'CHEBI',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CL_'},
                  'ECTO': {'prefix_prefix': 'ECTO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ECTO_'},
                  'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'NCBITaxon': {'prefix_prefix': 'NCBITaxon',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'QUDT': {'prefix_prefix': 'QUDT',
                           'prefix_reference': 'http://qudt.org/vocab/unit/'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'UCUM': {'prefix_prefix': 'UCUM',
                           'prefix_reference': 'http://unitsofmeasure.org/'},
                  'UO': {'prefix_prefix': 'UO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/UO_'},
                  'aop_framework': {'prefix_prefix': 'aop_framework',
                                    'prefix_reference': 'https://w3id.org/EHS-Data-Standards/aop_framework/'},
                  'assay_base': {'prefix_prefix': 'assay_base',
                                 'prefix_reference': 'https://w3id.org/EHS-Data-Standards/assay_base/'},
                  'assay_microschemas': {'prefix_prefix': 'assay_microschemas',
                                         'prefix_reference': 'https://w3id.org/EHS-Data-Standards/assay_microschemas/'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'owg': {'prefix_prefix': 'owg',
                          'prefix_reference': 'https://w3id.org/EHS-Data-Standards/soma/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'soma': {'prefix_prefix': 'soma',
                           'prefix_reference': 'https://w3id.org/EHS-Data-Standards/soma/'}},
     'see_also': ['https://EHS-Data-Standards.github.io/soma'],
     'source_file': 'src/soma/schema/soma.yaml',
     'title': 'SOMA Schema'} )

class BiologicalActionEnum(str, Enum):
    """
    Types of biological changes or actions in key events.
    """
    increased = "increased"
    """
    Increased level or activity
    """
    decreased = "decreased"
    """
    Decreased level or activity
    """
    altered = "altered"
    """
    Altered function or state (not quantitative)
    """
    impaired = "impaired"
    """
    Impaired function
    """
    disrupted = "disrupted"
    """
    Disrupted process or structure
    """
    activated = "activated"
    """
    Activated process or pathway
    """
    inhibited = "inhibited"
    """
    Inhibited process or pathway
    """


class BiologicalOrganizationLevelEnum(str, Enum):
    """
    Levels of biological organization for key events.
    """
    molecular = "molecular"
    """
    Molecular level (genes, proteins, metabolites)
    """
    cellular = "cellular"
    """
    Cellular level (cell function, signaling)
    """
    tissue = "tissue"
    """
    Tissue level (tissue structure, function)
    """
    organ = "organ"
    """
    Organ level (organ function)
    """
    organism = "organism"
    """
    Whole organism level (systemic effects)
    """
    population = "population"
    """
    Population level (ecological effects)
    """


class EvidenceSupportEnum(str, Enum):
    """
    Levels of evidence support for key event relationships.
    """
    strong = "strong"
    """
    Strong empirical support with mechanistic understanding
    """
    moderate = "moderate"
    """
    Moderate support with some mechanistic evidence
    """
    weak = "weak"
    """
    Limited evidence or indirect support
    """
    not_specified = "not_specified"
    """
    Evidence level not specified
    """


class QuantitativeUnderstandingEnum(str, Enum):
    """
    Levels of quantitative understanding for key event relationships.
    """
    high = "high"
    """
    Response-response relationship well characterized
    """
    moderate = "moderate"
    """
    Some quantitative data available
    """
    low = "low"
    """
    Limited quantitative understanding
    """
    not_specified = "not_specified"
    """
    Quantitative understanding not specified
    """


class OutcomeLevelEnum(str, Enum):
    """
    Levels at which adverse outcomes manifest.
    """
    individual = "individual"
    """
    Adverse outcome in an individual organism
    """
    population = "population"
    """
    Adverse outcome at the population level
    """


class SampleTypeEnum(str, Enum):
    """
    Types of biological samples for in vivo assays.
    """
    urine = "urine"
    """
    Urine sample
    """
    blood = "blood"
    """
    Blood sample
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
    Exhaled breath condensate
    """
    biopsy = "biopsy"
    """
    Tissue biopsy
    """
    sweat = "sweat"
    """
    Sweat sample
    """


class CellCultureGrowthModeEnum(str, Enum):
    """
    Cell culture growth modes.
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
    Cells cultured at air-liquid interface (ALI)
    """
    three_dimensional = "three_dimensional"
    """
    Cells grown in 3D matrix or scaffold
    """
    organoid = "organoid"
    """
    Self-organizing 3D tissue culture
    """
    spheroid = "spheroid"
    """
    Spherical cellular aggregates
    """


class SubstrateTypeEnum(str, Enum):
    """
    Types of cell culture substrates.
    """
    plastic = "plastic"
    """
    Standard tissue culture-treated plastic
    """
    collagen_coated = "collagen_coated"
    """
    Collagen-coated surface
    """
    matrigel = "matrigel"
    """
    Basement membrane matrix
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
    Permeable support for ALI culture
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
    Polydimethylsiloxane (microfluidics)
    """


class SupplementTypeEnum(str, Enum):
    """
    Categories of cell culture medium supplements.
    """
    growth_factor = "growth_factor"
    """
    Proteins that stimulate cell growth
    """
    antibiotic = "antibiotic"
    """
    Antimicrobial substances
    """
    antifungal = "antifungal"
    """
    Antifungal agents
    """
    hormone = "hormone"
    """
    Signaling molecules
    """
    vitamin = "vitamin"
    """
    Essential vitamins
    """
    amino_acid = "amino_acid"
    """
    Amino acid supplements
    """
    lipid = "lipid"
    """
    Lipid supplements
    """
    trace_element = "trace_element"
    """
    Essential trace elements
    """
    attachment_factor = "attachment_factor"
    """
    Factors promoting cell attachment
    """
    differentiation_factor = "differentiation_factor"
    """
    Factors promoting cell differentiation
    """


class AssayContextCapabilityEnum(str, Enum):
    """
    Indicates what experimental contexts an assay class supports. Used to constrain valid study_subject types and enable context-appropriate slots.
    """
    in_vitro_only = "in_vitro_only"
    """
    Assay can only be performed in vitro (cell cultures, tissue slices, organoids, etc.)
    """
    in_vivo_only = "in_vivo_only"
    """
    Assay can only be performed in vivo (requires samples from or measurements on living human or animal subjects)
    """
    in_vitro_or_in_vivo = "in_vitro_or_in_vivo"
    """
    Assay can be performed in either in vitro or in vivo contexts depending on the experimental design
    """


class CiliaryMotionPatternEnum(str, Enum):
    """
    Patterns of ciliary motion.
    """
    coordinated = "coordinated"
    """
    Normal coordinated beating pattern
    """
    dyskinetic = "dyskinetic"
    """
    Abnormal dyskinetic motion
    """
    immotile = "immotile"
    """
    Non-motile/static cilia
    """
    rotational = "rotational"
    """
    Rotational motion pattern
    """
    stiff = "stiff"
    """
    Stiff/rigid beating
    """


class DirectionalityEnum(str, Enum):
    """
    Directionality of mucociliary transport.
    """
    normal = "normal"
    """
    Normal directed transport
    """
    reversed = "reversed"
    """
    Reversed transport direction
    """
    absent = "absent"
    """
    No directed transport
    """
    variable = "variable"
    """
    Variable/inconsistent direction
    """



class NamedThing(ConfiguredBaseModel):
    """
    A generic entity with an identifier and name. Base class for all named entities in the schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop_framework'})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class KeyEvent(NamedThing):
    """
    A measurable change in biological state that is a step in an Adverse Outcome Pathway. Key Events represent the biological perturbations that assays measure to provide evidence for AOP-based mechanistic understanding. Key events can be Molecular Initiating Events (MIEs), intermediate Key Events, or Adverse Outcomes at the organism/population level.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:1000000',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/aop_framework'})

    biological_process: Optional[str] = Field(default=None, description="""The biological process affected by this key event. Should reference a GO biological process term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent', 'AdverseOutcome']} })
    biological_object: Optional[str] = Field(default=None, description="""The biological entity affected (protein, cell, tissue, organ).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_action: Optional[BiologicalActionEnum] = Field(default=None, description="""The type of change (increased, decreased, altered, impaired).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    level_of_biological_organization: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization at which this key event occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    occurs_in_cell_type: Optional[str] = Field(default=None, description="""The cell type in which this key event occurs. Should reference a Cell Ontology (CL) term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    occurs_in_anatomy: Optional[str] = Field(default=None, description="""The anatomical location where this key event occurs. Should reference a UBERON anatomy term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent', 'AdverseOutcome']} })
    aopwiki_id: Optional[str] = Field(default=None, description="""The AOP-Wiki identifier for this entity (e.g., \"AOP:411\" for an AOP, \"KE:1234\" for a key event).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent', 'AdverseOutcome', 'AdverseOutcomePathway']} })
    upstream_key_events: Optional[list[KeyEvent]] = Field(default=[], description="""Key events that lead to this key event (upstream in the pathway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_key_events: Optional[list[KeyEvent]] = Field(default=[], description="""Key events that follow this key event (downstream in the pathway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })

    @field_validator('biological_process')
    def pattern_biological_process(cls, v):
        pattern=re.compile(r"^GO:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid biological_process format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid biological_process format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('occurs_in_cell_type')
    def pattern_occurs_in_cell_type(cls, v):
        pattern=re.compile(r"^CL:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid occurs_in_cell_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid occurs_in_cell_type format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('occurs_in_anatomy')
    def pattern_occurs_in_anatomy(cls, v):
        pattern=re.compile(r"^UBERON:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid occurs_in_anatomy format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid occurs_in_anatomy format: {v}"
            raise ValueError(err_msg)
        return v


class KeyEventRelationship(NamedThing):
    """
    A directional relationship between two key events in an AOP. Represents the causal linkage between an upstream event and a downstream event with supporting evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop_framework'})

    upstream_event: Optional[KeyEvent] = Field(default=None, description="""The upstream key event in this relationship (cause).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    downstream_event: Optional[KeyEvent] = Field(default=None, description="""The downstream key event in this relationship (effect).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    relationship_type: Optional[str] = Field(default=None, description="""The type of causal relationship (directly leads to, indirectly leads to).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    evidence_support: Optional[EvidenceSupportEnum] = Field(default=None, description="""Level of evidence supporting this key event relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    quantitative_understanding: Optional[QuantitativeUnderstandingEnum] = Field(default=None, description="""Level of quantitative understanding of the relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class AdverseOutcome(NamedThing):
    """
    An adverse health outcome at the organism or population level that represents the apical endpoint of an Adverse Outcome Pathway. This is the final, clinically or ecologically relevant effect.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop_framework'})

    outcome_level: Optional[OutcomeLevelEnum] = Field(default=None, description="""The level at which the adverse outcome manifests (individual, population).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcome']} })
    biological_process: Optional[str] = Field(default=None, description="""The biological process affected by this key event. Should reference a GO biological process term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent', 'AdverseOutcome']} })
    occurs_in_anatomy: Optional[str] = Field(default=None, description="""The anatomical location where this key event occurs. Should reference a UBERON anatomy term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent', 'AdverseOutcome']} })
    aopwiki_id: Optional[str] = Field(default=None, description="""The AOP-Wiki identifier for this entity (e.g., \"AOP:411\" for an AOP, \"KE:1234\" for a key event).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent', 'AdverseOutcome', 'AdverseOutcomePathway']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })

    @field_validator('biological_process')
    def pattern_biological_process(cls, v):
        pattern=re.compile(r"^GO:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid biological_process format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid biological_process format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('occurs_in_anatomy')
    def pattern_occurs_in_anatomy(cls, v):
        pattern=re.compile(r"^UBERON:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid occurs_in_anatomy format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid occurs_in_anatomy format: {v}"
            raise ValueError(err_msg)
        return v


class AdverseOutcomePathway(NamedThing):
    """
    A sequence of causally linked events at different levels of biological organization that lead from a molecular initiating event through intermediate key events to an adverse health outcome. AOPs provide a structured framework for organizing mechanistic evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop_framework'})

    aopwiki_id: Optional[str] = Field(default=None, description="""The AOP-Wiki identifier for this entity (e.g., \"AOP:411\" for an AOP, \"KE:1234\" for a key event).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent', 'AdverseOutcome', 'AdverseOutcomePathway']} })
    molecular_initiating_event: Optional[MolecularInitiatingEvent] = Field(default=None, description="""The molecular initiating event that starts this AOP.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    key_events: Optional[list[KeyEvent]] = Field(default=[], description="""The key events in this AOP (intermediate events between MIE and AO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway', 'Container']} })
    key_event_relationships: Optional[list[KeyEventRelationship]] = Field(default=[], description="""The key event relationships connecting events in this AOP.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    adverse_outcome: Optional[AdverseOutcome] = Field(default=None, description="""The adverse outcome that is the apical endpoint of this AOP.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    stressors: Optional[list[str]] = Field(default=[], description="""Chemical or physical stressors that can trigger this AOP.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class MolecularInitiatingEvent(KeyEvent):
    """
    The initial molecular-level perturbation that starts an Adverse Outcome Pathway. The MIE is the direct interaction between a stressor and a biological target (e.g., receptor binding, enzyme inhibition).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/aop_framework'})

    target_molecule: Optional[str] = Field(default=None, description="""The molecular target of the stressor in the MIE (e.g., receptor, enzyme).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent']} })
    biological_process: Optional[str] = Field(default=None, description="""The biological process affected by this key event. Should reference a GO biological process term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent', 'AdverseOutcome']} })
    biological_object: Optional[str] = Field(default=None, description="""The biological entity affected (protein, cell, tissue, organ).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    biological_action: Optional[BiologicalActionEnum] = Field(default=None, description="""The type of change (increased, decreased, altered, impaired).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    level_of_biological_organization: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""The level of biological organization at which this key event occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    occurs_in_cell_type: Optional[str] = Field(default=None, description="""The cell type in which this key event occurs. Should reference a Cell Ontology (CL) term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    occurs_in_anatomy: Optional[str] = Field(default=None, description="""The anatomical location where this key event occurs. Should reference a UBERON anatomy term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent', 'AdverseOutcome']} })
    aopwiki_id: Optional[str] = Field(default=None, description="""The AOP-Wiki identifier for this entity (e.g., \"AOP:411\" for an AOP, \"KE:1234\" for a key event).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent', 'AdverseOutcome', 'AdverseOutcomePathway']} })
    upstream_key_events: Optional[list[KeyEvent]] = Field(default=[], description="""Key events that lead to this key event (upstream in the pathway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    downstream_key_events: Optional[list[KeyEvent]] = Field(default=[], description="""Key events that follow this key event (downstream in the pathway).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })

    @field_validator('biological_process')
    def pattern_biological_process(cls, v):
        pattern=re.compile(r"^GO:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid biological_process format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid biological_process format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('occurs_in_cell_type')
    def pattern_occurs_in_cell_type(cls, v):
        pattern=re.compile(r"^CL:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid occurs_in_cell_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid occurs_in_cell_type format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('occurs_in_anatomy')
    def pattern_occurs_in_anatomy(cls, v):
        pattern=re.compile(r"^UBERON:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid occurs_in_anatomy format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid occurs_in_anatomy format: {v}"
            raise ValueError(err_msg)
        return v


class Assay(NamedThing):
    """
    A planned process with the objective to produce information about biological state relevant to a Key Event in an Adverse Outcome Pathway. Assays are organized by the functional domain they assess (e.g., ciliary function, oxidative stress), and each domain-specific assay class contains named slots for the specific measurements it can produce. Assays inform on key events and contain the measurement data as named slots.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'OBI:0000070',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    informs_on_key_event: Optional[KeyEvent] = Field(default=None, description="""The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    study_subject: Optional[Union[StudySubject,ModelSystem,InVivoSubject,PopulationSubject,CellularSystem]] = Field(default=None, description="""The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_exposure_condition: Optional[list[ExposureCondition]] = Field(default=[], description="""The exposure condition(s) applied to the study subject. Captures the agent, concentration, duration, and timing of exposure/treatment. Multivalued to support co-exposures or dose-response series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    follows_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""The Protocol(s) that this assay follows. Any Protocol or Protocol subclass (ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is valid. Use this for general protocol references; assay subclasses also have typed protocol slots for domain-specific protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_specified_output: Optional[AssayOutputMeasurement] = Field(default=None, description="""The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000299']} })
    assay_date: Optional[date] = Field(default=None, description="""Date when the assay was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class AssayOutputMeasurement(NamedThing):
    """
    The measurement results produced by an assay. The specified output of a planned process. Each domain-specific assay class has a corresponding AssayOutputMeasurement subclass containing the named measurement slots for that assay type. This class represents the \"output\" in the Input/Process/Output model: what was measured and what values were obtained.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'exact_mappings': ['IAO:0000109'],
         'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class StudySubject(NamedThing):
    """
    The subject of a study — what the assay is performed on. Subclasses capture different experimental contexts (model systems, living subjects, populations) with context-appropriate slots. The type of subject determines which slots are available, replacing the old mixin pattern.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    subject_type: Literal["StudySubject"] = Field(default="StudySubject", description="""The specific type of study subject. Used to designate which concrete class (e.g., CellularSystem, InVivoSubject) is instantiated for polymorphic study_subject slots.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['StudySubject']} })
    model_species: Optional[SpeciesReference] = Field(default=None, description="""The species of origin for the cells or organism being studied. Reference to NCBITaxon term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudySubject', 'CellLine']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class ModelSystem(StudySubject):
    """
    An in vitro or ex vivo model system used to study biological processes. Parent class for cell-based and other model systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    subject_type: Literal["ModelSystem"] = Field(default="ModelSystem", description="""The specific type of study subject. Used to designate which concrete class (e.g., CellularSystem, InVivoSubject) is instantiated for polymorphic study_subject slots.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['StudySubject']} })
    model_species: Optional[SpeciesReference] = Field(default=None, description="""The species of origin for the cells or organism being studied. Reference to NCBITaxon term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudySubject', 'CellLine']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class InVivoSubject(StudySubject):
    """
    A living human or animal subject from whom measurements are taken. Used for clinical assays (lung function, BALF/sputum) and any assay performed on living subjects.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    age: Optional[QuantityValue] = Field(default=None, description="""Age of the subject.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoSubject']} })
    sex: Optional[str] = Field(default=None, description="""Biological sex of the subject.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoSubject']} })
    subject_characteristics: Optional[str] = Field(default=None, description="""Relevant subject characteristics (disease state, medications, etc.). TIER 1 for LungFunctionAssay per user feedback.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoSubject']} })
    disease_state: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoSubject', 'CellLine']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample (e.g., sputum, BALF, blood).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoSubject']} })
    collection_site: Optional[str] = Field(default=None, description="""Anatomical site of sample collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoSubject']} })
    collection_date: Optional[date] = Field(default=None, description="""Date when the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoSubject']} })
    sample_collection_method: Optional[str] = Field(default=None, description="""Method used for sample collection in vivo (e.g., bronchoscopy, induced sputum, spirometry).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoSubject']} })
    clinical_context: Optional[str] = Field(default=None, description="""Clinical context for in vivo measurements (e.g., routine screening, post-exposure assessment, disease monitoring, baseline spirometry).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoSubject']} })
    subject_type: Literal["InVivoSubject"] = Field(default="InVivoSubject", description="""The specific type of study subject. Used to designate which concrete class (e.g., CellularSystem, InVivoSubject) is instantiated for polymorphic study_subject slots.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['StudySubject']} })
    model_species: Optional[SpeciesReference] = Field(default=None, description="""The species of origin for the cells or organism being studied. Reference to NCBITaxon term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudySubject', 'CellLine']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class PopulationSubject(StudySubject):
    """
    A population or cohort of subjects studied in aggregate. Used for epidemiological or population-level analyses. Can optionally hold references to individual InVivoSubject members.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    cohort_size: Optional[int] = Field(default=None, description="""Number of subjects in the cohort or population.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PopulationSubject']} })
    inclusion_criteria: Optional[str] = Field(default=None, description="""Criteria for inclusion in the study population.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PopulationSubject']} })
    age_range: Optional[QuantityRange] = Field(default=None, description="""Age range of the study population.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PopulationSubject']} })
    subjects: Optional[list[InVivoSubject]] = Field(default=[], description="""Individual subjects in the population or cohort. Optional — use when individual-level data is available alongside aggregate cohort metadata.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PopulationSubject']} })
    subject_type: Literal["PopulationSubject"] = Field(default="PopulationSubject", description="""The specific type of study subject. Used to designate which concrete class (e.g., CellularSystem, InVivoSubject) is instantiated for polymorphic study_subject slots.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['StudySubject']} })
    model_species: Optional[SpeciesReference] = Field(default=None, description="""The species of origin for the cells or organism being studied. Reference to NCBITaxon term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudySubject', 'CellLine']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class Protocol(NamedThing):
    """
    A detailed set of steps for how to perform a specific assay. Protocols ensure reproducibility across laboratories. Contains universal slots; domain-specific details are in protocol subclasses (ImagingProtocol, StainingProtocol, etc.). Protocols can reference other protocols via sub_protocols to represent composite workflows (e.g., sample preparation, wash steps, or post-processing protocols that are shared across assays).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'OBI:0000272',
         'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    protocol_type: Literal["Protocol"] = Field(default="Protocol", description="""The specific type of protocol. Used to designate which concrete class (e.g., ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is instantiated for polymorphic protocol slots.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Protocol']} })
    protocol_version: Optional[str] = Field(default=None, description="""Version of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    equipment_required: Optional[list[str]] = Field(default=[], description="""Equipment required for this protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    sub_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""Other protocols that are part of this protocol's workflow. Use this to compose protocols from reusable steps (e.g., sample preparation, wash steps, fixation, post-processing). Any Protocol or Protocol subclass is valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    quality_control_criteria: Optional[str] = Field(default=None, description="""Quality control acceptance criteria.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    replicate_requirements: Optional[int] = Field(default=None, description="""Number of replicates required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    protocol_author: Optional[str] = Field(default=None, description="""Author of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    institution: Optional[str] = Field(default=None, description="""Institution where protocol was developed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    publication_reference: Optional[str] = Field(default=None, description="""Reference to protocol publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    last_updated: Optional[date] = Field(default=None, description="""Date protocol was last updated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    validation_status: Optional[str] = Field(default=None, description="""Validation status of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class ImagingProtocol(Protocol):
    """
    Protocol for imaging-based assays (CBF, ASL, MCC). Captures frame rate, duration, resolution, and tracer/labeling details.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    imaging_frame_rate: Optional[QuantityValue] = Field(default=None, description="""Frame rate for video/imaging acquisition (e.g., 200 fps).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImagingProtocol']} })
    imaging_duration: Optional[QuantityValue] = Field(default=None, description="""Duration of imaging session.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImagingProtocol']} })
    spatial_resolution: Optional[QuantityValue] = Field(default=None, description="""Spatial resolution of imaging (e.g., 1-2 um axial resolution).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImagingProtocol']} })
    fluorescent_labeling: Optional[str] = Field(default=None, description="""Fluorescent label or tracer used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImagingProtocol']} })
    fluorescent_tracer: Optional[str] = Field(default=None, description="""Fluorescent tracer used for tracking (MCC assays).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImagingProtocol']} })
    evaporation_prevention: Optional[str] = Field(default=None, description="""Method used to prevent evaporation (e.g., perfluorocarbon overlay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImagingProtocol']} })
    particle_tracking_method: Optional[str] = Field(default=None, description="""Method used for tracking particles or mucus.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImagingProtocol']} })
    temperature_control: Optional[QuantityValue] = Field(default=None, description="""Temperature conditions during the procedure (e.g., 37C).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImagingProtocol']} })
    humidity_control: Optional[QuantityValue] = Field(default=None, description="""Humidity conditions during the procedure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImagingProtocol']} })
    particle_size: Optional[QuantityValue] = Field(default=None, description="""Size of tracking particles.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ImagingProtocol']} })
    protocol_type: Literal["ImagingProtocol"] = Field(default="ImagingProtocol", description="""The specific type of protocol. Used to designate which concrete class (e.g., ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is instantiated for polymorphic protocol slots.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Protocol']} })
    protocol_version: Optional[str] = Field(default=None, description="""Version of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    equipment_required: Optional[list[str]] = Field(default=[], description="""Equipment required for this protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    sub_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""Other protocols that are part of this protocol's workflow. Use this to compose protocols from reusable steps (e.g., sample preparation, wash steps, fixation, post-processing). Any Protocol or Protocol subclass is valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    quality_control_criteria: Optional[str] = Field(default=None, description="""Quality control acceptance criteria.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    replicate_requirements: Optional[int] = Field(default=None, description="""Number of replicates required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    protocol_author: Optional[str] = Field(default=None, description="""Author of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    institution: Optional[str] = Field(default=None, description="""Institution where protocol was developed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    publication_reference: Optional[str] = Field(default=None, description="""Reference to protocol publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    last_updated: Optional[date] = Field(default=None, description="""Date protocol was last updated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    validation_status: Optional[str] = Field(default=None, description="""Validation status of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class StainingProtocol(Protocol):
    """
    Protocol for staining-based assays (goblet cell, immunofluorescence). Captures staining type, antibodies, fixation, and detection details.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    staining_type: Optional[str] = Field(default=None, description="""Type of staining used (e.g., immunofluorescence, AB-PAS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['StainingProtocol']} })
    antibodies_used: Optional[list[str]] = Field(default=[], description="""Antibodies used in staining or detection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StainingProtocol', 'MolecularAssayProtocol']} })
    detection_method: Optional[str] = Field(default=None, description="""Detection method used (e.g., flow cytometry, plate reader).""", json_schema_extra = { "linkml_meta": {'domain_of': ['StainingProtocol', 'MolecularAssayProtocol']} })
    normalization_method: Optional[str] = Field(default=None, description="""Method used for data normalization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StainingProtocol', 'MolecularAssayProtocol']} })
    fixation_method: Optional[str] = Field(default=None, description="""Fixation method used for tissue/cell preparation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StainingProtocol']} })
    counterstain: Optional[str] = Field(default=None, description="""Counterstain used (e.g., hematoxylin, DAPI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['StainingProtocol']} })
    protocol_type: Literal["StainingProtocol"] = Field(default="StainingProtocol", description="""The specific type of protocol. Used to designate which concrete class (e.g., ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is instantiated for polymorphic protocol slots.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Protocol']} })
    protocol_version: Optional[str] = Field(default=None, description="""Version of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    equipment_required: Optional[list[str]] = Field(default=[], description="""Equipment required for this protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    sub_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""Other protocols that are part of this protocol's workflow. Use this to compose protocols from reusable steps (e.g., sample preparation, wash steps, fixation, post-processing). Any Protocol or Protocol subclass is valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    quality_control_criteria: Optional[str] = Field(default=None, description="""Quality control acceptance criteria.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    replicate_requirements: Optional[int] = Field(default=None, description="""Number of replicates required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    protocol_author: Optional[str] = Field(default=None, description="""Author of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    institution: Optional[str] = Field(default=None, description="""Institution where protocol was developed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    publication_reference: Optional[str] = Field(default=None, description="""Reference to protocol publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    last_updated: Optional[date] = Field(default=None, description="""Date protocol was last updated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    validation_status: Optional[str] = Field(default=None, description="""Validation status of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class SpirometryProtocol(Protocol):
    """
    Protocol for lung function / spirometry assays. Captures spirometry standards, bronchodilator details, and plethysmography method.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    spirometry_standard: Optional[str] = Field(default=None, description="""Spirometry standard followed (e.g., ATS/ERS 2019).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpirometryProtocol']} })
    bronchodilator_agent: Optional[str] = Field(default=None, description="""Bronchodilator agent used (e.g., albuterol).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpirometryProtocol']} })
    bronchodilator_dose: Optional[QuantityValue] = Field(default=None, description="""Dose of bronchodilator administered.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpirometryProtocol']} })
    plethysmography_method: Optional[str] = Field(default=None, description="""Method for plethysmography measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpirometryProtocol']} })
    protocol_type: Literal["SpirometryProtocol"] = Field(default="SpirometryProtocol", description="""The specific type of protocol. Used to designate which concrete class (e.g., ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is instantiated for polymorphic protocol slots.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Protocol']} })
    protocol_version: Optional[str] = Field(default=None, description="""Version of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    equipment_required: Optional[list[str]] = Field(default=[], description="""Equipment required for this protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    sub_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""Other protocols that are part of this protocol's workflow. Use this to compose protocols from reusable steps (e.g., sample preparation, wash steps, fixation, post-processing). Any Protocol or Protocol subclass is valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    quality_control_criteria: Optional[str] = Field(default=None, description="""Quality control acceptance criteria.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    replicate_requirements: Optional[int] = Field(default=None, description="""Number of replicates required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    protocol_author: Optional[str] = Field(default=None, description="""Author of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    institution: Optional[str] = Field(default=None, description="""Institution where protocol was developed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    publication_reference: Optional[str] = Field(default=None, description="""Reference to protocol publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    last_updated: Optional[date] = Field(default=None, description="""Date protocol was last updated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    validation_status: Optional[str] = Field(default=None, description="""Validation status of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class MolecularAssayProtocol(Protocol):
    """
    Protocol for molecular biology assays (qRT-PCR, Western blot, ELISA). Captures detection method, normalization, primers, and platform details.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    detection_method: Optional[str] = Field(default=None, description="""Detection method used (e.g., flow cytometry, plate reader).""", json_schema_extra = { "linkml_meta": {'domain_of': ['StainingProtocol', 'MolecularAssayProtocol']} })
    normalization_method: Optional[str] = Field(default=None, description="""Method used for data normalization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StainingProtocol', 'MolecularAssayProtocol']} })
    antibodies_used: Optional[list[str]] = Field(default=[], description="""Antibodies used in staining or detection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StainingProtocol', 'MolecularAssayProtocol']} })
    primer_sequences: Optional[list[str]] = Field(default=[], description="""Primer sequences used for PCR-based methods.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularAssayProtocol']} })
    reference_gene: Optional[str] = Field(default=None, description="""Reference/housekeeping gene used for normalization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularAssayProtocol']} })
    lysis_buffer: Optional[str] = Field(default=None, description="""Lysis buffer used for sample preparation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularAssayProtocol']} })
    platform: Optional[str] = Field(default=None, description="""Assay platform or instrument used (e.g., QuantStudio, Illumina).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularAssayProtocol']} })
    protocol_type: Literal["MolecularAssayProtocol"] = Field(default="MolecularAssayProtocol", description="""The specific type of protocol. Used to designate which concrete class (e.g., ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is instantiated for polymorphic protocol slots.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['Protocol']} })
    protocol_version: Optional[str] = Field(default=None, description="""Version of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    equipment_required: Optional[list[str]] = Field(default=[], description="""Equipment required for this protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    sub_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""Other protocols that are part of this protocol's workflow. Use this to compose protocols from reusable steps (e.g., sample preparation, wash steps, fixation, post-processing). Any Protocol or Protocol subclass is valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    quality_control_criteria: Optional[str] = Field(default=None, description="""Quality control acceptance criteria.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    replicate_requirements: Optional[int] = Field(default=None, description="""Number of replicates required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    protocol_author: Optional[str] = Field(default=None, description="""Author of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    institution: Optional[str] = Field(default=None, description="""Institution where protocol was developed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    publication_reference: Optional[str] = Field(default=None, description="""Reference to protocol publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    last_updated: Optional[date] = Field(default=None, description="""Date protocol was last updated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    validation_status: Optional[str] = Field(default=None, description="""Validation status of the protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class QuantityValue(ConfiguredBaseModel):
    """
    A quantity with a numeric value and unit of measurement. Used for all measurement values in assays.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    value: Optional[str] = Field(default=None, description="""The numeric value of the quantity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })
    unit: Optional[Unit] = Field(default=None, description="""The unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue', 'QuantityRange']} })


class Unit(ConfiguredBaseModel):
    """
    A unit of measurement from a standard ontology (UO, UCUM, QUDT).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base',
         'id_prefixes': ['UO', 'UCUM', 'QUDT'],
         'slot_usage': {'id': {'name': 'id',
                               'pattern': '^(UO:\\d{7}|UCUM:\\S+|QUDT:\\S+)$'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(UO:\d{7}|UCUM:\S+|QUDT:\S+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class NamedEntity(ConfiguredBaseModel):
    """
    A reference to an entity with an identifier and name. Used for cell_type, tissue_context, participant references, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })


class CellTypeReference(NamedEntity):
    """
    A reference to a cell type from the Cell Ontology (CL).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base',
         'id_prefixes': ['CL'],
         'slot_usage': {'id': {'name': 'id', 'pattern': '^CL:\\d{7}$'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^CL:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class SpeciesReference(NamedEntity):
    """
    A reference to a species from the NCBI Taxonomy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base',
         'id_prefixes': ['NCBITaxon'],
         'slot_usage': {'id': {'name': 'id', 'pattern': '^NCBITaxon:\\d+$'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^NCBITaxon:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class ChemicalEntityReference(NamedEntity):
    """
    A reference to a chemical entity from CHEBI or an exposure concept from ECTO.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base',
         'id_prefixes': ['CHEBI', 'ECTO'],
         'slot_usage': {'id': {'name': 'id', 'pattern': '^(CHEBI:\\d+|ECTO:\\d{7})$'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(CHEBI:\d+|ECTO:\d{7})$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class AnatomicalEntityReference(NamedEntity):
    """
    A reference to an anatomical entity from UBERON.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base',
         'id_prefixes': ['UBERON'],
         'slot_usage': {'id': {'name': 'id', 'pattern': '^UBERON:\\d{7}$'}}})

    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^UBERON:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class ExposureCondition(NamedEntity):
    """
    A structured description of an exposure or treatment applied to a biological system. Captures what agent was applied, at what concentration, for how long, and when the measurement was taken relative to exposure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    exposure_agent: Optional[ChemicalEntityReference] = Field(default=None, description="""The chemical, biological, or environmental agent used for exposure or treatment. Reference to a CHEBI or ECTO ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureCondition']} })
    exposure_concentration: Optional[QuantityValue] = Field(default=None, description="""Concentration of the exposure agent applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureCondition']} })
    exposure_duration: Optional[QuantityValue] = Field(default=None, description="""Duration of exposure or treatment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureCondition']} })
    timing_post_exposure: Optional[QuantityValue] = Field(default=None, description="""Time after exposure when the measurement was taken. Used to capture the temporal relationship between exposure and assay readout.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureCondition']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })


class CellularSystem(ModelSystem):
    """
    Cell-based model systems that use living cells to model biological processes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    cell_line: Optional[CellLine] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    primary_cell: Optional[CellTypeReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    cell_type: Optional[CellTypeReference] = Field(default=None, description="""The cell type being studied. Reference to a Cell Ontology (CL) term. Used on CellularSystem and CellLine to describe the cell identity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CellLine'], 'slot_uri': 'EFO:0000324'} })
    anatomical_origin: Optional[AnatomicalEntityReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    cell_culture_growth_mode: Optional[CellCultureGrowthModeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CellCultureConditions']} })
    substrate_type: Optional[SubstrateTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CellCultureConditions']} })
    confluence_level: Optional[QuantityValue] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    passage_number: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CellCultureConditions']} })
    seeding_density: Optional[QuantityValue] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    coating: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    matrix_composition: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    size_range: Optional[QuantityRange] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    organoid_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    cell_type_ratios: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CiliaryFunctionOutput']} })
    culture_conditions: Optional[CellCultureConditions] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    culture_media: Optional[CellCultureMedium] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CellCultureConditions']} })
    days_at_differentiation: Optional[int] = Field(default=None, description="""Days at air-liquid interface or differentiation stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    donor_info: Optional[str] = Field(default=None, description="""Information about cell donor (e.g., healthy non-smoker, CF patient, age, anatomical region).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of biological replicates per donor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CellCultureConditions']} })
    subject_type: Literal["CellularSystem"] = Field(default="CellularSystem", description="""The specific type of study subject. Used to designate which concrete class (e.g., CellularSystem, InVivoSubject) is instantiated for polymorphic study_subject slots.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['StudySubject']} })
    model_species: Optional[SpeciesReference] = Field(default=None, description="""The species of origin for the cells or organism being studied. Reference to NCBITaxon term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudySubject', 'CellLine']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class CellLine(NamedEntity):
    """
    A cell line - a genetically stable cultured cell population.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base',
         'id_prefixes': ['CLO'],
         'slot_usage': {'id': {'name': 'id', 'pattern': '^CLO:\\d{7}$'}}})

    cell_type: Optional[CellTypeReference] = Field(default=None, description="""The cell type being studied. Reference to a Cell Ontology (CL) term. Used on CellularSystem and CellLine to describe the cell identity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CellLine'], 'slot_uri': 'EFO:0000324'} })
    model_species: Optional[SpeciesReference] = Field(default=None, description="""The species of origin for the cells or organism being studied. Reference to NCBITaxon term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudySubject', 'CellLine']} })
    tissue_origin: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine']} })
    disease_state: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['InVivoSubject', 'CellLine']} })
    supplier: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine']} })
    catalog_number: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'CellCultureMedium', 'MediumSupplement']} })
    authentication_method: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine']} })
    mycoplasma_status: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^CLO:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class CellCultureConditions(NamedEntity):
    """
    Detailed cell culture parameters including medium, environment, and timing.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['CLO:0037334'],
         'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    culture_media: Optional[CellCultureMedium] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CellCultureConditions']} })
    days_at_air_liquid_interface: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions']} })
    passage_number: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CellCultureConditions']} })
    substrate_type: Optional[SubstrateTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CellCultureConditions']} })
    cell_culture_growth_mode: Optional[CellCultureGrowthModeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CellCultureConditions']} })
    donor_count: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureConditions']} })
    replicates_per_donor: Optional[int] = Field(default=None, description="""Number of biological replicates per donor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CellCultureConditions']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })


class CellCultureMedium(NamedEntity):
    """
    Detailed formulation of cell culture medium including base medium and supplements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    base_medium: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    serum_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    serum_concentration: Optional[QuantityValue] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    supplements: Optional[list[MediumSupplement]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    osmolality: Optional[QuantityValue] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    manufacturer: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium', 'MediumSupplement']} })
    catalog_number: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'CellCultureMedium', 'MediumSupplement']} })
    lot_number: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    preparation_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })


class MediumSupplement(NamedEntity):
    """
    Supplement or additive to cell culture medium.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    supplement_type: Optional[SupplementTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['MediumSupplement']} })
    concentration: Optional[QuantityValue] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['MediumSupplement']} })
    manufacturer: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellCultureMedium', 'MediumSupplement']} })
    catalog_number: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellLine', 'CellCultureMedium', 'MediumSupplement']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })


class QuantityRange(ConfiguredBaseModel):
    """
    A range of quantity values with minimum and maximum bounds.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_base'})

    min_value: Optional[QuantityValue] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityRange']} })
    max_value: Optional[QuantityValue] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityRange']} })
    unit: Optional[Unit] = Field(default=None, description="""The unit of measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue', 'QuantityRange']} })


class CiliaryFunctionAssay(Assay):
    """
    Assay for measuring ciliary function including beat frequency, active area, cilia morphology, and ciliated cell populations. Informs on Key Event: \"Decreased ciliary function\" in respiratory AOPs.
    CONTEXT: Can be performed in vitro (tissue slices, spheroids) or in vivo (often using optical coherence tomography).
    TIER 1 slots (critical): beat_frequency_hz, active_area_percentage, cilia_length, cilia_per_cell, percentage_ciliated_cells, cell_type_ratios,
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'supported_contexts': {'tag': 'supported_contexts',
                                                'value': 'in_vitro_or_in_vivo'}},
         'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas',
         'slot_usage': {'has_specified_output': {'name': 'has_specified_output',
                                                 'range': 'CiliaryFunctionOutput'},
                        'study_subject': {'description': 'Can be ModelSystem (in vitro '
                                                         '- ALI cultures, tissue '
                                                         'slices, spheroids) or '
                                                         'InVivoSubject (in vivo - OCT '
                                                         'measurements)',
                                          'name': 'study_subject',
                                          'range': 'StudySubject'}}})

    analysis_software: Optional[str] = Field(default=None, description="""Software used for analysis (e.g., SAVA, Cilia FA).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaryFunctionAssay']} })
    airway_region: Optional[str] = Field(default=None, description="""Region of airway from which cells originated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaryFunctionAssay']} })
    informs_on_key_event: Optional[KeyEvent] = Field(default=None, description="""The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    study_subject: Optional[Union[StudySubject,ModelSystem,InVivoSubject,PopulationSubject,CellularSystem]] = Field(default=None, description="""Can be ModelSystem (in vitro - ALI cultures, tissue slices, spheroids) or InVivoSubject (in vivo - OCT measurements)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_exposure_condition: Optional[list[ExposureCondition]] = Field(default=[], description="""The exposure condition(s) applied to the study subject. Captures the agent, concentration, duration, and timing of exposure/treatment. Multivalued to support co-exposures or dose-response series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    follows_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""The Protocol(s) that this assay follows. Any Protocol or Protocol subclass (ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is valid. Use this for general protocol references; assay subclasses also have typed protocol slots for domain-specific protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_specified_output: Optional[CiliaryFunctionOutput] = Field(default=None, description="""The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000299']} })
    assay_date: Optional[date] = Field(default=None, description="""Date when the assay was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class CiliaryFunctionOutput(AssayOutputMeasurement):
    """
    Measurement results from a ciliary function assay. Contains the measured values for ciliary beat frequency, active area, cilia morphology, and ciliated cell populations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas'})

    beat_frequency_hz: Optional[QuantityValue] = Field(default=None, description="""Ciliary beat frequency measured in Hz. TIER 1 - critical for assessing ciliary function.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaryFunctionOutput']} })
    active_area_percentage: Optional[QuantityValue] = Field(default=None, description="""Percentage of epithelial surface with actively beating cilia. TIER 1 - critical for assessing ciliary coverage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaryFunctionOutput']} })
    cilia_length: Optional[QuantityValue] = Field(default=None, description="""Length of cilia measured in micrometers. TIER 1 - morphological assessment of cilia.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaryFunctionOutput']} })
    cilia_per_cell: Optional[QuantityValue] = Field(default=None, description="""Number of cilia per ciliated cell. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaryFunctionOutput']} })
    percentage_ciliated_cells: Optional[QuantityValue] = Field(default=None, description="""Percentage of cells that are ciliated. TIER 1 - critical for understanding ciliated cell populations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaryFunctionOutput']} })
    cell_type_ratios: Optional[list[str]] = Field(default=[], json_schema_extra = { "linkml_meta": {'domain_of': ['CellularSystem', 'CiliaryFunctionOutput']} })
    ciliary_motion_patterns: Optional[CiliaryMotionPatternEnum] = Field(default=None, description="""Patterns of ciliary motion (coordinated, dyskinetic, immotile). TIER 2 - supporting information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaryFunctionOutput']} })
    ciliary_beat_amplitude: Optional[QuantityValue] = Field(default=None, description="""Amplitude of ciliary beat. TIER 2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CiliaryFunctionOutput']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class ASLAssay(Assay):
    """
    Assay for measuring airway surface liquid properties including ASL height, periciliary layer depth, and ion composition. Informs on Key Event: \"Decreased ASL height\" or \"Altered airway hydration\" in CF-related AOPs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas',
         'slot_usage': {'has_specified_output': {'name': 'has_specified_output',
                                                 'range': 'ASLOutput'}}})

    informs_on_key_event: Optional[KeyEvent] = Field(default=None, description="""The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    study_subject: Optional[Union[StudySubject,ModelSystem,InVivoSubject,PopulationSubject,CellularSystem]] = Field(default=None, description="""The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_exposure_condition: Optional[list[ExposureCondition]] = Field(default=[], description="""The exposure condition(s) applied to the study subject. Captures the agent, concentration, duration, and timing of exposure/treatment. Multivalued to support co-exposures or dose-response series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    follows_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""The Protocol(s) that this assay follows. Any Protocol or Protocol subclass (ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is valid. Use this for general protocol references; assay subclasses also have typed protocol slots for domain-specific protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_specified_output: Optional[ASLOutput] = Field(default=None, description="""The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000299']} })
    assay_date: Optional[date] = Field(default=None, description="""Date when the assay was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class ASLOutput(AssayOutputMeasurement):
    """
    Measurement results from an airway surface liquid assay. Contains the measured values for ASL height, periciliary layer depth, and ion composition.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas'})

    asl_height_um: Optional[QuantityValue] = Field(default=None, description="""Airway surface liquid height in micrometers. TIER 1 - primary measurement for ASL assays.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ASLOutput']} })
    periciliary_layer_depth: Optional[QuantityValue] = Field(default=None, description="""Depth of the periciliary layer in micrometers. TIER 1 - helps give confidence to the outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ASLOutput']} })
    mucus_layer_thickness: Optional[QuantityValue] = Field(default=None, description="""Thickness of the mucus gel layer in micrometers. TIER 2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ASLOutput', 'MucociliaryClearanceOutput']} })
    ion_composition: Optional[str] = Field(default=None, description="""Ionic composition (Cl-, Na+, K+). TIER 3 - not critical for comparison but relevant for mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ASLOutput']} })
    asl_ph: Optional[QuantityValue] = Field(default=None, description="""pH of airway surface liquid. TIER 3.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ASLOutput']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class MucociliaryClearanceAssay(Assay):
    """
    Assay for measuring mucociliary clearance and transport. Informs on Key Event: \"Impaired mucociliary clearance\" in respiratory AOPs. TIER 1 slots (critical): transport_rate, directionality.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas',
         'slot_usage': {'has_specified_output': {'name': 'has_specified_output',
                                                 'range': 'MucociliaryClearanceOutput'}}})

    mucus_composition: Optional[str] = Field(default=None, description="""Composition of mucus. TIER 2 per feedback.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MucociliaryClearanceAssay']} })
    informs_on_key_event: Optional[KeyEvent] = Field(default=None, description="""The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    study_subject: Optional[Union[StudySubject,ModelSystem,InVivoSubject,PopulationSubject,CellularSystem]] = Field(default=None, description="""The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_exposure_condition: Optional[list[ExposureCondition]] = Field(default=[], description="""The exposure condition(s) applied to the study subject. Captures the agent, concentration, duration, and timing of exposure/treatment. Multivalued to support co-exposures or dose-response series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    follows_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""The Protocol(s) that this assay follows. Any Protocol or Protocol subclass (ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is valid. Use this for general protocol references; assay subclasses also have typed protocol slots for domain-specific protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_specified_output: Optional[MucociliaryClearanceOutput] = Field(default=None, description="""The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000299']} })
    assay_date: Optional[date] = Field(default=None, description="""Date when the assay was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class MucociliaryClearanceOutput(AssayOutputMeasurement):
    """
    Measurement results from a mucociliary clearance assay. Contains the measured values for transport rate, directionality, and clearance metrics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas'})

    transport_rate: Optional[QuantityValue] = Field(default=None, description="""Mucociliary transport rate. TIER 1 - primary outcome measure for MCC assays.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MucociliaryClearanceOutput']} })
    transport_directionality: Optional[DirectionalityEnum] = Field(default=None, description="""Directionality of mucociliary transport. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MucociliaryClearanceOutput']} })
    mucus_layer_thickness: Optional[QuantityValue] = Field(default=None, description="""Thickness of the mucus gel layer in micrometers. TIER 2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ASLOutput', 'MucociliaryClearanceOutput']} })
    percentage_active_transport: Optional[QuantityValue] = Field(default=None, description="""Percentage of area showing active transport. TIER 2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MucociliaryClearanceOutput']} })
    particle_clearance_time: Optional[QuantityValue] = Field(default=None, description="""Time for particle clearance. TIER 2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MucociliaryClearanceOutput']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class OxidativeStressAssay(Assay):
    """
    Assay for measuring oxidative stress markers. Informs on Key Event: \"Increased oxidative stress\" - often a Molecular Initiating Event (MIE) in respiratory toxicology AOPs. TIER 1 slots (critical): All surrogate markers for oxidative stress. Multiple detection methods expected - no single \"best\" for lung function.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas',
         'slot_usage': {'has_specified_output': {'name': 'has_specified_output',
                                                 'range': 'OxidativeStressOutput'}}})

    ros_probe_type: Optional[str] = Field(default=None, description="""Type of ROS probe used (DCFDA, DHE, MitoSOX, etc.). TIER 1 - varies by method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressAssay']} })
    informs_on_key_event: Optional[KeyEvent] = Field(default=None, description="""The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    study_subject: Optional[Union[StudySubject,ModelSystem,InVivoSubject,PopulationSubject,CellularSystem]] = Field(default=None, description="""The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_exposure_condition: Optional[list[ExposureCondition]] = Field(default=[], description="""The exposure condition(s) applied to the study subject. Captures the agent, concentration, duration, and timing of exposure/treatment. Multivalued to support co-exposures or dose-response series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    follows_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""The Protocol(s) that this assay follows. Any Protocol or Protocol subclass (ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is valid. Use this for general protocol references; assay subclasses also have typed protocol slots for domain-specific protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_specified_output: Optional[OxidativeStressOutput] = Field(default=None, description="""The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000299']} })
    assay_date: Optional[date] = Field(default=None, description="""Date when the assay was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class OxidativeStressOutput(AssayOutputMeasurement):
    """
    Measurement results from an oxidative stress assay. Contains all surrogate markers for oxidative stress including ROS levels, lipid peroxidation, protein oxidation, DNA damage, and antioxidant capacity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas'})

    reactive_oxygen_species: Optional[QuantityValue] = Field(default=None, description="""ROS level as fold change or fluorescence intensity. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    lipid_peroxidation: Optional[QuantityValue] = Field(default=None, description="""Lipid peroxidation level. TIER 1 - surrogate marker for OS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    malondialdehyde_level: Optional[QuantityValue] = Field(default=None, description="""MDA level - lipid peroxidation marker.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    four_hydroxynonenal_level: Optional[QuantityValue] = Field(default=None, description="""4-HNE level - lipid peroxidation marker.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    eight_isoprostane_level: Optional[QuantityValue] = Field(default=None, description="""8-isoprostane level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    protein_oxidation_markers: Optional[list[str]] = Field(default=[], description="""Protein oxidation markers (carbonyls, nitrotyrosine). TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    protein_carbonyl_content: Optional[QuantityValue] = Field(default=None, description="""Protein carbonyl content. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    nitrotyrosine_level: Optional[QuantityValue] = Field(default=None, description="""Nitrotyrosine level. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    dna_damage_markers: Optional[QuantityValue] = Field(default=None, description="""DNA damage markers (8-OHdG). TIER 1 - surrogate for OS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    eight_ohdg_level: Optional[QuantityValue] = Field(default=None, description="""8-OHdG level (DNA oxidation marker). TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    antioxidant_capacity: Optional[QuantityValue] = Field(default=None, description="""Total antioxidant capacity or GSH/GSSG ratio. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    glutathione_ratio: Optional[QuantityValue] = Field(default=None, description="""GSH/GSSG ratio indicating antioxidant status. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    antioxidant_enzyme_activities: Optional[str] = Field(default=None, description="""Antioxidant enzyme activities (SOD, catalase, GPx). TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    superoxide_dismutase_activity: Optional[QuantityValue] = Field(default=None, description="""SOD activity. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    catalase_activity: Optional[QuantityValue] = Field(default=None, description="""Catalase activity. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    glutathione_peroxidase_activity: Optional[QuantityValue] = Field(default=None, description="""GPx activity. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    total_antioxidant_capacity: Optional[QuantityValue] = Field(default=None, description="""Total antioxidant capacity. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    nrf2_activation: Optional[QuantityValue] = Field(default=None, description="""Nrf2 activation level. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OxidativeStressOutput']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class CFTRFunctionAssay(Assay):
    """
    Assay for measuring CFTR (Cystic Fibrosis Transmembrane Conductance Regulator) function. Informs on Key Event: \"Decreased CFTR function\" in cystic fibrosis-related AOPs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas',
         'slot_usage': {'has_specified_output': {'name': 'has_specified_output',
                                                 'range': 'CFTRFunctionOutput'}}})

    stimulation_agent: Optional[str] = Field(default=None, description="""Stimulation agent used (e.g., forskolin concentration).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionAssay']} })
    inhibitor_used: Optional[str] = Field(default=None, description="""Inhibitor used (e.g., CFTRinh-172).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionAssay']} })
    informs_on_key_event: Optional[KeyEvent] = Field(default=None, description="""The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    study_subject: Optional[Union[StudySubject,ModelSystem,InVivoSubject,PopulationSubject,CellularSystem]] = Field(default=None, description="""The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_exposure_condition: Optional[list[ExposureCondition]] = Field(default=[], description="""The exposure condition(s) applied to the study subject. Captures the agent, concentration, duration, and timing of exposure/treatment. Multivalued to support co-exposures or dose-response series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    follows_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""The Protocol(s) that this assay follows. Any Protocol or Protocol subclass (ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is valid. Use this for general protocol references; assay subclasses also have typed protocol slots for domain-specific protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_specified_output: Optional[CFTRFunctionOutput] = Field(default=None, description="""The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000299']} })
    assay_date: Optional[date] = Field(default=None, description="""Date when the assay was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class CFTRFunctionOutput(AssayOutputMeasurement):
    """
    Measurement results from a CFTR function assay. Contains the measured values for CFTR-mediated chloride secretion, forskolin response, and related electrophysiology measurements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas'})

    cftr_chloride_secretion: Optional[QuantityValue] = Field(default=None, description="""CFTR-mediated chloride secretion in uA/cm2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionOutput']} })
    cftr_forskolin_response: Optional[QuantityValue] = Field(default=None, description="""Forskolin-stimulated CFTR response.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionOutput']} })
    inhibitor_sensitive_current: Optional[QuantityValue] = Field(default=None, description="""Inhibitor-sensitive current measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionOutput']} })
    cftr_specific_current: Optional[QuantityValue] = Field(default=None, description="""CFTR-specific chloride secretory current.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionOutput']} })
    sweat_chloride_concentration: Optional[QuantityValue] = Field(default=None, description="""Sweat chloride concentration in mEq/L (CF diagnostic).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionOutput']} })
    nasal_potential_difference: Optional[QuantityValue] = Field(default=None, description="""Nasal potential difference in mV.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CFTRFunctionOutput']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class EGFRSignalingAssay(Assay):
    """
    Assay for measuring EGFR phosphorylation and downstream signaling. Informs on Key Event: \"EGFR activation\" in mucus hypersecretion AOPs.
    IMPORTANT: EGFR phosphorylation is the MOST SPECIFIC evidence for activation. Downstream kinase data alone is insufficient - needs phosphorylation measure OR inhibitor reversal for strong evidence. Cell type matters due to receptor location in ALI cultures.
    TIER 1 slots (critical): egfr_phosphorylation with site specification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas',
         'slot_usage': {'has_specified_output': {'name': 'has_specified_output',
                                                 'range': 'EGFRSignalingOutput'}}})

    normalization_reference: Optional[str] = Field(default=None, description="""Normalization reference (beta-actin, GAPDH, total EGFR).""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingAssay', 'GeneExpressionAssay']} })
    phosphorylation_site: Optional[str] = Field(default=None, description="""Specific phosphorylation site being measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingAssay']} })
    informs_on_key_event: Optional[KeyEvent] = Field(default=None, description="""The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    study_subject: Optional[Union[StudySubject,ModelSystem,InVivoSubject,PopulationSubject,CellularSystem]] = Field(default=None, description="""The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_exposure_condition: Optional[list[ExposureCondition]] = Field(default=[], description="""The exposure condition(s) applied to the study subject. Captures the agent, concentration, duration, and timing of exposure/treatment. Multivalued to support co-exposures or dose-response series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    follows_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""The Protocol(s) that this assay follows. Any Protocol or Protocol subclass (ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is valid. Use this for general protocol references; assay subclasses also have typed protocol slots for domain-specific protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_specified_output: Optional[EGFRSignalingOutput] = Field(default=None, description="""The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000299']} })
    assay_date: Optional[date] = Field(default=None, description="""Date when the assay was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class EGFRSignalingOutput(AssayOutputMeasurement):
    """
    Measurement results from an EGFR signaling assay. Contains the measured values for EGFR phosphorylation, total protein, and downstream kinase activation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas'})

    egfr_phosphorylation_y1068: Optional[QuantityValue] = Field(default=None, description="""EGFR phosphorylation at Y1068 residue (fold change). TIER 1 - MOST SPECIFIC evidence for EGFR activation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingOutput']} })
    egfr_phosphorylation_y1173: Optional[QuantityValue] = Field(default=None, description="""EGFR phosphorylation at Y1173 residue (fold change). TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingOutput']} })
    total_egfr_protein: Optional[QuantityValue] = Field(default=None, description="""Total EGFR protein level (loading control). TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingOutput']} })
    downstream_kinase_activation: Optional[str] = Field(default=None, description="""Activation levels of downstream kinases. TIER 2 - not specific to EGFR alone without phosphorylation data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingOutput']} })
    erk_phosphorylation: Optional[QuantityValue] = Field(default=None, description="""ERK phosphorylation level. TIER 2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingOutput']} })
    akt_phosphorylation: Optional[QuantityValue] = Field(default=None, description="""AKT phosphorylation level. TIER 2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingOutput']} })
    pathway_biomarkers: Optional[list[str]] = Field(default=[], description="""Pathway-specific biomarker signatures. TIER 2 - relationship to outcome needs further investigation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingOutput']} })
    egfr_ligand_expression: Optional[QuantityValue] = Field(default=None, description="""Expression of EGFR ligands (EGF, TGF-alpha, amphiregulin).""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingOutput']} })
    egfr_membrane_localization: Optional[QuantityValue] = Field(default=None, description="""EGFR membrane localization percentage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingOutput']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class GobletCellAssay(Assay):
    """
    Assay for measuring goblet cell populations and mucin production. Informs on Key Event: \"Goblet cell hyperplasia\" or \"Mucin hypersecretion\".
    IMPORTANT per domain feedback: Need BOTH cell counts AND mucin secretion measurements - cells may stay same but secretion changes. AB-PAS staining common for visualizing goblet cells. Some secreted mucins not tethered to goblet cells.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas',
         'slot_usage': {'has_specified_output': {'name': 'has_specified_output',
                                                 'range': 'GobletCellOutput'}}})

    informs_on_key_event: Optional[KeyEvent] = Field(default=None, description="""The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    study_subject: Optional[Union[StudySubject,ModelSystem,InVivoSubject,PopulationSubject,CellularSystem]] = Field(default=None, description="""The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_exposure_condition: Optional[list[ExposureCondition]] = Field(default=[], description="""The exposure condition(s) applied to the study subject. Captures the agent, concentration, duration, and timing of exposure/treatment. Multivalued to support co-exposures or dose-response series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    follows_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""The Protocol(s) that this assay follows. Any Protocol or Protocol subclass (ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is valid. Use this for general protocol references; assay subclasses also have typed protocol slots for domain-specific protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_specified_output: Optional[GobletCellOutput] = Field(default=None, description="""The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000299']} })
    assay_date: Optional[date] = Field(default=None, description="""Date when the assay was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class GobletCellOutput(AssayOutputMeasurement):
    """
    Measurement results from a goblet cell assay. Contains the measured values for goblet cell counts, mucin expression, and mucus properties.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas'})

    goblet_cell_count: Optional[QuantityValue] = Field(default=None, description="""Number of goblet cells (raw count). TIER 1 - want both raw and relative information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellOutput']} })
    goblet_cell_percentage: Optional[QuantityValue] = Field(default=None, description="""Percentage of goblet cells. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellOutput']} })
    muc5ac_mrna_expression: Optional[QuantityValue] = Field(default=None, description="""MUC5AC mRNA expression level (fold change). TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellOutput']} })
    muc5ac_protein_expression: Optional[QuantityValue] = Field(default=None, description="""MUC5AC protein expression level. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellOutput']} })
    muc5b_mrna_expression: Optional[QuantityValue] = Field(default=None, description="""MUC5B mRNA expression level (fold change). TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellOutput']} })
    muc5b_protein_expression: Optional[QuantityValue] = Field(default=None, description="""MUC5B protein expression level. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellOutput']} })
    muc5ac_muc5b_ratio: Optional[QuantityValue] = Field(default=None, description="""MUC5AC to MUC5B ratio. TIER 1 - important for disease state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellOutput']} })
    mucin_protein_concentration: Optional[QuantityValue] = Field(default=None, description="""Total mucin protein concentration. TIER 1 - want both direct and comparative measures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellOutput']} })
    mucin_secretion_rate: Optional[QuantityValue] = Field(default=None, description="""Mucin secretion rate. TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellOutput']} })
    percent_solids: Optional[QuantityValue] = Field(default=None, description="""Percent solids in apical secretion (overall secretion). TIER 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellOutput']} })
    goblet_to_ciliated_ratio: Optional[QuantityValue] = Field(default=None, description="""Ratio of goblet cells to ciliated cells. TIER 2 - related to transdifferentiation but not critical for outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellOutput']} })
    mucus_viscosity: Optional[QuantityValue] = Field(default=None, description="""Mucus viscosity in centipoise. TIER 2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GobletCellOutput']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class BALFSputumAssay(Assay):
    """
    Assay for measuring bronchoalveolar lavage fluid (BALF) or sputum composition. Informs on Key Event: \"Airway inflammation\" and provides evidence for inflammatory cell populations and cytokine levels.
    This assay is IN VIVO ONLY - requires samples from human or animal subjects.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'supported_contexts': {'tag': 'supported_contexts',
                                                'value': 'in_vivo_only'}},
         'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas',
         'slot_usage': {'has_specified_output': {'name': 'has_specified_output',
                                                 'range': 'BALFSputumOutput'},
                        'study_subject': {'name': 'study_subject',
                                          'range': 'InVivoSubject'}}})

    target_cell_type: Optional[CellTypeReference] = Field(default=None, description="""The specific cell type that is the primary focus of this assay's analysis, when the assay examines multiple cell populations in a sample (e.g., neutrophils in a BALF differential).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumAssay']} })
    informs_on_key_event: Optional[KeyEvent] = Field(default=None, description="""The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    study_subject: Optional[InVivoSubject] = Field(default=None, description="""The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_exposure_condition: Optional[list[ExposureCondition]] = Field(default=[], description="""The exposure condition(s) applied to the study subject. Captures the agent, concentration, duration, and timing of exposure/treatment. Multivalued to support co-exposures or dose-response series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    follows_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""The Protocol(s) that this assay follows. Any Protocol or Protocol subclass (ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is valid. Use this for general protocol references; assay subclasses also have typed protocol slots for domain-specific protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_specified_output: Optional[BALFSputumOutput] = Field(default=None, description="""The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000299']} })
    assay_date: Optional[date] = Field(default=None, description="""Date when the assay was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class BALFSputumOutput(AssayOutputMeasurement):
    """
    Measurement results from a BALF/sputum assay. Contains inflammatory cell differentials, cytokine concentrations, and microbiome metrics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas'})

    neutrophil_percentage: Optional[QuantityValue] = Field(default=None, description="""Neutrophil percentage in BALF/sputum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    eosinophil_percentage: Optional[QuantityValue] = Field(default=None, description="""Eosinophil percentage in BALF/sputum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    macrophage_percentage: Optional[QuantityValue] = Field(default=None, description="""Macrophage percentage in BALF/sputum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    lymphocyte_percentage: Optional[QuantityValue] = Field(default=None, description="""Lymphocyte percentage in BALF/sputum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    total_cell_count: Optional[QuantityValue] = Field(default=None, description="""Total cell count in BALF/sputum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    il6_concentration: Optional[QuantityValue] = Field(default=None, description="""IL-6 concentration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    il8_concentration: Optional[QuantityValue] = Field(default=None, description="""IL-8 concentration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    tnf_alpha_concentration: Optional[QuantityValue] = Field(default=None, description="""TNF-alpha concentration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    il1_beta_concentration: Optional[QuantityValue] = Field(default=None, description="""IL-1 beta concentration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    total_protein_concentration: Optional[QuantityValue] = Field(default=None, description="""Total protein concentration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    alpha_diversity: Optional[QuantityValue] = Field(default=None, description="""Alpha diversity (microbiome).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    beta_diversity: Optional[QuantityValue] = Field(default=None, description="""Beta diversity (microbiome).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    bacterial_load: Optional[QuantityValue] = Field(default=None, description="""Bacterial load (16S copies or CFU).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    cell_free_dna: Optional[QuantityValue] = Field(default=None, description="""Cell-free DNA concentration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BALFSputumOutput']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class LungFunctionAssay(Assay):
    """
    Clinical assay for measuring lung function. Informs on Adverse Outcome: \"Decreased lung function\" - the composite clinical outcome.
    IMPORTANT per domain feedback: - Subject characteristics (sex, species, age, height) are critical -
      often reported as % of predicted baseline
    - Reference dataset (GLI-2012 for humans) is essential for interpretation - Hemoglobin levels pair with DLCO measurements - Recent respiratory illness affects spirometry results
    TIER 1 slots (critical): fev1, fvc, subject_characteristics, reference_dataset. This assay is IN VIVO ONLY.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'supported_contexts': {'tag': 'supported_contexts',
                                                'value': 'in_vivo_only'}},
         'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas',
         'slot_usage': {'has_specified_output': {'name': 'has_specified_output',
                                                 'range': 'LungFunctionOutput'},
                        'study_subject': {'name': 'study_subject',
                                          'range': 'InVivoSubject'}}})

    reference_dataset: Optional[str] = Field(default=None, description="""Reference dataset for interpretation (GLI-2012 for humans). TIER 1 - essential for interpretation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionAssay']} })
    hemoglobin_level: Optional[QuantityValue] = Field(default=None, description="""Hemoglobin level. TIER 2 - pairs with DLCO.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionAssay']} })
    recent_respiratory_illness: Optional[str] = Field(default=None, description="""Recent respiratory illness (affects spirometry). TIER 2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionAssay']} })
    informs_on_key_event: Optional[KeyEvent] = Field(default=None, description="""The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    study_subject: Optional[InVivoSubject] = Field(default=None, description="""The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_exposure_condition: Optional[list[ExposureCondition]] = Field(default=[], description="""The exposure condition(s) applied to the study subject. Captures the agent, concentration, duration, and timing of exposure/treatment. Multivalued to support co-exposures or dose-response series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    follows_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""The Protocol(s) that this assay follows. Any Protocol or Protocol subclass (ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is valid. Use this for general protocol references; assay subclasses also have typed protocol slots for domain-specific protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_specified_output: Optional[LungFunctionOutput] = Field(default=None, description="""The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000299']} })
    assay_date: Optional[date] = Field(default=None, description="""Date when the assay was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class LungFunctionOutput(AssayOutputMeasurement):
    """
    Measurement results from a lung function assay. Contains spirometry measurements, diffusing capacity, and related clinical metrics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas'})

    fev1: Optional[QuantityValue] = Field(default=None, description="""Forced expiratory volume in 1 second. TIER 1 - primary spirometry measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    fvc: Optional[QuantityValue] = Field(default=None, description="""Forced vital capacity. TIER 1 - primary spirometry measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    fev1_fvc_ratio: Optional[QuantityValue] = Field(default=None, description="""Ratio of FEV1 to FVC (Tiffeneau-Pinelli index). TIER 2 - can be calculated from FEV1 and FVC.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    feno: Optional[QuantityValue] = Field(default=None, description="""Fractional exhaled nitric oxide in ppb. TIER 2 - marker for airway inflammation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    decline_rate: Optional[QuantityValue] = Field(default=None, description="""Longitudinal decline rate in mL/year. TIER 2 - useful for pre/post comparisons.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    bronchodilator_response: Optional[QuantityValue] = Field(default=None, description="""Response to bronchodilator (% change in FEV1). TIER 2 - informs reversibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    dlco: Optional[QuantityValue] = Field(default=None, description="""Diffusing capacity for carbon monoxide. TIER 2 - measure of fibrosis, needs hemoglobin level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    peak_expiratory_flow: Optional[QuantityValue] = Field(default=None, description="""Peak expiratory flow. TIER 2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    fef25_75: Optional[QuantityValue] = Field(default=None, description="""Forced expiratory flow 25-75%. TIER 3 - more variable than FEV1, FVC.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    total_lung_capacity: Optional[QuantityValue] = Field(default=None, description="""Total lung capacity. TIER 3 - requires more equipment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    functional_residual_capacity: Optional[QuantityValue] = Field(default=None, description="""Functional residual capacity. TIER 3 - requires more equipment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    residual_volume: Optional[QuantityValue] = Field(default=None, description="""Residual volume. TIER 3 - requires more equipment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    lung_compliance: Optional[QuantityValue] = Field(default=None, description="""Lung compliance. TIER 3 - most often reported for animals, difficult to relate to human exposure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    lung_elastance: Optional[QuantityValue] = Field(default=None, description="""Lung elastance. TIER 3 - most often reported for animals.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    lung_resistance: Optional[QuantityValue] = Field(default=None, description="""Lung resistance. TIER 3 - most often reported for animals.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LungFunctionOutput']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class FoxJExpressionAssay(Assay):
    """
    Assay for measuring FoxJ1 expression related to ciliogenesis. Informs on Key Event: \"Altered ciliogenesis\" in respiratory AOPs. FoxJ1 is a master transcription factor for motile cilia.
    This assay is primarily IN VITRO focused.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'supported_contexts': {'tag': 'supported_contexts',
                                                'value': 'in_vitro_only'}},
         'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas',
         'slot_usage': {'has_specified_output': {'name': 'has_specified_output',
                                                 'range': 'FoxJExpressionOutput'}}})

    informs_on_key_event: Optional[KeyEvent] = Field(default=None, description="""The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    study_subject: Optional[Union[StudySubject,ModelSystem,InVivoSubject,PopulationSubject,CellularSystem]] = Field(default=None, description="""The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_exposure_condition: Optional[list[ExposureCondition]] = Field(default=[], description="""The exposure condition(s) applied to the study subject. Captures the agent, concentration, duration, and timing of exposure/treatment. Multivalued to support co-exposures or dose-response series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    follows_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""The Protocol(s) that this assay follows. Any Protocol or Protocol subclass (ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is valid. Use this for general protocol references; assay subclasses also have typed protocol slots for domain-specific protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_specified_output: Optional[FoxJExpressionOutput] = Field(default=None, description="""The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000299']} })
    assay_date: Optional[date] = Field(default=None, description="""Date when the assay was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class FoxJExpressionOutput(AssayOutputMeasurement):
    """
    Measurement results from a FoxJ1 expression assay. Contains the measured values for FoxJ1 mRNA, protein, and cellular localization.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas'})

    foxj1_mrna_expression: Optional[QuantityValue] = Field(default=None, description="""FoxJ1 mRNA expression level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FoxJExpressionOutput']} })
    foxj1_protein_expression: Optional[QuantityValue] = Field(default=None, description="""FoxJ1 protein expression level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FoxJExpressionOutput']} })
    foxj1_positive_cell_percentage: Optional[QuantityValue] = Field(default=None, description="""Percentage of FoxJ1-positive cells.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FoxJExpressionOutput']} })
    foxj1_nuclear_localization: Optional[QuantityValue] = Field(default=None, description="""FoxJ1 nuclear localization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FoxJExpressionOutput']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class GeneExpressionAssay(Assay):
    """
    General assay for gene expression measurements. Renamed from TranscriptionFactorExpressionMeasurement per domain feedback - gene expression is more commonly the primary output.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'supported_contexts': {'tag': 'supported_contexts',
                                                'value': 'in_vitro_only'}},
         'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas',
         'slot_usage': {'has_specified_output': {'name': 'has_specified_output',
                                                 'range': 'GeneExpressionOutput'}}})

    target_gene: Optional[str] = Field(default=None, description="""Target gene being measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionAssay']} })
    gene_expression_method: Optional[str] = Field(default=None, description="""Method used for gene expression (qRT-PCR, RNA-seq, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionAssay']} })
    normalization_reference: Optional[str] = Field(default=None, description="""Normalization reference (beta-actin, GAPDH, total EGFR).""", json_schema_extra = { "linkml_meta": {'domain_of': ['EGFRSignalingAssay', 'GeneExpressionAssay']} })
    informs_on_key_event: Optional[KeyEvent] = Field(default=None, description="""The Key Event that this assay provides evidence for. This establishes the mechanistic connection between the assay measurements and the Adverse Outcome Pathway framework. Multiple assays can inform on the same key event, providing converging evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    study_subject: Optional[Union[StudySubject,ModelSystem,InVivoSubject,PopulationSubject,CellularSystem]] = Field(default=None, description="""The subject of the study — what the assay is performed on. Can be a ModelSystem (e.g., CellularSystem), an InVivoSubject, or a PopulationSubject. The type of subject determines which context slots are available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_exposure_condition: Optional[list[ExposureCondition]] = Field(default=[], description="""The exposure condition(s) applied to the study subject. Captures the agent, concentration, duration, and timing of exposure/treatment. Multivalued to support co-exposures or dose-response series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    follows_protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""The Protocol(s) that this assay follows. Any Protocol or Protocol subclass (ImagingProtocol, StainingProtocol, SpirometryProtocol, MolecularAssayProtocol) is valid. Use this for general protocol references; assay subclasses also have typed protocol slots for domain-specific protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    has_specified_output: Optional[GeneExpressionOutput] = Field(default=None, description="""The measurement results produced by this assay — the specified output of a planned process (OBI). Contains the domain-specific measurement values (e.g., beat frequency, cilia length for CiliaryFunctionAssay).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay'], 'exact_mappings': ['OBI:0000299']} })
    assay_date: Optional[date] = Field(default=None, description="""Date when the assay was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class GeneExpressionOutput(AssayOutputMeasurement):
    """
    Measurement results from a gene expression assay. Contains the measured values for mRNA level, protein level, and positive cell percentage.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/assay_microschemas'})

    mrna_level: Optional[QuantityValue] = Field(default=None, description="""mRNA expression level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionOutput']} })
    protein_level: Optional[QuantityValue] = Field(default=None, description="""Protein expression level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionOutput']} })
    percentage_positive_cells: Optional[QuantityValue] = Field(default=None, description="""Percentage of positive cells (IHC, flow cytometry).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionOutput']} })
    id: str = Field(default=..., description="""A unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity']} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'Unit', 'NamedEntity'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class Container(ConfiguredBaseModel):
    """
    Root container for outcomes research data. Organized around ASSAYS that inform on Key Events in Adverse Outcome Pathways (AOPs).
    The schema is assay-centric: each assay class contains named slots for its specific measurements, with an explicit connection to the Key Event it informs via the informs_on_key_event slot.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/EHS-Data-Standards/soma', 'tree_root': True})

    key_events: Optional[list[KeyEvent]] = Field(default=[], description="""The key events in this AOP (intermediate events between MIE and AO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway', 'Container']} })
    adverse_outcome_pathways: Optional[list[AdverseOutcomePathway]] = Field(default=[], description="""Collection of Adverse Outcome Pathways. AOPs describe sequences of causally linked events from molecular initiating events to adverse outcomes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    ciliary_function_assays: Optional[list[CiliaryFunctionAssay]] = Field(default=[], description="""Collection of ciliary function assays. Informs on Key Event: \"Decreased ciliary function\". Contains named slots for beat frequency, active area, cilia length, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    asl_assays: Optional[list[ASLAssay]] = Field(default=[], description="""Collection of airway surface liquid assays. Informs on Key Event: \"Decreased ASL height\" or \"Altered airway hydration\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    mcc_assays: Optional[list[MucociliaryClearanceAssay]] = Field(default=[], description="""Collection of mucociliary clearance assays. Informs on Key Event: \"Impaired mucociliary clearance\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    oxidative_stress_assays: Optional[list[OxidativeStressAssay]] = Field(default=[], description="""Collection of oxidative stress assays. Informs on Key Event: \"Increased oxidative stress\" - often a Molecular Initiating Event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    cftr_assays: Optional[list[CFTRFunctionAssay]] = Field(default=[], description="""Collection of CFTR function assays. Informs on Key Event: \"Decreased CFTR function\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    egfr_signaling_assays: Optional[list[EGFRSignalingAssay]] = Field(default=[], description="""Collection of EGFR signaling assays. Informs on Key Event: \"EGFR activation\". Note: EGFR phosphorylation is the most specific evidence for activation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    goblet_cell_assays: Optional[list[GobletCellAssay]] = Field(default=[], description="""Collection of goblet cell and mucin assays. Informs on Key Event: \"Goblet cell hyperplasia\" or \"Mucin hypersecretion\". Combined from previous GobletCellMeasurement and MucinProductionMeasurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    balf_sputum_assays: Optional[list[BALFSputumAssay]] = Field(default=[], description="""Collection of BALF and sputum assays. In vivo only. Informs on Key Event: \"Airway inflammation\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    lung_function_assays: Optional[list[LungFunctionAssay]] = Field(default=[], description="""Collection of lung function assays. In vivo only. Informs on Adverse Outcome: \"Decreased lung function\" - the composite clinical outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    foxj_assays: Optional[list[FoxJExpressionAssay]] = Field(default=[], description="""Collection of FoxJ1/ciliogenesis assays. Informs on Key Event: \"Altered ciliogenesis\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    gene_expression_assays: Optional[list[GeneExpressionAssay]] = Field(default=[], description="""Collection of gene expression assays. Generic assay for gene/protein expression measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    protocols: Optional[list[Union[Protocol,ImagingProtocol,StainingProtocol,SpirometryProtocol,MolecularAssayProtocol]]] = Field(default=[], description="""Collection of protocols. Contains Tier 2/3 procedural details important for reproducibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
KeyEvent.model_rebuild()
KeyEventRelationship.model_rebuild()
AdverseOutcome.model_rebuild()
AdverseOutcomePathway.model_rebuild()
MolecularInitiatingEvent.model_rebuild()
Assay.model_rebuild()
AssayOutputMeasurement.model_rebuild()
StudySubject.model_rebuild()
ModelSystem.model_rebuild()
InVivoSubject.model_rebuild()
PopulationSubject.model_rebuild()
Protocol.model_rebuild()
ImagingProtocol.model_rebuild()
StainingProtocol.model_rebuild()
SpirometryProtocol.model_rebuild()
MolecularAssayProtocol.model_rebuild()
QuantityValue.model_rebuild()
Unit.model_rebuild()
NamedEntity.model_rebuild()
CellTypeReference.model_rebuild()
SpeciesReference.model_rebuild()
ChemicalEntityReference.model_rebuild()
AnatomicalEntityReference.model_rebuild()
ExposureCondition.model_rebuild()
CellularSystem.model_rebuild()
CellLine.model_rebuild()
CellCultureConditions.model_rebuild()
CellCultureMedium.model_rebuild()
MediumSupplement.model_rebuild()
QuantityRange.model_rebuild()
CiliaryFunctionAssay.model_rebuild()
CiliaryFunctionOutput.model_rebuild()
ASLAssay.model_rebuild()
ASLOutput.model_rebuild()
MucociliaryClearanceAssay.model_rebuild()
MucociliaryClearanceOutput.model_rebuild()
OxidativeStressAssay.model_rebuild()
OxidativeStressOutput.model_rebuild()
CFTRFunctionAssay.model_rebuild()
CFTRFunctionOutput.model_rebuild()
EGFRSignalingAssay.model_rebuild()
EGFRSignalingOutput.model_rebuild()
GobletCellAssay.model_rebuild()
GobletCellOutput.model_rebuild()
BALFSputumAssay.model_rebuild()
BALFSputumOutput.model_rebuild()
LungFunctionAssay.model_rebuild()
LungFunctionOutput.model_rebuild()
FoxJExpressionAssay.model_rebuild()
FoxJExpressionOutput.model_rebuild()
GeneExpressionAssay.model_rebuild()
GeneExpressionOutput.model_rebuild()
Container.model_rebuild()
