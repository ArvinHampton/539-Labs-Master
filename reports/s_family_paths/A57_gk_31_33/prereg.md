# A57 preregistration: finite certificate for Parity Dominance, g_k with k = 31 and k = 33

Written 2026-10-22 (America/Chicago) BEFORE any A57 computation. Directory: `reports/s_family_paths/A57_gk_31_33/`.
Everything created by A57 is a NEW file in this directory. No existing file, certifier, or A41/A44/A49/A56 code is modified or imported.

## 0. Object

g_k(q) = sum_{n>=0} q^{n^2} / (-q^k; q^k)_n, odd k. Writing g_k(d) = [q^d] g_k, d allowed iff d mod k is a square mod k.
For odd k, (-1)^d g_k(d) = E_d - O_d (E: even n, O: odd n, every term a_n(m) >= 0).
Parity Dominance PD(k): there is D_k such that E_d <= (1 - eta_k) O_d for every allowed d >= D_k; then (-1)^d g_k(d) < 0, so g_k(d) != 0.
Claim to certify (Category A, computer-assisted): PD(31) and PD(33), hence g_k(d) != 0 for all allowed d > max Z_k, where Z_k is the (finite) set of allowed d with g_k(d) = 0.

## 1. Plan (pipeline = the A56 pipeline, including A56's sharper local-CLT layer; same method as k = 27, 29)

All parameters are fixed here: N1 = 1500, eta_t = 1e-6 (tail budget), u-box width H = 0.0025 for the block step, u-cells of width 0.01 on [0.19, 3.31]
with n0 = 1467 (= N1 - 33; covers n_i >= N1 - k for k <= 33), 128-bit arb balls, windows UA, UB, ULO, UHI, A0 from the A39/A41 window rule as in A56 (`params`).

