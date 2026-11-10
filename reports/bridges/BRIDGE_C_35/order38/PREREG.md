# order38 PREREG: RG35, Bernoulli-sum column span as reference (written and hashed before numerics)
Objects (order19/20, stored, no new Bernoulli objects): C2b_l(x) for l = 1..105 (C[2]) and C2b_l(−1/x) (SC[2]) on the 216-point grid. S = C2b(−1/x), X = x·35^{−1/2}·M·C2b(x), r_meas = ‖S − κ̂X‖/‖S‖ with global κ̂ (w = −1).
## Vacuity note (fixed before numerics)
If the reference span includes the −1/x images {C2b_l(−1/x)}, then every column of S is itself a reference vector. The leftover is 0 by construction and the test is VACUOUS. That variant is computed and reported as a vacuity control only.
## RG35 primary (non-vacuous variant)
Reference W_B = colspan{x·C2b_l(x) : l = 1..105} (216-dim function space; SVD rank reported, relative threshold 1e−9).
Leftover r_B = ‖(I − P_{W_B})S‖_F/‖S‖_F, no fit. This is the miss of the best arbitrary fixed 105×105 matrix law S ≈ x·C2b(x)·T, so r_B ≤ r_meas always.
PASS iff r_B/r_meas ≥ 1 − 1e−6, i.e. the S-matrix M (with κ̂) is already optimal and the law miss equals the out-of-span leftover. FAIL iff r_B/r_meas ≤ 0.9. Else inconclusive. Point by point: per-x leftover against per-x r, Spearman reported.
Prediction (blind): FAIL (an arbitrary T fits better than M).
## RG35b secondary: |num(x)| ordering (from the order37 post-hoc diagnostic; NOT blind, disclosed)
Group the per-point r(x) (global κ̂) by |num(x)|. Take groups with at least 3 points. Statistic: Spearman ρ between |num| and the group median r.
PASS iff ρ ≤ −0.9; FAIL iff ρ ≥ −0.5; else inconclusive. No exponent is fitted.
Prediction: PASS (consistency with the order37 observation, not independent evidence).
Category: B unless an exact identity emerges. v11 only for a proved statement.
Naming: RG* only, no labels L1–L7. "36" only as dim V. Geometric only; MAPS_CANDIDATES and REVIEW_2026-10-24 untouched; no Resonant objects; no bridge claim; E1–E3 OPEN; Ξ not identified.
