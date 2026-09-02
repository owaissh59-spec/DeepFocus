# Perioperative Care — Supplementary Notes, as a fold-and-staple booklet

`Perioperative_Care_Booklet_LEGAL.pdf` — **22 sheet-sides → 11 Legal sheets → 44 booklet pages.**
Print it, fold the stack once, staple the spine.

## Print settings — these matter

| Setting | Value |
|---|---|
| Paper | **Legal** (8.5 × 14 in) |
| Orientation | **Landscape** |
| Two-sided | **Yes — flip on SHORT edge** |
| Scale | **100% / "Actual size"** — never "Fit to page" |
| Pages per sheet | **1** (imposition is already in the PDF) |

Then: keep the 11 sheets in the order they come out, stack them printed-side-up,
fold the whole stack once down the middle, staple through the spine.

Landscape content on portrait-fed Legal means the sheet's short-edge hinge acts
as a left/right mirror in the content frame — which is exactly the swap the two
halves need. That is why it's short edge and not long edge.

## What's here

| File | What it is |
|---|---|
| `Perioperative_Care_Booklet_LEGAL.pdf` | **the thing to print** — imposed, 14 × 8.5 in |
| `periop_pages.pdf` | same content in plain reading order, 7 × 8.5 in (screen reading) |
| `render_docx.py` | `.docx` → reading-order booklet pages |
| `impose.py` | reading-order pages → imposed sheets |
| `make_test_pages.py` | numbered pages, for a fold test before the real run |
| `test_booklet.pdf` | 16 numbered pages imposed — print this first |
| `fonts/` | DejaVu Sans Condensed (see licence caveat below) |

## Layout

Pages are 7 × 8.5 in with small **mirrored** margins — 0.34 in outer, 0.52 in at
the fold — so text clears the spine without wasting the outer edge. Odd pages are
rectos (gutter left), even pages versos (gutter right). Page numbers sit on the
outer corner.

## How the source was interpreted

The `.docx` has no Heading styles — every paragraph is `Normal`, and structure
lives in direct formatting. Roles were recovered from the (bold, size, colour)
signature and remapped to real styles:

| Signature in the `.docx` | Role | Count |
|---|---|---|
| bold 17.0 navy `#1F3B73` | title | 1 |
| bold 10.5 green `#1B6B3A` | subtitle | 1 |
| 9.0 grey `#555555` | scope note | 1 |
| bold 14.5 navy | section heading | 18 |
| bold 11.5 green | subsection | 60 |
| 9.5 navy | MCQ question stem | 77 |
| 9.0 plain | MCQ options | 77 |
| 9.0 red `#9C2710` | MCQ answer + explanation | 77 |
| `▪` prefix | bullet | 93 |
| `N.` prefix | numbered rule | 39 |
| 9.5 plain / bold | body | 13 |
| — | tables (12 of them single-cell callouts) | 55 |

Every one of the 513 paragraphs and 55 tables is accounted for. Each MCQ is
wrapped so a question never separates from its answer across a page turn.

The notes use 38 distinct non-ASCII characters (`→ ▪ ≥ ≤ ≈ ↑ ↓ ∝ ₂ ⁶ γ µ °` …).
The built-in PDF fonts cover none of the arrows or maths signs — 385 characters
would have silently vanished. DejaVu Sans Condensed covers all 38 in all four
weights, and being condensed it also fits more per line on a 7-inch page.

## Signature bulge — the one real caveat

You asked for a single signature, and that's what this is: all 11 sheets nested
inside one another. But 11 sheets is past the comfortable limit (~8–10). Expect
the fold to bulge, and the inner leaves to creep outward past the outer ones by
roughly 2–3 mm at the fore-edge. Options:

- **Accept it** — with 0.34 in outer margins nothing gets cut off; it just looks
  slightly stepped at the fore-edge.
- **Trim the fore-edge flush** after folding, if you have a guillotine.
- **Add creep compensation** — shift each sheet's content toward the spine
  proportional to its depth in the nest. Say the word and I'll add it.
- **Split into 2 signatures** of 6 and 5 sheets — folds flat, needs binding
  rather than a single staple.

Also check your stapler reaches ~22 leaves; a standard desk stapler often won't.
A long-reach or saddle stapler will.

## Rebuilding

```bash
python3 -m venv .venv
.venv/bin/pip install pypdf reportlab python-docx

.venv/bin/python render_docx.py periop.docx periop_pages.pdf
.venv/bin/python impose.py periop_pages.pdf Perioperative_Care_Booklet_LEGAL.pdf -v
```

`impose.py` pads to a multiple of 4 and warns when a signature gets too thick.
It works on any PDF, not just this one.

## Attribution

`fonts/` contains DejaVu Sans Condensed, from the
[DejaVu Fonts project](https://dejavu-fonts.github.io/) (v2.37), under the
[DejaVu licence](https://dejavu-fonts.github.io/License.html) — a permissive
Bitstream Vera derivative. Full text in `fonts/LICENSE-DejaVu.txt`. The font
files are redistributed unmodified.
