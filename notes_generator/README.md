# M-Pharmacy Notes Generator

Python scripts that generate the study-notes DOCX
**"Advances in Drug Delivery System (MPT102T)"**
using the same visual design as the existing repo notes (Carewell Pharmacy
template) — **without the diagonal watermark**.

The generated notes are **150+ pages** (US Letter, Comic Sans MS 14 pt,
1.5 line spacing) and cover the complete MPT102T syllabus
(M. Pharmacy – Pharmaceutical Technology, Semester I) in depth with 33
diagrams, worked numericals, summary tables, highlighted boxes, model
short-notes, important questions, a glossary and a quick-revision section.

> The examination for this subject is **theoretical**, so the notes contain
> **no MCQs** — the emphasis is on definitions, classifications, mechanisms,
> labelled diagrams, merits/demerits and applications.

## Syllabus covered
1. Sustained Release (SR) & Controlled Release (CR) formulations
2. Oral sustained-release DDS (dissolution, diffusion, osmotic, ion-exchange,
   bioerodible, mucoadhesive mechanisms)
3. Microencapsulation
4. Implants and Inserts (subcutaneous, i.m., ocular, vaginal, uterine)
5. Transdermal DDS (skin permeation, iontophoresis, sonophoresis, latest
   developments)
6. Personalized Medicine (pharmacogenetics, customized DDS, bioelectronic
   medicine, 3D printing, telepharmacy)

Plus supporting chapters: NDDS introduction, polymer selection & monographs,
formulation optimization (DoE/QbD), evaluation methods, stability & regulatory
considerations, therapeutic applications, landmark case studies and future
trends.

## Design replicated
- US Letter page; "CAREWELL PHARMACY" header with brown rule; footer with page
  number and the Telegram line.
- Comic Sans MS body, red centered unit titles (with maroon rule), red
  sub-headings, black bold sub-topics, justified body text.
- Wingdings arrow bullets, maroon/grey styled tables, amber high-yield callout
  boxes and embedded schematic diagrams.

## Files
- `build_notes.py` — the design framework (fonts, colours, header/footer,
  headings, bullets, tables, boxes, figures) built on `python-docx`.
- `content.py` — the full academic content for all six units plus the
  supporting chapters, important questions, glossary and quick revision.
- `make_figures.py` — generates the 33 schematic diagrams (matplotlib) into
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
python estimate_pages.py   # (optional) estimate the page count
```
The DOCX is written one directory up (repo root) as
`Advances in Drug Delivery System (MPT102T).docx`.

## Notes on rendering
Open the DOCX in Microsoft Word (or Google Docs) for the intended appearance —
the Comic Sans MS font and Wingdings arrow bullets render correctly there. The
file contains **no watermark**.
