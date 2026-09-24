"""
build_notes.py
==============
Assembles the complete JKSSB Junior Pharmacist notes book.

Two-pass page numbering
-----------------------
The Table of Contents is a REAL static table with REAL page numbers, not a
field the reader has to refresh.

    Pass 1 : build the book with placeholder page numbers, render it to PDF
             with LibreOffice, and read off the page on which each chapter and
             each section actually starts.
    Pass 2 : rebuild the identical book with the real numbers substituted.

Because the TOC occupies exactly the same number of lines in both passes,
pagination does not shift between them; a verification pass confirms this.
"""

import os
import re
import subprocess
import sys

from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.shared import Cm, Inches, Pt, RGBColor

import content_part1 as P1
import content_part2 as P2
import docx_style as S

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.dirname(HERE)          # the repository root
BOOK_TITLE = "JKSSB Junior Pharmacist \u2014 Health Education & Sterilization"
DOCX_NAME = ("JKSSB_Junior_Pharmacist_Health_Education_and_"
             "Sterilization_Disinfection_Notes.docx")
PDF_NAME = DOCX_NAME.replace(".docx", ".pdf")
SOFFICE = "/opt/libreoffice26.2/program/soffice"


# ---------------------------------------------------------------------------
# THE TABLE OF CONTENTS STRUCTURE
# ---------------------------------------------------------------------------
# (level, label, key)   level 0 = part banner, 1 = chapter, 2 = section
TOC = [
    (0, "PART I \u2014 HEALTH EDUCATION", "PART1"),
    (1, "Chapter 1  \u00b7  Health, Disease and the Foundations of Health Education", "CH1"),
    (2, "1.1  The Concept of Health", "1.1"),
    (2, "1.2  Disease, Illness and Sickness", "1.2"),
    (2, "1.3  Health Promotion and the Ottawa Charter", "1.3"),
    (2, "1.4  Health Education and its Cousins \u2014 Distinguishing the Terms", "1.4"),
    (2, "1.5  Health Education in Primary Health Care", "1.5"),
    (1, "Chapter 2  \u00b7  Health Education \u2014 Definition, Aims, Objectives and Scope",
     "CH2"),
    (2, "2.1  Definitions of Health Education", "2.1"),
    (2, "2.2  Aim and Objectives of Health Education", "2.2"),
    (2, "2.3  Scope and Content of Health Education", "2.3"),
    (2, "2.4  Approaches and Models in Health Education", "2.4"),
    (2, "2.5  Health Education and the Pharmacist", "2.5"),
    (2, "2.6  Benefits and Limitations", "2.6"),
    (1, "Chapter 3  \u00b7  Principles of Health Education", "CH3"),
    (2, "3.1  Motivation in Detail", "3.1"),
    (2, "3.2  Principles of Learning Applied to Health Education", "3.2"),
    (2, "3.3  Barriers to Effective Health Education", "3.3"),
    (1, "Chapter 4  \u00b7  Ethics in Health Education", "CH4"),
    (2, "4.1  The Core Ethical Principles", "4.1"),
    (2, "4.2  Informed Consent in Health Education and Research", "4.2"),
    (2, "4.3  Code of Ethics for the Health Education Profession", "4.3"),
    (2, "4.4  Common Ethical Dilemmas and Pitfalls", "4.4"),
    (2, "4.5  Ethics for the Pharmacist as Health Educator", "4.5"),
    (1, "Chapter 5  \u00b7  The Health Educator \u2014 Attributes, Roles and "
        "Responsibilities", "CH5"),
    (2, "5.1  Attributes / Qualities of a Good Health Educator", "5.1"),
    (2, "5.2  Areas of Responsibility of a Health Educator", "5.2"),
    (2, "5.3  Functions of the Health Educator in the Field", "5.3"),
    (2, "5.4  The Health Education Workforce in India", "5.4"),
    (2, "5.5  Difficulties Faced by the Health Educator", "5.5"),
    (1, "Chapter 6  \u00b7  Communication \u2014 The Vehicle of Health Education", "CH6"),
    (2, "6.1  Aims and Functions of Communication", "6.1"),
    (2, "6.2  Elements of the Communication Process", "6.2"),
    (2, "6.3  Types of Communication", "6.3"),
    (2, "6.4  Barriers to Communication", "6.4"),
    (2, "6.5  The Seven C's of Effective Communication", "6.5"),
    (2, "6.6  Health Communication and BCC", "6.6"),
    (1, "Chapter 7  \u00b7  Essential Steps in Health Education", "CH7"),
    (2, "7.1  Part A \u2014 The Psychological / Behavioural Steps", "7.1"),
    (2, "7.2  Part B \u2014 Steps in Planning a Health Education Programme", "7.2"),
    (2, "7.3  Theories and Models Used to Plan Health Education", "7.3"),
    (2, "7.4  Evaluation of Health Education", "7.4"),
    (1, "Chapter 8  \u00b7  Methods of Health Education", "CH8"),
    (2, "8.1  Individual Approach", "8.1"),
    (2, "8.2  Group Approach", "8.2"),
    (2, "8.3  Mass Approach", "8.3"),
    (2, "8.4  Audio-Visual (AV) Aids", "8.4"),
    (2, "8.5  Choosing the Right Method", "8.5"),
    (2, "8.6  Health Education in Specific Settings", "8.6"),
    (1, "Chapter 9  \u00b7  History, Development and Growth of Health Education in India",
     "CH9"),
    (2, "9.1  The Ancient and Medieval Foundations", "9.1"),
    (2, "9.2  The Colonial Period \u2014 The Beginnings of Organised Health Education",
     "9.2"),
    (2, "9.3  Post-Independence Growth", "9.3"),
    (2, "9.4  The Central Health Education Bureau (CHEB)", "9.4"),
    (2, "9.5  Organisation of Health Education Services in India", "9.5"),
    (2, "9.6  Institutions and Professional Bodies", "9.6"),
    (2, "9.7  Achievements and Continuing Constraints", "9.7"),

    (0, "PART II \u2014 STERILIZATION & DISINFECTION", "PART2"),
    (1, "Chapter 10  \u00b7  Fundamentals and Terminology of Sterilization and "
        "Disinfection", "CH10"),
    (2, "10.1  The Essential Definitions", "10.1"),
    (2, "10.2  Types and Levels of Disinfection", "10.2"),
    (2, "10.3  Order of Microbial Resistance to Germicides", "10.3"),
    (2, "10.4  Kinetics of Microbial Death", "10.4"),
    (2, "10.5  Factors Influencing the Efficacy of Sterilization and Disinfection", "10.5"),
    (2, "10.6  Mechanisms of Antimicrobial Action", "10.6"),
    (2, "10.7  Master Classification of Methods", "10.7"),
    (2, "10.8  Control of Sterilization \u2014 Sterility Indicators", "10.8"),
    (1, "Chapter 11  \u00b7  Physical Methods \u2014 I : Sunlight, Drying and Dry Heat",
     "CH11"),
    (2, "11.1  Sunlight", "11.1"),
    (2, "11.2  Drying (Desiccation)", "11.2"),
    (2, "11.3  Dry Heat \u2014 General Principles", "11.3"),
    (2, "11.4  The Hot Air Oven in Detail", "11.4"),
    (1, "Chapter 12  \u00b7  Physical Methods \u2014 II : Moist Heat and the Autoclave",
     "CH12"),
    (2, "12.1  Moist Heat Below 100 \u00b0C", "12.1"),
    (2, "12.2  Moist Heat At 100 \u00b0C", "12.2"),
    (2, "12.3  Moist Heat Above 100 \u00b0C \u2014 The Autoclave", "12.3"),
    (2, "12.4  Dry Heat versus Moist Heat \u2014 The Comparison Table", "12.4"),
    (1, "Chapter 13  \u00b7  Physical Methods \u2014 III : Radiation and Sonic Energy",
     "CH13"),
    (2, "13.1  Classification of Radiation", "13.1"),
    (2, "13.2  Ultraviolet Radiation", "13.2"),
    (2, "13.3  Ionising Radiation \u2014 'Cold Sterilization'", "13.3"),
    (2, "13.4  Sonic and Ultrasonic Vibration", "13.4"),
    (1, "Chapter 14  \u00b7  Mechanical Methods \u2014 Filtration and Physical Removal",
     "CH14"),
    (2, "14.1  Filtration \u2014 Principle and Indications", "14.1"),
    (2, "14.2  Types of Filters", "14.2"),
    (2, "14.3  Laminar Air Flow and Biological Safety Cabinets", "14.3"),
    (2, "14.4  Other Mechanical Methods", "14.4"),
    (1, "Chapter 15  \u00b7  Chemical Methods of Sterilization and Disinfection", "CH15"),
    (2, "15.1  Properties of an Ideal Disinfectant", "15.1"),
    (2, "15.2  Classification of Chemical Agents", "15.2"),
    (2, "15.3  Alcohols", "15.3"),
    (2, "15.4  Aldehydes", "15.4"),
    (2, "15.5  Phenols and Related Compounds", "15.5"),
    (2, "15.6  Halogens", "15.6"),
    (2, "15.7  Oxidising Agents (Peroxygens)", "15.7"),
    (2, "15.8  Heavy Metals and Their Salts", "15.8"),
    (2, "15.9  Surface-Active Agents (Surfactants / Detergents)", "15.9"),
    (2, "15.10  Dyes", "15.10"),
    (2, "15.11  Acids and Alkalies", "15.11"),
    (2, "15.12  Gaseous Sterilization", "15.12"),
    (2, "15.13  Summary \u2014 Choosing a Chemical Agent", "15.13"),
    (1, "Chapter 16  \u00b7  Sterilization of Syringes, Glasswares, Apparatus and Hospital "
        "Articles", "CH16"),
    (2, "16.1  The Universal Sequence of Reprocessing", "16.1"),
    (2, "16.2  Sterilization of Syringes and Needles", "16.2"),
    (2, "16.3  Sterilization of Glasswares", "16.3"),
    (2, "16.4  Sterilization of Apparatus, Instruments and Other Hospital Articles", "16.4"),
    (2, "16.5  The Central Sterile Supply Department (CSSD)", "16.5"),
    (2, "16.6  Ready Reckoner \u2014 Article versus Method", "16.6"),
    (1, "Chapter 17  \u00b7  Disposal of Contaminated Media and Biomedical Waste "
        "Management", "CH17"),
    (2, "17.1  Disposal of Contaminated Culture Media and Laboratory Material", "17.1"),
    (2, "17.2  Biomedical Waste \u2014 Definition and Magnitude", "17.2"),
    (2, "17.3  Colour Coding and Categories \u2014 BMW Rules, 2016", "17.3"),
    (2, "17.4  Treatment Technologies and Their Standards", "17.4"),
    (2, "17.5  Handling Rules, Duties and Documentation", "17.5"),
    (2, "17.6  Spill Management and Standard Precautions", "17.6"),
    (2, "17.7  Pharmacy-Specific Disposal", "17.7"),
    (1, "Chapter 18  \u00b7  Quick Revision \u2014 Master Tables and Ready Reckoner",
     "CH18"),
    (2, "18.1  Temperature and Time \u2014 The Numbers That Must Be Automatic", "18.1"),
    (2, "18.2  Concentrations to Remember", "18.2"),
    (2, "18.3  Who's Who \u2014 Eponyms and Names", "18.3"),
    (2, "18.4  One-Line Facts Most Often Asked", "18.4"),
    (2, "18.5  Glossary of Terms", "18.5"),
]

