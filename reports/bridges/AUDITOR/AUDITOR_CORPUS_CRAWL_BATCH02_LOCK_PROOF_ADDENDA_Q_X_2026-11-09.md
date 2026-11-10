# AUDITOR — Full-corpus crawl, Batch 02: lock companions + PP Addenda Q, R, S, T, V, W, X
Written 2026-11-09 ~12:55 CST (America/Chicago) by Auditor. Owner authority: "All haults lifted", 2026-11-09 12:34 CST (pt1864u).
Limits kept: new dated file only (exclusive create). No frozen or hashed record and no sidecar was modified. No new v17 sidecar was written (that decision waits on the Owner). Tip `7cddb188…` untouched. No CERT, no Gemini, no external sends. No verdict was changed: the labels below report each document's own verdicts. The Auditor re-check columns are internal-consistency checks only, not CERTs.
R = /workspace/quantum-comp/reports/. "Stated date" comes from the filename or header. Every mtime is 2026-11-06 14:36–14:45 CST, from the same bulk copy noted in batch 01, so mtimes never carry the Nov 5 authoring time.

## 1. Custody table
| # | Artifact | sha256 | Sidecar | mtime (CST) vs stated |
|---|---|---|---|---|
| 1 | R/papers/RTA_FOUNDATION_BOUND/EDITORIAL_CANDIDATE_COUNT_CLARIFICATION_2026-11-05.md | a580714f3aa71afba1984fcd6451f2e48f633fe7efc70550e1b211ef9d472f6c | NONE | 11-06 14:40:42 vs "2026-11-05 CST" (:2) |
| 2 | R/AUDITOR_V16_DRAFT_QA/AUDITOR_ADVANCEMENTS_SINCE_RTA_V16_DRAFT_2026-11-05_INTERNAL_TEXT.txt | 571bf5c48b1eaedaf686eb924e6c2b1f1186f1c839074965069653d5240cef4f | NONE | 11-06 14:40:45 vs "Nov 5 ~16:38 CST" (:4) |
| 3 | R/bridges/AUDITOR/FINDINGS_AUDITOR_DIGEST_SINCE_RTA_V16_2026-11-05.md | d485dcc226402243f2bcb4c55e76fde260a0c7e46cb1220ecaffc4c1d49d17a7 | **MATCH** | 11-06 14:40:36 vs "11-05 ~12:50 CST" (:3) |
| 4 | R/FINDINGS_PP_OWNER_PDF_1715_MATH_REVIEW_ADDENDUM_Q_1919_2026-11-05.md | bbd8ddbc4c7f8d7d21c59ec110efceb1f4bfbb380d8fd5775257bbc782537bad | NONE | 11-06 14:40:44 vs 11-05 19:19 (filename) |
| 5 | …ADDENDUM_R_1926_2026-11-05.md | 5526834f87667506740797568332bdee081fa9919fc8ec6120127c882e9f470c | NONE | 11-06 14:40:44 vs 19:26 |
| 6 | …ADDENDUM_S_1932_2026-11-05.md | 0c47e6665e52440c331afe851aed237e89e0b72b3d3d7f9a7bdf3d8fe70710c6 | NONE | 11-06 14:40:44 vs 19:32 |
| 7 | …ADDENDUM_T_1938_2026-11-05.md | a57bd2df43fe5db98a61ae9bc8981b7d316bf20161f311d641ddca6489f5dbc0 | NONE | 11-06 14:40:44 vs 19:38 |
| 8 | …ADDENDUM_V_1949_2026-11-05.md | b77dc5711eef76499675bf357f827f34f3c354dab21daa8bfe5064c5cd1ab338 | NONE | 11-06 14:40:44 vs 19:49 |
| 9 | …ADDENDUM_W_1958_2026-11-05.md | e81d46d0cc431b35e6d69076a0f7b46ae3888c3ff898cd420d01b94e02222f6a | NONE | 11-06 14:40:44 vs 19:58 |
| 10 | …ADDENDUM_X_2002_2026-11-05.md | dec61d518f88e587ecf34ddb16e90b79c2f29a9e74b4484b3b414cc086c46bd0 | NONE | 11-06 14:40:44 vs 20:02 |
Stated chronology: Q 19:19 < R 19:26 < S 19:32 < T 19:38 < V 19:49 < W 19:58 < X 20:02, all before the v17 work began (NOTES_v17 ~20:37; BASELINE check 20:38:33). This is consistent with v17 §43 citing them.

