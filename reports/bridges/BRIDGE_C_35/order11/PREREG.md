# PREREG: order11. Weight-1 non-holomorphic completion of Θ_E from the C_arc boundary rays, or an obstruction
Written 2026-10-24, about 4:30 PM CDT, before any order11 numerics. Owner: Arvin Hampton. Parents order5–order10 and REVIEW_PARALLEL are read-only. New files only. CORE_FREEZE. Category A = proof or exact; Category B = numerical. Runs use nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No push, no sends.
Review rules: Θ_E = 𝓗(Φ) is an identification, not a bridge. There are three distinct unary-theta series (5n²/2 shared). M² = 35·P is exact Category A (order9 cyclo). The P-even lemma as stated in order7 is cited only as below (Lemma O), with its scope made explicit.

## 1. Candidate (constants fixed)
At the negative line c (c1 = (−1,1), or γc1), write sgn_c(ν) = sgn B(c,ν). The Zwegers correction is
  T_c(τ) = Σ_ν [E(B(c,ν)√y/√(−Q(c))) − sgn_c(ν)] q^{Q(ν)} e(B(ν,β)),  E(x) = erf(√π x).
At c1, the unimodular split u = ν1, m = ν1+ν2 gives Q = 7m²/2 − 5u²/2 and B(ν,β) = −5b0·u + 7(b0+b1)·m, so
  T_{c1} = −θ_{7/2}(τ) · Σ_{u∈α1+Z} sgn(u) erfc(√(10πy)|u|) e(−5u²τ/2 − 5b0·u),  θ_{7/2} = Σ_{m∈α1+α2+Z} e(7m²τ/2 + 7(b0+b1)m).
This is θ_{7/2} times the non-holomorphic Eichler integral of the 5n²/2 series.
At γc1: T_{γc1}(α,β) = T_{c1}(γ⁻¹α, γ⁻¹β), using B(γν',β) = B(ν',γ⁻¹β).
**Candidate:** F̂_E = Θ_E + κ·(T_{c1} − T_{γc1}), with **κ = ½** fixed. κ is also fitted freely, descriptive only.
**Predicted ξ₁ (Category A by differentiation):** ξ₁T_{c1} = √10·y^{1/2}·conj(θ_{7/2})·ϑ⁻_{α1}, with ϑ⁻ = Σ_{u∈α1+Z} u e(5u²τ/2 + 5b0·u). Hence
  ξ₁F̂_E = κ√10·y^{1/2}·[conj(θ_{7/2})ϑ⁻ at (α,β) − the same at (γ⁻¹α, γ⁻¹β)].

## 2. Lemma O (Category A, written before numerics)
Suppose a vector F of 105 functions, holomorphic or not, obeys F(−1/τ) = χ·(τ/√35)·M·F(τ) with a scalar χ ≠ 0. Applying S twice gives F = −χ²·P·F, using M² = 35P, which is exact.
- χ = ±1 forces F to be P-odd.
- χ = ±i forces F to be P-even.
- Any other χ forces F = 0.
This uses no holomorphy. The review restriction (finding 1) concerns |τ|-type laws, which are not of this form.
**Parities:** Θ_E is P-even, so Θ_E(−α,−β) = Θ_E(α,β). T_c is P-odd, because sgn_c and E are odd in ν. Every weight-3/2 unary ϑ_α = Σ u q^{au²} is P-odd and every weight-½ θ_α is P-even, so every ξ-image of the form ϑ·conj(θ) is P-odd.
**Corollary (Category A):** if F̂ = Θ_E + R, with ξ₁R in the span of such P-odd products, obeys the law for some χ, then:
- χ = ±1 is impossible, since it would need P-even part Θ_E + R_even = 0 with R_even holomorphic. That would make Θ_E = −R_even, a holomorphic P-even fixed-law object, which Lemma O forbids.
- χ = ±i requires R_odd = 0, so Θ_E + R_even with R_even holomorphic must obey the χ = ±i law.
**Consequence for this candidate (R = κ(T_{c1} − T_{γc1}) is P-odd and nonzero):** it fails for every χ and every κ ≠ 0, and κ = 0 reduces to order8 M3. **Predicted: FAIL.**

## 3. Numerical checks (mpmath dps 30, 3 τ values: 0.1+0.95i, −0.2+1.05i, 0.3+0.9i, with all 105 components)
- N1 parity: max|T(−α,−β) + T(α,β)| and max|Θ_E(−α,−β) − Θ_E(α,β)|. Pass ≤ 1e−25.
- N2 ξ check: ∂_τ̄T_{c1} by mp.diff in x and y against the formula (i√10/2)y^{−1/2}θ_{7/2}·conj(ϑ⁻). Pass ≤ 1e−15 relative.
- N3 S-law for χ ∈ {1, −1, i, −i}, κ = ½, and also κ best-fit per χ. Statistic r = max|F̂(−1/τ) − χ(τ/√35)MF̂(τ)| / max|F̂|. Pass ≤ 1e−15; FAIL ≥ 1e−4. **Predicted FAIL for all.** Also reported: the P-even and P-odd parts of the residual.
- Positive control: Ĝ_O = Σ ½(E(√10ν1√y) + E(√35ν2√y)) q^Q e(Bβ), the order6 completed odd pair, cancellation-safe erfc. It must pass χ = 1 at ≤ 1e−15; otherwise N3 is invalid.
- Θ_E alone with χ = ±i: a recheck of order8 M3 at dps 30. Predicted FAIL.

## 4. Verdict rule
"Completion exists under the fixed law" requires N3 to pass for some χ, with the control passing. Otherwise the obstruction is Category A (Lemma O plus the Corollary), confirmed numerically as Category B, and the full-series ξ-shadow is NOT located in any scalar-twisted fixed weight-1 M-law. The only open route is the χ = ±i law for Θ_E + (holomorphic P-even h), or a non-scalar or |τ|-type law.
