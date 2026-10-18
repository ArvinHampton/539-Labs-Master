# ψ cocycle: removing the conditions
*2026-10-17, for Arvin Hampton. Box-only work, read-only on the repo. Scripts and outputs: `2026-10-17-psi-conditions/`.*
*Scope: this is pure Maass-form and q-series analysis. It is separate from HQCC, and it claims nothing about TPC or RH.*

## Summary: which conditions are removed

| Condition in the previous report (`2026-10-17-psi-Cocycle.md`) | Status now |
|---|---|
| Green-form constant C = −π/2, previously from 30-digit quadrature only | **Removed.** Written analytic proof (§1); the symbolic ingredients are checked by sympy. |
| S-law u_L(−1/w) = u_R(w)/√35, previously from Borcherds Thm 4.1 plus numerics | **Removed.** Self-contained Poisson-summation proof (§2), with an explicit S matrix on a 140-label (72-dimensional) family. |
| T-law and closure of the family | **New, Cat A.** Z² with Gram A is an **odd** lattice, so T needs the characteristic vector w_c = (1/10, −1/35) ≡ a mod L′ (§2.3). |
| Only the (a,0) row was checked | **Removed.** All 140 rows were checked (§3): singular cancellation, the absence of half-integer terms, the period-integral closed form, and the three-term cocycle relation. All agree to ≤ 2.3·10⁻¹⁴. |
| ζ(−1,𝒦) = 29/60 from a single cone decomposition | **Confirmed** by 5 independent Shintani cones with 2, 23, 43, 58 and 130 classes (§4.1). Each gives exactly 1/10 and 29/1200. |
| Eisenstein vs cusp content of u_R | **Partly answered** (§4.2). Positive frequencies are pure Eisenstein (genus characters): Cat A, via PARI. Negative frequencies carry a nonzero **dihedral cusp part**: the existence is Cat A, but the explicit split is Cat B. |

**Still conditional.** Three standard analytic facts are used but not written out:
1. The Euler–Maclaurin radial expansions hold uniformly in a sector Re t > 0, so non-tangential approach is allowed.
2. Interchanging the Fourier sum and the Green-form integral (the K₀ series converge uniformly on y ≥ 1).
3. Correctness of PARI's ray-class routines. The class group is certified by `bnfcertify = 1`; the ray-class computations are standard algorithms that I did not certify independently.

Also not done: an explicit Hecke-eigenform basis for the cusp part, and its contribution to ψ.

---

## 1. The Green-form constant (Cat A, written proof)

**Notation.** R_z(w) = Im w / ((w−z)(w̄−z)), v = R_z^{1/2}, Green form [u,v] = u_w v dw + u v_{w̄} dw̄, T_n(w) = √y·K₀(2π|n|y)·e(nx).

**Lemma.** For z ∈ H, define F_n(z) := ∫_z^{z+i∞}[T_n, R_z^{1/2}] along the vertical ray. Then:
- F_n(z) = −(π/2)·e(nz) for n > 0;
- F_n(z) = 0 for n < 0;
- ∫_z^{z+i∞}[√y, R_z^{1/2}] = 1/2.

**Proof.**
1. **Symbolic ingredients** (`lemma_symbolic.py`, sympy; all results 0):
   - Δ_w R_z^{1/2} = ¼R_z^{1/2} for complex z;
   - ∂_{w̄}R_z = i/(2(w̄−z)²);
   - d[u,v] = (u_{ww̄}v − u v_{ww̄}) dw̄∧dw, which vanishes when Δu = Δv = ¼(·).
   So [T_n, R_z^{1/2}] is closed on H∖{z}.
2. **R_z(w) is holomorphic in z.** Hence z ↦ ∫_z^{P}[T_n, R_z^{1/2}] has ∂_{z̄}-derivative equal to minus the dw̄-coefficient at the endpoint, −T_n(z)·v_{w̄}(z).
   - v_{w̄} = ½R^{−1/2}·i/(2(w̄−z)²), and R^{−1/2} → 0 like |w−z|^{1/2} as w → z. So this derivative is 0.
   - Convergence at both ends is uniform: the integrand is O(s^{−1/2}) at s → 0 and has K₀ decay at ∞.
   - **So F_n is holomorphic on H.**
