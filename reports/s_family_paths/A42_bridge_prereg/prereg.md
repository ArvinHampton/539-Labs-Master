# A42 preregistration: a falsifiable bridge test between RNT and the residual side

**Owner:** Arvin Hampton (539 Labs) · **Drafted:** 2026-10-22, America/Chicago (CDT) · **Status:** PREREGISTRATION ONLY

`SF/` = `/workspace/quantum-comp/reports/s_family_paths/`. `OM/` = `/workspace/quantum-comp/oct17-master/` (the 539-Labs master repo copy on the box). New files only in `SF/A42_bridge_prereg/`.

> **Nothing has been computed for this preregistration.** No prediction below was evaluated at 539 or at any control. The drafter did not open A39/A40 zero lists, A37 output files, or any A41 result file (only the A41 `prereg/prereg.md`, which existed before this draft). The few facts in §2.3 are elementary residue arithmetic used to discard empty test cells; they are not outcomes.
>
> **Residual-vs-Resonant lock stays in force.** RNT and the residual side do not support each other unless a test below passes under the stated criteria. This document defines a test; it does not claim a link. No RH or TPC claims are made or implied. H_s is not redefined. No certifier code is touched or run by this test.

## 1. Fixed inputs (quoted, not re-derived)

### 1.1 RNT, Category A core
- `OM/docs/S2-11DM2ET-X-Axiomatic-Book/NonCircular_18_plus_521.md`: L_pref = ⌊e³/ln 3⌋ = 18, L_body = ⌊N_flux/9⌋ − 21 = 521, N_flux = ⌊e³·3⁵⌋ = 4880, so 18 + 521 = 539 (canonical derivation pointer: `Foundational_Arithmetic_Packaging.md`).
- `OM/README.md` (lines 44, 86–87): 539 is an engineered hard iteration budget under Principle (S); L_body = 521; L_pack = 18 + 521 = 539. Not a free-map stopping time.
- `OM/docs/S2-11DM2ET-X-Axiomatic-Book/N4_540_Harmonic_Ladder_2026-08-16.md`: 540 = 539 + 1, ladder Category A as trivial arithmetic; 0.1 s offset Category B.
- `SF/../heavy-daily/heavy-615919d3-n1n6-latest.md` (= `/workspace/quantum-comp/reports/heavy-daily/…`), N3: 539 = 7²·11, φ(539) = 420, ord_539(3) = 210, "ordinary arithmetic of (Z/539Z)*", no Category A link to (S). N4: sub-harmonics {5, 10, 15, 30, 45}, super-harmonics {1080, 1620, 2160, 2700, 5400}.
- `/workspace/quantum-comp/reports/self-audit/SELF_AUDIT.md` line 50: 3·68 + 5·67 = 539, 18 + 521 = 539, 539 = 7²·11.

### 1.2 Residual side, Category A core
- g_k(q) = Σ_{n≥0} q^{n²}/(−q^k;q^k)_n, E_d, O_d as in A38–A40. `SF/A39_gk_family/REPORT.md`, audited in `SF/A40_gk_audit/REPORT.md`: for odd k = 3..15, E_d ≤ (1−η_k)O_d for d ≥ D_k, hence OccFilt_k(∞) = {squares mod k}, with finite listed zero sets (A40 table: k = 7 has 24 zeros, last 247; k = 11 has 43 zeros, last 273).
- Even k = 2, 6, 10, 14: all classes ONE, elementary. MIX classes open: k = 4 c = 0; k = 8 c = 1; k = 12 c = 0, 4.
- `SF/A37_dihedral_count/REPORT.md`: the visible dihedral count d_dih(s) equals the proved dim S(ρ_s) at s = 9, 11, 23, 25.
- W = E(36) + C(6): two-way Z-parity split. The ternary {−1, 0, +1} is **not** tied to the E/C split.
- `SF/RTA_prereg/`: earlier RTA tests. P1 failed (no map found); P4 passed only generically.
- Concurrent: `SF/A41_uniform_oddk/prereg/prereg.md` (k = 17..25; theta / eta-quotient / Appell–Lerch origin of the squares pattern; c_exp(k)²/π² rationality via PSLQ).