Code policy. Some routines are COPIES of A56 routines (disclosed; sha256 of the A56 originals are listed in section 6; the copies are byte-identical to
those originals except for the file name and, where stated, an added driver). New A57 code: the driver `run_pd57.py` (adds a second tail mode and
logging), `params57.py` (A56's `params56.py` restricted to k = 31, 33; a copy with its output file renamed), the orchestration shell scripts, the comparison / report scripts.
The C programs are copies of A56's `modcert.c`, `gexact.c`, `eo56.c` (names changed to `*57`). Nothing is imported from outside the A57 directory.

Jobs (run ONE AT A TIME, sequentially; `nice -n 10`, `OMP_NUM_THREADS=1`, `ulimit -v 3000000` KB (< 3 GB)):

 J1  params57.py          -> params57.json (k = 31, 33). Cross-check against A56's params file (data read only).
 J2  make_cells57.py sharp -> cells57_sharp.json, consts57_sharp.json  (312 cells + window constants).
 J3  make_cells57.py c15   -> cells57_c15.json,   consts57_c15.json    (A41/A44-strength comparison layer).
 J4  run_pd57.py 31 33     -> pd57_results.json. Variants: SHARP_CONVEX (primary), SHARP_BALL, TIGHT, FAITH (the last two use the c15 layer and are comparison only).
 J5  exact GMP: gexact57 and eo57 for k = 31, 33 with D = 2,000,000 (exact zero set Z_k up to 2e6, a_n(m) >= 0 counter, last d with E_d >= O_d).
 J6  modcert57 for k = 31, 33 and the two primes p1 = 2^61 - 1 = 2305843009213693951, p2 = 4611686018427387847, D_cert = 60,000,000 (4 sequential jobs).
 J7  compare / merge script -> cert57.json (double zeros, comparison with exact zeros).
 J8  FFT sanity of the local-CLT layer (NOT part of the proof), 6 fixed points (n, u): (1467,0.55) (1467,1.04) (1500,1.065) (1500,1.5) (1500,2.6) (1501,3.2), sharp and c15 deltas, one job at a time.
 J9  REPORT.md, REPORT.pdf, SHA256SUMS; record mtimes (`stat`) of prereg, code copies, first outputs in `logs/mtimes.txt`.

Adaptation rule (declared in advance). If the primary pipeline does not close at N1 = 1500 for some k, I report which inequality fails and by how much, and I may
re-run J2/J4 for that k at a larger N1 (cells regenerated with n0 = N1 - 33, D_cert raised above the new D0). Such a run is labelled "adapted (N1 = ...)" and is
a separate, post-hoc entry; the N1 = 1500 result stays the preregistered result.

## 2. Success criteria (all must hold for a "closes" verdict for a given k)

 C1  Block step: R_k < 1 - eta_t with R_k the maximum over all 0.0025-wide u-boxes in [UA, UB] of the rigorous enclosure of the E/O block ratio (SHARP layer, s <= 1/N1, endpoint-interval arithmetic over arb).
     Then eta_k = 1 - R_k - 1e-6 > 0 is reported (truncated at 5 decimals). Forecast from A56 (not blind): R_31 = 0.882, R_33 = 0.905.
 C2  Tail step: with D_k = D0 = ceil((N1/alpha1)^2) from the A57 constants, (i) the u*-bracket check holds, (ii) the monotonicity criterion
     gap <= -2.5/sqrt(D) (tiny-alpha part: <= -4.5/sqrt(D)) holds, (iii) T(D0) <= 0 where T = log sqrt(D) + log 2 + max(sqrt(D) gap + g) + C* - log eta_t.
     Primary mode SHARP_CONVEX (F convex in alpha, endpoint evaluation, derivation in A56); SHARP_BALL (ball in alpha) is reported as well. A "closes with rigorous
     arithmetic" statement is made for the mode(s) in which all three hold; if only SHARP_CONVEX holds, the statement says so.
 C3  Local-CLT layer: all 312 cells computed with `mono_ok` true (every internal monotonicity / positivity check of the layer holds); max delta reported; delta < 0.1 everywhere in the windows used.
 C4  Finite certificate: D_cert = 6.0e7 >= D0(31), D0(33) (as computed in J4). For each k and each allowed d <= D_cert, a residue != 0 modulo p1 or p2 proves g_k(d) != 0;
     the double zeros (both residues 0) form the candidate set; every double zero is checked exactly (GMP). Required: the double zero set equals the exact zero set from J5
     on [0, 2e6] and there is no double zero in (2e6, D_cert] (if there is one it is evaluated exactly and, if it is a true zero, enters Z_k and max Z_k; if D0 > D_cert the range is extended before any verdict).
 C5  Verdict rule: "PD(k) certified at N1 = 1500 (computer-assisted, conditional on the local-CLT layer's derivation)" iff C1-C4 hold. Otherwise "does not close" with the failing inequality and its numerical gap.
     Data-only cross-checks (J5 counter neg = 0, J8) are reported but are not criteria.

## 3. What will be reported
eta_k margins, R_k and where attained, T values per variant, D0, alpha1, alpha2, delta_max, zero sets Z_k (count, max, full list), certificate range, residual dependencies.

## 4. Scope
Category A only. No claim about any other k, no claim beyond the stated finite-certificate + inequality statement. The sharper local-CLT layer is only as strong as its own derivation (A56 `clt56.py`); A57 re-runs it, does not re-prove it, and adds only a numerical FFT sanity check that is not a proof.

## 5. Timing record
The prereg is hashed (`prereg.sha256`) immediately after writing, before any code copy or run. mtimes recorded in `logs/mtimes.txt`.

## 6. sha256 of the A56 originals that will be copied (read-only reference)
```
54960056b8f0ec50c7552141c66879877913ab836e7d45347c671436590b3326  proof/arb_compat.py
69c1a7565b4f2d12c2f690fa4b45f94a5064bb6fd71e5fbc995957043c6291e9  proof/iv56.py
58010703009af404d185b2dc91b69e81ccc711486860d02a451f170ff64288ee  proof/clt56.py
b4331f5bb62147c00aa494cc5406ce3482fe5434fac840133796099798852417  proof/blocks56.py
34f5a34c0b325345a0b22151daa567c91abd0ba304472f980b49baada110249a  proof/tails56.py
73bdd47136e013103e95ed68778860dd85c5b9c3af9ae8995f9ef8f3ebbeab86  proof/params56.py
ba1b8bb011d25e420bd4cbaf63e400939e99a3aa4ba385fb285f64e03e81d430  proof/make_cells56.py
b26ef6cd65b0c02033117c0467d0d6a908aea5703a8711600554d7926293c8ea  proof/run_pd56.py
3ba3f1eb819a4a3525ed9f9a98b3a046a770d2932789683ecd517f714d8a1c03  proof/sanity56_clt.py
a228eaff1ac42094a28ec7b32ce495e233d3d78007d5ebd33dce4e35482caf08  cert/modcert.c
c8f5217910d230a585aff9fb1893614f19f5b83f443c98b8b8c98d9ad4e82f69  exact/gexact.c
ee02a79afc9e9f8a4f45abb59587f01ccf06eb8ddfa472ad9c2ba6f66dec015b  exact/eo56.c
8f9775a543b4fa257d0899f8ecf48d238ef02611fb7d412f7a8f7b411465231b  proof/params56.json (data, cross-check only)
```
