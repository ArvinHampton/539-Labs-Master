CATEGORY B NOTES
OccFilt_7(infty) / Theorem L / C_third, 2026-10-17
Every item in this file is CATEGORY B (heuristic, numerical, truncated, analogy, or unverified) or OPEN. Nothing here is a lock.
Companion to the Category A ledger U1_LEDGER_OCCFILT7_INF_THEOREM_L_Cthird_Zwegers_2026-10-17.md.
Sources (verbatim copies). OccFilt7_Inf_Theorem_L_2026-10-17/ (the three 2026-10-17 reports and their scripts).

Caveats. Computer-assisted work; Theorem L audited once, not formally verified. No TPC or RH claim. Distinct from HQCC termination claims. Residual is not Resonant (539 is a count). CORE_FREEZE untouched.


B1. Asymptotics (Category B)

- c = 0.39854 (closed form 0.398540028615674...) as the TRUE growth exponent of g_7(d). Rigorously only [0.398263, 0.398875] is pinned (Cat A, ledger). Fit over 2000 < d <= 10^6 per class mod 14: c = 0.39850 to 0.39856, b ~ -0.5 (Category B).
- E_d/O_d -> (1 - sqrt(1-y^2))/y = 0.5443407 as the TRUE limit. Measured 0.54451 @10^5, 0.544396 @10^6, 0.5443594 near D0, 0.5443583 near 10^7; gap ~ d^{-1/2} (Category B). The algebraic identity for the number is Cat A; the limit is Category B.
- O*/O -> y (0.83983; measured 0.839152 @10^5). E/O* -> 1/(1+y^{7/2}) (0.648153; measured 0.648886 @10^5). Category B.
- Class weights 1:2 (class 0 vs classes 1, 2, 4). Category B.
- The d^{-1/2} power; at d = 10^6, log|g| ~ 390.1 vs c sqrt(d) = 398.5, consistent with a -(3/4) log d-type correction. Category B.
- Sign pattern past the last sign change: sign g_7(d) = -(-1)^d; last sign change class 0 at 1127/1134, class 1 at 407, class 2 at 247, class 4 at 60. Observational, Category B.
- A000700 asymptotic exp(pi sqrt(m/6))/(2^{7/4} 3^{1/4} m^{3/4}) quoted from the OEIS formula section, no theorem number. Category B.


B2. Saddle-point heuristics (Category B)

- y root of y^7 + y^2 = 1 (y = 0.8398331470), u0 = -(7/2) ln y = 0.6109321448, V = (pi^2/6 - Li2(y^7))/4 - u0^2/7 = 0.2779597702, predicted c = 2 sqrt(V/7).
- Mechanism: at the saddle n ~ u0/eps, T_{2k+1}/T_{2k} -> y/(1 - y^{7/2}) ~ 1.8365 > 1, so odd n beat even n by a fixed factor. Heuristic only.
- Heuristic that zeros are finite (superseded in outcome by Theorem L, but the heuristic itself stays Category B).


B3. Injection / rho-window / transport tables (Category B, exhaustive exact checks on finite ranges only; not proofs)

- Fixed termwise injections (reflection, n -> n+7, n -> n-7) fail for every d tested up to 40000 (out_pairing.txt); failing terms up to ~15% of mass in classes 0 and 1, ~1e-5 in class 2 (out_window.txt).
- Averaging rule e_n <= (o_prev + o_next)/2 fails for all d tested up to 40000 (out_avg.txt).
- rho-windows (out_regions.txt, n <= 148, m <= 6000): rho_U falls ~0.68 -> 0.51 (gap-7/gap-5), ~0.223 (gap-1); rho_D rises ~0.51 -> above 0.73; saddle rho* ~ 0.60 inside the overlap.
- Fractional-transport design (block rules R, S+, S-). Heuristic design; route 3 block lemma replaced it.
- Numerically O*_d < O_d for all allowed d > 2738.


B4. Numerical cross-checks of route 3 (Category B)

