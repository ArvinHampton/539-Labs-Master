# NL DERIVED — D6: nonlinear (r,χ) Killing-spinor search for χ-dependent finite-amplitude BPS ℤ₂ walls on Bolza (CHECKPOINT PARTIAL)
2026-11-09, 2100 CST (America/Chicago). **NL derived proposal.** Additive only. Authority: OW t4426 d5eaeef3. The usage stop is lifted (OW t4431). Nothing adopted. **Junction: UNSOLVED. Count gap: unchanged.**
**Status: clean partial at a checkpoint.** The full nonlinear (r,χ) PDE solve outside the 5D truncation has **not** been done (D6-8). This file records what is settled so far.
Inputs:
- NL_ERRATUM20_ACCEPT_PP_8c57e68b_0a82cf18_2026-11-09_2056.md (6b10854d…)
- E19 (d3dd5a4c…)
- 2017 B12 file (f8801bff…)
- PP 0a82cf18 (Z1, Z2)
- CGR arXiv 1906.08900 (2.5), (2.6), (3.1), (3.3), (5.15), (5.16). Their math was re-checked where it is used here.

Scripts in /workspace/nl-bps-d6-2057/. **Each .py sidecar was frozen before its run.**
- z2_centre_flow_faces.py: 21bcbc3f…
- z2_scan_wide.py: 2b13a81b…. It crashed on non-real initial data; the partial log is kept.
- z2_scan_v3.py: 80fad08e…. This is the guarded rerun.

Logs were sealed after the runs. Limits: no CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… checked before and after.

**Tally: PROVED 4 · CONDITIONAL 2 · OPEN 2 · REFUTED 0 · total 8.**

> **No candidate wall found.** No NEC-respecting face was found in the Z2 scan. No obstruction to D6 was found either. D6 remains OPEN.

## 1. Wall-local algebra (11D HW-BPS, D1)
- **D6-1 (PROVED).** Decomposition of the bulk x-equation (F1).
  - On a warped product with flat x-directions, the x-row of the 11D KSE is ∂̸Aε = −(1/144)G̸ε, where G̸ runs over the 7 internal directions including n.
  - Take the sum and difference of the two wall sides with ε odd (Γ_nε = ε) and G odd. This gives the D1 x-row and the parallel relation ∂̸_∥Aε = −(1/36)Γ^nH̸ε, with H̸ = Γ^{bcd}G_{nbcd}.
  - In particular, a χ-dependent warp A(χ) at the wall requires H (the normal-leg flux) to be nonzero at the wall.
- **D6-2 (PROVED; analytic).** Classification F2 under SO(3) invariance and H_Σ.
  - Take joint eigenvalues Γ^{Σ12} = is₁, Γ^{χν} = is₂, Γ^{θφ} = is₃ and Γ^nε = ε. Wall data: f₄ = G_{χνθφ}, ω₁ = G_{Σ12χν}, ω₂ = G_{Σ12θφ}.
  - Define α = σs₂s₃f₄, β₁ = σs₁s₂ω₁, β₂ = σs₁s₃ω₂.
  - Then **k_x = (α+β₁+β₂)/6**, with M = K − k_x·1 given by:
    - M_ΣΣ = −(β₁+β₂)/2;
    - M_χχ = M_νν = −(α+β₁)/2;
    - M_θθ = M_φφ = −(α+β₂)/2;
    - M_χν = 0.
  - Derivation:
    - G̸ε = 24(−s₂s₃f₄ − s₁s₂ω₁ − s₁s₃ω₂)ε gives k_x.
    - For a = Σ₁, the term 12Γ_aΓ^{cde}G_{acde} = 72Γ^{Σ12}(ω₁Γ^{χν} + ω₂Γ^{θφ}) gives the extra −(β₁+β₂)/2.
    - For a = χ, the terms Γ_χΓ^{νθφ} → Γ^{χνθφ} and Γ_χΓ^{Σ1Σ2ν} → +Γ^{Σ12}Γ^{χν} (an even number of swaps) give the extra −(α+β₁)/2.
    - θ is analogous.
  - Consequences:
    - **NEC ⇔ β₁+β₂ ≥ 0, α+β₁ ≥ 0, α+β₂ ≥ 0.**
    - The D5 sign is NEC-compatible ⇔ β₁+β₂ ≥ 0.
    - k_x ≥ 0 follows from the NEC conditions.
  - Physical reading: calibrated M5 sheets on x×Σ (α), x×S²_{θφ} (β₁) and x×(χν) (β₂). β < 0 means a negative-tension constituent.
- **D6-3 (PROVED).** Wall-local algebra alone does **not** forbid an NEC-respecting HW-BPS wall.
  - Example: α = β₁ = β₂ = b > 0 gives k_x = b/2 > 0, M = −b·1 on all six directions, and k_Σ − k_x = −b. This is D5 with +σ/2 and the NEC-compatible sign.
  - D2 then holds: K_int = 6(k_x − b) = −6k_x requires b = 2k_x ✓, consistent.
  - This shows only that the local data are consistent. It is not a wall.
- **D6-4 (CONDITIONAL).** F4 twist charge. Take C₄ = {μ_a = 0} ≅ Σ×S², the χ = π/2 locus.
  - On C₄ only the twist term of CGR (2.6) survives. Bulk Bianchi then makes ∫_{C₄}G constant across the kept side.
  - Hence the odd ℤ₂ wall carries a **non-zero ω₂-charge 2Φ_tw, with sign ∝ l**.
  - **Condition:** no other sources meet C₄ on the kept side, and C₄ stays a non-degenerate cycle (smooth kept side).
  - Consequence: β₂ ≠ 0 at the wall, and its sign is η·|β₂|.
