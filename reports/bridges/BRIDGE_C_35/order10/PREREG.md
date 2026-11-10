# PREREG: order10. Laplacian of the weight-0 Siegel lift Φ₀ on the unit-arc boundary rays (e2, γe2)
Written 2026-10-24, about 4:05 PM CDT, before any order10 numerics. Owner: Arvin Hampton. Parents order5–order9 and REVIEW_PARALLEL are read-only. New files only. CORE_FREEZE. Category A = proof or exact; Category B = numerical. Runs use nice, OMP_NUM_THREADS=1 and ulimit -v 3000000. No push, no sends.
Review rules applied: Θ_E = 𝓗(Φ) is an identification, not a bridge. Lemma-2 A0 (2L = log(6+√35)) is not recounted. There are three distinct unary-theta series (5n²/2 shared). M² = 35·P is exact (order9 cyclo, Category A).

## 0. Object
Φ₀(τ) = ∫_0^{2L} Θ_{z(μ)}(τ) dμ with 2L = log(6+√35). z(μ) is the unit-speed hyperbola in the negative cone, Q(z) = −1, from ĉ1 = c1/√(5/2) to γĉ1. Then z' = z^⊥ (Q = +1) and z'' = z.
Θ_z(τ) = y^{1/2} Σ_{ν∈α+Z²} e(B(ν,β)) e(Q(ν)x) exp(−πy(2Q(ν)+s²)), with s = B(ν,z) and s' = B(ν,z'). Note Q(ν) = (s'² − s²)/4.

## 1. Derivation (Category A, written before numerics)
For G = y^{1/2}e^{−πyK}, K = 2Q + s² = (s²+s'²)/2, the Laplacian Δ₀ = −y²(∂x²+∂y²) acts on e(Qx)G as
  ΔG/G = 1/4 + πyK − π²y²s²s'².
In μ (using s' = ∂_μ s and s'' = s): ∂_μ²G/G = 4π²y²s²s'² − 4πyK. Therefore
  **Δ₀Θ_z = ¼Θ_z − ¼∂_μ²Θ_z**, and integrating over the arc:
  **(Δ₀ − ¼)Φ₀ = −¼[∂_μΘ_z]_{μ=0}^{μ=2L} = (π/2)·y^{3/2}·(B(γĉ1) − B(ĉ1)),**
where B(z)(τ) := Σ_ν e(B(ν,β)) s s' e(s'²τ/4)·e(−s²τ̄/4).
So Φ₀ is not harmonic. It is a Δ = ¼ eigenfunction up to two boundary terms (λ = ¼ is the y^{1/2} Siegel normalisation).
**Endpoint ĉ1 (ray e2):** s = √10·ν1 and s' = ±√14·(ν1+ν2). The sign is the orientation of z'(0) and is fixed numerically, not by hand. The map ν ↦ (u, m) = (ν1, ν1+ν2) is unimodular and B(ν,β) = −5b0·u + 7(b0+b1)·m, so the sum factorises exactly:
  B(ĉ1) = ±√140 · ϑ⁺(τ) · conj(ϑ⁻(τ)),
  ϑ⁺ = Σ_{m∈α1+α2+Z} m e(7m²τ/2 + 7(b0+b1)m)  (holomorphic, weight 3/2),
  ϑ⁻ = Σ_{u∈α1+Z} u e(5u²τ/2 + 5b0 u)  (weight 3/2: the 5n²/2 series).
**Endpoint γĉ1 (ray γe2):** this is the same expression with α → γ⁻¹α and β → γᵀ-transported twist (B(γν',β) = B(ν',γ⁻¹... ) is evaluated numerically as B(ν,β)).
**Predictions (Category A, checked numerically as Category B):**
- (D1) Per-Fourier-mode identity. For every N with |N| ≤ 8 and y ∈ {1/2, 1, 2}, the e(Nx)-coefficient of (Δ₀−¼)Φ₀ (μ-quadrature of the exact integrand) equals that of (π/2)y^{3/2}(B(γĉ1) − B(ĉ1)). Pass if relative ≤ 1e−15 at dps 30; FAIL if > 1e−6.
- (D2) Factorisation B(ĉ1) = ±√140·ϑ⁺·conj(ϑ⁻), checked on exact enumeration at 3 τ values: pass ≤ 1e−20.
- (D3) No new unary theta. The negative-ray factor at both endpoints is a 5n²/2 series with characteristic α1 (ĉ1) or (γ⁻¹α)_1 mod 1 (γĉ1). This is checked exactly in rationals. The positive factor is the 7m²/2 series at weight 3/2. Count of distinct weight-3/2 unary series with the 5n²/2, R²/34, 35m²/4 list: the 5n²/2 series recurs. **New: the weight-3/2 partner Σ m e(7m²τ/2)**, which previously appeared only as the weight-½ θ_{7/2}.
- (D4) γ-invariant companions (order9 list): B(γĉ1) = B(ĉ1) exactly, so (Δ₀−¼)Φ₀ = 0 (a pure Maass eigenform). Pass ≤ 1e−15.

## 2. Shadow verdict rule
"Even-piece ξ-shadow located" requires a weight-1 completion Θ̂_E with ξ₁Θ̂_E equal to a sum of weight-3/2 unary thetas. The Φ₀ route gives a weight-0 object whose (Δ−¼) defect is a product y^{3/2}ϑ⁺·conj(ϑ⁻) of two weight-3/2 thetas. That is the signature of a weight-0 eigenform with boundary, not of a weight-1 mock form. **Predicted: boundary terms located exactly (Category A), even-piece / full-series ξ₁-shadow NOT located.** The negative factor ϑ⁻ (5n²/2) is the candidate shadow: it is the factor that ξ would see.

## 3. Radial tests (order9 leftovers)
- R1′: Θ_E at x = 1/4, same 4 companions. Fit e = {−1, −½, 0, ½, 1, 3/2, 2, 5/2, 3} (9 terms) on 12 points t_j = 2^{−j/1.5}·0.02/(2m)², j = 0..11. Least squares in mpmath dps 40; sums in float64 (disclosed). Pass ≤ 1e−5·max(1,|pred|) for A0, A1, A2; FAIL > 1e−3; otherwise inconclusive. The order9 7-term verdict (inconclusive) stands as recorded.
- R2′: Θ_{C_arc} at x = 1/4, A0 against mean f·2·(2L)/√35 (Lemma-2 type, descriptive check only, not counted as evidence). Same fit.
