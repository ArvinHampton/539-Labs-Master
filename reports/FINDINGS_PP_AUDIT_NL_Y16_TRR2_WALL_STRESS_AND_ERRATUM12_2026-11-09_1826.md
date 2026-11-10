# PP audit: NL Y16 (HW wall −½tr R² stress, NEC) and NL erratum 12 (accepting fe0c3d92)
Author: Professor Proof (PP). Audit only. Additive new file. No CERT. Nothing adopted. Nothing sent. Tip 7cddb188 untouched.
Citation rule applied: OW 36683379 (18:15, sha 36683379… MATCH), all sources allowed, cited math must be checked; a citation alone never gives PROVED.

## Integrity
- I1 [PROVED] NL_DERIVED_Y16_HW_TRR2_WALL_STRESS_NEC_2026-11-09_1813.md = 7270a6b35c97822a4efe37b7f6e78d94efafd0ae44d298ba70554e926c9d5237 = sidecar.
- I2 [PROVED] NL_ERRATUM12_1800_ACCEPT_PP_fe0c3d92_2026-11-09_1813.md = 53d4f945e2d4df565cfa7cdae90dcda8a7b8c0c33855ee3efdf79004cd682230 = sidecar.
- I3 [PROVED] /workspace/nl-junction-1806/: y16.py (2a999eb3…) and y16_1812.log (fa443be5…) equal their sidecars.
- I4 [PROVED] PP rerun of y16.py → /workspace/audit-scratch/pp_1813_audit/y16_rerun.log (fa443be5…), byte-identical to y16_1812.log. Round check ∫Riem² = 64π² reproduced.
- I5 [PROVED] Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH.
- Attribution [PROVED]: "Y16 first" is Physicist's 18:05 relay, not OW 9bb1858c text. NL states this correctly.

## Y16 items (NL grade → PP grade)
- Q15 [PROVED, agree]. From the Z₂ Israel condition K_ab − h_ab K = −(κ²/2)S_ab and a null k = t̂+ê: K(k,k) = K(ê,ê) − k_t (static, K(t̂,ê)=0) = −(κ²/2)S(k,k). The YM term (1/λ²)tr F(k,·)·F(k,·) ≥ 0 because F(k,·) ⊥ k. The M5 term ≥ 0. So only S_R² can supply the needed S(k,k) < 0.
- Q2 [CONDITIONAL, agree]. Premise. HW (hep-th/9603142 eq. 1.13) say the tr R² piece is inferred from anomaly cancellation, and the action completion is inferred too.
- Q1 [CONDITIONAL, agree]. tr(R_ab R^ab) = −Riem² for real antisymmetric so(1,9) matrices. With the hermitian-trace convention that makes −|F|²/4λ² the right YM sign, L_R = +Riem²/(8λ²). This matches the sign of the heterotic +α′/8 Riem² term (not re-derived).
- Q0 [CONDITIONAL; arithmetic checked; normalization CONTESTED, see PP-1]. λ² = 2π(4πκ²)^{2/3} = (2π)⁷ and u = 2.000 for HW's printed value are both verified.
- Q3 [PROVED, agree]. T_ab = −(2/√h)δ(√h c Riem²)/δh^ab = −4c R_acde R_b^cde + c h_ab Riem² + 4c∇∇R terms. Sign check: L = −V gives T_tt = +V. The ∇^c∇^d R_acbd terms vanish when ∇R = 0. The equivalent "commuted" form −4∇²R_ab + 2∇∇R + 4R_acR^c_b − 4R^cd R_acbd also vanishes on Einstein-factor products, because R_acR^c_b = R^cd R_acbd factor by factor.
- Q4a [PROVED, agree]. On S⁴(R): Riem² = 24/R⁴ and R_ecde R_e^cde = 2(n−1)/R⁴ = 6/R⁴. On H²(ρ) the values are 4/ρ⁴ and 2/ρ⁴. This gives ρ_R = −c(24/R⁴ + 4/ρ⁴), with S(k,k) = −24c/R⁴ (fibre), −8c/ρ⁴ (Σ) and 0 (x).
- Q4b [CONDITIONAL on Q1, agree]. +12cκ²/R⁴ > 0.
- Q5 [PROVED in terms of λ, agree]. −24c/R⁴ · (8π²R⁴/3) = −64π²c = −8π²/λ². This is R-independent and equals −c∫_{round}Riem². The value "−2 M5 units" is CONDITIONAL on Q0; it becomes −1 under PP-1.
- Q6 [CONDITIONAL, agree]. The values 1.645/1.099/2.135/2.425 × round are reproduced. The labels are right: z=1 is MN2 and z=0 is MN1. Fix 3 applies.
- Q7 [PROVED given J1, agree]. The 4D integral ∫Riem² dvol₄ is scale-invariant, so the R² supply is N-independent while the requirements are ∝ N.
- Q8 [OPEN, agree]. Q14 [OPEN, agree].
- Q10 [CONDITIONAL, agree with a rounding fix]. 0.78×12252 = 9556.6. The fraction is 3.44×10⁻⁴ for MN2, but for z=3 it is 4.85/9556.6 = 5.07×10⁻⁴, which is not ≲5×10⁻⁴. See fix 2.
- Q11a [PROVED given J1, agree]. Q11b [CONDITIONAL, agree].
- Q12a [PROVED, agree]. The Bianchi tr R² integrated over a fibre uses TY|_{S⁴} = TS⁴ ⊕ trivial (the normal bundle of a fibre is trivial), and p₁(TS⁴) = 0 (TS⁴ ⊕ ℝ = ℝ⁵).
- Q12b [CONDITIONAL, agree]. The R² term raises the needed excess by |n_R| units: 2–5 with HW-printed λ, or 1–2.4 under PP-1.
- Q13 [PROVED, agree]. area(Σ) = 4π by Gauss–Bonnet; the result is local per unit area.
- NL tally 8/8/2/0 = 18 [PROVED]. It is arithmetic-correct and the lists match the items.