## 2. Definitions fixed now

### 2.1 Objects
- Q_k = {x² mod k}. For odd k, g_k(d) ≠ 0 forces d mod k ∈ Q_k, so the allowed classes are Q_k.
- **Forced zero.** An allowed d is a forced zero of g_k if there is no n ≥ 0 with n² ≤ d and n² ≡ d (mod k); these are zeros by construction. **Forced nonzero.** Exactly one n contributes, so g_k(d) = ±φ_n(·) ≠ 0. Z*_k = the set of allowed zeros of g_k that are neither forced zeros nor forced nonzeros (i.e. nontrivial zeros).
- Statistics per k: **Z(k)** = |Z*_k|; **L(k)** = max Z*_k (0 if empty); **T(k)** = last allowed d with E_d ≥ O_d.
- RNT target set (frozen): **R** = {5, 10, 15, 18, 30, 45, 210, 420, 521, 539, 540, 1080, 1620, 2160, 2700, 5400}. |R| = 16. A "hit" for an integer statistic X is X ∈ R.

### 2.2 Exact range and certification
- Exact integer E/O (pure Python, A40 `eo_indep.py` logic, copied, not edited) to d ≤ 2·10⁶ for every k used; two-prime mod-p certificate (A40/A41 `gcert.c` logic, copied into this folder, primes 2⁶¹−1 and 10¹⁸+3) to d ≤ 2·10⁷.
- A statistic is **Category A** for a given k only if a dominance bound E_d ≤ (1−η)O_d for d ≥ D_k is proved (A39 method) with D_k ≤ 2·10⁷. Otherwise it is **finite-range** (evidence only), and L(k), Z(k) are reported as "in [1, 2·10⁷]".

### 2.3 Design facts (residue arithmetic only, used to discard empty cells)
- |Q_7| = 4, |Q_11| = 6, |Q_49| = 22, |Q_77| = 24, |Q_539| = 132.
- 18 mod 539 and 521 mod 539 are **not** in Q_539, so g_539(18) = g_539(521) = 0 by construction. Every "18 or 521 is a zero of g_539" test is empty and is excluded.
- 521 ∉ Q_7, 18 ∉ Q_11, 18 ∉ Q_77, 521 ∉ Q_77, 521 ∉ Q_49. Excluded.
- 18 at k = 49 is a forced zero (d < 49, 18 not a square). Excluded.
- 540 ≡ 1 mod 49, 77 and 539; only n = 1 contributes for d = 540 at k = 49, 77 and 539 → forced nonzero. Excluded.
- 521 at k = 11 and 540 at k = 7, 11 lie above the audited last zeros (273, 247), so they are already Category A nonzeros. Excluded (no new information).
- ord_539(2) = ord_539(3) = ord_539(5) = 210 = λ(539) (the Carmichael exponent), and ord_539(10) = 42. So 210 is the generic maximal order mod 539, not specific to the base 3. Any order-based map must beat the base-2 and base-5 controls (§4.2).
- Smallest s ≥ 3 with 77 | s(s−2): 35, 44, 77, 79. Smallest with 539 | s(s−2): 198, 343, 539, 541.
- E(36) = 2·18 is a pre-existing visible numerical coincidence with L_pref = 18. It is declared **post hoc** and cannot count for any map.

## 3. Declared maps (closed list)

Only these three maps may be used later. Any map not declared here is inadmissible, including reparametrisations (e.g. 539 → 540, 18 → 36, 521 → 520, or a different target set R).

**M1 (modulus map).** RNT modulus 539 and its divisors → the residual family index: k ∈ K539 = {7, 11, 49, 77, 539}. Cells use only k ∈ {49, 77, 539} (k = 7, 11 are already audited and serve as anchors). The question is whether the residual statistics at 539-divisor levels carry RNT integers more often than at matched non-539 levels.

