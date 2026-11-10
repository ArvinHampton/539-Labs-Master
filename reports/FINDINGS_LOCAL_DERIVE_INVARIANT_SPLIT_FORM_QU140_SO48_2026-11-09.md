# FINDINGS — Local Path DERIVE: A-invariant split form on ℚ[U(140)] ⇒ A ↪ split SO₄₈(ℚ) — 2026-11-09

- Lane: Local Path. Written Nov 9, 2026 (~1:10 PM CST, America/Chicago) under Owner DIRECT ~1:00 PM CST (derive + additive writes). New dated file; nothing overwritten.
- No CERT. Tip sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 untouched (re-checked). Residual≠Resonant. No Gemini/external send.
- Settles item 9 of reports/FINDINGS_LOCAL_SO48_V23_LOCAL_DATUM_MATCH_CHECK_2026-11-09.md (sha 2135adfb…), which was OPEN.
- Setting (Owner/PP-Written): L_i = F[U140], n = 48, regular permutations R_c (reports/FINDINGS_PP_OWNER_PDF_1715_MATH_REVIEW_ADDENDUM_L_1856_2026-11-05.md:4–5). A = U(140) ≅ U(4)×U(5)×U(7) ≅ C₂×C₄×C₆.
- Notation: ε(Σ a_g g) = a_1; x* = Σ a_g g⁻¹; Â = character group.

## Local-derived definition
**LD-1 (Local-derived definition, not Owner-Written).** B_z(x,y) := ε(x·z·y*) on ℚ[A], for z ∈ ℚ[A] with z* = z. **Chosen z = [−1] = [139] ∈ A** (the element −1 mod 140, of order 2). Explicitly, on the basis A: B(g,h) = 1 if h ≡ −g (mod 140), else 0.

