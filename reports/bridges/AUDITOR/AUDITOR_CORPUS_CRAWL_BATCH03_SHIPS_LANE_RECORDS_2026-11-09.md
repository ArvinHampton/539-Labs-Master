# AUDITOR — Full-corpus crawl, Batch 03: ships (the lane records behind v17 ledger Rems 42.1–42.4)
Written: 2026-11-09 ~13:00 CST (America/Chicago), by Auditor.
Owner authority: "All haults lifted", 2026-11-09 12:34 CST (pt1864u).

Limits kept:
- This is a new dated file only (exclusive create).
- Nothing existing was modified. No sidecars were created.
- Tip `7cddb188…` untouched.
- No CERT, no Gemini, no external sends.
- No verdict was changed. Labels are each document's own verdicts. "Auditor re-check" means an internal-consistency or finite arithmetic check only.

Path prefixes:
- Q = /workspace/quantum-comp/
- R = Q/reports/

Every mtime is 2026-11-06 14:36–14:45 CST, from the bulk copy recorded in batch 01. Stated dates come from file headers.

## 1. Custody table
| # | Artifact (canonical path) | sha256 | Sidecar | mtime (CST) vs stated |
|---|---|---|---|---|
| 1 | R/FINDINGS_PP_OWNER_PDF_1715_MATH_REVIEW_2026-11-05.md | 17ab357b2e88c99296a18f4750ce8360a780bda152d24653831ba98e776f5bc2 | NONE | 11-06 14:40:44 vs Owner PDF 17:15, 11-05 (:1) |
| 2 | R/bridges/LOCAL/FINDINGS_LOCAL_SOFTSF_AMEND_PROOF_LOGIC_PASS_FLAG16_PURGE_LOCK_NOT_PROOF_2026-11-05.md | 5f0d666d927177672a7040316f4537834e5b15e9bb45bc9e899b53df47a62a9f | MATCH | 11-06 14:40:45 vs 11-05 (no time; PRESS says ~16:29) |
| 3 | R/bridges/PHYSICIST/SOFTSF_PRESS_FINDINGS_LOCAL_SOFTSF_AMEND_PROOF_LOGIC_PASS_FLAG16_PURGE_LOCK_NOT_PROOF_2026-11-05.md | b62625c33df84a95a9b752d0cff80a5d7a7ba2d472cde2f2de368051f7293169 | MATCH | 11-06 14:40:45 vs ~16:29 (:2) |
| 4 | R/FINDINGS_LOCAL_SOFTSF_PROOF_LOGIC_PASS_BRIDGEC_12INTAKES_2026-11-05.md | 2a5edc870a7a149c266f5b5792be3db1b00d656b44173030831b5017664de02d | MATCH | 11-06 14:40:43 vs after ~15:58 (:4) |
| 5 | R/ADDENDUM_EIGEN_PACK_I_REGRADE_2026-11-05.md | d67e9cd1ffc38274d1f114b69a3f319a6c4a631542a472727389a1dc617ed0e7 | MATCH | 11-06 14:40:44 vs 11-05; correction 16:30 (:14) |
| 6 | R/FINDINGS_NL_FORMAL_RESOLUTIONS_GAP_REVIEW_2026-11-05.md | 96f810645c6356c30b5edd2990da3f16657f866f56af22ff8cdbfe8a1007b0a6 | MATCH | 11-06 14:40:40 vs 14:23 (:4) |
| 7 | Q/bridges/AUDITOR/FINDINGS_PR2_AGENT_T3_4880_539_PROOF_REVIEW_2026-11-05.md | c531eacc62198b9839a27608588d2a83fb5b0b4a18736c8a4a5b2c16c7d60242 | MATCH | 11-06 14:40:44 vs ~16:27 (:1) |
| 8 | Q/bridges/AUDITOR/ADDENDUM_PR2_T3_V6_REGRADE_FALSE_2026-11-05.md | 17ae811b9ac169537e80de6995ab93a862ccf4503c49a2c5fea18a34ba888d63 | MATCH | 11-06 14:40:44 vs ~16:30 (:1) |
| 9 | Q/bridges/AUDITOR/FINDINGS_PR2_AGENT_GAP_SOURCES_PROOF_GRADE_2026-11-05.md | 398a39f12fd6b0aecfb29eb1e0a71500dffc68d73f58320788feee931d21ffbe | MATCH | 11-06 14:40:44 vs ~16:30 (:1) |
| 10 | R/OWNER_WRITE_CALL_53991ebf_AGENT_PHYSICS_PAPER_S2_11DM2ETX_INTERPRETATION_2026-11-05.md | 546a61dfe0cfe92b780f1d0fecf40a6a97eb8ca9e01df7688e4724bc767dc318 | MATCH | 11-06 14:40:36 vs ~13:01 (:2) |

