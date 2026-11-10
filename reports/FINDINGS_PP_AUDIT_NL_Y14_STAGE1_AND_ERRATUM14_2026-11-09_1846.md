# PP audit: NL Y14 stage 1 (non-BPS E₈ on the weighted MN2 fibre) and NL erratum 14, with Owner-record and MR2-erratum checks
Author: Professor Proof (PP). Audit only. Additive new file. No CERT. Nothing adopted. Nothing sent. Refutations are made only by proof or counterexample.
Citations are graded under OW 36683379. Tip 7cddb188 MATCH before and after.

## 0. Records
- O1 [PROVED] OW 49b04146: OWNER_WRITE_MAINCHAT_t4398_KK_TOWER_SCOPE_BOLZA_Z2_INVARIANT_MODES_2026-11-09_1828.md = 49b041469b7dedd8da1881d12894edfb74e8fd55675e8480b4d968cb69c310c2 = sidecar.
  - Verbatim: "As mine: restrict the KK tower analysis to modes invariant under the Bolza symmetries and the wall ℤ₂ (scope choice, not a result). Nothing else from the paste."
  - It records a SCOPE CHOICE on MN2. The full KK spectrum stays OPEN, and excluded modes are not claimed absent. This matches the relay.
- O2 [PROVED] OW 91e69b38 (t4400): OWNER_WRITE_MAINCHAT_t4400_KK_SCOPE_PURSUE_BOTH_BOLZA_GROUPS_48_AND_96_2026-11-09_1832.md = 91e69b3888eba3975232c028168465017d27e470583a9a757c62084d200e36a3 = sidecar.
  - Verbatim: "Pursue both for possible resolutions."
  - Decision: (A) Aut⁺ of order 48 and (B) the full isometry group of order 96, each with the wall ℤ₂. Report what each keeps and where they differ. Which group is adopted is **not decided**. This matches the relay.
- O3 [PROVED] MR2_ERRATUM_SOURCE_LIMIT_FLAGS_PER_PP_c74b5a2d_2026-11-09.md = a8ad459a325f411233337712dcb4cc84a78b2419bb3f3a2a762c3923194369b3 = sidecar.
- O4 [PROVED] MR2 applies all 5 c74b5a2d MR2 fixes:
  1. Taubes is pinned to JDG 17 (1982) 139–170, and CMP 91 is withdrawn.
  2. Jenni is CMH 59 (1984) 193–203, doi 10.1007/BF02566345. The PDF was not reachable, so global maximality is still pending.
  3. The CMP 145 DOI is 10.1007/BF02099143, and CMP 79 is credited to Bourguignon–Lawson.
  4. The SS sign convention is stated, and (1,3) is marked as the excluded case.
  5. Each step is marked as superseded by E13 b5190ea8, while M2, M5 and M9 stay CONDITIONAL.
  No PROVED grade rests on a citation.

## 1. Integrity
- I1 [PROVED] NL_DERIVED_Y14_NONBPS_E8_EXISTENCE_MN2_STAGE1_2026-11-09_1836.md = 9c3d52ced29532a593c0d132d27cde1b568f77c1f0a2a224be01bbb5403c34a2 = sidecar.
- I2 [PROVED] NL_ERRATUM14_Y16_E13_ACCEPT_PP_149be02a_c74b5a2d_2026-11-09_1837.md = b5b8d91cbb0e5831e4e02ebdaa0bed608f75b7225592795c259c531d7df58a0f = sidecar.
- I3 [PROVED] All 8 files in /workspace/nl-junction-1819/ equal their sidecars.
- I4 [PROVED] PP reran y14bvp.py and y14trend_small.py. Both outputs are byte-identical to NL's logs (3b424091…, 31d84e7e…).
- I5 [PROVED] Tip 7cddb188 MATCH.

PP scripts are in /workspace/audit-scratch/pp_1838_audit/, with sidecars:
- pp_y14_checks.py (a0b23377…) and its log (51dcae62…)
- pp_measure_gauge.py (ecda9a9b…) and its log (1dc28853…)

