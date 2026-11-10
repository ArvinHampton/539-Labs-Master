# Order 3: results — where the shadow enters (PREREG sha256 b479d46c…120f, unchanged)

Order run as preregistered: scripts hashed (scripts/SHA256SUMS) → Map 1 → sign control → Map 2 → Map 0.

## Map 1: decomposition identity (Category A)
**Statement.** For each piece P = r·e1 + N(21,−1) + N(0,1) with generators u1=(21,−1), u2=(0,1), the order-2 coefficient of entry 107 splits as A1_P = D_P + W_P^{(Q(u2))} + W_P^{(Q(u1))}, where
- the drift is D_P = −mean(f)(l1J_a + l2J_b);
- the sawtooth terms are W_P^{(Q(u_i))} = −(√π/2)Q(u_i)^{-1/2}·N^{-1}Σ f·B1(z_i/N).

The rays contribute R = Σ_walls ±(√π/2)Q(u)^{-1/2}·mean_u(f).

**Proof.** In the entry-107 formula, Q(u2) = r and Q(u1) = p. With A = [[2,7],[7,7]]:
- Q(0,1) = 7/2;
- Q(21,−1) = ½(2·441 − 2·7·21 + 7) = 595/2;
- Q(1,0) = 1, which is the generator on the boundary pieces and the walls.

So every W term carries exactly one of the labels Q ∈ {1, 7/2, 595/2}. The decomposition is a regrouping of the finite sum in entry 107, so it is exact. ∎

**Numerical check.** Over 105 companions × 216 points, the largest gap between the summed parts and order2 A01_float is 1.8e-15. **Pass.**

## Sign control (must pass before verdicts are read)
- A0 at w=1: rank 36, joint rank 36 (closed).
- A0 at the wrong sign: joint rank 72 > 36.
- **Control passed.**

## Map 2: closure tests (Category B, numerical ranks with SVD threshold 1e-9)
| part | rank | joint w=½ | joint w=1 | prediction | verdict |
|---|---|---|---|---|---|
| D | 58 | 116 | 98 | closed at w=1 | **FALSIFIED** |
| R | 105 | 210 | 210 | closed at w=½ | **FALSIFIED** |
| W[1] | 90 | 178 | 156 | not closed | consistent |
| W[7/2] | 60 | 116 | 120 | not closed | consistent |
| W[595/2] | 100 | 200 | 200 | not closed | consistent |
| W total | 105 | 210 | 210 | not closed | consistent |
| A1 | 105 | 210 | 210 | (order-2 result: not closed) | reproduced |

**Overall:** the preregistered claim, that the defect sits only in W while D and R are separately S-closed, is **falsified**. None of the parts closes on its own. The shadow is not located in the wall sawtooth by this split.

## Map 0: numeric anchor
Data from the orthant/cone series, fitted on the preregistered grid t_j = 2^{-j}·0.5/(297.5·(2m)²). The fitted t^{-1/2} coefficient matches A1 at all x ∈ {1, 1/2, 1/3, 2/3, 1/4, 1/5, 1/6}:
- largest relative error: 7.5e-6 (threshold 1e-3);
- **7/7 pass.**

The O(1) coefficient A2 (descriptive only) is in data/map0.json.
- x=1: −0.323 − 0.445i
- x=1/2: ≈ 0
- x=1/6: 2.33 + 1.89i
