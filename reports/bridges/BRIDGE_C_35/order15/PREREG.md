# PREREG: order15. Fresh preregistered tests C1′ and C2′, RG1′ sufficiency proof, discriminating RG1′
Written 2026-10-24, about 6:05 PM CDT, before any order15 numerics. Parents order5–order14 are read-only. New files only. CORE_FREEZE. Category A = proof or exact; Category B = numerical. Runs use nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No push, no sends, no bridge claims. Map-RG1′ is residual-internal, not a Residual–Resonant bridge.

**Fresh family K1:** α = a+μ, β = a, 35 companions (symbols FAM1), never used to tune. order14 rg1k1 used K1 only for B(ĉ1), not for C1/C2.

## 1. C1′ (B(ĉ′) ≡ 0 on K1, metric fixed)
- Prediction (Category A, by the order14 §1 proof): (Aα)_1 ∈ Z and (Aa)_1 = 0 hold for K1.
- Metric: err = |B(ĉ′)| / Σ|terms|, with exact s = √35·ν2 and s′ = −(2ν1+7ν2) computed from exact rationals. Box |n|,|k| ≤ 10, 3 τ (0.1+0.9i, −0.3+1.2i, 0.37+0.7i), dps 30.
- **Pass:** max ≤ 1e−25 over all 35 × 3. **FAIL:** > 1e−12.
- Control: |B(ĉ1)|/Σ|terms| > 1e−6 for at least one K1 companion.

## 2. C2′ (literal line-defect coverage, offsets range fixed in advance)
- Same definitions as order14 C2, on K1. The partner representative α_k comes from reduce over FAM1. Box |n|,|k| ≤ 80; this is a larger box, so it also serves as a holdout in range.
- Lines: n = c or k = c or n+21k = c with |c| ≤ 4.
- **Pass:** 0 uncovered support points of Δ_E and Δ_O. **FAIL:** ≥ 1.
- Also reported: full/half/finite counts by parity and direction.

## 3. RG1′ sufficiency at ĉ1 (Category A, proof written here)
Let u = ν1 and m = ν1+ν2. Then Q = 7m²/2 − 5u²/2 and B(ν,β) = −5b0·u + 7(b0+b1)·m. The ĉ1 term is Σ e(B(ν,β))·√140·u·m·e(7m²τ/2)·e(−5u²τ̄/2).
- **ρ_m:** (u,m) ↦ (u,−m), i.e. ν ↦ (ν1, −2ν1−ν2). This is an integral isometry; it negates the term's u·m and fixes the Gaussians.
  - It preserves α+Z² iff 2(α1+α2) ∈ Z.
  - It preserves the phase iff 14(b0+b1)·m ∈ Z for all m ∈ α1+α2+Z, i.e. 14(b0+b1) ∈ Z and 14(b0+b1)(α1+α2) ∈ Z.
  - Then B(ĉ1) = −B(ĉ1), so B(ĉ1) = 0.
- **ρ_u:** (u,m) ↦ (−u,m), i.e. ν ↦ (−ν1, ν2+2ν1). This is integral as well.
  - It preserves the coset iff 2α1 ∈ Z, and the phase iff 10b0 ∈ Z and 10b0·α1 ∈ Z.
  - Then B(ĉ1) = 0.
- **Sufficiency of RG1′ is therefore proved (Category A).** Necessity remains the prediction.

## 4. Discriminating RG1′ test (necessity), family with predicted zeros
- Family H: (μ, hA) and (a+μ, a+hA) with hA = (1/2, 0); 70 companions, never used before.
- Compute B(ĉ1) with exact s = √10·u and s′ = √14·m; same box, τ and dps as above.
- **Pass:** the measured zero set (≤ 1e−25) equals the RG1′-predicted set, the predicted set is nonempty, and every nonzero is > 1e−6. **FAIL:** otherwise.

## 5. Verdict rule
If C1′ and C2′ both pass, **"the hybrid shadow for the literal full series is located (preregistered)"**:
- the Category A pieces: Lemma O/W, B(ĉ′) ≡ 0, W2a, RG1′ sufficiency;
- the Category B pieces: C1′, C2′, order13 W2c, order8 M1.
Arvin's framing (local mock / non-local quantum modular) stays opinion.
