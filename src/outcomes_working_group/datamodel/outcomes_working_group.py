# Auto generated from outcomes_working_group.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-01-10T17:55:22
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

from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
AOPWIKI = CurieNamespace('AOPWIKI', 'https://aopwiki.org/aops/')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
CLO = CurieNamespace('CLO', 'http://purl.obolibrary.org/obo/CLO_')
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
NAMO = CurieNamespace('NAMO', 'http://purl.obolibrary.org/obo/NAMO_')
NCBIGENE = CurieNamespace('NCBIGENE', 'https://www.ncbi.nlm.nih.gov/gene/')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
NHANES = CurieNamespace('NHANES', 'https://wwwn.cdc.gov/Nchs/Nhanes/')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
OMRSE = CurieNamespace('OMRSE', 'http://purl.obolibrary.org/obo/OMRSE_')
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
WIKIDATA = CurieNamespace('wikidata', 'http://www.wikidata.org/entity/')
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


class EnvironmentalMeasurementId(MeasurementId):
    pass


class MechanicalMeasurementId(MeasurementId):
    pass


class MembranePropertyMeasurementId(MeasurementId):
    pass


class CellLineId(NamedThingId):
    pass


class CellCultureConditionsId(NamedThingId):
    pass


class CellCultureMediumId(NamedThingId):
    pass


class MediumSupplementId(NamedThingId):
    pass


class ModelSystemId(NamedThingId):
    pass


class CellularSystemId(ModelSystemId):
    pass


class TwoDCellCultureId(CellularSystemId):
    pass


class ThreeDCellCultureId(CellularSystemId):
    pass


class CoCultureId(CellularSystemId):
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


class GeographicEntityId(NamedThingId):
    pass


class StateId(GeographicEntityId):
    pass


class PublicUseMicrodataAreaId(GeographicEntityId):
    pass


class CountyId(GeographicEntityId):
    pass


class CensusTractId(GeographicEntityId):
    pass


class BlockGroupId(GeographicEntityId):
    pass


class SchoolId(NamedThingId):
    pass


class HouseholdId(NamedThingId):
    pass


