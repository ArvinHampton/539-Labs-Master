# NL DERIVED: per-direction tr R² stress versus the null Israel condition on MN2 wall faces
2026-11-09, 20:25 CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED**, unchanged. The count-gap status is unchanged.

Authority: **OW t4426** OWNER_WRITE_MAINCHAT_t4426_PURSUE_ALL_OPEN_JUNCTION_ROUTES_2026-11-09_1956.md = d5eaeef3f6b53270bd09e30053f6cdbf442d191c58a0a9fda30daff83907ffb3 ("Pursue all open"; χ-smearing is NOT decided; this is item 3, the per-direction tr R² check owed by Y15 §7 and E17). **OW t4431** OWNER_WRITE_MAINCHAT_t4431_LIFT_90_PERCENT_STOP_2026-11-09_2020.md = f700141d3ee862c7b077b0f67db5fb03b3adc56808c927ba1dd016c88910b1ec (the 90% stop is lifted; usage is still reported). Also OW 19a88b19 (MN N=2 working vacuum, CONDITIONAL; junction UNSOLVED); OW f825dfff (odd HW-type ℤ₂ wall, IR side kept); OW 36683379 (citations checked, never upgrade alone); OW f1d167d1 (where the algebra is named it is "resonant algebra"; it is not named in this file). Y15 1955 = 86a46df7…; Y16 1813 = 7270a6b3…; Erratum 14 N3; E17-NEC / E17 §2.

Limits: additive only. The Y16 script /workspace/nl-junction-1806/y16.py (2a999eb3…) is not edited. No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before and after. Usage 76.9% at the start of this item.

χ-smearing is not decided (OW t4426). The **χ-smeared** and **χ-uniform** branches are carried as separately labelled hypotheses wherever the choice matters.

**Tally: PROVED 3 · CONDITIONAL 5 · OPEN 1 · REFUTED 0 · total 9**

## 1. Question and setup

Y15-R2 used Y16's *integrated* bound (2–5 M5 units against a required 4189.5) as a stand-in for the *integrated* null component, and concluded that tr R² is about 10³ short. Erratum 14 N3 noted that the junction uses S(ℓ,ℓ) for each eigen-direction of K separately, with algebraic value −4c R_{ê cde} R_ê^{cde}, and that the per-direction values on the squashed IR fibre had not been computed. This file computes them, and asks: is there any null direction ℓ = t̂ + v, on any MN2 wall face, in which the tr R² stress has both the needed sign (S_R(ℓ,ℓ) < 0) and the needed size (|S_R| ≥ |S_req| = (2/κ²)|k_v − k_x|)?

Conventions, as in Y16 and face.py (ℓ_P = 1, 2κ² = (2π)⁸, T_M5 = (2π)⁻⁵, N_flux = 4880, L₇ = 2(πN)^{1/3} = 49.684382, L₅ = 37.653721, g_c = 2). Both normalizations are used: **u = 2** (HW printed) and **u = 1** (Conrad/Lü, Erratum 14 N1). c = 1/(8λ²), with λ² = (2π)⁷ · (2/u). The algebraic stress is T_{ab} = −4c R_{a cde} R_b^{cde} + c h_{ab} Riem², plus ∇∇R terms that vanish on locally symmetric products (Y16 Q3) and are **not** included here (they are part of Q8). For a static face, S(ℓ,ℓ) = T_{tt} + T_{vv} = −4c (I(t̂) + I(v)), with I(e) := R_{e cde} R_e^{cde}. Without warp mixing, I(t̂) = 0 and S(ℓ_v,ℓ_v) = −4c I(v).

Script and log, new dated directory `/workspace/nl-trr2-dir-2017/`, sidecars:
- trr2_per_direction_2026-11-09_2022.py = e0b48c9c6656db19fb61db21594af17a72a8919424cbc35fb3375928eeb7c2b4, **frozen before execution**
- trr2_per_direction_2026-11-09_2022.log = 0d64739d1e23792ae3a5e150713f59efd42ca3c62b385764681f73307f3cb382