## Results
1. **PROVED — classification.** Every A-invariant bilinear form B on ℚ[A] equals B_z with z = Σ_g B(1,g)·g⁻¹... precisely: set z_g := B(1, g⁻¹)… equivalently B(g,h) = B(1, h g⁻¹) (invariance), so B is determined by the function g ↦ B(1,g); put z := Σ_g B(1,g⁻¹)·g, then B(x,y) = ε(x z y*). B is symmetric ⇔ z* = z. Any such B is automatically inversion-compatible: B(x*,y*) = ε(x* z y) = ε((x* z y)*) = ε(x z y*) (A abelian, z*=z, ε(w*)=ε(w)).
2. **PROVED — real decomposition and signature.** ε(w) = (1/48)Σ_χ χ(w), and for real x, χ(x*) = conj χ(x). So B_z(x,x) = (1/48)Σ_χ χ(z)|χ(x)|², with χ(z) ∈ ℝ (since z*=z). Â has |A[2]| = 8 real characters (1-dim pieces, sign sgn χ(z)) and 20 conjugate pairs {χ, χ̄} with χ̄(z) = χ(z) (2-dim pieces, ±definite with sign sgn χ(z)). Nondegenerate ⇔ χ(z) ≠ 0 ∀χ; signature = (a+2b, 48−a−2b), a = #{real χ: χ(z)>0}, b = #{pairs: χ(z)>0}.
3. **PROVED — every sign pattern is rational-realizable.** ℚ[A] ≅ ∏_O ℚ(χ_O) over Galois orbits O of Â; symmetric z ↔ ∏ ℚ(χ_O)⁺. Orbit census by character order d: d=1:1, d=2:7 (field ℚ); d=3:1, d=6:7 (ℚ(√−3)); d=4:4 (ℚ(i)); d=12:4 (ℚ(ζ₁₂), real subfield ℚ(√3)). For d ≤ 6 the real subfield is ℚ, so each orbit (one real char or one pair) takes any rational sign; for d=12 each orbit is two pairs with values α, α′ conjugate in ℚ(√3), and signs are independent (α=1: ++; α=√3: +−). Hence all 2⁸·2²⁰ patterns occur.
4. **PROVED — explicit split z.** z = [−1]: z* = z (order 2); χ(z) = χ(−1) = ±1 ≠ 0 for every χ (nondegenerate); #{χ: χ(−1)=+1} = 24 (kernel of evaluation at an element of order 2 is an index-2 subgroup of Â) ⇒ signature (24,24). Since −g ≢ g (mod 140) for units (2g ≢ 0), A splits into 24 pairs {g, −g}; each span has Gram [[0,1],[1,0]] = H. So (ℤ[A], B) ≅ 24H **over ℤ**: even, unimodular, det = (−1)²⁴ = 1.
5. **PROVED — local invariants.** det = 1 (signed disc (−1)^{48·47/2}·1 = 1). Hasse invariants: 24H ≅ 24⟨1,−1⟩; only (−1,−1)_p pairs contribute, C(24,2) = 276 of them (even) ⇒ Hasse invariant +1 at every place p = 2, 3, 5, 7, 23, …, ∞. No other primes enter (all χ(z) = ±1, norms 1). Witt index 24 over ℚ and over every ℚ_p and ℝ: (ℚ[A], B) ≅ 24H, i.e. split.
6. **PROVED — the homomorphism.** ρ_reg: A → O(ℚ[A], B) ≅ O(24H) is well defined (B_z is A-invariant: B(ax,ay) = ε(a x z y* a⁻¹) = B(x,y)); faithful; image in **SO₄₈ split over ℚ**: an element of order m acts by 48/m m-cycles, odd only if m even and 48/m odd (m ∈ {16,48}); exponent of A is 12 ⇒ every regular permutation is even.
7. **PROVED — unramified at 23 (and everywhere).** ℤ[A] with B is unimodular over ℤ (step 4), so ℤ_{23}[A] is a self-dual lattice and A ⊂ SO(ℤ_{23}[A], B) ≅ split SO₄₈(ℤ_{23}), a hyperspecial maximal compact. 23 ∤ 48 = |A| and 23 ∤ det = 1, as expected. (The same holds at 2, 3, 5, 7.)
8. **Small exact check (sympy, 48×48):** Gram det = 1, symmetric, zero diagonal, eigenvalues {+1:24, −1:24}, A-invariance True, all 48 regular permutations even, element orders {1,2,3,4,6,12}. Consistent with 4–6.
9. **Not REFUTED.** A split rational invariant form exists, so the "no such embedding" alternative is refuted by the explicit z = [−1] (counterexample to non-existence).

## What this gives / does not give
- Gives (PROVED): a faithful A-equivariant embedding A = C₂×C₄×C₆ ↪ SO₄₈(ℚ) split, defined over ℤ, landing in the hyperspecial SO₄₈(ℤ_p) at every p.
- **OPEN:** this is a finite abelian subgroup, not an automorphic representation π of SO₄₈(𝔸) and not a local datum (Satake parameter) at v=23. It yields no Λ(s,π_𝔸), no ω₂₃, and no link to y_i = 23^{24−i}.
- **OPEN:** uniqueness. Many z give split forms (e.g. any order-2 g₀ ∈ A gives the same 24H structure; other ±1 patterns with paired orbits too). LD-1 is a choice, not forced by Owner text.
- **OPEN:** relation to the Codex's Γ₄₈ (positive-definite, Construction A). This form is the split ℚ-form, a different ℚ-form of D₂₄ from SO(Γ₄₈⊗ℚ) (compact at ∞); see item 7 (REFUTED conjunction) of the SO48 file.
- **OPEN:** any Bridge C role (boundary operators T_i, D, C0, C_M) preserving B. Not checked; α_ik unspecified (Addendum L).

## Rollup
PROVED 8 (items 1–7, 9) · CONDITIONAL 0 · OPEN 4 · REFUTED 0 (non-existence alternative refuted by counterexample, recorded under 9). No CERT. Tip untouched.
