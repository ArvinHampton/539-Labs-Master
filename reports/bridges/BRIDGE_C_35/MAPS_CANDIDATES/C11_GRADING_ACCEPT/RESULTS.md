# RESULTS: C11_GRADING_ACCEPT
PREREG.md sha256 eeb29cc9304cdc95a47103c4285d45f67cd654862c50c3688d4eb56a0d71c61b, hashed before scripts/test.py ran. Grading g = (−1)^τ, accepted by Arvin on 2026-10-24 (message accepting g and P_res).

| fibre r | block size | predicted S_r | measured S_r | holds? |
|---|---|---|---|---|
| 0 | 68 | 0 | 10 | no |
| 1 | 68 | 0 | 12 | no |
| 2 | 68 | 0 | 12 | no |
| 3 | 67 | ±1 | −13 | no |
| 4 | 67 | ±1 | −13 | no |
| 5 | 67 | ±1 | −11 | no |
| 6 | 67 | ±1 | −13 | no |
| 7 | 67 | ±1 | 13 | no |

g is non-constant (268 values of +1, 271 of −1), so the test is non-vacuous. Total Σg = −3; prefix-18 sum −2, body-521 sum −1 (descriptive).

**Verdict: C11 FAIL, Category A** (exact finite computation; the outcome was disclosed as expected in the PREREG, i.e. not blind). **Bridge: NO.** Map-C11 (P-even A₁ = 0 → fibre-block balance) is refuted under the accepted grading.

Mechanism (post-hoc, descriptive): towers span 21 or 20 integers, i.e. about 2.2–2.3 consecutive j. Over j, g is a square wave of period ≈ 4.5. Sampling it at stride 8 (one fibre) gives a slow beat, not cancellation, so the |S_r| ≈ 10–13 are coherent sums, not ±1 defects. All 8 conditions fail, not just a few.
