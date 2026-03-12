"""Tests for the SOMA flattening pipeline.

Tests introspection, forward flatten, and round-trip unflatten.
"""

import tempfile
from pathlib import Path

import yaml

from soma.flatten.flatten import flatten_container, flatten_yaml_file
from soma.flatten.introspect import introspect_schema
from soma.flatten.unflatten import unflatten_rows, unflatten_to_container

SCHEMA_PATH = Path(__file__).parent.parent / "src" / "soma" / "schema" / "soma.yaml"
TEST_DATA_DIR = Path(__file__).parent / "data" / "valid"

# The 3 initial assay types
INITIAL_ASSAY_TYPES = [
    "CiliaryFunctionAssay",
    "CFTRFunctionAssay",
    "GeneExpressionAssay",
]


def _get_specs():
    """Generate specs for the 3 initial assay types."""
    return introspect_schema(SCHEMA_PATH, assay_types=INITIAL_ASSAY_TYPES)


class TestIntrospection:
    """Tests for schema introspection and spec generation."""

    def test_generates_specs_for_all_types(self):
        specs = _get_specs()
        assert len(specs) == 3
        for name in INITIAL_ASSAY_TYPES:
            assert name in specs

    def test_ciliary_spec_has_qv_slots(self):
        specs = _get_specs()
        spec = specs["CiliaryFunctionAssay"]
        qvs = spec["flatten_rules"]["quantity_values"]
        prefixes = {qv["prefix"] for qv in qvs}
        assert "beat_frequency_hz" in prefixes
        assert "active_area_percentage" in prefixes
        assert "cilia_length" in prefixes

    def test_ciliary_spec_has_polymorphic_subject(self):
        specs = _get_specs()
        spec = specs["CiliaryFunctionAssay"]
        poly = spec["flatten_rules"]["polymorphic"]
        assert len(poly) > 0
        variants = poly[0]["variants"]
        assert "CellularSystem" in variants
        assert "InVivoSubject" in variants

    def test_cftr_spec_has_assay_specific_scalars(self):
        specs = _get_specs()
        spec = specs["CFTRFunctionAssay"]
        scalars = spec["flatten_rules"]["scalars"]
        assert "stimulation_agent" in scalars
        assert "inhibitor_used" in scalars

    def test_gene_expression_spec_has_assay_specific_scalars(self):
        specs = _get_specs()
        spec = specs["GeneExpressionAssay"]
        scalars = spec["flatten_rules"]["scalars"]
        assert "target_gene" in scalars
        assert "gene_expression_method" in scalars

    def test_specs_write_to_disk(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            specs = introspect_schema(
                SCHEMA_PATH,
                assay_types=INITIAL_ASSAY_TYPES,
                output_dir=tmpdir,
            )
            yaml_files = list(Path(tmpdir).glob("*.flat.yaml"))
            assert len(yaml_files) == 3

            # Verify files are valid YAML
            for f in yaml_files:
                with open(f) as fh:
                    data = yaml.safe_load(fh)
                assert "source_class" in data
                assert "flatten_rules" in data

    def test_exposure_multivalued_rules(self):
        specs = _get_specs()
        for spec in specs.values():
            mvs = spec["flatten_rules"]["multivalued"]
            expand_rules = [m for m in mvs if m["strategy"] == "expand_rows"]
            assert len(expand_rules) == 1
            assert expand_rules[0]["path"] == "has_exposure_condition"


class TestFlatten:
    """Tests for forward flattening."""

    def test_flatten_ciliary_function(self):
        specs = _get_specs()
        spec = specs["CiliaryFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-ciliary_function.yaml", spec)

        # 2 assays, each with 0 or 1 exposure -> 2 rows
        assert len(rows) == 2

        # First row: in-vitro with CellularSystem
        row1 = rows[0]
        assert row1["id"] == "CILIARY:001"
        assert row1["beat_frequency_hz_value"] == "8.5"
        assert row1["beat_frequency_hz_unit"] == "hertz"
        assert row1["subject_type"] == "CellularSystem"
        assert row1["cell_culture_growth_mode"] == "air_liquid_interface"
        assert row1["exposure_agent"] == "ozone"
        assert row1["exposure_concentration_value"] == "200"

        # Second row: in-vivo with InVivoSubject
        row2 = rows[1]
        assert row2["id"] == "CILIARY:002"
        assert row2["subject_type"] == "InVivoSubject"
        assert row2["sex"] == "female"
        assert row2["age_value"] == "38"

    def test_flatten_cftr(self):
        specs = _get_specs()
        spec = specs["CFTRFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-cftr.yaml", spec)

        assert len(rows) == 1
        row = rows[0]
        assert row["id"] == "CFTR:001"
        assert row["cftr_chloride_secretion_value"] == "15.2"
        assert row["stimulation_agent"] == "forskolin 10 uM"
        assert row["inhibitor_used"] == "CFTRinh-172"
        assert "Ussing chamber" in row["follows_protocols"]

    def test_flatten_gene_expression(self):
        specs = _get_specs()
        spec = specs["GeneExpressionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-gene_expression.yaml", spec)

        assert len(rows) == 1
        row = rows[0]
        assert row["id"] == "GE:001"
        assert row["mrna_level_value"] == "3.5"
        assert row["target_gene"] == "PR:000006689"
        assert row["exposure_agent"] == "lipopolysaccharide"

    def test_qv_decomposition(self):
        """QuantityValue slots produce _value and _unit columns."""
        specs = _get_specs()
        spec = specs["CiliaryFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-ciliary_function.yaml", spec)

        row = rows[0]
        # Every QV slot should have both _value and _unit
        for qv in spec["flatten_rules"]["quantity_values"]:
            prefix = qv["prefix"]
            assert f"{prefix}_value" in row
            assert f"{prefix}_unit" in row

    def test_delimited_protocols(self):
        """Protocols are joined with delimiter."""
        specs = _get_specs()
        spec = specs["CFTRFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-cftr.yaml", spec)

        row = rows[0]
        protos = row["follows_protocols"]
        assert " | " in protos
        assert "Ussing chamber short-circuit current protocol" in protos
        assert "Tissue mounting and equilibration protocol" in protos

    def test_delimited_supplements(self):
        """Culture media supplements are joined with delimiter."""
        specs = _get_specs()
        spec = specs["CiliaryFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-ciliary_function.yaml", spec)

        row = rows[0]
        supps = row.get("study_subject_culture_media_supplements")
        assert supps is not None
        assert "Hydrocortisone" in supps
        assert "Heparin" in supps

    def test_no_assays_returns_empty(self):
        """If the container has no assays of the specified type, return empty."""
        specs = _get_specs()
        spec = specs["CFTRFunctionAssay"]
        rows = flatten_container({"some_other_slot": []}, spec)
        assert rows == []


class TestUnflatten:
    """Tests for reverse flattening (unflatten)."""

    def test_unflatten_preserves_assay_id(self):
        specs = _get_specs()
        spec = specs["CiliaryFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-ciliary_function.yaml", spec)
        assays = unflatten_rows(rows, spec)

        assert len(assays) == 2
        assert assays[0]["id"] == "CILIARY:001"
        assert assays[1]["id"] == "CILIARY:002"

    def test_unflatten_reconstructs_qv(self):
        specs = _get_specs()
        spec = specs["CiliaryFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-ciliary_function.yaml", spec)
        assays = unflatten_rows(rows, spec)

        output = assays[0]["has_specified_output"]
        bf = output["beat_frequency_hz"]
        assert bf["value"] == "8.5"
        assert bf["unit"]["name"] == "hertz"

    def test_unflatten_reconstructs_subject(self):
        specs = _get_specs()
        spec = specs["CiliaryFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-ciliary_function.yaml", spec)
        assays = unflatten_rows(rows, spec)

        subject = assays[0]["study_subject"]
        assert subject["subject_type"] == "CellularSystem"
        assert subject["cell_culture_growth_mode"] == "air_liquid_interface"
        assert subject["model_species"]["id"] == "NCBITaxon:9606"

    def test_unflatten_reconstructs_exposure(self):
        specs = _get_specs()
        spec = specs["CiliaryFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-ciliary_function.yaml", spec)
        assays = unflatten_rows(rows, spec)

        exposures = assays[0]["has_exposure_condition"]
        assert len(exposures) == 1
        assert exposures[0]["exposure_agent"]["name"] == "ozone"
        assert exposures[0]["exposure_concentration"]["value"] == "200"

    def test_unflatten_reconstructs_protocols(self):
        specs = _get_specs()
        spec = specs["CFTRFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-cftr.yaml", spec)
        assays = unflatten_rows(rows, spec)

        protos = assays[0]["follows_protocols"]
        assert len(protos) == 2
        names = [p["name"] for p in protos]
        assert "Ussing chamber short-circuit current protocol" in names

    def test_unflatten_to_container(self):
        specs = _get_specs()
        spec = specs["CiliaryFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-ciliary_function.yaml", spec)
        container = unflatten_to_container(rows, spec)

        assert "ciliary_function_assays" in container
        assert len(container["ciliary_function_assays"]) == 2

    def test_roundtrip_gene_expression(self):
        """Full round-trip: YAML -> flatten -> unflatten -> check."""
        specs = _get_specs()
        spec = specs["GeneExpressionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-gene_expression.yaml", spec)
        assays = unflatten_rows(rows, spec)

        assay = assays[0]
        assert assay["id"] == "GE:001"
        assert assay["target_gene"] == "PR:000006689"
        assert assay["has_specified_output"]["mrna_level"]["value"] == "3.5"
        assert assay["study_subject"]["subject_type"] == "CellularSystem"

    def test_invivo_subject_roundtrip(self):
        """Verify InVivoSubject polymorphic fields survive round-trip."""
        specs = _get_specs()
        spec = specs["CiliaryFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-ciliary_function.yaml", spec)
        assays = unflatten_rows(rows, spec)

        # Second assay is InVivoSubject
        subject = assays[1]["study_subject"]
        assert subject["subject_type"] == "InVivoSubject"
        assert subject["sex"] == "female"
        assert subject["age"]["value"] == "38"
        assert subject["age"]["unit"]["name"] == "year"


class TestExcelIO:
    """Tests for Excel read/write."""

    def test_write_and_read_excel(self):
        from soma.flatten.excel_io import read_excel, write_excel

        specs = _get_specs()
        spec = specs["CiliaryFunctionAssay"]
        rows = flatten_yaml_file(TEST_DATA_DIR / "Container-ciliary_function.yaml", spec)

        with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as f:
            tmpfile = f.name

        write_excel({"CiliaryFunctionAssay": rows}, tmpfile)
        sheets = read_excel(tmpfile)

        assert "CiliaryFunctionAssay" in sheets
        read_rows = sheets["CiliaryFunctionAssay"]
        assert len(read_rows) == 2
        assert read_rows[0]["id"] == "CILIARY:001"
        assert str(read_rows[0]["beat_frequency_hz_value"]) == "8.5"

    def test_template_generation(self):
        from soma.flatten.excel_io import read_excel, write_template_excel

        specs = _get_specs()

        with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as f:
            tmpfile = f.name

        write_template_excel(specs, tmpfile)
        sheets = read_excel(tmpfile)

        assert len(sheets) == 3
        for name in INITIAL_ASSAY_TYPES:
            assert name in sheets
