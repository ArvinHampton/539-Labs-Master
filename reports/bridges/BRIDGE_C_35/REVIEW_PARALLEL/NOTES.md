# REVIEW_PARALLEL notes (process and disclosures). Times are CDT (America/Chicago).

## Process
- 15:42: Inventory. order8 had PREREG, scripts, logs and data, but no RESULTS/NOTES/REPORT; it was still running. Only its logs were read. No order8 file was touched.
- 15:44: `sha256sum -c PREREG.sha256` returned OK for order2 through order8.
- 15:47: Light check `scripts/weight_scan.py` (nice, OMP_NUM_THREADS=1, under 100 MB, under 1 s). Its first launch failed on a relative-path error before reading any data. The paths were fixed in the same file before any statistic was produced; nothing was preregistered for this check.
  - SVD threshold 1e−9, the same as order3.
  - The rows are the 216 positive x of XS, so \|x\| = x throughout. The sign question of finding 1 cannot be tested on these arrays.
- 15:55: Arithmetic checks by hand and in python, all exact identities:
  - Q(c1) = −5/2, Q(c2) = −17/2, Q(c′) = −35.
  - det(u,c) = −1, 17, 2.
  - L = arccosh(7/(2√3.5)) = 1.2389443651 = ½ log(6+√35).
  - I = 0.2094198203.

## Caveats
- The finding 1 argument uses M² = 35P (order7). The double application, for a signed law A0(−1/x) = (x√35)^{−1}MA0(x), gives A0 = −PA0; for the \|x\| law it gives A0 = PA0. That K2_0 is P-even follows from Q(−ν) = Q(ν) and β = 0, up to the A35 `reduce` phases, which were not re-inspected here. Treat finding 1 as an argument to verify, not as a new ledger fact.
- Finding 4/5's statement of the "derived weights" comes from a first-order Taylor treatment of −1/τ along the radial path. The exact coefficient of the A0 term was not derived.
- No new verdicts are claimed. Every recorded verdict in order2–order7 stands as written.
- No Residual↔Resonant link, T3, O_res, 539, crypto or g_k claim is made. No TPC/RH.
