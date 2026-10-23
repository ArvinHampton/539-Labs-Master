# A59 preregistration: independent re-derivation and re-implementation of the local-CLT layer (g_k, odd k <= 33)

Written 2026-10-22 (America/Chicago) BEFORE any A59 computation or code. Directory: `reports/s_family_paths/A59_clt_rederivation/`.
Everything A59 creates is a NEW file in this directory. Category A only (computer-assisted mathematics); no claim beyond the stated layer and block inequality.

## 0. What the layer must deliver (taken from the mathematical statements in A56/A57 `REPORT.md`; nothing else was read)

Object: for n >= 1 and tilt r = e^{-u/n} (u > 0), S = S_n(u) = sum_{j odd <= n} j B_j + sum_{n/2 < l <= n} 2 l N_l, with B_j ~ Bernoulli(1/(1+e^{ju/n})) and N_l geometric (P(N_l = t) = (1-w_l) w_l^t, w_l = e^{-2lu/n}), all independent.
(This is the probabilistic model of a_n(m) r^m / A_n(r) = P(S = m), A_n(x) = prod_{j<=n} 1/(1+(-x)^j); I re-derive it in DERIVATION.md.)
mu = E S, sigma^2 = Var S.

Layer statement L(n0, cells): for every u-cell [ua,ub] of a finite list covering the window, every integer n >= n0 and every u in the cell, with delta = delta_cell:
 (L1) sup over integers m of | sqrt(2 pi) sigma P(S = m) - exp(-(m-mu)^2/(2 sigma^2)) | <= delta;
 (L2) sigma^2/n^3 lies in [S_lo, S_hi] (enclosure), and mu/n^2 lies in [M_lo, M_hi].
Block inequality (A56/A57 form, re-derived by me): for even n >= N1 with odd partners n_pm = n +- k at the same tilt r (so u_pm = u n_pm/n),
 e_n / ( (o_{n-k} + o_{n+k})/2 ) <= R := (1 + delta_n) / ( (1/2) sum_{pm} rho_pm (1 - x_pm^2/(2 sigma_pm^2) - delta_pm) ),
 rho_pm = (A_{n_pm}(r)/A_n(r)) r^{(n_pm^2 - n^2)/k} sigma_n/sigma_pm,  x_pm = m_pm - mu_pm(r),  m_pm = m_n -+ 2n - k, mu_n(r) = m_n,
enclosed over u-boxes inside the window [UA, UB] and over s = 1/n in (0, 1/N1]. PD at k requires R_k + 1e-6 < 1 (eta_t = 1e-6); eta_k = 1 - R_k - 1e-6.
Window rule (A39/A41 as quoted in A56): y^k + y^2 = 1, u0 = -(k/2) ln y, UA = round(0.5 u0, 2), UB = round(2.6 u0, 2). N1 = 1500.
Tail lemmas (Chernoff, log A_n bounds) and the E-O identity are NOT re-derived by me except where the CLT layer enters (see 6).

## 1. Plan (jobs run one at a time; `nice -n 10`, `OMP_NUM_THREADS=1`, `ulimit -v 3000000` KB)

 J0  DERIVATION.md written first (math only), then code.
 J1  `code/` NEW implementation (python-flint arb balls, 128-bit+; plus a C program for an exact float64 DP of the pmf used only as a sanity check):
     - Fourier-inversion local CLT: main arc via Taylor with explicit third cumulant and a fourth-derivative bound; Gaussian tail via erfc; minor arcs via explicit lower bounds of sum_j v_j(1-cos j theta), v = p(1-p).
     - uniform in all n >= n0 = 1467 (= N1 - 33) via Riemann-sum enclosures with explicit midpoint-rule error terms (cells of the form x = j/n, s = 1/n in (0, 1/n0]).
     - cells: u in [0.40, 2.90], width 0.005 (500 cells) (superset of what k = 17..33 windows need after the factor 1 +- k/N1 for partner tilts); per cell I may choose any tau0 from a fixed list {0.3, 0.4, ..., 1.5} (choice does not affect rigour; the minimal certified delta is reported).
 J2  Own block code (`code/block59.py`), written from the formula of section 0 (NOT copied), u-boxes of width 0.0025/10 inside the A56-style 0.0025 grid, s in [0, 1/N1], endpoint balls in u; run for odd k = 17..33.
 J3  Numerical sanity (NOT part of the proof): exact float64 DP/convolution of the pmf (C program) and an independent frequency-sum check, at the fixed points (n,u) listed in section 3; report max_m error / certified delta.
 J4  ONLY AFTER J1-J3 are complete and their outputs frozen: read A56 data (cells json, pd56_results.json) and source (clt56.py, blocks56.py), compute the comparison table, diff and list every discrepancy.
 J5  Step 4: rerun my block code with (i) my delta, (ii) A56's published cell delta data (validation of my block code against A56's R), and (iii) as a cross-check, a byte-identical copy of A56's `blocks56.py` (+ its imports) driven with my delta file only if that needs a format conversion only (disclosed).