**M2 (schedule map).** The 18 + 521 split → membership in the nontrivial zero sets Z*_k, k ∈ K539. After §2.3 only one live cell remains: **"18 ∈ Z*_7"**.

**M3 (order map).** ord_7(3) = 6, ord_11(3) = 5 (factors of ord_539(3) = 210 via λ) → the orders of the Hecke / ray-class characters χ whose theta lifts span the dihedral part of S(ρ_s) in A37, at s with 7 | s(s−2) (s = 9, 23) or 11 | s(s−2) (s = 11). s = 25 (575 = 5²·23) is the internal control.

## 4. Predictions (exact; link hypothesis H₁ against null H₀)

### M1 predictions
- **P1.1 (generic pattern, not a link).** OccFilt_k(∞) = Q_k for k = 49, 77, 539. Expected under both H₀ and H₁. Logged as a pipeline check only; it **cannot** count toward a link.
- **P1.2 (link).** H₁: at least one of Z(k), L(k), T(k) for k ∈ {49, 77, 539} lies in R. H₀: hit rate equals the control hit rate (§5).
- **P1.3 (link, A41 branch; see §6).** Branch I only: the identity A41 finds for odd k has, at k ∈ {49, 77, 539}, a level or character conductor whose 7- or 11-part is exactly the 7- or 11-part of 539 times the generic factor that A41's identity predicts for all odd k. H₁ requires a *non-generic* extra factor: the identity at k = 539 has level or order divisible by 210 while the formula's generic value at k = 539 is not. H₀: the level equals A41's generic formula.

### M2 prediction
- **P2.1.** H₁: 18 ∈ Z*_7. H₀: 18 ∉ Z*_7 at the base rate |Z*_7| / #(non-forced allowed d ≤ 247) for k = 7. This is a single cell; even a hit has p ≥ that base rate and can never reach the threshold alone (§7). Declared so the map is closed, not because it has power.

### M3 predictions
- **P3.1.** H₁: the set of dihedral character orders at s = 9 contains 6, and at s = 23 contains 6.
- **P3.2.** H₁: the set at s = 11 contains 5.
- **P3.3 (control).** H₁ requires that s = 25 contains neither 5 nor 6 as character orders. Under H₀ the orders are set by class-group structure of the relevant imaginary quadratic orders, independent of 3.
- M3 has at most four s values with proved dims, so it **cannot** reach the significance threshold (§7). Any M3 outcome is evidence only.

## 5. Null models and coincidence probability

### 5.1 Integer controls for M1 (stand-ins for the 539 divisors)
- **Shape-matched k:** for k = 49: p² with p odd prime, p ≠ 7, p² ≤ 999 (9, 25, 121, 169, 289, 361, 529, 841, 961). For k = 77: pq, p < q odd primes, p, q ∉ {7, 11}, pq ≤ 999. For k = 539: p²q and pq², p ≠ q odd primes, p, q not both in {7, 11}, k ≤ 999.
- **Random-integer controls (539 replaced):** 20 odd N in (400, 700) with ≥ 2 distinct prime factors and 3 ∤ N, drawn with Python `random.Random(20261022).sample`, sorted: 403, 415, 437, 445, 451, 455, 473, 475, 485, 493, 511, 515, 533, 595, 611, 623, 665, 667, 671, 689. For each N the whole pipeline is rerun with 539 → N, k ∈ {divisors of N} ∪ {N}, R → R_N (18 → 18, 521 → N − 18, 539 → N, 540 → N + 1, 210 → ord_N(3), 420 → φ(N), ladder → multiples of N + 1 by the same factors).
- **All odd k pool:** every odd k in [27, 999] not dividing 539 (≈ 485 values), finite-range statistics only, for the empirical hit-rate distribution.

