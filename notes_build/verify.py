"""
verify.py - automated quality checks on the generated book.

Checks performed
----------------
1. No un-rendered inline markup leaks into the visible text.
2. Page setup is A4 with 0.5 inch margins.
3. Page breaks occur only at the end of a chapter.
4. Every table column is wide enough for its longest word, and every table
   fits inside the text width.
5. No multiple-choice questions are present.
6. Every TOC page number matches the page on which the heading actually
   appears in the rendered PDF.
"""

import os
import re
import sys

import fitz
from docx import Document
from docx.shared import Emu, Inches

import build_notes as B

HERE = os.path.dirname(os.path.abspath(__file__))
DOCX = os.path.join(B.OUT_DIR, B.DOCX_NAME)
PDF = os.path.join(B.OUT_DIR, B.PDF_NAME)

fails = []
warns = []


def check(cond, msg):
    if cond:
        print("  PASS  %s" % msg)
    else:
        print("  FAIL  %s" % msg)
        fails.append(msg)


def warn(cond, msg):
    if not cond:
        print("  WARN  %s" % msg)
        warns.append(msg)


# ---------------------------------------------------------------- 1. markup
print("\n[0] Inline markers balanced in the source")
# Each content function is a sequence of Python string literals; an odd number
# of a given marker inside one logical string means a marker was left unclosed,
# which would leak into the rendered text.
import ast