## 2. Claims and labels (each document's own verdicts; Auditor re-check noted)
### #1 Editorial clarification (nonnormative; it states it is not a theorem, :2)
- The 45/46/47 candidate tallies (:4) are editorial counts, so no math label applies. Sources cited at :6 were re-hashed and **MATCH**: PP 4e1cf035… and ABSORB 0a4ddb32…. The chain at :8 was re-hashed and MATCHES: OW 546a61df…, paper findings a7bf622f…, trace 2152f01e….
- ":10 all 100 TeX source files": the count matches (100 .tex files under v16 src). ":10 PDF sha 1fe7b8a2…" matches batch 01.
- ":12 See scope-inventory.json": **NOT FOUND** anywhere under /workspace/quantum-comp (blocker B2-3).
### #2 Advancements internal text (DRAFT, as reported, :2, :8)
- It is a compilation and grants no new PROVED status. Its as-reported tallies are:
  - PROVED: Local/PP = 2 (:70, :110), Gal(Q(ζ49)/Q) cyclic of order 42 (:73), PR2 finite-check trio (:95).
  - REFUTED-by-proof (counterexample): uniform 539 hitting via n₀ = 3^540 − 2 (:72), plus Cand-1 on N₀, literal HQCC, and the all-Z attractor (:112).
  - CONDITIONAL: 24-prime insufficiency (:74).
  - OPEN: 25-prime sufficiency, Cand-1⁺, Appell, QI, Ξ, the junction, S_eff as a formula, and the S² bridge (:81, :114).
