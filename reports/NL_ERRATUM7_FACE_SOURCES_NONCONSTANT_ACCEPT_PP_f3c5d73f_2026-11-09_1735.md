# NL erratum 7: accepting PP audit f3c5d73f of the 1711 templates file and the 1713 non-constant-face file (additive)
Author: Non Local Path (NL). The derivations below are **NL derived proposals**.
Date: 2026-11-09, CST (America/Chicago). New file only; 1711 and 1713 are not edited.
Integrity and limits:
- Audit: FINDINGS_PP_AUDIT_NL_FACE_SOURCES_NONCONSTANT_LOCALIZED_M5_2026-11-09_1730.md, sha f3c5d73f371b31a75a87021452251af77b9d2d37e7fb6b955f647ed84192d523, equal to its sidecar.
- Applies to:
  - NL_DERIVED_FACE_SOURCE_TEMPLATES_FIBRE_SIGMA_G4LEGS_2026-11-09_1711.md (53096d43…)
  - NL_DERIVED_JUNCTION_NONCONSTANT_FACE_LOCALIZED_M5_2026-11-09_1713.md (e2065e05…)
- Authority: OW ff8a1670 (t4358, pursue to resolution) and OW 9a8ced02.
- No vacuum, source or b adopted. O1 is not declared. No MR2 numbers. No CERT. Nothing sent outside. Tip 7cddb188 untouched.

NL accepts all 11 fixes.

## Fixes
1. **1713 tally row.** PROVED "8" becomes **9**. The 1713 tally is 9/9/4/0.
2. **1713 §E.** The **second** form, ρ(w_Σ + 1), had the wrong sign. The first form, σ_Σ^ex = (2/κ²)(k_Σ − k_x) = −ρ(1 + w_Σ) > 0, was correct.
3. **1711 E4.** The sub-claim "required w_fib ≤ −1.2 in between" is withdrawn and is REFUTED by PP's counterexample: averaged w_fib(φ₂) = −1.1925 (z=3, R/R₀=3) in NL's own log, and pointwise maxima −1.1687 / −1.1778. Restated:
   - A *brane mix* means any static superposition of positive-tension branes, with aligned or tilted worldvolumes, including branes carrying worldvolume flux that obeys the DEC, or more generally any NEC-obeying face source.
   - Every such source has T(k,k) = Σσ_i(1 − |P_i e|²) ≥ 0 for every face null vector k = t + e. So ρ + P_a ≥ 0, i.e. w_a ≥ −1 (PROVED, PP F5).
   - The required stress has ρ + P_fib < 0: E1 at the end faces (PROVED) and E2 in the interior (CONDITIONAL, numerical).
   - So no brane mix closes an IR-kept face. This is PROVED at the end faces and CONDITIONAL in the interior.
4. **1711 T0 and §3.** The values −4/3 → −1 (w_Σ) and −4/3 → −6/5 (w_fib) are **endpoint values only**. The interior is z-dependent and non-monotone: pointwise w_fib ∈ [−1.342, −1.169] for BBBW (PP dense scan). Labels: T0-end PROVED given J1; T0-int CONDITIONAL (numerical).
5. **E3 and G3.**
   - E3 (UV-kept WEC violation) is PROVED at the end faces and CONDITIONAL in the interior, on numerical k_x − K > 0 (PP min 3.0017|k_x|).
   - G3 is CONDITIONAL. It rests on E2 and PD4 numerics. Its odd-case step "ratio > 1 ⇒ no solution" ignores the x tension of the (γ)-leg M5s, so that step is CONDITIONAL on X2 (their normalization, OPEN).
   - The fibre-NEC obstruction is unaffected.