- **D6-5 (OPEN).** The decisive sign η = sgn(σs₁s₃Φ_tw), i.e. the HW spinor's s₁s₃ relative to the flux orientation, is undetermined without the bulk Killing spinor.
  - If η = +1, D6-3-type data are available.
  - If η = −1, the NEC needs α ≥ |β₂| and β₁ ≥ |β₂| (still allowed locally), i.e. more calibrated α/β₁ charge. Then the tadpole N_M5 + n_inst = 9760 must absorb it.

## 2. Z2 centre-manifold kept sides (w included; E20-6)
- **D6-6 (PROVED; analytic).** Slow manifold and its one-sidedness.
  - With ∂³_wV = −24·2^{2/3}g² and no Hessian mixing, the w equation w'' + 4A'w' = G_ww⁻¹∂_wV, with A' → −1/L, reduces on the slow manifold to w' = c·w², c = 2^{2/3}g²L (= 2.5198 at g=1).
  - Hence **w ≈ −1/(c(r−r₀)) → 0⁻ as r → +∞**. Only the side w < 0 creeps into MN2; w > 0 runs away in the IR.
  - The slaved (φ,λ) shift is O(w²): (δφ, δλ) = (0.2, 0.4333)·w² at g=1, from the script.
- **D6-7 (CONDITIONAL; numerical).** No NEC-respecting face in the scanned Z2 family.
  - Family: second-order three-scalar flows (G = diag(60,60,3), Hamiltonian constraint, A' < 0), started on the approximate slow manifold with Δ6 admixture d₆ along (−3:1). There were 48 real flows:
    - w₀ ∈ {−0.01, −0.03, −0.1, −0.3};
    - d₆ ∈ {−0.30, …, +0.10};
    - d₆ ≥ 0.15 has no real A' and was skipped.
  - Each flow was integrated toward the UV, and faces were sampled at 80 + 40 points (denser near the end).
  - 11D face data come from the uplift with w on: Δ = e^{−6λ}cos²χ + sin²χ e^{4λ}(e^{w}sin²θ + e^{−2w}cos²θ), and the fibre shape operator is ½ε g⁻¹∂_r g on (χ,θ,ν,ψ).
  - Results (z2_scan_v3.log):
    - **The worst-direction NEC margin max_v(k_v − k_x) stays positive on every face.** Its minimum over all faces and flows is **+0.431**, always set by a fibre direction.
    - Large negative d₆ makes k_Σ − k_x < 0 on some faces (down to −1.93), but the fibre still fails.
    - The D2 trace |K_int + 6k_x|/|k_x| gets close to zero at single grid points only for w₀ = −0.3 (min 0.010). It is never zero at every point of S⁴, and the NEC fails at those faces anyway.
  - **Conditions:** float accuracy; the initial data are only approximately on the centre manifold (an O(w²) slaving that is crude at w₀ = −0.3, so IR regularity at large |w₀| is not verified); a 9×7 grid in the (χ,θ) quadrant, using the ν and ψ rotation symmetries and reflections; finite scan ranges.
  - A finite scan cannot make this PROVED.
  - **Z2 verdict: OPEN** (E20-6 stands), with numerical evidence against NEC-respecting Z2 faces in the 5D truncation.

## 3. The nonlinear (r,χ) problem proper
- **D6-8 (OPEN).** A genuinely χ-dependent finite-amplitude wall needs a bulk that depends on (r,χ) **outside** the 5D consistent truncation.
  - Every truncation flow, W-flows and Z2 centre flows alike, gives χ-dependence only through Δ(χ). Within the truncation that family fails the 11D NEC (D3, D6-7) and never meets D2 at every point.
  - The natural setting is the BPS system of M5s on Σ with an extra (r,χ) dependence. Its AdS₅ limit is the LLM / SU(∞)-Toda class.
  - The required system: D2 at every point of S⁴, k_x ≥ 0, D5 with +σ/2 and NEC-compatible (β₁+β₂ ≥ 0) or an NEC-violating source, and Y15's k_v ≤ k_x on the kept side, with the kept side including the w direction and Z2.
  - This system was **not set up or solved** in this checkpoint.
  - **D6 verdict: OPEN in both branches.**
    - [χU] (χ-uniform, P = 2/5): a χ-uniform source must meet D2 pointwise against a face whose k_x carries Δ(χ)-dependence. Inside the truncation this fails (D6-7), and outside it, it is OPEN.
    - [χS] (χ-smeared, any n(χ) ≥ 0): the wall-local algebra (D6-2, D6-3) allows it, but bulk existence and η (D6-5) are OPEN.
  - Next steps: (i) fix η from the bulk MN2 Killing spinor projections (CGR §3) restricted to C₄; (ii) set up the (r,χ) BPS PDE as a deformation of the LLM-Toda data and test the D2 and NEC boundary conditions.

## 4. Impact
- No candidate wall was found, and no new no-go was proved.
- Gap: unchanged. Junction: UNSOLVED.
- The escape register is unchanged; D6 and Z2 stay OPEN.

## 5. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 4 | D6-1, D6-2, D6-3, D6-6 |
| CONDITIONAL | 2 | D6-4, D6-7 |
| OPEN | 2 | D6-5, D6-8 |
| REFUTED | 0 | — |

Check: 4 + 2 + 2 + 0 = 8.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