### 5.2 Order controls (M3 and P1.3)
- Replace 3 by 2, 5 and 10 (ord_539 = 210, 210, 42), and replace ord_7(3), ord_11(3) by ord_7(2) = 3, ord_11(2) = 10. An order-based hit must occur for base 3 and fail for these controls to count.

### 5.3 Coincidence probability and look-elsewhere correction
- For each cell c, statistic X_c, the p-value is p_c = (1 + #{controls with a hit in the same statistic}) / (1 + #controls), using the all-odd-k pool for P1.2 and the random-integer controls for the R_N version.
- Cells are counted over **all** declared maps: P1.2 (3 statistics × 3 values of k = 9 cells), P1.3 (1), P2.1 (1), P3.1–P3.3 (3). Total m = 14.
- Family-wise α = 0.05, Bonferroni: per-cell threshold α_c = 0.05/14 ≈ 3.6·10⁻³. With 485 pooled controls the smallest attainable p is ≈ 2.1·10⁻³, so only M1 cells can pass. That is intended.
- An analytic cross-check for P1.2: if X is roughly uniform on [1, X_max], P(hit) ≈ |R ∩ [1, X_max]| / X_max. This is reported next to the empirical rate; the empirical rate decides.

## 6. Ordering relative to A41 and branching

- A42 runs only **after** A41 has a frozen REPORT. Before running, record A41's REPORT sha256 in `A42_bridge_prereg/AMENDMENTS.md` (a new file, created at run time).
- **Branch I (A41 finds a theta / genus-character / Appell–Lerch identity for odd k):** run P1.3 with A41's identity applied unchanged at k = 49, 77, 539 and at all controls. If the identity is only proved for k ≤ 25, its use at larger k is finite-range evidence for P1.3.
- **Branch II (no identity):** P1.3 is recorded as **not run** (the cell stays in the count m = 14; no reallocation of α).
- In either branch, P1.1, P1.2, P2.1 and P3 run as written. No A41 output beyond its final verdict on "identity found / not found", and the identity itself in Branch I, may affect A42.

## 7. Pass / fail thresholds

- **Cell pass:** H₁ outcome and p_c ≤ 3.6·10⁻³ against the controls, and the same hit does **not** occur for the base-2/base-5 order controls where relevant.
- **Replication:** a passing M1 cell must also pass in a second independent control draw (seed 20261023, same rules), and the hit must appear at two of the three values k ∈ {49, 77, 539} *or* be proved Category A at one of them.
- **Testable link established:** at least one cell passes with replication. Then the lock is relaxed **only** for the specific declared map and statistic. Everything else stays separated.
- **Fail:** no cell passes. The result is reported as "no testable link under M1–M3". Maps M1–M3 are then retired and may not be retried with altered target sets, ranges or controls.
- **Inconclusive:** a cell passes but replication fails, or the Category A requirement for that k is unmet. Reported as evidence only; the lock holds.

## 8. What counts as Category A vs evidence

- **Category A:** exact identities proved for all d (dominance tail proved, finite range certified), exact residue arithmetic, and exact statements about Z*_k, L(k), T(k) for k with a proved tail. A *link* is Category A only if a proved identity ties an RNT invariant to a residual object for a family containing 539 **and** the same identity provably fails for the shape-matched controls.
- **Evidence only:** finite-range statistics, permutation p-values, PSLQ non-detections, any outcome at M2 or M3, any outcome at Branch I's k > 25 without proof.
- **Never counted:** P1.1, the forced zeros and nonzeros of §2.3, E(36) = 2·18, and any map or target not declared here.

## 9. Execution constraints

- Jobs run under `nice`, OMP_NUM_THREADS=1, `ulimit -v` 3 GB. Copied scripts are hashed before the first run; the code git hash or sha256 list goes into `AMENDMENTS.md` before any evaluation at 539.
- Controls go through the identical pipeline, in an order that interleaves them with 539-divisor values so the 539 values are not processed first.
- No existing file is modified, no certifier code is touched or run, H_s is not redefined, nothing is pushed.
