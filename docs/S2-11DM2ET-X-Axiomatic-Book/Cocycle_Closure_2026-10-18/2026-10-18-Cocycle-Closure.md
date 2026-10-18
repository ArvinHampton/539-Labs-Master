> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** The pre-§3A backup (.bak) is not included. §3B numerics are Cat B support for the Cat A proof in §3A. Category convention for Master (rev. 5): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Naming as in rev. 4: W_P = Fix(P); V_Eis/d_Eis = Eisenstein span/dimension; Theorem G = Lewis–Zagier; Lemma Prod1/Prod2; d_2(k,v). No 'Theorem L' label is introduced (Theorem L = the framework's Parity Dominance Theorem; Lemma L keeps its name). Erratum: ERRATUM_Consolidated_Rev5_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev5_2026-10-18/ (§13). No TPC/RH claim; distinct from HQCC termination claims; CORE_FREEZE holds.

# E-part cocycle: closure ((a) the constant, (b) the boundary step, (c) general cusps)

Date: 2026-10-18, about 18:20 CDT. Local only; nothing pushed. Builds on `2026-10-18-Open-Analytic.md` §4 (cocycle_gamma.py/.json) and `2026-10-17-psi-Cocycle.md` (A1–A4).
Labels: **Cat A** = proved; **Cat B** = numerical only. No TPC/RH claims.
Folder: `2026-10-18-Cocycle-Closure/`.

Notation:
- The Green form is [u,v] = u_w v dw + u v_{w̄} dw̄, and R_z(w) = Im w/((w−z)(w̄−z)).
- u_L(w) = √y Σ_{ν∈(a+Z²)/⟨γ⟩} K₀(2π|Q(ν)|y) e(Q(ν)x). It has **no constant term**, because Q has no zero on a+Z².
- f_u(z) := Σ_{n>0} A_n e(nz) is the Lewis–Zagier f-function of u = √y Σ A_n K₀(2π|n|y)e(nx) + b√y.
- γ′ = [[a,b],[c,d]], r := γ′⁻¹∞.

## 0. Status

| Item | Result | Status |
|---|---|---|
| (a) The constant | C = −π/2 derived by hand: the exact identity I_n(z) = C·e(nz), plus the y → ∞ asymptotics of the explicit integrand. Quadrature agrees to 18 digits | **A** |
| (b) Boundary step H → ℝ, both signs of cx+d | The radial expansion holds non-tangentially (sector-uniform Euler–Maclaurin). The singular terms cancel, and the branch sign is ε = sgn(cx+d), which gives the \|cx+d\| factor | **A** |
| (c) General γ′ (cusps not equivalent to ∞ under the multiplier group of u_L) | Vector identity with the constant-term vector b. It reduces exactly to the psi-Cocycle S-formula. The u-vector law u∘γ′ = ρ(γ′)u is now proved label by label (§3A); numerical test at STS, ST²S, ST³S in §3B | **A** (§3A proof; the numerics in §3B are Cat B support) |
| Numerical support | Cocycle at 45 rationals to 7e−13 (Open-Analytic). S-case at 84 rationals to 1e−13 (psi). Non-tangential κ fits in 4 directions, error going down with the step size | B (support only) |

## 1. (a) The constant C = −π/2 (Cat A)

Fix n > 0 and set f(Y) = √Y·K₀(2πnY) and u = f(Y)e(nX). Let I_n(z) = ∫_z^{z+i∞}[u, R_z^{1/2}].

**Step 1: I_n(z) = C·e(nz)** (psi-Cocycle A2, restated).
- R_z(w) is holomorphic in z.
- The z̄-derivative of the moving lower limit contributes the dw̄-part of the integrand at w = z. That part vanishes, since v_{w̄} ~ (w−z)^{1/2}.
- So I_n is holomorphic. It is also translation-covariant, i.e. e(nx)·g(y). A holomorphic function of this form must be C·e(nz).

**Step 2: the integrand on the ray w = z + is.** Use ∂_w = ½(∂_X − i∂_Y) and ∂_{w̄}R = (i/2)(w̄−z)⁻². On the ray:
- R = (y+s)/(s(2y+s)) and (w̄−z)² = −(2y+s)².
- dw = i ds and dw̄ = −i ds.

This gives

 I_n(iy) = ∫₀^∞ [ −½(2πn f − f′)(y+s)·R^{1/2} − ¼ f(y+s)·R^{−1/2}(2y+s)^{−2} ] ds.

Check: the n = 0 case (f = √Y) reproduces (y/2)s^{−1/2}(2y+s)^{−3/2}, whose integral is 1/2.

**Step 3: y → ∞.**
- f(Y) = (2√n)⁻¹e^{−2πnY}(1 + O(1/Y)) and f′ = −2πn f(1 + O(1/Y)), uniformly.
- R^{1/2} = (2s)^{−1/2}(1 + O(s/y)).
- The second term is O(y⁻²)·e^{−2πny}.

By dominated convergence (majorant ≲ s^{−1/2}(1+s)^{1/2}e^{−2πns}):

 e^{2πny} I_n(iy) → −2πn·(2√n)⁻¹ ∫₀^∞ e^{−2πns}(2s)^{−1/2} ds = −π√n · Γ(½)/(√2·√(2πn)) = **−π/2**.

Since e^{2πny}I_n(iy) = C exactly, **C = −π/2**.

For n < 0 the integral is bounded but would equal C′e^{2π|n|y}, so it is 0.

Hence, termwise (absolute convergence, exponential decay):

 **∫_z^{i∞}[u, R_z^{1/2}] = −(π/2)·f_u(z) + b/2.**

For u_L, f_{u_L} = 2E_L and b = 0, so **E_L(z) = −(1/π)∫_z^{i∞}[u_L, R_z^{1/2}]**.

Quadrature check (`c0_check.py/.txt`): e^{2πny}I_n(iy)/(−π/2) = 1 − O(10⁻¹⁸) at n = 1, 2 and y = 0.3, 1, 3.

## 2. (b) From H to rationals, both signs of cx+d (Cat A)

Assume u_L∘γ′ = u_L.

**2.1 Identity on H.**
1. R_{γ′z}(γ′w) = (cz+d)²R_z(w). This is a direct computation from Im γ′w = Im w/|cw+d|² and γ′w − γ′z = (w−z)/((cw+d)(cz+d)).
2. The Green form commutes with holomorphic pullback.
3. The vertical ray from γ′z pulls back to the geodesic from z to r.
4. Fix a branch ρ_z of R_z^{1/2} on H minus a cut from z to ℝ. The cut lies in the component of H ∖ (vertical ray ∪ geodesic) that does not contain the closing path, so ρ_z is the positive root on the vertical ray. On the geodesic, ρ_z = ε(z)(R_{γ′z}∘γ′)^{1/2}/(cz+d), where ε(z) ∈ {±1} is locally constant.
5. Closedness of the form gives

 **E_L(z) − ε(z)(cz+d)⁻¹E_L(γ′z) = −(1/π)∫_r^{i∞}[u_L, ρ_z] =: P(z).**

The integral converges at both ends, with no cuspidality needed:
- at i∞, u_L decays exponentially (no constant term);
- near r, u_L(w) = u_L(γ′w) with Im γ′w ≍ |w−r|⁻² along non-tangential paths, so the decay beats any algebraic growth of ρ and ρ_{w̄}.

**2.2 Non-tangential radial expansion.** At rational x,
- E_L(x+h) = Σ_ν e(xQ(ν))e^{−tQ(ν)} with t = −2πih;
- e(xQ) is periodic on a+Z² modulo a sublattice, so E_L is a finite combination of shifted-lattice cone sums of e^{−tQ}.

The closed cone F has Q ≥ δ|v|², since both edges have positive norm. So e^{−e^{iφ}Q} is Schwartz on F, with all seminorms uniform for |φ| ≤ π/2−δ′. The proved 2-D Euler–Maclaurin expansion (Open-Analytic §2: 1-D Zagier lemma, quadrant lemma, cone decomposition) has remainders given by explicit integrals of B̃_N against derivatives of f(tv). These are bounded uniformly in such sectors. Hence

 **E_L(x+h) = A(x)/t + κ_L(x) + O(|t|)** as h → 0 in any sector δ′ ≤ arg h ≤ π−δ′ (Cat A).

Numerical support (`nontangential_check.py/.txt`, s = 7, x = 1/2, 1/3, 2/5): fitted κ agrees with the exact value equally well in the directions φ = 30°, 45°, 90° and 135°. The errors are 2e−5 to 8e−4 and shrink with the step size (fit-limited). This is B, support only.

**2.3 The limit.** Let z → x non-tangentially, with cx+d ≠ 0 and x ≠ r. Then γ′z → γ′x non-tangentially (Möbius maps are conformal). Put t′ = −2πi(γ′z − γ′x) = t/((cz+d)(cx+d)). Then

 (cz+d)⁻¹E_L(γ′z) = A(γ′x)(cx+d)/t + κ_L(γ′x)/(cx+d) + O(t).

The singular part has no constant leftover, because (cz+d)⁻¹/t′ = (cx+d)/t exactly.

- **Right side.** For z → x the cut shrinks to a segment ending at x. ρ_z → R_x^{1/2} > 0, uniformly on compact subsets of H. The endpoint regions are dominated (|w−z| ≥ dist(x,r)/2 near r; R ~ 1/Im w at i∞). So P(z) → P(x) = −(1/π)∫_r^{i∞}[u_L, R_x^{1/2}], which is finite.
- **Singular terms.** Boundedness forces A(x) = ε(cx+d)A(γ′x).
- **Branch.** At real x, both R_x and R_{γ′x}∘γ′ are positive on H. The positive roots satisfy (R_{γ′x}∘γ′)^{1/2} = |cx+d|·R_x^{1/2}, so ε(x)(cx+d) = |cx+d|, i.e. **ε = sgn(cx+d)**.
- **Constant terms:**

 **κ_L(x) − |cx+d|⁻¹κ_L(γ′x) = −(1/π)∫_{γ′⁻¹∞}^{i∞}[u_L, R_x^{1/2}]**, for both signs of cx+d.

By-product: A(x) = |cx+d|·A(γ′x), the |·|-law of the singular profile.

On H with cx+d < 0 the identity reads E_L(z) + (cz+d)⁻¹E_L(γ′z) = P(z). This is why the holomorphic factor misses on that side (cocycle_holfactor.txt).

## 3. (c) General γ′: vector-valued version

Let u = (u_λ) be the full label vector (the 72-component Fix(P) vector, or all 140 labels). Assume u∘γ′ = ρ(γ′)u, with ρ generated by the matrices of Theorem 5.1 (S: e(B(α,β))/√35·Σ_p; T: phase and label shift).

Two facts:
- **Constant terms.** Only labels with α ∈ Z² have one, b_λ = log ε·e(B(0,β)) = log ε. The orbit of ν = 0 gives √y × (geodesic length).
- **f-functions.** f_{u_{α,β}} = E_{α,β} + E_{−α,−β}. This holds because ν ↦ −ν maps the −F branch of α+Z² onto F ∩ (−α+Z²) and the phase becomes e(B(·,−β)). For (a,0), the automorph R gives f = 2E_L.

Write Ê := f_u and Ẽ := ∫_z^{i∞}[u, R_z^{1/2}] = −(π/2)Ê + b/2 (§1). The argument of §2.1, now carried out with the vector, gives Ẽ(γ′z) = ε(cz+d)ρ(γ′)[Ẽ(z) − P̃(z)] with P̃ = ∫_r^{i∞}[u, ρ_z]. Near r the constant-term part gives an O(Im⁻²) integrand, so it converges. The limit of §2.3 then gives, at rational x ≠ r:

 **Ê(x) − |cx+d|⁻¹ρ(γ′)⁻¹Ê(γ′x) = −(2/π)∫_r^{i∞}[u, R_x^{1/2}] + (1/π)(b − |cx+d|⁻¹ρ(γ′)⁻¹b)**,

where Ê(x) means the vector of radial constants κ̂_λ.

Consistency checks (exact algebra):
- **Trivial multiplier on the L-row** (b_L = 0): this is §2.
- **γ′ = S** (r = 0, a cusp not equivalent to ∞ under the group of u_L). Take the L-row of the form Ê(γ′z) = ε(cz+d)ρ(γ′)[Ê + (2/π)P̃] − (1/π)(ε(cz+d)ρ(γ′)b − b), with ρ(S)_{L,·} = (1/√35)Σ_p e_{p,−a} and Σ_p b_{p,−a} = log ε. For x > 0 this gives

  κ_L(−1/x) − (x/√35)κ_R(x) = (x/(π√35))(∫_0^{i∞}[u_R, R_x^{1/2}] − (log ε)/2).

  That is exactly the psi-Cocycle formula, verified there at 84 rationals to 1.1e−13. For x < 0 it gives the |x| version (psi A4).
- Every γ′ is a word in S and T. T acts by phases and label shifts and has no integral term. The cocycle relation of the right-hand sides is the Stokes additivity of ∫_r^{i∞}.

**Status of (c).** Cat A. The vector law it relied on is proved in §3A (Poisson at a fixed majorant, T-law, reductions, exact γ²-periodicity, cycle integration; b is carried inside the theta identity). The full 140-row identity is confirmed numerically in §3B to ≤ 3e−12.

## 3A. The vector law u∘γ′ = M(γ′)u, label by label (Cat A)

Setting (s = 7): A = [[2,7],[7,7]], Q(ν) = ½νᵀAν, B(ν,μ) = νᵀAμ, L′ = A⁻¹Z² with |L′/Z²| = 35, a = (7/10, −1/5), γ = [[−1,−7],[2,13]] ∈ SO(A), ε = 6+√35. The labels are λ = (α,β) with α ∈ ({0,a}+L′)/Z² (70 classes) and β ∈ {0,−a}, so 140 labels in all.

**Step 0. Theta at a fixed majorant.** Take the geodesic of majorants c(t), t ∈ R, so that Q = Q₊,t + Q₋,t, where Q₊,t is positive definite and Q₋,t is negative definite. Set Q̃_t := Q₊,t − Q₋,t, which is positive definite. Take G_τ,t(ν) = e(τQ₊,t(ν) + τ̄Q₋,t(ν)) and

  Θ_{α,β}(τ; t) = Σ_{ν∈α+Z²} e(B(ν,β)) G_τ,t(ν).

For τ ∈ H we have |G| = exp(−2π Im τ · Q̃_t(ν)). So the series converges absolutely, uniformly for t in compacts and τ in compacts of H.

**Step 1. Poisson lemma (the Theorem 5.1 step-1 lemma at the fixed majorant).** The Fourier transform of ν ↦ G_τ,t(ν) is Ĝ(ξ) = det(−iM)^{−1/2} exp(−πi ξᵀM⁻¹ξ), where M = τA₊ + τ̄A₋ (with A± the Gram matrices of 2Q±). The matrix M has one eigen-direction with factor τ and one with τ̄. So det(−iM)^{1/2} = (−iτ)^{1/2}(iτ̄)^{1/2}·√|det A| = |τ|√35: the two square roots are complex conjugates.

Poisson summation over α+Z², with the character e(B(ν,β)), gives the dual sum over ξ ∈ Aβ + Z². Writing ξ = Aη with η ∈ β + L′, we get G_{−1/τ},t(Aη)ˆ = (|τ|/√35) G_τ,t(η). Splitting L′ = ⊔_{p∈L′/Z²}(p+Z²) gives

  Θ_{α,β}(−1/τ; t) = (|τ| e(B(α,β))/√35) Σ_{p∈L′/Z²} Θ_{p−β, α}(τ; t)   (every t; eq:thetaS of rev4).

The identity holds at the level of all terms, including ν = 0 and η = 0. Both sides are the full absolutely convergent sums.

**Step 2. T-law.** For n ∈ Z², Q(n) ≡ B(n,w_c) mod 1, where w_c = A⁻¹(0,½) = (1/10, −1/35). This is exact: Q − B(·,w_c) is additive mod 1 because B(n,m) ∈ Z, and it vanishes on generators (labels_exact.txt). Also G_{τ+1},t(ν) = e(Q(ν))G_τ,t(ν), since Q = Q₊ + Q₋. For ν = α+n,

  e(Q(ν)) = e(Q(α)) e(B(α,n)) e(B(n,w_c)) = e(−Q(α) − B(α,w_c)) · e(B(ν, α + w_c)).

Hence Θ_{α,β}(τ+1; t) = e(−Q(α) − B(α,w_c)) Θ_{α, α+β+w_c}(τ; t).

**Step 3. Reductions (immediate from the definition).**
- Θ_{α+n,β} = Θ_{α,β} for n ∈ Z².
- Θ_{α,β+μ} = e(B(α,μ)) Θ_{α,β} for μ ∈ L′, since B(n,μ) ∈ Z.
- Θ_{−α,−β} = Θ_{α,β}, by ν ↦ −ν, using G(−ν) = G(ν).

Exact check (labels_exact.py): every right-hand label in Steps 1–2 reduces this way to one of the 140 family labels. That is, p−β ∈ {0,a}+L′ and α ∈ {0,−a}+L′, and likewise for the T-target and the parity target. The resulting matrices are exactly F.Smatrix() and F.Tmatrix() (2026-10-18-S-Eigenvalues/family.py).

**Step 4. Cycle integration and the γ²-periodicity.** γ acts on the majorants by c(t) ↦ c(t + log ε), and G_τ,t(γν) = G_τ,t−log ε(ν). Substituting ν = γ²μ gives

  Θ_{α,β}(τ; t + 2log ε) = Σ_{μ∈γ⁻²(α+Z²)} e(B(μ, γ⁻²β)) G_τ,t(μ) = Θ_{γ⁻²α, γ⁻²β}(τ; t).

Exact check: k = 2 is the common stabiliser order (family.gamma_order() = 2). That is, γ²α ≡ α mod Z², γ²β − β ∈ L′, and B(α, γ²β−β) ∈ Z for all 140 labels. So by Step 3, t ↦ Θ_{α,β}(τ;t) is 2log ε-periodic for every label. Define

  u_{α,β}(w) := (√y/2) ∫_0^{2log ε} Θ_{α,β}(w; t) dt,  w = x+iy.

Unfolding the ν ≠ 0 terms over γ²-orbits gives the rev4 Bessel series, with factor ½ and the sum over ν mod γ². (Positive- and negative-norm orbits each give √y K₀(2π|Q(ν)|y)e(Q(ν)x) after the t-integral, the standard ∫e^{−2πyQ̃_t}dt = 2K₀ computation.)

**The constant term b.** The ν = 0 term contributes δ_{α∈Z²}·(√y/2)·2log ε = √y·log ε·δ_{α∈Z²}. So b_λ = log ε·δ_{α∈Z²}, and it is nonzero for exactly the 2 labels with α = 0 (labels_exact.txt).

**Step 5. The law.** Every right-hand label in Steps 1–2 is again 2log ε-periodic (Step 4 applies to all 140 labels). So we can integrate the Step 1 identity over t ∈ [0, 2log ε]; this is legitimate by uniform convergence. Using √Im(−1/w) = √y/|w|, the |w| from Step 1 cancels exactly:

  u_{α,β}(−1/w) = (e(B(α,β))/√35) Σ_p u_{p−β,α}(w),  i.e. u∘S = S_lab u.

Similarly, u∘T = T_lab u. Both identities hold component by component, constant terms included: b is not transformed separately, because the ν = 0 / η = 0 terms sit inside the theta identity. For a word γ′ = g₁⋯g_m in S^{±1} and T^{±1}, induction gives u∘γ′ = M(γ′)u with M(γ′) = M(g₁)⋯M(g_m), M(S) = S_lab, and M(T^{±1}) = T_lab^{±1}. T_lab is monomial and unitary; S acts as an involution on H.

**Convention reconciliation.** By Tensor-Pattern-Closure, on the full 140-dimensional label space the SL₂ relations hold for ρ(S) := S_lab⁻¹ and ρ(T) := T_lab, with ρ = ρ₅ ⊗ ρ₇ ⊗ ρ₂ factoring through SL₂(Z/140). The vector u takes values in W_P = Fix(P) (Pu = u, from the parity reduction), and on W_P we have S_lab = S_lab⁻¹. So M(γ′)u = ρ(γ′)u, with u∘γ′ = ρ(γ′)u for every γ′ ∈ SL₂(Z), independent of the chosen word.

**Status: Cat A.** Steps 0–5 are proofs. The finite inputs are the stabiliser order, the closure of the label set, and w_c; these are exact integer/Fraction computations (labels_exact.py/.txt). This removes the condition on (c) in §3.

**Numerical confirmation (Cat B, supporting only).** uvec.py implements the 140-component Bessel series (with the four cones F, −F, [f,γf), −[f,γf), each with k = 0, 1). It reproduces the S-law to 7e−14 and the T-law to 2e−14 at two points (test_slaw.py).

### 3B. Numerical test of the vector cocycle at γ′ = STS and γ′ = ST^kS (Cat B)

For γ′ = ST^kS = [[−1,0],[k,−1]], with cusp r = 1/k and M = S_lab T_lab^k S_lab, test all 140 rows of

  κ̂(γ′x) = |kx−1| M[κ̂(x) + (2/π)P(x)] − (1/π)(|kx−1| M b − b).

Here κ̂_λ = ½[κ_F(α,β) + κ_F(γ⁻¹α,γ⁻¹β) + κ_F(−α,−β) + κ_F(−γ⁻¹α,−γ⁻¹β)], computed exactly with fastkappa.cone_terms (Bernoulli sums), and P(x) = ∫_r^{i∞}[u, R_x^{1/2}] is computed by Gauss–Legendre on w = r+is. For s < 1/k the path is transported, u(w) = (S T_lab^{−k} S)u(γ′w).

| γ′ | x tested (both signs of cx+d) | max error over 140 rows |
|---|---|---|
| STS (k=1, multiplier S T S) | 1/2, 1/3, 2/3, −1/2, 0 (cx+d<0); 3/2, 2, 5/3 (>0) | ≤ 1.8e−14 |
| ST²S (k=2) | 1/3, 1/4, −1, 0 (<0); 2/3, 1, 3/5 (>0) | ≤ 1.0e−12 |
| ST³S (k=3) | 1/4, 1/5, −1/3 (<0); 1/2 (>0) | ≤ 3.3e−12 |

|κ̂| is up to 2.5, and 129 of the 140 entries of κ̂(1) are nonzero. The term (2/π)P is essential: |P| ≈ 1.49, and dropping it gives an error of 1.06. Doubling the node count leaves P unchanged to 5e−13. Output: vc_k1.txt, vc_k2.txt, vc_k3.txt, vector_cocycle.jsonl.

## 4. Open
- (Done, §3A.) Label-level proof of u∘γ′ = ρ(γ′)u.
- A new numerical test of (c) at a γ′ with nontrivial multiplier other than S, e.g. STS, needs κ and the period integrals for all components. Not run.

## 5. Files (`2026-10-18-Cocycle-Closure/`)
- `c0_check.py`, `c0_check.txt`: C = −π/2 by quadrature (18 digits).
- `nontangential_check.py`, `nontangential_check.txt`: non-tangential κ fits.
- Cited data: `2026-10-18-Open-Analytic/cocycle_gamma.json`, `cocycle_holfactor.txt`; `2026-10-17-psi-cocycle/psi_period.txt`, `maass_lift.txt`.

- 3A/3B (2026-10-18): `labels_exact.py/.txt` (exact finite inputs), `uvec.py` (140-component lift), `test_slaw.py`, `vector_cocycle.py`, `vc_k1.txt`, `vc_k2.txt`, `vc_k3.txt`, `vector_cocycle.jsonl`; backup of the previous report `Cocycle-Closure.pre-3A.md.bak`.
