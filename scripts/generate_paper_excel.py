#!/usr/bin/env python3
"""Generate separate Excel workbooks with SOMA-conformant data from two PM2.5 papers."""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

HEADER_FONT = Font(bold=True, size=11, color="FFFFFF")
HEADER_FILL = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
SECTION_FILL = PatternFill(start_color="D9E2F3", end_color="D9E2F3", fill_type="solid")
SECTION_FONT = Font(bold=True, size=11)
THIN_BORDER = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)
WRAP = Alignment(wrap_text=True, vertical="top")


def style_header(ws, row, max_col):
    for col in range(1, max_col + 1):
        cell = ws.cell(row=row, column=col)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = WRAP
        cell.border = THIN_BORDER


def style_section(ws, row, max_col, label):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=max_col)
    cell = ws.cell(row=row, column=1, value=label)
    cell.font = SECTION_FONT
    cell.fill = SECTION_FILL
    cell.border = THIN_BORDER


def add_data_row(ws, row, data, max_col):
    for col, val in enumerate(data, 1):
        cell = ws.cell(row=row, column=col, value=val)
        cell.alignment = WRAP
        cell.border = THIN_BORDER


def auto_width(ws, max_col, min_w=12, max_w=40):
    for col in range(1, max_col + 1):
        ws.column_dimensions[get_column_letter(col)].width = min(
            max(min_w, max(len(str(c.value or "")) for c in ws[get_column_letter(col)])),
            max_w,
        )


# =============================================================================
# Montgomery et al. 2020
# =============================================================================

