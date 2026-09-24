"""
build.py — assembles the Home Nursing study book.

Two-pass build:
  pass 1  : build with blank page numbers, render to PDF with LibreOffice,
            read back the real page on which every chapter/section starts
  pass 2+ : rebuild with those page numbers, re-render, and repeat until the
            numbers stop changing (a fixed point).  The Table of Contents
            therefore carries REAL page numbers, not field codes.
"""
import os
import re
import subprocess
import sys

from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.shared import Cm, Pt, RGBColor

import docx_kit as dk
from docx_kit import (BODY_FONT, HEAD_FONT, GREEN, GREY, NAVY, PURPLE, WHITE,
                      HEX_NAVY, HEX_NAVY_LT, USABLE_WIDTH_CM, _el, _para_borders,
                      shade)

import content_a as A
import content_b as B
import content_c as C
import content_d as D
import content_e as E
import content_f as F

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
SOFFICE = "/opt/libreoffice26.2/program/soffice"
DOCNAME = "Home_Nursing_Complete_Notes_JKSSB_Junior_Pharmacist"

CHAPTERS = [
    A.chapter_1, A.chapter_2, A.chapter_3, A.chapter_4, A.chapter_5,
    B.chapter_6, B.chapter_7, B.chapter_8, B.chapter_9,
    C.chapter_10, C.chapter_11, C.chapter_12, C.chapter_13,
    D.chapter_14, D.chapter_15, D.chapter_16, D.chapter_17,
    E.chapter_18, E.chapter_19, E.chapter_20, E.chapter_21,
    F.chapter_22, F.chapter_23, F.chapter_24, F.appendix,
]

# syllabus topic  ->  chapter where it is covered
SYLLABUS_MAP = [
    ("Introduction to Home Nursing", "1"),
    ("Nurse", "2"),
    ("Sick Room", "3"),
    ("Bed Making", "4"),
    ("Patient's Toilet", "5"),
    ("Observation of the Sick", "6"),
    ("Infection", "7"),
    ("Surgical Techniques", "8"),
    ("Diet", "9"),
    ("Medicines", "10"),
    ("Special Conditions & Treatments", "11"),
    ("Bandaging", "12"),
    ("Further Observations", "13"),
    ("Immunity & Infectious Diseases", "14"),
    ("Care of the Aged and Long-term Patient", "15"),
    ("Care of the Mentally Ill / Healthy Patient", "16"),
    ("Special Drugs, their Control & Administration", "17"),
    ("Preparation of the Patient for Operation and the After Care", "18"),
    ("Shock and Blood Transfusion", "19"),
    ("Special Treatment", "20"),
    ("Nursing in Special Diseases", "21"),
    ("The Hospital Services", "22"),
    ("Preparation for Special Treatment", "23"),
    ("Child Birth and Its Management", "24"),
]


