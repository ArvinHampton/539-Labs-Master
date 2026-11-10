# PREREG: PATTERN_ST_MARKOV (Map-PST1 / Map-PST2: |ST|² label chain → T-phase fibre, vs MF2)
Lock: written after explore (data/explore.sha256), before scripts/test.py. Explore never read ρ_res.
Source: rev8 tex (reports/self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Bridge_C_Consolidated_rev8_2026-10-19/bridge_c_consolidated_rev8.tex):
- l.274 S-law: each label goes to 35 labels with coefficient 1/√35.
- l.276 T-law: (α,β) → (α, α+β+w_c), with a unimodular phase. w_c ≡ a mod L′ (l.147) and 2a ∈ L′ (both checked).

## Transition
M_ST = M_S·M_T, entrywise |·|², where row i of each label matrix is the written expansion of u_i. M_T is a permutation, so |ST|² = |S|²·Π_T exactly. TS is logged too.
Explore finds M_ST doubly stochastic with 2 closed classes:
- C105 = coset types {(0,0),(0,1),(1,0)}, 105 labels;
- C35 = {(1,1)}, 35 labels.

## Maps
- **PST1 (primary, same rule as PSM1):** π = the Cesàro limit from the uniform law on 140 labels, which is uniform.
- **PST2 (written-count pattern):** π = the uniform stationary law on C105. Its size matches the written "105 companions" of Bridge C, independently of ρ_res.
- Fibre (both): T-phase 140·(Q(α)+B(α,w_c) mod 1) mod 8, as in PB2/PSM1.

## Prediction (each map)
push(π) = ρ_res = (1,8,3,0,7,8,5,0)/32 exactly.
- PASS iff exact equality. FAIL otherwise.
- VACUOUS if the push is uniform on the 6 open fibres.
- Also recorded: whether ANY stationary mix of C105 and C35 can put mass on fibres 2 and 6.
