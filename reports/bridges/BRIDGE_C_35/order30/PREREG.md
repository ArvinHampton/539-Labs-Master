# order30 PREREG (written and hashed before numerics)
Notation: R(Y) = Y(−1/x) − x·35^{−1/2}·M·Y(x) (order18 weight-1 law, κ = 1), on the 216-point grid. W = span{CO, Γ_γCO}; d(Y) = relative distance from W; non-vacuity requires d > 1e−3.
Stern–Brocot cones C_{n,i}, i = 1..2ⁿ, at depth n of K (as in order29).
## Arc measure (fixed; from order22/v8)
For rays u, v with Q > 0, the arc length of cone(u,v) on the hyperboloid is ℓ(u,v) = arccosh( uᵀAv / (2√(Q(u)Q(v))) ), with Q(u) = ½uᵀAu. For K: ℓ = arccosh(√(7/2)) = L = ½log(6+√35). ℓ is additive under subdivision (Σ_i ℓ_{n,i} = L, checked as a control).
## RG23 (primary)
Rule (no fit): W_n = Σ_i (ℓ_{n,i}/L)·Cor_{C_{n,i}}, depths n = 1, 2, 3, 4.
Targets: (a) cancellation e_n = ‖R(CO) + R(W_n)‖/‖R(CO)‖; (b) anti-alignment c_n = |cos(R(W_n), −R(CO))|; (c) scaled match s_n = min_λ ‖R(CO) + λR(W_n)‖/‖R(CO)‖, with λ reported (scale only).
PASS: e_4 ≤ 1e−6, or c_4 ≥ 1 − 1e−6.
FAIL: e_4 ≥ 0.1 and c_4 ≤ 0.99; also a divergence flag if e_n increases strictly for n = 2..4.
Else inconclusive. Non-vacuity: d(W_n) > 1e−3 for every n.
Prediction (blind): FAIL. Since Σw = 1 and each corner is O(1), W_n behaves like an averaged corner; I expect R(W_n) of order ‖R(CO)‖ with c_n < 0.99 and possibly a convergent but non-cancelling limit.
## RG24 (secondary, run in parallel)
Rule: the uniform combinatorial average U_n = 2^{−n} Σ_i Cor_{C_{n,i}} (rays at the written Stern–Brocot positions; equal weights), n = 1..4.
Target (CO's near-law explained by the average): t_n = ‖R(CO − U_n)‖/‖R(CO)‖. PASS t_4 ≤ 1e−6; FAIL t_4 ≥ 0.1; else inconclusive. Non-vacuity d(CO − U_n) > 1e−3 (CO − U_1 = ½CO − ⅛vtx is reported, but n = 1 is excluded from the verdict as span-trivial).
Also report the near-law residual of U_n (κ free, w = −1, order29 metric) against CO's 0.0585.
Prediction (blind): FAIL.
## Controls
C1 corner(K) = CO; C2 ‖R(CO)‖ = 54.4056376674763 (rel ≤ 1e−9); C3 Σ_i Cor_{C_{n,i}} = CO + ¼(2ⁿ−1)vtx (≤ 1e−12); C4 Σ ℓ_{n,i} = L (≤ 1e−12).
Rules: geometric only; MAPS_CANDIDATES (incl. BATCH8, DISCOVER, MARKOV, L3) untouched; no Resonant objects; no bridge claim; E1–E3 OPEN; Ξ not identified.
