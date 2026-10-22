# A35: The space spanned by the 35-component law vector, made exact

**For:** Arvin Hampton (539 Labs) · 2026-10-22, about 10:55 AM CDT.

**Folder:** `reports/s_family_paths/A35_lawspace_exact/`
- Scripts: `symbols.py`, `orbits.py`, `exact_dim.py`, `exact_main.py`, `exact_intertwiner.py`, `floatcheck.py`.
- Outputs: `exact_main.json`, `exact_dim.json`, `exact_intertwiner.json`, `quot_*.json`, `X_modp_*.npy`.

**Ground rules**
- CORE_FREEZE: H_s was not redefined and certifier code was not touched.
- Read-only imports: A32 (`exact_hom.py`, `exact_verify.json`), `A/scripts/weil_family.py`, and A33's `law.py`. The last is used only in the floating-point sanity check.
- New files only. Nothing was pushed or sent. No TPC or RH claims.
- **Cat A** = proved, or a computer certificate (CC) with exact arithmetic. **Cat B** = floating point.

**Notation**
- The **35-component law vector** has components G_{α,β}(x) = mean over ν ∈ α+Z² of e(x·Q(ν) + B(ν,β)), for x ∈ Q, with A = [[2,7],[7,7]].
- Its characteristic classes are, for μ ∈ D = A⁻¹Z²/Z²:
  - K2_μ = G_{a+μ,0}
  - K3_μ = G_{μ,a}
  - K4_μ = G_{μ,0}
  - K1_μ = G_{a+μ,a}
  
  Here a = (7/10, −1/5) and h_A = ½A⁻¹A* = (1/2, 0).
- **V** is the space of functions on Q spanned by K2∪K3∪K4.

## Summary

| Item | Status |
|---|---|
| (1) Profile S-law and T-law, closed-form M_S and M_T | **Proved** (Cat A). Correction: the factor is **\|x\|⁻¹**, not x⁻¹ |
| (2) Exact basis, dim V = 36, closure of V under S and T | **Proved / certified** (Cat A; upper bound proved, lower bound CC at two primes) |
| (3) V ≅ E with an explicit cyclotomic intertwiner; Hom(V⊗χᵏ, C) = 0 for all k | **Proved** (Cat A; intertwiner verified exactly in Q(ζ₅₈₈₀₀); Hom vanishing CC at two primes) |
| (4) K1 ≡ 0 | **Proved** (Cat A) |

## 1. The laws (Cat A, proof)
**Elementary rules.** These hold for all α, β ∈ Q² and all x:
- G_{α+n,β} = G_{α,β} for n ∈ Z².
- G_{α,β+λ} = e(B(α,λ))·G_{α,β} whenever Aλ ∈ Z². The reason is that B(n,λ) = nᵀAλ ∈ Z.
- G_{gα,gβ} = G_{α,β} for every automorph g ∈ GL₂(Z) with gᵀAg = A. This is a change of variables ν ↦ gν on the lattice coset; the integrand is periodic, so the mean is preserved.

**T-law.** For all α, β and all x:

G_{α,β}(x+1) = e(−Q(α) − B(α,h_A))·G_{α, β+α+h_A}(x).

*Proof.* Write ν = α+n. Then Q(n) = n₁² + 7n₁n₂ + (7/2)n₂² ≡ (7/2)n₂ ≡ ½nᵀA* = B(n,h_A) mod 1, using n₂² ≡ n₂ mod 2. Expanding gives Q(ν) ≡ B(ν, α+h_A) − Q(α) − B(α,h_A) mod 1, which is the law.

**S-law.** For all α, β and all x ∈ Q with x ≠ 0:

G_{α,β}(−1/x) = (1/(|x|·√35))·e(B(α,β))·Σ_{p∈D} G_{β+p,−α}(x).

