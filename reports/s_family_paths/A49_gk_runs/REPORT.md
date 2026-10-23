# A49: last-zero and sawtooth predictions for g_k, and Parity Dominance at N1 = 1500 (k = 3..15, 27..33)

**For:** Arvin Hampton · 2026-10-22 (CDT). All new files are in `A49_gk_runs/`. Jobs ran under `nice`, OMP_NUM_THREADS=1 and `ulimit -v` 3 GB; total disk use is about 2 MB. No TPC or RH claims. No Ramanujan Journal mention.

**Preregistration:** `prereg/prereg.md`, sha256 `c441f9b867882893eb79bf73a2e87bdbe0922e57825d5b01420138c64b764bf4` (`prereg/prereg.sha256`), written 18:00:41 CDT. The first A49 run finished at 18:00:50 CDT, so the file predates every run. The prereg labels its predictions P(a) and P(b); here they are called Prediction 1 (zeros beyond k(k+2)) and Prediction 2 (next jump of T(k)).

Notation as in ledger v6 entries 73–84: g_k(d) = Σ_n φ_n((d−n²)/k), allowed d means d mod k is a square, Z_k is the set of allowed zeros, E_d and O_d are the even-n and odd-n sums (odd k), and (−1)^d g_k(d) = E_d − O_d.

## 0. Summary

1. **Prediction 1 PASSES on every test set**, but my forecast for one test set was wrong. I forecast that the prime half would FAIL on the 166 primes 5 ≤ k ≤ 997. It passes: every prime has an unforced zero beyond k(k+2). The reason is a new proved family of zeros (Category A, §2.3): for every odd prime power k ≥ 9, g_k(k²+2k+4) = 0 if k ≡ 3 mod 4, and g_k(k²+3k+4) = 0 if k ≡ 1 mod 4. Both exceed k(k+2). Excluding these as well, 74 of the 164 primes k ≥ 11 (k ≤ 997) have no zero beyond k(k+2).
2. **Prediction 2 (jump at k = 63) FAILS as a point prediction.** The first jump at k ≥ 61 is at **k = 67**: ρ(65) = 23.848 → ρ(67) = 27.242 (T(67) = 3 331 509). The preregistered acceptance window {61, 63, 65, 67} contains 67, so the window version passes. The post-jump range [25, 28] holds at 67, 69, 71 and is exceeded at 73 (28.18) and 75 (28.43). k = 77 and 79 are censored at 5·10⁶.
3. **Parity Dominance (Category A, computer-assisted) is extended to odd k = 27 and 29, and rerun for k = 3..15 at N1 = 1500.** It fails at k = 31 and 33 (block ratio above 1 at N1 = 1500). **New proved range: every odd k ≤ 29** (k = 17..25 from A41/A44). Constants are in §3.
4. **k = 15 at N1 = 1500: η_15 = 0.19504**, not about 0.104. It rises from 0.06396 at N1 = 900 (that run used tail allowance 5·10⁻², and the new run uses 10⁻⁶, with the same box width 0.0025 and the closed-form tail).

## 1. Definitions fixed in the preregistration

- **Forced set.** k(k+2) is forced iff k is squarefree (entry 77). (k+2)²−3 is forced iff k is an odd prime power ≥ 5 (entry 78). Nothing else is removed; in particular the sporadic zero at (k+2)²−3 for k = 15 and 21 stays in the count. If a forced d is not itself a zero (it always is when it applies), it is not removed.
- **Last unforced zero.** L*(k; D) = max (Z_k ∩ [0, D] minus the forced set). "Zero beyond k(k+2)" means L*(k; D) > k(k+2).
- **Last dominance point.** T(k; D) = the largest allowed d ≤ D with E_d ≥ O_d (zeros count), odd k. ρ(k) = √T(k)/k. Censored if T > 0.95·D. A **jump** at k means ρ(k) − ρ(k−2) ≥ 1.5.
- Check of the definition on old data (k ≤ 59, A43/A41 exact runs): jumps at 7, 13, 21, 37, 47. This agrees with A45 and was known before the prereg.

## 2. Task 1

### 2.1 Runs
- Exact E/O (GMP integers, `exact/eo_gmp.c`, A43 code) to 5·10⁶ for odd k = 61..79: sign check `signbad = 0` for all ten.
- Two-prime modular scan (primes 2⁶¹−1 and 10¹⁸+3, `exact/gcert.c`) to 5·10⁶ for every k = 61..79. For odd k the double-zero set equals the exact zero set. For even k every double zero was re-evaluated exactly in Python integers (all are zeros).
- Tertiary set: two-prime scan of every even squarefree k ≤ 200 (41 values) to 2·10⁶, double zeros re-evaluated exactly.
- Secondary set: A43 exact zero lists (odd k ≤ 997, D = 2·10⁶), plus A41 data for k = 3 (Z_3 has max 43 > 15). Existing data, recomputed under L* (`analysis/lstar.py`, `analysis/lstar.json`).

