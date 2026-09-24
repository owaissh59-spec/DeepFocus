"""
docx_kit.py — A small typesetting toolkit for building exam-style study notes in DOCX.

Design goals
------------
* A4 page, tight but readable margins.
* Coloured heading hierarchy (chapter banner / section / sub-section / point).
* Professional tables: shaded header, alternating row fill, thin grid,
  PROPORTIONAL column widths derived from the amount of text in each column.
* Callout boxes (definition / high-yield / mnemonic / exam-point / caution / flow).
* Page numbers in the footer, running header, manual dot-leader Table of Contents
  whose page numbers are filled in from a measurement pass (see build_notes.py).
"""

import re
from docx import Document
from docx.shared import Pt, Cm, Mm, RGBColor
from docx.enum.text import (WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT,
                            WD_TAB_LEADER, WD_BREAK)
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# --------------------------------------------------------------------------
# palette
# --------------------------------------------------------------------------
NAVY      = '15325B'
BLUE      = '1F4E79'
LTBLUE    = 'DCE7F3'
LTBLUE2   = 'F1F6FB'
GREEN     = '1B6B34'
LTGREEN   = 'E7F4EA'
PURPLE    = '5B2C8D'
LTPURPLE  = 'F0E9F8'
MAROON    = '9B1B30'
LTRED     = 'FCEAEA'
AMBER     = '9A6300'
LTAMBER   = 'FFF6D9'
TEAL      = '0E6A6A'
LTTEAL    = 'E3F2F2'
GREY      = '595959'
LTGREY    = 'EFEFEF'
GRID      = 'A9BFD8'

BODY_FONT = 'Calibri'
HEAD_FONT = 'Calibri'

PAGE_W    = Mm(210)
PAGE_H    = Mm(297)
MARGIN_LR = Cm(1.8)
MARGIN_TB = Cm(1.6)
USABLE_CM = 21.0 - 3.6          # 17.4 cm


# --------------------------------------------------------------------------
# low level oxml helpers
# --------------------------------------------------------------------------
def _el(tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn(k), str(v))
    return e


def _shade(pr, fill):
    pr.append(_el('w:shd', **{'w:val': 'clear', 'w:color': 'auto', 'w:fill': fill}))


def para_shading(p, fill):
    _shade(p._p.get_or_add_pPr(), fill)


def cell_shading(cell, fill):
    _shade(cell._tc.get_or_add_tcPr(), fill)


def para_borders(p, **edges):
    """edges: top/bottom/left/right = (size_eighths, colour, space)"""
    pPr = p._p.get_or_add_pPr()
    pbdr = pPr.find(qn('w:pBdr'))
    if pbdr is None:
        pbdr = _el('w:pBdr')
        pPr.append(pbdr)
    for name in ('top', 'left', 'bottom', 'right'):
        if name in edges and edges[name]:
            size, colour, space = edges[name]
            pbdr.append(_el('w:' + name, **{'w:val': 'single', 'w:sz': size,
                                            'w:space': space, 'w:color': colour}))


def keep_with_next(p, value=True):
    pPr = p._p.get_or_add_pPr()
    pPr.append(_el('w:keepNext', **{'w:val': 'true' if value else 'false'}))


def cant_split(row):
    row._tr.get_or_add_trPr().append(_el('w:cantSplit'))


def repeat_header(row):
    row._tr.get_or_add_trPr().append(_el('w:tblHeader'))


def table_grid_borders(table, sz=4, colour=GRID, outer_sz=10, outer_colour=BLUE):
    tblPr = table._tbl.tblPr
    borders = _el('w:tblBorders')
    spec = [('top', outer_sz, outer_colour), ('left', outer_sz, outer_colour),
            ('bottom', outer_sz, outer_colour), ('right', outer_sz, outer_colour),
            ('insideH', sz, colour), ('insideV', sz, colour)]
    for name, s, c in spec:
        borders.append(_el('w:' + name, **{'w:val': 'single', 'w:sz': s,
                                           'w:space': 0, 'w:color': c}))
    tblPr.append(borders)


