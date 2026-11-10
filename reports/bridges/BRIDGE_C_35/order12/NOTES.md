# order12 RESULTS: Route A (χ = ±i with h) and Route B (|τ|-type weight (½,½))
Prereg: PREREG.md, sha256 221068a4…95a5, written before any numerics. Script hashes are in scripts/SHA256SUMS. Data: data/{a,b,b3,b3x}.json. Logs: logs/.

## Route A: Θ_E + h under the χ = ±i law, h in the span of 82 definite binary thetas (det 35), mpmath dps 25
- **A1 (individual, descriptive).** None of the 82 Θ_{A'} realises M at weight 1 for any χ. Residuals are 0.61–2.3 for all χ ∈ {±1, ±i}.
- **A2 (solve, 82 unknowns, 420 equations).** χ = i: r = 0.18 (holdout 0.15). χ = −i: r = 0.30 (holdout 0.23). **FAIL by the preregistered rule** (≥ 1e−4). h = 0 had already failed (order8 M3, order11).
- Disclosure: A1 shows that this basis contains no M-covariant vector. The A2 FAIL therefore excludes this preregistered basis only. It does not exclude a definite lattice whose discriminant form matches A in the companion coordinates, because none of the 82 does.

## Route B: law G(−1/τ) = |τ|(1/√35)MG(τ)
| Test | Result | Verdict |
|---|---|---|
| B1: Ψ₀ = y^{−1/2}Φ₀, dps 20, 40 GL nodes, box 12 | residual 4.9e−6 | **inconclusive** by rule (pass ≤ 1e−12, FAIL ≥ 1e−4); the 1e−6 level is consistent with quadrature/box error, but this is not shown |
| B2: y^{1/2}Θ_E | residual 1.00 | **FAIL, as predicted** (the Category A obstruction: holomorphic cannot obey the |τ| law) |
| B3, float64 leg, 11 x | \|x\| law residual 1e−10 to 7e−10 | **inconclusive** by rule (floor of float64 sums of N² ≤ 4.9·10⁵ terms) |
| B3, preregistered high-precision leg (b3x: exact integer phase reduction, longdouble) | \|x\| law 6e−19 to 1.2e−18 at x = 1/2, 1/3, −1/2, −1/3 | **pass** |
| B3, signed x^{−1} law at x < 0 | residual 2.0, at all 6 negative evaluations (both legs) | **FAIL**, which discriminates: the leading P-even sector law is sign-blind \|x\| |

- New content: the \|x\| law at x < 0 and on all 105 components. For x > 0 it is parent Theorem 3, so those points are a consistency check only.
- Route B "holds" per the preregistered rule only partly: B3 passes and B2 fails as predicted, but B1 is inconclusive.

## Shadow (success criterion), stated sharply
- **Lemma O (Category A).** A fixed weight-1 law with χ = ±1 forces P-odd; χ = ±i forces P-even. The full series has both parities, so **no single scalar-χ weight-1 law, and so no single ξ₁-shadow, exists for the full series.** It splits:
  - **P-odd sector: ξ₁-shadow located** (order5/order6, Category B confirmation of Category A derivations). It consists of the three distinct weight-3/2 unary thetas Σn e(5n²τ/2) (shared by the cone and the odd orthant), Σ R e(R²τ/34) and Σ m e(35m²τ/4), paired with θ_{7/2}, θ_{35/34}, θ_1. The axis half-lines are quantum only.
  - **P-even sector:** no holomorphic or ξ₁ completion under the χ = ±1 law (Category A), and none under χ = ±i in the tested basis (Category B). Its law is the |τ| weight-(½,½) law (B3 exact radial pass; B2 Category A). Its defect is the Laplacian one from order10, (Δ₀ − ¼)Φ₀ = (π/2)y^{3/2}[√140·ϑ⁺·conj(ϑ⁻)]_{ĉ1}^{γĉ1}. **The "shadow" of the P-even sector is therefore the conj(ϑ⁻) = 5n²/2 factor carried by ϑ⁺ = Σ m e(7m²τ/2) at weight 3/2**, which is a Δ-defect, not a ξ₁-image.
- **Verdict:** the full-series ξ₁-shadow is NOT located as one object. Lemma O shows that it cannot be. The P-odd half is located, and the P-even half's analogue is the order10 boundary defect.

## Sharpest remaining obstruction and the single next construction
- **Obstruction (Category A):** Lemma O and P-parity. The P-even sector can only carry χ = ±i or |τ|-type laws. The only proper χ = ±i candidates are definite lattices with the same discriminant form as A in the companion coordinates, and none of the 82 det-35 forms qualifies (A1).
- **Next construction:** the χ = ±i basis should be built from the Weil representation itself, by computing the discriminant form of the companion lattice and its signature-2 genus mates. That is the only way Route A can close. In parallel, test exactly whether the P-even part of the full series equals 𝓗 of an arc-combination of Siegel lifts (Θ_{C_arc}, Θ_E and the axis lines, by coefficients). If it does, the P-even shadow is the order10 boundary defect, stated in closed form.

## Candidate Residual↔Resonant map (statement only; NOT preregistered or tested; not a bridge)
**Map E1.** If an RTA/T3/O_res/Π object corresponds to C's P-even sector, it should carry a sign-blind |x|^{−1} leading-order law (Maass-type, λ = ¼) and not a holomorphic weight-1 law. Predicted test: its leading profiles at x < 0 obey g(−1/x) = |x|^{−1}(1/√35)Mg(x), and the signed law fails, as in B3. This would be a falsifiable statement about the Resonant side; it is handed to MAPS_CANDIDATES.

## Disclosures
- B3 float64 inconclusives were recorded by rule before the high-precision leg. b3x is preregistered (PREREG B3 "mp dps 40 at 1/2, 1/3"). It was implemented as exact integer phase reduction with longdouble trig (≈ 1e−19), not mpmath dps 40, and it was also run at −1/2 and −1/3. This deviation is disclosed.
- B1 inconclusive is recorded as such. No post-hoc rerun was done for lack of time.
- The Route A basis was enumerated as specified. A1 shows it is not M-covariant, so the test is weak.
- CORE_FREEZE was respected; the 35-component law vector was untouched.