### 2.2 Prediction 1: scores (every prime has L* > k(k+2); composite squarefree k with L* > k(k+2) are divisible by 3 or 5)

| test set | primes: L* > k(k+2) | composite squarefree with L* > k(k+2) | divisible by 3 or 5 | forecast | outcome |
|---|---|---|---|---|---|
| primary: k = 61..79, D = 5·10⁶ | 5 of 5 (61, 67, 71, 73, 79) | 65, 69 | both | PASS / PASS | PASS / PASS (the prime half was already known, so it is not a blind test) |
| secondary: odd k ≤ 999, D = 2·10⁶ | 167 of 167 (k = 3, 5 and 165 more) | 15, 33, 35, 39, 55, 65, 69, 111, 115, 123, 129, 201, 213, 291, 381, 519, 543, 717, 723, 993 (20 of 235) | all 20 | FAIL / PASS | **PASS / PASS** (prime half forecast wrong) |
| tertiary: even squarefree k ≤ 200, D = 2·10⁶ | 1 of 1 (k = 2) | 6 only (of 40) | yes | PASS | PASS (even k ≥ 10: none beyond k(k+2); L = k(k+2) for k = 10, 14) |

Margin: the smallest L*(k) − k(k+2) over primes 5 ≤ k ≤ 997 is 4 (k = 163). All composite exceptions are divisible by 3 or 5; this is evidence on finite data, not proved. A47 already showed that the sporadic (k+2)²−3 zeros at k = 15 and 21 are small-size coincidences.

Primary list (L* with the forced zeros removed; k(k+2) in brackets): 61: 8165 (3843); 65: 9545 (4355); 67: 5838 (4623); 69: 6150 (4899); 71: 9472 (5183); 73: 6625 (5475); 79: 7909 (6399). k = 75 (not squarefree) has last zero 7761 > 5775. No other k in 61..79 has a zero beyond k(k+2).

### 2.3 New proved zero family (Category A; found after the prereg while explaining the secondary result)

**Theorem.** Let k ≥ 9 be an odd prime power.

- If k ≡ 3 mod 4, g_k(k² + 2k + 4) = 0.
- If k ≡ 1 mod 4, g_k(k² + 3k + 4) = 0.


*Proof.* Take d = k² + 2k + 4 (or k² + 3k + 4). In both cases (k+1)² < d < (k+2)², so every contributing n has n ≤ k+1. Also d ≡ 4 mod k, so p^a | (n−2)(n+2). Since p is odd, p cannot divide both factors (it would divide 4), so n ≡ ±2 mod k, and in [0, k+1] this leaves n ∈ {2, k−2}.

- Case k ≡ 3 mod 4. The n = 2 term has m = k + 2. Now 1/((1+x)(1+x²)) = (1−x)/(1−x⁴), whose coefficients are +1, −1, 0, 0 for m ≡ 0, 1, 2, 3 mod 4. Here m ≡ 1 mod 4, so the term is −1. The n = k−2 term has m = 6 ≤ k−2, so it is c_6 = +1 (entry 76). Sum 0.
- Case k ≡ 1 mod 4. The n = 2 term has m = k + 3 ≡ 0 mod 4, so it is +1. The n = k−2 term has m = 7 ≤ k−2, so it is c_7 = −1. Sum 0. ∎

*Check:* exact Python integers, all 254 odd prime powers 9 ≤ k ≤ 1501: 0 failures (`analysis/new_zero_check.py`). The formula fails at k = 3, 5, 7 (values −1, −1, +1), as the proof predicts (it needs k − 2 ≥ 6 or 7). Among non-prime-powers ≤ 1501 only k = 15 gives zero at this d. Consequence: for every odd prime power k ≥ 9, L*(k) ≥ k(k+2) + 4 > k(k+2) with the forced zeros removed, so the prime half of Prediction 1 is proved for all primes k ≥ 11 (and k = 3, 5, 7 by the finite data in entry 80).

*Status.* This was found after the prereg, so it is an explanation, not a preregistered prediction. A cleaner statistic after this result would remove the three families (k(k+2), (k+2)²−3, class-4 zero). On k ≤ 997 that gives 74 of 164 primes k ≥ 11 with no zero beyond k(k+2); the prereg's L* does not do this.

### 2.4 Prediction 2: T(k) and the next jump (exact, D = 5·10⁶)