## PP new item
- PP-1 [CONDITIONAL; cited, math-unchecked for the anomaly derivation, arithmetic checked]. Conrad (hep-th/9708031) and Lü (hep-th/9711014) find η = λ⁶/κ⁴ = (4π)⁵ in downstairs units, 8× HW's printed value. That gives λ² = 4π(4πκ²)^{2/3} = 2(2π)⁷ and **u = 8π²/(λ²T_M5) = 1 exactly**. u = 1 is what the small-instanton ↔ one-M5 tension match requires, given NL's instanton energy 8π²|k|/λ² (that normalization is not re-checked here). Consequences:
  - Q5 becomes −1 unit.
  - Q6 n_R becomes −1.64/−1.10/−2.13/−2.42.
  - Q10's fraction is at most 2.5×10⁻⁴.
  - **No verdict changes.**
  - NL must check whether any 1750/1800 numbers (Y1, Y15) use u = 2.

## Erratum 12: PP fixes 1–10 of fe0c3d92
- E12-1 to E12-10 [PROVED: applied faithfully, 10/10]. Y3 split ✓. Y6 split ✓. Y15 interval and per-candidate ends ✓. Γ2 Jenni/FB-R, flagged second length, 48/96 ✓. Γ3 ✓. Γ5 ✓. Y1 ✓. Citation flag ✓ (now superseded by OW 36683379; see the citation-scope note). Erratum-11 note ✓. Attribution ✓.
- E12-T [PROVED]. The erratum tally 7/5/0/2 = 14 is correct.
- E12-1800 [PROVED]. The revised 1800 tally 13/11/3/2 = 29 is correct. Starting from 11/10/3/0: Y3 and Y6 (both PROVED) go out and 4 PROVED items come in; Y6-phys is added as CONDITIONAL; two items are REFUTED.

## NL fixes (additive erratum)
1. Q0/Q5/Q6/Q10/Q12b: give both normalizations (HW-printed u = 2; Conrad/Lü u = 1), label PP-1, and re-check Y1/Y15 for any use of u.
2. Q10: write "≤ 5.1×10⁻⁴ (z=3); 3.4×10⁻⁴ (MN2)" or round consistently.
3. Q6: n_R is the fibre-integrated energy. It equals the fibre NEC supply only after averaging over fibre directions (S(k,k) = −4cR_ecde R_e^cde per direction). State which ê the junction uses.
4. "No outside services" (header): it was true at 18:13; it is superseded by OW 36683379 (18:15).

## Rollup (this file)
PROVED 27 (I1–I5, attribution, Q15, Q3, Q4a, Q5, Q7, Q11a, Q12a, Q13, Y16 tally, E12-1…10, E12-T, E12-1800) · CONDITIONAL 9 (Q0, Q1, Q2, Q4b, Q6, Q10, Q11b, Q12b, PP-1) · OPEN 2 (Q8, Q14) · REFUTED 0 = 38.
Scripts: /workspace/audit-scratch/pp_1813_audit/y16_rerun.log (+ .sha256).
Tip 7cddb188 MATCH before and after. No CERT. No message sent. Nothing adopted.
