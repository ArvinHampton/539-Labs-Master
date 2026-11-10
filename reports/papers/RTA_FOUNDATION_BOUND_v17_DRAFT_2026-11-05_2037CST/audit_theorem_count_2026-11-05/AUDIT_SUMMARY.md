# Deep Theorem-Count Audit — RTA v17 DRAFT (RECONCILED)
Date: 2026-11-05 America/Chicago (reconciled same day)
Scope: read-only. PDF + active TeX input tree. Not a proof-validity audit.
Manuscript: not edited.

## Artifacts
- PDF: `RTA_FOUNDATION_BOUND_v17_DRAFT.pdf` (156 pp)
- Entry: `src/main_v17.tex` (52 active inputs)
- Audit dir: this directory
- Full row map: `v17_all_printed_theorems_74.csv` (74 rows)
- Env→PDF map: `v17_theorem_source_to_pdf_map_RECONCILED.csv` (63 rows)

## Counter architecture (`main_preamble.tex`)
`\newtheorem{theorem}{Theorem}[section]` with proposition/lemma/corollary/definition/remark/conjecture/catbremark sharing the theorem counter.
Therefore “numbered statements” ≠ “Theorems”.

---

## FINAL ANSWER — printed Theorem count

### Trustworthy total: **exactly 74** printed Theorems in the v17 PDF

Breakdown:
| source form | count | notes |
|-------------|------:|-------|
| Active `\begin{theorem}` | **63** | simulated section.N numbers; 0 duplicate IDs; all 63 found in PDF |
| Part I hardcoded `\textbf{Theorem N.M}` | **11** | `partI/p1_body.tex` only; all 11 found in PDF |
| **TOTAL printed Theorems** | **74** | |

No active `\begin{theorem}` was missed by extraction once multiline/indent PDF artifacts were handled.
No duplicate statement IDs among the 74 (foundation p.145 “Theorem 8.1 (Part I…)” is a citation restatement of Part I 8.1, not a 12th Part I theorem).

### Part I hardcoded list (all 11) → PDF
| id | PDF page |
|----|---------|
| 5.1, 5.3 | 17 |
| 5.5 | 18 |
| 6.6 | 23 |
| 6.9 | 25 |
| 7.4 | 26 |
| 7.6, 7.7 | 27 |
| 8.1 | 28 |
| 8.12 | 33 |
| 8.22 | 38 |

### “Exactly 5 additional hardcoded statements?”
**Yes, relative to the earlier regex STATEMENT extract.** That extract recovered 6 Part I headers (5.1, 5.3, 6.6, 7.6, 7.7, 8.1) and missed **5** more that are present in both source and PDF: **5.5, 6.9, 7.4, 8.12, 8.22** (leading whitespace / PDF artifact before `Theorem` broke `^Theorem` anchoring). Total Part I hardcoded = 6 + 5 = **11**, not 5 alone.

### v17 delta vs v16
- `\begin{theorem}`: 60 → **63** (+3 boundary theorems 43.8, 43.9, 43.10)
- Foundation renumber only: 42.3 → 44.3

---

## SUPERSEDED numbers (do not use)

| Prior figure | Where it appeared | Why superseded |
|--------------|-------------------|----------------|
| PDF canonical **71** / unique **70** | §A original table | Included citation/restatement noise; not a full Part I census |
| Cleaned PDF unique **68** | “Refined PDF cleaned” table | Undercount: missed 5 Part I headers (indent) + Theorem 21.3 (line-split `Theorem` / `21.3`) → 68+5+1=**74** |
| Uncertainty **~67/70** | §Uncertainty | Regex-only; replaced by full 63+11 enumeration |
| “63 + 5 hardcoded ≈ 68” | informal | Wrong Part I total; hardcoded count is **11**, not 5 |

---

## Shared-counter environments (exact, active tree, comment-stripped)
| env | v16 | v17 | delta |
|-----|----:|----:|------:|
| theorem | 60 | 63 | +3 |
| proposition | 90 | 94 | +4 |
| lemma | 24 | 24 | 0 |
| corollary | 14 | 14 | 0 |
| definition | 6 | 13 | +7 |
| remark | 33 | 41 | +8 |
| conjecture | 1 | 1 | 0 |
| catbremark | 8 | 8 | 0 |
| **TOTAL** | **236** | **258** | **+22** |

---

## NOTES_v16 “82” vs complete Category A box count

| object | count | meaning |
|--------|------:|---------|
| NOTES_v16 `total_now = 82 (=71+11)` | **82** | **Selected** editorial ledger of Category A *numbered statements* (mix of Thm/Prop/Def; only some are Theorems). Documentary, not recomputed from boxes. |
| v16 active `\catA{...}` uses | **127** | Independent complete count of Category A status boxes in the v16 input tree (excludes `\newcommand`). |
| v17 active `\catA{...}` uses | **133** | Same metric on v17 tree. |

**82 ≠ 127 ≠ 63 ≠ 74 ≠ 258.** Different objects:
- 82 = selected Cat A ledger (NOTES)
- 127/133 = all `\catA` boxes
- 63 = `\begin{theorem}`
- 74 = printed Theorem headers (63 + 11 Part I)
- 258 = all shared-counter envs

---

## Method (why 74 is exact, not regex-only)
1. Expand active input tree from `main_v17.tex`; strip TeX comments.
2. Simulate `theorem` counter within `section` across all shared-counter `\begin{...}` → predict all 63 theorem numbers; verify no duplicate predicted IDs.
3. Locate each predicted `Theorem N.M` in `pdftotext -layout` (handle indented lines and the p.73 split header for 21.3). Result: **63/63** mapped.
4. Separately parse all `\textbf{Theorem N.M}` in `partI/p1_body.tex` → **11**; locate each in PDF → **11/11**.
5. Discard false positive “Theorem 1.1]” (external citation) and mid-body restatements.

Remaining uncertainty: **none** on the printed Theorem total (74). Proof validity of those theorems is out of scope.
