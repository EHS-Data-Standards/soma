# Auto generated from outcomes_working_group.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-02-02T12:47:28
# Schema: outcomes_working_group
#
# id: https://w3id.org/EHS-Data-Standards/outcomes_working_group
# description: A LinkML data model for representing biological measurements, assays, and experimental protocols in the context of outcomes research. This is the main entry point that imports the measurement base schema and domain-specific microschemas.
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
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
QUDT = CurieNamespace('QUDT', 'http://example.org/UNKNOWN/QUDT/')
UCUM = CurieNamespace('UCUM', 'http://example.org/UNKNOWN/UCUM/')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MEASUREMENT_BASE = CurieNamespace('measurement_base', 'https://w3id.org/EHS-Data-Standards/measurement_base/')
MEASUREMENT_MICROSCHEMAS = CurieNamespace('measurement_microschemas', 'https://w3id.org/EHS-Data-Standards/measurement_microschemas/')
OUTCOMES_WORKING_GROUP = CurieNamespace('outcomes_working_group', 'https://w3id.org/EHS-Data-Standards/outcomes_working_group/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = OUTCOMES_WORKING_GROUP


# Types

# Class references
class MeasurementId(URIorCURIE):
    pass


class AssayId(URIorCURIE):
    pass


class MethodId(URIorCURIE):
    pass


class ProtocolId(URIorCURIE):
    pass


class UnitId(URIorCURIE):
    pass


class NamedEntityId(URIorCURIE):
    pass


class CiliaryFunctionMeasurementId(URIorCURIE):
    pass


class ASLMeasurementId(URIorCURIE):
    pass


class MCCMeasurementId(URIorCURIE):
    pass


class OxidativeStressMeasurementId(URIorCURIE):
    pass


class CFTRMeasurementId(URIorCURIE):
    pass


class EGFRMeasurementId(URIorCURIE):
    pass


class GobletCellMucinMeasurementId(URIorCURIE):
    pass


class BALFSputumMeasurementId(URIorCURIE):
    pass


class LungFunctionMeasurementId(URIorCURIE):
    pass


class FoxJMeasurementId(URIorCURIE):
    pass


class ExposureBiomarkerMeasurementId(URIorCURIE):
    pass


@dataclass(repr=False)
class Container(YAMLRoot):
    """
    A container for collections of measurements and related entities. Used as the root class for data validation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP["Container"]
    class_class_curie: ClassVar[str] = "outcomes_working_group:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.Container

    ciliary_measurements: Optional[Union[dict[Union[str, CiliaryFunctionMeasurementId], Union[dict, "CiliaryFunctionMeasurement"]], list[Union[dict, "CiliaryFunctionMeasurement"]]]] = empty_dict()
    asl_measurements: Optional[Union[dict[Union[str, ASLMeasurementId], Union[dict, "ASLMeasurement"]], list[Union[dict, "ASLMeasurement"]]]] = empty_dict()
    mcc_measurements: Optional[Union[dict[Union[str, MCCMeasurementId], Union[dict, "MCCMeasurement"]], list[Union[dict, "MCCMeasurement"]]]] = empty_dict()
    oxidative_stress_measurements: Optional[Union[dict[Union[str, OxidativeStressMeasurementId], Union[dict, "OxidativeStressMeasurement"]], list[Union[dict, "OxidativeStressMeasurement"]]]] = empty_dict()
    cftr_measurements: Optional[Union[dict[Union[str, CFTRMeasurementId], Union[dict, "CFTRMeasurement"]], list[Union[dict, "CFTRMeasurement"]]]] = empty_dict()
    egfr_measurements: Optional[Union[dict[Union[str, EGFRMeasurementId], Union[dict, "EGFRMeasurement"]], list[Union[dict, "EGFRMeasurement"]]]] = empty_dict()
    goblet_cell_mucin_measurements: Optional[Union[dict[Union[str, GobletCellMucinMeasurementId], Union[dict, "GobletCellMucinMeasurement"]], list[Union[dict, "GobletCellMucinMeasurement"]]]] = empty_dict()
    balf_sputum_measurements: Optional[Union[dict[Union[str, BALFSputumMeasurementId], Union[dict, "BALFSputumMeasurement"]], list[Union[dict, "BALFSputumMeasurement"]]]] = empty_dict()
    lung_function_measurements: Optional[Union[dict[Union[str, LungFunctionMeasurementId], Union[dict, "LungFunctionMeasurement"]], list[Union[dict, "LungFunctionMeasurement"]]]] = empty_dict()
    foxj_measurements: Optional[Union[dict[Union[str, FoxJMeasurementId], Union[dict, "FoxJMeasurement"]], list[Union[dict, "FoxJMeasurement"]]]] = empty_dict()
    exposure_biomarker_measurements: Optional[Union[dict[Union[str, ExposureBiomarkerMeasurementId], Union[dict, "ExposureBiomarkerMeasurement"]], list[Union[dict, "ExposureBiomarkerMeasurement"]]]] = empty_dict()
    protocols: Optional[Union[dict[Union[str, ProtocolId], Union[dict, "Protocol"]], list[Union[dict, "Protocol"]]]] = empty_dict()
    methods: Optional[Union[dict[Union[str, MethodId], Union[dict, "Method"]], list[Union[dict, "Method"]]]] = empty_dict()
    assays: Optional[Union[dict[Union[str, AssayId], Union[dict, "Assay"]], list[Union[dict, "Assay"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="ciliary_measurements", slot_type=CiliaryFunctionMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="asl_measurements", slot_type=ASLMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="mcc_measurements", slot_type=MCCMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="oxidative_stress_measurements", slot_type=OxidativeStressMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="cftr_measurements", slot_type=CFTRMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="egfr_measurements", slot_type=EGFRMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="goblet_cell_mucin_measurements", slot_type=GobletCellMucinMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="balf_sputum_measurements", slot_type=BALFSputumMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="lung_function_measurements", slot_type=LungFunctionMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="foxj_measurements", slot_type=FoxJMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="exposure_biomarker_measurements", slot_type=ExposureBiomarkerMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="protocols", slot_type=Protocol, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="methods", slot_type=Method, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="assays", slot_type=Assay, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Measurement(YAMLRoot):
    """
    The result of applying an assay to a specific sample at a specific time, producing a value (or values). This is
    the interface that domain-specific measurement microschemas implement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_BASE["Measurement"]
    class_class_curie: ClassVar[str] = "measurement_base:Measurement"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.Measurement

    id: Union[str, MeasurementId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    observation_type: Optional[str] = None
    quantity_measured: Optional[Union[dict, "QuantityValue"]] = None
    range_low: Optional[Union[dict, "QuantityValue"]] = None
    range_high: Optional[Union[dict, "QuantityValue"]] = None
    measured_entity: Optional[Union[dict, "NamedEntity"]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    uses: Optional[Union[dict, "Assay"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MeasurementId):
            self.id = MeasurementId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.observation_type is not None and not isinstance(self.observation_type, str):
            self.observation_type = str(self.observation_type)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedEntity):
            self.measured_entity = NamedEntity(**as_dict(self.measured_entity))

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.uses is not None and not isinstance(self.uses, Assay):
            self.uses = Assay(**as_dict(self.uses))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assay(YAMLRoot):
    """
    A test or experiment used to measure a specific biological or chemical activity; assays generate data on how a
    substance affects cells, tissues, or systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "OBI:0000070"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.Assay

    id: Union[str, AssayId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssayId):
            self.id = AssayId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Method(YAMLRoot):
    """
    A general approach or technique used to collect, measure, or analyze data (e.g., qPCR, RNA-Seq, high-speed video
    microscopy, ELISA).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_BASE["Method"]
    class_class_curie: ClassVar[str] = "measurement_base:Method"
    class_name: ClassVar[str] = "Method"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.Method

    id: Union[str, MethodId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    implements: Optional[Union[dict, Assay]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MethodId):
            self.id = MethodId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.implements is not None and not isinstance(self.implements, Assay):
            self.implements = Assay(**as_dict(self.implements))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Protocol(YAMLRoot):
    """
    A detailed set of steps for how to perform a test or collect data; protocols ensure consistency across
    laboratories or studies when generating exposure or biological data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000272"]
    class_class_curie: ClassVar[str] = "OBI:0000272"
    class_name: ClassVar[str] = "Protocol"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.Protocol

    id: Union[str, ProtocolId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    specified_by: Optional[Union[dict, Method]] = None
    follows: Optional[Union[dict, Assay]] = None
    study_context: Optional[Union[str, "StudyContextEnum"]] = None
    imaging_frame_rate: Optional[Union[dict, "QuantityValue"]] = None
    imaging_duration: Optional[Union[dict, "QuantityValue"]] = None
    spatial_resolution: Optional[Union[dict, "QuantityValue"]] = None
    temperature_control: Optional[Union[dict, "QuantityValue"]] = None
    humidity_control: Optional[Union[dict, "QuantityValue"]] = None
    evaporation_control: Optional[str] = None
    detection_method: Optional[str] = None
    staining_type: Optional[str] = None
    antibody_used: Optional[Union[str, list[str]]] = empty_list()
    probe_type: Optional[str] = None
    normalization_method: Optional[str] = None
    replicate_count: Optional[int] = None
    quality_control_criteria: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProtocolId):
            self.id = ProtocolId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.specified_by is not None and not isinstance(self.specified_by, Method):
            self.specified_by = Method(**as_dict(self.specified_by))

        if self.follows is not None and not isinstance(self.follows, Assay):
            self.follows = Assay(**as_dict(self.follows))

        if self.study_context is not None and not isinstance(self.study_context, StudyContextEnum):
            self.study_context = StudyContextEnum(self.study_context)

        if self.imaging_frame_rate is not None and not isinstance(self.imaging_frame_rate, QuantityValue):
            self.imaging_frame_rate = QuantityValue(**as_dict(self.imaging_frame_rate))

        if self.imaging_duration is not None and not isinstance(self.imaging_duration, QuantityValue):
            self.imaging_duration = QuantityValue(**as_dict(self.imaging_duration))

        if self.spatial_resolution is not None and not isinstance(self.spatial_resolution, QuantityValue):
            self.spatial_resolution = QuantityValue(**as_dict(self.spatial_resolution))

        if self.temperature_control is not None and not isinstance(self.temperature_control, QuantityValue):
            self.temperature_control = QuantityValue(**as_dict(self.temperature_control))

        if self.humidity_control is not None and not isinstance(self.humidity_control, QuantityValue):
            self.humidity_control = QuantityValue(**as_dict(self.humidity_control))

        if self.evaporation_control is not None and not isinstance(self.evaporation_control, str):
            self.evaporation_control = str(self.evaporation_control)

        if self.detection_method is not None and not isinstance(self.detection_method, str):
            self.detection_method = str(self.detection_method)

        if self.staining_type is not None and not isinstance(self.staining_type, str):
            self.staining_type = str(self.staining_type)

        if not isinstance(self.antibody_used, list):
            self.antibody_used = [self.antibody_used] if self.antibody_used is not None else []
        self.antibody_used = [v if isinstance(v, str) else str(v) for v in self.antibody_used]

        if self.probe_type is not None and not isinstance(self.probe_type, str):
            self.probe_type = str(self.probe_type)

        if self.normalization_method is not None and not isinstance(self.normalization_method, str):
            self.normalization_method = str(self.normalization_method)

        if self.replicate_count is not None and not isinstance(self.replicate_count, int):
            self.replicate_count = int(self.replicate_count)

        if self.quality_control_criteria is not None and not isinstance(self.quality_control_criteria, str):
            self.quality_control_criteria = str(self.quality_control_criteria)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InVitroContext(YAMLRoot):
    """
    Context slots for in vitro measurements using cell culture systems. Mix this into microschemas that can be
    performed on cultured cells.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_BASE["InVitroContext"]
    class_class_curie: ClassVar[str] = "measurement_base:InVitroContext"
    class_name: ClassVar[str] = "InVitroContext"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.InVitroContext

    cell_culture_system: Optional[str] = None
    days_at_differentiation: Optional[int] = None
    passage_number: Optional[int] = None
    substrate_type: Optional[str] = None
    donor_info: Optional[str] = None
    replicates_per_donor: Optional[int] = None
    culture_medium: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cell_culture_system is not None and not isinstance(self.cell_culture_system, str):
            self.cell_culture_system = str(self.cell_culture_system)

        if self.days_at_differentiation is not None and not isinstance(self.days_at_differentiation, int):
            self.days_at_differentiation = int(self.days_at_differentiation)

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.substrate_type is not None and not isinstance(self.substrate_type, str):
            self.substrate_type = str(self.substrate_type)

        if self.donor_info is not None and not isinstance(self.donor_info, str):
            self.donor_info = str(self.donor_info)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        if self.culture_medium is not None and not isinstance(self.culture_medium, str):
            self.culture_medium = str(self.culture_medium)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InVivoContext(YAMLRoot):
    """
    Context slots for in vivo measurements from human or animal subjects. Mix this into microschemas that can be
    performed on living subjects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_BASE["InVivoContext"]
    class_class_curie: ClassVar[str] = "measurement_base:InVivoContext"
    class_name: ClassVar[str] = "InVivoContext"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.InVivoContext

    participant: Optional[Union[dict, "NamedEntity"]] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    collection_site: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    subject_characteristics: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.participant is not None and not isinstance(self.participant, NamedEntity):
            self.participant = NamedEntity(**as_dict(self.participant))

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.collection_site is not None and not isinstance(self.collection_site, str):
            self.collection_site = str(self.collection_site)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.subject_characteristics is not None and not isinstance(self.subject_characteristics, str):
            self.subject_characteristics = str(self.subject_characteristics)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(YAMLRoot):
    """
    A quantity with a numeric value and unit of measurement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_BASE["QuantityValue"]
    class_class_curie: ClassVar[str] = "measurement_base:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.QuantityValue

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

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_BASE["Unit"]
    class_class_curie: ClassVar[str] = "measurement_base:Unit"
    class_name: ClassVar[str] = "Unit"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.Unit

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
    A reference to an entity with an identifier and name. Used for measured_entity, participant, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_BASE["NamedEntity"]
    class_class_curie: ClassVar[str] = "measurement_base:NamedEntity"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.NamedEntity

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
class CiliaryFunctionMeasurement(YAMLRoot):
    """
    Measurement of ciliary function including beat frequency, active area, cilia morphology, and ciliated cell
    populations. Can be performed in vitro on ALI cultures or in vivo via intranasal imaging (e.g., μOCT).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_MICROSCHEMAS["CiliaryFunctionMeasurement"]
    class_class_curie: ClassVar[str] = "measurement_microschemas:CiliaryFunctionMeasurement"
    class_name: ClassVar[str] = "CiliaryFunctionMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.CiliaryFunctionMeasurement

    id: Union[str, CiliaryFunctionMeasurementId] = None
    observation_type: Optional[Union[str, "CiliaryFunctionObservationTypeEnum"]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity_measured: Optional[Union[dict, QuantityValue]] = None
    range_low: Optional[Union[dict, QuantityValue]] = None
    range_high: Optional[Union[dict, QuantityValue]] = None
    measured_entity: Optional[Union[dict, NamedEntity]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    uses: Optional[Union[dict, Assay]] = None
    cell_culture_system: Optional[str] = None
    days_at_differentiation: Optional[int] = None
    passage_number: Optional[int] = None
    substrate_type: Optional[str] = None
    donor_info: Optional[str] = None
    replicates_per_donor: Optional[int] = None
    culture_medium: Optional[str] = None
    participant: Optional[Union[dict, NamedEntity]] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    collection_site: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    subject_characteristics: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CiliaryFunctionMeasurementId):
            self.id = CiliaryFunctionMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, CiliaryFunctionObservationTypeEnum):
            self.observation_type = CiliaryFunctionObservationTypeEnum(self.observation_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedEntity):
            self.measured_entity = NamedEntity(**as_dict(self.measured_entity))

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.uses is not None and not isinstance(self.uses, Assay):
            self.uses = Assay(**as_dict(self.uses))

        if self.cell_culture_system is not None and not isinstance(self.cell_culture_system, str):
            self.cell_culture_system = str(self.cell_culture_system)

        if self.days_at_differentiation is not None and not isinstance(self.days_at_differentiation, int):
            self.days_at_differentiation = int(self.days_at_differentiation)

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.substrate_type is not None and not isinstance(self.substrate_type, str):
            self.substrate_type = str(self.substrate_type)

        if self.donor_info is not None and not isinstance(self.donor_info, str):
            self.donor_info = str(self.donor_info)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        if self.culture_medium is not None and not isinstance(self.culture_medium, str):
            self.culture_medium = str(self.culture_medium)

        if self.participant is not None and not isinstance(self.participant, NamedEntity):
            self.participant = NamedEntity(**as_dict(self.participant))

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.collection_site is not None and not isinstance(self.collection_site, str):
            self.collection_site = str(self.collection_site)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.subject_characteristics is not None and not isinstance(self.subject_characteristics, str):
            self.subject_characteristics = str(self.subject_characteristics)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ASLMeasurement(YAMLRoot):
    """
    Measurement of airway surface liquid properties including ASL height, periciliary layer depth, and ion
    composition. Critical for assessing airway hydration status in CF and other mucociliary disorders.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_MICROSCHEMAS["ASLMeasurement"]
    class_class_curie: ClassVar[str] = "measurement_microschemas:ASLMeasurement"
    class_name: ClassVar[str] = "ASLMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.ASLMeasurement

    id: Union[str, ASLMeasurementId] = None
    observation_type: Optional[Union[str, "ASLObservationTypeEnum"]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity_measured: Optional[Union[dict, QuantityValue]] = None
    range_low: Optional[Union[dict, QuantityValue]] = None
    range_high: Optional[Union[dict, QuantityValue]] = None
    measured_entity: Optional[Union[dict, NamedEntity]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    uses: Optional[Union[dict, Assay]] = None
    cell_culture_system: Optional[str] = None
    days_at_differentiation: Optional[int] = None
    passage_number: Optional[int] = None
    substrate_type: Optional[str] = None
    donor_info: Optional[str] = None
    replicates_per_donor: Optional[int] = None
    culture_medium: Optional[str] = None
    participant: Optional[Union[dict, NamedEntity]] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    collection_site: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    subject_characteristics: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ASLMeasurementId):
            self.id = ASLMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, ASLObservationTypeEnum):
            self.observation_type = ASLObservationTypeEnum(self.observation_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedEntity):
            self.measured_entity = NamedEntity(**as_dict(self.measured_entity))

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.uses is not None and not isinstance(self.uses, Assay):
            self.uses = Assay(**as_dict(self.uses))

        if self.cell_culture_system is not None and not isinstance(self.cell_culture_system, str):
            self.cell_culture_system = str(self.cell_culture_system)

        if self.days_at_differentiation is not None and not isinstance(self.days_at_differentiation, int):
            self.days_at_differentiation = int(self.days_at_differentiation)

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.substrate_type is not None and not isinstance(self.substrate_type, str):
            self.substrate_type = str(self.substrate_type)

        if self.donor_info is not None and not isinstance(self.donor_info, str):
            self.donor_info = str(self.donor_info)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        if self.culture_medium is not None and not isinstance(self.culture_medium, str):
            self.culture_medium = str(self.culture_medium)

        if self.participant is not None and not isinstance(self.participant, NamedEntity):
            self.participant = NamedEntity(**as_dict(self.participant))

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.collection_site is not None and not isinstance(self.collection_site, str):
            self.collection_site = str(self.collection_site)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.subject_characteristics is not None and not isinstance(self.subject_characteristics, str):
            self.subject_characteristics = str(self.subject_characteristics)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MCCMeasurement(YAMLRoot):
    """
    Measurement of mucociliary clearance and transport including mucus transport rate, directionality, and clearance
    efficiency. Assesses the coordinated function of cilia and mucus for pathogen clearance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_MICROSCHEMAS["MCCMeasurement"]
    class_class_curie: ClassVar[str] = "measurement_microschemas:MCCMeasurement"
    class_name: ClassVar[str] = "MCCMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.MCCMeasurement

    id: Union[str, MCCMeasurementId] = None
    observation_type: Optional[Union[str, "MCCObservationTypeEnum"]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity_measured: Optional[Union[dict, QuantityValue]] = None
    range_low: Optional[Union[dict, QuantityValue]] = None
    range_high: Optional[Union[dict, QuantityValue]] = None
    measured_entity: Optional[Union[dict, NamedEntity]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    uses: Optional[Union[dict, Assay]] = None
    cell_culture_system: Optional[str] = None
    days_at_differentiation: Optional[int] = None
    passage_number: Optional[int] = None
    substrate_type: Optional[str] = None
    donor_info: Optional[str] = None
    replicates_per_donor: Optional[int] = None
    culture_medium: Optional[str] = None
    participant: Optional[Union[dict, NamedEntity]] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    collection_site: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    subject_characteristics: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MCCMeasurementId):
            self.id = MCCMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, MCCObservationTypeEnum):
            self.observation_type = MCCObservationTypeEnum(self.observation_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedEntity):
            self.measured_entity = NamedEntity(**as_dict(self.measured_entity))

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.uses is not None and not isinstance(self.uses, Assay):
            self.uses = Assay(**as_dict(self.uses))

        if self.cell_culture_system is not None and not isinstance(self.cell_culture_system, str):
            self.cell_culture_system = str(self.cell_culture_system)

        if self.days_at_differentiation is not None and not isinstance(self.days_at_differentiation, int):
            self.days_at_differentiation = int(self.days_at_differentiation)

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.substrate_type is not None and not isinstance(self.substrate_type, str):
            self.substrate_type = str(self.substrate_type)

        if self.donor_info is not None and not isinstance(self.donor_info, str):
            self.donor_info = str(self.donor_info)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        if self.culture_medium is not None and not isinstance(self.culture_medium, str):
            self.culture_medium = str(self.culture_medium)

        if self.participant is not None and not isinstance(self.participant, NamedEntity):
            self.participant = NamedEntity(**as_dict(self.participant))

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.collection_site is not None and not isinstance(self.collection_site, str):
            self.collection_site = str(self.collection_site)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.subject_characteristics is not None and not isinstance(self.subject_characteristics, str):
            self.subject_characteristics = str(self.subject_characteristics)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OxidativeStressMeasurement(YAMLRoot):
    """
    Measurement of oxidative stress markers including reactive oxygen species, lipid peroxidation products, protein
    oxidation, DNA damage, and antioxidant capacity. Key molecular initiating event in respiratory toxicology AOPs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_MICROSCHEMAS["OxidativeStressMeasurement"]
    class_class_curie: ClassVar[str] = "measurement_microschemas:OxidativeStressMeasurement"
    class_name: ClassVar[str] = "OxidativeStressMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.OxidativeStressMeasurement

    id: Union[str, OxidativeStressMeasurementId] = None
    observation_type: Optional[Union[str, "OxidativeStressObservationTypeEnum"]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity_measured: Optional[Union[dict, QuantityValue]] = None
    range_low: Optional[Union[dict, QuantityValue]] = None
    range_high: Optional[Union[dict, QuantityValue]] = None
    measured_entity: Optional[Union[dict, NamedEntity]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    uses: Optional[Union[dict, Assay]] = None
    cell_culture_system: Optional[str] = None
    days_at_differentiation: Optional[int] = None
    passage_number: Optional[int] = None
    substrate_type: Optional[str] = None
    donor_info: Optional[str] = None
    replicates_per_donor: Optional[int] = None
    culture_medium: Optional[str] = None
    participant: Optional[Union[dict, NamedEntity]] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    collection_site: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    subject_characteristics: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OxidativeStressMeasurementId):
            self.id = OxidativeStressMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, OxidativeStressObservationTypeEnum):
            self.observation_type = OxidativeStressObservationTypeEnum(self.observation_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedEntity):
            self.measured_entity = NamedEntity(**as_dict(self.measured_entity))

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.uses is not None and not isinstance(self.uses, Assay):
            self.uses = Assay(**as_dict(self.uses))

        if self.cell_culture_system is not None and not isinstance(self.cell_culture_system, str):
            self.cell_culture_system = str(self.cell_culture_system)

        if self.days_at_differentiation is not None and not isinstance(self.days_at_differentiation, int):
            self.days_at_differentiation = int(self.days_at_differentiation)

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.substrate_type is not None and not isinstance(self.substrate_type, str):
            self.substrate_type = str(self.substrate_type)

        if self.donor_info is not None and not isinstance(self.donor_info, str):
            self.donor_info = str(self.donor_info)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        if self.culture_medium is not None and not isinstance(self.culture_medium, str):
            self.culture_medium = str(self.culture_medium)

        if self.participant is not None and not isinstance(self.participant, NamedEntity):
            self.participant = NamedEntity(**as_dict(self.participant))

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.collection_site is not None and not isinstance(self.collection_site, str):
            self.collection_site = str(self.collection_site)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.subject_characteristics is not None and not isinstance(self.subject_characteristics, str):
            self.subject_characteristics = str(self.subject_characteristics)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CFTRMeasurement(YAMLRoot):
    """
    Measurement of CFTR (cystic fibrosis transmembrane conductance regulator) function including chloride secretion,
    CFTR-mediated current, and clinical indicators like sweat chloride concentration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_MICROSCHEMAS["CFTRMeasurement"]
    class_class_curie: ClassVar[str] = "measurement_microschemas:CFTRMeasurement"
    class_name: ClassVar[str] = "CFTRMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.CFTRMeasurement

    id: Union[str, CFTRMeasurementId] = None
    observation_type: Optional[Union[str, "CFTRObservationTypeEnum"]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity_measured: Optional[Union[dict, QuantityValue]] = None
    range_low: Optional[Union[dict, QuantityValue]] = None
    range_high: Optional[Union[dict, QuantityValue]] = None
    measured_entity: Optional[Union[dict, NamedEntity]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    uses: Optional[Union[dict, Assay]] = None
    cell_culture_system: Optional[str] = None
    days_at_differentiation: Optional[int] = None
    passage_number: Optional[int] = None
    substrate_type: Optional[str] = None
    donor_info: Optional[str] = None
    replicates_per_donor: Optional[int] = None
    culture_medium: Optional[str] = None
    participant: Optional[Union[dict, NamedEntity]] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    collection_site: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    subject_characteristics: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CFTRMeasurementId):
            self.id = CFTRMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, CFTRObservationTypeEnum):
            self.observation_type = CFTRObservationTypeEnum(self.observation_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedEntity):
            self.measured_entity = NamedEntity(**as_dict(self.measured_entity))

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.uses is not None and not isinstance(self.uses, Assay):
            self.uses = Assay(**as_dict(self.uses))

        if self.cell_culture_system is not None and not isinstance(self.cell_culture_system, str):
            self.cell_culture_system = str(self.cell_culture_system)

        if self.days_at_differentiation is not None and not isinstance(self.days_at_differentiation, int):
            self.days_at_differentiation = int(self.days_at_differentiation)

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.substrate_type is not None and not isinstance(self.substrate_type, str):
            self.substrate_type = str(self.substrate_type)

        if self.donor_info is not None and not isinstance(self.donor_info, str):
            self.donor_info = str(self.donor_info)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        if self.culture_medium is not None and not isinstance(self.culture_medium, str):
            self.culture_medium = str(self.culture_medium)

        if self.participant is not None and not isinstance(self.participant, NamedEntity):
            self.participant = NamedEntity(**as_dict(self.participant))

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.collection_site is not None and not isinstance(self.collection_site, str):
            self.collection_site = str(self.collection_site)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.subject_characteristics is not None and not isinstance(self.subject_characteristics, str):
            self.subject_characteristics = str(self.subject_characteristics)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EGFRMeasurement(YAMLRoot):
    """
    Measurement of EGFR (epidermal growth factor receptor) pathway activation including receptor phosphorylation,
    downstream kinase activation, and ligand expression. Key signaling pathway in airway inflammation and mucin
    regulation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_MICROSCHEMAS["EGFRMeasurement"]
    class_class_curie: ClassVar[str] = "measurement_microschemas:EGFRMeasurement"
    class_name: ClassVar[str] = "EGFRMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.EGFRMeasurement

    id: Union[str, EGFRMeasurementId] = None
    observation_type: Optional[Union[str, "EGFRObservationTypeEnum"]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity_measured: Optional[Union[dict, QuantityValue]] = None
    range_low: Optional[Union[dict, QuantityValue]] = None
    range_high: Optional[Union[dict, QuantityValue]] = None
    measured_entity: Optional[Union[dict, NamedEntity]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    uses: Optional[Union[dict, Assay]] = None
    cell_culture_system: Optional[str] = None
    days_at_differentiation: Optional[int] = None
    passage_number: Optional[int] = None
    substrate_type: Optional[str] = None
    donor_info: Optional[str] = None
    replicates_per_donor: Optional[int] = None
    culture_medium: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EGFRMeasurementId):
            self.id = EGFRMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, EGFRObservationTypeEnum):
            self.observation_type = EGFRObservationTypeEnum(self.observation_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedEntity):
            self.measured_entity = NamedEntity(**as_dict(self.measured_entity))

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.uses is not None and not isinstance(self.uses, Assay):
            self.uses = Assay(**as_dict(self.uses))

        if self.cell_culture_system is not None and not isinstance(self.cell_culture_system, str):
            self.cell_culture_system = str(self.cell_culture_system)

        if self.days_at_differentiation is not None and not isinstance(self.days_at_differentiation, int):
            self.days_at_differentiation = int(self.days_at_differentiation)

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.substrate_type is not None and not isinstance(self.substrate_type, str):
            self.substrate_type = str(self.substrate_type)

        if self.donor_info is not None and not isinstance(self.donor_info, str):
            self.donor_info = str(self.donor_info)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        if self.culture_medium is not None and not isinstance(self.culture_medium, str):
            self.culture_medium = str(self.culture_medium)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GobletCellMucinMeasurement(YAMLRoot):
    """
    Measurement of goblet cell populations and mucin production including goblet cell counts, mucin gene/protein
    expression, and mucus properties. Assesses goblet cell hyperplasia and mucus hypersecretion phenotypes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_MICROSCHEMAS["GobletCellMucinMeasurement"]
    class_class_curie: ClassVar[str] = "measurement_microschemas:GobletCellMucinMeasurement"
    class_name: ClassVar[str] = "GobletCellMucinMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.GobletCellMucinMeasurement

    id: Union[str, GobletCellMucinMeasurementId] = None
    observation_type: Optional[Union[str, "GobletCellMucinObservationTypeEnum"]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity_measured: Optional[Union[dict, QuantityValue]] = None
    range_low: Optional[Union[dict, QuantityValue]] = None
    range_high: Optional[Union[dict, QuantityValue]] = None
    measured_entity: Optional[Union[dict, NamedEntity]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    uses: Optional[Union[dict, Assay]] = None
    cell_culture_system: Optional[str] = None
    days_at_differentiation: Optional[int] = None
    passage_number: Optional[int] = None
    substrate_type: Optional[str] = None
    donor_info: Optional[str] = None
    replicates_per_donor: Optional[int] = None
    culture_medium: Optional[str] = None
    participant: Optional[Union[dict, NamedEntity]] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    collection_site: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    subject_characteristics: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GobletCellMucinMeasurementId):
            self.id = GobletCellMucinMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, GobletCellMucinObservationTypeEnum):
            self.observation_type = GobletCellMucinObservationTypeEnum(self.observation_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedEntity):
            self.measured_entity = NamedEntity(**as_dict(self.measured_entity))

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.uses is not None and not isinstance(self.uses, Assay):
            self.uses = Assay(**as_dict(self.uses))

        if self.cell_culture_system is not None and not isinstance(self.cell_culture_system, str):
            self.cell_culture_system = str(self.cell_culture_system)

        if self.days_at_differentiation is not None and not isinstance(self.days_at_differentiation, int):
            self.days_at_differentiation = int(self.days_at_differentiation)

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.substrate_type is not None and not isinstance(self.substrate_type, str):
            self.substrate_type = str(self.substrate_type)

        if self.donor_info is not None and not isinstance(self.donor_info, str):
            self.donor_info = str(self.donor_info)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        if self.culture_medium is not None and not isinstance(self.culture_medium, str):
            self.culture_medium = str(self.culture_medium)

        if self.participant is not None and not isinstance(self.participant, NamedEntity):
            self.participant = NamedEntity(**as_dict(self.participant))

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.collection_site is not None and not isinstance(self.collection_site, str):
            self.collection_site = str(self.collection_site)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.subject_characteristics is not None and not isinstance(self.subject_characteristics, str):
            self.subject_characteristics = str(self.subject_characteristics)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BALFSputumMeasurement(YAMLRoot):
    """
    Measurement of bronchoalveolar lavage fluid (BALF) or sputum components including inflammatory cell profiles,
    cytokine levels, microbiome composition, and protein concentrations. Clinical assessment of airway inflammation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_MICROSCHEMAS["BALFSputumMeasurement"]
    class_class_curie: ClassVar[str] = "measurement_microschemas:BALFSputumMeasurement"
    class_name: ClassVar[str] = "BALFSputumMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.BALFSputumMeasurement

    id: Union[str, BALFSputumMeasurementId] = None
    observation_type: Optional[Union[str, "BALFSputumObservationTypeEnum"]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity_measured: Optional[Union[dict, QuantityValue]] = None
    range_low: Optional[Union[dict, QuantityValue]] = None
    range_high: Optional[Union[dict, QuantityValue]] = None
    measured_entity: Optional[Union[dict, NamedEntity]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    uses: Optional[Union[dict, Assay]] = None
    participant: Optional[Union[dict, NamedEntity]] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    collection_site: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    subject_characteristics: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BALFSputumMeasurementId):
            self.id = BALFSputumMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, BALFSputumObservationTypeEnum):
            self.observation_type = BALFSputumObservationTypeEnum(self.observation_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedEntity):
            self.measured_entity = NamedEntity(**as_dict(self.measured_entity))

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.uses is not None and not isinstance(self.uses, Assay):
            self.uses = Assay(**as_dict(self.uses))

        if self.participant is not None and not isinstance(self.participant, NamedEntity):
            self.participant = NamedEntity(**as_dict(self.participant))

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.collection_site is not None and not isinstance(self.collection_site, str):
            self.collection_site = str(self.collection_site)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.subject_characteristics is not None and not isinstance(self.subject_characteristics, str):
            self.subject_characteristics = str(self.subject_characteristics)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LungFunctionMeasurement(YAMLRoot):
    """
    Measurement of lung function parameters via spirometry and other pulmonary function tests including FEV1, FVC,
    FEV1/FVC ratio, and diffusing capacity. Clinical outcomes for respiratory health assessment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_MICROSCHEMAS["LungFunctionMeasurement"]
    class_class_curie: ClassVar[str] = "measurement_microschemas:LungFunctionMeasurement"
    class_name: ClassVar[str] = "LungFunctionMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.LungFunctionMeasurement

    id: Union[str, LungFunctionMeasurementId] = None
    observation_type: Optional[Union[str, "LungFunctionObservationTypeEnum"]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity_measured: Optional[Union[dict, QuantityValue]] = None
    range_low: Optional[Union[dict, QuantityValue]] = None
    range_high: Optional[Union[dict, QuantityValue]] = None
    measured_entity: Optional[Union[dict, NamedEntity]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    uses: Optional[Union[dict, Assay]] = None
    participant: Optional[Union[dict, NamedEntity]] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    collection_site: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    subject_characteristics: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LungFunctionMeasurementId):
            self.id = LungFunctionMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, LungFunctionObservationTypeEnum):
            self.observation_type = LungFunctionObservationTypeEnum(self.observation_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedEntity):
            self.measured_entity = NamedEntity(**as_dict(self.measured_entity))

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.uses is not None and not isinstance(self.uses, Assay):
            self.uses = Assay(**as_dict(self.uses))

        if self.participant is not None and not isinstance(self.participant, NamedEntity):
            self.participant = NamedEntity(**as_dict(self.participant))

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.collection_site is not None and not isinstance(self.collection_site, str):
            self.collection_site = str(self.collection_site)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.subject_characteristics is not None and not isinstance(self.subject_characteristics, str):
            self.subject_characteristics = str(self.subject_characteristics)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FoxJMeasurement(YAMLRoot):
    """
    Measurement of FoxJ1 expression and related ciliogenesis markers. FoxJ1 is a master regulator of
    multiciliogenesis, and its expression indicates ciliated cell differentiation status.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_MICROSCHEMAS["FoxJMeasurement"]
    class_class_curie: ClassVar[str] = "measurement_microschemas:FoxJMeasurement"
    class_name: ClassVar[str] = "FoxJMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.FoxJMeasurement

    id: Union[str, FoxJMeasurementId] = None
    observation_type: Optional[Union[str, "FoxJObservationTypeEnum"]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity_measured: Optional[Union[dict, QuantityValue]] = None
    range_low: Optional[Union[dict, QuantityValue]] = None
    range_high: Optional[Union[dict, QuantityValue]] = None
    measured_entity: Optional[Union[dict, NamedEntity]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    uses: Optional[Union[dict, Assay]] = None
    cell_culture_system: Optional[str] = None
    days_at_differentiation: Optional[int] = None
    passage_number: Optional[int] = None
    substrate_type: Optional[str] = None
    donor_info: Optional[str] = None
    replicates_per_donor: Optional[int] = None
    culture_medium: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoxJMeasurementId):
            self.id = FoxJMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, FoxJObservationTypeEnum):
            self.observation_type = FoxJObservationTypeEnum(self.observation_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedEntity):
            self.measured_entity = NamedEntity(**as_dict(self.measured_entity))

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.uses is not None and not isinstance(self.uses, Assay):
            self.uses = Assay(**as_dict(self.uses))

        if self.cell_culture_system is not None and not isinstance(self.cell_culture_system, str):
            self.cell_culture_system = str(self.cell_culture_system)

        if self.days_at_differentiation is not None and not isinstance(self.days_at_differentiation, int):
            self.days_at_differentiation = int(self.days_at_differentiation)

        if self.passage_number is not None and not isinstance(self.passage_number, int):
            self.passage_number = int(self.passage_number)

        if self.substrate_type is not None and not isinstance(self.substrate_type, str):
            self.substrate_type = str(self.substrate_type)

        if self.donor_info is not None and not isinstance(self.donor_info, str):
            self.donor_info = str(self.donor_info)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        if self.culture_medium is not None and not isinstance(self.culture_medium, str):
            self.culture_medium = str(self.culture_medium)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureBiomarkerMeasurement(YAMLRoot):
    """
    Measurement of biomarkers indicating exposure to environmental agents including urinary metabolites (e.g.,
    cotinine for tobacco smoke), blood levels, and other exposure indicators.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MEASUREMENT_MICROSCHEMAS["ExposureBiomarkerMeasurement"]
    class_class_curie: ClassVar[str] = "measurement_microschemas:ExposureBiomarkerMeasurement"
    class_name: ClassVar[str] = "ExposureBiomarkerMeasurement"
    class_model_uri: ClassVar[URIRef] = OUTCOMES_WORKING_GROUP.ExposureBiomarkerMeasurement

    id: Union[str, ExposureBiomarkerMeasurementId] = None
    observation_type: Optional[Union[str, "ExposureBiomarkerObservationTypeEnum"]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity_measured: Optional[Union[dict, QuantityValue]] = None
    range_low: Optional[Union[dict, QuantityValue]] = None
    range_high: Optional[Union[dict, QuantityValue]] = None
    measured_entity: Optional[Union[dict, NamedEntity]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    uses: Optional[Union[dict, Assay]] = None
    participant: Optional[Union[dict, NamedEntity]] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    collection_site: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    subject_characteristics: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureBiomarkerMeasurementId):
            self.id = ExposureBiomarkerMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, ExposureBiomarkerObservationTypeEnum):
            self.observation_type = ExposureBiomarkerObservationTypeEnum(self.observation_type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedEntity):
            self.measured_entity = NamedEntity(**as_dict(self.measured_entity))

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.uses is not None and not isinstance(self.uses, Assay):
            self.uses = Assay(**as_dict(self.uses))

        if self.participant is not None and not isinstance(self.participant, NamedEntity):
            self.participant = NamedEntity(**as_dict(self.participant))

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.collection_site is not None and not isinstance(self.collection_site, str):
            self.collection_site = str(self.collection_site)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.subject_characteristics is not None and not isinstance(self.subject_characteristics, str):
            self.subject_characteristics = str(self.subject_characteristics)

        super().__post_init__(**kwargs)


# Enumerations
class StudyContextEnum(EnumDefinitionImpl):
    """
    The experimental context for a protocol or measurement.
    """
    in_vitro = PermissibleValue(
        text="in_vitro",
        description="Performed on cultured cells or tissues")
    in_vivo = PermissibleValue(
        text="in_vivo",
        description="Performed on living human or animal subjects")
    ex_vivo = PermissibleValue(
        text="ex_vivo",
        description="Performed on tissue removed from an organism")

    _defn = EnumDefinition(
        name="StudyContextEnum",
        description="The experimental context for a protocol or measurement.",
    )

class SampleTypeEnum(EnumDefinitionImpl):
    """
    Types of biological samples for in vivo measurements.
    """
    urine = PermissibleValue(
        text="urine",
        description="Urine sample")
    blood = PermissibleValue(
        text="blood",
        description="Blood sample (whole blood, serum, or plasma)")
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
        description="Exhaled breath condensate (EBC)")
    biopsy = PermissibleValue(
        text="biopsy",
        description="Tissue biopsy")
    sweat = PermissibleValue(
        text="sweat",
        description="Sweat sample (e.g., for sweat chloride test)")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
        description="Types of biological samples for in vivo measurements.",
    )

class CiliaryFunctionObservationTypeEnum(EnumDefinitionImpl):
    """
    Observation types for ciliary function measurements.
    """
    ciliary_beat_frequency = PermissibleValue(
        text="ciliary_beat_frequency",
        description="Ciliary beat frequency (Hz)",
        meaning=GO["0003341"])
    ciliary_active_area_percentage = PermissibleValue(
        text="ciliary_active_area_percentage",
        description="Percentage of epithelial surface with actively beating cilia")
    cilia_length = PermissibleValue(
        text="cilia_length",
        description="Length of cilia (μm)")
    cilia_per_cell = PermissibleValue(
        text="cilia_per_cell",
        description="Number of cilia per cell")
    percentage_ciliated_cells = PermissibleValue(
        text="percentage_ciliated_cells",
        description="Percentage of cells that are ciliated")
    ciliary_motion_pattern = PermissibleValue(
        text="ciliary_motion_pattern",
        description="Pattern of ciliary motion (coordinated, dyskinetic, immotile)")
    ciliary_beat_amplitude = PermissibleValue(
        text="ciliary_beat_amplitude",
        description="Amplitude of ciliary beat stroke")

    _defn = EnumDefinition(
        name="CiliaryFunctionObservationTypeEnum",
        description="Observation types for ciliary function measurements.",
    )

class ASLObservationTypeEnum(EnumDefinitionImpl):
    """
    Observation types for airway surface liquid measurements.
    """
    asl_height = PermissibleValue(
        text="asl_height",
        description="Airway surface liquid height/depth (μm)")
    periciliary_layer_depth = PermissibleValue(
        text="periciliary_layer_depth",
        description="Periciliary layer (PCL) depth (μm)")
    mucus_layer_thickness = PermissibleValue(
        text="mucus_layer_thickness",
        description="Thickness of the mucus gel layer (μm)")
    asl_chloride_concentration = PermissibleValue(
        text="asl_chloride_concentration",
        description="Chloride ion concentration in ASL")
    asl_sodium_concentration = PermissibleValue(
        text="asl_sodium_concentration",
        description="Sodium ion concentration in ASL")
    asl_potassium_concentration = PermissibleValue(
        text="asl_potassium_concentration",
        description="Potassium ion concentration in ASL")
    asl_ph = PermissibleValue(
        text="asl_ph",
        description="pH of airway surface liquid")

    _defn = EnumDefinition(
        name="ASLObservationTypeEnum",
        description="Observation types for airway surface liquid measurements.",
    )

class MCCObservationTypeEnum(EnumDefinitionImpl):
    """
    Observation types for mucociliary clearance measurements.
    """
    mucociliary_transport_rate = PermissibleValue(
        text="mucociliary_transport_rate",
        description="Rate of mucus/particle transport (mm/min or μm/s)",
        meaning=GO["0120197"])
    transport_directionality = PermissibleValue(
        text="transport_directionality",
        description="Directionality of mucociliary transport")
    percentage_active_transport = PermissibleValue(
        text="percentage_active_transport",
        description="Percentage of surface with active mucociliary transport")
    particle_clearance_time = PermissibleValue(
        text="particle_clearance_time",
        description="Time to clear particles from a defined region")
    biofilm_clearance_rate = PermissibleValue(
        text="biofilm_clearance_rate",
        description="Rate of bacterial biofilm clearance")
    bacterial_load = PermissibleValue(
        text="bacterial_load",
        description="Bacterial load remaining after clearance (CFU)")

    _defn = EnumDefinition(
        name="MCCObservationTypeEnum",
        description="Observation types for mucociliary clearance measurements.",
    )

class OxidativeStressObservationTypeEnum(EnumDefinitionImpl):
    """
    Observation types for oxidative stress measurements.
    """
    reactive_oxygen_species = PermissibleValue(
        text="reactive_oxygen_species",
        description="Reactive oxygen species level (fluorescence intensity or fold change)",
        meaning=CHEBI["26523"])
    malondialdehyde = PermissibleValue(
        text="malondialdehyde",
        description="Malondialdehyde (MDA) level - lipid peroxidation marker",
        meaning=CHEBI["16213"])
    four_hydroxynonenal = PermissibleValue(
        text="four_hydroxynonenal",
        description="4-Hydroxynonenal (4-HNE) level - lipid peroxidation marker",
        meaning=CHEBI["58968"])
    eight_isoprostane = PermissibleValue(
        text="eight_isoprostane",
        description="8-Isoprostane level - lipid peroxidation marker")
    protein_carbonyl = PermissibleValue(
        text="protein_carbonyl",
        description="Protein carbonyl content - protein oxidation marker")
    nitrotyrosine = PermissibleValue(
        text="nitrotyrosine",
        description="Nitrotyrosine level - protein nitration marker")
    eight_ohdg = PermissibleValue(
        text="eight_ohdg",
        description="8-OHdG level - DNA oxidation marker")
    glutathione_ratio = PermissibleValue(
        text="glutathione_ratio",
        description="GSH/GSSG ratio - antioxidant capacity")
    superoxide_dismutase_activity = PermissibleValue(
        text="superoxide_dismutase_activity",
        description="Superoxide dismutase (SOD) enzyme activity")
    catalase_activity = PermissibleValue(
        text="catalase_activity",
        description="Catalase enzyme activity")
    glutathione_peroxidase_activity = PermissibleValue(
        text="glutathione_peroxidase_activity",
        description="Glutathione peroxidase (GPx) enzyme activity")
    total_antioxidant_capacity = PermissibleValue(
        text="total_antioxidant_capacity",
        description="Total antioxidant capacity of sample")
    nrf2_activation = PermissibleValue(
        text="nrf2_activation",
        description="NRF2 pathway activation level")

    _defn = EnumDefinition(
        name="OxidativeStressObservationTypeEnum",
        description="Observation types for oxidative stress measurements.",
    )

class CFTRObservationTypeEnum(EnumDefinitionImpl):
    """
    Observation types for CFTR function measurements.
    """
    cftr_chloride_secretion = PermissibleValue(
        text="cftr_chloride_secretion",
        description="CFTR-mediated chloride secretory current (μA/cm²)")
    cftr_forskolin_response = PermissibleValue(
        text="cftr_forskolin_response",
        description="CFTR response to forskolin stimulation")
    cftr_inhibitor_sensitive_current = PermissibleValue(
        text="cftr_inhibitor_sensitive_current",
        description="CFTRinh-172 sensitive current")
    sweat_chloride_concentration = PermissibleValue(
        text="sweat_chloride_concentration",
        description="Sweat chloride concentration (mEq/L) - CF diagnostic")
    nasal_potential_difference = PermissibleValue(
        text="nasal_potential_difference",
        description="Nasal potential difference measurement")

    _defn = EnumDefinition(
        name="CFTRObservationTypeEnum",
        description="Observation types for CFTR function measurements.",
    )

class EGFRObservationTypeEnum(EnumDefinitionImpl):
    """
    Observation types for EGFR signaling measurements.
    """
    egfr_phosphorylation = PermissibleValue(
        text="egfr_phosphorylation",
        description="EGFR phosphorylation level (specify site, e.g., Y1068, Y1173)")
    egfr_total_protein = PermissibleValue(
        text="egfr_total_protein",
        description="Total EGFR protein expression")
    erk_phosphorylation = PermissibleValue(
        text="erk_phosphorylation",
        description="ERK1/2 phosphorylation (downstream kinase)")
    akt_phosphorylation = PermissibleValue(
        text="akt_phosphorylation",
        description="AKT phosphorylation (downstream kinase)")
    egfr_ligand_expression = PermissibleValue(
        text="egfr_ligand_expression",
        description="EGFR ligand expression (EGF, TGF-α, amphiregulin)")
    egfr_membrane_localization = PermissibleValue(
        text="egfr_membrane_localization",
        description="EGFR membrane localization")

    _defn = EnumDefinition(
        name="EGFRObservationTypeEnum",
        description="Observation types for EGFR signaling measurements.",
    )

class GobletCellMucinObservationTypeEnum(EnumDefinitionImpl):
    """
    Observation types for goblet cell and mucin measurements.
    """
    goblet_cell_count = PermissibleValue(
        text="goblet_cell_count",
        description="Number or percentage of goblet cells",
        meaning=CL["0000160"])
    goblet_to_ciliated_ratio = PermissibleValue(
        text="goblet_to_ciliated_ratio",
        description="Ratio of goblet cells to ciliated cells")
    muc5ac_expression = PermissibleValue(
        text="muc5ac_expression",
        description="MUC5AC gene or protein expression")
    muc5b_expression = PermissibleValue(
        text="muc5b_expression",
        description="MUC5B gene or protein expression")
    muc5ac_muc5b_ratio = PermissibleValue(
        text="muc5ac_muc5b_ratio",
        description="Ratio of MUC5AC to MUC5B expression")
    mucin_protein_concentration = PermissibleValue(
        text="mucin_protein_concentration",
        description="Total mucin protein concentration")
    mucin_secretion_rate = PermissibleValue(
        text="mucin_secretion_rate",
        description="Rate of mucin secretion")
    mucus_viscosity = PermissibleValue(
        text="mucus_viscosity",
        description="Viscosity of airway mucus")
    percent_solids = PermissibleValue(
        text="percent_solids",
        description="Percent solids in mucus/secretions")

    _defn = EnumDefinition(
        name="GobletCellMucinObservationTypeEnum",
        description="Observation types for goblet cell and mucin measurements.",
    )

class BALFSputumObservationTypeEnum(EnumDefinitionImpl):
    """
    Observation types for BALF and sputum measurements.
    """
    neutrophil_percentage = PermissibleValue(
        text="neutrophil_percentage",
        description="Percentage of neutrophils in differential cell count")
    eosinophil_percentage = PermissibleValue(
        text="eosinophil_percentage",
        description="Percentage of eosinophils in differential cell count")
    macrophage_percentage = PermissibleValue(
        text="macrophage_percentage",
        description="Percentage of macrophages in differential cell count")
    lymphocyte_percentage = PermissibleValue(
        text="lymphocyte_percentage",
        description="Percentage of lymphocytes in differential cell count")
    total_cell_count = PermissibleValue(
        text="total_cell_count",
        description="Total cell count in sample")
    il6_concentration = PermissibleValue(
        text="il6_concentration",
        description="IL-6 cytokine concentration")
    il8_concentration = PermissibleValue(
        text="il8_concentration",
        description="IL-8 (CXCL8) cytokine concentration")
    tnf_alpha_concentration = PermissibleValue(
        text="tnf_alpha_concentration",
        description="TNF-α cytokine concentration")
    il1_beta_concentration = PermissibleValue(
        text="il1_beta_concentration",
        description="IL-1β cytokine concentration")
    total_protein_concentration = PermissibleValue(
        text="total_protein_concentration",
        description="Total protein concentration")
    alpha_diversity = PermissibleValue(
        text="alpha_diversity",
        description="Microbiome alpha diversity metric")
    beta_diversity = PermissibleValue(
        text="beta_diversity",
        description="Microbiome beta diversity metric")
    bacterial_load = PermissibleValue(
        text="bacterial_load",
        description="Total bacterial load (16S copies or CFU)")

    _defn = EnumDefinition(
        name="BALFSputumObservationTypeEnum",
        description="Observation types for BALF and sputum measurements.",
    )

class LungFunctionObservationTypeEnum(EnumDefinitionImpl):
    """
    Observation types for lung function measurements.
    """
    fev1 = PermissibleValue(
        text="fev1",
        description="Forced expiratory volume in 1 second (L or % predicted)",
        meaning=HP["0002088"])
    fvc = PermissibleValue(
        text="fvc",
        description="Forced vital capacity (L or % predicted)")
    fev1_fvc_ratio = PermissibleValue(
        text="fev1_fvc_ratio",
        description="Ratio of FEV1 to FVC")
    fef25_75 = PermissibleValue(
        text="fef25_75",
        description="Forced expiratory flow at 25-75% of FVC")
    pef = PermissibleValue(
        text="pef",
        description="Peak expiratory flow")
    dlco = PermissibleValue(
        text="dlco",
        description="Diffusing capacity for carbon monoxide")
    feno = PermissibleValue(
        text="feno",
        description="Fractional exhaled nitric oxide (ppb)")
    bronchodilator_response = PermissibleValue(
        text="bronchodilator_response",
        description="Change in FEV1 after bronchodilator administration")
    lung_function_decline_rate = PermissibleValue(
        text="lung_function_decline_rate",
        description="Rate of FEV1 decline over time (mL/year)")

    _defn = EnumDefinition(
        name="LungFunctionObservationTypeEnum",
        description="Observation types for lung function measurements.",
    )

class FoxJObservationTypeEnum(EnumDefinitionImpl):
    """
    Observation types for FoxJ1 and ciliogenesis measurements.
    """
    foxj1_mrna_expression = PermissibleValue(
        text="foxj1_mrna_expression",
        description="FoxJ1 mRNA expression level")
    foxj1_protein_expression = PermissibleValue(
        text="foxj1_protein_expression",
        description="FoxJ1 protein expression level")
    foxj1_positive_cell_percentage = PermissibleValue(
        text="foxj1_positive_cell_percentage",
        description="Percentage of FoxJ1-positive cells")
    foxj1_nuclear_localization = PermissibleValue(
        text="foxj1_nuclear_localization",
        description="FoxJ1 nuclear localization")

    _defn = EnumDefinition(
        name="FoxJObservationTypeEnum",
        description="Observation types for FoxJ1 and ciliogenesis measurements.",
    )

class ExposureBiomarkerObservationTypeEnum(EnumDefinitionImpl):
    """
    Observation types for exposure biomarker measurements.
    """
    urinary_cotinine = PermissibleValue(
        text="urinary_cotinine",
        description="Urinary cotinine level (tobacco smoke biomarker)",
        meaning=CHEBI["68641"])
    serum_cotinine = PermissibleValue(
        text="serum_cotinine",
        description="Serum cotinine level")
    urinary_1_hydroxypyrene = PermissibleValue(
        text="urinary_1_hydroxypyrene",
        description="Urinary 1-hydroxypyrene (PAH biomarker)")
    blood_lead = PermissibleValue(
        text="blood_lead",
        description="Blood lead concentration")
    urinary_arsenic = PermissibleValue(
        text="urinary_arsenic",
        description="Urinary arsenic species")
    urinary_cadmium = PermissibleValue(
        text="urinary_cadmium",
        description="Urinary cadmium concentration")
    exhaled_co = PermissibleValue(
        text="exhaled_co",
        description="Exhaled carbon monoxide (smoking biomarker)")

    _defn = EnumDefinition(
        name="ExposureBiomarkerObservationTypeEnum",
        description="Observation types for exposure biomarker measurements.",
    )

# Slots
class slots:
    pass

slots.ciliary_measurements = Slot(uri=OUTCOMES_WORKING_GROUP.ciliary_measurements, name="ciliary_measurements", curie=OUTCOMES_WORKING_GROUP.curie('ciliary_measurements'),
                   model_uri=OUTCOMES_WORKING_GROUP.ciliary_measurements, domain=None, range=Optional[Union[dict[Union[str, CiliaryFunctionMeasurementId], Union[dict, CiliaryFunctionMeasurement]], list[Union[dict, CiliaryFunctionMeasurement]]]])

slots.asl_measurements = Slot(uri=OUTCOMES_WORKING_GROUP.asl_measurements, name="asl_measurements", curie=OUTCOMES_WORKING_GROUP.curie('asl_measurements'),
                   model_uri=OUTCOMES_WORKING_GROUP.asl_measurements, domain=None, range=Optional[Union[dict[Union[str, ASLMeasurementId], Union[dict, ASLMeasurement]], list[Union[dict, ASLMeasurement]]]])

slots.mcc_measurements = Slot(uri=OUTCOMES_WORKING_GROUP.mcc_measurements, name="mcc_measurements", curie=OUTCOMES_WORKING_GROUP.curie('mcc_measurements'),
                   model_uri=OUTCOMES_WORKING_GROUP.mcc_measurements, domain=None, range=Optional[Union[dict[Union[str, MCCMeasurementId], Union[dict, MCCMeasurement]], list[Union[dict, MCCMeasurement]]]])

slots.oxidative_stress_measurements = Slot(uri=OUTCOMES_WORKING_GROUP.oxidative_stress_measurements, name="oxidative_stress_measurements", curie=OUTCOMES_WORKING_GROUP.curie('oxidative_stress_measurements'),
                   model_uri=OUTCOMES_WORKING_GROUP.oxidative_stress_measurements, domain=None, range=Optional[Union[dict[Union[str, OxidativeStressMeasurementId], Union[dict, OxidativeStressMeasurement]], list[Union[dict, OxidativeStressMeasurement]]]])

slots.cftr_measurements = Slot(uri=OUTCOMES_WORKING_GROUP.cftr_measurements, name="cftr_measurements", curie=OUTCOMES_WORKING_GROUP.curie('cftr_measurements'),
                   model_uri=OUTCOMES_WORKING_GROUP.cftr_measurements, domain=None, range=Optional[Union[dict[Union[str, CFTRMeasurementId], Union[dict, CFTRMeasurement]], list[Union[dict, CFTRMeasurement]]]])

slots.egfr_measurements = Slot(uri=OUTCOMES_WORKING_GROUP.egfr_measurements, name="egfr_measurements", curie=OUTCOMES_WORKING_GROUP.curie('egfr_measurements'),
                   model_uri=OUTCOMES_WORKING_GROUP.egfr_measurements, domain=None, range=Optional[Union[dict[Union[str, EGFRMeasurementId], Union[dict, EGFRMeasurement]], list[Union[dict, EGFRMeasurement]]]])

slots.goblet_cell_mucin_measurements = Slot(uri=OUTCOMES_WORKING_GROUP.goblet_cell_mucin_measurements, name="goblet_cell_mucin_measurements", curie=OUTCOMES_WORKING_GROUP.curie('goblet_cell_mucin_measurements'),
                   model_uri=OUTCOMES_WORKING_GROUP.goblet_cell_mucin_measurements, domain=None, range=Optional[Union[dict[Union[str, GobletCellMucinMeasurementId], Union[dict, GobletCellMucinMeasurement]], list[Union[dict, GobletCellMucinMeasurement]]]])

slots.balf_sputum_measurements = Slot(uri=OUTCOMES_WORKING_GROUP.balf_sputum_measurements, name="balf_sputum_measurements", curie=OUTCOMES_WORKING_GROUP.curie('balf_sputum_measurements'),
                   model_uri=OUTCOMES_WORKING_GROUP.balf_sputum_measurements, domain=None, range=Optional[Union[dict[Union[str, BALFSputumMeasurementId], Union[dict, BALFSputumMeasurement]], list[Union[dict, BALFSputumMeasurement]]]])

slots.lung_function_measurements = Slot(uri=OUTCOMES_WORKING_GROUP.lung_function_measurements, name="lung_function_measurements", curie=OUTCOMES_WORKING_GROUP.curie('lung_function_measurements'),
                   model_uri=OUTCOMES_WORKING_GROUP.lung_function_measurements, domain=None, range=Optional[Union[dict[Union[str, LungFunctionMeasurementId], Union[dict, LungFunctionMeasurement]], list[Union[dict, LungFunctionMeasurement]]]])

slots.foxj_measurements = Slot(uri=OUTCOMES_WORKING_GROUP.foxj_measurements, name="foxj_measurements", curie=OUTCOMES_WORKING_GROUP.curie('foxj_measurements'),
                   model_uri=OUTCOMES_WORKING_GROUP.foxj_measurements, domain=None, range=Optional[Union[dict[Union[str, FoxJMeasurementId], Union[dict, FoxJMeasurement]], list[Union[dict, FoxJMeasurement]]]])

slots.exposure_biomarker_measurements = Slot(uri=OUTCOMES_WORKING_GROUP.exposure_biomarker_measurements, name="exposure_biomarker_measurements", curie=OUTCOMES_WORKING_GROUP.curie('exposure_biomarker_measurements'),
                   model_uri=OUTCOMES_WORKING_GROUP.exposure_biomarker_measurements, domain=None, range=Optional[Union[dict[Union[str, ExposureBiomarkerMeasurementId], Union[dict, ExposureBiomarkerMeasurement]], list[Union[dict, ExposureBiomarkerMeasurement]]]])

slots.protocols = Slot(uri=OUTCOMES_WORKING_GROUP.protocols, name="protocols", curie=OUTCOMES_WORKING_GROUP.curie('protocols'),
                   model_uri=OUTCOMES_WORKING_GROUP.protocols, domain=None, range=Optional[Union[dict[Union[str, ProtocolId], Union[dict, Protocol]], list[Union[dict, Protocol]]]])

slots.methods = Slot(uri=OUTCOMES_WORKING_GROUP.methods, name="methods", curie=OUTCOMES_WORKING_GROUP.curie('methods'),
                   model_uri=OUTCOMES_WORKING_GROUP.methods, domain=None, range=Optional[Union[dict[Union[str, MethodId], Union[dict, Method]], list[Union[dict, Method]]]])

slots.assays = Slot(uri=OUTCOMES_WORKING_GROUP.assays, name="assays", curie=OUTCOMES_WORKING_GROUP.curie('assays'),
                   model_uri=OUTCOMES_WORKING_GROUP.assays, domain=None, range=Optional[Union[dict[Union[str, AssayId], Union[dict, Assay]], list[Union[dict, Assay]]]])

slots.id = Slot(uri=MEASUREMENT_BASE.id, name="id", curie=MEASUREMENT_BASE.curie('id'),
                   model_uri=OUTCOMES_WORKING_GROUP.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=OUTCOMES_WORKING_GROUP.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=OUTCOMES_WORKING_GROUP.description, domain=None, range=Optional[str])

slots.observation_type = Slot(uri=MEASUREMENT_BASE.observation_type, name="observation_type", curie=MEASUREMENT_BASE.curie('observation_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.observation_type, domain=None, range=Optional[str])

slots.quantity_measured = Slot(uri=MEASUREMENT_BASE.quantity_measured, name="quantity_measured", curie=MEASUREMENT_BASE.curie('quantity_measured'),
                   model_uri=OUTCOMES_WORKING_GROUP.quantity_measured, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.range_low = Slot(uri=MEASUREMENT_BASE.range_low, name="range_low", curie=MEASUREMENT_BASE.curie('range_low'),
                   model_uri=OUTCOMES_WORKING_GROUP.range_low, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.range_high = Slot(uri=MEASUREMENT_BASE.range_high, name="range_high", curie=MEASUREMENT_BASE.curie('range_high'),
                   model_uri=OUTCOMES_WORKING_GROUP.range_high, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.measured_entity = Slot(uri=MEASUREMENT_BASE.measured_entity, name="measured_entity", curie=MEASUREMENT_BASE.curie('measured_entity'),
                   model_uri=OUTCOMES_WORKING_GROUP.measured_entity, domain=None, range=Optional[Union[dict, NamedEntity]])

slots.measurement_method = Slot(uri=MEASUREMENT_BASE.measurement_method, name="measurement_method", curie=MEASUREMENT_BASE.curie('measurement_method'),
                   model_uri=OUTCOMES_WORKING_GROUP.measurement_method, domain=None, range=Optional[str])

slots.measurement_date = Slot(uri=MEASUREMENT_BASE.measurement_date, name="measurement_date", curie=MEASUREMENT_BASE.curie('measurement_date'),
                   model_uri=OUTCOMES_WORKING_GROUP.measurement_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.uses = Slot(uri=MEASUREMENT_BASE.uses, name="uses", curie=MEASUREMENT_BASE.curie('uses'),
                   model_uri=OUTCOMES_WORKING_GROUP.uses, domain=None, range=Optional[Union[dict, Assay]])

slots.implements = Slot(uri=MEASUREMENT_BASE.implements, name="implements", curie=MEASUREMENT_BASE.curie('implements'),
                   model_uri=OUTCOMES_WORKING_GROUP.implements, domain=None, range=Optional[Union[dict, Assay]])

slots.specified_by = Slot(uri=MEASUREMENT_BASE.specified_by, name="specified_by", curie=MEASUREMENT_BASE.curie('specified_by'),
                   model_uri=OUTCOMES_WORKING_GROUP.specified_by, domain=None, range=Optional[Union[dict, Method]])

slots.follows = Slot(uri=MEASUREMENT_BASE.follows, name="follows", curie=MEASUREMENT_BASE.curie('follows'),
                   model_uri=OUTCOMES_WORKING_GROUP.follows, domain=None, range=Optional[Union[dict, Assay]])

slots.study_context = Slot(uri=MEASUREMENT_BASE.study_context, name="study_context", curie=MEASUREMENT_BASE.curie('study_context'),
                   model_uri=OUTCOMES_WORKING_GROUP.study_context, domain=None, range=Optional[Union[str, "StudyContextEnum"]])

slots.imaging_frame_rate = Slot(uri=MEASUREMENT_BASE.imaging_frame_rate, name="imaging_frame_rate", curie=MEASUREMENT_BASE.curie('imaging_frame_rate'),
                   model_uri=OUTCOMES_WORKING_GROUP.imaging_frame_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.imaging_duration = Slot(uri=MEASUREMENT_BASE.imaging_duration, name="imaging_duration", curie=MEASUREMENT_BASE.curie('imaging_duration'),
                   model_uri=OUTCOMES_WORKING_GROUP.imaging_duration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.spatial_resolution = Slot(uri=MEASUREMENT_BASE.spatial_resolution, name="spatial_resolution", curie=MEASUREMENT_BASE.curie('spatial_resolution'),
                   model_uri=OUTCOMES_WORKING_GROUP.spatial_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.temperature_control = Slot(uri=MEASUREMENT_BASE.temperature_control, name="temperature_control", curie=MEASUREMENT_BASE.curie('temperature_control'),
                   model_uri=OUTCOMES_WORKING_GROUP.temperature_control, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.humidity_control = Slot(uri=MEASUREMENT_BASE.humidity_control, name="humidity_control", curie=MEASUREMENT_BASE.curie('humidity_control'),
                   model_uri=OUTCOMES_WORKING_GROUP.humidity_control, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.evaporation_control = Slot(uri=MEASUREMENT_BASE.evaporation_control, name="evaporation_control", curie=MEASUREMENT_BASE.curie('evaporation_control'),
                   model_uri=OUTCOMES_WORKING_GROUP.evaporation_control, domain=None, range=Optional[str])

slots.detection_method = Slot(uri=MEASUREMENT_BASE.detection_method, name="detection_method", curie=MEASUREMENT_BASE.curie('detection_method'),
                   model_uri=OUTCOMES_WORKING_GROUP.detection_method, domain=None, range=Optional[str])

slots.staining_type = Slot(uri=MEASUREMENT_BASE.staining_type, name="staining_type", curie=MEASUREMENT_BASE.curie('staining_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.staining_type, domain=None, range=Optional[str])

slots.antibody_used = Slot(uri=MEASUREMENT_BASE.antibody_used, name="antibody_used", curie=MEASUREMENT_BASE.curie('antibody_used'),
                   model_uri=OUTCOMES_WORKING_GROUP.antibody_used, domain=None, range=Optional[Union[str, list[str]]])

slots.probe_type = Slot(uri=MEASUREMENT_BASE.probe_type, name="probe_type", curie=MEASUREMENT_BASE.curie('probe_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.probe_type, domain=None, range=Optional[str])

slots.normalization_method = Slot(uri=MEASUREMENT_BASE.normalization_method, name="normalization_method", curie=MEASUREMENT_BASE.curie('normalization_method'),
                   model_uri=OUTCOMES_WORKING_GROUP.normalization_method, domain=None, range=Optional[str])

slots.replicate_count = Slot(uri=MEASUREMENT_BASE.replicate_count, name="replicate_count", curie=MEASUREMENT_BASE.curie('replicate_count'),
                   model_uri=OUTCOMES_WORKING_GROUP.replicate_count, domain=None, range=Optional[int])

slots.quality_control_criteria = Slot(uri=MEASUREMENT_BASE.quality_control_criteria, name="quality_control_criteria", curie=MEASUREMENT_BASE.curie('quality_control_criteria'),
                   model_uri=OUTCOMES_WORKING_GROUP.quality_control_criteria, domain=None, range=Optional[str])

slots.cell_culture_system = Slot(uri=MEASUREMENT_BASE.cell_culture_system, name="cell_culture_system", curie=MEASUREMENT_BASE.curie('cell_culture_system'),
                   model_uri=OUTCOMES_WORKING_GROUP.cell_culture_system, domain=None, range=Optional[str])

slots.days_at_differentiation = Slot(uri=MEASUREMENT_BASE.days_at_differentiation, name="days_at_differentiation", curie=MEASUREMENT_BASE.curie('days_at_differentiation'),
                   model_uri=OUTCOMES_WORKING_GROUP.days_at_differentiation, domain=None, range=Optional[int])

slots.passage_number = Slot(uri=MEASUREMENT_BASE.passage_number, name="passage_number", curie=MEASUREMENT_BASE.curie('passage_number'),
                   model_uri=OUTCOMES_WORKING_GROUP.passage_number, domain=None, range=Optional[int])

slots.substrate_type = Slot(uri=MEASUREMENT_BASE.substrate_type, name="substrate_type", curie=MEASUREMENT_BASE.curie('substrate_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.substrate_type, domain=None, range=Optional[str])

slots.donor_info = Slot(uri=MEASUREMENT_BASE.donor_info, name="donor_info", curie=MEASUREMENT_BASE.curie('donor_info'),
                   model_uri=OUTCOMES_WORKING_GROUP.donor_info, domain=None, range=Optional[str])

slots.replicates_per_donor = Slot(uri=MEASUREMENT_BASE.replicates_per_donor, name="replicates_per_donor", curie=MEASUREMENT_BASE.curie('replicates_per_donor'),
                   model_uri=OUTCOMES_WORKING_GROUP.replicates_per_donor, domain=None, range=Optional[int])

slots.culture_medium = Slot(uri=MEASUREMENT_BASE.culture_medium, name="culture_medium", curie=MEASUREMENT_BASE.curie('culture_medium'),
                   model_uri=OUTCOMES_WORKING_GROUP.culture_medium, domain=None, range=Optional[str])

slots.participant = Slot(uri=MEASUREMENT_BASE.participant, name="participant", curie=MEASUREMENT_BASE.curie('participant'),
                   model_uri=OUTCOMES_WORKING_GROUP.participant, domain=None, range=Optional[Union[dict, NamedEntity]])

slots.sample_type = Slot(uri=MEASUREMENT_BASE.sample_type, name="sample_type", curie=MEASUREMENT_BASE.curie('sample_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.sample_type, domain=None, range=Optional[Union[str, "SampleTypeEnum"]])

slots.collection_site = Slot(uri=MEASUREMENT_BASE.collection_site, name="collection_site", curie=MEASUREMENT_BASE.curie('collection_site'),
                   model_uri=OUTCOMES_WORKING_GROUP.collection_site, domain=None, range=Optional[str])

slots.collection_date = Slot(uri=MEASUREMENT_BASE.collection_date, name="collection_date", curie=MEASUREMENT_BASE.curie('collection_date'),
                   model_uri=OUTCOMES_WORKING_GROUP.collection_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.subject_characteristics = Slot(uri=MEASUREMENT_BASE.subject_characteristics, name="subject_characteristics", curie=MEASUREMENT_BASE.curie('subject_characteristics'),
                   model_uri=OUTCOMES_WORKING_GROUP.subject_characteristics, domain=None, range=Optional[str])

slots.value = Slot(uri=MEASUREMENT_BASE.value, name="value", curie=MEASUREMENT_BASE.curie('value'),
                   model_uri=OUTCOMES_WORKING_GROUP.value, domain=None, range=Optional[str])

slots.unit = Slot(uri=MEASUREMENT_BASE.unit, name="unit", curie=MEASUREMENT_BASE.curie('unit'),
                   model_uri=OUTCOMES_WORKING_GROUP.unit, domain=None, range=Optional[Union[dict, Unit]])

slots.CiliaryFunctionMeasurement_observation_type = Slot(uri=MEASUREMENT_BASE.observation_type, name="CiliaryFunctionMeasurement_observation_type", curie=MEASUREMENT_BASE.curie('observation_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.CiliaryFunctionMeasurement_observation_type, domain=CiliaryFunctionMeasurement, range=Optional[Union[str, "CiliaryFunctionObservationTypeEnum"]])

slots.ASLMeasurement_observation_type = Slot(uri=MEASUREMENT_BASE.observation_type, name="ASLMeasurement_observation_type", curie=MEASUREMENT_BASE.curie('observation_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.ASLMeasurement_observation_type, domain=ASLMeasurement, range=Optional[Union[str, "ASLObservationTypeEnum"]])

slots.MCCMeasurement_observation_type = Slot(uri=MEASUREMENT_BASE.observation_type, name="MCCMeasurement_observation_type", curie=MEASUREMENT_BASE.curie('observation_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.MCCMeasurement_observation_type, domain=MCCMeasurement, range=Optional[Union[str, "MCCObservationTypeEnum"]])

slots.OxidativeStressMeasurement_observation_type = Slot(uri=MEASUREMENT_BASE.observation_type, name="OxidativeStressMeasurement_observation_type", curie=MEASUREMENT_BASE.curie('observation_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.OxidativeStressMeasurement_observation_type, domain=OxidativeStressMeasurement, range=Optional[Union[str, "OxidativeStressObservationTypeEnum"]])

slots.CFTRMeasurement_observation_type = Slot(uri=MEASUREMENT_BASE.observation_type, name="CFTRMeasurement_observation_type", curie=MEASUREMENT_BASE.curie('observation_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.CFTRMeasurement_observation_type, domain=CFTRMeasurement, range=Optional[Union[str, "CFTRObservationTypeEnum"]])

slots.EGFRMeasurement_observation_type = Slot(uri=MEASUREMENT_BASE.observation_type, name="EGFRMeasurement_observation_type", curie=MEASUREMENT_BASE.curie('observation_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.EGFRMeasurement_observation_type, domain=EGFRMeasurement, range=Optional[Union[str, "EGFRObservationTypeEnum"]])

slots.GobletCellMucinMeasurement_observation_type = Slot(uri=MEASUREMENT_BASE.observation_type, name="GobletCellMucinMeasurement_observation_type", curie=MEASUREMENT_BASE.curie('observation_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.GobletCellMucinMeasurement_observation_type, domain=GobletCellMucinMeasurement, range=Optional[Union[str, "GobletCellMucinObservationTypeEnum"]])

slots.BALFSputumMeasurement_observation_type = Slot(uri=MEASUREMENT_BASE.observation_type, name="BALFSputumMeasurement_observation_type", curie=MEASUREMENT_BASE.curie('observation_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.BALFSputumMeasurement_observation_type, domain=BALFSputumMeasurement, range=Optional[Union[str, "BALFSputumObservationTypeEnum"]])

slots.LungFunctionMeasurement_observation_type = Slot(uri=MEASUREMENT_BASE.observation_type, name="LungFunctionMeasurement_observation_type", curie=MEASUREMENT_BASE.curie('observation_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.LungFunctionMeasurement_observation_type, domain=LungFunctionMeasurement, range=Optional[Union[str, "LungFunctionObservationTypeEnum"]])

slots.FoxJMeasurement_observation_type = Slot(uri=MEASUREMENT_BASE.observation_type, name="FoxJMeasurement_observation_type", curie=MEASUREMENT_BASE.curie('observation_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.FoxJMeasurement_observation_type, domain=FoxJMeasurement, range=Optional[Union[str, "FoxJObservationTypeEnum"]])

slots.ExposureBiomarkerMeasurement_observation_type = Slot(uri=MEASUREMENT_BASE.observation_type, name="ExposureBiomarkerMeasurement_observation_type", curie=MEASUREMENT_BASE.curie('observation_type'),
                   model_uri=OUTCOMES_WORKING_GROUP.ExposureBiomarkerMeasurement_observation_type, domain=ExposureBiomarkerMeasurement, range=Optional[Union[str, "ExposureBiomarkerObservationTypeEnum"]])
