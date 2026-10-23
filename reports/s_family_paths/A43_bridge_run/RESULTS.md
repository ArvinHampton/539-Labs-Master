# A43: run of the A42 preregistered bridge test (RNT ↔ residual side)

**For:** Arvin Hampton (539 Labs) · 2026-10-22, America/Chicago (CDT). Compute ran from 16:08 to 16:20 CDT.
`SF/` = `/workspace/quantum-comp/reports/s_family_paths/`. All new files are in `SF/A43_bridge_run/`, plus the run-time `SF/A42_bridge_prereg/AMENDMENTS.md` that §6 of the prereg requires.

**Preregistration.** `A42_bridge_prereg/prereg.md` has sha256 `ae93ad54a795babc6297cf6ac8960269728b68fd3b5de91a0c10267aa3a94405`. I verified it before starting, and it matched.

**Prior attempt.** Neither `A43_bridge_run/` nor `AMENDMENTS.md` existed when I started, so nothing was moved aside and no `A43_bridge_run_aborted/` folder was created.

**AMENDMENTS.md.** Final sha256 `cd9087098bb3ba07f4a90a4e8b72a9e1a7cbf06143be52621ef640dd8760b2d5`. It records:
- the sha256 of A41 REPORT.md, REPORT.pdf and SHA256SUMS, and of A44 REPORT.md;
- the sha256 of every script, recorded before the first run;
- deviations D1 to D7, and a correction to D8 made during the run.

**Ground rules.**
- Jobs ran under `nice` with OMP_NUM_THREADS=1 and `ulimit -v` = 3 GB.
- No existing file was modified. No certifier code was touched.
- Nothing was pushed. No TPC or RH claim is made.

## Bottom line

**Fail: no testable link under M1 to M3.** No cell gave an H₁ outcome that met the Bonferroni threshold α_c = 0.05/14 ≈ 3.6·10⁻³. So no link criterion is met, the Residual-vs-Resonant lock stays in force, and under §7 maps M1 to M3 are retired.

**Status of the evidence.** Everything below is finite-range evidence, except for residue arithmetic and the audited k = 7 zero list. No dominance tail was proved for k = 49, 77 or 539, so no P1.2 statistic is Category A.

## Per-cell outcomes (m = 14)

