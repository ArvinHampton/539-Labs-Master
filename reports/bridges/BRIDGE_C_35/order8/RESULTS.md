# order8 results: linking the P-even even piece Θ_E to weight-0 Siegel objects
PREREG sha256 13b9df4f…f6d1 (unchanged). Script hashes: scripts/SHA256SUMS. No interior float span test is used as evidence. The only interior test is M3, a fixed-matrix residual with one free scalar, the same design as order5 Z. Deviations are in NOTES.md, and the verdicts below are the preregistered ones.

## Category A (derived; sketches flagged)
- **Orthant angle.** The hyperbolic angle of the orthant between ĉ1 and ĉ′ is L = arccosh(7/(2√3.5)) = ½·log(6+√35). The two agree to 20 digits (mp), so the orthant is exactly half of the unit-group fundamental angle.
- **Map 𝓗.** M1 uses 𝓗 = D^{1/2} ∘ (y→∞ projection). The Laplace derivation of Θ_E = 𝓗(Φ_orth) is a *sketch*.
- **Radial expansion of Φ_orth (Poisson).** t^{1/2}Φ_orth = (2π)^{−1/2}(2π/√35)·L·mean f + O(t^∞).
- **Character twist (S² algebra).** Under ρ_L ⊗ χ with χ(S) = ±i, the weight-1 law forces P-even. This is the P-altering candidate.

## Category B (numerical)
| map | test | statistic | verdict |
|---|---|---|---|
| **M1**: Θ_E = 𝓗(Φ_orth), coefficient-wise | 105 companions, all N ≤ 8, mp dps 25, y = 1e4/2e4 extrapolated | max \|c_Φ − c_E\| = 8.7e−10 | **pass** |
| **M2b/M2a**: t^{1/2}Φ_orth is constant and equals the Poisson constant | x = 1 and ½, 2 companions, t = 2e−3 … 5e−4 | constancy 2.5e−14; vs prediction 4.3e−14 | **pass** (x = ½ is degenerate: mean f = 0) |
| **M2c**: radial A0, A1, A2 of Θ_E vs prediction (A0 from Φ via √(2/π); A1, A2 = edge/corner formula of the two shifted orthants) | x ∈ {1, ½, ⅓}, 4 companions, preregistered 6-point grid, 5-term fit | A0 err ≤ 3.5e−8; A1 err ≤ 1.4e−5; A2 err 2.1e−5 … 9.5e−4 | **FAIL** (threshold 1e−5) |
| **M3**: twisted law Θ_E(−1/τ) = c·(τ/√35)·M·Θ_E(τ), with c = ±i required | 660 τ, fixed M, free scalar c | c* = 0.001 + 0.080i, r = 0.54 | **FAIL** (as predicted) |
| M3: same for the product-completed Ê | | c* = 0.002 − 0.701i, r = 0.375 | **FAIL** (as predicted) |
| M3 control: Ĥ | | c* = 1.000, r = 7.5e−16 | pass |

**Post-hoc check of M2c (descriptive, not a verdict; NOTES 1).** I refit with 8 t-points and terms up to t². At x = 1 the max error is 3.7e−7, and at x = ⅓ it is 5.2e−6. This suggests the M2c failure comes from the under-resolved preregistered fit, not from the prediction. The recorded verdict remains FAIL.

## Verdicts
- **M1 holds (Category B, Category A sketch).** The even double-orthant is exactly the image of the modular weight-0 Siegel object Φ_orth = ∫_{ĉ1}^{ĉ′}Θ_z dμ under 𝓗 (the half-derivative of the holomorphic projection). Φ_orth obeys the fixed weight-0 law (1/√35)·M of the 35-component law vector. 𝓗 is not modular-equivariant, so this is a mixed, non-modular link.
- **M2:** the Φ side passes. The Θ_E radial comparison **FAILS** at the preregistered resolution.
- **M3 (character twist / P-altering):** **FAILS.** Neither Θ_E nor Ê is modular under ρ_L ⊗ χ.
- **Full-series shadow (ξ-sense): NOT located.** By the preregistered rule, the even piece is identified as 𝓗(Φ_orth) (non-modular link), but the ξ-shadow of the full series is not located.
