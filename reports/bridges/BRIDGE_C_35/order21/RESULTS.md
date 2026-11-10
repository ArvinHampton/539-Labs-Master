# order21 RESULTS
PREREG sha256 980ede89123837ceea8750b09c2c1303c1888cb5c117358b6389f6e847361f8b (hashed before numerics; Maps RG8a, RG8b hashed there).
| test | value | verdict |
|---|---|---|
| K0 DFT reconstruction of C2b (x and −1/x, all) | max abs 2.1e−14 | PASS |
| K1 reproduce order20 rel(X) | 9.4949e−4 (diff 4e−18) | PASS |
| RG8a K=0: low / high | rel 2.7e−3 (abs 4.18) / rel 8.6e−3 (abs 4.33); joint rank 72 | — |
| RG8a K=1: low / high | rel 3.2e−3 / 2.9e−2; joint rank 90 | — |
| RG8a K=2: low / high | rel 3.4e−3 / 7.4e−2; joint rank 90 | — |
| **Map RG8a** (low-|k| carries the near-law) | low rel ≥ 1e−3 for all K ≤ 2 | **FAIL** |
| **Map RG8b** (smooth defect) | s(D) = 0.878 (control s(X) = 0.977) | **FAIL** |
| RG8b secondary (A2_corner defect) | s(D) = 0.855, s(X) = 0.977 | (reported) |
## Reading
The order20 guess is falsified: truncating to low |k| makes the law worse (rel 2.7e−3 → 3.4e−3), not better than the full X (9.5e−4); the near-law is not localised in the k-spectrum. The defect is not smooth in x on [1/2,3], so there is no quantum-modular-type explanation of this shape.
## Category A
Only the elementary fact c_0 = B2(α2)/N² (multiplication theorem), so the k=0 term is (B2(α2) − 1/6)·G_{α,β}. Nothing new warrants v8.
## Category B
All table entries.
