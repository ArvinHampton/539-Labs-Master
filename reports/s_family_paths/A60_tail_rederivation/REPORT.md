# A60 REPORT: independent re-derivation and re-implementation of the tail step (g_k, odd k = 17..33, N1 = 1500)

Category A (computer-assisted mathematics). Times are America/Chicago (CDT). Directory: `reports/s_family_paths/A60_tail_rederivation/`; every file here is new. No TPC/RH claim, nothing beyond the statements below.

## 0. Outcome

**Category (a): confirms.** With my own derivation and new code (python-flint arb at 256 bits, exact integers, C modular arithmetic):

* The tail inequality closes for every odd k = 17..33: T(D0) = -39.38 (k=17) ... -29.67 (k=31), -28.55 (k=33) in the convex-endpoint mode, with D0 = ceil((N1/alpha_1)^2) = 53 864 548 (k=31) and 55 887 431 (k=33). Monotone for all d >= D0 (gap gamma = -0.0088 / -0.0085, criterion gamma <= -2.5/sqrt(D0) = -3.4e-4 holds by a factor ~26). My T is 3.6 to 4.0 LOWER (stronger) than A56's TIGHT/SHARP T for every k (A56/A57: -26.02/-26.10 (k=31), -24.98/-25.05 (k=33)); my D0 is 0.31 % to 0.34 % LARGER than A56's (ratio 1.0031..1.0034), which is inside the 0.5 % band I preregistered. A larger alpha_1 or D0 is not an error either way (section 3).
* Exact zero sets (Python integers, d <= 300 000 and, as an extra, d <= 2 000 000): counts/maxima k=27: 68/1375, k=29: 121/1934, k=31: 127/1712, k=33: 88/1587, all equal to the claimed values; the full lists for k=31 and 33 equal the lists printed in A57 element by element.
* E-O identity: (-1)^d g_k(d) = E_d - O_d verified (a) against the q-series definition (phi recursion) and (b) against the product formula for a_n, d <= 20 000, all k = 17..33: 0 mismatches; a_n(m) >= 0 in every entry (0 negative entries), nonallowed d give E = O = 0.
* Finite certificate: modulo p1 = 2^61-1 and p2 = 4611686018427387847 up to D_cert = 1e6 * ceil(D0/1e6) (>= D0 for every k; 54 000 000 for k=31, 56 000 000 for k=33): the double zeros equal the exact zero set for all nine k, no double zero above 300 000, no single-prime zero.
* Ball-arithmetic artefact: confirmed, but with a correction to where the loss comes from (section 5). Using A56's source structure after the freeze I reproduce the quoted A57 numbers to 0.01: ball mode T = +2.709 (A57: +2.714, k=31), +4.373 (+4.385, k=33); convex mode -26.100 (-26.096), -25.052 (-25.051). About 22.5-23.5 of the ~29 lost in ball mode comes from the ball lower bound of the central odd term over the alpha-window of width 2k/sqrt(D) (~0.009), about 6 from the 0.0025-wide tail boxes.

Not claimed: the local-CLT layer (enters only through the single hypothesis H_CLT below, not proved here), the block ratio R_k < 1 - eta_t (not re-derived), PD itself for any k. The statement delivered is: given H_CLT and the block step, the tail part of E_d is <= eta_t * O_d for all allowed d >= D0, and for allowed d in (max Z_k, D0) g_k(d) != 0 by the certificate.

## 1. What was done and in what order (precise timeline)

Evidence for ordering: terminal `date`/`stat` output at the time of work, `mtime_prereg.txt` (written by `stat` right after the prereg was hashed), log contents. Filesystem mtimes were reset: the box restarted at 22:21:44 CDT and the track directory was restored at 22:24:49 CDT with EVERY file re-stamped (22:24:49) and `out/` missing (A61 documents the same event, `A61_clt_proofs/out_regen_note.md`). So the mtimes of `prereg.md`, `prereg.sha256`, `mtime_prereg.txt`, `DERIVATION.md` and the code files are now 22:24:49 or later; they do NOT show the original order. The original times are:

| time (CDT, 2026-10-22) | event | evidence |
|---|---|---|
| ~21:45 | task received; A56/A57 `REPORT.md`, A57 `prereg.md` read (statements only); A59 directory listing / `prereg.md` head and `FREEZE_time.txt` read for format only | transcript |
| 21:53:05.30 | `prereg.md` and `prereg.sha256` written and hashed (before any code or run) | `mtime_prereg.txt` content (survives the restore); `sha256sum -c prereg.sha256` still OK (sha256 2097d404...94ab) |
| 21:54:33 | first `DERIVATION.md` written (before code) | `date` output |
| ~21:55-22:00 | `a60lib.py`, `j2_selfchecks.py` run (closed forms, Riemann bracket, Chernoff and odd lower bound checks), `j3_window.py` | outputs seen in transcript; `logs/j2_selfchecks.log`, `logs/j3_window.log` regenerated |
| ~22:00-22:06 | first full tail run (`tail60.py`), `exact60.py`, `modcert60.c`, sanity runs. The first tail run used an x-bound with a spurious factor 1/y (kappa 0.009 instead of ~0.7); found by hand (x ~ 2y/alpha*), corrected in code and in `DERIVATION.md` (section 9, revision log) BEFORE any comparison with A56 numbers except the table already in the REPORT.md files; first-run log kept in `logs/superseded/`. The corrected tail run produced `tail_k17.json` etc. at about 22:03-22:10 (this is the 'about 22:06' in the task note) | transcript, `logs/superseded/j5_tail_all_first_run_xbound_bug.log` |
| 22:05-22:28 | modular certificate, k=17..25 (`logs/j7_jobs_before_restore.log`) | log |
| 22:21:44 / 22:24:49 | box restart / restore: all mtimes reset, `out/` lost, running jobs killed | A61 note; observed |
| 22:29-22:57 | ALL outputs in `out/` regenerated from the unchanged code (`run_chainA.sh`, `run_modcert.sh`); results equal the pre-restore numbers seen in the terminal (e.g. T(27) = -31.3746, T(29) = -30.6278, T(31) = -29.6702 both before and after) | transcript, `logs/` |
| 22:57:17 | FREEZE: sha256 of code/, out/, logs/, DERIVATION.md, prereg files in `FREEZE.sha256` (88 files); `FREEZE_time.txt` | stat; `sha256sum -c FREEZE.sha256` still passes |
| after 22:57 | A56 source read (`proof/tails56.py`, `params56.py`, `run_pd56.py`, `cert/modcert.c`, `exact/eo56.c`, `exact/gexact.c`), diff in section 6; `code_post/` written; then A61 REPORT read for context only | `code_post/` |

Independence, stated honestly: the A56/A57 REPORT.md files contain the formulas for F(alpha,u), Phi1, the +-log 2 and g(u) terms of the log A_n bounds, the window rule, the formula T(D) and the -2.5/sqrt(D) criterion, and the numbers T, D0, alpha_1, alpha_2. So the derivation is a re-derivation guided by those statements, not a blind one: I re-proved every lemma with explicit constants (and found different, tighter constants in places), and the code is new, but I knew the target values. No A56/A57 source was read before the freeze. No routine is copied from anywhere; nothing was imported from A56/A57/A59/A61. The A61 findings and proofs were read only after the freeze.

## 2. The derivation (summary; full text in `DERIVATION.md`)

