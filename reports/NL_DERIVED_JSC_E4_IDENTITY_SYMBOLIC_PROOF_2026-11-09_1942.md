# NL DERIVED: closed-form proof of the E4 identity R_rχ = (3/2) β′ ∂_χ ln D̃
2026-11-09, CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED** (19a88b19), unchanged.
Authority: OW 90cec14c. Refers to NL_DERIVED_JSC_BREATHING_MODE_EQUATIONS_MN2_2026-11-09_1935.md (sha ebdda4b6…), items E3, E4, E10. That file is unchanged.
Script: /workspace/nl-jsc-1939/e4_symbolic_proof.py (sha 53104aca…), log e4_symbolic_proof.log (with sidecar).

**Tally: PROVED 3 · CONDITIONAL 0 · OPEN 0 · REFUTED 0 · total 3**

## Setup
The metric is
ds² = D̃^{1/3}e^{2γβ}[e^{2f}(−dt² + dx₁² + dx₂² + dx₃² + dr²) + e^{2g}(du² + dv²)/v²] + ¼e^{2β}D̃^{−2/3}[X_b^{−1}(s²dχ² + c²dΩ₂) + X_a^{−1}(c²dχ² + s²(dφ₁ + a₁du/v)²)],
with D̃ = X_b c² + X_a s², s = sin χ and c = cos χ.

Everything is kept generic and symbolic: X_a, X_b > 0, the twist coefficient a₁, the constant γ, and the functions f(r), g(r), β(r). MN2 is the case X_a = 2^{−3/5}, X_b = 2^{2/5}, a₁ = 1.

## Results
- **P1 (PROVED, exact symbolic computation).** For this metric,
  R_rχ = 3(X_a − X_b) sin 2χ · β′ / (2D̃) = (3/2) β′ ∂_χ ln D̃,
  identically in γ, f, g, β″ and a₁.
  - sympy returns R_rχ − (3/2)β′∂_χ ln D̃ = 0 after simplification. It also returns R_rχ = −3(X_a − X_b) sin 2χ β′ / (X_a cos 2χ − X_a − X_b cos 2χ − X_b), whose denominator equals −2D̃ (runtime 29 s).
  - This agrees with the 40-digit numerics in /workspace/nl-jsc-1905 (ratio 1.5 at 15 points).
  - It also agrees with the SO(5)-singlet case: R_rχ = 0 when X_a = X_b.
- **P2 (PROVED).** If G₄ has no r-leg and g_rχ = 0, then T_rχ = (1/12)(G_{rPQR}G_χ^{PQR} − (1/12)g_rχ G²) = 0. So the rχ Einstein equation in the uniform ansatz reads (3/2)β′ ∂_χ ln D̃ = 0. When X_a ≠ X_b, ∂_χ ln D̃ ≠ 0 on (0, π/2), so **β′ ≡ 0**. This upgrades E4 (1935 file) from CONDITIONAL to PROVED; the condition (a closed-form proof) is now met.
- **P3 (PROVED; upgrades E10).** At the face, C4 requires β′ = −2f′/(1+2γ), which is nonzero because k_x > 0 (for γ ≠ −½; at γ = −½ C4 has no solution at all). By P2, β′ = 0. So on MN2 the C4 breathing face closure **cannot be realized in the uniform-breathing ansatz**, for any γ.

## Notes
- The 1935 file's E4 sentence "The condition is a closed-form proof of the identity, which has not been done" meant that the claim was conditional on such a proof. This file supplies it.
- E3 (REFUTED) is unchanged. P1 is the general form of its counterexample.
