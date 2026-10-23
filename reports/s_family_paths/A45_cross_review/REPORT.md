# A45: cross-review of A31–A44 and LEDGER_CatA_clean_v5

**For:** Arvin Hampton · 2026-10-22, about 4:30 PM CDT. Folder: `SF/A45_cross_review/`, where `SF/` = `/workspace/quantum-comp/reports/s_family_paths/`.

**Ground rules.** Only new files were written, all in this folder. No existing file was modified, nothing was pushed, and no certifier code was touched. The light computations ran under `nice` with OMP_NUM_THREADS=1 and `ulimit -v` 3 GB, with peak memory under 0.3 GB. Imports were read-only: A36 `classdata.py` (class-group structure) and the A39, A41 and A43 data files. No TPC or RH claims are made.

**Categories.**
- **Cat A:** proved, or an exact certificate.
- **Evidence:** an observed pattern in existing data.
- **Conjecture:** a stated extrapolation.

Every correlation found here is flagged as worth preregistering. None is claimed as a result.

**State of the A37 jobs.** No A37 job is running. `logs/alldone3` reads ALLDONE (16:13 CDT). The outputs are:
- s = 27, KR = 16 (15:36): (+,+) rank 1 with an Eisenstein part, (−,−) rank 2, genus lifts add 0.
- s = 29, KR = 16 (15:37): the same pattern.
- s = 25, KR = 16 (16:13): (+,+) rank 1, (−,−) rank 2, genus lifts add 0.

Nothing was killed.

---

## 1. Contradictions between reports (numbers, claims, constants)

| # | Where | Conflict | Severity / resolution |
|---|---|---|---|
| C1 | A34 §2.3 table and A36 verdict table, against A34 §3.3 | The tables give dim S(ρ_s) at s = 27 and 29 as "certified [3,4]" or "3 or 4". A34 §3.3 says the (+,+) certificates never finished at s = 27 or 29, nor did (−,−) at s = 29, and adds "the upper bound 4 at s = 27 is not certified either". | **Real.** Only **dim ≥ 3** is certified at s = 27 and 29, which is how ledger v5 entry 23 states it. The "≤ 4" is not certified. |
| C2 | A36 §3 text vs A36 table and ledger entry 29 | The text says "All **12** eigen-systems pass". The table has **15** rows (1+2+3+3+3+3), and ledger 29 says 15 × 8 tests. | Typo-level, but it is a numeric contradiction. 15 is correct. |
| C3 | A32 §2 | "the spectrum allows up to **37** matched unknowns". With ρ₃₅ multiplicities (1, 2×5, 4×6) and every matching eigenvalue of multiplicity 1 in ρ_7\|W, the count is Σ m₃₅·m_W = **35**. | Minor arithmetic error. The conclusion (vanishing forced by S) is unaffected. |
| C4 | A32 §2 "each with multiplicity 1 there" vs `results.json` | This is true for the 12 ρ₃₅ eigenvalues. But ρ_7\|W (42-dim) has 36 distinct T-eigenvalues, 6 of them doubled: 19, 31, 59, 111, 131 and 139 /140. These are exactly the C eigenvalues q + 1/4, so spec(C) ⊂ spec(E). | Consistent once spelled out. A35 "36 distinct on E" is fine. Worth one sentence in the ledger, since it is why T alone cannot separate C from E. |
| C5 | A33 S-law weight x⁻¹ vs A35 / ledger 39 \|x\|⁻¹ | The signed form fails for x < 0 (A35 floatcheck, error 2). | A35 already corrected it. A33 is stale. |
| C6 | Zero counts: A39/A40/A41/A44 "#zeros" vs A42/A43 Z(k) | k = 7: 24 vs Z = 23. k = 11: 43 vs Z = 40 (the A42 prereg itself quotes "k = 11 has 43 zeros"). | **Definitional.** A39–A44 count every allowed zero, including forced ones. A43's primary Z excludes zeros with no contributing n, and Zlit (16, 25) excludes single-contributor zeros too. These are three different statistics under one word. |
| C7 | A42 §2.1 "forced nonzero" premise | False: φ_n(2) = 0 for n ≥ 2. | A43 AMENDMENTS already corrected it. §3.2 below shows the same mechanism is systematic, not a one-off. |
| C8 | A42 §4 P3.3 null | It reads "class-group structure of the relevant **imaginary** quadratic orders". K_s = Q(√(s(s−2))) is **real** quadratic. | Wording error in a retired prereg. No effect on the outcome. |
| C9 | η for k = 7: ledger entry 75 (0.2272, worst block class 2 = 0.7727328) vs A39/A40 (0.27687 via the universal block, R = 0.7231290) | Both are valid bounds. The ledger carries the weaker one, and A40 verified the stronger one. | Stale ledger value (see S3). |
| C10 | T(D₇): A39 table −6.80 vs A39's own JSON −6.776 (A40 B4) | Also η rounding: A39 prints 0.39749 and 0.06397, while A40 truncates to 0.39748 and 0.06396. | Documented in A40. Any downstream use should take the A40 values. |
| C11 | A36 s = 11 "ring-class character of **order 4**" | The sampled ψ(𝔭) orders for that system are only 2 and 1, because no sampled prime lies in a class of order 4. A43 D7 then entered "4 (ring)" as data. | Order 4 is **inferred** from Cl ≅ Z/4, not observed. The sampled orders are lower bounds (divisors). |
| C12 | Ledger 8 wording vs A11 §140 and A31 §2 caveat | Ledger 8 says the original W, E, C "reduce to C[D] … vanishing statements transfer". A11 states that E0 = E_A10 beyond s = 18 was only **observed numerically**. Entries 2, 4 and 10 explicitly use E := ρ-span(δ₀). | Possible scope overstatement in entry 8. It should say "with E := ρ-span(δ₀)", or cite where E0 = E_A10 is proved. |
| C13 | The "35-component law vector" vs dim V = dim E = 36 | No contradiction. 35 = \|D(A_7)\| labels per candidate family. Each of K2, K3 and K4 has only 12 independent orbit functions, and V = span(K2 ∪ K3 ∪ K4) = 3·12 = 36 = dim E = 3G(35). | The name is misleading: no single 35-vector spans V. Suggest the name "law module V (36-dim, from 105 symbols)". |
| C14 | Ledger numbering | A34 cites v1 entry numbers (14, 17, 23, 24), which are v5 entries 14, 18, 24 and 25. | Cross-reference hazard. Any future citation should give the ledger version. |

