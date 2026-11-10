# order37 RESULTS: RG34 (per-point miss vs den(x))
PREREG sha256 98279e7a15f162b19d99522cf06dfd23147ac0529a5e0f64d5c1fca14925fa41 (hashed before numerics). Stored arrays only (order19 C2b); full 216-point grid.
Global: κ̂ = 1.0000147 − 0.00034i; r_global = 0.0030492 (reproduces orders 34–36).
## RG34: FAIL (Category B)
Rule: r_pred(x) = r(1)/den(x)², with c = r(1) = 0.1408 and p = 2 fixed.
| metric | value | threshold |
|---|---|---|
| median relative error e | 0.592 | PASS ≤ 0.10, FAIL ≥ 0.5 |
| 90th percentile e | 0.876 | PASS ≤ 0.25 |
c-free cancellation, median of r·d²/r(1) per denominator d (≈ 1 under the hypothesis):
d = 1: 0.60 | 2: 1.05 | 3: 1.33 | 4: 1.58 | 5: 1.72 | 6: 1.90 | 7: 2.01 | 8: 2.19 | 9: 2.28 | 10: 2.41 | 11: 2.56 | 12: 2.69 | 13: 2.80 | 14: 2.84 | 15: 2.98
The ratio grows steadily with d, so the decay is slower than den^{−2}. (d = 1 is below 1 because the x = 1 point is the largest of the den = 1 points.) Prediction FAIL (blind): correct.
## Diagnostics (reported only, not verdict)
- Spearman(r, den) = −0.67; Spearman(r, |num(x)|) = −0.96; Spearman(r, max(den, |num|)) = −0.94.
- Log-log slope p̂ ≈ 1.41 (against den) and 1.44 (against max). Not fitted into any claim.
- The miss is ordered far more tightly by |num(x)| = den(−1/x), the side where L_B's aliasing (N′ = 2|num|) acts, than by den(x).
Point-by-point table: data/o37.json (x, den, r, r_pred, e).
## Category
B only. A: none. v11: no. Ξ: not identified. E1–E3 OPEN.
