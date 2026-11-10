# order4b results: weight-0 vector law for A2?
PREREG sha256 5346382c…dbef2 (unchanged). Script hashes in scripts/SHA256SUMS. Category B: numerical ranks. Mod-p certification is not feasible because the entries are transcendental.

## Anchor
A012 at x=1 reproduces the order3c A2 value exactly (difference 0.0). **Pass.**

## Sign control (gating)
- A0 at w=1: rank 36, closed.
- A0 at w=0: joint rank 72, not closed.
- **Passed.** The test separates weights.

## Tests (105 companions × 216 points)
| test | rank | joint | closed |
|---|---|---|---|
| T0: A2, w=0 | 73 | 146 | **no** |
| A2, w=½ (descriptive) | 73 | 146 | no |
| A2, w=1 (descriptive) | 73 | 146 | no |
| T1: affine span [A2, \|x\|^{½}A1, \|x\|A0] | 214 | 216 | no |

## Verdicts
- **T0:** the weight-0 law is falsified (Category B). The S-image of A2 is linearly independent of A2 (joint rank = 2 × 73).
- **T1:** not closed. The span rank is 214 out of 216 rows, so the test is close to saturation and its discriminating power is low. It is reported as stated, not as strong evidence.