#: Text to search for in the rendered PDF to locate each TOC key.
#: Chapters are located by their banner text, sections by their heading text.
SEARCH_TEXT = {
    "PART1": "PART I \u2014 HEALTH EDUCATION",
    "PART2": "PART II \u2014 STERILIZATION & DISINFECTION",
}


def _search_key(level, label, key):
    """The literal string that will appear in the PDF for this TOC entry."""
    if key in SEARCH_TEXT:
        return SEARCH_TEXT[key]
    if level == 1:
        # chapter banner reads:  CHAPTER 7   ESSENTIAL STEPS IN HEALTH EDUCATION
        num = key[2:]
        title = label.split("\u00b7", 1)[1].strip()
        return "CHAPTER %s %s" % (num, title.upper())
    return label


# ---------------------------------------------------------------------------
# COVER AND TOC RENDERING
# ---------------------------------------------------------------------------
def add_cover(doc):
    S.cover_page(
        doc,
        title="Health Education",
        subtitle="&  Sterilization and Disinfection",
        exam="JKSSB \u00b7 Junior Pharmacist Recruitment Examination",
        topics=[
            ("I", "Health Education",
             "Principles \u00b7 Ethics \u00b7 Attributes of the health educator \u00b7 "
             "Essential steps \u00b7 Introduction to the main methods \u00b7 History, "
             "development and growth of health education in India \u00b7 Various methods of "
             "health education"),
            ("II", "Sterilization & Disinfection",
             "Physical, chemical and mechanical methods \u00b7 Disposal of contaminated "
             "media \u00b7 Sterilization of syringes, glasswares and apparatus \u00b7 "
             "Biomedical waste management"),
        ],
        meta_lines=[
            "**Complete theory notes \u2014 no question bank, pure study material**",
            "18 chapters \u00b7 140+ tables and summary boxes \u00b7 A4",
            "__Compiled from standard references: Park's Textbook of Preventive and Social "
            "Medicine; Ananthanarayan & Paniker's Textbook of Microbiology;__",
            "__Bio-Medical Waste Management Rules, 2016; WHO and CDC guidelines on "
            "disinfection and sterilization.__",
        ],
    )
    S.page_break(doc)


