# A42 AMENDMENTS (created at run time by the A43 run, 2026-10-22, America/Chicago CDT)

Written BEFORE any evaluation at k = 49, 77, 539 or any control.

## Pre-run checks
- prereg.md sha256 verified: ae93ad54a795babc6297cf6ac8960269728b68fd3b5de91a0c10267aa3a94405 (match).
- Prior aborted attempt: neither SF/A43_bridge_run/ nor A42_bridge_prereg/AMENDMENTS.md existed at start, so nothing was moved to A43_bridge_run_aborted/ (none created).

## Frozen inputs (sha256)
- A41_uniform_oddk/REPORT.md  7ec18f976ee542e3ad2c75b51ff6f3bc5201b5c5844ebd950e50076d2b8ed802
- A41_uniform_oddk/REPORT.pdf b23365d5f129bff5de8257542dc40c33ea7a020c303b9fd9544499f2a8ac6e97
- A41_uniform_oddk/SHA256SUMS d0cc4f54ff7cd66fc93ee3d5e261ef81ad4a58bcfd8a56fa93c6c4d9248f0368
- A44_oddk_audit/REPORT.md    2a959e0393c2aaa6a69f550fdbd301c7d92c0addd99ddb008967dd32a6dd05ff
- A41 verdict used (only this, per §6): "No uniform closed-form identity was found" -> **Branch II: P1.3 NOT RUN** (stays in m = 14, no alpha reallocation).
- A44: all items VERIFIED; minor gap only in max-min step of the growth constant (irrelevant to A42 cells).

## Code (sha256, before first run; SF/A43_bridge_run/scripts/)
- eo_indep.py ba55c8e29afc60a350128bb6605be7bdbe87b9b4ca2d4f02781147adecc636b0 (byte-identical copy of A40 exact/eo_indep.py)
- gcert.c     8cd7934bc41af60fcb21c45894dcfe2d159d8ff3e623fd6c266d7fac0ddeecbd (byte-identical copy of A41 cert/gcert.c)
- eo_gmp.c    e72ba8b9b9c01fb48cb9663592659bfa9facda695c52a4bb6a385353f548f6e9 (new; see D1)
- draw.py     reproduces the seed-20261022 list of §5.1 exactly; seed 20261023 gives 407 413 425 475 481 493 497 511 515 533 535 545 551 595 611 635 667 679 695 697.

## Deviations / resolutions of unspecified points (fixed before looking)
- D1 (implementation). Pure-Python eo_indep.py to d <= 2e6 for ~500 control k is infeasible in the time budget. eo_indep.py (unchanged) is run at k = 49, 77, 539 at D = 2e6. All other k use eo_gmp.c: the same ladder in exact GMP integers, computing G exactly, checking sign(b_n(m)) = (-1)^m for every term (signbad = 0 required) so that (-1)^d G(d) = E_d - O_d exactly. Validated before use against audited A40/A41 outputs (k = 7, 11 at D = 3e5; k = 17, 25 at D = 5e5): zero lists and last E>=O identical, signbad 0. It is also cross-checked against eo_indep.py at k = 49, 77, 539.
- D2 (ranges). As declared in §2.2: exact to 2e6, two-prime gcert to 2e7 (primes 2^61-1, 10^18+3). Z(k), L(k) are taken from double zeros in [1, 2e7] (exact zero set required to equal the double-zero set on [1, 2e6]); T(k) from exact E/O on [1, 2e6] only (mod p cannot give the sign). No dominance tail is proved for any k here, so all P1.2 statistics are finite-range (evidence) per §2.2.
- D3 (T(k) if no allowed d in [1, 2e6] has E >= O): T = 0 (not in R).
- D4 (R_N ladder). R_N = {18, N-18, N, N+1, ord_N(3), phi(N)} U {(N+1)*f : f in {1/108,1/54,1/36,1/18,1/12, 2,3,4,5,10}, integer results only}  (the 5,10,15,30,45 of R are 540/108, /54, /36, /18, /12).
- D5 (R_N per-cell statistic). For the random-integer version a control N "hits" statistic X if X(k') in R_N for some composite k' in K_N = {composite divisors of N} U {N} (mirrors the composite 49, 77, 539; primes 7, 11 are anchors). The 539 side is counted as a hit for X if any of X(49), X(77), X(539) is in R. p = (1 + #hits)/(1 + 20). Minimum attainable p = 1/21 > alpha_c, so this version cannot pass on its own; it is reported for replication (seeds 20261022 and 20261023).
- D6 (pool). All-odd-k pool = odd k in [27, 999] with k not dividing 539: 484 values (prereg said ~485). Shape-matched controls (subsets, plus 9, 15, 25 below 27) reported as secondary hit rates; decision uses the pool as written in §5.3.
- D7 (M3 orders). Character orders are read from A36 REPORT.md §eigen-system table (as identified by A36: s=9 quadratic ray; s=11 ring order 4 + ray with values of order 4; s=23 three quadratic ray; s=25 ring order 3 or 6, ray with values of order 6, quadratic ray). No new computation. Orders inferred from 8 sampled primes are lower bounds (divisors of true order); flagged evidence.
- D8 (observation from residue arithmetic only, not an outcome): at k = 7, d = 18 has exactly one contributing n (n = 2), so 18 is a forced nonzero and 18 notin Z*_7 by construction. P2.1 is still run/recorded as declared; the prereg §2.3 had not listed this exclusion.
- Job order interleaves controls with 49/77/539 (deterministic shuffle, seed 539, recorded in data/joblist.txt).

## Amendment added during the run (2026-10-22 16:12 CDT) — correction of D8, BEFORE any P1.2 result was looked at
- While evaluating P2.1 from the audited A40 k = 7 double-zero list, d = 18 is found to be a certified zero of g_7 although only n = 2 contributes: phi_2(2) = [x^2] 1/((1+x)(1+x^2)) = 0. So the prereg premise in §2.1 "exactly one n contributes, so g_k(d) = ±phi_n(.) != 0" is FALSE in general (phi_n(m) can vanish for n >= 2; phi_1 never vanishes, so the §2.3 exclusion of d = 540, where only n = 1 contributes, remains valid). D8 above is withdrawn.
- Rule fixed now for all cells (before P1.2 values were seen): PRIMARY Z*_k = certified allowed zeros d >= 1 with at least one contributing n (i.e. the prereg's "nontrivial zeros": all zeros not forced by the absence of contributing n). SENSITIVITY (literal §2.1 wording) Z*lit_k = zeros with >= 2 contributing n. Z, L are reported under both; the decision uses PRIMARY, and any cell whose outcome differs between the two readings is flagged.
- P2.1 is reported under both readings; with base rate >= 0.18 it cannot reach alpha_c in either.
