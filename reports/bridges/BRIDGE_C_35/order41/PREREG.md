# order41 PREREG: RG38, blind two-variable design (written and hashed before numerics)
Method: order19 comps() verbatim (C2b = third component) at x and −1/x, 105 companions. Fixed κ̂ = 1.0000146975519928 − 0.00033624064241876014i and fixed M; no refit.
r(x) = ‖C2b(−1/x) − κ̂·x·35^{−1/2}·M·C2b(x)‖/‖C2b(−1/x)‖.
Design (fixed): num ∈ {61, 67, 71} × den ∈ {1, 2, 4, 5}, x = num/den (12 points; none in XS, which is asserted).
## RG38
Strict-decrease claims, 17 in total:
- along every fixed-num line in den (1 → 2 → 4 → 5): 3 lines × 3 steps;
- along every fixed-den line in num (61 → 67 → 71): 4 lines × 2 steps.
PASS iff all 17 strict decreases hold. FAIL iff ≥ 3 violations. Else inconclusive. No exponent is fitted.
Prediction: PASS. The pattern was seen post hoc in order39; these points are blind.
Category: B. Naming: RG* only, no labels L1–L7. MAPS_CANDIDATES untouched; no Resonant objects; no new objects; no bridge claim.
