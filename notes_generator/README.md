# M-Pharmacy Notes Generator

Python scripts that generate the study-notes DOCX
**"Formulation Development of Pharmaceutical and Cosmetic Products (MPH204T)"**
using the same visual design as the existing repo notes (Carewell Pharmacy
template) — **without the diagonal watermark**.

The generated notes are **~125–130 pages** (US Letter, Comic Sans MS 14 pt,
1.5 line spacing), covering all 5 units in depth with diagrams, worked
numericals, summary tables, highlighted boxes, ~130 MCQs, important questions
and a glossary.

## Design replicated
- US Letter page; "CAREWELL PHARMACY" header with brown rule; footer with page
  number and the Telegram line.
- Comic Sans MS body, red centered unit titles (with maroon rule), red
  sub-headings, black bold sub-topics, justified body text.
- Wingdings arrow bullets, maroon/grey styled tables, amber high-yield callout
  boxes, embedded diagrams and MCQs with green answers.

## Files
- `build_notes.py` — the design framework (fonts, colours, header/footer,
  headings, bullets, tables, boxes, figures, MCQs) built on `python-docx`.
- `content.py` — the full academic content for the 5 units, deep-dive sections,
  additional topics & numericals, important questions, MCQ bank, glossary and
  quick revision.
- `make_figures.py` — generates the 19 schematic diagrams (matplotlib) into
  `figures/`.
- `figures/` — the generated PNG diagrams embedded in the notes.
- `estimate_pages.py` — offline pagination estimator (sanity-checks the page
  count without needing Word/LibreOffice).

## Usage
```bash
pip install python-docx matplotlib numpy pillow
cd notes_generator
python make_figures.py     # generate diagrams
python build_notes.py      # build the DOCX (written to the repo root)
```
The DOCX is written one directory up (repo root).

## Notes on rendering
Open the DOCX in Microsoft Word (or Google Docs) for the intended appearance —
the Comic Sans MS font, Wingdings arrow bullets and star markers render
correctly there. The file contains **no watermark**.