Independence protocol. Read so far: `A56_A49_audit/REPORT.md`, `A57_gk_31_33/REPORT.md`, `A57_gk_31_33/prereg.md` (statements only), and top-level file NAMES (`ls`) of the A56/A57 directories. No A41/A44/A49/A56/A57 source or data file is read before J4. No code is imported or copied before J5.

## 2. Pre-declared outcome rule (k = 27, 29, 31, 33; k = 17..25 reported as extra)

Let delta_blk(k) = max delta used by my block run, R_k(mine) the max block ratio with my delta (A56 form, same boxes). A56 comparators: R_27 = 0.83798, R_29 = 0.85970, R_31 = 0.8819648, R_33 = 0.9052174; max block delta 0.0576 (k=31), 0.0590 (k=33).
 (a) layer verified, equal or tighter: every certified cell of mine satisfies L1 (rigorous), the sanity check never exceeds my delta, R_k(mine) + 1e-6 < 1 for k = 27..33, and for each of these k my max block delta is <= A56's (0.0576 / 0.0590 for k = 31/33; A56 values for 27/29 taken at J4) and R_k(mine) <= A56's R_k + 1e-4.
 (b) my delta larger somewhere (or R_k(mine) > A56's + 1e-4) but R_k(mine) + 1e-6 < 1 for all k = 27..33: verified with weaker constants; margins reported.
 (c) some k in 27..33 has R_k(mine) + 1e-6 >= 1: reported with the box, delta and amount.
 (d) flagged in addition (not exclusive of a/b/c) if J4 finds a discrepancy in clt56.py that matters: a certified A56 delta below the true error in the sanity check, a violated hypothesis, or an arithmetic error. Discrepancies that are only convention differences are listed but not (d).
If the sanity check exceeds my certified delta anywhere, my derivation is wrong: that is reported as a failure, the bug fixed, and the fix logged; the first-run output is kept.

## 3. Fixed sanity points (chosen now)
Exact DP: (n,u) = (1467, 0.45), (1467, 1.04), (1468, 1.04), (1500, 0.70), (1500, 1.50), (1501, 2.00), (1600, 2.60), (1467, 2.90), (2000, 1.00), (3001, 0.60), (3000, 2.60), (1467, 0.40). Extra large-n check by truncated frequency sum: n = 8000, 20000 at u = 0.6, 1.04, 2.6 (certified delta evaluated at the same cell, valid for all n >= n0).

## 4. Disclosures
Allowed floating point: only in the sanity programs and in figure/PDF generation. All delta, S, M, block quantities use python-flint arb balls (>= 128 bits) or exact integers. Limits: memory <= 3 GB. Timestamps are filesystem mtimes (self-attested); the hash is stored beside the file.

## 5. Scope
Category A only. No TPC/RH statement. Only the local-CLT layer and the block inequality that consumes it, at N1 = 1500.

## 6. Tail step
I do not re-derive the tail step. I will only report the sensitivity of the A57 tail quantity C* to the CLT constant (it enters as -log(1 - delta_C)-type terms), using A57's published numbers (T(D0) ~ -25 to -26), as a remark, not a verdict.
