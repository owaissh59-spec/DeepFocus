# -*- coding: utf-8 -*-
"""Build the First-Aid study-notes book.

Two passes are made:
  pass 1 -> lay out the book with an empty contents page, export to PDF,
            read back the real page number of every heading;
  pass 2 -> rebuild the identical book with those page numbers printed in the
            table of contents.
Because only the digits in the contents change, pagination is unaffected.
"""
import importlib
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bookkit import Book                                    # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("OUT_DIR", HERE)
SOFFICE = "/opt/libreoffice25.8/program/soffice"

CHAPTERS = [
    "ch01_outline",
    "ch02_body",
    "ch03_dressings",
    "ch04_cpr",
    "ch05_wounds",
    "ch06_haemorrhage",
    "ch07_shock",
    "ch08_electric",
    "ch09_artificial_respiration",
    "ch10_asphyxia",
    "ch11_fractures",
    "ch12_unconsciousness",
    "ch13_epilepsy",
    "ch14_poisons",
    "ch15_common_conditions",
    "ch16_transport",
    "ch17_medicines",
    "ch18_appendix",
]

TITLE_LINES = ["FIRST AID", "Complete Study Notes"]


def _modules():
    mods = []
    for name in CHAPTERS:
        path = os.path.join(HERE, name + ".py")
        if os.path.exists(path):
            mods.append(importlib.import_module(name))
    return mods


def render_content(b):
    for m in _modules():
        m.render(b)


def collect_entries():
    dry = Book()
    render_content(dry)
    return dry.toc_entries


def build(page_map=None, entries=None):
    b = Book()
    b.build_running_heads()
    b.cover(
        TITLE_LINES,
        "Complete, Chapter-wise Study Notes for the Whole Syllabus",
        "JKSSB  \u2022  COMPETITIVE EXAMINATION NOTES",
        "Prepared strictly on the prescribed syllabus \u2014 based on St. John "
        "Ambulance, Indian Red Cross Society, AHA/ERC 2020\u201325 resuscitation "
        "guidelines and standard textbooks.",
        ["**Every syllabus topic covered in depth** \u2014 nothing left to a "
         "second book: outline of first aid, structure and functions of the body, "
         "dressings and bandages, CPR, wounds, haemorrhage, shock, electric shock, "
         "artificial respiration, asphyxia, fractures and dislocation, "
         "unconsciousness and fainting, epilepsy and hysteria, poisons and food "
         "poisoning, common conditions, transport of the injured and common "
         "medicines.",
         "**Exam-oriented presentation** \u2014 definitions, classifications, "
         "signs and symptoms, step-by-step management, do's and don'ts, normal "
         "values, and comparison tables in the exact form in which questions are "
         "set.",
         "**Colour-coded learning aids** \u2014 blue Key Point boxes, red Exam "
         "Focus boxes, purple Mnemonic boxes, green Definition boxes and amber "
         "Caution boxes.",
         "**One-line recap** at the end of every chapter for last-minute "
         "revision, plus quick-reference appendices of normal values, first-aid "
         "records, antidotes and abbreviations."])
    entries = entries if entries is not None else collect_entries()
    b.static_toc(entries, page_map,
                 note="Page numbers refer to the printed page numbers shown in "
                      "the footer of this book.")
    render_content(b)
    return b


def to_pdf(docx_path):
    env = dict(os.environ, HOME=os.path.join(OUT_DIR, ".lo_home"))
    subprocess.run([SOFFICE, "--headless", "--norestore", "--convert-to", "pdf",
                    "--outdir", OUT_DIR, docx_path], check=True, env=env,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return os.path.splitext(docx_path)[0] + ".pdf"


def norm(s):
    s = re.sub(r"\s+", " ", s)
    return s.replace("\u2014", "-").replace("\u2013", "-").strip().lower()


def page_numbers(pdf_path, entries):
    """Locate each TOC entry's key text in the PDF and return {key: page}."""
    import fitz
    doc = fitz.open(pdf_path)
    pages = [norm(p.get_text()) for p in doc]
    result, missing = {}, []
    cursor = 0
    for e in entries:
        if not e.get("key"):
            continue
        needle = norm(e["key"])
        found = None
        for i in range(cursor, len(pages)):
            if needle in pages[i]:
                found = i + 1
                break
        if found is None:                      # search from the very beginning
            for i, txt in enumerate(pages):
                if needle in txt:
                    found = i + 1
                    break
        if found is None:
            missing.append(e["key"])
        else:
            result[e["key"]] = found
            cursor = found - 1
    doc.close()
    return result, missing, len(pages)


def main():
    entries = collect_entries()
    tmp = os.path.join(OUT_DIR, "_pass1.docx")
    build(None, entries).save(tmp)
    pdf = to_pdf(tmp)
    pmap, missing, npages = page_numbers(pdf, entries)
    print("pass 1: %d pages, %d/%d headings located"
          % (npages, len(pmap), len([e for e in entries if e.get('key')])))
    for m in missing[:12]:
        print("   NOT FOUND:", m)

    final = os.path.join(OUT_DIR, "First-Aid-Complete-Study-Notes.docx")
    build(pmap, entries).save(final)
    pdf2 = to_pdf(final)
    pmap2, missing2, npages2 = page_numbers(pdf2, entries)
    drift = {k: (pmap[k], pmap2[k]) for k in pmap2
             if k in pmap and pmap[k] != pmap2[k]}
    print("pass 2: %d pages; %d entries drifted" % (npages2, len(drift)))
    for k, v in list(drift.items())[:12]:
        print("   DRIFT:", k, v)
    if drift:                                   # one corrective pass
        build(pmap2, entries).save(final)
        pdf3 = to_pdf(final)
        pmap3, _, npages3 = page_numbers(pdf3, entries)
        drift2 = {k: (pmap2[k], pmap3[k]) for k in pmap3
                  if k in pmap2 and pmap2[k] != pmap3[k]}
        print("pass 3: %d pages; %d entries drifted" % (npages3, len(drift2)))
    for junk in (tmp, os.path.join(OUT_DIR, "_pass1.pdf")):
        if os.path.exists(junk):
            os.remove(junk)
    print("WROTE:", final)


if __name__ == "__main__":
    main()