class PersonId(NamedThingId):
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
    states: Optional[Union[dict[Union[str, StateId], Union[dict, "State"]], list[Union[dict, "State"]]]] = empty_dict()
    public_use_microdata_areas: Optional[Union[dict[Union[str, PublicUseMicrodataAreaId], Union[dict, "PublicUseMicrodataArea"]], list[Union[dict, "PublicUseMicrodataArea"]]]] = empty_dict()
    counties: Optional[Union[dict[Union[str, CountyId], Union[dict, "County"]], list[Union[dict, "County"]]]] = empty_dict()
    census_tracts: Optional[Union[dict[Union[str, CensusTractId], Union[dict, "CensusTract"]], list[Union[dict, "CensusTract"]]]] = empty_dict()
    block_groups: Optional[Union[dict[Union[str, BlockGroupId], Union[dict, "BlockGroup"]], list[Union[dict, "BlockGroup"]]]] = empty_dict()
    households: Optional[Union[dict[Union[str, HouseholdId], Union[dict, "Household"]], list[Union[dict, "Household"]]]] = empty_dict()
    persons: Optional[Union[dict[Union[str, PersonId], Union[dict, "Person"]], list[Union[dict, "Person"]]]] = empty_dict()
    schools: Optional[Union[dict[Union[str, SchoolId], Union[dict, "School"]], list[Union[dict, "School"]]]] = empty_dict()
    cellular_systems: Optional[Union[dict[Union[str, CellularSystemId], Union[dict, "CellularSystem"]], list[Union[dict, "CellularSystem"]]]] = empty_dict()
    two_d_cell_cultures: Optional[Union[dict[Union[str, TwoDCellCultureId], Union[dict, "TwoDCellCulture"]], list[Union[dict, "TwoDCellCulture"]]]] = empty_dict()
    three_d_cell_cultures: Optional[Union[dict[Union[str, ThreeDCellCultureId], Union[dict, "ThreeDCellCulture"]], list[Union[dict, "ThreeDCellCulture"]]]] = empty_dict()
    co_cultures: Optional[Union[dict[Union[str, CoCultureId], Union[dict, "CoCulture"]], list[Union[dict, "CoCulture"]]]] = empty_dict()
    cell_lines: Optional[Union[dict[Union[str, CellLineId], Union[dict, "CellLine"]], list[Union[dict, "CellLine"]]]] = empty_dict()
    environmental_measurements: Optional[Union[dict[Union[str, EnvironmentalMeasurementId], Union[dict, "EnvironmentalMeasurement"]], list[Union[dict, "EnvironmentalMeasurement"]]]] = empty_dict()
    mechanical_measurements: Optional[Union[dict[Union[str, MechanicalMeasurementId], Union[dict, "MechanicalMeasurement"]], list[Union[dict, "MechanicalMeasurement"]]]] = empty_dict()

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

        self._normalize_inlined_as_list(slot_name="states", slot_type=State, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="public_use_microdata_areas", slot_type=PublicUseMicrodataArea, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="counties", slot_type=County, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="census_tracts", slot_type=CensusTract, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="block_groups", slot_type=BlockGroup, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="households", slot_type=Household, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="persons", slot_type=Person, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="schools", slot_type=School, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="cellular_systems", slot_type=CellularSystem, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="two_d_cell_cultures", slot_type=TwoDCellCulture, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="three_d_cell_cultures", slot_type=ThreeDCellCulture, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="co_cultures", slot_type=CoCulture, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="cell_lines", slot_type=CellLine, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="environmental_measurements", slot_type=EnvironmentalMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="mechanical_measurements", slot_type=MechanicalMeasurement, key_name="id", keyed=True)

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
    A role representing an individual's participation in a study. Links a Person to a specific study cohort and
    captures study-specific identifiers and attributes. Age and sex are recorded at enrollment and may differ from the
    Person's current values or values in other study registrations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Participant"]
    class_class_curie: ClassVar[str] = "owg:Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = OWG.Participant

    id: Union[str, ParticipantId] = None
    person: Optional[Union[str, PersonId]] = None
    part_of_cohort: Optional[Union[str, CohortId]] = None
    participant_id: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[Union[str, "SexEnum"]] = None
    enrollment_date: Optional[Union[str, XSDDate]] = None
    withdrawal_date: Optional[Union[str, XSDDate]] = None
    study_arm: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParticipantId):
            self.id = ParticipantId(self.id)

        if self.person is not None and not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

        if self.part_of_cohort is not None and not isinstance(self.part_of_cohort, CohortId):
            self.part_of_cohort = CohortId(self.part_of_cohort)

        if self.participant_id is not None and not isinstance(self.participant_id, str):
            self.participant_id = str(self.participant_id)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        if self.sex is not None and not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self.enrollment_date is not None and not isinstance(self.enrollment_date, XSDDate):
            self.enrollment_date = XSDDate(self.enrollment_date)

        if self.withdrawal_date is not None and not isinstance(self.withdrawal_date, XSDDate):
            self.withdrawal_date = XSDDate(self.withdrawal_date)

        if self.study_arm is not None and not isinstance(self.study_arm, str):
            self.study_arm = str(self.study_arm)

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
class EnvironmentalMeasurement(Measurement):
    """
    A measurement of environmental conditions for cell culture systems including temperature, CO2, O2 percentage,
    humidity, and pH. Used to document incubator and culture conditions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["EnvironmentalMeasurement"]
    class_class_curie: ClassVar[str] = "owg:EnvironmentalMeasurement"
    class_name: ClassVar[str] = "EnvironmentalMeasurement"
    class_model_uri: ClassVar[URIRef] = OWG.EnvironmentalMeasurement

    id: Union[str, EnvironmentalMeasurementId] = None
    observation_type: Optional[Union[str, "EnvironmentalMeasurementTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalMeasurementId):
            self.id = EnvironmentalMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, EnvironmentalMeasurementTypeEnum):
            self.observation_type = EnvironmentalMeasurementTypeEnum(self.observation_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MechanicalMeasurement(Measurement):
    """
    A measurement of mechanical stimulation parameters for advanced culture systems like organ-on-chip and
    microphysiological systems. Includes stretch frequency/amplitude, shear stress, flow rate, and pressure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["MechanicalMeasurement"]
    class_class_curie: ClassVar[str] = "owg:MechanicalMeasurement"
    class_name: ClassVar[str] = "MechanicalMeasurement"
    class_model_uri: ClassVar[URIRef] = OWG.MechanicalMeasurement

    id: Union[str, MechanicalMeasurementId] = None
    observation_type: Optional[Union[str, "MechanicalMeasurementTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MechanicalMeasurementId):
            self.id = MechanicalMeasurementId(self.id)

        if self.observation_type is not None and not isinstance(self.observation_type, MechanicalMeasurementTypeEnum):
            self.observation_type = MechanicalMeasurementTypeEnum(self.observation_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MembranePropertyMeasurement(Measurement):
    """
    A measurement of membrane properties for transwell, ALI, and organ-on-chip culture systems. Includes pore size,
    pore density, thickness, surface area, and TEER.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["MembranePropertyMeasurement"]
    class_class_curie: ClassVar[str] = "owg:MembranePropertyMeasurement"
    class_name: ClassVar[str] = "MembranePropertyMeasurement"
    class_model_uri: ClassVar[URIRef] = OWG.MembranePropertyMeasurement

    id: Union[str, MembranePropertyMeasurementId] = None
    membrane_material: Optional[str] = None
    observation_type: Optional[Union[str, "MembranePropertyTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MembranePropertyMeasurementId):
            self.id = MembranePropertyMeasurementId(self.id)

        if self.membrane_material is not None and not isinstance(self.membrane_material, str):
            self.membrane_material = str(self.membrane_material)

        if self.observation_type is not None and not isinstance(self.observation_type, MembranePropertyTypeEnum):
            self.observation_type = MembranePropertyTypeEnum(self.observation_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellLine(NamedThing):
    """
    A cell line - a genetically stable cultured cell population that contains individual cell line cells. Reference to
    a specific cell line with identifiers from cell line repositories.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CLO["0000031"]
    class_class_curie: ClassVar[str] = "CLO:0000031"
    class_name: ClassVar[str] = "CellLine"
    class_model_uri: ClassVar[URIRef] = OWG.CellLine

    id: Union[str, CellLineId] = None
    cell_culture_type: Optional[Union[dict, "CellType"]] = None
    model_species: Optional[Union[dict, "Organism"]] = None
    tissue_origin: Optional[Union[dict, "AnatomicalEntity"]] = None
    disease_state: Optional[Union[dict, Disease]] = None
    supplier: Optional[str] = None
    catalog_number: Optional[str] = None
    authentication_method: Optional[str] = None
    mycoplasma_status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)

        if self.cell_culture_type is not None and not isinstance(self.cell_culture_type, CellType):
            self.cell_culture_type = CellType(**as_dict(self.cell_culture_type))

        if self.model_species is not None and not isinstance(self.model_species, Organism):
            self.model_species = Organism(**as_dict(self.model_species))

        if self.tissue_origin is not None and not isinstance(self.tissue_origin, AnatomicalEntity):
            self.tissue_origin = AnatomicalEntity(**as_dict(self.tissue_origin))

        if self.disease_state is not None and not isinstance(self.disease_state, Disease):
            self.disease_state = Disease(**as_dict(self.disease_state))

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
class CellCultureConditions(NamedThing):
    """
    Detailed cell culture parameters including medium, environment, and timing.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["CellCultureConditions"]
    class_class_curie: ClassVar[str] = "owg:CellCultureConditions"
    class_name: ClassVar[str] = "CellCultureConditions"
    class_model_uri: ClassVar[URIRef] = OWG.CellCultureConditions

    id: Union[str, CellCultureConditionsId] = None
    culture_media: Optional[Union[dict, "CellCultureMedium"]] = None
    days_at_air_liquid_interface: Optional[int] = None
    passage_number: Optional[int] = None
    substrate_type: Optional[Union[str, "SubstrateTypeEnum"]] = None
    cell_culture_growth_mode: Optional[Union[str, "CellCultureGrowthModeEnum"]] = None
    environmental_measurements: Optional[Union[dict[Union[str, EnvironmentalMeasurementId], Union[dict, EnvironmentalMeasurement]], list[Union[dict, EnvironmentalMeasurement]]]] = empty_dict()
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

        self._normalize_inlined_as_list(slot_name="environmental_measurements", slot_type=EnvironmentalMeasurement, key_name="id", keyed=True)

        if self.donor_count is not None and not isinstance(self.donor_count, int):
            self.donor_count = int(self.donor_count)

        if self.replicates_per_donor is not None and not isinstance(self.replicates_per_donor, int):
            self.replicates_per_donor = int(self.replicates_per_donor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellCultureMedium(NamedThing):
    """
    Detailed formulation of cell culture medium including base medium and supplements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["CellCultureMedium"]
    class_class_curie: ClassVar[str] = "owg:CellCultureMedium"
    class_name: ClassVar[str] = "CellCultureMedium"
    class_model_uri: ClassVar[URIRef] = OWG.CellCultureMedium

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
class MediumSupplement(NamedThing):
    """
    Supplement or additive to cell culture medium.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["MediumSupplement"]
    class_class_curie: ClassVar[str] = "owg:MediumSupplement"
    class_name: ClassVar[str] = "MediumSupplement"
    class_model_uri: ClassVar[URIRef] = OWG.MediumSupplement

    id: Union[str, MediumSupplementId] = None
    supplement_type: Optional[Union[str, "SupplementTypeEnum"]] = None
    supplement_entity: Optional[Union[dict, ChemicalEntity]] = None
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

        if self.supplement_entity is not None and not isinstance(self.supplement_entity, ChemicalEntity):
            self.supplement_entity = ChemicalEntity(**as_dict(self.supplement_entity))

        if self.concentration is not None and not isinstance(self.concentration, QuantityValue):
            self.concentration = QuantityValue(**as_dict(self.concentration))

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.catalog_number is not None and not isinstance(self.catalog_number, str):
            self.catalog_number = str(self.catalog_number)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelSystem(NamedThing):
    """
    Abstract base class for model systems used in biomedical research. Encompasses cellular systems,
    microphysiological systems, and in silico models.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["0000000"]
    class_class_curie: ClassVar[str] = "NAMO:0000000"
    class_name: ClassVar[str] = "ModelSystem"
    class_model_uri: ClassVar[URIRef] = OWG.ModelSystem

    id: Union[str, ModelSystemId] = None
    model_species: Optional[Union[dict, "Organism"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.model_species is not None and not isinstance(self.model_species, Organism):
            self.model_species = Organism(**as_dict(self.model_species))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellularSystem(ModelSystem):
    """
    Cell-based model systems that use living cells to model biological processes. Includes 2D cultures, 3D systems,
    and co-cultures. Abstract base class for specific culture types.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["0000001"]
    class_class_curie: ClassVar[str] = "NAMO:0000001"
    class_name: ClassVar[str] = "CellularSystem"
    class_model_uri: ClassVar[URIRef] = OWG.CellularSystem

    id: Union[str, CellularSystemId] = None
    cell_line: Optional[Union[dict, CellLine]] = None
    cell_line_lineage: Optional[str] = None
    primary_cultured_cell: Optional[Union[dict, "CellType"]] = None
    cell_culture_type: Optional[Union[dict, "CellType"]] = None
    anatomical_origin: Optional[Union[dict, "AnatomicalEntity"]] = None
    cell_culture_growth_mode: Optional[Union[str, "CellCultureGrowthModeEnum"]] = None
    cell_line_modification: Optional[Union[str, "CellLineModificationEnum"]] = None
    induced_pluripotent_stem_cell_line: Optional[Union[bool, Bool]] = None
    culture_conditions: Optional[Union[dict, CellCultureConditions]] = None
    culture_media: Optional[Union[dict, CellCultureMedium]] = None
    environmental_measurements: Optional[Union[dict[Union[str, EnvironmentalMeasurementId], Union[dict, EnvironmentalMeasurement]], list[Union[dict, EnvironmentalMeasurement]]]] = empty_dict()
    mechanical_measurements: Optional[Union[dict[Union[str, MechanicalMeasurementId], Union[dict, MechanicalMeasurement]], list[Union[dict, MechanicalMeasurement]]]] = empty_dict()
    membrane_properties: Optional[Union[dict[Union[str, MembranePropertyMeasurementId], Union[dict, MembranePropertyMeasurement]], list[Union[dict, MembranePropertyMeasurement]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cell_line is not None and not isinstance(self.cell_line, CellLine):
            self.cell_line = CellLine(**as_dict(self.cell_line))

        if self.cell_line_lineage is not None and not isinstance(self.cell_line_lineage, str):
            self.cell_line_lineage = str(self.cell_line_lineage)

        if self.primary_cultured_cell is not None and not isinstance(self.primary_cultured_cell, CellType):
            self.primary_cultured_cell = CellType(**as_dict(self.primary_cultured_cell))

        if self.cell_culture_type is not None and not isinstance(self.cell_culture_type, CellType):
            self.cell_culture_type = CellType(**as_dict(self.cell_culture_type))

        if self.anatomical_origin is not None and not isinstance(self.anatomical_origin, AnatomicalEntity):
            self.anatomical_origin = AnatomicalEntity(**as_dict(self.anatomical_origin))

        if self.cell_culture_growth_mode is not None and not isinstance(self.cell_culture_growth_mode, CellCultureGrowthModeEnum):
            self.cell_culture_growth_mode = CellCultureGrowthModeEnum(self.cell_culture_growth_mode)

        if self.cell_line_modification is not None and not isinstance(self.cell_line_modification, CellLineModificationEnum):
            self.cell_line_modification = CellLineModificationEnum(self.cell_line_modification)

        if self.induced_pluripotent_stem_cell_line is not None and not isinstance(self.induced_pluripotent_stem_cell_line, Bool):
            self.induced_pluripotent_stem_cell_line = Bool(self.induced_pluripotent_stem_cell_line)

        if self.culture_conditions is not None and not isinstance(self.culture_conditions, CellCultureConditions):
            self.culture_conditions = CellCultureConditions(**as_dict(self.culture_conditions))

        if self.culture_media is not None and not isinstance(self.culture_media, CellCultureMedium):
            self.culture_media = CellCultureMedium(**as_dict(self.culture_media))

        self._normalize_inlined_as_list(slot_name="environmental_measurements", slot_type=EnvironmentalMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="mechanical_measurements", slot_type=MechanicalMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="membrane_properties", slot_type=MembranePropertyMeasurement, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TwoDCellCulture(CellularSystem):
    """
    Conventional monolayer cell cultures grown on flat surfaces. Includes adherent and suspension cultures in standard
    tissue culture vessels.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["0000002"]
    class_class_curie: ClassVar[str] = "NAMO:0000002"
    class_name: ClassVar[str] = "TwoDCellCulture"
    class_model_uri: ClassVar[URIRef] = OWG.TwoDCellCulture

    id: Union[str, TwoDCellCultureId] = None
    substrate_type: Optional[Union[str, "SubstrateTypeEnum"]] = None
    confluence_level: Optional[Union[dict, QuantityValue]] = None
    passage_number: Optional[int] = None
    seeding_density: Optional[Union[dict, QuantityValue]] = None
    coating: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TwoDCellCultureId):
            self.id = TwoDCellCultureId(self.id)

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

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThreeDCellCulture(CellularSystem):
    """
    Three-dimensional cell culture systems including spheroids, organoids, and scaffold-based cultures. Provides
    enhanced physiological relevance with 3D architecture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["0000003"]
    class_class_curie: ClassVar[str] = "NAMO:0000003"
    class_name: ClassVar[str] = "ThreeDCellCulture"
    class_model_uri: ClassVar[URIRef] = OWG.ThreeDCellCulture

    id: Union[str, ThreeDCellCultureId] = None
    three_d_architecture: Optional[Union[str, "ThreeDArchitectureEnum"]] = None
    matrix_composition: Optional[str] = None
    size_range: Optional[Union[dict, QuantityRange]] = None
    organoid_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThreeDCellCultureId):
            self.id = ThreeDCellCultureId(self.id)

        if self.three_d_architecture is not None and not isinstance(self.three_d_architecture, ThreeDArchitectureEnum):
            self.three_d_architecture = ThreeDArchitectureEnum(self.three_d_architecture)

        if self.matrix_composition is not None and not isinstance(self.matrix_composition, str):
            self.matrix_composition = str(self.matrix_composition)

        if self.size_range is not None and not isinstance(self.size_range, QuantityRange):
            self.size_range = QuantityRange(**as_dict(self.size_range))

        if self.organoid_type is not None and not isinstance(self.organoid_type, str):
            self.organoid_type = str(self.organoid_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoCulture(CellularSystem):
    """
    Co-culture systems combining multiple cell types to simulate tissue microenvironments and cell-cell interactions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NAMO["0000004"]
    class_class_curie: ClassVar[str] = "NAMO:0000004"
    class_name: ClassVar[str] = "CoCulture"
    class_model_uri: ClassVar[URIRef] = OWG.CoCulture

    id: Union[str, CoCultureId] = None
    coculture_configuration: Optional[Union[str, "CoCultureConfigurationEnum"]] = None
    cell_type_ratios: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CoCultureId):
            self.id = CoCultureId(self.id)

        if self.coculture_configuration is not None and not isinstance(self.coculture_configuration, CoCultureConfigurationEnum):
            self.coculture_configuration = CoCultureConfigurationEnum(self.coculture_configuration)

        if not isinstance(self.cell_type_ratios, list):
            self.cell_type_ratios = [self.cell_type_ratios] if self.cell_type_ratios is not None else []
        self.cell_type_ratios = [v if isinstance(v, str) else str(v) for v in self.cell_type_ratios]

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


@dataclass(repr=False)
class GeographicEntity(NamedThing):
    """
    Abstract base class for geographic entities used in synthetic population modeling. Provides common geographic
    identifier infrastructure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["GeographicEntity"]
    class_class_curie: ClassVar[str] = "owg:GeographicEntity"
    class_name: ClassVar[str] = "GeographicEntity"
    class_model_uri: ClassVar[URIRef] = OWG.GeographicEntity

    id: Union[str, GeographicEntityId] = None
    federal_information_processing_standard_code: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.federal_information_processing_standard_code is not None and not isinstance(self.federal_information_processing_standard_code, str):
            self.federal_information_processing_standard_code = str(self.federal_information_processing_standard_code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class State(GeographicEntity):
    """
    A U.S. state or equivalent territory with associated geographic properties. Contains counties and public use
    microdata areas.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["State"]
    class_class_curie: ClassVar[str] = "owg:State"
    class_name: ClassVar[str] = "State"
    class_model_uri: ClassVar[URIRef] = OWG.State

    id: Union[str, StateId] = None
    abbreviation: Optional[str] = None
    counties: Optional[Union[dict[Union[str, CountyId], Union[dict, "County"]], list[Union[dict, "County"]]]] = empty_dict()
    public_use_microdata_areas: Optional[Union[dict[Union[str, PublicUseMicrodataAreaId], Union[dict, "PublicUseMicrodataArea"]], list[Union[dict, "PublicUseMicrodataArea"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StateId):
            self.id = StateId(self.id)

        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        self._normalize_inlined_as_list(slot_name="counties", slot_type=County, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="public_use_microdata_areas", slot_type=PublicUseMicrodataArea, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicUseMicrodataArea(GeographicEntity):
    """
    Public Use Microdata Areas (PUMAs) are non-overlapping, statistical geographic areas that partition each state or
    equivalent entity into geographic areas containing no fewer than 100,000 people each. They cover the entirety of
    the United States, Puerto Rico, and Guam.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["PublicUseMicrodataArea"]
    class_class_curie: ClassVar[str] = "owg:PublicUseMicrodataArea"
    class_name: ClassVar[str] = "PublicUseMicrodataArea"
    class_model_uri: ClassVar[URIRef] = OWG.PublicUseMicrodataArea

    id: Union[str, PublicUseMicrodataAreaId] = None
    state_federal_information_processing_standard_code: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicUseMicrodataAreaId):
            self.id = PublicUseMicrodataAreaId(self.id)

        if self.state_federal_information_processing_standard_code is not None and not isinstance(self.state_federal_information_processing_standard_code, str):
            self.state_federal_information_processing_standard_code = str(self.state_federal_information_processing_standard_code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class County(GeographicEntity):
    """
    A county or equivalent administrative subdivision with associated properties. Contains census tracts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["County"]
    class_class_curie: ClassVar[str] = "owg:County"
    class_name: ClassVar[str] = "County"
    class_model_uri: ClassVar[URIRef] = OWG.County

    id: Union[str, CountyId] = None
    state_federal_information_processing_standard_code: Optional[str] = None
    census_tracts: Optional[Union[dict[Union[str, CensusTractId], Union[dict, "CensusTract"]], list[Union[dict, "CensusTract"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CountyId):
            self.id = CountyId(self.id)

        if self.state_federal_information_processing_standard_code is not None and not isinstance(self.state_federal_information_processing_standard_code, str):
            self.state_federal_information_processing_standard_code = str(self.state_federal_information_processing_standard_code)

        self._normalize_inlined_as_list(slot_name="census_tracts", slot_type=CensusTract, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CensusTract(GeographicEntity):
    """
    A census tract is a small, relatively permanent geographic area within a county, used to collect and present
    demographic data from the census, usually containing between 2,500 and 8,000 residents and designed to be as
    homogeneous as possible in terms of population characteristics and living conditions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["CensusTract"]
    class_class_curie: ClassVar[str] = "owg:CensusTract"
    class_name: ClassVar[str] = "CensusTract"
    class_model_uri: ClassVar[URIRef] = OWG.CensusTract

    id: Union[str, CensusTractId] = None
    state_federal_information_processing_standard_code: Optional[str] = None
    county_federal_information_processing_standard_code: Optional[str] = None
    block_groups: Optional[Union[dict[Union[str, BlockGroupId], Union[dict, "BlockGroup"]], list[Union[dict, "BlockGroup"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CensusTractId):
            self.id = CensusTractId(self.id)

        if self.state_federal_information_processing_standard_code is not None and not isinstance(self.state_federal_information_processing_standard_code, str):
            self.state_federal_information_processing_standard_code = str(self.state_federal_information_processing_standard_code)

        if self.county_federal_information_processing_standard_code is not None and not isinstance(self.county_federal_information_processing_standard_code, str):
            self.county_federal_information_processing_standard_code = str(self.county_federal_information_processing_standard_code)

        self._normalize_inlined_as_list(slot_name="block_groups", slot_type=BlockGroup, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BlockGroup(GeographicEntity):
    """
    A statistical division within a census tract, typically containing between 600 and 3,000 people, which is used by
    the Census Bureau to present demographic data at a smaller, more localized level than the entire census tract.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["BlockGroup"]
    class_class_curie: ClassVar[str] = "owg:BlockGroup"
    class_name: ClassVar[str] = "BlockGroup"
    class_model_uri: ClassVar[URIRef] = OWG.BlockGroup

    id: Union[str, BlockGroupId] = None
    census_tract_federal_information_processing_standard_code: Optional[str] = None
    state_federal_information_processing_standard_code: Optional[str] = None
    county_federal_information_processing_standard_code: Optional[str] = None
    households: Optional[Union[dict[Union[str, HouseholdId], Union[dict, "Household"]], list[Union[dict, "Household"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BlockGroupId):
            self.id = BlockGroupId(self.id)

        if self.census_tract_federal_information_processing_standard_code is not None and not isinstance(self.census_tract_federal_information_processing_standard_code, str):
            self.census_tract_federal_information_processing_standard_code = str(self.census_tract_federal_information_processing_standard_code)

        if self.state_federal_information_processing_standard_code is not None and not isinstance(self.state_federal_information_processing_standard_code, str):
            self.state_federal_information_processing_standard_code = str(self.state_federal_information_processing_standard_code)

        if self.county_federal_information_processing_standard_code is not None and not isinstance(self.county_federal_information_processing_standard_code, str):
            self.county_federal_information_processing_standard_code = str(self.county_federal_information_processing_standard_code)

        self._normalize_inlined_as_list(slot_name="households", slot_type=Household, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class School(NamedThing):
    """
    A school entity representing an educational institution where synthetic population persons may be assigned for
    modeling purposes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["School"]
    class_class_curie: ClassVar[str] = "owg:School"
    class_name: ClassVar[str] = "School"
    class_model_uri: ClassVar[URIRef] = OWG.School

    id: Union[str, SchoolId] = None
    federal_information_processing_standard_code: Optional[str] = None
    state_federal_information_processing_standard_code: Optional[str] = None
    county_federal_information_processing_standard_code: Optional[str] = None
    census_tract_federal_information_processing_standard_code: Optional[str] = None
    block_group_federal_information_processing_standard_code: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SchoolId):
            self.id = SchoolId(self.id)

        if self.federal_information_processing_standard_code is not None and not isinstance(self.federal_information_processing_standard_code, str):
            self.federal_information_processing_standard_code = str(self.federal_information_processing_standard_code)

        if self.state_federal_information_processing_standard_code is not None and not isinstance(self.state_federal_information_processing_standard_code, str):
            self.state_federal_information_processing_standard_code = str(self.state_federal_information_processing_standard_code)

        if self.county_federal_information_processing_standard_code is not None and not isinstance(self.county_federal_information_processing_standard_code, str):
            self.county_federal_information_processing_standard_code = str(self.county_federal_information_processing_standard_code)

        if self.census_tract_federal_information_processing_standard_code is not None and not isinstance(self.census_tract_federal_information_processing_standard_code, str):
            self.census_tract_federal_information_processing_standard_code = str(self.census_tract_federal_information_processing_standard_code)

        if self.block_group_federal_information_processing_standard_code is not None and not isinstance(self.block_group_federal_information_processing_standard_code, str):
            self.block_group_federal_information_processing_standard_code = str(self.block_group_federal_information_processing_standard_code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Household(NamedThing):
    """
    A household entity representing a group of people living together in a single dwelling unit. Used in synthetic
    population modeling.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Household"]
    class_class_curie: ClassVar[str] = "owg:Household"
    class_name: ClassVar[str] = "Household"
    class_model_uri: ClassVar[URIRef] = OWG.Household

    id: Union[str, HouseholdId] = None
    serial_number: Optional[str] = None
    household_identifier: Optional[str] = None
    household_head_age: Optional[int] = None
    household_income: Optional[float] = None
    household_head_race: Optional[str] = None
    household_size: Optional[int] = None
    household_persons: Optional[Union[dict[Union[str, PersonId], Union[dict, "Person"]], list[Union[dict, "Person"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HouseholdId):
            self.id = HouseholdId(self.id)

        if self.serial_number is not None and not isinstance(self.serial_number, str):
            self.serial_number = str(self.serial_number)

        if self.household_identifier is not None and not isinstance(self.household_identifier, str):
            self.household_identifier = str(self.household_identifier)

        if self.household_head_age is not None and not isinstance(self.household_head_age, int):
            self.household_head_age = int(self.household_head_age)

        if self.household_income is not None and not isinstance(self.household_income, float):
            self.household_income = float(self.household_income)

        if self.household_head_race is not None and not isinstance(self.household_head_race, str):
            self.household_head_race = str(self.household_head_race)

        if self.household_size is not None and not isinstance(self.household_size, int):
            self.household_size = int(self.household_size)

        self._normalize_inlined_as_list(slot_name="household_persons", slot_type=Person, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(NamedThing):
    """
    A person (individual human being) with demographic and geographic attributes. Persons can participate in studies
    through the Participant role, which links a Person to a specific study cohort. In synthetic population contexts,
    persons are members of households within geographic hierarchies. Age and sex on Person represent current or
    snapshot values from the source data (e.g., census), distinct from study-specific values captured on Participant
    at enrollment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWG["Person"]
    class_class_curie: ClassVar[str] = "owg:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = OWG.Person

    id: Union[str, PersonId] = None
    age: Optional[int] = None
    sex: Optional[Union[str, "SexEnum"]] = None
    race: Optional[str] = None
    species: Optional[str] = None
    state_federal_information_processing_standard_code: Optional[str] = None
    county_federal_information_processing_standard_code: Optional[str] = None
    census_tract_federal_information_processing_standard_code: Optional[str] = None
    block_group_federal_information_processing_standard_code: Optional[str] = None
    serial_number: Optional[str] = None
    household_identifier: Optional[str] = None
    household_head_age: Optional[int] = None
    household_income: Optional[float] = None
    household_head_race: Optional[str] = None
    household_size: Optional[int] = None
    assigned_school: Optional[Union[str, SchoolId]] = None
    person_order: Optional[int] = None
    relationship_to_household_head: Optional[Union[str, "RelationshipToHouseholdHeadEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        if self.sex is not None and not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self.race is not None and not isinstance(self.race, str):
            self.race = str(self.race)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.state_federal_information_processing_standard_code is not None and not isinstance(self.state_federal_information_processing_standard_code, str):
            self.state_federal_information_processing_standard_code = str(self.state_federal_information_processing_standard_code)

        if self.county_federal_information_processing_standard_code is not None and not isinstance(self.county_federal_information_processing_standard_code, str):
            self.county_federal_information_processing_standard_code = str(self.county_federal_information_processing_standard_code)

        if self.census_tract_federal_information_processing_standard_code is not None and not isinstance(self.census_tract_federal_information_processing_standard_code, str):
            self.census_tract_federal_information_processing_standard_code = str(self.census_tract_federal_information_processing_standard_code)

        if self.block_group_federal_information_processing_standard_code is not None and not isinstance(self.block_group_federal_information_processing_standard_code, str):
            self.block_group_federal_information_processing_standard_code = str(self.block_group_federal_information_processing_standard_code)

        if self.serial_number is not None and not isinstance(self.serial_number, str):
            self.serial_number = str(self.serial_number)

        if self.household_identifier is not None and not isinstance(self.household_identifier, str):
            self.household_identifier = str(self.household_identifier)

        if self.household_head_age is not None and not isinstance(self.household_head_age, int):
            self.household_head_age = int(self.household_head_age)

        if self.household_income is not None and not isinstance(self.household_income, float):
            self.household_income = float(self.household_income)

        if self.household_head_race is not None and not isinstance(self.household_head_race, str):
            self.household_head_race = str(self.household_head_race)

        if self.household_size is not None and not isinstance(self.household_size, int):
            self.household_size = int(self.household_size)

        if self.assigned_school is not None and not isinstance(self.assigned_school, SchoolId):
            self.assigned_school = SchoolId(self.assigned_school)

        if self.person_order is not None and not isinstance(self.person_order, int):
            self.person_order = int(self.person_order)

        if self.relationship_to_household_head is not None and not isinstance(self.relationship_to_household_head, RelationshipToHouseholdHeadEnum):
            self.relationship_to_household_head = RelationshipToHouseholdHeadEnum(self.relationship_to_household_head)

        super().__post_init__(**kwargs)


# Enumerations
class ExposureRouteEnum(EnumDefinitionImpl):
    """
    Routes of exposure to chemicals or environmental factors
    """
    oral = PermissibleValue(
        text="oral",
        description="Oral ingestion",
        meaning=ECTO["0000895"])
    dermal = PermissibleValue(
        text="dermal",
        description="Dermal contact",
        meaning=ECTO["0000896"])
    inhalation = PermissibleValue(
        text="inhalation",
        description="Inhalation",
        meaning=ECTO["0000897"])
    injection = PermissibleValue(
        text="injection",
        description="Injection")
    unknown = PermissibleValue(
        text="unknown",
        description="Unknown route")

    _defn = EnumDefinition(
        name="ExposureRouteEnum",
        description="Routes of exposure to chemicals or environmental factors",
    )

class ExposureMediumEnum(EnumDefinitionImpl):
    """
    Medium through which exposure occurs
    """
    air = PermissibleValue(
        text="air",
        description="Air",
        meaning=ENVO["00002005"])
    water = PermissibleValue(
        text="water",
        description="Water",
        meaning=ENVO["00002006"])
    food = PermissibleValue(
        text="food",
        description="Food",
        meaning=FOODON["00002403"])
    soil = PermissibleValue(
        text="soil",
        description="Soil",
        meaning=ENVO["00001998"])
    dust = PermissibleValue(
        text="dust",
        description="Dust")
    consumer_product = PermissibleValue(
        text="consumer_product",
        description="Consumer product")
    unknown = PermissibleValue(
        text="unknown",
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
    qrt_pcr = PermissibleValue(
        text="qrt_pcr",
        description="Quantitative real-time polymerase chain reaction",
        meaning=OBI["0000893"])
    rna_seq = PermissibleValue(
        text="rna_seq",
        description="RNA sequencing (bulk)",
        meaning=OBI["0001271"])
    single_cell_rna_seq = PermissibleValue(
        text="single_cell_rna_seq",
        description="Single-cell RNA sequencing",
        meaning=OBI["0002631"])
    microarray = PermissibleValue(
        text="microarray",
        description="Gene expression microarray",
        meaning=OBI["0000424"])
    nanostring = PermissibleValue(
        text="nanostring",
        description="NanoString nCounter gene expression assay",
        meaning=OBI["0002142"])
    northern_blot = PermissibleValue(
        text="northern_blot",
        description="Northern blot for RNA detection",
        meaning=OBI["0000822"])
    in_situ_hybridization = PermissibleValue(
        text="in_situ_hybridization",
        description="In situ hybridization (ISH, FISH, RNAscope)",
        meaning=OBI["0001686"])
    western_blot = PermissibleValue(
        text="western_blot",
        description="Western blot (immunoblot) for protein detection",
        meaning=OBI["0000714"])
    elisa = PermissibleValue(
        text="elisa",
        description="Enzyme-linked immunosorbent assay",
        meaning=OBI["0000661"])
    immunohistochemistry = PermissibleValue(
        text="immunohistochemistry",
        description="Immunohistochemistry on tissue sections",
        meaning=OBI["0001986"])
    immunofluorescence = PermissibleValue(
        text="immunofluorescence",
        description="Immunofluorescence staining",
        meaning=OBI["0001501"])
    flow_cytometry = PermissibleValue(
        text="flow_cytometry",
        description="Flow cytometry for protein expression",
        meaning=OBI["0000916"])
    mass_spectrometry = PermissibleValue(
        text="mass_spectrometry",
        description="Mass spectrometry-based proteomics",
        meaning=OBI["0000470"])
    immunoprecipitation = PermissibleValue(
        text="immunoprecipitation",
        description="Immunoprecipitation followed by detection",
        meaning=OBI["0000928"])
    luminex = PermissibleValue(
        text="luminex",
        description="Luminex multiplex bead-based assay",
        meaning=OBI["0001632"])
    other = PermissibleValue(
        text="other",
        description="Other assay method not listed")

    _defn = EnumDefinition(
        name="ExpressionAssayMethodEnum",
        description="""Methods used to measure gene or protein expression. Includes transcriptomic, proteomic, and imaging-based approaches.""",
    )

class BiologicalOrganizationLevelEnum(EnumDefinitionImpl):
    """
    Levels of biological organization
    """
    molecular = PermissibleValue(
        text="molecular",
        description="Molecular level",
        meaning=EFO["0001432"])
    cellular = PermissibleValue(
        text="cellular",
        description="Cellular level",
        meaning=CL["0000000"])
    tissue = PermissibleValue(
        text="tissue",
        description="Tissue level",
        meaning=UBERON["0000479"])
    organ = PermissibleValue(
        text="organ",
        description="Organ level",
        meaning=UBERON["0000062"])
    organism = PermissibleValue(
        text="organism",
        description="Organism level",
        meaning=UBERON["0000468"])
    population = PermissibleValue(
        text="population",
        description="Population level")

    _defn = EnumDefinition(
        name="BiologicalOrganizationLevelEnum",
        description="Levels of biological organization",
    )

class StudyTypeEnum(EnumDefinitionImpl):
    """
    Types of research studies
    """
    cohort = PermissibleValue(
        text="cohort",
        description="Cohort study",
        meaning=EFO["0001444"])
    cross_sectional = PermissibleValue(
        text="cross_sectional",
        description="Cross-sectional study",
        meaning=EFO["0001745"])
    case_control = PermissibleValue(
        text="case_control",
        description="Case-control study",
        meaning=EFO["0001427"])
    randomized_controlled_trial = PermissibleValue(
        text="randomized_controlled_trial",
        description="Randomized controlled trial",
        meaning=EFO["0001427"])
    survey = PermissibleValue(
        text="survey",
        description="Survey")
    gwas = PermissibleValue(
        text="gwas",
        description="Genome-wide association study",
        meaning=EFO["0000508"])
    other = PermissibleValue(
        text="other",
        description="Other study type")

    _defn = EnumDefinition(
        name="StudyTypeEnum",
        description="Types of research studies",
    )

class SexEnum(EnumDefinitionImpl):
    """
    Biological sex
    """
    male = PermissibleValue(
        text="male",
        description="Male",
        meaning=PATO["0000384"])
    female = PermissibleValue(
        text="female",
        description="Female",
        meaning=PATO["0000383"])
    unknown = PermissibleValue(
        text="unknown",
        description="Unknown")

    _defn = EnumDefinition(
        name="SexEnum",
        description="Biological sex",
    )

class SampleTypeEnum(EnumDefinitionImpl):
    """
    Types of biological and environmental samples
    """
    blood = PermissibleValue(
        text="blood",
        description="Blood sample")
    urine = PermissibleValue(
        text="urine",
        description="Urine sample")
    serum = PermissibleValue(
        text="serum",
        description="Serum sample")
    plasma = PermissibleValue(
        text="plasma",
        description="Plasma sample")
    tissue = PermissibleValue(
        text="tissue",
        description="Tissue sample")
    saliva = PermissibleValue(
        text="saliva",
        description="Saliva sample")
    hair = PermissibleValue(
        text="hair",
        description="Hair sample")
    nail = PermissibleValue(
        text="nail",
        description="Nail sample")
    air = PermissibleValue(
        text="air",
        description="Air sample (environmental)")
    water = PermissibleValue(
        text="water",
        description="Water sample (environmental)")
    soil = PermissibleValue(
        text="soil",
        description="Soil sample (environmental)")
    other = PermissibleValue(
        text="other",
        description="Other sample type")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
        description="Types of biological and environmental samples",
    )

class SummaryStatisticEnum(EnumDefinitionImpl):
    """
    Types of summary statistics
    """
    mean = PermissibleValue(
        text="mean",
        description="Arithmetic mean")
    median = PermissibleValue(
        text="median",
        description="Median")
    mode = PermissibleValue(
        text="mode",
        description="Mode")
    percentile = PermissibleValue(
        text="percentile",
        description="Percentile")
    standard_deviation = PermissibleValue(
        text="standard_deviation",
        description="Standard deviation")
    variance = PermissibleValue(
        text="variance",
        description="Variance")
    range = PermissibleValue(
        text="range",
        description="Range")
    interquartile_range = PermissibleValue(
        text="interquartile_range",
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
    FEV1_FEC_ratio = PermissibleValue(
        text="FEV1_FEC_ratio",
        description="Ratio of FEV1 to FVC (Tiffeneau-Pinelli index)",
        meaning=NCIT["C120835"])
    FEF25_75 = PermissibleValue(
        text="FEF25_75",
        description="Forced expiratory flow at 25-75% of FVC",
        meaning=NCIT["C38085"])
    peak_expiratory_flow = PermissibleValue(
        text="peak_expiratory_flow",
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
    bronchodilator_response = PermissibleValue(
        text="bronchodilator_response",
        description="Change in lung function after bronchodilator administration")
    lung_function_decline_rate = PermissibleValue(
        text="lung_function_decline_rate",
        description="Rate of decline in lung function over time")
    ciliary_beat_frequency = PermissibleValue(
        text="ciliary_beat_frequency",
        description="Frequency of ciliary beating in Hz",
        meaning=GO["0003341"])
    ciliary_active_area_percentage = PermissibleValue(
        text="ciliary_active_area_percentage",
        description="Percentage of epithelial surface with active cilia")
    cilia_per_cell = PermissibleValue(
        text="cilia_per_cell",
        description="Number of cilia per epithelial cell")
    cilia_length = PermissibleValue(
        text="cilia_length",
        description="Length of cilia in micrometers")
    percentage_ciliated_cells = PermissibleValue(
        text="percentage_ciliated_cells",
        description="Percentage of cells that are ciliated")
    asl_height = PermissibleValue(
        text="asl_height",
        description="Airway surface liquid height in micrometers")
    periciliary_layer_depth = PermissibleValue(
        text="periciliary_layer_depth",
        description="Depth of periciliary liquid layer (reduced in disease)")
    mucus_layer_thickness = PermissibleValue(
        text="mucus_layer_thickness",
        description="Thickness of the mucus gel layer")
    mucociliary_transport_rate = PermissibleValue(
        text="mucociliary_transport_rate",
        description="Rate of mucociliary transport (mm/min)",
        meaning=GO["0120197"])
    mucociliary_directionality = PermissibleValue(
        text="mucociliary_directionality",
        description="Directionality and coordination of mucociliary transport")
    particle_clearance_rate = PermissibleValue(
        text="particle_clearance_rate",
        description="Rate of particle clearance from airways")
    goblet_cell_count = PermissibleValue(
        text="goblet_cell_count",
        description="Number or percentage of goblet cells",
        meaning=CL["0000160"])
    goblet_to_ciliated_ratio = PermissibleValue(
        text="goblet_to_ciliated_ratio",
        description="Ratio of goblet cells to ciliated cells")
    mucin_protein_concentration = PermissibleValue(
        text="mucin_protein_concentration",
        description="Concentration of secreted mucin protein")
    mucus_viscosity = PermissibleValue(
        text="mucus_viscosity",
        description="Viscosity of airway mucus")
    CFTR_chloride_secretion = PermissibleValue(
        text="CFTR_chloride_secretion",
        description="CFTR-mediated chloride secretory current")
    inhibitor_sensitive_current = PermissibleValue(
        text="inhibitor_sensitive_current",
        description="Current sensitive to CFTR inhibitors (e.g., CFTRinh-172)")
    sweat_chloride_concentration = PermissibleValue(
        text="sweat_chloride_concentration",
        description="Chloride concentration in sweat (CF diagnostic)")
    reactive_oxygen_species = PermissibleValue(
        text="reactive_oxygen_species",
        description="Reactive oxygen species (ROS) level",
        meaning=CHEBI["26523"])
    lipid_peroxidation = PermissibleValue(
        text="lipid_peroxidation",
        description="Lipid peroxidation markers (MDA, 8-isoprostane)")
    protein_carbonyls = PermissibleValue(
        text="protein_carbonyls",
        description="Protein carbonyl content (protein oxidation marker)")
    DNA_8ohdg = PermissibleValue(
        text="DNA_8ohdg",
        description="8-hydroxydeoxyguanosine (DNA oxidative damage marker)")
    glutathione_ratio = PermissibleValue(
        text="glutathione_ratio",
        description="GSH/GSSG ratio (antioxidant capacity)")
    superoxide_dismutase_activity = PermissibleValue(
        text="superoxide_dismutase_activity",
        description="Superoxide dismutase (SOD) enzyme activity")
    catalase_activity = PermissibleValue(
        text="catalase_activity",
        description="Catalase enzyme activity")
    glutathione_peroxidase_activity = PermissibleValue(
        text="glutathione_peroxidase_activity",
        description="Glutathione peroxidase (GPx) activity")
    total_antioxidant_capacity = PermissibleValue(
        text="total_antioxidant_capacity",
        description="Total antioxidant capacity of sample")
    TEER = PermissibleValue(
        text="TEER",
        description="Transepithelial electrical resistance")
    paracellular_permeability = PermissibleValue(
        text="paracellular_permeability",
        description="Paracellular permeability coefficient")
    IL6_level = PermissibleValue(
        text="IL6_level",
        description="Interleukin-6 concentration",
        meaning=NCIT["C20487"])
    IL8_level = PermissibleValue(
        text="IL8_level",
        description="Interleukin-8 (CXCL8) concentration",
        meaning=NCIT["C20506"])
    IL13_level = PermissibleValue(
        text="IL13_level",
        description="Interleukin-13 concentration",
        meaning=NCIT["C20497"])
    TNF_alpha_level = PermissibleValue(
        text="TNF_alpha_level",
        description="Tumor necrosis factor alpha concentration",
        meaning=NCIT["C20535"])
    neutrophil_percentage = PermissibleValue(
        text="neutrophil_percentage",
        description="Percentage of neutrophils in BALF or sputum")
    eosinophil_percentage = PermissibleValue(
        text="eosinophil_percentage",
        description="Percentage of eosinophils in BALF or sputum")
    macrophage_percentage = PermissibleValue(
        text="macrophage_percentage",
        description="Percentage of macrophages in BALF or sputum")
    total_inflammatory_cell = PermissibleValue(
        text="total_inflammatory_cell",
        description="Total inflammatory cell count")
    LDH_release = PermissibleValue(
        text="LDH_release",
        description="Lactate dehydrogenase release (cell damage marker)")
    cell_viability = PermissibleValue(
        text="cell_viability",
        description="Cell viability percentage")
    mtt_reduction = PermissibleValue(
        text="mtt_reduction",
        description="MTT assay result (metabolic activity)")
    apoptosis_rate = PermissibleValue(
        text="apoptosis_rate",
        description="Rate of apoptotic cell death")
    gene_expression = PermissibleValue(
        text="gene_expression",
        description="""Gene expression level (mRNA). Use with GeneExpressionMeasurement class to specify target_gene, tissue_context, and assay_method.""")
    protein_expression = PermissibleValue(
        text="protein_expression",
        description="""Protein expression level. Use with ProteinExpressionMeasurement class to specify target_protein, tissue_context, and assay_method.""")
    protein_phosphorylation = PermissibleValue(
        text="protein_phosphorylation",
        description="""Protein phosphorylation level. Use with ProteinExpressionMeasurement class and specify phosphorylation_site (e.g., Y1068 for EGFR).""")
    protein_localization = PermissibleValue(
        text="protein_localization",
        description="""Protein subcellular localization (membrane, cytoplasm, nucleus). Use with ProteinExpressionMeasurement class.""")
    expression_ratio = PermissibleValue(
        text="expression_ratio",
        description="""Ratio of expression between two genes or proteins (e.g., MUC5AC/MUC5B ratio). Specify both targets in description.""")
    percentage_positive_cells = PermissibleValue(
        text="percentage_positive_cells",
        description="Percentage of cells positive for a marker (IHC, flow cytometry)")
    urinary_arsenic_level = PermissibleValue(
        text="urinary_arsenic_level",
        description="Urinary arsenic concentration")
    urinary_cotinine_level = PermissibleValue(
        text="urinary_cotinine_level",
        description="Urinary cotinine (tobacco exposure biomarker)")
    urinary_bpa_level = PermissibleValue(
        text="urinary_bpa_level",
        description="Urinary bisphenol A concentration")
    urinary_phthalate_metabolites = PermissibleValue(
        text="urinary_phthalate_metabolites",
        description="Urinary phthalate metabolite concentrations")
    pm2_5_exposure = PermissibleValue(
        text="pm2_5_exposure",
        description="Fine particulate matter (PM2.5) exposure level")
    ozone_exposure = PermissibleValue(
        text="ozone_exposure",
        description="Ozone exposure concentration")
    NO2_exposure = PermissibleValue(
        text="NO2_exposure",
        description="Nitrogen dioxide exposure concentration")
    polycyclic_aromatic_hydrocarbons = PermissibleValue(
        text="polycyclic_aromatic_hydrocarbons",
        description="PAH metabolite levels")
    body_mass_index = PermissibleValue(
        text="body_mass_index",
        description="Body mass index (BMI)",
        meaning=NCIT["C16358"])
    body_weight = PermissibleValue(
        text="body_weight",
        description="Body weight measurement",
        meaning=NCIT["C81328"])
    height = PermissibleValue(
        text="height",
        description="Height measurement",
        meaning=NCIT["C25347"])
    alpha_diversity = PermissibleValue(
        text="alpha_diversity",
        description="Microbiome alpha diversity metric")
    beta_diversity = PermissibleValue(
        text="beta_diversity",
        description="Microbiome beta diversity metric")
    bacterial_load = PermissibleValue(
        text="bacterial_load",
        description="Total bacterial load (CFU or 16S copies)")
    other = PermissibleValue(
        text="other",
        description="Other measurement type not listed")

    _defn = EnumDefinition(
        name="MeasurementTypeEnum",
        description="""Types of measurements and observations for outcomes research, with emphasis on respiratory health and environmental toxicant effects.""",
    )

class RelationshipToHouseholdHeadEnum(EnumDefinitionImpl):
    """
    Relationship of a person to the household head (householder) in census data. Based on PUMS RELP variable coding.
    """
    householder = PermissibleValue(
        text="householder",
        description="Reference person (head of household)")
    spouse = PermissibleValue(
        text="spouse",
        description="Husband or wife of the householder")
    child = PermissibleValue(
        text="child",
        description="Biological, adopted, or stepchild of the householder")
    other_relative = PermissibleValue(
        text="other_relative",
        description="Other relative of the householder (parent, sibling, grandchild, etc.)")
    nonrelative = PermissibleValue(
        text="nonrelative",
        description="Non-relative of the householder (roommate, boarder, etc.)")
    foster_child = PermissibleValue(
        text="foster_child",
        description="Foster child")
    foster_parent = PermissibleValue(
        text="foster_parent",
        description="Foster parent")
    other_nonrelative = PermissibleValue(
        text="other_nonrelative",
        description="Other non-relative")

    _defn = EnumDefinition(
        name="RelationshipToHouseholdHeadEnum",
        description="""Relationship of a person to the household head (householder) in census data. Based on PUMS RELP variable coding.""",
    )

class EnvironmentalMeasurementTypeEnum(EnumDefinitionImpl):
    """
    Types of environmental conditions measured for cell culture systems. Used to constrain observation_type in
    EnvironmentalMeasurement.
    """
    co2_percentage = PermissibleValue(
        text="co2_percentage",
        description="Carbon dioxide percentage in incubator atmosphere")
    o2_percentage = PermissibleValue(
        text="o2_percentage",
        description="Oxygen percentage in incubator (for hypoxic cultures)")
    temperature = PermissibleValue(
        text="temperature",
        description="Incubator or culture temperature",
        meaning=PATO["0000146"])
    humidity = PermissibleValue(
        text="humidity",
        description="Relative humidity in incubator",
        meaning=PATO["0015009"])
    nitrogen_balance = PermissibleValue(
        text="nitrogen_balance",
        description="Nitrogen percentage in atmosphere")
    ph = PermissibleValue(
        text="ph",
        description="pH of culture medium",
        meaning=PATO["0001842"])

    _defn = EnumDefinition(
        name="EnvironmentalMeasurementTypeEnum",
        description="""Types of environmental conditions measured for cell culture systems. Used to constrain observation_type in EnvironmentalMeasurement.""",
    )

class MechanicalMeasurementTypeEnum(EnumDefinitionImpl):
    """
    Types of mechanical stimulation parameters for advanced culture systems like organ-on-chip and microphysiological
    systems. Used to constrain observation_type in MechanicalMeasurement.
    """
    stretch_frequency = PermissibleValue(
        text="stretch_frequency",
        description="Frequency of cyclic mechanical stretch (Hz)")
    stretch_amplitude = PermissibleValue(
        text="stretch_amplitude",
        description="Amplitude of mechanical stretch as percentage of original length")
    shear_stress = PermissibleValue(
        text="shear_stress",
        description="Fluid shear stress applied to cells (dyn/cm2 or Pa)")
    flow_rate = PermissibleValue(
        text="flow_rate",
        description="Fluid flow rate in microfluidic or perfusion systems")
    perfusion_rate = PermissibleValue(
        text="perfusion_rate",
        description="Media perfusion rate for continuous culture systems")
    pressure = PermissibleValue(
        text="pressure",
        description="Hydrostatic or pneumatic pressure",
        meaning=PATO["0001025"])

    _defn = EnumDefinition(
        name="MechanicalMeasurementTypeEnum",
        description="""Types of mechanical stimulation parameters for advanced culture systems like organ-on-chip and microphysiological systems. Used to constrain observation_type in MechanicalMeasurement.""",
    )

class MembranePropertyTypeEnum(EnumDefinitionImpl):
    """
    Types of membrane properties measured for transwell, ALI, and organ-on-chip culture systems. Used to constrain
    observation_type in MembranePropertyMeasurement.
    """
    pore_size = PermissibleValue(
        text="pore_size",
        description="Diameter of membrane pores (typically in micrometers)")
    pore_density = PermissibleValue(
        text="pore_density",
        description="Number of pores per unit area")
    thickness = PermissibleValue(
        text="thickness",
        description="Membrane thickness",
        meaning=PATO["0000915"])
    surface_area = PermissibleValue(
        text="surface_area",
        description="Total membrane surface area")
    teer = PermissibleValue(
        text="teer",
        description="Transepithelial electrical resistance")

    _defn = EnumDefinition(
        name="MembranePropertyTypeEnum",
        description="""Types of membrane properties measured for transwell, ALI, and organ-on-chip culture systems. Used to constrain observation_type in MembranePropertyMeasurement.""",
    )

class CellCultureGrowthModeEnum(EnumDefinitionImpl):
    """
    Cell culture growth modes including traditional and advanced systems. Based on CLO cell culture growth mode terms.
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
        description="Cells cultured at interface between air and liquid medium (ALI)",
        meaning=OBI["0600047"])
    three_dimensional = PermissibleValue(
        text="three_dimensional",
        description="Cells grown in 3D matrix or scaffold")
    organoid = PermissibleValue(
        text="organoid",
        description="Self-organizing 3D tissue culture from stem cells")
    spheroid = PermissibleValue(
        text="spheroid",
        description="Spherical cellular aggregates formed by self-aggregation")

    _defn = EnumDefinition(
        name="CellCultureGrowthModeEnum",
        description="""Cell culture growth modes including traditional and advanced systems. Based on CLO cell culture growth mode terms.""",
    )

class SubstrateTypeEnum(EnumDefinitionImpl):
    """
    Types of cell culture substrates and surfaces. Includes traditional and advanced substrate materials.
    """
    plastic = PermissibleValue(
        text="plastic",
        description="Standard tissue culture-treated plastic")
    collagen_coated = PermissibleValue(
        text="collagen_coated",
        description="Collagen-coated surface for enhanced cell attachment")
    matrigel = PermissibleValue(
        text="matrigel",
        description="Basement membrane matrix (Matrigel/Geltrex)")
    fibronectin_coated = PermissibleValue(
        text="fibronectin_coated",
        description="Fibronectin-coated surface")
    laminin_coated = PermissibleValue(
        text="laminin_coated",
        description="Laminin-coated surface")
    transwell_insert = PermissibleValue(
        text="transwell_insert",
        description="Permeable support for air-liquid interface culture")
    hydrogel = PermissibleValue(
        text="hydrogel",
        description="Three-dimensional hydrogel matrix")
    glass = PermissibleValue(
        text="glass",
        description="Glass surface or coverslip")
    pdms = PermissibleValue(
        text="pdms",
        description="Polydimethylsiloxane (for microfluidics/organ-on-chip)")

    _defn = EnumDefinition(
        name="SubstrateTypeEnum",
        description="""Types of cell culture substrates and surfaces. Includes traditional and advanced substrate materials.""",
    )

class SupplementTypeEnum(EnumDefinitionImpl):
    """
    Categories of cell culture medium supplements and additives.
    """
    growth_factor = PermissibleValue(
        text="growth_factor",
        description="Proteins that stimulate cell growth, proliferation, and differentiation",
        meaning=CHEBI["23924"])
    antibiotic = PermissibleValue(
        text="antibiotic",
        description="Antimicrobial substances used to prevent bacterial contamination",
        meaning=CHEBI["33281"])
    antifungal = PermissibleValue(
        text="antifungal",
        description="Antifungal agents to prevent fungal contamination",
        meaning=CHEBI["35718"])
    hormone = PermissibleValue(
        text="hormone",
        description="Signaling molecules that regulate cell physiology",
        meaning=CHEBI["24621"])
    vitamin = PermissibleValue(
        text="vitamin",
        description="Organic compounds essential for normal growth and nutrition",
        meaning=CHEBI["33229"])
    amino_acid = PermissibleValue(
        text="amino_acid",
        description="Amino acid supplements for protein synthesis",
        meaning=CHEBI["33709"])
    cytokine = PermissibleValue(
        text="cytokine",
        description="Small proteins important in cell signaling",
        meaning=CHEBI["63895"])
    buffer = PermissibleValue(
        text="buffer",
        description="pH buffering agents (HEPES, bicarbonate)",
        meaning=CHEBI["35225"])
    serum = PermissibleValue(
        text="serum",
        description="Serum supplements (FBS, human serum)")
    differentiation_factor = PermissibleValue(
        text="differentiation_factor",
        description="Factors that induce or maintain cell differentiation")

    _defn = EnumDefinition(
        name="SupplementTypeEnum",
        description="Categories of cell culture medium supplements and additives.",
    )

class CellLineModificationEnum(EnumDefinitionImpl):
    """
    Types of genetic or other modifications applied to cell lines.
    """
    none = PermissibleValue(
        text="none",
        description="Unmodified cell line")
    transfection = PermissibleValue(
        text="transfection",
        description="Transient or stable DNA/RNA transfection")
    viral_transduction = PermissibleValue(
        text="viral_transduction",
        description="Viral vector-mediated gene transfer (lentiviral, adenoviral, AAV)")
    crispr_knockout = PermissibleValue(
        text="crispr_knockout",
        description="CRISPR/Cas9-mediated gene knockout")
    crispr_knockin = PermissibleValue(
        text="crispr_knockin",
        description="CRISPR/Cas9-mediated gene knockin or base editing")
    rnai = PermissibleValue(
        text="rnai",
        description="RNA interference-mediated gene knockdown (siRNA, shRNA)")
    overexpression = PermissibleValue(
        text="overexpression",
        description="Stable or transient gene overexpression")
    reporter = PermissibleValue(
        text="reporter",
        description="Reporter gene insertion (GFP, luciferase, fluorescent proteins)")
    immortalization = PermissibleValue(
        text="immortalization",
        description="Immortalization of primary cells (hTERT, SV40, etc.)")

    _defn = EnumDefinition(
        name="CellLineModificationEnum",
        description="Types of genetic or other modifications applied to cell lines.",
    )

class ThreeDArchitectureEnum(EnumDefinitionImpl):
    """
    Types of three-dimensional cell culture architectures.
    """
    spheroid = PermissibleValue(
        text="spheroid",
        description="Spherical cellular aggregates formed by self-aggregation")
    organoid = PermissibleValue(
        text="organoid",
        description="Self-organizing 3D tissue derived from stem cells")
    scaffold_based = PermissibleValue(
        text="scaffold_based",
        description="Cells grown on/in synthetic or natural scaffolds")
    hydrogel_encapsulated = PermissibleValue(
        text="hydrogel_encapsulated",
        description="Cells encapsulated within hydrogel matrix")
    bioprinted = PermissibleValue(
        text="bioprinted",
        description="3D bioprinted tissue constructs")
    microcarrier = PermissibleValue(
        text="microcarrier",
        description="Cells grown on microcarrier beads in suspension")
    hanging_drop = PermissibleValue(
        text="hanging_drop",
        description="Spheroids formed using hanging drop method")

    _defn = EnumDefinition(
        name="ThreeDArchitectureEnum",
        description="Types of three-dimensional cell culture architectures.",
    )

class CoCultureConfigurationEnum(EnumDefinitionImpl):
    """
    Physical configurations for co-culture systems combining multiple cell types.
    """
    direct_contact = PermissibleValue(
        text="direct_contact",
        description="Cell types in direct physical contact on same surface")
    transwell = PermissibleValue(
        text="transwell",
        description="Cell types separated by permeable membrane insert")
    conditioned_medium = PermissibleValue(
        text="conditioned_medium",
        description="One cell type exposed to conditioned medium from another")
    microfluidic = PermissibleValue(
        text="microfluidic",
        description="Cell types in separate microfluidic compartments with shared media")
    spheroid_core_shell = PermissibleValue(
        text="spheroid_core_shell",
        description="One cell type forms core, another forms surrounding shell")
    patterned = PermissibleValue(
        text="patterned",
        description="Cell types arranged in defined spatial patterns")

    _defn = EnumDefinition(
        name="CoCultureConfigurationEnum",
        description="Physical configurations for co-culture systems combining multiple cell types.",
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

slots.person = Slot(uri=OWG.person, name="person", curie=OWG.curie('person'),
                   model_uri=OWG.person, domain=None, range=Optional[Union[str, PersonId]])

slots.enrollment_date = Slot(uri=OWG.enrollment_date, name="enrollment_date", curie=OWG.curie('enrollment_date'),
                   model_uri=OWG.enrollment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.withdrawal_date = Slot(uri=OWG.withdrawal_date, name="withdrawal_date", curie=OWG.curie('withdrawal_date'),
                   model_uri=OWG.withdrawal_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.study_arm = Slot(uri=OWG.study_arm, name="study_arm", curie=OWG.curie('study_arm'),
                   model_uri=OWG.study_arm, domain=None, range=Optional[str])

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

slots.federal_information_processing_standard_code = Slot(uri=OWG.federal_information_processing_standard_code, name="federal_information_processing_standard_code", curie=OWG.curie('federal_information_processing_standard_code'),
                   model_uri=OWG.federal_information_processing_standard_code, domain=None, range=Optional[str])

slots.state_federal_information_processing_standard_code = Slot(uri=OWG.state_federal_information_processing_standard_code, name="state_federal_information_processing_standard_code", curie=OWG.curie('state_federal_information_processing_standard_code'),
                   model_uri=OWG.state_federal_information_processing_standard_code, domain=None, range=Optional[str])

slots.county_federal_information_processing_standard_code = Slot(uri=OWG.county_federal_information_processing_standard_code, name="county_federal_information_processing_standard_code", curie=OWG.curie('county_federal_information_processing_standard_code'),
                   model_uri=OWG.county_federal_information_processing_standard_code, domain=None, range=Optional[str])

slots.census_tract_federal_information_processing_standard_code = Slot(uri=OWG.census_tract_federal_information_processing_standard_code, name="census_tract_federal_information_processing_standard_code", curie=OWG.curie('census_tract_federal_information_processing_standard_code'),
                   model_uri=OWG.census_tract_federal_information_processing_standard_code, domain=None, range=Optional[str])

slots.block_group_federal_information_processing_standard_code = Slot(uri=OWG.block_group_federal_information_processing_standard_code, name="block_group_federal_information_processing_standard_code", curie=OWG.curie('block_group_federal_information_processing_standard_code'),
                   model_uri=OWG.block_group_federal_information_processing_standard_code, domain=None, range=Optional[str])

slots.abbreviation = Slot(uri=OWG.abbreviation, name="abbreviation", curie=OWG.curie('abbreviation'),
                   model_uri=OWG.abbreviation, domain=None, range=Optional[str])

slots.counties = Slot(uri=OWG.counties, name="counties", curie=OWG.curie('counties'),
                   model_uri=OWG.counties, domain=None, range=Optional[Union[dict[Union[str, CountyId], Union[dict, County]], list[Union[dict, County]]]])

slots.public_use_microdata_areas = Slot(uri=OWG.public_use_microdata_areas, name="public_use_microdata_areas", curie=OWG.curie('public_use_microdata_areas'),
                   model_uri=OWG.public_use_microdata_areas, domain=None, range=Optional[Union[dict[Union[str, PublicUseMicrodataAreaId], Union[dict, PublicUseMicrodataArea]], list[Union[dict, PublicUseMicrodataArea]]]])

slots.census_tracts = Slot(uri=OWG.census_tracts, name="census_tracts", curie=OWG.curie('census_tracts'),
                   model_uri=OWG.census_tracts, domain=None, range=Optional[Union[dict[Union[str, CensusTractId], Union[dict, CensusTract]], list[Union[dict, CensusTract]]]])

slots.block_groups = Slot(uri=OWG.block_groups, name="block_groups", curie=OWG.curie('block_groups'),
                   model_uri=OWG.block_groups, domain=None, range=Optional[Union[dict[Union[str, BlockGroupId], Union[dict, BlockGroup]], list[Union[dict, BlockGroup]]]])

slots.households = Slot(uri=OWG.households, name="households", curie=OWG.curie('households'),
                   model_uri=OWG.households, domain=None, range=Optional[Union[dict[Union[str, HouseholdId], Union[dict, Household]], list[Union[dict, Household]]]])

slots.persons = Slot(uri=OWG.persons, name="persons", curie=OWG.curie('persons'),
                   model_uri=OWG.persons, domain=None, range=Optional[Union[dict[Union[str, PersonId], Union[dict, Person]], list[Union[dict, Person]]]])

slots.states = Slot(uri=OWG.states, name="states", curie=OWG.curie('states'),
                   model_uri=OWG.states, domain=None, range=Optional[Union[dict[Union[str, StateId], Union[dict, State]], list[Union[dict, State]]]])

slots.schools = Slot(uri=OWG.schools, name="schools", curie=OWG.curie('schools'),
                   model_uri=OWG.schools, domain=None, range=Optional[Union[dict[Union[str, SchoolId], Union[dict, School]], list[Union[dict, School]]]])

slots.serial_number = Slot(uri=OWG.serial_number, name="serial_number", curie=OWG.curie('serial_number'),
                   model_uri=OWG.serial_number, domain=None, range=Optional[str])

slots.household_identifier = Slot(uri=OWG.household_identifier, name="household_identifier", curie=OWG.curie('household_identifier'),
                   model_uri=OWG.household_identifier, domain=None, range=Optional[str])

slots.household_head_age = Slot(uri=OWG.household_head_age, name="household_head_age", curie=OWG.curie('household_head_age'),
                   model_uri=OWG.household_head_age, domain=None, range=Optional[int])

slots.household_income = Slot(uri=OWG.household_income, name="household_income", curie=OWG.curie('household_income'),
                   model_uri=OWG.household_income, domain=None, range=Optional[float])

slots.household_head_race = Slot(uri=OWG.household_head_race, name="household_head_race", curie=OWG.curie('household_head_race'),
                   model_uri=OWG.household_head_race, domain=None, range=Optional[str])

slots.household_size = Slot(uri=OWG.household_size, name="household_size", curie=OWG.curie('household_size'),
                   model_uri=OWG.household_size, domain=None, range=Optional[int])

slots.household_persons = Slot(uri=OWG.household_persons, name="household_persons", curie=OWG.curie('household_persons'),
                   model_uri=OWG.household_persons, domain=None, range=Optional[Union[dict[Union[str, PersonId], Union[dict, Person]], list[Union[dict, Person]]]])

slots.assigned_school = Slot(uri=OWG.assigned_school, name="assigned_school", curie=OWG.curie('assigned_school'),
                   model_uri=OWG.assigned_school, domain=None, range=Optional[Union[str, SchoolId]])

slots.person_order = Slot(uri=OWG.person_order, name="person_order", curie=OWG.curie('person_order'),
                   model_uri=OWG.person_order, domain=None, range=Optional[int])

slots.relationship_to_household_head = Slot(uri=OWG.relationship_to_household_head, name="relationship_to_household_head", curie=OWG.curie('relationship_to_household_head'),
                   model_uri=OWG.relationship_to_household_head, domain=None, range=Optional[Union[str, "RelationshipToHouseholdHeadEnum"]])

slots.race = Slot(uri=OWG.race, name="race", curie=OWG.curie('race'),
                   model_uri=OWG.race, domain=None, range=Optional[str])

slots.cell_line = Slot(uri=CLO['0000031'], name="cell_line", curie=CLO.curie('0000031'),
                   model_uri=OWG.cell_line, domain=None, range=Optional[Union[dict, CellLine]])

slots.cell_line_lineage = Slot(uri=OWG.cell_line_lineage, name="cell_line_lineage", curie=OWG.curie('cell_line_lineage'),
                   model_uri=OWG.cell_line_lineage, domain=None, range=Optional[str])

slots.cell_line_modification = Slot(uri=OWG.cell_line_modification, name="cell_line_modification", curie=OWG.curie('cell_line_modification'),
                   model_uri=OWG.cell_line_modification, domain=None, range=Optional[Union[str, "CellLineModificationEnum"]])

slots.induced_pluripotent_stem_cell_line = Slot(uri=OWG.induced_pluripotent_stem_cell_line, name="induced_pluripotent_stem_cell_line", curie=OWG.curie('induced_pluripotent_stem_cell_line'),
                   model_uri=OWG.induced_pluripotent_stem_cell_line, domain=None, range=Optional[Union[bool, Bool]])

slots.primary_cultured_cell = Slot(uri=OWG.primary_cultured_cell, name="primary_cultured_cell", curie=OWG.curie('primary_cultured_cell'),
                   model_uri=OWG.primary_cultured_cell, domain=None, range=Optional[Union[dict, CellType]])

slots.cell_culture_type = Slot(uri=EFO['0000324'], name="cell_culture_type", curie=EFO.curie('0000324'),
                   model_uri=OWG.cell_culture_type, domain=None, range=Optional[Union[dict, CellType]])

slots.anatomical_origin = Slot(uri=UBERON['0001062'], name="anatomical_origin", curie=UBERON.curie('0001062'),
                   model_uri=OWG.anatomical_origin, domain=None, range=Optional[Union[dict, AnatomicalEntity]])

slots.model_species = Slot(uri=OWG.model_species, name="model_species", curie=OWG.curie('model_species'),
                   model_uri=OWG.model_species, domain=None, range=Optional[Union[dict, Organism]])

slots.cell_culture_growth_mode = Slot(uri=OWG.cell_culture_growth_mode, name="cell_culture_growth_mode", curie=OWG.curie('cell_culture_growth_mode'),
                   model_uri=OWG.cell_culture_growth_mode, domain=None, range=Optional[Union[str, "CellCultureGrowthModeEnum"]])

slots.substrate_type = Slot(uri=OWG.substrate_type, name="substrate_type", curie=OWG.curie('substrate_type'),
                   model_uri=OWG.substrate_type, domain=None, range=Optional[Union[str, "SubstrateTypeEnum"]])

slots.culture_conditions = Slot(uri=OWG.culture_conditions, name="culture_conditions", curie=OWG.curie('culture_conditions'),
                   model_uri=OWG.culture_conditions, domain=None, range=Optional[Union[dict, CellCultureConditions]])

slots.culture_media = Slot(uri=OWG.culture_media, name="culture_media", curie=OWG.curie('culture_media'),
                   model_uri=OWG.culture_media, domain=None, range=Optional[Union[dict, CellCultureMedium]])

slots.environmental_measurements = Slot(uri=OWG.environmental_measurements, name="environmental_measurements", curie=OWG.curie('environmental_measurements'),
                   model_uri=OWG.environmental_measurements, domain=None, range=Optional[Union[dict[Union[str, EnvironmentalMeasurementId], Union[dict, EnvironmentalMeasurement]], list[Union[dict, EnvironmentalMeasurement]]]])

slots.mechanical_measurements = Slot(uri=OWG.mechanical_measurements, name="mechanical_measurements", curie=OWG.curie('mechanical_measurements'),
                   model_uri=OWG.mechanical_measurements, domain=None, range=Optional[Union[dict[Union[str, MechanicalMeasurementId], Union[dict, MechanicalMeasurement]], list[Union[dict, MechanicalMeasurement]]]])

slots.membrane_properties = Slot(uri=OWG.membrane_properties, name="membrane_properties", curie=OWG.curie('membrane_properties'),
                   model_uri=OWG.membrane_properties, domain=None, range=Optional[Union[dict[Union[str, MembranePropertyMeasurementId], Union[dict, MembranePropertyMeasurement]], list[Union[dict, MembranePropertyMeasurement]]]])

slots.three_d_architecture = Slot(uri=OWG.three_d_architecture, name="three_d_architecture", curie=OWG.curie('three_d_architecture'),
                   model_uri=OWG.three_d_architecture, domain=None, range=Optional[Union[str, "ThreeDArchitectureEnum"]])

slots.matrix_composition = Slot(uri=OWG.matrix_composition, name="matrix_composition", curie=OWG.curie('matrix_composition'),
                   model_uri=OWG.matrix_composition, domain=None, range=Optional[str])

slots.size_range = Slot(uri=OWG.size_range, name="size_range", curie=OWG.curie('size_range'),
                   model_uri=OWG.size_range, domain=None, range=Optional[Union[dict, QuantityRange]])

slots.organoid_type = Slot(uri=OWG.organoid_type, name="organoid_type", curie=OWG.curie('organoid_type'),
                   model_uri=OWG.organoid_type, domain=None, range=Optional[str])

slots.coculture_configuration = Slot(uri=OWG.coculture_configuration, name="coculture_configuration", curie=OWG.curie('coculture_configuration'),
                   model_uri=OWG.coculture_configuration, domain=None, range=Optional[Union[str, "CoCultureConfigurationEnum"]])

slots.cell_type_ratios = Slot(uri=OWG.cell_type_ratios, name="cell_type_ratios", curie=OWG.curie('cell_type_ratios'),
                   model_uri=OWG.cell_type_ratios, domain=None, range=Optional[Union[str, list[str]]])

slots.membrane_material = Slot(uri=OWG.membrane_material, name="membrane_material", curie=OWG.curie('membrane_material'),
                   model_uri=OWG.membrane_material, domain=None, range=Optional[str])

slots.coating = Slot(uri=OWG.coating, name="coating", curie=OWG.curie('coating'),
                   model_uri=OWG.coating, domain=None, range=Optional[str])

slots.confluence_level = Slot(uri=OWG.confluence_level, name="confluence_level", curie=OWG.curie('confluence_level'),
                   model_uri=OWG.confluence_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.seeding_density = Slot(uri=OWG.seeding_density, name="seeding_density", curie=OWG.curie('seeding_density'),
                   model_uri=OWG.seeding_density, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.passage_number = Slot(uri=OWG.passage_number, name="passage_number", curie=OWG.curie('passage_number'),
                   model_uri=OWG.passage_number, domain=None, range=Optional[int])

slots.days_at_air_liquid_interface = Slot(uri=OWG.days_at_air_liquid_interface, name="days_at_air_liquid_interface", curie=OWG.curie('days_at_air_liquid_interface'),
                   model_uri=OWG.days_at_air_liquid_interface, domain=None, range=Optional[int])

slots.donor_count = Slot(uri=OWG.donor_count, name="donor_count", curie=OWG.curie('donor_count'),
                   model_uri=OWG.donor_count, domain=None, range=Optional[int])

slots.replicates_per_donor = Slot(uri=OWG.replicates_per_donor, name="replicates_per_donor", curie=OWG.curie('replicates_per_donor'),
                   model_uri=OWG.replicates_per_donor, domain=None, range=Optional[int])

slots.base_medium = Slot(uri=OWG.base_medium, name="base_medium", curie=OWG.curie('base_medium'),
                   model_uri=OWG.base_medium, domain=None, range=Optional[str])

slots.serum_type = Slot(uri=OWG.serum_type, name="serum_type", curie=OWG.curie('serum_type'),
                   model_uri=OWG.serum_type, domain=None, range=Optional[str])

slots.serum_concentration = Slot(uri=OWG.serum_concentration, name="serum_concentration", curie=OWG.curie('serum_concentration'),
                   model_uri=OWG.serum_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.supplements = Slot(uri=OWG.supplements, name="supplements", curie=OWG.curie('supplements'),
                   model_uri=OWG.supplements, domain=None, range=Optional[Union[dict[Union[str, MediumSupplementId], Union[dict, MediumSupplement]], list[Union[dict, MediumSupplement]]]])

slots.osmolality = Slot(uri=OWG.osmolality, name="osmolality", curie=OWG.curie('osmolality'),
                   model_uri=OWG.osmolality, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.manufacturer = Slot(uri=OWG.manufacturer, name="manufacturer", curie=OWG.curie('manufacturer'),
                   model_uri=OWG.manufacturer, domain=None, range=Optional[str])

slots.catalog_number = Slot(uri=OWG.catalog_number, name="catalog_number", curie=OWG.curie('catalog_number'),
                   model_uri=OWG.catalog_number, domain=None, range=Optional[str])

slots.lot_number = Slot(uri=OWG.lot_number, name="lot_number", curie=OWG.curie('lot_number'),
                   model_uri=OWG.lot_number, domain=None, range=Optional[str])

slots.preparation_date = Slot(uri=OWG.preparation_date, name="preparation_date", curie=OWG.curie('preparation_date'),
                   model_uri=OWG.preparation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.supplement_type = Slot(uri=OWG.supplement_type, name="supplement_type", curie=OWG.curie('supplement_type'),
                   model_uri=OWG.supplement_type, domain=None, range=Optional[Union[str, "SupplementTypeEnum"]])

slots.supplement_entity = Slot(uri=OWG.supplement_entity, name="supplement_entity", curie=OWG.curie('supplement_entity'),
                   model_uri=OWG.supplement_entity, domain=None, range=Optional[Union[dict, ChemicalEntity]])

slots.concentration = Slot(uri=OWG.concentration, name="concentration", curie=OWG.curie('concentration'),
                   model_uri=OWG.concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.tissue_origin = Slot(uri=OWG.tissue_origin, name="tissue_origin", curie=OWG.curie('tissue_origin'),
                   model_uri=OWG.tissue_origin, domain=None, range=Optional[Union[dict, AnatomicalEntity]])

slots.disease_state = Slot(uri=OWG.disease_state, name="disease_state", curie=OWG.curie('disease_state'),
                   model_uri=OWG.disease_state, domain=None, range=Optional[Union[dict, Disease]])

slots.supplier = Slot(uri=OWG.supplier, name="supplier", curie=OWG.curie('supplier'),
                   model_uri=OWG.supplier, domain=None, range=Optional[str])

slots.authentication_method = Slot(uri=OWG.authentication_method, name="authentication_method", curie=OWG.curie('authentication_method'),
                   model_uri=OWG.authentication_method, domain=None, range=Optional[str])

slots.mycoplasma_status = Slot(uri=OWG.mycoplasma_status, name="mycoplasma_status", curie=OWG.curie('mycoplasma_status'),
                   model_uri=OWG.mycoplasma_status, domain=None, range=Optional[str])

slots.cellular_systems = Slot(uri=OWG.cellular_systems, name="cellular_systems", curie=OWG.curie('cellular_systems'),
                   model_uri=OWG.cellular_systems, domain=None, range=Optional[Union[dict[Union[str, CellularSystemId], Union[dict, CellularSystem]], list[Union[dict, CellularSystem]]]])

slots.two_d_cell_cultures = Slot(uri=OWG.two_d_cell_cultures, name="two_d_cell_cultures", curie=OWG.curie('two_d_cell_cultures'),
                   model_uri=OWG.two_d_cell_cultures, domain=None, range=Optional[Union[dict[Union[str, TwoDCellCultureId], Union[dict, TwoDCellCulture]], list[Union[dict, TwoDCellCulture]]]])

slots.three_d_cell_cultures = Slot(uri=OWG.three_d_cell_cultures, name="three_d_cell_cultures", curie=OWG.curie('three_d_cell_cultures'),
                   model_uri=OWG.three_d_cell_cultures, domain=None, range=Optional[Union[dict[Union[str, ThreeDCellCultureId], Union[dict, ThreeDCellCulture]], list[Union[dict, ThreeDCellCulture]]]])

slots.co_cultures = Slot(uri=OWG.co_cultures, name="co_cultures", curie=OWG.curie('co_cultures'),
                   model_uri=OWG.co_cultures, domain=None, range=Optional[Union[dict[Union[str, CoCultureId], Union[dict, CoCulture]], list[Union[dict, CoCulture]]]])

slots.cell_lines = Slot(uri=OWG.cell_lines, name="cell_lines", curie=OWG.curie('cell_lines'),
                   model_uri=OWG.cell_lines, domain=None, range=Optional[Union[dict[Union[str, CellLineId], Union[dict, CellLine]], list[Union[dict, CellLine]]]])

slots.quantityValue__unit = Slot(uri=OWG.unit, name="quantityValue__unit", curie=OWG.curie('unit'),
                   model_uri=OWG.quantityValue__unit, domain=None, range=Optional[Union[dict, Unit]])

slots.quantityValue__value = Slot(uri=OWG.value, name="quantityValue__value", curie=OWG.curie('value'),
                   model_uri=OWG.quantityValue__value, domain=None, range=Optional[str])

slots.quantityRange__lower_bound = Slot(uri=OWG.lower_bound, name="quantityRange__lower_bound", curie=OWG.curie('lower_bound'),
                   model_uri=OWG.quantityRange__lower_bound, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.quantityRange__upper_bound = Slot(uri=OWG.upper_bound, name="quantityRange__upper_bound", curie=OWG.curie('upper_bound'),
                   model_uri=OWG.quantityRange__upper_bound, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.Participant_age = Slot(uri=OWG.age, name="Participant_age", curie=OWG.curie('age'),
                   model_uri=OWG.Participant_age, domain=Participant, range=Optional[int])

slots.Participant_sex = Slot(uri=OWG.sex, name="Participant_sex", curie=OWG.curie('sex'),
                   model_uri=OWG.Participant_sex, domain=Participant, range=Optional[Union[str, "SexEnum"]])

slots.EnvironmentalMeasurement_observation_type = Slot(uri=OWG.observation_type, name="EnvironmentalMeasurement_observation_type", curie=OWG.curie('observation_type'),
                   model_uri=OWG.EnvironmentalMeasurement_observation_type, domain=EnvironmentalMeasurement, range=Optional[Union[str, "EnvironmentalMeasurementTypeEnum"]])

slots.MechanicalMeasurement_observation_type = Slot(uri=OWG.observation_type, name="MechanicalMeasurement_observation_type", curie=OWG.curie('observation_type'),
                   model_uri=OWG.MechanicalMeasurement_observation_type, domain=MechanicalMeasurement, range=Optional[Union[str, "MechanicalMeasurementTypeEnum"]])

slots.MembranePropertyMeasurement_observation_type = Slot(uri=OWG.observation_type, name="MembranePropertyMeasurement_observation_type", curie=OWG.curie('observation_type'),
                   model_uri=OWG.MembranePropertyMeasurement_observation_type, domain=MembranePropertyMeasurement, range=Optional[Union[str, "MembranePropertyTypeEnum"]])

slots.Person_age = Slot(uri=OWG.age, name="Person_age", curie=OWG.curie('age'),
                   model_uri=OWG.Person_age, domain=Person, range=Optional[int])

slots.Person_sex = Slot(uri=OWG.sex, name="Person_sex", curie=OWG.curie('sex'),
                   model_uri=OWG.Person_sex, domain=Person, range=Optional[Union[str, "SexEnum"]])
