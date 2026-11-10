# RESULTS: PATTERN_BNU_RR (Map-PBR1, Map-PBR2)
PREREG sha256 51050fe71935c8113088b4eea76cf5684177ace94b69a11f38798104ac7f33bb. Hashed after explore and before test (logs/test.log).

| fibre | ρ_res (MF2) | PBR1: 10·B(ν,a) mod 8 | PBR2: 140·T-phase mod 8 |
|---|---|---|---|
| 0 | 1/32 | 1/8 | 8/35 |
| 1 | 1/4 | 1/8 | 11/70 |
| 2 | 3/32 | 1/8 | 0 |
| 3 | 0 | 1/8 | 9/70 |
| 4 | 7/32 | 1/8 | 19/70 |
| 5 | 1/4 | 1/8 | 3/35 |
| 6 | 5/32 | 1/8 | 0 |
| 7 | 0 | 1/8 | 9/70 |

- PBR1: TV = 3/8. This is uniform on all 8 fibres (not uniform-on-6, so not VACUOUS by the PREREG definition), but it carries no information. **FAIL (Category A).**
- PBR2: TV = 71/140. Mass 9/35 sits on {3,7}, and fibres 2 and 6 are empty. **FAIL (Category A).**
- Both maps escape PS1a (fibres 1 and 5 get mass), but neither matches.

Bridge: **NO.**
