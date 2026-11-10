# PREREG: PATTERN_BNU_RR (Map-PBR1: B(ν,a) fibre; Map-PBR2: T-phase fibre), vs MF2
Lock: written after explore (data/explore.sha256), before scripts/test.py. Explore never read ρ_res.
Source: reports/self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Bridge_C_Consolidated_rev8_2026-10-19/bridge_c_consolidated_rev8.tex.
- l.896: "B(ν,a) = Re θ/10". By l.143 (Aa = (0,7/2)), B(ν,a) = (7/2)ν2.
- l.276: T-law "u_{α,β}(w+1) = e(−Q(α) − B(α,w_c)) u_{α,α+β+w_c}", with w_c = (1/10,−1/35) (l.147).
- 140 labels as in PATTERN_FIBRE_RR.

## Map-PBR1 (primary; unsigned density, as preferred)
- Fibre f = 10·B(ν,a) mod 8. 10 is the least integer making B(ν,a) integral on all labels; it equals the written /10 of l.896.
- Weighting: natural density over ν ∈ α+Z², uniform over the 140 labels.
- The signed w-content variant is logged in explore only and is not a pass criterion.

## Map-PBR2 (second, written T-law)
- Fibre f = 140·(Q(α)+B(α,w_c) mod 1) mod 8. 140 is the least common denominator, and it equals the level 140 of l.896.
- Weighting: uniform over the 140 labels; β does not change the phase.

## Prediction (each map separately)
ρ_map = ρ_res = (1,8,3,0,7,8,5,0)/32 exactly (MF2).
- PASS iff exact rational equality. FAIL otherwise.
- VACUOUS if ρ_map is uniform on the 6 open fibres.
- Also recorded: TV distance, supports, and mass on {3,7}.
No complement or flip transform is registered.