## 2. Stale or inconsistent status labels

| # | Item | Current label (where) | Should be |
|---|---|---|---|
| S1 | A37 §5 "s = 27 and s = 29" | Empty placeholder `<!-- S2729 -->`. CHECKPOINT says "s = 27/29 pending". | Finished. KR = 16: (+,+) 1 Eis, (−,−) 2, mixed 0, genus adds 0, at both s. |
| S2 | A37 §2: "s = 25 (5−,23−) 1 (KR = 10)" and "A KR = 16 control rerun at s = 25 was not done" | stale | Done (16:13 CDT). Rank 2 = certified 2, genus adds 0. The coverage explanation is confirmed. |
| S3 | Ledger v5 §7 (title "g_7 parity dominance"; entries 73–78) | Only k = 7, η = 0.2272, "one independent audit", certificate to 10⁷ | Missing, all audited: A39 + A40 (odd k = 3..15, η_7 = 0.27687), A41 + A44 (k = 17..25 at N1 = 1500, certificate to 6·10⁷), R1 independently re-derived (A44), the even-k ONE/MIX criterion (A41 + A44), and the pairing identity. |
| S4 | A39 "not independently audited" | A39 | Audited by A40, VERIFIED. |
| S5 | A41 Verdict 4 and §5: "not independently audited" | A41 | Audited by A44, VERIFIED (A44 C4). |
| S6 | A38 / ledger 75: R1 "audited once, inherited" | A38, A39, A40 | Re-derived from first principles and reimplemented (A44 §1). |
| S7 | A39 §4: "1 − c_k ≍ √(2 log k/k)" listed as Cat B | A39 | Proved (A41 §2, verified A44 §4). |
| S8 | A41 Cat A: "max_a min_u F = c, c² = L(z)/k" | A41 §1 and §5 | Cat A only for the **critical value** of F_k. The max–min identification is numerical (A44 gap C1). A42 AMENDMENTS records this correctly. |
| S9 | A33: V ≅ E and K1 ≡ 0 as Cat B | A33 | Cat A (A35). |
| S10 | A32: "Open: the B3 law vector, which has never been built" and "No B3 law vector exists anywhere" | A32 §1, §5 | Superseded. Candidates were built in A33, and the module was made exact in A35. |
| S11 | A31: entry 7 "may be upgraded to P-rel F1–F5, IC by A31" | A31 | Ledger v5 entry 7 carries the proof, but no status tag. Harmless, but the IC marker is lost. |
| S12 | A40 T(D_15) thin margin "T = −0.011" | A39 | A40 passes k = 15 with η_t = 10⁻², T = −2.14. That would allow η_15 = 1 − 0.8860341 − 0.01 ≈ **0.10396** instead of 0.06396. *Not stated as proved here:* I did not rerun the truncation, so this needs one confirming run. |
| S13 | A42 prereg "Status: PREREGISTRATION ONLY" and maps M1–M3 | A42 | Retired per §7 after the negative A43 run. The prereg should carry a pointer to A43. |
| S14 | Ledger 76 range 10⁷ | Ledger | A38 says 10⁸ and 10⁹ certificates exist. A39/A40 have two-prime certificates to 2·10⁷ for k = 7. Not wrong, only conservative. |

