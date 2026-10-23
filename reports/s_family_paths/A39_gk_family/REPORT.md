# A39: Parity Dominance for the family g_k(q) = Σ q^{n²}/(−q^k;q^k)_n, k = 2..15

Date: 2026-10-22 (CDT). Folder: `reports/s_family_paths/A39_gk_family/`. New files only.

Constraints observed:
- CORE_FREEZE untouched: H_s is not used or redefined, and no certifier code was modified. `g7mod.c` was not touched; `cert/gkmod.c` is new.
- No TPC or RH claim is made.
- Nothing was pushed or sent.

## Verdict

**Odd k.** For every odd k in {3, 5, 7, 9, 11, 13, 15}, the Parity Dominance method generalises.
- Proved (Category A, computer-assisted, **not independently audited**): E_d ≤ (1−η_k)·O_d for all allowed d ≥ D_k. The explicit constants are in the table below.
- Every D_k is ≤ 1.28·10^7, and the new two-prime nonvanishing certificate covers d ≤ 2·10^7.
- Hence **OccFilt_k(∞) = {squares mod k}**, and the full zero set of g_k is exactly the finite list found for d ≤ 2000.

**Even k.** The method does not apply, because there is no parity split. This is proved below.
- For k = 2, 6, 10, 14, every class has no cancellation. The zero sets are proved finite by an elementary argument, and OccFilt_k(∞) = {squares mod k} (Category A).
- For k = 4, 8, 12, the "MIX" classes (k=4: c=0; k=8: c=1; k=12: c=0, 4) have two cancelling groups of the same parity. There is no proof for them.
  - They have no zeros in (2000, 2·10^7], certified.
  - Numerically the two groups agree to more than 9 digits. The sign of g oscillates periodically in √d.
  - Whether these classes belong to OccFilt_k(∞) is **open**.

**Uniform in k.** The method is not uniform in k.
- The local-CLT input does not depend on k.
- The block and tail steps are parametrised by k, but each needs its own computer verification.
- The proved η_k decreases with k. The predicted limiting ratio c_k tends to 1 as k → ∞ (Category B), so this method cannot give one η for all k.

## 1. Definitions and the family in the sources

- **Family.** g_k(q) = Σ_{n≥0} q^{n²}/(−q^k;q^k)_n. This is exactly the framework's g_s, "Master contact 23": `Residual_Packaging_and_Series_Manuscript_FINAL_2026-08-20.txt` and `g_s_Closed_Forms_2026-10-18/`. The named residual cases are s ∈ {7, 8, 11}.
- **Related object.** The sources also use P_s = (−q^s;q^s)_∞·g_s, an Euler double sum. It is a different object, and its zero set was not studied here. No other g-family was found. I write k to avoid any clash with the frozen H_s.
- **Coefficients.** g_k(d) = Σ_n φ_n(m), where m = (d−n²)/k ∈ Z_{≥0} and φ_n(m) = [x^m]∏_{j≤n}(1+x^j)^{−1}.
- **Allowed classes.** g_k(d) = 0 trivially unless d is a square mod k. The allowed classes are the squares mod k; for k = 7 this gives {0, 1, 2, 4}.
- **OccFilt_k(∞)** = the set of allowed c such that g_k(d) ≠ 0 for all sufficiently large d ≡ c (mod k).

## 2. Category A: general-k algebra (proved here)

**Positivity (any k; k-independent).** For all n, m: (−1)^m φ_n(m) = a_n(m) := [x^m] ∏_{odd j≤n}(1+x^j) / ∏_{⌊n/2⌋<l≤n}(1−x^{2l}) ≥ 0.

*Proof.* Put y = −x. Then 1/(1+y^j) = (1−y^j)/(1−y^{2j}) = (1−y^j)/(1−x^{2j}).
- The numerator ∏_{j≤n}(1−y^j) equals ∏_{odd j}(1+x^j)·∏_{l≤⌊n/2⌋}(1−x^{2l}).
- The second factor cancels the first ⌊n/2⌋ factors of ∏_{j≤n}(1−x^{2j}).
- What remains has non-negative coefficients. ∎

Also verified: the exact series agrees with direct q-expansion of g_k for d ≤ 2000, for every k = 2..15 (assert in `exact/gk_exact.py`).