1. A_n(x) = prod_{j odd<=n}(1+x^j) prod_{floor(n/2)<l<=n}(1-x^{2l})^{-1}, so a_n(m) >= 0; (-1)^d g_k(d) = E_d - O_d (odd k).
2. Chernoff for EVEN n with no additive constant: log A_n(e^{-u/n}) <= n Phi1(u) (convexity of log(1+e^{-x}) gives the midpoint bound on odd j, monotonicity of -log(1-e^{-x}) the bound on the l-sum). Hence e_n <= exp(sqrt(d) F(alpha,u)). A56/A57's form `n Phi1 + log 2 + g(u)` is weaker and also valid (A61: upper bound proved for even n only; the tail uses only even n).
3. Odd lower bound: log A_n >= n Phi1 - (1/2) log 2 - (1/2) g(u) (odd n).
4. F convex in alpha: F_alpha_alpha = 2u/(k alpha^3) > 0. For fixed u, sup over [a,b] of F is exactly max(F(a),F(b)); no ball loss.
5. Tiny alpha <= 0.005: u = 1.5 alpha, Phi1(u) <= (1/2)(1 - ln 2 - ln u + 3u/4) (from 1-e^{-s} >= s e^{-s/2}), F <= B(alpha) + c/k, increasing in alpha.
6. Central odd term: odd n_c within k of alpha* sqrt(d) in the square class; fixed tilt u*; x = m - mu_n(u*) bounded by 2 y^2 (alpha*y+k)^2/(alpha*y-k)^3 + a_M n + b_M, sigma^2 in [S_lo n^3, S_hi n^3] (Riemann midpoint lemma, explicit constants, all n >= n0c); H_CLT with delta_H = 0.15 gives log o_c >= y F* - C_o(y) (tangent correction k|F_alpha| ~ 1e-15).
7. D0: alpha_1 = 1/sqrt(1+k M_lo(UA)), M_lo from the same midpoint lemma at the point UA (n >= N1-k), D0 = ceil((N1/alpha_1)^2); the tail is even n with alpha <= alpha_1 or >= alpha_2.
8. T(y) = ln(y/2) + y gamma + C_o(y) - ln eta_t; T' <= gamma + 2.5/y.

Hypothesis H_CLT (used, not proved): |sqrt(2 pi) sigma P(S=m) - exp(-x^2/2sigma^2)| <= delta_H = 0.15 at u* for all n >= n0c. The inequality needs delta_H < exp(-kappa^2/2) (about 0.78 at k=31, 0.76 at k=33).

## 3. Tail results and comparison with A56 / A57

`tail60.py` (primary: convex endpoints on adaptive-argmin pieces of width 0.0005; all pieces tile [0.005, alpha_1] and [alpha_2, 1] exactly, `verify_cover60.py`), constants per k:

| k | alpha* | u* | F* | S_lo..S_hi (n>=n0c) | n0c | kappa(D0) | C_o(D0) | gamma | y0*gamma | tiny F bound | T dH=0 | T dH=0.15 | T dH=0.5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 17 | 0.365073 | 0.852539 | 0.2747357 | 0.63680..0.63714 | 2235 | 0.426 | 13.179 | -0.012060 | -74.41 | 0.1012 | -39.56 | -39.38 | -38.77 |
| 19 | 0.356159 | 0.885669 | 0.2617603 | 0.58662..0.58693 | 2266 | 0.464 | 13.169 | -0.011823 | -75.86 | 0.0920 | -40.99 | -40.80 | -40.17 |
| 21 | 0.348201 | 0.915979 | 0.2505339 | 0.54544..0.54573 | 2261 | 0.506 | 13.147 | -0.010900 | -71.47 | 0.0844 | -36.60 | -36.41 | -35.76 |
| 23 | 0.341023 | 0.943930 | 0.2406901 | 0.51096..0.51123 | 2282 | 0.544 | 13.145 | -0.010603 | -71.68 | 0.0782 | -36.78 | -36.59 | -35.92 |
| 25 | 0.334495 | 0.969877 | 0.2319624 | 0.48161..0.48186 | 2298 | 0.583 | 13.147 | -0.010284 | -71.44 | 0.0730 | -36.52 | -36.33 | -35.62 |
| 27 | 0.328513 | 0.994098 | 0.2241519 | 0.45628..0.45653 | 2283 | 0.625 | 13.137 | -0.009453 | -66.49 | 0.0686 | -31.58 | -31.37 | -30.64 |
| 29 | 0.323000 | 1.016816 | 0.2171060 | 0.43417..0.43440 | 2294 | 0.664 | 13.145 | -0.009145 | -65.78 | 0.0647 | -30.83 | -30.63 | -29.86 |
| 31 | 0.317891 | 1.038213 | 0.2107061 | 0.41467..0.41490 | 2302 | 0.703 | 13.157 | -0.008836 | -64.85 | 0.0614 | -29.88 | -29.67 | -28.86 |
| 33 | 0.313134 | 1.058440 | 0.2048578 | 0.39734..0.39756 | 2307 | 0.742 | 13.171 | -0.008529 | -63.76 | 0.0585 | -28.77 | -28.55 | -27.70 |

