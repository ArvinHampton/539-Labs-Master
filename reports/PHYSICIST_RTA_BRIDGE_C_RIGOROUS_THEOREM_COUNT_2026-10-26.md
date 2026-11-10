# RTA + Bridge Series C — rigorously proved theorem count
Written: 2026-10-26 ~7:30 PM CDT (America/Chicago). Read-only on sources; counts quoted from artifacts only (invent-ban).

## Result
- **total_now = 64**
- **baseline_before_2026-10-26 = 64**
- **today_added = none (0)**

## A. Baseline (64)
- T928U (2026-10-25): 64 distinct established theorems = 62 in Zenodo 23644022 (v12) + Thm 8.4 and supplemental Thm 1 of Zenodo 22143607. Bridge C rev2–rev9.2 / Clean / Clean-v2 theorems are earlier numberings of v12 theorems (e.g. rev9.2 Thm 11.3 = v12 Thm 19.3; Thm 13.16 = v12 Thm 20.5) — counted once.
- v13 (main_v13.tex) = v12 inputs + front_v13 + partIII_partial_v13.tex only. partIII_partial_v13 contains no theorem environment and states "This subsection is a status inventory, not a new set of proofs"; Auditor 1c9ff854… (MATCH-with-SF) and SF1 recheck (MATCH, PDF b07e72ac…) confirm no proofs added. So v12/v13 dedupe → +0.
- Every v12/v13 theorem carries "Status (Category A)" (paper convention: proved / exact / computer-assisted / cited).
- Local Cat A closures (AW-α, O-α, PB-α, E-α, NL A1–A12) and LOCKED records (G-A1c, G-R2, B3-α, T-α) are Auditor-confirmed acceptances/LOCKs, not theorem-labeled proofs → not counted (LOCK ≠ proved).

## B. 2026-10-26 scan (713 .md files with today's mtime; 87 matching PROVED/Theorem). Candidates, all rejected:
| Candidate | Lane | File | Reason rejected |
|---|---|---|---|
| Lemma NL-JOIN-1 "structural cite-proof" | NL | bridges/NONLOCAL_QM_EH11D/PROOF_NL_JOIN_1_RIGOROUS_2026-10-26.md | Lemma, not theorem; (P1) rests on Owner LOCK e41ceac4… (LOCK ≠ proof); "NO PASS CLAIM"; not in paper inventory |
| P5a κ=4 cusp-space vanishing | MR2 / Auditor | MR2-FINDINGS-P5A-REWRITE-CONGRUENCY; AUDITOR t1126u, t1034u | Tagged "to prove"; "whether the cusp space is {0} … NOT asserted" — unproved |
| "Theorem 1/2 (E_leak …) k_min ≥ 35 / ≥ 46" | PR1 | PR1-FINDINGS-E_LEAK_TERM_DEPENDENCY_TABLE_2026-10-26.md | Conditional on Axiom N ("not Owner-Written"); symbol-count bound on NL sheet, not RTA/Bridge C; Soft SF FINDINGS only |
| R3-1, R3-2(a)(b)(c)(e) PROVED items (θ³f ≡ f⊗χ₋₇ mod 7, etc.), Eigen "ACCEPT PROVED" | MR2 / Eigen | MR2-FINDINGS-CATB2-CONTINUE-PARTIAL-R3; EIGEN_REVIEW_RELAY_MR2_CATB2_CONTINUE_R3 | Unlabeled lemma-level items in a PARTIAL FINDINGS; not theorem-labeled; not in paper |
| F2 residual identity on slice; Prop B′/B″ | MR2 | MR2-FINDINGS-CATB2-TEITELBAUM-DEEPEN-RESUME | Status PARTIAL; B′/B″ conditional propositions |
| F1/F2 (GEOM11D), A1–A4 (archimedean) | MR2 | MR2-FINDINGS-FREE-PURSUE-MISSED-VARS-GEOM11D; MR2-FINDINGS-ARCHIMEDEAN-RESIDUAL-CORR | Findings/propositions, PARTIAL |
| Lemma D1; G1 injectivity lemma | MR1 | FINDINGS_MR1_MESH_N_GT18_W7_SLASH_PREMISE; FINDINGS_MR1_COOK_RESUME_MATHLIT_G1_N36N6_PACKAGING | Lemmas; application UNPROVEN / G1 PARTIAL |
| ρ̄-Sturm depth 18 | MR1 / Eigen | FINDINGS_MR1_Q18_DEPTH_JUSTIFY_CITE | Explicitly "NOT a proved ρ̄-Sturm theorem" |
| PR1 L1–L3, F1–F5, "PROVED by inspection" rows | PR1 / Auditor SoftSF | PR1-FINDINGS-CATALOG…, -HEPP_QM_GR… | Catalog/ABSENT inspection, not theorems |
| Hom-A35 Cat A | PR1 | PR1-FINDINGS-VANISHING-LEAD-RANK14_HOM-A35-CATA | Quotes existing corpus Cat A result, not new |
No new .tex/paper build dated 2026-10-26 (only literature PDFs downloaded).

## Excluded notables
P5a κ=4 cusp-space vanishing (unproved, "to prove"); Remark (Category B) 11.11 cusp rows; Theorem 1.1 (external cited); 18 corollaries + propositions; residual question for C OPEN; Bridge PARTIAL / READY NO; X4 ABSENT; G-A3 PAUSED; Rank-20 δ_W₇ SAMPLE ONLY.

## Ambiguities (could change count by ≥1)
1. Thm 11.10 (Closed form of E_R): Cat A but "proof is given in outline … No arithmetic proof … is claimed" → strict reading −1.
2. Thms 26.7, 26.9 (K3): "Category A (cited)" — proofs rest on Nikulin/Morrison/Torelli → strict "proved here" reading −2.
3. Conditional Cat A: 11.5 (Baker, q-expansion), 19.3 (cited congruence), 20.11 (cited C3), 24.5 (cited analyticity) → if conditional excluded −4.
4. 22143607 Thm 8.4 (cocycle vanishes "to machine precision"; uniqueness off sample points open) and supplemental Thm 1 (discrete half only) → −1 to −2.
   Strictest combined reading: 64 − 9 = 55 (or 54).
5. If PR1 "Theorem 1/2 (E_leak)" were accepted as theorems: +2 today (rejected: conditional on non-Owner Axiom N, outside RTA/Bridge C).
6. If MR2 R3 PROVED items (Eigen-accepted) were promoted to theorem status: up to +5 today.

## Sources
T928U_RTA_THEOREM_COUNT_2026-10-25.md; papers/RTA_FOUNDATION_BOUND/NOTES_v13.md, src/main_v13.tex (+ all \input files), partIII_partial_v13.tex, RTA_FOUNDATION_BOUND_v13.pdf (pdftotext); bridges/AUDITOR/FINDINGS_2026-10-25_paper_v13_partial_claim_audit.md and _SF1_recheck.md; Bridge C rev7–rev9.2/Clean/Clean-v2 via T928U dedupe; 2026-10-26 files listed in §B. LOCK_DIGEST/LOCK_SUPERSEDE_INDEX t1055u grepped: zero occurrences of "theorem"/"proved" → they add no theorems (LOCK ≠ proof).
