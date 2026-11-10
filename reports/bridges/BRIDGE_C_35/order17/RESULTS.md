# order17 RESULTS
PREREG sha256 d3938e1c034b961d3577d3253bb3d836f189db7542fea0923fe2d4a2e313e049 (written and hashed before numerics).

## Verdicts by the preregistered rules (recorded first)
| test | value | verdict |
|---|---|---|
| C0 control (fixed-M law on A0) | r0 = 1.3e−15 | PASS |
| K1 gate (Cor. R1 + line terms + P) | e = 1.0e−15 | PASS |
| T1 primary, weight ½, full A1c | r = 0.9991 | **FAIL** |
| T2 w=0, w=1, full | r = 0.9994, 0.9992 | FAIL |
| T1/T2 on Π+A1c (w=½,0,1) | r ≈ 0.996 | FAIL |
| T1/T2 on Π−A1c | r ≈ 0.99999 | FAIL (vacuous by PREREG) |
Predictions: K1 PASS (correct), T1 FAIL (recorded), Π+ FAIL (recorded).

## Post-hoc reading (disclosed; not a change of verdict)
‖A1c‖_F = 4.0e−14 against ‖A1_lit‖_F = 63.35 (relative 6e−16): A1c is zero to rounding at all 216 points and at their −1/x images, in both sectors. The relative residual r is a ratio of rounding noise, so T1/T2 are non-discriminating (same zero-target defect as order13 W2d). Diagnostics (scripts/diag_posthoc.py): ‖Π+(A1_lit − A1_lines)‖ = 2.4e−14, ‖Π+ A1_pred‖ = 8.7e−15, ‖Π− A0‖ = 1.4e−15.

## Category A (new, proofs in NOTES / paper v5)
- Prop. Z: the Zwegers law of Ĥ, Ĝ_O is exactly (35^{−1/2}M, T), χ = 1 — Category A (Zwegers Cor. 2.9 + verbatim match with the symbol rules + exact closure). App. D item sh2 is no longer needed as evidence.
- Thm. R: the completed P-odd series has A_j = 0 for all j at every rational x.
- Thm. E (found from the zero target, proved afterwards): A1(S^E) = 0 for every companion and rational x (the ++ and −− quadrant boundary terms cancel class by class because B̄1 is odd).
- Hence A1_lit = A1(lines) + A1(S^o) exactly, and **A1 minus the explicit completion and line terms is identically 0**. A weight-½ (or any) fixed-M law for it holds only vacuously.

## Paper
RTA_FOUNDATION_BOUND_v5.pdf built (see NOTES).
