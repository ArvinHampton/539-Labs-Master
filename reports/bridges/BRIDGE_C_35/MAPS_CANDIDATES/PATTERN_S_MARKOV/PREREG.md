# PREREG: PATTERN_S_MARKOV (Map-PSM1: |S|² label chain, stationary law → T-phase fibre, vs MF2)
Lock: written after explore (data/explore.sha256), before scripts/test.py. Explore never read ρ_res.
Source: rev8 tex (reports/self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Bridge_C_Consolidated_rev8_2026-10-19/bridge_c_consolidated_rev8.tex), l.274:
"u_{α,β}(−1/w) = e(B(α,β))/√35 Σ_{p∈L′/Z²} u_{p−β,α}(w)".
The 140 labels are as in PATTERN_FIBRE_RR. The second index is reduced mod L′ (2a ∈ L′, so a ≡ −a), and the first mod Z².

## Transition
P((α,β) → (p−β, α mod L′)) = |e(·)/√35|² = 1/35 for each p ∈ L′/Z² (35 targets).
Explore finds this matrix is doubly stochastic and reducible, with 3 closed classes (coset α, coset β): (0,0), (1,1), and the 2-cycle (0,1)↔(1,0).

## Stationary law (pattern rule; no class is selected)
π = the Cesàro limit of the chain started from the uniform law on all 140 labels, i.e. the S-orbit average of the whole written family. Uniform is invariant (doubly stochastic), so π = uniform on 140.

## Fibre
The T-phase fibre of PB2: 140·(Q(α)+B(α,w_c) mod 1) mod 8. The T-law is the written partner of the S-law in the same theorem (l.274–276).
140·Q is not label-constant, so it cannot be pushed forward from a law on labels; it is not used.

## Prediction
push(π) = ρ_res = (1,8,3,0,7,8,5,0)/32 exactly.
- PASS iff exact equality. FAIL otherwise.
- VACUOUS if the push is uniform on the 6 open fibres.
- Also recorded: whether ANY stationary law (any convex mix of the 3 classes) can match.