def table_cell_margins(table, top=40, bottom=40, left=85, right=85):
    tblPr = table._tbl.tblPr
    mar = _el('w:tblCellMar')
    for name, v in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        mar.append(_el('w:' + name, **{'w:w': v, 'w:type': 'dxa'}))
    tblPr.append(mar)


def fixed_layout(table):
    table.autofit = False
    table._tbl.tblPr.append(_el('w:tblLayout', **{'w:type': 'fixed'}))


def set_table_width(table, cm=USABLE_CM):
    table._tbl.tblPr.append(_el('w:tblW', **{'w:w': int(cm * 567), 'w:type': 'dxa'}))


def add_field(paragraph, instr, size=8.5, colour=GREY, bold=False):
    r = paragraph.add_run()
    r.font.size = Pt(size)
    r.font.color.rgb = RGBColor.from_string(colour)
    r.font.bold = bold
    r.font.name = BODY_FONT
    fld = _el('w:fldChar', **{'w:fldCharType': 'begin'})
    instr_el = OxmlElement('w:instrText')
    instr_el.set(qn('xml:space'), 'preserve')
    instr_el.text = instr
    end = _el('w:fldChar', **{'w:fldCharType': 'end'})
    r._r.append(fld)
    r._r.append(instr_el)
    r._r.append(end)


# --------------------------------------------------------------------------
# inline markup:  **bold**  *italic*  __underline__  `mono`  ==highlight==
# --------------------------------------------------------------------------
_TOKEN = re.compile(r'(\*\*.+?\*\*|__.+?__|==.+?==|`.+?`|\*(?!\*).+?\*)', re.S)


def _tidy(text):
    """Keep units attached to their number so that a line break never leaves
    a lonely '%' or '°C' at the start of a line."""
    text = text.replace(' %', '\u00A0%').replace(' \u00B0C', '\u00A0\u00B0C')
    text = text.replace(' cm', '\u00A0cm').replace(' mm', '\u00A0mm')
    return text


def add_runs(paragraph, text, size=None, colour=None, bold=None, italic=None,
             font=BODY_FONT):
    for part in _TOKEN.split(_tidy(text)):
        if not part:
            continue
        b, i, u, hl, mono = bold, italic, False, False, False
        t = part
        if part.startswith('**') and part.endswith('**') and len(part) > 4:
            t, b = part[2:-2], True
        elif part.startswith('__') and part.endswith('__') and len(part) > 4:
            t, u = part[2:-2], True
        elif part.startswith('==') and part.endswith('==') and len(part) > 4:
            t, hl, b = part[2:-2], True, True
        elif part.startswith('`') and part.endswith('`') and len(part) > 2:
            t, mono = part[1:-1], True
        elif part.startswith('*') and part.endswith('*') and len(part) > 2:
            t, i = part[1:-1], True
        run = paragraph.add_run(t)
        run.font.name = 'Consolas' if mono else font
        if size:
            run.font.size = Pt(size - 0.5 if mono else size)
        if b is not None:
            run.font.bold = b
        if i is not None:
            run.font.italic = i
        run.font.underline = u
        if hl:
            run.font.color.rgb = RGBColor.from_string(MAROON)
        elif mono:
            run.font.color.rgb = RGBColor.from_string(BLUE)
        elif colour:
            run.font.color.rgb = RGBColor.from_string(colour)


def plain(text):
    """strip inline markup - used for width measurement & TOC keys"""
    out = re.sub(r'\*\*|__|==|`|\*', '', text)
    return out


# --------------------------------------------------------------------------
# proportional column widths
# --------------------------------------------------------------------------
def _damp(n):
    """Longer strings get more width, but sub-linearly, so one very long
    column cannot starve the others."""
    n = float(n)
    if n <= 14:
        return n
    return 14.0 + (n - 14.0) ** 0.68