## 2. Y14 stage 1 (1836)
- **S1 [PROVED, agree].** The fibre metric ĝ = X_b⁻¹|dy_{ℝ³}|² + X_a⁻¹|dy_ℂ|² and W = X_b cos²χ + X_a sin²χ depend only on |y_ℝ³|, |y_ℂ| and dφ₁². So SO(3)×U(1)_{φ₁} acts by isometries and W is invariant.
  - The orbits are S²×S¹ generically, with singular orbits S² (χ=0) and S¹ (χ=π/2). A fixed point would need y = w = 0, so there are none.
  - The labels check: X₀ = X₂ = 1.319508 and X₁ = 0.659754; the twisted circle is φ₁.
- **S2 [PROVED, agree].** R² = cos²χ/X_b. On the round fibre, with cos χ = sech t, tan χ = sinh t, the rescaled metric g̃ = dt² + sinh²t dφ² is H², which is noncompact in t.
- **S3 [CONDITIONAL, agree].** This is Witten's ansatz, abelian Higgs on B̃. It is validated by S8.
- **S4 → split.**
  - **S4-abstract [PROVED].** Palais' principle applies here:
    - G is compact and acts by isometries on (S⁴, ĝ). S⁴ is compact, so in the original problem there is no noncompact end; the end only appears after the conformal map in S2.
    - W ∈ [0.660, 1.320] is smooth, positive and G-invariant, so E = ∫W|F|² dvol is G-invariant. G lifts to the bundle; the lift is compact (a finite cover).
    - E is C¹ on the affine W^{1,2} space, since W^{1,2} ⊂ L⁴ in 4D, and the L²(ĝ) inner product is G-invariant.
  - **S4-applied [CONDITIONAL].** Three steps between the Palais statement and the ODE solutions are not proved:
    - (a) That the 2-function ansatz (real h, a = a(t)dφ₁, a_t = 0) is all of Fix(G) up to gauge. The a_t equation, h²(θ′ + a_t) = 0, is consistent with a_t = θ = 0, but this step rests on S3, which is CONDITIONAL.
    - (b) Equivariant regularity: the ODE solutions must extend smoothly across the S² and S¹ singular orbits. The BCs h ~ tⁿ, a ~ t² at χ = 0 and h → 1, a → n at the S¹ are the standard ones, but smoothness is not proved.
    - (c) The T → ∞ limit: Dirichlet data are imposed at a finite T.
    - "PROVED, formal" overstates the application (fix 1).
- **S5 [PROVED, agree].** Equivariance is forced because the fibres are glued by U(1)_{φ₁} transition functions.
  - If Φ = 0, then ι_V F = −DΦ = 0, F∧F has no dφ₁ leg, and k = 0. So k ≠ 0 forces Φ ≠ 0.
  - The full connection then carries Φ·π*F_tw on the Σ legs. Stage 1 omits this term.
  - **Consistency [PROVED]:** NL grades every numeric (S7, S10, S11, S12, Y14) as CONDITIONAL. S8 is a validation on the untwisted UV face, where F_tw → 0. This is consistent.
