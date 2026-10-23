# A38: Lemma L (E_d ≤ (1−η)·O_d) and OccFilt_7(∞)

Date: 2026-10-22 (CDT). Folder: `reports/s_family_paths/A38_lemmaL/`. New files only. CORE_FREEZE untouched: H_s is not redefined and no certifier code was modified. No TPC or RH claim is made. Nothing was pushed or sent.

## Verdict

**Lemma L is already proved (computer-assisted). It is not open.** The proof is the "route 3" pass of 2026-10-17 (rev 2), which was audited once and later renamed the *Parity Dominance Theorem*. The brief's "open since 2026-10-17" describes the first and second passes only. The third pass closed the lemma that same evening.

This session did three things:
1. checked the prior proof's files against their checksums;
2. reran its rigorous verification and reproduced every constant exactly;
3. ran an independent exact computation of E_d/O_d up to d = 3·10^6, extending the earlier exact range of 10^6.

I found no error. I did not write a new or second proof. Two limits still apply: the status is still "computer-assisted, one independent audit, no formal verification", and the reproduction here used the same code.

## 1. Definitions (from the 2026-10-17 report)

- g_7(q) = Σ_{n≥0} q^{n²}/(−q^7;q^7)_n. Its coefficients are g_7(d) = Σ_n φ_n((d−n²)/7), where φ_n(m) = [x^m] ∏_{j≤n} 1/(1+x^j).
- **Allowed d:** d mod 7 ∈ {0,1,2,4}. These are the classes containing some n² mod 7.
- **OccFilt_7(∞):** the set of residues mod 7 where g_7(d) ≠ 0 for all sufficiently large d. The target statement is OccFilt_7(∞) = {0,1,2,4}. Concretely, g_7(d) ≠ 0 for every allowed d > 247.
- **a_n(m)** = (−1)^m φ_n(m) = [x^m] ∏_{odd j≤n}(1+x^j) / ∏_{k=⌊n/2⌋+1}^{n}(1−x^{2k}). This is ≥ 0 (A1).
- **E_d** = Σ_{n even} a_n((d−n²)/7) and **O_d** = Σ_{n odd} a_n((d−n²)/7). Both sums run over n with n² ≤ d and n² ≡ d (mod 7).
- Then (−1)^d g_7(d) = E_d − O_d (A2).
- **Lemma L:** there exist explicit η > 0 and D0 ≤ 10^7 such that E_d ≤ (1−η)O_d for every allowed d ≥ D0.
- Lemma L together with the finite certification gives OccFilt_7(∞).

## 2. Prior work located

Main file: `reports/self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/OccFilt7_Inf_Theorem_L_2026-10-17/2026-10-17-Lever-3-OccFilt7-Lower-Bound.md`. The same tree is in `oct17-master/docs/...`.

- **Pass 1 (conditional).** This pass proved A1 to A4:
  - positivity;
  - the even/odd split;
  - the ladder T_{2k+1} = T_{2k}·q^{4k+1}/(1−q^{14k+7});
  - the reduction.

  It stated Lemma L as open.
- **Pass 2 (partial).** This pass added three items:
  - exact ladder inequalities in n (L1);
  - two obstructions: no single-layer-pair certificate (L2), and no fixed-partner injection, by a pole-order argument (L3);
  - a fractional-transport plan that needed the analytic inputs R1 to R4.
- **Pass 3, route 3 (proof).** This pass proved R1 to R4:
  - a local CLT for the tilted restricted-partition model, with explicit D1, D2 and D3, minor-arc bounds, and Lemma S for uniformity in n;
  - block ratio bounds checked by mpmath interval arithmetic for n ≥ 900;
  - Chernoff tail bounds.

  Result: **E_d ≤ (1−0.2272)·O_d for all allowed d ≥ D0 = 8 890 003 (n1 = 900).**
- **Audit and rev 2.** One adversarial audit found 7 issues: 3 repairable and 4 cosmetic. All were patched and rerun, and the constants were unchanged or moved in the favourable direction.
- **Naming.** `ERRATUM_Rename_Theorem_L_to_Parity_Dominance_Theorem_2026-10-17.md` renames the theorem. "Lemma L" keeps its name as the target inequality.
- **Finite range.** g_7(d) ≠ 0 is certified for allowed 247 < d ≤ 10^7 (`g7mod`, 2 primes). Later certificates extend this to 10^8 and 10^9. The 10^7 range already covers d < D0.
- **Later consolidated papers (rev 5 to rev 9, 2026-10-18/19).** They only repeat the naming convention. They do not change the status.
- **grok_export chats (A22 `chats/f7cf38a4…`).** They hold the pass-1 summary, which says "Lemma L itself remains open". That summary predates pass 3.
- **GitHub.** The `gh` CLI on the box is not authenticated, so no remote read of ArvinHampton/539-Labs-Master was possible. The local mirrors `oct17-master/` and `reports/self-audit/repo/` were used instead.

