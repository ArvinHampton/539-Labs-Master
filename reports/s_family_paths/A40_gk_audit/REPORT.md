# A40: Independent audit of A39 (g_k family, k = 2..15)

Date: 2026-10-22 (CDT). Folder: `reports/s_family_paths/A40_gk_audit/`. New files only; no existing file or certifier code was modified; nothing pushed.

Object: g_k(q) = Σ_{n≥0} q^{n²}/(−q^k;q^k)_n, g_k(d) = Σ_n φ_n((d−n²)/k), φ_n(m) = [x^m]∏_{j≤n}(1+x^j)^{−1}; a_n(m) = (−1)^m φ_n(m) ≥ 0. For odd k, (−1)^d g_k(d) = E_d − O_d (even / odd n).

## Verdicts

| k | claim in A39 | verdict | proved statement (Category A) |
|---|---|---|---|
| 3 | PD, E_d ≤ (1−η)O_d, d ≥ 5 988 500 | **VERIFIED** (η digit, see B1) | η = 0.39748 (A39 printed 0.39749); zeros: 9, last 43 |
| 5 | same, d ≥ 7 321 266 | **VERIFIED** | η = 0.32961; 17 zeros, last 176 |
| 7 | same, d ≥ 8 890 003 | **VERIFIED** | η = 0.27687; 24 zeros, last 247 |
| 9 | same, d ≥ 9 791 834 | **VERIFIED** | η = 0.22197; 20 zeros, last 118 |
| 11 | same, d ≥ 11 073 024 | **VERIFIED** | η = 0.18073; 43 zeros, last 273 |
| 13 | same, d ≥ 11 836 583 | **VERIFIED** | η = 0.14192; 54 zeros, last 545 |
| 15 | same, d ≥ 12 789 969 | **VERIFIED** (η digit, see B1) | η = 0.06396 (A39 printed 0.06397); 55 zeros, last 565 |
| 2, 6, 10, 14 | all classes ONE, elementary | **VERIFIED** | zero sets finite and exactly as listed |
| 4, 8, 12 (ONE classes) | elementary | **VERIFIED** | no zeros beyond the listed ones |
| 4 c=0; 8 c=1; 12 c=0,4 (MIX) | open | **OPEN** (correctly labelled) | only: no zero in (last listed, 2·10^7] |

For odd k the verdict means: E_d ≤ (1−η_k)O_d for every allowed d ≥ D_k, hence OccFilt_k(∞) = {squares mod k}, and the complete zero set of g_k on allowed classes is the listed finite set. No FAIL was found.

Scope of the verdict: the local-CLT layer R1 (`clt.py`, `sums.py`) is k-independent and byte-identical to the audited A38 copy (sha256 1f4fa761…, c23705a0…). It was **not** re-derived here; its outputs (S_lo, δ per u-cell, M_lo/M_hi, S_hi) are used as inputs. Everything k-dependent was re-derived and recomputed with new code.

## Audit of the A39 scripts

**`blocks_k.py` / `verify_blocks_k.py`** (diff against A38 checked line by line).
- Universal block e_n ≤ R·½(o_{n−k} + o_{n+k}), n even: for odd k, n±k are odd, in the same square class, and each odd n′ is charged by n′±k only, weight ½ each, so total weight ≤ 1. Correct.
- Step factors: A_{j}/A_{j−1} = 1/(1−x^j) for odd j, 1/(1+x^j) for even j (the a_n generating function in x). The code's ε = (−1)^m with m = n+t−1, j = n+t, base n even: matches.
- r^{(n_i²−n²)/k} = exp(−u(2·off + off²s)/k), X = x_i/n = −(2off+off²s)/k − Δμ/n: correct.
- Gaussian factor: x_i²/(2σ_i²) ≤ X²·s·(1+k s)³/(2S_i) with s ≤ 1/(N1−k), n_i ≥ n−k: correct. Lower bound e^{−y} ≥ 1−y; positivity of 1−gfac−δ and of the denominator asserted.
- Cell coverage for member tilts u(1±k s) is outward and asserted. All arithmetic is mpmath interval (prec 100); floats only for box edges (exact binary) and JSON records (outward rounded).
- No error found.