# ---------------------------------------------------------------- front matter
def cover(b):
    d = b.doc
    b._p("", after=26)

    p = d.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    shade(p._p, HEX_NAVY)
    r = p.add_run("  COMPLETE STUDY NOTES  ")
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.name = BODY_FONT
    r.font.color.rgb = WHITE

    t = b._p("HOME NURSING", size=Pt(46), bold=True, color=NAVY, font=HEAD_FONT,
             align=WD_ALIGN_PARAGRAPH.CENTER, before=18, after=4)
    _para_borders(t, bottom=(18, HEX_NAVY), top=(18, HEX_NAVY), space=8)

    b._p("Examination-oriented, fully covered, topper's notes",
         size=Pt(12.5), italic=True, color=GREY, font=HEAD_FONT,
         align=WD_ALIGN_PARAGRAPH.CENTER, before=10, after=30)

    b._p("JKSSB  JUNIOR  PHARMACIST", size=Pt(20), bold=True, color=GREEN,
         font=HEAD_FONT, align=WD_ALIGN_PARAGRAPH.CENTER, after=4)
    b._p("Jammu & Kashmir Services Selection Board", size=Pt(11.5), italic=True,
         color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER, after=26)

    b.box("num", [
        "__What this book covers__ — every topic of the Home Nursing section of the syllabus, in the same order as the syllabus:",
        "* Introduction to Home Nursing • Nurse • Sick Room • Bed Making • Patient's Toilet • Observation of the Sick",
        "* Infection • Surgical Techniques • Diet • Medicines • Special Conditions & Treatments • Bandaging",
        "* Further Observations • Immunity & Infectious Diseases • Care of the Aged and the Long-term Patient",
        "* Care of the Mentally Ill Patient • Special Drugs, their Control & Administration",
        "* Preparation of the Patient for Operation and the After Care • Shock and Blood Transfusion",
        "* Special Treatment • Nursing in Special Diseases • The Hospital Services",
        "* Preparation for Special Treatment • Child Birth and Its Management  __+ Rapid Revision Appendix__",
    ], title="24 CHAPTERS  •  25 SECTIONS OF THE SYLLABUS  •  ONE BOOK")

    b._p("", after=16)
    b.box("hy", [
        "* Read a chapter fully once, then revise only the coloured boxes and tables — they carry the examination-worthy facts.",
        "* __Blue boxes__ = definitions.  __Yellow boxes__ = high-yield/most-asked points.  __Purple boxes__ = memory aids.",
        "* __Green boxes__ = practical/clinical points.  __Red boxes__ = cautions and 'never do this'.  __Grey boxes__ = chapter recap.",
        "* Every chapter ends with a __'Chapter at a Glance'__ recap; the book ends with a __Rapid Revision__ appendix (Appendix A).",
        "* Tables are the highest-yield part of this subject — numbers, timings, temperatures, colour codes and schedules are asked directly.",
    ], title="HOW TO USE THIS BOOK")


def syllabus_page(b):
    b._p("Syllabus Coverage Map", size=Pt(22), bold=True, color=NAVY,
         font=HEAD_FONT, after=2, break_before=True)
    _para_borders(b.doc.paragraphs[-1], bottom=(12, HEX_NAVY), space=2)
    b._p("Each topic printed in the official syllabus is mapped to the chapter of this book in which it is covered "
         "in full. Nothing in the syllabus has been left out.",
         size=Pt(10), italic=True, color=GREY, after=8)
    rows = [[t, "Chapter " + c] for t, c in SYLLABUS_MAP]
    rows.append(["Rapid Revision — key facts, figures and one-liners of the whole subject", "Appendix A"])
    b.table(["Syllabus topic", "Covered in"], rows,
            caption=None, align_center_cols=(1,), size=Pt(10))
    b.box("clinical", [
        "__A note on how the subject is examined.__ In the JKSSB Junior Pharmacist paper, Home Nursing questions are "
        "almost always __single-fact recall__: a normal value, a temperature, a position, a colour code, a time interval, "
        "a definition, the 'commonest' or 'best' answer, or the first step in a procedure. Every such fact in this book is "
        "printed in __bold navy__ or inside a coloured box so that it can be picked out in a final revision.",
    ], title="EXAM STRATEGY")


def toc_pages(b, pages):
    """pages: dict tag -> printed page number (or None on the first pass)."""
    b._p("Table of Contents", size=Pt(24), bold=True, color=NAVY,
         font=HEAD_FONT, after=2, break_before=True)
    _para_borders(b.doc.paragraphs[-1], bottom=(12, HEX_NAVY), space=2)
    b._p("Chapter-wise contents with page numbers", size=Pt(10), italic=True,
         color=GREY, after=10)

    def entry(number, title, tag, level):
        p = b.doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(3 if level == 1 else 0.5)
        pf.space_after = Pt(1 if level == 1 else 0.5)
        pf.line_spacing = 1.0
        pf.left_indent = Cm(0 if level == 1 else 0.85)
        pf.tab_stops.add_tab_stop(Cm(USABLE_WIDTH_CM), WD_TAB_ALIGNMENT.RIGHT,
                                  WD_TAB_LEADER.DOTS)
        if level == 1:
            label = ("Appendix " if number == "A" else "Chapter ") + str(number)
            r = p.add_run(label + "   ")
            r.font.size = Pt(9)
            r.font.bold = True
            r.font.name = BODY_FONT
            r.font.color.rgb = GREEN
            r = p.add_run(title)
            r.font.size = Pt(11.5)
            r.font.bold = True
            r.font.name = HEAD_FONT
            r.font.color.rgb = NAVY
        else:
            r = p.add_run("%s  %s" % (number, title))
            r.font.size = Pt(9.5)
            r.font.name = BODY_FONT
            r.font.color.rgb = dk.BODY
        num = pages.get(tag)
        r = p.add_run("\t" + (str(num) if num else "—"))
        r.font.size = Pt(10 if level == 1 else 9.5)
        r.font.bold = (level == 1)
        r.font.name = BODY_FONT
        r.font.color.rgb = NAVY if level == 1 else GREY

    for level, number, title, tag in b.toc_outline:
        entry(number, title, tag, level)