- Chernoff + T1 holds for all 756,131 nonzero a_n(m) with d <= 40000 (max excess -0.707).
- Exact float DP at n = 900, u = 0.6: local-CLT error 0.0236 in delta-units vs rigorous delta <= 0.152; mu/n^2 = 0.61600, sigma^2/n^3 = 1.33551 inside enclosures.
- Audit spot tests: empirical delta 0.019-0.031 vs rigorous 0.115-0.151; empirical block ratios <= 0.563 / 0.559 / 0.596 vs rigorous 0.7227-0.7727; hardest class (2) agrees.
- Limitation: d <= 10^6 is below the n >= 900 regime, so block inequalities are not testable on exact data in their range of validity.
- Signed long-double ladder is numerically unstable (ladder.py, not used).


B5. ADH sigma(q) analogy (Category B as an analogy)

- Andrews-Dyson-Hickerson, Partitions and indefinite quadratic forms, Invent. Math. 91 (1988) 391-407 (as cited in the Lever 3 md; no theorem number used). sigma(q) = sum q^{n(n+1)/2}/(-q;q)_n has infinitely many zero coefficients and tiny coefficients; the source md lists those cited facts as Cat A by citation, but they are not relied on in the ledger.
- The comparison "g_7 grows, sigma cancels, so g_7 behaves differently" is Category B analogy.


B6. Zwegers numerics (Category B)

- Cor. 2.9(5) on theta_{a,0}, tau = it, 35 classes, n,k in [-60,60]: t = 0.9 diff 1.7e-16; t = 1.3 diff 5.9e-17 (after erfc fix; plain erf run disagreed ~1e-10).
- The formula and hypothesis check are Cat A (ledger); these numbers are Category B.


B7. Lever 1 negatives and Bailey searches (Category B)

- Bailey inversion (a = 1, base q, beta_n = 1/(-q^s;q^s)_n) for s = 7, 8, 11: alpha_n non-polynomial; only (-q^s;q^s)_n clears denominators; numerators dense (s = 7, n = 1..5: 5, 14, 25, 43, 78 terms). Truncated at q^400, n <= 5-7.
- "No terminating Bailey pair for s >= 3" / no published Bailey pair fits g_s for s >= 3: rests on truncation and a non-exhaustive search (Slater's list not searched exhaustively). Category B (moved here from the requested ledger list; the source md marks it Category B).
- s = 2 closed form alpha_n = 2(-1)^n q^{n(n+1)/2}(1+q^n)/(1+q^{2n}): guess fitted for n <= 7.
- F3 g_7 retry: split n = 7m + j moves but does not remove the base mismatch; a = q non-terminating at s = 7 to q^300; conjugate pairs in base q^7 cannot produce q^{n^2}. Verdict: no Hecke form found for g_7; stopped.
- First implementation of the last line of HM (4.5) did not match; cause not found; no claim either way.


B8. Mock theta comparison (Category B, from the status report)

- First 61 coefficients of g_7, g_8, g_11; no OEIS hit for g_7, g_8; g_11 vs A025441 spurious.
- No match with 3rd-order f, 7th-order F_0/F_1/F_2, 8th-order S_0/S_1/T_0/T_1 (suggestive only).
- Possible PhiStab + partial-theta route for a Hecke form of g_s: unexecuted.
- Andrews-Berndt entries not checked page by page; Zagier QMF references cited for concepts only.


OPEN (unchanged)

- C_third ALONE (positive-cone remainder sum_{n>=0,k>=1} q^{Q_+}; not a theta function; not shown mock modular).
- Object B. Per_off. Remark 8.5. Slash_two.
- QM of g_s for s = 7, 8, 11 (CONJECTURE).
- Two-sided effective bound |E_d/O_d - 0.5443407| <= delta(d): not achieved.
- Multiplicative asymptotic exp(c sqrt d + lower order)(1 +- eps(d)): not achieved.

Hygiene. CATEGORY B throughout. Computer-assisted; one audit. No TPC or RH claim. Distinct from HQCC. Residual is not Resonant; 539 is a count. CORE_FREEZE untouched.
