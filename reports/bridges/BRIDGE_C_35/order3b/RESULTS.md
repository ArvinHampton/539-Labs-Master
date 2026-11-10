# order3b results: regrouping A1 by Q-class and by theta characteristic
PREREG sha256 bf5a02c6…cfdc (unchanged). Run order as preregistered. Scripts are hashed in scripts/SHA256SUMS.

## Map 1 (Category A): ray split
**Statement.** R = R[7/2] + R[595/2], where:
- R[7/2] collects the walls ±(0,1), with Q(0,±1) = 7/2;
- R[595/2] collects the walls ±(21,−1), with Q = ½(2·441 − 294 + 7) = 595/2.

**Proof.** The four walls in R are exactly these directions, so this is a partition of a finite sum. ∎

**Numerical check:** max |R[7/2] + R[595/2] − R| = 2.8e-17 over 216 points, both at x and at −1/x. **Pass.**

## Sign control (gating)
- A0: rank 36, closed at w=1.
- Wrong sign: joint rank 72 > 36.
- **Passed.**

## Closure tests (Category B; numerical ranks, SVD threshold 1e-9)
| group | rank | joint w=½ | joint w=1 | Θ1 (K2+K3) rank → joint w=½ | Θ2 (K4) rank → joint w=½ |
|---|---|---|---|---|---|
| G[1] = W[1] | 90 | 178 | 156 | 62 → 122 | 29 → 58 |
| G[7/2] = W[7/2]+R[7/2] | 60 | 116 | 120 | 40 → 80 | 20 → 36 |
| G[595/2] = W[595/2]+R[595/2] | 100 | 200 | 200 | 67 → 134 | 33 → 66 |
| G[D] = D | 58 | 116 | 98 | 39 → 78 | 19 → 38 |
| A1 | 105 | 210 | 210 | 70 → 140 | 35 → 70 |

None of these is closed, at w=½ or at w=1, in any block (full values in data/closure3b.json).

Descriptive: A0 restricted to Θ1 gives rank 24, closed; A0 restricted to Θ2 gives rank 12, closed. So the characteristic blocks are S-stable at order 1, and 24 + 12 = 36.

## Verdicts
- **P-Q: not localised by Q-class.** All four Q-class groups fail to close.
- **P-Θ: not localised by characteristic.** Neither Θ1 nor Θ2 closes for A1. A1 is full rank in both blocks (70 and 35), and the joint ranks double.
