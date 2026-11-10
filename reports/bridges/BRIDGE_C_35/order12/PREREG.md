# PREREG: order12. Two routes for the P-even sector
Written 2026-10-24, about 4:58 PM CDT, before any order12 numerics. Owner: Arvin Hampton. Parents order5–order11, the parent RESULTS (Theorem 3), and REVIEW_PARALLEL are read-only. New files only. CORE_FREEZE. Category A = proof or exact; Category B = numerical. Runs use nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No push, no sends.
Standing rules: Lemma O (F = −χ²PF) is Category A. M² = 35P is exact. There are three distinct unary thetas (5n²/2 shared). Θ_E = 𝓗(Φ) is an identification, not a bridge. No float64 interior span tests (all law tests below use mpmath with few unknowns). FAIL is recorded by the preregistered rule before any post-hoc.
Law convention (order8/order11, control-validated): F(−1/τ) = χ·(τ/√35)·M·F(τ). τ set: T4 = {0.1+0.95i, −0.2+1.05i, 0.3+0.9i, −0.05+1.15i}.

## Route A: χ = ±i law for Θ_E + h, with h holomorphic and P-even
Already failed: h = 0 (order8 M3; order11, with residuals 0.92 for χ = i and 0.53 for χ = −i).
**Basis for h (fixed):** positive-definite binary theta vectors Θ_{A'}(α,β;τ) = Σ_{ν∈α+Z²} e(½νᵀA'ν·τ + νᵀA'β), on the same 105 companions (α,β).
- A' = [[a,b],[b,c]] are integers with ac − b² = 35, |b| ≤ 7, a, c ≤ 42. That gives **82 matrices** (signature (2,0), det 35, like −det A).
- All are holomorphic, weight 1 and P-even.
- Rationale: a definite lattice with the same discriminant form as A has Weil-representation factor e(−2/8) = −i relative to signature (1,1). That is exactly χ = −i.
**Tests (mpmath dps 25):**
- A1 (individual): residual r_χ(A') = max over T4 of |Θ_{A'}(−1/τ) − χ(τ/√35)MΘ_{A'}(τ)| / max|Θ_{A'}|, for χ ∈ {i, −i, 1, −1}. This is descriptive: it says which A' realise M at weight 1.
- **A2 (solve):** minimise over x ∈ C^{82} the residual of Θ_E + Σ x_k Θ_{A'_k} under the χ = ±i law. There are 4 τ × 105 = 420 complex equations for 82 unknowns; normal equations at dps 25. Statistic r = max residual / max|Θ_E + h| over T4.
  - **Pass** if r ≤ 1e−15 for χ = i or χ = −i, and then a holdout residual at 2 new τ (0.15+1.0i, −0.25+0.92i) is also ≤ 1e−15.
  - **FAIL** if r ≥ 1e−4.
  - **Predicted: FAIL.** Reason: Θ_E is a holomorphic indefinite-cone series whose radial A1 and A2 carry edge (wall) terms (order8 M2c/order9 R1), whereas definite thetas have A1 = A2 = 0 at every rational. The χ-law would force these walls to cancel.

## Route B: |τ|-type weight-(½,½) law for the P-even sector
**Predicted law (fixed):** G(−1/τ) = |τ|·(1/√35)·M·G(τ). This is the same as weight 0 for y^{1/2}G: if Φ obeys the weight-0 law, then Ψ := y^{−1/2}Φ obeys this law (Category A, one line).
- B1: Ψ₀ = y^{−1/2}Φ₀ (full unit arc, order7/order10). Law residual at T4, mpmath dps 20, with 40 Gauss–Legendre arc nodes. **Predicted pass** ≤ 1e−12. This is a recheck of order7 at high precision, so it is not new evidence.
- B2 (Category A obstruction, numeric confirmation): G = y^{1/2}Θ_E cannot obey the law. It would require Θ_E(−1/τ) = (ττ̄/√35)MΘ_E(τ), with a holomorphic left side and a non-holomorphic right side, forcing Θ_E = 0. Numeric FAIL predicted (≥ 1e−4) at T4. The same holds for y^{1/2}(any holomorphic P-even piece of the full series).
- **B3 (radial, high precision, discriminating):** let g_j(x) = (1/N²)Σ_{ν∈α_j+Z² mod N} e(Q(ν)x + B(ν,β_j)), with N = 2·70·den(x) and periodicity asserted. By order8/order9, g is the leading radial profile of Ψ₀ and Θ_{C_arc}, up to one constant across all components.
  - Prediction: **g(−1/x) = |x|^{−1}·(1/√35)·M·g(x)** for x ∈ {1, 1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5} and also **x ∈ {−1/2, −1/3, −2/5}**. The signed alternative x^{−1} is predicted to FAIL at x < 0. This discriminates the |x| law from the holomorphic one.
  - Pass ≤ 1e−12 relative (float64 finite sums, a disclosed Category B, plus mp dps 40 at x = 1/2, 1/3).
  - Disclosure: for x > 0 the |x| law is the parent Theorem 3 (proved), so x > 0 is a consistency check. The x < 0 points and the extension to all 105 components are the new content.
**Verdict rule:**
- Route B "holds" iff B1 and B3 (|x|) pass and B2 fails, as predicted.
- The full-series ξ-shadow counts as located only if a non-holomorphic completion of the P-even sector of the full series is exhibited whose ξ-image is a sum of unary-theta products. Route B gives a law (|τ|-type weight (½,½)) for Ψ₀, not a ξ₁-shadow. **Predicted: shadow NOT located in the ξ₁ sense.** The P-even sector is governed by the weight-(½,½) Maass-type law, with the order10 boundary defect.
