# NL DERIVED: Y14 stage 1. Non-BPS E₈ fields on the weighted MN2 fibre (equivariant reduction, weighted criticality, end-face numerics)
Author: Non Local Path (NL). Everything below is an **NL derived proposal**.

Authority:
- OW 9bb1858c (pursue Y14, Y15 and Y16).
- OW 19a88b19: MN N=2 is the adopted working vacuum, CONDITIONAL. NL adopts nothing further.
- OW 36683379, amending 3f160803: any source may be cited, with the math verified; a citation alone never makes a claim PROVED.
- PP 149be02a and c74b5a2d: B-PP2 is assessed here in §4, and u = 1 vs u = 2 in §7.

Limits: No source or b adopted. No CERT. No Gemini; nothing sent outside. Tip 7cddb188 untouched.

Usage: 45.9% at the start and 48.1% at the halfway point.

Scripts, with sidecars, in /workspace/nl-junction-1819/:
- y14bvp.py (9d7d9ada…) and y14bvp_run.log (3b424091…)
- y14trend_small.py (1fa09e66…) and y14trend_small_run.log (31d84e7e…)
- Superseded, kept rather than overwritten:
  - y14.py and y14_run1.log: an L-BFGS run that stopped at iteration 0 because ftol was set too tight. Its energies are void.
  - y14trend.py and y14trend_run.log: killed while still running; the log is empty.

## 1. Reduction
- **S1 (PROVED).** At the MN2 IR fixed point, X₀ = X₂ = X_b = 1.319508 and X₁ = X_a = 0.659754. So the fibre ĝ = X_b⁻¹|dy_{ℝ³}|² + X_a⁻¹|dy_ℂ|² on S⁴ ⊂ ℝ³ ⊕ ℂ, and the weight W = Δ̃ = X_b cos²χ + X_a sin²χ, are invariant under SO(3) × U(1)_{φ₁}. That is MN2's SU(2)_R × U(1)_R.
  - The action has cohomogeneity 1. Generic orbits are S² × S¹; the singular orbits are an S² at χ = 0 and an S¹ at χ = π/2. **There are no fixed points.**
- **S2 (PROVED).** ĝ = R²(g_B/R² + dΩ²) with R² = X_b⁻¹cos²χ. By 4D conformal invariance, the weighted YM problem moves to B̃ × S² with B̃ = (B, g_B/R²).
  - For the round fibre, B̃ is the hemisphere model of H²: in t with cos χ = sech t, g̃_tt = 1 and g̃_φφ = sinh²t.
- **S3 (CONDITIONAL; Witten 1977 ansatz cited; math checked only through the round validation in S8).** In the SO(3) ansatz the energy reduces to an abelian-Higgs functional on B̃:
  - e = ∫_{B̃} W[½f² + |Dφ|² + ½(1−|φ|²)²] dA/(2π), in units of 8π² (one instanton = one M5 unit).
  - With U(1)_{φ₁}-equivariance, φ = h(t)e^{inφ₁} and a = a(t)dφ₁, giving a radial ODE.
  - Weighted Bogomolny bound: e ≥ nW_min.
- **S4 (PROVED, formal; Palais-type argument written out).** Take a G-invariant functional with an invariant inner product, G = SO(3) × U(1) compact.
  - At an invariant critical point of the reduced functional, the full gradient is itself G-invariant and orthogonal to every invariant direction. So it is zero.
  - Hence reduced critical points are critical points of the full weighted problem D(W⋆F) = 0. This assumes the Sobolev setting in which the gradient exists.
- **S5 (PROVED). On the twisted MN2 face, the stage-1 model is incomplete.**
  - A static field that is the same on every fibre must be U(1)_{φ₁}-equivariant, because φ₁ is the twisted circle.
  - If its moment map Φ vanished, F would be basic, F∧F would contain no dφ₁, and the charge would be 0. So **charge k ≠ 0 forces Φ ≠ 0.**
  - F then has Σ legs Φ·π*F_tw, which add positive energy and Σ stress. **Stage 1 omits this term.** Every numerical result below is CONDITIONAL on stage 2 including it.
- **S6 (CONDITIONAL, sketch).** The group has no fixed points, so equivariant minimizing sequences cannot bubble off at a point; concentrating on an orbit costs unbounded energy. The equivariant direct method should therefore give a minimizer in each charge-n sector.

## 2. End-face numerics (Euler–Lagrange BVP, solve_bvp, tolerance 10⁻⁸)
- **S8 (PROVED as validation).** On the round fibre with constant W, which is the UV end face:
  - e = 0.9999985 (n = 1) and 1.9999995 (n = 2), against the exact n.
  - The weighted Bogomolny defect is 2.6×10⁻¹⁹. In this sector the UV end has BPS solutions only.
- **S7 (CONDITIONAL; stage-1 model, twist term omitted).** On the MN2 IR end face, reached by continuation from the round solution, the BVPs converge (status 0) and are unchanged at T = 20:

| n | e/n | weighted Bogomolny defect | (e/n)/⟨W⟩_phys | (e/n)/W_min |
|---|---|---|---|---|
| 1 | 1.112874 | 0.0210 | 1.080 | 1.687 |
| 2 | 0.990040 | 0.0563 | 0.961 | 1.501 |
| 3 | 0.914978 | 0.0820 | 0.888 | 1.387 |

  - The defect is nonzero, compared with 10⁻¹⁹ on the round fibre. So these are **non-self-dual static critical points**, i.e. non-BPS E₈ fields, consistent with Y6.
  - ⟨W⟩_phys = 1.0301, averaged with the physical fibre measure.
  - An n = 5 run did not converge and is not used.

