# AUDITOR — Full-corpus crawl, Batch 01: RTA v16 lock set + v17 DRAFT
Written: 2026-11-09 ~12:50 CST (America/Chicago) by Auditor.
Authority: Owner in chat 2026-11-09 12:34 CST, "All haults lifted" (pt1864u). This lifts the 90% latch, the 15:58 hash/custody halt, and the read-only rule.
Limits kept: this is a new dated file only (exclusive create). No paper, sidecar, NOTES or src file was modified. Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` not touched; re-hashed at write time = `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` (unchanged). No CERT. No Gemini or external sends. No verdict changed.
Method: pdfinfo, sha256sum, stat, full `pdftotext -layout` of both PDFs (v16 148 pages / 96,899 words; v17 156 pages / 101,127 words), active `\input` tree expansion from main_v16.tex and main_v17.tex (comments stripped), `diff -r` of the two src trees, and an exact symbolic (sympy) plus float rank re-computation of the v17 §43 numbers. These are internal-consistency checks, not a CERT.
Paths below: P16 = `/workspace/quantum-comp/reports/papers/RTA_FOUNDATION_BOUND/`, P17 = `/workspace/quantum-comp/reports/papers/RTA_FOUNDATION_BOUND_v17_DRAFT_2026-11-05_2037CST/`.

## (a) PDF custody facts (all times CST)
| | v16 (FROZEN) | v17 DRAFT |
|---|---|---|
| File | P16/RTA_FOUNDATION_BOUND_v16.pdf | P17/RTA_FOUNDATION_BOUND_v17_DRAFT.pdf |
| pdfinfo Pages | 148 | 156 |
| pdfinfo CreationDate | Thu 2026-11-05 11:36:20 CST | Thu 2026-11-05 20:46:59 CST |
| Producer | xdvipdfmx (tectonic) | xdvipdfmx (tectonic) |
| File mtime | 2026-11-06 14:40:35 CST | 2026-11-06 14:40:45 CST |
| Size | 1,207,122 B | 1,249,705 B |
| Computed sha256 | `1fe7b8a2e245e90009c41726db13518b4c752e99ba4e08b4ffd006d8a73c3297` | `9b407e1b0805b2129ce95665b8c2343f9b7ccaa564126277c41b545bfff9d285` |
| Sidecar | `.pdf.sha256` line 1: `1fe7b8a2…73c3297  RTA_FOUNDATION_BOUND_v16.pdf` (relative path) | `.pdf.sha256` line 1: `ee88d1cd57892bafff707e53517df30b81192a5988938ea6159d2dd78733763a  /workspace/…/RTA_FOUNDATION_BOUND_v17_DRAFT.pdf` (absolute path) |
| Sidecar result | **MATCH** | **MISMATCH** (custody discrepancy recorded; sidecar not rewritten) |

Other lock-set hashes: P16/NOTES_v16.md sha `061eac86c303a4ce6dcf74e14b5c4f53a139b3c195bc16e5e4125c7d0d593d03` = its sidecar (MATCH).
Custody note: every file in both folders has mtime 2026-11-06 14:38–14:40 CST, which is a bulk copy or restore event. File mtimes therefore do NOT carry the Nov 5 authoring times. The authoring times come only from pdfinfo CreationDate and from in-file text (NOTES_v16.md:5 "Written: 2026-11-05 ~11:36"; NOTES_v17.md:6 "~20:37 CST").

## (b) v17 sidecar mismatch — QA-fix recompile explanation: **UNDETERMINED**
Evidence FOR a post-delivery recompile:
- P17/DRAFT_MILESTONES.txt:11 "20:42:50 pages rendered; deliverable ready"; :12 "20:45:50 content fixes applied"; :13 "20:46:05 recompiled after QA fixes"; :14 "20:47:04 QA-fix delivered".
- P17/DELIVERY_REPORT_FIX.txt:1 "v17 DRAFT QA-fix recompile — 2026-11-05 CST"; :6 lists the fixes.
- P17/audit_theorem_count_2026-11-05/build_listing.txt:2–8: compile_stdout.txt 20:41, compile_stdout2.txt 20:42, compile_fix/fix2/fix3.txt 20:46, main_v17.pdf **20:47, 1,249,705 B** (equal to the current PDF size). The current CreationDate 20:46:59 is the post-fix build.
- Content changed between the two deliveries: DELIVERY_REPORT.txt:16 reports the pre-fix additive census as thm3/prop7/def9/rem7 = 26. The current active tree census is thm3/prop4/def7/rem8 = 22, consistent with fix item "ledger unnumbered" (DELIVERY_REPORT_FIX.txt:6). qa_pages/ (boundary p.139–142) versus qa_pages_fix/ (p.140–144) shows the layout moved.
Evidence MISSING:
- No record states when the sidecar was written or what file `ee88d1cd…` hashed. DELIVERY_REPORT.txt and DELIVERY_REPORT_FIX.txt quote no PDF sha. A corpus-wide grep of /workspace and the stores finds `ee88d1cd` and `9b407e1b` only in the sidecar itself. The sidecar mtime was lost in the Nov 6 14:40 copy. The pre-fix PDF is not on disk, so it cannot be hashed for comparison.
Verdict: the recompile itself is SUPPORTED. That the sidecar predates it (that is, that `ee88d1cd` hashed the 20:42 build) is NOT established, so the explanation is UNDETERMINED. The format also differs from the v16 sidecar (absolute vs relative path), suggesting a different writer or step. Record as custody discrepancy C17-1. No tampering is inferred.

## (c) Statement inventory (own census; matches audit)
Active-tree census, comment-stripped:
| env | v16 | v17 | Δ |
|---|---:|---:|---:|
| theorem | 60 | 63 | +3 |
| proposition | 90 | 94 | +4 |
| lemma | 24 | 24 | 0 |
| corollary | 14 | 14 | 0 |
| definition | 6 | 13 | +7 |
| remark | 33 | 41 | +8 |
| conjecture | 1 | 1 | 0 |
| catbremark | 8 | 8 | 0 |
| **total** | **236** | **258** | **+22** |
Part I hardcoded `\textbf{Theorem N.M}` (partI/p1_body.tex): 11 in both. **Printed Theorems: v16 60+11 = 71; v17 63+11 = 74; Δ = +3.** This AGREES with audit_theorem_count_2026-11-05/AUDIT_SUMMARY.md:21–28, 50, 67–77. `\catA` boxes: 127 → 133.
Caution: the "71" printed-theorem count of v16 is a different object from the "71" summand in NOTES_v16.md:8 (total_now 82 = 71 + 11 mixed Category A statements). This is a numerical coincidence and must not be conflated (cf. AUDIT_SUMMARY.md:81–94).

The 3 new Theorems (P17/src/partIII_boundary_rank_v17.tex):
- Thm 43.8 `thm:v17-bare` (tex :133–145, PDF p.142): bare stacked selector matrix, rank 24.
- Thm 43.9 `thm:v17-M36` (tex :147–162, p.142): original-table M, rank 36, ker M = {0} ⊕ ker H01, dim 12.
- Thm 43.10 `thm:v17-M48` (tex :164–207, p.143): singleton tuning a_{xy³}: 6−s → 7−s gives rank M′ = 48, plus the spectra of H′ (14 values, Σ = 48) and H01′ (9 values, Σ = 24).
The other 19 new envs: Defs 43.1–43.4, 43.6, 43.7, 43.11 (:12, :24, :32, :50, :113, :121, :210); Rem 43.5 orbits (:69), 43.12 capacity-OPEN (:226), 43.15 Poisson (:251), 43.16 geometry (:255); Props 43.13 compression (:231), 43.14 inert-prime (:239); ledger Rems 42.1–42.4 (partIII_postv16_ledger_v17.tex:32, 36, 40, 44); Props E.1, E.2 (appE_withdrawn_v17.tex:4, 18).
Removed statements: **none**. Every v16 env row is present in v17 in the same order (diff of env/file sequences shows insertions only).
Renumbering: Foundation section 42 → 44 (e.g., Thm 42.3 → 44.3, v17 PDF p.145). Appendix E is appended, so no appendix shifts.
Changed hypotheses: **none**. The only edits to inherited files are a label split: v16 had a DUPLICATE label `lem:parity` (partII/s16_cthird.tex:44 and partIII_improper_v10.tex:4). v17 renames these `lem:parity-cthird` / `lem:parity-improper` and updates refs at s07_lz.tex:98, s16_cthird.tex:70, s17_sfamily.tex:32, s23_deps.tex:10, partIII_improper_v10.tex:17. Statement text is otherwise byte-identical. main_v17 differs from main_v16 only at :3 (front_v17), :50–51 (two new chapters), :61 (appE). glossary_v17 = glossary_v16 byte-identical. partIII_local_adv_v16.tex is byte-identical in both trees.

## (d) Status of new v17 statements, as written
- Thm 43.8: **PROVED-in-paper** (proof :142–144). Auditor re-check: rank 24. Consistent.
- Thm 43.9: **PROVED-in-paper** (proof :159–161; spectrum cited from Addendum S/T). Auditor exact re-check: the H01 spectrum {0:12 (exactly the odd-q characters), 76+16s:1, 4:1, −4:1, 2:2, −2:2, 10−8s:2, 14−8s:2, 20−8s:1} reproduces exactly; rank H01 = 12, rank M = 36.
- Thm 43.10: **PROVED-in-paper** (proof :204–206). Auditor exact re-check: all 14 H′ eigenvalues and multiplicities and all 9 H01′ values reproduce exactly; rank M′ = 48. The paper scopes capacity as OPEN (:202, :207).
- Prop 43.13: PROVED-in-paper as a linear-algebra warning (counterexample I₃₅ ⊕ N ⊕ 0₁₁, dim 48, rank 36; consistent).
- Prop 43.14: PROVED/recorded (proof cites Addenda J/W/X). Spot checks consistent: disc Q(√35) = 140; (140/3) = −1, so 3 is inert; 4 generates 1+3Z₃; |C₃^×| = 3^Q. Its modular→Iwasawa clause is UNDEFINED/CONDITIONAL as written.
- Rem 43.12 capacity: **OPEN** (catB :229). Rems 43.15/43.16: OPEN / CONDITIONAL as written.
- Prop E.1: exclusion record (Clifford/quantum readings are not in the proved core). It refutes nothing (:14).
- Prop E.2: **OPEN/UNDEFINED** (catB :24).
- Ledger Rems 42.1–42.4: "as reported" provenance only. They are not new Foundation Bound theorems (ledger :30, :33).
- Defs: definitions. Def 43.1's claims check out: 8 π-fixed points = {k odd, ℓ ∈ {0,3}}; 20 pairs; 28 orbits; π(c) = c⁻¹y⁻². Def 43.2 checks: [K:Q] = 8, since √35 ∉ Q(i,√3). The 48-entry table (:93–110) agrees with the orbit rule (:52–60) and the orbit list (:74–87), and all weights are π-invariant.
Precise internal inconsistencies in v17 new material: **none found**. Minor presentation gap: the character indices p (in (−1)^p, :170) and q ("odd q", :153) are not defined in §43. Not an error.
**Inconsistency found in FROZEN v16 (cross-reference, not mathematics):** because the label `lem:parity` was duplicated, the v16 PDF prints "Lemma 39.18" (the unimodular-cone lemma Cor_{−C} = Cor_C, v16 p.124) where the Parity-splitting Lemma 24.3 is meant. This happens at v16 p.55 (s07_lz.tex:98), p.81 (s16_cthird.tex:70, proof (iii)), p.82 (s17_sfamily.tex:32) and p.103 (s23_deps.tex:10, dependency table). v17 prints "Lemma 24.3" correctly at these sites. v16 is frozen and is NOT edited. Recorded as erratum E16-1 for the Owner.

## (e) Bridge relevance (file:line)
- Residual ≠ Resonant: partIII_local_adv_v16.tex:164–189 (Prop `prop:Seff` (iv) :173–175; Prop `prop:res-vs-res` :183–189, catA). Present in both papers (identical file). front_v16.tex:7 and front_v17.tex:16 say "RTA, also called Resonant Algebra" (naming only).
- D1: partIII_local_adv_v16.tex:143–162 (Thm `thm:D1`: rank-1 over Q on H²(F); H¹ = 0; formality); glossary_v16/17.tex:71–72.
- S_eff: partIII_local_adv_v16.tex:165–181; glossary :73.
- Layer2: partIII_local_adv_v16.tex:155, :162 ("Layer 2 … not constructed from D1 in this paper"). This is the only occurrence.
- Λ₀: partIII_local_adv_v16.tex:61–80 (`prop:Lambda0-none`: no normalisation; Res ζ_K ≈ 0.837679 as Hecke-scale fallback only); glossary :68; partIII_partial_v16.tex:50.
- S²-11DM²ET-X: partII/s01_intro.tex:8 (both trees). This is the only occurrence, naming the programme Bridge Series C comes from. **No "junction" text in either paper.**
- v17 §43 / §42 / App E add no Residual/Resonant, D1, S_eff, Layer2 or Λ₀ claims. §43 states it "does not identify Ξ, and does not close capacity" (boundary :6).

## (f) Blockers and next batch
Blockers:
- B1: custody discrepancy C17-1 (sidecar ee88… ≠ PDF 9b40…) is UNDETERMINED. To resolve it, the writer of the sidecar or a pre-fix PDF copy must surface. A new dated sidecar alongside (never overwriting) needs an Owner decision.
- B2: provenance source `/tmp/q.py` cited at boundary_rank_v17.tex:9 and :70 is **absent** on the box. The orbit table can be checked only for internal consistency (done), not against its source.
- B3: erratum E16-1 in frozen v16. Fixing it requires a v17+ decision, never a v16 edit.
- B4: no junction / S²-11DM²ET-X bridge statement exists in either paper. The bridge audit must go to the lane records.
Next batch 02 (10 artifacts; order lock → proof → ships → packaging):
1. lock: P16/EDITORIAL_CANDIDATE_COUNT_CLARIFICATION_2026-11-05.md
2. lock: /workspace/quantum-comp/reports/AUDITOR_V16_DRAFT_QA/AUDITOR_ADVANCEMENTS_SINCE_RTA_V16_DRAFT_2026-11-05_INTERNAL_TEXT.txt
3. lock: reports/bridges/AUDITOR/FINDINGS_AUDITOR_DIGEST_SINCE_RTA_V16_2026-11-05.md
4. proof: reports/FINDINGS_PP_OWNER_PDF_1715_MATH_REVIEW_ADDENDUM_Q_1919_2026-11-05.md
5. proof: …ADDENDUM_R_1926…
6. proof: …ADDENDUM_S_1932…
7. proof: …ADDENDUM_T_1938…
8. proof: …ADDENDUM_V_1949…
9. proof: …ADDENDUM_W_1958…
10. proof: …ADDENDUM_X_2002…
Then ships (Local/NL/Eigen/PR2 lane records cited in ledger Rems 42.1–42.4), then packaging (src tgz/zip, qa_pages).
