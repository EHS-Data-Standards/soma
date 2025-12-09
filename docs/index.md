# Adverse Outcome Pathway (AOP) Data Model

This LinkML schema models **Adverse Outcome Pathways (AOPs)** - structured representations of biological pathways linking molecular initiating events to adverse outcomes at the organism or population level.

## What are AOPs?

An Adverse Outcome Pathway describes a sequential chain of causally linked events at different biological levels that lead from a molecular initiating event (MIE) through intermediate key events (KEs) to an adverse outcome (AO). AOPs are used in toxicology, environmental health, and risk assessment to understand how chemical exposures or other stressors lead to adverse health effects.

## Schema Components

This data model captures:

- **Adverse Outcome Pathways**: Complete pathways linking molecular initiating events to adverse outcomes
- **Key Events**: Measurable biological changes at molecular, cellular, organ, or organism levels
- **Key Event Relationships**: Directed associations between key events with supporting evidence
- **Measurement Processes**: Detailed specifications of experimental methods, assays, and measurements used to assess key events
- **Scientific Evidence**: Supporting data from peer-reviewed literature

## Context

This schema is part of the **Source-to-Outcome (S2O) continuum** framework, enabling standardized representation of biological pathway data for:

- Environmental health and safety assessment
- Toxicological pathway analysis
- Risk assessment and regulatory decision-making
- Integration with chemical exposure and epidemiological data

## Schema Visualizations

The following diagrams provide visual representations of the data model structure and relationships:

- **Mermaid ER Diagram**: [Interactive entity relationship diagram](elements/schema_diagram.mmd) - View the schema structure in Mermaid format
- **SQL ER Diagram**: [SQL database entity relationship diagram](elements/sql_er_diagram.png) - Visual representation of the SQL schema
- **PlantUML Diagram**: [UML class diagram](elements/schema_diagram.puml) - Detailed class structure in PlantUML format

## Documentation

- Auto-generated [schema documentation](elements/index.md)