*Proof (Poisson summation).*
1. **Set-up.** Put Z = yA + itI with t > 0, and f(ν) = exp(πi·νᵀZν + 2πi·B(ν,β)).
2. **Poisson summation:** Σ_{ν∈α+Z²} f(ν) = det(−iZ)^{−1/2} · Σ_{w∈Z²} e(wᵀα) · exp(−πi·(w−Aβ)ᵀZ⁻¹(w−Aβ)).
3. **Substitution.** Put w − Aβ = −Aγ. Then γ runs over β + A⁻¹Z², and e(wᵀα) = e(B(α,β) − B(γ,α)).
4. **Left side as t → 0.** The integrand is periodic, so a finite Fourier expansion and Poisson summation for the Gaussian give t·LHS → G_{α,β}(y), with an exponentially small error.
5. **Right side.**
   - **Determinant.** A has eigenvalues λ₁ > 0 > λ₂. With principal branches, det(−iZ)^{1/2} → √(|y|λ₁)·e^{∓iπ/4} · √(|y||λ₂|)·e^{±iπ/4} = |y|·√35, for either sign of y. Signature 0 means no eighth root of unity survives.
   - **Expansion of the quadratic form.** A·Z⁻¹·A = A/y − (it/y²)·I + O(t²). The O(t²) term changes the phase by O(t²|γ|²), which contributes O(1) against a main term of order 1/t.
   - **Mean on the dual side.** The main term is a periodic phase e(−Q(γ)/y − B(γ,α)) on the coset β + A⁻¹Z² (density 35) times the Gaussian e^{−πt|γ|²/y²}. Its sum is 35·(mean)·y²/t, and the mean over β + A⁻¹Z² equals (1/35)·Σ_p G_{β+p,−α}(−1/y).
6. **Conclusion.** Together: G_{α,β}(y) = (|y|/√35)·e(B(α,β))·Σ_p G_{β+p,−α}(−1/y). Putting y = −1/x gives the stated law. ∎

**Closed forms (Cat A).** `symbols.py` reduces every term with the elementary rules. On the 105 symbols K2∪K3∪K4:
- **M_S:** each row is (1/√35)·Σ of 35 terms of the form e(k/9800).
- **M_T:** monomial. It acts diagonally on K2 and swaps K3_μ ↔ K4_μ, with e(k/9800) phases.

The family K1 is closed on its own under both laws.

**Sign of x (Cat B corroboration, `floatcheck.py`).**
- On 72 rationals of both signs: the |x|⁻¹ law has error 5·10⁻¹⁵ and the T-law 1·10⁻¹⁵.
- The signed x⁻¹ version **fails for x < 0** (error 2).
- So item (1) as worded ("x⁻¹") is correct only for x > 0. The correct weight factor is |x|⁻¹.

## 2. Exact basis and dim V = 36 (Cat A)
- **Upper bound (proved).**
  - The automorph group search (`orbits.py`) gives 12 elements with |entries| ≤ 40, including ±I and γ = [[−1,−7],[2,13]].
  - Under these elements, the 105 symbols fall into **36 orbits**: 12 in each of K2, K3 and K4, of sizes 1, 2 and 4.
  - Within an orbit, every symbol equals e(k/9800) times the orbit representative. No orbit is forced to vanish.
  - So V is spanned by the 36 orbit representatives, and **dim V ≤ 36**.
  - Cross-check: the relation rank is 69 at two primes, and the relation span is closed under S and T.
- **Lower bound (CC).**
  - The Gauss means of all 105 symbols were evaluated **exactly mod p** at the 48 rationals h/m with m ≤ 6 and −2m ≤ h < 2m.
  - The primes were p = 1 764 001 and 6 468 001, both ≡ 1 mod 588 000, with ζ mapped to a root of unity in F_p.
  - The rank is **36** at both primes.
  - The values lie in Z[ζ][1/(4m)²], so the rank can only drop under reduction. Hence the char-0 rank is ≥ 36, and **dim V = 36**.