(y0 = sqrt(D0); T columns use the same gamma; delta_H dependence is mild.)

Comparison table (`out/compare_tables.md`):

| k | UA | UB | alpha_1 | alpha_2 | D0 (A60) | D0 (A56) | ratio | gamma (A60, convex) | T(D0) A60 convex w0.0005 | T A56 TIGHT | T A56 SHARP | T A60 - T A56 TIGHT | D_cert |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 17 | 0.43 | 2.22 | 0.2431203 | 0.6504527 | 38,066,234 | 37,947,145 | 1.00314 | -0.012060 | -39.380 | -35.34 | -35.41 | -4.04 | 39,000,000 |
| 19 | 0.44 | 2.3 | 0.2337668 | 0.6419021 | 41,173,400 | 41,043,238 | 1.00317 | -0.011823 | -40.803 | -36.8 | -36.87 | -4.00 | 42,000,000 |
| 21 | 0.46 | 2.38 | 0.2287813 | 0.6350762 | 42,987,434 | 42,849,645 | 1.00322 | -0.010900 | -36.410 | -32.49 | -32.55 | -3.92 | 43,000,000 |
| 23 | 0.47 | 2.45 | 0.2218915 | 0.6281679 | 45,698,435 | 45,550,651 | 1.00324 | -0.010603 | -36.594 | -32.68 | -32.75 | -3.91 | 46,000,000 |
| 25 | 0.48 | 2.52 | 0.2159216 | 0.6224434 | 48,260,345 | 48,102,974 | 1.00327 | -0.010284 | -36.327 | -32.49 | -32.56 | -3.84 | 49,000,000 |
| 27 | 0.5 | 2.58 | 0.2132533 | 0.6162918 | 49,475,615 | 49,312,289 | 1.00331 | -0.009453 | -31.375 | -27.55 | -27.62 | -3.82 | 50,000,000 |
| 29 | 0.51 | 2.64 | 0.2085555 | 0.6110152 | 51,729,610 | 51,557,554 | 1.00334 | -0.009145 | -30.628 | -26.87 | -26.95 | -3.76 | 52,000,000 |
| 31 | 0.52 | 2.7 | 0.2043806 | 0.6064843 | 53,864,548 | 53,684,094 | 1.00336 | -0.008836 | -29.670 | -26.02 | -26.1 | -3.65 | 54,000,000 |
| 33 | 0.53 | 2.75 | 0.2006477 | 0.6012532 | 55,887,431 | 55,698,896 | 1.00338 | -0.008529 | -28.551 | -24.98 | -25.05 | -3.57 | 56,000,000 |

Mode comparison, T(D0) (all use the same D0, same pieces/u inside a row; widths W):