## 3. Missed or under-reported variables

1. **N1 cutoff (CLT start).** η_k is not a function of k alone.
   - At N1 = 900, η falls from 0.397 (k = 3) to 0.064 (k = 15). At N1 = 1500, k = 17 gives 0.169, higher than k = 15.
   - The ratio η_k/(1 − c_k) is 0.73, 0.67, 0.61, 0.52, 0.44, 0.36 and 0.17 for k = 3..15 (N1 = 900). It is 0.46, 0.40, 0.34, 0.27 and 0.20 for k = 17..25 (N1 = 1500). It resets when N1 changes.
   - So the A39 statement "the proved η_k decreases with k" is confounded with N1. k = 3..15 have not been run at N1 = 1500.
2. **Box width H and tail allowance η_t.** A40 shows a finer H (0.0005) lowers every R_k by 0.003–0.009, and the closed-form Φ1 tail removes the need for η_t = 5·10⁻² at k = 15. The tabulated η_k are therefore artefacts of the chosen (N1, H, η_t, window), not best constants.
3. **KR (column range) in A37.** KR = 6 and KR = 10 undercount the (−,−) rank at s = 25: rank 1 against the true 2. KR = 16 recovers 2 at s = 25, 27 and 29. Rank is a lower bound, so KR saturation at s = 27 and 29 is *assumed*, not shown. A KR = 20 spot check would bound it.
4. **Sampled primes (8) for character orders.** These give lower bounds, i.e. divisors of the true orders.
   - At s = 29 (3+,29+), no sampled prime is principal, so the ring-class test is incomplete (A36 says so).
   - At s = 11 (ring) the observed order is 2, and the "order 4" is inferred (C11).
   - At s = 25 the two ring-class pairs cannot be told apart on the sample (A36 §3).
   - A43 M3 used these as data: harmless (H₀), but the cell was underpowered by construction.
5. **Squarefreeness of k, and primality** (new, §4.3). These control the largest zero L(k) almost completely. The variable was never conditioned on in A39–A43. The A42 null "X uniform on [1, X_max]" is therefore misspecified for L. That was harmless, because the outcome was H₀ anyway.
6. **Forced-zero convention** (C6). This was not fixed across reports.
7. **Exact range vs T(k).** For k ≥ 61, T(k) sits at the 2·10⁶ edge (A43 caveat). A41's fit of T ~ k^{3.7} used k = 7..25 only. See §4.1.
8. **Upper-bound certifier inputs (M = 6, Q = 40).** These are fixed across every dim S(ρ_s) certificate. The [3, ?] brackets at s = 15, 17, 27, 29 and 31 might move with M and Q. This was never varied.
9. **The single prime ℓ in A36 eigenvalue tests.** The false-pass probability is ≤ 10⁻⁷ per test (stated). One more ℓ would make the tests independent of that estimate.
10. **The s ≤ 51 scope of dim V = s(s−1).** Entries 14 and 25 are restricted to it. Predictions in §4.4 at s ≤ 51 stay inside that scope.