def add_toc(doc, pages):
    """
    Render the contents page. `pages` maps key -> page number string.
    A dot-leader tab is used so the page numbers align on the right margin.
    """
    head = doc.add_paragraph()
    head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    head.paragraph_format.space_before = Pt(2)
    head.paragraph_format.space_after = Pt(1)
    S._style_run(head.add_run("TABLE OF CONTENTS"), bold=True, size=Pt(20),
                 color=S.NAVY, font=S.HEAD_FONT)
    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub.paragraph_format.space_after = Pt(6)
    S._style_run(sub.add_run("Chapter-wise index with page numbers"), italic=True,
                 size=Pt(9.5), color=S.GREY, font=S.HEAD_FONT)
    S.rule(doc, color="C9A227", sz=12, space_after=6)

    right = S.usable_width(doc)
    for level, label, key in TOC:
        page = pages.get(key, "\u2014")
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.line_spacing = 1.0
        pf.tab_stops.add_tab_stop(right, WD_TAB_ALIGNMENT.RIGHT,
                                  leader=__import__("docx").enum.text.WD_TAB_LEADER.DOTS)

        if level == 0:
            pf.space_before = Pt(7)
            pf.space_after = Pt(2)
            S.para_shade(p, "0B315E")
            S.para_borders(p, edges=("left",), sz=18, color="C9A227")
            S._style_run(p.add_run("  " + label), bold=True, size=Pt(11.5),
                         color=S.WHITE, font=S.HEAD_FONT)
            S._style_run(p.add_run("\t"), size=Pt(11.5), color=S.WHITE)
            S._style_run(p.add_run(str(page) + "  "), bold=True, size=Pt(11.5),
                         color=S.WHITE, font=S.HEAD_FONT)
        elif level == 1:
            pf.space_before = Pt(3.5)
            pf.space_after = Pt(0.5)
            pf.left_indent = Inches(0.10)
            S._style_run(p.add_run(label), bold=True, size=Pt(10.4), color=S.BLUE,
                         font=S.HEAD_FONT)
            S._style_run(p.add_run("\t"), size=Pt(10.4))
            S._style_run(p.add_run(str(page)), bold=True, size=Pt(10.4), color=S.BLUE,
                         font=S.HEAD_FONT)
        else:
            pf.space_before = Pt(0)
            pf.space_after = Pt(0)
            pf.left_indent = Inches(0.40)
            S._style_run(p.add_run(label), size=Pt(9.3), color=S.BLACK,
                         font=S.BODY_FONT)
            S._style_run(p.add_run("\t"), size=Pt(9.3))
            S._style_run(p.add_run(str(page)), size=Pt(9.3), color=S.GREY,
                         font=S.BODY_FONT)

    S.rule(doc, color="0F4C81", sz=8, space_before=8, space_after=4)
    note = doc.add_paragraph()
    note.alignment = WD_ALIGN_PARAGRAPH.CENTER
    S._style_run(note.add_run("Page numbers above refer to the printed page numbers shown "
                              "in the footer of every page."),
                 italic=True, size=Pt(8.5), color=S.GREY, font=S.HEAD_FONT)
    S.page_break(doc)


