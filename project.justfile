## Add your own just recipes here. This is imported by the main justfile.

# Generate flattening specs from schema introspection
[group('flatten')]
gen-flat-specs:
  uv run soma-flatten introspect

# Generate empty Excel template from flattening specs
[group('flatten')]
gen-flat-excel:
  uv run soma-flatten gen-excel -o soma_template.xlsx

# Flatten test YAML files to Excel
[group('flatten')]
flatten-tests:
  uv run soma-flatten flatten tests/data/valid/Container-ciliary_function.yaml tests/data/valid/Container-cftr.yaml tests/data/valid/Container-gene_expression.yaml -o tests/data/flat_output.xlsx

# Round-trip test: flatten -> unflatten -> validate
[group('flatten')]
test-roundtrip:
  @echo "Flattening test data..."
  uv run soma-flatten flatten tests/data/valid/Container-ciliary_function.yaml tests/data/valid/Container-cftr.yaml tests/data/valid/Container-gene_expression.yaml -o /tmp/soma_roundtrip.xlsx
  @echo "Unflattening..."
  uv run soma-flatten unflatten /tmp/soma_roundtrip.xlsx -o /tmp/soma_roundtrip/
  @echo "Round-trip complete. Output in /tmp/soma_roundtrip/"