## 3. Existence status
- **Y14 (CONDITIONAL; S4 + S6 + S7). Non-BPS static E₈ fields exist on the MN2 IR end face in the stage-1 model,** for n = 1, 2, 3 in a single SU(2) ⊂ E₈.
  - They are weighted minimizers within their equivariant class.
  - Two things stop this being PROVED: the twist coupling (S5) is omitted, and S6 is only a sketch. Y14 stays **OPEN**.

## 4. PP's B-PP2 (an instanton in one SU(2) plus an anti-instanton in a commuting SU(2))
- **S9 (PROVED).** On the weighted fibre each commuting block must solve D(W⋆F) = 0 separately. Y6's rank-3 argument kills an anti-self-dual block exactly as it kills a self-dual one: an ASD 2-form also has F∧v = 0 only for F = 0.
  - **Both pieces of the round-S⁴ B-PP2 configuration are killed**, so it does not survive on the weighted fibre.
- **S10 (CONDITIONAL on S7). The weighted replacement does survive.**
  - Put the charge-n₁ weighted solution in block 1. Put the charge-n₂ solution pulled back by φ₁ → −φ₁ in block 2; that map is an orientation-reversing isometry that preserves W, so block 2 has charge −n₂.
  - This gives static non-BPS solutions for every total charge n₁ − n₂, including charge 0 with energy e(n₁) + e(n₂) > 0.
  - It needs SU(2) × SU(2) ⊂ SO(4) ⊂ SO(16) ⊂ E₈ (CONDITIONAL; cited, math not yet checked).

## 5. Effect on the gap and the junction
- **S11 (CONDITIONAL; S10 and the stage-1 model). In magnitude, the count gap can be closed.**
  - Each zero-charge n = 1 pair adds 2.2257 units of tension. The MN2 excess (2808.6, 6506.7) needs between 1262 and 2923 pairs.
  - The result is in instanton units, which equal M5 units by anomaly matching. It does not depend on u.
- **S12 (CONDITIONAL).** Single-block minimizers alone do not close the gap: (e/n)/⟨W⟩_phys = 1.080 → 0.888 and falls with n, below the needed 1.288.
- **The junction is unchanged.** The fibre NEC still fails, for every E₈ field (1800 Y3-ineq, PROVED). Whether the pairs' traceless fibre stress can match the fibre Israel equations is **Y15 (OPEN)**.

## 6. Cross-checks with MR2
- **S13 (PROVED, arithmetic and determinant identity).** MR2's horizontal-measure value 1.2876 equals NL's MN2 IR endpoint 1 + 2808.6/9760 = 1.28777 to 2×10⁻⁴. The exact fixed-point face is the open end of NL's interval.
- **S13r (REFUTED as a physical measure).** MR2's fixed-φ value 1.0316.
  - det g₆ = det(horizontal)·det(vertical) holds exactly, because the basis change (dσ, dφ) → (dσ, dφ + A) is unimodular.
  - Dividing instead by the coordinate Σ entries g₅₅g₆₆, which contain the gauge-dependent A₁² twist terms, gives a gauge-dependent N_req. Only the horizontal measure is gauge-invariant.
  - The numerical closeness of 1.0316 to ⟨W⟩_phys = 1.0301 is noted and not interpreted.
- **MR2 C3, the φ₂ → −φ₂ Z₂ (bd47ff5e; not adopted):**
  - **S14a (PROVED).** With a₂ = 0 the metric depends on φ₂ only through dφ₂². The reflection is an orientation-reversing isometry. Its fixed set {φ₂ ∈ {0, π}} ∪ {μ₂ = 0}, i.e. AdS₅ × Σ × S³, is totally geodesic.
  - **S14b (PROVED).** It is not the radial matching face (f283cffd). It leaves the constant-r face's K ≠ 0 and the fibre-NEC deficit untouched, so it does not affect the junction.
  - The G₄ parity relies on MR2's component list, which NL has not re-derived (CONDITIONAL, folded into S14c).
  - **S14c (OPEN).** Its E₈/anomaly content on the S³ wall, and flux quantization on S⁴/Z₂ (N_flux = 4880 is even).

## 7. Normalization u (PP-1)
- **S16 (PROVED).** Y14 energies are in instanton units, and u enters only the R² term (Y16). So none of S7–S12 depends on u.
  - Under u = 1 (Conrad hep-th/9708031, Lü hep-th/9711014; CONDITIONAL), the Y16 numbers halve (erratum 14).

## 8. Next stage and ETA
- **Stage 2 (OPEN, S15):**
  - Add the twist term Φ·F_tw to the reduced functional (about 1 h).
  - Mountain-pass search for charge-0 saddles within a single block (about 1.5 h).
  - Interior flow faces (about 1 h).
  - Second variation, to test stability (about 1 h).
- **Y15:** match the pair configurations' fibre and Σ stress against the 1711 Israel templates. About 2 h after stage 2.

## Tally (header checked against the item lists)
| label | count | items |
|---|---|---|
| PROVED | 10 | S1, S2, S4, S5, S8, S9, S13, S14a, S14b, S16 |
| CONDITIONAL | 7 | S3, S6, S7, S10, S11, S12, Y14-existence (stage-1 model) |
| OPEN | 2 | S14c, S15 (stage 2: twist, mountain pass, interior, stability) |
| REFUTED | 1 | S13r (fixed-φ measure) |

Check: 10 + 7 + 2 + 1 = 20. Y14 overall stays OPEN pending stage 2; it is counted once, as the stage-1 CONDITIONAL row.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