def add_how_to_use(doc):
    S.h2(doc, "How to Use These Notes", color=S.NAVY)
    S.para(doc, "The notes are organised as a two-part book that follows the syllabus "
                "wording exactly. Everything is explained in running prose first and then "
                "compressed into a table, so that the first reading builds understanding "
                "and every later reading is a rapid revision from the tables.")
    S.table(doc,
            ["Visual cue", "What it means"],
            [["**Blue chapter banner**", "Start of a new chapter. A page break occurs only "
              "at the end of a chapter, so each chapter reads continuously."],
             ["**Teal underlined heading**", "A major section of the chapter."],
             ["**Green heading with a triangle**", "A sub-section."],
             ["**Blue-shaded box marked DEFINITION**",
              "A definition or principle to be reproduced verbatim."],
             ["**Yellow-shaded box marked MNEMONIC**",
              "A memory aid or a string of numbers worth memorising."],
             ["**Pink-shaded box marked HIGH-YIELD FOR EXAM**",
              "Facts that are asked most often. If time is short, read only these."],
             ["**Violet-shaded box marked REMEMBER**",
              "A clarification, a common confusion, or a practical tip."],
             ["^^Purple bold text^^", "A key term or the name of a concept."],
             ["~~Dark red bold text~~",
              "A number, date, temperature or value that must be recalled exactly."],
             ["**Bold text**", "Emphasis on the examinable part of a sentence."],
             ["__Italic text__", "Scientific names, foreign words and book titles."]],
            header_fill=S.SH_HEADER_BLUE, fractions=[0.30, 0.70])
    S.box(doc, "note",
          ["The two parts are independent \u2014 they may be read in either order.",
           "**Chapter 18 is a pure revision chapter**; read it last, and read it again on "
           "the day before the examination.",
           "No multiple-choice questions are included: this is a study text, by design."])
    S.page_break(doc)