Mirrors (identical sha, located by content hash):
- #2 and #3 also sit under Q/bridges/{AUDITOR,PHYSICIST,PROFESSOR_PROOF,LOCAL} and R/bridges/{AUDITOR,PROFESSOR_PROOF,LOCAL}, plus R/ for #3.
- #5 also under Q/bridges/{PHYSICIST,PROFESSOR_PROOF} and R/bridges/{PHYSICIST,PROFESSOR_PROOF}.
- #7–#9 exist ONLY under Q/bridges/{AUDITOR,PHYSICIST,PROFESSOR_PROOF}, not under R/. Their sidecars live in that tree, which is why the batch-02 sidecar search of R/ missed them.
- #10 is mirrored 6× under Q/bridges/.

Sidecars: 9 of 10 MATCH. #1 has none.

## 2. Claims and labels (document verdicts; Auditor checks noted)
### #1 PP math review of the Owner 17:15 PDF
- §3: "det K_140 ≠ 0" → **REFUTED-by-proof** (:5; row 7 is identically 0 under the document's own rule).
- §3: K defined as the Kronecker symbol → **REFUTED-by-proof as inconsistent** (:6). Auditor check: (35/9) = +1. Correct.
- §3: D1, D2, D3 and 25-prime sufficiency → **OPEN** (:7).
- §3: Gal(Q(ζ49)/Q) cyclic of order 42; conductor of Q(√35) = 140 → **PROVED** (definition) (:9). Auditor check: correct.
- §1: Israel condition with [K_ij] − γ_ij[K] = 0 "matching 4D stress" → **REFUTED-by-proof as inconsistent** (:12; it forces S_ij = 0).
- §1: Σ codimension → GAP/OPEN (:13). 𝒥_finite, R_x, a(t) → OPEN (:14).
- §2: S_eff := 539 → **DEFINITION** (stipulation) (:17). Λ₀/κ are Tier E (:18). Auditor check: √(2/0.7858) = 1.595361. Correct.
- §2: P[Φ] and confinement N − |W| = 0 → **OPEN** (:19).
- The script does not parse, so it is not evidence (:8).
- Wording nit, verdict unchanged: :18 calls a_μ = 11659181×10⁻¹⁰ the "measured value". That figure coincides with the 2020 Theory-Initiative **SM prediction** (116 591 810 × 10⁻¹¹), not the experimental average. The Tier-E / non-arithmetic classification stands either way. External fact, from Auditor's general knowledge; not re-sourced on the box.
- §3 K_140 rows not re-derived: the source txt/script is not in this batch.
### #2 Local AMEND FLAG #16
- Purge fence → reclassified from PROVED to **lock status (Decision 4), not math PROVED** (:11, :19, :24).
- Rollup (:30–34):
  - **PROVED 2**: #1 Haar70 fenced; #2 BT↛ℍⁿ.
  - **REFUTED 2**: Cand-1 on ℕ₀; QI ⇒ unique R_c.
  - **DEFECT 1**: literal T₃/HQCC.
  - **PARTIAL 4**
  - **ABSENT/OPEN 10**
- Supersedes the #4 rollup at :77 ("PROVED 3"). Consistent with v17 Rem 42.1 and advancements :70.
### #3 PRESS for #2
- Restates #2 (:11–18). Its FINDINGS path at :6 (R/FINDINGS_LOCAL_SOFTSF_AMEND…) exists with the same sha (5f0d666d). No new claims.
### #4 Local Bridge C proof-logic pass (20 claims, :54–74)
- **PROVED**: #1 Haar70 identity, #2 BT↛ℍⁿ.
- **REFUTED-by-proof**: #4 Cand-1 on ℕ₀ (n = 0), #11 QI ⇒ unique R_c.
- **DEFECT** (literal map false): #3.
- **PARTIAL/OPEN**: #5, #6, #8, #10.
- **ABSENT/OPEN**: #7, #9, #12–#15, #17, #20.
- #18: Residual≠Resonant fence kept. #19: out-of-scope.
- #16 "PROVED as locked" (:70, :77) is **superseded by #2** and is lock status only.
- Auditor checks:
  - T(0) = 0. Correct.
  - Haar formula: (1−3⁻⁴)/(1−3^{−(ν+3)}) is consistent with the shell measure (1−3⁻⁴)·3^{−4k} (also #9 :9).
### #5 Eigen Pack I regrade
- Gal cyclic of order 42 → **PROVED** (:5).
- Mod-140 ⇒ D1 descent → **GAP/OPEN** (:7). D3 → **OPEN** (:8). D2 → **OPEN/ABSENT** (:9). "D1/D3 UNLOCKED" → **OPEN** (:10).
- 25-prime sufficiency: **REFUTED (:6, :12) is retracted to OPEN by the 16:30 correction (:14–15).**
- 24-prime insufficiency → **CONDITIONAL** on H1 (the RREF has entries in ℚ, i.e. D1) and H2 (no bad primes) (:17–19).
- The :12 "Net" line is stale relative to :15. This is an in-file correction, not an inconsistency.
- Consistent with v17 Rem 42.3.
### #6 NL formal resolutions gap review (Owner Docs A and B)
- Doc A seed-2 orbit term "367" → **REFUTED-by-proof** (arithmetic: 3·122 − 1 = 365) (:21).
- T3_ref(4880) 14 steps and T^539 = 2 → **PROVED** (finite check) (:22).
- Doc B "guarantees bounded convergence" → **OPEN** (conjectural; empirical only) (:23).
- Haar preservation / ternary conjugacy → unsupported/**OPEN** (:23).
- √(2/0.7858) arithmetic → PROVED. Provenance → **OPEN** (:24).
- R_c re-grounding → no evidence/**OPEN** (:25).
- Literal isometry → withdrawn (false; NL B2 obstruction) (:30).
- QI embedding → **OPEN** (no F, λ, ε) (:31).
- Junction → **OPEN/missing** (:32, :49).
- 539 = fixed budget → consistent (definition) (:35). Q1, Q2, Q3, Q7, Q9, Q10 → OPEN (:68).
- Auditor re-checks:
  - 365 confirmed: (3^{n+1}+1)/2 = 365 at n = 5.
  - 1.595361 confirmed; differences 3.9×10⁻⁵ and 6.9×10⁻⁵ confirmed.
  - Sweep 1 ≤ n < 200000: all reach {1,2}, maximum 81 steps (≤ 400 as claimed). This is evidence only and leaves the claim OPEN.
  - :24 cites "RTA v16 Prop 41.5" for 0.7858. The v16 PDF does print Prop 41.5 (Scale-free Local cite-lifts) listing 0.7858 as a candidate that does NOT enter. Correct citation.
### #7 PR2 T3 review
- V1 well-defined map, V2 4880 → 1 in 14 steps, V3 T^539(4880) = 2 → **PROVED** (:8–10).
- V4 literal map/HQCC → **REFUTED-by-proof** (:11; orbit 1, 4, 13, 40, …).
- V5 on ℤ → **REFUTED-by-proof** (:12; T(0) = 0, T(−1) = −1).
- V5′ positive-integer termination → **OPEN** (:13).
- V6 → OPEN at :14, **superseded by #8**.
- V7 539 = S_eff → **OPEN**, consistent (:15). V8 → consistent (:16).
- Auditor re-check: 14-step orbit, T^539(4880) = 2, T(0) = 0 and T(−1) = −1 all reproduce.
### #8 PR2 V6 regrade
- Uniform 539-step bound → **REFUTED-by-proof** (:2–4). Witness n₀ = 3^540 − 2, with T^j(n₀) + 2 = 4^j·3^{540−j}.
- Auditor exact check: every iterate stays > 2 for 540 steps, and T^540(n₀) = 4^540 − 2. Reproduced.
- Revised tally: PROVED 3 / FALSE 3 / OPEN 2 / consistent 1 (:6). Matches v17 Rem 42.4.
### #9 PR2 GAP-sources grade
- **PROVED**: P5 finite orbit, P4 539 = S_eff ≠ stopping time (definitional), P3 Haar70 (with dominated-convergence AMEND), P1 Residual≠Resonant in the weak, no-supplied-map sense.
- **DEFINITIONAL**: P2 (D1/S_eff locks).
- FAIL 0 (:13).
- Paper display defect: (2n+1)/3 is non-integral on residue 2 (:6). Auditor check: T(2) = 5/3 under exact division. Correct.
- :10 cites RTA Prop 41.11–41.12. The v16 PDF prints Prop 41.11 (Static cell budget S_eff) and Prop 41.12 (Residual is not Resonant). **Citation correct.** Section 41 is unchanged in v17.
- Note: the v16 Prop 41.11 text refers to "Proposition 42.6" (T3); that becomes 44.6 in v17 because of the §42 → §44 renumber.
### #10 Owner Write: S²-11DM²ET-X interpretation paper (directive, not a math claim)
- It sets the task and hygiene rules (:6–26).
- Its "math ground" list (:15–21) is an Owner citation list. It carries no proof status of its own.

## 3. Conflicts with batch 01, batch 02, or report source 1cb3d342
- **C3-1 (extends C2-1):** #10 :15 says "RTA Foundation Bound v16: **82 theorems**".
  - Batch 01 found 82 mixed numbered statements (NOTES_v16:8) and 71 printed Theorems.
  - This is an Owner Write, so it was not edited and is not covered by the C2-1 erratum (which corrects only 1cb3d342).
  - It is flagged for the Owner. It is the likely origin of the "82-theorem label" wording copied into 1cb3d342 :18.
- **C3-2:** #10 :16 says "45 provable candidates". The editorial clarification (batch 02 #1 :4) says 45 is a primary-tag tally of PROVABLE-CANDIDATE, and "a proof candidate is not a completed proof". Wording conflict only; flagged, not edited.
- **C3-3 (wording risk):** #10 :21 calls "residual ternary algebra and resonant algebra" "Soft SF-proven anchors". This sits next to the Residual≠Resonant fence (#4 #18; #9 P1; v16 Prop 41.12). front_v16.tex:7 does say RTA is "also called Resonant Algebra", so it is naming, not a precise inconsistency. Any paper prose should keep Residual ≠ Resonant explicit.
- **C3-4:** the g−2 label nit in #1 :18 (above).
- **C3-5 (supersessions, not conflicts):** #4 :77 "PROVED 3" → #2 "PROVED 2"; #7 V6 OPEN → #8 FALSE; #5 :6/:12 REFUTED → :15 OPEN. The v17 ledger Rems 42.1–42.4 and the advancements text already use the superseding values.
- No conflict found with the batch-02 Addenda or v17 §43.

## 4. Bridge touchpoints
- **Residual ≠ Resonant:**
  - #2 :5, :40; #3 :4; #4 :6, :72 (#18 fence; any bridge ABSENT), :96
  - #6 :35; #9 :10 (P1 PROVED, weak form, cites v16 Prop 41.12); #10 :21 (C3-3)
- **D1 (paper classifier):**
  - #9 :11 and #10 :20 (D₁/S_eff lock OW 96f8d42e).
  - "D1–D3" in #1 :4–7, :25 and #5 :1, :7–12 are **Eigen-lane** items, not the paper's Thm 41.10 D1 (see C2-4).
- **S_eff:**
  - #1 :16–17 (S_eff := 539 is a stipulation).
  - #6 :35 (S_eff = 539 identification not adopted).
  - #7 V7 :15 (OPEN); #9 P4 :8 (PROVED definitional); #10 :20.
- **Layer2:** none in batch 03.
- **Junction / S²-11DM²ET-X:**
  - #1 §1 :11–14 (Israel condition inconsistent; codimension GAP).
  - #4 #14 :68 (Israel ABSENT for Local).
  - #6 :32, :48–49 (junction still missing; NL-Q3 OPEN).
  - #10 :1, :7 (S²-11DM²ET-X GR-extension paper directive).
- **Λ₀:** #1 :18, :25; #4 #8, #17 :62, :71; #6 :24.

## 5. Blockers
- B3-1: #1 has no sidecar. Sidecar creation is pending the Owner.
- B3-2: #7–#9 exist only in the Q/bridges/ tree, with no R/ canonical copy. The Owner should decide which tree is canonical.
- B3-3: the #1 §3 source (Owner PDF txt/script, L54–73 and L200–259) was not in scope, so the det K_140 row was not re-derived.
- B3-4: C3-1 and C3-2 are in an Owner Write. They can only be corrected by an Owner decision; the Auditor will not edit Owner Writes.
- B3-5: carried forward: C17-1 (v17 sidecar), E16-1 (v16 cross-ref), B2-1 (missing sidecars), B2-2 (/tmp/q.py and /tmp/v.py absent), B2-3 (scope-inventory.json missing).

## 6. Batch 04 (packaging), in crawl order
P16 = R/papers/RTA_FOUNDATION_BOUND/
P17 = R/papers/RTA_FOUNDATION_BOUND_v17_DRAFT_2026-11-05_2037CST/
1. P16/RTA_FOUNDATION_BOUND_src.zip
2. P17/RTA_FOUNDATION_BOUND_v17_DRAFT_src_minimal.tgz
3. P17/qa_pages/ (9 PNG)
4. P17/qa_pages_fix/ (6 PNG + excerpt.txt)
5. P16/tools/conv_partI.py
6. P16/tools/edit_partII.py
7. P16/RTA_FOUNDATION_BOUND_v15.pdf + .sha256
8. P16/RTA_FOUNDATION_BOUND_v14.pdf + .sha256 + .sha256.src
9. P16/RTA_FOUNDATION_BOUND.pdf (unversioned)
10. P16/src v14 sidecars: front_v14.tex.sha256, main_v14.tex.sha256, partIII_draft_v14.tex.sha256, plus P16/NOTES_v14.md.sha256
