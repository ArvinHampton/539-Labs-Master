# PREREG: order16. Closed-form line terms; RG1′ necessity; feed into paper v4
Written 2026-10-24, about 6:20 PM CDT, before any order16 numerics. Parents are read-only. New files only. CORE_FREEZE. Category A = proof or exact; Category B = numerical. Runs use nice, OMP_NUM_THREADS=1, ulimit -v 3000000.

## A. Line terms in closed form (Category A, algebra written here)
For a companion (α,β) with paper representative α, ν = α+v, v = (n,k) ∈ Z². Signs s1 = sgn ν1, s2 = sgn ν2, s3 = sgn(ν1+21ν2), with sgn 0 = 0. The literal weight is W(v) = 1[n≥0]1[k≥0] − ½(sgn n + sgn(n+21k)). The ν-sign weight is p(ν) = ¼(1+s1)(1+s2) − ½(s1+s3).
Put
- h1(n) = 1[n≥0] − ½(1+s1), h2(k) = 1[k≥0] − ½(1+s2);
- g1(n) = sgn n − s1, g3(m) = sgn m − sgn(m+σ), with m = n+21k and σ = α1+21α2.
**Identity:** W(v) − p(ν) = ½(1+s1)h2(k) + ½(1+s2)h1(n) + h1(n)h2(k) − ½g1(n) − ½g3(m).
Each of h1, h2, g1, g3 is supported on the finitely many integers between 0 and −α1 (h1, g1), between 0 and −α2 (h2), or between 0 and −σ (g3), endpoints included as computed.
**Line terms.** With L(τ) := S_{α,β} − S^ν_{α,β}:
- **half-lines along e1** (ν2 = c := k+α2 fixed, weight h2(k)·½(1+sgn ν1)): Q = w² − (35/4)c², w = ν1 + 7c/2. This is a partial theta in w ∈ α1+7c/2+Z, w ≥ 7c/2, with Eichler partner Σ w e(w²τ).
- **half-lines along e2** (ν1 = c fixed, weight h1(n)·½(1+sgn ν2)): Q = (7/2)m² − (5/2)c², m = c+ν2 ≥ c. This is a partial theta with partner Σ m e(7m²τ/2).
- **points:** h1h2 ≠ 0, a finite set.
- **full lines ν1 = c** (weight −½g1(n)): q^{−5c²/2}·Σ_{m∈c+α2+Z} e(7m²τ/2 + …), a weight-½ unary theta.
- **full lines n+21k = M** (weight −½g3(M)): with ν0 = (α1+M, α2) and u = (−21,1), Q(ν0+ku) = (595/2)(k + B(ν0,u)/595)² + Q(ν0) − B(ν0,u)²/1190. This is a weight-½ unary theta of norm 595/2.
**Checks:**
- (A1) The identity holds exactly at every ν with |n|,|k| ≤ 100, for all 140 FAM1 companions (exact rationals). Pass = 0 mismatches.
- (A2) The support table per companion (finite data: the sets and values of h1, h2, g1, g3) is written to data/lineterms.json.
- (A3, Category B) At τ = 0.1+0.9i and −0.2+1.05i, for 3 companions, S_{α,β} = S^ν + L at mpmath dps 25 with box 40. Pass ≤ 1e−18.

## B. RG1′ necessity: proof (Category A, written here)
By order10 D2 (an exact unimodular factorisation; Category A algebra), B(ĉ1) = √140·ϑ⁺(τ)·conj(ϑ⁻(τ)), with ϑ⁺ = Σ_{m∈δ+Z} m e(7m²τ/2 + c⁺m), δ = α1+α2, c⁺ = 7(b0+b1), and ϑ⁻ = Σ_{u∈α1+Z} u e(5u²τ/2 + c⁻u), c⁻ = 5b0.
**Lemma.** Let ϑ = Σ_{m∈δ+Z} m e(Am²τ + cm) with A > 0. Then ϑ ≡ 0 iff 2δ ∈ Z, 2c ∈ Z and 2cδ ∈ Z.
*Proof.* ϑ is a convergent series in powers q^{Am²}, and distinct values of m² give distinct exponents. By uniqueness of Fourier coefficients in x = Re τ at fixed y, ϑ ≡ 0 iff each coefficient vanishes. The coefficient of q^{Am²} is m e(cm) + [−m ∈ δ+Z](−m)e(−cm).
- If 2δ ∉ Z, −m is never in δ+Z, so the coefficient is m e(cm) ≠ 0 for m ≠ 0, and some m ≠ 0 exists.
- If 2δ ∈ Z, the coefficient is m(e(cm) − e(−cm)), which vanishes for all m iff 2cm ∈ Z for all m ∈ δ+Z. For m = δ+j that means 2cδ ∈ Z and 2c ∈ Z. ∎
**Corollary (RG1′ iff).** ϑ⁺ is holomorphic and conj(ϑ⁻) is antiholomorphic. If both are nonzero, their zero sets are closed and nowhere dense, so the product is nonzero on a dense open set. Hence B(ĉ1) ≡ 0 iff ϑ⁺ ≡ 0 or ϑ⁻ ≡ 0. By the Lemma:
- ϑ⁺ ≡ 0 iff 2(α1+α2), 14(b0+b1) and 14(b0+b1)(α1+α2) are in Z (the ρ_m criterion);
- ϑ⁻ ≡ 0 iff 2α1, 10b0 and 10b0α1 are in Z (the ρ_u criterion).
So **RG1′ holds as an iff (Category A)**. The same Lemma applies to the P-odd ξ₁ factor ϑ⁻ (5n²/2) and gives its exact vanishing set.
- (B1, consistency) The criterion equals the measured zero sets recorded in order14 rg1 (105), order15 H (70) and order14 rg1k1 (K1). Exact comparison of stored data. Pass = equality.

## C. Paper v4
Absorb the Category A facts (Lemma O, Lemma W, M² = 35P, (MT)³ = 35√35P, B(ĉ′) ≡ 0, RG1′ iff, the line-term identity, the P-even Laplacian identity, W2a) with full proofs. Category B facts go to remarks and App. D only.

## Maps
No new Residual–Resonant map is proposed. **Map RG2 (residual-internal, statement only):** the c1-end shadow pieces of the two sectors vanish together exactly on the ρ_u set. This is a corollary of the Lemma (Category A), so it needs no test.