## 4. Patterns tested on existing data (light computation)

Scripts: `scripts/cl_struct.py`, `gk_patterns.py`, `gk_more.py`, `last_zero.py`, `last_zero2.py`. Outputs: `cl_struct.json`, `gk_patterns.json`, `gk_more.json`, `gk_rows.json`, `last_zero*.json`.

g_k data: 499 odd k, namely 3..999 from A43 (exact to 2·10⁶, zero sets matched to a two-prime certificate to 2·10⁷), plus A39/A41 for k ≤ 25.

**Look-elsewhere: 21 pattern tests were run in total** (listed in §4.6). Bonferroni at family-wise 0.05 gives a per-test threshold of 0.0024.

### 4.1 T(k) = last allowed d with E_d ≥ O_d: no stable power law, step structure (evidence)
- A refit on k = 7..25 reproduces A41's exponent: 3.66.
- Out of sample (k = 27..59, where T < 1.9·10⁶), observed/predicted runs 0.93, 0.87, 0.81, 0.76, 0.71 (k = 27..35), then jumps to 0.97 (k = 37), decays to 0.79 (k = 45), jumps to 1.00 (k = 47), and decays to 0.82 (k = 59).
- A refit over everything gives exponent 3.30. **A41's "k^{3.7}" is range-dependent** (Cat B claim weakened).
- √T(k)/k is piecewise smooth with jumps at k = 7, 13, 21, 37 and 47. The plateau values are about 2.2–2.7, 4.8–5.7, 7.9–9.2, 11.6–14.0, 17.1–18.1 and 21.1–23.2.
- **Strength:** clear in the data, since it is monotone within blocks. **The mechanism is unknown.** Preregistration-worthy: the next jump lies at some k in 61..79, which would need an exact range of about 5·10⁶.

### 4.2 Zero counts (evidence; mostly explained by construction)
- Z(k) (A39-style count) tracks |Q_k|: Spearman 0.999. log Z ≈ 1.89 log|Q_k| − 0.23 log k.
- Prime vs composite residual: Mann–Whitney p = 0.025. **Not significant** after correction.
- Zeros concentrate in classes with few square roots: mean zeros per class are 511, 56, 58, 24, 21 and 8 for 1, 2, 3, 4, 5 and 6 roots.
  - Non-unit classes hold 59 % of zeros against 34 % of classes (p ≈ 10⁻⁴⁸).
  - Class 0 for prime k holds 5 % of zeros against 0.45 % expected.
  - **Expected by construction:** fewer contributing n means fewer terms to cancel, and more forced zeros. This is not a new phenomenon.
- Parity of zero positions: 50.0 % even (p = 0.47). Null.

### 4.3 Largest zero L(k): two structural zeros (Cat A, elementary, proved here; not independently audited)
**Fact used.** ∏_{j≥1}(1 + x^j)⁻¹ = (x; x²)_∞ has coefficients c₀..c₆ = 1, −1, 0, −1, 1, −1, 1. For n ≥ m, φ_n(m) = c_m. Among m ≤ 400, the only zero coefficient is c₂ (exact computation).

**(i) Squarefree odd k ≥ 3: g_k(k(k+2)) = 0.**
- *Proof.* Put d = k² + 2k. Then (k+1)² > d, so the contributing n satisfy n ≤ k and k | n². Since k is squarefree, k | n, so n ∈ {0, k}.
- The two terms are φ₀(k+2) = 0 and φ_k(2) = c₂ = 0. ∎
- **Data:** 403/403 squarefree k have this zero, and 0/96 non-squarefree k do.

