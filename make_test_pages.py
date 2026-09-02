#!/usr/bin/env python3
"""Generate a PDF of big numbered 7x8.5in pages, to verify imposition/folding."""
import sys

from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

IN = 72.0
W, H = 7 * IN, 8.5 * IN

n = int(sys.argv[1]) if len(sys.argv) > 1 else 16
out = sys.argv[2] if len(sys.argv) > 2 else "test_pages.pdf"

c = canvas.Canvas(out, pagesize=(W, H))
for i in range(1, n + 1):
    # frame so you can see the trim/fold alignment after printing
    c.setStrokeColor(HexColor("#cccccc"))
    c.setLineWidth(0.5)
    c.rect(9, 9, W - 18, H - 18)

    c.setFillColor(HexColor("#111111"))
    c.setFont("Helvetica-Bold", 160)
    c.drawCentredString(W / 2, H / 2 - 55, str(i))

    c.setFont("Helvetica", 11)
    label = "recto (gutter left)" if i % 2 else "verso (gutter right)"
    c.drawCentredString(W / 2, H - 40, f"page {i} of {n} - {label}")
    c.showPage()
c.save()
print(f"wrote {out} ({n} pages at 7 x 8.5 in)")