| k | convex W=0.0005 | convex W=0.0025 | convex W=0.0001 | ball(alpha) W=0.0025 | ball(alpha) W=0.0001 | ball(alpha,u) W=0.0025 | ball(alpha,u) W=0.0001 | y0*(gamma_ballcoarse - gamma_convex) | y0*(gamma_ballfine - gamma_convex) |
|---|---|---|---|---|---|---|---|---|---|
| 17 | -39.38 | -39.38 | -39.38 | -33.21 | -39.13 | 1378.21 | -36.09 | 6.17 | 0.25 |
| 19 | -40.80 | -40.80 | -40.80 | -35.40 | -40.61 | 44.20 | -37.50 | 5.39 | 0.19 |
| 21 | -36.41 | -36.40 | -36.41 | -30.92 | -36.18 | 1488.94 | -33.13 | 5.48 | 0.23 |
| 23 | -36.59 | -36.58 | -36.59 | -31.00 | -36.33 | 619.71 | -33.28 | 5.57 | 0.27 |
| 25 | -36.33 | -36.32 | -36.33 | -30.09 | -36.06 | 51.91 | -32.86 | 6.23 | 0.27 |
| 27 | -31.37 | -31.37 | -31.37 | -24.86 | -31.15 | 56.39 | -27.97 | 6.51 | 0.23 |
| 29 | -30.63 | -30.62 | -30.63 | -24.42 | -30.40 | 57.85 | -27.17 | 6.20 | 0.23 |
| 31 | -29.67 | -29.65 | -29.67 | -23.87 | -29.42 | 59.18 | -26.19 | 5.78 | 0.25 |
| 33 | -28.55 | -28.55 | -28.55 | -21.61 | -28.31 | 63.24 | -26.30 | 6.94 | 0.25 |

Exact zero sets (D <= 300000) and modular certificate:

| k | #Z_k | max Z_k | neg a_n(m) | E-O identity mismatches (def vs rec / def vs product, d<=20000) | last allowed d<=3e5 with E>=O | D_cert | double zeros mod p1,p2 | double zeros = exact set | double zeros > 3e5 |
|---|---|---|---|---|---|---|---|---|---|
| 17 | 80 | 1137 | 0 | 0 / 0 | 22628 | 39,000,000 | 80 | True | 0 |
| 19 | 89 | 766 | 0 | 0 / 0 | 30344 | 42,000,000 | 89 | True | 0 |
| 21 | 88 | 2055 | 0 | 0 / 0 | 59661 | 43,000,000 | 88 | True | 0 |
| 23 | 105 | 837 | 0 | 0 / 0 | 78453 | 46,000,000 | 105 | True | 0 |
| 25 | 76 | 936 | 0 | 0 / 0 | 97904 | 49,000,000 | 76 | True | 0 |
| 27 | 68 | 1375 | 0 | 0 / 0 | 120613 | 50,000,000 | 68 | True | 0 |
| 29 | 121 | 1934 | 0 | 0 / 0 | 146421 | 52,000,000 | 121 | True | 0 |
| 31 | 127 | 1712 | 0 | 0 / 0 | 174344 | 54,000,000 | 127 | True | 0 |
| 33 | 88 | 1587 | 0 | 0 / 0 | 205161 | 56,000,000 | 88 | True | 0 |

Reading. (i) alpha_1, alpha_2: A56/A57 take M_lo(UA), M_hi(UB) as extrema over a u-cell of width 0.01 (their `consts56_*.json`, k=29: M_lo(UA) = 0.75567 vs my point value 0.75831), so their alpha_1 is larger (k=31: 0.2047239 vs my 0.2043806) and alpha_2 smaller (0.6050689 vs 0.6064843); any alpha_1' >= the true bound is valid for the interface, and D0 = (N1/alpha_1')^2 shrinks as alpha_1' grows, so their D0 is smaller (0.3 %) and my tail region is smaller. Both valid; the certificate range D_cert >= my D0 also covers their D0. (ii) My gap at A57's own alpha_1 for k=31 is -0.008773 (A57: -0.008696), at k=33 -0.008468 (-0.008394): A57's is slightly less negative, i.e. conservative by 7.5e-5 (about 0.55 in T). (iii) Reconstruction of A57's T from its printed ingredients with its formula (log sqrt(D) + log 2 + sqrt(D) gap + g(u_c) + C* - log eta_t) gives -26.098 (k=31, quoted -26.096) and -25.053 (k=33, -25.051), so I read their formula correctly; the 3.6-4.0 difference to mine is, for k=31: count log y vs log(y/2) 0.69, the extra log 2 0.69, g(u_c) at the worst piece about 0.90 (outside C* in A57's formula; mine has only (1/2) g(u*) inside C_o), C* 13.305 vs my C_o 13.157 (0.15), and the gap 1.03 (my y0*gamma is 1.03 lower than A57's printed gap times its y); sum about 3.5, rest ~0.1 from rounding of the printed gap. (iv) My saddle for k=29 (alpha* 0.3229999, u* 1.016816, F* 0.2171060) equals A56's.

