#!/usr/bin/env python3
"""
Generate ADDITIONAL / SUPPLEMENTARY study notes on
"Sterilization and Disinfection" for GPAT & Pharmacy job exams.

These notes are designed to COMPLEMENT the user's existing scanned notes
(GDC GPAT notes + a typed Part B) by filling the high-yield gaps that
mock tests frequently target: sterilization kinetics with numericals,
detailed heat/radiation/gaseous/filtration methods, full disinfectant
classification & mechanisms, evaluation of disinfectants (phenol
coefficient etc.), sterility testing per IP, and biological/chemical
indicators.

Visual style matches the user's established template
(create_joints_notes.py / create_tissues_notes.py):
Legal page size, 1.27 cm margins, colored headings, shaded tables,
highlight boxes, section dividers, two-column MCQ layout, quick revision.

Sources: Hugo & Russell's Pharmaceutical Microbiology, Ananthanarayan &
Paniker's Microbiology, Lachman (Theory & Practice of Industrial Pharmacy),
Aulton's Pharmaceutics, Indian Pharmacopoeia, Block's Disinfection,
Sterilization & Preservation.
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml


# ----------------------------------------------------------------------
# STYLING HELPERS (reused from the user's established template)
# ----------------------------------------------------------------------
def set_cell_shading(cell, color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)


def add_table_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}/>')
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:color="2E4057"/>'
        f'<w:left w:val="single" w:sz="6" w:color="2E4057"/>'
        f'<w:bottom w:val="single" w:sz="6" w:color="2E4057"/>'
        f'<w:right w:val="single" w:sz="6" w:color="2E4057"/>'
        f'<w:insideH w:val="single" w:sz="4" w:color="2E4057"/>'
        f'<w:insideV w:val="single" w:sz="4" w:color="2E4057"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)


def create_styled_table(doc, headers, rows, header_color="1B4F72"):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    add_table_borders(table)

    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}/>')
    cellMargin = parse_xml(
        f'<w:tblCellMar {nsdecls("w")}>'
        f'<w:top w:w="20" w:type="dxa"/>'
        f'<w:left w:w="40" w:type="dxa"/>'
        f'<w:bottom w:w="20" w:type="dxa"/>'
        f'<w:right w:w="40" w:type="dxa"/>'
        f'</w:tblCellMar>'
    )
    tblPr.append(cellMargin)

    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        run = p.add_run(header)
        run.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.size = Pt(8.5)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_cell_shading(cell, header_color)

    for row_idx, row_data in enumerate(rows):
        for col_idx, cell_text in enumerate(row_data):
            cell = table.rows[row_idx + 1].cells[col_idx]
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            run = p.add_run(str(cell_text))
            run.font.size = Pt(8)
            if row_idx % 2 == 0:
                set_cell_shading(cell, "EBF5FB")
    return table


def add_highlight_box(doc, title, content, color="FEF9E7", border_color="F39C12"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.rows[0].cells[0]
    set_cell_shading(cell, color)

    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMargin = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="30" w:type="dxa"/>'
        f'<w:left w:w="60" w:type="dxa"/>'
        f'<w:bottom w:w="30" w:type="dxa"/>'
        f'<w:right w:w="60" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMargin)

    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="12" w:color="{border_color}"/>'
        f'<w:bottom w:val="single" w:sz="12" w:color="{border_color}"/>'
        f'<w:left w:val="single" w:sz="12" w:color="{border_color}"/>'
        f'<w:right w:val="single" w:sz="12" w:color="{border_color}"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)

    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.line_spacing = 1.0
    run = p.add_run(f"  {title}")
    run.bold = True
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(0x8B, 0x45, 0x13)

    if isinstance(content, list):
        for item in content:
            p = cell.add_paragraph()
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            run = p.add_run(f"  {item}")
            run.font.size = Pt(8.5)
    else:
        p = cell.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        run = p.add_run(f"  {content}")
        run.font.size = Pt(8.5)


def add_section_divider(doc, color="1B4F72"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.rows[0].cells[0]
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:bottom w:val="single" w:sz="18" w:color="{color}"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)


def add_heading_styled(doc, text, level=1):
    heading = doc.add_heading(text, level=level)
    for run in heading.runs:
        if level == 1:
            run.font.color.rgb = RGBColor(0x1B, 0x4F, 0x72)
            run.font.size = Pt(18)
        elif level == 2:
            run.font.color.rgb = RGBColor(0x15, 0x4F, 0x0B)
            run.font.size = Pt(14)
        elif level == 3:
            run.font.color.rgb = RGBColor(0x6C, 0x3A, 0x83)
            run.font.size = Pt(11)
    return heading


def add_bullet_points(doc, items, bold_prefix=False):
    for item in items:
        p = doc.add_paragraph(style='List Bullet')
        if bold_prefix and ':' in item:
            parts = item.split(':', 1)
            run = p.add_run(parts[0] + ':')
            run.bold = True
            run.font.size = Pt(9)
            run = p.add_run(parts[1])
            run.font.size = Pt(9)
        else:
            run = p.add_run(item)
            run.font.size = Pt(9)


def add_numbered_list(doc, items):
    for item in items:
        p = doc.add_paragraph(style='List Number')
        run = p.add_run(item)
        run.font.size = Pt(9)


def add_body_text(doc, text, bold=False, italic=False):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(9.5)
    run.bold = bold
    run.italic = italic
    return p


def set_columns(section, num):
    sectPr = section._sectPr
    cols = sectPr.makeelement(qn('w:cols'), {})
    cols.set(qn('w:num'), str(num))
    if num > 1:
        cols.set(qn('w:space'), '360')
    sectPr.append(cols)


def new_legal_section(doc, columns=1):
    s = doc.add_section()
    s.page_width = Inches(8.5)
    s.page_height = Inches(14)
    s.top_margin = Cm(1.27)
    s.bottom_margin = Cm(1.27)
    s.left_margin = Cm(1.27)
    s.right_margin = Cm(1.27)
    set_columns(s, columns)
    return s


# ----------------------------------------------------------------------
# TITLE PAGE
# ----------------------------------------------------------------------
def create_title_page(doc):
    doc.add_paragraph()
    doc.add_paragraph()

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("STERILIZATION & DISINFECTION")
    run.bold = True
    run.font.size = Pt(26)
    run.font.color.rgb = RGBColor(0x1B, 0x4F, 0x72)

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Additional High-Yield Notes \u2014 Gap-Filler Edition")
    run.font.size = Pt(17)
    run.font.color.rgb = RGBColor(0x2E, 0x86, 0xC1)
    run.italic = True

    info = doc.add_paragraph()
    info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = info.add_run("Supplement to your existing notes \u2014 covering the topics mock tests love to ask")
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(0x6C, 0x3A, 0x83)

    sources = doc.add_paragraph()
    sources.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = sources.add_run("Sources: Hugo & Russell | Ananthanarayan & Paniker | Lachman | Aulton | Indian Pharmacopoeia")
    run.font.size = Pt(9.5)
    run.italic = True
    run.font.color.rgb = RGBColor(0x56, 0x6D, 0x7E)

    exams = doc.add_paragraph()
    exams.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = exams.add_run("For: GPAT | Drug Inspector | Pharmacist Recruitment | NIPER | University Exams")
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(0x78, 0x28, 0x1F)
    run.bold = True

    doc.add_paragraph()
    add_highlight_box(
        doc,
        "HOW TO USE THIS SUPPLEMENT",
        ["This document deliberately focuses on the DETAILED, NUMERICAL and COMPARISON-BASED areas",
         "that are under-covered in most basic notes but are heavily tested in mock papers:",
         "  \u2022 Sterilization kinetics with worked numericals (D, Z, F, F\u2080, SAL)",
         "  \u2022 Every heat method (pasteurization, tyndallization, inspissation, autoclave types)",
         "  \u2022 Radiation, gaseous (EO/formaldehyde/BPL/plasma) and filtration in exam-depth",
         "  \u2022 Full disinfectant classification + mechanisms + concentrations",
         "  \u2022 Evaluation of disinfectants (Rideal-Walker, Chick-Martin, Kelsey-Sykes)",
         "  \u2022 Sterility testing (IP), biological & chemical indicators",
         "  \u2022 60+ previous-year style MCQs with explanations + quick-revision tables"],
        color="E8F8F5", border_color="1ABC9C")


# ----------------------------------------------------------------------
# SECTION 1 - CORE DEFINITIONS (quick refresher + fine distinctions)
# ----------------------------------------------------------------------
def add_definitions(doc):
    add_heading_styled(doc, "1. KEY DEFINITIONS \u2014 THE FINE DISTINCTIONS", 1)
    add_section_divider(doc)
    add_body_text(doc, "Examiners love the subtle differences between these terms. Learn them as pairs.", italic=True)

    create_styled_table(doc,
        ["Term", "Precise Meaning", "Key Exam Point"],
        [
            ["Sterilization", "Complete destruction / removal of ALL microorganisms including bacterial spores",
             "An ABSOLUTE term \u2014 an object is either sterile or not (no 'partially sterile')"],
            ["Disinfection", "Destruction of vegetative pathogens (not necessarily spores) on inanimate objects",
             "Directed at NON-LIVING surfaces; may not kill spores"],
            ["Antisepsis", "Destruction/inhibition of microbes on LIVING tissue (skin, mucosa)",
             "Antiseptic = used on living tissue; Disinfectant = on inanimate objects"],
            ["Sanitization", "Reducing microbial load to a safe public-health level",
             "Used for utensils, catering equipment (e.g., 99.9% reduction)"],
            ["Decontamination", "Removal/neutralization of contaminants so item is safe to handle",
             "First step before disinfection/sterilization"],
            ["Asepsis", "Techniques/conditions that PREVENT entry of microbes",
             "Medical asepsis vs Surgical asepsis (sterile field)"],
            ["Sepsis / Sepsis", "Presence of pathogens or their toxins in blood/tissue", "Opposite of asepsis"],
            ["-cidal vs -static", "-cidal = KILLS microbes; -static = INHIBITS growth (reversible)",
             "Bactericidal, sporicidal, virucidal, fungicidal vs bacteriostatic"],
            ["Sterilant", "A chemical agent capable of killing spores (achieving sterility)",
             "e.g., glutaraldehyde, EO, H\u2082O\u2082 plasma, peracetic acid"],
            ["Preservative", "Substance preventing microbial growth in a formulation during shelf-life/use",
             "Bacteriostatic in nature; e.g., benzalkonium Cl, parabens, phenylmercuric nitrate"],
        ],
        header_color="1A5276")

    add_highlight_box(doc, "HIGH YIELD: The Resistance Ladder (most \u2192 least resistant)",
                     ["Prions  >  Bacterial spores  >  Coccidia (Cryptosporidium)  >  Mycobacteria  >",
                      "Non-enveloped (small) viruses  >  Fungi  >  Vegetative bacteria  >  Enveloped viruses",
                      "\u2192 A method that kills bacterial SPORES will kill everything below them.",
                      "\u2192 Prions resist normal autoclaving (need 134\u00b0C/18 min pre-vacuum + 1 N NaOH)."],
                     color="FDEDEC", border_color="E74C3C")


# ----------------------------------------------------------------------
# SECTION 2 - STERILIZATION KINETICS (WITH NUMERICALS)
# ----------------------------------------------------------------------
def add_kinetics(doc):
    add_heading_styled(doc, "2. STERILIZATION KINETICS & THERMAL CONCEPTS", 1)
    add_section_divider(doc)
    add_body_text(doc, "Microbial death by heat follows FIRST-ORDER (logarithmic) kinetics \u2014 a constant "
                       "FRACTION (not number) of the population dies per unit time. Hence sterility is "
                       "expressed as a PROBABILITY, never as an absolute zero.")

    add_heading_styled(doc, "2.1 The Core Parameters", 2)
    create_styled_table(doc,
        ["Parameter", "Definition", "Formula / Typical Value", "Exam Note"],
        [
            ["D-value\n(Decimal Reduction Time)",
             "Time (at a constant temp) to kill 90% of the population, i.e., reduce it by 1 log (factor of 10)",
             "D = t / (log N\u2080 \u2212 log N)\nUnit: minutes",
             "Higher D-value = MORE resistant organism. D depends on organism, temp & medium"],
            ["Z-value",
             "The temperature rise (\u00b0C) needed to reduce the D-value to 1/10th (one log)",
             "Typically Z = 10\u00b0C for moist heat (steam)",
             "Z reflects how sensitive D is to temperature; smaller Z = more temp-sensitive"],
            ["F-value",
             "Equivalent time (min) of heating at a stated temperature delivered to a product",
             "F = D(base) \u00d7 (log N\u2080 \u2212 log N)",
             "Lethality expressed at a reference temperature"],
            ["F\u2080-value",
             "Equivalent lethality in minutes delivered at 121\u00b0C with Z = 10\u00b0C",
             "Overkill standard: F\u2080 \u2265 12 minutes",
             "The MOST asked value \u2014 basis of moist-heat cycle design"],
            ["SAL\n(Sterility Assurance Level)",
             "Probability of a single unit being NON-sterile after the process",
             "Pharma standard SAL = 10\u207b\u2076",
             "'10\u207b\u2076' = not more than 1 non-sterile item per 1,000,000 items"],
            ["Inactivation Factor (IF)",
             "Factor by which population is reduced",
             "IF = N\u2080 / N = 10^(t/D)",
             "Links exposure time and D-value to total kill"],
        ],
        header_color="1A5276")

    add_heading_styled(doc, "2.2 Thermal Death Terms (often confused)", 2)
    create_styled_table(doc,
        ["Term", "Definition"],
        [
            ["Thermal Death Time (TDT)", "Minimum TIME required to kill a microbial suspension at a GIVEN temperature"],
            ["Thermal Death Point (TDP)", "Lowest TEMPERATURE that kills all organisms in a suspension in 10 minutes"],
            ["Decimal Reduction Time", "Same as D-value (time for 1 log/90% reduction)"],
        ],
        header_color="6C3483")

    add_highlight_box(doc, "WORKED NUMERICAL 1 \u2014 D-value",
                     ["Q: A population of 10\u2076 spores is reduced to 10\u00b2 after 8 minutes at 121\u00b0C. Find D\u2081\u2082\u2081.",
                      "D = t / (log N\u2080 \u2212 log N) = 8 / (6 \u2212 2) = 8 / 4 = 2 minutes.",
                      "Interpretation: every 2 minutes at 121\u00b0C reduces the population by one log (90%)."],
                     color="EBF5FB", border_color="2E86C1")

    add_highlight_box(doc, "WORKED NUMERICAL 2 \u2014 F\u2080 & sterility",
                     ["Q: Initial bioburden = 10\u00b2 spores/unit, D\u2081\u2082\u2081 = 1.5 min. Time at 121\u00b0C to reach SAL 10\u207b\u2076?",
                      "Total log reduction needed = log(10\u00b2) \u2212 log(10\u207b\u2076) = 2 \u2212 (\u22126) = 8 logs.",
                      "Time = D \u00d7 log reduction = 1.5 \u00d7 8 = 12 minutes  (\u2248 the F\u2080 \u2265 12 overkill rule).",
                      "This is exactly WHY the pharmaceutical overkill standard is F\u2080 = 12 minutes."],
                     color="FEF9E7", border_color="F39C12")

    add_highlight_box(doc, "WORKED NUMERICAL 3 \u2014 Z-value",
                     ["Q: D\u2081\u2082\u2081 = 2 min and D\u2081\u2081\u2081 = 20 min. Find Z.",
                      "D increased 10\u00d7 (2 \u2192 20) when temp fell by (121 \u2212 111) = 10\u00b0C.",
                      "A 10\u00d7 change in D over 10\u00b0C \u21d2 Z = 10\u00b0C."],
                     color="E8F8F5", border_color="1ABC9C")


# ----------------------------------------------------------------------
# SECTION 3 - MOIST HEAT (all methods)
# ----------------------------------------------------------------------
def add_moist_heat(doc):
    add_heading_styled(doc, "3. MOIST HEAT STERILIZATION \u2014 ALL METHODS", 1)
    add_section_divider(doc)
    add_body_text(doc, "Mechanism of kill: moist heat causes IRREVERSIBLE COAGULATION & DENATURATION of "
                       "structural proteins and enzymes. Moist heat is far more efficient than dry heat "
                       "(latent heat of steam + better penetration), so it kills at LOWER temperatures.")

    add_heading_styled(doc, "3.1 Temperature < 100\u00b0C", 2)
    create_styled_table(doc,
        ["Method", "Conditions", "Use / Notes"],
        [
            ["Pasteurization \u2013 Holder (LTHT)", "63\u00b0C for 30 min", "Milk; kills pathogens, NOT spores"],
            ["Pasteurization \u2013 Flash (HTST)", "72\u00b0C for 15 sec", "Rapid; better flavour retention"],
            ["Pasteurization \u2013 UHT", "125\u2013140\u00b0C for 1\u20132 sec", "Long shelf-life 'sterile' milk"],
            ["Inspissation", "80\u201385\u00b0C for 30 min \u00d7 3 days", "Solidifies serum media (Loeffler, LJ medium)"],
            ["Vaccine bath", "60\u00b0C for 1 hr", "Heat-labile vaccine preparation"],
        ],
        header_color="1E8449")

    add_highlight_box(doc, "HIGH YIELD: Why 63\u00b0C for pasteurization?",
                     ["Pasteurization temp is set to kill Coxiella burnetii (Q-fever) \u2014 the MOST heat-resistant",
                      "non-sporing pathogen in milk. Also kills Mycobacterium bovis (TB), Brucella, Salmonella.",
                      "Phosphatase test = checks adequacy of pasteurization (enzyme destroyed if done right)."],
                     color="FDEDEC", border_color="E74C3C")

    add_heading_styled(doc, "3.2 Temperature at 100\u00b0C", 2)
    create_styled_table(doc,
        ["Method", "Conditions", "Notes"],
        [
            ["Boiling", "100\u00b0C for 10\u201330 min", "Kills vegetative forms; NOT reliably sporicidal"],
            ["Tyndallization\n(Fractional / Intermittent)", "100\u00b0C (free steam) 20\u201330 min on 3 successive days",
             "Between heatings, spores germinate \u2192 killed next day. For sugars/gelatin media that can't stand autoclaving"],
            ["Steam at 100\u00b0C (Koch/Arnold)", "Free flowing steam 90 min", "Single exposure; not sporicidal"],
        ],
        header_color="7D3C98")

    add_heading_styled(doc, "3.3 Temperature > 100\u00b0C \u2014 The Autoclave", 2)
    add_body_text(doc, "The autoclave works on the principle that water boils when its vapour pressure equals "
                       "the surrounding pressure; increasing pressure raises the boiling point, giving "
                       "SATURATED STEAM UNDER PRESSURE. It is the steam (not the pressure) that sterilizes.")
    create_styled_table(doc,
        ["Temperature", "Pressure (above atm.)", "Holding Time"],
        [
            ["121\u00b0C", "15 psi (1.05 kg/cm\u00b2)", "15 minutes (standard)"],
            ["126\u00b0C", "20 psi (1.40 kg/cm\u00b2)", "10 minutes"],
            ["134\u00b0C", "30 psi (2.10 kg/cm\u00b2)", "3 minutes"],
            ["115\u00b0C", "10 psi (0.70 kg/cm\u00b2)", "30 minutes"],
        ],
        header_color="1A5276")

    add_bullet_points(doc, [
        "Holding time = penetration time + destruction time + safety margin (NOT just the clock time)",
        "Air must be removed \u2014 trapped air lowers the true temperature of the steam (air is a poor conductor)",
        "Downward-displacement (gravity) autoclave: steam pushes denser air out the bottom drain",
        "Pre-vacuum (high-vacuum) autoclave: pump removes air first \u2192 faster steam penetration (porous loads, drapes)",
        "Used for: aqueous solutions, dressings, surgical instruments, culture media, rubber",
        "NOT used for: oils, powders, greases (steam can't penetrate) \u2192 use dry heat instead"
    ], bold_prefix=False)

    add_highlight_box(doc, "AUTOCLAVE QUALITY CONTROL (very high yield)",
                     ["Biological indicator: Geobacillus stearothermophilus spores (kills at 121\u00b0C \u2192 proves sterility)",
                      "Bowie-Dick test: checks AIR REMOVAL & steam penetration in pre-vacuum autoclaves (not lethality)",
                      "Chemical indicators: Browne's tube (green = sterile), autoclave tape (stripes appear)",
                      "Thermocouples: physical measurement of chamber/load temperature"],
                     color="E8F8F5", border_color="1ABC9C")


# ----------------------------------------------------------------------
# SECTION 4 - DRY HEAT
# ----------------------------------------------------------------------
def add_dry_heat(doc):
    add_heading_styled(doc, "4. DRY HEAT STERILIZATION", 1)
    add_section_divider(doc)
    add_body_text(doc, "Mechanism of kill: dry heat destroys by OXIDATION of cell constituents, protein "
                       "denaturation and toxic effect of raised electrolyte levels. It needs HIGHER "
                       "temperatures and LONGER times than moist heat.")

    create_styled_table(doc,
        ["Method", "Conditions", "Application"],
        [
            ["Red heat", "Heat to redness in flame", "Inoculating loops, wires, forceps tips"],
            ["Flaming", "Pass through flame (no redness)", "Scalpels, mouths of tubes, glass slides"],
            ["Incineration", "Complete burning to ash", "Contaminated waste, carcasses, dressings"],
            ["Hot Air Oven", "160\u00b0C / 2 h, 170\u00b0C / 1 h, 180\u00b0C / 30 min", "Glassware, oils, powders, greases, metal instruments"],
            ["Infrared radiation", "Radiant heat (conveyor)", "Rapid mass sterilization of syringes, catheters"],
        ],
        header_color="1E8449")

    add_highlight_box(doc, "HOT AIR OVEN \u2014 EXAM POINTS",
                     ["Holding temperature/time (IP): 160\u00b0C for 2 hours is the classic combination",
                      "Biological indicator: Bacillus atrophaeus (formerly B. subtilis var. niger) spores",
                      "Must NOT overload; allow hot-air circulation; cool slowly to avoid glassware cracking",
                      "Ideal for moisture-sensitive & steam-impenetrable items: fixed oils, glycerin, liquid",
                      "paraffin, dusting powders, glassware (pipettes, flasks), sharp metal instruments"],
                     color="FEF9E7", border_color="F39C12")

    add_highlight_box(doc, "MOIST vs DRY HEAT \u2014 one-line comparison",
                     ["Moist heat kills by COAGULATION of proteins at LOWER temp (better penetration, latent heat).",
                      "Dry heat kills by OXIDATION at HIGHER temp/longer time (for oils, powders, glassware)."],
                     color="F4ECF7", border_color="8E44AD")


# ----------------------------------------------------------------------
# SECTION 5 - RADIATION
# ----------------------------------------------------------------------
def add_radiation(doc):
    add_heading_styled(doc, "5. RADIATION STERILIZATION", 1)
    add_section_divider(doc)

    add_heading_styled(doc, "5.1 Ionizing Radiation ('Cold Sterilization')", 2)
    create_styled_table(doc,
        ["Feature", "Details"],
        [
            ["Types", "Gamma rays, X-rays, high-energy electron (cathode/beta) beams"],
            ["Sources", "Gamma: Cobalt-60 (chief), Caesium-137;  Electron beam: linear accelerators"],
            ["Sterilizing dose", "25 kGy (= 2.5 Mrad) is the accepted standard dose"],
            ["Mechanism", "Ionization \u2192 free radicals + direct DNA strand damage (high LET, deep penetration)"],
            ["Advantages", "No heat (ideal for heat-labile items), high penetration, done on final packed product"],
            ["Applications", "Disposable plastics (syringes, catheters), sutures, surgical blades, gloves, PPE, some drugs"],
            ["Biological indicator", "Bacillus pumilus spores (classical)"],
        ],
        header_color="1A5276")

    add_highlight_box(doc, "RADIATION DOSE TERMS (food/pharma)",
                     ["Radappertization: high dose (25\u201350 kGy) \u2192 commercial 'sterility'",
                      "Radicidation: lower dose to kill non-spore pathogens (like radiation pasteurization)",
                      "Radurization: low dose to reduce spoilage organisms & extend shelf-life",
                      "Order of resistance to radiation is NOT the same as to heat (e.g., some Deinococcus are radioresistant)."],
                     color="EBF5FB", border_color="2E86C1")

    add_heading_styled(doc, "5.2 Non-Ionizing Radiation", 2)
    create_styled_table(doc,
        ["Type", "Wavelength / Nature", "Mechanism & Use"],
        [
            ["Ultraviolet (UV)", "200\u2013280 nm; germicidal peak \u2248 260\u2013265 nm",
             "Forms THYMINE DIMERS in DNA. Poor penetration \u2192 surface, air (BSC/laminar flow), water disinfection"],
            ["Infrared (IR)", "Longer than visible", "Acts as DRY HEAT (thermal), not a true radiation kill"],
        ],
        header_color="7D3C98")

    add_highlight_box(doc, "UV \u2014 HIGH YIELD",
                     ["DNA absorption maximum \u2248 260 nm \u2014 this is why 254 nm mercury lamps are used.",
                      "Damage: pyrimidine (thymine) dimers block replication.",
                      "Repair: photoreactivation (light-dependent) & excision (dark) repair can reverse UV damage.",
                      "Limitation: cannot penetrate glass, plastic, turbid liquids \u2192 surface/air only, not for deep sterilization."],
                     color="E8F8F5", border_color="1ABC9C")


# ----------------------------------------------------------------------
# SECTION 6 - GASEOUS STERILIZATION
# ----------------------------------------------------------------------
def add_gaseous(doc):
    add_heading_styled(doc, "6. GASEOUS (CHEMICAL VAPOUR) STERILIZATION", 1)
    add_section_divider(doc)

    add_heading_styled(doc, "6.1 Ethylene Oxide (EO / EtO)", 2)
    add_body_text(doc, "The most important low-temperature sterilant for heat- and moisture-sensitive devices. "
                       "EO is an ALKYLATING agent \u2014 it alkylates sulphydryl (-SH), amino, carboxyl and "
                       "hydroxyl groups of proteins and nucleic acids, blocking reproduction.")
    create_styled_table(doc,
        ["Parameter", "Requirement / Note"],
        [
            ["Nature", "Colourless gas, sweet ethereal odour; FLAMMABLE & EXPLOSIVE in air"],
            ["Made non-explosive by", "Diluting with inert gas: CO\u2082 or nitrogen (e.g., 10% EO + 90% CO\u2082)"],
            ["Concentration", "~450\u20131200 mg/L"],
            ["Temperature", "30\u201360\u00b0C (typically 54\u00b0C)"],
            ["Relative humidity", "30\u201360% (moisture essential \u2014 dry spores are resistant)"],
            ["Exposure time", "2\u201348 h depending on load; then AERATION to remove residues"],
            ["Toxic residues", "Ethylene glycol & ethylene chlorohydrin \u2192 must aerate"],
            ["Hazards", "Toxic, mutagenic, carcinogenic, irritant \u2192 needs aeration & monitoring"],
            ["Biological indicator", "Bacillus atrophaeus spores"],
            ["Uses", "Plastics, catheters, sutures, prosthetic heart valves, ventilators, powders, complex devices"],
        ],
        header_color="1A5276")

    add_heading_styled(doc, "6.2 Other Gaseous / Vapour Agents", 2)
    create_styled_table(doc,
        ["Agent", "Key Facts"],
        [
            ["Formaldehyde (gas)", "Alkylating; fumigation of rooms/safety cabinets (with KMnO\u2084 or steam). Formalin = 37\u201340% aqueous solution; paraformaldehyde on heating releases gas"],
            ["Beta-propiolactone (BPL)", "More active than formaldehyde but POOR penetration & CARCINOGENIC. Used to sterilize vaccines, sera, tissue grafts, blood plasma"],
            ["H\u2082O\u2082 gas plasma (STERRAD)", "Low-temp; free radicals from vaporized H\u2082O\u2082 in plasma phase. For heat/moisture-sensitive devices; no toxic residue"],
            ["Peracetic acid vapour", "Strong oxidizer, sporicidal even at low temp; used for endoscopes (STERIS)"],
            ["Chlorine dioxide / Ozone", "Oxidizing gases; ozone for water & some device sterilization"],
        ],
        header_color="1E8449")

    add_highlight_box(doc, "GAS STERILANT MECHANISMS \u2014 remember this split",
                     ["ALKYLATING agents: Ethylene oxide, Formaldehyde, Beta-propiolactone.",
                      "OXIDIZING agents: Hydrogen peroxide plasma, Peracetic acid, Ozone, Chlorine dioxide."],
                     color="F4ECF7", border_color="8E44AD")


# ----------------------------------------------------------------------
# SECTION 7 - FILTRATION
# ----------------------------------------------------------------------
def add_filtration(doc):
    add_heading_styled(doc, "7. STERILIZATION BY FILTRATION", 1)
    add_section_divider(doc)
    add_body_text(doc, "Filtration PHYSICALLY REMOVES microbes rather than killing them \u2014 the method of choice "
                       "for HEAT-LABILE liquids (sera, antibiotic & enzyme solutions, vitamins, hormones) and "
                       "for air. Note: ordinary filters do NOT remove viruses or mycoplasma.")

    create_styled_table(doc,
        ["Filter Type", "Material / Nature", "Notes"],
        [
            ["Membrane filter", "Cellulose acetate/nitrate, PVDF, PTFE, nylon (screen filter)",
             "Sterilizing grade = 0.22 \u00b5m; 0.45 \u00b5m for bioburden reduction. Reusable-checkable integrity"],
            ["Sintered glass filter", "Fused ground glass discs", "Chemically inert, reusable, brittle"],
            ["Seitz filter", "Asbestos + cellulose pad (depth filter)", "Adsorbs organisms; asbestos now largely obsolete"],
            ["Candle filters", "Diatomaceous earth (Berkefeld), unglazed porcelain (Chamberland), (Mandler)",
             "Traditional depth filters for water/fluids"],
            ["HEPA filter", "Pleated glass-fibre", "Removes 99.97% of particles \u2265 0.3 \u00b5m \u2192 laminar flow / BSC air"],
        ],
        header_color="7D3C98")

    add_highlight_box(doc, "FILTRATION \u2014 HIGH YIELD NUMBERS & TESTS",
                     ["Sterilizing membrane pore size = 0.22 \u00b5m (also written 0.2 \u00b5m).",
                      "0.45 \u00b5m does NOT guarantee sterility (some small organisms pass).",
                      "HEPA = 99.97% efficiency at the most-penetrating size 0.3 \u00b5m.",
                      "Integrity tests: Bubble point test, Pressure hold / diffusion test.",
                      "Filter validation organism: Brevundimonas diminuta (Pseudomonas diminuta) for 0.22 \u00b5m;",
                      "Serratia marcescens historically for 0.45 \u00b5m.",
                      "Depth filter (traps within matrix) vs Screen/membrane filter (sieves at surface)."],
                     color="FEF9E7", border_color="F39C12")


# ----------------------------------------------------------------------
# SECTION 8 - DISINFECTANTS & ANTISEPTICS (chemical)
# ----------------------------------------------------------------------
def add_disinfectants(doc):
    add_heading_styled(doc, "8. CHEMICAL DISINFECTANTS & ANTISEPTICS", 1)
    add_section_divider(doc)
    add_body_text(doc, "Classify by chemical group \u2014 examiners ask 'which class does agent X belong to' and "
                       "'what is its mechanism'. Master the table below.")

    create_styled_table(doc,
        ["Class", "Examples", "Mechanism", "Uses / Notes"],
        [
            ["Phenolics", "Phenol (carbolic acid \u2013 the standard), cresol (Lysol), chloroxylenol (Dettol), hexachlorophene",
             "Membrane damage + protein denaturation", "Surfaces; phenol is the reference for phenol coefficient"],
            ["Alcohols", "Ethanol (60\u201390%, optimum 70%), isopropanol",
             "Protein denaturation + lipid dissolution (needs water)", "Skin antiseptic; NOT sporicidal; volatile"],
            ["Halogens \u2013 Chlorine", "Hypochlorites (bleach), chloramine, Cl\u2082 gas",
             "Oxidation (hypochlorous acid)", "Water, surfaces; inactivated by organic matter"],
            ["Halogens \u2013 Iodine", "Tincture of iodine, iodophors (povidone-iodine/Betadine)",
             "Oxidation / iodination of proteins", "Skin & wound antiseptic; iodophors are less irritant"],
            ["Aldehydes", "Glutaraldehyde (2%, Cidex), formaldehyde, OPA (0.55%)",
             "ALKYLATION of proteins/nucleic acids", "Glutaraldehyde: cold sterilant/HLD for endoscopes (sporicidal)"],
            ["Oxidizing agents", "Hydrogen peroxide, peracetic acid, potassium permanganate",
             "Free radical oxidation of cell components", "H\u2082O\u2082 & peracetic acid are sporicidal"],
            ["Heavy metals", "Silver nitrate, silver sulfadiazine, mercurials (thiomersal), copper",
             "Protein precipitation; OLIGODYNAMIC action", "AgNO\u2083 (Cred\u00e9's \u2013 ophthalmia neonatorum); burns (Ag-sulfadiazine)"],
            ["Surface-active agents", "Cationic: benzalkonium chloride, cetrimide, cetylpyridinium",
             "Disrupt cell membrane (surfactant)", "Cationic (QACs) most germicidal; anionic = soaps"],
            ["Biguanides", "Chlorhexidine (Savlon = chlorhexidine + cetrimide)",
             "Membrane disruption + cytoplasm precipitation", "Skin prep, mouthwash, surgical scrub"],
            ["Dyes", "Aniline dyes (brilliant/malachite green), acridine dyes (acriflavine, proflavine)",
             "Interfere with nucleic acid / cell wall", "Selective for Gram-positive; wound antiseptics"],
            ["Acids / Alkalis", "Benzoic, boric, sorbic acids; strong alkalis",
             "pH-mediated protein/enzyme damage", "Preservatives; food; laboratory decontamination"],
            ["Gaseous agents", "EO, formaldehyde, BPL (see Section 6)", "Alkylation / oxidation", "Heat-labile devices"],
        ],
        header_color="1A5276")

    add_highlight_box(doc, "QUATERNARY AMMONIUM COMPOUNDS (QACs) \u2014 favourite MCQ trap",
                     ["Cationic surfactants (benzalkonium chloride, cetrimide) \u2014 most active surface-active class.",
                      "INACTIVATED by: soaps/anionic detergents, hard water, organic matter, cotton/gauze.",
                      "Poor against: Pseudomonas, Mycobacterium, bacterial spores, non-enveloped viruses.",
                      "Pseudomonas can actually GROW in weak QAC solutions \u2014 a classic exam point."],
                     color="FDEDEC", border_color="E74C3C")

    add_highlight_box(doc, "AGENTS THAT ARE SPORICIDAL (i.e., true sterilants)",
                     ["Glutaraldehyde (2%), Formaldehyde, Ethylene oxide, Hydrogen peroxide, Peracetic acid,",
                      "Chlorine dioxide, high-concentration hypochlorite. (Alcohols & QACs are NOT sporicidal.)"],
                     color="E8F8F5", border_color="1ABC9C")

    add_heading_styled(doc, "8.1 Factors Affecting Disinfectant Action", 2)
    add_bullet_points(doc, [
        "Concentration & contact time: higher concentration/longer time = greater kill (except alcohol needs water)",
        "Temperature: activity generally increases with temperature",
        "pH: affects the degree of ionization and hence activity of the agent",
        "Organic matter (blood, pus, faeces): reduces activity (esp. chlorine, QACs) \u2192 clean before disinfecting",
        "Microbial load (bioburden) & type: more organisms / spores = harder to kill",
        "Nature of surface & presence of biofilm: biofilms are highly protective"
    ], bold_prefix=True)


# ----------------------------------------------------------------------
# SECTION 9 - EVALUATION OF DISINFECTANTS
# ----------------------------------------------------------------------
def add_evaluation(doc):
    add_heading_styled(doc, "9. EVALUATION OF DISINFECTANTS", 1)
    add_section_divider(doc)
    add_body_text(doc, "This section is the SINGLE most common 'gap' in students' notes and a favourite for "
                       "mock-test surprises. Learn the test names, organisms and what each measures.")

    create_styled_table(doc,
        ["Test", "Principle / What it Measures", "Test Organism", "Key Point"],
        [
            ["Phenol Coefficient \u2013 Rideal-Walker (RW) method",
             "Ratio of the highest dilution of test disinfectant to that of phenol killing the organism in a set time (7.5 min but not 5 min)",
             "Salmonella typhi",
             "NO organic matter used \u2192 gives an over-optimistic (high) value"],
            ["Chick-Martin method",
             "Same idea BUT performed in presence of ORGANIC matter (yeast suspension / dried faeces)",
             "Salmonella typhi (or S. aureus)",
             "More realistic (lower) coefficient than RW"],
            ["Kelsey-Sykes (Capacity) test",
             "Capacity of a disinfectant to retain activity when repeatedly challenged with fresh culture",
             "Ps. aeruginosa, Proteus, E. coli, S. aureus",
             "In-use style; gives a recommended use-dilution"],
            ["Use-dilution test (AOAC)",
             "Determines maximum dilution that still kills on carriers (US official method)",
             "S. choleraesuis, S. aureus, Ps. aeruginosa",
             "Carrier (steel ring) method"],
            ["In-use test",
             "Tests the actual in-use diluted disinfectant from the ward for viable organisms",
             "Environmental isolates",
             "Detects contaminated / exhausted disinfectant in practice"],
        ],
        header_color="1A5276")

    add_highlight_box(doc, "PHENOL COEFFICIENT \u2014 how to interpret",
                     ["Phenol coefficient = (dilution of disinfectant killing in time t) / (dilution of phenol killing in time t).",
                      "PC > 1  \u2192 disinfectant is MORE potent than phenol.",
                      "PC < 1  \u2192 LESS potent than phenol.",
                      "PC = 1  \u2192 equal to phenol.",
                      "Rideal-Walker uses S. typhi and NO organic load; Chick-Martin ADDS organic matter."],
                     color="FEF9E7", border_color="F39C12")

    add_highlight_box(doc, "WORKED NUMERICAL \u2014 Phenol coefficient",
                     ["Disinfectant kills at a dilution of 1:300; phenol kills at 1:100 (same time & organism).",
                      "PC = 300 / 100 = 3.0  \u2192 the disinfectant is 3\u00d7 as potent as phenol."],
                     color="EBF5FB", border_color="2E86C1")


# ----------------------------------------------------------------------
# SECTION 10 - STERILITY TESTING & INDICATORS
# ----------------------------------------------------------------------
def add_sterility_testing(doc):
    add_heading_styled(doc, "10. STERILITY TESTING & VALIDATION (IP/USP)", 1)
    add_section_divider(doc)
    add_body_text(doc, "Sterility testing confirms the ABSENCE of viable organisms in a sterilized product. "
                       "Two official methods: (1) Membrane filtration (preferred) and (2) Direct inoculation.")

    create_styled_table(doc,
        ["Medium", "Detects", "Incubation Temperature", "Duration"],
        [
            ["Fluid Thioglycollate Medium (FTM)", "Anaerobic + aerobic bacteria", "30\u201335\u00b0C", "14 days"],
            ["Soybean-Casein Digest Medium (SCDM / TSB)", "Fungi + aerobic bacteria", "20\u201325\u00b0C", "14 days"],
        ],
        header_color="1E8449")

    add_bullet_points(doc, [
        "Membrane filtration: sample filtered (0.45 \u00b5m), membrane washed & transferred to media \u2192 best for antibiotics/oils (removes inhibitors)",
        "Direct inoculation: product added directly to media (used when filtration not feasible)",
        "Incubation period: 14 days; observe for turbidity (growth)",
        "Positive & negative controls must be run; aseptic technique / laminar flow essential",
        "A single non-sterile unit \u2192 the batch fails (subject to retest rules)"
    ], bold_prefix=False)

    add_heading_styled(doc, "10.1 Biological Indicators (memorize the organism per method)", 2)
    create_styled_table(doc,
        ["Sterilization Method", "Biological Indicator (spore)"],
        [
            ["Moist heat / Autoclave (121\u00b0C)", "Geobacillus stearothermophilus (formerly Bacillus stearothermophilus)"],
            ["Dry heat / Hot air oven", "Bacillus atrophaeus (formerly B. subtilis var. niger)"],
            ["Ethylene oxide gas", "Bacillus atrophaeus"],
            ["Ionizing radiation", "Bacillus pumilus"],
            ["Filtration (validation)", "Brevundimonas diminuta (Pseudomonas diminuta)"],
            ["Low-temp H\u2082O\u2082 plasma", "Geobacillus stearothermophilus"],
        ],
        header_color="6C3483")

    add_heading_styled(doc, "10.2 Chemical Indicators", 2)
    add_bullet_points(doc, [
        "Bowie-Dick test: air removal / steam penetration test for pre-vacuum autoclaves",
        "Browne's tube: liquid changes colour (red \u2192 green) when correct time-temperature reached",
        "Autoclave/indicator tape: diagonal stripes develop \u2014 shows a pack was PROCESSED (not that it is sterile)",
        "Integrating indicators (Class 5) & emulating indicators (Class 6): respond to all critical variables"
    ], bold_prefix=False)

    add_highlight_box(doc, "CHEMICAL vs BIOLOGICAL INDICATOR \u2014 don't confuse",
                     ["Chemical indicator = shows the item was EXPOSED to the process (a colour/physical change).",
                      "Biological indicator = uses resistant SPORES to PROVE microbial kill (the gold standard).",
                      "'Tape turned black' means processed, NOT necessarily sterile \u2014 classic MCQ trick."],
                     color="FDEDEC", border_color="E74C3C")


# ----------------------------------------------------------------------
# SECTION 11 - MCQs (two-column)
# ----------------------------------------------------------------------
def add_mcq_section(doc):
    new_legal_section(doc, columns=2)
    add_heading_styled(doc, "11. PREVIOUS-YEAR STYLE MCQs (GPAT/Drug Inspector)", 1)
    add_section_divider(doc)
    add_body_text(doc, "60+ MCQs focused on the gap topics above. Each has the answer and a short explanation.",
                  bold=True)

    mcqs = [
        ("Q1. The D-value of an organism is the time required to:",
         "(a) Kill 100% (b) Reduce population by 90% (c) Reduce by 50% (d) Double the population",
         "Answer: (b) Reduce population by 90% (1 log)",
         "D-value (decimal reduction time) = time for a 1-log (10-fold) reduction at a constant temperature."),

        ("Q2. F\u2080 value is the equivalent lethality (min) delivered at:",
         "(a) 100\u00b0C (b) 115\u00b0C (c) 121\u00b0C with Z=10\u00b0C (d) 134\u00b0C",
         "Answer: (c) 121\u00b0C with Z = 10\u00b0C",
         "F\u2080 is the reference lethality at 121\u00b0C assuming Z = 10\u00b0C; overkill standard is F\u2080 \u2265 12 min."),

        ("Q3. Sterility Assurance Level (SAL) for pharmaceutical products is:",
         "(a) 10\u207b\u00b3 (b) 10\u207b\u2076 (c) 10\u207b\u00b9 (d) 100%",
         "Answer: (b) 10\u207b\u2076",
         "SAL 10\u207b\u2076 = probability of not more than one non-sterile unit per million units."),

        ("Q4. Z-value is defined as the temperature change that alters D-value by:",
         "(a) 2 times (b) 10 times (c) 50% (d) 100 times",
         "Answer: (b) 10 times (one log)",
         "Z-value = \u00b0C rise needed to reduce the D-value to one-tenth. For steam it is typically 10\u00b0C."),

        ("Q5. The standard sterilizing dose for radiation sterilization is:",
         "(a) 2.5 kGy (b) 25 kGy (c) 250 kGy (d) 0.25 kGy",
         "Answer: (b) 25 kGy",
         "25 kGy (2.5 Mrad) is the accepted sterilizing dose for ionizing radiation."),

        ("Q6. The chief source of gamma radiation for sterilization is:",
         "(a) Cobalt-60 (b) Uranium-235 (c) Radium-226 (d) Iodine-131",
         "Answer: (a) Cobalt-60",
         "Cobalt-60 is the principal gamma source; Caesium-137 is an alternative."),

        ("Q7. UV radiation kills microbes primarily by forming:",
         "(a) Free chlorine (b) Thymine dimers (c) Ozone (d) Peroxide",
         "Answer: (b) Thymine dimers in DNA",
         "UV (peak ~260 nm) creates pyrimidine (thymine) dimers, blocking DNA replication."),

        ("Q8. Germicidal UV lamps emit maximally near:",
         "(a) 190 nm (b) 254 nm (c) 365 nm (d) 400 nm",
         "Answer: (b) 254 nm",
         "Low-pressure mercury lamps emit ~254 nm, close to the DNA absorption max (~260 nm)."),

        ("Q9. Ethylene oxide sterilizes by:",
         "(a) Oxidation (b) Alkylation (c) Coagulation (d) Chelation",
         "Answer: (b) Alkylation",
         "EO alkylates -SH, -NH\u2082, -COOH and -OH groups of proteins & nucleic acids."),

        ("Q10. EO is made non-explosive by mixing with:",
         "(a) Oxygen (b) CO\u2082 or nitrogen (c) Hydrogen (d) Methane",
         "Answer: (b) CO\u2082 or nitrogen",
         "Inert diluents (CO\u2082/N\u2082, formerly fluorocarbons) prevent EO's flammability/explosivity."),

        ("Q11. Toxic residue of ethylene oxide sterilization includes:",
         "(a) Ethylene glycol & ethylene chlorohydrin (b) Formic acid (c) Methanol (d) Acetone",
         "Answer: (a) Ethylene glycol & ethylene chlorohydrin",
         "These residues necessitate a post-cycle aeration step."),

        ("Q12. Which humidity is required for effective EO sterilization?",
         "(a) 0% (b) 30\u201360% (c) 90\u2013100% (d) Humidity is irrelevant",
         "Answer: (b) 30\u201360% RH",
         "Moisture is essential; dry spores are highly resistant to EO."),

        ("Q13. Biological indicator for moist heat (autoclave) is:",
         "(a) Bacillus atrophaeus (b) Geobacillus stearothermophilus (c) Bacillus pumilus (d) Clostridium tetani",
         "Answer: (b) Geobacillus stearothermophilus",
         "Its spores are highly heat-resistant and killed at 121\u00b0C, validating the autoclave."),

        ("Q14. Biological indicator for dry heat & EO is:",
         "(a) G. stearothermophilus (b) Bacillus atrophaeus (c) Bacillus pumilus (d) E. coli",
         "Answer: (b) Bacillus atrophaeus (formerly B. subtilis var. niger)",
         "Same organism is used for dry heat and ethylene oxide validation."),

        ("Q15. Biological indicator for radiation sterilization is:",
         "(a) B. pumilus (b) G. stearothermophilus (c) B. atrophaeus (d) S. aureus",
         "Answer: (a) Bacillus pumilus",
         "Classical biological indicator for ionizing radiation."),

        ("Q16. Autoclave standard conditions are:",
         "(a) 100\u00b0C/10 psi/10 min (b) 121\u00b0C/15 psi/15 min (c) 160\u00b0C/2 h (d) 134\u00b0C/5 psi/3 min",
         "Answer: (b) 121\u00b0C, 15 psi, 15 min",
         "Saturated steam under pressure; it is the steam (latent heat), not pressure, that sterilizes."),

        ("Q17. What actually sterilizes in an autoclave?",
         "(a) Pressure (b) Dry air (c) Saturated steam (d) Vacuum",
         "Answer: (c) Saturated steam (moist heat)",
         "Pressure only raises the boiling point; steam provides latent heat & penetration."),

        ("Q18. The Bowie-Dick test checks:",
         "(a) Sterility (b) Air removal/steam penetration (c) Spore death (d) Pressure",
         "Answer: (b) Air removal & steam penetration",
         "It is a pre-vacuum autoclave function test, not a lethality/sterility test."),

        ("Q19. Hot air oven standard condition (IP):",
         "(a) 121\u00b0C/15 min (b) 160\u00b0C/2 h (c) 100\u00b0C/30 min (d) 63\u00b0C/30 min",
         "Answer: (b) 160\u00b0C for 2 hours",
         "Also 170\u00b0C/1 h or 180\u00b0C/30 min; kills by oxidation."),

        ("Q20. Dry heat is preferred for:",
         "(a) Aqueous injections (b) Oils, powders & glassware (c) Rubber (d) Culture media",
         "Answer: (b) Oils, powders & glassware",
         "Steam cannot penetrate oils/powders \u2192 dry heat used."),

        ("Q21. Pasteurization (holder method) conditions:",
         "(a) 63\u00b0C/30 min (b) 100\u00b0C/10 min (c) 121\u00b0C/15 min (d) 72\u00b0C/30 min",
         "Answer: (a) 63\u00b0C for 30 min (LTHT)",
         "Flash/HTST = 72\u00b0C/15 sec; UHT = 125\u2013140\u00b0C/1\u20132 sec."),

        ("Q22. Pasteurization temperature is set to kill which resistant pathogen?",
         "(a) E. coli (b) Coxiella burnetii (c) Staph. aureus (d) Lactobacillus",
         "Answer: (b) Coxiella burnetii",
         "The most heat-resistant non-sporing pathogen in milk."),

        ("Q23. Tyndallization is:",
         "(a) 100\u00b0C for 20\u201330 min on 3 successive days (b) 63\u00b0C/30 min (c) 160\u00b0C/2 h (d) 121\u00b0C/15 min",
         "Answer: (a) Intermittent 100\u00b0C \u00d7 3 days",
         "Also called fractional/intermittent sterilization; spores germinate between heatings then are killed."),

        ("Q24. Inspissation is used to sterilize/solidify:",
         "(a) Water (b) Serum-containing media (Loeffler, LJ) (c) Oils (d) Glassware",
         "Answer: (b) Serum media",
         "80\u201385\u00b0C for 30 min on 3 successive days."),

        ("Q25. Sterilizing-grade membrane filter pore size:",
         "(a) 0.45 \u00b5m (b) 0.22 \u00b5m (c) 1.2 \u00b5m (d) 5 \u00b5m",
         "Answer: (b) 0.22 \u00b5m",
         "0.45 \u00b5m does not guarantee removal of the smallest bacteria."),

        ("Q26. Filter validation is done using:",
         "(a) E. coli (b) Brevundimonas diminuta (c) S. aureus (d) B. subtilis",
         "Answer: (b) Brevundimonas (Pseudomonas) diminuta",
         "Small size makes it the challenge organism for 0.22 \u00b5m filters."),

        ("Q27. HEPA filters remove particles \u2265 0.3 \u00b5m with efficiency:",
         "(a) 90% (b) 95% (c) 99.97% (d) 100%",
         "Answer: (c) 99.97%",
         "HEPA supplies particle-free air to laminar-flow benches and BSCs."),

        ("Q28. Membrane filter integrity is checked by:",
         "(a) Bubble point test (b) Gram staining (c) pH test (d) Bowie-Dick test",
         "Answer: (a) Bubble point test",
         "Also pressure-hold/diffusion tests confirm integrity."),

        ("Q29. The standard reference disinfectant for phenol coefficient is:",
         "(a) Cresol (b) Phenol (c) Ethanol (d) Chlorhexidine",
         "Answer: (b) Phenol",
         "Phenol coefficient compares a disinfectant's potency to phenol."),

        ("Q30. Rideal-Walker method uses which test organism?",
         "(a) S. aureus (b) Salmonella typhi (c) Ps. aeruginosa (d) E. coli",
         "Answer: (b) Salmonella typhi",
         "RW test is performed WITHOUT added organic matter."),

        ("Q31. Which test evaluates disinfectants in presence of organic matter?",
         "(a) Rideal-Walker (b) Chick-Martin (c) Bubble point (d) Bowie-Dick",
         "Answer: (b) Chick-Martin",
         "Organic matter (yeast/faeces) gives more realistic (lower) coefficients."),

        ("Q32. A phenol coefficient of 3 means the disinfectant is:",
         "(a) 1/3 as active as phenol (b) 3 times as active as phenol (c) Equal to phenol (d) Inactive",
         "Answer: (b) 3 times as active as phenol",
         "PC > 1 = more potent than phenol."),

        ("Q33. The capacity test for disinfectants is the:",
         "(a) Kelsey-Sykes test (b) Rideal-Walker test (c) AOAC test (d) Koch test",
         "Answer: (a) Kelsey-Sykes (capacity) test",
         "Assesses ability to retain activity under repeated microbial challenge."),

        ("Q34. Optimum bactericidal concentration of ethanol is:",
         "(a) 100% (b) 70% (c) 40% (d) 10%",
         "Answer: (b) 70%",
         "Water is needed for protein denaturation; absolute alcohol is less effective."),

        ("Q35. Which agent is NOT sporicidal?",
         "(a) Glutaraldehyde (b) Ethylene oxide (c) 70% ethanol (d) Peracetic acid",
         "Answer: (c) 70% ethanol",
         "Alcohols kill vegetative cells but not spores."),

        ("Q36. 2% glutaraldehyde (Cidex) is chiefly used to:",
         "(a) Sterilize glassware (b) Cold-sterilize endoscopes (c) Purify water (d) Preserve vaccines",
         "Answer: (b) Cold-sterilize endoscopes",
         "High-level disinfectant / chemical sterilant; sporicidal on long contact."),

        ("Q37. Which disinfectant class do benzalkonium chloride and cetrimide belong to?",
         "(a) Phenolics (b) Quaternary ammonium (cationic surfactants) (c) Aldehydes (d) Halogens",
         "Answer: (b) Quaternary ammonium compounds",
         "Cationic surfactants; membrane-disrupting."),

        ("Q38. QACs are INACTIVATED by:",
         "(a) Hard water & soaps (b) Sunlight only (c) Sugar (d) Nothing",
         "Answer: (a) Hard water, soaps/anionic detergents & organic matter",
         "Also weak against Pseudomonas, mycobacteria & spores."),

        ("Q39. Chlorhexidine belongs to which class?",
         "(a) Biguanide (b) Aldehyde (c) Phenol (d) Alcohol",
         "Answer: (a) Biguanide",
         "Savlon = chlorhexidine + cetrimide; used as skin/mucosal antiseptic."),

        ("Q40. Oligodynamic action is shown by:",
         "(a) Heavy metals (silver, copper) (b) Alcohols (c) Phenols (d) Aldehydes",
         "Answer: (a) Heavy metals",
         "Trace amounts of metal ions (Ag, Cu) are antimicrobial \u2014 oligodynamic action."),

        ("Q41. Silver nitrate (Cred\u00e9's method) prevents:",
         "(a) Tetanus (b) Ophthalmia neonatorum (c) TB (d) Rabies",
         "Answer: (b) Ophthalmia neonatorum",
         "1% AgNO\u2083 instilled into newborn eyes against gonococcal conjunctivitis."),

        ("Q42. Povidone-iodine is an example of a(n):",
         "(a) Iodophor (b) Phenol (c) Biguanide (d) Alcohol",
         "Answer: (a) Iodophor",
         "Iodine complexed with a carrier (povidone); less irritant, sustained release."),

        ("Q43. Beta-propiolactone (BPL) is mainly limited by:",
         "(a) Being non-toxic (b) Carcinogenicity & poor penetration (c) High cost only (d) Low activity",
         "Answer: (b) Carcinogenicity & poor penetration",
         "Despite high activity; used for vaccines, sera, tissue grafts."),

        ("Q44. Formalin is:",
         "(a) 37\u201340% aqueous formaldehyde (b) 2% glutaraldehyde (c) 70% ethanol (d) 10% phenol",
         "Answer: (a) 37\u201340% aqueous formaldehyde",
         "Used for fumigation and tissue fixation."),

        ("Q45. STERRAD system uses:",
         "(a) Hydrogen peroxide gas plasma (b) Steam (c) Dry heat (d) UV",
         "Answer: (a) H\u2082O\u2082 gas plasma",
         "Low-temperature sterilization with no toxic residue."),

        ("Q46. Fluid thioglycollate medium in sterility testing detects:",
         "(a) Only fungi (b) Aerobic + anaerobic bacteria (c) Viruses (d) Prions",
         "Answer: (b) Aerobic + anaerobic bacteria",
         "Incubated at 30\u201335\u00b0C for 14 days."),

        ("Q47. Soybean-casein digest medium is incubated at:",
         "(a) 20\u201325\u00b0C (b) 30\u201335\u00b0C (c) 37\u00b0C (d) 55\u00b0C",
         "Answer: (a) 20\u201325\u00b0C",
         "For fungi and aerobic bacteria; 14-day incubation."),

        ("Q48. The preferred sterility-testing method for antibiotic solutions is:",
         "(a) Direct inoculation (b) Membrane filtration (c) Pour plate (d) Streak plate",
         "Answer: (b) Membrane filtration",
         "It removes inhibitory antibiotic before culture."),

        ("Q49. Sterility test incubation period is:",
         "(a) 24 h (b) 48 h (c) 7 days (d) 14 days",
         "Answer: (d) 14 days",
         "Standard incubation to detect slow-growing contaminants."),

        ("Q50. Which is the MOST resistant to sterilization?",
         "(a) Enveloped virus (b) Vegetative bacteria (c) Prions (d) Fungi",
         "Answer: (c) Prions",
         "Prions resist routine autoclaving; need 134\u00b0C/18 min + NaOH."),

        ("Q51. Among microbes, bacterial endospores are killed by all EXCEPT:",
         "(a) Autoclaving (b) Ethylene oxide (c) 70% alcohol (d) Glutaraldehyde",
         "Answer: (c) 70% alcohol",
         "Alcohol is not sporicidal."),

        ("Q52. Incineration is best suited for:",
         "(a) Reusable instruments (b) Contaminated waste/carcasses (c) Milk (d) Injections",
         "Answer: (b) Contaminated waste/carcasses",
         "Complete destruction by burning to ash."),

        ("Q53. Red heat is used to sterilize:",
         "(a) Bacteriological loops & wires (b) Scalpels (c) Glass pipettes (d) Rubber",
         "Answer: (a) Loops & wires",
         "Heated to redness directly in flame."),

        ("Q54. Which chemical indicator only shows a pack was 'processed'?",
         "(a) Autoclave tape (b) Spore strip (c) Thermocouple (d) Bowie-Dick pack",
         "Answer: (a) Autoclave tape",
         "Colour/stripe change indicates exposure, NOT sterility."),

        ("Q55. First-order (logarithmic) death kinetics implies:",
         "(a) Constant number die per unit time (b) Constant fraction die per unit time (c) All die at once (d) None die",
         "Answer: (b) Constant fraction per unit time",
         "Hence sterility is expressed as a probability (SAL)."),

        ("Q56. Peracetic acid is classed as a(n):",
         "(a) Alkylating agent (b) Oxidizing agent (c) Cationic surfactant (d) Dye",
         "Answer: (b) Oxidizing agent",
         "Sporicidal even at low temperature; used for endoscopes."),

        ("Q57. Which pair correctly matches agent \u2192 mechanism?",
         "(a) Glutaraldehyde \u2192 oxidation (b) EO \u2192 alkylation (c) H\u2082O\u2082 \u2192 alkylation (d) Alcohol \u2192 chelation",
         "Answer: (b) Ethylene oxide \u2192 alkylation",
         "Glutaraldehyde/formaldehyde/EO alkylate; H\u2082O\u2082/peracetic acid oxidize."),

        ("Q58. The gas used with EO to prevent explosion was historically a fluorocarbon; now common is:",
         "(a) O\u2082 (b) CO\u2082 or N\u2082 (c) H\u2082 (d) He",
         "Answer: (b) CO\u2082 or N\u2082",
         "Inert diluent gases render the mixture non-flammable."),

        ("Q59. Which method removes rather than kills microbes?",
         "(a) Autoclaving (b) Filtration (c) Radiation (d) EO gas",
         "Answer: (b) Filtration",
         "Physical removal; ideal for heat-labile fluids."),

        ("Q60. Depth filters differ from membrane filters in that they:",
         "(a) Sieve only at the surface (b) Trap organisms within the filter matrix (c) Are always 0.22 \u00b5m (d) Cannot be used for liquids",
         "Answer: (b) Trap within the matrix",
         "Sintered glass/Seitz/candle filters are depth filters; membranes are screen filters."),

        ("Q61. Which is a low-temperature STERILANT (not just a disinfectant)?",
         "(a) 70% ethanol (b) Benzalkonium chloride (c) Ethylene oxide (d) Cetrimide",
         "Answer: (c) Ethylene oxide",
         "EO achieves sterility (sporicidal); alcohols/QACs do not."),

        ("Q62. Ozone and chlorine dioxide sterilize by:",
         "(a) Alkylation (b) Oxidation (c) Coagulation (d) Filtration",
         "Answer: (b) Oxidation",
         "Both are oxidizing gaseous agents."),
    ]

    for q, opts, ans, expl in mcqs:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(q)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0x1B, 0x4F, 0x72)

        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(opts)
        r.font.size = Pt(8)

        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(ans)
        r.bold = True
        r.font.size = Pt(8)
        r.font.color.rgb = RGBColor(0x15, 0x4F, 0x0B)

        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(expl)
        r.italic = True
        r.font.size = Pt(7.5)
        r.font.color.rgb = RGBColor(0x56, 0x6D, 0x7E)


# ----------------------------------------------------------------------
# SECTION 12 - QUICK REVISION
# ----------------------------------------------------------------------
def add_quick_revision(doc):
    new_legal_section(doc, columns=1)
    add_heading_styled(doc, "12. QUICK REVISION \u2014 LAST-MINUTE TABLES", 1)
    add_section_divider(doc)

    add_heading_styled(doc, "Numbers You MUST Remember", 2)
    create_styled_table(doc,
        ["Parameter", "Value"],
        [
            ["Autoclave (standard)", "121\u00b0C, 15 psi, 15 min"],
            ["Autoclave (rapid)", "134\u00b0C, 30 psi, 3 min"],
            ["Hot air oven", "160\u00b0C / 2 h (or 170\u00b0C/1 h, 180\u00b0C/30 min)"],
            ["Pasteurization (holder/LTHT)", "63\u00b0C / 30 min"],
            ["Pasteurization (flash/HTST)", "72\u00b0C / 15 sec"],
            ["Pasteurization (UHT)", "125\u2013140\u00b0C / 1\u20132 sec"],
            ["Tyndallization", "100\u00b0C, 20\u201330 min \u00d7 3 days"],
            ["Inspissation", "80\u201385\u00b0C, 30 min \u00d7 3 days"],
            ["Radiation dose", "25 kGy (2.5 Mrad)"],
            ["UV germicidal peak", "254\u2013265 nm"],
            ["Sterilizing filter pore size", "0.22 \u00b5m"],
            ["HEPA efficiency", "99.97% at 0.3 \u00b5m"],
            ["F\u2080 (overkill)", "\u2265 12 min"],
            ["SAL (pharma)", "10\u207b\u2076"],
            ["Sterility test incubation", "14 days"],
        ],
        header_color="1B4F72")

    add_heading_styled(doc, "Biological Indicators \u2014 rapid recall", 2)
    create_styled_table(doc,
        ["Method", "Indicator Organism"],
        [
            ["Moist heat / autoclave", "Geobacillus stearothermophilus"],
            ["Dry heat & Ethylene oxide", "Bacillus atrophaeus"],
            ["Ionizing radiation", "Bacillus pumilus"],
            ["Filtration validation", "Brevundimonas diminuta"],
        ],
        header_color="6C3483")

    add_heading_styled(doc, "Mechanism Buckets", 2)
    add_highlight_box(doc, "GROUP BY MECHANISM",
                     ["COAGULATION of protein: moist heat (autoclave, pasteurization).",
                      "OXIDATION: dry heat, H\u2082O\u2082, peracetic acid, ozone, chlorine, iodine.",
                      "ALKYLATION: ethylene oxide, formaldehyde, glutaraldehyde, beta-propiolactone.",
                      "MEMBRANE disruption: alcohols, phenols, QACs, chlorhexidine.",
                      "DNA damage: ionizing radiation, UV (thymine dimers).",
                      "PHYSICAL removal: filtration."],
                     color="E8F8F5", border_color="1ABC9C")

    add_heading_styled(doc, "Evaluation Tests \u2014 rapid recall", 2)
    create_styled_table(doc,
        ["Test", "Organism / Feature"],
        [
            ["Rideal-Walker", "S. typhi; NO organic matter (over-estimates)"],
            ["Chick-Martin", "S. typhi/S. aureus; WITH organic matter (realistic)"],
            ["Kelsey-Sykes", "Capacity test under repeated challenge"],
            ["Use-dilution (AOAC)", "Carrier method; S. choleraesuis, S. aureus, Ps. aeruginosa"],
            ["In-use test", "Checks the actual diluted disinfectant in wards"],
        ],
        header_color="1E8449")

    add_highlight_box(doc, "EXAM STRATEGY \u2014 highest-yield for THIS topic",
                     ["1. D / Z / F / F\u2080 / SAL definitions & a simple numerical \u2014 asked almost every paper.",
                      "2. Biological indicator organism for each method \u2014 pure recall marks.",
                      "3. Autoclave vs hot air oven conditions & what each is used for.",
                      "4. Phenol coefficient (RW vs Chick-Martin) \u2014 the classic 'surprise' MCQ.",
                      "5. EO parameters, alkylation, residues, non-explosive mixing.",
                      "6. Filter pore size (0.22 \u00b5m), HEPA 99.97%, validation organism.",
                      "7. Which agents are sporicidal vs not (alcohols/QACs are NOT).",
                      "8. Pasteurization temps + Coxiella burnetii; tyndallization vs inspissation.",
                      "9. Sterility testing media (FTM vs SCDM), temperatures, 14-day incubation.",
                      "10. Resistance ladder: prions > spores > mycobacteria > ... > enveloped viruses."],
                     color="FEF9E7", border_color="F39C12")

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("\u2014 End of Supplement \u2014  Best of luck for your exam!")
    r.italic = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x6C, 0x3A, 0x83)


# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
def main():
    doc = Document()

    for section in doc.sections:
        section.page_width = Inches(8.5)
        section.page_height = Inches(14)
        section.top_margin = Cm(1.27)
        section.bottom_margin = Cm(1.27)
        section.left_margin = Cm(1.27)
        section.right_margin = Cm(1.27)

    style = doc.styles['Normal']
    style.paragraph_format.space_before = Pt(2)
    style.paragraph_format.space_after = Pt(2)
    style.paragraph_format.line_spacing = 1.0
    style.font.size = Pt(9.5)

    for i in range(1, 4):
        hs = doc.styles[f'Heading {i}']
        hs.paragraph_format.space_before = Pt(6)
        hs.paragraph_format.space_after = Pt(3)
        hs.paragraph_format.line_spacing = 1.0

    for style_name in ['List Bullet', 'List Number']:
        try:
            ls = doc.styles[style_name]
            ls.paragraph_format.space_before = Pt(1)
            ls.paragraph_format.space_after = Pt(1)
            ls.paragraph_format.line_spacing = 1.0
        except KeyError:
            pass

    create_title_page(doc)
    add_definitions(doc)
    add_kinetics(doc)
    add_moist_heat(doc)
    add_dry_heat(doc)
    add_radiation(doc)
    add_gaseous(doc)
    add_filtration(doc)
    add_disinfectants(doc)
    add_evaluation(doc)
    add_sterility_testing(doc)
    add_mcq_section(doc)
    add_quick_revision(doc)

    output_path = "Sterilization_and_Disinfection_Additional_Notes.docx"
    doc.save(output_path)
    print(f"Document saved successfully: {output_path}")
    print("Topic: Sterilization & Disinfection (Additional / Gap-Filler Notes)")
    print("Includes: 62 MCQs with explanations + quick-revision tables")
    print("Format: Legal (8.5x14), 1.27cm margins, compact spacing")


if __name__ == "__main__":
    main()
