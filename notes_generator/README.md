# M-Pharmacy Notes Generator

Python scripts that generate the study-notes DOCX
**"Formulation Development of Pharmaceutical and Cosmetic Products (MPH204T)"**
using the same visual design as the existing repo notes (Carewell Pharmacy
template) — **without the diagonal watermark**.

## Design replicated
- US Letter page, "CAREWELL PHARMACY" header with brown rule, footer with page
  number and Telegram line.
- Comic Sans MS body, red centered unit titles, red sub-headings, black bold
  sub-topics, justified body text.
- Wingdings arrow bullets and maroon/grey styled tables.

## Files
- `build_notes.py` — the design framework (fonts, colours, header/footer,
  headings, bullets, tables) built on `python-docx`.
- `content.py` — the full academic content for the 5 units + syllabus.

## Usage
```bash
pip install python-docx
cd notes_generator
python build_notes.py
```
The DOCX is written one directory up (repo root).