### #3 Since-v16 digest (hash and facts only, :5)
- Facts only, no math claims. Its v16 PDF and NOTES MATCH lines (:13) agree with batch 01. The 16 CONFIRM rows (:30–45) were not re-hashed in this batch; they are deferred to the ships batch.
### #4 Addendum Q
- Owner "full rank proof" → **REFUTED-by-proof** (:3–11). B = [I 0; Θ_B 0] has rank 24, and the Gram determinant is 0.
- Repairs (i) and (ii) → CONDITIONAL on the selector or T choice (:13–15).
- Coefficient proposal: positivity, twisted closure, and the λ_pqr formula → **REFUTED-by-proof** (:20–29).
- Physical α, Ω, Λ and the N/W/capacity link → OPEN (:37).
- Auditor check: the witness at :23 (x⁻¹y⁻² = xy²) and the identity i²ω³ = 1 at :28 are correct.
### #5 Addendum R and R.1
- Orbit table and twisted symmetry → PROVED by exact enumeration (:3–8).
- "Dense mixing", "independence ⇒ rank 48", and "N ≤ spr|T|" → **REFUTED-by-proof** (:18–24, :32, :41).
- |W| ≤ N → PROVED by the triangle inequality (:28).
- The signed spr bound → PROVED for a single coefficient only; any other W is OPEN (:33–36, :74).
- NP-completeness → UNSUPPORTED/OPEN (:38).
- R.1: the exact 13-value spectrum of H and its invertibility → **PROVED** (:48–69).
- Auditor exact re-computation agrees: all 13 values and multiplicities, degree 127+39√35, min |λ| = |3−√35| ≈ 2.916, and the operator is symmetric because the weights are π-invariant.
- R.1 errata (:71–74) qualify R :8 (positivity: 47 active weights, O2 = 0) and R :29. This is self-correction within the file, not a conflict.
### #6 Addendum S
- Block reduction rank M = 24 + rank H01 → PROVED (:8–11).
- H01 spectrum, rank 36, nullity 12 → **PROVED** (:13–31). Auditor re-check agrees.
- Owner "rank M = 24" and "48" → **REFUTED-by-proof** (:31).
- "row(AD) = row(A)" → REFUTED-by-proof (:34).
- Path Thm 3 bounds → PROVED under the hypothesis of a field embedded in ℝ or ℂ (:37–42).
- Capacity → OPEN (:46).
### #7 Addendum T
- Rank 36 for the exact table → PROVED (:5).
- "Immutable for all positive weights" → **REFUTED-by-proof** by the counterexample a_{xy³} → 7−√35, which gives rank M′ = 48 (:6–19). The checks hold: π(xy³) = xy³ and 7−√35 > 0.
- Capacity → OPEN (:24).
### #8 Addendum V
- The tuned H′ spectrum (14 values, Σ = 48) and det H′ ≠ 0 → **PROVED** (:7–26).
- The t4129 list → **REFUTED-by-proof** (:28–32).
- H01′ spectrum, rank 48 → PROVED (:34–40).
- The claim "all even-q values have a nonzero √35 coefficient" → REFUTED-by-proof (:38).
- Auditor exact re-check agrees: all 14 H′ values and all 9 H01′ values.
- Note: the source script /tmp/v.py (:1) is ABSENT on the box, as is /tmp/q.py.
### #9 Addendum W (and W.1)
- VALID → PROVED: item 6 for group-ring elements, 13 (3 is inert), 18 (|F₃^×| = 3^Z discrete), 20 (4 generates 1+3Z₃).
- FALSE → **REFUTED-by-proof**: items 2, 3, 4, 7, 9 ("unary weight 3/2"), 10 (normalisation; corrected by W.1 :85–88 to ξ_{1/2}C = +iψ), 15, 18 (C₃ discrete), 19, 22.
- ND → OPEN/undefined: items 1, 5 (over F), 8, 11, 14, 16, 21, 23.
- UNS → OPEN: items 12, 17, 24.
- Status line: original rank 36 and tuned rank 48 PROVED; capacity OPEN (:78–79).
- Auditor checks agree on items 3 (−48κ on the trivial character), 9 (12/2+1 = 7 under the stated hypotheses, :89), 10/W.1 (+iψ), 15, 19, and 22.
### #10 Addendum X
- Naming H′ = H + R_x; capacity → OPEN (:3–6).
- "rank 36 ⇒ PBP* invertible" → **REFUTED-by-proof** (:8–10). The U*BV fix → PROVED (:11–12).
- Field equality → **REFUTED-by-proof**, degree 8 ≠ 16 (:14–17).
- "v3 det B_red = 0 ⇒ isometry" → REFUTED-by-proof. The GLₙ(O_F3) condition → PROVED (:21–25).
- "Complex P defines an F3-lattice" → ND/OPEN.
- Items 6 and 7 → VALID (:27–29).
No precise internal inconsistency was found in Q–X once the in-file errata (R.1, W.1) are applied.

## 3. Conflicts with batch-01 facts or report source 1cb3d342
- **C2-1 (count wording):** the "Theorem count" heading at NOTES_v16.md:8 propagates into several records:
  - Digest #3 :15 and :77 ("Theorem count … 82 = 71 (v15) + 11").
  - Report source 1cb3d342… (AUDITOR_PQC_ADVANCEMENT_REPORT_OWNER_1629_V16BASELINE_FOUNDATIONAL_PHRASE_2026-11-05.md) :16 ("theorem count total_now = 82") and :18 ("82-theorem label").
  - Batch 01 established that 82 counts mixed numbered statements, while v16 has **71 printed Theorems** (60 + 11 Part I). That v16 "71" is a different object from the "71" summand in the NOTES. The digest's "71 (v15)" reading is unverified, and the v15 count was not recomputed.
  - #2 :44 words this correctly ("82 numbered statements, NOT 82 … proofs").
  - Fix by an additive erratum only; 1cb3d342 is not edited.