**`tails_k.py`**.
- F_k(α,u) = αΦ1(u) + (1−α²)u/(kα) and ρ = (1/α²−1)/k: correct substitutions.
- Central odd term: odd members of one chain n ≡ r (mod k) are 2k apart, so an odd n* with n*/√d ∈ [a0, a0+2k/√d] exists. Correct. n* ≥ a0√D_k ≥ 900 = N1 holds for every k (checked).
- Tiny α (re-derived here): with u = kα²/2 and 1−e^{−t} ≥ t e^{−t/2}, Φ1(u) ≤ ½(1 − log 2 − log u + 3u/4), giving F ≤ (α/2)(2 − log k − 2 log α + (3/8)kα²); A39 uses the weaker 0.75k. g(u) ≤ log(2d/k)+1. Correct.
- Monotonicity in d: T(d) has slope ≤ 2.5/√d (+2 for tiny α) in √d, matched by the gap thresholds −2.5/√D0, −4.5/√D0. Correct.
- Tail coverage: even n either has α < α1 (includes all n < N1 since D0 = ⌈(N1/α1)²⌉), α ∈ [α1, α2] (block region, u ∈ [UA,UB], n ≥ N1), α ≥ α2, or α ≤ 0.005. Covered for all d ≥ D0. Correct.
- Rerunning with larger η_t after a failure is valid (η = 1 − R − η_t).

**Finite range (`cert/gkmod.c`)**: ladder 1/(1−x^n) (n odd), 1/(1+x^n) (n even) gives a_n; sign (−1)^m applied; mod-p arithmetic overflow-safe (p < 2^62). Correct. Nonzero mod p ⇒ nonzero; zeros-mod-both-primes coincide with the exact zero set, which lies inside the exact range.

**Even k (§2 of A39)**: ONE/MIX classification, the Frobenius argument (parts 2L, 2L+2, odd part 1; a_n(m) > 0 for m ≥ 2L(L−1)+1) and B_c are correct.

### Bugs and defects found (none changes a verdict)
- **B1 (rounding, report table).** η_k is rounded *up* in the last printed digit for k = 3 (1 − 0.6025109317 − 10^−6 = 0.3974880… printed 0.39749) and k = 15 (1 − 0.8860340509 − 0.05 = 0.0639659… printed 0.06397). Correct truncated values: 0.39748, 0.06396. The 4-digit values used in the exact cross-check (0.3974, 0.0639) are safe.
- **B2 (cosmetic).** `tails_k.py` keeps the A38 constant 7 in `top = alpha1 + 7/sD`. It only enlarges the tail α-range (extra coverage), so it is harmless; should read k or be dropped.
- **B3 (unasserted hypothesis).** `tails_k.py` uses δ = 0.2 in C* without asserting δ ≤ 0.2 on [ULO,UHI]. It holds: the inherited cells give δ ≤ 0.125 there for every k (checked here).
- **B4 (documentation).** No raw `out_k7_N900.txt`; the table's T(D_7) = −6.80 is the A38 value, while A39's own `tails_k7…json` has T = −6.776. Stale docstring comment "n* ≤ 0.45√d".
- **B5 (rigour of a side check).** `exact/eta_exact.py` compares 9-digit rounded ratios. Re-done here with exact integer comparisons on d ≤ 3·10^5: same last-violation values. Not needed for the main theorem.

## Independent verification (new code)

All runs: nice, OMP_NUM_THREADS=1, ulimit −v 3 GB.

