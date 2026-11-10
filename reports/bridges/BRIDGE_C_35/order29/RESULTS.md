# order29 RESULTS
PREREG sha256 abf67d465337c6a44fa933341b51418d279a96e84f54a759a183a932fb3baaac (hashed before numerics).
## Recovered order17 law
The fixed-M law with a free scalar κ and weight w is r(w) = min_κ ‖S − κ x^{−w}35^{−1/2}MY‖/‖S‖, applied to lines plus completion. For A2 the completion is A2(S^o) = 0, so the object tested is LN.
## Controls
C1 corner(K) = CO: 0.0, PASS. C2 ‖R(CO)‖ = 54.406: rel err 0.0, PASS. Iterated subdivision Σ Cor = CO + ¼(2ⁿ−1)vtx: 2.2e−14, 4.3e−14, 9.6e−14 for n = 1, 2, 3, PASS.
## RG21 (primary): FAIL
| object | non-vac d | r(w=−1) | r(−½) | r(0) | r(½) | r(1) | r_min | verdict |
|---|---|---|---|---|---|---|---|---|
| LN | 0.998 | 0.992 | 0.992 | 0.993 | 0.997 | 0.999 | 0.992 | **FAIL** |
| Π+LN | 0.994 | 0.9999 | 0.9999 | 0.9999 | 0.9999 | 1.000 | 0.9999 | FAIL |
| Π−LN | 1.000 | 0.983 | 0.982 | 0.983 | 0.992 | 0.998 | 0.982 | FAIL |
| CO (comparison) | — | 0.0585 | 0.210 | 0.503 | 0.848 | 0.982 | 0.0585 | FAIL |
Absolute residuals for LN are ≈105.5 at every weight, with ‖S_LN‖ ≈ 106. Even with κ free, M·LN is essentially uncorrelated with LN(−1/x).
**Near-law isolated as corner-only: NO by the preregistered criterion**, which needed LN to PASS. Descriptively (Category B), the near-law (r ≈ 0.06 at w = −1, κ ≈ 1) is seen only in the corner. The lines show no law at all (r ≈ 0.99) in either P-sector, so the lines are not a hidden law-obeying part. Prediction FAIL was correct (blind with respect to this metric).
## RG22 (secondary): FAIL at all depths (rule fixed in PREREG: Stern–Brocot alternating signs, coefficient 1)
| depth n | cones | non-vac d | ‖R(Alt_n)‖ | ‖R(CO+Alt_n)‖ | rel to ‖R(CO)‖ | |cos(R(Alt_n), −R(CO))| | verdict |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 0.580 | 224.9 | 219.0 | 4.02 | 0.229 | FAIL / FAIL |
| 2 | 4 | 0.582 | 418.9 | 415.7 | 7.64 | 0.125 | FAIL / FAIL |
| 3 | 8 | 0.653 | 727.2 | 726.1 | 13.35 | 0.060 | FAIL / FAIL |
‖R(Alt_n)‖ grows with depth and its alignment with −R(CO) decays. The rule is divergent and does not converge to a cancellation. Prediction FAIL was correct (blind).
## Category
A: none new (the iterated subdivision identity is v8 Prop. subdiv applied n times). B: all numbers above. v11: no. Ξ: not identified. E1–E3 OPEN.
