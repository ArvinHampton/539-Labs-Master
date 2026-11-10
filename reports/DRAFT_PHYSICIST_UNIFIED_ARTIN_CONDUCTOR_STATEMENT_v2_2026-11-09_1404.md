# DRAFT v2 — Unified statement bounded by the Artin conductor
Physicist and Mathematician, 2026-11-09 ~14:04 CST (America/Chicago). Additive successor to 65b367ef (unchanged). Applies Auditor cross-check 034605bf. Not adopted; no CERT; tip 7cddb188 untouched.

Setup as v1. "D̂1" below = PP's D̂1 (bd3730eb), not the residual D1 or the BH-slot D1.

## PROVED
1. f = 7.4.a.a: a_7 = -7, Steinberg at 7, eps_7 = +1 (root number +1); conductor exponent 1, tame.
2. f ⊗ chi_{-7}: conductor exponent 2, level 49, a_7 = 0; the unique matching rational newform at level 49. Its Atkin–Lehner sign at 49 is W_49 = -1 (Auditor PARI, 034605bf).
3. Among twists of f by characters of conductor 7 (tame at 7), the 7-part of the level is at most 49. [v1 "any twist" was FALSE: a wild order-7 character mod 49 gives conductor 7^4 = 2401.]
4. U(140) ≅ C2×C4×C6 (= [12,2,2]), order 48. Q(sqrt(-7)) and Q(sqrt(35)) characters mod 140; 23 splits in both.
5. a_n ≡ n^13 sigma_19(n) mod 49 for 7∤n, n <= 5311; fails mod 343 (n = 2).
6. 539 = 7^2·11 = floor((4880-21)/9) = 3·68 + 5·67.
7. λ(s_alpha δ) = 1 on truncated F (PP's D̂1 setting).

## CONDITIONAL
- Congruence for all n: on Chen–Kiming.
- D̂1(s_alpha δ) = 1 as a project statement: on the DP-a normalisation / Owner adoption (B14-3).
- T3^539(4880) = 2 (exact computation) as the project's step: on DP-b adoption.

## OWNER DEFINITION
- "W7 = +1" means eps_7 on f at level 7 (OW c4c0f1c0). Path C (rho(W7) absent on V42) stands.

## OPEN
- P5a's level-49 referent. f ⊗ chi_{-7} has W_49 = -1, so it cannot carry "+1" under Γ0(49)+; it is not a referent unless the Owner rules otherwise. Level 49 carries W_49 only, no separate W_7.
- Any link among 7^2 in 539, U(140), V42 and D̂1 beyond the shared prime 7; no role for 11; 980 is not the level of any quadratic twist of f.