**Sign split.** Since g_k(d) = Σ_n (−1)^m a_n(m), set P_d = Σ_{m even} a_n(m) and N_d = Σ_{m odd} a_n(m). Then g_k(d) = P_d − N_d with P_d, N_d ≥ 0.
- **k odd.** km ≡ m (mod 2), so (−1)^m = (−1)^{d−n²} = (−1)^{d+n}. Hence (−1)^d g_k(d) = E_d − O_d, where E_d and O_d sum a_n((d−n²)/k) over even and odd n respectively.
  - Along a residue chain n ≡ r (mod k), consecutive members n and n+k have opposite parity.
  - So every allowed class mixes parities. This is type **PD**.
- **k even.** n² ≡ d (mod k) forces n ≡ d (mod 2), so every contributing n has the parity of d, and there is no parity split.
  - Moreover (n+k)² ≡ n² (mod 2k), because 2nk ≡ 0 and k² ≡ 0 (mod 2k). So the sign depends only on n mod k, through n² mod 2k.
  - The class is type **ONE** if all roots r of r² ≡ c (mod k) give the same r² mod 2k. Then all terms of g_k(d) have one sign.
  - Otherwise the class is type **MIX**: two sign groups, both of the parity of d. In k = 2..15 the MIX classes are k=4: c=0; k=8: c=1; k=12: c=0, 4. Classification is in `prereg/classify.py`.

**ONE classes: zeros are finite, with explicit bound (`exact/one_classes.py`).** Fix c and the smallest n ≥ 3 with n² ≡ c (mod k), and put L = ⌊n/2⌋+1.
- For n ≥ 3, the parts 2L and 2L+2 both occur in A_n, and every integer ≥ L(L−1) is a non-negative combination of L and L+1.
- So a_n(m) > 0 for all m ≥ 2L(L−1)+1: use the odd part 1 for odd m.
- Because all terms have one sign, g_k(d) ≠ 0 for every d ≡ c (mod k) with d ≥ B_c = n² + k(2L(L−1)+1). The largest B_c in the range is 1778 (k=14, c=0).
- Below B_c the exact run decides.

Result: for k ∈ {2, 6, 10, 14}, and for the ONE classes of k = 4, 8, 12, the class is in OccFilt_k(∞), with the exact zero lists in §5.

## 3. Category A: Parity Dominance for odd k (computer-assisted, unaudited adaptation)

**Method.** This is the route of `OccFilt7_Inf_Theorem_L_2026-10-17` (A38), adapted to general odd k.
- **(R1) Local CLT.** `clt.py` and `sums.py` are copied byte-identically. They concern A_n alone, so **R1 does not depend on k**. Only the u-window where it is evaluated changes.
- **(R2/R3) Blocks (`proof/blocks_k.py`).** One universal block is used for every class: e_n against ½(o_{n−k} + o_{n+k}).
  - n±k lie in the same square class and have the opposite parity.
  - Each odd term receives total weight ≤ 1, and the chains for distinct roots mod k are disjoint.
  - The k-dependence enters through r^{(n_i²−n²)/k}, the offsets ±k, and the bound n_i ≥ n−k.
  - Sanity check: at k = 7 this reproduces A38's class-0 ratio 0.7231289922 exactly.
- **(R4) Tails (`proof/tails_k.py`).**
  - F_k(α,u) = αΦ1(u) + (1−α²)u/(kα).
  - The central odd term n* has α ∈ [a0, a0 + 2k/√d], and its saddle u* is certified in [ulo, uhi] per k.
  - Tiny-α constants: c0 = 2 − log k, the coefficient 0.75k, and g ≤ log(2d/k) + 1.
  - Sanity check: at k = 7 this reproduces A38's D0 = 8 890 003, Ψ_low = 0.395568 and gap −0.014809.
- **Parameters.** N1 = 900 and a u-window [0.5u0, 2.6u0], where u0 = −(k/2)ln y and y^k + y² = 1. The CLT error δ ≤ 0.186 holds on every window used, and tails_k uses δ = 0.2.

**Result.** For every allowed d ≥ D_k, E_d ≤ (1−η_k)·O_d, with η_k = 1 − R_k − η_t:

| k | u-window | block ratio R_k | tail η_t | **η_k** | **D_k** | CLT δ max | T(D_k) |
|---|---|---|---|---|---|---|---|
| 3 | [0.21, 1.10] | 0.6025109 | 10^−6 | **0.39749** | 5 988 500 | 0.127 | −15.4 |
| 5 | [0.27, 1.38] | 0.6703845 | 10^−6 | **0.32961** | 7 321 266 | 0.139 | −4.64 |
| 7 | [0.30, 1.60] | 0.7231290 | 10^−6 | **0.27687** | 8 890 003 | 0.151 | −6.80 |
| 9 | [0.34, 1.76] | 0.7680282 | 10^−2 | **0.22197** | 9 791 834 | 0.161 | −6.72 |
| 11 | [0.36, 1.89] | 0.8092646 | 10^−2 | **0.18073** | 11 073 024 | 0.170 | −5.97 |
| 13 | [0.39, 2.02] | 0.8480780 | 10^−2 | **0.14192** | 11 836 583 | 0.178 | −1.03 |
| 15 | [0.41, 2.12] | 0.8860341 | 5·10^−2 | **0.06397** | 12 789 969 | 0.186 | −0.011 |

