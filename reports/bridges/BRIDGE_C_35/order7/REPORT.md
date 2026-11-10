# order7 REPORT (descriptive notes; verdicts as in RESULTS.md)
PREREG sha256 251f3058…0e28 (unchanged). Script hashes: scripts/SHA256SUMS. Deviations are listed in NOTES.md, and all verdicts below are as recorded.

## §0 Parity lemma
**Check.** M² − 35P = 0, verified numerically to 8.9e−30 (mpmath, dps 30; float64 gives 1.8e−14). Here M is the fixed 35-component law vector S-matrix and P is the involution (α,β) ↦ (−α,−β) with its phases.

**Status.** This is Category A by Weil-representation theory: S² = Z acts as α ↦ −α with e(−sig/4) = 1 for signature (1,1). The numerical check confirms it. The exact cyclotomic check promised in the PREREG was not done (NOTES 1).

**Consequence (Category A, given M² = 35P).** No nonzero P-even vector can obey the fixed weight-1 S-law F(−1/τ) = (τ/√35)·M·F(τ). Applying the law twice gives F = −PF. The even double orthant is P-even, so **no completion of it can obey the fixed weight-1 law**. This explains the order6 failure. P-even objects are allowed at weight 0 and weight 2.

## Candidate 1: non-Vignéras weight-1 object (Category B)
The candidate is p_λ = ½(1 + E1E2) + λ·exp(−π(ℓ1² + ℓ2²)), using the two orthant error-function terms from order6, E1 = E(√10·ν1·√y) and E2 = E(√35·ν2·√y), with ℓ1 = √10·ν1·√y and ℓ2 = √35·ν2·√y. The best fit is λ* = −0.657 − 0.002i.

| quantity | value |
|---|---|
| residual at λ = 0 | 0.903 |
| residual at λ* | 0.482 |
| finite-difference check of ∂_τ̄ (product rule) | 3.4e−9 |

**Verdict: fails, as predicted by the lemma.** The finite-difference shadow check passes, but it is only a calculus check: the ∂_τ̄ is not a sum of unary-theta products.

## Candidate 2: weight-0 Siegel / Hecke–Maass objects for Q(√35)
The objects are Φ_k = ∫ e^{2πikμ/μ_tot}·Θ_z dμ over the unit-group arc from c1 to γc1. Here γ = [[−1,−7],[2,13]] (the unit 6+√35) and μ_tot = 2.478 ≈ log(6+√35) = 2.478, consistent.

Law Φ(−1/τ) = ε·(1/√35)·M·Φ(τ), weight 0, on 120 interior τ:

| object | ε = +1 | ε = −1 | parity PΦ = Φ |
|---|---|---|---|
| Φ_0 | 5.5e−15 | 2.0 | 6.1e−15 |
| Φ_1 | 1.2e−14 | 0.85 | 2.7e−14 |

**Verdict: pass, with ε = +1, Category B.** It also follows from Siegel's theorem for each Θ_z (Category A by citation). These are genuine P-even, weight-0 objects that obey the fixed 35-component law vector S-law.

**Coupling to the even piece is inconclusive.** The test asked whether Ê lies in the span of y^{∓1/2}Φ_k. The residual is 4.3e−10, between the pass and fail lines. The interior-span test turned out to be non-discriminating (see Candidate 3), so no coupling claim is made.

## Candidate 3: enlarged law space W_420 = span[Ê, Ĥ, Ĝ_O, Θ_E]
This space is separate from the 35-component law vector. Ê is the product-completed even piece, Ĥ the completed cone part, Ĝ_O the completed odd orthant pair, and Θ_E the holomorphic even series. The test used 660 interior τ.

- **First run (c3.py): void.** The positive control failed (residual 0.93). The cause was identically-zero companion columns, which were divided by their own ~1e−17 norms (NOTES 2).
- **Disclosed rerun (c3b.py), with near-zero columns dropped:**

| target | residual, w = 0 | residual, w = 1 |
|---|---|---|
| Ĥ (positive control, w = 1) | 2.0e−7 | 9.9e−9 |
| Ê | 1.6e−9 | 2.8e−10 |
| Θ_E | 4.3e−6 | 5.0e−7 |
| Ŝ_ν (full, completed) | 4.3e−8 | 4.1e−9 |

  The numerical rank of W is 97, with singular values decaying smoothly through the cut (1.1e−12 → 7.1e−13). There is no gap.
- **Verdict: inconclusive / void.** The positive control does not reach the 1e−10 pass line. Every target, including the wrong-weight Ĥ at w = 0, lands between 1e−10 and 1e−4. Holomorphic functions on a compact τ-patch are numerically low-rank in float64, so this design cannot separate "law holds" from "law fails". This is a design failure, not evidence either way.

## Verdicts and the shadow
| item | verdict |
|---|---|
| Parity lemma | holds (numerically to 1e−30; Category A by Weil-rep theory) |
| C1 (weight-1 non-Vignéras) | **fails**; it is ruled out in principle at weight 1 by the lemma |
| C2 (weight-0 Siegel/Hecke–Maass) | **objects pass** the fixed weight-0 law (ε = +1); coupling to the even piece **inconclusive** |
| C3 (W_420) | **void/inconclusive** (non-discriminating design) |
| Full-series shadow | **NOT located** |