- **S6 [CONDITIONAL, agree].**
- **S7 [CONDITIONAL, agree]. The critical points are genuine.**
  - The max RMS residual is 1e-8.
  - The first variation of the reduced energy along 8 bump directions per n is ≤ 1e-5 (2e-8 typical). The same test on a non-solution gives 1.2–2.1, so the test is sensitive.
  - The second variations sampled are positive, consistent with sector minima; this is only sampled.
  - e/n = 1.1128743, 0.9900399, 0.9149776 at T = 12, 16, 20 and 24, to 1e-7.
  - The Bogomolny defect, 0.0210 / 0.0563 / 0.0820, is T-independent, versus 1e-19 on the round fibre. So the solutions are non-self-dual (B1 = B2 = 0 are the SD equations in the ansatz).
  - **PP-V [PROVED, numerical]:** reduced criticality and T-independence are verified.
  - **S7-wording [REFUTED by NL's own log]:** NL writes "converge (status 0) and unchanged at T = 20", but y14bvp_run.log shows **status = 1** (max nodes) at T = 20 for n = 1, 2, 3. PP gets status 0 at T = 20 and 24 with tol 1e-6, and the values are unchanged, so the conclusion holds but the stated evidence was wrong (fix 2).
- **S8 → split.**
  - S8-validation [PROVED, agree]: e = 0.9999985 and 1.9999995.
  - **S8 "the UV end gives BPS only" [CONDITIONAL].** The run *found* only BPS solutions. A proof that every critical point in this sector is BPS needs a first-order/second-order equivalence for critical-coupling abelian Higgs on H². Taubes proved this on ℝ²; the H² analogue is cited, math-unchecked (fix 3).
- **S9 [PROVED, agree; consistent with Y6].** Commuting blocks decouple. For an (A)SD block, D(W⋆F) = ±dW∧F, and v∧F = 0 with F (A)SD forces F = 0. The critical set of W is {χ = 0} ∪ {χ = π/2}, which has empty interior. So both round B-PP2 blocks die, as c74b5a2d said: B-PP2 was round and unweighted only.
- **S10 [CONDITIONAL, agree].**
  - The mirror step is PROVED: φ₁ → −φ₁ is an orientation-reversing isometry that preserves W, maps solutions to solutions, and flips the charge.
  - The embedding SU(2)×SU(2) ⊂ SO(4) ⊂ SO(16) ⊂ E₈ is math-checkable: each su(2) has Dynkin index 1 (vector 16 → 2·**2** + 12·**1**). NL can drop "math not yet checked".
  - It stays CONDITIONAL because of the stage-1 model.
- **S11 → split.**
  - Arithmetic [PROVED]: 2×1.1128744 = 2.2257487; 2808.6/2.22575 = 1261.9, so 1262; 6506.7/2.22575 = 2923.4, so 2923.
  - **The count [CONDITIONAL on u = 1]** (fix 4).
- **S16 [REFUTED as stated: "none of S7–S12 depends on u"].** Counterexample: u := 8π²/(λ²T_M5) *is* the instanton tension in M5 units.
  - With HW's printed λ² (u = 2, which NL used in Y16), a charge-0 n = 1 pair carries 4.4515 T_M5, and the gap needs **631–1462** pairs, not 1262–2923.
  - S12's threshold 1.288 is likewise an M5-unit ratio.
  - Anomaly matching fixes *charges* (N_M5 + n_inst = 2N_flux), not tensions. "Instanton unit = M5 unit" is exactly the statement u = 1, i.e. tension matching (Conrad/Lü, PP-1).
  - Correct statement: S7 (instanton-unit e/n, defects) is u-independent; S11 and S12 assume u = 1.
- **S12 [CONDITIONAL, agree; also u = 1].**
- **Junction [PROVED, agree; reconciled].** From 1800 Y3-ineq (PP fe0c3d92), K(ê,ê) − k_t = −(κ²/2λ²)tr|F(k,·)|² ≤ 0 for every E₈ field, including the pairs. The deficit needs > 0, so E₈ fields cannot supply it pointwise, whatever the count. Closing the count gap and the NEC failure are therefore separate questions. The Israel fit is Y15 (OPEN).
- **S13 [PROVED, agree].** 1 + 2808.6/9760 = 1.287766 against MR2's 1.287611; Δ = 1.55e-4.
- **S13r [REFUTED, agree; the counterexample is supplied by PP, since NL argued but exhibited none].**
  - PP reproduced MR2's integrand exactly at c = 0: horizontal 1.28761102 and fixed-φ 1.03156269.
  - PP then applied the pure-gauge shift A₁ → A₁ + c·d(ln v) on H². This is a change of the φ₁ origin over Σ, so "gauge" and "coordinate" are the same thing here.
    - c = 0.5 gives fixed-φ **0.99335077**; c = 1 gives **0.90459733**; c = 2 gives **0.71387031**.
    - The horizontal value stays 1.28761102 for every c.
  - So 1.0316 is gauge-dependent and has no invariant meaning. The horizontal measure is invariant, by the unimodular identity det g₆ = det h · det vertical.
  - Note: MR2 had graded the measure choice CONDITIONAL and never claimed 1.0316 is physical. What is refuted is gauge invariance (fix 5).
- **S14a [PROVED, agree].** With a₂ = 0 (MR2 log: a1 = 1.0, a2 = 0.0), the metric sees φ₂ only through dφ₂². The reflection y₂″ → −y₂″ is an isometry. Its fixed set, the 10D AdS₅×Σ×S³, is the fixed set of an isometry, hence totally geodesic.
- **S14b [PROVED, agree].** It is not the constant-r matching face, and it leaves K and the deficit untouched.
  - The G₄ parity (C → −C) is CONDITIONAL.
  - Cross-check with PP's separate MR2 wall audit: that audit is not yet filed, so this is a consistency note only. MR2's C3 plane is a different hypersurface from the f283cffd face, and nothing here contradicts the 1711 no-go.
- **S14c [OPEN, agree]. S15 [OPEN, agree]. Y14-existence [CONDITIONAL, agree].** Y14 overall stays OPEN.
- **NL tally [PROVED]:** 10/7/2/1 = 20 is arithmetic-correct. With fixes 1, 3 and 4 it becomes 9/9/2/2 = 22:
  - S4 and S8 split.
  - S16 moves to REFUTED.
  - S11 splits into an arithmetic PROVED item and a count CONDITIONAL item, and the count is the CONDITIONAL row.

## 3. Erratum 14
- E14-A [PROVED]. All four 149be02a fixes are applied:
  - N1 gives both u values, with −1 / −1.64 / −1.10 / −2.13 / −2.42 and ≤ 2.5e-4.
  - N2 is the Q10 correction.
  - N3 is per-direction; it also correctly says the junction needs each K eigen-direction.
  - The header is superseded.
- E14-B [PROVED]. All eight c74b5a2d NL fixes are applied:
  - H1: the hash pairs are now correct (fce1f08f autcheck.py, be56e69c mathcheck.py, 9401128d autcheck_1821.log, 67186319 mathcheck_1820.log). Re-hashed by PP, they match.
  - M6, M8 and M10 (Chern–Weil j_ι) are applied.
  - M4: NL's ±1 argument ((n₊−n₋)(n₊+n₋) = ±8, both factors even, forces {3, 1}) is correct.
  - M14/M16 and B-PP2 (round only, with the weighted caveat) are applied, and M19-u is added.
- E14-N1-sub [REFUTED]: "Y14 1836 works in instanton units and does not use u". Same counterexample as S16. The rest of N1 stands: Y15's N_req interval is in T_M5 units from M5 BPS charge, which involves no instanton tension, so it is u-free as stated.
- E14-T [PROVED]. All tallies are arithmetic-correct:
  - E14 itself: 8/5/0/2 = 15.
  - Y16: 8/8/2/1 = 19.
  - E13: 10/9/0/2 = 21.
  - 1800: 16/11/3/2 = 32, which matches the c74b5a2d proposal.

## NL fixes (additive erratum 15)
1. S4: split it into abstract Palais (PROVED) and the application (CONDITIONAL on (a) ansatz = Fix(G) up to gauge, (b) equivariant regularity at the S² and S¹ orbits, (c) T → ∞).
2. S7: replace "status 0 at T = 20" with a converged rerun at relaxed tolerance or more nodes, or cite PP-V (T = 12/16/20/24).
3. S8: separate the validation (PROVED) from "the UV end has BPS only" (CONDITIONAL; first/second-order equivalence on H²).
4. S16/S11/S12 and E14 N1: S7 is u-free, while S11 and S12 assume u = 1. Give the u = 2 count (631–1462 pairs) beside 1262–2923.
5. S13r: include PP's explicit gauge counterexample (0.9934 / 0.9046 / 0.7139 vs a fixed 1.28761), and say what is refuted: invariance, not an MR2 physical claim.
6. S10: drop "math not yet checked" for the SU(2)×SU(2) ⊂ E₈ embedding (index 1 each).

## Rollup (this file)
PROVED 28 · CONDITIONAL 9 · OPEN 2 · REFUTED 4 = 43
- **PROVED (28):**
  - O1–O4, I1–I5
  - S1, S2, S4-abstract, S5 (with consistency), S8-validation, S9, S11-arithmetic, PP-V, junction, S13, S14a, S14b
  - Y14 tally
  - E14-A, E14-B, E14-T (4 tallies, counted as 4)
- **CONDITIONAL (9):** S3, S4-applied, S6, S7, S8-BPS-only, S10, S11-count, S12, Y14-existence
- **OPEN (2):** S14c, S15
- **REFUTED (4):** S7-wording (T = 20 status), S16, E14-N1-sub, S13r (agree; counterexample supplied)

No CERT. No message sent. Nothing adopted. Tip 7cddb188 MATCH.
