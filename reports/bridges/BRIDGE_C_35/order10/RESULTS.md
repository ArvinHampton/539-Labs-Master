# order10 RESULTS: Laplacian of the weight-0 Siegel lift Φ₀ on the unit-arc boundary rays
Prereg: PREREG.md, sha256 f5d2213d…c24e in PREREG.sha256, written before any numerics. Scripts are hashed in scripts/SHA256SUMS.

## Theorem (Category A, derived in PREREG §1 before numerics)
Δ₀Θ_z = ¼Θ_z − ¼∂_μ²Θ_z, therefore
**(Δ₀ − ¼)Φ₀ = (π/2)·y^{3/2}·[B(γĉ1) − B(ĉ1)]**,
with B(ĉ1) = √140 · ϑ⁺(τ) · conj(ϑ⁻(τ)). The orientation sign is +1 (measured).
- ϑ⁺ = Σ_{m∈α1+α2+Z} m·e(7m²τ/2 + 7(b0+b1)m): weight-3/2 holomorphic, on the ray e2.
- ϑ⁻ = Σ_{u∈α1+Z} u·e(5u²τ/2 + 5b0·u): weight 3/2, the 5n²/2 series, on the negative line c1.
- The γĉ1 endpoint (ray γe2) has the same form with α → γ⁻¹α.

## Verdicts (Category B numerical confirmation, mpmath dps 30)
| Test | Result | Verdict |
|---|---|---|
| D1: per-Fourier-mode identity, \|N\| ≤ 8, y ∈ {½, 1, 2}, 18 companions | max relative error 7.1e−30 | **pass** |
| D2: exact factorisation into ϑ⁺·conj(ϑ⁻), 3 τ | 1.0e−30 | **pass** |
| D3: characteristics (exact rationals) | the γ-end 5n²/2 characteristics (γ⁻¹α)_1 mod 1, up to sign, lie in the same set of 10 classes as α1 | **pass (exact)** |
| D4: γ-invariant companions have zero defect | 8.5e−7, inconclusive by the preregistered rule | **inconclusive** |
| R1′: Θ_E at x = 1/4, 9 terms on 12 points, dps-40 least squares | max error 1.4e−7 | **pass** |
| R2′: Θ_{C_arc} A0 at x = 1/4 | 6.3e−12 | **pass** (Lemma-2 type, descriptive, not counted) |

**D4 note.** The preregistered rule gives inconclusive. A post-hoc rerun (d4posthoc.py, descriptive only) used the full Q-shell (box 200 instead of 14) and got ≤ 1.0e−29 for all 15 γ-invariant companions. This shows the shortfall was a box-truncation artefact: γ moves shell points outside a 29×29 box. With the full shell, the γ-invariant companions are pure Δ = ¼ eigenforms.

**R1′ settles order9's x = 1/4 inconclusive** as a fit-resolution artefact; the order9 verdict stays recorded as inconclusive.

## Shadow verdict (preregistered rule)
- The boundary terms are located exactly (Category A, confirmed Category B). They are products y^{3/2}·ϑ⁺·conj(ϑ⁻) of two weight-3/2 unary thetas at each ray.
- **The even-piece and full-series ξ₁-shadow is NOT located.** Φ₀ is a weight-0 Δ = ¼ object with boundary, not a weight-1 completion of Θ_E.
- The antiholomorphic factor ϑ⁻ is the 5n²/2 series again. The distinct weight-3/2 unary series in the ξ-sense therefore stay **three** (5n²/2 shared; plus R²/34 and 35m²/4).
- The new ingredient is the weight-3/2 holomorphic partner Σ m·e(7m²τ/2). It appeared before only as the weight-½ θ_{7/2}.
- Θ_E = 𝓗(Φ) remains an identification, not a bridge. M² = 35·P is exact (Category A, order9 cyclo).
