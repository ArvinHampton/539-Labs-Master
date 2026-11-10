# Addendum V: exact spectrum of the tuned 48-coefficient H′ (bounded exact enumeration, sympy, /tmp/v.py)

Setup: the original orbit table A, B, C, D, with O6 = {xy³} tuned from 6−√35 to 7−√35 and shift w = y. Each eigenvalue is computed exactly as λ′(χ_{p,q,r}) = Σ_c a_c χ(cy).

Proof of the shift: xy³ multiplied by y is x. Since χ(x) = (−1)^p, we get λ′ = λ + (−1)^p. So the p = 0 characters move by +1 and the p = 1 characters move by −1. The original 13 distinct values therefore do not map one-to-one onto 13 tuned values.

## Tuned spectrum: 14 distinct values, 48 total, none zero

| value | mult | p = 0 | p = 1 |
|---|---|---|---|
| 128+39√35 | 1 | 1 | 0 |
| 2−9√35 | 2 | 2 | 0 |
| 6−9√35 | 2 | 2 | 0 |
| 24−9√35 | 1 | 1 | 0 |
| −6−√35 | 1 | 0 | 1 |
| −4−√35 | 3 | 1 | 2 |
| −2−√35 | 14 | 2 | 12 |
| −√35 | 14 | 12 | 2 |
| 2−√35 | 3 | 2 | 1 |
| 4−√35 | 1 | 1 | 0 |
| −26+7√35 | 1 | 0 | 1 |
| −24+7√35 | 2 | 0 | 2 |
| −20+7√35 | 2 | 0 | 2 |
| −18+7√35 | 1 | 0 | 1 |

Every value has a nonzero √35 coefficient. Since √35 is irrational, no value is 0, so det H′ ≠ 0.

## The inserted t4129 list is FALSE

- It sums to 46 multiplicities, not 48.
- Its values are not the tuned eigenvalues. For example, it lists 31+9√35 and the ±6/±18 families, none of which occur.
- It gives the trivial eigenvalue as 127+39√35. The tuned trivial eigenvalue is 128+39√35.

## H01′ spectrum: CONFIRMED as stated by Physicist (exact)

1 (×12), 77+16√35 (×1), 5 (×1), −3 (×1), 3 (×2), −1 (×2), 11−8√35 (×2), 15−8√35 (×2), 21−8√35 (×1).

The cross-block claim that "all 12 even-q values have a nonzero √35 coefficient" is FALSE. The S block has the rational eigenvalues ±4 and ±2.

None of the H01′ eigenvalues is zero, so H01′ has full rank 24. With rank M′ = 24 + rank H01′, this gives rank M′ = 48. The rank-48 result stands.

No CERT, no .tex, tip untouched.