3. **Translation covariance.** T_n(w+ξ) = e(nξ)T_n(w) and R_{z+ξ}(w+ξ) = R_z(w), so F_n(z+ξ) = e(nξ)F_n(z) for real ξ. Hence F_n(z)e(−nz) is holomorphic and depends only on y, so it is a constant: F_n = C_n·e(nz).
4. **n < 0.** |F_n| stays bounded as y → ∞, while |e(nz)| = e^{2π|n|y} grows. So C_n = 0.
5. **n > 0: computing C_n by Laplace's method as y → ∞.** Along w = z + is, R = (y+s)/(s(2y+s)) > 0. Write a = 2πn, Y = y+s. The integrand is exactly

   −e(nx)·{ [aY(K₀+K₁) − K₀/2] / (2√(s(2y+s))) + K₀√s / (4(2y+s)^{3/2}) },  with K_ν = K_ν(aY).

   - Multiply by e^{ay} and use K_ν(X) = √(π/(2X))·e^{−X}·(1+O(1/X)) uniformly for X ≥ ay (DLMF 10.40.2).
   - The main term becomes √(πa(y+s)/2)·e^{−as}/√(s(2y+s)) ≤ √(πa/2)·e^{−as}/√s, which is dominated. Pointwise it tends to (√(πa)/2)·s^{−1/2}e^{−as}, whose integral is (√(πa)/2)·√(π/a) = π/2.
   - The other two terms are O(y^{−1/2}) after multiplying by e^{ay}.
   - So F_n·e^{ay}/e(nx) → −π/2. Since this ratio is exactly C_n for every y, **C_n = −π/2 for every n > 0.**
6. **n = 0.** The integrand is (y/2)·s^{−1/2}(2y+s)^{−3/2}, which integrates to (1/4)·B(½,1) = 1/2.

The earlier 30-digit quadrature (`../2026-10-17-psi-cocycle/lemma_c1.txt`) agrees, and is now only a cross-check. This is the s = 1/2 case of Lewis–Zagier, *Period functions for Maass wave forms I*, Ann. Math. 153 (2001), arXiv:math/0101270, Ch. II §2. The citation was checked earlier; the proof above does not depend on it.

## 2. The S- and T-laws, derived (Cat A)

### 2.1 Poisson summation at a fixed majorant
- **Lattice and duals.** L = Z², Gram A = [[2,7],[7,7]], det A = −35. The dual is L′ = A⁻¹Z², and L′/L has order 35.
- **Theta functions.** Fix a majorant (a point v of the γ-geodesic) and put G_τ(ν) = e(τQ₊(ν) + τ̄Q₋(ν)). For any α, β ∈ ℝ²:

  Θ_{α,β}(τ) := Σ_{ν∈α+Z²} e(B(ν,β))·G_τ(ν).

- **Poisson.** Σ_n g(n+α) = Σ_m ĝ(m)e(m·α), with g = G_{−1/τ}·e(B(·,β)), ĝ(m) = Ĝ(m − Aβ), and m = Aμ (μ ∈ L′).
- **The Gaussian transform.** Ĝ_{−1/τ}(Aη) = (|τ|/√35)·G_τ(η). The factor is det(M/i)^{−1/2} with det(M/i) = (τ/i)(iτ̄)·35 = 35|τ|²; the two square roots are complex conjugates, so their product is |τ|.
- **Result.** Writing η = μ − β:

  **Θ_{α,β}(−1/τ) = |τ|·(e(B(α,β))/√35)·Σ_{p∈L′/Z²} Θ_{p−β, α}(τ).**

- Integrating over the geodesic of ⟨γ^k⟩ (k = 2 is the common stabiliser order on all labels) and multiplying by √y, with √Im(−1/τ) = √y/|τ|, gives the weight-0 Maass S-law:

  **u_{α,β}(−1/w) = (e(B(α,β))/√35)·Σ_p u_{p−β, α}(w).**

  The constant term √y·log ε comes from ν = 0 and appears exactly when α ∈ Z².
- **Our old row.** For (α,β) = (a,0), the right-hand side is (1/√35)Σ_p u_{p,a}. Using u_{p,a} = u_{−p,−a} (from ν → −ν), this equals u_R/√35. So the old S-law is now proved.

### 2.2 Reductions
- u_{α+n,β} = u_{α,β} for n ∈ Z².
- u_{α,β+μ} = e(B(α,μ))·u_{α,β} for μ ∈ L′; this is well defined because B(Z², L′) ⊂ Z.
- u_{−α,−β} = u_{α,β}.

