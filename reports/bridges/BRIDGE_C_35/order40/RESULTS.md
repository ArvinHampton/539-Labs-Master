# order40 RESULTS: RG37, (0,1)-edge decomposition
PREREG sha256 069e6712e02f349c9cb8a27d445ec7aa30738c631216e8c00f41d972d647f031 (hashed before numerics). Stored arrays only (order19 C2a/C2b, order34 pieces).
## I-e2: T_e2((1,n),(0,1)) = ((1+n)/2)·C2a, n = 1..6: PASS
Max error 1.2e−12. This is the e2 analogue of T_e1 = ((2n+7)/4)·C2b. Q(e2) = 7/2 enters only the coefficient B/(4Q(e2)) = (7+7n)/14. It is Category A only in the bookkeeping sense (immediate from the definitions).
## RG37a: PASS (consistency)
r(T_e2) = r(C2a) = 0.020718 on 6/6 cones (identical to < 1e−12), and the criterion is met. The near-law carrier on (0,1)-edge cones is T_e2, a multiple of the single Bernoulli sum C2a.
## RG37b: PASS (Category B; not blind; order34 observed these values)
| cone | r(T_e2) | r(B2 part) | r(T_BB) |
|---|---|---|---|
| ((1,1),(0,1)) | 0.02072 | 0.02317 | 0.265 |
| ((1,2),(0,1)) | 0.02072 | 0.02276 | 0.397 |
| ((1,3),(0,1)) | 0.02072 | 0.02225 | 0.378 |
| ((1,4),(0,1)) | 0.02072 | 0.02257 | 0.439 |
| ((1,5),(0,1)) | 0.02072 | 0.02167 | 0.432 |
| ((1,6),(0,1)) | 0.02072 | 0.02196 | 0.524 |
The B2 part sits within [½, 2]·r(C2a) on 6/6 cones, and T_BB fails on 6/6.
## Controls
- r(C2b) = 0.0030492, matching the (1,0)-edge value (order34).
- Interior cones: 0/44 B2 pieces are a scalar multiple of C2a or C2b (best-scale residual ≥ 1e−3), PASS.
## Reading
The edge rule is now explicit:
- an e1 edge gives a B2 piece ∝ C2b, with r = 0.00305;
- an e2 edge gives a B2 piece ∝ C2a, with r = 0.0207;
- an interior cone gives B2 pieces that are sheared sums, worse (r 0.04–0.17).
The near-law grade is the law miss of the coordinate Bernoulli sum attached to the edge. Q(e) only scales.
## Category
A: I-e2 (bookkeeping identity, too trivial for the paper). B: RG37b. v11: no. Ξ: not identified. E1–E3 OPEN.