| k | 61 | 63 | 65 | 67 | 69 | 71 | 73 | 75 | 77 | 79 |
|---|---|---|---|---|---|---|---|---|---|---|
| T(k) | 2 032 764 | 2 163 991 | 2 402 920 | 3 331 509 | 3 615 885 | 3 921 828 | 4 230 862 | 4 546 884 | 4 857 055 (censored) | 5 000 000 (censored) |
| ρ(k) | 23.373 | 23.350 | 23.848 | **27.242** | 27.559 | 27.892 | 28.177 | 28.431 | 28.622 | 28.305 |
| increment | +0.25 | −0.02 | +0.50 | **+3.39** | +0.32 | +0.33 | +0.28 | +0.25 | +0.19 | −0.32 |

- Jumps so far: **7, 13, 21, 37, 47, 67**. Gaps between jumps: 6, 8, 16, 10, 20.
- Point prediction (63): **FAIL**. Window prediction ({61, 63, 65, 67}): **PASS**, at its edge.
- Post-jump ρ in [25, 28] at the jump: pass (27.242). The plateau leaves the range at k = 73.
- Exactly one jump in 61..79: not decided. No second jump in 69..75, and k = 77, 79 are censored.
- Plateau slopes: within each plateau ρ grows by 0.25–0.34 per step, as before.
- The mechanism of the jump positions is still unknown. I do not offer a formula; a fit to six jump positions would be post hoc.

## 3. Task 2: Parity Dominance at N1 = 1500 (Category A, computer-assisted)

**Method.** The A41 method: local-CLT layer, block ratios on u-boxes of width 0.0025 (window parameters from the A39/A41 `run_k.sh` rule applied to `saddle.json`), closed-form tails with η_t = 10⁻⁶, and D_k = ⌈(N1/α1)²⌉. Two complete pipelines were run for every k:
1. A41 code (`proof_A41/`: `clt.py`, `sums.py`, `blocks_k.py`, `verify_blocks_k.py`, `tails_k.py`, and `tails_indep_A49.py`, the closed-form tail check).
2. The independent local-CLT layer (`proof_A44/clt_indep.py`, cells of width 0.01 valid for n ≥ 1467) with `blocks_indep.py` (python-flint balls) and `tails_A44.py`.

The reported R_k is the larger of the two block ratios and D_k the larger of the two D_k, so the table is conservative. η_k = 1 − R_k − 10⁻⁶, truncated at the fifth decimal.

| k | R_k (A41 cells) | R_k (independent cells) | R_k used | tail margin T(D_k) (A41 / indep.) | D_k | η_k (N1 = 1500) | η_k at N1 = 900 (ledger) | η_k/(1 − c_k) |
|---|---|---|---|---|---|---|---|---|
| 3 | 0.5695634 | 0.5696327 | 0.5696327 | -58.71 / -59.56 | 16,677,061 | 0.43036 | 0.39748 (R 0.6025) | 0.791 |
| 5 | 0.6308769 | 0.6308670 | 0.6308769 | -41.78 / -42.94 | 20,392,280 | 0.36912 | 0.32961 (R 0.6704) | 0.752 |
| 7 | 0.6766216 | 0.6765257 | 0.6766216 | -36.72 / -37.85 | 23,928,260 | 0.32337 | 0.27687 (R 0.7231) | 0.710 |
| 9 | 0.7141402 | 0.7140340 | 0.7141402 | -31.33 / -32.43 | 27,279,558 | 0.28585 | 0.22197 (R 0.7680) | 0.665 |
| 11 | 0.7470252 | 0.7467666 | 0.7470252 | -31.47 / -31.54 | 30,851,000 | 0.25297 | 0.18073 (R 0.8093) | 0.618 |
| 13 | 0.7768933 | 0.7765630 | 0.7768933 | -23.86 / -23.93 | 32,980,768 | 0.22310 | 0.14192 (R 0.8481) | 0.569 |
| 15 | 0.8049517 | 0.8045579 | 0.8049517 | -20.26 / -20.33 | 35,639,193 | 0.19504 | 0.06396 (R 0.8860) | 0.516 |
| 27 | 0.9616335 | 0.9612190 | 0.9616335 | -1.52 / -1.59 | 49,340,462 | 0.03836 | n/a | 0.119 |
| 29 | 0.9880828 | 0.9879831 | 0.9880828 | -0.06 / -0.12 | 51,587,220 | 0.01191 | n/a | 0.038 |
| 31 | 1.0152113 | 1.0154648 | 1.0154648 | 3.60 / 2.62 | 53,715,197 | none (R > 1) | n/a | n/a |
| 33 | 1.0436421 | 1.0436127 | 1.0436421 | 4.62 / 4.56 | 55,731,381 | none (R > 1) | n/a | n/a |

Each pipeline requires R_k + 10⁻⁶ < 1 and T(D_k) ≤ 0 (and the tail monotonicity checks, all true). This holds for k = 3..15, 27, 29. It fails for k = 31 (R = 1.0155, T > 0) and k = 33 (R = 1.0436, T > 0): the method does not close at N1 = 1500 for k ≥ 31.