# ---------------------------------------------------------------------------
# BOOK ASSEMBLY
# ---------------------------------------------------------------------------
def build(pages, path):
    doc = S.new_document()
    S.build_footer(doc, BOOK_TITLE)
    S.suppress_first_page_footer(doc)

    add_cover(doc)
    add_toc(doc, pages)
    add_how_to_use(doc)

    S.part_title(doc, "Part I", "Health Education",
                 "Principles \u00b7 Ethics \u00b7 The Health Educator \u00b7 Essential "
                 "Steps \u00b7 Methods \u00b7 Growth in India")
    for i in range(1, 10):
        getattr(P1, "chapter_%02d" % i)(doc)

    S.part_title(doc, "Part II", "Sterilization & Disinfection",
                 "Physical \u00b7 Chemical \u00b7 Mechanical Methods \u00b7 Syringes, "
                 "Glasswares & Apparatus \u00b7 Waste Disposal")
    for i in range(10, 19):
        getattr(P2, "chapter_%d" % i)(doc)

    doc.save(path)
    return path


# ---------------------------------------------------------------------------
# PDF RENDERING AND PAGE-NUMBER EXTRACTION
# ---------------------------------------------------------------------------
def to_pdf(docx_path, workdir):
    subprocess.run(
        [SOFFICE, "--headless", "--norestore", "--convert-to", "pdf",
         "--outdir", workdir, docx_path],
        check=True, capture_output=True, timeout=900,
        env={**os.environ, "HOME": workdir},
    )
    pdf = os.path.join(
        workdir, os.path.basename(docx_path).rsplit(".", 1)[0] + ".pdf")
    if not os.path.exists(pdf):
        raise RuntimeError("LibreOffice did not produce %s" % pdf)
    return pdf