p_c = (1 + #pool controls with a hit) / (1 + 484). The pool is all odd k in [27, 999] with k ∤ 539.
- When the 539-side value is **not** in R, the outcome is H₀ and the cell cannot pass. The p shown is then the p it would have had with a hit.
- R = {5, 10, 15, 18, 30, 45, 210, 420, 521, 539, 540, 1080, 1620, 2160, 2700, 5400}.

| cell | value | in R? | pool hits / 484 | p_c (if hit) | analytic ≈ | outcome |
|---|---|---|---|---|---|---|
| P1.2 Z(49) | 85 | no | 2 | 6.2·10⁻³ | 6.4·10⁻³ | H₀ |
| P1.2 Z(77) | 140 | no | 2 | 6.2·10⁻³ | 6.4·10⁻³ | H₀ |
| P1.2 Z(539) | 239 | no | 2 | 6.2·10⁻³ | 6.4·10⁻³ | H₀ |
| P1.2 L(49) | 4043 | no | 0 | 2.1·10⁻³ | 1.5·10⁻⁵ | H₀ |
| P1.2 L(77) | 6083 | no | 0 | 2.1·10⁻³ | 1.5·10⁻⁵ | H₀ |
| P1.2 L(539) | 76015 | no | 0 | 2.1·10⁻³ | 1.5·10⁻⁵ | H₀ |
| P1.2 T(49) | 1119311 | no | 0 | 2.1·10⁻³ | 8·10⁻⁶ | H₀ |
| P1.2 T(77) | 1807498 | no | 0 | 2.1·10⁻³ | 8·10⁻⁶ | H₀ |
| P1.2 T(539) | 1999992 | no | 0 | 2.1·10⁻³ | 8·10⁻⁶ | H₀ |
| P1.3 | — | — | — | — | — | **not run** (Branch II: A41 found no uniform identity); counted in m |
| P2.1 18 ∈ Z*₇ | primary reading: yes | — | — | p = base rate 23/141 = 0.163 | — | H₁ outcome, **not significant**. Under the literal reading the outcome is H₀ (base rate 16/126 = 0.127). |
| P3.1 6 ∈ orders(s=9), orders(s=23) | {2}; {2,2,2} | — | — | no control p defined; evidence only | — | H₀ |
| P3.2 5 ∈ orders(s=11) | {4 (ring), 4 (ray)} | — | — | evidence only | — | H₀ |
| P3.3 control: s=25 has neither 5 nor 6 | {3 or 6 (ring), 6, 2} | — | — | evidence only | — | the H₁ requirement fails (6 is present) |

**Pool hits.**
- Z: k = 45 has Z = 45, and k = 423 has Z = 210.
- L and T: no pool hits.

**Shape-matched controls (secondary).** Hits for (Z, L, T):
- p²: 0/0/0 out of 9.
- pq: 0/0/0 out of 141.
- p²q and pq²: 2/0/0 out of 47.

**R_N version (D4, D5).** The 539 side has no hit in Z, L or T, for either seed. Control families that hit:
- seed 20261022: none in Z, L or T;
- seed 20261023: none in Z, L or T.

The minimum attainable p in this version is 1/21, so it could not pass on its own. Replication is moot because no primary cell passed.

**Sensitivity: literal Z* reading (see the correction below).**
- Zlit = 43, 42 and 81 at k = 49, 77 and 539. None is in R, and the pool rate is 46/484. Llit = L.
- R_N version: the only control hits are N = 455 (seed 1) and N = 407 (seed 2), both in Zlit.
- No cell outcome changes between the two readings, except P2.1, which is not significant either way.

**Order controls (§5.2).** Base 3 produced no hit, so the base-2, base-5 and base-10 controls have nothing to beat. For the record: ord₇(2) = 3 and ord₁₁(2) = 10 do not occur at s = 9, 23 or 11 either.

## P1.1 pipeline check (never counts)

Finite-range check of OccFilt_k = Q_k:
- k = 49: |Q| = 22, last zero 4043.
- k = 77: |Q| = 24, last zero 6083.
- k = 539: |Q| = 132, last zero 76015.

In each case there is no zero in (last zero, 2·10⁷], so every allowed class is nonzero across that whole interval. This is consistent with the generic pattern and is evidence only.

## Correction of a prereg premise (logged in AMENDMENTS.md)

§2.1 of the prereg assumes that a d with exactly one contributing n is nonzero ("forced nonzero"). That is **false**.
- **Counterexample.** At k = 7, d = 18 only n = 2 contributes, and φ₂(2) = [x²] 1/((1+x)(1+x²)) = 0. The audited A40 two-prime list has 18 as a zero of g₇.
- **What still holds.** φ₁ never vanishes, so the §2.3 exclusion of d = 540 (only n = 1 contributes) remains valid.
- **Rule used.** I fixed this rule before looking at any P1.2 value: primary Z* means certified zeros with at least one contributing n (the prereg's "nontrivial zeros"), and the literal wording (at least two contributing n) is reported as a sensitivity check.
- **Effect on P2.1.** Under the primary reading the P2.1 "hit" comes from a single vanishing coefficient φ₂(2) = 0, which is elementary. It is far from significant (p = 0.163).

## Method and certification

**Exact range (to 2·10⁶).**
- k = 49, 77, 539: `scripts/eo_indep.py`, a byte-identical copy of the A40 script.
- All 497 k (pool, shape extras 9, 15, 25, the divisors of all 40 drawn N, and the anchors): `scripts/eo_gmp.c`, an exact GMP port of the same ladder with a sign check (signbad = 0 everywhere). This is deviation D1.
- **Port validation.** The port matched the audited A40/A41 outputs at k = 7, 11, 17 and 25. It also matched eo_indep.py at k = 49, 77 and 539 on both the zero lists and T.

**Mod-p certificate (to 2·10⁷).** `scripts/gcert.c`, a byte-identical copy of the A41 script, run with primes 2⁶¹−1 and 10¹⁸+3 for all 497 k.
- No k has a single-prime-only zero.
- For every k, the double-zero set on [1, 2·10⁶] equals the exact zero set.

**Reuse.** The audited A40 k = 7 lists match our k = 7 run: 24 zeros, last zero 247.

**Category.**
- Z and L are counts and maxima of double zeros in [1, 2·10⁷]. They are evidence, reported as "in [1, 2·10⁷]".
- T is "last allowed d ≤ 2·10⁶ with E ≥ O", from exact integers.

**Caveat on T.** For 465 of the 484 pool k, and for k = 539, T is within 10⁵ of the 2·10⁶ edge. So T at this range mostly measures the range, not a converged threshold. It did not produce any hit.

**M3 inputs.** Character orders come from the A36 REPORT eigen-system table (D7); there was no new computation. Orders read from 8 sampled primes are lower bounds.

## Files

- `scripts/`: eo_indep.py, eo_gmp.c, gcert.c, draw.py, mkjobs.py, run.sh, analyze.py, mk_pdf.py, and SHA256SUMS.
- `data/`:
  - `exact/eo_k*.json` (497 files)
  - `cert/z_k*_p*.txt`
  - `py/` (eo_indep at k = 49, 77, 539)
  - `validate/`
  - `draws.json`, `joblist.txt` (interleaved order, shuffle seed 539)
  - `P2_1.txt`, `results.json`
- `logs/`