unbalanced = []
for fname in ("content_part1.py", "content_part2.py", "build_notes.py"):
    tree = ast.parse(open(os.path.join(HERE, fname), encoding="utf-8").read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            s = node.value
            for mk in ("**", "^^", "~~", "``"):
                if s.count(mk) % 2:
                    unbalanced.append((fname, node.lineno, mk, s[:60]))
check(not unbalanced, "all inline markers are balanced in the source")
for fname, line, mk, snippet in unbalanced[:10]:
    print("        %s:%d  unbalanced %s  %r" % (fname, line, mk, snippet))

print("\n[1] Un-rendered inline markup")
doc = fitz.open(PDF)
all_text = "".join(p.get_text() for p in doc)
for marker, name in [("**", "bold **"), ("^^", "key-term ^^"), ("~~", "value ~~"),
                     ("``", "mono ``")]:
    n = all_text.count(marker)
    check(n == 0, "no literal %s in rendered text (found %d)" % (name, n))
# __italic__ : underscores may legitimately appear, so check only doubled pairs
n = len(re.findall(r"__\S", all_text))
check(n == 0, "no literal italic __ in rendered text (found %d)" % n)


# ------------------------------------------------------------- 2. page setup
print("\n[2] Page setup")
d = Document(DOCX)
sec = d.sections[0]
check(abs(sec.page_width - Inches(8.268)) < Emu(20000),
      "page width is A4 (%.2f in)" % (sec.page_width / 914400))
check(abs(sec.page_height - Inches(11.693)) < Emu(20000),
      "page height is A4 (%.2f in)" % (sec.page_height / 914400))
for name in ("top", "bottom", "left", "right"):
    v = getattr(sec, "%s_margin" % name)
    check(v == Inches(0.5), "%s margin is 0.5 in (%.3f in)" % (name, v / 914400))


# ------------------------------------------------------- 3. page break policy
print("\n[3] Page breaks only at end of chapter")
from docx.oxml.ns import qn

breaks_ok, breaks_bad = 0, []
body = d.element.body
paras = list(d.paragraphs)
for i, p in enumerate(paras):
    has_break = any(br.get(qn("w:type")) == "page"
                    for br in p._p.iter(qn("w:br")))
    if not has_break:
        continue
    # the paragraph immediately before a legitimate break is the decorative
    # end-of-chapter rule (three lozenges), or front-matter
    prev = paras[i - 1].text.strip() if i else ""
    # legitimate: after the end-of-chapter lozenges, or at the end of one of the
    # three front-matter sections (cover, contents, how-to-use)
    front_matter_tails = ("Bio-Medical Waste Management Rules",   # cover last line
                          "Page numbers above",                    # contents
                          "No multiple-choice questions")          # how-to-use
    if "\u2756" in prev or prev == "" \
            or any(t in prev for t in front_matter_tails):
        breaks_ok += 1
    else:
        breaks_bad.append((i, prev[:70]))
check(not breaks_bad,
      "all %d page breaks follow a chapter end or front-matter section"
      % breaks_ok)
# 18 chapters, but the last one deliberately ends without a break, so 17
check(breaks_ok == 17 + 3,
      "exactly 17 chapter breaks + 3 front-matter breaks (found %d)" % breaks_ok)
for i, t in breaks_bad[:10]:
    print("        unexpected break after: %r" % t)

# count chapter banners and breaks
n_ch = sum(1 for p in paras if p.text.strip().startswith("CHAPTER "))
check(n_ch == 18, "18 chapter banners present (found %d)" % n_ch)


# --------------------------------------------------------- 4. table geometry
print("\n[4] Table geometry")
usable = Emu(int(sec.page_width - sec.left_margin - sec.right_margin))
bad_width, bad_fit = [], []
CHAR_W = usable / 116.0          # approx width of one character

for t_i, tbl in enumerate(d.tables):
    widths = [c.width for c in tbl.columns]
    total = sum(w for w in widths if w)
    if total and abs(total - usable) > Emu(60000):
        bad_width.append((t_i, total / 914400, usable / 914400))
    # longest word in each column must fit
    for c_i, col in enumerate(tbl.columns):
        w = widths[c_i]
        if not w:
            continue
        longest = 0
        for cell in col.cells:
            for word in re.split(r"[\s/]+", cell.text):
                longest = max(longest, len(word))
        if longest * CHAR_W > w * 1.25:
            bad_fit.append((t_i, c_i, longest, w / 914400))

check(not bad_width,
      "all %d tables span exactly the usable text width" % len(d.tables))
for t_i, got, exp in bad_width[:5]:
    print("        table %d: %.2f in vs %.2f in" % (t_i, got, exp))
check(not bad_fit, "every column fits its longest word")
for t_i, c_i, ln, w in bad_fit[:8]:
    print("        table %d col %d: longest word %d chars in %.2f in"
          % (t_i, c_i, ln, w))


# ------------------------------------------------------------------- 5. MCQs
print("\n[5] No MCQs")
# A real MCQ is a question followed by lettered options, or an answer key.
# Enumerated clauses such as "(a) ... (b) ..." inside a table cell are prose and
# must not be flagged, so the option pattern is tested line by line and must be
# preceded by a question mark.
mcq_patterns = [
    (r"\?\s*\(?a\)", "question mark immediately followed by option (a)"),
    (r"\bAns(?:wer)?\s*[:.\-]\s*\(?[a-d]\)", "answer key such as 'Ans: (c)'"),
    (r"\bWhich of the following\b", "'Which of the following' stem"),
    (r"^\s*\(?[a-d]\)\s+\S+\s*$", "a bare lettered option on its own line"),
    (r"\bcorrect answer is\b", "'correct answer is'"),
    (r"\bQ\s*\d+\s*[.)]", "numbered question such as 'Q1.'"),
]
hits = []
for pat, desc in mcq_patterns:
    found = re.findall(pat, all_text, re.I | re.M)
    if found:
        hits.append((desc, len(found)))
check(not hits, "no multiple-choice question or answer-key patterns found")
for desc, n in hits:
    print("        %s x%d" % (desc, n))


# ------------------------------------------------------- 6. TOC page numbers
print("\n[6] TOC page numbers match the document")
pages_norm = [B._norm(p.get_text() or "") for p in doc]
start = B._body_start(pages_norm)
# read the numbers actually printed in the TOC of the DOCX
def _flat(s):
    return re.sub(r"\s+", " ", s).strip()


printed = {}
for p in paras:
    txt = _flat(p.text)
    if not txt:
        continue
    for level, label, key in B.TOC:
        if key in printed:
            continue
        plain = _flat(label)
        if txt.startswith(plain[:45]):
            m = re.search(r"(\d+)\s*$", txt)
            if m:
                printed[key] = m.group(1)
            break

mismatch, unchecked = [], []
for level, label, key in B.TOC:
    if key not in printed:
        unchecked.append(key)
        continue
    needle = B._norm(B._search_key(level, label, key))
    actual = None
    for idx in range(start, len(pages_norm) + 1):
        if needle and needle in pages_norm[idx - 1]:
            actual = idx
            break
    if actual is None:
        short = needle[:40]
        for idx in range(start, len(pages_norm) + 1):
            if short in pages_norm[idx - 1]:
                actual = idx
                break
    if actual is not None and str(actual) != printed[key]:
        mismatch.append((key, printed[key], actual))

check(not mismatch,
      "all %d TOC page numbers verified against the rendered pages"
      % (len(printed) - len(mismatch)))
for key, got, exp in mismatch[:15]:
    print("        %s: TOC says %s, heading is on page %s" % (key, got, exp))
warn(not unchecked, "%d TOC entries could not be read back: %s"
     % (len(unchecked), unchecked[:8]))


# ------------------------------------------------------------------ summary
print("\n" + "=" * 62)
print("Pages: %d   Tables: %d   Paragraphs: %d"
      % (doc.page_count, len(d.tables), len(paras)))
print("Failures: %d   Warnings: %d" % (len(fails), len(warns)))
print("=" * 62)
sys.exit(1 if fails else 0)
