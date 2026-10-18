# Path C lemmas (written 2026-10-18, CDT)

**Lemma C1. The radial-order obstruction. [Cat A, elementary]**

Hypotheses.
- Γ ⊂ SL2(Z) has finite index.
- g is holomorphic of weight 1 on Γ (any finite-order multiplier) and holomorphic at the cusps.
- f is holomorphic on H, of moderate growth at the cusps. It has a logarithmic cocycle: f(γτ) = f(τ) + α_γ log(cτ+d) + β_γ for γ ∈ Γ (e.g. f = log η, or log-type Eichler integrals of weight-2 Eisenstein series).

Conclusion. Fix a rational x = h/k and set τ = x + it with t → 0+. Then

  f(τ)g(τ) = A t^{-2} + B t^{-1} log t + C t^{-1} + O(t^{-2} e^{-c/t}),

with c > 0. The same holds for any finite sum Σ f_j g_j. If the vector-valued T-matrix has Jordan blocks, the expansion gains finitely many terms t^{-m} (log t)^j with m ≥ 1. In every case:
- no half-integer orders appear;
- no orders t^0, t^1, … appear.

Proof.
1. Choose γ ∈ SL2(Z) with γ(h/k) = ∞, say γ = [[a, b], [−k, h]].
2. Then cτ + d = −ikt and Im γτ = 1/(k²t).
3. Expand g at the cusp: g(τ) = (cτ+d)^{-1} ĝ(γτ), where ĝ = g|γ^{-1} has a q-expansion of some width w. So g = (−ikt)^{-1}[b0 + O(e^{−2π/(w k² t)})].
4. Expand f at the cusp: f(τ) = f̂(γτ) − α log(cτ+d) − β, where f̂ = f∘γ^{-1}.
   - The cocycle of the stabiliser of ∞ is a constant, so f̂(z + w) − f̂(z) = const.
   - Hence f̂(z) − (const/w)z is w-periodic and holomorphic. Moderate growth then gives f̂ = c1 z + c0 + O(e^{−2π Im z / w}).
   - Substituting, f = c1(−a/k + i/(k²t)) + c0 − α log(−ikt) − β + (exponentially small).
5. Multiply the two expansions. Each exponentially small factor e^{−c/t} times a power of t or log t is smaller than every power of t. ∎

Consequence. C_third's two sectors are the Zwegers part (half-integer orders t^{∓1/2}, which are nonzero; Lemma P of the C_third report) and the E part (regular orders t^0, t^1, which are nonzero, e.g. C_0 = P_0 ≠ 0). No object in this class carries either sector, so no product of this kind can unify them with C_third's radial data.

**Lemma C2. The |cx+d| factor at the 1/t level. [Conditional, on the same inputs as O1]**

1. At the 1/t level, Lemma C1 gives the boundary profile σ_{fg}(x) = B0(x)·a_g(x).
   - The term t^{-1} log t carries α·a_g(x).
   - The pure t^{-1} term carries a_g(x)·(c0 − α log k − α·(iπ/2)·(…) − β) + c1-terms.
2. Under γ:
   - a_g(γx) = χ(γ)·(cx+d)·|cx+d|^{-2}·a_g(x), up to unimodular constants. This is the holomorphic factor, with sign sgn(cx+d) relative to |·|.
   - The log cocycle contributes α(log|cx+d| + iπ·1_{cx+d<0}) + β.
3. To obtain E_L's law (factor |cx+d|, no log|·|), the log|cx+d| contamination must cancel along T-orbits x + Nn.
   - log n is independent of exponential polynomials in n, so the α·a_g profile must vanish.
   - The iπ·1_{cx+d<0} term carries the same α·a_g profile, so it vanishes as well.
4. What remains is the holomorphic law, which O1 excludes (the exponential polynomial would equal +A for n ≥ 0 and −A for n < 0).

So within this class, the |cx+d| factor is not reproduced either.

Not covered.
- Non-holomorphic weight-1 objects (harmonic, or real-analytic of signature (1,1), e.g. Siegel theta lifts). E_L itself is of this type.
- Weight-0 objects whose cocycles are non-logarithmic (higher-depth or polylogarithmic iterated integrals).

The question of whether an exotic class unifies the two sectors therefore stays open in that larger generality.
