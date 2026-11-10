# PREREG: MAPS_CANDIDATES/BATCH2 (Map-C7 to Map-C11)
Written 2026-10-24 at about 6:35 PM CDT, before any BATCH2 test. Owner: Arvin Hampton. New files only. CORE_FREEZE. All maps are **Category B** until proved; a pass is a survived prediction, not a Residual–Resonant bridge. C1–C6 are not reused. No T3/O_res/Π q-series is constructed. Runs: nice, OMP_NUM_THREADS=1, ulimit -v 3000000.
Sources:
- Modular: the 35-component law vector symbols (A35_lawspace_exact/symbols.py T_rows, phases e(k/9800)); Prop. Z (Zwegers law (35^{−1/2}M, T), χ = 1, order17); hybrid shadow (order15); A₁ split, P-even A₁ = 0 (order17).
- Residual: canonical T3 (oct17-master/README.md); L = 18+521 = 539; N_star = 14 (grok-chats/raw/chat-03.txt).

## Map-C7: T-matrix order vs the 7-part of 539 (modular → residual)
Source: M_T on the 105 symbols (monomial, phases e(k/9800)). Target: 539 = 7²·11.
Prediction (NEW): the order of M_T as a 105×105 monomial matrix is divisible by 49, and is not divisible by 11.
PASS iff both hold (exact integer arithmetic).

## Map-C8: maximum free T3 depth on [1,539] vs the window (residual-internal)
Prediction (NEW): max_{1≤n≤539} (free T3 steps from n to 1) = 18.
PASS iff the maximum is exactly 18 and every n reaches 1 (cap 10⁵ steps).

## Map-C9: short-basin count vs the body (residual-internal)
Prediction (NEW): #{n ∈ [1,539] : free T3 steps to 1 ≤ 14} = 521.
PASS iff the count is exactly 521.

## Map-C10: hybrid shadow → Π segments (modular → Resonant). OPEN
Source: four shadow pieces (three P-odd unary thetas plus the P-even e₂ Laplacian defect). Target: Π.
Prediction: Π, written as a 539-step word, splits into exactly 4 maximal segments of constant T3 branch-type class, with lengths ordered like the theta norms (1/34 < 5/2 < 35/4).
Next measurement: a written, hashed 539-step Π from residual sources. Not available, so OPEN.

## Map-C11: P-even A₁ = 0 → ±1 balance on the fibre blocks (modular → residual). OPEN
Prediction: under a written ±1 grading of O_res elements, every one of the 8 fibre blocks has signed sum 0 for the 68-blocks, with an odd defect ±1 for the 67-blocks.
Next measurement: a written ±1 grading on O_res (none located). OPEN.
