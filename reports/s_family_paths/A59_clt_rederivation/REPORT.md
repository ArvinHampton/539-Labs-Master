# A59 REPORT: independent re-derivation and re-implementation of the local-CLT layer (g_k, odd k <= 33, N1 = 1500)

Category A (computer-assisted mathematics). Scope: the local-CLT layer for S_n(u) and the block inequality that consumes it. No statement beyond that. Times are America/Chicago (CDT), filesystem mtimes (self-attested).

## 0. Outcome: category (a)

Preregistered rule (prereg.md section 2, option (a)): my certified layer is equal or tighter than A56's in every one of 500 cells, the sanity checks never exceed my delta, R_k(mine) + 1e-6 < 1 for k = 27..33, my max block delta is below A56's (0.0437 vs 0.0576 for k = 31, 0.0444 vs 0.0590 for k = 33), and R_k(mine) < R_k(A56). No (d)-grade discrepancy was found in `clt56.py` (see section 5). Limits: see section 8.

## 1. Timeline (independence protocol)

| step | time (CDT) |
|---|---|
| prereg.md written, sha256 ed3c1aa2...ea632 (prereg.sha256, mtime_prereg.txt) | 2026-10-22 20:29:11 |
| DERIVATION.md sections 0-7, code, cells, block runs, sanity runs (J1-J3) | before 20:43 |
| outputs/code frozen (FREEZE_J1_J3.sha256, FREEZE_time.txt) | 20:43:36 |
| A56 data and source first read (J4), A56 block code run with my delta (J5) | after 20:43 |
| random-DP and true-ratio sanity (extras), DERIVATION section 8, this report | ~20:50 to 21:10 |

Before 20:43 I read only the REPORT.md files of A56/A57 (and A57 prereg). After the freeze I read, read-only: A56 `clt56.py`, `blocks56.py`, `iv56.py`, `run_pd56.py`, `cells56_sharp.json`, `cells56_c15.json`, `pd56_results.json`, `params56.json`. A41/A44 source was not read.

## 2. What was built (all new code in `code/`)

- `DERIVATION.md`: model (E-O identity, product form, probabilistic representation), Fourier inversion with main arc (exact third cumulant, fourth-derivative bound), Gaussian tail (erfc), five minor-arc regimes (block bound for sum (1 - cos j theta)), uniform-in-n >= 1467 Riemann-sum enclosures, and the block inequality with finite exact sums for the partner ratios.
- `arbutil59.py`, `riem59.py`, `clt59.py`, `run_cells59.py`: python-flint arb balls; 500 cells.
- `block59.py`: independent block code (formula of DERIVATION section 6).
- Sanity (floating point, not part of the proof): `dp59.c` (exact float64 DP of the pmf), `freq59.py` (frequency sum at large n), `check_enclosures59.py`, `check_minor59.py`, `check_partner59.py`, `trueratio59.py`.

## 3. delta comparison (mine vs A56)

Cells: mine = 500 cells of width 0.005 on [0.40, 2.90], n >= n0 = 1467. A56 data = `cells56_sharp.json` ("sharp") and `cells56_c15.json` ("c15"), data only. A56 delta taken as the max over A56 cells intersecting my cell (`j4/compare_cells59.py`, `out/compare_cells59.json`).

Max delta over the block window (window widened by 1 +- 33/1500 for partner tilts), `out/window_delta_table.txt`:

| k | window (UA, UB) | mine | A56 sharp | A56 c15 |
|---|---|---|---|---|
| 17 | 0.43, 2.22 | 0.0376 | 0.0479 | 0.1255 |
| 19 | 0.44, 2.30 | 0.0385 | 0.0497 | 0.1255 |
| 21 | 0.46, 2.38 | 0.0395 | 0.0510 | 0.1255 |
| 23 | 0.47, 2.45 | 0.0404 | 0.0523 | 0.1255 |
| 25 | 0.48, 2.52 | 0.0413 | 0.0540 | 0.1255 |
| 27 | 0.50, 2.58 | 0.0423 | 0.0554 | 0.1255 |
| 29 | 0.51, 2.64 | 0.0430 | 0.0564 | 0.1255 |
| 31 | 0.52, 2.70 | 0.0437 | 0.0576 | 0.1255 |
| 33 | 0.53, 2.75 | 0.0444 | 0.0590 | 0.1255 |

The A56-sharp values for k = 31, 33 reproduce the quoted 0.058 / 0.059 (0.0576 / 0.0590). Mine/A56-sharp ratio over the 500 cells: min 0.697, max 0.828; mine <= A56 sharp in 500/500 cells; mine/c15 max 0.376. Samples:

