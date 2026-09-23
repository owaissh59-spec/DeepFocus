#!/usr/bin/env python3
"""Resize DOCX tables to the writable width of their pages.

This utility is intended for documents whose margins were changed after their
layout was designed. Microsoft Word does not automatically expand fixed-width
tables when the writable page area grows, so such tables can appear shifted to
the left.

What the script does
--------------------
* Reads each section's page width and left/right margins.
* Sets every top-level table to exactly that section's writable width.
* Centres every table and removes table indentation.
* Preserves the existing proportional widths of the columns while scaling them.
* Updates table-grid and individual-cell widths, including horizontally merged
  cells.
* Fits nested tables to the usable width of their parent cells instead of the
  whole page.
* Optionally sets all four page margins before resizing the tables.
* Writes a new DOCX by default, leaving the input file untouched.

Requires: Python 3.9+ and python-docx
Install:  py -m pip install python-docx
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches

W = "w:"
DEFAULT_CELL_MARGIN_TWIPS = 108  # Word's usual default (0.075 inch) per side


def direct_children(element, tag: str) -> Iterable:
    """Yield direct child elements having the specified qualified tag."""
    wanted = qn(tag)
    for child in element.iterchildren():
        if child.tag == wanted:
            yield child


def find_or_add(parent, tag: str, before: tuple[str, ...] = ()):
    """Find a direct child or create it at a schema-safe position."""
    found = parent.find(qn(tag))
    if found is not None:
        return found

    new = OxmlElement(tag)
    before_tags = {qn(item) for item in before}
    for index, child in enumerate(parent):
        if child.tag in before_tags:
            parent.insert(index, new)
            return new
    parent.append(new)
    return new


def set_width_element(element, width_twips: int) -> None:
    element.set(qn("w:w"), str(max(1, int(width_twips))))
    element.set(qn("w:type"), "dxa")


def get_span(tc) -> int:
    tc_pr = tc.find(qn("w:tcPr"))
    if tc_pr is None:
        return 1
    span = tc_pr.find(qn("w:gridSpan"))
    if span is None:
        return 1
    try:
        return max(1, int(span.get(qn("w:val"), "1")))
    except ValueError:
        return 1


def table_column_count(tbl) -> int:
    """Return the logical number of grid columns in a table."""
    grid = tbl.find(qn("w:tblGrid"))
    if grid is not None:
        columns = list(direct_children(grid, "w:gridCol"))
        if columns:
            return len(columns)

    count = 0
    for tr in direct_children(tbl, "w:tr"):
        logical = sum(get_span(tc) for tc in direct_children(tr, "w:tc"))
        count = max(count, logical)
    return count


def current_grid_widths(tbl, column_count: int) -> list[int]:
    """Read existing grid widths; use equal widths if the grid is absent."""
    grid = tbl.find(qn("w:tblGrid"))
    widths: list[int] = []
    if grid is not None:
        for col in direct_children(grid, "w:gridCol"):
            try:
                widths.append(max(1, int(col.get(qn("w:w"), "0"))))
            except ValueError:
                widths.append(1)

    if len(widths) != column_count or sum(widths) <= 0:
        widths = [1] * column_count
    return widths


def scale_widths(widths: list[int], target_twips: int) -> list[int]:
    """Scale widths to target while preserving their exact proportions."""
    total = sum(widths)
    if total <= 0:
        widths = [1] * len(widths)
        total = len(widths)

    # Round every column, then put any rounding remainder in the widest column.
    scaled = [max(1, round(target_twips * value / total)) for value in widths]
    remainder = target_twips - sum(scaled)
    widest = max(range(len(scaled)), key=lambda i: scaled[i])
    scaled[widest] = max(1, scaled[widest] + remainder)

    # Very small target widths can trigger a one-twip discrepancy after the
    # max(1) guard. Correct it without allowing a zero-width column.
    discrepancy = target_twips - sum(scaled)
    if discrepancy:
        for index in sorted(range(len(scaled)), key=lambda i: scaled[i], reverse=True):
            candidate = scaled[index] + discrepancy
            if candidate >= 1:
                scaled[index] = candidate
                break
    return scaled


def side_margin(tc, parent_tbl, side: str) -> int:
    """Read an effective left/right cell margin in twips."""
    aliases = (side, "start" if side == "left" else "end")
    tc_pr = tc.find(qn("w:tcPr"))
    if tc_pr is not None:
        tc_mar = tc_pr.find(qn("w:tcMar"))
        if tc_mar is not None:
            for name in aliases:
                item = tc_mar.find(qn(f"w:{name}"))
                if item is not None:
                    try:
                        return max(0, int(item.get(qn("w:w"), "0")))
                    except ValueError:
                        pass

    tbl_pr = parent_tbl.find(qn("w:tblPr"))
    if tbl_pr is not None:
        tbl_mar = tbl_pr.find(qn("w:tblCellMar"))
        if tbl_mar is not None:
            for name in aliases:
                item = tbl_mar.find(qn(f"w:{name}"))
                if item is not None:
                    try:
                        return max(0, int(item.get(qn("w:w"), "0")))
                    except ValueError:
                        pass
    return DEFAULT_CELL_MARGIN_TWIPS


def set_table_properties(tbl, target_twips: int) -> None:
    """Set overall width, fixed layout, centred alignment and zero indent."""
    tbl_pr = tbl.find(qn("w:tblPr"))
    if tbl_pr is None:
        tbl_pr = OxmlElement("w:tblPr")
        tbl.insert(0, tbl_pr)

    tbl_w = find_or_add(
        tbl_pr,
        "w:tblW",
        before=("w:jc", "w:tblCellSpacing", "w:tblInd", "w:tblBorders"),
    )
    set_width_element(tbl_w, target_twips)

    jc = find_or_add(
        tbl_pr,
        "w:jc",
        before=("w:tblCellSpacing", "w:tblInd", "w:tblBorders"),
    )
    jc.set(qn("w:val"), "center")

    tbl_ind = find_or_add(
        tbl_pr,
        "w:tblInd",
        before=("w:tblBorders", "w:shd", "w:tblLayout"),
    )
    tbl_ind.set(qn("w:w"), "0")
    tbl_ind.set(qn("w:type"), "dxa")

    layout = find_or_add(
        tbl_pr,
        "w:tblLayout",
        before=("w:tblCellMar", "w:tblLook", "w:tblCaption"),
    )
    layout.set(qn("w:type"), "fixed")


def update_grid(tbl, widths: list[int]) -> None:
    """Replace the table grid with the scaled column widths."""
    old_grid = tbl.find(qn("w:tblGrid"))
    new_grid = OxmlElement("w:tblGrid")
    for width in widths:
        col = OxmlElement("w:gridCol")
        col.set(qn("w:w"), str(width))
        new_grid.append(col)

    if old_grid is not None:
        tbl.replace(old_grid, new_grid)
    else:
        tbl_pr = tbl.find(qn("w:tblPr"))
        insert_at = tbl.index(tbl_pr) + 1 if tbl_pr is not None else 0
        tbl.insert(insert_at, new_grid)


def resize_table(tbl, target_twips: int, depth: int = 0) -> tuple[int, int]:
    """Resize a table and its nested tables.

    Returns (tables_resized, maximum_nesting_depth).
    """
    column_count = table_column_count(tbl)
    if column_count == 0:
        return 0, depth

    target_twips = max(column_count, int(target_twips))
    widths = scale_widths(current_grid_widths(tbl, column_count), target_twips)
    set_table_properties(tbl, target_twips)
    update_grid(tbl, widths)

    resized = 1
    maximum_depth = depth

    for tr in direct_children(tbl, "w:tr"):
        column_index = 0
        for tc in direct_children(tr, "w:tc"):
            span = min(get_span(tc), column_count - column_index)
            if span <= 0:
                span = 1
            cell_width = sum(widths[column_index : column_index + span])
            column_index += span

            tc_pr = tc.find(qn("w:tcPr"))
            if tc_pr is None:
                tc_pr = OxmlElement("w:tcPr")
                tc.insert(0, tc_pr)
            tc_w = find_or_add(
                tc_pr,
                "w:tcW",
                before=("w:gridSpan", "w:vMerge", "w:tcBorders", "w:shd"),
            )
            set_width_element(tc_w, cell_width)

            inner_width = max(
                1,
                cell_width
                - side_margin(tc, tbl, "left")
                - side_margin(tc, tbl, "right"),
            )
            for nested in direct_children(tc, "w:tbl"):
                nested_count, nested_depth = resize_table(
                    nested, inner_width, depth + 1
                )
                resized += nested_count
                maximum_depth = max(maximum_depth, nested_depth)

    return resized, maximum_depth


def section_writable_width_twips(section) -> int:
    return int(
        section.page_width.twips
        - section.left_margin.twips
        - section.right_margin.twips
    )


def resize_document_tables(document: Document) -> tuple[int, int, list[int]]:
    """Resize every table, using the section containing each body table."""
    sections = list(document.sections)
    writable_widths = [section_writable_width_twips(s) for s in sections]
    if not writable_widths:
        raise ValueError("The document contains no section properties.")

    body = document._element.body
    section_index = 0
    resized = 0
    maximum_depth = 0

    # In WordprocessingML, the section break is stored on the paragraph that
    # ends the current section. Tables before it belong to the current section.
    for child in body.iterchildren():
        if child.tag == qn("w:tbl"):
            count, depth = resize_table(
                child, writable_widths[min(section_index, len(sections) - 1)]
            )
            resized += count
            maximum_depth = max(maximum_depth, depth)
        elif child.tag == qn("w:p"):
            p_pr = child.find(qn("w:pPr"))
            if p_pr is not None and p_pr.find(qn("w:sectPr")) is not None:
                section_index += 1

    # Resize tables in headers and footers as well. Linked header/footer parts
    # are processed only once.
    seen_parts: set[str] = set()
    for index, section in enumerate(sections):
        width = writable_widths[index]
        containers = (
            section.header,
            section.first_page_header,
            section.even_page_header,
            section.footer,
            section.first_page_footer,
            section.even_page_footer,
        )
        for container in containers:
            key = str(container.part.partname)
            if key in seen_parts:
                continue
            seen_parts.add(key)
            for tbl in direct_children(container._element, "w:tbl"):
                count, depth = resize_table(tbl, width)
                resized += count
                maximum_depth = max(maximum_depth, depth)

    return resized, maximum_depth, writable_widths


def default_output(input_path: Path) -> Path:
    return input_path.with_name(f"{input_path.stem}_tables_fixed.docx")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Expand every DOCX table to the writable page width while "
            "preserving proportional column widths."
        )
    )
    parser.add_argument("input", type=Path, help="input .docx file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="output .docx (default: INPUT_tables_fixed.docx)",
    )
    parser.add_argument(
        "--margin",
        type=float,
        metavar="INCHES",
        help=(
            "optionally set top, bottom, left and right margins in every "
            "section before resizing (example: --margin 0.5)"
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_arguments()
    source = args.input.expanduser().resolve()
    destination = (
        args.output.expanduser().resolve()
        if args.output
        else default_output(source)
    )

    if source.suffix.lower() != ".docx":
        print("Error: the input must be a .docx file.", file=sys.stderr)
        return 2
    if not source.is_file():
        print(f"Error: input file not found: {source}", file=sys.stderr)
        return 2
    if destination == source:
        print(
            "Error: choose a different output filename so the original stays safe.",
            file=sys.stderr,
        )
        return 2
    if args.margin is not None and not (0.1 <= args.margin <= 3.0):
        print("Error: --margin must be between 0.1 and 3.0 inches.", file=sys.stderr)
        return 2

    destination.parent.mkdir(parents=True, exist_ok=True)
    document = Document(source)

    if args.margin is not None:
        margin = Inches(args.margin)
        for section in document.sections:
            section.top_margin = margin
            section.bottom_margin = margin
            section.left_margin = margin
            section.right_margin = margin

    resized, depth, widths = resize_document_tables(document)
    document.save(destination)

    print(f"Created: {destination}")
    print(f"Tables resized (including nested tables): {resized}")
    print(f"Maximum table nesting depth: {depth}")
    print(
        "Writable widths by section: "
        + ", ".join(f"{width / 1440:.3f} in" for width in widths)
    )
    print("Original file was not changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