def proportional_widths(headers, rows, total_cm=USABLE_CM, min_cm=1.35,
                        header_weight=1.15, size=9.0):
    """Column widths proportional to the amount of text each column carries,
    with a per-column floor wide enough that the longest word of the HEADER
    never has to break in the middle."""
    ncols = len(headers)
    char_cm = 0.0195 * size          # rough mean glyph width of bold Calibri
    measures, floors = [], []
    for c in range(ncols):
        cells = [plain(str(r[c])) for r in rows if c < len(r)]
        longest = max([len(x) for x in cells] + [0])
        avg = (sum(len(x) for x in cells) / len(cells)) if cells else 0
        body = 0.65 * longest + 0.35 * avg * 1.6
        h = plain(str(headers[c]))
        measures.append(max(_damp(body), _damp(len(h) * header_weight) * 0.9, 4.0))
        longest_word = max([len(w) for w in h.split()] + [1])
        floors.append(max(min_cm, longest_word * char_cm + 0.33))
    if sum(floors) > total_cm:       # too many columns for the floors: relax
        floors = [f * total_cm / sum(floors) for f in floors]
    total = sum(measures)
    widths = [total_cm * m / total for m in measures]
    for _ in range(60):
        deficit = sum(max(0.0, floors[i] - w) for i, w in enumerate(widths))
        if deficit < 1e-6:
            break
        surplus_idx = [i for i, w in enumerate(widths) if w > floors[i] + 0.25]
        if not surplus_idx:
            break
        pool = sum(widths[i] - floors[i] for i in surplus_idx)
        if pool <= 0:
            break
        for i in surplus_idx:
            widths[i] -= min(deficit * (widths[i] - floors[i]) / pool,
                             widths[i] - floors[i])
        widths = [max(w, floors[i]) for i, w in enumerate(widths)]
    scale = total_cm / sum(widths)
    return [w * scale for w in widths]


def apply_widths(table, widths_cm):
    tbl = table._tbl
    grid = tbl.find(qn('w:tblGrid'))
    if grid is not None:
        tbl.remove(grid)
    grid = _el('w:tblGrid')
    for w in widths_cm:
        grid.append(_el('w:gridCol', **{'w:w': int(w * 567)}))
    tblPr = tbl.tblPr
    tblPr.addnext(grid)
    for row in table.rows:
        for idx, cell in enumerate(row.cells):
            if idx < len(widths_cm):
                cell.width = Cm(widths_cm[idx])


