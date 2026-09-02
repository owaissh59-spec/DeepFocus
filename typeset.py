#!/usr/bin/env python3
"""
Typeset notes (.docx, .md, .txt) into reading-order 7 x 8.5 in pages,
ready to be fed to impose.py.

Margins are small and MIRRORED: odd pages are rectos (right-hand side of
the fold) so their gutter is on the left; even pages are versos and their
gutter is on the right. That keeps text off the fold without wasting the
outer edge.

Usage:
    python typeset.py notes.docx pages.pdf [--title "..."] [--font-size 9.5]
"""

import argparse
import html
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

IN = 72.0
PAGE_W, PAGE_H = 7 * IN, 8.5 * IN

OUTER = 0.34 * IN     # small outer margin
GUTTER = 0.52 * IN    # a little more at the fold
TOP = 0.38 * IN
BOTTOM = 0.42 * IN


# ---------------------------------------------------------------- inline

def inline(text):
    """Convert light markdown emphasis into reportlab paragraph markup."""
    t = html.escape(text, quote=False)
    t = re.sub(r"`([^`]+)`", r'<font face="Courier">\1</font>', t)
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"__(.+?)__", r"<b>\1</b>", t)
    return t


# ---------------------------------------------------------------- readers

def read_docx(path):
    """Flatten a .docx into markdown-ish lines, keeping headings/lists/tables."""
    import docx

    d = docx.Document(path)
    out = []

    for block in _iter_docx_blocks(d):
        if isinstance(block, docx.table.Table):
            rows = [
                [c.text.strip().replace("\n", " ") for c in r.cells]
                for r in block.rows
            ]
            rows = [r for r in rows if any(c for c in r)]
            if not rows:
                continue
            out.append("")
            out.append("| " + " | ".join(rows[0]) + " |")
            out.append("|" + "|".join(["---"] * len(rows[0])) + "|")
            for r in rows[1:]:
                out.append("| " + " | ".join(r) + " |")
            out.append("")
            continue

        text = block.text.strip()
        style = (block.style.name or "") if block.style is not None else ""

        if not text:
            out.append("")
            continue

        m = re.match(r"Heading (\d)", style)
        if m:
            out.append("")
            out.append("#" * min(int(m.group(1)), 4) + " " + text)
            out.append("")
        elif "List Bullet" in style or "List Paragraph" in style:
            out.append("- " + re.sub(r"^[\u2022\-\*\u00b7]\s*", "", text))
        elif "List Number" in style:
            out.append("1. " + re.sub(r"^\d+[\.\)]\s*", "", text))
        elif style in ("Title", "Subtitle"):
            out.append("")
            out.append("# " + text)
            out.append("")
        else:
            out.append(text)
            out.append("")

    return "\n".join(out)


