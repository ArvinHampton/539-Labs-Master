# PP audit: five MR2 files under OW t4436 (erratum 4c618493, register c5a65972, batch-2 04b94770, batch-1 3da6285a, L1-everywhere db06bd2c)
Written 2026-11-09 2219 CST by Professor Proof (Soft SF audit). New additive file in reports/. Nothing was written into MR2's directories, and nothing is adopted. Authority: OW t4436 (32881263…), d5eaeef3, b0b9ae7f, 8b26c786, 90cec14c. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Exact tests only (polynomial reduction, factor, Sturm count, minimal_polynomial, or mpmath.iv); no simplify==0. Tip 7cddb188… was re-hashed at 22:18 CST and is unchanged.

## 1. Integrity
- **All five reports have sha = sidecar:** 4c618493515b ✓, c5a6597232da ✓, 04b947700136 ✓, 3da6285a9685 ✓, db06bd2ce15c ✓.
- **/workspace/mr2-branch-2134/:** all 33 *.sha256 sidecars match (15 .py, 15 .log, 3 .pkl). Every .py sidecar predates its log. L1_Nprime_roots has py 22:08:04.417, sidecar .421, log .817, so it was frozen before its run.
- **R_closedform_…_2142.log.sha256.pre_append = 96c3b633…** does NOT match the current log (43c8be31…). This is expected and honestly disclosed in 04b94770: the first sidecar hashed the "KILLED" note, then the surviving process overwrote the log (log mtime 21:47:57 > pre_append 21:44). That log contains only an AssertionError (EXIT 1) and one float line ∂R/∂r = ∂R/∂y ≈ 0. It supports no exact claim. r, y independence is PROVED independently below.
- **Disclosed post-run sidecars:** sym_R_probe_v2 .log, and the R_symbolic*.pkl sidecars (21:57; the pkls are from 21:34/21:37). No graded claim rests on them.
- **Script-name times run ahead of mtimes.** For example, Phi_bounds_"2156" was frozen at 21:52:23, before Phi_bounds_v2_"2154". This is disclosed; the mtimes are authoritative.

**Frozen-script shas (sidecar = actual):**
- sym_R_probe 61cd2b86…
- sym_R_probe_v2 eebd9400…
- R_closedform 14625779…
- R_mu_chart 486c1c2d…
- G2_R7_slice 2a66fdfd…
- G2_R7_slice_v2 5a6d4659…
- Phi_bounds 84ac46e4…
- Phi_bounds_v2 0d61743d…
- R_monotone_and_Rc_arith 76831625…
- L1_trRR_interval 7fee50e3…
- L1_trRR_validate_v2 9fa27766…
- L1_trRR_validate_v3 9f79038d…
- TW_null_energy 19abe063…
- L1_everywhere_symbolic 2f2b9d4f…
- L1_Nprime_roots 16859a5c…

## 2. PP independent exact recomputation
All in /workspace/audit-scratch/pp_branch5_2215/. This is PP's own Christoffel/Riemann engine. The metric is transcribed from the 516438eb ansatz (X₁ = c⁻³, X₂ = X₀ = c², F = c⁻⁴, G_s = c/4, a₁ = 1, a₂ = 0), with c = 2^{1/5} and d = Δ^{1/3} kept as symbols. The chain rule for d is done by hand, and the final reduction is exact modulo d³ − Δ and c⁵ − 2. Both are irreducible (Eisenstein; Δ is not a cube in ℚ(c)(u,v)), so {1, d, d²} is a basis.

Scripts:
- pp_eng.py 03a6ce2d
- pp_R11v3.py 65a5b392 / log 0b02f77b. Earlier versions crashed on Groebner generators (pp_R11) and on a print (pp_R11v2); the crash logs are kept.
- pp_checks2.py a8283d1c / log e7b807d1
- pp_L1_TW2.py 5eed0a44 / log b62caad3