| u-cell | mine | A56 sharp | A56 c15 |
|---|---|---|---|
| 0.400-0.405 | 0.0228 | 0.0327 | 0.0863 |
| 0.600-0.605 | 0.0233 | 0.0287 | 0.0870 |
| 1.000-1.005 | 0.0254 | 0.0307 | 0.0939 |
| 1.040-1.045 | 0.0257 | 0.0311 | 0.0949 |
| 1.500-1.505 | 0.0295 | 0.0368 | 0.1098 |
| 2.000-2.005 | 0.0347 | 0.0439 | 0.1218 |
| 2.600-2.605 | 0.0418 | 0.0550 | 0.1187 |
| 2.895-2.900 | 0.0455 | 0.0609 | 0.1208 |

The S = sigma^2/n^3 and M = mu/n^2 enclosures of mine and A56 intersect in all 500 cells (consistency check, `inter` field).

Why mine is tighter (not an error, see section 6 for how it was validated): I keep the exact third cumulant and a fourth-derivative bound in the Taylor remainder instead of a sup-bound on the third derivative, and use u-cells of width 0.005 with per-cell choice of the main-arc cut tau0.

## 4. Block inequality with my delta

R_k = max over u-boxes (width 0.0025/10) and s in (0, 1/1500], A56 form of the Gaussian factor, `out/block59_final.json`; eta = 1 - R_k (preregistered margin 1e-6 included in the checks):

| k | my R_k | eta | argmax u | A56 R_k (published) | A56 code + my delta (A56 boxes) | A56 code + A56 sharp delta |
|---|---|---|---|---|---|---|
| 15 | 0.6858 | 0.3142 | 0.830 | | 0.7008 | 0.7099 |
| 17 | 0.7051 | 0.2949 | 0.865 | | 0.7229 | 0.7316 |
| 19 | 0.7233 | 0.2767 | 0.900 | | 0.7443 | 0.7529 |
| 21 | 0.7407 | 0.2593 | 0.925 | | 0.7655 | 0.7741 |
| 23 | 0.7577 | 0.2423 | 0.955 | | 0.7863 | 0.7950 |
| 25 | 0.7743 | 0.2257 | 0.980 | | 0.8072 | 0.8161 |
| 27 | 0.7905 | 0.2095 | 1.000 | 0.83798 | 0.8285 | 0.8380 |
| 29 | 0.8068 | 0.1932 | 1.025 | 0.85970 | 0.8498 | 0.8597 |
| 31 | 0.8229 | 0.1771 | 1.045 | 0.88196 | 0.8718 | 0.8820 |
| 33 | 0.8391 | 0.1609 | 1.065 | 0.90522 | 0.8942 | 0.9052 |

Notes: all boxes passed (failed_boxes = 0) for all k. Column "A56 code + my delta" is the byte-identical copy of A56's block code (`j4/A56_copy/`, verified by cmp, hashes below) with only the delta input replaced (data conversion only): eta = 0.171 / 0.150 / 0.128 / 0.105 for k = 27 / 29 / 31 / 33. Other runs: exact-exp Gaussian factor (`block59_expmode.json`): 0.7902 / 0.8063 / 0.8224 / 0.8385; my block code with A56-sharp delta (`block59_with_A56sharp_delta.json`): 0.7994 / 0.8158 / 0.8323 / 0.8489; with A56 c15 delta: 0.9099 / 0.9294 / 0.9489 / 0.9685 (still < 1). Refined boxes (Hdiv 20, 8 s-pieces; extra, not preregistered): k = 31: 0.8171, k = 33: 0.8323.

My R is below the A56 code's R for two reasons: tighter delta (about 0.01 of R), and the plain-interval product for the 31-term rho in A56's coarse boxes overestimates by 4-5% (dependency effect). With matched granularity (Hdiv 1, s 1 pieces) and A56's delta, my block code reproduces A56's published R within +-0.0014 (`out/block59_A56sharp_H1s1.json`), which validates my block code independently.

## 5. Diff against clt56.py: every discrepancy

1. Docstring typo in `clt56.py` (descriptive text, not used in computation). Not a mathematical issue.
2. A56's REPORT does not prove the kappa shift bound |B'''(iy; q)| <= (v(1-2p) + t0 v p)/cos(t0/2)^3. I tested it numerically (`j4/check_A56_K3_claim.py`, `logs/J4_K3_claim.log`): max ratio actual/claimed = 0.99958 (<= 1) over t0 in {0.1,...,1.4} and q in a 500-point grid. Numerically valid and tight, not proven by me. A proof is missing in the A56 text; this is a documentation gap, not (d).
3. The cos-sum bound used in the minor arcs is stated without justification in A56's text; my derivation (Lemma 7) gives the same type of bound, 1/|sin theta|.
4. Looser constants: A56 uses a sup-bound for the third derivative and wider cells; its delta is 20-30% larger than mine (section 3).
5. One delta is used for both the center index n and the partners n +- k; I use the max of cells over u(1 +- k/N1) for the partners. Equivalent in effect, slightly more conservative in A56.
6. Coarse block boxes in A56 (width 0.0025 plain interval arithmetic) cost about 0.04-0.05 in R at k = 31; sound but conservative (section 4).
7. A56-form relaxation e^{-t} >= 1 - t costs about 5e-4 in R.

