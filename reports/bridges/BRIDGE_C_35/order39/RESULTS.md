# order39 RESULTS: RG36 (blind |num| ordering on new points)
PREREG sha256 e25a92538820ff61f0b507cf432a0ee5d55f4dd1fb49c6490a5e1727b036773d (hashed before numerics).
Method: order19 comps() verbatim. κ̂ fixed (1.0000147 − 0.00034i) and M fixed; no refit. 12 new points, none in XS.
## RG36: FAIL (Category B)
| x | r | x | r | x | r |
|---|---|---|---|---|---|
| 41 | 0.01180 | 41/2 | 0.00551 | 41/3 | 0.00437 |
| 43 | 0.01147 | 43/2 | 0.00534 | 43/3 | 0.00426 |
| 47 | 0.01096 | 47/2 | 0.00503 | 47/3 | 0.00400 |
| 53 | 0.01026 | | | 53/3 | 0.00372 |
| 59 | 0.00965 | | | | |
- Below the reference 0.0013404: 0/12. Median of the new points: 0.00543, about 4× the reference.
- Pooled Spearman: −0.55 (PASS required ≤ −0.9).
- FAIL by both FAIL conditions. The prediction PASS (blind) was **wrong**.
## Reading
- The |num| ordering seen in orders 37–38 does not extrapolate. In the 216-point grid, large |num| goes together with moderate den. With den ∈ {1, 2, 3} fixed small, large |num| does not drive r down to the 1e−3 level.
- Within each fixed den, r still decreases with |num| (den 1: 0.0118 → 0.0096; den 3: 0.0044 → 0.0037), and for fixed |num| r decreases with den (e.g. 41: 0.0118 / 0.0055 / 0.0044).
- The miss depends on both num and den; neither alone orders it. The order38 RG35b PASS was confounded by the composition of the XS grid, which is exactly why it was labelled a consistency result.
## Optional 54-dim span subtest
Not run (preregistered as deferred; it would be circular).
## Category
B only. A: none. v11: no. Ξ: not identified. E1–E3 OPEN.