# ==========================================================================
class Book:
    def __init__(self, running_title, page_map=None):
        self.doc = Document()
        self.page_map = page_map or {}
        self.toc_entries = []          # (level, number, title, key)
        self.running_title = running_title
        self._setup()

    # ---------------- document setup ----------------
    def _setup(self):
        d = self.doc
        s = d.sections[0]
        s.page_width, s.page_height = PAGE_W, PAGE_H
        s.left_margin = s.right_margin = MARGIN_LR
        s.top_margin = s.bottom_margin = MARGIN_TB
        s.header_distance = Cm(0.8)
        s.footer_distance = Cm(0.8)
        s.different_first_page_header_footer = True

        normal = d.styles['Normal']
        normal.font.name = BODY_FONT
        normal.font.size = Pt(10.5)
        normal.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
        pf = normal.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(3)
        pf.line_spacing = 1.06
        rpr = normal.element.get_or_add_rPr()
        rfonts = rpr.get_or_add_rFonts()
        rfonts.set(qn('w:eastAsia'), BODY_FONT)
        rfonts.set(qn('w:cs'), BODY_FONT)

        for name, size, colour, bold, italic, before, after in (
                ('Heading 1', 15.5, 'FFFFFF', True, False, 2, 8),
                ('Heading 2', 13.0, BLUE, True, False, 13, 4),
                ('Heading 3', 11.5, GREEN, True, False, 9, 2),
                ('Heading 4', 10.5, PURPLE, True, True, 7, 1)):
            st = d.styles[name]
            st.font.name = HEAD_FONT
            st.font.size = Pt(size)
            st.font.bold = bold
            st.font.italic = italic
            st.font.color.rgb = RGBColor.from_string(colour)
            st.paragraph_format.space_before = Pt(before)
            st.paragraph_format.space_after = Pt(after)
            st.paragraph_format.keep_with_next = True
            st.paragraph_format.line_spacing = 1.0

        self._header_footer()

    def _header_footer(self):
        s = self.doc.sections[0]
        hdr = s.header.paragraphs[0]
        hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_runs(hdr, self.running_title, size=8, colour=BLUE, bold=True)
        para_borders(hdr, bottom=(6, GRID, 2))

        ftr = s.footer.paragraphs[0]
        ftr.alignment = WD_ALIGN_PARAGRAPH.CENTER
        para_borders(ftr, top=(6, GRID, 2))
        add_runs(ftr, 'Page ', size=8.5, colour=GREY)
        add_field(ftr, 'PAGE', size=9, colour=NAVY, bold=True)
        add_runs(ftr, ' of ', size=8.5, colour=GREY)
        add_field(ftr, 'NUMPAGES', size=9, colour=NAVY, bold=True)
        add_runs(ftr, '   |   JKSSB Junior Pharmacist — Stores Records & Procedures',
                 size=8, colour=GREY)

    # ---------------- primitives ----------------
    def _p(self, text='', style=None, size=None, colour=None, bold=None,
           italic=None, align=None, before=None, after=None, left=None,
           first_line=None, spacing=None):
        p = self.doc.add_paragraph(style=style)
        if text:
            add_runs(p, text, size=size, colour=colour, bold=bold, italic=italic)
        pf = p.paragraph_format
        if align is not None:
            p.alignment = align
        if before is not None:
            pf.space_before = Pt(before)
        if after is not None:
            pf.space_after = Pt(after)
        if left is not None:
            pf.left_indent = Cm(left)
        if first_line is not None:
            pf.first_line_indent = Cm(first_line)
        if spacing is not None:
            pf.line_spacing = spacing
        return p

    def spacer(self, pts=4):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        p.add_run().font.size = Pt(pts)
        return p

    def page_break(self):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.add_run().add_break(WD_BREAK.PAGE)

    # ---------------- headings ----------------
    def part(self, label, title):
        """Part divider strip (not a page break)."""
        p = self._p(after=2, before=10, align=WD_ALIGN_PARAGRAPH.CENTER)
        para_shading(p, MAROON)
        add_runs(p, label + '  \u2022  ' + title.upper(), size=11.5,
                 colour='FFFFFF', bold=True)
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(8)
        self.toc_entries.append(('part', label, title, None))
        return p

    def chapter(self, number, title, subtitle=None):
        # 'CH::' prefix = match case-sensitively against the raw page text, so that
        # a cross-reference in running prose ("see Chapter 9") cannot be mistaken
        # for the chapter banner itself.  '||' = AND of substrings.
        key = 'CH::CHAPTER %s||%s' % (number, re.sub(r'\s+', ' ', plain(title)).strip().upper())
        p = self.doc.add_paragraph(style='Heading 1')
        para_shading(p, NAVY)
        para_borders(p, left=(24, MAROON, 4))
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.left_indent = Cm(0.18)
        add_runs(p, 'CHAPTER %s  \u2502  ' % number, size=12, colour='F2C14E', bold=True)
        add_runs(p, title.upper(), size=14.5, colour='FFFFFF', bold=True)
        if subtitle:
            sp = self._p(subtitle, size=9.5, colour=GREY, italic=True, after=6,
                         before=2)
            para_borders(sp, bottom=(6, 'F2C14E', 3))
        self.toc_entries.append(('ch', str(number), title, key))
        return p

    def h2(self, number, title):
        p = self.doc.add_paragraph(style='Heading 2')
        add_runs(p, '%s  ' % number, size=13, colour=MAROON, bold=True)
        add_runs(p, title, size=13, colour=BLUE, bold=True)
        para_borders(p, bottom=(8, LTBLUE, 2))
        self.toc_entries.append(('h2', number, title, _norm('%s %s' % (number, title))))
        return p

    def h3(self, title, number=None):
        p = self.doc.add_paragraph(style='Heading 3')
        add_runs(p, ('%s ' % number if number else '') + title, size=11.5,
                 colour=GREEN, bold=True)
        return p

    def h4(self, title):
        p = self.doc.add_paragraph(style='Heading 4')
        add_runs(p, title, size=10.5, colour=PURPLE, bold=True, italic=True)
        return p

    def rule(self, colour=GRID):
        p = self._p(after=4, before=4)
        para_borders(p, bottom=(6, colour, 1))
        p.paragraph_format.line_spacing = 1.0
        return p

    # ---------------- body text ----------------
    def p(self, text, size=10.5, **kw):
        return self._p(text, size=size, align=WD_ALIGN_PARAGRAPH.JUSTIFY, **kw)

    def lead(self, text, size=10.5):
        p = self._p(text, size=size, italic=True, colour=BLUE, after=5,
                    align=WD_ALIGN_PARAGRAPH.JUSTIFY, left=0.1)
        return p

    def bullets(self, items, level=0, size=10.5, marker=None, after=2):
        markers = ['\u25A0', '\u25CF', '\u25AA', '\u2013']
        out = []
        for it in items:
            p = self._p(after=after)
            pf = p.paragraph_format
            pf.left_indent = Cm(0.55 + 0.55 * level)
            pf.first_line_indent = Cm(-0.38)
            pf.line_spacing = 1.05
            m = marker or markers[min(level, 3)]
            add_runs(p, m + ' ', size=size - 1.5,
                     colour=[MAROON, BLUE, GREEN, GREY][min(level, 3)], bold=True)
            add_runs(p, it, size=size)
            out.append(p)
        return out

    def numbered(self, items, size=10.5, start=1, level=0, after=2, colour=MAROON):
        for i, it in enumerate(items, start):
            p = self._p(after=after)
            pf = p.paragraph_format
            pf.left_indent = Cm(0.75 + 0.55 * level)
            pf.first_line_indent = Cm(-0.75)
            pf.line_spacing = 1.05
            add_runs(p, '%s. ' % i, size=size, colour=colour, bold=True)
            add_runs(p, it, size=size)

    def steps(self, items, size=10.5, label='Step'):
        for i, it in enumerate(items, 1):
            p = self._p(after=2)
            pf = p.paragraph_format
            pf.left_indent = Cm(1.55)
            pf.first_line_indent = Cm(-1.55)
            pf.line_spacing = 1.05
            add_runs(p, '%s %-2d ' % (label, i), size=size - 0.5, colour=MAROON, bold=True)
            add_runs(p, it, size=size)

    def kv(self, pairs, size=10.5, key_colour=BLUE, indent=0.55):
        for k, v in pairs:
            p = self._p(after=2)
            pf = p.paragraph_format
            pf.left_indent = Cm(indent)
            pf.first_line_indent = Cm(-0.38)
            pf.line_spacing = 1.05
            add_runs(p, '\u25B8 ', size=size - 1, colour=MAROON, bold=True)
            add_runs(p, k + ': ', size=size, colour=key_colour, bold=True)
            add_runs(p, v, size=size)

    def flow(self, stages, size=9.5):
        """Horizontal-ish process flow rendered as a chain of shaded chips."""
        p = self._p(after=5, before=3, align=WD_ALIGN_PARAGRAPH.CENTER)
        p.paragraph_format.line_spacing = 1.35
        for i, s in enumerate(stages):
            if i:
                add_runs(p, '  \u27A4  ', size=size, colour=MAROON, bold=True)
            r = p.add_run(' %s ' % plain(s))
            r.font.name = BODY_FONT
            r.font.size = Pt(size)
            r.font.bold = True
            r.font.color.rgb = RGBColor.from_string(NAVY)
            rpr = r._r.get_or_add_rPr()
            _shade(rpr, LTBLUE)
        return p

    # ---------------- callout boxes ----------------
    def box(self, kind, title, body=None, bullets=None, size=10.0):
        styles = {
            'def':   (LTBLUE2, BLUE,   'DEFINITION'),
            'hy':    (LTAMBER, AMBER,  'HIGH-YIELD'),
            'mnem':  (LTPURPLE, PURPLE, 'MNEMONIC'),
            'exam':  (LTGREEN, GREEN,  'EXAM POINT'),
            'caution': (LTRED, MAROON, 'CAUTION'),
            'note':  (LTTEAL, TEAL,    'NOTE'),
            'formula': (LTGREY, NAVY,  'FORMULA'),
        }
        fill, accent, default_label = styles.get(kind, styles['note'])
        label = title or default_label
        t = self.doc.add_table(rows=1, cols=1)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        fixed_layout(t)
        set_table_width(t)
        apply_widths(t, [USABLE_CM])
        table_cell_margins(t, top=60, bottom=60, left=110, right=110)
        cell = t.cell(0, 0)
        cell_shading(cell, fill)
        _box_borders(cell, accent)
        cant_split(t.rows[0])

        first = cell.paragraphs[0]
        first.paragraph_format.space_after = Pt(2 if (body or bullets) else 0)
        first.paragraph_format.line_spacing = 1.03
        add_runs(first, ('%s  ' % _ICON.get(kind, '\u25C6')), size=size,
                 colour=accent, bold=True)
        add_runs(first, label.upper() + ('  \u2014  ' if body else ''),
                 size=size - 0.5, colour=accent, bold=True)
        if body:
            add_runs(first, body, size=size)
        if bullets:
            for b in bullets:
                bp = cell.add_paragraph()
                pf = bp.paragraph_format
                pf.left_indent = Cm(0.45)
                pf.first_line_indent = Cm(-0.32)
                pf.space_after = Pt(1)
                pf.line_spacing = 1.03
                add_runs(bp, '\u25AA ', size=size - 1.5, colour=accent, bold=True)
                add_runs(bp, b, size=size)
        self.spacer(3)
        return t

    # ---------------- tables ----------------
    def table(self, headers, rows, size=9.0, widths=None, first_col_bold=True,
              caption=None, align_centre_cols=None, header_fill=NAVY,
              zebra=LTBLUE2, min_cm=1.35):
        if caption:
            cp = self._p(caption, size=9.5, colour=MAROON, bold=True, after=2,
                         before=6)
            keep_with_next(cp)
        t = self.doc.add_table(rows=1, cols=len(headers))
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        fixed_layout(t)
        set_table_width(t)
        table_grid_borders(t)
        table_cell_margins(t, top=34, bottom=34, left=72, right=72)

        hdr = t.rows[0]
        for i, h in enumerate(headers):
            c = hdr.cells[i]
            cell_shading(c, header_fill)
            para = c.paragraphs[0]
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para.paragraph_format.space_after = Pt(0)
            para.paragraph_format.space_before = Pt(0)
            para.paragraph_format.line_spacing = 1.0
            add_runs(para, str(h), size=size, colour='FFFFFF', bold=True)
            c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        repeat_header(hdr)
        cant_split(hdr)

        for ri, row in enumerate(rows):
            tr = t.add_row()
            cant_split(tr)
            for ci in range(len(headers)):
                c = tr.cells[ci]
                if zebra and ri % 2 == 1:
                    cell_shading(c, zebra)
                txt = str(row[ci]) if ci < len(row) else ''
                lines = txt.split('\n')
                for li, line in enumerate(lines):
                    para = c.paragraphs[0] if li == 0 else c.add_paragraph()
                    para.paragraph_format.space_after = Pt(0 if li == len(lines) - 1 else 1)
                    para.paragraph_format.space_before = Pt(0)
                    para.paragraph_format.line_spacing = 1.02
                    if align_centre_cols and ci in align_centre_cols:
                        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    bold = True if (ci == 0 and first_col_bold) else None
                    colour = NAVY if (ci == 0 and first_col_bold) else None
                    add_runs(para, line, size=size, bold=bold, colour=colour)
                c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

        w = widths or proportional_widths(headers, rows, min_cm=min_cm, size=size)
        if widths:
            tot = sum(widths)
            w = [x * USABLE_CM / tot for x in widths]
        apply_widths(t, w)
        self.spacer(4)
        return t

    # ---------------- cover & contents ----------------
    def cover(self, title, subtitle, syllabus_lines, meta_lines):
        self.spacer(26)
        p = self._p(align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
        add_runs(p, 'JKSSB  \u2022  JUNIOR PHARMACIST', size=13, colour=MAROON,
                 bold=True)
        p2 = self._p(align=WD_ALIGN_PARAGRAPH.CENTER, after=8)
        add_runs(p2, 'COMPLETE EXAM NOTES', size=10.5, colour=GREY, bold=True)

        band = self._p(align=WD_ALIGN_PARAGRAPH.CENTER, after=0, before=4)
        para_shading(band, NAVY)
        para_borders(band, top=(18, MAROON, 2), bottom=(18, MAROON, 2))
        band.paragraph_format.line_spacing = 1.15
        add_runs(band, '\n' + title + '\n', size=26, colour='FFFFFF', bold=True)

        sp = self._p(align=WD_ALIGN_PARAGRAPH.CENTER, after=14, before=6)
        add_runs(sp, subtitle, size=12.5, colour=BLUE, bold=True)

        self.box('note', 'SYLLABUS COVERED BY THIS BOOK', bullets=syllabus_lines,
                 size=10.5)
        self.spacer(10)
        t = self.doc.add_table(rows=1, cols=1)
        fixed_layout(t)
        set_table_width(t, 12.0)
        apply_widths(t, [12.0])
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        table_cell_margins(t, 60, 60, 110, 110)
        cell = t.cell(0, 0)
        cell_shading(cell, LTGREY)
        _box_borders(cell, NAVY)
        for i, line in enumerate(meta_lines):
            para = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para.paragraph_format.space_after = Pt(1)
            para.paragraph_format.line_spacing = 1.05
            add_runs(para, line, size=9.5, colour=NAVY)
        self.page_break()

    def contents_placeholder(self):
        """Marks where the TOC must be injected; returns nothing.
        The TOC is written by write_contents() using self.toc_entries, so this
        is called AFTER all content in a two-pass build (see build_notes.py)."""
        raise NotImplementedError


# --------------------------------------------------------------------------
_ICON = {'def': '\u25C6', 'hy': '\u2605', 'mnem': '\u266B', 'exam': '\u2714',
         'caution': '\u26A0', 'note': '\u25CF', 'formula': '\u0192'}


def _box_borders(cell, accent):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = _el('w:tcBorders')
    borders.append(_el('w:left', **{'w:val': 'single', 'w:sz': 26, 'w:space': 0,
                                    'w:color': accent}))
    for name in ('top', 'bottom', 'right'):
        borders.append(_el('w:' + name, **{'w:val': 'single', 'w:sz': 6,
                                           'w:space': 0, 'w:color': accent}))
    tcPr.append(borders)


def _norm(s):
    return re.sub(r'\s+', ' ', plain(s)).strip().lower()
