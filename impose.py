#!/usr/bin/env python3
"""
Impose a reading-order PDF into a single-signature saddle-stitch booklet
on landscape Legal sheets (14 x 8.5 in), folded once down the middle.

Sheet layout (one signature, left binding, LTR reading order):

    sheet i front:  [ N-2i+2 | 2i-1   ]
    sheet i back:   [ 2i     | N-2i+1 ]

Output page order is front, back, front, back... so the printer's duplex
does the work. Landscape content on portrait-fed Legal paper means
FLIP ON SHORT EDGE is the correct duplex setting: the sheet's short-edge
hinge becomes a left/right mirror in the landscape content frame, which
is exactly the swap the two halves need.

Usage:
    python impose.py in.pdf out.pdf [--shrink 0.98] [--verbose]
"""

import argparse
import sys

from pypdf import PageObject, PdfReader, PdfWriter, Transformation
from pypdf.generic import RectangleObject

IN = 72.0                      # points per inch
SHEET_W, SHEET_H = 14.0 * IN, 8.5 * IN   # landscape Legal
HALF_W = SHEET_W / 2.0                   # 7 in -> one page of the fold


def signature_order(n_pages: int):
    """Yield (left_page, right_page) 1-indexed, or None for a blank."""
    n = n_pages
    for i in range(1, n // 4 + 1):
        yield (n - 2 * i + 2, 2 * i - 1)      # front of sheet i
        yield (2 * i, n - 2 * i + 1)          # back of sheet i


def place(sheet, src, x_offset, shrink):
    """Center `src` into the half-sheet starting at x_offset."""
    sw = float(src.mediabox.width)
    sh = float(src.mediabox.height)
    if sw <= 0 or sh <= 0:
        return

    scale = min(HALF_W / sw, SHEET_H / sh) * shrink
    tx = x_offset + (HALF_W - sw * scale) / 2.0
    ty = (SHEET_H - sh * scale) / 2.0

    sheet.merge_transformed_page(
        src, Transformation().scale(scale).translate(tx, ty)
    )


def impose(in_path, out_path, shrink=1.0, verbose=False):
    reader = PdfReader(in_path)
    real = len(reader.pages)

    # Pad to a multiple of 4 -- a signature is always whole sheets.
    n = real + (-real % 4)
    sheets = n // 4

    writer = PdfWriter()
    plan = []

    for slot, (left, right) in enumerate(signature_order(n)):
        sheet = PageObject.create_blank_page(width=SHEET_W, height=SHEET_H)
        sheet.mediabox = RectangleObject((0, 0, SHEET_W, SHEET_H))

        for pageno, x in ((left, 0.0), (right, HALF_W)):
            if pageno <= real:
                place(sheet, reader.pages[pageno - 1], x, shrink)

        writer.add_page(sheet)
        plan.append(
            (
                slot // 2 + 1,
                "front" if slot % 2 == 0 else "back",
                left if left <= real else None,
                right if right <= real else None,
            )
        )

    with open(out_path, "wb") as fh:
        writer.write(fh)

    if verbose:
        blank = lambda p: "blank" if p is None else str(p)
        print(f"  content pages : {real}")
        print(f"  padded to     : {n}  ({n - real} blank)")
        print(f"  legal sheets  : {sheets}")
        print(f"  output pages  : {len(writer.pages)}")
        print("  imposition:")
        for s, side, l, r in plan:
            print(f"    sheet {s:>2} {side:<5}  [ {blank(l):>5} | {blank(r):<5} ]")
        if sheets > 10:
            print(
                f"\n  !! {sheets} sheets in one signature will bulge at the fold."
                "\n     Consider creep compensation or multiple signatures."
            )

    return real, n, sheets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument(
        "--shrink",
        type=float,
        default=1.0,
        help="scale factor inside each half-sheet (e.g. 0.98 to inset)",
    )
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()

    try:
        impose(a.input, a.output, a.shrink, a.verbose)
    except FileNotFoundError:
        sys.exit(f"error: no such file: {a.input}")

    print(f"wrote {a.output}")


if __name__ == "__main__":
    main()
