# FINDINGS — PP Soft SF audit — Eigen O5/O6 lane-resolution 3af326ba… — 2026-11-05
REPORTS ONLY. No CERT. Tip 7cddb188… tip_touched NO. invent HOLD STANDS.
Authority: OW a0c2ed5a… (MATCH). FINDINGS 3af326ba… and PRESS 6d8f228a… (bridges/AUDITOR) MATCH their sidecars. The compute dir SHA256SUMS all check OK.
O5:
- Kr QQ, zero-polar and G1-mem are all REMAINING. They are not over-claimed: CONFIRM.
- The mod-p Galois fact (Kr invariant under ζ₄₉→ζ₄₉² at a single prime 7840981) is correctly worded as "suggests" Q(√−7). Arithmetic check: 2 has order 21 in (ℤ/49)^×, and its fixed field in ℚ(ζ₄₉) is the unique quadratic subfield ℚ(√−7). This is consistent.
- PP re-read the log: Q(√−7) holdout 0/3000 and Q-only 0/3000. These MATCH the claim.
- NOTE: a single-prime invariance is a diagnostic, not a proof of the field of definition. A σ₃ test is still needed, as the FINDINGS states.
O6:
- PP re-ran o6_target_check.py: target [0] gives W2/N4, [1] gives W0/N2, [2] gives W4/N4, and no target state is named in the corpus at §2.1. The output MATCHes.
- ABSENT, with [1] inferred and not stated: CONFIRM. A target needs an Owner/author-stated reading before it can be used.
Verdict: CONFIRM, 1 NOTE. Soft SF → Keeper.