The fibre chart and the quadrature (n = 24 Gauss–Legendre, 576 nodes in a (θ,ψ) octant, ×(2π)² for the φ's) are those of y16.py. The 4-metric in that script is γ = Δ̃^{−2/3} Ĝ; the physical fibre metric is (L₇/g_c)² γ, so I_phys = I_y16 / (L₇/g_c)⁴ with L₇/g_c = 24.842191.

## 2. Checks against Y16

- **R2-round (PROVED; analytic on the unit round S⁴, reproduced by the script).** On the y16 unit round S⁴, Riem² = 24 and I(ê) = 6 in every fibre direction at every node, ∫ Riem² dvol = 64π² = 631.654682 (byte-agreement with y16 to all printed digits), and the identity Σ_{a=1}^{4} I(e_a) = Riem² holds to 7×10⁻¹⁵. The warp tensor H_{ij} = ∇_i∇_j u + ∂_i u ∂_j u vanishes (max |H|² = 3×10⁻³², a float zero), as it must for constant Δ̃.

- **R2-Y16 (PROVED as a reproduction of Y16 Q6).** On the MN2 IR fibre (X₁ = 0.659754, X₂ = X₀ = 1.319508), ∫ Riem² dvol = 1038.933973 = 1.644782 × round, and the direction-average |n_R| = c ∫ Riem² dvol / T_M5 equals **3.2896 M5 units at u = 2** and **1.6448 at u = 1**, matching Y16 / Erratum 14 N1. The identity Σ I(e_a) = Riem² holds to 8.5×10⁻¹⁴.

## 3. Exact MN2 IR face, fibre directions

At the exact MN2 IR face, k_Σ = k_fib = 0 and k_x = −Δ̃^{−1/6}/L₅ < 0 (face.py). So |S_req|(ℓ_v,ℓ_v) = (2/κ²) k with k = Δ̃^{−1/6}/L₅, which varies over S⁴ by only about 12% (Δ̃ ∈ [X₁, X₀] = [0.659754, 1.319508]). The n = 24 grid reaches Δ̃ ∈ [0.666420, 1.319508]; it does not quite hit the X₁ pole (a coordinate singularity, not a curvature singularity). The most favourable node is already the one of least Δ̃ on the grid (θ = 1.6714, ψ = 0.0038), i.e. at the X₁ axis to the resolution of the chart.

- **R2-sign (CONDITIONAL: fibre-intrinsic algebraic part, n = 24 grid, ∇∇R and the twist omitted).** I(ê) > 0 in every fibre direction at every node (min I_min = 1.155). So S_R(ℓ_fib, ℓ_fib) = −4c I(ê) is negative, which is the sign the junction needs. The needed sign is not the issue; the size is.

- **R2-IR (CONDITIONAL: same hypotheses; both u; float64).** Pointwise on the grid, in the most favourable fibre direction at each node,
  |S_R|/|S_req| ranges from 5.009×10⁻⁴ to **3.494×10⁻³ at u = 2**, and from 2.505×10⁻⁴ to **1.747×10⁻³ at u = 1**.
  The shortfall factor at the best node is **286 (u = 2)** or **572 (u = 1)**. The same node realises the maximum ratio and the minimum Δ̃. Directional anisotropy is mild: at that node, I_max / (Riem²/4) = 1.207. The larger variation is positional (Riem² ranges over a factor 10.91 on the grid; I_max ranges from 6.16 to 48.14 in y16 units). An unphysical upper envelope that uses I_max in every fibre direction at once still integrates to only 4.706 M5 units at u = 2 (2.353 at u = 1), against the required 4189.5, a factor 890 (u = 2) or 1780 (u = 1). Smoothness of the curvature on the compact S⁴ precludes a jump by 10² in the last 1% of Δ̃ down to X₁, so the missed pole does not change the shortfall class.
  **χ-uniform branch and χ-smeared branch, on this face:** both are subject to this same pointwise bound (see R2-chi).

## 4. Warp mixing, Σ and x, and the UV face

- **R2-warp (CONDITIONAL: algebraic H-bound, ∇∇R and the twist still omitted).** u = v = (1/6) ln Δ̃ + const, so the warp Hessians of the ℝ^{1,3} and Σ blocks coincide. On the MN2 IR grid, max |H|² = 0.3089 and max I_fib = 48.14 (y16 units), hence 6 max|H|² / max I_fib = **0.0385**. Mixed algebraic Riemann of order H therefore corrects I(ℓ_fib) at the few-percent level, and I(t̂) (which enters S(ℓ,ℓ) = −4c(I(t̂)+I(ê))) is of the same order. Warp mixing cannot close a shortfall of a few hundred.

- **R2-Σ (CONDITIONAL: intrinsic H² curvature of Σ only, plus the same omitted terms).** With R_Σ = L₇ e^{g₀} Δ̃^{1/6} ∈ [24.884, 27.884], I(ê_Σ) = 2/R_Σ⁴ gives |S_R|/|S_req| at most **1.442×10⁻⁴ (u = 2)** or 7.209×10⁻⁵ (u = 1), smaller than the fibre ratios. Without warp mixing, I(ê_x) = 0.

- **R2-UV (CONDITIONAL on Q1, c > 0, and on R₄ = L₇/g_c; the integrated Q5 value is PROVED in terms of λ as in Y16).** On the UV end (round S⁴ of physical radius R₄ = L₇/g_c, ρ → ∞), S(ℓ_fib,ℓ_fib) = −24c/R₄⁴ is isotropic, so there is no directional concentration. The pointwise ratio is **6.148×10⁻⁴ at u = 2** (shortfall 1627) and 3.074×10⁻⁴ at u = 1 (shortfall 3253). The integrated supply is −u M5 units against N_req → 10N/3 = 16266.7, a fraction 1.23×10⁻⁴ (u = 2). This is worse than the IR face, as expected from the larger requirement and the absent squash concentration.

## 5. The two χ-branches, C4 faces, and interior faces

- **R2-chi (PROVED, as a statement about the exact-MN2 IR face geometry).** On the exact MN2 IR face, k_x = −Δ̃^{−1/6}/L₅ and the intrinsic fibre and Σ curvatures are properties of the induced 10D metric of that face. They do not depend on the wall source density n(χ). Therefore the **χ-uniform** and **χ-smeared** branches see the same pointwise S_R and the same pointwise S_req on this face. χ-smearing cannot evade a pointwise shortfall that holds everywhere on S⁴.

- **R2-C4 (PROVED, given K4 and k_x > 0; C4 face data, not a bulk solution).** On a breathing C4 face (k_fib = −2k_x, k_Σ = k_x), S(ℓ_fib,ℓ_fib) = −(2/κ²)(k_fib − k_x) = 6k_x/κ² and S(ℓ_Σ,ℓ_Σ) = 0. If k_x > 0, every fibre and Σ null direction already satisfies NEC with no help from tr R² (K4; E18 / 1948). The “needed size” question does not arise for those directions on C4. K4 does not establish k_x > 0 for any actual bulk solution, and “tension = charge” on the twisted S⁴ remains OPEN (E16-F3). This item does not claim a C4 junction.

- **R2-int (OPEN).** Interior CLP faces were not rescanned with a per-direction I(ê). Q8 (the sign of S_R², including ∇∇R, on interior faces) remains OPEN. Two remarks, not a substitute for that computation: (i) Y16 Q7 still applies, so every four-derivative wall term is O(1/N) of the deficit on every face, integrated and (on a smooth face) pointwise up to an O(1) concentration factor; (ii) the IR fibre is the most squashed of the flow (the UV is round, concentration 1), and the I2 margin on interior faces is of the same order as 1/L₅ (Y15-int, min margin 2.01×10⁻² ℓ_P⁻¹). A concentration of order 10²–10³ is not expected. The twist and the ∇∇R terms are not computed here on any face.

## 6. Verdict

Under the computed algebraic fibre-intrinsic part, with a few-percent warp-mixing bound, on the exact MN2 IR face and at the UV end, and for both u = 1 and u = 2:

- The tr R² stress **does** have the needed sign in every fibre direction on the sampled IR grid (R2-sign).
- It does **not** have the needed size in any null direction checked. The best pointwise ratio is 3.5×10⁻³ (u = 2) or 1.7×10⁻³ (u = 1), a shortfall of a few hundred, not a factor of order one. The integrated “~10³ short” of Y15-R2 is slightly pessimistic relative to the best node (286 at u = 2) and remains the right order for the direction-average and for the UV face.
- Both χ-branches are on the same footing on this face (R2-chi).
- **The junction remains UNSOLVED. The count gap is unchanged.** Y15's no-go for E₈ + σ ≥ 0 M5s + the HW tr R² term, IR side kept, is not lifted by passing from the integrated bound to the per-direction algebraic computation. A breathing C4 face with k_x > 0 does not need this term for the null condition (R2-C4), but that is a different face, and no bulk solution is on record.

## 7. Tally (header checked)

| label | count | items |
|---|---|---|
| PROVED | 3 | R2-round, R2-Y16, R2-chi |
| CONDITIONAL | 5 | R2-sign, R2-IR, R2-warp, R2-Σ, R2-UV |
| OPEN | 1 | R2-int (interior ∇∇R / Q8, and the twist on all faces) |
| REFUTED | 0 | — |

Check: 3 + 5 + 1 + 0 = 9. R2-C4 is a restatement of K4 (already PROVED in 1948 / E18) applied to this question, and is not re-counted. The omitted ∇∇R and twist are the reason R2-IR, R2-sign, R2-warp and R2-Σ stay CONDITIONAL, and are part of R2-int's OPEN residual.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