Sensitivity to the one hypothesis: for k=31 T = -29.88 (delta_H=0), -29.67 (0.15), -28.86 (0.5); delta_H = 0.8 is outside the proof (exp(-kappa^2/2) = 0.78).

Numerical sanity (not part of the proof, `out/sanity60*.json`): at the exact worst odd n in [alpha* y0 - k, alpha* y0 + k] the actual |x|/sigma is <= my bound kappa(D0) for k = 17, 27, 29, 31, 33 (e.g. 0.616 vs 0.703 at k=31), with S_n and M_n inside the enclosures; at d ~ 1.5e6 (k=29) and 1.8e6 (k=31) every exact even term in the tail region lies below exp(y F(alpha,u_i)) for its piece (0 violations of 26 + 26 checked terms), and the tiny-alpha terms are below y B. Exact finite-n checks of Chernoff (29 274 pairs, 0 violations), of log A_n bounds (even upper, odd lower) and of the Riemann brackets at n = 1467, 1468, 2001, 3000 pass (`out/j2_selfchecks.json`).

## 4. Zero sets, E-O identity, certificate

Exact (`exact60.py`, Python integers, recursion a_n[m] = a_{n-1}[m] - (-1)^n a_n[m-n]), D = 300 000 (preregistered) and D = 2 000 000 (extra, k = 27, 29, 31, 33; identical sets):

| k | 27 | 29 | 31 | 33 |
|---|---|---|---|---|
| #Z_k, max Z_k | 68, 1375 | 121, 1934 | 127, 1712 | 88, 1587 |
| claimed | 68, 1375 | 121, 1934 | 127, 1712 | 88, 1587 |
| list equal to A57's printed list | n/a | n/a | yes | yes |
| last allowed d with E >= O (D=3e5) | 120 613 | 146 421 | 174 344 | 205 161 |

(`out/zero_compare.json`; the last-d values equal those quoted in A56/A57.) Other k: Z_17 = 80 (max 1137), Z_19 = 89 (766), Z_21 = 88 (2055), Z_23 = 105 (837), Z_25 = 76 (936). Use of the zero sets: for allowed d > max Z_k, either d < D_cert and the modular certificate gives a nonzero residue (so g_k(d) != 0), or d >= D0 and PD (block + tail) gives E_d < O_d.

The table above ('Exact zero sets ... modular certificate') lists, for every odd k = 17..33: zero count, maximum, negative-entry count, identity mismatches (0/0), D_cert and that the double zeros of the modular run equal the exact set (all True, none beyond 3e5). `modcert60.c` runs both primes in one pass (add/sub only), about 3 min per k.

## 5. Ball vs fine-box vs convex-endpoint modes