The exact windows are in each `out_k*_N900.txt` header. Raw outputs are in `proof/out_k*_N900.txt` and `proof/out_tails_k*_eta*.txt`.
- With η_t = 10^−6, R4 failed for k = 9, 11, 13 and 15; those failures are recorded.
- R4 was rerun with a larger tail allowance η_t, as stated in the table. That is legitimate, because any η_t works if T(D_k) ≤ 0.
- For k = 15 the margin is thin (T = −0.011).

**k = 7 bonus.** The universal block covers all four classes, so A38's η improves from 0.2272 to **0.27687** at the same D0. This uses the same verified code paths, plus the universal pattern.

**Finite range (`cert/gkmod.c`, new code).** For k ∈ {3, 4, 5, 7, 8, 9, 11, 12, 13, 15}, g_k(d) mod p was computed for d ≤ 2·10^7 with p = 2^62−57 and p = 2^62−87.
- In every case, the allowed d with g ≡ 0 mod both primes are exactly the zero set from the exact run (`cert/cert_summary.json`). Every other allowed d ≤ 2·10^7 has g_k(d) ≠ 0.
- k = 2 was also run to 5·10^7 with one prime: 4 zeros, the known ones.

**Conclusion.** For odd k ≤ 15, OccFilt_k(∞) = {squares mod k}, and the complete zero set of g_k is the list in §5.

Status and caveats:
- Category A, computer-assisted. The k-parametrised scripts are a fresh adaptation, and **no independent audit of them has been done**. The A38 code they derive from was audited once.
- The blocks and tails reuse the A38 interval machinery unchanged apart from the k-substitutions listed in the script headers.

**Exact cross-check (Category A on the stated range).** For odd k, the inequality E_d ≤ (1−η_k)O_d holds for all allowed d with d_k < d ≤ 3·10^5·k. Here η_k is rounded down to 4 digits. `exact/eta_exact.py` compares ratios rounded to 9 digits; the closest any ratio comes to the threshold is 6·10^−5, so rounding cannot change the outcome.

| k | 3 | 5 | 7 | 9 | 11 | 13 | 15 |
|---|---|---|---|---|---|---|---|
| d_k (last violation) | 159 | 580 | 1372 | 4573 | 7800 | 11948 | 15879 |
| last d with E_d ≥ O_d | 43 | 176 | 1127 | 2056 | 3872 | 10635 | 14739 |

## 4. Which steps are uniform in k

| step | k-dependence | status |
|---|---|---|
| Positivity, sign split | none / parity of k | proved for all k |
| R1 local CLT for A_n (δ, minor arc, Lemma S) | **none** (depends only on u-window and n1) | proved; cells reusable |
| R2/R3 block lemma | algebra parametric in k; numerical interval check per k; needs n1 ≫ k | verified k = 3..15 odd |
| R4 tails | F_k, central u*, tiny-α constants: explicit in k; check per k | verified k = 3..15 odd |
| finite range | D_k ≈ (900/α1(k))², α1 decreasing in k | covered by certificate ≤ 2·10^7 |
| even k | no parity split (proved) | method inapplicable |

**Uniform statement, as far as it goes (Category A).** For every odd k, Parity Dominance reduces to two finite interval checks, R2/R3 and R4, with the same R1. Both checks pass for every odd k ≤ 15.

**Obstruction to uniformity (Category B).**
- The predicted limit E/O → c_k = (1−y^{k/2})/y tends to 1 as k → ∞, with 1−c_k ≍ √(2 log k / k).
- The block slack (δ ≈ 0.13–0.19) grows with k.
- So η_k → 0, and no k-uniform η is available from this route. The proved η_k falls from 0.397 at k = 3 to 0.064 at k = 15.
- Extending to k ≥ 17 likely needs a larger n1 (smaller δ), and hence larger D_k and certificates.

## 5. Zero sets (Category A: exact to 3·10^5·k, plus certificates and proofs above)

