# Map-RG1′. Preregistered 2026-10-24, about 6:15 PM CDT, after RG1 FAILed and before any RG1′ test
RG1′ was found post-hoc on the 105 companions (rg1posthoc). That fit is descriptive only and is not counted as evidence.
**Rule.** At the endpoint c1, B_j(ĉ1) ≡ 0 iff at least one of the two endpoint reflections preserves companion j:
- ρ_m: (u,m) ↦ (u,−m). Criterion: 2(α1+α2), 14(b0+b1) and 14(b0+b1)(α1+α2) are all in Z.
- ρ_u: (u,m) ↦ (−u,m). Criterion: 2α1, 10b0 and 10b0·α1 are all in Z.
Sufficiency is Category A (same argument as PREREG §1). Necessity is the prediction.
**Fresh test set** (not used before): the K1 family, α = a+μ, β = a, 35 companions (symbols FAM1). Compute B(ĉ1) as in c1.py (3 τ, dps 30, box 10). Zero means ≤ 1e−25·Σ|terms|. To avoid the float-rounding artefact found in C1, s and s′ are computed exactly as √10·ν1 and √14·(ν1+ν2).
**Pass:** the predicted zero set equals the measured zero set, and every nonzero is > 1e−6. **FAIL:** otherwise.