### 2.3 T-law (odd lattice)
- Q(n) = n₁² + 7n₁n₂ + (7/2)n₂² is not integral on Z², so Z² is an **odd** lattice.
- Its characteristic vector is w_c = A⁻¹(0,½) = (1/10, −1/35): e(Q(n)) = e(B(n,w_c)). Since A(a − w_c) = (0,3), we have **w_c ≡ a mod L′**.
- Then

  **u_{α,β}(w+1) = e(−Q(α) − B(α,w_c))·u_{α, α+β+w_c}(w).**

- With the naive even-lattice T-law the check fails by O(1). With w_c it holds to 7·10⁻¹⁶ (`slaw_check.txt`).

### 2.4 The family and the matrices
- **Labels.** α ∈ ({0,a}+L′)/Z² (70 classes) and β ∈ {0,−a}: 140 labels in all, listed in `labels.txt`.
- **Matrices.**
  - **S matrix**: (S)_{(α,β),c} = (e(B(α,β))/√35)·Σ_p [phase from §2.2] δ_{c, red(p−β, α)}. Every row has exactly 35 entries, each of modulus 1/√35. The matrix is unitary.
  - **T matrix**: monomial (one entry per row) and unitary.
  - Both are saved as `S_matrix.npy` and `T_matrix.npy` (`family.py`, `dump_matrices.py`).
- **Group relations.**
  - S² = P exactly, where P is the label map (α,β) → (−α,−β).
  - On the P-invariant subspace (dimension **72**), S² = I and (ST)³ = I to 1.3·10⁻¹⁵.
  - So the family carries a 72-dimensional representation of PSL₂(Z). This replaces the "36 × 36" ansatz: the 36 earlier components are not closed under T.
- **Numerical checks on all 140 rows**, at three points with y ≈ 1, using Bessel series for every u_{α,β} (`slaw_check.txt`):
  - |u(−1/w) − S·u(w)| ≤ 1.2·10⁻¹⁵;
  - |u(w+1) − T·u(w)| ≤ 7·10⁻¹⁶;
  - |P·u − u| ≤ 6·10⁻¹⁶.

## 3. Every row of the S-cocycle (Cat A: exact Bernoulli sums vs. an independent period integral)

**Definitions.**
- f_{α,β} := (1/k)·Σ_{i<k}(E^F_{γ^{−i}(α,β)} + E^F_{−γ^{−i}(α,β)}). This is the positive-frequency part of u_{α,β}, by the Lemma.
- Φ(x) := κ(−1/x) − |x|·S·κ(x), where κ is the vector of exact radial constant terms (`kappa_all.py`).
- Row (a,0) reproduces the old ψ exactly: Φ_{(a,0)}(1)/2 = 0.0068839937604 − 0.0382597122170i.

**Checks at x ∈ {1, 1/3, 2, 3/5, 7/4, −1, −2/3}, all 140 rows** (`rows_check.txt`):

| Check | Max deviation |
|---|---|
| Singular parts cancel: \|x\|·s(−1/x) = S·s(x) | 9.0·10⁻¹⁶ |
| No t^{−1/2} terms on any row | 5.7·10⁻¹⁶ |
| P·κ = κ | 5.3·10⁻¹⁵ |
| Period-integral closed form on every row (below) | 2.3·10⁻¹⁴ |

**The closed form, for every row** u = u_{α,β}, with U := S-row combination and J_v(z) = ∫_i^{i∞}[v, R_z^{1/2}]:

  **Φ_u(x) = −(2/π)·[ |x|·a₀(U)/2 − a₀(u)/2 − |x|·J_U(x) + J_u(−1/x) ]**

This is §1 combined with the Stokes argument. The rows with a₀(u) ≠ 0 (α ∈ Z²) work provided the path from z to 0 is the image of the vertical ray, which approaches 0 tangentially to iℝ, so no arc term arises.

**Three-term cocycle relation.** From T-invariance (f(z+1) = T·f(z) exactly) and (ST)³ = I on the span:

  Φ(z) = T·Φ(z/(z+1)) + (z/(z+1))·T S T·Φ(z+1).

Checked at z ∈ {1, 1/2, 2/3, 3/2} on all rows: max deviation 7·10⁻¹⁵.

**Consequence.** Every row of the S-cocycle is real-analytic on ℝ∖{0}, given by the period integral above. So the full 72-dimensional E/f-vector is a vector-valued quantum modular form of weight 1 for the factor |cx+d|. The only remaining inputs are the standard analytic facts in the Summary.

## 4. Extras

