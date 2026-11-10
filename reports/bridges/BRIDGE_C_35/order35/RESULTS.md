# order35 RESULTS: RG32 (quantitative L_B leakage)
PREREG sha256 04ab3e7dddfee76d7ce7e4f089325a146b7e0b8a8bd515a9a61a4ae5bbfb8007 (hashed before numerics).
Grid: P7 = {1, 1/2, 2, 1/3, 3, 2/3, 3/2} × 105 companions, as fixed in PREREG. The full grid is infeasible for the exact L_B right-hand side.
## Control D0: PASS
Exact L_B (ii) reconstruction S_in + S_out = C2b(−1/x): max error 3.3e−15. Terms: 42 875 inside (reduce to a companion) and 52 675 outside.
## RG32: FAIL (Category B)
| quantity | value |
|---|---|
| r_meas(P7) (direct, w = −1, κ free) | 0.05853 (κ̂ = 0.9977 − 0.0229i) |
| r_leak (outside mass ⟂ law direction, no fit) | 0.3527 |
| relative difference | 5.03 (threshold PASS ≤ 1e−6, FAIL ≥ 1e−2) |
| H1: S_in ∈ span{X} | FAIL (perpendicular share 0.926) |
| outside share ‖S_out‖/‖S‖ | 0.926 |
| k = 0 share of the inside part | 0.325 |
Prediction FAIL (blind): correct.
## Reading
- Classifying L_B terms by whether their characteristic reduces to a companion is not a classification by span. 93% of S sits in "outside" characteristics, yet S is still within ~6% of the fixed-M law direction on P7. The outside Gauss means at x must be largely linear combinations of companion means through relations beyond the reduction rules (Gauss-mean linear relations).
- So the outside-characteristic mass does not measure the law miss, and the near-law size is NOT an exact consequence of L_B leakage in this sense.
- On P7, r(C2b) = 0.0585, far above the full-grid 0.00305. The near-law quality depends strongly on which points are in the grid (the small-denominator points are worse). As disclosed in PREREG, 0.00305 itself could not be tested.
- (0,1)-edge cones (r ≈ 0.022): out of scope as preregistered. L_B is proved only for the ρ2 coordinate; nothing was tested and no new objects were introduced.
## Category
A: none new. v11: no. Ξ: not identified. E1–E3 OPEN.
