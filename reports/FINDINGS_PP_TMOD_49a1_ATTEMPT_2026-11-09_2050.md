# FINDINGS (PP): discharging T-mod for 49a1 and its twists by a PP-checked CM argument. 2026-11-09, ~20:50 CST (America/Chicago)

- **Auditor:** Professor Proof (Soft SF). Audit only. Nothing adopted. No CERT. No Gemini. Nothing sent outside.
- **Additive file:** the 2030 file (69d33456…), 1949 (edcd9551…), 1955 (bc12df1a…) and 2025 (ac9fe667…) are not edited.
- **Tip:** /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad9…. It matched before and after; read only.
- **Naming:** "resonant algebra" (naming only).
- **Rule (OW 3f160803 as amended by 36683379, PP ruling):** a citation never makes a result PROVED by itself.
- **Evidence:** /workspace/audit-scratch/pp_tmod_49a1/. Every script and log has a .sha256 sidecar.

| File | sha256 (first 8 hex) | Content |
|---|---|---|
| pp_cm_49a1_v2.py / .log | b664ed61 / 2142b0fe | α: E → E, α*ω = ((1+√−7)/2)ω, 7-kernel, Δ² |
| pp_cm_49a1_xmap.py / .log | cc648b84 / cc38b659 | reduced x-map of α, its resultant and denominators |
| pp_theta_psi_gamma0_49_v2.py / .log | ff6b3f50 / 2ffc6081 | exact Γ₀(49)-invariance certificate for θ_ψ |
| pp_tmod_arith.py / .log | 68bf6843 / 93a78b46 | c(n) = a_n(E); PARI f; W₄₉; V7/V9 matrices |
| pp_tmod_twists_v2.py / .log | 831e440e / 0fdf3195 | Gauss sums, conductors, a_p and ε of all twists |

Superseded runs are kept: pp_cm_49a1 (v1 crashed after its first checks), pp_theta_psi v1 (wrong sanity relation, explained in §2), and pp_tmod_twists v1 (sign typo, explained in §3).

## 0. Route choice
**Option A (CM, Deuring/Hecke done by hand) was chosen.**
- Option B (Livné) needs more unverified machinery: ℓ-adic Galois representations of both sides, the Eichler–Shimura relation for the comparison form, and Chebotarev density. Those are deep, and each would be a residual citation.
- Option A needs only:
  - textbook elliptic-curve foundations, which the 2030 file already used without a tag in V2–V4;
  - Poisson summation on ℝ²;
  - elementary algebraic number theory.
- Everything specific to 49a1 is proved below and checked by exact computation.

## 1. Base F0: residual cited facts
These are textbook facts, not specific to this problem. The 2030 file already relies on F0-1 to F0-4 inside V2, V3 and V4 without a tag.

| Tag | Precise statement | Status |
|---|---|---|
| F0-1 | Silverman AEC III.4, III.6, II.2. Isogenies are group homomorphisms. End(E) is a ring. The dual satisfies φ̂φ = [deg φ]. deg is a positive definite quadratic form on End(E), and (φ+ψ)^ = φ̂+ψ̂. #ker φ = deg φ for separable φ. deg φ equals the degree of the x-coordinate map | textbook; same layer as V2/V4; not re-derived this session |
| F0-2 | Silverman III.5.2, II.4.2. (φ+ψ)*ω = φ*ω + ψ*ω. In characteristic 0, φ ↦ φ*ω/ω is an injective ring homomorphism End(E) → K̄ | textbook; same layer |
| F0-3 | Silverman V.1, II.2.11. For the q-power Frobenius π: #E(F_q) = deg(1−π) and π + π̂ = a_q | textbook; already used in V2/V4 |
| F0-4 | Silverman VII.2.1 and §VII.3. At a prime of good reduction, reduction of points is a homomorphism. An endomorphism whose rational map is 𝔭-integral reduces to an endomorphism of Ẽ, and reduction respects + and ∘ | textbook; same layer |
| F0-5 (T-PSF) | Poisson summation Σ_{m∈M} g(m+h) = vol(M)⁻¹ Σ_{μ∈M*} ĝ(μ) e(μ·h) for Schwartz g on ℝ². Proof: the periodization is smooth and periodic, and the Fourier series of a smooth function on the torus converges absolutely to it | standard analysis; PP checked the proof outline; Fourier inversion on the torus is the only foundational input |
| F0-6 | O_K = ℤ[ω], ω = (1+√−7)/2, is norm-Euclidean, hence a UFD with units ±1. p splits ⇔ x²−x+2 has a root mod p. Quadratic reciprocity (p/7) = (−7/p) follows from g₇² = −7 | **PP verified**: h(−7) = 1 from reduced forms (only (1,1,2)); g₇² + 7 = 0 in ℤ[ζ₇], exact; reciprocity also checked for p < 10⁵ |