Same D0, same pieces and u (u = argmin at piece midpoint) inside a row; second table above. Convex endpoints: T = -29.65 for W = 0.0025 and -29.67 for W = 0.0005 or 0.0001 (no width dependence, as proved). Ball in alpha only (arb ball over the piece): loses y0 * W * Phi1(u), 5.4-6.9 for W = 0.0025 (T = -23.87 at k=31), 0.2-0.3 for W = 0.0001. My pre-freeze hypothesis, that a u-interval of fixed width inside the ball accounts for the rest, was wrong (diagnostic `modes_extra60.py`, `out/modes_extra_k27_29_31_33.json`: a u-ball of width 0.0025 gives T = -4.3, of width 0.01 gives T = +58; kept as a diagnostic, not a criterion).

After the freeze, A56's `tails56.py` shows the actual mechanism (code_post/post_diag60.py, `out/post_diag60.json`), using A57's own alpha_1, alpha_2, D0 and A57's formula with its C*:

| k | tail boxes | central lower bound PsiL | T (mine) | quoted A57 |
|---|---|---|---|---|
| 31 | convex | convex (tangent) | -26.100 | -26.096 |
| 31 | ball W=0.0025 | ball over window [A0, A0+2k/sqrt D] | +2.709 | +2.714 |
| 31 | convex | ball | -4.117 | (A57 fine-ball, W=0.0001 tail: -3.874) |
| 31 | ball | convex | -19.274 | |
| 33 | convex | convex | -25.052 | -25.051 |
| 33 | ball | ball | +4.373 | +4.385 |
| 33 | convex | ball | -2.093 | (A57 fine-ball: -1.832) |
| 33 | ball | convex | -18.585 | |

So the quoted failure of the ball mode is a genuine ball-arithmetic artefact (the convex/tangent evaluation is rigorous and exact for the same inequality), but ~22.5 (k=31) / 23.5 (k=33) of it is the ball-valued lower bound of the central odd term (alpha-window width 2k/sqrt(D) ~ 0.009, `PsiL`), and only ~6 to 7 is from the 0.0025-wide tail boxes. That is why A57's post-hoc fine boxes (0.0001) only recover ~6.6 and not all of it. A56's text (and the task note) attributes it to the alpha-box width; that attribution is incomplete, not wrong in kind.

## 6. After the freeze: A56 source read and diff

Read: `proof/tails56.py`, `params56.py`, `run_pd56.py`, `cert/modcert.c`, `exact/eo56.c`, `exact/gexact.c` (and the data `consts56_*.json`, `params56.json`). Every difference found:

1. Chernoff constant: A56 uses log e_n <= sqrt(d) F + log 2 + g(u_c); I prove the bound without the extra `log 2 + g(u)` for even n (valid, tighter). A56's form is also valid (A61: proved for even n). No error.
2. Number of terms: A56 uses log sqrt(D) (count <= y), I use log(y/2). Both valid.
3. Central term: A56 takes the exact saddle tilt u_n in the window [ULO, UHI] (x = 0, bracket check `ok_ustar`), lower-bounds F by PsiL over the alpha-window and u-window, C* = (1/2) log 2 + g(ULO) + (1/2) log(2 pi) + (3/2) log n*_hi + (1/2) log S_hi - log(1-delta) with delta = max cell delta (0.0336/0.0338 for k=31/33 per A57). I use a fixed u*, bound x/sigma (kappa <= 0.74) and one delta_H = 0.15, and F* with a tangent correction. Different routes to the same type of constant; C_o = 13.14-13.18 vs C* = 13.28-13.31 (+ their `log 2 + g`).
4. M_lo(UA), M_hi(UB): A56 uses cell-wise extrema (cells of width 0.01), mine point values with the midpoint lemma: alpha_1 0.17 % larger, alpha_2 0.23 % smaller in A56, D0 smaller by 0.33 %. Valid either way.
5. Tiny alpha: A56's `Ftiny` = (alpha_t/2)(2 - ln k - 2 ln alpha_t + (3/8) k alpha_t^2) is exactly my bound (3.4) evaluated at u = k alpha^2/2 (the ln 2 cancels), so I find no discrepancy (I first doubted the 3/8; it is correct for u_c = k alpha^2/2). Numerically it is >= min_u F at alpha = 0.005 for k = 17, 25, 33 (margin ~2e-7); its tiny gap (~-0.19) has huge room. My own tiny bound uses u = 1.5 alpha and gives 0.06-0.10.
6. Ball-mode attribution (section 5): documentation discrepancy only.
7. `assert (A0*sD).lower() >= N1`: A56 requires the central odd term n >= N1; mine needs only n >= n0c ~ 2300; irrelevant.
8. C code: `cert/modcert.c`, `eo56.c`, `gexact.c` implement the same recursions as mine (signed sum, add for odd n / subtract for even n, `(D-n*n)/k`, allowed-class test), one prime per run (A57 ran two); no difference in logic found. Their zero lists equal mine (section 4).
9. No bug found in A56's tail step, params, or certificate code. `run_pd56.py` FAITH/TIGHT/SHARP variants are as described in A56's report.