Results:
- **[R11] Closed form: PROVED.** R₁₁ depends only on (c, d, u); there is no r, y or μ₂. num·d¹⁰ − P(p)·den reduces to **exactly 0** modulo (d³ − Δ, c⁵ − 2), with P = −p³ + (20/3)p² − 16p + 40/3 and p = μ₁². The value at (α, β) = (1/3, 2/7) is 5.5514551029130873154036783611, which matches 516438eb.
- **[M] Monotonicity and range: PROVED.**
  - dR/dp = 2^{−4/3}(1−p/2)^{−13/3}·(2−p)(3p² − 20p + 56)/18. The quadratic has discriminant −272 < 0, so dR/dp > 0 on [0, 1].
  - MR2's form 18Q = −3p³ + 26p² − 96p + 112 is the same polynomial.
  - R(0) − 10·2^{2/3}/3 has minimal polynomial x, and R(1) has minimal polynomial x − 12.
  - Interval checks: Φ range [0.3086655162769, 0.7000095264011] ℓ_p⁻²; ratio 9·2^{1/3}/5 = 2.2678578898.
- **[G2] R₇, exact closed form.** Both R₇ (induced) and R₇ (warp-stripped) depend on μ₁ only. The rigorous iv values (rationals entered as iv quotients, width < 10⁻⁴⁶) are:
  - (t-i): 30.750104268171, 34.073693574140, 28.754465257859, 37.331278617912
  - (t-ii): 20.832967805384, 26.223114927042, 17.692042512638, 31.654689250989
  - All exclude 0 and all equal MR2's values.
- **[L1] Pontryagin component on F₁₀, own Riemann.**
  - P_{x y v φ₁} ≡ 0.
  - P_{x y u φ₁}·y² is y-free, and (P_{xyuφ₁}|_{y=1} − 2μ₁N′/D) reduces to **exactly 0**, with MR2's N′ and D = c·d⁹(p−2)²(c³d⁶ + 4d³p + c⁷p²).
  - iv values: −1.161192993378910693119… at (1,1,1/3,1/4), and −2.105789254477301124531… at (1,1,1/2,−1/5).
- **[N′]** −½(p−2)(p+2)²(p²+4p−6) expands exactly to MR2's hand expansion. Real roots are −2−√10, −2 (double), −2+√10 and 2. The Sturm count on [0, 1] is 0. N′(0) = −24·2^{4/5} and N′(1) = −(9/2)·2^{4/5}.
- **[TW]** iv values of k_s, R_kk^bulk(ê_y), the margin at ε = ℓ/2, and the threshold:

  | point | k_s | R_kk^bulk(ê_y) | margin | threshold |
  |---|---|---|---|---|
  | (1/3,1/4) | 1.271981 | 3.045526 | −1.021199 | 0.835311ℓ = 41.50 ℓ_p |
  | (9/10,1/10) | 1.373801 | 1.205353 | −2.144925 | 2.279500ℓ = **113.26 ℓ_p** |
  | (1/10,9/10) and (1/10,1/10) | 1.260974 | 3.164131 | −0.939883 | 39.60 ℓ_p |

  All reproduce MR2. Note that R(ê_y, ê_y) on its own is negative (−2.54, −8.24); only the null sum R_kk is positive, which is all the NEC needs.
- **[Rc]** iv, with κ ∈ [1.5976222, 1.5976225] (OW 45aeba5f definition) and ℓ = 2(4880π)^{1/3}:
  - kε ∈ [**0.0405133**, 0.0454746]; at k = 1/L₅ it is 0.0424293.
  - (L₅/R_c)² ∈ [555.47876, 555.47897].
  - The largest computed m·R_c is √(84/555.479) = 0.38887.

## 3. Per-claim verdicts