**(ii) Prime k ≥ 5: g_k((k+2)² − 3) = 0.**
- *Proof.* Put d = k² + 4k + 1 ≡ 1 (mod k). The roots of n² ≡ 1 are n ≡ ±1, and n² ≤ d gives n ∈ {1, k−1, k+1}.
- The terms are φ₁(k+4) = (−1)^{k+4} = −1, φ_{k−1}(6) = c₆ = +1 (this needs k − 1 ≥ 6, and k = 5 is checked directly), and φ_{k+1}(2) = 0. The sum is 0. ∎
- **Data:** 165/165 primes 7 ≤ k ≤ 997 have this zero, and so does k = 5.

**Consequences (evidence on top of the lemmas).**
- For 215 of 403 squarefree k, L(k) = k(k+2) exactly.
- For every prime k (167/167), L(k) > k(k+2). In 74 of the primes above 50, L(k) = (k+2)² − 3 exactly.
- Only 21 of 236 composite squarefree k have L > k(k+2), and every one of them is divisible by 3 or 5 (Fisher p ≈ 10⁻⁹⁰ for prime vs composite).
- **Implications:**
  - "L(k) ~ k^{1.75}" and "L ≈ k²" are artefacts of these isolated-coefficient zeros.
  - A42/A43's L statistic mostly measured k(k+2).
  - The A41 prereg P1 ("all zeros < 2000") must fail for every squarefree k ≥ 45 by construction.
- **Preregistration-worthy:** define L*(k) as the last zero that is *not* explained by a single vanishing c_m term, and test it instead.

### 4.4 dim S(ρ_s) vs class groups of O = Z[√(s(s−2))] (evidence; one discriminating point)
I computed the wide class group structure for odd s = 5..51 (A36 code, read-only).

**A36's post-hoc formula h − |Cl²|, tested out of sample on certified dims not used in its fit:**
- It matches at s = 5, 7, 13 and 19.
- It is consistent with the brackets at s = 15 and 17 (it predicts 3, and the bracket is [3,4]).
- **It fails at s = 21:** it predicts 6, but the certified dim is 5 (ledger 21, which assumes Γ(1596)-invariance via Wohlfahrt). Cl(O₂₁) ≅ Z/2 × Z/4.

**Alternative formula found here, post hoc (the second formula tried): (h + |Cl[2]|)/2 − 1**, i.e. the number of non-trivial characters of Cl(O) up to conjugation.
- It fits all 10 certified values (s = 5, 7, 9, 11, 13, 19, 21, 23, 25 and the s = 15/17 brackets).
- It agrees with h − |Cl²| whenever Cl is cyclic with |Cl[2]| = 2, so **s = 21 is its only discriminating data point**.
- Its "character" reading is also **not** literal. At s = 25 the observed split is (ring, ray) = (1, 2), not (2, 1). The count matches; the composition does not.
- **Strength: weak** (two formulas tried; one discriminating point, which carries an extra hypothesis).

**Preregistration-worthy predictions:**

| s | 33 | 35 | 39 | 41 | 45 | 47 | 49 | 51 |
|---|---|---|---|---|---|---|---|---|
| h − \|Cl²\| | 6 | 7 | 6 | 9 | 6 | 9 | 4 | 9 |
| (h + \|Cl[2]\|)/2 − 1 | 5 | 7 | 5 | 7 | 5 | 7 | 4 | 7 |

The two formulas are distinguishable at s = 33, 39, 41, 45, 47 and 51. Both predict 3 at s = 27, 29, 31 and 37.

### 4.5 Other tests
- **Character orders (A36, 8 primes):** the maximum sampled order equals exp(Cl(O)) at s = 9, 11, 23, 25 and 29, but not at s = 27 (3 vs 6). 5/6, but the samples are lower bounds, so this is weak.
- **Cross-family (s ↔ k):** I took the residuals of log Z(k) and log L(k) against log k and compared them with h(4k(k−2)) for odd k ≤ 51. Spearman −0.12 (p = 0.56) and −0.11 (p = 0.61). **Null:** no s-family/g_k link is visible.
- **T vs L after detrending in k** (k ≤ 59): Spearman 0.01 (p = 0.95). Null.
- **d_k (last η-violation)/T(k), k = 3..15:** 3.7, 3.3, 1.2, 2.2, 2.0, 1.1 and 1.1. Irregular, with no pattern.
- **η_k vs 1 − c_k:** see §3.1. The ratio is confounded with N1.
- **Genus lifts:** at every s run (9..29), "genus-only" rank equals the lift + Hecke rank in every sector. Consistent with A37. That this is forced at s = 27 and 29 is not proved.