- k=2: 2, 8, 10, 26
- k=3: 3, 4, 6, 7, 15, 28, 31, 40, 43
- k=4 (MIX class 0 only to 2·10^7): 12, 20, 48, 52, 60, 84, 116, 140
- k=5: 17 zeros, last 176
- k=6: 3, 6, 12, 18, 21, 24, 30, 46, 48, 78
- k=7: the 24 known, last 247
- k=8: 17 zeros, last 1657 (class 1 MIX; certified only to 2·10^7)
- k=9: 20 zeros, last 118
- k=10: 17 zeros, last 120
- k=11: 43 zeros, last 273
- k=12: 23 zeros, last 1564 (MIX classes 0 and 4; to 2·10^7)
- k=13: 54 zeros, last 545
- k=14: 30 zeros, last 224
- k=15: 55 zeros, last 565

Full lists are in `exact/summary_k_D.json`.

## 6. Preregistration and outcome

`prereg/prereg.md` (sha256 `04a2b7ee…5127ae`, together with `classes_2000.json` and `classify.py` in `prereg.sha256`) was written at 13:10:36 CDT. It used only the data for d ≤ 2000. The file's own text says "13:2x"; the file mtime is authoritative. The large runs started afterwards.

| prediction | outcome |
|---|---|
| Z: classes with no zero in (1000, 2000] have no new zero (every PD and ONE class, k = 4 c = 0, k = 12 c = 0) | **confirmed** for every such class, exact to 3·10^5·k and certified to 2·10^7 (k = 2: 5·10^7) |
| Z: k = 8 c = 1 and k = 12 c = 4 (zeros at 1657 and 1564) predicted to have recurring zeros | **failed**: no new zero up to 2·10^7 |
| S: odd k, E/O → c_k = (1−y^{k/2})/y | **confirmed (Category B)**. At D = 3·10^5·k the exact ratio is c_k + O(d^{−1/2}): k = 3: 0.4558843 vs 0.4558810; k = 15: 0.6220196 vs 0.6219026 |
| M: MIX, min(P,N)/max(P,N) → 1 and recurring sign changes | **confirmed (Category B)** |
| ONE: finitely many zeros | **proved** (§2) |

Details of the MIX classes (`exact/mix_detail.py`; Category B):
- The ratio min(P,N)/max(P,N) equals 1 to 9 digits.
- log10|g| ≈ 0.5–0.75 · log10 P (k = 8 at d ≈ 4·10^5: 61.3 vs 100.8).
- Sign changes for k = 8 and k = 12 occur at √d spaced periodically, about 11.9 apart for k = 8 and 18.5 apart for k = 12. This suggests g ≈ A·e^{c′√d}·cos(ω√d + φ) from a complex saddle.
- For k = 4, class 0, the sign alternates with d (step 8).
- Infinitely many sign changes, but exact zeros only by coincidence, would make these classes heuristically in OccFilt_k(∞). This is **not proved**.

## 7. Category B summary (not proofs)

- The limits c_k and exponents c_exp(k) come from `proof/saddle.py`. For k = 7 they reproduce A38's 0.3985400 and 0.5443407.
- The MIX oscillation picture and log|g| scaling.
- The asymptotic obstruction η_k → 0.

## 8. Open

- An independent audit of `blocks_k.py` and `tails_k.py`, the k-substitutions.
- The MIX classes (k = 4, 8, 12): nonvanishing for large d would need a two-term (complex-saddle) asymptotic with explicit error.
- Odd k ≥ 17.
- A k-uniform statement.
- P_s, which was not studied.

## Files

- `prereg/`: prereg.md, prereg.sha256, classify.py, classes_2000.json.
- `exact/`:
  - gk_exact.py (exact P/N for any k), with outputs gk_k_D.tsv.gz and summary_k_D.json for D = 2000 and D = 3·10^5·k;
  - analyze.py with analysis_big.json;
  - one_classes.py with one_classes.json;
  - eta_exact.py with eta_exact.json;
  - mix_detail.py with mix_k_400000.tsv;
  - run_big.sh, big.log, SHA256SUMS.
- `proof/`:
  - clt.py and sums.py (A38 copies, identical hashes);
  - blocks_k.py, verify_blocks_k.py, tails_k.py, saddle.py, run_k.sh;
  - out_* and JSON outputs, SHA256SUMS.
- `cert/`: gkmod.c, run_cert.sh, zeros_k*_D20000000_p*.txt, cert_summary.json, cert.log, partial_D5e7/ (k = 2 to 5·10^7), SHA256SUMS.

Resources: every run used nice and OMP_NUM_THREADS=1, with a 3 GB ulimit; the largest exact run was k = 15, D = 4.5·10^6.
