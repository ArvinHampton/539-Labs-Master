# order37 PREREG: RG34, per-point miss vs den(x) (written and hashed before numerics)
Data (stored only): order19/data/rg5_arrays.npz (C2b = C[2], SC[2]), full 216-point grid XS; M from S_rows. No new Bernoulli objects.
Per-point miss: X(x) = x·35^{−1/2}·M·C2b(x), S(x) = C2b(−1/x). κ̂ is the single global least-squares κ over the full grid (w = −1, as orders 31–36). r(x) = ‖S(x) − κ̂X(x)‖/‖S(x)‖ for each x.
## Hypothesis (form fixed; p = 2 fixed, not fitted)
r(x) ≈ c·den(x)^{−2}, where den(x) is the reduced denominator of x.
Rule for c (fixed): c = r(1), the single point with den = 1 and x = 1; no fit. Then r_pred(x) = r(1)/den(x)².
Cancellation test (c-free): for each den value d, the median over points with den = d of r(x)·d²/r(1) should be ≈ 1.
## Metrics and verdict
e(x) = |r(x) − r_pred(x)|/r(x) over the 215 points other than x = 1.
PASS iff median e ≤ 0.10 and the 90th percentile of e ≤ 0.25. FAIL iff median e ≥ 0.5. Else inconclusive.
Diagnostics (not used for the verdict): Spearman(r, den) (prediction negative); Spearman(r, |num(x)|) (the S side lives at −1/x, whose denominator is |num(x)|); a least-squares log-log slope p̂ against den, reported only. Same check with den replaced by max(den, |num|).
Prediction (blind): FAIL. Order36 per-point r varied by only ~15× between den = 1 and den = 13, which is much slower than den^{−2}.
Category: B (numerical). A PASS would still be Category B unless derived from L_B; v11 only for a proved statement.
Naming: RG* only, no labels L1–L7. Geometric only; MAPS_CANDIDATES untouched; no Resonant objects; no bridge claim; E1–E3 OPEN; Ξ not identified.
