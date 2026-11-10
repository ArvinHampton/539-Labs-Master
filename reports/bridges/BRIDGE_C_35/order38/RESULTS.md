# order38 RESULTS: RG35 / RG35b
PREREG sha256 3fa7c2db7e301a528885b4f24f49d20bdd994c82dd1a1a0236a94f8e659b4fca (hashed before numerics). Stored order19 C2b arrays only; full 216-point grid.
r_meas = 0.0030492 (κ̂ = 1.0000147 − 0.00034i).
## Vacuity control (preregistered)
Span including the −1/x images: rank 104; leftover of S = 2.1e−10. Vacuous by construction, as stated; not a test.
## RG35 primary: FAIL (Category B)
| quantity | value |
|---|---|
| rank W_B = colspan{x·C2b_l(x)} | 54 (of 105 columns) |
| r_B = ‖(I−P_{W_B})S‖/‖S‖, no fit | 0.0020579 |
| r_B / r_meas | 0.675 (PASS ≥ 1−1e−6; FAIL ≤ 0.9) |
| Spearman(per-point leftover, per-point r) | 0.94 |
Prediction FAIL (blind): correct.
Reading: even the best arbitrary 105×105 matrix law S ≈ x·C2b(x)·T leaves 0.00206. About two thirds of the near-law miss (by norm) is intrinsic: S(x) lies partly outside the span of the 54 independent Bernoulli functions x·C2b_l(x). The remaining third is specific to the choice T = κ̂M. Leftover and miss are strongly co-located point by point (ρ = 0.94).
## RG35b secondary: |num(x)| ordering: PASS (not blind; disclosed)
31 groups with ≥ 3 points (|num| = 1..37). Spearman(|num|, group median r) = −0.996 (PASS ≤ −0.9).
Group medians fall monotonically from 0.032 (|num| = 1) to 0.0013 (|num| = 37), with two tiny inversions (20 vs 19, 23 vs 22).
This confirms the order37 post-hoc observation as a hashed test, but the hypothesis was formed from the same data, so it is a consistency result.
## Category
B only. A: none. v11: no. Ξ: not identified. E1–E3 OPEN.
