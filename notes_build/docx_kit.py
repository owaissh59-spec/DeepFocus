"""
docx_kit.py — Styling toolkit for building an exam-grade, visually rich A4 study book.

Design goals
------------
*  A4 page, tight but readable margins
*  Colour-coded heading hierarchy (chapter / section / sub-section / point-head)
*  Professional tables: shaded header, alternating rows, PROPORTIONAL column
   widths computed from the text each column actually holds
*  Highlight boxes (definition / high-yield / mnemonic / clinical / caution)
*  Footer page numbers  ->  needed for a real page-numbered Table of Contents
*  Page breaks ONLY at the end of a chapter
"""

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ROW_HEIGHT_RULE
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor, Emu

# ----------------------------------------------------------------------------
# Palette
# ----------------------------------------------------------------------------
NAVY = RGBColor(0x14, 0x2C, 0x57)        # chapter titles
GREEN = RGBColor(0x0E, 0x6B, 0x4A)       # section titles
PURPLE = RGBColor(0x6A, 0x1B, 0x7A)      # sub-section titles
MAROON = RGBColor(0x8C, 0x1C, 0x2B)      # point heads
BODY = RGBColor(0x1A, 0x1A, 0x1A)
GREY = RGBColor(0x55, 0x55, 0x55)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

HEX_NAVY = "142C57"
HEX_NAVY_LT = "DCE4F2"
HEX_GREEN = "0E6B4A"
HEX_PURPLE = "6A1B7A"
HEX_ROW_ALT = "F1F5FB"
HEX_TBL_LINE = "A8BAD6"

BOX_STYLES = {
    # key            fill      border    title-colour  default title
    "def":      ("EAF2FB", "2E6DA4", "1B4F82", "DEFINITION"),
    "hy":       ("FFF6DA", "D9A400", "8A6100", "HIGH-YIELD / MOST ASKED"),
    "mnemonic": ("F3EAFB", "7B3FA0", "5C2278", "MEMORY AID"),
    "clinical": ("EAF7EF", "2E8B57", "1B6239", "CLINICAL / PRACTICAL POINT"),
    "caution":  ("FDECEC", "C0392B", "94231A", "CAUTION / NEVER DO THIS"),
    "recap":    ("EFF3F8", "142C57", "142C57", "CHAPTER AT A GLANCE"),
    "num":      ("E9F4F8", "1B7A8C", "125966", "NUMBERS TO REMEMBER"),
}

BODY_FONT = "Calibri"
HEAD_FONT = "Cambria"

BODY_SIZE = Pt(10.5)
TABLE_SIZE = Pt(9)

USABLE_WIDTH_CM = 21.0 - 1.7 - 1.7   # A4 width minus L/R margins


# ----------------------------------------------------------------------------
# low-level xml helpers
# ----------------------------------------------------------------------------
def _el(tag, **attrs):
    if ":" not in tag:
        tag = "w:" + tag
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn("w:" + k), v)
    return e


def shade(element, hex_fill):
    """Apply solid shading to a paragraph-properties or cell-properties owner."""
    pr = element.get_or_add_pPr() if hasattr(element, "get_or_add_pPr") else element
    pr.append(_el("shd", val="clear", color="auto", fill=hex_fill))


def _cell_shade(cell, hex_fill):
    cell._tc.get_or_add_tcPr().append(_el("shd", val="clear", color="auto", fill=hex_fill))


def _para_borders(p, *, left=None, bottom=None, top=None, right=None, space=4):
    pPr = p._p.get_or_add_pPr()
    bd = OxmlElement("w:pBdr")
    for name, spec in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        if spec:
            sz, color = spec
            bd.append(_el(name, val="single", sz=str(sz), space=str(space), color=color))
    pPr.append(bd)


def _cell_margins(cell, top=40, bottom=40, left=70, right=70):
    tcMar = OxmlElement("w:tcMar")
    for name, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        tcMar.append(_el(name, w=str(val), type="dxa"))
    cell._tc.get_or_add_tcPr().append(tcMar)


def _vertical_align(cell, val="center"):
    cell._tc.get_or_add_tcPr().append(_el("vAlign", val=val))


def _keep_with_next(p, on=True):
    pPr = p._p.get_or_add_pPr()
    pPr.append(_el("keepNext", val="1" if on else "0"))