No violated hypothesis, no certified A56 delta below the true error in any sanity point, no arithmetic error found. So (d) is not triggered.

## 6. Independent numerical sanity (floating point; not part of the proof)

Ratio = true sup_m error / certified delta (must be < 1):

| check | points | max ratio | min ratio |
|---|---|---|---|
| exact float64 DP, 12 preregistered (n,u), n = 1467..3001 (`out/sanity59_dp.json`) | 12 | 0.791 | 0.519 |
| exact DP, 60 random (n in [1467,1700), u in [0.40,2.90], seed 59) (extra) | 60 | 0.789 | 0.692 |
| frequency sum, n = 8000, 20000 (`out/sanity59_freq.json`) | 7 | 0.335 | 0.198 |
| arb enclosure checks of S, M, k3, k4 vs direct sums (`check_enclosures59`) | 400 trials | 0 violations | |
| minor-arc bound |phi| <= exp(-B_tot) vs exact char. function (`check_minor59`) | 976 points | 0 violations | |
| partner finite sums vs direct sums and signed log A (`check_partner59`) | | rel. agreement 7e-16 | |

True error is about 0.8 of my certified delta at the worst points, so the certified delta is not very loose, and never below the truth.

True block ratio (extra; exact pmfs, n = 1500, e_n / ((o_{n-k} + o_{n+k})/2), `out/trueratio59.json`): max over u in {0.6, 0.9, 1.0, 1.04, 1.07, 1.5, 2.0}: k = 27: 0.739 (cert. 0.7905), k = 29: 0.749 (0.8068), k = 31: 0.765 (0.8229), k = 33: 0.779 (0.8391). All true ratios <= certified R (max true/R = 0.935 over all 28 points). The integer m_n = round(mu_n) is used instead of exactly mu_n = m_n, which differs by <= 0.5 out of sigma ~ 4e4 and is negligible against the 0.05 margin.

## 7. Tail step (sensitivity remark only)

I did not re-derive the tail step (Chernoff lemmas, log A_n bounds) nor A57's tail quantity C*. Remark only: the CLT constant enters A57's tail quantity through -log(1 - delta_C)-type terms; with A57's published T(D0) of about -25 to -26, a change of delta from 0.058 to 0.044 changes such a term by about 0.01-0.02, far below the margin. This is a remark and not a verdict.

## 8. Limits and disclosures

- Layer proof (L1, L2) is in DERIVATION.md sections 2-5 with the arb ball constants in the cells file; I did not formally verify it in a proof assistant. The sanity checks are not part of the proof. Interval/ball arithmetic is python-flint 0.9.0 (arb, >= 128 bits).
- The kappa shift bound of A56 was only checked numerically (section 5, item 2).
- The tail step, Chernoff lemmas and the finite certificate were not re-derived; only the sensitivity remark above.
- Preregistered cells and boxes were followed. Extras not preregistered: 60 random DP points, true-ratio check, refined boxes (Hdiv 20), exact-exp mode, A56-code and A56-delta cross-runs.
- A first block run `block59_test.json` (same code and parameters) preceded the final run; kept. A first version of `trueratio59.py` had wrong shift indices and a float overflow; replaced (corrected version in `code/`, faulty one in `scratch/`), the DERIVATION section 8 notes this. A heredoc leftover in `sanity59.py` was removed before the run.
- Byte-identical copies of A56 `blocks56.py`, `iv56.py`, `arb_compat.py` in `j4/A56_copy/` (sha256 b4331f5b..., 69c1a756..., 54960056...; verified with cmp), used only for the A56-code column of section 4; A56 `clt56.py` (sha256 58010703...) was read only.
- Floating point only in sanity programs and the PDF. Memory limit <= 3 GB (ulimit), nice, OMP_NUM_THREADS=1.
- Category A only; no claim beyond the local-CLT layer and block inequality at N1 = 1500.

## 9. Files

DERIVATION.md, REPORT.md, REPORT.pdf, SHA256SUMS, prereg.md, prereg.sha256, mtime_prereg.txt, FREEZE_J1_J3.sha256, FREEZE_time.txt, code/, out/, logs/, j4/, scratch/.
