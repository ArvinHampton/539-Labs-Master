# A57: finite certificate for Parity Dominance of g_k, k = 31 and k = 33 (N1 = 1500, A56's sharper local-CLT layer)

Date: 2026-10-22 (America/Chicago, CDT). Author: Grok Bot, for Arvin Hampton (539 Labs). Category A (computer-assisted, certified). All paths are under `reports/s_family_paths/A57_gk_31_33/`. Every file here is new; no existing file, certifier, or A41/A44/A49/A56 code was modified.

## 0. Verdicts

| k | verdict at N1 = 1500 | block ratio R_k | eta_k = 1 - R_k - 1e-6 | tail T(D0) (rigorous, endpoint/convex) | D0 | zero set Z_k (count, max) |
|---|---|---|---|---|---|---|
| 31 | **all preregistered criteria C1-C4 hold: PD(31) certified (computer-assisted, conditional on the local-CLT layer's derivation)** | 0.8819648 | **0.11803** | -26.096 | 53 684 094 | 127, max 1712 |
| 33 | **all preregistered criteria C1-C4 hold: PD(33) certified (computer-assisted, conditional on the local-CLT layer's derivation)** | 0.9052174 | **0.09478** | -25.051 | 55 698 896 | 88, max 1587 |

Statement certified, for k in {31, 33}: for every allowed d (d mod k a square mod k) with d > max Z_k one has g_k(d) != 0, where Z_k is the finite set of allowed d with g_k(d) = 0 listed in section 5. For d < D0 this is the finite certificate (section 4); for d >= D0 it is Parity Dominance, E_d <= (1 - eta_k) O_d, hence (-1)^d g_k(d) = E_d - O_d < 0.

Every inequality closes with rigorous arithmetic (128-bit arb balls, endpoint intervals); the one place where the plain-ball evaluation needs care is the tail (section 3.2): ball-in-alpha with 0.0025-wide alpha-boxes does NOT close (T = +2.714 for k = 31, +4.385 for k = 33), the endpoint evaluation (justified by convexity of F in alpha) closes by about 26, and a post-hoc re-run with plain balls on 0.0001-wide alpha-boxes (no convexity used) also closes (T = -3.874, -1.832). Nothing failed in the primary (preregistered) mode.

## 1. Setup (preregistered, `prereg.md`, sha256 in `prereg.sha256`)

g_k(q) = sum_n q^(n^2) / (-q^k; q^k)_n. For odd k and allowed d, (-1)^d g_k(d) = E_d - O_d (even/odd n, all terms a_n(m) >= 0). Pipeline = A56's: block step (R_k over 0.0025-wide u-boxes, UA..UB windows), tail step (Chernoff + local CLT at the saddle, eta_t = 1e-6), local-CLT layer (312 cells of width 0.01 on u in [0.19, 3.31], valid for all n >= 1467 = N1 - 33; "sharp" tau0-optimised cells, max delta 0.08727 over all cells; delta_max over the blocks actually used 0.0576 (k = 31), 0.0590 (k = 33)), then the finite certificate by two-prime modular recursion to D_cert = 6.0e7 >= D0, with exact GMP checks. Parameters (A57 re-computation, equal to A56's file): k = 31: u0 = u* = 1.038213, alpha* = 0.317891, windows UA = 0.52, UB = 2.70, ULO = 0.851, UHI = 1.277, A0 = 0.318; k = 33: u0 = 1.058440, alpha* = 0.313134, UA = 0.53, UB = 2.75, ULO = 0.868, UHI = 1.302, A0 = 0.313.

Code disclosure. Copies of A56 routines (byte-identical, verified with `cmp`): `proof/arb_compat.py, iv56.py, clt56.py, blocks56.py, tails56.py, sanity56_clt.py`; `cert/modcert57.c`, `exact/gexact57.c`, `exact/eo57.c` (copies of `modcert.c`, `gexact.c`, `eo56.c`, renamed). Modified copies (diffs in `proof/DIFF_params.txt`, `proof/DIFF_make_cells.txt`): `params57.py` (k restricted to 31, 33; output renamed), `make_cells57.py` (file names), `mk_pdf57.py`. New code: `run_pd57.py` (driver, adds the SHARP_BALL variant), `tails57fine.py` (post-hoc extra), `cert/compare57.py`, the three runner scripts. The numerical modules are therefore A56's code, re-run; **this is a re-run of the same code, not an independent re-implementation.** The sha256 of the A56 originals are in the prereg and the copies match them (SHA256SUMS lists the copies).

## 2. Local-CLT layer

312 cells recomputed (`proof/cells57_sharp.json`, 19 s) with `mono_ok` true in every cell; the cells, the window constants and `params57.json` are equal, as data, to A56's files (checked by JSON equality). The layer asserts: for every cell and every n >= 1467, |sqrt(2 pi) sigma P(S=m) - exp(-(m-mu)^2/(2 sigma^2))| <= delta for all integers m, plus enclosures of sigma^2/n^3 and mu/n^2.

Non-rigorous FFT spot check (exact distribution of S by FFT of the characteristic function, float64; `logs/J8_sanity_fft.out`), six fixed points chosen in advance:

| (n, u) | true max error | certified delta (sharp) | certified delta (c15, A41/A44 strength) |
|---|---|---|---|
| (1467, 0.55) | 0.01817 | 0.02923 | 0.08655 |
| (1467, 1.04) | 0.02029 | 0.03112 | 0.09491 |
| (1500, 1.065) | 0.02020 | 0.03091 | 0.09436 |
| (1500, 1.5) | 0.02289 | 0.03634 | 0.10853 |
| (1500, 2.6) | 0.03104 | 0.05408 | 0.11738 |
| (1501, 3.2) | 0.03535 | 0.07115 | 0.12667 |

In all six the true error is below the certified delta (ratio 0.50-0.65 for the sharp layer), and sigma^2/n^3 and mu/n^2 lie inside the enclosures. This is evidence, not proof.

## 3. Inequalities (N1 = 1500, eta_t = 1e-6; `proof/pd57_results.json`, `logs/J4_pd.log`)

### 3.1 Block step (C1)

| k | variant | R_k (max over boxes, at u) | eta_k | min odd-side factor | block delta_max |
|---|---|---|---|---|---|
| 31 | **SHARP (primary)** | **0.8819648** (u = 1.04, 872 boxes) | **0.11803** | 0.88257 | 0.0576 |
| 31 | c15 layer, s <= 1/N1 (comparison) | 1.0060660 | none (R > 1) | 0.82617 | 0.1255 |
| 31 | c15 layer, A41/A44 conventions (comparison) | 1.0096631 | none | 0.82427 | 0.1255 |
| 33 | **SHARP (primary)** | **0.9052174** (u = 1.065, 888 boxes) | **0.09478** | 0.87388 | 0.0590 |
| 33 | c15 layer, s <= 1/N1 (comparison) | 1.0333917 | none | 0.81724 | 0.1255 |
| 33 | c15 layer, A41/A44 conventions (comparison) | 1.0377167 | none | 0.81500 | 0.1255 |

The block inequality R_k + 1e-6 < 1 holds with the sharp layer (margin 0.118 and 0.095, against the largest block delta used, 0.058 and 0.059; positive "odd-side" factors 1 - x^2/(2 sigma^2) - delta > 0.87 in every box). With the A41/A44-strength layer R_k exceeds 1 by 0.0097 / 0.0377 (c15, conservative conventions): this is a limitation of those constants.

### 3.2 Tail step (C2)

| k | alpha1 | alpha2 | D0 | mode | T(D0) | max gap | u*-bracket | monotone | closes |
|---|---|---|---|---|---|---|---|---|---|
| 31 | 0.2047239 | 0.6050689 | 53 684 094 | endpoint/convex (primary) | **-26.096** | -0.008696 | yes | yes | **yes** |
| 31 | | | | ball in alpha, boxes 0.0025 | +2.714 | -0.004764 | yes | yes | **no, by +2.714** |
| 31 | | | | ball in alpha, boxes 0.0001 (post-hoc) | -3.874 | -0.005662 | yes | yes | yes |
| 33 | 0.200987 | 0.5998149 | 55 698 896 | endpoint/convex (primary) | **-25.051** | -0.008394 | yes | yes | **yes** |
| 33 | | | | ball in alpha, boxes 0.0025 | +4.385 | -0.004451 | yes | yes | **no, by +4.385** |
| 33 | | | | ball in alpha, boxes 0.0001 (post-hoc) | -1.832 | -0.005282 | yes | yes | yes |

T(D) = log sqrt(D) + log 2 + max(sqrt(D) gap + g) + C* - log eta_t must be <= 0 (C* = 13.305 for k = 31 and 13.278 for k = 33 with the tail delta 0.0336 / 0.0338, from the sharp cells over the central window). The coarse-ball failure is the evaluation artefact already known for this style (a ball in alpha of width 0.0025 loses about sqrt(D) * width * |dF/dalpha| ~ 27-29 in T); the true gap at alpha1, alpha2 is negative (about -0.0087), so the Chernoff tail is of size e^(-26) times eta_t. F is convex in alpha (d^2F/dalpha^2 = 2u/(k alpha^3) > 0), so the endpoint evaluation is exact in this respect; the fine-ball run is an independent confirmation of the same inequality that does not use convexity (boxes 0.0001 instead of 0.0025, same code with one constant changed, `proof/tails57fine.py`; it is a post-hoc extra, not a preregistered criterion). With the c15 layer the tail passes in endpoint mode (T = -26.02, -24.98) and fails in ball mode (+2.90, +4.57, A41/A44 conventions with delta_C = 0.2).

## 4. Finite certificate (C4)

For allowed d <= D_cert = 60 000 000 (>= D0 = 53 684 094 and 55 698 896), G[d] = (-1)^d g_k(d) was accumulated by the signed recursion a_n[m] = a_{n-1}[m] - (-1)^n a_n[m-n] modulo p1 = 2^61 - 1 and p2 = 4 611 686 018 427 387 847 (`cert/modcert57.c`, four sequential jobs of 74-80 s). A residue != 0 for either prime proves g_k(d) != 0; the "double zeros" (both residues 0) are the only remaining candidates.

| k | double zeros mod p1 | mod p2 | double zeros (both) | max | exact zero set d <= 2e6 (GMP, `gexact57`) | equal | double zeros > 2e6 |
|---|---|---|---|---|---|---|---|
| 31 | 127 | 127 | 127 | 1712 | 127, max 1712 | yes | 0 |
| 33 | 88 | 88 | 88 | 1587 | 88, max 1587 | yes | 0 |

Both primes gave identical lists (no prime-specific false zero). The exact E/O program (`eo57`, GMP, d <= 2e6) found no negative a_n(m) (counter 0), has the same zero list, and the last allowed d <= 2e6 with E_d >= O_d is 174 344 (k = 31) and 205 161 (k = 33), far below D0 (data only). Hence for allowed d > max Z_k: d < D0 by the certificate, d >= D0 by PD.

## 5. Zero sets Z_k (allowed d with g_k(d) = 0, exact)

k = 31: count 127, min 2, max **1712**: 2, 5, 7, 8, 10, 14, 18, 19, 20, 28, 31, 33, 38, 39, 41, 45, 50, 51, 59, 62, 66, 69, 70, 71, 72, 76, 78, 82, 87, 90, 93, 97, 98, 101, 103, 107, 111, 113, 124, 126, 132, 134, 138, 143, 155, 162, 163, 165, 171, 183, 186, 190, 194, 206, 217, 221, 231, 248, 253, 256, 258, 279, 289, 310, 314, 320, 324, 341, 345, 349, 355, 361, 372, 380, 382, 403, 411, 413, 434, 438, 441, 442, 465, 469, 496, 504, 527, 535, 537, 558, 562, 566, 589, 593, 620, 628, 651, 659, 661, 682, 686, 713, 717, 744, 752, 754, 775, 806, 810, 837, 868, 872, 899, 900, 907, 930, 931, 993, 996, 1023, 1027, 1086, 1101, 1163, 1312, 1400, 1712

k = 33: count 88, min 3, max **1587**: 3, 12, 15, 22, 27, 31, 33, 45, 48, 49, 55, 60, 66, 70, 75, 78, 88, 91, 93, 99, 100, 102, 103, 111, 126, 130, 132, 133, 147, 148, 159, 165, 169, 187, 192, 198, 199, 210, 214, 231, 232, 235, 247, 256, 264, 265, 267, 268, 280, 291, 297, 298, 301, 324, 330, 331, 357, 363, 396, 423, 429, 433, 456, 462, 463, 495, 528, 532, 561, 562, 588, 594, 627, 660, 693, 726, 759, 792, 825, 858, 891, 924, 957, 990, 1023, 1056, 1155, 1587

(`cert/cert57.json`, `exact/gexact57_k*_D2000000.json`.)

## 6. Caveats and residual dependencies (no overclaiming)

1. **The sharper local-CLT layer is only as strong as its own derivation.** The result depends on the claim that, for every n >= 1467 and every u in each cell, the local-CLT error is <= delta (A56's `clt56.py`: Taylor/major-arc term D1 with a third-derivative bound K3, Gaussian tail D2, minor arcs D3 by Abel summation and Riemann-sum lemmas with total-variation error terms). A57 re-ran this code and did not re-derive or re-prove the layer; the only extra check is the non-rigorous FFT spot check of section 2 (six points, true error 50-65 % of the certified delta). A flaw in that derivation, or a software bug in the shared code, would affect A56 and A57 alike; A57 does not provide an independent code base.
2. The block margin (eta = 0.118 / 0.095) is larger than the block delta (0.058 / 0.059), but it is the local-CLT layer that supplies the control of E/O for n >= N1; the tail step uses the CLT at the saddle only through C*.
3. The tail's primary mode uses the convexity of F in alpha (elementary, derived in A56); the post-hoc fine-ball run confirms the same inequality without it.
4. Tail lemmas (Chernoff bound, log A_n bounds with +-log 2 and g(u)), the block algebra and the E - O identity are those of A56; they are not re-derived here.
5. Floating-point edges of the cells pass through JSON as float64 (A56's outward one-ulp convention); everything else is arb at 128 bits. The modular and GMP computations are exact integer arithmetic.
6. Scope: only k = 31 and 33 at N1 = 1500; no claim for k > 33. This report states the nonvanishing/finite-certificate statement of section 0; the translation into OccFilt_k(infinity) = squares mod k is by the definitions already in the project and is not re-derived here.
7. Timestamps are filesystem mtimes on one machine (self-attested): prereg and its hash 19:33:05.114 CDT; code copies 19:33:15; `params57.json` (first output) 19:34:14; certificate outputs 19:37-19:41; sanity and post-hoc extra 19:41-20:05. A first launch of the runner (19:33-19:34) had a logging-path bug and was killed after its first two jobs (J1, J2); its outputs are in `logs/aborted_first_launch/` and were not used (the relaunch re-ran everything from J1; the re-generated params, cells and constants are byte-identical to the aborted ones).
8. Deviations from the prereg: none in the criteria or parameters. Additions beyond it: the SHARP_BALL variant (in the prereg), the post-hoc fine-ball run (labelled post-hoc), and the exact range 2e6 (as preregistered).

## 7. Resources and files

`nice -n 10`, `OMP_NUM_THREADS=1`, `ulimit -v 3 000 000` KB; one job at a time (job times in `logs/jobs.log`); the largest job (modular certificate) holds one 480 MB array. Files: `prereg.md`, `prereg.sha256`, `REPORT.md`, `REPORT.pdf`, `SHA256SUMS`, `mk_pdf57.py`; `proof/` (code, cells, params, constants, `pd57_results.json`, `tails57fine_results.json`); `cert/` (`modcert57`, residue lists, `cert57.json`); `exact/` (GMP programs and outputs); `logs/` (`jobs.log`, `mtimes.txt`, job logs, FFT output); runner scripts `run_all_prep.sh`, `run_exact_cert.sh`, `run_sanity_fine.sh`.
