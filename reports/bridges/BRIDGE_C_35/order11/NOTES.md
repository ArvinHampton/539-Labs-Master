# order11 RESULTS: weight-1 completion of Θ_E from the C_arc rays, and its obstruction
Prereg: PREREG.md, sha256 5d41a83a…d989, written before any numerics. Script hashes are in scripts/SHA256SUMS. Data: data/s.json. Log: logs/s.log.

## Candidate
F̂_E = Θ_E + ½(T_{c1} − T_{γc1}), where T_{c1} = −θ_{7/2}·Σ_u sgn(u)·erfc(√(10πy)|u|)·e(−5u²τ/2 − 5b0·u) is θ_{7/2} times the non-holomorphic Eichler integral of the 5n²/2 series.
ξ₁F̂_E = ½√10·y^{1/2}·[conj(θ_{7/2})·ϑ⁻ at (α,β) − the same at (γ⁻¹α, γ⁻¹β)].

## Verdicts
| Test | Result | Verdict |
|---|---|---|
| N1 parity: T is P-odd, Θ_E is P-even (all 105 components) | 9.9e−32 / 5.0e−32 | pass |
| N2 ξ formula, by mp.diff | 1.8e−31 | pass (calculus check) |
| Control Ĝ_O, χ = 1 (dps 20) | 3.6e−21 | **pass**, so the test is valid |
| N3, χ = 1, κ = ½ | 0.68 (best-fit κ: 0.65) | **FAIL** |
| N3, χ = −1, κ = ½ | 0.69 (best-fit κ: 0.65) | **FAIL** |
| N3, χ = i, κ = ½ | 0.96 (best-fit κ: 0.92) | **FAIL** |
| N3, χ = −i, κ = ½ | 0.65 (best-fit κ: 0.53) | **FAIL** |
| Θ_E alone, χ = ±i (recheck of order8 M3 at dps 30) | 0.92 / 0.53 | **FAIL** |

The best-fit κ is about 0.01–0.05, essentially 0: the correction cannot repair the law. T_{c1} − T_{γc1} alone also fails every χ (0.42–0.56).

## Obstruction (Category A: Lemma O and its Corollary, PREREG §2)
- **Lemma O.** If a vector F of 105 functions, holomorphic or not, obeys F(−1/τ) = χ(τ/√35)MF(τ) for a scalar χ, then F = −χ²PF. This follows from M² = 35P, which is exact.
- **Parity.** Θ_E is P-even. Every Eichler correction built from weight-3/2 unary thetas paired with weight-½ thetas is P-odd.
- **No completion of this form exists** for any scalar χ and any κ:
  - χ = ±1 forces the P-even part to vanish, which is impossible since Θ_E ≠ 0.
  - χ = ±i forces the P-odd correction to vanish, which reduces to Θ_E (plus a holomorphic P-even term) obeying the χ = ±i law. For Θ_E alone this is falsified (Category B).
- The numbers above confirm this (Category B).
- Scope: this obstruction holds without holomorphy. The review's restriction concerns |τ|-type laws, which are not of this form.

## Full-series ξ-shadow
**NOT located in any scalar-twisted fixed weight-1 M-law.**
- The pieces already located (cone Ĥ, odd pair Ĝ_O) are P-odd, consistent with χ = 1.
- The P-even sector (Θ_E, and the even part of the full series) cannot carry a fixed weight-1 τ-law with χ = ±1 at all.
- The even sector's natural law is the weight-0 / |τ|-type law of y^{1/2}Φ₀ (order7, order10).
- There remain three distinct unary-theta series (5n²/2 shared). Θ_E = 𝓗(Φ) is an identification, not a bridge. M² = 35P is exact (Category A).

## Disclosures
- The S-law tests run at 3 interior τ in mpmath (dps 30; control at dps 20). These are fixed-matrix law tests, not float64 span tests, and they are secondary to Lemma O.
- Lattice boxes are truncated (tails below e^{−140}). Θ_E for axis companions uses edge weight ½.
- The best-fit κ is descriptive only. Every verdict was recorded by the preregistered rule; no post-hoc rerun was done.
- The χ = ±i route for Θ_E + h with h holomorphic and P-even is not excluded in general; only h = 0 was tested.

## Open next step
Two options:
(a) Test the χ = ±i law for Θ_E + h, with h in the span of P-even holomorphic weight-1 theta series of the lattice (finite and exact: Hecke-type for the definite forms of discriminant −35·k). Use exact q-expansion coefficients and solve for h by linear algebra.
(b) Formulate the P-even sector's law as a |τ|-type weight-(½,½) law and test y^{1/2}·(even part) exactly. This is the review finding-1 type.
