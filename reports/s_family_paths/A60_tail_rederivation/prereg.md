# A60 preregistration: independent re-derivation and re-implementation of the TAIL step (g_k, odd k = 17..33)

Written 2026-10-22 (America/Chicago) BEFORE any A60 computation or code. Directory: `reports/s_family_paths/A60_tail_rederivation/`.
Everything A60 creates is a NEW file in this directory. Category A only (computer-assisted mathematics); no claim beyond the tail inequality and the finite-certificate bridge stated below.

## 0. What the tail step must deliver (taken ONLY from the mathematical statements in A56/A57 `REPORT.md` / `prereg.md`; no A56/A57 source code was read, and none will be read before the freeze in section 6)

Object: g_k(q) = sum_n q^{n^2}/(-q^k;q^k)_n, odd k, g_k(d) = [q^d] g_k, d allowed iff d mod k is a square mod k.
 (S1) E-O identity: (-1)^d g_k(d) = E_d - O_d with E_d, O_d the sums over even / odd n of a_n(m_n), m_n = (d-n^2)/k, a_n(m) >= 0 the coefficients of A_n(x) = prod_{j<=n} 1/(1+(-x)^j).
 (S2) Window rule (A39/A41 as quoted in A56): y^k + y^2 = 1, u0 = -(k/2) ln y, UA = round(0.5 u0, 2), UB = round(2.6 u0, 2); N1 = 1500, n0 = N1 - k, eta_t = 1e-6.
      alpha_1 = 1/sqrt(1 + k M_lo(UA)), alpha_2 = 1/sqrt(1 + k M_hi(UB)), M_lo/M_hi enclosures of mu_n(e^{-u/n})/n^2 for all n >= n0; D0 = ceil((N1/alpha_1)^2).
 (S3) Tail inequality: for all d >= D0, the contribution to E_d of even n with alpha = n/sqrt(d) <= alpha_1 or >= alpha_2 is <= eta_t * O_d. Reported as T(D0) < 0 where T = log(bound on tail sum / (eta_t * lower bound on one odd term)).
      Reference values to compare with (not used): T = -26.096 (k = 31), -25.051 (k = 33), D0 = 53 684 094 / 55 698 896 (k = 31 / 33); A56 table of D0 for k = 17..33; alpha_1 = 0.2089032 (k = 29, A56).
 (S4) Finite certificate: for allowed d < D0 (and > max Z_k), g_k(d) != 0 by exact / modular computation; zero sets Z_k with counts 68, 121, 127, 88 and maxima 1375, 1934, 1712, 1587 for k = 27, 29, 31, 33.
 (S5) Local CLT enters only through ONE hypothesis (H_CLT): for the odd term used as reference, |sqrt(2 pi) sigma P(S=m) - exp(-(m-mu)^2/(2 sigma^2))| <= delta_H at the tilt u* for all n >= n0. I take delta_H = 0.15 (covers every constant quoted in A56/A57 for the non-sharp layer, 0.127; sharp layer 0.087). I do NOT prove H_CLT (that is the A59 layer); I report T for delta_H in {0, 0.15, 0.5} to show sensitivity.

