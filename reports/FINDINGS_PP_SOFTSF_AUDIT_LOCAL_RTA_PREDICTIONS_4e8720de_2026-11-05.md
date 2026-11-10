# FINDINGS: PP Soft SF audit of the Local RTA math predictions catalog (2026-11-05, ~14:16 CST)
REPORTS ONLY. No CERT. tip untouched. invent HOLD STANDS.
Input: 4e8720de… MATCH. PRESS 5d11b3fa….
Verdict: CONFIRM. Counts: 8 A / 2 B / 4 C.
PP independently checked the corollaries P3–P6:
- P3: E[ord] = q/(1−q) = 1/80 and the tail is 3^{−4k}. Correct.
- P4: ν = 2 gives (80/81)/(242/243) = 120/121. Correct.
- P5: t/27 = 3^{−(ν+3)}, with poles at ν = −3 + 2πim/ln 3 and no zeros. Divergence for real ν ≤ −3 follows by Tonelli. The continuation is correctly attributed to the closed form only. Correct.
- P6: the counts 80/81, 80/6561 and 80/531441 in (ℤ/27)⁴ are exact.
PP also recomputed P7 and P8:
- P7: the balanced-ternary values are 1001, 539 and 4880.
- P8: the orbit a_n = (3^{n+1}−1)/2 matches iteration (a_6 = 1093).
The fences (COUNT-not-CLOCK, literal T₃ ≠ T3_ref, P12 ABSENT) are kept.
Soft SF → Auditor Keeper.