def _iter_docx_blocks(doc):
    """Yield paragraphs and tables in true document order."""
    import docx
    from docx.oxml.ns import qn
    from docx.table import Table as DTable
    from docx.text.paragraph import Paragraph as DPara

    body = doc.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            yield DPara(child, doc)
        elif child.tag == qn("w:tbl"):
            yield DTable(child, doc)


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def load(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".docx":
        return read_docx(path)
    if ext == ".doc":
        sys.exit("error: legacy .doc is not supported -- save as .docx first")
    return read_text(path)


# ---------------------------------------------------------------- styles

def build_styles(base):
    lead = base * 1.28
    body = ParagraphStyle(
        "body",
        fontName="Helvetica",
        fontSize=base,
        leading=lead,
        alignment=TA_LEFT,
        spaceAfter=base * 0.42,
        allowWidows=0,
        allowOrphans=0,
        hyphenationLang="",
    )
    return {
        "body": body,
        "h1": ParagraphStyle(
            "h1", parent=body, fontName="Helvetica-Bold",
            fontSize=base + 4.5, leading=(base + 4.5) * 1.18,
            spaceBefore=base * 0.9, spaceAfter=base * 0.45,
            textColor=colors.HexColor("#000000"),
        ),
        "h2": ParagraphStyle(
            "h2", parent=body, fontName="Helvetica-Bold",
            fontSize=base + 2, leading=(base + 2) * 1.2,
            spaceBefore=base * 0.8, spaceAfter=base * 0.3,
        ),
        "h3": ParagraphStyle(
            "h3", parent=body, fontName="Helvetica-BoldOblique",
            fontSize=base + 0.5, leading=(base + 0.5) * 1.2,
            spaceBefore=base * 0.6, spaceAfter=base * 0.22,
        ),
        "h4": ParagraphStyle(
            "h4", parent=body, fontName="Helvetica-Bold",
            fontSize=base, leading=lead,
            spaceBefore=base * 0.5, spaceAfter=base * 0.16,
        ),
        "li": ParagraphStyle(
            "li", parent=body, spaceAfter=base * 0.16, leading=lead * 0.98
        ),
        "quote": ParagraphStyle(
            "quote", parent=body, leftIndent=10, fontName="Helvetica-Oblique",
            textColor=colors.HexColor("#333333"),
        ),
        "cell": ParagraphStyle(
            "cell", parent=body, fontSize=base - 1.2,
            leading=(base - 1.2) * 1.2, spaceAfter=0,
        ),
        "cellh": ParagraphStyle(
            "cellh", parent=body, fontName="Helvetica-Bold",
            fontSize=base - 1.2, leading=(base - 1.2) * 1.2, spaceAfter=0,
        ),
    }


# ---------------------------------------------------------------- parsing

BULLET = re.compile(r"^(\s*)[-*\u2022\u00b7]\s+(.*)$")
NUMBER = re.compile(r"^(\s*)\d+[\.\)]\s+(.*)$")
HEADING = re.compile(r"^(#{1,4})\s+(.*)$")
RULE = re.compile(r"^\s*([-*_])\s*(\1\s*){2,}$")
TABLE_SEP = re.compile(r"^\s*\|?[\s:\-|]+\|[\s:\-|]*$")


def parse(text, S, avail_w):
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    flow = []
    i = 0
    n = len(lines)

    while i < n:
        raw = lines[i]
        line = raw.rstrip()

        if not line.strip():
            i += 1
            continue

        if RULE.match(line):
            flow.append(Spacer(1, 3))
            flow.append(
                HRFlowable(
                    width="100%", thickness=0.5,
                    color=colors.HexColor("#999999"), spaceAfter=5,
                )
            )
            i += 1
            continue

        m = HEADING.match(line)
        if m:
            lvl = len(m.group(1))
            flow.append(Paragraph(inline(m.group(2)), S[f"h{lvl}"]))
            i += 1
            continue

        # pipe table
        if "|" in line and i + 1 < n and TABLE_SEP.match(lines[i + 1]):
            rows, i = _eat_table(lines, i)
            tbl = _make_table(rows, S, avail_w)
            if tbl is not None:
                flow.append(Spacer(1, 3))
                flow.append(tbl)
                flow.append(Spacer(1, 5))
            continue

        if BULLET.match(line) or NUMBER.match(line):
            items, i, ordered = _eat_list(lines, i)
            flow.append(_make_list(items, S, ordered))
            continue

        if line.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(lines[i].lstrip()[1:].strip())
                i += 1
            flow.append(Paragraph(inline(" ".join(buf)), S["quote"]))
            continue

        # plain paragraph: gather until blank / structural line
        buf = [line.strip()]
        i += 1
        while i < n:
            nxt = lines[i]
            if (
                not nxt.strip()
                or HEADING.match(nxt)
                or BULLET.match(nxt)
                or NUMBER.match(nxt)
                or RULE.match(nxt)
                or nxt.lstrip().startswith(">")
                or ("|" in nxt and i + 1 < n and TABLE_SEP.match(lines[i + 1]))
            ):
                break
            buf.append(nxt.strip())
            i += 1
        flow.append(Paragraph(inline(" ".join(buf)), S["body"]))

    return flow


def _eat_list(lines, i):
    items = []
    ordered = bool(NUMBER.match(lines[i]))
    n = len(lines)
    while i < n:
        line = lines[i].rstrip()
        mb = BULLET.match(line)
        mn = NUMBER.match(line)
        if mb or mn:
            m = mb or mn
            indent = len(m.group(1).expandtabs(4))
            items.append((indent // 2, m.group(2).strip()))
            i += 1
        elif line.strip() and items and not HEADING.match(line):
            # continuation of the previous bullet
            lvl, prev = items[-1]
            items[-1] = (lvl, prev + " " + line.strip())
            i += 1
        else:
            break
    return items, i, ordered


def _make_list(items, S, ordered):
    flowables = []
    for lvl, text in items:
        style = ParagraphStyle(
            f"li{lvl}", parent=S["li"], leftIndent=S["li"].leftIndent + lvl * 11
        )
        flowables.append(ListItem(Paragraph(inline(text), style), leftIndent=12))
    return ListFlowable(
        flowables,
        bulletType="1" if ordered else "bullet",
        start="1" if ordered else None,
        bulletFontSize=S["li"].fontSize - 1,
        leftIndent=13,
        bulletOffsetY=0,
        spaceAfter=S["li"].fontSize * 0.5,
    )


def _eat_table(lines, i):
    header = _split_row(lines[i])
    i += 2  # header + separator
    rows = [header]
    while i < len(lines) and "|" in lines[i] and lines[i].strip():
        rows.append(_split_row(lines[i]))
        i += 1
    return rows, i


def _split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def _make_table(rows, S, avail_w):
    if not rows:
        return None
    ncol = max(len(r) for r in rows)
    if ncol < 1:
        return None
    rows = [r + [""] * (ncol - len(r)) for r in rows]

    data = [[Paragraph(inline(c), S["cellh"]) for c in rows[0]]] + [
        [Paragraph(inline(c), S["cell"]) for c in r] for r in rows[1:]
    ]

    t = Table(data, colWidths=[avail_w / ncol] * ncol, repeatRows=1, hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#888888")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8e8e8")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return t


# ---------------------------------------------------------------- document

class BookDoc(BaseDocTemplate):
    """Alternates recto/verso templates so the gutter mirrors."""

    def handle_pageBegin(self):
        self._handle_pageBegin()
        self._handle_nextPageTemplate("verso" if self.page % 2 else "recto")


def footer(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 7.5)
    canv.setFillColor(colors.HexColor("#666666"))
    recto = doc.page % 2 == 1
    x = PAGE_W - OUTER if recto else OUTER
    canv.drawRightString(x, BOTTOM * 0.45, str(doc.page)) if recto else \
        canv.drawString(x, BOTTOM * 0.45, str(doc.page))
    canv.restoreState()


def typeset(in_path, out_path, font_size=9.5, title=None, pad_to_4=True):
    S = build_styles(font_size)
    text = load(in_path)

    avail_w = PAGE_W - OUTER - GUTTER
    avail_h = PAGE_H - TOP - BOTTOM

    doc = BookDoc(
        out_path,
        pagesize=(PAGE_W, PAGE_H),
        title=title or os.path.splitext(os.path.basename(in_path))[0],
    )
    doc.addPageTemplates(
        [
            PageTemplate(
                id="recto",
                frames=[Frame(GUTTER, BOTTOM, avail_w, avail_h, id="r",
                              leftPadding=0, rightPadding=0,
                              topPadding=0, bottomPadding=0)],
                onPage=footer,
            ),
            PageTemplate(
                id="verso",
                frames=[Frame(OUTER, BOTTOM, avail_w, avail_h, id="v",
                              leftPadding=0, rightPadding=0,
                              topPadding=0, bottomPadding=0)],
                onPage=footer,
            ),
        ]
    )

    flow = []
    if title:
        flow.append(Paragraph(inline(title), S["h1"]))
        flow.append(
            HRFlowable(width="100%", thickness=0.7,
                       color=colors.HexColor("#333333"), spaceAfter=7)
        )
    flow += parse(text, S, avail_w)

    doc.build(flow)

    # pad to a multiple of 4 so the signature is whole sheets
    from pypdf import PdfReader, PdfWriter

    r = PdfReader(out_path)
    real = len(r.pages)
    if pad_to_4 and real % 4:
        w = PdfWriter()
        for p in r.pages:
            w.add_page(p)
        while len(w.pages) % 4:
            w.add_blank_page(width=PAGE_W, height=PAGE_H)
        with open(out_path, "wb") as fh:
            w.write(fh)
        return real, len(w.pages)
    return real, real


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--title", default=None)
    ap.add_argument("--font-size", type=float, default=9.5)
    ap.add_argument("--no-pad", action="store_true")
    a = ap.parse_args()

    real, total = typeset(
        a.input, a.output, a.font_size, a.title, pad_to_4=not a.no_pad
    )
    extra = f"  (+{total - real} blank to fill the signature)" if total != real else ""
    print(f"wrote {a.output}: {total} pages at 7 x 8.5 in{extra}")


if __name__ == "__main__":
    main()
