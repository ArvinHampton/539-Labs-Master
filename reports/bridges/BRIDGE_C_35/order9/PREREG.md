# PREREG: order9. Full unit-arc test: Θ_E + γ(Θ_E) vs 𝓗(Φ₀)
Written 2026-10-24, about 3:48 PM CDT (America/Chicago), before any order9 computation. Owner: Arvin Hampton.
Parents: order5–order8 (read-only; order8 m1.py weight routine copied, order5 lib5mp imported read-only). New files only. CORE_FREEZE. Category A = proof/exact; B = numerical. nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No push/sends. No interior float span tests.

## 0. Geometry (Category A, finite algebra, written before numerics)
γ = [[−1,−7],[2,13]] (unit 6+√35, γᵀAγ = A), γ⁻¹ = [[13,7],[−2,−1]], improper automorph σ = [[1,7],[0,−1]] (fixes e1, Q(σv) = Q(v)).
Negative lines ↔ positive orthogonal directions: c1^⊥ = e2, c′^⊥ = e1, (γc1)^⊥ = γe2 = (−7,13), γe1 = (−1,2), γ⁻¹e2 = (7,−1).
Hyperbolic angles (cosh = B/(2√(Q Q))): ∠(e1,e2) = ∠(e2,γe1) = ∠(γe1,γe2) = L = ½log(6+√35); ∠(e2,γe2) = 2L = log(6+√35).
Ordering in the positive cone component: (7,−1) – e1 – e2 – γe1 – γe2. Hence the unit arc [ĉ1, γĉ1] ↔ positive cone C_arc = cone(e2, γe2) = cone(e2,γe1) ∪ γ(orth), with cone(e2,γe1) = σ₂(orth) for the reflection σ₂ fixing e2. **The orthant itself is NOT inside C_arc.**
Consequence by the order8 Laplace map: 𝓗(Φ₀) = Θ_{C_arc} := Σ_{ν∈±C_arc} w(ν) e(Q(ν)τ+B(ν,β)), w = 1 inside, ½ on the two edge lines.

## 1. Predictions (coefficient identities, mpmath dps 25, N ≤ 8, all 105 companions, y = 1e4/2e4 linear extrapolation in 1/y as order8 M1)
- **U1 (Arvin's statement as given):** c_{𝓗Φ₀}(N) = c_E(N) + c_{γE}(N), with c_{γE}(N) = Σ_{ν∈α+Z², γ⁻¹ν∈±orth} EVEN(γ⁻¹ν)e(B(ν,β)). **Predicted: FAIL** (geometry §0: orth ⊄ C_arc). Fail if max diff > 1e−4.
- **U2 (corrected):** c_{𝓗Φ₀}(N) = c_{C_arc}(N) (edge weights ½). **Predicted: PASS** (≤ 1e−7).
- **U3 (Hecke completeness, descriptive identity):** for companions whose coset and twist are γ-invariant (γ(α+Z²) = α+Z² and e(B(γν,β)) = e(B(ν,β))), c_{C_arc}(N) = Σ over ⟨γ⟩-orbits of {ν: Q(ν)=N} of e(B(ν,β)) (each orbit once). Pass ≤ 1e−10 (exact enumeration); companions not γ-invariant are listed.
- Also reported: L_arc = arccosh(−B(ĉ1,γĉ1)/2) vs log(6+√35) (Category A check, ≤ 1e−20).

## 2. Radial tests (rational points, t-grid scaled with denominator)
Fit model for every radial test: S(t) = Σ_{i} c_i t^{e_i}, e = {−1, −½, 0, ½, 1, 3/2, 2} (7 terms), on t_j = 2^{−j}·0.02/(2m)², j = 0..7 (8 points).
- **R1 (order8 M2c with the corrected fit):** Θ_E at x ∈ {1, 1/3, 1/4}, 4 generic companions (as order8): A0, A1, A2 vs the order3c formula on the two shifted orthant pieces (A0 also = mean f·2L/√35). Pass ≤ 1e−5·max(1,|pred|) for all; fail > 1e−3; else inconclusive.
- **R2 (unit arc, A0):** Θ_{C_arc} brute force at x ∈ {1, 1/3}, same 4 companions: A0 vs √(2/π)·lim t^{1/2}Φ₀ = mean f·2·(2L)/√35. Pass ≤ 1e−6·max(1,|pred|). A1, A2 descriptive only (no lib decomposition for the index-7 cone C_arc).

## 3. Verdict rule
- U1 verdict as measured (predicted FAIL). If U2 passes: "𝓗(Φ₀) is the complete Hecke-type cone sum over C_arc = σ₂(orth) ∪ γ(orth)".
- ξ-shadow of the full series is "located" only if a modular object (fixed law) is obtained for the even piece; 𝓗 is non-equivariant, so U2 alone does NOT locate it. Expected: not located.
