# -*- coding: utf-8 -*-
"""Offline pagination estimator for the generated DOCX.

Simulates Word layout using Comic Sans MS average metrics and the exact
page/spacing settings used by build_notes.py. Reports a page-count range
(narrow vs wide character-width assumptions).
"""
import sys, os, math
from docx import Document
from docx.oxml.ns import qn
from PIL import Image

DOCX = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "Advances in Drug Delivery System (MPT102T).docx")
FIGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")

# page geometry (points)
PAGE_H = 11 * 72
TOP, BOT = 0.9 * 72, 0.9 * 72
HEADER = 26      # header line + rule
FOOTER = 44      # footer two lines + rule
USABLE_H = PAGE_H - TOP - BOT - HEADER - FOOTER
TEXT_W = (8.5 - 2.0) * 72   # 6.5 in usable width in points


def run_fontsize(p):
    for r in p.runs:
        if r.font.size:
            return r.font.size.pt
    # style default
    return 14.0


def para_height(p, char_w_em):
    pf = p.paragraph_format
    size = run_fontsize(p)
    ls = pf.line_spacing if pf.line_spacing else 1.5
    if not isinstance(ls, float):
        ls = 1.5
    sa = pf.space_after.pt if pf.space_after is not None else 8
    sb = pf.space_before.pt if pf.space_before is not None else 0
    li = pf.left_indent.pt if pf.left_indent is not None else 0
    avail = TEXT_W - max(li, 0)
    text = p.text
    if not text.strip():
        lines = 1
    else:
        char_w = size * char_w_em
        chars_per_line = max(1, int(avail / char_w))
        lines = max(1, math.ceil(len(text) / chars_per_line))
    return lines * size * ls + sa + sb


def table_height(t, char_w_em):
    h = 0
    for row in t.rows:
        row_lines = 1
        for c in row.cells:
            size = 10.5
            for p in c.paragraphs:
                fs = run_fontsize(p)
                size = fs
            # width of this cell
            cw = c.width.pt if c.width else (TEXT_W / len(row.cells))
            char_w = size * char_w_em
            cpl = max(1, int((cw - 12) / char_w))
            txt = c.text
            lines = max(1, math.ceil(len(txt) / cpl)) if txt.strip() else 1
            row_lines = max(row_lines, lines)
        # row height: lines * size*1.1 + cell margins (~7pt top+bottom)
        h += row_lines * 11 * 1.15 + 8
    return h + 6  # trailing spacer


def fig_height(width_in, fname):
    path = os.path.join(FIGDIR, fname)
    ar = 0.6
    if os.path.exists(path):
        w, hh = Image.open(path).size
        ar = hh / w
    return width_in * 72 * ar + 22  # + caption


def estimate(char_w_em):
    doc = Document(DOCX)
    body = doc.element.body
    # map for tables/paras
    from docx.text.paragraph import Paragraph
    from docx.table import Table
    used = 0
    pages = 1
    # track figure widths by scanning paragraphs with images: approximate 4.8in avg
    for child in body.iterchildren():
        tag = child.tag
        if tag == qn('w:p'):
            p = Paragraph(child, doc)
            # page break?
            if 'w:br' in child.xml and 'type="page"' in child.xml:
                pages += 1; used = 0; continue
            # image?
            if child.findall('.//' + qn('a:blip')):
                # estimate figure by drawing extent
                exts = child.findall('.//' + qn('wp:extent'))
                if exts:
                    cx = int(exts[0].get('cx')) / 914400.0  # EMU->in
                    from PIL import Image as _I
                    h = cx * 72 * 0.62 + 4
                else:
                    h = 200
                if used + h > USABLE_H:
                    pages += 1; used = 0
                used += h
                continue
            h = para_height(p, char_w_em)
            if used + h > USABLE_H:
                pages += 1; used = 0
            used += h
        elif tag == qn('w:tbl'):
            t = Table(child, doc)
            h = table_height(t, char_w_em)
            # tables can split; add proportionally
            remaining = USABLE_H - used
            if h <= remaining:
                used += h
            else:
                h -= remaining
                pages += 1 + int(h // USABLE_H)
                used = h % USABLE_H
    return pages


if __name__ == "__main__":
    for label, cw in [("narrow (Arial-like 0.50em)", 0.50),
                      ("medium (0.53em)", 0.53),
                      ("Comic Sans-like wide (0.57em)", 0.57)]:
        print("%-32s -> ~%d pages" % (label, estimate(cw)))
