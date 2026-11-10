# REPORT — Bridge C order4a (explicit shadow candidate)
PREREG sha256 cb914b77…ed34b (unchanged). Script hash in scripts/SHA256SUMS. Category B: numerical ranks. Mod-p certification is not feasible because the entries are transcendental.

## Sign control (gating)
- A0 at w=1: rank 36, closed.
- Wrong sign: joint rank 72 > 36.
- **Passed.**

## Tests: A1^c = A1 − Σ ε_Q W[Q]
| ε (W[1],W[7/2],W[595/2]) | rank | joint w=½ | joint w=1 | closed |
|---|---|---|---|---|
| 000 (A1) | 105 | 210 | 210 | no |
| 001 | 91 | 182 | 182 | no |
| 010 | 104 | 208 | 208 | no |
| 011 | 90 | 180 | 180 | no |
| 100 | 105 | 210 | 210 | no |
| 101 | 87 | 170 | 156 | no |
| 110 | 103 | 206 | 206 | no |
| **111 (primary: D+R)** | 58 | 116 | 98 | **no** |

## Verdicts
- **Primary:** candidate falsified (Category B). D+R does not close at w=½ or at w=1.
- **Secondary:** no ε closes.
