# order25 RESULTS
PREREG sha256 5db9b84c9cabe1ac42c198d0855838bc737f091d4c354e9985c96f0a89bd7853 (hashed before numerics; RG15, RG16 hashed there).
| test | value | verdict |
|---|---|---|
| E1 Γ_γ² = I (exact: permutation involution, exponents sum ≡ 0 mod 9800) | true | PASS (Category A) |
| E2 [Γ_γ, M] = 0 (exact exponent multisets mod 9800) | 0 mismatches of 105² | PASS (Category A) |
| rank P_+ / P_− | 60 / 45 | — |
| identity Y_− = −½D; anti-invariance Γ Y_− = −Y_− | 7.9e−15; 0.0 | PASS |
| **RG15** law for Y_− = P_−A2_corner | abs 52.031 (predicted 52.03), ‖S‖ 744, rel 0.070 | **FAIL** |
| **RG16** defect mostly anti-invariant | share_− = 0.915; Pythagoras 2.3e−15 | **PASS** |
## Where the defect lives
‖R(A2_corner)‖ = 54.41 splits orthogonally into P_+ 15.90 and P_− 52.03: 91.5% of the squared defect is Γ-anti-invariant, i.e. sits in ½(Cor_K − Cor_{γ⁻¹K}).
Disclosure: RG15/RG16 predictions were derived from order24 numbers (consistency checks, not blind tests).
## Category A (folded into v9)
Γ_γ² = I, [Γ_γ, M] = 0 (exact); orthogonal split of the law residual; Y_− = ½(Cor_K − Cor_{γ⁻¹K}).
## Paper
RTA_FOUNDATION_BOUND_v9.pdf, 134 pages.