### File 1: 4c618493 (erratum: SV per PP 3f1749e1, BPS per PP 5abd02c6). **CONFIRMED**
- All seven 3f1749e1 fixes are applied faithfully:
  - A1: tally 10/3/2/0 = 15
  - A2: D3 text
  - A3: row 7 as implication
  - A4: split 11a PROVED / 11b COND (as a sub-statement, so it stays at 15 rows; acceptable)
  - A5: BF bound saturated, PROVED in the truncation; the full-spectrum statement stays COND
  - A6: df ⊕ *dg decomposition PROVED, 23.0786 COND, 5D masses OPEN
  - A7: χ decoupling listed as a premise
- R1–R3 match 5abd02c6 §fixes verbatim in substance.
- The NL E20 (6b10854d ✓) and PP 2252cafc (✓) fold-ins are faithful: Z1 PROVED; Z2 OPEN; E20-7 scoping; D6-6 with c = 2^{4/3}g and slaving (1/5, 13/30)w² at leading order, existence by the cited centre-manifold theorem.
- There are no new math claims. The header time 21:35 vs mtime 21:30:47 is self-flagged in the register.

### File 2: c5a65972 (register). **CONFIRMED with flags**
- Every option has a label, a status, a keep/drop criterion (directly, or through the general rule in line 11) and conflicts listed.
- **Definitional rulings** (DPa-*, DPb-*, L2-1/2/4, Rc-3, G2-1, P-3: "math does not choose"): **fair.** Each is kept as viable, with well-definedness or consistency PROVED where claimed, and the drop route (inconsistency with adopted data) is stated in line 11. None is dropped by fiat.
- L2-3 is not purely definitional: it is OPEN pending a target definition, which is an Owner input. That is acceptable as written.
- **Flag: c2.**
  - B1-c2 is kept as a labelled branch (listed under Viable/OPEN). "Conflicts with Group A" is a scope conflict (OW 8b26c786 is a choice), not a REF. So the listing is not a drop.
  - However, the row has no keep/drop criterion and no next computation ("—"). MR2 itself is unsure whether the standing "no c2 work" refers to this item.
  - Under t4436, parking indefinitely without a criterion amounts to a **de facto drop by fiat**.
  - Fix: give it a criterion, e.g. keep = cases (i′)/(ii′) of 8399be55 re-derived on doubled MN2 with r ∈ Isom(Bolza) \ Aut⁺; drop = an inconsistency proof. Mark it "parked pending an Owner ruling on whether t4436 lifts 'no c2 work'". Settling that referent is an Owner question, not MR2's.
- The priority list is ordered by cost, not by preference. ✓

### File 3: 04b94770 (batch 2)
| claim | MR2 | PP |
|---|---|---|
| T3-1 closed form R = P(p)/Δ^{10/3} | PROVED (given S) | **PROVED** (exact reduction; S = smooth extension from the μ₀ > 0 chart, plus the μ₀ → −μ₀ isometry) |
| r, y independence | PROVED | **PROVED** (isometries; and the exact R has no r, y) |
| T3-2 monotone; range [10·2^{2/3}/3, 12] | PROVED | **PROVED** (factor (2−p)(3p²−20p+56) > 0; minimal polynomials) |
| 4b-ii Φ range | COND → PROVED | **PROVED** as a statement about 144R/ℓ². Reading it as G·G stays COND (K1 on shell). |
| 4c R_max = 12 | COND → PROVED | **PROVED** |
| T3-3 Φ-3 EH lock | REF | **REFUTED (PROVED)**: k²ℓ² ∈ [2^{2/3}, 2] ∌ 1 |
| T3-4 Φ-2 EH lock | REF | **REFUTED (PROVED)**. Needs R̄ ≥ 12·2^{2/3} = 19.0488 while R̄ ≤ 12, for any positive weight. Premise: k is in the stated AdS₅ warped-radius family. Float R̄ values COND. |
| T3-5 W-2 finite | PROVED (implication) | **PROVED** (implication of K1 on shell plus compact M₆); value COND |
| T3-6 W-3 diverges | REF | **REFUTED** as finite without a cutoff (PROVED). It uses ‖G‖² = 6R > 0, i.e. K1 on shell; state that premise in T3-6. |
| T3-7 G2-2 (t-i), (t-ii) torsion-free | REF | **REFUTED** (implication): R₇ ≠ 0 is PP-certified exactly. The premise is the standard fact G₂ ⊂ Spin(7) fixes a spinor, so a parallel spinor gives Ric = 0; MR2's sketch is correct. (t-iii) is **OPEN**. |
| T3-8a Rc-1 kε | PROVED arith. | **PROVED (arithmetic, PP interval-certified).** The interval is **[0.040513, 0.045475]**; MR2's lower end 0.04052 is rounded the wrong way (see fixes). Reading it as "thin wall" is COND. |
| T3-8b Rc-2 cutoff 555.479; all computed modes below | PROVED arith.; masses COND | **PROVED arithmetic** ([555.4788, 555.4790]). As KK masses it is **COND**. |
| Φ̄ values, W-2 value, Rc-2 as KK masses | COND | **COND** |
- **Tally sentence:** garbled, as self-flagged. Read it as **8/3/1/4 = 16**; PP agrees.