The deep cited theorems are **no longer used** for 49a1 and its twists: T-mod, T-Hecke, and the T-tw and T-AL sign laws in the instances needed (§3). Still cited: T-AL (newform part), T-GZK, T-theta, C2, C3.

## 2. Theorem M (PP). L(49a1, s) = L(θ_ψ, s) with θ_ψ ∈ S₂(Γ₀(49)), θ_ψ|W₄₉ = −θ_ψ, and FE sign +1 = ellrootno(49a1)
Notation:
- E = [1,−1,0,−2,−1]; K = ℚ(√−7); O = ℤ[ω].
- χ(λ) = (λ mod √−7 | 7), using O/√−7 ≅ F₇ with ω ↦ 4.
- θ_ψ = ½ Σ_{λ∈O} χ(λ) λ q^{Nλ}.

**(a) The CM endomorphism** (pp_cm_49a1_v2, _xmap; exact sympy/PARI over K).
- φ is Vélu's 2-isogeny with kernel T = ((−5+√−7)/8, ·).
- ι: E′ → E is PARI's ellisisom, [u, r, s, t] = [(−1−√−7)/2, (5−√−7)/8, (−3−√−7)/4, (−5+√−7)/16].
- α := [−1]∘ι∘φ.
- Checked exactly:
  - α maps E to E: the curve equation holds modulo the ideal.
  - α*ω = c·ω with c = (1+√−7)/2, which satisfies c² − c + 2 = 0.
- The reduced x-map is X_α = (−(3+√−7)/8·x² + (√−7−1)/4)/(x + (5−√−7)/8), of degree 2.
- The coefficient denominators involve only 2. The norm of the resultant is 7²/2⁶.
- By F0-2, α² − α + 2 = 0 and the conjugate α^σ = 1 − α in End(E). So ℤ[α] ≅ O via α ↦ ω, and ^ corresponds to complex conjugation.
- For p ∤ 14, α reduces modulo every 𝔭 | p to α_p with the same relations and degree 2 (F0-4).

**(b) Inert p ∤ 14.**
- The coefficients of α_p lie in F_{p²}, and Frobenius acts on them as σ. So π∘α_p = (1−α_p)∘π.
- With s = 2α_p − 1 (deg s = 7, so s is invertible in End⊗ℚ): πs = −sπ.
- Then s(1+π)s⁻¹ = 1 − π, so deg(1+π) = deg(1−π), so 1 + a_p + p = 1 − a_p + p, so **a_p = 0**.
- θ_ψ has no element of norm p, so its coefficient is 0 as well.

**(c) Split p ∤ 14.** Here α_p is defined over F_p, so π commutes with α_p. Let F = ℚ(α_p, π) ⊂ End(E_p)⊗ℚ.
- F is commutative and stable under ^, since α̂ = 1 − α and π̂ = a_p − π.
- For x ≠ 0, x x̂ = deg x > 0, so F is a field.
- Every x in the fixed field F₀ of ^ satisfies x² = deg x ∈ ℚ. Hence F₀ = ℚ: if x ∉ ℚ, then (x+1)² ∈ ℚ forces x ∈ ℚ.
- So F = ℚ(α_p) ≅ K. π is integral, so π ↔ π_K ∈ O with N(π_K) = p and a_p = Tr π_K.

