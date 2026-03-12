"""CLI for SOMA schema flattening tools.

Commands:
    soma-flatten introspect   - Schema -> FlatteningSpec YAML
    soma-flatten gen-excel    - Generate empty Excel workbook template
    soma-flatten flatten      - Nested YAML -> flat Excel
    soma-flatten unflatten    - Flat Excel -> nested YAML
    soma-flatten validate     - Unflatten + validate against source schema
"""

from __future__ import annotations

from pathlib import Path

import click
import yaml

from soma.flatten.introspect import ASSAY_COLLECTION_SLOTS, introspect_schema

# Default paths relative to package
_PACKAGE_DIR = Path(__file__).parent
_SPECS_DIR = _PACKAGE_DIR / "specs"
_SCHEMA_DIR = _PACKAGE_DIR.parent / "schema"
_DEFAULT_SCHEMA = _SCHEMA_DIR / "soma.yaml"


def _load_specs(specs_dir: Path, assay_types: list[str] | None = None) -> dict:
    """Load flattening specs from YAML files."""
    specs = {}
    for spec_file in sorted(specs_dir.glob("*.flat.yaml")):
        with open(spec_file) as f:
            spec = yaml.safe_load(f)
        class_name = spec["source_class"]
        if assay_types is None or class_name in assay_types:
            specs[class_name] = spec
    return specs


@click.group()
def cli():
    """SOMA schema flattening tools for Excel data entry."""
    pass


@cli.command()
@click.option(
    "--schema", "-s",
    type=click.Path(exists=True),
    default=None,
    help="Path to soma.yaml schema file",
)
@click.option(
    "--output-dir", "-o",
    type=click.Path(),
    default=None,
    help="Output directory for spec YAML files",
)
@click.option(
    "--assay-type", "-a",
    multiple=True,
    help="Specific assay type(s) to introspect (default: all)",
)
def introspect(schema, output_dir, assay_type):
    """Introspect the SOMA schema and generate FlatteningSpec YAML files."""
    schema_path = Path(schema) if schema else _DEFAULT_SCHEMA
    out_dir = Path(output_dir) if output_dir else _SPECS_DIR
    types = list(assay_type) if assay_type else None

    click.echo(f"Introspecting schema: {schema_path}")
    specs = introspect_schema(schema_path, assay_types=types, output_dir=out_dir)

    for name in specs:
        click.echo(f"  Generated spec: {name}")
    click.echo(f"Wrote {len(specs)} specs to {out_dir}")


@cli.command("gen-excel")
@click.option(
    "--specs-dir", "-d",
    type=click.Path(exists=True),
    default=None,
    help="Directory containing FlatteningSpec YAML files",
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default="soma_template.xlsx",
    help="Output Excel file path",
)
@click.option(
    "--assay-type", "-a",
    multiple=True,
    help="Specific assay type(s) to include",
)
def gen_excel(specs_dir, output, assay_type):
    """Generate an empty Excel workbook template from FlatteningSpecs."""
    from soma.flatten.excel_io import write_template_excel

    specs_path = Path(specs_dir) if specs_dir else _SPECS_DIR
    types = list(assay_type) if assay_type else None
    specs = _load_specs(specs_path, types)

    if not specs:
        click.echo("No specs found. Run 'introspect' first.", err=True)
        raise SystemExit(1)

    out = write_template_excel(specs, output)
    click.echo(f"Template written to {out}")


@cli.command()
@click.argument("yaml_files", nargs=-1, type=click.Path(exists=True))
@click.option(
    "--specs-dir", "-d",
    type=click.Path(exists=True),
    default=None,
    help="Directory containing FlatteningSpec YAML files",
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default="soma_flat.xlsx",
    help="Output Excel file path",
)
@click.option(
    "--assay-type", "-a",
    multiple=True,
    help="Specific assay type(s) to flatten",
)
def flatten(yaml_files, specs_dir, output, assay_type):
    """Flatten nested YAML file(s) to a flat Excel workbook."""
    from soma.flatten.excel_io import write_excel
    from soma.flatten.flatten import flatten_yaml_file

    specs_path = Path(specs_dir) if specs_dir else _SPECS_DIR
    types = list(assay_type) if assay_type else None
    specs = _load_specs(specs_path, types)

    if not specs:
        click.echo("No specs found. Run 'introspect' first.", err=True)
        raise SystemExit(1)

    sheets_data: dict[str, list[dict]] = {}

    for yaml_file in yaml_files:
        for class_name, spec in specs.items():
            rows = flatten_yaml_file(yaml_file, spec)
            if rows:
                sheet = spec.get("target_sheet", class_name)
                sheets_data.setdefault(sheet, []).extend(rows)

    if not sheets_data:
        click.echo("No data found to flatten.", err=True)
        raise SystemExit(1)

    out = write_excel(sheets_data, output)
    click.echo(f"Flattened data written to {out}")
    for sheet, rows in sheets_data.items():
        click.echo(f"  {sheet}: {len(rows)} rows")


