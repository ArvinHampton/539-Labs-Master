# order34 RESULTS
PREREG sha256 aa27e04b2bfcc752a5cff27a20ab05524207d40dec82b37cb02a29583bc60f3a (hashed before numerics).
Order20 definitions recovered from order20/PREREG.md and scripts/o20.py (Prop. L_B), with arrays from order19/data/rg5_arrays.npz: C = [C11, C2a, C2b].
Control: piece reconstruction against stored corners: 5.7e−14, PASS.
## RG31.1: B2 part T_B2 on all 37 cones: FAIL (Category B)
- e1-cones (9/9): r = 0.0031–0.0037, criterion met.
- Control cones (28): 0 of 28 reach r ≤ 0.01; r ranges 0.0217–0.168.
  - Cones with edge (0,1) (e2 = (0,1), Q = 3.5): r 0.0217–0.0232; these meet the 0.10 criterion but not 0.01.
  - Interior cones: r 0.023–0.168; 19 of them also fail the 0.10 criterion, mostly on κ.
- 28/37 bad, so FAIL by rule. The prediction PASS (blind for the controls) was **wrong**.
- Reading: the B2 part obeys the law closely only when one edge is e1. Its quality orders as e1 edge (0.003) < e2 edge (0.022) < interior (0.04–0.17). The near-law is tied to the edge vectors, not only to the B̄1B̄1 term.
## RG31.2: B̄1B̄1 term T_BB on all 37 cones: PASS
It fails the criterion on 37/37 (min r = 0.181). Prediction correct.
## RG31.3: identities with order20 Bernoulli objects: all PASS (exact to rounding)
| identity | max error |
|---|---|
| T_e1(K) = (7/4)·C2b | 2.9e−13 |
| T_other(K) = ½·C2a | 1.7e−13 |
| T_BB(K) = C11 | 6.4e−14 |
| T_e1((1,0),(n,1)) = ((2n+7)/4)·C2b, n = 1..8 | 1.0e−12 |
Normalisation ratios: 1.75, 0.5, 1.0 exactly. Consistency: r(C2b) = 0.0030492 = r(T_e1) to 2.5e−17.
These identities follow directly from the definitions (same sums, same coordinates: in every basis ((1,0),(n,1)) the second coordinate is ν2). They are a check, not new mathematics.
**Is the r ≈ 0.003 miss the known S-law effect? Yes, qualitatively.** T_e1 is exactly ((2n+7)/4)·C2b. Prop. L_B (order20, Category A) gives C2b an exact S-law into Gauss means whose characteristics β+λ′_k+p lie outside the 105 companions, and order20 RG7 showed that this image leaves the span of the 35-component law vector. Hence no fixed-M law can hold for T_e1, and its miss is the L_B leakage. A quantitative prediction of the size 0.003 is not made here.
## Category
A: none new (the identities are by definition; L_B was already Category A in v7). v11: no. Ξ: not identified. E1–E3 OPEN.
