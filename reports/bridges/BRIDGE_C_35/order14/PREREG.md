# PREREG: order14. Closing the hybrid-shadow gaps for the literal full series
Written 2026-10-24, about 5:40 PM CDT, before any order14 numerics. Owner: Arvin Hampton. Parents order5–order13 are read-only. New files only. CORE_FREEZE. Category A = proof or exact; Category B = numerical. Runs use nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No push, no sends, no bridge claims.
Standing: Lemma O and Lemma W (order13 W1) are Category A. There are three distinct unary thetas (5n²/2 shared). Θ_E = 𝓗(Φ_orth) is an identification. Arvin's "local mock / non-local quantum modular" framing is opinion only.

## 1. Proof: B(ĉ′) ≡ 0 (Category A, written here)
B(ĉ′)(α,β;τ) = Σ_{ν∈α+Z²} e(B(ν,β))·s s′·e(s′²τ/4)·e(−s²τ̄/4), with s = √35·ν2 and s′ = ±(2ν1+7ν2).
Let ρ := −σ = [[−1,−7],[0,1]], so ρ(ν) = (−ν1−7ν2, ν2). Then:
- ρ is an isometry: Q(ρν) = Q(ν).
- ρ fixes ν2, so s is unchanged, and it sends 2ν1+7ν2 to −(2ν1+7ν2), so s′ changes sign. The term's ss′ flips sign and both Gaussians are unchanged.
- **Coset:** ρα − α = (−2α1−7α2, 0) = (−(Aα)_1, 0). For every companion, (Aα)_1 ∈ Z: for K2, α = a+μ with Aμ ∈ Z² and (Aa)_1 = 2·7/10 − 7/5 = 0; for K3 and K4, α = μ. So ρ maps α+Z² onto itself.
- **Phase:** B(ν,β) − B(ρν,β) = (Aν)_1·(Aβ)_1, with (Aν)_1 ∈ Z. Here β ∈ {0, a} and (Aa)_1 = 0, so the phase is invariant.
- Hence B(ĉ′) = −B(ĉ′), so **B(ĉ′) ≡ 0** for all 105 companions. ∎
- The same argument at ĉ1 would need an isometry fixing ν1 and negating ν1+ν2 while preserving the coset; this is not claimed. The ĉ1 term is predicted to be nonzero for some companions.

## 2. Tests
- **C1 (W2d rerun with the preregistered metric).** err = |direct − glued| / Σ|terms|, at 3 τ (0.1+0.9i, −0.3+1.2i, 0.37+0.7i), for all 105 companions, mpmath dps 30. Pass ≤ 1e−25; FAIL > 1e−12. Also reported: |B(ĉ′)|/Σ|terms| (predicted ≤ 1e−25 by §1) and |B(ĉ1)|/Σ|terms|. The ĉ1 value is predicted nonzero (> 1e−6) for at least one companion; this is the non-triviality control, and C1 is invalid without it.
- **C2 (literal line corrections, exact rationals).** The literal series uses v = ν − α_j with the sym_pair representatives (as in order2/3c): W(v) = 1[n≥0]1[k≥0] − ½(sgn n + sgn(n+21k)).
  - P acts termwise as (PS)_j = Σ_{ν∈α+Z²} W(−ν − α_k) q^{Q(ν)} e(B(ν,β)), where k is the companion of class −α.
  - P-even literal weight: E_lit(ν) = ½(W(ν−α) + W(−ν−α_k)). P-odd: O_lit(ν) = ½(W(ν−α) − W(−ν−α_k)).
  - Line defects: Δ_E = E_lit − ¼(1+s1s2) and Δ_O = O_lit − [¼(s1+s2) − ½(s1+s3)], with s_i the ν-signs.
  - **Prediction:** on the box |n|,|k| ≤ 60, every support point of Δ_E and Δ_O lies on the lines n ∈ {−1,0,1}, k ∈ {−1,0,1}, or n+21k ∈ {−1,0,1}, or on finitely many isolated points.
  - Each line is classified as full (Δ ≠ 0 at both ends, |t| > 30) or half. Every line's Q-restriction is positive definite: Q(e1) = 1, Q(e2) = 7/2, Q(21,−1) = 297.5.
  - Pass = 0 uncovered support points. Report the P-parity of each line class.
- **E2-int (Map E2, internal and cheap).** The leading radial vector g(x) (order12 b3x method) is P-even: max|g − P g| / max|g| ≤ 1e−15 at x ∈ {1/2, 1/3, −1/2, 2/5}. A FAIL would falsify the parity→law-type map E2 for C itself.

## 3. Verdict rule
**The hybrid shadow is located for the literal full series** iff §1 holds, C1 passes (including the control), and C2 passes. The literal statement then reads:
- S = [P-odd: Zwegers-completed Ĥ, Ĝ_O with ξ₁-shadow = the three unary thetas] + [P-even: ½𝓗(Φ_orth), with Laplacian defect ±(π/4)√140·y^{3/2}·ϑ⁺_{7/2}·conj(ϑ⁻_{5/2})] + [finite line terms].
- The line terms are full lines, which are holomorphic weight-½ unary thetas with no shadow, and half-lines, which are partial/false thetas whose quantum partners are weight-3/2 unary series. Each is assigned to a parity.
- Otherwise, the gap is stated.

## 4. Maps (statements fixed; tests only where cheap)
- **E2:** P-parity determines law type. P-odd means a holomorphic χ = 1 law (Lemma W); P-even means an |x|/|τ|-type law. Internal test: E2-int. The Resonant-side test is OPEN.
- **E3:** the 5n²/2 series at characteristic α1 is the unique unary theta shared by both sectors. Prediction: any weight-3/2 theta in T3/O_res is this series. OPEN, since no T3/O_res q-series is available. Next measurement: the q-expansion exponents of the T3/O_res object compared with 5u²/2, u ∈ α1+Z.
- **E1:** the Resonant half stays OPEN, as before.
