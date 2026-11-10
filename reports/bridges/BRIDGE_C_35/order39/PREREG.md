# order39 PREREG: RG36, blind |num| ordering on new points (written and hashed before numerics)
Method: C2b evaluated exactly as in order19/scripts/l0.py (comps(): third component Σ f·B2((α2+n)/N)), at x and −1/x, for all 105 companions. No new objects.
Law (fixed from prior orders; no refit): κ̂ = 1.0000146975519928 − 0.00033624064241876014i (order37/38 global value) and the S-matrix M from S_rows.
Per-point r(x) = ‖C2b(−1/x) − κ̂·x·35^{−1/2}·M·C2b(x)‖/‖C2b(−1/x)‖.
## New points (fixed; none are in XS, which the script asserts)
NP = {41, 43, 47, 53, 59, 41/2, 43/2, 47/2, 41/3, 43/3, 47/3, 53/3} (12 points; |num| 41–59; den ∈ {1, 2, 3}).
## RG36 (blind)
Reference: the |num| = 37 group median from order38, 0.0013404.
(a) Below: the number of new points with r < 0.0013404.
(b) Continuation: the median r of the new points is below 0.0013404, AND the pooled Spearman ρ between |num| and group median r is ≤ −0.9. Pooled groups: the order38 groups with ≥ 3 points, plus one group per new |num| value (median over its den ∈ {1, 2, 3} points).
PASS iff (a) ≥ 11/12 and (b) holds. FAIL iff the new-point median ≥ 0.0013404, or (a) ≤ 8/12. Else inconclusive.
Prediction (blind for these points): PASS.
## Optional 54-dim span subtest
Not run. I cannot state an L_B-characteristic count for the rank 54 without first inspecting the data, which would be circular. Deferred.
Category: B. v11 only for a proved statement.
Naming: RG* only, no labels L1–L7; "36" only as dim V. Geometric only; MAPS_CANDIDATES and REVIEW_2026-10-24 untouched; no Resonant objects; no bridge claim; E1–E3 OPEN; Ξ not identified.