def _cant_split(row):
    row._tr.get_or_add_trPr().append(_el("cantSplit"))


def _repeat_header(row):
    row._tr.get_or_add_trPr().append(_el("tblHeader"))


def field(paragraph, instr, *, size=Pt(9), bold=False, color=GREY, font=BODY_FONT):
    """Insert a Word field (e.g. PAGE, NUMPAGES)."""
    r = paragraph.add_run()
    fld = _el("fldChar", fldCharType="begin")
    r._r.append(fld)
    r2 = paragraph.add_run()
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = instr
    r2._r.append(it)
    r3 = paragraph.add_run()
    r3._r.append(_el("fldChar", fldCharType="end"))
    for rr in (r, r2, r3):
        rr.font.size = size
        rr.font.bold = bold
        rr.font.color.rgb = color
        rr.font.name = font
    return paragraph


# ----------------------------------------------------------------------------
# Column-width engine
# ----------------------------------------------------------------------------
# Approximate mean glyph advance (cm) for Calibri at the table font size (9 pt).
_CHAR_CM = 0.178
_PAD_CM = 0.32            # left + right cell margin + slack
_MIN_COL_CM = 1.20
_MARKUP = ("**", "__", "~", "##")


def _clean(s):
    s = str(s or "")
    for m in ("**", "__", "##"):
        s = s.replace(m, "")
    return s.replace("~", "").replace("* ", "")


def proportional_widths(rows, total_cm=USABLE_WIDTH_CM, header_bonus=1.10):
    """
    Column widths in cm, proportional to the amount of text each column really
    carries.  Two regimes:
      * if every column can show its longest line on one line -> widths are the
        'natural' widths scaled up to fill the page (no wasted space);
      * otherwise widths are shared out by a damped natural width, clamped so
        that no column is narrower than its longest single word (no ugly
        mid-word breaks) and none is wider than it needs (no empty gaps).
    """
    ncols = max(len(r) for r in rows)
    norm = [[_clean(r[i] if i < len(r) else "") for i in range(ncols)] for r in rows]

    nat, mini, hard_max = [], [], []
    for i in range(ncols):
        col = [r[i] for r in norm]
        lens = []
        for j, c in enumerate(col):
            longest_line = max((len(x) for x in c.split("\n")), default=0)
            lens.append(longest_line * (header_bonus if j == 0 else 1.0))
        maxlen = max(lens) if lens else 1.0
        meanlen = (sum(lens) / len(lens)) if lens else 1.0
        blended = 0.70 * maxlen + 0.30 * meanlen
        nat.append(max(blended * _CHAR_CM + _PAD_CM, _MIN_COL_CM))
        hard_max.append(max(maxlen * _CHAR_CM + _PAD_CM, _MIN_COL_CM))
        longest_word = 1
        for c in col:
            for w in c.replace("/", "/ ").replace("-", "- ").replace("(", " (").split():
                longest_word = max(longest_word, len(w))
        mini.append(max(_MIN_COL_CM, min(longest_word * _CHAR_CM + _PAD_CM,
                                         total_cm / ncols * 1.8)))

    if sum(mini) >= total_cm:                      # very cramped: share by minima
        f = total_cm / sum(mini)
        return [m * f for m in mini]

    if sum(nat) <= total_cm:                       # everything fits comfortably
        extra = total_cm - sum(nat)
        s = sum(nat)
        return [n + extra * n / s for n in nat]

    # wrapping regime -------------------------------------------------------
    w = [n ** 0.75 for n in nat]
    s = sum(w)
    widths = [total_cm * x / s for x in w]
    for _ in range(25):
        fixed, free = {}, []
        for i in range(ncols):
            if widths[i] < mini[i]:
                fixed[i] = mini[i]
            elif widths[i] > hard_max[i]:
                fixed[i] = hard_max[i]
            else:
                free.append(i)
        if not fixed:
            break
        remaining = total_cm - sum(fixed.values())
        if not free or remaining <= 0:
            for i in fixed:
                widths[i] = fixed[i]
            break
        base = sum(nat[i] ** 0.75 for i in free)
        new = list(widths)
        for i, v in fixed.items():
            new[i] = v
        for i in free:
            new[i] = remaining * (nat[i] ** 0.75) / base
        if max(abs(new[i] - widths[i]) for i in range(ncols)) < 0.01:
            widths = new
            break
        widths = new
    f = total_cm / sum(widths)
    return [x * f for x in widths]