@cli.command()
@click.argument("excel_file", type=click.Path(exists=True))
@click.option(
    "--specs-dir", "-d",
    type=click.Path(exists=True),
    default=None,
    help="Directory containing FlatteningSpec YAML files",
)
@click.option(
    "--output-dir", "-o",
    type=click.Path(),
    default=".",
    help="Output directory for YAML files",
)
def unflatten(excel_file, specs_dir, output_dir):
    """Unflatten an Excel workbook back to nested YAML files."""
    from soma.flatten.excel_io import read_excel
    from soma.flatten.unflatten import unflatten_to_yaml

    specs_path = Path(specs_dir) if specs_dir else _SPECS_DIR
    specs = _load_specs(specs_path)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    sheets = read_excel(excel_file)

    # Map sheet names to specs
    sheet_to_spec = {}
    for class_name, spec in specs.items():
        sheet_name = spec.get("target_sheet", class_name)
        sheet_to_spec[sheet_name] = spec

    written = []
    for sheet_name, rows in sheets.items():
        if sheet_name not in sheet_to_spec:
            click.echo(f"  Skipping unknown sheet: {sheet_name}")
            continue
        if not rows:
            continue

        spec = sheet_to_spec[sheet_name]
        container_slot = spec["container_slot"]
        out_file = out_dir / f"Container-{container_slot}.yaml"
        unflatten_to_yaml(rows, spec, out_file)
        written.append(out_file)
        click.echo(f"  {sheet_name} -> {out_file}")

    click.echo(f"Wrote {len(written)} YAML files to {out_dir}")


@cli.command()
@click.argument("excel_file", type=click.Path(exists=True))
@click.option(
    "--schema", "-s",
    type=click.Path(exists=True),
    default=None,
    help="Path to soma.yaml schema file for validation",
)
@click.option(
    "--specs-dir", "-d",
    type=click.Path(exists=True),
    default=None,
    help="Directory containing FlatteningSpec YAML files",
)
def validate(excel_file, schema, specs_dir):
    """Unflatten Excel and validate against the source schema."""
    import subprocess
    import tempfile

    from soma.flatten.excel_io import read_excel
    from soma.flatten.unflatten import unflatten_to_yaml

    schema_path = Path(schema) if schema else _DEFAULT_SCHEMA
    specs_path = Path(specs_dir) if specs_dir else _SPECS_DIR
    specs = _load_specs(specs_path)

    sheets = read_excel(excel_file)

    sheet_to_spec = {}
    for class_name, spec in specs.items():
        sheet_name = spec.get("target_sheet", class_name)
        sheet_to_spec[sheet_name] = spec

    all_valid = True
    with tempfile.TemporaryDirectory() as tmpdir:
        for sheet_name, rows in sheets.items():
            if sheet_name not in sheet_to_spec or not rows:
                continue

            spec = sheet_to_spec[sheet_name]
            container_slot = spec["container_slot"]
            out_file = Path(tmpdir) / f"Container-{container_slot}.yaml"
            unflatten_to_yaml(rows, spec, out_file)

            result = subprocess.run(
                ["linkml-validate", "-s", str(schema_path), str(out_file)],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                click.echo(f"  VALID: {sheet_name}")
            else:
                click.echo(f"  INVALID: {sheet_name}")
                click.echo(f"    {result.stderr.strip()}")
                all_valid = False

    if all_valid:
        click.echo("All sheets validate successfully!")
    else:
        click.echo("Some sheets failed validation.", err=True)
        raise SystemExit(1)


def main():
    cli()


if __name__ == "__main__":
    main()
