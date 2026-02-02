# About

## The Outcomes Working Group

The Outcomes Working Group is part of the [EHS Data Standards](https://github.com/EHS-Data-Standards)
initiative, focused on developing standardized data models for environmental health sciences research.

## Project Goals

This project aims to:

1. **Standardize data representation** for exposure-outcome relationships in EHS research
2. **Enable data interoperability** across studies, cohorts, and institutions
3. **Support mechanistic understanding** through integration with Adverse Outcome Pathways (AOPs)
4. **Bridge epidemiological and toxicological data** from human studies and model systems

## The Data Model

### Design Principles

The Outcomes Working Group Data Model follows these principles:

- **Ontology-first** - All entities are mapped to established biomedical ontologies
- **FAIR-compliant** - Supports Findable, Accessible, Interoperable, and Reusable data
- **Extensible** - New entity types can be added without breaking existing data
- **Multi-scale** - Captures data from molecular to population levels

### Technology Stack

The model is built using:

- [LinkML](https://linkml.io/) - Linked Data Modeling Language for schema definition
- [MkDocs](https://www.mkdocs.org/) with [Material theme](https://squidfunk.github.io/mkdocs-material/)
  for documentation
- Python for data validation and transformation

### Core Domains

| Domain | Description |
|--------|-------------|
| Study Entities | Studies, cohorts, and participant enrollment |
| Exposures | Chemical, dietary, environmental, and occupational exposures |
| Measurements | Biomarkers, phenotypes, gene/protein expression |
| Health Outcomes | Phenotypes, diseases, and adverse outcomes |
| AOPs | Adverse Outcome Pathways linking exposure to outcome |
| Model Systems | Cell cultures and in vitro exposure systems |
| Populations | Synthetic population geographic hierarchies |

## Contributing

We welcome contributions from the community. To contribute:

1. Visit the [GitHub repository](https://github.com/EHS-Data-Standards/outcomes-working-group)
2. Review the existing schema in `src/outcomes_working_group/schema/`
3. Open an issue to discuss proposed changes
4. Submit a pull request with your contributions

## Development

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) for package management
- [just](https://github.com/casey/just/) for running commands

### Quick Start

```bash
# Install dependencies
just install

# Generate documentation
just gen-doc

# Run local documentation server
just testdoc

# Run all tests
just test
```

### Project Structure

```
outcomes-working-group/
├── src/
│   ├── docs/                    # Documentation source files
│   └── outcomes_working_group/
│       ├── schema/              # LinkML schema definition
│       └── datamodel/           # Generated Python models
├── docs/
│   └── elements/                # Generated schema docs
├── project/                     # Generated artifacts
├── tests/
│   └── data/                    # Test data files
└── examples/                    # Usage examples
```

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

This project uses the [linkml-project-copier](https://github.com/dalito/linkml-project-copier)
template for project structure and build tooling.

## Contact

For questions or feedback, please open an issue on the
[GitHub repository](https://github.com/EHS-Data-Standards/outcomes-working-group/issues).