### File 4: 3da6285a (batch 1)
- **Routine validation: PROVED.** R ∈ [5.55145510291308731540367836112…] ✓ (this log prints at dps 40).
- **L1 tr R∧R ≢ 0 on F₁₀: PROVED.** The interval evaluation itself is sound (rationals go to iv.mpf). However, the L1 log **prints its endpoints through mp.mpf at the default dps = 15**, so the quoted 20 digits are double-rounded. "−1.16119299337891068720" is wrong from digit 17 on: the true value is −1.161192993378910693119. The claimed "width < 10⁻³⁰" is not shown in the log. The sign is unaffected, and PP's exact closed form supersedes this evidence.
- **F ≠ 0 required: PROVED**, given HW (tr F² = ½ tr R²).
- **Lemma TW: PROVED as an implication.** P-i and P-ii are explicit ✓. Two further premises are used but not listed as premises, and should be named P-iii: (a) the null Einstein equation κ²T_kk = R_kk of two-derivative 11D supergravity holds inside the wall; (b) 4-form flux stress satisfies the NEC. The proof steps check: product Ricci split; R̂(t̂,t̂) = A_ss + 4A_s²; the ĝ_ab term drops on null k; ∂_ρω = 0 with no internal Γ̂^m_tt; ∫A_ss = −2k_s; P-ii makes the A_s² term ≤ 0.
- **Numbers table: PROVED** (PP rigorous iv reproduction).
- **2b as an NEC escape (fixed internal metric): REFUTED**, as an implication of P-i, P-ii and P-iii.
- The threshold "≈ 113 ℓ_p" is the **proper width at (μ₁, μ₂) = (9/10, 1/10)**. Proper width varies with z for a fixed coordinate width, so say so.
- **OPEN:** 2b identification ε_y = R_S4; L1 "everywhere" (now split in file 5).
- Self-flags (ii) (log label) and (iii) (batch-2 tally): confirmed.
- **Tally: 4/0/2/1 = 7; PP agrees.**

