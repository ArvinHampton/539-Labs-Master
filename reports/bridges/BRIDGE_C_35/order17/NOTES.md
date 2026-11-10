# order17 NOTES (disclosures)
- Order: PREREG written and hashed (d3938e1c…e049) → k1t1.py hashed in scripts/SHA256SUMS → run → verdicts recorded in RESULTS → post-hoc diag_posthoc.py (hashed after).
- T1 primary FAIL is recorded by the preregistered relative-residual rule. The target A1c is identically zero (‖A1c‖ = 4e−14), so r ≈ 1 is noise/noise; the rule was not designed for a zero target (same defect as order13 W2d). Verdict unchanged; reading is post-hoc.
- PREREG predicted Π+A1c = ½A1(S^E) ≠ 0 and T2 FAIL on Π+. In fact ½A1(S^E) = 0. Theorem E (A1(S^E) = 0) was found from this zero and proved afterwards (quadrant-pair cancellation with odd B̄1). It is Category A but post-hoc in origin.
- Part 2: Zwegers law ↔ (35^{−1/2}M, T), χ=1 is Category A by citation (Zwegers thesis Cor. 2.9) plus the verbatim match with the symbol S/T rules and the exact closure in S_rows/T_rows. Residual dependence: the exact printed form of Cor. 2.9; numerics of orders 5/6/11 corroborate. No further certificate needed.
- Theorem R relies on the Schwartz property of the completed odd kernel, argued via Zwegers' convergence estimate (noted as a problem in the paper NOTES_v5).
- The K1 gate shares the phase code (order2 lib2.phase_ints) with order3 parts; the formulas (wall sawtooth vs piece decomposition) are independent.
- No new Residual–Resonant map; E1–E3 OPEN. Framing (local mock / non-local quantum modular; "residual geometric bridge") remains opinion; no bridge claim.
- Runs: nice, OMP_NUM_THREADS=1, peak well under 3 GB, ~3 min. No push, no sends. New files only.
