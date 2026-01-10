# Auto generated from outcomes_working_group.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-01-10T15:24:03
# Schema: outcomes_working_group
#
# id: https://w3id.org/EHS-Data-Standards/outcomes_working_group
# description: A LinkML data model for representing biological measurements, assays, and experimental protocols in the context of outcomes research.
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

from linkml_runtime.linkml_model.types import Date, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
AOPWIKI = CurieNamespace('AOPWIKI', 'https://aopwiki.org/aops/')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
CTD_CHEMICAL = CurieNamespace('CTD_CHEMICAL', 'http://ctdbase.org/detail.go?type=chem&acc=')
CTD_GENE = CurieNamespace('CTD_GENE', 'http://ctdbase.org/detail.go?type=gene&acc=')
DTXSID = CurieNamespace('DTXSID', 'https://comptox.epa.gov/dashboard/dsstoxdb/results?search=')
ECTO = CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_')
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
FOODON = CurieNamespace('FOODON', 'http://purl.obolibrary.org/obo/FOODON_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
GWAS = CurieNamespace('GWAS', 'https://www.ebi.ac.uk/gwas/studies/')
GXA = CurieNamespace('GXA', 'https://www.ebi.ac.uk/gxa/experiments/')
HHEAR = CurieNamespace('HHEAR', 'http://hadatac.org/ont/hhear#')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
MP = CurieNamespace('MP', 'http://purl.obolibrary.org/obo/MP_')
NCBIGENE = CurieNamespace('NCBIGENE', 'https://www.ncbi.nlm.nih.gov/gene/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
NHANES = CurieNamespace('NHANES', 'https://wwwn.cdc.gov/Nchs/Nhanes/')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://identifiers.org/pubchem.compound/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UCUM = CurieNamespace('UCUM', 'http://unitsofmeasure.org/')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
UPHENO = CurieNamespace('UPHENO', 'http://purl.obolibrary.org/obo/UPHENO_')
USDA_PESTICIDE = CurieNamespace('USDA_PESTICIDE', 'https://www.ams.usda.gov/datasets/pdp/')
ZP = CurieNamespace('ZP', 'http://purl.obolibrary.org/obo/ZP_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
CHEAR = CurieNamespace('chear', 'http://hadatac.org/ont/chear#')
FHIR = CurieNamespace('fhir', 'http://hl7.org/fhir/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWG = CurieNamespace('owg', 'https://w3id.org/EHS-Data-Standards/outcomes-working-group/')
QUDT = CurieNamespace('qudt', 'http://qudt.org/vocab/unit/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = OWG


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class UnitId(NamedThingId):
    pass


class OntologyTermId(NamedThingId):
    pass


class TissueId(NamedThingId):
    pass


class BiologicalEntityId(NamedThingId):
    pass


class ChemicalEntityId(NamedThingId):
    pass


class ExposureEventId(NamedThingId):
    pass


class BiologicalResponseId(NamedThingId):
    pass


class HealthOutcomeId(NamedThingId):
    pass


class StudyEntityId(NamedThingId):
    pass


class MeasurementId(NamedThingId):
    pass


class AssociationId(NamedThingId):
    pass


class ChemicalExposureId(ExposureEventId):
    pass


class DietaryExposureId(ExposureEventId):
    pass


class EnvironmentalExposureId(ExposureEventId):
    pass


class OccupationalExposureId(ExposureEventId):
    pass


class PhenotypeId(HealthOutcomeId):
    pass


class DiseaseId(HealthOutcomeId):
    pass


class AdverseOutcomeId(HealthOutcomeId):
    pass


class AdverseOutcomePathwayId(NamedThingId):
    pass


class MolecularInitiatingEventId(BiologicalResponseId):
    pass


class KeyEventId(BiologicalResponseId):
    pass


class KeyEventRelationshipId(AssociationId):
    pass


class StudyId(StudyEntityId):
    pass


class CohortId(StudyEntityId):
    pass


class ParticipantId(StudyEntityId):
    pass


class ExposureMeasurementId(MeasurementId):
    pass


class BiomarkerMeasurementId(MeasurementId):
    pass


class PhenotypeMeasurementId(MeasurementId):
    pass


class AggregatedMeasurementId(MeasurementId):
    pass


class GeneExpressionMeasurementId(MeasurementId):
    pass


class ProteinExpressionMeasurementId(MeasurementId):
    pass


class GeneId(BiologicalEntityId):
    pass


class ProteinId(BiologicalEntityId):
    pass


class CellTypeId(BiologicalEntityId):
    pass


class AnatomicalEntityId(BiologicalEntityId):
    pass


class OrganismId(BiologicalEntityId):
    pass


class ExposureToPhenotypeAssociationId(AssociationId):
    pass


class ChemicalToGeneAssociationId(AssociationId):
    pass


class GeneToDiseaseAssociationId(AssociationId):
    pass


@dataclass(repr=False)
class Container(YAMLRoot):
    """
    A container for collections of measurements and related entities. Used as the root class for data validation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Container"]
    class_class_curie: ClassVar[str] = "owg:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = OWG.Container

    studies: Optional[Union[dict[Union[str, StudyId], Union[dict, "Study"]], list[Union[dict, "Study"]]]] = empty_dict()
    cohorts: Optional[Union[dict[Union[str, CohortId], Union[dict, "Cohort"]], list[Union[dict, "Cohort"]]]] = empty_dict()
    participants: Optional[Union[dict[Union[str, ParticipantId], Union[dict, "Participant"]], list[Union[dict, "Participant"]]]] = empty_dict()
    exposure_measurements: Optional[Union[dict[Union[str, ExposureMeasurementId], Union[dict, "ExposureMeasurement"]], list[Union[dict, "ExposureMeasurement"]]]] = empty_dict()
    biomarker_measurements: Optional[Union[dict[Union[str, BiomarkerMeasurementId], Union[dict, "BiomarkerMeasurement"]], list[Union[dict, "BiomarkerMeasurement"]]]] = empty_dict()
    phenotype_measurements: Optional[Union[dict[Union[str, PhenotypeMeasurementId], Union[dict, "PhenotypeMeasurement"]], list[Union[dict, "PhenotypeMeasurement"]]]] = empty_dict()
    aggregated_measurements: Optional[Union[dict[Union[str, AggregatedMeasurementId], Union[dict, "AggregatedMeasurement"]], list[Union[dict, "AggregatedMeasurement"]]]] = empty_dict()
    gene_expression_measurements: Optional[Union[dict[Union[str, GeneExpressionMeasurementId], Union[dict, "GeneExpressionMeasurement"]], list[Union[dict, "GeneExpressionMeasurement"]]]] = empty_dict()
    protein_expression_measurements: Optional[Union[dict[Union[str, ProteinExpressionMeasurementId], Union[dict, "ProteinExpressionMeasurement"]], list[Union[dict, "ProteinExpressionMeasurement"]]]] = empty_dict()
    chemical_exposures: Optional[Union[dict[Union[str, ChemicalExposureId], Union[dict, "ChemicalExposure"]], list[Union[dict, "ChemicalExposure"]]]] = empty_dict()
    dietary_exposures: Optional[Union[dict[Union[str, DietaryExposureId], Union[dict, "DietaryExposure"]], list[Union[dict, "DietaryExposure"]]]] = empty_dict()
    environmental_exposures: Optional[Union[dict[Union[str, EnvironmentalExposureId], Union[dict, "EnvironmentalExposure"]], list[Union[dict, "EnvironmentalExposure"]]]] = empty_dict()
    occupational_exposures: Optional[Union[dict[Union[str, OccupationalExposureId], Union[dict, "OccupationalExposure"]], list[Union[dict, "OccupationalExposure"]]]] = empty_dict()
    phenotypes: Optional[Union[dict[Union[str, PhenotypeId], Union[dict, "Phenotype"]], list[Union[dict, "Phenotype"]]]] = empty_dict()
    diseases: Optional[Union[dict[Union[str, DiseaseId], Union[dict, "Disease"]], list[Union[dict, "Disease"]]]] = empty_dict()
    adverse_outcomes: Optional[Union[dict[Union[str, AdverseOutcomeId], Union[dict, "AdverseOutcome"]], list[Union[dict, "AdverseOutcome"]]]] = empty_dict()
    adverse_outcome_pathways: Optional[Union[dict[Union[str, AdverseOutcomePathwayId], Union[dict, "AdverseOutcomePathway"]], list[Union[dict, "AdverseOutcomePathway"]]]] = empty_dict()
    genes: Optional[Union[dict[Union[str, GeneId], Union[dict, "Gene"]], list[Union[dict, "Gene"]]]] = empty_dict()
    proteins: Optional[Union[dict[Union[str, ProteinId], Union[dict, "Protein"]], list[Union[dict, "Protein"]]]] = empty_dict()
    cell_types: Optional[Union[dict[Union[str, CellTypeId], Union[dict, "CellType"]], list[Union[dict, "CellType"]]]] = empty_dict()
    anatomical_entities: Optional[Union[dict[Union[str, AnatomicalEntityId], Union[dict, "AnatomicalEntity"]], list[Union[dict, "AnatomicalEntity"]]]] = empty_dict()
    organisms: Optional[Union[dict[Union[str, OrganismId], Union[dict, "Organism"]], list[Union[dict, "Organism"]]]] = empty_dict()
    exposure_to_phenotype_associations: Optional[Union[dict[Union[str, ExposureToPhenotypeAssociationId], Union[dict, "ExposureToPhenotypeAssociation"]], list[Union[dict, "ExposureToPhenotypeAssociation"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="studies", slot_type=Study, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="cohorts", slot_type=Cohort, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="participants", slot_type=Participant, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="exposure_measurements", slot_type=ExposureMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="biomarker_measurements", slot_type=BiomarkerMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="phenotype_measurements", slot_type=PhenotypeMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aggregated_measurements", slot_type=AggregatedMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="gene_expression_measurements", slot_type=GeneExpressionMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="protein_expression_measurements", slot_type=ProteinExpressionMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="chemical_exposures", slot_type=ChemicalExposure, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dietary_exposures", slot_type=DietaryExposure, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="environmental_exposures", slot_type=EnvironmentalExposure, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="occupational_exposures", slot_type=OccupationalExposure, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="phenotypes", slot_type=Phenotype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="diseases", slot_type=Disease, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="adverse_outcomes", slot_type=AdverseOutcome, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="adverse_outcome_pathways", slot_type=AdverseOutcomePathway, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="genes", slot_type=Gene, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="proteins", slot_type=Protein, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="cell_types", slot_type=CellType, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="anatomical_entities", slot_type=AnatomicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="organisms", slot_type=Organism, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="exposure_to_phenotype_associations", slot_type=ExposureToPhenotypeAssociation, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity in the exposome
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["NamedThing"]
    class_class_curie: ClassVar[str] = "owg:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = OWG.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[Union[str, list[str]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, str) else str(v) for v in self.category]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Unit(NamedThing):
    """
    A unit of measurement from a standard ontology (UO, UCUM, QUDT)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Unit"]
    class_class_curie: ClassVar[str] = "owg:Unit"
    class_name: ClassVar[str] = "Unit"
    class_model_uri: ClassVar[URIRef] = OWG.Unit

    id: Union[str, UnitId] = None
    unit_label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnitId):
            self.id = UnitId(self.id)

        if self.unit_label is not None and not isinstance(self.unit_label, str):
            self.unit_label = str(self.unit_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(YAMLRoot):
    """
    A quantity with a numeric value and unit of measurement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["Quantity"]
    class_class_curie: ClassVar[str] = "fhir:Quantity"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = OWG.QuantityValue

    unit: Optional[Union[dict, Unit]] = None
    value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.unit is not None and not isinstance(self.unit, Unit):
            self.unit = Unit(**as_dict(self.unit))

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityRange(YAMLRoot):
    """
    A range of quantities with lower and upper bounds
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["Range"]
    class_class_curie: ClassVar[str] = "fhir:Range"
    class_name: ClassVar[str] = "QuantityRange"
    class_model_uri: ClassVar[URIRef] = OWG.QuantityRange

    lower_bound: Optional[Union[dict, QuantityValue]] = None
    upper_bound: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.lower_bound is not None and not isinstance(self.lower_bound, QuantityValue):
            self.lower_bound = QuantityValue(**as_dict(self.lower_bound))

        if self.upper_bound is not None and not isinstance(self.upper_bound, QuantityValue):
            self.upper_bound = QuantityValue(**as_dict(self.upper_bound))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OntologyTerm(NamedThing):
    """
    A reference to an ontology term with both identifier and human-readable name. Used for measured entities,
    phenotypes, and other ontology-backed concepts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["OntologyTerm"]
    class_class_curie: ClassVar[str] = "owg:OntologyTerm"
    class_name: ClassVar[str] = "OntologyTerm"
    class_model_uri: ClassVar[URIRef] = OWG.OntologyTerm

    id: Union[str, OntologyTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyTermId):
            self.id = OntologyTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tissue(NamedThing):
    """
    A reference to an anatomical tissue or structure with identifier and name. Used for tissue_context in expression
    measurements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Tissue"]
    class_class_curie: ClassVar[str] = "owg:Tissue"
    class_name: ClassVar[str] = "Tissue"
    class_model_uri: ClassVar[URIRef] = OWG.Tissue

    id: Union[str, TissueId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TissueId):
            self.id = TissueId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalEntity(NamedThing):
    """
    Biological entities including genes, proteins, cells, and anatomical structures
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["BiologicalEntity"]
    class_class_curie: ClassVar[str] = "owg:BiologicalEntity"
    class_name: ClassVar[str] = "BiologicalEntity"
    class_model_uri: ClassVar[URIRef] = OWG.BiologicalEntity

    id: Union[str, BiologicalEntityId] = None

@dataclass(repr=False)
class ChemicalEntity(NamedThing):
    """
    A chemical entity including compounds, drugs, and metabolites
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["24431"]
    class_class_curie: ClassVar[str] = "CHEBI:24431"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = OWG.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    chebi_id: Optional[Union[str, URIorCURIE]] = None
    dtxsid: Optional[str] = None
    chembl_id: Optional[str] = None
    pubchem_cid: Optional[int] = None
    cas_number: Optional[str] = None
    inchi: Optional[str] = None
    smiles: Optional[str] = None
    molecular_formula: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        if self.chebi_id is not None and not isinstance(self.chebi_id, URIorCURIE):
            self.chebi_id = URIorCURIE(self.chebi_id)

        if self.dtxsid is not None and not isinstance(self.dtxsid, str):
            self.dtxsid = str(self.dtxsid)

        if self.chembl_id is not None and not isinstance(self.chembl_id, str):
            self.chembl_id = str(self.chembl_id)

        if self.pubchem_cid is not None and not isinstance(self.pubchem_cid, int):
            self.pubchem_cid = int(self.pubchem_cid)

        if self.cas_number is not None and not isinstance(self.cas_number, str):
            self.cas_number = str(self.cas_number)

        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        if self.molecular_formula is not None and not isinstance(self.molecular_formula, str):
            self.molecular_formula = str(self.molecular_formula)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureEvent(NamedThing):
    """
    An event in which an organism is exposed to a chemical or environmental factor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["ExposureEvent"]
    class_class_curie: ClassVar[str] = "owg:ExposureEvent"
    class_name: ClassVar[str] = "ExposureEvent"
    class_model_uri: ClassVar[URIRef] = OWG.ExposureEvent

    id: Union[str, ExposureEventId] = None
    exposed_to_chemical: Optional[Union[str, ChemicalEntityId]] = None
    exposure_route: Optional[Union[str, "ExposureRouteEnum"]] = None
    exposure_duration: Optional[str] = None
    exposure_concentration: Optional[float] = None
    exposure_medium: Optional[Union[str, "ExposureMediumEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.exposed_to_chemical is not None and not isinstance(self.exposed_to_chemical, ChemicalEntityId):
            self.exposed_to_chemical = ChemicalEntityId(self.exposed_to_chemical)

        if self.exposure_route is not None and not isinstance(self.exposure_route, ExposureRouteEnum):
            self.exposure_route = ExposureRouteEnum(self.exposure_route)

        if self.exposure_duration is not None and not isinstance(self.exposure_duration, str):
            self.exposure_duration = str(self.exposure_duration)

        if self.exposure_concentration is not None and not isinstance(self.exposure_concentration, float):
            self.exposure_concentration = float(self.exposure_concentration)

        if self.exposure_medium is not None and not isinstance(self.exposure_medium, ExposureMediumEnum):
            self.exposure_medium = ExposureMediumEnum(self.exposure_medium)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalResponse(NamedThing):
    """
    A biological response at the molecular, cellular, or tissue level
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["BiologicalResponse"]
    class_class_curie: ClassVar[str] = "owg:BiologicalResponse"
    class_name: ClassVar[str] = "BiologicalResponse"
    class_model_uri: ClassVar[URIRef] = OWG.BiologicalResponse

    id: Union[str, BiologicalResponseId] = None

@dataclass(repr=False)
class HealthOutcome(NamedThing):
    """
    A health-related outcome including phenotypes and diseases
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["HealthOutcome"]
    class_class_curie: ClassVar[str] = "owg:HealthOutcome"
    class_name: ClassVar[str] = "HealthOutcome"
    class_model_uri: ClassVar[URIRef] = OWG.HealthOutcome

    id: Union[str, HealthOutcomeId] = None

@dataclass(repr=False)
class StudyEntity(NamedThing):
    """
    Entities related to studies, cohorts, and participants
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["StudyEntity"]
    class_class_curie: ClassVar[str] = "owg:StudyEntity"
    class_name: ClassVar[str] = "StudyEntity"
    class_model_uri: ClassVar[URIRef] = OWG.StudyEntity

    id: Union[str, StudyEntityId] = None

@dataclass(repr=False)
class Measurement(NamedThing):
    """
    A measurement observation with a typed quantity value and optional reference ranges
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Measurement"]
    class_class_curie: ClassVar[str] = "owg:Measurement"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = OWG.Measurement

    id: Union[str, MeasurementId] = None
    observation_type: Optional[Union[str, "MeasurementTypeEnum"]] = None
    quantity_measured: Optional[Union[dict, QuantityValue]] = None
    range_low: Optional[Union[dict, QuantityValue]] = None
    range_high: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.observation_type is not None and not isinstance(self.observation_type, MeasurementTypeEnum):
            self.observation_type = MeasurementTypeEnum(self.observation_type)

        if self.quantity_measured is not None and not isinstance(self.quantity_measured, QuantityValue):
            self.quantity_measured = QuantityValue(**as_dict(self.quantity_measured))

        if self.range_low is not None and not isinstance(self.range_low, QuantityValue):
            self.range_low = QuantityValue(**as_dict(self.range_low))

        if self.range_high is not None and not isinstance(self.range_high, QuantityValue):
            self.range_high = QuantityValue(**as_dict(self.range_high))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Association(NamedThing):
    """
    A relationship between two entities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Association"]
    class_class_curie: ClassVar[str] = "owg:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = OWG.Association

    id: Union[str, AssociationId] = None

@dataclass(repr=False)
class ChemicalExposure(ExposureEvent):
    """
    Exposure to a chemical substance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ECTO["0000006"]
    class_class_curie: ClassVar[str] = "ECTO:0000006"
    class_name: ClassVar[str] = "ChemicalExposure"
    class_model_uri: ClassVar[URIRef] = OWG.ChemicalExposure

    id: Union[str, ChemicalExposureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalExposureId):
            self.id = ChemicalExposureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DietaryExposure(ExposureEvent):
    """
    Exposure through dietary consumption
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOODON["00002403"]
    class_class_curie: ClassVar[str] = "FOODON:00002403"
    class_name: ClassVar[str] = "DietaryExposure"
    class_model_uri: ClassVar[URIRef] = OWG.DietaryExposure

    id: Union[str, DietaryExposureId] = None
    food_item: Optional[str] = None
    serving_size: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DietaryExposureId):
            self.id = DietaryExposureId(self.id)

        if self.food_item is not None and not isinstance(self.food_item, str):
            self.food_item = str(self.food_item)

        if self.serving_size is not None and not isinstance(self.serving_size, str):
            self.serving_size = str(self.serving_size)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentalExposure(ExposureEvent):
    """
    Exposure to environmental factors
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ECTO["0000001"]
    class_class_curie: ClassVar[str] = "ECTO:0000001"
    class_name: ClassVar[str] = "EnvironmentalExposure"
    class_model_uri: ClassVar[URIRef] = OWG.EnvironmentalExposure

    id: Union[str, EnvironmentalExposureId] = None
    environmental_context: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalExposureId):
            self.id = EnvironmentalExposureId(self.id)

        if self.environmental_context is not None and not isinstance(self.environmental_context, str):
            self.environmental_context = str(self.environmental_context)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OccupationalExposure(ExposureEvent):
    """
    Exposure in an occupational setting
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ECTO["0000002"]
    class_class_curie: ClassVar[str] = "ECTO:0000002"
    class_name: ClassVar[str] = "OccupationalExposure"
    class_model_uri: ClassVar[URIRef] = OWG.OccupationalExposure

    id: Union[str, OccupationalExposureId] = None
    occupation: Optional[str] = None
    workplace: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OccupationalExposureId):
            self.id = OccupationalExposureId(self.id)

        if self.occupation is not None and not isinstance(self.occupation, str):
            self.occupation = str(self.occupation)

        if self.workplace is not None and not isinstance(self.workplace, str):
            self.workplace = str(self.workplace)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Phenotype(HealthOutcome):
    """
    An observable characteristic or trait
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UPHENO["0001001"]
    class_class_curie: ClassVar[str] = "UPHENO:0001001"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = OWG.Phenotype

    id: Union[str, PhenotypeId] = None
    severity: Optional[str] = None
    onset_age: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeId):
            self.id = PhenotypeId(self.id)

        if self.severity is not None and not isinstance(self.severity, str):
            self.severity = str(self.severity)

        if self.onset_age is not None and not isinstance(self.onset_age, str):
            self.onset_age = str(self.onset_age)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disease(HealthOutcome):
    """
    A disease or medical condition
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MONDO["0000001"]
    class_class_curie: ClassVar[str] = "MONDO:0000001"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = OWG.Disease

    id: Union[str, DiseaseId] = None
    disease_category: Optional[str] = None
    affected_anatomy: Optional[Union[str, AnatomicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        if self.disease_category is not None and not isinstance(self.disease_category, str):
            self.disease_category = str(self.disease_category)

        if self.affected_anatomy is not None and not isinstance(self.affected_anatomy, AnatomicalEntityId):
            self.affected_anatomy = AnatomicalEntityId(self.affected_anatomy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdverseOutcome(HealthOutcome):
    """
    An adverse health outcome in the context of an Adverse Outcome Pathway
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["AdverseOutcome"]
    class_class_curie: ClassVar[str] = "owg:AdverseOutcome"
    class_name: ClassVar[str] = "AdverseOutcome"
    class_model_uri: ClassVar[URIRef] = OWG.AdverseOutcome

    id: Union[str, AdverseOutcomeId] = None
    outcome_level: Optional[Union[str, "BiologicalOrganizationLevelEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdverseOutcomeId):
            self.id = AdverseOutcomeId(self.id)

        if self.outcome_level is not None and not isinstance(self.outcome_level, BiologicalOrganizationLevelEnum):
            self.outcome_level = BiologicalOrganizationLevelEnum(self.outcome_level)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdverseOutcomePathway(NamedThing):
    """
    A sequence of causally linked events at different levels of biological organization that lead from exposure to
    adverse health outcomes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["AdverseOutcomePathway"]
    class_class_curie: ClassVar[str] = "owg:AdverseOutcomePathway"
    class_name: ClassVar[str] = "AdverseOutcomePathway"
    class_model_uri: ClassVar[URIRef] = OWG.AdverseOutcomePathway

    id: Union[str, AdverseOutcomePathwayId] = None
    aopwiki_id: Optional[str] = None
    molecular_initiating_event: Optional[Union[str, MolecularInitiatingEventId]] = None
    key_events: Optional[Union[Union[str, KeyEventId], list[Union[str, KeyEventId]]]] = empty_list()
    key_event_relationships: Optional[Union[Union[str, KeyEventRelationshipId], list[Union[str, KeyEventRelationshipId]]]] = empty_list()
    adverse_outcome: Optional[Union[str, AdverseOutcomeId]] = None
    stressors: Optional[Union[Union[str, ChemicalEntityId], list[Union[str, ChemicalEntityId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdverseOutcomePathwayId):
            self.id = AdverseOutcomePathwayId(self.id)

        if self.aopwiki_id is not None and not isinstance(self.aopwiki_id, str):
            self.aopwiki_id = str(self.aopwiki_id)

        if self.molecular_initiating_event is not None and not isinstance(self.molecular_initiating_event, MolecularInitiatingEventId):
            self.molecular_initiating_event = MolecularInitiatingEventId(self.molecular_initiating_event)

        if not isinstance(self.key_events, list):
            self.key_events = [self.key_events] if self.key_events is not None else []
        self.key_events = [v if isinstance(v, KeyEventId) else KeyEventId(v) for v in self.key_events]

        if not isinstance(self.key_event_relationships, list):
            self.key_event_relationships = [self.key_event_relationships] if self.key_event_relationships is not None else []
        self.key_event_relationships = [v if isinstance(v, KeyEventRelationshipId) else KeyEventRelationshipId(v) for v in self.key_event_relationships]

        if self.adverse_outcome is not None and not isinstance(self.adverse_outcome, AdverseOutcomeId):
            self.adverse_outcome = AdverseOutcomeId(self.adverse_outcome)

        if not isinstance(self.stressors, list):
            self.stressors = [self.stressors] if self.stressors is not None else []
        self.stressors = [v if isinstance(v, ChemicalEntityId) else ChemicalEntityId(v) for v in self.stressors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularInitiatingEvent(BiologicalResponse):
    """
    The initial molecular-level perturbation that starts an Adverse Outcome Pathway
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ECTO["3000000"]
    class_class_curie: ClassVar[str] = "ECTO:3000000"
    class_name: ClassVar[str] = "MolecularInitiatingEvent"
    class_model_uri: ClassVar[URIRef] = OWG.MolecularInitiatingEvent

    id: Union[str, MolecularInitiatingEventId] = None
    biological_process: Optional[str] = None
    biological_object: Optional[str] = None
    biological_action: Optional[str] = None
    occurs_in_cell_type: Optional[Union[str, CellTypeId]] = None
    occurs_in_anatomy: Optional[Union[str, AnatomicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularInitiatingEventId):
            self.id = MolecularInitiatingEventId(self.id)

        if self.biological_process is not None and not isinstance(self.biological_process, str):
            self.biological_process = str(self.biological_process)

        if self.biological_object is not None and not isinstance(self.biological_object, str):
            self.biological_object = str(self.biological_object)

        if self.biological_action is not None and not isinstance(self.biological_action, str):
            self.biological_action = str(self.biological_action)

        if self.occurs_in_cell_type is not None and not isinstance(self.occurs_in_cell_type, CellTypeId):
            self.occurs_in_cell_type = CellTypeId(self.occurs_in_cell_type)

        if self.occurs_in_anatomy is not None and not isinstance(self.occurs_in_anatomy, AnatomicalEntityId):
            self.occurs_in_anatomy = AnatomicalEntityId(self.occurs_in_anatomy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeyEvent(BiologicalResponse):
    """
    A measurable change in biological state that is a step in an Adverse Outcome Pathway
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ECTO["1000000"]
    class_class_curie: ClassVar[str] = "ECTO:1000000"
    class_name: ClassVar[str] = "KeyEvent"
    class_model_uri: ClassVar[URIRef] = OWG.KeyEvent

    id: Union[str, KeyEventId] = None
    biological_process: Optional[str] = None
    biological_object: Optional[str] = None
    biological_action: Optional[str] = None
    level_of_biological_organization: Optional[Union[str, "BiologicalOrganizationLevelEnum"]] = None
    occurs_in_cell_type: Optional[Union[str, CellTypeId]] = None
    occurs_in_anatomy: Optional[Union[str, AnatomicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeyEventId):
            self.id = KeyEventId(self.id)

        if self.biological_process is not None and not isinstance(self.biological_process, str):
            self.biological_process = str(self.biological_process)

        if self.biological_object is not None and not isinstance(self.biological_object, str):
            self.biological_object = str(self.biological_object)

        if self.biological_action is not None and not isinstance(self.biological_action, str):
            self.biological_action = str(self.biological_action)

        if self.level_of_biological_organization is not None and not isinstance(self.level_of_biological_organization, BiologicalOrganizationLevelEnum):
            self.level_of_biological_organization = BiologicalOrganizationLevelEnum(self.level_of_biological_organization)

        if self.occurs_in_cell_type is not None and not isinstance(self.occurs_in_cell_type, CellTypeId):
            self.occurs_in_cell_type = CellTypeId(self.occurs_in_cell_type)

        if self.occurs_in_anatomy is not None and not isinstance(self.occurs_in_anatomy, AnatomicalEntityId):
            self.occurs_in_anatomy = AnatomicalEntityId(self.occurs_in_anatomy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeyEventRelationship(Association):
    """
    A directional relationship between two key events in an AOP
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["KeyEventRelationship"]
    class_class_curie: ClassVar[str] = "owg:KeyEventRelationship"
    class_name: ClassVar[str] = "KeyEventRelationship"
    class_model_uri: ClassVar[URIRef] = OWG.KeyEventRelationship

    id: Union[str, KeyEventRelationshipId] = None
    upstream_event: Optional[Union[str, KeyEventId]] = None
    downstream_event: Optional[Union[str, KeyEventId]] = None
    relationship_type: Optional[str] = None
    evidence_support: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeyEventRelationshipId):
            self.id = KeyEventRelationshipId(self.id)

        if self.upstream_event is not None and not isinstance(self.upstream_event, KeyEventId):
            self.upstream_event = KeyEventId(self.upstream_event)

        if self.downstream_event is not None and not isinstance(self.downstream_event, KeyEventId):
            self.downstream_event = KeyEventId(self.downstream_event)

        if self.relationship_type is not None and not isinstance(self.relationship_type, str):
            self.relationship_type = str(self.relationship_type)

        if self.evidence_support is not None and not isinstance(self.evidence_support, str):
            self.evidence_support = str(self.evidence_support)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(StudyEntity):
    """
    A research study or survey
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EFO["0001444"]
    class_class_curie: ClassVar[str] = "EFO:0001444"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = OWG.Study

    id: Union[str, StudyId] = None
    study_type: Optional[Union[str, "StudyTypeEnum"]] = None
    population: Optional[str] = None
    enrollment_period: Optional[str] = None
    geographic_location: Optional[str] = None
    principal_investigator: Optional[str] = None
    publications: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self.study_type is not None and not isinstance(self.study_type, StudyTypeEnum):
            self.study_type = StudyTypeEnum(self.study_type)

        if self.population is not None and not isinstance(self.population, str):
            self.population = str(self.population)

        if self.enrollment_period is not None and not isinstance(self.enrollment_period, str):
            self.enrollment_period = str(self.enrollment_period)

        if self.geographic_location is not None and not isinstance(self.geographic_location, str):
            self.geographic_location = str(self.geographic_location)

        if self.principal_investigator is not None and not isinstance(self.principal_investigator, str):
            self.principal_investigator = str(self.principal_investigator)

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, str) else str(v) for v in self.publications]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Cohort(StudyEntity):
    """
    A group of individuals in a study
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Cohort"]
    class_class_curie: ClassVar[str] = "owg:Cohort"
    class_name: ClassVar[str] = "Cohort"
    class_model_uri: ClassVar[URIRef] = OWG.Cohort

    id: Union[str, CohortId] = None
    part_of_study: Optional[Union[str, StudyId]] = None
    cohort_size: Optional[int] = None
    inclusion_criteria: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CohortId):
            self.id = CohortId(self.id)

        if self.part_of_study is not None and not isinstance(self.part_of_study, StudyId):
            self.part_of_study = StudyId(self.part_of_study)

        if self.cohort_size is not None and not isinstance(self.cohort_size, int):
            self.cohort_size = int(self.cohort_size)

        if self.inclusion_criteria is not None and not isinstance(self.inclusion_criteria, str):
            self.inclusion_criteria = str(self.inclusion_criteria)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Participant(StudyEntity):
    """
    An individual participant in a study
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Participant"]
    class_class_curie: ClassVar[str] = "owg:Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = OWG.Participant

    id: Union[str, ParticipantId] = None
    part_of_cohort: Optional[Union[str, CohortId]] = None
    participant_id: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[Union[str, "SexEnum"]] = None
    species: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParticipantId):
            self.id = ParticipantId(self.id)

        if self.part_of_cohort is not None and not isinstance(self.part_of_cohort, CohortId):
            self.part_of_cohort = CohortId(self.part_of_cohort)

        if self.participant_id is not None and not isinstance(self.participant_id, str):
            self.participant_id = str(self.participant_id)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        if self.sex is not None and not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureMeasurement(Measurement):
    """
    A measurement of exposure to a chemical or environmental factor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["ExposureMeasurement"]
    class_class_curie: ClassVar[str] = "owg:ExposureMeasurement"
    class_name: ClassVar[str] = "ExposureMeasurement"
    class_model_uri: ClassVar[URIRef] = OWG.ExposureMeasurement

    id: Union[str, ExposureMeasurementId] = None
    measured_entity: Optional[Union[dict, OntologyTerm]] = None
    participant: Optional[Union[str, ParticipantId]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureMeasurementId):
            self.id = ExposureMeasurementId(self.id)

        if self.measured_entity is not None and not isinstance(self.measured_entity, OntologyTerm):
            self.measured_entity = OntologyTerm(**as_dict(self.measured_entity))

        if self.participant is not None and not isinstance(self.participant, ParticipantId):
            self.participant = ParticipantId(self.participant)

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiomarkerMeasurement(Measurement):
    """
    A measurement of a biological marker
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["BiomarkerMeasurement"]
    class_class_curie: ClassVar[str] = "owg:BiomarkerMeasurement"
    class_name: ClassVar[str] = "BiomarkerMeasurement"
    class_model_uri: ClassVar[URIRef] = OWG.BiomarkerMeasurement

    id: Union[str, BiomarkerMeasurementId] = None
    biomarker_type: Optional[str] = None
    measured_entity: Optional[Union[dict, OntologyTerm]] = None
    participant: Optional[Union[str, ParticipantId]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiomarkerMeasurementId):
            self.id = BiomarkerMeasurementId(self.id)

        if self.biomarker_type is not None and not isinstance(self.biomarker_type, str):
            self.biomarker_type = str(self.biomarker_type)

        if self.measured_entity is not None and not isinstance(self.measured_entity, OntologyTerm):
            self.measured_entity = OntologyTerm(**as_dict(self.measured_entity))

        if self.participant is not None and not isinstance(self.participant, ParticipantId):
            self.participant = ParticipantId(self.participant)

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeMeasurement(Measurement):
    """
    A measurement of a phenotypic trait or functional assay
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["PhenotypeMeasurement"]
    class_class_curie: ClassVar[str] = "owg:PhenotypeMeasurement"
    class_name: ClassVar[str] = "PhenotypeMeasurement"
    class_model_uri: ClassVar[URIRef] = OWG.PhenotypeMeasurement

    id: Union[str, PhenotypeMeasurementId] = None
    phenotype: Optional[Union[dict, OntologyTerm]] = None
    measured_entity: Optional[Union[dict, OntologyTerm]] = None
    participant: Optional[Union[str, ParticipantId]] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeMeasurementId):
            self.id = PhenotypeMeasurementId(self.id)

        if self.phenotype is not None and not isinstance(self.phenotype, OntologyTerm):
            self.phenotype = OntologyTerm(**as_dict(self.phenotype))

        if self.measured_entity is not None and not isinstance(self.measured_entity, OntologyTerm):
            self.measured_entity = OntologyTerm(**as_dict(self.measured_entity))

        if self.participant is not None and not isinstance(self.participant, ParticipantId):
            self.participant = ParticipantId(self.participant)

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AggregatedMeasurement(Measurement):
    """
    An aggregated or summary measurement across a cohort or population
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["AggregatedMeasurement"]
    class_class_curie: ClassVar[str] = "owg:AggregatedMeasurement"
    class_name: ClassVar[str] = "AggregatedMeasurement"
    class_model_uri: ClassVar[URIRef] = OWG.AggregatedMeasurement

    id: Union[str, AggregatedMeasurementId] = None
    measured_entity: Optional[Union[dict, OntologyTerm]] = None
    cohort: Optional[Union[str, CohortId]] = None
    summary_statistic: Optional[Union[str, "SummaryStatisticEnum"]] = None
    sample_size: Optional[int] = None
    stratification: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AggregatedMeasurementId):
            self.id = AggregatedMeasurementId(self.id)

        if self.measured_entity is not None and not isinstance(self.measured_entity, OntologyTerm):
            self.measured_entity = OntologyTerm(**as_dict(self.measured_entity))

        if self.cohort is not None and not isinstance(self.cohort, CohortId):
            self.cohort = CohortId(self.cohort)

        if self.summary_statistic is not None and not isinstance(self.summary_statistic, SummaryStatisticEnum):
            self.summary_statistic = SummaryStatisticEnum(self.summary_statistic)

        if self.sample_size is not None and not isinstance(self.sample_size, int):
            self.sample_size = int(self.sample_size)

        if self.stratification is not None and not isinstance(self.stratification, str):
            self.stratification = str(self.stratification)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneExpressionMeasurement(Measurement):
    """
    A measurement of gene expression (mRNA level) in a specific biological context. Captures the target gene,
    tissue/cell type context, and assay methodology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["GeneExpressionMeasurement"]
    class_class_curie: ClassVar[str] = "owg:GeneExpressionMeasurement"
    class_name: ClassVar[str] = "GeneExpressionMeasurement"
    class_model_uri: ClassVar[URIRef] = OWG.GeneExpressionMeasurement

    id: Union[str, GeneExpressionMeasurementId] = None
    target_gene: Optional[Union[dict, "Gene"]] = None
    tissue_context: Optional[Union[dict, Tissue]] = None
    cell_type_context: Optional[Union[dict, "CellType"]] = None
    assay_method: Optional[Union[str, "ExpressionAssayMethodEnum"]] = None
    normalization_reference: Optional[str] = None
    participant: Optional[Union[str, ParticipantId]] = None
    measurement_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneExpressionMeasurementId):
            self.id = GeneExpressionMeasurementId(self.id)

        if self.target_gene is not None and not isinstance(self.target_gene, Gene):
            self.target_gene = Gene(**as_dict(self.target_gene))

        if self.tissue_context is not None and not isinstance(self.tissue_context, Tissue):
            self.tissue_context = Tissue(**as_dict(self.tissue_context))

        if self.cell_type_context is not None and not isinstance(self.cell_type_context, CellType):
            self.cell_type_context = CellType(**as_dict(self.cell_type_context))

        if self.assay_method is not None and not isinstance(self.assay_method, ExpressionAssayMethodEnum):
            self.assay_method = ExpressionAssayMethodEnum(self.assay_method)

        if self.normalization_reference is not None and not isinstance(self.normalization_reference, str):
            self.normalization_reference = str(self.normalization_reference)

        if self.participant is not None and not isinstance(self.participant, ParticipantId):
            self.participant = ParticipantId(self.participant)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinExpressionMeasurement(Measurement):
    """
    A measurement of protein expression or post-translational modification (e.g., phosphorylation) in a specific
    biological context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["ProteinExpressionMeasurement"]
    class_class_curie: ClassVar[str] = "owg:ProteinExpressionMeasurement"
    class_name: ClassVar[str] = "ProteinExpressionMeasurement"
    class_model_uri: ClassVar[URIRef] = OWG.ProteinExpressionMeasurement

    id: Union[str, ProteinExpressionMeasurementId] = None
    target_protein: Optional[Union[dict, "Protein"]] = None
    phosphorylation_site: Optional[str] = None
    tissue_context: Optional[Union[dict, Tissue]] = None
    cell_type_context: Optional[Union[dict, "CellType"]] = None
    assay_method: Optional[Union[str, "ExpressionAssayMethodEnum"]] = None
    normalization_reference: Optional[str] = None
    participant: Optional[Union[str, ParticipantId]] = None
    measurement_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinExpressionMeasurementId):
            self.id = ProteinExpressionMeasurementId(self.id)

        if self.target_protein is not None and not isinstance(self.target_protein, Protein):
            self.target_protein = Protein(**as_dict(self.target_protein))

        if self.phosphorylation_site is not None and not isinstance(self.phosphorylation_site, str):
            self.phosphorylation_site = str(self.phosphorylation_site)

        if self.tissue_context is not None and not isinstance(self.tissue_context, Tissue):
            self.tissue_context = Tissue(**as_dict(self.tissue_context))

        if self.cell_type_context is not None and not isinstance(self.cell_type_context, CellType):
            self.cell_type_context = CellType(**as_dict(self.cell_type_context))

        if self.assay_method is not None and not isinstance(self.assay_method, ExpressionAssayMethodEnum):
            self.assay_method = ExpressionAssayMethodEnum(self.assay_method)

        if self.normalization_reference is not None and not isinstance(self.normalization_reference, str):
            self.normalization_reference = str(self.normalization_reference)

        if self.participant is not None and not isinstance(self.participant, ParticipantId):
            self.participant = ParticipantId(self.participant)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Gene(BiologicalEntity):
    """
    A gene or genetic element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Gene"]
    class_class_curie: ClassVar[str] = "owg:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = OWG.Gene

    id: Union[str, GeneId] = None
    ncbigene_id: Optional[str] = None
    symbol: Optional[str] = None
    in_taxon: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        if self.ncbigene_id is not None and not isinstance(self.ncbigene_id, str):
            self.ncbigene_id = str(self.ncbigene_id)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.in_taxon is not None and not isinstance(self.in_taxon, str):
            self.in_taxon = str(self.in_taxon)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Protein(BiologicalEntity):
    """
    A protein or polypeptide
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Protein"]
    class_class_curie: ClassVar[str] = "owg:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = OWG.Protein

    id: Union[str, ProteinId] = None
    encoded_by_gene: Optional[Union[dict, Gene]] = None
    symbol: Optional[str] = None
    in_taxon: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)

        if self.encoded_by_gene is not None and not isinstance(self.encoded_by_gene, Gene):
            self.encoded_by_gene = Gene(**as_dict(self.encoded_by_gene))

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.in_taxon is not None and not isinstance(self.in_taxon, str):
            self.in_taxon = str(self.in_taxon)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellType(BiologicalEntity):
    """
    A type of cell
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CL["0000000"]
    class_class_curie: ClassVar[str] = "CL:0000000"
    class_name: ClassVar[str] = "CellType"
    class_model_uri: ClassVar[URIRef] = OWG.CellType

    id: Union[str, CellTypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellTypeId):
            self.id = CellTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnatomicalEntity(BiologicalEntity):
    """
    An anatomical structure or system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UBERON["0001062"]
    class_class_curie: ClassVar[str] = "UBERON:0001062"
    class_name: ClassVar[str] = "AnatomicalEntity"
    class_model_uri: ClassVar[URIRef] = OWG.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organism(BiologicalEntity):
    """
    An individual organism
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Organism"]
    class_class_curie: ClassVar[str] = "owg:Organism"
    class_name: ClassVar[str] = "Organism"
    class_model_uri: ClassVar[URIRef] = OWG.Organism

    id: Union[str, OrganismId] = None
    species: Optional[str] = None
    taxon_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismId):
            self.id = OrganismId(self.id)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.taxon_id is not None and not isinstance(self.taxon_id, str):
            self.taxon_id = str(self.taxon_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureToPhenotypeAssociation(Association):
    """
    An association between an exposure and a phenotype
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["ExposureToPhenotypeAssociation"]
    class_class_curie: ClassVar[str] = "owg:ExposureToPhenotypeAssociation"
    class_name: ClassVar[str] = "ExposureToPhenotypeAssociation"
    class_model_uri: ClassVar[URIRef] = OWG.ExposureToPhenotypeAssociation

    id: Union[str, ExposureToPhenotypeAssociationId] = None
    exposure: Optional[Union[str, ExposureEventId]] = None
    phenotype: Optional[Union[dict, OntologyTerm]] = None
    association_type: Optional[str] = None
    evidence: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureToPhenotypeAssociationId):
            self.id = ExposureToPhenotypeAssociationId(self.id)

        if self.exposure is not None and not isinstance(self.exposure, ExposureEventId):
            self.exposure = ExposureEventId(self.exposure)

        if self.phenotype is not None and not isinstance(self.phenotype, OntologyTerm):
            self.phenotype = OntologyTerm(**as_dict(self.phenotype))

        if self.association_type is not None and not isinstance(self.association_type, str):
            self.association_type = str(self.association_type)

        if self.evidence is not None and not isinstance(self.evidence, str):
            self.evidence = str(self.evidence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalToGeneAssociation(Association):
    """
    An association between a chemical and a gene
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["ChemicalToGeneAssociation"]
    class_class_curie: ClassVar[str] = "owg:ChemicalToGeneAssociation"
    class_name: ClassVar[str] = "ChemicalToGeneAssociation"
    class_model_uri: ClassVar[URIRef] = OWG.ChemicalToGeneAssociation

    id: Union[str, ChemicalToGeneAssociationId] = None
    chemical: Optional[Union[str, ChemicalEntityId]] = None
    gene: Optional[Union[str, GeneId]] = None
    interaction_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalToGeneAssociationId):
            self.id = ChemicalToGeneAssociationId(self.id)

        if self.chemical is not None and not isinstance(self.chemical, ChemicalEntityId):
            self.chemical = ChemicalEntityId(self.chemical)

        if self.gene is not None and not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        if self.interaction_type is not None and not isinstance(self.interaction_type, str):
            self.interaction_type = str(self.interaction_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneToDiseaseAssociation(Association):
    """
    An association between a gene and a disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["GeneToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "owg:GeneToDiseaseAssociation"
    class_name: ClassVar[str] = "GeneToDiseaseAssociation"
    class_model_uri: ClassVar[URIRef] = OWG.GeneToDiseaseAssociation

    id: Union[str, GeneToDiseaseAssociationId] = None
    gene: Optional[Union[str, GeneId]] = None
    disease: Optional[Union[str, DiseaseId]] = None
    association_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneToDiseaseAssociationId):
            self.id = GeneToDiseaseAssociationId(self.id)

        if self.gene is not None and not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        if self.disease is not None and not isinstance(self.disease, DiseaseId):
            self.disease = DiseaseId(self.disease)

        if self.association_type is not None and not isinstance(self.association_type, str):
            self.association_type = str(self.association_type)

        super().__post_init__(**kwargs)


# Enumerations
class ExposureRouteEnum(EnumDefinitionImpl):
    """
    Routes of exposure to chemicals or environmental factors
    """
    Oral = PermissibleValue(
        text="Oral",
        description="Oral ingestion",
        meaning=ECTO["0000895"])
    Dermal = PermissibleValue(
        text="Dermal",
        description="Dermal contact",
        meaning=ECTO["0000896"])
    Inhalation = PermissibleValue(
        text="Inhalation",
        description="Inhalation",
        meaning=ECTO["0000897"])
    Injection = PermissibleValue(
        text="Injection",
        description="Injection")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown route")

    _defn = EnumDefinition(
        name="ExposureRouteEnum",
        description="Routes of exposure to chemicals or environmental factors",
    )

class ExposureMediumEnum(EnumDefinitionImpl):
    """
    Medium through which exposure occurs
    """
    Air = PermissibleValue(
        text="Air",
        description="Air",
        meaning=ENVO["00002005"])
    Water = PermissibleValue(
        text="Water",
        description="Water",
        meaning=ENVO["00002006"])
    Food = PermissibleValue(
        text="Food",
        description="Food",
        meaning=FOODON["00002403"])
    Soil = PermissibleValue(
        text="Soil",
        description="Soil",
        meaning=ENVO["00001998"])
    Dust = PermissibleValue(
        text="Dust",
        description="Dust")
    ConsumerProduct = PermissibleValue(
        text="ConsumerProduct",
        description="Consumer product")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown medium")

    _defn = EnumDefinition(
        name="ExposureMediumEnum",
        description="Medium through which exposure occurs",
    )

class ExpressionAssayMethodEnum(EnumDefinitionImpl):
    """
    Methods used to measure gene or protein expression. Includes transcriptomic, proteomic, and imaging-based
    approaches.
    """
    qRT_PCR = PermissibleValue(
        text="qRT_PCR",
        description="Quantitative real-time polymerase chain reaction",
        meaning=OBI["0000893"])
    RNA_Seq = PermissibleValue(
        text="RNA_Seq",
        description="RNA sequencing (bulk)",
        meaning=OBI["0001271"])
    Single_Cell_RNA_Seq = PermissibleValue(
        text="Single_Cell_RNA_Seq",
        description="Single-cell RNA sequencing",
        meaning=OBI["0002631"])
    Microarray = PermissibleValue(
        text="Microarray",
        description="Gene expression microarray",
        meaning=OBI["0000424"])
    NanoString = PermissibleValue(
        text="NanoString",
        description="NanoString nCounter gene expression assay",
        meaning=OBI["0002142"])
    Northern_Blot = PermissibleValue(
        text="Northern_Blot",
        description="Northern blot for RNA detection",
        meaning=OBI["0000822"])
    In_Situ_Hybridization = PermissibleValue(
        text="In_Situ_Hybridization",
        description="In situ hybridization (ISH, FISH, RNAscope)",
        meaning=OBI["0001686"])
    Western_Blot = PermissibleValue(
        text="Western_Blot",
        description="Western blot (immunoblot) for protein detection",
        meaning=OBI["0000714"])
    ELISA = PermissibleValue(
        text="ELISA",
        description="Enzyme-linked immunosorbent assay",
        meaning=OBI["0000661"])
    Immunohistochemistry = PermissibleValue(
        text="Immunohistochemistry",
        description="Immunohistochemistry on tissue sections",
        meaning=OBI["0001986"])
    Immunofluorescence = PermissibleValue(
        text="Immunofluorescence",
        description="Immunofluorescence staining",
        meaning=OBI["0001501"])
    Flow_Cytometry = PermissibleValue(
        text="Flow_Cytometry",
        description="Flow cytometry for protein expression",
        meaning=OBI["0000916"])
    Mass_Spectrometry = PermissibleValue(
        text="Mass_Spectrometry",
        description="Mass spectrometry-based proteomics",
        meaning=OBI["0000470"])
    Immunoprecipitation = PermissibleValue(
        text="Immunoprecipitation",
        description="Immunoprecipitation followed by detection",
        meaning=OBI["0000928"])
    Luminex = PermissibleValue(
        text="Luminex",
        description="Luminex multiplex bead-based assay",
        meaning=OBI["0001632"])
    Other = PermissibleValue(
        text="Other",
        description="Other assay method not listed")

    _defn = EnumDefinition(
        name="ExpressionAssayMethodEnum",
        description="""Methods used to measure gene or protein expression. Includes transcriptomic, proteomic, and imaging-based approaches.""",
    )

class BiologicalOrganizationLevelEnum(EnumDefinitionImpl):
    """
    Levels of biological organization
    """
    Molecular = PermissibleValue(
        text="Molecular",
        description="Molecular level",
        meaning=EFO["0001432"])
    Cellular = PermissibleValue(
        text="Cellular",
        description="Cellular level",
        meaning=CL["0000000"])
    Tissue = PermissibleValue(
        text="Tissue",
        description="Tissue level",
        meaning=UBERON["0000479"])
    Organ = PermissibleValue(
        text="Organ",
        description="Organ level",
        meaning=UBERON["0000062"])
    Organism = PermissibleValue(
        text="Organism",
        description="Organism level",
        meaning=UBERON["0000468"])
    Population = PermissibleValue(
        text="Population",
        description="Population level")

    _defn = EnumDefinition(
        name="BiologicalOrganizationLevelEnum",
        description="Levels of biological organization",
    )

class StudyTypeEnum(EnumDefinitionImpl):
    """
    Types of research studies
    """
    Cohort = PermissibleValue(
        text="Cohort",
        description="Cohort study",
        meaning=EFO["0001444"])
    CrossSectional = PermissibleValue(
        text="CrossSectional",
        description="Cross-sectional study",
        meaning=EFO["0001745"])
    CaseControl = PermissibleValue(
        text="CaseControl",
        description="Case-control study",
        meaning=EFO["0001427"])
    RandomizedControlledTrial = PermissibleValue(
        text="RandomizedControlledTrial",
        description="Randomized controlled trial",
        meaning=EFO["0001427"])
    Survey = PermissibleValue(
        text="Survey",
        description="Survey")
    Gwas = PermissibleValue(
        text="Gwas",
        description="Genome-wide association study",
        meaning=EFO["0000508"])
    Other = PermissibleValue(
        text="Other",
        description="Other study type")

    _defn = EnumDefinition(
        name="StudyTypeEnum",
        description="Types of research studies",
    )

class SexEnum(EnumDefinitionImpl):
    """
    Biological sex
    """
    Male = PermissibleValue(
        text="Male",
        description="Male",
        meaning=PATO["0000384"])
    Female = PermissibleValue(
        text="Female",
        description="Female",
        meaning=PATO["0000383"])
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown")

    _defn = EnumDefinition(
        name="SexEnum",
        description="Biological sex",
    )

class SampleTypeEnum(EnumDefinitionImpl):
    """
    Types of biological and environmental samples
    """
    Blood = PermissibleValue(
        text="Blood",
        description="Blood sample")
    Urine = PermissibleValue(
        text="Urine",
        description="Urine sample")
    Serum = PermissibleValue(
        text="Serum",
        description="Serum sample")
    Plasma = PermissibleValue(
        text="Plasma",
        description="Plasma sample")
    Tissue = PermissibleValue(
        text="Tissue",
        description="Tissue sample")
    Saliva = PermissibleValue(
        text="Saliva",
        description="Saliva sample")
    Hair = PermissibleValue(
        text="Hair",
        description="Hair sample")
    Nail = PermissibleValue(
        text="Nail",
        description="Nail sample")
    Air = PermissibleValue(
        text="Air",
        description="Air sample (environmental)")
    Water = PermissibleValue(
        text="Water",
        description="Water sample (environmental)")
    Soil = PermissibleValue(
        text="Soil",
        description="Soil sample (environmental)")
    Other = PermissibleValue(
        text="Other",
        description="Other sample type")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
        description="Types of biological and environmental samples",
    )

class SummaryStatisticEnum(EnumDefinitionImpl):
    """
    Types of summary statistics
    """
    Mean = PermissibleValue(
        text="Mean",
        description="Arithmetic mean")
    Median = PermissibleValue(
        text="Median",
        description="Median")
    Mode = PermissibleValue(
        text="Mode",
        description="Mode")
    Percentile = PermissibleValue(
        text="Percentile",
        description="Percentile")
    StandardDeviation = PermissibleValue(
        text="StandardDeviation",
        description="Standard deviation")
    Variance = PermissibleValue(
        text="Variance",
        description="Variance")
    Range = PermissibleValue(
        text="Range",
        description="Range")
    InterquartileRange = PermissibleValue(
        text="InterquartileRange",
        description="Interquartile range")

    _defn = EnumDefinition(
        name="SummaryStatisticEnum",
        description="Types of summary statistics",
    )

class MeasurementTypeEnum(EnumDefinitionImpl):
    """
    Types of measurements and observations for outcomes research, with emphasis on respiratory health and
    environmental toxicant effects.
    """
    FEV1 = PermissibleValue(
        text="FEV1",
        description="Forced expiratory volume in 1 second",
        meaning=NCIT["C38083"])
    FVC = PermissibleValue(
        text="FVC",
        description="Forced vital capacity",
        meaning=NCIT["C38082"])
    FEV1_FVC_Ratio = PermissibleValue(
        text="FEV1_FVC_Ratio",
        description="Ratio of FEV1 to FVC (Tiffeneau-Pinelli index)",
        meaning=NCIT["C120835"])
    FEF25_75 = PermissibleValue(
        text="FEF25_75",
        description="Forced expiratory flow at 25-75% of FVC",
        meaning=NCIT["C38085"])
    PeakExpiratoryFlow = PermissibleValue(
        text="PeakExpiratoryFlow",
        description="Peak expiratory flow rate",
        meaning=NCIT["C38086"])
    DLCO = PermissibleValue(
        text="DLCO",
        description="Diffusing capacity of the lung for carbon monoxide",
        meaning=NCIT["C38087"])
    FeNO = PermissibleValue(
        text="FeNO",
        description="Fractional exhaled nitric oxide (airway inflammation marker)",
        meaning=NCIT["C124353"])
    BronchodilatorResponse = PermissibleValue(
        text="BronchodilatorResponse",
        description="Change in lung function after bronchodilator administration")
    LungFunctionDeclineRate = PermissibleValue(
        text="LungFunctionDeclineRate",
        description="Rate of decline in lung function over time")
    CiliaryBeatFrequency = PermissibleValue(
        text="CiliaryBeatFrequency",
        description="Frequency of ciliary beating in Hz",
        meaning=GO["0003341"])
    CiliaryActiveAreaPercentage = PermissibleValue(
        text="CiliaryActiveAreaPercentage",
        description="Percentage of epithelial surface with active cilia")
    CiliaPerCell = PermissibleValue(
        text="CiliaPerCell",
        description="Number of cilia per epithelial cell")
    CiliaLength = PermissibleValue(
        text="CiliaLength",
        description="Length of cilia in micrometers")
    PercentageCiliatedCells = PermissibleValue(
        text="PercentageCiliatedCells",
        description="Percentage of cells that are ciliated")
    ASLHeight = PermissibleValue(
        text="ASLHeight",
        description="Airway surface liquid height in micrometers")
    PericiliaryLayerDepth = PermissibleValue(
        text="PericiliaryLayerDepth",
        description="Depth of periciliary liquid layer (reduced in disease)")
    MucusLayerThickness = PermissibleValue(
        text="MucusLayerThickness",
        description="Thickness of the mucus gel layer")
    MucociliaryTransportRate = PermissibleValue(
        text="MucociliaryTransportRate",
        description="Rate of mucociliary transport (mm/min)",
        meaning=GO["0120197"])
    MucociliaryDirectionality = PermissibleValue(
        text="MucociliaryDirectionality",
        description="Directionality and coordination of mucociliary transport")
    ParticleClearanceRate = PermissibleValue(
        text="ParticleClearanceRate",
        description="Rate of particle clearance from airways")
    GobletCellCount = PermissibleValue(
        text="GobletCellCount",
        description="Number or percentage of goblet cells",
        meaning=CL["0000160"])
    GobletToCiliatedRatio = PermissibleValue(
        text="GobletToCiliatedRatio",
        description="Ratio of goblet cells to ciliated cells")
    MucinProteinConcentration = PermissibleValue(
        text="MucinProteinConcentration",
        description="Concentration of secreted mucin protein")
    MucusViscosity = PermissibleValue(
        text="MucusViscosity",
        description="Viscosity of airway mucus")
    CFTRChlorideSecretion = PermissibleValue(
        text="CFTRChlorideSecretion",
        description="CFTR-mediated chloride secretory current")
    InhibitorSensitiveCurrent = PermissibleValue(
        text="InhibitorSensitiveCurrent",
        description="Current sensitive to CFTR inhibitors (e.g., CFTRinh-172)")
    SweatChlorideConcentration = PermissibleValue(
        text="SweatChlorideConcentration",
        description="Chloride concentration in sweat (CF diagnostic)")
    ReactiveOxygenSpecies = PermissibleValue(
        text="ReactiveOxygenSpecies",
        description="Reactive oxygen species (ROS) level",
        meaning=CHEBI["26523"])
    LipidPeroxidation = PermissibleValue(
        text="LipidPeroxidation",
        description="Lipid peroxidation markers (MDA, 8-isoprostane)")
    ProteinCarbonyls = PermissibleValue(
        text="ProteinCarbonyls",
        description="Protein carbonyl content (protein oxidation marker)")
    DNA_8OHdG = PermissibleValue(
        text="DNA_8OHdG",
        description="8-hydroxydeoxyguanosine (DNA oxidative damage marker)")
    GlutathioneRatio = PermissibleValue(
        text="GlutathioneRatio",
        description="GSH/GSSG ratio (antioxidant capacity)")
    SuperoxideDismutaseActivity = PermissibleValue(
        text="SuperoxideDismutaseActivity",
        description="Superoxide dismutase (SOD) enzyme activity")
    CatalaseActivity = PermissibleValue(
        text="CatalaseActivity",
        description="Catalase enzyme activity")
    GlutathionePeroxidaseActivity = PermissibleValue(
        text="GlutathionePeroxidaseActivity",
        description="Glutathione peroxidase (GPx) activity")
    TotalAntioxidantCapacity = PermissibleValue(
        text="TotalAntioxidantCapacity",
        description="Total antioxidant capacity of sample")
    TEER = PermissibleValue(
        text="TEER",
        description="Transepithelial electrical resistance")
    ParacellularPermeability = PermissibleValue(
        text="ParacellularPermeability",
        description="Paracellular permeability coefficient")
    IL6Level = PermissibleValue(
        text="IL6Level",
        description="Interleukin-6 concentration",
        meaning=NCIT["C20487"])
    IL8Level = PermissibleValue(
        text="IL8Level",
        description="Interleukin-8 (CXCL8) concentration",
        meaning=NCIT["C20506"])
    IL13Level = PermissibleValue(
        text="IL13Level",
        description="Interleukin-13 concentration",
        meaning=NCIT["C20497"])
    TNFAlphaLevel = PermissibleValue(
        text="TNFAlphaLevel",
        description="Tumor necrosis factor alpha concentration",
        meaning=NCIT["C20535"])
    NeutrophilPercentage = PermissibleValue(
        text="NeutrophilPercentage",
        description="Percentage of neutrophils in BALF or sputum")
    EosinophilPercentage = PermissibleValue(
        text="EosinophilPercentage",
        description="Percentage of eosinophils in BALF or sputum")
    MacrophagePercentage = PermissibleValue(
        text="MacrophagePercentage",
        description="Percentage of macrophages in BALF or sputum")
    TotalInflammatoryCell = PermissibleValue(
        text="TotalInflammatoryCell",
        description="Total inflammatory cell count")
    LDHRelease = PermissibleValue(
        text="LDHRelease",
        description="Lactate dehydrogenase release (cell damage marker)")
    CellViability = PermissibleValue(
        text="CellViability",
        description="Cell viability percentage")
    MTTReduction = PermissibleValue(
        text="MTTReduction",
        description="MTT assay result (metabolic activity)")
    ApoptosisRate = PermissibleValue(
        text="ApoptosisRate",
        description="Rate of apoptotic cell death")
    GeneExpression = PermissibleValue(
        text="GeneExpression",
        description="""Gene expression level (mRNA). Use with GeneExpressionMeasurement class to specify target_gene, tissue_context, and assay_method.""")
    ProteinExpression = PermissibleValue(
        text="ProteinExpression",
        description="""Protein expression level. Use with ProteinExpressionMeasurement class to specify target_protein, tissue_context, and assay_method.""")
    ProteinPhosphorylation = PermissibleValue(
        text="ProteinPhosphorylation",
        description="""Protein phosphorylation level. Use with ProteinExpressionMeasurement class and specify phosphorylation_site (e.g., Y1068 for EGFR).""")
    ProteinLocalization = PermissibleValue(
        text="ProteinLocalization",
        description="""Protein subcellular localization (membrane, cytoplasm, nucleus). Use with ProteinExpressionMeasurement class.""")
    ExpressionRatio = PermissibleValue(
        text="ExpressionRatio",
        description="""Ratio of expression between two genes or proteins (e.g., MUC5AC/MUC5B ratio). Specify both targets in description.""")
    PercentagePositiveCells = PermissibleValue(
        text="PercentagePositiveCells",
        description="Percentage of cells positive for a marker (IHC, flow cytometry)")
    BloodLeadLevel = PermissibleValue(
        text="BloodLeadLevel",
        description="Blood lead concentration",
        meaning=HHEAR["00000001"])
    BloodCadmiumLevel = PermissibleValue(
        text="BloodCadmiumLevel",
        description="Blood cadmium concentration")
    BloodMercuryLevel = PermissibleValue(
        text="BloodMercuryLevel",
        description="Blood mercury concentration")
    UrinaryArsenicLevel = PermissibleValue(
        text="UrinaryArsenicLevel",
        description="Urinary arsenic concentration")
    UrinaryCotinineLevel = PermissibleValue(
        text="UrinaryCotinineLevel",
        description="Urinary cotinine (tobacco exposure biomarker)")
    UrinaryBPALevel = PermissibleValue(
        text="UrinaryBPALevel",
        description="Urinary bisphenol A concentration")
    UrinaryPhthalateMetabolites = PermissibleValue(
        text="UrinaryPhthalateMetabolites",
        description="Urinary phthalate metabolite concentrations")
    PM2_5Exposure = PermissibleValue(
        text="PM2_5Exposure",
        description="Fine particulate matter (PM2.5) exposure level")
    OzoneExposure = PermissibleValue(
        text="OzoneExposure",
        description="Ozone exposure concentration")
    NO2Exposure = PermissibleValue(
        text="NO2Exposure",
        description="Nitrogen dioxide exposure concentration")
    PolycyclicAromaticHydrocarbons = PermissibleValue(
        text="PolycyclicAromaticHydrocarbons",
        description="PAH metabolite levels")
    BodyMassIndex = PermissibleValue(
        text="BodyMassIndex",
        description="Body mass index (BMI)",
        meaning=NCIT["C16358"])
    BodyWeight = PermissibleValue(
        text="BodyWeight",
        description="Body weight measurement",
        meaning=NCIT["C81328"])
    Height = PermissibleValue(
        text="Height",
        description="Height measurement",
        meaning=NCIT["C25347"])
    AlphaDiversity = PermissibleValue(
        text="AlphaDiversity",
        description="Microbiome alpha diversity metric")
    BetaDiversity = PermissibleValue(
        text="BetaDiversity",
        description="Microbiome beta diversity metric")
    BacterialLoad = PermissibleValue(
        text="BacterialLoad",
        description="Total bacterial load (CFU or 16S copies)")
    Other = PermissibleValue(
        text="Other",
        description="Other measurement type not listed")

    _defn = EnumDefinition(
        name="MeasurementTypeEnum",
        description="""Types of measurements and observations for outcomes research, with emphasis on respiratory health and environmental toxicant effects.""",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=OWG.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=OWG.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=OWG.description, domain=None, range=Optional[str])

slots.category = Slot(uri=OWG.category, name="category", curie=OWG.curie('category'),
                   model_uri=OWG.category, domain=None, range=Optional[Union[str, list[str]]])

slots.xref = Slot(uri=OWG.xref, name="xref", curie=OWG.curie('xref'),
                   model_uri=OWG.xref, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.unit_label = Slot(uri=OWG.unit_label, name="unit_label", curie=OWG.curie('unit_label'),
                   model_uri=OWG.unit_label, domain=None, range=Optional[str])

slots.chebi_id = Slot(uri=OWG.chebi_id, name="chebi_id", curie=OWG.curie('chebi_id'),
                   model_uri=OWG.chebi_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^CHEBI:\d+$'))

slots.dtxsid = Slot(uri=OWG.dtxsid, name="dtxsid", curie=OWG.curie('dtxsid'),
                   model_uri=OWG.dtxsid, domain=None, range=Optional[str],
                   pattern=re.compile(r'^DTXSID\d{7,9}$'))

slots.chembl_id = Slot(uri=OWG.chembl_id, name="chembl_id", curie=OWG.curie('chembl_id'),
                   model_uri=OWG.chembl_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^CHEMBL\d+$'))

slots.pubchem_cid = Slot(uri=OWG.pubchem_cid, name="pubchem_cid", curie=OWG.curie('pubchem_cid'),
                   model_uri=OWG.pubchem_cid, domain=None, range=Optional[int])

slots.cas_number = Slot(uri=OWG.cas_number, name="cas_number", curie=OWG.curie('cas_number'),
                   model_uri=OWG.cas_number, domain=None, range=Optional[str])

slots.inchi = Slot(uri=OWG.inchi, name="inchi", curie=OWG.curie('inchi'),
                   model_uri=OWG.inchi, domain=None, range=Optional[str])

slots.smiles = Slot(uri=OWG.smiles, name="smiles", curie=OWG.curie('smiles'),
                   model_uri=OWG.smiles, domain=None, range=Optional[str])

slots.molecular_formula = Slot(uri=OWG.molecular_formula, name="molecular_formula", curie=OWG.curie('molecular_formula'),
                   model_uri=OWG.molecular_formula, domain=None, range=Optional[str])

slots.exposed_to_chemical = Slot(uri=CHEBI['24431'], name="exposed_to_chemical", curie=CHEBI.curie('24431'),
                   model_uri=OWG.exposed_to_chemical, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.exposure_route = Slot(uri=OWG.exposure_route, name="exposure_route", curie=OWG.curie('exposure_route'),
                   model_uri=OWG.exposure_route, domain=None, range=Optional[Union[str, "ExposureRouteEnum"]])

slots.exposure_duration = Slot(uri=OWG.exposure_duration, name="exposure_duration", curie=OWG.curie('exposure_duration'),
                   model_uri=OWG.exposure_duration, domain=None, range=Optional[str])

slots.exposure_concentration = Slot(uri=OWG.exposure_concentration, name="exposure_concentration", curie=OWG.curie('exposure_concentration'),
                   model_uri=OWG.exposure_concentration, domain=None, range=Optional[float])

slots.exposure_medium = Slot(uri=OWG.exposure_medium, name="exposure_medium", curie=OWG.curie('exposure_medium'),
                   model_uri=OWG.exposure_medium, domain=None, range=Optional[Union[str, "ExposureMediumEnum"]])

slots.food_item = Slot(uri=OWG.food_item, name="food_item", curie=OWG.curie('food_item'),
                   model_uri=OWG.food_item, domain=None, range=Optional[str])

slots.serving_size = Slot(uri=OWG.serving_size, name="serving_size", curie=OWG.curie('serving_size'),
                   model_uri=OWG.serving_size, domain=None, range=Optional[str])

slots.environmental_context = Slot(uri=OWG.environmental_context, name="environmental_context", curie=OWG.curie('environmental_context'),
                   model_uri=OWG.environmental_context, domain=None, range=Optional[str])

slots.occupation = Slot(uri=OWG.occupation, name="occupation", curie=OWG.curie('occupation'),
                   model_uri=OWG.occupation, domain=None, range=Optional[str])

slots.workplace = Slot(uri=OWG.workplace, name="workplace", curie=OWG.curie('workplace'),
                   model_uri=OWG.workplace, domain=None, range=Optional[str])

slots.severity = Slot(uri=OWG.severity, name="severity", curie=OWG.curie('severity'),
                   model_uri=OWG.severity, domain=None, range=Optional[str])

slots.onset_age = Slot(uri=OWG.onset_age, name="onset_age", curie=OWG.curie('onset_age'),
                   model_uri=OWG.onset_age, domain=None, range=Optional[str])

slots.disease_category = Slot(uri=OWG.disease_category, name="disease_category", curie=OWG.curie('disease_category'),
                   model_uri=OWG.disease_category, domain=None, range=Optional[str])

slots.affected_anatomy = Slot(uri=OWG.affected_anatomy, name="affected_anatomy", curie=OWG.curie('affected_anatomy'),
                   model_uri=OWG.affected_anatomy, domain=None, range=Optional[Union[str, AnatomicalEntityId]])

slots.outcome_level = Slot(uri=OWG.outcome_level, name="outcome_level", curie=OWG.curie('outcome_level'),
                   model_uri=OWG.outcome_level, domain=None, range=Optional[Union[str, "BiologicalOrganizationLevelEnum"]])

slots.aopwiki_id = Slot(uri=OWG.aopwiki_id, name="aopwiki_id", curie=OWG.curie('aopwiki_id'),
                   model_uri=OWG.aopwiki_id, domain=None, range=Optional[str])

slots.molecular_initiating_event = Slot(uri=OWG.molecular_initiating_event, name="molecular_initiating_event", curie=OWG.curie('molecular_initiating_event'),
                   model_uri=OWG.molecular_initiating_event, domain=None, range=Optional[Union[str, MolecularInitiatingEventId]])

slots.key_events = Slot(uri=OWG.key_events, name="key_events", curie=OWG.curie('key_events'),
                   model_uri=OWG.key_events, domain=None, range=Optional[Union[Union[str, KeyEventId], list[Union[str, KeyEventId]]]])

slots.key_event_relationships = Slot(uri=OWG.key_event_relationships, name="key_event_relationships", curie=OWG.curie('key_event_relationships'),
                   model_uri=OWG.key_event_relationships, domain=None, range=Optional[Union[Union[str, KeyEventRelationshipId], list[Union[str, KeyEventRelationshipId]]]])

slots.adverse_outcome = Slot(uri=OWG.adverse_outcome, name="adverse_outcome", curie=OWG.curie('adverse_outcome'),
                   model_uri=OWG.adverse_outcome, domain=None, range=Optional[Union[str, AdverseOutcomeId]])

slots.stressors = Slot(uri=OWG.stressors, name="stressors", curie=OWG.curie('stressors'),
                   model_uri=OWG.stressors, domain=None, range=Optional[Union[Union[str, ChemicalEntityId], list[Union[str, ChemicalEntityId]]]])

slots.biological_process = Slot(uri=OWG.biological_process, name="biological_process", curie=OWG.curie('biological_process'),
                   model_uri=OWG.biological_process, domain=None, range=Optional[str])

slots.biological_object = Slot(uri=OWG.biological_object, name="biological_object", curie=OWG.curie('biological_object'),
                   model_uri=OWG.biological_object, domain=None, range=Optional[str])

slots.biological_action = Slot(uri=OWG.biological_action, name="biological_action", curie=OWG.curie('biological_action'),
                   model_uri=OWG.biological_action, domain=None, range=Optional[str])

slots.occurs_in_cell_type = Slot(uri=CL['0000000'], name="occurs_in_cell_type", curie=CL.curie('0000000'),
                   model_uri=OWG.occurs_in_cell_type, domain=None, range=Optional[Union[str, CellTypeId]])

slots.occurs_in_anatomy = Slot(uri=UBERON['0001062'], name="occurs_in_anatomy", curie=UBERON.curie('0001062'),
                   model_uri=OWG.occurs_in_anatomy, domain=None, range=Optional[Union[str, AnatomicalEntityId]])

slots.level_of_biological_organization = Slot(uri=OWG.level_of_biological_organization, name="level_of_biological_organization", curie=OWG.curie('level_of_biological_organization'),
                   model_uri=OWG.level_of_biological_organization, domain=None, range=Optional[Union[str, "BiologicalOrganizationLevelEnum"]])

slots.upstream_event = Slot(uri=OWG.upstream_event, name="upstream_event", curie=OWG.curie('upstream_event'),
                   model_uri=OWG.upstream_event, domain=None, range=Optional[Union[str, KeyEventId]])

slots.downstream_event = Slot(uri=OWG.downstream_event, name="downstream_event", curie=OWG.curie('downstream_event'),
                   model_uri=OWG.downstream_event, domain=None, range=Optional[Union[str, KeyEventId]])

slots.relationship_type = Slot(uri=OWG.relationship_type, name="relationship_type", curie=OWG.curie('relationship_type'),
                   model_uri=OWG.relationship_type, domain=None, range=Optional[str])

slots.evidence_support = Slot(uri=OWG.evidence_support, name="evidence_support", curie=OWG.curie('evidence_support'),
                   model_uri=OWG.evidence_support, domain=None, range=Optional[str])

slots.study_type = Slot(uri=OWG.study_type, name="study_type", curie=OWG.curie('study_type'),
                   model_uri=OWG.study_type, domain=None, range=Optional[Union[str, "StudyTypeEnum"]])

slots.population = Slot(uri=OWG.population, name="population", curie=OWG.curie('population'),
                   model_uri=OWG.population, domain=None, range=Optional[str])

slots.enrollment_period = Slot(uri=OWG.enrollment_period, name="enrollment_period", curie=OWG.curie('enrollment_period'),
                   model_uri=OWG.enrollment_period, domain=None, range=Optional[str])

slots.geographic_location = Slot(uri=OWG.geographic_location, name="geographic_location", curie=OWG.curie('geographic_location'),
                   model_uri=OWG.geographic_location, domain=None, range=Optional[str])

slots.principal_investigator = Slot(uri=OWG.principal_investigator, name="principal_investigator", curie=OWG.curie('principal_investigator'),
                   model_uri=OWG.principal_investigator, domain=None, range=Optional[str])

slots.publications = Slot(uri=OWG.publications, name="publications", curie=OWG.curie('publications'),
                   model_uri=OWG.publications, domain=None, range=Optional[Union[str, list[str]]])

slots.part_of_study = Slot(uri=OWG.part_of_study, name="part_of_study", curie=OWG.curie('part_of_study'),
                   model_uri=OWG.part_of_study, domain=None, range=Optional[Union[str, StudyId]])

slots.cohort_size = Slot(uri=OWG.cohort_size, name="cohort_size", curie=OWG.curie('cohort_size'),
                   model_uri=OWG.cohort_size, domain=None, range=Optional[int])

slots.inclusion_criteria = Slot(uri=OWG.inclusion_criteria, name="inclusion_criteria", curie=OWG.curie('inclusion_criteria'),
                   model_uri=OWG.inclusion_criteria, domain=None, range=Optional[str])

slots.part_of_cohort = Slot(uri=BIOLINK.member_of, name="part_of_cohort", curie=BIOLINK.curie('member_of'),
                   model_uri=OWG.part_of_cohort, domain=None, range=Optional[Union[str, CohortId]])

slots.participant_id = Slot(uri=OWG.participant_id, name="participant_id", curie=OWG.curie('participant_id'),
                   model_uri=OWG.participant_id, domain=None, range=Optional[str])

slots.age = Slot(uri=OWG.age, name="age", curie=OWG.curie('age'),
                   model_uri=OWG.age, domain=None, range=Optional[int])

slots.sex = Slot(uri=OWG.sex, name="sex", curie=OWG.curie('sex'),
                   model_uri=OWG.sex, domain=None, range=Optional[Union[str, "SexEnum"]])

slots.species = Slot(uri=OWG.species, name="species", curie=OWG.curie('species'),
                   model_uri=OWG.species, domain=None, range=Optional[str])

slots.observation_type = Slot(uri=OWG.observation_type, name="observation_type", curie=OWG.curie('observation_type'),
                   model_uri=OWG.observation_type, domain=None, range=Optional[Union[str, "MeasurementTypeEnum"]])

slots.quantity_measured = Slot(uri=OWG.quantity_measured, name="quantity_measured", curie=OWG.curie('quantity_measured'),
                   model_uri=OWG.quantity_measured, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.range_low = Slot(uri=OWG.range_low, name="range_low", curie=OWG.curie('range_low'),
                   model_uri=OWG.range_low, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.range_high = Slot(uri=OWG.range_high, name="range_high", curie=OWG.curie('range_high'),
                   model_uri=OWG.range_high, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.measured_entity = Slot(uri=OWG.measured_entity, name="measured_entity", curie=OWG.curie('measured_entity'),
                   model_uri=OWG.measured_entity, domain=None, range=Optional[Union[dict, OntologyTerm]])

slots.participant = Slot(uri=OWG.participant, name="participant", curie=OWG.curie('participant'),
                   model_uri=OWG.participant, domain=None, range=Optional[Union[str, ParticipantId]])

slots.measurement_method = Slot(uri=OWG.measurement_method, name="measurement_method", curie=OWG.curie('measurement_method'),
                   model_uri=OWG.measurement_method, domain=None, range=Optional[str])

slots.measurement_date = Slot(uri=OWG.measurement_date, name="measurement_date", curie=OWG.curie('measurement_date'),
                   model_uri=OWG.measurement_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.sample_type = Slot(uri=OWG.sample_type, name="sample_type", curie=OWG.curie('sample_type'),
                   model_uri=OWG.sample_type, domain=None, range=Optional[Union[str, "SampleTypeEnum"]])

slots.biomarker_type = Slot(uri=OWG.biomarker_type, name="biomarker_type", curie=OWG.curie('biomarker_type'),
                   model_uri=OWG.biomarker_type, domain=None, range=Optional[str])

slots.phenotype = Slot(uri=OWG.phenotype, name="phenotype", curie=OWG.curie('phenotype'),
                   model_uri=OWG.phenotype, domain=None, range=Optional[Union[dict, OntologyTerm]])

slots.cohort = Slot(uri=OWG.cohort, name="cohort", curie=OWG.curie('cohort'),
                   model_uri=OWG.cohort, domain=None, range=Optional[Union[str, CohortId]])

slots.summary_statistic = Slot(uri=OWG.summary_statistic, name="summary_statistic", curie=OWG.curie('summary_statistic'),
                   model_uri=OWG.summary_statistic, domain=None, range=Optional[Union[str, "SummaryStatisticEnum"]])

slots.sample_size = Slot(uri=OWG.sample_size, name="sample_size", curie=OWG.curie('sample_size'),
                   model_uri=OWG.sample_size, domain=None, range=Optional[int])

slots.stratification = Slot(uri=OWG.stratification, name="stratification", curie=OWG.curie('stratification'),
                   model_uri=OWG.stratification, domain=None, range=Optional[str])

slots.target_gene = Slot(uri=OWG.target_gene, name="target_gene", curie=OWG.curie('target_gene'),
                   model_uri=OWG.target_gene, domain=None, range=Optional[Union[dict, Gene]])

slots.target_protein = Slot(uri=OWG.target_protein, name="target_protein", curie=OWG.curie('target_protein'),
                   model_uri=OWG.target_protein, domain=None, range=Optional[Union[dict, Protein]])

slots.tissue_context = Slot(uri=OWG.tissue_context, name="tissue_context", curie=OWG.curie('tissue_context'),
                   model_uri=OWG.tissue_context, domain=None, range=Optional[Union[dict, Tissue]])

slots.cell_type_context = Slot(uri=OWG.cell_type_context, name="cell_type_context", curie=OWG.curie('cell_type_context'),
                   model_uri=OWG.cell_type_context, domain=None, range=Optional[Union[dict, CellType]])

slots.assay_method = Slot(uri=OWG.assay_method, name="assay_method", curie=OWG.curie('assay_method'),
                   model_uri=OWG.assay_method, domain=None, range=Optional[Union[str, "ExpressionAssayMethodEnum"]])

slots.phosphorylation_site = Slot(uri=OWG.phosphorylation_site, name="phosphorylation_site", curie=OWG.curie('phosphorylation_site'),
                   model_uri=OWG.phosphorylation_site, domain=None, range=Optional[str])

slots.normalization_reference = Slot(uri=OWG.normalization_reference, name="normalization_reference", curie=OWG.curie('normalization_reference'),
                   model_uri=OWG.normalization_reference, domain=None, range=Optional[str])

slots.ncbigene_id = Slot(uri=OWG.ncbigene_id, name="ncbigene_id", curie=OWG.curie('ncbigene_id'),
                   model_uri=OWG.ncbigene_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+$'))

slots.symbol = Slot(uri=OWG.symbol, name="symbol", curie=OWG.curie('symbol'),
                   model_uri=OWG.symbol, domain=None, range=Optional[str])

slots.in_taxon = Slot(uri=OWG.in_taxon, name="in_taxon", curie=OWG.curie('in_taxon'),
                   model_uri=OWG.in_taxon, domain=None, range=Optional[str])

slots.encoded_by_gene = Slot(uri=OWG.encoded_by_gene, name="encoded_by_gene", curie=OWG.curie('encoded_by_gene'),
                   model_uri=OWG.encoded_by_gene, domain=None, range=Optional[Union[dict, Gene]])

slots.cl_id = Slot(uri=OWG.cl_id, name="cl_id", curie=OWG.curie('cl_id'),
                   model_uri=OWG.cl_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^CL:\d{7}$'))

slots.uberon_id = Slot(uri=OWG.uberon_id, name="uberon_id", curie=OWG.curie('uberon_id'),
                   model_uri=OWG.uberon_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^UBERON:\d{7}$'))

slots.taxon_id = Slot(uri=OWG.taxon_id, name="taxon_id", curie=OWG.curie('taxon_id'),
                   model_uri=OWG.taxon_id, domain=None, range=Optional[str])

slots.exposure = Slot(uri=OWG.exposure, name="exposure", curie=OWG.curie('exposure'),
                   model_uri=OWG.exposure, domain=None, range=Optional[Union[str, ExposureEventId]])

slots.chemical = Slot(uri=OWG.chemical, name="chemical", curie=OWG.curie('chemical'),
                   model_uri=OWG.chemical, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.gene = Slot(uri=OWG.gene, name="gene", curie=OWG.curie('gene'),
                   model_uri=OWG.gene, domain=None, range=Optional[Union[str, GeneId]])

slots.disease = Slot(uri=OWG.disease, name="disease", curie=OWG.curie('disease'),
                   model_uri=OWG.disease, domain=None, range=Optional[Union[str, DiseaseId]])

slots.association_type = Slot(uri=OWG.association_type, name="association_type", curie=OWG.curie('association_type'),
                   model_uri=OWG.association_type, domain=None, range=Optional[str])

slots.evidence = Slot(uri=OWG.evidence, name="evidence", curie=OWG.curie('evidence'),
                   model_uri=OWG.evidence, domain=None, range=Optional[str])

slots.interaction_type = Slot(uri=OWG.interaction_type, name="interaction_type", curie=OWG.curie('interaction_type'),
                   model_uri=OWG.interaction_type, domain=None, range=Optional[str])

slots.genetic_variant = Slot(uri=OWG.genetic_variant, name="genetic_variant", curie=OWG.curie('genetic_variant'),
                   model_uri=OWG.genetic_variant, domain=None, range=Optional[str])

slots.p_value = Slot(uri=OWG.p_value, name="p_value", curie=OWG.curie('p_value'),
                   model_uri=OWG.p_value, domain=None, range=Optional[float])

slots.effect_size = Slot(uri=OWG.effect_size, name="effect_size", curie=OWG.curie('effect_size'),
                   model_uri=OWG.effect_size, domain=None, range=Optional[float])

slots.exposure_measurements = Slot(uri=OWG.exposure_measurements, name="exposure_measurements", curie=OWG.curie('exposure_measurements'),
                   model_uri=OWG.exposure_measurements, domain=None, range=Optional[Union[dict[Union[str, ExposureMeasurementId], Union[dict, ExposureMeasurement]], list[Union[dict, ExposureMeasurement]]]])

slots.biomarker_measurements = Slot(uri=OWG.biomarker_measurements, name="biomarker_measurements", curie=OWG.curie('biomarker_measurements'),
                   model_uri=OWG.biomarker_measurements, domain=None, range=Optional[Union[dict[Union[str, BiomarkerMeasurementId], Union[dict, BiomarkerMeasurement]], list[Union[dict, BiomarkerMeasurement]]]])

slots.phenotype_measurements = Slot(uri=OWG.phenotype_measurements, name="phenotype_measurements", curie=OWG.curie('phenotype_measurements'),
                   model_uri=OWG.phenotype_measurements, domain=None, range=Optional[Union[dict[Union[str, PhenotypeMeasurementId], Union[dict, PhenotypeMeasurement]], list[Union[dict, PhenotypeMeasurement]]]])

slots.gene_expression_measurements = Slot(uri=OWG.gene_expression_measurements, name="gene_expression_measurements", curie=OWG.curie('gene_expression_measurements'),
                   model_uri=OWG.gene_expression_measurements, domain=None, range=Optional[Union[dict[Union[str, GeneExpressionMeasurementId], Union[dict, GeneExpressionMeasurement]], list[Union[dict, GeneExpressionMeasurement]]]])

slots.protein_expression_measurements = Slot(uri=OWG.protein_expression_measurements, name="protein_expression_measurements", curie=OWG.curie('protein_expression_measurements'),
                   model_uri=OWG.protein_expression_measurements, domain=None, range=Optional[Union[dict[Union[str, ProteinExpressionMeasurementId], Union[dict, ProteinExpressionMeasurement]], list[Union[dict, ProteinExpressionMeasurement]]]])

slots.aggregated_measurements = Slot(uri=OWG.aggregated_measurements, name="aggregated_measurements", curie=OWG.curie('aggregated_measurements'),
                   model_uri=OWG.aggregated_measurements, domain=None, range=Optional[Union[dict[Union[str, AggregatedMeasurementId], Union[dict, AggregatedMeasurement]], list[Union[dict, AggregatedMeasurement]]]])

slots.studies = Slot(uri=OWG.studies, name="studies", curie=OWG.curie('studies'),
                   model_uri=OWG.studies, domain=None, range=Optional[Union[dict[Union[str, StudyId], Union[dict, Study]], list[Union[dict, Study]]]])

slots.cohorts = Slot(uri=OWG.cohorts, name="cohorts", curie=OWG.curie('cohorts'),
                   model_uri=OWG.cohorts, domain=None, range=Optional[Union[dict[Union[str, CohortId], Union[dict, Cohort]], list[Union[dict, Cohort]]]])

slots.participants = Slot(uri=OWG.participants, name="participants", curie=OWG.curie('participants'),
                   model_uri=OWG.participants, domain=None, range=Optional[Union[dict[Union[str, ParticipantId], Union[dict, Participant]], list[Union[dict, Participant]]]])

slots.chemicals = Slot(uri=OWG.chemicals, name="chemicals", curie=OWG.curie('chemicals'),
                   model_uri=OWG.chemicals, domain=None, range=Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]])

slots.genes = Slot(uri=OWG.genes, name="genes", curie=OWG.curie('genes'),
                   model_uri=OWG.genes, domain=None, range=Optional[Union[dict[Union[str, GeneId], Union[dict, Gene]], list[Union[dict, Gene]]]])

slots.proteins = Slot(uri=OWG.proteins, name="proteins", curie=OWG.curie('proteins'),
                   model_uri=OWG.proteins, domain=None, range=Optional[Union[dict[Union[str, ProteinId], Union[dict, Protein]], list[Union[dict, Protein]]]])

slots.ciliary_measurements = Slot(uri=OWG.ciliary_measurements, name="ciliary_measurements", curie=OWG.curie('ciliary_measurements'),
                   model_uri=OWG.ciliary_measurements, domain=None, range=Optional[Union[dict[Union[str, PhenotypeMeasurementId], Union[dict, PhenotypeMeasurement]], list[Union[dict, PhenotypeMeasurement]]]])

slots.asl_measurements = Slot(uri=OWG.asl_measurements, name="asl_measurements", curie=OWG.curie('asl_measurements'),
                   model_uri=OWG.asl_measurements, domain=None, range=Optional[Union[dict[Union[str, PhenotypeMeasurementId], Union[dict, PhenotypeMeasurement]], list[Union[dict, PhenotypeMeasurement]]]])

slots.mcc_measurements = Slot(uri=OWG.mcc_measurements, name="mcc_measurements", curie=OWG.curie('mcc_measurements'),
                   model_uri=OWG.mcc_measurements, domain=None, range=Optional[Union[dict[Union[str, PhenotypeMeasurementId], Union[dict, PhenotypeMeasurement]], list[Union[dict, PhenotypeMeasurement]]]])

slots.goblet_cell_measurements = Slot(uri=OWG.goblet_cell_measurements, name="goblet_cell_measurements", curie=OWG.curie('goblet_cell_measurements'),
                   model_uri=OWG.goblet_cell_measurements, domain=None, range=Optional[Union[dict[Union[str, PhenotypeMeasurementId], Union[dict, PhenotypeMeasurement]], list[Union[dict, PhenotypeMeasurement]]]])

slots.oxidative_stress_measurements = Slot(uri=OWG.oxidative_stress_measurements, name="oxidative_stress_measurements", curie=OWG.curie('oxidative_stress_measurements'),
                   model_uri=OWG.oxidative_stress_measurements, domain=None, range=Optional[Union[dict[Union[str, BiomarkerMeasurementId], Union[dict, BiomarkerMeasurement]], list[Union[dict, BiomarkerMeasurement]]]])

slots.barrier_measurements = Slot(uri=OWG.barrier_measurements, name="barrier_measurements", curie=OWG.curie('barrier_measurements'),
                   model_uri=OWG.barrier_measurements, domain=None, range=Optional[Union[dict[Union[str, BiomarkerMeasurementId], Union[dict, BiomarkerMeasurement]], list[Union[dict, BiomarkerMeasurement]]]])

slots.cytotoxicity_measurements = Slot(uri=OWG.cytotoxicity_measurements, name="cytotoxicity_measurements", curie=OWG.curie('cytotoxicity_measurements'),
                   model_uri=OWG.cytotoxicity_measurements, domain=None, range=Optional[Union[dict[Union[str, BiomarkerMeasurementId], Union[dict, BiomarkerMeasurement]], list[Union[dict, BiomarkerMeasurement]]]])

slots.chemical_exposures = Slot(uri=OWG.chemical_exposures, name="chemical_exposures", curie=OWG.curie('chemical_exposures'),
                   model_uri=OWG.chemical_exposures, domain=None, range=Optional[Union[dict[Union[str, ChemicalExposureId], Union[dict, ChemicalExposure]], list[Union[dict, ChemicalExposure]]]])

slots.dietary_exposures = Slot(uri=OWG.dietary_exposures, name="dietary_exposures", curie=OWG.curie('dietary_exposures'),
                   model_uri=OWG.dietary_exposures, domain=None, range=Optional[Union[dict[Union[str, DietaryExposureId], Union[dict, DietaryExposure]], list[Union[dict, DietaryExposure]]]])

slots.environmental_exposures = Slot(uri=OWG.environmental_exposures, name="environmental_exposures", curie=OWG.curie('environmental_exposures'),
                   model_uri=OWG.environmental_exposures, domain=None, range=Optional[Union[dict[Union[str, EnvironmentalExposureId], Union[dict, EnvironmentalExposure]], list[Union[dict, EnvironmentalExposure]]]])

slots.occupational_exposures = Slot(uri=OWG.occupational_exposures, name="occupational_exposures", curie=OWG.curie('occupational_exposures'),
                   model_uri=OWG.occupational_exposures, domain=None, range=Optional[Union[dict[Union[str, OccupationalExposureId], Union[dict, OccupationalExposure]], list[Union[dict, OccupationalExposure]]]])

slots.phenotypes = Slot(uri=OWG.phenotypes, name="phenotypes", curie=OWG.curie('phenotypes'),
                   model_uri=OWG.phenotypes, domain=None, range=Optional[Union[dict[Union[str, PhenotypeId], Union[dict, Phenotype]], list[Union[dict, Phenotype]]]])

slots.diseases = Slot(uri=OWG.diseases, name="diseases", curie=OWG.curie('diseases'),
                   model_uri=OWG.diseases, domain=None, range=Optional[Union[dict[Union[str, DiseaseId], Union[dict, Disease]], list[Union[dict, Disease]]]])

slots.adverse_outcomes = Slot(uri=OWG.adverse_outcomes, name="adverse_outcomes", curie=OWG.curie('adverse_outcomes'),
                   model_uri=OWG.adverse_outcomes, domain=None, range=Optional[Union[dict[Union[str, AdverseOutcomeId], Union[dict, AdverseOutcome]], list[Union[dict, AdverseOutcome]]]])

slots.adverse_outcome_pathways = Slot(uri=OWG.adverse_outcome_pathways, name="adverse_outcome_pathways", curie=OWG.curie('adverse_outcome_pathways'),
                   model_uri=OWG.adverse_outcome_pathways, domain=None, range=Optional[Union[dict[Union[str, AdverseOutcomePathwayId], Union[dict, AdverseOutcomePathway]], list[Union[dict, AdverseOutcomePathway]]]])

slots.cell_types = Slot(uri=OWG.cell_types, name="cell_types", curie=OWG.curie('cell_types'),
                   model_uri=OWG.cell_types, domain=None, range=Optional[Union[dict[Union[str, CellTypeId], Union[dict, CellType]], list[Union[dict, CellType]]]])

slots.anatomical_entities = Slot(uri=OWG.anatomical_entities, name="anatomical_entities", curie=OWG.curie('anatomical_entities'),
                   model_uri=OWG.anatomical_entities, domain=None, range=Optional[Union[dict[Union[str, AnatomicalEntityId], Union[dict, AnatomicalEntity]], list[Union[dict, AnatomicalEntity]]]])

slots.organisms = Slot(uri=OWG.organisms, name="organisms", curie=OWG.curie('organisms'),
                   model_uri=OWG.organisms, domain=None, range=Optional[Union[dict[Union[str, OrganismId], Union[dict, Organism]], list[Union[dict, Organism]]]])

slots.exposure_to_phenotype_associations = Slot(uri=OWG.exposure_to_phenotype_associations, name="exposure_to_phenotype_associations", curie=OWG.curie('exposure_to_phenotype_associations'),
                   model_uri=OWG.exposure_to_phenotype_associations, domain=None, range=Optional[Union[dict[Union[str, ExposureToPhenotypeAssociationId], Union[dict, ExposureToPhenotypeAssociation]], list[Union[dict, ExposureToPhenotypeAssociation]]]])

slots.quantityValue__unit = Slot(uri=OWG.unit, name="quantityValue__unit", curie=OWG.curie('unit'),
                   model_uri=OWG.quantityValue__unit, domain=None, range=Optional[Union[dict, Unit]])

slots.quantityValue__value = Slot(uri=OWG.value, name="quantityValue__value", curie=OWG.curie('value'),
                   model_uri=OWG.quantityValue__value, domain=None, range=Optional[str])

slots.quantityRange__lower_bound = Slot(uri=OWG.lower_bound, name="quantityRange__lower_bound", curie=OWG.curie('lower_bound'),
                   model_uri=OWG.quantityRange__lower_bound, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.quantityRange__upper_bound = Slot(uri=OWG.upper_bound, name="quantityRange__upper_bound", curie=OWG.curie('upper_bound'),
                   model_uri=OWG.quantityRange__upper_bound, domain=None, range=Optional[Union[dict, QuantityValue]])