## 1. Plan (jobs one at a time; `nice -n 10`, `OMP_NUM_THREADS=1`, memory <= 3 GB; A48 jobs may use up to 6 GB of the box)

 J0  DERIVATION.md (math only) written before code. Parameters below are fixed here.
 J1  `code/` NEW code, python-flint 0.9 arb at 256 bits (Li2 via arb polylog), exact rationals/integers for the exact parts, C (add/sub mod 2^61-1 and a second prime) for the modular certificate. No code is copied from any earlier directory.
 J2  Closed forms and self-checks: Phi1, M(u) = -Phi1'(u), S(u) = -M'(u); check against direct finite sums for n in {50, 200, 1467, 3000}; check Chernoff bound a_n(m) <= exp(n Phi1(u) + u m/n) (even n) and the odd lower bound on log A_n against exact a_n(m) (exact integer recursion) on a grid.
 J3  Window constants per odd k = 17..33: u0, UA, UB, M_lo(UA), M_hi(UB) via Riemann-sum midpoint-rule enclosures valid for all n >= n0; alpha_1, alpha_2, D0.
 J4  Saddle (alpha*, u*) of F(alpha,u) = alpha Phi1(u) + (1-alpha^2) u/(k alpha) (stationary in both variables), F*, S_lo/S_hi and M-error at u* (all n >= n0), x/sigma bound.
 J5  Tail pieces: alpha in [0.005, alpha_1] and [alpha_2, 1]. Fixed-width alpha pieces of width W = 0.0025 are used for the MODE comparison (u per piece = argmin_u F at piece midpoint, float search; the u used is then a fixed dyadic number); the primary mode uses the adaptive pieces described in DERIVATION.md. Tiny-alpha region alpha <= 0.005 by the analytic bound with u = c*alpha, c = 1.5.
     Modes (same pieces, same u): CONVEX (max of F at the two endpoints, justified by convexity in alpha), BALL_COARSE (arb ball over the whole piece, W = 0.0025), BALL_FINE (arb ball, W = 0.0001 sub-pieces, same u per sub-piece = argmin at its midpoint). T(D0) for each, for k = 17..33.
 J6  Exact zero sets: exact integer recursion (Python ints) for d <= 300 000 for all odd k = 17..33 (zero set of allowed d, count, max, a_n(m) >= 0 check); independent direct computation of g_k(d) from the q-series definition (sum_n q^{n^2}/(-q^k;q^k)_n, coefficientwise 1/(1+x^i) recursion) for d <= 20 000 and comparison with (-1)^d (E_d - O_d) computed from the product formula A_n = prod_{j odd}(1+x^j) prod_{n/2<l<=n} (1-x^{2l})^{-1} (E-O identity check).
 J7  Modular certificate: G[d] = (-1)^d g_k(d) mod p1 = 2^61 - 1 and p2 = 4611686018427387847 for all d <= D_cert(k) = 1e6 * ceil(D0/1e6) (>= D0), k = 17..33 odd; nonzero residue in either prime proves g_k(d) != 0; double zeros must equal the exact zero set on [0, 300 000] and none beyond (any beyond is evaluated exactly).
 J8  Compare with A56/A57 values; table.
 J9  FREEZE: sha256 of code/ and out/ recorded in `FREEZE_time.txt` / `FREEZE.sha256` BEFORE any A56/A57 source file is opened. Only then read A56 source (`proof/tails56.py`, `proof/params56.py`, `proof/run_pd56.py`, `cert/modcert.c`, `exact/*.c`, and A57 copies) and diff: list every discrepancy.
 J10 REPORT.md, REPORT.pdf, SHA256SUMS.

## 2. Success criteria and outcome categories (fixed in advance)

 (a) confirms: my T(D0) < 0 in CONVEX mode for every odd k = 17..33 with my own constants, my D0 within 0.5 % of A56's D0 for each k, zero sets for k = 27, 29, 31, 33 equal in count and max, E-O identity verified on d <= 20 000, certificate has no double zero beyond the exact zero set up to D_cert >= D0.
 (b) confirms with weaker constants: all of the above but T(D0) > A56's T by more than 2 for some k (still < 0), or D0 more than 0.5 % larger (still <= the A56/A57 certificate range 5.4e7 / 6e7 for k = 27, 29 / 31, 33).
 (c) fails: any of T(D0) >= 0 in CONVEX mode, a lemma that cannot be proved with explicit constants, a zero set mismatch, a double zero beyond the exact range. I will say where and by how much.
 (d) bug / discrepancy in A56: reported only after the freeze (J9), when a concrete difference in A56 source implies a different value or an invalid step.
Whatever happens, no claim beyond Category A, nothing about other statements; BALL modes are diagnostics, not criteria.

## 3. Disclosures
 - Read before this prereg: A56/A57 `REPORT.md`, A57 `prereg.md`; the directory listing and file names/mtimes of A59 (to match the preregistration/freeze format only).
 - No routine is copied from anywhere. Any later copy will be disclosed and byte-identical.
 - Timestamps are filesystem mtimes on one machine (self-attested).