# ---------------------------------------------------------------- build passes
def make_doc(pages, outline):
    b = dk.Book()
    b.footer()
    b.toc_outline = outline
    cover(b)
    syllabus_page(b)
    if outline:
        toc_pages(b, pages)
    for fn in CHAPTERS:
        fn(b)
    return b


def render(path):
    env = dict(os.environ, HOME="/tmp")
    subprocess.run([SOFFICE, "--headless", "--norestore", "--convert-to", "pdf",
                    "--outdir", OUT, path], check=True, env=env,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return os.path.splitext(path)[0] + ".pdf"


def norm(s):
    s = s.replace("\u2014", "-").replace("\u2013", "-").replace("\u2019", "'")
    s = s.replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip()


def page_texts(pdf):
    txt = subprocess.run(["pdftotext", "-enc", "UTF-8", pdf, "-"],
                         capture_output=True, text=True, check=True).stdout
    return [norm(p) for p in txt.split("\f")]


def locate(outline, pdf):
    """Return {tag: printed page number} using the rendered PDF."""
    texts = page_texts(pdf)
    found = {}
    # chapter 1 marks the start of the body; ignore the contents pages
    first = 0
    for i, t in enumerate(texts):
        if "CHAPTER 1 Introduction to Home Nursing" in t:
            first = i
            break
    for level, number, title, tag in outline:
        if level == 1:
            label = ("CHAPTER " + str(number))
            needle = norm("%s %s" % (label, title))[:60]
        else:
            needle = norm("%s %s" % (number, title))[:45]
        for i in range(first, len(texts)):
            if needle in texts[i]:
                found[tag] = i + 1        # printed page == pdf page (continuous)
                break
    return found


def main():
    os.makedirs(OUT, exist_ok=True)
    docx_path = os.path.join(OUT, DOCNAME + ".docx")

    # ---- pass 0: discover the outline (chapters + sections) -----------------
    probe = make_doc({}, [])
    outline = list(probe.toc_entries)
    print("outline: %d chapters, %d sections"
          % (sum(1 for e in outline if e[0] == 1),
             sum(1 for e in outline if e[0] == 2)))

    pages = {}
    for attempt in range(1, 7):
        b = make_doc(pages, outline)
        b.save(docx_path)
        pdf = render(docx_path)
        new = locate(outline, pdf)
        missing = [t for _, _, _, t in outline if t not in new]
        same = (new == pages)
        n_pages = len(page_texts(pdf))
        print("pass %d: %d pages, %d/%d entries located, stable=%s"
              % (attempt, n_pages, len(new), len(outline), same))
        if missing:
            print("   !! not located:", missing[:8])
        if same and attempt > 1:
            break
        pages = new

    # final build with the settled numbers
    b = make_doc(pages, outline)
    b.save(docx_path)
    pdf = render(docx_path)
    final = locate(outline, pdf)
    drift = {k: (pages.get(k), final.get(k)) for k in final if pages.get(k) != final.get(k)}
    print("FINAL: %d pages; TOC mismatches: %d" % (len(page_texts(pdf)), len(drift)))
    if drift:
        print("   drift:", list(drift.items())[:10])
    print("saved:", docx_path)
    return docx_path


if __name__ == "__main__":
    main()