**(d) Which prime above p.**
- The cubic x³+x²−2x−1 divides ψ₇ (pp_tmod_arith [A]). Its disc is 49.
- Checked exactly: x(2P) is again a root, and X_α maps the roots to roots. Hence ⟨P⟩ is α-stable. α acts on it by a root of x²−x+2 mod 7, which is 4 (double root).
- So ⟨P⟩ = ker(2α−1) = ker √−7.
- Let Δ = ∏_{k=1,2,4}(2y+x)(kP). Since (2y+x)² = 4x³−3x²−8x−4, Δ² = Res(cubic, 4x³−3x²−8x−4) = **−343** (exact).
- Mod p (split, p ∤ 14): (−7/p) = 1, so Δ̃ ∈ F_p^×. π acts on ⟨P̃⟩ as c ≡ π_K mod √−7.
- If c were a non-residue, then c·{1,2,4} = −{1,2,4} and (2y+x)(−Q) = −(2y+x)(Q), so Δ̃^p = −Δ̃. That would give Δ̃ = 0, a contradiction.
- So χ(π_K) = 1 = χ(π̄_K), because conjugation is trivial on O/√−7. Since χ(−1) = −1, θ_ψ's p-th coefficient is ½·Σ_{±π_K, ±π̄_K} χ(λ)λ = π_K + π̄_K = **a_p**.

**(e) Euler products.**
- θ_ψ's coefficients are Σ_{N𝔞=n} ψ(𝔞) with ψ(λO) = χ(λ)λ. This is well defined because χ(−λ)(−λ) = χ(λ)λ, and it uses F0-6.
- Split p: ψ(𝔭)ψ(𝔭̄) = p.
- Inert p: ψ(pO) = (p/7)·p = −p, giving the local factor 1 + p^{1−2s}.
- p = 7: the local factor is 1, matching additive reduction with a₇ = 0.
- p = 2: a₂ = 1 = Tr ω with χ(ω) = (4|7) = 1, computed directly.
- So **c(n) = a_n(E) for all n**. As a check, c(n) = a_n for all n ≤ 4000 (exact) and the w-part vanishes.

**(f) Modularity of θ_ψ** (pp_theta_psi_gamma0_49_v2). Take the lattice M = √−7·O ⊂ ℂ, with Q = N, Gram_B = [[14,7],[7,28]], and |D| = |M#/M| = 343.
- Define Θ_δ = Σ_{m∈δ+M} m·e(τQ(m)). Then θ_ψ = v·Θ with v = ½(k|7) on k·1 ∈ O/M.
- PP derived the transformation laws from F0-5 and the Gaussian transform (computed in the file):
  - Θ|₂T = diag(e(Q))Θ;
  - Θ|₂S = (i/(7√7))[e(B(δ,h))]Θ, where i/(7√7) = g₇/49.
- **The certificate:**
  - Γ₀(49) has 56 cosets and 48 Schreier generators (length ≤ 24, at most 10 S letters).
  - v·R(g) = v holds for **every** generator, modulo 95 primes ℓ ≡ 1 (mod 49), ℓ < 2²⁶, at one degree-1 prime each.
  - Norm bound: the entries of β = 2·49^s(vR(g) − v) lie in ℤ[ζ₄₉], and |σβ_i| ≤ 2·49^s(√6/2 + ½), because σ(R) stays unitary. So |N β_i| ≤ 10^732.5, while the product of the ℓ is 10^743.5. Hence β = 0 exactly.
  - Sanity checks on the odd subspace, where Θ lives (Θ_{−δ} = −Θ_δ): S⁻¹S = I, S² = I and (ST)³ = I pass for every ℓ.
  - v1's sanity check wrongly tested S⁴ and (ST)³ on all of ℂ³⁴³, where S² = −1 on the even part. Its generator test was identical and also passed.
- Cuspidality: every θ_ψ|γ is a combination of the Θ_δ, and the m = 0 term vanishes because P(0) = 0.
- **So θ_ψ ∈ S₂(Γ₀(49)).**