## 3. Category A (proved or exact)

1. **Prior proof (cited, not re-proved here).** Lemma L holds with η = 0.2272 and D0 = 8 890 003. Its status is Category A, computer-assisted, with one independent audit plus the rev 2 patches. It is not a formal verification. With the certification to 10^7, OccFilt_7(∞) = {0,1,2,4}, and the largest allowed-class zero is d = 247.
2. **Integrity.** `sha256sum -c` on `lemmaL/route3/SHA256SUMS` gives 32/32 OK (`sha_check.txt`).
3. **Reproduction (exact rerun, same code).** The scripts were copied to `rerun_route3/` and run with `nice` and OMP_NUM_THREADS=1.
   - `verify_blocks.py 900 0.3 1.6`: the block ratios are 0.7231289922, 0.7397366846, **0.7727327796** (class 2) and 0.7356179382. Max δ = 0.1517943, and the minimum odd-side factor is 0.78508. The output is identical to `out_verify_blocks_rev2.txt`.
   - `tails.py 900 0.3 1.6 0.152 1e-6`: D0 = 8 890 003, Ψ_low = 0.395568, max tail gap −0.014809, and T(D0) = −6.8025. The output reports "R4 verified: True" and is byte-identical to `out_tails.txt`.
   - The resulting margin is η = 1 − 0.77273278 − 10^−6 = 0.227266.
4. **Independent exact computation (`exact/eo_exact.py`).** This is new code using exact Python integers. A_n is built by exact division ladders and cross-checked against the direct product for n ≤ 30.
   - For allowed 1128 ≤ d ≤ 3·10^6: O_d > E_d.
   - The last d with E_d ≥ O_d in each class is 1127 (class 0), 407 (class 1), 247 (class 2) and 60 (class 4). This agrees with the prior 10^6 run.
   - **E_d ≤ (1−0.2272)·O_d holds for every allowed d with 1324 ≤ d ≤ 3·10^6.** The last violation is at d = 1323.
   - The thresholds for larger η are: η = 0.3 from d ≥ 2347, η = 0.4 from d ≥ 4516, and η = 0.45 from d ≥ 10809.
   - Note on rigour: the inequality tests compare integers exactly. The ratio values in the TSV files are correctly rounded floats and are used only for reporting.
5. **What is not covered by an exact η-inequality.** For 3·10^6 < d < D0, only g_7(d) ≠ 0 is certified, not E_d ≤ (1−η)O_d. This does not matter for OccFilt_7(∞). It does mean that "Lemma L with η = 0.2272 for all d ≥ 1324" is **not** established.

## 4. Category B (numerical or heuristic; not proofs)

- Observed best η, i.e. 1 − max E/O over each window:

  | window (allowed d) | max E_d/O_d | observed η |
  |---|---|---|
  | 1128–9999 | 0.99442 at d=1134 (class 0) | 0.0056 |
  | 10^4–10^5 | 0.55438 at d=10003 | 0.4456 |
  | 10^5–10^6 | 0.544514 at d=100003 | 0.45549 |
  | 10^6–3·10^6 | 0.544396 at d=1000024 | **0.45560** |

- E_d/O_d decreases toward the closed form (1−√(1−y²))/y = 0.5443407, where y⁷ + y² = 1. At d ≈ 3·10^6 the ratio is 0.5443728, and the gap scales like d^{−1/2}. So the asymptotically best η appears to be ≈ 0.45566. That this limit holds is Category B.
- The rigorous η = 0.2272 is conservative by about a factor 2. The slack comes from the local-CLT error δ ≈ 0.15, against an empirical value of about 0.02–0.03. Tightening it would need larger n1 or an Edgeworth term, as the prior report already notes.

## 5. Open items (unchanged)

- A formal verification or second independent audit of the route-3 interval code.
- A two-sided bound |E_d/O_d − 0.5443407| ≤ δ(d) (prior "steering (b)", not achieved).
- An exact η-inequality on (3·10^6, D0). This is optional and not needed for OccFilt_7(∞).

## Files

- `REPORT.md`, `REPORT.html`, `REPORT.pdf`
- `sha_check.txt`: checksum check of the prior route-3 folder
- `rerun_route3/`: copies of the prior scripts (unmodified) and `out_verify_blocks.txt`, `out_tails.txt`
- `exact/eo_exact.py`: independent exact E_d, O_d. Usage: `python3 eo_exact.py D`. D = 3·10^6 takes 2 min 8 s and stays under 3 GB.
- `exact/stats.py`, `exact/stats_1e6.json`, `exact/stats_1e6_3e6.json`, `exact/summary_*.json`, and `exact/eo_*.tsv(.gz)`: per-d E/O ratios