### 4.6 Look-elsewhere tally (21 tests)
1. T power-law out of sample.
2. T step structure (post hoc, from test 1).
3. Z vs k / |Q_k|.
4. Z prime vs composite.
5. L vs k².
6. The k(k+2) zero.
7. The (k+2)² − 3 zero.
8. L > k(k+2), prime vs composite.
9. Zeros in non-unit classes.
10. Class-0 zeros for primes.
11. Zeros per class vs root count.
12. Parity of zeros.
13. η vs 1 − c_k.
14. d_k/T.
15. T–L partial correlation.
16. Z residual vs h.
17. L residual vs h.
18. h − |Cl²| out of sample.
19. The (h + |Cl[2]|)/2 − 1 fit.
20. Character order vs exp Cl.
21. spec(C) ⊂ spec(E) check.

Of these:
- **Passing Bonferroni and not trivially explained:** tests 2, 6, 7 and 8. Tests 6 and 7 are now proved, and test 8 is largely explained by them.
- **Explained by construction:** tests 3, 9, 10 and 11.
- **Null:** tests 4, 12, 15, 16 and 17.
- **Weak / low-n:** tests 18, 19 and 20.

## 5. Recommended next tests (preregister first)
1. **dim S(ρ_s) at s = 33 or 39** (a single sector suffices) to discriminate the two class-group formulas of §4.4. Also re-examine s = 21, the only discriminating point: does it hold without the Wohlfahrt hypothesis?
2. **The upper bound at s = 27 and 29.** Finish the (+,+) and (−,−) certificates, or vary M and Q. Until then, change "[3,4]" to "≥ 3" in A34 and A36.
3. **T(k) jumps.** Run an exact E/O to 5·10⁶ for k = 61..79, with the predicted jump location preregistered.
4. **N1 decoupling.** Rerun the k = 3..15 PD proofs at N1 = 1500, finer H and closed-form tails, to obtain best η_k and to test whether η_k/(1 − c_k) is smooth in k at fixed N1.
5. **L*(k).** Restate the zero statistics excluding single-coefficient zeros (§4.3), and generalise lemmas (i) and (ii) to every "one live term with c_m = 0 or two cancelling terms" pattern.
6. **Character data.** Sample more split primes, including principal ones at s = 29, and a second ℓ.
7. **A37 KR = 20 spot check** at s = 27 (−,−).
8. **Ledger v6.**
   - Add A39–A44 (audited) and the two lemmas of §4.3 after an independent audit.
   - Update η_7 to 0.27687.
   - Fix entry 8's scope wording.
   - Add the spec(C) ⊂ spec(E) remark.
   - Fix A36's "12 → 15".

## Category summary
- **Cat A (new here, elementary, not yet audited):** the zeros g_k(k(k+2)) = 0 for squarefree odd k, and g_k((k+2)² − 3) = 0 for prime k ≥ 5.
- **Cat A (checks):** spec(C) ⊂ spec(E) at s = 7 (from A32's exact spectrum), and the class-group structures of `cl_struct.json`. The latter are exact via reduction cycles (A36 code).
- **Evidence:**
  - the T(k) step structure;
  - the range-dependence of the k^{3.7} fit;
  - the L(k) vs primality/squarefreeness statistics beyond the lemmas;
  - the class-group formula fits;
  - the character-order pattern.
- **Conjecture:** none is asserted.

## Files
- `REPORT.md`, `REPORT.pdf`, `mk_pdf.py`
- `scripts/`: cl_struct.py, gk_patterns.py, gk_more.py, last_zero.py, last_zero2.py
- Outputs: cl_struct.json, gk_patterns.json, gk_more.json, gk_rows.json, last_zero.json, last_zero2.json