**(g) Fricke sign without Sturm.**
- The S-law at 49τ gives θ_ψ|W₄₉ = g₇·Σ_δ ĉ(δ)Θ_δ(49τ), with ĉ(δ) = ½(7Trδ|7)g₇. That equals −½Σ_{λ∈O}(Trλ|7)λ q^{Nλ}.
- Since Tr(a+bω) = 2a+b ≡ 2(a+4b) mod 7 and (2|7) = 1, (Trλ|7) = χ(λ) identically (checked over O/7O).
- **So θ_ψ|W₄₉ = −θ_ψ.**
- By V1, Λ(E,s) = +Λ(E,2−s). ellrootno(49a1) = +1 (exact), and PARI's mfatkininit also gives w₄₉ = −1.
- Float sanity only (not used): |θ(−1/(49τ)) + 49τ²θ(τ)| ≈ 1.5e−16, and |θ|γ − θ| ≈ 1.3e−13 near the cusp −92/245.
- Consequence for row 2a: PARI's newform f lies in S₂(Γ₀(49)) (computational base), its coefficients equal c(n) for n ≤ 600, and the Sturm bound is 9.33. By V5, **f = θ_ψ**.

**Theorem M is PROVED on base F0.** No modularity, Hecke, Deuring or Atkin–Lehner theorem is cited.

## 3. Twists (V7, V9 now PP-proved; pp_tmod_arith [E], pp_tmod_twists_v2)
- **V7 (twist modularity).** Let χ be primitive quadratic mod r. Then f_χ = g(χ)⁻¹Σ_u χ(u) f|[[1,u/r],[0,1]] is the coefficient twist.
  - This uses Σ_u χ(u)e(nu/r) = χ(n)g(χ) for all n. It was checked exactly by mod-ℓ plus a norm bound for r = 20, 40, 44, 53, 57, 172, 188, 248, 264, 316, together with primitivity.
  - For γ = [[a,b],[Nr²k,d]], the matrix [[1,u/r],[0,1]]γ[[1,−ud²/r],[0,1]] lies in Γ₀(N). Symbolically, its upper-right entry is b − Nd²ku² − Nbdkru (integral).
  - So f_χ ∈ S₂(Γ₀(Nr²)) with character χ(d)² = 1.
  - This replaces T-tw (Shimura 3.64) in the instances used.
- **V9 (Fricke sign of a twist).** With v ≡ −(Nu)⁻¹ mod r and γ_u = [[r,−v],[−Nu,(1+Nuv)/r]] ∈ Γ₀(N), det = 1:
  - [[1,u/r],[0,1]]·W_{Nr²} = r·W_N·γ_u·[[1,v/r],[0,1]], an exact symbolic identity.
  - Hence f_χ|W_{Nr²} = w·χ(−N)·f_χ whenever f|W_N = w·f and (r,N) = 1.
  - This replaces the T-AL **sign law** for these instances. Newform theory is not needed for this.
- **Instances** (all exact, pp_tmod_twists_v2). The curves are Ξ = elltwist(E,140), E^{−20}, and E^D for the nine N2 discriminants D ∈ {40, 44, 53, 57, 172, 188, 248, 264, 316}.
  - All D are fundamental and coprime to 7. For Ξ, χ₁₄₀ = χ₋₂₀χ₋₇.
  - Each conductor N(E^D) = 49D² equals the level of f_χ.
  - Every bad p has a_p = 0.
  - a_p(E^D) = χ(p)a_p(E): by V3 for good p; for Ξ this uses χ₋₇(p) = 1 whenever a_p ≠ 0. Also checked for p < 6000.
  - So L(E^D, s) = L(f_χ, s).
  - The predicted sign ε = −χ(−49)·w(θ_ψ) = χ(−1) equals ellrootno in all 11 cases: −1 for Ξ and E^{−20}, +1 for the nine.
  - The v1 log printed "match: False" because of a spurious extra factor −1 in the prediction code. That is fixed in v2, and the data are otherwise identical.
- **R_{χ₁₄₀}θ_ψ = R_{χ₋₂₀}θ_ψ identically.** c is multiplicative, c(7^j) = 0, c vanishes at odd powers of inert primes, and χ₋₇ = 1 on split primes and on squares. Checked for n ≤ 5000.

