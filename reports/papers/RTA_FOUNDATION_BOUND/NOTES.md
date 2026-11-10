# NOTES — RTA_FOUNDATION_BOUND (assembly notes; not part of the paper)

Build: `cd src && pdflatex -output-directory=../build main.tex` (x3). Output: RTA_FOUNDATION_BOUND.pdf (119 pp). 0 errors, 0 undefined/multiply-defined refs.
Tools: tools/conv_partI.py (PAPER_gk_v1 PAPER.md -> LaTeX, numbering +2), tools/edit_partII.py (Bridge C Clean v2 tex edits).

## Sources (read-only)
- Bridge C Clean v2, heavy-daily/2026-10-19-Bridge-C-Clean-v2/ (70 pp) -> Part II + App. C. (rev8, 77 pp, superseded by Clean v2; not used.)
- s_family_paths/PAPER_gk_v1/PAPER.md (27 pp) -> Part I + App. A, B.
- reports/bridges/BRIDGE_C_35 (top, order2, order3, order3b, order3c, order4a) -> Part III; Category B to App. D.
- Ledger v8 entries 37-42, 94, 98-100, 104-109; A51_bridgeC_exact; A53_RTA_maps; RTA manuscript draft 2026-08-24 -> Part IV.

## Open slot
- ORDER4B-SLOT (src/partIII.tex, Section 36, LaTeX comment): order4b was still running at assembly (PREREG, data, empty logs, no REPORT/RESULTS). Its PREREG says all verdicts are Category B (no mod-p certification possible), so it can only add to App. D / a remark.

## Problems found during assembly
1. RTA manuscript uses P_s for two different series; resolved: \Porth_s vs Pi_s, Prop. 2.x proves Pi_s = (-q^s;q^s)_inf g_s.
2. Ledger 40 cited stale exact_dim.json.
3. Preregistration grid design errors: Map B-radial, order2 Map 1.
4. Sign error in order2 Map 3.
5. A52 items 7-8 false as written (excluded).
6. A53: d = 29 closure unexplained (Category B only).
7. Part I Xi_k clashes with shadow Xi; Part II V, E clash with Part III spaces -> renamed V_35, E_36, C_6.
8. Identification of E_36 with Part II's split cited from ledger 32, not reproved in the paper.
9. Duplicate labels sec:lead, thm:profile (Part II vs III) renamed.
10. Part I App. A.5 sentence comparing to "earlier statements" reworded (no mention of past corrections).
11. Remaining cosmetic: one overfull line (66pt, sha256 hash in App. A.4, p.114) and small (<20pt) overfulls in Part I tables p.35.

## Excluded from theorems (Category B; remarks / App. D only)
All closure/rank tests (order2 Map 3, order3, order3b regrouping, order3c closure ranks, order4a: sawtooth candidate falsified, no epsilon closes); numerical fits; |A1(1/2)| = sqrt(pi)/4 (observed); A2 S-law (untested; order4b pending).

## v2 (2026-10-24)
- Added src/glossary.tex ("Symbol key", 44 rows, \ref-based), input after TOC in front.tex. Built with -jobname=v2 -> RTA_FOUNDATION_BOUND_v2.pdf (122 pp). Original PDF untouched.
- order4b still unfinished at v2 build (no REPORT/RESULTS); ORDER4B-SLOT unchanged.

## v3
- Filled ORDER4B-SLOT (two Category B remarks, Sec. 36), App. D items 4a extended + 4b, Open Problems 1-2 updated. RTA_FOUNDATION_BOUND_v3.pdf.