**Remarks.**
- k = 29 is marginal. R_29 = 0.98808, and T(D_29) = −0.057 (A41 code) and −0.119 (independent code), computed in ball arithmetic. The margin is real but small.
- The η_k/(1 − c_k) ratio at fixed N1 = 1500 falls smoothly with k: 0.79, 0.75, 0.71, 0.67, 0.62, 0.57, 0.52 for k = 3..15 and 0.46, 0.40, 0.34, 0.27, 0.20 for k = 17..25 (A45), then 0.12 and 0.04 at k = 27 and 29. The earlier non-monotone look (η_17 above η_15) came from N1 = 900 against 1500; at one N1 the ratio is smooth. This is a finite-data observation.
- The N1 = 900 caveat is closed. R_k falls by 0.03 to 0.08 against N1 = 900 for k ≤ 15 (R_15: 0.8860 → 0.8050).
- Prereg check for Task 2: k = 27, 29 pass and 31, 33 fail: as forecast. η_15 in [0.09, 0.12]: **missed** (0.19504); the "about 0.104" value was not reproduced, because the N1 = 900 value 0.064 was held down by η_t = 5·10⁻².
- The independent R1 cells and the A41 cells give block ratios that agree to within 0.0004 for every k here (the independent cells are lower except at k = 3, 5 and 31, where they are higher by at most 0.00025), and k = 33 needed cells up to u = 3.2 (the first block run stopped with a cell-cover assertion, log kept as `proof_A44/blocks_k33_firstattempt_failed.log`).

### Certificate ranges (nonvanishing and zero sets)
Two-prime certificate (`cert/gcert.c`, primes 2⁶¹−1 and 10¹⁸+3) for every allowed d ≤ 6·10⁷ for k = 3..15, 27, 29. This exceeds every D_k above (largest: 51 587 220 at k = 29). The earlier certificate for k ≤ 15 reached only 2·10⁷, which is below D_k at N1 = 1500 for k ≥ 5 (D_15 = 35.6 million), so it had to be redone. For each k the double-zero set equals the exact integer zero set computed to 2·10⁶ (`cert/compare.json`, all 9 match, no double zero beyond 2·10⁶). Hence the zero sets are complete:

| k | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 27 | 29 |
|---|---|---|---|---|---|---|---|---|---|
| #Z_k | 9 | 17 | 24 | 20 | 43 | 54 | 55 | **68** | **121** |
| max Z_k | 43 | 176 | 247 | 118 | 273 | 545 | 565 | **1375** | **1934** |

The values for k ≤ 15 agree with ledger entry 80. For k = 31 and 33 (not proved) the exact zero sets to 2·10⁶ have 127 and 88 elements, with maxima 1712 and 1587, and the last d with E_d ≥ O_d is 174 344 and 205 161 (identical to A43).

**Consequence (Category A, computer-assisted).** For odd k ≤ 29 (k = 3..15 at N1 = 1500, k = 17..25 from A41/A44, k = 27, 29 here), OccFilt_k(∞) = {squares mod k}, E_d ≤ (1 − η_k)·O_d for allowed d ≥ D_k, and g_k(d) ≠ 0 for every allowed d > max Z_k. The two constants for k = 27 and 29 are new and have not been audited by anyone other than these two pipelines of mine.

## 4. Deviations and caveats
- The class-4 zero family (§2.3) was found after the prereg; the prereg's forced set did not include it.
- Secondary-set k = 3 is added from A41/A40 data, because A43's directory starts at k = 5.
- The preregistered tertiary scan uses D = 2·10⁶ (the prereg says so); zeros of even k beyond 2·10⁶ are not excluded.
- Prediction 1 is a finite-range statement; L* is not proved to be a last zero for any k in 61..79 because no tail is proved there.
- `proof_A41/saddle.py` was extended to k ≤ 33; the saddle values for k ≤ 25 are identical to A41's (checked: all equal). The A38 `clt.py` and `sums.py` were called read-only through `r1_oracle_A49.py`; copies in `proof_A41/` are byte copies of A41's.
- Nothing outside `A49_gk_runs/` was modified.

## 5. Files
`prereg/` (prereg and hash); `exact/` (`eo_gmp.c`, `gcert.c`, `run_exact.sh`, `run_even.sh`, `eo_k61..79.json`); `scan/` (two-prime zero lists, odd and even); `analysis/` (`lstar.py`, `lstar.json`, `tk.py`, `tk.json`, `summarize.py`, `pd_summary.json`, `new_zero_check.py`, `new_zero_check.json`); `proof_A41/` and `proof_A44/` (code, cells, block and tail JSON, logs); `cert/` (`gcert`, zero lists, `compare.py`, `compare.json`, `eo_k*_D2000000.json`); `logs/`; `SHA256SUMS`; `REPORT.md`; `REPORT.pdf`.