Category (d) is therefore not triggered. Category (b) is not triggered either: my constants are stronger than A56's, and D0 differs by +0.33 % (larger).

## 7. Context from A61 (read after the freeze, not used)

A61 states that the log A_n upper bound with `+ log 2 + g` is claimed for all n in the A56 docstring but proved only for even n, the only case used; this agrees with section 2 item 2 (my bound is derived for even n, and the check in `j2_selfchecks.py` tests it for even n only). A61's `tail61.py` also closes for all odd k = 17..33 (T from -22.78 to -35.07, with A56's D0). I did not examine A61's code or numbers beyond reading its report.

## 8. Remaining dependencies and caveats

* H_CLT (local CLT at the tilt u*, n >= ~2300, delta_H <= 0.15): not proved here; the A56/A59/A61 layer supplies it (A56's constants for the c15 layer are <= 0.127 in the relevant windows).
* The block step (R_k < 1 - eta_t) and the window interface (u_n in [UA, UB] for alpha in (alpha_1, alpha_2)) are used as stated; the interface lemma is re-derived in `DERIVATION.md` section 6 but the block ratio is not.
* The midpoint-rule lemma constants (sup |f''| by arb series on 64 boxes) are computer-assisted; enclosures validated against exact finite sums in `j2_selfchecks.py`.
* The modular certificate proves g_k(d) != 0 for d outside the exact zero set up to D_cert; above D_cert PD is used.
* Rigour boundary: arb balls (256 bit) and exact rationals/integers; floating point only in argmin searches of u (any positive u is valid, then fixed as an exact rational) and in sanity checks.
* All timestamps are filesystem mtimes on one machine, re-stamped by the 22:24:49 restore; the original ordering rests on the recorded `stat` text in `mtime_prereg.txt`, the terminal record, and the sha256 of the preregistration, not on any external time-stamp.
* Every `out/` file was regenerated after the restore from unchanged code (deterministic; spot numbers equal the pre-restore ones).

## 9. Files

`prereg.md`, `prereg.sha256`, `mtime_prereg.txt`, `DERIVATION.md`, `FREEZE.sha256`, `FREEZE_time.txt`, `FREEZE_note_before_reading_A56.txt`, `REPORT.md`, `REPORT.pdf`, `SHA256SUMS`; `code/` (frozen: `a60lib.py`, `j2_selfchecks.py`, `j3_window.py`, `tail60.py`, `exact60.py`, `modcert60.c`, `sanity60.py`, `modes_extra60.py`, `verify_cover60.py`, `zero_compare60.py`, `compare60.py`, `decomp60.py`, run scripts, `mk_pdf60.py`); `code_post/` (post-freeze: `post_diag60.py`, `mk_report_tables60.py`); `out/` (tail_k*.json, j3_window.json, exact_k*_D300000.json, exact2e6/, cert/, compare.json, compare_tables.md, constants_table.md, decomp.json, sanity60*.json, zero_compare.json, modes_extra_k27_29_31_33.json, post_diag60.json); `logs/`.