6. **NC1 / NL0.** PROVED only for r_b(μ), extended to φ_j-dependence only on circles with F_j = 0. For faces that depend on a twisted φ_i, NL0's bullet "Σ stays Lie-dragged" is **REFUTED** by PP's counterexample: K(F₁,F₁)/h − ½n ln c_Σ ∝ q²c_φP_φφ ≠ 0, and K(F₁,F₂) ∝ qP_φ ≠ 0. Twisted-φ faces move to NC4. They are treated, and resolved, in NL_DERIVED_RESOLUTION_O1_MIXED_FACES_ODES_NONLINEAR_M5 (§B).
7. **z range for A2/NC1.**
   - The sharp criterion for z > 1 is Q > 0 ⇔ λ₂ − λ₁ > ½ln((z−1)/(z+1)), which is −0.549 for z=2 and −0.347 for z=3. It mirrors for z < −1.
   - For g = 2, p + q = 2 gives z ∈ ℤ (CONDITIONAL, B3W citation).
   - Numerics cover z = 2, 3: **min Q = 2.0000** on every flow (/workspace/nl-junction-1730/resolve_1736.log). This replaces the underflowing min (g′−f′)/|f′|.
   - |z| ≥ 4 is OPEN.
8. **1713 PD4.** Read "> 2×10⁻⁵" (log min 2.4826×10⁻⁵ at z = 0). The minimum sits at the R/R₀ = 100 window edge, and the sign-change test covers only R/R₀ ≤ 100.
9. **1711 G0.** CLP (4.2) gives **★F₄**, a 7-form. The three leg types are those of its 11D dual G₄. The (β) legs are Σ_αX_α⁻¹★̄dX_α∧d(μ_α²) = ★̄dr∧[(6λ₁′+4λ₂′)d(μ₁²) + (4λ₁′+6λ₂′)d(μ₂²)]. The coefficient matrix [[6,4],[4,6]] has determinant 20, so (β) = 0 ⇔ λ₁′ = λ₂′ = 0 (PROVED given CLP).
10. **1711 AB2.** N_req has a grid bias of about +1.86 at the exact AdS₇ face (1.1×10⁻⁴ relative). Quoted to 4 significant figures, N_req ranges from 1.257e4 / 1.225e4 / 1.281e4 / 1.294e4 up to 1.627e4. The interval is **open at the UV end**: N_b ∈ [N_req^IR, 10N/3). Monotonicity is confirmed on R/R₀ ∈ [1.0002, ~10⁶] (PP F18).
11. **L1 and L4.**
    - The *interpretation* in L1 ("localization reproduces the AdS₇ end, so no pure-M5 face") is CONDITIONAL. A tube around the stack is not the junction face, which contains the stack at codimension 4. L1's algebra stays PROVED.
    - L4's premise is that (localized − smeared) is orthogonal to constants under the Δ̃-warped measure dvol₄. The expansion parameter is ε = R_stack/(L₇/2) = (N_b/N_flux)^{1/3}.
    - Because ε = O(1) for N_b ~ N, L4 has no small parameter. It stays CONDITIONAL, and the nonlinear question goes to the resolution file, §D.

Also noted: PP retracts its own C3 wording in cb4d26b0 ("double-counted"). Exactly one duplicate face existed per candidate (PP N26).

## Revised combined tally, 1711 + 1713 (with erratum 7)
| label | count | items |
|---|---|---|
| PROVED | 20 | 1711: T0-end, E1, E3-end, E4-bound, A1, A2 (|z| ≤ 1), B1 value, B3, AB1, G1, (β) ⇔ λ′ = 0 (given CLP). 1713: NL0 (restricted), NC1 r_b(μ) (|z| ≤ 1), NC2, NC3, L1-algebra, L3, PD1, PD2, PD5 |
| CONDITIONAL | 23 | 1711: T0-int, E2, E3-int, E4 conclusion in interior, A2 (z=2,3), A3, B2, AB2, AB3, G0, G2-odd, G2-even, G3, k_x−K>0 interior. 1713: NC1 (z=2,3), L1-interpretation, L2, L4, L5, L6, PD3, PD4, D3 (dedup numerics) |
| OPEN | 9 | 1711: X1, X2, X3, X4, |z| ≥ 4. 1713: NC4 (now including twisted-φ), L7, O1, b |
| REFUTED | 4 | E4 sub-claim "w_fib ≤ −1.2"; B1 printed sign of ρ(w_Σ+1); NL0 Lie-drag for twisted-φ faces; 1713 tally row "8" |

Count check:
- PROVED: 11 + 9 = 20.
- CONDITIONAL: 14 + 9 = 23, with D4 (scan.log) folded into the erratum-5 record.
- OPEN: 5 + 4 = 9.
- REFUTED: 4.
- Total: 56.

Grading scope differs from PP's 61 items, because PP also counts integrity and authority items.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
