# order47 RESULTS: exact certification
PREREG sha256 72d93d589f678bad16706dd06d0fdae0255c3ad1b4eaee21425ecdde49158e39 (hashed before the run).
Method: exact integer arithmetic in Z[ζ_9800]. Products are formed by exponent addition mod 9800. The zero test uses the Z-basis ζ^r·ζ^{140i} (r < 140, i < 24), via Φ_9800(x) = Φ_70(x^140), with exact reduction mod Φ_70. No floating point in the verdicts.
| identity | nonzero entries of LHS − RHS (of 105²) | verdict |
|---|---|---|
| control: M² = 35·P | 0 | PASS (machinery validated) |
| control: M·M^† = 34·I (wrong on purpose) | 105 | rejected, as required |
| **X1: conj(M)·Π·M = 35·Π** | 0 | **PASS (exact)** |
| **X2: M·M^† = 35·I** | 0 | **PASS (exact)** |
Run time ~2 s.
## Consequence (as fixed in PREREG)
With fact (i) (Y(−x) = conj(ΠY(x)) for real-weight sums; proved), the order45 identity is now **Category A, proved**:
R_Y(1/x) = −x^{−1}·conj(Π(kM)^{−1}R_Y(x)) and ‖R_Y(1/x)‖ = ‖R_Y(x)‖/|x|.
## v11: YES
papers/RTA_FOUNDATION_BOUND/RTA_FOUNDATION_BOUND_v11.pdf, 135 pages (new files: main_v11, front_v11, partIII_inv_v11, appD_v11, NOTES_v11.md; v10 untouched).
New: Proposition (exact, computer-assisted) conj(M)ΠM = 35Π and MM^† = 35I; Theorem (x ↔ 1/x symmetry for real-weight sums); Category B remark; App. D item.