## 4. Which 2030 rows move (all relative to base F0, the same base as V2–V4)
| Row (2030 grade) | New grade | Basis |
|---|---|---|
| E1 ε = −w_N (C on T-mod) | **PROVED** for the instances used (49a1, Ξ, the N2 twists); the general claim for all E is not made | §2(g), §3, V1 |
| E2 w₁₉₆₀₀ = −ε = +1 (C on T-mod) | **PROVED** | V9: w = χ₋₂₀(−49)·(−1) = +1, computed rather than deduced from E1 |
| E4 XW L68, w-reading (C on T-mod) | **PROVED** | V9 instance |
| E5 w₁₉₆₀₀ = w₄₉·χ₋₂₀(−49) (C on T-mod or T-AL) | **PROVED** | V9 |
| E9 "same newform" (C on T-mod) | **CONDITIONAL on T-AL-new** (narrowed) | PROVED: L(Ξ) = L(E^{−20}) = L(R_{χ₋₂₀}θ_ψ), one modular form in S₂(Γ₀(19600)). Not proved: that this form is a *newform* of level 19600 (Atkin–Lehner/Li newform theory). 2g only excludes level 980 |
| E11b analytic ranks (C on T-mod) | **PROVED** | the FE of L(Ξ) and L(49a1) is now proved (V1 + §2–3), and the rapidly convergent series follow from Hecke's integral. The arb certificate was already sound |
| 2a f = θ_ψ (C on T-Hecke) | **PROVED** | §2(f) + V5 |
| 2c f_Ξ = R_{χ₁₄₀}f = R_{χ₋₂₀}f (C on T-mod and T-tw) | **PROVED** | the identity of q-series is exact and needs no Sturm bound; modularity at 19600 comes from V7 |
| 2d w₁₉₆₀₀(f_Ξ) = +1 (C on T-AL) | **PROVED** | V9 + §2(g) |
| N2 nine twists, L(1) = 0 (C on T-GZK and T-mod) | **CONDITIONAL on T-GZK** only (narrowed) | the L-functions, their FE and ε = +1 (even order) are now PROVED. Getting L(1) = 0 from rank 2 needs "L(1) ≠ 0 ⇒ rank 0" (Kolyvagin, or Coates–Wiles 1977 for CM): still cited |
| 2f (C on T-tw and T-theta) | **CONDITIONAL on T-theta** only (narrowed) | T-tw is replaced by V7 |
| 1955 C4 (C on T-mod) | **PROVED** | follows from E11b; the bc12df1a tally returns to **4/0/0/0/0** |
| 2025 B2′ (C on T-Hecke) | **PROVED** | the zero set of a_p comes from §2(b), (c) |

Unchanged: 2b and 2f′ (T-theta); 3b-i, 3b-ii(b), N1, O-a, A4 (C2/C3); B2, B3 (twist lemmas from the 2025 file, which are not the V7 setting; not re-examined here); E11a and 3d (float).

## 5. Revised Local rollup (replaces 29/23/7/1/1)
| Block | P | C | O | R | PENDING |
|---|---|---|---|---|---|
| Erratum E1–E11b (12) | 10 (+E1, E2, E4, E5, E11b) | 2 (E9, E11a) | 0 | 0 | 0 |
| Bridge C + PP (25) | 11 (+2a, 2c, 2d) | 9 | 4 | 1 | 0 |
| 2025 new rows | 17 (+B2′) | 3 (A4, B2, B3) | 3 | 0 | 1 |
| **Total (61)** | **38** | **14** | **7** | **1** | **1** |

**PROVED 38 · CONDITIONAL 14 · OPEN 7 · REFUTED 1 · PENDING 1, plus V₈₄.**

Disclosure on F0:
- The nine upgrades rest on F0, the same textbook layer the 2030 file already accepted inside V2–V4.
- If the Owner wants F0-1 to F0-5 tagged under the strict rule, all nine would read "CONDITIONAL on F0". Every V2/V4-dependent row would then need the same tag, so applying it consistently would require a separate ruling.
- PP does not claim more than this.

## 6. Fixes for Local (additive)
1. Carry the §4 grades. Tag E9 with T-AL-new, N2 with T-GZK, and 2f with T-theta.
2. Cite this file and pp_tmod_49a1 for modularity, and drop "Deuring–Hecke/BCDT cited" for 49a1 and its twists.
3. State E1 only for the instances proved, not for every E.
4. N2: say "ε = +1 PROVED; L(1) = 0 CONDITIONAL on Kolyvagin or Coates–Wiles".
5. E11b: "analytic rank 1 (Ξ) and 0 (49a1), PROVED on base F0; no GZK used".

PP findings only. Nothing adopted. No CERT. Tip 7cddb188 untouched. No external sends. No Gemini.
