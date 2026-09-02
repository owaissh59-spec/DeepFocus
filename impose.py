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


def signature_order(n_pages: int, sheets_per_sig=None):
    """
    Yield (left_page, right_page) 1-indexed for each sheet side.

    sheets_per_sig=None  -> one signature holding everything (all sheets nested)
    sheets_per_sig=k     -> gatherings of k sheets (4k pages) each, folded
                            separately and then stacked. The final gathering
                            takes whatever is left.
    """
    n = n_pages
    if sheets_per_sig is None:
        groups = [(1, n)]
    else:
        per = sheets_per_sig * 4
        groups = [(s + 1, min(s + per, n)) for s in range(0, n, per)]

    for start, end in groups:
        m = end - start + 1                       # pages in this gathering
        off = start - 1
        for i in range(1, m // 4 + 1):
            yield (off + m - 2 * i + 2, off + 2 * i - 1)      # front
            yield (off + 2 * i, off + m - 2 * i + 1)          # back


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


def impose(in_path, out_path, shrink=1.0, verbose=False, sheets_per_sig=None):
    reader = PdfReader(in_path)
    real = len(reader.pages)

    # Pad to a multiple of 4 -- a signature is always whole sheets.
    n = real + (-real % 4)
    sheets = n // 4

    writer = PdfWriter()
    plan = []

    for slot, (left, right) in enumerate(signature_order(n, sheets_per_sig)):
        sheet = PageObject.create_blank_page(width=SHEET_W, height=SHEET_H)
        sheet.mediabox = RectangleObject((0, 0, SHEET_W, SHEET_H))

        for pageno, x in ((left, 0.0), (right, HALF_W)):
            if pageno <= real:
                place(sheet, reader.pages[pageno - 1], x, shrink)

        writer.add_page(sheet)
        gsheet = slot // 2 + 1
        sig = 1 if sheets_per_sig is None else (gsheet - 1) // sheets_per_sig + 1
        plan.append(
            (
                sig,
                gsheet,
                "front" if slot % 2 == 0 else "back",
                left if left <= real else None,
                right if right <= real else None,
            )
        )

    with open(out_path, "wb") as fh:
        writer.write(fh)

    nsigs = max(p[0] for p in plan)

    if verbose:
        blank = lambda p: "blank" if p is None else str(p)
        print(f"  content pages : {real}")
        print(f"  padded to     : {n}  ({n - real} blank)")
        print(f"  legal sheets  : {sheets}")
        print(f"  signatures    : {nsigs}"
              + ("  (single signature)" if nsigs == 1
                 else f"  ({sheets_per_sig} sheets each, last may be short)"))
        print(f"  output pages  : {len(writer.pages)}")
        print("  imposition:")
        prev = None
        for sig, s, side, l, r in plan:
            if sig != prev:
                print(f"    -- signature {sig} --")
                prev = sig
            print(f"    sheet {s:>2} {side:<5}  [ {blank(l):>5} | {blank(r):<5} ]")

        thickest = sheets if nsigs == 1 else sheets_per_sig
        if thickest > 10:
            print(
                f"\n  !! {thickest} sheets nested in one signature will bulge badly."
                "\n     A desk stapler will not reach through it. Consider"
                "\n     --sheets-per-sig 3 or 4, or creep compensation."
            )

    return real, n, sheets, nsigs


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
    ap.add_argument(
        "--sheets-per-sig",
        type=int,
        default=None,
        help="sheets per gathering (default: one signature for everything)",
    )
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()

    try:
        impose(a.input, a.output, a.shrink, a.verbose, a.sheets_per_sig)
    except FileNotFoundError:
        sys.exit(f"error: no such file: {a.input}")

    print(f"wrote {a.output}")


if __name__ == "__main__":
    main()