- **C2-2 (mtimes):** #2 :40 records the v16 PDF mtime as 11:36:46 and the NOTES mtime as 11:36:53. The disk now shows 11-06 14:40 for both, because the copy reset the mtimes; the hashes still MATCH. The 1cb3d342 report source also cited ~11:36:46/53. These were historical observations and are no longer reproducible.
- **C2-3 (v17 ABSENT):** #3 :14, :78 and #2 :55 say v17 is ABSENT. That was true as of ~12:50 and ~16:38 on Nov 5; v17 appeared at ~20:37. These statements are superseded, not wrong.
- **C2-4 (D1 naming collision):** "Eigen D1–D3" (#2 :74, :81, :94, :121; 1cb3d342 :40, :52) are Eigen-lane items. They are not the paper's Thm D1 rank-1 classifier (v16 partIII_local_adv_v16.tex:143). Do not conflate them.
- **C2-5:** "quoted, not re-hashed" (#2 :38, :14) is now superseded: batch 01 re-hashed the v16 PDF, NOTES and tip, and all MATCH.
- No conflict was found with v17 §43. Its Thm 43.8–43.10, Prop 43.13 and Prop 43.14 match Addenda Q, S, T, V, W and X exactly, including the p ∤ 140 filter with cutoff and the [K:Q] = 8 field degree.

## 4. Bridge touchpoints
- Residual ≠ Resonant: #2 :67 (already in v16), #2 :95 (P1 "weak Residual≠Resonant" as citation closure). The digest has none, and Addenda Q–X have none.
- D1 (paper): #2 :46, :67, :86 ("D₁ Layer2 transfer beyond paper D1" is a missing definition); 1cb3d342 :20, :44.
- S_eff: #2 :46, :67, :81, :86, :95 ("539 = S_eff" OPEN), :114, :122–124.
- Layer2: #3 :25, :82, :94 (ABSENT; "not from D1" is a paper claim only); #2 :46, :81, :123.
- Junction / S²-11DM²ET-X: #2 :81, :86 ("remains OPEN as a proved local–nonlocal junction"), :114, :119–120, :124, :128 (junction specialist request, UNASSIGNED); #3 :22, :65, :79 (OW AMEND S2 2c341bc7…). The editorial chain OW 546a61df… is the S²-11DM²ET-X interpretation-paper Owner Write.
- Addenda Q–X: no bridge touchpoints. W :48 ("kernel 12 ⇒ shadow/capacity closed" is UNS) and W :8–11 (mock-modular items ND) are the nearest.

## 5. Blockers
- B2-1: 9 of 10 batch artifacts, including all seven Addenda Q–X, have **no sidecar**. Their custody rests only on this file's hashes. Writing new sidecars is an Owner decision and was not done.
- B2-2: the computation sources /tmp/q.py and /tmp/v.py are absent. The Addenda spectra were re-derived independently by Auditor and match.
- B2-3: scope-inventory.json, cited at #1 :12, was not found.
- B2-4: the count-wording conflict C2-1 needs an additive erratum file if the Owner wants it.
- B2-5: carried from batch 01: C17-1 (v17 sidecar) and E16-1 (v16 cross-reference erratum).

## 6. Batch 03 (ships: lane records behind v17 ledger Rems 42.1–42.4)
1. R/FINDINGS_PP_OWNER_PDF_1715_MATH_REVIEW_2026-11-05.md (the base review for Addenda A–X)
2. R/bridges/LOCAL/FINDINGS_LOCAL_SOFTSF_AMEND_PROOF_LOGIC_PASS_FLAG16_PURGE_LOCK_NOT_PROOF_2026-11-05.md (FLAG #16 AMEND, 5f0d666d)
3. R/bridges/PHYSICIST/SOFTSF_PRESS_FINDINGS_LOCAL_SOFTSF_AMEND_PROOF_LOGIC_PASS_FLAG16_PURGE_LOCK_NOT_PROOF_2026-11-05.md (PRESS b62625c3)
4. R/FINDINGS_LOCAL_SOFTSF_PROOF_LOGIC_PASS_BRIDGEC_12INTAKES_2026-11-05.md (PP CONFIRM Bridge C, 2a5edc87)
5. R/ADDENDUM_EIGEN_PACK_I_REGRADE_2026-11-05.md (d67e9cd1)
6. R/FINDINGS_NL_FORMAL_RESOLUTIONS_GAP_REVIEW_2026-11-05.md (NL formal status)
7. PR2 T3 review c531eacc (path to be located by content hash)
8. PR2 V6 FALSE addendum 17ae811b (path to be located)
9. PR2 citation closure 398a39f1 (path to be located)
10. R/OWNER_WRITE_CALL_53991ebf_AGENT_PHYSICS_PAPER_S2_11DM2ETX_INTERPRETATION_2026-11-05.md (546a61df, the S²-11DM²ET-X citation target)