- **Consequences.**
  - The 36 orbit representatives form an **exact basis** of V.
  - The relation space is exactly the kernel of evaluation.
  - **V is closed under S and T**, because both laws hold for all x and map the symbols into the symbols.
  - The quotient matrices M_S and M_T on V are explicit cyclotomic matrices. They satisfy S⁴ = 1 and (ST)³ = S² mod p, for exactly one of the two roots of 35 mod p. That root is the same one that ρ_7|W selects.

## 3. V ≅ E, and no χᵏ-twisted map into C (Cat A)
**Mod-p Hom dimensions** (`exact_main.json`; A32's method; identical at both primes):
- End(V) = 1.
- Hom(V, E) = Hom(E, V) = Hom(V, W) = 1.
- **Hom(V⊗χᵏ, C) = Hom(C, V⊗χᵏ) = 0 for all k = 0, …, 11.**
- Hom(V⊗χᵏ, E) = 0 for k ≠ 0.
- Each mod-p dimension is an upper bound for the char-0 dimension, so every vanishing above is **exact**.
- E and C are coordinate blocks of W (orbit indices 26, 28, …, 36 form C), and the block-diagonal form was verified exactly.

**Explicit intertwiner** (`exact_intertwiner.py`), with N = 58 800:
- **T-eigenbases.** On V, T is monomial with 1- and 2-cycles, and its T-eigenbasis is exact over Z[½, ζ_N]. On E, T is likewise monomial.
- **T-spectra.** Both spectra consist of the same **36 distinct** values, in exact agreement.
- **The map.** X = P_E · Π · diag(c) · P_V⁻¹, where:
  - P_V and P_E are the exact eigenvector matrices (P⁻¹P = I checked exactly);
  - Π matches equal eigenvalues;
  - **every c_i is a root of unity ζ_N^{e_i}**. The exponents are listed in `exact_intertwiner.json`.
- **Exact verification.**
  - X·S_V = S_E·X: **0 of 1296 entries fail**, checked by reduction modulo the cyclotomic polynomial Φ₅₈₈₀₀. The factor 1/√35 (positive root on both sides) cancels.
  - X·T_V = T_E·X holds by the exact eigenvalue match.
  - X is invertible because it is a product of invertible factors.
- **Therefore V ≅ E, with no twist (proved).**
- Since dim V = dim E = 36, together with the vanishing Hom(V⊗χᵏ, C) = 0 for every k: **the 35-component law vector has no image in C under any η^{2k} twist, including χ³ (η⁶).** This upgrades A33's Cat B statements to Cat A.

## 4. K1 ≡ 0 (Cat A, proof)
1. **Zero at x = 0.** G_{α,a}(0) = e(B(α,a))·mean over n ∈ Z² of e(nᵀAa). Here Aa = (0, 7/2), so the mean is the mean of (−1)^{n₂}, which is 0. So K1(0) = 0.
2. **Closure.** The family K1 is closed under both laws (`symbols.py`): T maps K1 to K1 monomially, and S maps K1 to combinations of K1.
3. **Induction on the denominator.**
   - For an integer x = n: K1(n) = M_Tⁿ·K1(0) = 0.
   - For x = h/m with m ≥ 2: write x = n + r/m with 0 < r < m. By the S-law, K1(r/m) = (r/m)·M_S·K1(−m/r), and −m/r has the smaller denominator r.
4. **Conclusion.** Hence **K1 ≡ 0 on Q**, matching A33's floating-point observation.

## Not claimed
- **Scope of the S-law.** It is proved for the leading radial profiles (the 35-component law vector) only. Nothing is claimed about the cone sums beyond leading order.
- **Gauss-mean values.** The evaluations used for the lower bound are mod-p certificates, not full cyclotomic values.

## Status
- **Cat A:** items (1)–(4) as proved or certified above. The only correction is the |x|⁻¹ weight factor.
- **Cat B:** only the floating-point corroboration in `floatcheck.py`.