def create_montgomery_workbook():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    # --- Metadata ---
    ws = wb.create_sheet("Metadata")
    ws.sheet_properties.tabColor = "4472C4"
    meta = [
        ["Field", "Value"],
        ["Short Name", "Montgomery2020"],
        ["Title", "Genome-Wide Analysis Reveals Mucociliary Remodeling of the Nasal Airway Epithelium Induced by Urban PM2.5"],
        ["Authors", "Montgomery MT, Sajuthi SP, Cho SH, Everman JL, Rios CL, Goldfarbmuren KC, Jackson ND, Saef B, Cromie M, Eng C, Medina V, Elhawary JR, Oh SS, Rodriguez-Santana J, Vladar EK, Burchard EG, Seibold MA"],
        ["Journal", "Am J Respir Cell Mol Biol 2020;63(2):172-184"],
        ["DOI", "10.1165/rcmb.2019-0454OC"],
        ["PMCID", "PMC7397762"],
        ["URL", "https://academic.oup.com/ajrcmb/article/63/2/172/8461239"],
        ["", ""],
        ["In Vitro Model", "Primary human nasal AECs at ALI, 28-32 days differentiation"],
        ["In Vivo Model", "None (in vitro only)"],
        ["PM2.5 Source", "3 California cities (Bakersfield/Fresno, Sacramento, Yuba City), 2011"],
        ["PM2.5 Extract", "Water-soluble (WE) and organic-soluble (OE) fractions"],
        ["Key Concentrations", "OE: 0.045, 0.45, 4.5 µg/cm²; WE: 3, 30 µg/cm²"],
        ["Acute Protocol", "2 stimulations 24h apart, harvest 24h after second"],
        ["Chronic Protocol", "5 stimulations over 5 days (high OE dose)"],
        ["Toxicity", "<1% by LDH assay at all concentrations"],
        ["", ""],
        ["SOMA Assay Types Used", "GeneExpressionAssay, GobletCellAssay, FoxJExpressionAssay"],
    ]
    for i, row in enumerate(meta, 1):
        for j, val in enumerate(row, 1):
            cell = ws.cell(row=i, column=j, value=val)
            cell.alignment = WRAP
            cell.border = THIN_BORDER
            if i == 1:
                cell.font = HEADER_FONT
                cell.fill = HEADER_FILL
    ws.column_dimensions["A"].width = 25
    ws.column_dimensions["B"].width = 80

    # --- Data sheet ---
    ws = wb.create_sheet("Assay Data")

    headers = [
        "Assay ID", "Assay Type", "Assay Name", "Description",
        "Target Gene", "Method", "Measurement Slot", "Value",
        "Unit", "Unit ID", "Exposure Agent", "Exposure Conc",
        "Conc Unit", "Exposure Duration", "Duration Unit",
        "Study Subject Type", "Subject ID", "Cell Type",
        "Cell Type ID", "Species", "Culture Mode",
        "Days Differentiated", "Donor Info",
        "Key Event", "Biological Action", "Bio Organization Level",
        "Protocol ID", "Protocol Name", "Detection Method",
        "p-value", "Source Figure/Table",
    ]
    ncol = len(headers)
    ws.append(headers)
    style_header(ws, 1, ncol)
    r = 2

    # Acute RNA-seq moderate OE
    style_section(ws, r, ncol, "GENE EXPRESSION — Acute (RNA-seq, moderate OE 0.45 µg/cm²)")
    r += 1

    sub = ("CellularSystem", "soma:montgomery-culture-001", "nasal epithelial cell",
           "CL:0002603", "Homo sapiens", "air_liquid_interface", 28,
           "12 donors (6 healthy, 6 asthmatic) GALA II")
    prot = ("PROTOCOL:montgomery-rnaseq-001", "RNA-seq KAPA mRNA HyperPrep", "Illumina NovaSeq 6000")
    exp = ("PM2.5 organic extract", "0.45", "µg/cm²", "48", "hour")

    rows = [
        ("GE:montgomery-cyp1a1-mod", "GeneExpressionAssay", "CYP1A1 mRNA – moderate OE",
         "Most highly upregulated gene; AhR pathway activation by PAH", "PR:000005470 (CYP1A1)", "RNA-seq",
         "mrna_level", 6.21, "log2 fold change", "UO:0000193", *exp, *sub,
         "AhR pathway activation", "activated", "molecular", *prot, "", "Fig 2"),
        ("GE:montgomery-il1a-mod", "GeneExpressionAssay", "IL1A mRNA – moderate OE",
         "Hub cytokine driving epithelial inflammatory response", "PR:000001551 (IL1A)", "RNA-seq",
         "mrna_level", 0.91, "log2 fold change", "UO:0000193", *exp, *sub,
         "IL-1 inflammatory program", "increased", "molecular", *prot, "", "Fig 3"),
        ("GE:montgomery-il1b-mod", "GeneExpressionAssay", "IL1B mRNA – moderate OE",
         "Hub cytokine; drives mucus metaplasia via SPDEF/FOXA3/XBP1", "PR:000001554 (IL1B)", "RNA-seq",
         "mrna_level", 1.22, "log2 fold change", "UO:0000193", *exp, *sub,
         "IL-1 inflammatory program", "increased", "molecular", *prot, "", "Fig 3"),
        ("GE:montgomery-muc5ac-mod", "GeneExpressionAssay", "MUC5AC mRNA – moderate OE",
         "Mucus secretory cell enrichment Padj=1.19e-74", "PR:000011230 (MUC5AC)", "RNA-seq",
         "mrna_level", 0.90, "log2 fold change", "UO:0000193", *exp, *sub,
         "Goblet cell hyperplasia", "increased", "cellular", *prot, "", "Fig 4"),
        ("GE:montgomery-muc2-mod", "GeneExpressionAssay", "MUC2 mRNA – moderate OE",
         "Mucin gene upregulated at moderate dose", "PR:000011228 (MUC2)", "RNA-seq",
         "mrna_level", 1.34, "log2 fold change", "UO:0000193", *exp, *sub,
         "Goblet cell hyperplasia", "increased", "cellular", *prot, "", "Fig 4"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # High OE
    style_section(ws, r, ncol, "GENE EXPRESSION — Acute (RNA-seq, high OE 4.5 µg/cm²)")
    r += 1
    sub_h = ("CellularSystem", "soma:montgomery-culture-high", "nasal epithelial cell",
             "CL:0002603", "Homo sapiens", "air_liquid_interface", 28, "5 donors GALA II")
    exp_h = ("PM2.5 organic extract", "4.5", "µg/cm²", "48", "hour")
    rows = [
        ("GE:montgomery-scgb1a1-high", "GeneExpressionAssay", "SCGB1A1 mRNA – high OE",
         "Club cell marker downregulated", "PR:000014857 (SCGB1A1)", "RNA-seq",
         "mrna_level", -0.92, "log2 fold change", "UO:0000193", *exp_h, *sub_h,
         "Club cell marker loss", "decreased", "cellular", *prot, "Padj=1.13e-3", "Fig 4"),
        ("GE:montgomery-muc5b-high", "GeneExpressionAssay", "MUC5B mRNA – high OE",
         "MUC5B trending down at high dose", "PR:000011231 (MUC5B)", "RNA-seq",
         "mrna_level", -0.79, "log2 fold change", "UO:0000193", *exp_h, *sub_h,
         "Goblet cell hyperplasia", "increased", "cellular", *prot, "Padj=1.0e-1", "Fig 4"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # Chronic qPCR
    style_section(ws, r, ncol, "GENE EXPRESSION — Chronic 5-day (qPCR)")
    r += 1
    sub_c = ("CellularSystem", "soma:montgomery-culture-chronic", "nasal epithelial cell",
             "CL:0002603", "Homo sapiens", "air_liquid_interface", 28, "4-5 donors GALA II")
    exp_c = ("PM2.5 organic extract", "4.5", "µg/cm²", "120", "hour")
    prot_q = ("PROTOCOL:montgomery-qpcr-001", "qRT-PCR validation", "qRT-PCR")
    rows = [
        ("GE:montgomery-muc5ac-chronic", "GeneExpressionAssay", "MUC5AC mRNA – chronic OE",
         "MUC5AC upregulated after 5-day chronic stimulation", "PR:000011230 (MUC5AC)", "qRT-PCR",
         "mrna_level", 1.72, "log2 fold change", "UO:0000193", *exp_c, *sub_c,
         "Goblet cell hyperplasia", "increased", "cellular", *prot_q, "p=1.27e-2", "Fig 6"),
        ("GE:montgomery-muc5b-chronic", "GeneExpressionAssay", "MUC5B mRNA – chronic OE",
         "MUC5B trending down (not significant)", "PR:000011231 (MUC5B)", "qRT-PCR",
         "mrna_level", -0.72, "log2 fold change", "UO:0000193", *exp_c, *sub_c,
         "Goblet cell hyperplasia", "increased", "cellular", *prot_q, "p=9.74e-2", "Fig 6"),
        ("GE:montgomery-spdef-chronic", "GeneExpressionAssay", "SPDEF mRNA – chronic OE",
         "Mucus metaplasia TF; protein 1.5-fold (p=1.07e-2, WB)", "PR:000014070 (SPDEF)", "qRT-PCR",
         "mrna_level", 0.84, "log2 fold change", "UO:0000193", *exp_c, *sub_c,
         "Goblet cell hyperplasia", "increased", "cellular", *prot_q, "p=3.19e-2", "Fig 6"),
        ("GE:montgomery-scgb1a1-chronic", "GeneExpressionAssay", "SCGB1A1 mRNA – chronic OE",
         "Club cell marker loss after chronic stimulation", "PR:000014857 (SCGB1A1)", "qRT-PCR",
         "mrna_level", -1.51, "log2 fold change", "UO:0000193", *exp_c, *sub_c,
         "Club cell marker loss", "decreased", "cellular", *prot_q, "p=2.94e-2", "Fig 6"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # Goblet Cell Assays
    style_section(ws, r, ncol, "GOBLET CELL ASSAYS — Chronic 5-day")
    r += 1
    rows = [
        ("GCM:montgomery-muc5ac-if", "GobletCellAssay", "MUC5AC+ cells – chronic OE (IF)",
         "All 4 donors showed MUC5AC+ cell increase", "", "Immunofluorescence",
         "muc5ac_protein_expression", 2.88, "fold change", "UO:0000193", *exp_c, *sub_c,
         "Goblet cell hyperplasia", "increased", "cellular",
         "PROTOCOL:montgomery-if-001", "Immunofluorescence MUC5AC", "Confocal microscopy",
         "p=3.19e-2", "Fig 7"),
        ("GCM:montgomery-muc5ac-secretion", "GobletCellAssay", "MUC5AC secretion – chronic OE",
         "ATP-induced MUC5AC secretion increased; n=5 donors", "", "ELISA",
         "mucin_secretion_rate", 2.2, "fold change", "UO:0000193", *exp_c, *sub_c,
         "Mucin hypersecretion", "increased", "cellular",
         "PROTOCOL:montgomery-elisa-001", "Colorimetric ELISA", "Absorbance 490 nm",
         "p=1.54e-2", "Fig 7"),
        ("GCM:montgomery-muc5b-if", "GobletCellAssay", "MUC5B+ cells – chronic OE (IF)",
         "All 4 donors showed MUC5B+ cell decrease", "", "Immunofluorescence",
         "muc5b_protein_expression", 0.74, "fold change", "UO:0000193", *exp_c, *sub_c,
         "Goblet cell hyperplasia", "increased", "cellular",
         "PROTOCOL:montgomery-if-001", "Immunofluorescence MUC5B", "Confocal microscopy",
         "p=8.84e-2", "Fig 7"),
        ("GCM:montgomery-muc5b-secretion", "GobletCellAssay", "MUC5B secretion – chronic OE",
         "ATP-induced MUC5B secretion decreased; n=5 donors", "", "ELISA",
         "mucin_secretion_rate", 0.81, "fold change", "UO:0000193", *exp_c, *sub_c,
         "Mucin hypersecretion", "increased", "cellular",
         "PROTOCOL:montgomery-elisa-001", "Colorimetric ELISA", "Absorbance 490 nm",
         "p=3.59e-3", "Fig 7"),
        ("GCM:montgomery-abpas", "GobletCellAssay", "Mucin+ cells (AB-PAS) – chronic OE",
         "3 of 4 donors showed increase in mucin-positive cells", "", "AB-PAS staining",
         "goblet_cell_percentage", 2.01, "fold change", "UO:0000193", *exp_c, *sub_c,
         "Goblet cell hyperplasia", "increased", "cellular",
         "PROTOCOL:montgomery-abpas-001", "Alcian blue-PAS staining", "Light microscopy",
         "p=6.52e-2", "Fig 7"),
        ("GCM:montgomery-spdef-protein", "GobletCellAssay", "SPDEF protein – chronic OE (WB)",
         "1.5-fold increase in SPDEF protein; actin-normalized; n=5", "", "Western blot",
         "goblet_cell_percentage", 1.5, "fold change", "UO:0000193", *exp_c, *sub_c,
         "Goblet cell hyperplasia", "increased", "cellular",
         "PROTOCOL:montgomery-wb-001", "Western blot SPDEF", "Densitometry",
         "p=1.07e-2", "Fig 7"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # FOXJ1
    style_section(ws, r, ncol, "FOXJ1 EXPRESSION — Chronic 5-day")
    r += 1
    rows = [
        ("FOXJ:montgomery-mrna", "FoxJExpressionAssay", "FOXJ1 mRNA – chronic OE",
         "FOXJ1 mRNA downregulated after chronic stimulation", "", "qRT-PCR",
         "foxj1_mrna_expression", -0.36, "log2 fold change", "UO:0000193", *exp_c,
         "CellularSystem", "soma:montgomery-culture-chronic", "nasal epithelial cell",
         "CL:0002603", "Homo sapiens", "air_liquid_interface", 28, "3 donors GALA II",
         "Altered ciliogenesis", "decreased", "cellular",
         *prot_q, "p=1.92e-2", "Fig 8"),
        ("FOXJ:montgomery-nuclei", "FoxJExpressionAssay", "FOXJ1+ nuclei – chronic OE (IF)",
         "75% average decrease in FOXJ1+ nuclei vs mock; n=3 donors", "", "Immunofluorescence",
         "foxj1_positive_cell_percentage", "75% decrease", "percent decrease", "", *exp_c,
         "CellularSystem", "soma:montgomery-culture-chronic", "nasal epithelial cell",
         "CL:0002603", "Homo sapiens", "air_liquid_interface", 28, "3 donors GALA II",
         "Altered ciliogenesis", "decreased", "cellular",
         "PROTOCOL:montgomery-if-001", "Immunofluorescence FOXJ1", "Confocal microscopy",
         "p=1.20e-2", "Fig 8"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # Dose-response
    style_section(ws, r, ncol, "DOSE-RESPONSE SUMMARY (DEG counts)")
    r += 1
    rows = [
        ("", "", "Low OE DEGs", "11 DEGs; 9/11 overlap moderate dose",
         "", "RNA-seq", "DEG count", 11, "count", "", "PM2.5 OE", "0.045", "µg/cm²", "48", "hour",
         "CellularSystem", "soma:montgomery-culture-001", "nasal epithelial cell", "CL:0002603",
         "Homo sapiens", "air_liquid_interface", 28, "5 donors", "", "", "",
         "", "", "", "", "Fig 1"),
        ("", "", "Moderate OE DEGs", "424 DEGs (281 up, 143 down)",
         "", "RNA-seq", "DEG count", 424, "count", "", "PM2.5 OE", "0.45", "µg/cm²", "48", "hour",
         "CellularSystem", "soma:montgomery-culture-001", "nasal epithelial cell", "CL:0002603",
         "Homo sapiens", "air_liquid_interface", 28, "12 donors", "", "", "",
         "", "", "", "", "Fig 1-2"),
        ("", "", "High OE DEGs", "1296 DEGs; ciliated cell enrichment Padj=3.57e-118",
         "", "RNA-seq", "DEG count", 1296, "count", "", "PM2.5 OE", "4.5", "µg/cm²", "48", "hour",
         "CellularSystem", "soma:montgomery-culture-high", "nasal epithelial cell", "CL:0002603",
         "Homo sapiens", "air_liquid_interface", 28, "5 donors", "", "", "",
         "", "", "", "", "Fig 1,5"),
        ("", "", "NIST 2786 DEGs", "111 DEGs; Pearson r=0.75 with mod OE (P=1.68e-34)",
         "", "RNA-seq", "DEG count", 111, "count", "", "NIST 2786 fine PM", "30", "µg/cm²", "48", "hour",
         "CellularSystem", "soma:montgomery-culture-nist", "nasal epithelial cell", "CL:0002603",
         "Homo sapiens", "air_liquid_interface", 28, "4 donors", "", "", "",
         "", "", "", "", "Fig 2"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    auto_width(ws, ncol)

    out = "/Users/SMoxon/Documents/src/soma/src/docs/Montgomery2020_PM25_Mucociliary_SOMA.xlsx"
    wb.save(out)
    print(f"Saved: {out}")


# =============================================================================
# Liu et al. 2024
# =============================================================================

def create_liu_workbook():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    # --- Metadata ---
    ws = wb.create_sheet("Metadata")
    ws.sheet_properties.tabColor = "4472C4"
    meta = [
        ["Field", "Value"],
        ["Short Name", "Liu2024"],
        ["Title", "PM2.5 Exposure Inhibits Transepithelial Anion Short-circuit Current by Downregulating P2Y2 Receptor/CFTR Pathway"],
        ["Authors", "Liu X, Li Z, Shan J, Wang F, Li Z, Luo S, Wu J"],
        ["Journal", "Int J Med Sci 2024;21(10):1929-1944"],
        ["DOI", "10.7150/ijms.96777"],
        ["URL", "https://www.medsci.org/v21p1929.htm"],
        ["Ethics", "GDREC2019347A; SYXK(Guangdong)2017-0178"],
        ["", ""],
        ["In Vitro Model", "Calu-3 human airway epithelial cells, submerged monolayer, transwell (Corning 3801)"],
        ["In Vitro Medium", "DMEM + 10% FBS + 1% pen/strep, 21-day post-confluency, 37°C, 5% CO2"],
        ["In Vivo Model", "Male Balb/c mice (6-8 wk, 18-22g, SPF), OVA-induced asthma (n=50, 5 groups of 10)"],
        ["In Vivo Protocol", "OVA sensitization d1,7,14 (IP); OVA challenge d21-27 (inhaled 1%); treatments d21-27 (nasal)"],
        ["PM2.5 Source", "Guangzhou, China (Jul-Nov 2019), high-flow sampler at 1.05 m³/min"],
        ["In Vitro PM2.5", "100 µg/mL in serum-free DMEM/F12; 24h and 48h exposures"],
        ["Treatment Groups", "Control (PBS), ATP (10 µM), PM2.5 (100 µg/mL), ATP+PM2.5, Suramin (100 µM), PM2.5+Suramin"],
        ["In Vivo Treatments", "Saline, OVA alone, OVA+PM2.5 (100 µg/mL nasal), OVA+ATP (50 mg/kg nasal), OVA+Suramin (50 mg/kg nasal)"],
        ["", ""],
        ["SOMA Assay Types", "CFTRFunctionAssay, GeneExpressionAssay, GobletCellAssay, BALFSputumAssay, LungFunctionAssay"],
    ]
    for i, row in enumerate(meta, 1):
        for j, val in enumerate(row, 1):
            cell = ws.cell(row=i, column=j, value=val)
            cell.alignment = WRAP
            cell.border = THIN_BORDER
            if i == 1:
                cell.font = HEADER_FONT
                cell.fill = HEADER_FILL
    ws.column_dimensions["A"].width = 25
    ws.column_dimensions["B"].width = 90

    # --- Data sheet ---
    ws = wb.create_sheet("Assay Data")
    headers = [
        "Assay ID", "Assay Type", "Assay Name", "Description",
        "Target Gene/Protein", "Method", "Measurement Slot", "Value",
        "Unit", "Unit ID", "Exposure Agent", "Exposure Conc",
        "Conc Unit", "Exposure Duration", "Duration Unit",
        "Study Subject Type", "Subject ID", "Cell Type / Species",
        "Cell Line / Strain", "Culture Mode / Animal Model",
        "Treatment Group",
        "Key Event", "Biological Action", "Bio Organization Level",
        "Protocol ID", "Protocol Name", "Detection Method",
        "Significance", "Source Figure/Table",
    ]
    ncol = len(headers)
    ws.append(headers)
    style_header(ws, 1, ncol)
    r = 2

    # Helper tuples
    calu3 = ("CellularSystem", "soma:liu-calu3-001", "Calu-3 (human airway epithelial)",
             "CLO:0003679 (Calu-3)", "Submerged monolayer, transwell, 21d")
    mouse_pm = ("InVivoSubject", "SUBJECT:liu-mouse-ova-pm25", "Mus musculus",
                "Male Balb/c, 6-8 wk, SPF", "OVA-induced asthma + PM2.5")
    mouse_atp = ("InVivoSubject", "SUBJECT:liu-mouse-ova-atp", "Mus musculus",
                 "Male Balb/c, 6-8 wk, SPF", "OVA-induced asthma + ATP")
    mouse_sur = ("InVivoSubject", "SUBJECT:liu-mouse-ova-suramin", "Mus musculus",
                 "Male Balb/c, 6-8 wk, SPF", "OVA-induced asthma + Suramin")
    mouse_ctrl = ("InVivoSubject", "SUBJECT:liu-mouse-control", "Mus musculus",
                  "Male Balb/c, 6-8 wk, SPF", "Saline control")

    # CFTR Function
    style_section(ws, r, ncol, "CFTR FUNCTION — Ussing Chamber Short-Circuit Current")
    r += 1
    rows = [
        ("CFTR:liu-ctrl-24h", "CFTRFunctionAssay", "CFTR Isc – Control + ATP 24h",
         "Baseline ATP-induced Isc in control Calu-3", "CFTR", "Ussing chamber",
         "cftr_chloride_secretion", "1.0 (baseline)", "fold change", "UO:0000193",
         "None (PBS)", "", "", "24", "hour", *calu3, "Control",
         "Decreased CFTR function", "decreased", "molecular",
         "PROTOCOL:liu-ussing-001", "Ussing chamber Isc", "Electrophysiology", "", "Fig 1C-E"),
        ("CFTR:liu-pm25-24h", "CFTRFunctionAssay", "CFTR Isc – PM2.5 + ATP 24h",
         "Significantly slower Isc increase; dIsc/dT decreased vs control", "CFTR", "Ussing chamber",
         "cftr_chloride_secretion", "decreased", "fold change", "UO:0000193",
         "PM2.5", "100", "µg/mL", "24", "hour", *calu3, "PM2.5",
         "Decreased CFTR function", "decreased", "molecular",
         "PROTOCOL:liu-ussing-001", "Ussing chamber Isc", "Electrophysiology", "p<0.05", "Fig 1C-E"),
        ("CFTR:liu-mouse-ctrl", "CFTRFunctionAssay", "Mouse trachea Isc – Control",
         "ATP-induced Isc in control tracheal tissue (ATP 100 µM)", "CFTR", "Ussing chamber",
         "cftr_chloride_secretion", "1.0 (baseline)", "fold change", "UO:0000193",
         "Saline", "", "", "", "", *mouse_ctrl, "Control",
         "Decreased CFTR function", "decreased", "molecular",
         "PROTOCOL:liu-ussing-001", "Ussing chamber – mouse trachea", "Electrophysiology", "", "Fig 2C-D"),
        ("CFTR:liu-mouse-pm25", "CFTRFunctionAssay", "Mouse trachea Isc – OVA+PM2.5",
         "dIsc lower vs control; dIsc/dT decreased", "CFTR", "Ussing chamber",
         "cftr_chloride_secretion", "decreased", "fold change", "UO:0000193",
         "PM2.5 nasal", "100", "µg/mL", "7", "day", *mouse_pm, "OVA+PM2.5",
         "Decreased CFTR function", "decreased", "molecular",
         "PROTOCOL:liu-ussing-001", "Ussing chamber – mouse trachea", "Electrophysiology", "p<0.05", "Fig 2C-D"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # P2Y2R/CFTR Protein (WB)
    style_section(ws, r, ncol, "GENE EXPRESSION — P2Y2R & CFTR Protein (Western Blot, In Vitro)")
    r += 1
    rows = [
        ("GE:liu-p2y2r-wb-24h", "GeneExpressionAssay", "P2Y2R protein – PM2.5 24h",
         "Significantly decreased; ATP+PM2.5 << ATP alone (p<0.01)", "P2Y2R (Abcam ab272891)", "Western blot",
         "protein_level", "decreased", "fold change", "UO:0000193",
         "PM2.5", "100", "µg/mL", "24", "hour", *calu3, "PM2.5",
         "Decreased P2Y2R", "decreased", "molecular",
         "PROTOCOL:liu-wb-001", "WB P2Y2R/CFTR", "ChemiScope chemiluminescence", "p<0.05", "Fig 3C-E"),
        ("GE:liu-cftr-wb-24h", "GeneExpressionAssay", "CFTR protein – PM2.5 24h",
         "Significantly decreased; ATP+PM2.5 << ATP alone (p<0.01)", "CFTR (CST 78335S)", "Western blot",
         "protein_level", "decreased", "fold change", "UO:0000193",
         "PM2.5", "100", "µg/mL", "24", "hour", *calu3, "PM2.5",
         "Decreased CFTR function", "decreased", "molecular",
         "PROTOCOL:liu-wb-001", "WB P2Y2R/CFTR", "ChemiScope chemiluminescence", "p<0.05", "Fig 3C-E"),
        ("GE:liu-p2y2r-wb-48h", "GeneExpressionAssay", "P2Y2R protein – PM2.5 48h",
         "Further decreased; ATP+PM2.5 << ATP (p<0.01)", "P2Y2R (Abcam ab272891)", "Western blot",
         "protein_level", "decreased", "fold change", "UO:0000193",
         "PM2.5", "100", "µg/mL", "48", "hour", *calu3, "PM2.5",
         "Decreased P2Y2R", "decreased", "molecular",
         "PROTOCOL:liu-wb-001", "WB P2Y2R/CFTR", "ChemiScope chemiluminescence", "p<0.05", "Fig 3F-H"),
        ("GE:liu-cftr-wb-48h", "GeneExpressionAssay", "CFTR protein – PM2.5 48h",
         "Further decreased; ATP+PM2.5 << ATP (p<0.01)", "CFTR (CST 78335S)", "Western blot",
         "protein_level", "decreased", "fold change", "UO:0000193",
         "PM2.5", "100", "µg/mL", "48", "hour", *calu3, "PM2.5",
         "Decreased CFTR function", "decreased", "molecular",
         "PROTOCOL:liu-wb-001", "WB P2Y2R/CFTR", "ChemiScope chemiluminescence", "p<0.05", "Fig 3F-H"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # P2Y2R mRNA (qPCR)
    style_section(ws, r, ncol, "GENE EXPRESSION — P2Y2R mRNA (qRT-PCR, In Vitro)")
    r += 1
    rows = [
        ("GE:liu-p2y2r-mrna-24h", "GeneExpressionAssay", "P2Y2R mRNA – PM2.5 24h",
         "Downregulated; ATP no change vs control", "P2Y2R (P2RY2)", "qRT-PCR",
         "mrna_level", "downregulated", "fold change", "UO:0000193",
         "PM2.5", "100", "µg/mL", "24", "hour", *calu3, "PM2.5",
         "Decreased P2Y2R", "decreased", "molecular",
         "PROTOCOL:liu-qpcr-001", "qRT-PCR P2Y2R", "GAPDH-normalized", "", "Fig 3A"),
        ("GE:liu-p2y2r-mrna-48h", "GeneExpressionAssay", "P2Y2R mRNA – PM2.5 48h",
         "Further downregulated; ATP up vs ctrl (p<0.05)", "P2Y2R (P2RY2)", "qRT-PCR",
         "mrna_level", "downregulated", "fold change", "UO:0000193",
         "PM2.5", "100", "µg/mL", "48", "hour", *calu3, "PM2.5",
         "Decreased P2Y2R", "decreased", "molecular",
         "PROTOCOL:liu-qpcr-001", "qRT-PCR P2Y2R", "GAPDH-normalized", "p<0.05 ATP vs ctrl", "Fig 3B"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # In Vivo IHC/WB
    style_section(ws, r, ncol, "GENE EXPRESSION — Lung Tissue P2Y2R & CFTR (IHC + WB, In Vivo)")
    r += 1
    rows = [
        ("GE:liu-p2y2r-ihc", "GeneExpressionAssay", "P2Y2R IHC – OVA+PM2.5 lung",
         "Dramatically decreased; OVA+PM2.5 << OVA (p<0.05); OVA+ATP >> OVA (p<0.05)",
         "P2Y2R (1:500, Abcam)", "IHC",
         "percentage_positive_cells", "decreased", "% positive area", "UO:0000187",
         "PM2.5", "100", "µg/mL nasal", "7", "day", *mouse_pm, "OVA+PM2.5",
         "Decreased P2Y2R", "decreased", "molecular",
         "PROTOCOL:liu-ihc-001", "IHC P2Y2R", "DAB 0.05%", "p<0.05", "Fig 6B-C"),
        ("GE:liu-cftr-ihc", "GeneExpressionAssay", "CFTR IHC – OVA+PM2.5 lung",
         "Dramatically decreased; OVA+PM2.5 << OVA (p<0.05); OVA+ATP >> OVA (p<0.05)",
         "CFTR (1:1000, Abclone)", "IHC",
         "percentage_positive_cells", "decreased", "% positive area", "UO:0000187",
         "PM2.5", "100", "µg/mL nasal", "7", "day", *mouse_pm, "OVA+PM2.5",
         "Decreased CFTR", "decreased", "molecular",
         "PROTOCOL:liu-ihc-001", "IHC CFTR", "DAB 0.05%", "p<0.05", "Fig 6B-C"),
        ("GE:liu-p2y2r-wb-lung", "GeneExpressionAssay", "P2Y2R WB – OVA+PM2.5 lung",
         "OVA+PM2.5 << OVA (p<0.05); OVA+ATP > OVA (p<0.05)",
         "P2Y2R", "Western blot",
         "protein_level", "decreased", "fold change", "UO:0000193",
         "PM2.5", "100", "µg/mL nasal", "7", "day", *mouse_pm, "OVA+PM2.5",
         "Decreased P2Y2R", "decreased", "molecular",
         "PROTOCOL:liu-wb-001", "WB lung tissue", "Chemiluminescence", "p<0.05", "Fig 6D-F"),
        ("GE:liu-cftr-wb-lung", "GeneExpressionAssay", "CFTR WB – OVA+PM2.5 lung",
         "OVA+PM2.5 << OVA (p<0.05); OVA+ATP > OVA (p<0.05)",
         "CFTR", "Western blot",
         "protein_level", "decreased", "fold change", "UO:0000193",
         "PM2.5", "100", "µg/mL nasal", "7", "day", *mouse_pm, "OVA+PM2.5",
         "Decreased CFTR", "decreased", "molecular",
         "PROTOCOL:liu-wb-001", "WB lung tissue", "Chemiluminescence", "p<0.05", "Fig 6D-F"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # Goblet Cell (PAS)
    style_section(ws, r, ncol, "GOBLET CELL ASSAYS — PAS Staining (In Vivo)")
    r += 1
    rows = [
        ("GCM:liu-pas-ova-pm25", "GobletCellAssay", "Goblet cells – OVA+PM2.5 (PAS)",
         "Evidently higher than OVA alone (p<0.001); near trachea/bronchus",
         "", "PAS staining",
         "goblet_cell_percentage", "increased", "percent", "UO:0000187",
         "PM2.5", "100", "µg/mL nasal", "7", "day", *mouse_pm, "OVA+PM2.5",
         "Goblet cell hyperplasia", "increased", "cellular",
         "PROTOCOL:liu-pas-001", "PAS staining", "Light microscopy", "p<0.001", "Fig 8B,E"),
        ("GCM:liu-pas-ova-atp", "GobletCellAssay", "Goblet cells – OVA+ATP (PAS)",
         "Lower than OVA alone (p<0.001); ATP partially rescues",
         "", "PAS staining",
         "goblet_cell_percentage", "decreased vs OVA", "percent", "UO:0000187",
         "ATP", "50", "mg/kg nasal", "7", "day", *mouse_atp, "OVA+ATP",
         "Goblet cell hyperplasia", "increased", "cellular",
         "PROTOCOL:liu-pas-001", "PAS staining", "Light microscopy", "p<0.001", "Fig 8B,E"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # BALF Cytokines
    style_section(ws, r, ncol, "BALF — Th2 Cytokines (In Vivo, ELISA)")
    r += 1
    rows = [
        ("BALF:liu-il4", "BALFSputumAssay", "IL-4 in BALF – OVA+PM2.5",
         "Significantly increased vs OVA (p<0.05); OVA+ATP lower (p<0.05)", "IL-4", "ELISA",
         "(IL-4, not in SOMA slots)", "increased vs OVA", "relative", "",
         "PM2.5", "100", "µg/mL nasal", "7", "day", *mouse_pm, "OVA+PM2.5",
         "Th2 airway inflammation", "increased", "tissue",
         "PROTOCOL:liu-elisa-001", "ELISA IL-4 (Absin)", "ELISA", "p<0.05", "Fig 7B"),
        ("BALF:liu-il5", "BALFSputumAssay", "IL-5 in BALF – OVA+PM2.5",
         "Significantly increased vs OVA (p<0.05); OVA+ATP lower (p<0.05)", "IL-5", "ELISA",
         "(IL-5, not in SOMA slots)", "increased vs OVA", "relative", "",
         "PM2.5", "100", "µg/mL nasal", "7", "day", *mouse_pm, "OVA+PM2.5",
         "Th2 airway inflammation", "increased", "tissue",
         "PROTOCOL:liu-elisa-001", "ELISA IL-5 (Absin)", "ELISA", "p<0.05", "Fig 7C"),
        ("BALF:liu-il13", "BALFSputumAssay", "IL-13 in BALF – OVA+PM2.5",
         "Increased vs OVA (p<0.05); Suramin > OVA (p<0.05)", "IL-13", "ELISA",
         "(IL-13, not in SOMA slots)", "increased vs OVA", "relative", "",
         "PM2.5", "100", "µg/mL nasal", "7", "day", *mouse_pm, "OVA+PM2.5",
         "Th2 airway inflammation", "increased", "tissue",
         "PROTOCOL:liu-elisa-001", "ELISA IL-13 (Absin)", "ELISA", "p<0.05", "Fig 7D"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # Lung Function
    style_section(ws, r, ncol, "LUNG FUNCTION — Airway Hyperresponsiveness (In Vivo, Plethysmography)")
    r += 1
    rows = [
        ("LF:liu-ova-pm25", "LungFunctionAssay", "sRaw – OVA+PM2.5",
         "sRaw elevated vs OVA at all MCh concentrations",
         "", "Whole-body plethysmography",
         "lung_resistance", "increased vs OVA", "cmH2O/mL/s", "",
         "PM2.5", "100", "µg/mL nasal", "7", "day", *mouse_pm, "OVA+PM2.5",
         "Airway hyperresponsiveness", "increased", "organ",
         "PROTOCOL:liu-lungfx-001", "BUXCO plethysmography", "MCh 0,5,10,20 mg/mL", "", "Fig 7A"),
        ("LF:liu-ova-suramin", "LungFunctionAssay", "sRaw – OVA+Suramin",
         "sRaw higher than OVA at 20 mg/mL MCh (p<0.05)",
         "", "Whole-body plethysmography",
         "lung_resistance", "increased vs OVA", "cmH2O/mL/s", "",
         "Suramin", "50", "mg/kg nasal", "7", "day", *mouse_sur, "OVA+Suramin",
         "Airway hyperresponsiveness", "increased", "organ",
         "PROTOCOL:liu-lungfx-001", "BUXCO plethysmography", "MCh 0,5,10,20 mg/mL", "p<0.05 at 20 mg/mL", "Fig 7A"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # Histopathology
    style_section(ws, r, ncol, "HISTOPATHOLOGY — HE + Masson (In Vivo)")
    r += 1
    rows = [
        ("", "", "HE Smith Score – OVA+PM2.5",
         "Higher than OVA; destroyed alveolar structure, thick septum",
         "", "HE staining",
         "Smith injury score", "elevated vs OVA", "score (0-16)", "",
         "PM2.5", "100", "µg/mL nasal", "7", "day", *mouse_pm, "OVA+PM2.5",
         "Lung injury", "increased", "tissue",
         "", "HE + Smith scoring", "Blinded pathologist", "", "Fig 8A,D"),
        ("", "", "Masson collagen – OVA+PM2.5",
         "Increased collagen vs OVA; ATP reduced deposition",
         "", "Masson staining",
         "collagen % positive", "increased vs OVA", "% positive area", "",
         "PM2.5", "100", "µg/mL nasal", "7", "day", *mouse_pm, "OVA+PM2.5",
         "Airway remodeling", "increased", "tissue",
         "", "Masson trichrome", "Light microscopy", "", "Fig 8C,F"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    # Calcium
    style_section(ws, r, ncol, "CALCIUM MEASUREMENT — Flow Cytometry (In Vitro)")
    r += 1
    rows = [
        ("", "", "Ca2+ fluorescence – ATP 24h",
         "Fluo-3/AM significantly higher than control (p<0.01)",
         "", "Flow cytometry (BD Accuri C6 Plus)",
         "mean fluorescence", "increased", "MFI", "",
         "ATP", "10", "µM", "24", "hour", *calu3, "ATP",
         "P2Y2R calcium signaling", "increased", "molecular",
         "PROTOCOL:liu-flowcyt-001", "Fluo-3/AM calcium", "FITC channel", "p<0.01", "Fig 4"),
        ("", "", "Ca2+ fluorescence – ATP+PM2.5 24h",
         "Significantly lower than ATP alone (p<0.01)",
         "", "Flow cytometry (BD Accuri C6 Plus)",
         "mean fluorescence", "decreased vs ATP", "MFI", "",
         "PM2.5 + ATP", "100 + 10", "µg/mL + µM", "24", "hour", *calu3, "ATP+PM2.5",
         "P2Y2R calcium signaling", "decreased", "molecular",
         "PROTOCOL:liu-flowcyt-001", "Fluo-3/AM calcium", "FITC channel", "p<0.01", "Fig 4"),
        ("", "", "Ca2+ fluorescence – ATP 48h",
         "Significantly higher than control (p<0.01)",
         "", "Flow cytometry (BD Accuri C6 Plus)",
         "mean fluorescence", "increased", "MFI", "",
         "ATP", "10", "µM", "48", "hour", *calu3, "ATP",
         "P2Y2R calcium signaling", "increased", "molecular",
         "PROTOCOL:liu-flowcyt-001", "Fluo-3/AM calcium", "FITC channel", "p<0.01", "Fig 5"),
        ("", "", "Ca2+ fluorescence – ATP+PM2.5 48h",
         "Significantly lower than ATP alone (p<0.01)",
         "", "Flow cytometry (BD Accuri C6 Plus)",
         "mean fluorescence", "decreased vs ATP", "MFI", "",
         "PM2.5 + ATP", "100 + 10", "µg/mL + µM", "48", "hour", *calu3, "ATP+PM2.5",
         "P2Y2R calcium signaling", "decreased", "molecular",
         "PROTOCOL:liu-flowcyt-001", "Fluo-3/AM calcium", "FITC channel", "p<0.01", "Fig 5"),
    ]
    for row_data in rows:
        add_data_row(ws, r, row_data, ncol)
        r += 1

    auto_width(ws, ncol)

    out = "/Users/SMoxon/Documents/src/soma/src/docs/Liu2024_PM25_CFTR_SOMA.xlsx"
    wb.save(out)
    print(f"Saved: {out}")


if __name__ == "__main__":
    create_montgomery_workbook()
    create_liu_workbook()