def _norm(s):
    """Collapse whitespace and unify dashes so PDF text can be matched."""
    s = s.replace("\u2014", " ").replace("\u2013", " ").replace("\u2019", "'")
    s = s.replace("\u00b7", " ").replace("\u00a0", " ")
    return re.sub(r"\s+", " ", s).strip().lower()


#: Unique text on the last page of the front matter. Everything at or before
#: this page is cover / contents / how-to-use and must be excluded from the
#: search, otherwise every heading would be "found" on the contents page.
FRONT_MATTER_SENTINEL = "How to Use These Notes"


def _body_start(pages):
    """1-based number of the first page of the book proper."""
    needle = _norm(FRONT_MATTER_SENTINEL)
    last = 0
    for idx, text in enumerate(pages, start=1):
        if needle in text:
            last = idx
    return last + 1 if last else 1


def page_map(pdf_path):
    """Return key -> page number, located by searching the text of each page."""
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)
    pages = [_norm(p.extract_text() or "") for p in reader.pages]
    start = _body_start(pages)

    found, missing = {}, []
    for level, label, key in TOC:
        needle = _norm(_search_key(level, label, key))
        hit = None
        for idx in range(start, len(pages) + 1):
            if needle and needle in pages[idx - 1]:
                hit = idx
                break
        if hit is None:
            # retry on a shortened needle for very long headings that the PDF
            # text extractor may have split across lines
            short = needle[:40]
            for idx in range(start, len(pages) + 1):
                if short and short in pages[idx - 1]:
                    hit = idx
                    break
        if hit is None:
            missing.append((key, label))
            found[key] = "\u2014"
        else:
            found[key] = str(hit)
    return found, missing, len(pages)


def main():
    workdir = os.path.join(HERE, "_work")
    os.makedirs(workdir, exist_ok=True)
    final_docx = os.path.join(OUT_DIR, DOCX_NAME)

    # ---- pass 1 : placeholders (same width as real numbers)
    print("Pass 1: building with placeholder page numbers \u2026")
    placeholders = {key: "00" for _, _, key in TOC}
    draft = os.path.join(workdir, "draft.docx")
    build(placeholders, draft)

    print("Pass 1: rendering to PDF \u2026")
    pdf1 = to_pdf(draft, workdir)
    pages1, missing, total1 = page_map(pdf1)
    print("        %d pages; %d TOC entries located, %d missing"
          % (total1, len(TOC) - len(missing), len(missing)))
    for key, label in missing:
        print("        !! not located: %s  (%s)" % (key, label[:60]))

    # ---- pass 2 : real numbers
    print("Pass 2: rebuilding with real page numbers \u2026")
    build(pages1, final_docx)

    # ---- verification : do the numbers still hold?
    print("Verifying pagination \u2026")
    pdf2 = to_pdf(final_docx, workdir)
    pages2, missing2, total2 = page_map(pdf2)
    drift = {k: (pages1[k], pages2[k]) for k in pages1
             if pages1.get(k) != pages2.get(k)}
    if drift:
        print("        pagination drifted for %d entries; applying pass 3"
              % len(drift))
        for k, (a, b) in list(drift.items())[:10]:
            print("          %s: %s -> %s" % (k, a, b))
        build(pages2, final_docx)
        pdf3 = to_pdf(final_docx, workdir)
        pages3, _, total3 = page_map(pdf3)
        drift3 = {k for k in pages2 if pages2.get(k) != pages3.get(k)}
        print("        after pass 3: %d entries still drifting; total pages %d"
              % (len(drift3), total3))
        final_pdf = pdf3
        total = total3
    else:
        print("        pagination stable at %d pages \u2014 TOC numbers are correct."
              % total2)
        final_pdf = pdf2
        total = total2

    # keep a PDF next to the DOCX for convenience
    import shutil
    shutil.copy(final_pdf, os.path.join(OUT_DIR, PDF_NAME))

    print("\nDONE")
    print("  DOCX : %s" % final_docx)
    print("  PDF  : %s" % os.path.join(OUT_DIR, PDF_NAME))
    print("  Pages: %d" % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