### File 5: db06bd2c (L1 everywhere)
- **E1: PROVED** (PP exact reduction to 0). Fix: the component carries a factor **y⁻²** (P·y² is y-free), so MR2's formula is the y = 1 value. The **first D expression is garbled** ("2^{3/5}Δ^{2/3}·Δ^{4/3}…"). The correct form is D = 2^{1/5}Δ³(p−2)²(2^{3/5}Δ² + 4Δp + 2^{7/5}p²) = 2^{1/5}d⁹(p−2)²(2^{3/5}d⁶ + 4d³p + 2^{7/5}p²); MR2's "exactly" line is correct. P_{xyμ₂φ₁} ≡ 0 is confirmed.
- **E2: PROVED.** The N′ factoring is exact (PP expand; Sturm count 0 on [0, 1]), and D > 0 on [0, 1]. MR2's factoring step was hand-checked, and its frozen L1_Nprime_roots run is consistent. Coverage gap to state explicitly: the chart only covers μ₀ > 0. μ₀ < 0 follows from the μ₀ → −μ₀ isometry. At μ₀ = 0 with 0 < μ₁ < 1, switching to the chart (μ₁, μ₀) leaves the dx∧dy∧dμ₁∧dφ₁ coefficient unchanged because P_{xyμ₂φ₁} ≡ 0. The μ₁ = 0 Cartesian argument holds ✓.
- **E3 (vanishing on {μ₁ = 1}): COND.** This is fair: 208 components were not checked symbolically.
- **Tally: 2/1/0/0; PP agrees.**

## 4. PP tally (new claims in files 3–5; files 1–2 make no new math claims)
| file | PROVED | COND | OPEN | REF |
|---|---|---|---|---|
| 04b94770 | 8 | 3 | 1 | 4 |
| 3da6285a | 4 | 0 | 2 | 1 |
| db06bd2c | 2 | 1 | 0 | 0 |
| **total** | **14** | **4** | **3** | **5** |

Total = 26. Carried unchanged: ff7fb67f 10/3/2/0 = 15; BPS 14/2/1/1 = 18.

## 5. Anything refuting MR2
**No graded claim is refuted.** Two small numeric errors are refuted by computation:
- **(a)** The Rc-1 lower endpoint: kε_min = 0.0405133 < 0.04052 as stated. Use [0.04051, 0.04548].
- **(b)** The 20-digit L1 interval values quoted in 3da6285a: digits past ~16 are print artifacts of dps 15.

Neither changes a label.

## 6. Fixes for MR2 (additive erratum)
1. 04b94770 T3-8 / register Rc-1: change kε ∈ [0.04052, 0.04548] to **[0.04051, 0.04548]**. Add "PP interval-certified".
2. 3da6285a: re-quote the L1 values as −1.16119299337891069312… and −2.10578925447730112453…, or quote only 15 digits. Note that the L1 logs print at dps 15, so the width claim is not shown there; the closed form db06bd2c supersedes them.
3. 3da6285a lemma TW: add **P-iii** (null Einstein equation inside the wall, and flux NEC) as a premise. State the 113 ℓ_p threshold as the proper width at (9/10, 1/10).
4. db06bd2c E1: add the y⁻² factor. Replace the garbled first D expression with D = 2^{1/5}Δ³(p−2)²(2^{3/5}Δ² + 4Δp + 2^{7/5}p²).
5. db06bd2c E2: state the chart coverage (μ₀ → −μ₀ isometry; the μ₀ = 0 chart switch using P_{xyμ₂φ₁} ≡ 0).
6. 04b94770 T3-6: state K1 on shell (‖G‖² = 6R) as the premise. T3-7: state the G₂ ⊂ Spin(7) spinor-stabilizer fact as a standard premise.
7. 04b94770 tally: replace the garbled sentence with "PROVED 8 · COND 3 · OPEN 1 · REF 4 = 16" (as already self-flagged).
8. Register B1-c2: add a keep/drop criterion and a next computation. Mark it "parked pending Owner ruling on whether t4436 lifts 'no c2 work'", so the parking is not a drop by fiat.
9. Register: update the statuses of Φ-2, Φ-3, 4b-ii, 4c, W-2, W-3, G2-2 (t-i/t-ii), 1b-ii L1 and 2b to the PP grades above; the current text is from before batch 2.

**Verdict:** All five files are confirmed, subject to the fixes above. The closed form, range, monotonicity, R₇ ≠ 0, the L1 closed form and N′, the TW numbers and the Rc arithmetic are all independently reproduced exactly. Nothing is adopted, and the junction is UNSOLVED.
