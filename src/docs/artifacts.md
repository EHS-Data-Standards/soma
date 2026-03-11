# Generated Artifacts

Download the generated model serializations:

- [JSON Schema](artifacts/soma.schema.json)
- [Pydantic Model](artifacts/soma_pydantic.py)
- [Python Dataclasses](artifacts/soma.py)
- [Excel Spreadsheet](artifacts/soma.xlsx)

## Paper-Derived SOMA Data

SOMA-conformant data extracted from published PM2.5 research papers. Each workbook contains
assay measurements mapped to the SOMA schema with full provenance (figure/table references,
p-values, protocols, exposure conditions).

### Montgomery et al. (2020)

**"Genome-Wide Analysis Reveals Mucociliary Remodeling of the Nasal Airway Epithelium Induced by Urban PM2.5"**

Am J Respir Cell Mol Biol. 2020;63(2):172-184 |
[Paper](https://academic.oup.com/ajrcmb/article/63/2/172/8461239) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC7397762/) |
DOI: 10.1165/rcmb.2019-0454OC

- [Excel Workbook](artifacts/Montgomery2020_PM25_Mucociliary_SOMA.xlsx)
- SOMA assay types: GeneExpressionAssay, GobletCellAssay, FoxJExpressionAssay
- Key findings: CYP1A1 LFC=6.21 (AhR activation), MUC5AC+ cells FC=2.88, FOXJ1+ nuclei 75% decrease, 424 DEGs at moderate dose

### Liu et al. (2024)

**"PM2.5 Exposure Inhibits Transepithelial Anion Short-circuit Current by Downregulating P2Y2 Receptor/CFTR Pathway"**

Int J Med Sci. 2024;21(10):1929-1944 |
[Paper](https://www.medsci.org/v21p1929.htm) |
DOI: 10.7150/ijms.96777

- [Excel Workbook](artifacts/Liu2024_PM25_CFTR_SOMA.xlsx)
- SOMA assay types: CFTRFunctionAssay, GeneExpressionAssay, GobletCellAssay, BALFSputumAssay, LungFunctionAssay
- Key findings: PM2.5 downregulates P2Y2R/CFTR (p<0.05), inhibits Isc, increases goblet cells (p<0.001), elevates Th2 cytokines
