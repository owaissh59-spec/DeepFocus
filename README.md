# Booklet imposition (Legal, single signature, left binding)

Turns notes into a fold-and-staple booklet PDF.

> **Status:** the pipeline is built and verified, but it has **not** yet been run
> on the real Perioperative Care notes — that `.docx` never arrived intact.
> Every PDF in this repo contains **placeholder text only**.

## Print settings

| Setting | Value |
|---|---|
| Paper | Legal (8.5 x 14 in) |
| Orientation | Landscape |
| Duplex | Two-sided, **flip on short edge** |
| Scale | 100% / "Actual size" — do **not** use "Fit to page" |
| Pages per sheet | 1 (imposition is already baked into the PDF) |

Print, stack all sheets in order printed-side-up, fold the whole stack once
down the middle, staple through the spine.

## Files

| File | What it is |
|---|---|
| `typeset.py` | `.docx` / `.md` / `.txt` -> reading-order 7 x 8.5 in pages |
| `impose.py` | reading-order pages -> imposed landscape Legal sheets |
| `make_test_pages.py` | numbered pages for verifying folds |
| `sample_booklet.pdf` | **placeholder** — imposed, ready to print |
| `sample_pages.pdf` | **placeholder** — reading order, before imposition |
| `test_booklet.pdf` | 16 numbered pages, imposed — use this to test folding |

## Usage

```bash
python3 -m venv .venv
.venv/bin/pip install pypdf reportlab python-docx

.venv/bin/python typeset.py notes.docx pages.pdf --title "Perioperative Care"
.venv/bin/python impose.py pages.pdf booklet.pdf -v
```

## Layout

Pages are 7 x 8.5 in with small mirrored margins — 0.34 in on the outer edge,
0.52 in at the fold — so text clears the spine without wasting the outer edge.

Imposition for `N` pages (padded to a multiple of 4), sheet `i` from the
outside in:

```
front:  [ N-2i+2 | 2i-1   ]
back:   [ 2i     | N-2i+1 ]
```

Landscape content on portrait-fed Legal means the sheet's short-edge hinge
becomes a left/right mirror in the content frame — which is exactly the swap
the two halves need. Hence short-edge duplex.

## Signature size caveat

One signature holds together well up to roughly 8-10 sheets (32-40 pages).
Beyond that the fold bulges and inner leaves creep outward past the outer ones.
`impose.py -v` warns when you cross that line.