1. **Exact E/O** (`exact/eo_indep.py`, pure Python integers, ladder for ∏1/(1+x^j) with sign checked rather than assumed; signbad = 0 for all k). Odd k to d ≤ 3·10^5, even k to d ≤ 10^5. Zero sets, last d with E_d ≥ O_d, and last violation of E_d ≤ (1−η)O_d with η = 0.3974, 0.3296, 0.2768, 0.2219, 0.1807, 0.1419, 0.0639 equal A39 exactly: 159, 580, 1372, 4573, 7800, 11948, 15879.
2. **Certificate** (`cert/gcert.c`, different recurrence: φ_n directly, no sign substitution; primes 2^61−1 and 10^18+3). For all k = 2..15 and d ≤ 2·10^7, the allowed d with g_k(d) ≡ 0 mod both primes are exactly the exact zero sets (`cert/compare.json`). 2·10^7 > max D_k = 12 789 969.
3. **Blocks** (`proof/blocks_indep.py`, python-flint arb balls, re-derived formulas, inherited R1 cells). Upper bounds for R_k:

   | k | 3 | 5 | 7 | 9 | 11 | 13 | 15 |
   |---|---|---|---|---|---|---|---|
   | A39 R_k (H=0.0025) | 0.6025109 | 0.6703845 | 0.7231290 | 0.7680282 | 0.8092646 | 0.8480780 | 0.8860341 |
   | A40, H = 0.0025 | 0.6025294 | 0.6704353 | 0.7232370 | 0.7682228 | 0.8095884 | 0.8486974 | 0.8870357 |
   | A40, H = 0.0005 | 0.5995894 | 0.6663262 | 0.7180124 | 0.7621931 | 0.8024774 | 0.8404471 | 0.8777221 |

   At equal box width, the ball arithmetic is slightly looser (as expected); on finer boxes it gives a smaller certified bound, ≤ A39's R_k for every k. So A39's R_k is a valid bound.
4. **Tails** (`proof/tails_indep.py`, arb; Φ1 by the closed form Φ1(u) = [Li2(−e^{−u}) + π²/12 + Li2(e^{−u}) − Li2(e^{−2u})]/(2u), derived here, instead of A39's Riemann enclosure). Same D_k as A39 for every k; u* bracket, monotonicity and T ≤ 0 all pass:

   | k | 3 | 5 | 7 | 9 | 11 | 13 | 15 |
   |---|---|---|---|---|---|---|---|
   | η_t | 10^−6 | 10^−6 | 10^−6 | 10^−2 | 10^−2 | 10^−2 | 5·10^−2 |
   | T(D_k), A40 | −19.08 | −8.31 | −10.27 | −10.13 | −9.81 | −4.77 | −3.74 |
   | T(D_k), A39 | −15.4 | −4.64 | −6.78 | −6.72 | −5.97 | −1.03 | −0.011 |

   The thin k = 15 margin in A39 comes from the looser Φ1 enclosure. With the closed form it passes even with η_t = 10^−2 (T = −2.14).
5. **Even k** (`exact/even_check.py`): ONE/MIX types recomputed and identical to A39; positivity lemma checked exactly for 3 ≤ n ≤ 60, m ≤ 3000; a_n = (−1)^m φ_n checked for n ≤ 30. Every zero of a ONE class is < B_c (max B_c = 1778, k = 14, c = 0), and the exact run to 10^5 decides below B_c.

## Proved statements (Category A)

- For odd k ∈ {3,…,15} and every allowed d ≥ D_k (table): E_d ≤ (1−η_k)O_d with η_k as in the verdict table. Computer-assisted, using the inherited R1 layer. Hence g_k(d) ≠ 0 for every allowed d > (last listed zero), and OccFilt_k(∞) = {squares mod k}.
- For k ∈ {2,6,10,14} and the ONE classes of k ∈ {4,8,12}: the zero set is finite and equals the listed set (elementary bound plus exact computation below B_c).
- For the MIX classes: g_k(d) ≠ 0 for listed-zero < d ≤ 2·10^7 only. Nonvanishing for all large d remains **open**.

## Files
`exact/` (eo_indep.py, even_check.py, eo_k*_D*.json, even_check.json, exact.log) · `cert/` (gcert.c, run.sh, z_k*_p*.txt, compare.py, compare.json, cert.log) · `proof/` (blocks_indep.py, tails_indep.py, r1_oracle.py, r1_constants.json, blocks_indep_k*.json, fine/blocks_fine.log, tails_indep_k*.json).
