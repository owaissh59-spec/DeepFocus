# Perioperative Care notes → fold-and-staple booklets (Legal, left binding)

Your repo contains **two different documents** from two different generator
scripts. Both are converted. Filenames now say which is which, verified by
extracting the title text back out of each finished PDF.

| Booklet | Title on page 1 | Words | Tables | MCQs | Pages | Sheets |
|---|---|---|---|---|---|---|
| `EXAM_FOCUSED_Booklet_LEGAL_44p_*.pdf` | SUPPLEMENTARY NOTES — **EXAM-FOCUSED** | 18,720 | 55 | 77 | 44 | 11 |
| `GAP_ANALYSIS_Booklet_LEGAL_60p_*.pdf` | SUPPLEMENTARY NOTES — **WHAT YOUR PDF DID NOT COVER** | 27,858 | 71 | 88 | 60 | 15 |

The exam-focused set is the **smaller** of the two. The gap-analysis set is
~49 % more words, which is why it runs 60 pages instead of 44.

Sources: `create_exam_focused_notes.py` → exam-focused;
`create_perioperative_supplement.py` → gap-analysis. Only the exam-focused
`.docx` is committed in your repo; the gap-analysis one is regenerated from its
script.

## Which file to print

`_1sig` = one signature, everything nested, one fold, one staple.
`_4sig` = gatherings of 4 sheets; fold and staple each separately, then stack.

| | recommended |
|---|---|
| Exam-focused (44 p, 11 sheets) | `_1sig` is workable; `_4sig` if your stapler struggles |
| Gap-analysis (60 p, 15 sheets) | **`_4sig`** — 15 nested sheets is 30 leaves and won't staple |

## Print settings — these matter

| Setting | Value |
|---|---|
| Paper | **Legal** (8.5 × 14 in) |
| Orientation | **Landscape** |
| Two-sided | **Yes — flip on SHORT edge** |
| Scale | **100% / "Actual size"** — never "Fit to page" |
| Pages per sheet | **1** (imposition is already in the PDF) |

Landscape content on portrait-fed Legal means the sheet's short-edge hinge acts
as a left/right mirror in the content frame — exactly the swap the two halves
need. That is why it's short edge, not long edge.

**Single signature:** keep the sheets in print order, stack printed-side-up,
fold the whole stack once, staple the spine.

**Gatherings:** sheets arrive in groups of 4 (last group short). Fold and staple
each group on its own, then stack the booklets in order. Reading order runs
straight through.

## Signature thickness

A single signature is comfortable to about 8–10 sheets. Past that the fold
bulges and inner leaves creep outward at the fore-edge:

| | 1 signature | gatherings of 4 |
|---|---|---|
| 44 p / 11 sheets | 22 leaves, creep ~3 mm | 3 booklets, creep ~1 mm |
| 60 p / 15 sheets | 30 leaves, **won't staple** | 4 booklets, creep ~1 mm |

Outer margins are 0.34 in, so nothing is cut off either way — creep only makes
the fore-edge look stepped.

## Layout

Pages are 7 × 8.5 in with small **mirrored** margins — 0.34 in outer, 0.52 in at
the fold — so text clears the spine without wasting the outer edge. Odd pages
are rectos (gutter left), even pages versos (gutter right). Page numbers sit on
the outer corner. Every MCQ is bound so a question never separates from its
answer across a page turn.

## How the sources were interpreted

Neither `.docx` uses Heading styles — every paragraph is `Normal`, with
structure carried in direct formatting. Roles are recovered from the
(bold, size, colour) signature:

| Signature | Role |
|---|---|
| bold 17pt navy `#1F3B73` | title |
| bold 10.5pt green `#1B6B3A` | subtitle |
| 9pt grey `#555555` | scope note |
| bold 14.5–15pt navy | section heading |
| bold 11.5–12pt green | subsection |
| bold 10.5pt **purple `#6A288F`** | sub-subsection *(gap-analysis only)* |
| 9.5pt navy | MCQ question stem |
| 9pt plain | MCQ options |
| 9pt red `#9C2710` | MCQ answer + explanation |
| `▪` prefix | bullet |
| single-cell table | callout box |

Everything is accounted for: 513 paragraphs + 55 tables (exam-focused),
546 + 71 (gap-analysis).

## Fonts

The notes use 45 distinct non-ASCII characters (`→ ▪ ≥ ≤ ≈ ↑ ↓ ∝ ₂ ⁶ γ µ ° ⚠` …).
The built-in PDF fonts cover none of the arrows or maths signs, so several
hundred characters would have silently vanished. `fonts/` bundles DejaVu Sans
Condensed, which covers all but two, and being condensed fits more per line.

The two it lacks are `✅` and `❌` in the gap-analysis coverage-audit table — no
general text font has them. They are remapped to `✔` and `✘`, which DejaVu does
have, so the audit legend still reads correctly.

## Rebuilding

```bash
python3 -m venv .venv
.venv/bin/pip install pypdf reportlab python-docx

.venv/bin/python render_docx.py notes.docx pages.pdf
.venv/bin/python impose.py pages.pdf booklet.pdf -v                    # one signature
.venv/bin/python impose.py pages.pdf booklet.pdf --sheets-per-sig 4 -v # gatherings of 4
```

`impose.py` pads to a multiple of 4, warns when a signature is too thick to
staple, and works on any PDF, not just these.

## Files

| File | What it is |
|---|---|
| `EXAM_FOCUSED_Booklet_LEGAL_44p_1sig.pdf` | exam-focused, one signature |
| `EXAM_FOCUSED_Booklet_LEGAL_44p_4sig.pdf` | exam-focused, gatherings of 4 |
| `GAP_ANALYSIS_Booklet_LEGAL_60p_1sig.pdf` | gap-analysis, one signature |
| `GAP_ANALYSIS_Booklet_LEGAL_60p_4sig.pdf` | gap-analysis, gatherings of 4 |
| `*_pages_reading_order.pdf` | 7 × 8.5 in, plain reading order, for screen |
| `*_source.docx` | the exact `.docx` each booklet was built from |
| `render_docx.py` | `.docx` → reading-order booklet pages |
| `impose.py` | reading-order pages → imposed sheets, 1 or N signatures |
| `make_test_pages.py`, `test_booklet.pdf` | 16 numbered pages, for a fold test |
| `fonts/` | DejaVu Sans Condensed (licence below) |

## Attribution

`fonts/` contains DejaVu Sans Condensed from the
[DejaVu Fonts project](https://dejavu-fonts.github.io/) (v2.37), under the
[DejaVu licence](https://dejavu-fonts.github.io/License.html), a permissive
Bitstream Vera derivative. Full text in `fonts/LICENSE-DejaVu.txt`. Files are
redistributed unmodified.
