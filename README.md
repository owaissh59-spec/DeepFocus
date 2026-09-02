# Perioperative Care notes → fold-and-staple booklets (Legal, left binding)

There are **two different documents** in your `DeepFocus` repo, produced by two
different generator scripts. Both are converted here.

| Booklet | Source document | Pages | Legal sheets |
|---|---|---|---|
| `Perioperative_Care_Booklet_LEGAL.pdf` | *SUPPLEMENTARY NOTES — EXAM-FOCUSED* (77 MCQs, 55 tables) | 44 | 11 |
| `Supplementary_Notes_Booklet_LEGAL.pdf` | *SUPPLEMENTARY NOTES — WHAT YOUR PDF DID NOT COVER* (88 MCQs, 71 tables) | 60 | 15 |
| `Supplementary_Notes_Booklet_LEGAL_4sig.pdf` | same as above, split into 4 gatherings | 60 | 15 |

The two are genuinely different documents, not versions of one another — the
second is a gap-analysis against the studied PDF and opens with a coverage-audit
table; the first is the trimmed syllabus-ordered set.

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

**Single signature** (the two files without `_4sig`): keep the sheets in the
order they print, stack printed-side-up, fold the whole stack once, staple the
spine.

**Four gatherings** (`_4sig`): the sheets arrive in groups of 4, 4, 4 and 3.
Fold and staple **each group separately**, then stack the four booklets in
order. Reading order runs straight through.

## Read this before printing the 60-page one

`Supplementary_Notes_Booklet_LEGAL.pdf` is a single signature of **15 sheets**,
because that is what you asked for — but it is not really practical:

- 15 nested sheets is **30 leaves**. A desk stapler tops out around 20–25 and
  will not reach through it; you'd need a long-reach saddle stapler.
- Creep at the fore-edge will be roughly **4–6 mm** — the inner leaves stick
  out noticeably past the outer ones.

`Supplementary_Notes_Booklet_LEGAL_4sig.pdf` is the same content in gatherings
of 4 sheets. Each folds flat, staples with anything, and creep drops to about
1 mm. Only cost is four stapled booklets instead of one.

The 44-page exam-focused booklet at 11 sheets is borderline but workable as a
single signature.

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
| bold 10.5pt **purple `#6A288F`** | sub-subsection *(supplement only)* |
| 9.5pt navy | MCQ question stem |
| 9pt plain | MCQ options |
| 9pt red `#9C2710` | MCQ answer + explanation |
| `▪` prefix | bullet |
| single-cell table | callout box |

Both documents are fully accounted for: 546 paragraphs + 71 tables for the
supplement, 513 + 55 for the exam-focused set.

## Fonts

The notes use 45 distinct non-ASCII characters (`→ ▪ ≥ ≤ ≈ ↑ ↓ ∝ ₂ ⁶ γ µ ° ⚠` …).
The built-in PDF fonts cover none of the arrows or maths signs, so several
hundred characters would have silently vanished. `fonts/` bundles DejaVu Sans
Condensed, which covers all but two, and being condensed fits more per line.

The two it doesn't cover are the emoji `✅` and `❌` in the coverage-audit table.
No general text font has them. They are remapped to `✔` and `✘`, which DejaVu
does have, so the audit legend still reads correctly.

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
| `render_docx.py` | `.docx` → reading-order booklet pages |
| `impose.py` | reading-order pages → imposed sheets, 1 or N signatures |
| `make_test_pages.py` | numbered pages for a fold test |
| `test_booklet.pdf` | 16 numbered pages imposed — print this first |
| `*_pages.pdf` | reading order, 7 × 8.5 in, for screen reading |
| `fonts/` | DejaVu Sans Condensed (licence below) |

## Attribution

`fonts/` contains DejaVu Sans Condensed from the
[DejaVu Fonts project](https://dejavu-fonts.github.io/) (v2.37), under the
[DejaVu licence](https://dejavu-fonts.github.io/License.html), a permissive
Bitstream Vera derivative. Full text in `fonts/LICENSE-DejaVu.txt`. Files are
redistributed unmodified.
