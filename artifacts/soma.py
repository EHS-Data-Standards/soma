# Auto generated from soma.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-12T19:08:23
# Schema: soma
#
# id: https://w3id.org/EHS-Data-Standards/soma
# description: A LinkML data model for representing biological assays, measurements, and experimental protocols in the context of outcomes research. The schema is centered around ASSAYS that inform on Key Events in Adverse Outcome Pathways (AOPs), with named slots for specific measurements.
#   This is the main entry point that imports the AOP framework, assay base schema, and domain-specific assay microschemas.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
CLO = CurieNamespace('CLO', 'http://purl.obolibrary.org/obo/CLO_')
ECTO = CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_')
EFO = CurieNamespace('EFO', 'http://www.ebi.ac.uk/efo/EFO_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
QUDT = CurieNamespace('QUDT', 'http://qudt.org/vocab/unit/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UCUM = CurieNamespace('UCUM', 'http://unitsofmeasure.org/')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
AOP_FRAMEWORK = CurieNamespace('aop_framework', 'https://w3id.org/EHS-Data-Standards/aop_framework/')
ASSAY_BASE = CurieNamespace('assay_base', 'https://w3id.org/EHS-Data-Standards/assay_base/')
ASSAY_MICROSCHEMAS = CurieNamespace('assay_microschemas', 'https://w3id.org/EHS-Data-Standards/assay_microschemas/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWG = CurieNamespace('owg', 'https://w3id.org/EHS-Data-Standards/soma/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SOMA = CurieNamespace('soma', 'https://w3id.org/EHS-Data-Standards/soma/')
DEFAULT_ = SOMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class KeyEventId(NamedThingId):
    pass


class KeyEventRelationshipId(NamedThingId):
    pass


class AdverseOutcomeId(NamedThingId):
    pass


class AdverseOutcomePathwayId(NamedThingId):
    pass


class MolecularInitiatingEventId(KeyEventId):
    pass


class AssayId(NamedThingId):
    pass


class AssayOutputMeasurementId(NamedThingId):
    pass


class StudySubjectId(NamedThingId):
    pass


class ModelSystemId(StudySubjectId):
    pass


class InVivoSubjectId(StudySubjectId):
    pass


class PopulationSubjectId(StudySubjectId):
    pass


class ProtocolId(NamedThingId):
    pass


class ImagingProtocolId(ProtocolId):
    pass


class StainingProtocolId(ProtocolId):
    pass


class SpirometryProtocolId(ProtocolId):
    pass


class MolecularAssayProtocolId(ProtocolId):
    pass


class UnitId(URIorCURIE):
    pass


class NamedEntityId(URIorCURIE):
    pass


class CellTypeReferenceId(NamedEntityId):
    pass


class SpeciesReferenceId(NamedEntityId):
    pass


class ChemicalEntityReferenceId(NamedEntityId):
    pass


class AnatomicalEntityReferenceId(NamedEntityId):
    pass


class ExposureConditionId(NamedEntityId):
    pass


class CellularSystemId(ModelSystemId):
    pass


class CellLineId(NamedEntityId):
    pass


class CellCultureConditionsId(NamedEntityId):
    pass


class CellCultureMediumId(NamedEntityId):
    pass


class MediumSupplementId(NamedEntityId):
    pass


class CiliaryFunctionAssayId(AssayId):
    pass


class CiliaryFunctionOutputId(AssayOutputMeasurementId):
    pass


class ASLAssayId(AssayId):
    pass


class ASLOutputId(AssayOutputMeasurementId):
    pass


class MucociliaryClearanceAssayId(AssayId):
    pass


class MucociliaryClearanceOutputId(AssayOutputMeasurementId):
    pass


class OxidativeStressAssayId(AssayId):
    pass


class OxidativeStressOutputId(AssayOutputMeasurementId):
    pass


class CFTRFunctionAssayId(AssayId):
    pass


class CFTRFunctionOutputId(AssayOutputMeasurementId):
    pass


class EGFRSignalingAssayId(AssayId):
    pass


class EGFRSignalingOutputId(AssayOutputMeasurementId):
    pass


class GobletCellAssayId(AssayId):
    pass


class GobletCellOutputId(AssayOutputMeasurementId):
    pass


class BALFSputumAssayId(AssayId):
    pass


class BALFSputumOutputId(AssayOutputMeasurementId):
    pass


class LungFunctionAssayId(AssayId):
    pass


class LungFunctionOutputId(AssayOutputMeasurementId):
    pass


class FoxJExpressionAssayId(AssayId):
    pass


class FoxJExpressionOutputId(AssayOutputMeasurementId):
    pass


class GeneExpressionAssayId(AssayId):
    pass


class GeneExpressionOutputId(AssayOutputMeasurementId):
    pass


@dataclass(repr=False)
class Container(YAMLRoot):
    """
    Root container for outcomes research data. Organized around ASSAYS that inform on Key Events in Adverse Outcome
    Pathways (AOPs).
    The schema is assay-centric: each assay class contains named slots for its specific measurements, with an explicit
    connection to the Key Event it informs via the informs_on_key_event slot.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOMA["Container"]
    class_class_curie: ClassVar[str] = "soma:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = SOMA.Container

    key_events: Optional[Union[dict[Union[str, KeyEventId], Union[dict, "KeyEvent"]], list[Union[dict, "KeyEvent"]]]] = empty_dict()
    adverse_outcome_pathways: Optional[Union[dict[Union[str, AdverseOutcomePathwayId], Union[dict, "AdverseOutcomePathway"]], list[Union[dict, "AdverseOutcomePathway"]]]] = empty_dict()
    ciliary_function_assays: Optional[Union[dict[Union[str, CiliaryFunctionAssayId], Union[dict, "CiliaryFunctionAssay"]], list[Union[dict, "CiliaryFunctionAssay"]]]] = empty_dict()
    asl_assays: Optional[Union[dict[Union[str, ASLAssayId], Union[dict, "ASLAssay"]], list[Union[dict, "ASLAssay"]]]] = empty_dict()
    mcc_assays: Optional[Union[dict[Union[str, MucociliaryClearanceAssayId], Union[dict, "MucociliaryClearanceAssay"]], list[Union[dict, "MucociliaryClearanceAssay"]]]] = empty_dict()
    oxidative_stress_assays: Optional[Union[dict[Union[str, OxidativeStressAssayId], Union[dict, "OxidativeStressAssay"]], list[Union[dict, "OxidativeStressAssay"]]]] = empty_dict()
    cftr_assays: Optional[Union[dict[Union[str, CFTRFunctionAssayId], Union[dict, "CFTRFunctionAssay"]], list[Union[dict, "CFTRFunctionAssay"]]]] = empty_dict()
    egfr_signaling_assays: Optional[Union[dict[Union[str, EGFRSignalingAssayId], Union[dict, "EGFRSignalingAssay"]], list[Union[dict, "EGFRSignalingAssay"]]]] = empty_dict()
    goblet_cell_assays: Optional[Union[dict[Union[str, GobletCellAssayId], Union[dict, "GobletCellAssay"]], list[Union[dict, "GobletCellAssay"]]]] = empty_dict()
    balf_sputum_assays: Optional[Union[dict[Union[str, BALFSputumAssayId], Union[dict, "BALFSputumAssay"]], list[Union[dict, "BALFSputumAssay"]]]] = empty_dict()
    lung_function_assays: Optional[Union[dict[Union[str, LungFunctionAssayId], Union[dict, "LungFunctionAssay"]], list[Union[dict, "LungFunctionAssay"]]]] = empty_dict()
    foxj_assays: Optional[Union[dict[Union[str, FoxJExpressionAssayId], Union[dict, "FoxJExpressionAssay"]], list[Union[dict, "FoxJExpressionAssay"]]]] = empty_dict()
    gene_expression_assays: Optional[Union[dict[Union[str, GeneExpressionAssayId], Union[dict, "GeneExpressionAssay"]], list[Union[dict, "GeneExpressionAssay"]]]] = empty_dict()
    protocols: Optional[Union[dict[Union[str, ProtocolId], Union[dict, "Protocol"]], list[Union[dict, "Protocol"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="key_events", slot_type=KeyEvent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="adverse_outcome_pathways", slot_type=AdverseOutcomePathway, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ciliary_function_assays", slot_type=CiliaryFunctionAssay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="asl_assays", slot_type=ASLAssay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="mcc_assays", slot_type=MucociliaryClearanceAssay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="oxidative_stress_assays", slot_type=OxidativeStressAssay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="cftr_assays", slot_type=CFTRFunctionAssay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="egfr_signaling_assays", slot_type=EGFRSignalingAssay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="goblet_cell_assays", slot_type=GobletCellAssay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="balf_sputum_assays", slot_type=BALFSputumAssay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="lung_function_assays", slot_type=LungFunctionAssay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="foxj_assays", slot_type=FoxJExpressionAssay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="gene_expression_assays", slot_type=GeneExpressionAssay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="protocols", slot_type=Protocol, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic entity with an identifier and name. Base class for all named entities in the schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_FRAMEWORK["NamedThing"]
    class_class_curie: ClassVar[str] = "aop_framework:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = SOMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeyEvent(NamedThing):
    """
    A measurable change in biological state that is a step in an Adverse Outcome Pathway. Key Events represent the
    biological perturbations that assays measure to provide evidence for AOP-based mechanistic understanding. Key
    events can be Molecular Initiating Events (MIEs), intermediate Key Events, or Adverse Outcomes at the
    organism/population level.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ECTO["1000000"]
    class_class_curie: ClassVar[str] = "ECTO:1000000"
    class_name: ClassVar[str] = "KeyEvent"
    class_model_uri: ClassVar[URIRef] = SOMA.KeyEvent

    id: Union[str, KeyEventId] = None
    biological_process: Optional[Union[str, URIorCURIE]] = None
    biological_object: Optional[str] = None
    biological_action: Optional[Union[str, "BiologicalActionEnum"]] = None
    level_of_biological_organization: Optional[Union[str, "BiologicalOrganizationLevelEnum"]] = None
    occurs_in_cell_type: Optional[Union[str, URIorCURIE]] = None
    occurs_in_anatomy: Optional[Union[str, URIorCURIE]] = None
    aopwiki_id: Optional[str] = None
    upstream_key_events: Optional[Union[dict[Union[str, KeyEventId], Union[dict, "KeyEvent"]], list[Union[dict, "KeyEvent"]]]] = empty_dict()
    downstream_key_events: Optional[Union[dict[Union[str, KeyEventId], Union[dict, "KeyEvent"]], list[Union[dict, "KeyEvent"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeyEventId):
            self.id = KeyEventId(self.id)

        if self.biological_process is not None and not isinstance(self.biological_process, URIorCURIE):
            self.biological_process = URIorCURIE(self.biological_process)

        if self.biological_object is not None and not isinstance(self.biological_object, str):
            self.biological_object = str(self.biological_object)

        if self.biological_action is not None and not isinstance(self.biological_action, BiologicalActionEnum):
            self.biological_action = BiologicalActionEnum(self.biological_action)

        if self.level_of_biological_organization is not None and not isinstance(self.level_of_biological_organization, BiologicalOrganizationLevelEnum):
            self.level_of_biological_organization = BiologicalOrganizationLevelEnum(self.level_of_biological_organization)

        if self.occurs_in_cell_type is not None and not isinstance(self.occurs_in_cell_type, URIorCURIE):
            self.occurs_in_cell_type = URIorCURIE(self.occurs_in_cell_type)

        if self.occurs_in_anatomy is not None and not isinstance(self.occurs_in_anatomy, URIorCURIE):
            self.occurs_in_anatomy = URIorCURIE(self.occurs_in_anatomy)

        if self.aopwiki_id is not None and not isinstance(self.aopwiki_id, str):
            self.aopwiki_id = str(self.aopwiki_id)

        self._normalize_inlined_as_list(slot_name="upstream_key_events", slot_type=KeyEvent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="downstream_key_events", slot_type=KeyEvent, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeyEventRelationship(NamedThing):
    """
    A directional relationship between two key events in an AOP. Represents the causal linkage between an upstream
    event and a downstream event with supporting evidence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_FRAMEWORK["KeyEventRelationship"]
    class_class_curie: ClassVar[str] = "aop_framework:KeyEventRelationship"
    class_name: ClassVar[str] = "KeyEventRelationship"
    class_model_uri: ClassVar[URIRef] = SOMA.KeyEventRelationship

    id: Union[str, KeyEventRelationshipId] = None
    upstream_event: Optional[Union[dict, KeyEvent]] = None
    downstream_event: Optional[Union[dict, KeyEvent]] = None
    relationship_type: Optional[str] = None
    evidence_support: Optional[Union[str, "EvidenceSupportEnum"]] = None
    quantitative_understanding: Optional[Union[str, "QuantitativeUnderstandingEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeyEventRelationshipId):
            self.id = KeyEventRelationshipId(self.id)

        if self.upstream_event is not None and not isinstance(self.upstream_event, KeyEvent):
            self.upstream_event = KeyEvent(**as_dict(self.upstream_event))

        if self.downstream_event is not None and not isinstance(self.downstream_event, KeyEvent):
            self.downstream_event = KeyEvent(**as_dict(self.downstream_event))

        if self.relationship_type is not None and not isinstance(self.relationship_type, str):
            self.relationship_type = str(self.relationship_type)

        if self.evidence_support is not None and not isinstance(self.evidence_support, EvidenceSupportEnum):
            self.evidence_support = EvidenceSupportEnum(self.evidence_support)

        if self.quantitative_understanding is not None and not isinstance(self.quantitative_understanding, QuantitativeUnderstandingEnum):
            self.quantitative_understanding = QuantitativeUnderstandingEnum(self.quantitative_understanding)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdverseOutcome(NamedThing):
    """
    An adverse health outcome at the organism or population level that represents the apical endpoint of an Adverse
    Outcome Pathway. This is the final, clinically or ecologically relevant effect.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_FRAMEWORK["AdverseOutcome"]
    class_class_curie: ClassVar[str] = "aop_framework:AdverseOutcome"
    class_name: ClassVar[str] = "AdverseOutcome"
    class_model_uri: ClassVar[URIRef] = SOMA.AdverseOutcome

    id: Union[str, AdverseOutcomeId] = None
    outcome_level: Optional[Union[str, "OutcomeLevelEnum"]] = None
    biological_process: Optional[Union[str, URIorCURIE]] = None
    occurs_in_anatomy: Optional[Union[str, URIorCURIE]] = None
    aopwiki_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdverseOutcomeId):
            self.id = AdverseOutcomeId(self.id)

        if self.outcome_level is not None and not isinstance(self.outcome_level, OutcomeLevelEnum):
            self.outcome_level = OutcomeLevelEnum(self.outcome_level)

        if self.biological_process is not None and not isinstance(self.biological_process, URIorCURIE):
            self.biological_process = URIorCURIE(self.biological_process)

        if self.occurs_in_anatomy is not None and not isinstance(self.occurs_in_anatomy, URIorCURIE):
            self.occurs_in_anatomy = URIorCURIE(self.occurs_in_anatomy)

        if self.aopwiki_id is not None and not isinstance(self.aopwiki_id, str):
            self.aopwiki_id = str(self.aopwiki_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdverseOutcomePathway(NamedThing):
    """
    A sequence of causally linked events at different levels of biological organization that lead from a molecular
    initiating event through intermediate key events to an adverse health outcome. AOPs provide a structured framework
    for organizing mechanistic evidence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_FRAMEWORK["AdverseOutcomePathway"]
    class_class_curie: ClassVar[str] = "aop_framework:AdverseOutcomePathway"
    class_name: ClassVar[str] = "AdverseOutcomePathway"
    class_model_uri: ClassVar[URIRef] = SOMA.AdverseOutcomePathway

    id: Union[str, AdverseOutcomePathwayId] = None
    aopwiki_id: Optional[str] = None
    molecular_initiating_event: Optional[Union[dict, "MolecularInitiatingEvent"]] = None
    key_events: Optional[Union[dict[Union[str, KeyEventId], Union[dict, KeyEvent]], list[Union[dict, KeyEvent]]]] = empty_dict()
    key_event_relationships: Optional[Union[dict[Union[str, KeyEventRelationshipId], Union[dict, KeyEventRelationship]], list[Union[dict, KeyEventRelationship]]]] = empty_dict()
    adverse_outcome: Optional[Union[dict, AdverseOutcome]] = None
    stressors: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdverseOutcomePathwayId):
            self.id = AdverseOutcomePathwayId(self.id)

        if self.aopwiki_id is not None and not isinstance(self.aopwiki_id, str):
            self.aopwiki_id = str(self.aopwiki_id)

        if self.molecular_initiating_event is not None and not isinstance(self.molecular_initiating_event, MolecularInitiatingEvent):
            self.molecular_initiating_event = MolecularInitiatingEvent(**as_dict(self.molecular_initiating_event))

        self._normalize_inlined_as_list(slot_name="key_events", slot_type=KeyEvent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="key_event_relationships", slot_type=KeyEventRelationship, key_name="id", keyed=True)

        if self.adverse_outcome is not None and not isinstance(self.adverse_outcome, AdverseOutcome):
            self.adverse_outcome = AdverseOutcome(**as_dict(self.adverse_outcome))

        if not isinstance(self.stressors, list):
            self.stressors = [self.stressors] if self.stressors is not None else []
        self.stressors = [v if isinstance(v, str) else str(v) for v in self.stressors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularInitiatingEvent(KeyEvent):
    """
    The initial molecular-level perturbation that starts an Adverse Outcome Pathway. The MIE is the direct interaction
    between a stressor and a biological target (e.g., receptor binding, enzyme inhibition).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AOP_FRAMEWORK["MolecularInitiatingEvent"]
    class_class_curie: ClassVar[str] = "aop_framework:MolecularInitiatingEvent"
    class_name: ClassVar[str] = "MolecularInitiatingEvent"
    class_model_uri: ClassVar[URIRef] = SOMA.MolecularInitiatingEvent

    id: Union[str, MolecularInitiatingEventId] = None
    target_molecule: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularInitiatingEventId):
            self.id = MolecularInitiatingEventId(self.id)

        if self.target_molecule is not None and not isinstance(self.target_molecule, str):
            self.target_molecule = str(self.target_molecule)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assay(NamedThing):
    """
    A planned process with the objective to produce information about biological state relevant to a Key Event in an
    Adverse Outcome Pathway. Assays are organized by the functional domain they assess (e.g., ciliary function,
    oxidative stress), and each domain-specific assay class contains named slots for the specific measurements it can
    produce. Assays inform on key events and contain the measurement data as named slots.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "OBI:0000070"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = SOMA.Assay

    id: Union[str, AssayId] = None
    informs_on_key_event: Optional[Union[dict, KeyEvent]] = None
    study_subject: Optional[Union[dict, "StudySubject"]] = None
    has_exposure_condition: Optional[Union[dict[Union[str, ExposureConditionId], Union[dict, "ExposureCondition"]], list[Union[dict, "ExposureCondition"]]]] = empty_dict()
    follows_protocols: Optional[Union[dict[Union[str, ProtocolId], Union[dict, "Protocol"]], list[Union[dict, "Protocol"]]]] = empty_dict()
    has_specified_output: Optional[Union[dict, "AssayOutputMeasurement"]] = None
    assay_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.informs_on_key_event is not None and not isinstance(self.informs_on_key_event, KeyEvent):
            self.informs_on_key_event = KeyEvent(**as_dict(self.informs_on_key_event))

        if self.study_subject is not None and not isinstance(self.study_subject, StudySubject):
            self.study_subject = StudySubject(**as_dict(self.study_subject))

        self._normalize_inlined_as_list(slot_name="has_exposure_condition", slot_type=ExposureCondition, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="follows_protocols", slot_type=Protocol, key_name="id", keyed=True)

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, AssayOutputMeasurement):
            self.has_specified_output = AssayOutputMeasurement(**as_dict(self.has_specified_output))

        if self.assay_date is not None and not isinstance(self.assay_date, XSDDate):
            self.assay_date = XSDDate(self.assay_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssayOutputMeasurement(NamedThing):
    """
    The measurement results produced by an assay. The specified output of a planned process. Each domain-specific
    assay class has a corresponding AssayOutputMeasurement subclass containing the named measurement slots for that
    assay type. This class represents the "output" in the Input/Process/Output model: what was measured and what
    values were obtained.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["AssayOutputMeasurement"]
    class_class_curie: ClassVar[str] = "assay_base:AssayOutputMeasurement"
    class_name: ClassVar[str] = "AssayOutputMeasurement"
    class_model_uri: ClassVar[URIRef] = SOMA.AssayOutputMeasurement

    id: Union[str, AssayOutputMeasurementId] = None

@dataclass(repr=False)
class StudySubject(NamedThing):
    """
    The subject of a study — what the assay is performed on. Subclasses capture different experimental contexts (model
    systems, living subjects, populations) with context-appropriate slots. The type of subject determines which slots
    are available, replacing the old mixin pattern.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["StudySubject"]
    class_class_curie: ClassVar[str] = "assay_base:StudySubject"
    class_name: ClassVar[str] = "StudySubject"
    class_model_uri: ClassVar[URIRef] = SOMA.StudySubject

    id: Union[str, StudySubjectId] = None
    subject_type: Optional[str] = None
    model_species: Optional[Union[dict, "SpeciesReference"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudySubjectId):
            self.id = StudySubjectId(self.id)

        self.subject_type = str(self.class_name)

        if self.model_species is not None and not isinstance(self.model_species, SpeciesReference):
            self.model_species = SpeciesReference(**as_dict(self.model_species))

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "subject_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class ModelSystem(StudySubject):
    """
    An in vitro or ex vivo model system used to study biological processes. Parent class for cell-based and other
    model systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["ModelSystem"]
    class_class_curie: ClassVar[str] = "assay_base:ModelSystem"
    class_name: ClassVar[str] = "ModelSystem"
    class_model_uri: ClassVar[URIRef] = SOMA.ModelSystem

    id: Union[str, ModelSystemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelSystemId):
            self.id = ModelSystemId(self.id)

        super().__post_init__(**kwargs)
        self.subject_type = str(self.class_name)


@dataclass(repr=False)
class InVivoSubject(StudySubject):
    """
    A living human or animal subject from whom measurements are taken. Used for clinical assays (lung function,
    BALF/sputum) and any assay performed on living subjects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["InVivoSubject"]
    class_class_curie: ClassVar[str] = "assay_base:InVivoSubject"
    class_name: ClassVar[str] = "InVivoSubject"
    class_model_uri: ClassVar[URIRef] = SOMA.InVivoSubject

    id: Union[str, InVivoSubjectId] = None
    age: Optional[Union[dict, "QuantityValue"]] = None
    sex: Optional[str] = None
    subject_characteristics: Optional[str] = None
    disease_state: Optional[str] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    collection_site: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    sample_collection_method: Optional[str] = None
    clinical_context: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InVivoSubjectId):
            self.id = InVivoSubjectId(self.id)

        if self.age is not None and not isinstance(self.age, QuantityValue):
            self.age = QuantityValue(**as_dict(self.age))

        if self.sex is not None and not isinstance(self.sex, str):
            self.sex = str(self.sex)

        if self.subject_characteristics is not None and not isinstance(self.subject_characteristics, str):
            self.subject_characteristics = str(self.subject_characteristics)

        if self.disease_state is not None and not isinstance(self.disease_state, str):
            self.disease_state = str(self.disease_state)

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.collection_site is not None and not isinstance(self.collection_site, str):
            self.collection_site = str(self.collection_site)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.sample_collection_method is not None and not isinstance(self.sample_collection_method, str):
            self.sample_collection_method = str(self.sample_collection_method)

        if self.clinical_context is not None and not isinstance(self.clinical_context, str):
            self.clinical_context = str(self.clinical_context)

        super().__post_init__(**kwargs)
        self.subject_type = str(self.class_name)


@dataclass(repr=False)
class PopulationSubject(StudySubject):
    """
    A population or cohort of subjects studied in aggregate. Used for epidemiological or population-level analyses.
    Can optionally hold references to individual InVivoSubject members.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["PopulationSubject"]
    class_class_curie: ClassVar[str] = "assay_base:PopulationSubject"
    class_name: ClassVar[str] = "PopulationSubject"
    class_model_uri: ClassVar[URIRef] = SOMA.PopulationSubject

    id: Union[str, PopulationSubjectId] = None
    cohort_size: Optional[int] = None
    inclusion_criteria: Optional[str] = None
    age_range: Optional[Union[dict, "QuantityRange"]] = None
    subjects: Optional[Union[dict[Union[str, InVivoSubjectId], Union[dict, InVivoSubject]], list[Union[dict, InVivoSubject]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PopulationSubjectId):
            self.id = PopulationSubjectId(self.id)

        if self.cohort_size is not None and not isinstance(self.cohort_size, int):
            self.cohort_size = int(self.cohort_size)

        if self.inclusion_criteria is not None and not isinstance(self.inclusion_criteria, str):
            self.inclusion_criteria = str(self.inclusion_criteria)

        if self.age_range is not None and not isinstance(self.age_range, QuantityRange):
            self.age_range = QuantityRange(**as_dict(self.age_range))

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=InVivoSubject, key_name="id", keyed=True)

        super().__post_init__(**kwargs)
        self.subject_type = str(self.class_name)


@dataclass(repr=False)
class Protocol(NamedThing):
    """
    A detailed set of steps for how to perform a specific assay. Protocols ensure reproducibility across laboratories.
    Contains universal slots; domain-specific details are in protocol subclasses (ImagingProtocol, StainingProtocol,
    etc.). Protocols can reference other protocols via sub_protocols to represent composite workflows (e.g., sample
    preparation, wash steps, or post-processing protocols that are shared across assays).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000272"]
    class_class_curie: ClassVar[str] = "OBI:0000272"
    class_name: ClassVar[str] = "Protocol"
    class_model_uri: ClassVar[URIRef] = SOMA.Protocol

    id: Union[str, ProtocolId] = None
    protocol_type: Optional[str] = None
    protocol_version: Optional[str] = None
    equipment_required: Optional[Union[str, list[str]]] = empty_list()
    sub_protocols: Optional[Union[dict[Union[str, ProtocolId], Union[dict, "Protocol"]], list[Union[dict, "Protocol"]]]] = empty_dict()
    quality_control_criteria: Optional[str] = None
    replicate_requirements: Optional[int] = None
    protocol_author: Optional[str] = None
    institution: Optional[str] = None
    publication_reference: Optional[str] = None
    last_updated: Optional[Union[str, XSDDate]] = None
    validation_status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProtocolId):
            self.id = ProtocolId(self.id)

        self.protocol_type = str(self.class_name)

        if self.protocol_version is not None and not isinstance(self.protocol_version, str):
            self.protocol_version = str(self.protocol_version)

        if not isinstance(self.equipment_required, list):
            self.equipment_required = [self.equipment_required] if self.equipment_required is not None else []
        self.equipment_required = [v if isinstance(v, str) else str(v) for v in self.equipment_required]

        self._normalize_inlined_as_list(slot_name="sub_protocols", slot_type=Protocol, key_name="id", keyed=True)

        if self.quality_control_criteria is not None and not isinstance(self.quality_control_criteria, str):
            self.quality_control_criteria = str(self.quality_control_criteria)

        if self.replicate_requirements is not None and not isinstance(self.replicate_requirements, int):
            self.replicate_requirements = int(self.replicate_requirements)

        if self.protocol_author is not None and not isinstance(self.protocol_author, str):
            self.protocol_author = str(self.protocol_author)

        if self.institution is not None and not isinstance(self.institution, str):
            self.institution = str(self.institution)

        if self.publication_reference is not None and not isinstance(self.publication_reference, str):
            self.publication_reference = str(self.publication_reference)

        if self.last_updated is not None and not isinstance(self.last_updated, XSDDate):
            self.last_updated = XSDDate(self.last_updated)

        if self.validation_status is not None and not isinstance(self.validation_status, str):
            self.validation_status = str(self.validation_status)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "protocol_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class ImagingProtocol(Protocol):
    """
    Protocol for imaging-based assays (CBF, ASL, MCC). Captures frame rate, duration, resolution, and tracer/labeling
    details.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["ImagingProtocol"]
    class_class_curie: ClassVar[str] = "assay_base:ImagingProtocol"
    class_name: ClassVar[str] = "ImagingProtocol"
    class_model_uri: ClassVar[URIRef] = SOMA.ImagingProtocol

    id: Union[str, ImagingProtocolId] = None
    imaging_frame_rate: Optional[Union[dict, "QuantityValue"]] = None
    imaging_duration: Optional[Union[dict, "QuantityValue"]] = None
    spatial_resolution: Optional[Union[dict, "QuantityValue"]] = None
    fluorescent_labeling: Optional[str] = None
    fluorescent_tracer: Optional[str] = None
    evaporation_prevention: Optional[str] = None
    particle_tracking_method: Optional[str] = None
    temperature_control: Optional[Union[dict, "QuantityValue"]] = None
    humidity_control: Optional[Union[dict, "QuantityValue"]] = None
    particle_size: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImagingProtocolId):
            self.id = ImagingProtocolId(self.id)

        if self.imaging_frame_rate is not None and not isinstance(self.imaging_frame_rate, QuantityValue):
            self.imaging_frame_rate = QuantityValue(**as_dict(self.imaging_frame_rate))

        if self.imaging_duration is not None and not isinstance(self.imaging_duration, QuantityValue):
            self.imaging_duration = QuantityValue(**as_dict(self.imaging_duration))

        if self.spatial_resolution is not None and not isinstance(self.spatial_resolution, QuantityValue):
            self.spatial_resolution = QuantityValue(**as_dict(self.spatial_resolution))

        if self.fluorescent_labeling is not None and not isinstance(self.fluorescent_labeling, str):
            self.fluorescent_labeling = str(self.fluorescent_labeling)

        if self.fluorescent_tracer is not None and not isinstance(self.fluorescent_tracer, str):
            self.fluorescent_tracer = str(self.fluorescent_tracer)

        if self.evaporation_prevention is not None and not isinstance(self.evaporation_prevention, str):
            self.evaporation_prevention = str(self.evaporation_prevention)

        if self.particle_tracking_method is not None and not isinstance(self.particle_tracking_method, str):
            self.particle_tracking_method = str(self.particle_tracking_method)

        if self.temperature_control is not None and not isinstance(self.temperature_control, QuantityValue):
            self.temperature_control = QuantityValue(**as_dict(self.temperature_control))

        if self.humidity_control is not None and not isinstance(self.humidity_control, QuantityValue):
            self.humidity_control = QuantityValue(**as_dict(self.humidity_control))

        if self.particle_size is not None and not isinstance(self.particle_size, QuantityValue):
            self.particle_size = QuantityValue(**as_dict(self.particle_size))

        super().__post_init__(**kwargs)
        self.protocol_type = str(self.class_name)


@dataclass(repr=False)
class StainingProtocol(Protocol):
    """
    Protocol for staining-based assays (goblet cell, immunofluorescence). Captures staining type, antibodies,
    fixation, and detection details.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["StainingProtocol"]
    class_class_curie: ClassVar[str] = "assay_base:StainingProtocol"
    class_name: ClassVar[str] = "StainingProtocol"
    class_model_uri: ClassVar[URIRef] = SOMA.StainingProtocol

    id: Union[str, StainingProtocolId] = None
    staining_type: Optional[str] = None
    antibodies_used: Optional[Union[str, list[str]]] = empty_list()
    detection_method: Optional[str] = None
    normalization_method: Optional[str] = None
    fixation_method: Optional[str] = None
    counterstain: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StainingProtocolId):
            self.id = StainingProtocolId(self.id)

        if self.staining_type is not None and not isinstance(self.staining_type, str):
            self.staining_type = str(self.staining_type)

        if not isinstance(self.antibodies_used, list):
            self.antibodies_used = [self.antibodies_used] if self.antibodies_used is not None else []
        self.antibodies_used = [v if isinstance(v, str) else str(v) for v in self.antibodies_used]

        if self.detection_method is not None and not isinstance(self.detection_method, str):
            self.detection_method = str(self.detection_method)

        if self.normalization_method is not None and not isinstance(self.normalization_method, str):
            self.normalization_method = str(self.normalization_method)

        if self.fixation_method is not None and not isinstance(self.fixation_method, str):
            self.fixation_method = str(self.fixation_method)

        if self.counterstain is not None and not isinstance(self.counterstain, str):
            self.counterstain = str(self.counterstain)

        super().__post_init__(**kwargs)
        self.protocol_type = str(self.class_name)


@dataclass(repr=False)
class SpirometryProtocol(Protocol):
    """
    Protocol for lung function / spirometry assays. Captures spirometry standards, bronchodilator details, and
    plethysmography method.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["SpirometryProtocol"]
    class_class_curie: ClassVar[str] = "assay_base:SpirometryProtocol"
    class_name: ClassVar[str] = "SpirometryProtocol"
    class_model_uri: ClassVar[URIRef] = SOMA.SpirometryProtocol

    id: Union[str, SpirometryProtocolId] = None
    spirometry_standard: Optional[str] = None
    bronchodilator_agent: Optional[str] = None
    bronchodilator_dose: Optional[Union[dict, "QuantityValue"]] = None
    plethysmography_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpirometryProtocolId):
            self.id = SpirometryProtocolId(self.id)

        if self.spirometry_standard is not None and not isinstance(self.spirometry_standard, str):
            self.spirometry_standard = str(self.spirometry_standard)

        if self.bronchodilator_agent is not None and not isinstance(self.bronchodilator_agent, str):
            self.bronchodilator_agent = str(self.bronchodilator_agent)

        if self.bronchodilator_dose is not None and not isinstance(self.bronchodilator_dose, QuantityValue):
            self.bronchodilator_dose = QuantityValue(**as_dict(self.bronchodilator_dose))

        if self.plethysmography_method is not None and not isinstance(self.plethysmography_method, str):
            self.plethysmography_method = str(self.plethysmography_method)

        super().__post_init__(**kwargs)
        self.protocol_type = str(self.class_name)


@dataclass(repr=False)
class MolecularAssayProtocol(Protocol):
    """
    Protocol for molecular biology assays (qRT-PCR, Western blot, ELISA). Captures detection method, normalization,
    primers, and platform details.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["MolecularAssayProtocol"]
    class_class_curie: ClassVar[str] = "assay_base:MolecularAssayProtocol"
    class_name: ClassVar[str] = "MolecularAssayProtocol"
    class_model_uri: ClassVar[URIRef] = SOMA.MolecularAssayProtocol

    id: Union[str, MolecularAssayProtocolId] = None
    detection_method: Optional[str] = None
    normalization_method: Optional[str] = None
    antibodies_used: Optional[Union[str, list[str]]] = empty_list()
    primer_sequences: Optional[Union[str, list[str]]] = empty_list()
    reference_gene: Optional[str] = None
    lysis_buffer: Optional[str] = None
    platform: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularAssayProtocolId):
            self.id = MolecularAssayProtocolId(self.id)

        if self.detection_method is not None and not isinstance(self.detection_method, str):
            self.detection_method = str(self.detection_method)

        if self.normalization_method is not None and not isinstance(self.normalization_method, str):
            self.normalization_method = str(self.normalization_method)

        if not isinstance(self.antibodies_used, list):
            self.antibodies_used = [self.antibodies_used] if self.antibodies_used is not None else []
        self.antibodies_used = [v if isinstance(v, str) else str(v) for v in self.antibodies_used]

        if not isinstance(self.primer_sequences, list):
            self.primer_sequences = [self.primer_sequences] if self.primer_sequences is not None else []
        self.primer_sequences = [v if isinstance(v, str) else str(v) for v in self.primer_sequences]

        if self.reference_gene is not None and not isinstance(self.reference_gene, str):
            self.reference_gene = str(self.reference_gene)

        if self.lysis_buffer is not None and not isinstance(self.lysis_buffer, str):
            self.lysis_buffer = str(self.lysis_buffer)

        if self.platform is not None and not isinstance(self.platform, str):
            self.platform = str(self.platform)

        super().__post_init__(**kwargs)
        self.protocol_type = str(self.class_name)


@dataclass(repr=False)
class QuantityValue(YAMLRoot):
    """
    A quantity with a numeric value and unit of measurement. Used for all measurement values in assays.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["QuantityValue"]
    class_class_curie: ClassVar[str] = "assay_base:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = SOMA.QuantityValue

    value: Optional[str] = None
    unit: Optional[Union[dict, "Unit"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, Unit):
            self.unit = Unit(**as_dict(self.unit))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Unit(YAMLRoot):
    """
    A unit of measurement from a standard ontology (UO, UCUM, QUDT).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["Unit"]
    class_class_curie: ClassVar[str] = "assay_base:Unit"
    class_name: ClassVar[str] = "Unit"
    class_model_uri: ClassVar[URIRef] = SOMA.Unit

    id: Union[str, UnitId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnitId):
            self.id = UnitId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedEntity(YAMLRoot):
    """
    A reference to an entity with an identifier and name. Used for cell_type, tissue_context, participant references,
    etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["NamedEntity"]
    class_class_curie: ClassVar[str] = "assay_base:NamedEntity"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = SOMA.NamedEntity

    id: Union[str, NamedEntityId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellTypeReference(NamedEntity):
    """
    A reference to a cell type from the Cell Ontology (CL).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["CellTypeReference"]
    class_class_curie: ClassVar[str] = "assay_base:CellTypeReference"
    class_name: ClassVar[str] = "CellTypeReference"
    class_model_uri: ClassVar[URIRef] = SOMA.CellTypeReference

    id: Union[str, CellTypeReferenceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellTypeReferenceId):
            self.id = CellTypeReferenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpeciesReference(NamedEntity):
    """
    A reference to a species from the NCBI Taxonomy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["SpeciesReference"]
    class_class_curie: ClassVar[str] = "assay_base:SpeciesReference"
    class_name: ClassVar[str] = "SpeciesReference"
    class_model_uri: ClassVar[URIRef] = SOMA.SpeciesReference

    id: Union[str, SpeciesReferenceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpeciesReferenceId):
            self.id = SpeciesReferenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntityReference(NamedEntity):
    """
    A reference to a chemical entity from CHEBI or an exposure concept from ECTO.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["ChemicalEntityReference"]
    class_class_curie: ClassVar[str] = "assay_base:ChemicalEntityReference"
    class_name: ClassVar[str] = "ChemicalEntityReference"
    class_model_uri: ClassVar[URIRef] = SOMA.ChemicalEntityReference

    id: Union[str, ChemicalEntityReferenceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityReferenceId):
            self.id = ChemicalEntityReferenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnatomicalEntityReference(NamedEntity):
    """
    A reference to an anatomical entity from UBERON.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["AnatomicalEntityReference"]
    class_class_curie: ClassVar[str] = "assay_base:AnatomicalEntityReference"
    class_name: ClassVar[str] = "AnatomicalEntityReference"
    class_model_uri: ClassVar[URIRef] = SOMA.AnatomicalEntityReference

    id: Union[str, AnatomicalEntityReferenceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityReferenceId):
            self.id = AnatomicalEntityReferenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureCondition(NamedEntity):
    """
    A structured description of an exposure or treatment applied to a biological system. Captures what agent was
    applied, at what concentration, for how long, and when the measurement was taken relative to exposure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["ExposureCondition"]
    class_class_curie: ClassVar[str] = "assay_base:ExposureCondition"
    class_name: ClassVar[str] = "ExposureCondition"
    class_model_uri: ClassVar[URIRef] = SOMA.ExposureCondition

    id: Union[str, ExposureConditionId] = None
    exposure_agent: Optional[Union[dict, ChemicalEntityReference]] = None
    exposure_concentration: Optional[Union[dict, QuantityValue]] = None
    exposure_duration: Optional[Union[dict, QuantityValue]] = None
    timing_post_exposure: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureConditionId):
            self.id = ExposureConditionId(self.id)

        if self.exposure_agent is not None and not isinstance(self.exposure_agent, ChemicalEntityReference):
            self.exposure_agent = ChemicalEntityReference(**as_dict(self.exposure_agent))

        if self.exposure_concentration is not None and not isinstance(self.exposure_concentration, QuantityValue):
            self.exposure_concentration = QuantityValue(**as_dict(self.exposure_concentration))

        if self.exposure_duration is not None and not isinstance(self.exposure_duration, QuantityValue):
            self.exposure_duration = QuantityValue(**as_dict(self.exposure_duration))

        if self.timing_post_exposure is not None and not isinstance(self.timing_post_exposure, QuantityValue):
            self.timing_post_exposure = QuantityValue(**as_dict(self.timing_post_exposure))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellularSystem(ModelSystem):
    """
    Cell-based model systems that use living cells to model biological processes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["CellularSystem"]
    class_class_curie: ClassVar[str] = "assay_base:CellularSystem"
    class_name: ClassVar[str] = "CellularSystem"
    class_model_uri: ClassVar[URIRef] = SOMA.CellularSystem

    id: Union[str, CellularSystemId] = None
    cell_line: Optional[Union[dict, "CellLine"]] = None
    primary_cell: Optional[Union[dict, CellTypeReference]] = None
    cell_type: Optional[Union[dict, CellTypeReference]] = None
    anatomical_origin: Optional[Union[dict, AnatomicalEntityReference]] = None
    cell_culture_growth_mode: Optional[Union[str, "CellCultureGrowthModeEnum"]] = None
    substrate_type: Optional[Union[str, "SubstrateTypeEnum"]] = None
    confluence_level: Optional[Union[dict, QuantityValue]] = None
    passage_number: Optional[int] = None
    seeding_density: Optional[Union[dict, QuantityValue]] = None
    coating: Optional[str] = None
    matrix_composition: Optional[str] = None
    size_range: Optional[Union[dict, "QuantityRange"]] = None
    organoid_type: Optional[str] = None
    cell_type_ratios: Optional[Union[str, list[str]]] = empty_list()
    culture_conditions: Optional[Union[dict, "CellCultureConditions"]] = None
    culture_media: Optional[Union[dict, "CellCultureMedium"]] = None
    days_at_differentiation: Optional[int] = None
    donor_info: Optional[str] = None
    replicates_per_donor: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellularSystemId):
            self.id = CellularSystemId(self.id)

        if self.cell_line is not None and not isinstance(self.cell_line, CellLine):
            self.cell_line = CellLine(**as_dict(self.cell_line))

        if self.primary_cell is not None and not isinstance(self.primary_cell, CellTypeReference):
            self.primary_cell = CellTypeReference(**as_dict(self.primary_cell))

        if self.cell_type is not None and not isinstance(self.cell_type, CellTypeReference):
            self.cell_type = CellTypeReference(**as_dict(self.cell_type))

        if self.anatomical_origin is not None and not isinstance(self.anatomical_origin, AnatomicalEntityReference):
            self.anatomical_origin = AnatomicalEntityReference(**as_dict(self.anatomical_origin))

        if self.cell_culture_growth_mode is not None and not isinstance(self.cell_culture_growth_mode, CellCultureGrowthModeEnum):
            self.cell_culture_growth_mode = CellCultureGrowthModeEnum(self.cell_culture_growth_mode)

        if self.substrate_type is not None and not isinstance(self.substrate_type, SubstrateTypeEnum):
            self.substrate_type = SubstrateTypeEnum(self.substrate_type)

        if self.confluence_level is not None and not isinstance(self.confluence_level, QuantityValue):
            self.confluence_level = QuantityValue(**as_dict(self.confluence_level))

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.seeding_density is not None and not isinstance(self.seeding_density, QuantityValue):
            self.seeding_density = QuantityValue(**as_dict(self.seeding_density))

        if self.coating is not None and not isinstance(self.coating, str):
            self.coating = str(self.coating)

        if self.matrix_composition is not None and not isinstance(self.matrix_composition, str):
            self.matrix_composition = str(self.matrix_composition)

        if self.size_range is not None and not isinstance(self.size_range, QuantityRange):
            self.size_range = QuantityRange(**as_dict(self.size_range))

        if self.organoid_type is not None and not isinstance(self.organoid_type, str):
            self.organoid_type = str(self.organoid_type)

        if not isinstance(self.cell_type_ratios, list):
            self.cell_type_ratios = [self.cell_type_ratios] if self.cell_type_ratios is not None else []
        self.cell_type_ratios = [v if isinstance(v, str) else str(v) for v in self.cell_type_ratios]

        if self.culture_conditions is not None and not isinstance(self.culture_conditions, CellCultureConditions):
            self.culture_conditions = CellCultureConditions(**as_dict(self.culture_conditions))

        if self.culture_media is not None and not isinstance(self.culture_media, CellCultureMedium):
            self.culture_media = CellCultureMedium(**as_dict(self.culture_media))

        if self.days_at_differentiation is not None and not isinstance(self.days_at_differentiation, int):
            self.days_at_differentiation = int(self.days_at_differentiation)

        if self.donor_info is not None and not isinstance(self.donor_info, str):
            self.donor_info = str(self.donor_info)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        super().__post_init__(**kwargs)
        self.subject_type = str(self.class_name)


@dataclass(repr=False)
class CellLine(NamedEntity):
    """
    A cell line - a genetically stable cultured cell population.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["CellLine"]
    class_class_curie: ClassVar[str] = "assay_base:CellLine"
    class_name: ClassVar[str] = "CellLine"
    class_model_uri: ClassVar[URIRef] = SOMA.CellLine

    id: Union[str, CellLineId] = None
    cell_type: Optional[Union[dict, CellTypeReference]] = None
    model_species: Optional[Union[dict, SpeciesReference]] = None
    tissue_origin: Optional[str] = None
    disease_state: Optional[str] = None
    supplier: Optional[str] = None
    catalog_number: Optional[str] = None
    authentication_method: Optional[str] = None
    mycoplasma_status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)

        if self.cell_type is not None and not isinstance(self.cell_type, CellTypeReference):
            self.cell_type = CellTypeReference(**as_dict(self.cell_type))

        if self.model_species is not None and not isinstance(self.model_species, SpeciesReference):
            self.model_species = SpeciesReference(**as_dict(self.model_species))

        if self.tissue_origin is not None and not isinstance(self.tissue_origin, str):
            self.tissue_origin = str(self.tissue_origin)

        if self.disease_state is not None and not isinstance(self.disease_state, str):
            self.disease_state = str(self.disease_state)

        if self.supplier is not None and not isinstance(self.supplier, str):
            self.supplier = str(self.supplier)

        if self.catalog_number is not None and not isinstance(self.catalog_number, str):
            self.catalog_number = str(self.catalog_number)

        if self.authentication_method is not None and not isinstance(self.authentication_method, str):
            self.authentication_method = str(self.authentication_method)

        if self.mycoplasma_status is not None and not isinstance(self.mycoplasma_status, str):
            self.mycoplasma_status = str(self.mycoplasma_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellCultureConditions(NamedEntity):
    """
    Detailed cell culture parameters including medium, environment, and timing.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["CellCultureConditions"]
    class_class_curie: ClassVar[str] = "assay_base:CellCultureConditions"
    class_name: ClassVar[str] = "CellCultureConditions"
    class_model_uri: ClassVar[URIRef] = SOMA.CellCultureConditions

    id: Union[str, CellCultureConditionsId] = None
    culture_media: Optional[Union[dict, "CellCultureMedium"]] = None
    days_at_air_liquid_interface: Optional[int] = None
    passage_number: Optional[int] = None
    substrate_type: Optional[Union[str, "SubstrateTypeEnum"]] = None
    cell_culture_growth_mode: Optional[Union[str, "CellCultureGrowthModeEnum"]] = None
    donor_count: Optional[int] = None
    replicates_per_donor: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellCultureConditionsId):
            self.id = CellCultureConditionsId(self.id)

        if self.culture_media is not None and not isinstance(self.culture_media, CellCultureMedium):
            self.culture_media = CellCultureMedium(**as_dict(self.culture_media))

        if self.days_at_air_liquid_interface is not None and not isinstance(self.days_at_air_liquid_interface, int):
            self.days_at_air_liquid_interface = int(self.days_at_air_liquid_interface)

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.substrate_type is not None and not isinstance(self.substrate_type, SubstrateTypeEnum):
            self.substrate_type = SubstrateTypeEnum(self.substrate_type)

        if self.cell_culture_growth_mode is not None and not isinstance(self.cell_culture_growth_mode, CellCultureGrowthModeEnum):
            self.cell_culture_growth_mode = CellCultureGrowthModeEnum(self.cell_culture_growth_mode)

        if self.donor_count is not None and not isinstance(self.donor_count, int):
            self.donor_count = int(self.donor_count)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellCultureMedium(NamedEntity):
    """
    Detailed formulation of cell culture medium including base medium and supplements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["CellCultureMedium"]
    class_class_curie: ClassVar[str] = "assay_base:CellCultureMedium"
    class_name: ClassVar[str] = "CellCultureMedium"
    class_model_uri: ClassVar[URIRef] = SOMA.CellCultureMedium

    id: Union[str, CellCultureMediumId] = None
    base_medium: Optional[str] = None
    serum_type: Optional[str] = None
    serum_concentration: Optional[Union[dict, QuantityValue]] = None
    supplements: Optional[Union[dict[Union[str, MediumSupplementId], Union[dict, "MediumSupplement"]], list[Union[dict, "MediumSupplement"]]]] = empty_dict()
    osmolality: Optional[Union[dict, QuantityValue]] = None
    manufacturer: Optional[str] = None
    catalog_number: Optional[str] = None
    lot_number: Optional[str] = None
    preparation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellCultureMediumId):
            self.id = CellCultureMediumId(self.id)

        if self.base_medium is not None and not isinstance(self.base_medium, str):
            self.base_medium = str(self.base_medium)

        if self.serum_type is not None and not isinstance(self.serum_type, str):
            self.serum_type = str(self.serum_type)

        if self.serum_concentration is not None and not isinstance(self.serum_concentration, QuantityValue):
            self.serum_concentration = QuantityValue(**as_dict(self.serum_concentration))

        self._normalize_inlined_as_list(slot_name="supplements", slot_type=MediumSupplement, key_name="id", keyed=True)

        if self.osmolality is not None and not isinstance(self.osmolality, QuantityValue):
            self.osmolality = QuantityValue(**as_dict(self.osmolality))

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.catalog_number is not None and not isinstance(self.catalog_number, str):
            self.catalog_number = str(self.catalog_number)

        if self.lot_number is not None and not isinstance(self.lot_number, str):
            self.lot_number = str(self.lot_number)

        if self.preparation_date is not None and not isinstance(self.preparation_date, XSDDate):
            self.preparation_date = XSDDate(self.preparation_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediumSupplement(NamedEntity):
    """
    Supplement or additive to cell culture medium.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["MediumSupplement"]
    class_class_curie: ClassVar[str] = "assay_base:MediumSupplement"
    class_name: ClassVar[str] = "MediumSupplement"
    class_model_uri: ClassVar[URIRef] = SOMA.MediumSupplement

    id: Union[str, MediumSupplementId] = None
    supplement_type: Optional[Union[str, "SupplementTypeEnum"]] = None
    concentration: Optional[Union[dict, QuantityValue]] = None
    manufacturer: Optional[str] = None
    catalog_number: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MediumSupplementId):
            self.id = MediumSupplementId(self.id)

        if self.supplement_type is not None and not isinstance(self.supplement_type, SupplementTypeEnum):
            self.supplement_type = SupplementTypeEnum(self.supplement_type)

        if self.concentration is not None and not isinstance(self.concentration, QuantityValue):
            self.concentration = QuantityValue(**as_dict(self.concentration))

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.catalog_number is not None and not isinstance(self.catalog_number, str):
            self.catalog_number = str(self.catalog_number)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityRange(YAMLRoot):
    """
    A range of quantity values with minimum and maximum bounds.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_BASE["QuantityRange"]
    class_class_curie: ClassVar[str] = "assay_base:QuantityRange"
    class_name: ClassVar[str] = "QuantityRange"
    class_model_uri: ClassVar[URIRef] = SOMA.QuantityRange

    min_value: Optional[Union[dict, QuantityValue]] = None
    max_value: Optional[Union[dict, QuantityValue]] = None
    unit: Optional[Union[dict, Unit]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.min_value is not None and not isinstance(self.min_value, QuantityValue):
            self.min_value = QuantityValue(**as_dict(self.min_value))

        if self.max_value is not None and not isinstance(self.max_value, QuantityValue):
            self.max_value = QuantityValue(**as_dict(self.max_value))

        if self.unit is not None and not isinstance(self.unit, Unit):
            self.unit = Unit(**as_dict(self.unit))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CiliaryFunctionAssay(Assay):
    """
    Assay for measuring ciliary function including beat frequency, active area, cilia morphology, and ciliated cell
    populations. Informs on Key Event: "Decreased ciliary function" in respiratory AOPs.
    CONTEXT: Can be performed in vitro (tissue slices, spheroids) or in vivo (often using optical coherence
    tomography).
    TIER 1 slots (critical): beat_frequency_hz, active_area_percentage, cilia_length, cilia_per_cell,
    percentage_ciliated_cells, cell_type_ratios,
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["CiliaryFunctionAssay"]
    class_class_curie: ClassVar[str] = "assay_microschemas:CiliaryFunctionAssay"
    class_name: ClassVar[str] = "CiliaryFunctionAssay"
    class_model_uri: ClassVar[URIRef] = SOMA.CiliaryFunctionAssay

    id: Union[str, CiliaryFunctionAssayId] = None
    analysis_software: Optional[str] = None
    airway_region: Optional[str] = None
    study_subject: Optional[Union[dict, StudySubject]] = None
    has_specified_output: Optional[Union[dict, "CiliaryFunctionOutput"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CiliaryFunctionAssayId):
            self.id = CiliaryFunctionAssayId(self.id)

        if self.analysis_software is not None and not isinstance(self.analysis_software, str):
            self.analysis_software = str(self.analysis_software)

        if self.airway_region is not None and not isinstance(self.airway_region, str):
            self.airway_region = str(self.airway_region)

        if self.study_subject is not None and not isinstance(self.study_subject, StudySubject):
            self.study_subject = StudySubject(**as_dict(self.study_subject))

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, CiliaryFunctionOutput):
            self.has_specified_output = CiliaryFunctionOutput(**as_dict(self.has_specified_output))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CiliaryFunctionOutput(AssayOutputMeasurement):
    """
    Measurement results from a ciliary function assay. Contains the measured values for ciliary beat frequency, active
    area, cilia morphology, and ciliated cell populations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["CiliaryFunctionOutput"]
    class_class_curie: ClassVar[str] = "assay_microschemas:CiliaryFunctionOutput"
    class_name: ClassVar[str] = "CiliaryFunctionOutput"
    class_model_uri: ClassVar[URIRef] = SOMA.CiliaryFunctionOutput

    id: Union[str, CiliaryFunctionOutputId] = None
    beat_frequency_hz: Optional[Union[dict, QuantityValue]] = None
    active_area_percentage: Optional[Union[dict, QuantityValue]] = None
    cilia_length: Optional[Union[dict, QuantityValue]] = None
    cilia_per_cell: Optional[Union[dict, QuantityValue]] = None
    percentage_ciliated_cells: Optional[Union[dict, QuantityValue]] = None
    cell_type_ratios: Optional[Union[str, list[str]]] = empty_list()
    ciliary_motion_patterns: Optional[Union[str, "CiliaryMotionPatternEnum"]] = None
    ciliary_beat_amplitude: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CiliaryFunctionOutputId):
            self.id = CiliaryFunctionOutputId(self.id)

        if self.beat_frequency_hz is not None and not isinstance(self.beat_frequency_hz, QuantityValue):
            self.beat_frequency_hz = QuantityValue(**as_dict(self.beat_frequency_hz))

        if self.active_area_percentage is not None and not isinstance(self.active_area_percentage, QuantityValue):
            self.active_area_percentage = QuantityValue(**as_dict(self.active_area_percentage))

        if self.cilia_length is not None and not isinstance(self.cilia_length, QuantityValue):
            self.cilia_length = QuantityValue(**as_dict(self.cilia_length))

        if self.cilia_per_cell is not None and not isinstance(self.cilia_per_cell, QuantityValue):
            self.cilia_per_cell = QuantityValue(**as_dict(self.cilia_per_cell))

        if self.percentage_ciliated_cells is not None and not isinstance(self.percentage_ciliated_cells, QuantityValue):
            self.percentage_ciliated_cells = QuantityValue(**as_dict(self.percentage_ciliated_cells))

        if not isinstance(self.cell_type_ratios, list):
            self.cell_type_ratios = [self.cell_type_ratios] if self.cell_type_ratios is not None else []
        self.cell_type_ratios = [v if isinstance(v, str) else str(v) for v in self.cell_type_ratios]

        if self.ciliary_motion_patterns is not None and not isinstance(self.ciliary_motion_patterns, CiliaryMotionPatternEnum):
            self.ciliary_motion_patterns = CiliaryMotionPatternEnum(self.ciliary_motion_patterns)

        if self.ciliary_beat_amplitude is not None and not isinstance(self.ciliary_beat_amplitude, QuantityValue):
            self.ciliary_beat_amplitude = QuantityValue(**as_dict(self.ciliary_beat_amplitude))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ASLAssay(Assay):
    """
    Assay for measuring airway surface liquid properties including ASL height, periciliary layer depth, and ion
    composition. Informs on Key Event: "Decreased ASL height" or "Altered airway hydration" in CF-related AOPs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["ASLAssay"]
    class_class_curie: ClassVar[str] = "assay_microschemas:ASLAssay"
    class_name: ClassVar[str] = "ASLAssay"
    class_model_uri: ClassVar[URIRef] = SOMA.ASLAssay

    id: Union[str, ASLAssayId] = None
    has_specified_output: Optional[Union[dict, "ASLOutput"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ASLAssayId):
            self.id = ASLAssayId(self.id)

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, ASLOutput):
            self.has_specified_output = ASLOutput(**as_dict(self.has_specified_output))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ASLOutput(AssayOutputMeasurement):
    """
    Measurement results from an airway surface liquid assay. Contains the measured values for ASL height, periciliary
    layer depth, and ion composition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["ASLOutput"]
    class_class_curie: ClassVar[str] = "assay_microschemas:ASLOutput"
    class_name: ClassVar[str] = "ASLOutput"
    class_model_uri: ClassVar[URIRef] = SOMA.ASLOutput

    id: Union[str, ASLOutputId] = None
    asl_height_um: Optional[Union[dict, QuantityValue]] = None
    periciliary_layer_depth: Optional[Union[dict, QuantityValue]] = None
    mucus_layer_thickness: Optional[Union[dict, QuantityValue]] = None
    ion_composition: Optional[str] = None
    asl_ph: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ASLOutputId):
            self.id = ASLOutputId(self.id)

        if self.asl_height_um is not None and not isinstance(self.asl_height_um, QuantityValue):
            self.asl_height_um = QuantityValue(**as_dict(self.asl_height_um))

        if self.periciliary_layer_depth is not None and not isinstance(self.periciliary_layer_depth, QuantityValue):
            self.periciliary_layer_depth = QuantityValue(**as_dict(self.periciliary_layer_depth))

        if self.mucus_layer_thickness is not None and not isinstance(self.mucus_layer_thickness, QuantityValue):
            self.mucus_layer_thickness = QuantityValue(**as_dict(self.mucus_layer_thickness))

        if self.ion_composition is not None and not isinstance(self.ion_composition, str):
            self.ion_composition = str(self.ion_composition)

        if self.asl_ph is not None and not isinstance(self.asl_ph, QuantityValue):
            self.asl_ph = QuantityValue(**as_dict(self.asl_ph))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MucociliaryClearanceAssay(Assay):
    """
    Assay for measuring mucociliary clearance and transport. Informs on Key Event: "Impaired mucociliary clearance" in
    respiratory AOPs. TIER 1 slots (critical): transport_rate, directionality.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["MucociliaryClearanceAssay"]
    class_class_curie: ClassVar[str] = "assay_microschemas:MucociliaryClearanceAssay"
    class_name: ClassVar[str] = "MucociliaryClearanceAssay"
    class_model_uri: ClassVar[URIRef] = SOMA.MucociliaryClearanceAssay

    id: Union[str, MucociliaryClearanceAssayId] = None
    mucus_composition: Optional[str] = None
    has_specified_output: Optional[Union[dict, "MucociliaryClearanceOutput"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MucociliaryClearanceAssayId):
            self.id = MucociliaryClearanceAssayId(self.id)

        if self.mucus_composition is not None and not isinstance(self.mucus_composition, str):
            self.mucus_composition = str(self.mucus_composition)

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, MucociliaryClearanceOutput):
            self.has_specified_output = MucociliaryClearanceOutput(**as_dict(self.has_specified_output))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MucociliaryClearanceOutput(AssayOutputMeasurement):
    """
    Measurement results from a mucociliary clearance assay. Contains the measured values for transport rate,
    directionality, and clearance metrics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["MucociliaryClearanceOutput"]
    class_class_curie: ClassVar[str] = "assay_microschemas:MucociliaryClearanceOutput"
    class_name: ClassVar[str] = "MucociliaryClearanceOutput"
    class_model_uri: ClassVar[URIRef] = SOMA.MucociliaryClearanceOutput

    id: Union[str, MucociliaryClearanceOutputId] = None
    transport_rate: Optional[Union[dict, QuantityValue]] = None
    transport_directionality: Optional[Union[str, "DirectionalityEnum"]] = None
    mucus_layer_thickness: Optional[Union[dict, QuantityValue]] = None
    percentage_active_transport: Optional[Union[dict, QuantityValue]] = None
    particle_clearance_time: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MucociliaryClearanceOutputId):
            self.id = MucociliaryClearanceOutputId(self.id)

        if self.transport_rate is not None and not isinstance(self.transport_rate, QuantityValue):
            self.transport_rate = QuantityValue(**as_dict(self.transport_rate))

        if self.transport_directionality is not None and not isinstance(self.transport_directionality, DirectionalityEnum):
            self.transport_directionality = DirectionalityEnum(self.transport_directionality)

        if self.mucus_layer_thickness is not None and not isinstance(self.mucus_layer_thickness, QuantityValue):
            self.mucus_layer_thickness = QuantityValue(**as_dict(self.mucus_layer_thickness))

        if self.percentage_active_transport is not None and not isinstance(self.percentage_active_transport, QuantityValue):
            self.percentage_active_transport = QuantityValue(**as_dict(self.percentage_active_transport))

        if self.particle_clearance_time is not None and not isinstance(self.particle_clearance_time, QuantityValue):
            self.particle_clearance_time = QuantityValue(**as_dict(self.particle_clearance_time))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OxidativeStressAssay(Assay):
    """
    Assay for measuring oxidative stress markers. Informs on Key Event: "Increased oxidative stress" - often a
    Molecular Initiating Event (MIE) in respiratory toxicology AOPs. TIER 1 slots (critical): All surrogate markers
    for oxidative stress. Multiple detection methods expected - no single "best" for lung function.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["OxidativeStressAssay"]
    class_class_curie: ClassVar[str] = "assay_microschemas:OxidativeStressAssay"
    class_name: ClassVar[str] = "OxidativeStressAssay"
    class_model_uri: ClassVar[URIRef] = SOMA.OxidativeStressAssay

    id: Union[str, OxidativeStressAssayId] = None
    ros_probe_type: Optional[str] = None
    has_specified_output: Optional[Union[dict, "OxidativeStressOutput"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OxidativeStressAssayId):
            self.id = OxidativeStressAssayId(self.id)

        if self.ros_probe_type is not None and not isinstance(self.ros_probe_type, str):
            self.ros_probe_type = str(self.ros_probe_type)

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, OxidativeStressOutput):
            self.has_specified_output = OxidativeStressOutput(**as_dict(self.has_specified_output))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OxidativeStressOutput(AssayOutputMeasurement):
    """
    Measurement results from an oxidative stress assay. Contains all surrogate markers for oxidative stress including
    ROS levels, lipid peroxidation, protein oxidation, DNA damage, and antioxidant capacity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["OxidativeStressOutput"]
    class_class_curie: ClassVar[str] = "assay_microschemas:OxidativeStressOutput"
    class_name: ClassVar[str] = "OxidativeStressOutput"
    class_model_uri: ClassVar[URIRef] = SOMA.OxidativeStressOutput

    id: Union[str, OxidativeStressOutputId] = None
    reactive_oxygen_species: Optional[Union[dict, QuantityValue]] = None
    lipid_peroxidation: Optional[Union[dict, QuantityValue]] = None
    malondialdehyde_level: Optional[Union[dict, QuantityValue]] = None
    four_hydroxynonenal_level: Optional[Union[dict, QuantityValue]] = None
    eight_isoprostane_level: Optional[Union[dict, QuantityValue]] = None
    protein_oxidation_markers: Optional[Union[str, list[str]]] = empty_list()
    protein_carbonyl_content: Optional[Union[dict, QuantityValue]] = None
    nitrotyrosine_level: Optional[Union[dict, QuantityValue]] = None
    dna_damage_markers: Optional[Union[dict, QuantityValue]] = None
    eight_ohdg_level: Optional[Union[dict, QuantityValue]] = None
    antioxidant_capacity: Optional[Union[dict, QuantityValue]] = None
    glutathione_ratio: Optional[Union[dict, QuantityValue]] = None
    antioxidant_enzyme_activities: Optional[str] = None
    superoxide_dismutase_activity: Optional[Union[dict, QuantityValue]] = None
    catalase_activity: Optional[Union[dict, QuantityValue]] = None
    glutathione_peroxidase_activity: Optional[Union[dict, QuantityValue]] = None
    total_antioxidant_capacity: Optional[Union[dict, QuantityValue]] = None
    nrf2_activation: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OxidativeStressOutputId):
            self.id = OxidativeStressOutputId(self.id)

        if self.reactive_oxygen_species is not None and not isinstance(self.reactive_oxygen_species, QuantityValue):
            self.reactive_oxygen_species = QuantityValue(**as_dict(self.reactive_oxygen_species))

        if self.lipid_peroxidation is not None and not isinstance(self.lipid_peroxidation, QuantityValue):
            self.lipid_peroxidation = QuantityValue(**as_dict(self.lipid_peroxidation))

        if self.malondialdehyde_level is not None and not isinstance(self.malondialdehyde_level, QuantityValue):
            self.malondialdehyde_level = QuantityValue(**as_dict(self.malondialdehyde_level))

        if self.four_hydroxynonenal_level is not None and not isinstance(self.four_hydroxynonenal_level, QuantityValue):
            self.four_hydroxynonenal_level = QuantityValue(**as_dict(self.four_hydroxynonenal_level))

        if self.eight_isoprostane_level is not None and not isinstance(self.eight_isoprostane_level, QuantityValue):
            self.eight_isoprostane_level = QuantityValue(**as_dict(self.eight_isoprostane_level))

        if not isinstance(self.protein_oxidation_markers, list):
            self.protein_oxidation_markers = [self.protein_oxidation_markers] if self.protein_oxidation_markers is not None else []
        self.protein_oxidation_markers = [v if isinstance(v, str) else str(v) for v in self.protein_oxidation_markers]

        if self.protein_carbonyl_content is not None and not isinstance(self.protein_carbonyl_content, QuantityValue):
            self.protein_carbonyl_content = QuantityValue(**as_dict(self.protein_carbonyl_content))

        if self.nitrotyrosine_level is not None and not isinstance(self.nitrotyrosine_level, QuantityValue):
            self.nitrotyrosine_level = QuantityValue(**as_dict(self.nitrotyrosine_level))

        if self.dna_damage_markers is not None and not isinstance(self.dna_damage_markers, QuantityValue):
            self.dna_damage_markers = QuantityValue(**as_dict(self.dna_damage_markers))

        if self.eight_ohdg_level is not None and not isinstance(self.eight_ohdg_level, QuantityValue):
            self.eight_ohdg_level = QuantityValue(**as_dict(self.eight_ohdg_level))

        if self.antioxidant_capacity is not None and not isinstance(self.antioxidant_capacity, QuantityValue):
            self.antioxidant_capacity = QuantityValue(**as_dict(self.antioxidant_capacity))

        if self.glutathione_ratio is not None and not isinstance(self.glutathione_ratio, QuantityValue):
            self.glutathione_ratio = QuantityValue(**as_dict(self.glutathione_ratio))

        if self.antioxidant_enzyme_activities is not None and not isinstance(self.antioxidant_enzyme_activities, str):
            self.antioxidant_enzyme_activities = str(self.antioxidant_enzyme_activities)

        if self.superoxide_dismutase_activity is not None and not isinstance(self.superoxide_dismutase_activity, QuantityValue):
            self.superoxide_dismutase_activity = QuantityValue(**as_dict(self.superoxide_dismutase_activity))

        if self.catalase_activity is not None and not isinstance(self.catalase_activity, QuantityValue):
            self.catalase_activity = QuantityValue(**as_dict(self.catalase_activity))

        if self.glutathione_peroxidase_activity is not None and not isinstance(self.glutathione_peroxidase_activity, QuantityValue):
            self.glutathione_peroxidase_activity = QuantityValue(**as_dict(self.glutathione_peroxidase_activity))

        if self.total_antioxidant_capacity is not None and not isinstance(self.total_antioxidant_capacity, QuantityValue):
            self.total_antioxidant_capacity = QuantityValue(**as_dict(self.total_antioxidant_capacity))

        if self.nrf2_activation is not None and not isinstance(self.nrf2_activation, QuantityValue):
            self.nrf2_activation = QuantityValue(**as_dict(self.nrf2_activation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CFTRFunctionAssay(Assay):
    """
    Assay for measuring CFTR (Cystic Fibrosis Transmembrane Conductance Regulator) function. Informs on Key Event:
    "Decreased CFTR function" in cystic fibrosis-related AOPs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["CFTRFunctionAssay"]
    class_class_curie: ClassVar[str] = "assay_microschemas:CFTRFunctionAssay"
    class_name: ClassVar[str] = "CFTRFunctionAssay"
    class_model_uri: ClassVar[URIRef] = SOMA.CFTRFunctionAssay

    id: Union[str, CFTRFunctionAssayId] = None
    stimulation_agent: Optional[str] = None
    inhibitor_used: Optional[str] = None
    has_specified_output: Optional[Union[dict, "CFTRFunctionOutput"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CFTRFunctionAssayId):
            self.id = CFTRFunctionAssayId(self.id)

        if self.stimulation_agent is not None and not isinstance(self.stimulation_agent, str):
            self.stimulation_agent = str(self.stimulation_agent)

        if self.inhibitor_used is not None and not isinstance(self.inhibitor_used, str):
            self.inhibitor_used = str(self.inhibitor_used)

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, CFTRFunctionOutput):
            self.has_specified_output = CFTRFunctionOutput(**as_dict(self.has_specified_output))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CFTRFunctionOutput(AssayOutputMeasurement):
    """
    Measurement results from a CFTR function assay. Contains the measured values for CFTR-mediated chloride secretion,
    forskolin response, and related electrophysiology measurements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["CFTRFunctionOutput"]
    class_class_curie: ClassVar[str] = "assay_microschemas:CFTRFunctionOutput"
    class_name: ClassVar[str] = "CFTRFunctionOutput"
    class_model_uri: ClassVar[URIRef] = SOMA.CFTRFunctionOutput

    id: Union[str, CFTRFunctionOutputId] = None
    cftr_chloride_secretion: Optional[Union[dict, QuantityValue]] = None
    cftr_forskolin_response: Optional[Union[dict, QuantityValue]] = None
    inhibitor_sensitive_current: Optional[Union[dict, QuantityValue]] = None
    cftr_specific_current: Optional[Union[dict, QuantityValue]] = None
    sweat_chloride_concentration: Optional[Union[dict, QuantityValue]] = None
    nasal_potential_difference: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CFTRFunctionOutputId):
            self.id = CFTRFunctionOutputId(self.id)

        if self.cftr_chloride_secretion is not None and not isinstance(self.cftr_chloride_secretion, QuantityValue):
            self.cftr_chloride_secretion = QuantityValue(**as_dict(self.cftr_chloride_secretion))

        if self.cftr_forskolin_response is not None and not isinstance(self.cftr_forskolin_response, QuantityValue):
            self.cftr_forskolin_response = QuantityValue(**as_dict(self.cftr_forskolin_response))

        if self.inhibitor_sensitive_current is not None and not isinstance(self.inhibitor_sensitive_current, QuantityValue):
            self.inhibitor_sensitive_current = QuantityValue(**as_dict(self.inhibitor_sensitive_current))

        if self.cftr_specific_current is not None and not isinstance(self.cftr_specific_current, QuantityValue):
            self.cftr_specific_current = QuantityValue(**as_dict(self.cftr_specific_current))

        if self.sweat_chloride_concentration is not None and not isinstance(self.sweat_chloride_concentration, QuantityValue):
            self.sweat_chloride_concentration = QuantityValue(**as_dict(self.sweat_chloride_concentration))

        if self.nasal_potential_difference is not None and not isinstance(self.nasal_potential_difference, QuantityValue):
            self.nasal_potential_difference = QuantityValue(**as_dict(self.nasal_potential_difference))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EGFRSignalingAssay(Assay):
    """
    Assay for measuring EGFR phosphorylation and downstream signaling. Informs on Key Event: "EGFR activation" in
    mucus hypersecretion AOPs.
    IMPORTANT: EGFR phosphorylation is the MOST SPECIFIC evidence for activation. Downstream kinase data alone is
    insufficient - needs phosphorylation measure OR inhibitor reversal for strong evidence. Cell type matters due to
    receptor location in ALI cultures.
    TIER 1 slots (critical): egfr_phosphorylation with site specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["EGFRSignalingAssay"]
    class_class_curie: ClassVar[str] = "assay_microschemas:EGFRSignalingAssay"
    class_name: ClassVar[str] = "EGFRSignalingAssay"
    class_model_uri: ClassVar[URIRef] = SOMA.EGFRSignalingAssay

    id: Union[str, EGFRSignalingAssayId] = None
    normalization_reference: Optional[str] = None
    phosphorylation_site: Optional[str] = None
    has_specified_output: Optional[Union[dict, "EGFRSignalingOutput"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EGFRSignalingAssayId):
            self.id = EGFRSignalingAssayId(self.id)

        if self.normalization_reference is not None and not isinstance(self.normalization_reference, str):
            self.normalization_reference = str(self.normalization_reference)

        if self.phosphorylation_site is not None and not isinstance(self.phosphorylation_site, str):
            self.phosphorylation_site = str(self.phosphorylation_site)

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, EGFRSignalingOutput):
            self.has_specified_output = EGFRSignalingOutput(**as_dict(self.has_specified_output))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EGFRSignalingOutput(AssayOutputMeasurement):
    """
    Measurement results from an EGFR signaling assay. Contains the measured values for EGFR phosphorylation, total
    protein, and downstream kinase activation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["EGFRSignalingOutput"]
    class_class_curie: ClassVar[str] = "assay_microschemas:EGFRSignalingOutput"
    class_name: ClassVar[str] = "EGFRSignalingOutput"
    class_model_uri: ClassVar[URIRef] = SOMA.EGFRSignalingOutput

    id: Union[str, EGFRSignalingOutputId] = None
    egfr_phosphorylation_y1068: Optional[Union[dict, QuantityValue]] = None
    egfr_phosphorylation_y1173: Optional[Union[dict, QuantityValue]] = None
    total_egfr_protein: Optional[Union[dict, QuantityValue]] = None
    downstream_kinase_activation: Optional[str] = None
    erk_phosphorylation: Optional[Union[dict, QuantityValue]] = None
    akt_phosphorylation: Optional[Union[dict, QuantityValue]] = None
    pathway_biomarkers: Optional[Union[str, list[str]]] = empty_list()
    egfr_ligand_expression: Optional[Union[dict, QuantityValue]] = None
    egfr_membrane_localization: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EGFRSignalingOutputId):
            self.id = EGFRSignalingOutputId(self.id)

        if self.egfr_phosphorylation_y1068 is not None and not isinstance(self.egfr_phosphorylation_y1068, QuantityValue):
            self.egfr_phosphorylation_y1068 = QuantityValue(**as_dict(self.egfr_phosphorylation_y1068))

        if self.egfr_phosphorylation_y1173 is not None and not isinstance(self.egfr_phosphorylation_y1173, QuantityValue):
            self.egfr_phosphorylation_y1173 = QuantityValue(**as_dict(self.egfr_phosphorylation_y1173))

        if self.total_egfr_protein is not None and not isinstance(self.total_egfr_protein, QuantityValue):
            self.total_egfr_protein = QuantityValue(**as_dict(self.total_egfr_protein))

        if self.downstream_kinase_activation is not None and not isinstance(self.downstream_kinase_activation, str):
            self.downstream_kinase_activation = str(self.downstream_kinase_activation)

        if self.erk_phosphorylation is not None and not isinstance(self.erk_phosphorylation, QuantityValue):
            self.erk_phosphorylation = QuantityValue(**as_dict(self.erk_phosphorylation))

        if self.akt_phosphorylation is not None and not isinstance(self.akt_phosphorylation, QuantityValue):
            self.akt_phosphorylation = QuantityValue(**as_dict(self.akt_phosphorylation))

        if not isinstance(self.pathway_biomarkers, list):
            self.pathway_biomarkers = [self.pathway_biomarkers] if self.pathway_biomarkers is not None else []
        self.pathway_biomarkers = [v if isinstance(v, str) else str(v) for v in self.pathway_biomarkers]

        if self.egfr_ligand_expression is not None and not isinstance(self.egfr_ligand_expression, QuantityValue):
            self.egfr_ligand_expression = QuantityValue(**as_dict(self.egfr_ligand_expression))

        if self.egfr_membrane_localization is not None and not isinstance(self.egfr_membrane_localization, QuantityValue):
            self.egfr_membrane_localization = QuantityValue(**as_dict(self.egfr_membrane_localization))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GobletCellAssay(Assay):
    """
    Assay for measuring goblet cell populations and mucin production. Informs on Key Event: "Goblet cell hyperplasia"
    or "Mucin hypersecretion".
    IMPORTANT per domain feedback: Need BOTH cell counts AND mucin secretion measurements - cells may stay same but
    secretion changes. AB-PAS staining common for visualizing goblet cells. Some secreted mucins not tethered to
    goblet cells.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["GobletCellAssay"]
    class_class_curie: ClassVar[str] = "assay_microschemas:GobletCellAssay"
    class_name: ClassVar[str] = "GobletCellAssay"
    class_model_uri: ClassVar[URIRef] = SOMA.GobletCellAssay

    id: Union[str, GobletCellAssayId] = None
    has_specified_output: Optional[Union[dict, "GobletCellOutput"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GobletCellAssayId):
            self.id = GobletCellAssayId(self.id)

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, GobletCellOutput):
            self.has_specified_output = GobletCellOutput(**as_dict(self.has_specified_output))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GobletCellOutput(AssayOutputMeasurement):
    """
    Measurement results from a goblet cell assay. Contains the measured values for goblet cell counts, mucin
    expression, and mucus properties.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["GobletCellOutput"]
    class_class_curie: ClassVar[str] = "assay_microschemas:GobletCellOutput"
    class_name: ClassVar[str] = "GobletCellOutput"
    class_model_uri: ClassVar[URIRef] = SOMA.GobletCellOutput

    id: Union[str, GobletCellOutputId] = None
    goblet_cell_count: Optional[Union[dict, QuantityValue]] = None
    goblet_cell_percentage: Optional[Union[dict, QuantityValue]] = None
    muc5ac_mrna_expression: Optional[Union[dict, QuantityValue]] = None
    muc5ac_protein_expression: Optional[Union[dict, QuantityValue]] = None
    muc5b_mrna_expression: Optional[Union[dict, QuantityValue]] = None
    muc5b_protein_expression: Optional[Union[dict, QuantityValue]] = None
    muc5ac_muc5b_ratio: Optional[Union[dict, QuantityValue]] = None
    mucin_protein_concentration: Optional[Union[dict, QuantityValue]] = None
    mucin_secretion_rate: Optional[Union[dict, QuantityValue]] = None
    percent_solids: Optional[Union[dict, QuantityValue]] = None
    goblet_to_ciliated_ratio: Optional[Union[dict, QuantityValue]] = None
    mucus_viscosity: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GobletCellOutputId):
            self.id = GobletCellOutputId(self.id)

        if self.goblet_cell_count is not None and not isinstance(self.goblet_cell_count, QuantityValue):
            self.goblet_cell_count = QuantityValue(**as_dict(self.goblet_cell_count))

        if self.goblet_cell_percentage is not None and not isinstance(self.goblet_cell_percentage, QuantityValue):
            self.goblet_cell_percentage = QuantityValue(**as_dict(self.goblet_cell_percentage))

        if self.muc5ac_mrna_expression is not None and not isinstance(self.muc5ac_mrna_expression, QuantityValue):
            self.muc5ac_mrna_expression = QuantityValue(**as_dict(self.muc5ac_mrna_expression))

        if self.muc5ac_protein_expression is not None and not isinstance(self.muc5ac_protein_expression, QuantityValue):
            self.muc5ac_protein_expression = QuantityValue(**as_dict(self.muc5ac_protein_expression))

        if self.muc5b_mrna_expression is not None and not isinstance(self.muc5b_mrna_expression, QuantityValue):
            self.muc5b_mrna_expression = QuantityValue(**as_dict(self.muc5b_mrna_expression))

        if self.muc5b_protein_expression is not None and not isinstance(self.muc5b_protein_expression, QuantityValue):
            self.muc5b_protein_expression = QuantityValue(**as_dict(self.muc5b_protein_expression))

        if self.muc5ac_muc5b_ratio is not None and not isinstance(self.muc5ac_muc5b_ratio, QuantityValue):
            self.muc5ac_muc5b_ratio = QuantityValue(**as_dict(self.muc5ac_muc5b_ratio))

        if self.mucin_protein_concentration is not None and not isinstance(self.mucin_protein_concentration, QuantityValue):
            self.mucin_protein_concentration = QuantityValue(**as_dict(self.mucin_protein_concentration))

        if self.mucin_secretion_rate is not None and not isinstance(self.mucin_secretion_rate, QuantityValue):
            self.mucin_secretion_rate = QuantityValue(**as_dict(self.mucin_secretion_rate))

        if self.percent_solids is not None and not isinstance(self.percent_solids, QuantityValue):
            self.percent_solids = QuantityValue(**as_dict(self.percent_solids))

        if self.goblet_to_ciliated_ratio is not None and not isinstance(self.goblet_to_ciliated_ratio, QuantityValue):
            self.goblet_to_ciliated_ratio = QuantityValue(**as_dict(self.goblet_to_ciliated_ratio))

        if self.mucus_viscosity is not None and not isinstance(self.mucus_viscosity, QuantityValue):
            self.mucus_viscosity = QuantityValue(**as_dict(self.mucus_viscosity))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BALFSputumAssay(Assay):
    """
    Assay for measuring bronchoalveolar lavage fluid (BALF) or sputum composition. Informs on Key Event: "Airway
    inflammation" and provides evidence for inflammatory cell populations and cytokine levels.
    This assay is IN VIVO ONLY - requires samples from human or animal subjects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["BALFSputumAssay"]
    class_class_curie: ClassVar[str] = "assay_microschemas:BALFSputumAssay"
    class_name: ClassVar[str] = "BALFSputumAssay"
    class_model_uri: ClassVar[URIRef] = SOMA.BALFSputumAssay

    id: Union[str, BALFSputumAssayId] = None
    target_cell_type: Optional[Union[dict, CellTypeReference]] = None
    study_subject: Optional[Union[dict, InVivoSubject]] = None
    has_specified_output: Optional[Union[dict, "BALFSputumOutput"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BALFSputumAssayId):
            self.id = BALFSputumAssayId(self.id)

        if self.target_cell_type is not None and not isinstance(self.target_cell_type, CellTypeReference):
            self.target_cell_type = CellTypeReference(**as_dict(self.target_cell_type))

        if self.study_subject is not None and not isinstance(self.study_subject, InVivoSubject):
            self.study_subject = InVivoSubject(**as_dict(self.study_subject))

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, BALFSputumOutput):
            self.has_specified_output = BALFSputumOutput(**as_dict(self.has_specified_output))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BALFSputumOutput(AssayOutputMeasurement):
    """
    Measurement results from a BALF/sputum assay. Contains inflammatory cell differentials, cytokine concentrations,
    and microbiome metrics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["BALFSputumOutput"]
    class_class_curie: ClassVar[str] = "assay_microschemas:BALFSputumOutput"
    class_name: ClassVar[str] = "BALFSputumOutput"
    class_model_uri: ClassVar[URIRef] = SOMA.BALFSputumOutput

    id: Union[str, BALFSputumOutputId] = None
    neutrophil_percentage: Optional[Union[dict, QuantityValue]] = None
    eosinophil_percentage: Optional[Union[dict, QuantityValue]] = None
    macrophage_percentage: Optional[Union[dict, QuantityValue]] = None
    lymphocyte_percentage: Optional[Union[dict, QuantityValue]] = None
    total_cell_count: Optional[Union[dict, QuantityValue]] = None
    il6_concentration: Optional[Union[dict, QuantityValue]] = None
    il8_concentration: Optional[Union[dict, QuantityValue]] = None
    tnf_alpha_concentration: Optional[Union[dict, QuantityValue]] = None
    il1_beta_concentration: Optional[Union[dict, QuantityValue]] = None
    total_protein_concentration: Optional[Union[dict, QuantityValue]] = None
    alpha_diversity: Optional[Union[dict, QuantityValue]] = None
    beta_diversity: Optional[Union[dict, QuantityValue]] = None
    bacterial_load: Optional[Union[dict, QuantityValue]] = None
    cell_free_dna: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BALFSputumOutputId):
            self.id = BALFSputumOutputId(self.id)

        if self.neutrophil_percentage is not None and not isinstance(self.neutrophil_percentage, QuantityValue):
            self.neutrophil_percentage = QuantityValue(**as_dict(self.neutrophil_percentage))

        if self.eosinophil_percentage is not None and not isinstance(self.eosinophil_percentage, QuantityValue):
            self.eosinophil_percentage = QuantityValue(**as_dict(self.eosinophil_percentage))

        if self.macrophage_percentage is not None and not isinstance(self.macrophage_percentage, QuantityValue):
            self.macrophage_percentage = QuantityValue(**as_dict(self.macrophage_percentage))

        if self.lymphocyte_percentage is not None and not isinstance(self.lymphocyte_percentage, QuantityValue):
            self.lymphocyte_percentage = QuantityValue(**as_dict(self.lymphocyte_percentage))

        if self.total_cell_count is not None and not isinstance(self.total_cell_count, QuantityValue):
            self.total_cell_count = QuantityValue(**as_dict(self.total_cell_count))

        if self.il6_concentration is not None and not isinstance(self.il6_concentration, QuantityValue):
            self.il6_concentration = QuantityValue(**as_dict(self.il6_concentration))

        if self.il8_concentration is not None and not isinstance(self.il8_concentration, QuantityValue):
            self.il8_concentration = QuantityValue(**as_dict(self.il8_concentration))

        if self.tnf_alpha_concentration is not None and not isinstance(self.tnf_alpha_concentration, QuantityValue):
            self.tnf_alpha_concentration = QuantityValue(**as_dict(self.tnf_alpha_concentration))

        if self.il1_beta_concentration is not None and not isinstance(self.il1_beta_concentration, QuantityValue):
            self.il1_beta_concentration = QuantityValue(**as_dict(self.il1_beta_concentration))

        if self.total_protein_concentration is not None and not isinstance(self.total_protein_concentration, QuantityValue):
            self.total_protein_concentration = QuantityValue(**as_dict(self.total_protein_concentration))

        if self.alpha_diversity is not None and not isinstance(self.alpha_diversity, QuantityValue):
            self.alpha_diversity = QuantityValue(**as_dict(self.alpha_diversity))

        if self.beta_diversity is not None and not isinstance(self.beta_diversity, QuantityValue):
            self.beta_diversity = QuantityValue(**as_dict(self.beta_diversity))

        if self.bacterial_load is not None and not isinstance(self.bacterial_load, QuantityValue):
            self.bacterial_load = QuantityValue(**as_dict(self.bacterial_load))

        if self.cell_free_dna is not None and not isinstance(self.cell_free_dna, QuantityValue):
            self.cell_free_dna = QuantityValue(**as_dict(self.cell_free_dna))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LungFunctionAssay(Assay):
    """
    Clinical assay for measuring lung function. Informs on Adverse Outcome: "Decreased lung function" - the composite
    clinical outcome.
    IMPORTANT per domain feedback: - Subject characteristics (sex, species, age, height) are critical -
    often reported as % of predicted baseline
    - Reference dataset (GLI-2012 for humans) is essential for interpretation - Hemoglobin levels pair with DLCO
    measurements - Recent respiratory illness affects spirometry results
    TIER 1 slots (critical): fev1, fvc, subject_characteristics, reference_dataset. This assay is IN VIVO ONLY.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["LungFunctionAssay"]
    class_class_curie: ClassVar[str] = "assay_microschemas:LungFunctionAssay"
    class_name: ClassVar[str] = "LungFunctionAssay"
    class_model_uri: ClassVar[URIRef] = SOMA.LungFunctionAssay

    id: Union[str, LungFunctionAssayId] = None
    reference_dataset: Optional[str] = None
    hemoglobin_level: Optional[Union[dict, QuantityValue]] = None
    recent_respiratory_illness: Optional[str] = None
    study_subject: Optional[Union[dict, InVivoSubject]] = None
    has_specified_output: Optional[Union[dict, "LungFunctionOutput"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LungFunctionAssayId):
            self.id = LungFunctionAssayId(self.id)

        if self.reference_dataset is not None and not isinstance(self.reference_dataset, str):
            self.reference_dataset = str(self.reference_dataset)

        if self.hemoglobin_level is not None and not isinstance(self.hemoglobin_level, QuantityValue):
            self.hemoglobin_level = QuantityValue(**as_dict(self.hemoglobin_level))

        if self.recent_respiratory_illness is not None and not isinstance(self.recent_respiratory_illness, str):
            self.recent_respiratory_illness = str(self.recent_respiratory_illness)

        if self.study_subject is not None and not isinstance(self.study_subject, InVivoSubject):
            self.study_subject = InVivoSubject(**as_dict(self.study_subject))

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, LungFunctionOutput):
            self.has_specified_output = LungFunctionOutput(**as_dict(self.has_specified_output))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LungFunctionOutput(AssayOutputMeasurement):
    """
    Measurement results from a lung function assay. Contains spirometry measurements, diffusing capacity, and related
    clinical metrics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["LungFunctionOutput"]
    class_class_curie: ClassVar[str] = "assay_microschemas:LungFunctionOutput"
    class_name: ClassVar[str] = "LungFunctionOutput"
    class_model_uri: ClassVar[URIRef] = SOMA.LungFunctionOutput

    id: Union[str, LungFunctionOutputId] = None
    fev1: Optional[Union[dict, QuantityValue]] = None
    fvc: Optional[Union[dict, QuantityValue]] = None
    fev1_fvc_ratio: Optional[Union[dict, QuantityValue]] = None
    feno: Optional[Union[dict, QuantityValue]] = None
    decline_rate: Optional[Union[dict, QuantityValue]] = None
    bronchodilator_response: Optional[Union[dict, QuantityValue]] = None
    dlco: Optional[Union[dict, QuantityValue]] = None
    peak_expiratory_flow: Optional[Union[dict, QuantityValue]] = None
    fef25_75: Optional[Union[dict, QuantityValue]] = None
    total_lung_capacity: Optional[Union[dict, QuantityValue]] = None
    functional_residual_capacity: Optional[Union[dict, QuantityValue]] = None
    residual_volume: Optional[Union[dict, QuantityValue]] = None
    lung_compliance: Optional[Union[dict, QuantityValue]] = None
    lung_elastance: Optional[Union[dict, QuantityValue]] = None
    lung_resistance: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LungFunctionOutputId):
            self.id = LungFunctionOutputId(self.id)

        if self.fev1 is not None and not isinstance(self.fev1, QuantityValue):
            self.fev1 = QuantityValue(**as_dict(self.fev1))

        if self.fvc is not None and not isinstance(self.fvc, QuantityValue):
            self.fvc = QuantityValue(**as_dict(self.fvc))

        if self.fev1_fvc_ratio is not None and not isinstance(self.fev1_fvc_ratio, QuantityValue):
            self.fev1_fvc_ratio = QuantityValue(**as_dict(self.fev1_fvc_ratio))

        if self.feno is not None and not isinstance(self.feno, QuantityValue):
            self.feno = QuantityValue(**as_dict(self.feno))

        if self.decline_rate is not None and not isinstance(self.decline_rate, QuantityValue):
            self.decline_rate = QuantityValue(**as_dict(self.decline_rate))

        if self.bronchodilator_response is not None and not isinstance(self.bronchodilator_response, QuantityValue):
            self.bronchodilator_response = QuantityValue(**as_dict(self.bronchodilator_response))

        if self.dlco is not None and not isinstance(self.dlco, QuantityValue):
            self.dlco = QuantityValue(**as_dict(self.dlco))

        if self.peak_expiratory_flow is not None and not isinstance(self.peak_expiratory_flow, QuantityValue):
            self.peak_expiratory_flow = QuantityValue(**as_dict(self.peak_expiratory_flow))

        if self.fef25_75 is not None and not isinstance(self.fef25_75, QuantityValue):
            self.fef25_75 = QuantityValue(**as_dict(self.fef25_75))

        if self.total_lung_capacity is not None and not isinstance(self.total_lung_capacity, QuantityValue):
            self.total_lung_capacity = QuantityValue(**as_dict(self.total_lung_capacity))

        if self.functional_residual_capacity is not None and not isinstance(self.functional_residual_capacity, QuantityValue):
            self.functional_residual_capacity = QuantityValue(**as_dict(self.functional_residual_capacity))

        if self.residual_volume is not None and not isinstance(self.residual_volume, QuantityValue):
            self.residual_volume = QuantityValue(**as_dict(self.residual_volume))

        if self.lung_compliance is not None and not isinstance(self.lung_compliance, QuantityValue):
            self.lung_compliance = QuantityValue(**as_dict(self.lung_compliance))

        if self.lung_elastance is not None and not isinstance(self.lung_elastance, QuantityValue):
            self.lung_elastance = QuantityValue(**as_dict(self.lung_elastance))

        if self.lung_resistance is not None and not isinstance(self.lung_resistance, QuantityValue):
            self.lung_resistance = QuantityValue(**as_dict(self.lung_resistance))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FoxJExpressionAssay(Assay):
    """
    Assay for measuring FoxJ1 expression related to ciliogenesis. Informs on Key Event: "Altered ciliogenesis" in
    respiratory AOPs. FoxJ1 is a master transcription factor for motile cilia.
    This assay is primarily IN VITRO focused.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["FoxJExpressionAssay"]
    class_class_curie: ClassVar[str] = "assay_microschemas:FoxJExpressionAssay"
    class_name: ClassVar[str] = "FoxJExpressionAssay"
    class_model_uri: ClassVar[URIRef] = SOMA.FoxJExpressionAssay

    id: Union[str, FoxJExpressionAssayId] = None
    has_specified_output: Optional[Union[dict, "FoxJExpressionOutput"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoxJExpressionAssayId):
            self.id = FoxJExpressionAssayId(self.id)

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, FoxJExpressionOutput):
            self.has_specified_output = FoxJExpressionOutput(**as_dict(self.has_specified_output))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FoxJExpressionOutput(AssayOutputMeasurement):
    """
    Measurement results from a FoxJ1 expression assay. Contains the measured values for FoxJ1 mRNA, protein, and
    cellular localization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["FoxJExpressionOutput"]
    class_class_curie: ClassVar[str] = "assay_microschemas:FoxJExpressionOutput"
    class_name: ClassVar[str] = "FoxJExpressionOutput"
    class_model_uri: ClassVar[URIRef] = SOMA.FoxJExpressionOutput

    id: Union[str, FoxJExpressionOutputId] = None
    foxj1_mrna_expression: Optional[Union[dict, QuantityValue]] = None
    foxj1_protein_expression: Optional[Union[dict, QuantityValue]] = None
    foxj1_positive_cell_percentage: Optional[Union[dict, QuantityValue]] = None
    foxj1_nuclear_localization: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoxJExpressionOutputId):
            self.id = FoxJExpressionOutputId(self.id)

        if self.foxj1_mrna_expression is not None and not isinstance(self.foxj1_mrna_expression, QuantityValue):
            self.foxj1_mrna_expression = QuantityValue(**as_dict(self.foxj1_mrna_expression))

        if self.foxj1_protein_expression is not None and not isinstance(self.foxj1_protein_expression, QuantityValue):
            self.foxj1_protein_expression = QuantityValue(**as_dict(self.foxj1_protein_expression))

        if self.foxj1_positive_cell_percentage is not None and not isinstance(self.foxj1_positive_cell_percentage, QuantityValue):
            self.foxj1_positive_cell_percentage = QuantityValue(**as_dict(self.foxj1_positive_cell_percentage))

        if self.foxj1_nuclear_localization is not None and not isinstance(self.foxj1_nuclear_localization, QuantityValue):
            self.foxj1_nuclear_localization = QuantityValue(**as_dict(self.foxj1_nuclear_localization))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneExpressionAssay(Assay):
    """
    General assay for gene expression measurements. Renamed from TranscriptionFactorExpressionMeasurement per domain
    feedback - gene expression is more commonly the primary output.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["GeneExpressionAssay"]
    class_class_curie: ClassVar[str] = "assay_microschemas:GeneExpressionAssay"
    class_name: ClassVar[str] = "GeneExpressionAssay"
    class_model_uri: ClassVar[URIRef] = SOMA.GeneExpressionAssay

    id: Union[str, GeneExpressionAssayId] = None
    target_gene: Optional[Union[str, URIorCURIE]] = None
    gene_expression_method: Optional[str] = None
    normalization_reference: Optional[str] = None
    has_specified_output: Optional[Union[dict, "GeneExpressionOutput"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneExpressionAssayId):
            self.id = GeneExpressionAssayId(self.id)

        if self.target_gene is not None and not isinstance(self.target_gene, URIorCURIE):
            self.target_gene = URIorCURIE(self.target_gene)

        if self.gene_expression_method is not None and not isinstance(self.gene_expression_method, str):
            self.gene_expression_method = str(self.gene_expression_method)

        if self.normalization_reference is not None and not isinstance(self.normalization_reference, str):
            self.normalization_reference = str(self.normalization_reference)

        if self.has_specified_output is not None and not isinstance(self.has_specified_output, GeneExpressionOutput):
            self.has_specified_output = GeneExpressionOutput(**as_dict(self.has_specified_output))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneExpressionOutput(AssayOutputMeasurement):
    """
    Measurement results from a gene expression assay. Contains the measured values for mRNA level, protein level, and
    positive cell percentage.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ASSAY_MICROSCHEMAS["GeneExpressionOutput"]
    class_class_curie: ClassVar[str] = "assay_microschemas:GeneExpressionOutput"
    class_name: ClassVar[str] = "GeneExpressionOutput"
    class_model_uri: ClassVar[URIRef] = SOMA.GeneExpressionOutput

    id: Union[str, GeneExpressionOutputId] = None
    mrna_level: Optional[Union[dict, QuantityValue]] = None
    protein_level: Optional[Union[dict, QuantityValue]] = None
    percentage_positive_cells: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneExpressionOutputId):
            self.id = GeneExpressionOutputId(self.id)

        if self.mrna_level is not None and not isinstance(self.mrna_level, QuantityValue):
            self.mrna_level = QuantityValue(**as_dict(self.mrna_level))

        if self.protein_level is not None and not isinstance(self.protein_level, QuantityValue):
            self.protein_level = QuantityValue(**as_dict(self.protein_level))

        if self.percentage_positive_cells is not None and not isinstance(self.percentage_positive_cells, QuantityValue):
            self.percentage_positive_cells = QuantityValue(**as_dict(self.percentage_positive_cells))

        super().__post_init__(**kwargs)


# Enumerations
class BiologicalActionEnum(EnumDefinitionImpl):
    """
    Types of biological changes or actions in key events.
    """
    increased = PermissibleValue(
        text="increased",
        description="Increased level or activity")
    decreased = PermissibleValue(
        text="decreased",
        description="Decreased level or activity")
    altered = PermissibleValue(
        text="altered",
        description="Altered function or state (not quantitative)")
    impaired = PermissibleValue(
        text="impaired",
        description="Impaired function")
    disrupted = PermissibleValue(
        text="disrupted",
        description="Disrupted process or structure")
    activated = PermissibleValue(
        text="activated",
        description="Activated process or pathway")
    inhibited = PermissibleValue(
        text="inhibited",
        description="Inhibited process or pathway")

    _defn = EnumDefinition(
        name="BiologicalActionEnum",
        description="Types of biological changes or actions in key events.",
    )

class BiologicalOrganizationLevelEnum(EnumDefinitionImpl):
    """
    Levels of biological organization for key events.
    """
    molecular = PermissibleValue(
        text="molecular",
        description="Molecular level (genes, proteins, metabolites)")
    cellular = PermissibleValue(
        text="cellular",
        description="Cellular level (cell function, signaling)")
    tissue = PermissibleValue(
        text="tissue",
        description="Tissue level (tissue structure, function)")
    organ = PermissibleValue(
        text="organ",
        description="Organ level (organ function)")
    organism = PermissibleValue(
        text="organism",
        description="Whole organism level (systemic effects)")
    population = PermissibleValue(
        text="population",
        description="Population level (ecological effects)")

    _defn = EnumDefinition(
        name="BiologicalOrganizationLevelEnum",
        description="Levels of biological organization for key events.",
    )

class EvidenceSupportEnum(EnumDefinitionImpl):
    """
    Levels of evidence support for key event relationships.
    """
    strong = PermissibleValue(
        text="strong",
        description="Strong empirical support with mechanistic understanding")
    moderate = PermissibleValue(
        text="moderate",
        description="Moderate support with some mechanistic evidence")
    weak = PermissibleValue(
        text="weak",
        description="Limited evidence or indirect support")
    not_specified = PermissibleValue(
        text="not_specified",
        description="Evidence level not specified")

    _defn = EnumDefinition(
        name="EvidenceSupportEnum",
        description="Levels of evidence support for key event relationships.",
    )

class QuantitativeUnderstandingEnum(EnumDefinitionImpl):
    """
    Levels of quantitative understanding for key event relationships.
    """
    high = PermissibleValue(
        text="high",
        description="Response-response relationship well characterized")
    moderate = PermissibleValue(
        text="moderate",
        description="Some quantitative data available")
    low = PermissibleValue(
        text="low",
        description="Limited quantitative understanding")
    not_specified = PermissibleValue(
        text="not_specified",
        description="Quantitative understanding not specified")

    _defn = EnumDefinition(
        name="QuantitativeUnderstandingEnum",
        description="Levels of quantitative understanding for key event relationships.",
    )

class OutcomeLevelEnum(EnumDefinitionImpl):
    """
    Levels at which adverse outcomes manifest.
    """
    individual = PermissibleValue(
        text="individual",
        description="Adverse outcome in an individual organism")
    population = PermissibleValue(
        text="population",
        description="Adverse outcome at the population level")

    _defn = EnumDefinition(
        name="OutcomeLevelEnum",
        description="Levels at which adverse outcomes manifest.",
    )

class SampleTypeEnum(EnumDefinitionImpl):
    """
    Types of biological samples for in vivo assays.
    """
    urine = PermissibleValue(
        text="urine",
        description="Urine sample")
    blood = PermissibleValue(
        text="blood",
        description="Blood sample")
    sputum = PermissibleValue(
        text="sputum",
        description="Induced or spontaneous sputum")
    balf = PermissibleValue(
        text="balf",
        description="Bronchoalveolar lavage fluid")
    nasal_epithelium = PermissibleValue(
        text="nasal_epithelium",
        description="Nasal epithelial sample")
    bronchial_epithelium = PermissibleValue(
        text="bronchial_epithelium",
        description="Bronchial epithelial sample")
    exhaled_breath_condensate = PermissibleValue(
        text="exhaled_breath_condensate",
        description="Exhaled breath condensate")
    biopsy = PermissibleValue(
        text="biopsy",
        description="Tissue biopsy")
    sweat = PermissibleValue(
        text="sweat",
        description="Sweat sample")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
        description="Types of biological samples for in vivo assays.",
    )

class CellCultureGrowthModeEnum(EnumDefinitionImpl):
    """
    Cell culture growth modes.
    """
    adherent = PermissibleValue(
        text="adherent",
        description="Cells grow attached to a surface",
        meaning=CLO["0000028"])
    suspension = PermissibleValue(
        text="suspension",
        description="Cells grow suspended in culture medium",
        meaning=CLO["0000029"])
    air_liquid_interface = PermissibleValue(
        text="air_liquid_interface",
        description="Cells cultured at air-liquid interface (ALI)",
        meaning=OBI["0600047"])
    three_dimensional = PermissibleValue(
        text="three_dimensional",
        description="Cells grown in 3D matrix or scaffold")
    organoid = PermissibleValue(
        text="organoid",
        description="Self-organizing 3D tissue culture")
    spheroid = PermissibleValue(
        text="spheroid",
        description="Spherical cellular aggregates")

    _defn = EnumDefinition(
        name="CellCultureGrowthModeEnum",
        description="Cell culture growth modes.",
    )

class SubstrateTypeEnum(EnumDefinitionImpl):
    """
    Types of cell culture substrates.
    """
    plastic = PermissibleValue(
        text="plastic",
        description="Standard tissue culture-treated plastic")
    collagen_coated = PermissibleValue(
        text="collagen_coated",
        description="Collagen-coated surface")
    matrigel = PermissibleValue(
        text="matrigel",
        description="Basement membrane matrix")
    fibronectin_coated = PermissibleValue(
        text="fibronectin_coated",
        description="Fibronectin-coated surface")
    laminin_coated = PermissibleValue(
        text="laminin_coated",
        description="Laminin-coated surface")
    transwell_insert = PermissibleValue(
        text="transwell_insert",
        description="Permeable support for ALI culture")
    hydrogel = PermissibleValue(
        text="hydrogel",
        description="Three-dimensional hydrogel matrix")
    glass = PermissibleValue(
        text="glass",
        description="Glass surface or coverslip")
    pdms = PermissibleValue(
        text="pdms",
        description="Polydimethylsiloxane (microfluidics)")

    _defn = EnumDefinition(
        name="SubstrateTypeEnum",
        description="Types of cell culture substrates.",
    )

class SupplementTypeEnum(EnumDefinitionImpl):
    """
    Categories of cell culture medium supplements.
    """
    growth_factor = PermissibleValue(
        text="growth_factor",
        description="Proteins that stimulate cell growth",
        meaning=CHEBI["23924"])
    antibiotic = PermissibleValue(
        text="antibiotic",
        description="Antimicrobial substances",
        meaning=CHEBI["33281"])
    antifungal = PermissibleValue(
        text="antifungal",
        description="Antifungal agents",
        meaning=CHEBI["35718"])
    hormone = PermissibleValue(
        text="hormone",
        description="Signaling molecules",
        meaning=CHEBI["24621"])
    vitamin = PermissibleValue(
        text="vitamin",
        description="Essential vitamins",
        meaning=CHEBI["33229"])
    amino_acid = PermissibleValue(
        text="amino_acid",
        description="Amino acid supplements",
        meaning=CHEBI["33709"])
    lipid = PermissibleValue(
        text="lipid",
        description="Lipid supplements",
        meaning=CHEBI["18059"])
    trace_element = PermissibleValue(
        text="trace_element",
        description="Essential trace elements")
    attachment_factor = PermissibleValue(
        text="attachment_factor",
        description="Factors promoting cell attachment")
    differentiation_factor = PermissibleValue(
        text="differentiation_factor",
        description="Factors promoting cell differentiation")

    _defn = EnumDefinition(
        name="SupplementTypeEnum",
        description="Categories of cell culture medium supplements.",
    )

class AssayContextCapabilityEnum(EnumDefinitionImpl):
    """
    Indicates what experimental contexts an assay class supports. Used to constrain valid study_subject types and
    enable context-appropriate slots.
    """
    in_vitro_only = PermissibleValue(
        text="in_vitro_only",
        description="Assay can only be performed in vitro (cell cultures, tissue slices, organoids, etc.)")
    in_vivo_only = PermissibleValue(
        text="in_vivo_only",
        description="""Assay can only be performed in vivo (requires samples from or measurements on living human or animal subjects)""")
    in_vitro_or_in_vivo = PermissibleValue(
        text="in_vitro_or_in_vivo",
        description="""Assay can be performed in either in vitro or in vivo contexts depending on the experimental design""")

    _defn = EnumDefinition(
        name="AssayContextCapabilityEnum",
        description="""Indicates what experimental contexts an assay class supports. Used to constrain valid study_subject types and enable context-appropriate slots.""",
    )

class CiliaryMotionPatternEnum(EnumDefinitionImpl):
    """
    Patterns of ciliary motion.
    """
    coordinated = PermissibleValue(
        text="coordinated",
        description="Normal coordinated beating pattern")
    dyskinetic = PermissibleValue(
        text="dyskinetic",
        description="Abnormal dyskinetic motion")
    immotile = PermissibleValue(
        text="immotile",
        description="Non-motile/static cilia")
    rotational = PermissibleValue(
        text="rotational",
        description="Rotational motion pattern")
    stiff = PermissibleValue(
        text="stiff",
        description="Stiff/rigid beating")

    _defn = EnumDefinition(
        name="CiliaryMotionPatternEnum",
        description="Patterns of ciliary motion.",
    )

class DirectionalityEnum(EnumDefinitionImpl):
    """
    Directionality of mucociliary transport.
    """
    normal = PermissibleValue(
        text="normal",
        description="Normal directed transport")
    reversed = PermissibleValue(
        text="reversed",
        description="Reversed transport direction")
    absent = PermissibleValue(
        text="absent",
        description="No directed transport")
    variable = PermissibleValue(
        text="variable",
        description="Variable/inconsistent direction")

    _defn = EnumDefinition(
        name="DirectionalityEnum",
        description="Directionality of mucociliary transport.",
    )

# Slots
class slots:
    pass

slots.adverse_outcome_pathways = Slot(uri=SOMA.adverse_outcome_pathways, name="adverse_outcome_pathways", curie=SOMA.curie('adverse_outcome_pathways'),
                   model_uri=SOMA.adverse_outcome_pathways, domain=None, range=Optional[Union[dict[Union[str, AdverseOutcomePathwayId], Union[dict, AdverseOutcomePathway]], list[Union[dict, AdverseOutcomePathway]]]])

slots.ciliary_function_assays = Slot(uri=SOMA.ciliary_function_assays, name="ciliary_function_assays", curie=SOMA.curie('ciliary_function_assays'),
                   model_uri=SOMA.ciliary_function_assays, domain=None, range=Optional[Union[dict[Union[str, CiliaryFunctionAssayId], Union[dict, CiliaryFunctionAssay]], list[Union[dict, CiliaryFunctionAssay]]]])

slots.asl_assays = Slot(uri=SOMA.asl_assays, name="asl_assays", curie=SOMA.curie('asl_assays'),
                   model_uri=SOMA.asl_assays, domain=None, range=Optional[Union[dict[Union[str, ASLAssayId], Union[dict, ASLAssay]], list[Union[dict, ASLAssay]]]])

slots.mcc_assays = Slot(uri=SOMA.mcc_assays, name="mcc_assays", curie=SOMA.curie('mcc_assays'),
                   model_uri=SOMA.mcc_assays, domain=None, range=Optional[Union[dict[Union[str, MucociliaryClearanceAssayId], Union[dict, MucociliaryClearanceAssay]], list[Union[dict, MucociliaryClearanceAssay]]]])

slots.oxidative_stress_assays = Slot(uri=SOMA.oxidative_stress_assays, name="oxidative_stress_assays", curie=SOMA.curie('oxidative_stress_assays'),
                   model_uri=SOMA.oxidative_stress_assays, domain=None, range=Optional[Union[dict[Union[str, OxidativeStressAssayId], Union[dict, OxidativeStressAssay]], list[Union[dict, OxidativeStressAssay]]]])

slots.cftr_assays = Slot(uri=SOMA.cftr_assays, name="cftr_assays", curie=SOMA.curie('cftr_assays'),
                   model_uri=SOMA.cftr_assays, domain=None, range=Optional[Union[dict[Union[str, CFTRFunctionAssayId], Union[dict, CFTRFunctionAssay]], list[Union[dict, CFTRFunctionAssay]]]])

slots.egfr_signaling_assays = Slot(uri=SOMA.egfr_signaling_assays, name="egfr_signaling_assays", curie=SOMA.curie('egfr_signaling_assays'),
                   model_uri=SOMA.egfr_signaling_assays, domain=None, range=Optional[Union[dict[Union[str, EGFRSignalingAssayId], Union[dict, EGFRSignalingAssay]], list[Union[dict, EGFRSignalingAssay]]]])

slots.goblet_cell_assays = Slot(uri=SOMA.goblet_cell_assays, name="goblet_cell_assays", curie=SOMA.curie('goblet_cell_assays'),
                   model_uri=SOMA.goblet_cell_assays, domain=None, range=Optional[Union[dict[Union[str, GobletCellAssayId], Union[dict, GobletCellAssay]], list[Union[dict, GobletCellAssay]]]])

slots.balf_sputum_assays = Slot(uri=SOMA.balf_sputum_assays, name="balf_sputum_assays", curie=SOMA.curie('balf_sputum_assays'),
                   model_uri=SOMA.balf_sputum_assays, domain=None, range=Optional[Union[dict[Union[str, BALFSputumAssayId], Union[dict, BALFSputumAssay]], list[Union[dict, BALFSputumAssay]]]])

slots.lung_function_assays = Slot(uri=SOMA.lung_function_assays, name="lung_function_assays", curie=SOMA.curie('lung_function_assays'),
                   model_uri=SOMA.lung_function_assays, domain=None, range=Optional[Union[dict[Union[str, LungFunctionAssayId], Union[dict, LungFunctionAssay]], list[Union[dict, LungFunctionAssay]]]])

slots.foxj_assays = Slot(uri=SOMA.foxj_assays, name="foxj_assays", curie=SOMA.curie('foxj_assays'),
                   model_uri=SOMA.foxj_assays, domain=None, range=Optional[Union[dict[Union[str, FoxJExpressionAssayId], Union[dict, FoxJExpressionAssay]], list[Union[dict, FoxJExpressionAssay]]]])

slots.gene_expression_assays = Slot(uri=SOMA.gene_expression_assays, name="gene_expression_assays", curie=SOMA.curie('gene_expression_assays'),
                   model_uri=SOMA.gene_expression_assays, domain=None, range=Optional[Union[dict[Union[str, GeneExpressionAssayId], Union[dict, GeneExpressionAssay]], list[Union[dict, GeneExpressionAssay]]]])

slots.protocols = Slot(uri=SOMA.protocols, name="protocols", curie=SOMA.curie('protocols'),
                   model_uri=SOMA.protocols, domain=None, range=Optional[Union[dict[Union[str, ProtocolId], Union[dict, Protocol]], list[Union[dict, Protocol]]]])

slots.id = Slot(uri=AOP_FRAMEWORK.id, name="id", curie=AOP_FRAMEWORK.curie('id'),
                   model_uri=SOMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=SOMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=SOMA.description, domain=None, range=Optional[str])

slots.biological_process = Slot(uri=AOP_FRAMEWORK.biological_process, name="biological_process", curie=AOP_FRAMEWORK.curie('biological_process'),
                   model_uri=SOMA.biological_process, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^GO:\d{7}$'))

slots.biological_object = Slot(uri=AOP_FRAMEWORK.biological_object, name="biological_object", curie=AOP_FRAMEWORK.curie('biological_object'),
                   model_uri=SOMA.biological_object, domain=None, range=Optional[str])

slots.biological_action = Slot(uri=AOP_FRAMEWORK.biological_action, name="biological_action", curie=AOP_FRAMEWORK.curie('biological_action'),
                   model_uri=SOMA.biological_action, domain=None, range=Optional[Union[str, "BiologicalActionEnum"]])

slots.level_of_biological_organization = Slot(uri=AOP_FRAMEWORK.level_of_biological_organization, name="level_of_biological_organization", curie=AOP_FRAMEWORK.curie('level_of_biological_organization'),
                   model_uri=SOMA.level_of_biological_organization, domain=None, range=Optional[Union[str, "BiologicalOrganizationLevelEnum"]])

slots.occurs_in_cell_type = Slot(uri=AOP_FRAMEWORK.occurs_in_cell_type, name="occurs_in_cell_type", curie=AOP_FRAMEWORK.curie('occurs_in_cell_type'),
                   model_uri=SOMA.occurs_in_cell_type, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^CL:\d{7}$'))

slots.occurs_in_anatomy = Slot(uri=AOP_FRAMEWORK.occurs_in_anatomy, name="occurs_in_anatomy", curie=AOP_FRAMEWORK.curie('occurs_in_anatomy'),
                   model_uri=SOMA.occurs_in_anatomy, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^UBERON:\d{7}$'))

slots.aopwiki_id = Slot(uri=AOP_FRAMEWORK.aopwiki_id, name="aopwiki_id", curie=AOP_FRAMEWORK.curie('aopwiki_id'),
                   model_uri=SOMA.aopwiki_id, domain=None, range=Optional[str])

slots.upstream_key_events = Slot(uri=AOP_FRAMEWORK.upstream_key_events, name="upstream_key_events", curie=AOP_FRAMEWORK.curie('upstream_key_events'),
                   model_uri=SOMA.upstream_key_events, domain=None, range=Optional[Union[dict[Union[str, KeyEventId], Union[dict, KeyEvent]], list[Union[dict, KeyEvent]]]])

slots.downstream_key_events = Slot(uri=AOP_FRAMEWORK.downstream_key_events, name="downstream_key_events", curie=AOP_FRAMEWORK.curie('downstream_key_events'),
                   model_uri=SOMA.downstream_key_events, domain=None, range=Optional[Union[dict[Union[str, KeyEventId], Union[dict, KeyEvent]], list[Union[dict, KeyEvent]]]])

slots.upstream_event = Slot(uri=AOP_FRAMEWORK.upstream_event, name="upstream_event", curie=AOP_FRAMEWORK.curie('upstream_event'),
                   model_uri=SOMA.upstream_event, domain=None, range=Optional[Union[dict, KeyEvent]])

slots.downstream_event = Slot(uri=AOP_FRAMEWORK.downstream_event, name="downstream_event", curie=AOP_FRAMEWORK.curie('downstream_event'),
                   model_uri=SOMA.downstream_event, domain=None, range=Optional[Union[dict, KeyEvent]])

slots.relationship_type = Slot(uri=AOP_FRAMEWORK.relationship_type, name="relationship_type", curie=AOP_FRAMEWORK.curie('relationship_type'),
                   model_uri=SOMA.relationship_type, domain=None, range=Optional[str])

slots.evidence_support = Slot(uri=AOP_FRAMEWORK.evidence_support, name="evidence_support", curie=AOP_FRAMEWORK.curie('evidence_support'),
                   model_uri=SOMA.evidence_support, domain=None, range=Optional[Union[str, "EvidenceSupportEnum"]])

slots.quantitative_understanding = Slot(uri=AOP_FRAMEWORK.quantitative_understanding, name="quantitative_understanding", curie=AOP_FRAMEWORK.curie('quantitative_understanding'),
                   model_uri=SOMA.quantitative_understanding, domain=None, range=Optional[Union[str, "QuantitativeUnderstandingEnum"]])

slots.outcome_level = Slot(uri=AOP_FRAMEWORK.outcome_level, name="outcome_level", curie=AOP_FRAMEWORK.curie('outcome_level'),
                   model_uri=SOMA.outcome_level, domain=None, range=Optional[Union[str, "OutcomeLevelEnum"]])

slots.molecular_initiating_event = Slot(uri=AOP_FRAMEWORK.molecular_initiating_event, name="molecular_initiating_event", curie=AOP_FRAMEWORK.curie('molecular_initiating_event'),
                   model_uri=SOMA.molecular_initiating_event, domain=None, range=Optional[Union[dict, MolecularInitiatingEvent]])

slots.key_events = Slot(uri=AOP_FRAMEWORK.key_events, name="key_events", curie=AOP_FRAMEWORK.curie('key_events'),
                   model_uri=SOMA.key_events, domain=None, range=Optional[Union[dict[Union[str, KeyEventId], Union[dict, KeyEvent]], list[Union[dict, KeyEvent]]]])

slots.key_event_relationships = Slot(uri=AOP_FRAMEWORK.key_event_relationships, name="key_event_relationships", curie=AOP_FRAMEWORK.curie('key_event_relationships'),
                   model_uri=SOMA.key_event_relationships, domain=None, range=Optional[Union[dict[Union[str, KeyEventRelationshipId], Union[dict, KeyEventRelationship]], list[Union[dict, KeyEventRelationship]]]])

slots.adverse_outcome = Slot(uri=AOP_FRAMEWORK.adverse_outcome, name="adverse_outcome", curie=AOP_FRAMEWORK.curie('adverse_outcome'),
                   model_uri=SOMA.adverse_outcome, domain=None, range=Optional[Union[dict, AdverseOutcome]])

slots.stressors = Slot(uri=AOP_FRAMEWORK.stressors, name="stressors", curie=AOP_FRAMEWORK.curie('stressors'),
                   model_uri=SOMA.stressors, domain=None, range=Optional[Union[str, list[str]]])

slots.target_molecule = Slot(uri=AOP_FRAMEWORK.target_molecule, name="target_molecule", curie=AOP_FRAMEWORK.curie('target_molecule'),
                   model_uri=SOMA.target_molecule, domain=None, range=Optional[str])

slots.informs_on_key_event = Slot(uri=ASSAY_BASE.informs_on_key_event, name="informs_on_key_event", curie=ASSAY_BASE.curie('informs_on_key_event'),
                   model_uri=SOMA.informs_on_key_event, domain=None, range=Optional[Union[dict, KeyEvent]])

slots.has_specified_output = Slot(uri=ASSAY_BASE.has_specified_output, name="has_specified_output", curie=ASSAY_BASE.curie('has_specified_output'),
                   model_uri=SOMA.has_specified_output, domain=None, range=Optional[Union[dict, AssayOutputMeasurement]])

slots.cell_type = Slot(uri=EFO['0000324'], name="cell_type", curie=EFO.curie('0000324'),
                   model_uri=SOMA.cell_type, domain=None, range=Optional[Union[dict, CellTypeReference]])

slots.target_cell_type = Slot(uri=ASSAY_BASE.target_cell_type, name="target_cell_type", curie=ASSAY_BASE.curie('target_cell_type'),
                   model_uri=SOMA.target_cell_type, domain=None, range=Optional[Union[dict, CellTypeReference]])

slots.model_species = Slot(uri=ASSAY_BASE.model_species, name="model_species", curie=ASSAY_BASE.curie('model_species'),
                   model_uri=SOMA.model_species, domain=None, range=Optional[Union[dict, SpeciesReference]])

slots.subject_type = Slot(uri=ASSAY_BASE.subject_type, name="subject_type", curie=ASSAY_BASE.curie('subject_type'),
                   model_uri=SOMA.subject_type, domain=None, range=Optional[str])

slots.study_subject = Slot(uri=ASSAY_BASE.study_subject, name="study_subject", curie=ASSAY_BASE.curie('study_subject'),
                   model_uri=SOMA.study_subject, domain=None, range=Optional[Union[dict, StudySubject]])

slots.sample_collection_method = Slot(uri=ASSAY_BASE.sample_collection_method, name="sample_collection_method", curie=ASSAY_BASE.curie('sample_collection_method'),
                   model_uri=SOMA.sample_collection_method, domain=None, range=Optional[str])

slots.clinical_context = Slot(uri=ASSAY_BASE.clinical_context, name="clinical_context", curie=ASSAY_BASE.curie('clinical_context'),
                   model_uri=SOMA.clinical_context, domain=None, range=Optional[str])

slots.has_exposure_condition = Slot(uri=ASSAY_BASE.has_exposure_condition, name="has_exposure_condition", curie=ASSAY_BASE.curie('has_exposure_condition'),
                   model_uri=SOMA.has_exposure_condition, domain=None, range=Optional[Union[dict[Union[str, ExposureConditionId], Union[dict, ExposureCondition]], list[Union[dict, ExposureCondition]]]])

slots.protocol_type = Slot(uri=ASSAY_BASE.protocol_type, name="protocol_type", curie=ASSAY_BASE.curie('protocol_type'),
                   model_uri=SOMA.protocol_type, domain=None, range=Optional[str])

slots.follows_protocols = Slot(uri=ASSAY_BASE.follows_protocols, name="follows_protocols", curie=ASSAY_BASE.curie('follows_protocols'),
                   model_uri=SOMA.follows_protocols, domain=None, range=Optional[Union[dict[Union[str, ProtocolId], Union[dict, Protocol]], list[Union[dict, Protocol]]]])

slots.sub_protocols = Slot(uri=ASSAY_BASE.sub_protocols, name="sub_protocols", curie=ASSAY_BASE.curie('sub_protocols'),
                   model_uri=SOMA.sub_protocols, domain=None, range=Optional[Union[dict[Union[str, ProtocolId], Union[dict, Protocol]], list[Union[dict, Protocol]]]])

slots.days_at_differentiation = Slot(uri=ASSAY_BASE.days_at_differentiation, name="days_at_differentiation", curie=ASSAY_BASE.curie('days_at_differentiation'),
                   model_uri=SOMA.days_at_differentiation, domain=None, range=Optional[int])

slots.donor_info = Slot(uri=ASSAY_BASE.donor_info, name="donor_info", curie=ASSAY_BASE.curie('donor_info'),
                   model_uri=SOMA.donor_info, domain=None, range=Optional[str])

slots.replicates_per_donor = Slot(uri=ASSAY_BASE.replicates_per_donor, name="replicates_per_donor", curie=ASSAY_BASE.curie('replicates_per_donor'),
                   model_uri=SOMA.replicates_per_donor, domain=None, range=Optional[int])

slots.assay_date = Slot(uri=ASSAY_BASE.assay_date, name="assay_date", curie=ASSAY_BASE.curie('assay_date'),
                   model_uri=SOMA.assay_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age = Slot(uri=ASSAY_BASE.age, name="age", curie=ASSAY_BASE.curie('age'),
                   model_uri=SOMA.age, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sex = Slot(uri=ASSAY_BASE.sex, name="sex", curie=ASSAY_BASE.curie('sex'),
                   model_uri=SOMA.sex, domain=None, range=Optional[str])

slots.subject_characteristics = Slot(uri=ASSAY_BASE.subject_characteristics, name="subject_characteristics", curie=ASSAY_BASE.curie('subject_characteristics'),
                   model_uri=SOMA.subject_characteristics, domain=None, range=Optional[str])

slots.sample_type = Slot(uri=ASSAY_BASE.sample_type, name="sample_type", curie=ASSAY_BASE.curie('sample_type'),
                   model_uri=SOMA.sample_type, domain=None, range=Optional[Union[str, "SampleTypeEnum"]])

slots.collection_site = Slot(uri=ASSAY_BASE.collection_site, name="collection_site", curie=ASSAY_BASE.curie('collection_site'),
                   model_uri=SOMA.collection_site, domain=None, range=Optional[str])

slots.collection_date = Slot(uri=ASSAY_BASE.collection_date, name="collection_date", curie=ASSAY_BASE.curie('collection_date'),
                   model_uri=SOMA.collection_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.cohort_size = Slot(uri=ASSAY_BASE.cohort_size, name="cohort_size", curie=ASSAY_BASE.curie('cohort_size'),
                   model_uri=SOMA.cohort_size, domain=None, range=Optional[int])

slots.inclusion_criteria = Slot(uri=ASSAY_BASE.inclusion_criteria, name="inclusion_criteria", curie=ASSAY_BASE.curie('inclusion_criteria'),
                   model_uri=SOMA.inclusion_criteria, domain=None, range=Optional[str])

slots.age_range = Slot(uri=ASSAY_BASE.age_range, name="age_range", curie=ASSAY_BASE.curie('age_range'),
                   model_uri=SOMA.age_range, domain=None, range=Optional[Union[dict, QuantityRange]])

slots.subjects = Slot(uri=ASSAY_BASE.subjects, name="subjects", curie=ASSAY_BASE.curie('subjects'),
                   model_uri=SOMA.subjects, domain=None, range=Optional[Union[dict[Union[str, InVivoSubjectId], Union[dict, InVivoSubject]], list[Union[dict, InVivoSubject]]]])

slots.protocol_version = Slot(uri=ASSAY_BASE.protocol_version, name="protocol_version", curie=ASSAY_BASE.curie('protocol_version'),
                   model_uri=SOMA.protocol_version, domain=None, range=Optional[str])

slots.sop_reference = Slot(uri=ASSAY_BASE.sop_reference, name="sop_reference", curie=ASSAY_BASE.curie('sop_reference'),
                   model_uri=SOMA.sop_reference, domain=None, range=Optional[str])

slots.imaging_frame_rate = Slot(uri=ASSAY_BASE.imaging_frame_rate, name="imaging_frame_rate", curie=ASSAY_BASE.curie('imaging_frame_rate'),
                   model_uri=SOMA.imaging_frame_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.imaging_duration = Slot(uri=ASSAY_BASE.imaging_duration, name="imaging_duration", curie=ASSAY_BASE.curie('imaging_duration'),
                   model_uri=SOMA.imaging_duration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.spatial_resolution = Slot(uri=ASSAY_BASE.spatial_resolution, name="spatial_resolution", curie=ASSAY_BASE.curie('spatial_resolution'),
                   model_uri=SOMA.spatial_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.temperature_control = Slot(uri=ASSAY_BASE.temperature_control, name="temperature_control", curie=ASSAY_BASE.curie('temperature_control'),
                   model_uri=SOMA.temperature_control, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.humidity_control = Slot(uri=ASSAY_BASE.humidity_control, name="humidity_control", curie=ASSAY_BASE.curie('humidity_control'),
                   model_uri=SOMA.humidity_control, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.evaporation_prevention = Slot(uri=ASSAY_BASE.evaporation_prevention, name="evaporation_prevention", curie=ASSAY_BASE.curie('evaporation_prevention'),
                   model_uri=SOMA.evaporation_prevention, domain=None, range=Optional[str])

slots.fluorescent_labeling = Slot(uri=ASSAY_BASE.fluorescent_labeling, name="fluorescent_labeling", curie=ASSAY_BASE.curie('fluorescent_labeling'),
                   model_uri=SOMA.fluorescent_labeling, domain=None, range=Optional[str])

slots.fluorescent_tracer = Slot(uri=ASSAY_BASE.fluorescent_tracer, name="fluorescent_tracer", curie=ASSAY_BASE.curie('fluorescent_tracer'),
                   model_uri=SOMA.fluorescent_tracer, domain=None, range=Optional[str])

slots.particle_tracking_method = Slot(uri=ASSAY_BASE.particle_tracking_method, name="particle_tracking_method", curie=ASSAY_BASE.curie('particle_tracking_method'),
                   model_uri=SOMA.particle_tracking_method, domain=None, range=Optional[str])

slots.particle_size = Slot(uri=ASSAY_BASE.particle_size, name="particle_size", curie=ASSAY_BASE.curie('particle_size'),
                   model_uri=SOMA.particle_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.spirometry_standard = Slot(uri=ASSAY_BASE.spirometry_standard, name="spirometry_standard", curie=ASSAY_BASE.curie('spirometry_standard'),
                   model_uri=SOMA.spirometry_standard, domain=None, range=Optional[str])

slots.bronchodilator_agent = Slot(uri=ASSAY_BASE.bronchodilator_agent, name="bronchodilator_agent", curie=ASSAY_BASE.curie('bronchodilator_agent'),
                   model_uri=SOMA.bronchodilator_agent, domain=None, range=Optional[str])

slots.bronchodilator_dose = Slot(uri=ASSAY_BASE.bronchodilator_dose, name="bronchodilator_dose", curie=ASSAY_BASE.curie('bronchodilator_dose'),
                   model_uri=SOMA.bronchodilator_dose, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plethysmography_method = Slot(uri=ASSAY_BASE.plethysmography_method, name="plethysmography_method", curie=ASSAY_BASE.curie('plethysmography_method'),
                   model_uri=SOMA.plethysmography_method, domain=None, range=Optional[str])

slots.detection_method = Slot(uri=ASSAY_BASE.detection_method, name="detection_method", curie=ASSAY_BASE.curie('detection_method'),
                   model_uri=SOMA.detection_method, domain=None, range=Optional[str])

slots.staining_type = Slot(uri=ASSAY_BASE.staining_type, name="staining_type", curie=ASSAY_BASE.curie('staining_type'),
                   model_uri=SOMA.staining_type, domain=None, range=Optional[str])

slots.antibodies_used = Slot(uri=ASSAY_BASE.antibodies_used, name="antibodies_used", curie=ASSAY_BASE.curie('antibodies_used'),
                   model_uri=SOMA.antibodies_used, domain=None, range=Optional[Union[str, list[str]]])

slots.normalization_method = Slot(uri=ASSAY_BASE.normalization_method, name="normalization_method", curie=ASSAY_BASE.curie('normalization_method'),
                   model_uri=SOMA.normalization_method, domain=None, range=Optional[str])

slots.quality_control_criteria = Slot(uri=ASSAY_BASE.quality_control_criteria, name="quality_control_criteria", curie=ASSAY_BASE.curie('quality_control_criteria'),
                   model_uri=SOMA.quality_control_criteria, domain=None, range=Optional[str])

slots.replicate_requirements = Slot(uri=ASSAY_BASE.replicate_requirements, name="replicate_requirements", curie=ASSAY_BASE.curie('replicate_requirements'),
                   model_uri=SOMA.replicate_requirements, domain=None, range=Optional[int])

slots.protocol_author = Slot(uri=ASSAY_BASE.protocol_author, name="protocol_author", curie=ASSAY_BASE.curie('protocol_author'),
                   model_uri=SOMA.protocol_author, domain=None, range=Optional[str])

slots.institution = Slot(uri=ASSAY_BASE.institution, name="institution", curie=ASSAY_BASE.curie('institution'),
                   model_uri=SOMA.institution, domain=None, range=Optional[str])

slots.publication_reference = Slot(uri=ASSAY_BASE.publication_reference, name="publication_reference", curie=ASSAY_BASE.curie('publication_reference'),
                   model_uri=SOMA.publication_reference, domain=None, range=Optional[str])

slots.last_updated = Slot(uri=ASSAY_BASE.last_updated, name="last_updated", curie=ASSAY_BASE.curie('last_updated'),
                   model_uri=SOMA.last_updated, domain=None, range=Optional[Union[str, XSDDate]])

slots.validation_status = Slot(uri=ASSAY_BASE.validation_status, name="validation_status", curie=ASSAY_BASE.curie('validation_status'),
                   model_uri=SOMA.validation_status, domain=None, range=Optional[str])

slots.fixation_method = Slot(uri=ASSAY_BASE.fixation_method, name="fixation_method", curie=ASSAY_BASE.curie('fixation_method'),
                   model_uri=SOMA.fixation_method, domain=None, range=Optional[str])

slots.counterstain = Slot(uri=ASSAY_BASE.counterstain, name="counterstain", curie=ASSAY_BASE.curie('counterstain'),
                   model_uri=SOMA.counterstain, domain=None, range=Optional[str])

slots.primer_sequences = Slot(uri=ASSAY_BASE.primer_sequences, name="primer_sequences", curie=ASSAY_BASE.curie('primer_sequences'),
                   model_uri=SOMA.primer_sequences, domain=None, range=Optional[Union[str, list[str]]])

slots.reference_gene = Slot(uri=ASSAY_BASE.reference_gene, name="reference_gene", curie=ASSAY_BASE.curie('reference_gene'),
                   model_uri=SOMA.reference_gene, domain=None, range=Optional[str])

slots.lysis_buffer = Slot(uri=ASSAY_BASE.lysis_buffer, name="lysis_buffer", curie=ASSAY_BASE.curie('lysis_buffer'),
                   model_uri=SOMA.lysis_buffer, domain=None, range=Optional[str])

slots.platform = Slot(uri=ASSAY_BASE.platform, name="platform", curie=ASSAY_BASE.curie('platform'),
                   model_uri=SOMA.platform, domain=None, range=Optional[str])

slots.equipment_required = Slot(uri=ASSAY_BASE.equipment_required, name="equipment_required", curie=ASSAY_BASE.curie('equipment_required'),
                   model_uri=SOMA.equipment_required, domain=None, range=Optional[Union[str, list[str]]])

slots.key_reagents = Slot(uri=ASSAY_BASE.key_reagents, name="key_reagents", curie=ASSAY_BASE.curie('key_reagents'),
                   model_uri=SOMA.key_reagents, domain=None, range=Optional[Union[str, list[str]]])

slots.general_procedure = Slot(uri=ASSAY_BASE.general_procedure, name="general_procedure", curie=ASSAY_BASE.curie('general_procedure'),
                   model_uri=SOMA.general_procedure, domain=None, range=Optional[str])

slots.obi_mapping = Slot(uri=ASSAY_BASE.obi_mapping, name="obi_mapping", curie=ASSAY_BASE.curie('obi_mapping'),
                   model_uri=SOMA.obi_mapping, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.exposure_agent = Slot(uri=ASSAY_BASE.exposure_agent, name="exposure_agent", curie=ASSAY_BASE.curie('exposure_agent'),
                   model_uri=SOMA.exposure_agent, domain=None, range=Optional[Union[dict, ChemicalEntityReference]])

slots.exposure_duration = Slot(uri=ASSAY_BASE.exposure_duration, name="exposure_duration", curie=ASSAY_BASE.curie('exposure_duration'),
                   model_uri=SOMA.exposure_duration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.exposure_concentration = Slot(uri=ASSAY_BASE.exposure_concentration, name="exposure_concentration", curie=ASSAY_BASE.curie('exposure_concentration'),
                   model_uri=SOMA.exposure_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.timing_post_exposure = Slot(uri=ASSAY_BASE.timing_post_exposure, name="timing_post_exposure", curie=ASSAY_BASE.curie('timing_post_exposure'),
                   model_uri=SOMA.timing_post_exposure, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cell_line = Slot(uri=ASSAY_BASE.cell_line, name="cell_line", curie=ASSAY_BASE.curie('cell_line'),
                   model_uri=SOMA.cell_line, domain=None, range=Optional[Union[dict, CellLine]])

slots.primary_cell = Slot(uri=ASSAY_BASE.primary_cell, name="primary_cell", curie=ASSAY_BASE.curie('primary_cell'),
                   model_uri=SOMA.primary_cell, domain=None, range=Optional[Union[dict, CellTypeReference]])

slots.anatomical_origin = Slot(uri=ASSAY_BASE.anatomical_origin, name="anatomical_origin", curie=ASSAY_BASE.curie('anatomical_origin'),
                   model_uri=SOMA.anatomical_origin, domain=None, range=Optional[Union[dict, AnatomicalEntityReference]])

slots.cell_culture_growth_mode = Slot(uri=ASSAY_BASE.cell_culture_growth_mode, name="cell_culture_growth_mode", curie=ASSAY_BASE.curie('cell_culture_growth_mode'),
                   model_uri=SOMA.cell_culture_growth_mode, domain=None, range=Optional[Union[str, "CellCultureGrowthModeEnum"]])

slots.culture_conditions = Slot(uri=ASSAY_BASE.culture_conditions, name="culture_conditions", curie=ASSAY_BASE.curie('culture_conditions'),
                   model_uri=SOMA.culture_conditions, domain=None, range=Optional[Union[dict, CellCultureConditions]])

slots.culture_media = Slot(uri=ASSAY_BASE.culture_media, name="culture_media", curie=ASSAY_BASE.curie('culture_media'),
                   model_uri=SOMA.culture_media, domain=None, range=Optional[Union[dict, CellCultureMedium]])

slots.substrate_type = Slot(uri=ASSAY_BASE.substrate_type, name="substrate_type", curie=ASSAY_BASE.curie('substrate_type'),
                   model_uri=SOMA.substrate_type, domain=None, range=Optional[Union[str, "SubstrateTypeEnum"]])

slots.passage_number = Slot(uri=ASSAY_BASE.passage_number, name="passage_number", curie=ASSAY_BASE.curie('passage_number'),
                   model_uri=SOMA.passage_number, domain=None, range=Optional[int])

slots.days_at_air_liquid_interface = Slot(uri=ASSAY_BASE.days_at_air_liquid_interface, name="days_at_air_liquid_interface", curie=ASSAY_BASE.curie('days_at_air_liquid_interface'),
                   model_uri=SOMA.days_at_air_liquid_interface, domain=None, range=Optional[int])

slots.donor_count = Slot(uri=ASSAY_BASE.donor_count, name="donor_count", curie=ASSAY_BASE.curie('donor_count'),
                   model_uri=SOMA.donor_count, domain=None, range=Optional[int])

slots.confluence_level = Slot(uri=ASSAY_BASE.confluence_level, name="confluence_level", curie=ASSAY_BASE.curie('confluence_level'),
                   model_uri=SOMA.confluence_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.seeding_density = Slot(uri=ASSAY_BASE.seeding_density, name="seeding_density", curie=ASSAY_BASE.curie('seeding_density'),
                   model_uri=SOMA.seeding_density, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.coating = Slot(uri=ASSAY_BASE.coating, name="coating", curie=ASSAY_BASE.curie('coating'),
                   model_uri=SOMA.coating, domain=None, range=Optional[str])

slots.matrix_composition = Slot(uri=ASSAY_BASE.matrix_composition, name="matrix_composition", curie=ASSAY_BASE.curie('matrix_composition'),
                   model_uri=SOMA.matrix_composition, domain=None, range=Optional[str])

slots.size_range = Slot(uri=ASSAY_BASE.size_range, name="size_range", curie=ASSAY_BASE.curie('size_range'),
                   model_uri=SOMA.size_range, domain=None, range=Optional[Union[dict, QuantityRange]])

slots.organoid_type = Slot(uri=ASSAY_BASE.organoid_type, name="organoid_type", curie=ASSAY_BASE.curie('organoid_type'),
                   model_uri=SOMA.organoid_type, domain=None, range=Optional[str])

slots.cell_type_ratios = Slot(uri=ASSAY_BASE.cell_type_ratios, name="cell_type_ratios", curie=ASSAY_BASE.curie('cell_type_ratios'),
                   model_uri=SOMA.cell_type_ratios, domain=None, range=Optional[Union[str, list[str]]])

slots.tissue_origin = Slot(uri=ASSAY_BASE.tissue_origin, name="tissue_origin", curie=ASSAY_BASE.curie('tissue_origin'),
                   model_uri=SOMA.tissue_origin, domain=None, range=Optional[str])

slots.disease_state = Slot(uri=ASSAY_BASE.disease_state, name="disease_state", curie=ASSAY_BASE.curie('disease_state'),
                   model_uri=SOMA.disease_state, domain=None, range=Optional[str])

slots.supplier = Slot(uri=ASSAY_BASE.supplier, name="supplier", curie=ASSAY_BASE.curie('supplier'),
                   model_uri=SOMA.supplier, domain=None, range=Optional[str])

slots.catalog_number = Slot(uri=ASSAY_BASE.catalog_number, name="catalog_number", curie=ASSAY_BASE.curie('catalog_number'),
                   model_uri=SOMA.catalog_number, domain=None, range=Optional[str])

slots.authentication_method = Slot(uri=ASSAY_BASE.authentication_method, name="authentication_method", curie=ASSAY_BASE.curie('authentication_method'),
                   model_uri=SOMA.authentication_method, domain=None, range=Optional[str])

slots.mycoplasma_status = Slot(uri=ASSAY_BASE.mycoplasma_status, name="mycoplasma_status", curie=ASSAY_BASE.curie('mycoplasma_status'),
                   model_uri=SOMA.mycoplasma_status, domain=None, range=Optional[str])

slots.base_medium = Slot(uri=ASSAY_BASE.base_medium, name="base_medium", curie=ASSAY_BASE.curie('base_medium'),
                   model_uri=SOMA.base_medium, domain=None, range=Optional[str])

slots.serum_type = Slot(uri=ASSAY_BASE.serum_type, name="serum_type", curie=ASSAY_BASE.curie('serum_type'),
                   model_uri=SOMA.serum_type, domain=None, range=Optional[str])

slots.serum_concentration = Slot(uri=ASSAY_BASE.serum_concentration, name="serum_concentration", curie=ASSAY_BASE.curie('serum_concentration'),
                   model_uri=SOMA.serum_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.supplements = Slot(uri=ASSAY_BASE.supplements, name="supplements", curie=ASSAY_BASE.curie('supplements'),
                   model_uri=SOMA.supplements, domain=None, range=Optional[Union[dict[Union[str, MediumSupplementId], Union[dict, MediumSupplement]], list[Union[dict, MediumSupplement]]]])

slots.osmolality = Slot(uri=ASSAY_BASE.osmolality, name="osmolality", curie=ASSAY_BASE.curie('osmolality'),
                   model_uri=SOMA.osmolality, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.manufacturer = Slot(uri=ASSAY_BASE.manufacturer, name="manufacturer", curie=ASSAY_BASE.curie('manufacturer'),
                   model_uri=SOMA.manufacturer, domain=None, range=Optional[str])

slots.lot_number = Slot(uri=ASSAY_BASE.lot_number, name="lot_number", curie=ASSAY_BASE.curie('lot_number'),
                   model_uri=SOMA.lot_number, domain=None, range=Optional[str])

slots.preparation_date = Slot(uri=ASSAY_BASE.preparation_date, name="preparation_date", curie=ASSAY_BASE.curie('preparation_date'),
                   model_uri=SOMA.preparation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.supplement_type = Slot(uri=ASSAY_BASE.supplement_type, name="supplement_type", curie=ASSAY_BASE.curie('supplement_type'),
                   model_uri=SOMA.supplement_type, domain=None, range=Optional[Union[str, "SupplementTypeEnum"]])

slots.concentration = Slot(uri=ASSAY_BASE.concentration, name="concentration", curie=ASSAY_BASE.curie('concentration'),
                   model_uri=SOMA.concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.value = Slot(uri=ASSAY_BASE.value, name="value", curie=ASSAY_BASE.curie('value'),
                   model_uri=SOMA.value, domain=None, range=Optional[str])

slots.unit = Slot(uri=ASSAY_BASE.unit, name="unit", curie=ASSAY_BASE.curie('unit'),
                   model_uri=SOMA.unit, domain=None, range=Optional[Union[dict, Unit]])

slots.min_value = Slot(uri=ASSAY_BASE.min_value, name="min_value", curie=ASSAY_BASE.curie('min_value'),
                   model_uri=SOMA.min_value, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.max_value = Slot(uri=ASSAY_BASE.max_value, name="max_value", curie=ASSAY_BASE.curie('max_value'),
                   model_uri=SOMA.max_value, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.beat_frequency_hz = Slot(uri=ASSAY_MICROSCHEMAS.beat_frequency_hz, name="beat_frequency_hz", curie=ASSAY_MICROSCHEMAS.curie('beat_frequency_hz'),
                   model_uri=SOMA.beat_frequency_hz, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.active_area_percentage = Slot(uri=ASSAY_MICROSCHEMAS.active_area_percentage, name="active_area_percentage", curie=ASSAY_MICROSCHEMAS.curie('active_area_percentage'),
                   model_uri=SOMA.active_area_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cilia_length = Slot(uri=ASSAY_MICROSCHEMAS.cilia_length, name="cilia_length", curie=ASSAY_MICROSCHEMAS.curie('cilia_length'),
                   model_uri=SOMA.cilia_length, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cilia_per_cell = Slot(uri=ASSAY_MICROSCHEMAS.cilia_per_cell, name="cilia_per_cell", curie=ASSAY_MICROSCHEMAS.curie('cilia_per_cell'),
                   model_uri=SOMA.cilia_per_cell, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.percentage_ciliated_cells = Slot(uri=ASSAY_MICROSCHEMAS.percentage_ciliated_cells, name="percentage_ciliated_cells", curie=ASSAY_MICROSCHEMAS.curie('percentage_ciliated_cells'),
                   model_uri=SOMA.percentage_ciliated_cells, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ciliary_motion_patterns = Slot(uri=ASSAY_MICROSCHEMAS.ciliary_motion_patterns, name="ciliary_motion_patterns", curie=ASSAY_MICROSCHEMAS.curie('ciliary_motion_patterns'),
                   model_uri=SOMA.ciliary_motion_patterns, domain=None, range=Optional[Union[str, "CiliaryMotionPatternEnum"]])

slots.ciliary_beat_amplitude = Slot(uri=ASSAY_MICROSCHEMAS.ciliary_beat_amplitude, name="ciliary_beat_amplitude", curie=ASSAY_MICROSCHEMAS.curie('ciliary_beat_amplitude'),
                   model_uri=SOMA.ciliary_beat_amplitude, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.analysis_software = Slot(uri=ASSAY_MICROSCHEMAS.analysis_software, name="analysis_software", curie=ASSAY_MICROSCHEMAS.curie('analysis_software'),
                   model_uri=SOMA.analysis_software, domain=None, range=Optional[str])

slots.airway_region = Slot(uri=ASSAY_MICROSCHEMAS.airway_region, name="airway_region", curie=ASSAY_MICROSCHEMAS.curie('airway_region'),
                   model_uri=SOMA.airway_region, domain=None, range=Optional[str])

slots.asl_height_um = Slot(uri=ASSAY_MICROSCHEMAS.asl_height_um, name="asl_height_um", curie=ASSAY_MICROSCHEMAS.curie('asl_height_um'),
                   model_uri=SOMA.asl_height_um, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.periciliary_layer_depth = Slot(uri=ASSAY_MICROSCHEMAS.periciliary_layer_depth, name="periciliary_layer_depth", curie=ASSAY_MICROSCHEMAS.curie('periciliary_layer_depth'),
                   model_uri=SOMA.periciliary_layer_depth, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mucus_layer_thickness = Slot(uri=ASSAY_MICROSCHEMAS.mucus_layer_thickness, name="mucus_layer_thickness", curie=ASSAY_MICROSCHEMAS.curie('mucus_layer_thickness'),
                   model_uri=SOMA.mucus_layer_thickness, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ion_composition = Slot(uri=ASSAY_MICROSCHEMAS.ion_composition, name="ion_composition", curie=ASSAY_MICROSCHEMAS.curie('ion_composition'),
                   model_uri=SOMA.ion_composition, domain=None, range=Optional[str])

slots.asl_ph = Slot(uri=ASSAY_MICROSCHEMAS.asl_ph, name="asl_ph", curie=ASSAY_MICROSCHEMAS.curie('asl_ph'),
                   model_uri=SOMA.asl_ph, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.transport_rate = Slot(uri=ASSAY_MICROSCHEMAS.transport_rate, name="transport_rate", curie=ASSAY_MICROSCHEMAS.curie('transport_rate'),
                   model_uri=SOMA.transport_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.transport_directionality = Slot(uri=ASSAY_MICROSCHEMAS.transport_directionality, name="transport_directionality", curie=ASSAY_MICROSCHEMAS.curie('transport_directionality'),
                   model_uri=SOMA.transport_directionality, domain=None, range=Optional[Union[str, "DirectionalityEnum"]])

slots.percentage_active_transport = Slot(uri=ASSAY_MICROSCHEMAS.percentage_active_transport, name="percentage_active_transport", curie=ASSAY_MICROSCHEMAS.curie('percentage_active_transport'),
                   model_uri=SOMA.percentage_active_transport, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.particle_clearance_time = Slot(uri=ASSAY_MICROSCHEMAS.particle_clearance_time, name="particle_clearance_time", curie=ASSAY_MICROSCHEMAS.curie('particle_clearance_time'),
                   model_uri=SOMA.particle_clearance_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mucus_composition = Slot(uri=ASSAY_MICROSCHEMAS.mucus_composition, name="mucus_composition", curie=ASSAY_MICROSCHEMAS.curie('mucus_composition'),
                   model_uri=SOMA.mucus_composition, domain=None, range=Optional[str])

slots.reactive_oxygen_species = Slot(uri=ASSAY_MICROSCHEMAS.reactive_oxygen_species, name="reactive_oxygen_species", curie=ASSAY_MICROSCHEMAS.curie('reactive_oxygen_species'),
                   model_uri=SOMA.reactive_oxygen_species, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.ros_probe_type = Slot(uri=ASSAY_MICROSCHEMAS.ros_probe_type, name="ros_probe_type", curie=ASSAY_MICROSCHEMAS.curie('ros_probe_type'),
                   model_uri=SOMA.ros_probe_type, domain=None, range=Optional[str])

slots.lipid_peroxidation = Slot(uri=ASSAY_MICROSCHEMAS.lipid_peroxidation, name="lipid_peroxidation", curie=ASSAY_MICROSCHEMAS.curie('lipid_peroxidation'),
                   model_uri=SOMA.lipid_peroxidation, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.malondialdehyde_level = Slot(uri=ASSAY_MICROSCHEMAS.malondialdehyde_level, name="malondialdehyde_level", curie=ASSAY_MICROSCHEMAS.curie('malondialdehyde_level'),
                   model_uri=SOMA.malondialdehyde_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.four_hydroxynonenal_level = Slot(uri=ASSAY_MICROSCHEMAS.four_hydroxynonenal_level, name="four_hydroxynonenal_level", curie=ASSAY_MICROSCHEMAS.curie('four_hydroxynonenal_level'),
                   model_uri=SOMA.four_hydroxynonenal_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.eight_isoprostane_level = Slot(uri=ASSAY_MICROSCHEMAS.eight_isoprostane_level, name="eight_isoprostane_level", curie=ASSAY_MICROSCHEMAS.curie('eight_isoprostane_level'),
                   model_uri=SOMA.eight_isoprostane_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.protein_oxidation_markers = Slot(uri=ASSAY_MICROSCHEMAS.protein_oxidation_markers, name="protein_oxidation_markers", curie=ASSAY_MICROSCHEMAS.curie('protein_oxidation_markers'),
                   model_uri=SOMA.protein_oxidation_markers, domain=None, range=Optional[Union[str, list[str]]])

slots.protein_carbonyl_content = Slot(uri=ASSAY_MICROSCHEMAS.protein_carbonyl_content, name="protein_carbonyl_content", curie=ASSAY_MICROSCHEMAS.curie('protein_carbonyl_content'),
                   model_uri=SOMA.protein_carbonyl_content, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.nitrotyrosine_level = Slot(uri=ASSAY_MICROSCHEMAS.nitrotyrosine_level, name="nitrotyrosine_level", curie=ASSAY_MICROSCHEMAS.curie('nitrotyrosine_level'),
                   model_uri=SOMA.nitrotyrosine_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dna_damage_markers = Slot(uri=ASSAY_MICROSCHEMAS.dna_damage_markers, name="dna_damage_markers", curie=ASSAY_MICROSCHEMAS.curie('dna_damage_markers'),
                   model_uri=SOMA.dna_damage_markers, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.eight_ohdg_level = Slot(uri=ASSAY_MICROSCHEMAS.eight_ohdg_level, name="eight_ohdg_level", curie=ASSAY_MICROSCHEMAS.curie('eight_ohdg_level'),
                   model_uri=SOMA.eight_ohdg_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.antioxidant_capacity = Slot(uri=ASSAY_MICROSCHEMAS.antioxidant_capacity, name="antioxidant_capacity", curie=ASSAY_MICROSCHEMAS.curie('antioxidant_capacity'),
                   model_uri=SOMA.antioxidant_capacity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.glutathione_ratio = Slot(uri=ASSAY_MICROSCHEMAS.glutathione_ratio, name="glutathione_ratio", curie=ASSAY_MICROSCHEMAS.curie('glutathione_ratio'),
                   model_uri=SOMA.glutathione_ratio, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.antioxidant_enzyme_activities = Slot(uri=ASSAY_MICROSCHEMAS.antioxidant_enzyme_activities, name="antioxidant_enzyme_activities", curie=ASSAY_MICROSCHEMAS.curie('antioxidant_enzyme_activities'),
                   model_uri=SOMA.antioxidant_enzyme_activities, domain=None, range=Optional[str])

slots.superoxide_dismutase_activity = Slot(uri=ASSAY_MICROSCHEMAS.superoxide_dismutase_activity, name="superoxide_dismutase_activity", curie=ASSAY_MICROSCHEMAS.curie('superoxide_dismutase_activity'),
                   model_uri=SOMA.superoxide_dismutase_activity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.catalase_activity = Slot(uri=ASSAY_MICROSCHEMAS.catalase_activity, name="catalase_activity", curie=ASSAY_MICROSCHEMAS.curie('catalase_activity'),
                   model_uri=SOMA.catalase_activity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.glutathione_peroxidase_activity = Slot(uri=ASSAY_MICROSCHEMAS.glutathione_peroxidase_activity, name="glutathione_peroxidase_activity", curie=ASSAY_MICROSCHEMAS.curie('glutathione_peroxidase_activity'),
                   model_uri=SOMA.glutathione_peroxidase_activity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.total_antioxidant_capacity = Slot(uri=ASSAY_MICROSCHEMAS.total_antioxidant_capacity, name="total_antioxidant_capacity", curie=ASSAY_MICROSCHEMAS.curie('total_antioxidant_capacity'),
                   model_uri=SOMA.total_antioxidant_capacity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.nrf2_activation = Slot(uri=ASSAY_MICROSCHEMAS.nrf2_activation, name="nrf2_activation", curie=ASSAY_MICROSCHEMAS.curie('nrf2_activation'),
                   model_uri=SOMA.nrf2_activation, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.detection_method_details = Slot(uri=ASSAY_MICROSCHEMAS.detection_method_details, name="detection_method_details", curie=ASSAY_MICROSCHEMAS.curie('detection_method_details'),
                   model_uri=SOMA.detection_method_details, domain=None, range=Optional[Union[str, list[str]]])

slots.cftr_chloride_secretion = Slot(uri=ASSAY_MICROSCHEMAS.cftr_chloride_secretion, name="cftr_chloride_secretion", curie=ASSAY_MICROSCHEMAS.curie('cftr_chloride_secretion'),
                   model_uri=SOMA.cftr_chloride_secretion, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cftr_forskolin_response = Slot(uri=ASSAY_MICROSCHEMAS.cftr_forskolin_response, name="cftr_forskolin_response", curie=ASSAY_MICROSCHEMAS.curie('cftr_forskolin_response'),
                   model_uri=SOMA.cftr_forskolin_response, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.inhibitor_sensitive_current = Slot(uri=ASSAY_MICROSCHEMAS.inhibitor_sensitive_current, name="inhibitor_sensitive_current", curie=ASSAY_MICROSCHEMAS.curie('inhibitor_sensitive_current'),
                   model_uri=SOMA.inhibitor_sensitive_current, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cftr_specific_current = Slot(uri=ASSAY_MICROSCHEMAS.cftr_specific_current, name="cftr_specific_current", curie=ASSAY_MICROSCHEMAS.curie('cftr_specific_current'),
                   model_uri=SOMA.cftr_specific_current, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sweat_chloride_concentration = Slot(uri=ASSAY_MICROSCHEMAS.sweat_chloride_concentration, name="sweat_chloride_concentration", curie=ASSAY_MICROSCHEMAS.curie('sweat_chloride_concentration'),
                   model_uri=SOMA.sweat_chloride_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.nasal_potential_difference = Slot(uri=ASSAY_MICROSCHEMAS.nasal_potential_difference, name="nasal_potential_difference", curie=ASSAY_MICROSCHEMAS.curie('nasal_potential_difference'),
                   model_uri=SOMA.nasal_potential_difference, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.stimulation_agent = Slot(uri=ASSAY_MICROSCHEMAS.stimulation_agent, name="stimulation_agent", curie=ASSAY_MICROSCHEMAS.curie('stimulation_agent'),
                   model_uri=SOMA.stimulation_agent, domain=None, range=Optional[str])

slots.inhibitor_used = Slot(uri=ASSAY_MICROSCHEMAS.inhibitor_used, name="inhibitor_used", curie=ASSAY_MICROSCHEMAS.curie('inhibitor_used'),
                   model_uri=SOMA.inhibitor_used, domain=None, range=Optional[str])

slots.egfr_phosphorylation_y1068 = Slot(uri=ASSAY_MICROSCHEMAS.egfr_phosphorylation_y1068, name="egfr_phosphorylation_y1068", curie=ASSAY_MICROSCHEMAS.curie('egfr_phosphorylation_y1068'),
                   model_uri=SOMA.egfr_phosphorylation_y1068, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.egfr_phosphorylation_y1173 = Slot(uri=ASSAY_MICROSCHEMAS.egfr_phosphorylation_y1173, name="egfr_phosphorylation_y1173", curie=ASSAY_MICROSCHEMAS.curie('egfr_phosphorylation_y1173'),
                   model_uri=SOMA.egfr_phosphorylation_y1173, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.total_egfr_protein = Slot(uri=ASSAY_MICROSCHEMAS.total_egfr_protein, name="total_egfr_protein", curie=ASSAY_MICROSCHEMAS.curie('total_egfr_protein'),
                   model_uri=SOMA.total_egfr_protein, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.downstream_kinase_activation = Slot(uri=ASSAY_MICROSCHEMAS.downstream_kinase_activation, name="downstream_kinase_activation", curie=ASSAY_MICROSCHEMAS.curie('downstream_kinase_activation'),
                   model_uri=SOMA.downstream_kinase_activation, domain=None, range=Optional[str])

slots.erk_phosphorylation = Slot(uri=ASSAY_MICROSCHEMAS.erk_phosphorylation, name="erk_phosphorylation", curie=ASSAY_MICROSCHEMAS.curie('erk_phosphorylation'),
                   model_uri=SOMA.erk_phosphorylation, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.akt_phosphorylation = Slot(uri=ASSAY_MICROSCHEMAS.akt_phosphorylation, name="akt_phosphorylation", curie=ASSAY_MICROSCHEMAS.curie('akt_phosphorylation'),
                   model_uri=SOMA.akt_phosphorylation, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.pathway_biomarkers = Slot(uri=ASSAY_MICROSCHEMAS.pathway_biomarkers, name="pathway_biomarkers", curie=ASSAY_MICROSCHEMAS.curie('pathway_biomarkers'),
                   model_uri=SOMA.pathway_biomarkers, domain=None, range=Optional[Union[str, list[str]]])

slots.egfr_ligand_expression = Slot(uri=ASSAY_MICROSCHEMAS.egfr_ligand_expression, name="egfr_ligand_expression", curie=ASSAY_MICROSCHEMAS.curie('egfr_ligand_expression'),
                   model_uri=SOMA.egfr_ligand_expression, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.egfr_membrane_localization = Slot(uri=ASSAY_MICROSCHEMAS.egfr_membrane_localization, name="egfr_membrane_localization", curie=ASSAY_MICROSCHEMAS.curie('egfr_membrane_localization'),
                   model_uri=SOMA.egfr_membrane_localization, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.normalization_reference = Slot(uri=ASSAY_MICROSCHEMAS.normalization_reference, name="normalization_reference", curie=ASSAY_MICROSCHEMAS.curie('normalization_reference'),
                   model_uri=SOMA.normalization_reference, domain=None, range=Optional[str])

slots.phosphorylation_site = Slot(uri=ASSAY_MICROSCHEMAS.phosphorylation_site, name="phosphorylation_site", curie=ASSAY_MICROSCHEMAS.curie('phosphorylation_site'),
                   model_uri=SOMA.phosphorylation_site, domain=None, range=Optional[str])

slots.goblet_cell_count = Slot(uri=ASSAY_MICROSCHEMAS.goblet_cell_count, name="goblet_cell_count", curie=ASSAY_MICROSCHEMAS.curie('goblet_cell_count'),
                   model_uri=SOMA.goblet_cell_count, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.goblet_cell_percentage = Slot(uri=ASSAY_MICROSCHEMAS.goblet_cell_percentage, name="goblet_cell_percentage", curie=ASSAY_MICROSCHEMAS.curie('goblet_cell_percentage'),
                   model_uri=SOMA.goblet_cell_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.muc5ac_mrna_expression = Slot(uri=ASSAY_MICROSCHEMAS.muc5ac_mrna_expression, name="muc5ac_mrna_expression", curie=ASSAY_MICROSCHEMAS.curie('muc5ac_mrna_expression'),
                   model_uri=SOMA.muc5ac_mrna_expression, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.muc5ac_protein_expression = Slot(uri=ASSAY_MICROSCHEMAS.muc5ac_protein_expression, name="muc5ac_protein_expression", curie=ASSAY_MICROSCHEMAS.curie('muc5ac_protein_expression'),
                   model_uri=SOMA.muc5ac_protein_expression, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.muc5b_mrna_expression = Slot(uri=ASSAY_MICROSCHEMAS.muc5b_mrna_expression, name="muc5b_mrna_expression", curie=ASSAY_MICROSCHEMAS.curie('muc5b_mrna_expression'),
                   model_uri=SOMA.muc5b_mrna_expression, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.muc5b_protein_expression = Slot(uri=ASSAY_MICROSCHEMAS.muc5b_protein_expression, name="muc5b_protein_expression", curie=ASSAY_MICROSCHEMAS.curie('muc5b_protein_expression'),
                   model_uri=SOMA.muc5b_protein_expression, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.muc5ac_muc5b_ratio = Slot(uri=ASSAY_MICROSCHEMAS.muc5ac_muc5b_ratio, name="muc5ac_muc5b_ratio", curie=ASSAY_MICROSCHEMAS.curie('muc5ac_muc5b_ratio'),
                   model_uri=SOMA.muc5ac_muc5b_ratio, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mucin_protein_concentration = Slot(uri=ASSAY_MICROSCHEMAS.mucin_protein_concentration, name="mucin_protein_concentration", curie=ASSAY_MICROSCHEMAS.curie('mucin_protein_concentration'),
                   model_uri=SOMA.mucin_protein_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mucin_secretion_rate = Slot(uri=ASSAY_MICROSCHEMAS.mucin_secretion_rate, name="mucin_secretion_rate", curie=ASSAY_MICROSCHEMAS.curie('mucin_secretion_rate'),
                   model_uri=SOMA.mucin_secretion_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.percent_solids = Slot(uri=ASSAY_MICROSCHEMAS.percent_solids, name="percent_solids", curie=ASSAY_MICROSCHEMAS.curie('percent_solids'),
                   model_uri=SOMA.percent_solids, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.goblet_to_ciliated_ratio = Slot(uri=ASSAY_MICROSCHEMAS.goblet_to_ciliated_ratio, name="goblet_to_ciliated_ratio", curie=ASSAY_MICROSCHEMAS.curie('goblet_to_ciliated_ratio'),
                   model_uri=SOMA.goblet_to_ciliated_ratio, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.mucus_viscosity = Slot(uri=ASSAY_MICROSCHEMAS.mucus_viscosity, name="mucus_viscosity", curie=ASSAY_MICROSCHEMAS.curie('mucus_viscosity'),
                   model_uri=SOMA.mucus_viscosity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.imaging_protocol = Slot(uri=ASSAY_MICROSCHEMAS.imaging_protocol, name="imaging_protocol", curie=ASSAY_MICROSCHEMAS.curie('imaging_protocol'),
                   model_uri=SOMA.imaging_protocol, domain=None, range=Optional[Union[dict, ImagingProtocol]])

slots.staining_protocol = Slot(uri=ASSAY_MICROSCHEMAS.staining_protocol, name="staining_protocol", curie=ASSAY_MICROSCHEMAS.curie('staining_protocol'),
                   model_uri=SOMA.staining_protocol, domain=None, range=Optional[Union[dict, StainingProtocol]])

slots.molecular_protocol = Slot(uri=ASSAY_MICROSCHEMAS.molecular_protocol, name="molecular_protocol", curie=ASSAY_MICROSCHEMAS.curie('molecular_protocol'),
                   model_uri=SOMA.molecular_protocol, domain=None, range=Optional[Union[dict, MolecularAssayProtocol]])

slots.spirometry_protocol = Slot(uri=ASSAY_MICROSCHEMAS.spirometry_protocol, name="spirometry_protocol", curie=ASSAY_MICROSCHEMAS.curie('spirometry_protocol'),
                   model_uri=SOMA.spirometry_protocol, domain=None, range=Optional[Union[dict, SpirometryProtocol]])

slots.neutrophil_percentage = Slot(uri=ASSAY_MICROSCHEMAS.neutrophil_percentage, name="neutrophil_percentage", curie=ASSAY_MICROSCHEMAS.curie('neutrophil_percentage'),
                   model_uri=SOMA.neutrophil_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.eosinophil_percentage = Slot(uri=ASSAY_MICROSCHEMAS.eosinophil_percentage, name="eosinophil_percentage", curie=ASSAY_MICROSCHEMAS.curie('eosinophil_percentage'),
                   model_uri=SOMA.eosinophil_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.macrophage_percentage = Slot(uri=ASSAY_MICROSCHEMAS.macrophage_percentage, name="macrophage_percentage", curie=ASSAY_MICROSCHEMAS.curie('macrophage_percentage'),
                   model_uri=SOMA.macrophage_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.lymphocyte_percentage = Slot(uri=ASSAY_MICROSCHEMAS.lymphocyte_percentage, name="lymphocyte_percentage", curie=ASSAY_MICROSCHEMAS.curie('lymphocyte_percentage'),
                   model_uri=SOMA.lymphocyte_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.total_cell_count = Slot(uri=ASSAY_MICROSCHEMAS.total_cell_count, name="total_cell_count", curie=ASSAY_MICROSCHEMAS.curie('total_cell_count'),
                   model_uri=SOMA.total_cell_count, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.il6_concentration = Slot(uri=ASSAY_MICROSCHEMAS.il6_concentration, name="il6_concentration", curie=ASSAY_MICROSCHEMAS.curie('il6_concentration'),
                   model_uri=SOMA.il6_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.il8_concentration = Slot(uri=ASSAY_MICROSCHEMAS.il8_concentration, name="il8_concentration", curie=ASSAY_MICROSCHEMAS.curie('il8_concentration'),
                   model_uri=SOMA.il8_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tnf_alpha_concentration = Slot(uri=ASSAY_MICROSCHEMAS.tnf_alpha_concentration, name="tnf_alpha_concentration", curie=ASSAY_MICROSCHEMAS.curie('tnf_alpha_concentration'),
                   model_uri=SOMA.tnf_alpha_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.il1_beta_concentration = Slot(uri=ASSAY_MICROSCHEMAS.il1_beta_concentration, name="il1_beta_concentration", curie=ASSAY_MICROSCHEMAS.curie('il1_beta_concentration'),
                   model_uri=SOMA.il1_beta_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.total_protein_concentration = Slot(uri=ASSAY_MICROSCHEMAS.total_protein_concentration, name="total_protein_concentration", curie=ASSAY_MICROSCHEMAS.curie('total_protein_concentration'),
                   model_uri=SOMA.total_protein_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.alpha_diversity = Slot(uri=ASSAY_MICROSCHEMAS.alpha_diversity, name="alpha_diversity", curie=ASSAY_MICROSCHEMAS.curie('alpha_diversity'),
                   model_uri=SOMA.alpha_diversity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.beta_diversity = Slot(uri=ASSAY_MICROSCHEMAS.beta_diversity, name="beta_diversity", curie=ASSAY_MICROSCHEMAS.curie('beta_diversity'),
                   model_uri=SOMA.beta_diversity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bacterial_load = Slot(uri=ASSAY_MICROSCHEMAS.bacterial_load, name="bacterial_load", curie=ASSAY_MICROSCHEMAS.curie('bacterial_load'),
                   model_uri=SOMA.bacterial_load, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cell_free_dna = Slot(uri=ASSAY_MICROSCHEMAS.cell_free_dna, name="cell_free_dna", curie=ASSAY_MICROSCHEMAS.curie('cell_free_dna'),
                   model_uri=SOMA.cell_free_dna, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fev1 = Slot(uri=ASSAY_MICROSCHEMAS.fev1, name="fev1", curie=ASSAY_MICROSCHEMAS.curie('fev1'),
                   model_uri=SOMA.fev1, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fvc = Slot(uri=ASSAY_MICROSCHEMAS.fvc, name="fvc", curie=ASSAY_MICROSCHEMAS.curie('fvc'),
                   model_uri=SOMA.fvc, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.reference_dataset = Slot(uri=ASSAY_MICROSCHEMAS.reference_dataset, name="reference_dataset", curie=ASSAY_MICROSCHEMAS.curie('reference_dataset'),
                   model_uri=SOMA.reference_dataset, domain=None, range=Optional[str])

slots.fev1_fvc_ratio = Slot(uri=ASSAY_MICROSCHEMAS.fev1_fvc_ratio, name="fev1_fvc_ratio", curie=ASSAY_MICROSCHEMAS.curie('fev1_fvc_ratio'),
                   model_uri=SOMA.fev1_fvc_ratio, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.feno = Slot(uri=ASSAY_MICROSCHEMAS.feno, name="feno", curie=ASSAY_MICROSCHEMAS.curie('feno'),
                   model_uri=SOMA.feno, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.decline_rate = Slot(uri=ASSAY_MICROSCHEMAS.decline_rate, name="decline_rate", curie=ASSAY_MICROSCHEMAS.curie('decline_rate'),
                   model_uri=SOMA.decline_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bronchodilator_response = Slot(uri=ASSAY_MICROSCHEMAS.bronchodilator_response, name="bronchodilator_response", curie=ASSAY_MICROSCHEMAS.curie('bronchodilator_response'),
                   model_uri=SOMA.bronchodilator_response, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dlco = Slot(uri=ASSAY_MICROSCHEMAS.dlco, name="dlco", curie=ASSAY_MICROSCHEMAS.curie('dlco'),
                   model_uri=SOMA.dlco, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.hemoglobin_level = Slot(uri=ASSAY_MICROSCHEMAS.hemoglobin_level, name="hemoglobin_level", curie=ASSAY_MICROSCHEMAS.curie('hemoglobin_level'),
                   model_uri=SOMA.hemoglobin_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.recent_respiratory_illness = Slot(uri=ASSAY_MICROSCHEMAS.recent_respiratory_illness, name="recent_respiratory_illness", curie=ASSAY_MICROSCHEMAS.curie('recent_respiratory_illness'),
                   model_uri=SOMA.recent_respiratory_illness, domain=None, range=Optional[str])

slots.peak_expiratory_flow = Slot(uri=ASSAY_MICROSCHEMAS.peak_expiratory_flow, name="peak_expiratory_flow", curie=ASSAY_MICROSCHEMAS.curie('peak_expiratory_flow'),
                   model_uri=SOMA.peak_expiratory_flow, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fef25_75 = Slot(uri=ASSAY_MICROSCHEMAS.fef25_75, name="fef25_75", curie=ASSAY_MICROSCHEMAS.curie('fef25_75'),
                   model_uri=SOMA.fef25_75, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.total_lung_capacity = Slot(uri=ASSAY_MICROSCHEMAS.total_lung_capacity, name="total_lung_capacity", curie=ASSAY_MICROSCHEMAS.curie('total_lung_capacity'),
                   model_uri=SOMA.total_lung_capacity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.functional_residual_capacity = Slot(uri=ASSAY_MICROSCHEMAS.functional_residual_capacity, name="functional_residual_capacity", curie=ASSAY_MICROSCHEMAS.curie('functional_residual_capacity'),
                   model_uri=SOMA.functional_residual_capacity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.residual_volume = Slot(uri=ASSAY_MICROSCHEMAS.residual_volume, name="residual_volume", curie=ASSAY_MICROSCHEMAS.curie('residual_volume'),
                   model_uri=SOMA.residual_volume, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.lung_compliance = Slot(uri=ASSAY_MICROSCHEMAS.lung_compliance, name="lung_compliance", curie=ASSAY_MICROSCHEMAS.curie('lung_compliance'),
                   model_uri=SOMA.lung_compliance, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.lung_elastance = Slot(uri=ASSAY_MICROSCHEMAS.lung_elastance, name="lung_elastance", curie=ASSAY_MICROSCHEMAS.curie('lung_elastance'),
                   model_uri=SOMA.lung_elastance, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.lung_resistance = Slot(uri=ASSAY_MICROSCHEMAS.lung_resistance, name="lung_resistance", curie=ASSAY_MICROSCHEMAS.curie('lung_resistance'),
                   model_uri=SOMA.lung_resistance, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.foxj1_mrna_expression = Slot(uri=ASSAY_MICROSCHEMAS.foxj1_mrna_expression, name="foxj1_mrna_expression", curie=ASSAY_MICROSCHEMAS.curie('foxj1_mrna_expression'),
                   model_uri=SOMA.foxj1_mrna_expression, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.foxj1_protein_expression = Slot(uri=ASSAY_MICROSCHEMAS.foxj1_protein_expression, name="foxj1_protein_expression", curie=ASSAY_MICROSCHEMAS.curie('foxj1_protein_expression'),
                   model_uri=SOMA.foxj1_protein_expression, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.foxj1_positive_cell_percentage = Slot(uri=ASSAY_MICROSCHEMAS.foxj1_positive_cell_percentage, name="foxj1_positive_cell_percentage", curie=ASSAY_MICROSCHEMAS.curie('foxj1_positive_cell_percentage'),
                   model_uri=SOMA.foxj1_positive_cell_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.foxj1_nuclear_localization = Slot(uri=ASSAY_MICROSCHEMAS.foxj1_nuclear_localization, name="foxj1_nuclear_localization", curie=ASSAY_MICROSCHEMAS.curie('foxj1_nuclear_localization'),
                   model_uri=SOMA.foxj1_nuclear_localization, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.target_gene = Slot(uri=ASSAY_MICROSCHEMAS.target_gene, name="target_gene", curie=ASSAY_MICROSCHEMAS.curie('target_gene'),
                   model_uri=SOMA.target_gene, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.mrna_level = Slot(uri=ASSAY_MICROSCHEMAS.mrna_level, name="mrna_level", curie=ASSAY_MICROSCHEMAS.curie('mrna_level'),
                   model_uri=SOMA.mrna_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.protein_level = Slot(uri=ASSAY_MICROSCHEMAS.protein_level, name="protein_level", curie=ASSAY_MICROSCHEMAS.curie('protein_level'),
                   model_uri=SOMA.protein_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.percentage_positive_cells = Slot(uri=ASSAY_MICROSCHEMAS.percentage_positive_cells, name="percentage_positive_cells", curie=ASSAY_MICROSCHEMAS.curie('percentage_positive_cells'),
                   model_uri=SOMA.percentage_positive_cells, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.gene_expression_method = Slot(uri=ASSAY_MICROSCHEMAS.gene_expression_method, name="gene_expression_method", curie=ASSAY_MICROSCHEMAS.curie('gene_expression_method'),
                   model_uri=SOMA.gene_expression_method, domain=None, range=Optional[str])

slots.Unit_id = Slot(uri=AOP_FRAMEWORK.id, name="Unit_id", curie=AOP_FRAMEWORK.curie('id'),
                   model_uri=SOMA.Unit_id, domain=Unit, range=Union[str, UnitId],
                   pattern=re.compile(r'^(UO:\d{7}|UCUM:\S+|QUDT:\S+)$'))

slots.CellTypeReference_id = Slot(uri=AOP_FRAMEWORK.id, name="CellTypeReference_id", curie=AOP_FRAMEWORK.curie('id'),
                   model_uri=SOMA.CellTypeReference_id, domain=CellTypeReference, range=Union[str, CellTypeReferenceId],
                   pattern=re.compile(r'^CL:\d{7}$'))

slots.SpeciesReference_id = Slot(uri=AOP_FRAMEWORK.id, name="SpeciesReference_id", curie=AOP_FRAMEWORK.curie('id'),
                   model_uri=SOMA.SpeciesReference_id, domain=SpeciesReference, range=Union[str, SpeciesReferenceId],
                   pattern=re.compile(r'^NCBITaxon:\d+$'))

slots.ChemicalEntityReference_id = Slot(uri=AOP_FRAMEWORK.id, name="ChemicalEntityReference_id", curie=AOP_FRAMEWORK.curie('id'),
                   model_uri=SOMA.ChemicalEntityReference_id, domain=ChemicalEntityReference, range=Union[str, ChemicalEntityReferenceId],
                   pattern=re.compile(r'^(CHEBI:\d+|ECTO:\d{7})$'))

slots.AnatomicalEntityReference_id = Slot(uri=AOP_FRAMEWORK.id, name="AnatomicalEntityReference_id", curie=AOP_FRAMEWORK.curie('id'),
                   model_uri=SOMA.AnatomicalEntityReference_id, domain=AnatomicalEntityReference, range=Union[str, AnatomicalEntityReferenceId],
                   pattern=re.compile(r'^UBERON:\d{7}$'))

slots.CellLine_id = Slot(uri=AOP_FRAMEWORK.id, name="CellLine_id", curie=AOP_FRAMEWORK.curie('id'),
                   model_uri=SOMA.CellLine_id, domain=CellLine, range=Union[str, CellLineId],
                   pattern=re.compile(r'^CLO:\d{7}$'))

slots.CiliaryFunctionAssay_study_subject = Slot(uri=ASSAY_BASE.study_subject, name="CiliaryFunctionAssay_study_subject", curie=ASSAY_BASE.curie('study_subject'),
                   model_uri=SOMA.CiliaryFunctionAssay_study_subject, domain=CiliaryFunctionAssay, range=Optional[Union[dict, StudySubject]])

slots.CiliaryFunctionAssay_has_specified_output = Slot(uri=ASSAY_BASE.has_specified_output, name="CiliaryFunctionAssay_has_specified_output", curie=ASSAY_BASE.curie('has_specified_output'),
                   model_uri=SOMA.CiliaryFunctionAssay_has_specified_output, domain=CiliaryFunctionAssay, range=Optional[Union[dict, "CiliaryFunctionOutput"]])

slots.ASLAssay_has_specified_output = Slot(uri=ASSAY_BASE.has_specified_output, name="ASLAssay_has_specified_output", curie=ASSAY_BASE.curie('has_specified_output'),
                   model_uri=SOMA.ASLAssay_has_specified_output, domain=ASLAssay, range=Optional[Union[dict, "ASLOutput"]])

slots.MucociliaryClearanceAssay_has_specified_output = Slot(uri=ASSAY_BASE.has_specified_output, name="MucociliaryClearanceAssay_has_specified_output", curie=ASSAY_BASE.curie('has_specified_output'),
                   model_uri=SOMA.MucociliaryClearanceAssay_has_specified_output, domain=MucociliaryClearanceAssay, range=Optional[Union[dict, "MucociliaryClearanceOutput"]])

slots.OxidativeStressAssay_has_specified_output = Slot(uri=ASSAY_BASE.has_specified_output, name="OxidativeStressAssay_has_specified_output", curie=ASSAY_BASE.curie('has_specified_output'),
                   model_uri=SOMA.OxidativeStressAssay_has_specified_output, domain=OxidativeStressAssay, range=Optional[Union[dict, "OxidativeStressOutput"]])

slots.CFTRFunctionAssay_has_specified_output = Slot(uri=ASSAY_BASE.has_specified_output, name="CFTRFunctionAssay_has_specified_output", curie=ASSAY_BASE.curie('has_specified_output'),
                   model_uri=SOMA.CFTRFunctionAssay_has_specified_output, domain=CFTRFunctionAssay, range=Optional[Union[dict, "CFTRFunctionOutput"]])

slots.EGFRSignalingAssay_has_specified_output = Slot(uri=ASSAY_BASE.has_specified_output, name="EGFRSignalingAssay_has_specified_output", curie=ASSAY_BASE.curie('has_specified_output'),
                   model_uri=SOMA.EGFRSignalingAssay_has_specified_output, domain=EGFRSignalingAssay, range=Optional[Union[dict, "EGFRSignalingOutput"]])

slots.GobletCellAssay_has_specified_output = Slot(uri=ASSAY_BASE.has_specified_output, name="GobletCellAssay_has_specified_output", curie=ASSAY_BASE.curie('has_specified_output'),
                   model_uri=SOMA.GobletCellAssay_has_specified_output, domain=GobletCellAssay, range=Optional[Union[dict, "GobletCellOutput"]])

slots.BALFSputumAssay_study_subject = Slot(uri=ASSAY_BASE.study_subject, name="BALFSputumAssay_study_subject", curie=ASSAY_BASE.curie('study_subject'),
                   model_uri=SOMA.BALFSputumAssay_study_subject, domain=BALFSputumAssay, range=Optional[Union[dict, InVivoSubject]])

slots.BALFSputumAssay_has_specified_output = Slot(uri=ASSAY_BASE.has_specified_output, name="BALFSputumAssay_has_specified_output", curie=ASSAY_BASE.curie('has_specified_output'),
                   model_uri=SOMA.BALFSputumAssay_has_specified_output, domain=BALFSputumAssay, range=Optional[Union[dict, "BALFSputumOutput"]])

slots.LungFunctionAssay_study_subject = Slot(uri=ASSAY_BASE.study_subject, name="LungFunctionAssay_study_subject", curie=ASSAY_BASE.curie('study_subject'),
                   model_uri=SOMA.LungFunctionAssay_study_subject, domain=LungFunctionAssay, range=Optional[Union[dict, InVivoSubject]])

slots.LungFunctionAssay_has_specified_output = Slot(uri=ASSAY_BASE.has_specified_output, name="LungFunctionAssay_has_specified_output", curie=ASSAY_BASE.curie('has_specified_output'),
                   model_uri=SOMA.LungFunctionAssay_has_specified_output, domain=LungFunctionAssay, range=Optional[Union[dict, "LungFunctionOutput"]])

slots.FoxJExpressionAssay_has_specified_output = Slot(uri=ASSAY_BASE.has_specified_output, name="FoxJExpressionAssay_has_specified_output", curie=ASSAY_BASE.curie('has_specified_output'),
                   model_uri=SOMA.FoxJExpressionAssay_has_specified_output, domain=FoxJExpressionAssay, range=Optional[Union[dict, "FoxJExpressionOutput"]])

slots.GeneExpressionAssay_has_specified_output = Slot(uri=ASSAY_BASE.has_specified_output, name="GeneExpressionAssay_has_specified_output", curie=ASSAY_BASE.curie('has_specified_output'),
                   model_uri=SOMA.GeneExpressionAssay_has_specified_output, domain=GeneExpressionAssay, range=Optional[Union[dict, "GeneExpressionOutput"]])