# ----------------------------------------------------------------------------
# Builder
# ----------------------------------------------------------------------------
class Book:
    def __init__(self):
        self.doc = Document()
        self._setup_page()
        self._setup_styles()
        self.toc_entries = []        # (level, number, title, tag)

    # -------------------------------------------------- page / styles
    def _setup_page(self):
        s = self.doc.sections[0]
        s.page_width = Cm(21.0)
        s.page_height = Cm(29.7)
        s.left_margin = Cm(1.7)
        s.right_margin = Cm(1.7)
        s.top_margin = Cm(1.6)
        s.bottom_margin = Cm(1.5)
        s.header_distance = Cm(0.8)
        s.footer_distance = Cm(0.7)
        self.section = s

    def _setup_styles(self):
        st = self.doc.styles["Normal"]
        st.font.name = BODY_FONT
        st.font.size = BODY_SIZE
        st.font.color.rgb = BODY
        st.element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)
        pf = st.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(2.5)
        pf.line_spacing = 1.02
        pf.widow_control = True

    def footer(self, text="Home Nursing  •  JKSSB Junior Pharmacist"):
        sec = self.section
        sec.different_first_page_header_footer = True
        p = sec.footer.paragraphs[0]
        p.paragraph_format.tab_stops.add_tab_stop(Cm(USABLE_WIDTH_CM), WD_TAB_ALIGNMENT.RIGHT)
        r = p.add_run(text + "\t")
        r.font.size = Pt(8)
        r.font.color.rgb = GREY
        r.font.name = BODY_FONT
        r2 = p.add_run("Page ")
        r2.font.size = Pt(8)
        r2.font.bold = True
        r2.font.color.rgb = NAVY
        r2.font.name = BODY_FONT
        field(p, "PAGE", size=Pt(8), bold=True, color=NAVY)
        _para_borders(p, top=(6, HEX_TBL_LINE), space=3)
        # keep first page (cover) clean
        fp = sec.first_page_footer.paragraphs[0]
        fp.text = ""

    # -------------------------------------------------- primitives
    def _p(self, text="", *, size=None, bold=False, italic=False, color=None,
           font=None, align=None, before=0, after=2.5, left=0.0, first=0.0,
           hanging=None, spacing=None, keep=False, caps=False,
           break_before=False):
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        if break_before:
            pf.page_break_before = True
        pf.space_before = Pt(before)
        pf.space_after = Pt(after)
        pf.left_indent = Cm(left)
        if hanging is not None:
            pf.first_line_indent = Cm(-hanging)
        elif first:
            pf.first_line_indent = Cm(first)
        if spacing:
            pf.line_spacing = spacing
        if align is not None:
            pf.alignment = align
        if keep:
            _keep_with_next(p)
        if text:
            r = p.add_run(text)
            r.font.size = size or BODY_SIZE
            r.font.bold = bold
            r.font.italic = italic
            r.font.name = font or BODY_FONT
            r.font.color.rgb = color or BODY
            if caps:
                r.font.all_caps = True
        return p

    def rich(self, segments, *, left=0.0, hanging=None, size=None, after=2.5,
             before=0, align=None, bullet=None, spacing=None):
        """segments: list of (text, style) where style ∈ {'', 'b','i','bi','k','t','n'}"""
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(before)
        pf.space_after = Pt(after)
        pf.left_indent = Cm(left)
        if hanging:
            pf.first_line_indent = Cm(-hanging)
        if spacing:
            pf.line_spacing = spacing
        if align is not None:
            pf.alignment = align
        if bullet:
            r = p.add_run(bullet + "  ")
            r.font.size = size or BODY_SIZE
            r.font.name = BODY_FONT
            r.font.bold = True
            r.font.color.rgb = NAVY
        for text, sty in segments:
            r = p.add_run(text)
            r.font.size = size or BODY_SIZE
            r.font.name = BODY_FONT
            r.font.bold = "b" in sty
            r.font.italic = "i" in sty
            if "k" in sty:                     # key term
                r.font.bold = True
                r.font.color.rgb = NAVY
            elif "t" in sty:                   # technical term
                r.font.italic = True
                r.font.color.rgb = PURPLE
            elif "n" in sty:                   # number / value
                r.font.bold = True
                r.font.color.rgb = MAROON
            else:
                r.font.color.rgb = BODY
        return p

    # -------------------------------------------------- headings
    def chapter(self, number, title, subtitle=None):
        """Chapter heading — the ONLY place a page break occurs.

        The break is set as 'page break before' on the chapter band rather than
        emitted as a break character, so a chapter that happens to end exactly
        at the foot of a page does not leave an empty page behind.
        """
        self._trim_trailing_blank()
        tag = f"CH{number}"
        self.toc_entries.append((1, str(number), title, tag))

        band = self.doc.add_paragraph()
        band.paragraph_format.page_break_before = True
        band.paragraph_format.space_before = Pt(0)
        band.paragraph_format.space_after = Pt(0)
        band.paragraph_format.line_spacing = 1.0
        shade(band._p, HEX_NAVY)
        r = band.add_run(f"  CHAPTER {number}  ")
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.name = BODY_FONT
        r.font.color.rgb = WHITE
        r.font.all_caps = True
        _keep_with_next(band)

        h = self.doc.add_paragraph()
        h.paragraph_format.space_before = Pt(3)
        h.paragraph_format.space_after = Pt(1)
        h.paragraph_format.line_spacing = 1.0
        r = h.add_run(title)
        r.font.size = Pt(19)
        r.font.bold = True
        r.font.name = HEAD_FONT
        r.font.color.rgb = NAVY
        _para_borders(h, bottom=(12, HEX_NAVY), space=2)
        _keep_with_next(h)

        if subtitle:
            p = self._p(subtitle, size=Pt(9.5), italic=True, color=GREY,
                        before=2, after=7, keep=True)
        else:
            self._p("", after=4)
        return self

    def section_h(self, number, title):
        tag = f"S{number}"
        self.toc_entries.append((2, number, title, tag))
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(9)
        pf.space_after = Pt(3)
        pf.line_spacing = 1.0
        pf.left_indent = Cm(0.0)
        shade(p._p, HEX_NAVY_LT)
        _para_borders(p, left=(18, HEX_NAVY), space=6)
        r = p.add_run(f" {number}  {title}")
        r.font.size = Pt(13)
        r.font.bold = True
        r.font.name = HEAD_FONT
        r.font.color.rgb = NAVY
        _keep_with_next(p)
        return self

    def sub(self, title, *, before=7):
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(before)
        pf.space_after = Pt(2)
        pf.line_spacing = 1.0
        r = p.add_run(title)
        r.font.size = Pt(11.5)
        r.font.bold = True
        r.font.name = HEAD_FONT
        r.font.color.rgb = PURPLE
        _keep_with_next(p)
        return self

    def sub2(self, title, *, before=5):
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(before)
        pf.space_after = Pt(1)
        pf.line_spacing = 1.0
        r = p.add_run(title)
        r.font.size = Pt(10.5)
        r.font.bold = True
        r.font.italic = True
        r.font.name = BODY_FONT
        r.font.color.rgb = GREEN
        _keep_with_next(p)
        return self

    # -------------------------------------------------- text blocks
    def text(self, body, *, size=None, after=3, before=0, left=0.0, italic=False,
             align=WD_ALIGN_PARAGRAPH.JUSTIFY):
        self._p(body, size=size, after=after, before=before, left=left,
                italic=italic, align=align)
        return self

    def bullets(self, items, *, level=1, size=None, after=1.6, before=0):
        marks = {1: "•", 2: "–", 3: "·"}
        indents = {1: (0.62, 0.42), 2: (1.12, 0.40), 3: (1.60, 0.38)}
        left, hang = indents[level]
        for i, it in enumerate(items):
            segs = it if isinstance(it, list) else self._auto(it)
            self.rich(segs, left=left, hanging=hang, size=size or BODY_SIZE,
                      after=after, before=before if i == 0 else 0,
                      bullet=marks[level])
        return self

    def kv_bullets(self, pairs, *, level=1, size=None, after=1.6, sep=" — "):
        """pairs: list of (term, explanation) -> term rendered bold navy."""
        items = []
        for term, expl in pairs:
            items.append([(term, "k"), (sep, ""), *self._auto(expl)])
        return self.bullets(items, level=level, size=size, after=after)

    def numbered(self, items, *, size=None, after=1.8, left=0.70, start=1):
        for i, it in enumerate(items, start):
            segs = it if isinstance(it, list) else self._auto(it)
            p = self.rich([(f"{i}. ", "k"), *segs], left=Cm(left).cm if False else left,
                          hanging=0.50, size=size or BODY_SIZE, after=after)
        return self

    @staticmethod
    def _auto(s):
        """Mini markup:  **bold**  __key__  ~italic~  ##number##"""
        import re
        out, pos = [], 0
        pat = re.compile(r"\*\*(.+?)\*\*|__(.+?)__|~(.+?)~|##(.+?)##")
        for m in pat.finditer(s):
            if m.start() > pos:
                out.append((s[pos:m.start()], ""))
            if m.group(1) is not None:
                out.append((m.group(1), "b"))
            elif m.group(2) is not None:
                out.append((m.group(2), "k"))
            elif m.group(3) is not None:
                out.append((m.group(3), "i"))
            else:
                out.append((m.group(4), "n"))
            pos = m.end()
        if pos < len(s):
            out.append((s[pos:], ""))
        return out or [(s, "")]

    # -------------------------------------------------- tables
    def table(self, header, rows, *, size=TABLE_SIZE, caption=None,
              align_center_cols=(), before=4, after=6, total_cm=USABLE_WIDTH_CM,
              first_col_bold=True, header_fill=HEX_NAVY, zebra=True):
        if caption:
            self._p(caption, size=Pt(9.5), bold=True, color=GREEN,
                    before=before, after=1.5, keep=True)
        data = [list(header)] + [list(r) for r in rows]
        widths = proportional_widths(data, total_cm=total_cm)

        t = self.doc.add_table(rows=0, cols=len(header))
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        tblPr = t._tbl.tblPr
        tblPr.append(_el("tblLayout", type="fixed"))
        tblPr.append(_el("tblW", w=str(int(Cm(total_cm).twips)), type="dxa"))
        tblPr.append(_el("tblInd", w="0", type="dxa"))
        # borders
        bd = OxmlElement("w:tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            bd.append(_el(edge, val="single", sz="6", space="0", color=HEX_TBL_LINE))
        tblPr.append(bd)

        grid = t._tbl.tblGrid
        for gc, w in zip(grid.findall(qn("w:gridCol")), widths):
            gc.set(qn("w:w"), str(int(Cm(w).twips)))

        for ri, rowdata in enumerate(data):
            row = t.add_row()
            _cant_split(row)
            if ri == 0:
                _repeat_header(row)
            for ci in range(len(header)):
                cell = row.cells[ci]
                cell.width = Cm(widths[ci])
                _cell_margins(cell)
                _vertical_align(cell, "center" if ri == 0 else "top")
                if ri == 0:
                    _cell_shade(cell, header_fill)
                elif zebra and ri % 2 == 0:
                    _cell_shade(cell, HEX_ROW_ALT)
                txt = str(rowdata[ci]) if ci < len(rowdata) else ""
                self._fill_cell(cell, txt, size=size, header=(ri == 0),
                                bold=(first_col_bold and ci == 0 and ri > 0),
                                center=(ri == 0 or ci in align_center_cols))
        self._p("", size=Pt(2), after=after)
        return self

    def _fill_cell(self, cell, text, *, size, header=False, bold=False, center=False):
        lines = str(text).split("\n")
        cell.paragraphs[0].text = ""
        for i, line in enumerate(lines):
            p = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
            pf = p.paragraph_format
            pf.space_before = Pt(0)
            pf.space_after = Pt(0.5)
            pf.line_spacing = 1.0
            if center:
                pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
            bullet = line.startswith("* ")
            if bullet:
                line = line[2:]
                pf.left_indent = Cm(0.28)
                pf.first_line_indent = Cm(-0.28)
                rb = p.add_run("• ")
                rb.font.size = size
                rb.font.name = BODY_FONT
                rb.font.color.rgb = NAVY
            for txt, sty in self._auto(line):
                r = p.add_run(txt)
                r.font.size = size
                r.font.name = BODY_FONT
                if header:
                    r.font.bold = True
                    r.font.color.rgb = WHITE
                else:
                    r.font.bold = bold or ("b" in sty) or ("k" in sty)
                    if "k" in sty:
                        r.font.color.rgb = NAVY
                    elif "t" in sty:
                        r.font.italic = True
                        r.font.color.rgb = PURPLE
                    elif "n" in sty:
                        r.font.color.rgb = MAROON
                        r.font.bold = True
                    else:
                        r.font.italic = "i" in sty
                        r.font.color.rgb = BODY

    # -------------------------------------------------- boxes
    def box(self, kind, lines, *, title=None, size=Pt(9.5), before=5, after=6,
            total_cm=USABLE_WIDTH_CM):
        fill, border, tcol, deftitle = BOX_STYLES[kind]
        t = self.doc.add_table(rows=1, cols=1)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        tblPr = t._tbl.tblPr
        tblPr.append(_el("tblLayout", type="fixed"))
        tblPr.append(_el("tblW", w=str(int(Cm(total_cm).twips)), type="dxa"))
        tblPr.append(_el("tblInd", w="0", type="dxa"))
        bd = OxmlElement("w:tblBorders")
        for edge, sz in (("top", 6), ("bottom", 6), ("right", 6), ("insideH", 6), ("insideV", 6)):
            bd.append(_el(edge, val="single", sz=str(sz), space="0", color=border))
        bd.append(_el("left", val="single", sz="24", space="0", color=border))
        tblPr.append(bd)
        for gc in t._tbl.tblGrid.findall(qn("w:gridCol")):
            gc.set(qn("w:w"), str(int(Cm(total_cm).twips)))

        cell = t.rows[0].cells[0]
        cell.width = Cm(total_cm)
        _cell_shade(cell, fill)
        _cell_margins(cell, top=70, bottom=70, left=120, right=110)
        cell.paragraphs[0].text = ""

        ttl = title if title is not None else deftitle
        first = cell.paragraphs[0]
        first.paragraph_format.space_after = Pt(2)
        first.paragraph_format.line_spacing = 1.0
        r = first.add_run(ttl)
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.all_caps = True
        r.font.name = BODY_FONT
        r.font.color.rgb = RGBColor.from_string(tcol)

        items = lines if isinstance(lines, (list, tuple)) else [lines]
        for ln in items:
            p = cell.add_paragraph()
            pf = p.paragraph_format
            pf.space_after = Pt(1.5)
            pf.line_spacing = 1.03
            if isinstance(ln, str) and ln.startswith("* "):
                ln = ln[2:]
                pf.left_indent = Cm(0.34)
                pf.first_line_indent = Cm(-0.34)
                rb = p.add_run("• ")
                rb.font.size = size
                rb.font.bold = True
                rb.font.name = BODY_FONT
                rb.font.color.rgb = RGBColor.from_string(tcol)
            segs = ln if isinstance(ln, list) else self._auto(ln)
            for txt, sty in segs:
                rr = p.add_run(txt)
                rr.font.size = size
                rr.font.name = BODY_FONT
                rr.font.bold = "b" in sty or "k" in sty or "n" in sty
                rr.font.italic = "i" in sty or "t" in sty
                rr.font.color.rgb = (RGBColor.from_string(tcol) if ("k" in sty or "n" in sty)
                                     else BODY)
        self._p("", size=Pt(2), after=after)
        return self

    def divider(self, *, before=4, after=4):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(before)
        p.paragraph_format.space_after = Pt(after)
        p.paragraph_format.line_spacing = 1.0
        _para_borders(p, bottom=(6, HEX_TBL_LINE), space=1)
        return self

    def spacer(self, pts=6):
        self._p("", size=Pt(2), after=pts)
        return self

    def page_break(self):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.add_run().add_break(WD_BREAK.PAGE)
        return self

    def _trim_trailing_blank(self):
        """Remove the trailing spacer paragraph left by a table/box.

        Without this, a spacer that happens to fall past the foot of the page
        produces an almost empty page just before the next chapter's break.
        """
        paras = self.doc.paragraphs
        while paras and not paras[-1].text.strip():
            el = paras[-1]._element
            parent = el.getparent()
            if parent is None:
                break
            parent.remove(el)
            paras = self.doc.paragraphs

    # -------------------------------------------------- output
    def save(self, path):
        self._trim_trailing_blank()
        self.doc.save(path)
        return path