### 4.1 ζ(−1,𝒦) by independent Shintani cones (Cat A, exact; `shintani_check.txt`)
- Fundamental domains [r, γr) were taken for r = (1,0), (1,1), (1,2), (2,1), (3,2). These are single non-unimodular cones with |det| = 2, 23, 58, 43, 130.
- Each was split into |det| residue classes, and the exact Euler–Maclaurin expansion was computed on each.
- **Every decomposition gives** zero t^{∓1/2} terms, ζ_E(0) = 1/10 and ζ_E(−1) = 29/1200, so **ζ(−1,𝒦) = 29/60**, the same as before.

### 4.2 Eisenstein vs cusp
**PARI facts** (cypari2 2.2.4; `rayclass_pari.txt`; `bnfcertify = 1`):
- For K = Q(√35): Cl = Z/2, narrow class group Cl⁺ = (Z/2)², fundamental unit 6+√35.
- Ray class group mod 𝔣∞₁∞₂, with 𝔣 = 𝔭₂𝔭₅: **Z/8 × Z/2**, order 16.
- Galois conjugation σ acts as g₁ ↦ 5g₁, g₂ ↦ 4g₁ + g₂.
- The two primes above 13 lie in classes [1,0] and [5,0], which σ swaps. The ramified prime 𝔭₇ lies in [1,1], which σ fixes.

**Characters.** χ_{j,l}(c) = e(jc₁/8 + lc₂/2). Then χ∘σ = χ_{5j, l+j}, so χ is σ-invariant ⇔ j is even. There are 8 such characters.
- **σ-invariant ⇒ genus.** The cyclic extension cut out by χ is Galois over Q with a central cyclic subgroup of index 2, hence abelian. By Kronecker–Weber, χ = ψ∘N, so L(s,χ) = L(s,ψ)·L(s,ψχ₁₄₀) and its θ is Eisenstein.
- **The class sum.** θ_𝒦 = (1/16)Σ_χ χ̄(𝒦)θ_χ, with θ_χ = θ_{χσ}. For a σ-non-invariant pair the combined coefficient is ∝ χ̄(𝒦)(1 + (−1)^j), which is 0 for odd j.

**Positive frequencies (f = 2E): pure Eisenstein (Cat A, given the PARI data).** Numerically, r_𝒦(n) = h(n mod 280)·Σ_{d|n}(35/d) with h ∈ {0, ½} for all n < 60 000 coprime to 70, and r(p) depends only on p mod 280 for p < 4·10⁵ (`split_test.txt`).

**Negative frequencies: nonzero dihedral cusp part.**
- The negative-norm vectors of u_L lie in the σ-fixed class [1,1] (they start at norm 7, i.e. 𝔭₇). Its coefficients 2χ̄([1,1]) do not vanish for odd j.
- Numerically r″(p) ∈ {0, 2} is **not** periodic mod 280 or 560 (`split_neg.txt`).
- So u_L, and therefore u_R = √35·u_L∘S, has nonzero cusp content. These are Maass's dihedral λ = 1/4 cusp forms from the 4 non-genus σ-pairs.
- Because the positive frequencies are cusp-free, the cusp part must be an even/odd combination with vanishing positive coefficients.

**Status.**
- Cat A: the character bookkeeping and the vanishing on the positive side.
- Cat B: the identification of the negative-side pieces with specific Hecke eigen-Maass forms (infinity types not assigned), and the split of ψ into ψ_Eis + ψ_cusp. Not computed.

## 5. What is left
1. Writing out the standard analytic facts: uniform sectorial Euler–Maclaurin, and interchange of sum and integral.
2. An explicit eigenbasis for the cusp part (infinity types of χ_{j,l}; the even/odd pairing χ ↔ χε) and the split ψ = ψ_Eis + ψ_cusp.
3. The s = 8 and s = 11 analogues (not attempted this round).

## Files (`2026-10-17-psi-conditions/`)
- Family and matrices: `family.py`, `dump_matrices.py` (`dump_matrices.txt`, `labels.txt`, `S_matrix.npy`, `T_matrix.npy`)
- Maass components: `uvec.py`
- S-, T- and group-law checks: `slaw_check.py` (`slaw_check.txt`)
- All-rows cocycle checks: `kappa_all.py`, `rows_check.py` (`rows_check.txt`, `phi_rows.npy`)
- Lemma ingredients: `lemma_symbolic.py` (`lemma_symbolic.txt`)
- Shintani cross-check: `shintani_check.py` (`shintani_check.txt`)
- Ray class data: `rayclass_pari.py` (`rayclass_pari.txt`)
- Eisenstein/cusp tests: `split_test.py` (`split_test.txt`), `split_neg.py` (`split_neg.txt`)
