# Home Nursing — Complete Study Notes (JKSSB Junior Pharmacist)

Generator for the study-notes book `out/Home_Nursing_Complete_Notes_JKSSB_Junior_Pharmacist.docx`.

## The book

| | |
|---|---|
| Pages | 142 (A4, 21 × 29.7 cm) |
| Chapters | 24 syllabus chapters + Appendix A (Rapid Revision) |
| Sections | 206 numbered sections, all listed in the index with page numbers |
| Tables | 242 |
| Contents | No MCQs — study notes only |

Covers every topic of the Home Nursing syllabus section, in syllabus order:
Introduction to Home Nursing · Nurse · Sick Room · Bed Making · Patient's Toilet ·
Observation of the Sick · Infection · Surgical Techniques · Diet · Medicines ·
Special Conditions & Treatments · Bandaging · Further Observations ·
Immunity & Infectious Diseases · Care of the Aged and Long-term Patient ·
Care of the Mentally Ill Patient · Special Drugs, their Control & Administration ·
Preparation of the Patient for Operation and the After Care · Shock and Blood Transfusion ·
Special Treatment · Nursing in Special Diseases · The Hospital Services ·
Preparation for Special Treatment · Child Birth and Its Management.

## Layout rules implemented

* **A4** page, margins 1.7 cm (L/R), 1.6/1.5 cm (T/B).
* **Page breaks only at chapter ends** — applied as `page-break-before` on the chapter
  band, so a chapter that ends at the foot of a page leaves no empty page behind.
* **Proportional table columns** — `docx_kit.proportional_widths()` sizes every column
  from the text it actually carries, clamped so no column is narrower than its longest
  word and none wider than it needs. Table layout is fixed, header rows repeat.
* **Real page numbers in the Table of Contents** (static text, not field codes).

## Files

| File | Contents |
|---|---|
| `docx_kit.py` | Styling toolkit — `Book` class, headings, tables, boxes, footer, column-width engine |
| `content_a.py` | Chapters 1–5 |
| `content_b.py` | Chapters 6–9 |
| `content_c.py` | Chapters 10–13 |
| `content_d.py` | Chapters 14–17 |
| `content_e.py` | Chapters 18–21 |
| `content_f.py` | Chapters 22–24 + Appendix A |
| `build.py` | Cover, syllabus map, index, and the two-pass build |

## Rebuilding

```bash
pip install python-docx
python3 build.py
```

`build.py` builds the document, renders it to PDF with LibreOffice, reads back the page
on which every chapter and section actually starts, and rebuilds with those numbers —
repeating until the numbers stop changing. It prints a verification line; the index is
correct when it reports `TOC mismatches: 0`.

Requires LibreOffice (`soffice`, path set at the top of `build.py`) and `pdftotext`
(poppler-utils) for the page-number pass.
