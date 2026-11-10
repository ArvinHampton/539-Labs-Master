# FINDINGS — PP audit of NL Y14 stage 2 and Y15 (fibre Israel), MN2 odd HW-type wall
Auditor: PP (Professor Proof), Soft SF audit agent. Pure math. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Refutation only by proof or counterexample. Nothing adopted, no CERT, nothing sent, no agent messaged, no Gemini. This is a new file; no existing file was edited.
Nomenclature (OW 81b74a31 / f1d167d1): "resonant algebra" where needed; no affected names occur below.
Junction authority: OW 90cec14c = OWNER_WRITE_MAINCHAT_t4415_PURSUE_S4_BREATHING_MODE_JUNCTION_2026-11-09_1906.md, sha 90cec14c1ccbeba5743f64d735c690c3bd8849c080158ac895ccd88516196ff2. I checked it: the file matches its sidecar. It is a GO, not an adoption. NL cites OW 9bb1858c instead (OWNER_WRITE_VOICE_11fd320e_PURSUE_NL_E8_OPEN_PATHS_Y14_Y15_TRR2_NEC_2026-11-09_1805.md, sha 9bb1858c…ff27c, which also matches its sidecar). Both are valid authorities. Citations are allowed with the math checked (OW 36683379).
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, checked at the start and again at write time. It is unchanged.

## 0. Inputs and provenance
| file | sha256 | sidecar | mtime (CST) |
|---|---|---|---|
| NL_DERIVED_Y14_NONBPS_E8_EXISTENCE_MN2_STAGE2_2026-11-09_1950.md | 5e079f4aa6d5ea5a3a84f9f9f66abb249fd432b0af849e94e4cc3c6c494f2ebd | MATCH | 19:43:50 |
| …STAGE2_2026-11-09_1945.md (draft) | 100a70d7… | MATCH | 19:43:33 |
| NL_DERIVED_Y15_FIBRE_ISRAEL_MN2_2026-11-09_1955.md | 86a46df7… | MATCH | 19:44:43 |
| /workspace/nl-junction-1851/*.py, *.log | all sidecars | MATCH | all sidecars written 19:44:53 |

- **Draft status.** The 1945 draft has no void marker inside it. The only supersession notice is in the 1950 file. A diff shows the two differ only in the Q0 step-3 formula and the tally block. Supersession by a later file is acceptable under the additive rule, but a reader who opens 1945 alone cannot tell it is superseded (fix N1).
- **Filename times.** All three NL filename times (1945, 1950, 1955) are later than the files' own mtimes (19:43:33, 19:43:50, 19:44:43). Each name is post-dated by 2 to 10 minutes (fix N2).
- **Frozen-before-run.** This is not satisfied. Every script and log sidecar was written at 19:44:53, after the runs. These are integrity sidecars only, not freeze sidecars (fix N3).
- **Unreferenced artefacts.** stab_q0.log, stab_q0_run.log, stab_q0_run2.log, stab_q0_run3.log and q0_newton.{py,log} are present and sidecarred, but neither NL file cites them (fix N4).

## 1. PP reruns (scratch /workspace/pp_nl_2000)
- **y15.py rerun.** y15_rerun.log (sha d3021873…65fb) is byte-identical to NL's y15_run.log, apart from my appended exit line. That gives 398 faces, and I2 fails at every grid point on all 398.
- **n = 1 twisted IR solution rerun** (e1.py 59f4e434…, e1.log 0f5a84b5…). Status 0, rms 9.8e-9. Results:
  - e = 1.1743083885 and e_u = 1.0660516672. Both match NL's table to every printed digit.
  - The twist part is e_tw = 0.0594520.
  - The weighted Bogomolny residual is **bog = 0.013081 ≠ 0**.
- **c value.** From flowlin.fixed(1), g₀ = −0.62383246, X_a = 0.65975, X_b = 1.31951, so r = X_b/X_a = 2.0000000. Then c = (2e^{g₀})^{−4} = 0.7578582832551991, and 2^{−0.4} = 0.757858283255199. T4 is confirmed.
- **T-check log** (run_bign_Tcheck.log). At n = 20, 80, 110 and 160, the T=12 and T=16 runs agree to ≤ 3e-8 relative, both with status 0. The log also contains T=22 runs with **status 1** (not converged), and the file does not mention them (fix N5).
- **postproc arithmetic.** I re-did it by hand from run_ir_bign.log. Every (A)–(D) bracket is correct for u = 1 and u = 2. One case looked like a slip but is not: (C) "> 160" for u=1 with e_u. It uses u·e_u(n) − n, and e_u(160) − 160 = 2787.28 < 2808.6, so "> 160" is correct.
- **S12′ ratios.** u·e_u/n = 1.0661, 1.1442, 1.2292, 1.3200, 1.4155. These match NL, and the crossing of 1.288 is at n = 4.

## 2. Independent derivations (priority a: Y15 I1, I2, signs, trace)
Conventions are mostly-plus. T_MN = tr(F_MP F_N^P) − ¼g_MN tr F² with a positive-definite trace, and ε = ¼F_MN F^MN (= ½|F|² in form norm, NL's convention).
- **YM blocks.** Take a static wall field with **no x-legs**, fibre legs F_f and Σ legs Φ·F_tw.
  - T^x_x = −¼(F_f² + F_Σ²) = −ε_f − ε_Σ.
  - In 2D, F_ac F_b^c = ½δ_ab F_Σ². So T^Σ_Σ = ½F_Σ² − ¼(F_f² + F_Σ²) = ε_Σ − ε_f.
  - T^i_j = τ^i_j − ε_Σ δ^i_j, where τ is traceless.
  - All three agree with NL §2.
- **I1 in general form.** For any field with no x-legs, T^a_a − T^x_x = |F(e_a,·)|² ≥ 0 for each Σ unit vector e_a. Mixed Σ–fibre legs only add a non-negative amount. Smeared M5s, S = −σP_wv, are isotropic on x ⊕ Σ and cancel. So I1 is PROVED **given no x-legs**.
- **Counterexample to I1 without that hypothesis.** Let F have only the component F_{x¹y}, with y a fibre direction. Then T^Σ_Σ − T^{x¹}_{x¹} = −|F(x̂¹,·)|² < 0.
  - So I1 needs 4D Poincaré invariance of the wall field. That hypothesis is enough: on R^{1,3} there is no invariant 2-form or vector, so F_{μν} = F_{μi} = 0.
  - NL does not state this hypothesis (fix N6).
- **I2.** For null ℓ = t̂ + ê, T(ℓ,ℓ) = F(ℓ,·)·F(ℓ,·) ≥ 0 for **every** YM field, x-legs included, because F(ℓ,·) is orthogonal to the null vector ℓ and so is spacelike or null. In NL's variables: ε_f + ε_Σ + τ(ê,ê) − ε_Σ = |F(ê,·)|². The M5 term is −σP(ℓ,ℓ) = −σh_tt = +σ. So I2 is PROVED for σ ≥ 0, with no symmetry hypothesis needed.
- **Required values.** Use S^a_b = −(2/κ²)(K^a_b − δ^a_b K) with K^x_x = k_x = −k, K^Σ = K^fib = 0 and K = −4k on the IR face.
  - This gives S^x_x = −6k/κ², S^Σ_Σ = S^fib = −8k/κ², so S^Σ_Σ − S^x_x = −2k/κ².
  - It also gives S(ℓ,ℓ) = S_tt + S_ee = 6k/κ² − 8k/κ² = −2k/κ².
  - These match MR2's 6 : 8 : 8, NL Y15-1, and my own smoothed-kink computation (PP aeb9ab13 audit, s = +1: δ-parts −6k and −8k, with WRONG_SIGN giving the opposite).
- **Sign and orientation.** The sign is fixed by the geometry once the **IR side is kept** (NL 1655 P3 / OW f825dfff). It does not depend on a normal-vector convention.
  - If the UV side were kept, every required value would flip. I2 would then be satisfiable, but the wall energy density would be −6k/κ² < 0, which needs σ < 0.
  - So Y15's verdict is scoped to "IR side kept", which is the working premise.
- **Trace.** The fibre trace of the YM + M5 stress is −4ε_Σ, and the required value is −32k/κ², so ε_Σ = 8k/κ². The I1 requirement gives ε_Σ = −k/κ². These are contradictory.
  - This is correct, but it is **not independent** of I1: it uses I1's required value. I1 alone already forces ε_Σ < 0 (fix N7).
- **Unifying corollary (PP, PROVED).** NEC along ℓ_v = t̂ + v requires k_v ≤ k_x for every unit wall-spatial direction v, Σ and fibre directions included. For E₈ fields, I1 is exactly the Σ case of this. At the MN2 IR face, k_Σ = k_fib = 0 > k_x = −k at every point of S⁴. So every NEC-satisfying wall content fails there, with margin k.

## 3. Priority b — weighted e vs unweighted e_u
- **Measure.** Fibre metric (L₇/2)²Δ̃^{−2/3}ĝ gives dvol₄ ∝ Δ̃^{−4/3}dvol_ĝ, and the fibre ε ∝ Δ̃^{4/3}|F|²_ĝ. So ε dvol₄ = |F|²_ĝ dvol_ĝ, which is conformally invariant.
- **Weight.** The x-block and Σ-block volume factors give √h ∝ Δ̃^{(4+2)/6} relative to the fibre, which is W = Δ̃.
- **Twist term.** ε_Σ dvol₄ ∝ Δ̃^{−2}R^{−4}(n−a)² = (weighted twist density)/W.
- **So** NL's "unweighted = weighted/W" (y14s2.py) is exactly e_u = ∫ε dvol₄. T5's two integrals are correctly defined and do differ: **PROVED**.
- **Which one enters is a modelling choice.**
  - The Israel x-equation S^x_x = −ε − σ = −(2/κ²)(k_x − K) holds pointwise on the fibre.
  - Integrating it against **any** positive fibre measure gives a valid necessary condition. With dvol₄ the integrated ε is e_u, as in P3c. With the 10D measure √h, which carries the Σ and x warp factors, it is e. A 4D-units version would also carry the x-warp, (wF₀)² as in PP aeb9ab13.
  - "e_u is what enters" is therefore true **relative to P3c's choice of measure**. It is CONDITIONAL on that choice, and it is never sufficient, because the obstruction is pointwise.
  - NL already places this inside S11-count (CONDITIONAL on P3c). PP agrees, but the T5 wording should say "is what enters P3c's dvol₄-integrated count" (fix N8).

## 4. Priority c — MP2, S11-real, S2-2, Q0
- **MP2 (PROVED, agree).** Mutually commuting SU(2)s have commuting, independent Cartan generators, so there are at most rank E₈ = 8 of them. Spin(16)/ℤ₂ ⊂ E₈ contains Spin(4)⁴ ⊃ SU(2)⁸, which realizes 8. Each has index 1 (16 → 2·**2** + 12·**1**). So there are at most 4 decoupled mirror pairs.
- **S11-real (REFUTED, agree, scoped).** The proof (MP2 + S5) refutes stage 1's ≳10³ independent unit pairs **as a sum of decoupled commuting SU(2) blocks with additive energy**.
  - S5 (PROVED in stage 1, agreed in PP 5374a906) gives U(1)_{φ₁}-equivariance only. "Each SU(2) block is one equivariant connection **of one charge**" holds in the SO(3)×U(1) ansatz (S4-applied (a)).
  - A U(1)-equivariant connection inside one block can carry several separated (anti-)instantons, for example centred on the U(1)-fixed S². Such configurations are not exact block sums and are not covered by the refutation. They fall under Q0-out and ST2, which are OPEN.
  - The refutation stands for the stated additive-pair description. NL's phrase "more than 4 separate pairs cannot occur" must say "as decoupled commuting blocks" (fix N9).
- **S2-2 (NL: PROVED → PP: CONDITIONAL; there is a gap in the proof).** NL argues "the twist sources D(W⋆F_fib) ≠ 0 wherever Φ ≠ 0, so the solution is not self-dual".
  - Self-duality gives D⋆F = 0, but D(W⋆F) = dW∧⋆F is not zero, because W = Δ̃ is not constant on the MN2 fibre (X_a ≠ X_b).
  - So "D(W⋆F) ≠ 0" does not contradict self-duality. What has to be excluded is a self-dual F for which dW∧⋆F exactly cancels the twist source. The argument does not exclude that.
  - The claim is supported numerically: PP's rerun gives Bogomolny residual 0.01308 ≠ 0 at n = 1. It is not proved for every n ≥ 1 (fix N10).
- **Q0 (PROVED within the ansatz, agree).**
  - Step 1: multiply by a and integrate by parts. This needs the boundary term [2Baa′] to vanish. That holds because a ~ t² at the S² orbit (from the BC a′t₀ = 2a) and a → 0 at the S¹ orbit, but NL does not say so (fix N11).
  - Step 2: I re-derived dE/dℓ = h_ℓ(h_ℓℓ + U′) = −(ρ_ℓ/ρ)h_ℓ². If h(0) = ±1, E is constant and h is constant. This is correct.
  - Step 3: I verified dρ/dχ = X_b(1−2σ) + X_a(2σ + σ/(1−σ)) = X_a f(σ). The minimum −q + 2√(2q) ≥ 0 holds iff q ≤ 8 (r ≤ 9). r = 2 at the IR point, and r ∈ [1, 2] on the flow. Correct.
- **Other stage-2 items.**
  - T1, T2, MP1: PROVED, agree. For T2, deg K_Σ = 2g−2 and Area(H²/Γ) = 4π(g−1) = 2π(2g−2) at K = −1.
  - T3 and S4-applied: CONDITIONAL, agree.
  - T4: PROVED, agree. The c value is verified, and the twist-term power of W is consistent with §3.

## 5. Priority d — numerics, and u-normalisation
- **Float-only numerics.** Everything runs in float64 with scipy solve_bvp, tolerance 1e-7 to 1e-8. There is no mpmath and no interval arithmetic. So S2-1, S2-3, S2-c, S11-count, S12′, ST1 and Y15-int are correctly graded CONDITIONAL.
- **Y15-int overstatement.** The 398-face scan in y15.py counts **only I2** (`bad += all(max_e k_e − k_x > 0)`). I1 is evaluated only on the 9 listed faces.
  - NL's text "on all 398 sampled faces … **both** necessary conditions fail at every S⁴ grid point" overstates what was computed. Only I2 was checked on all 398 faces.
  - The verdict still stands, because I2 alone excludes every face (min margin +2.01×10⁻² ℓ_P⁻¹) (fix N12).
  - A 120×60 grid is not "every point of S⁴", so the label stays CONDITIONAL.
  - Analytically, at the UV, k_fib → 0 and k_x → −1/L₇, so the margin tends to 1/L₇ > 0, consistent with the numerics.
- **ST1.** The lowest discrete Hessian eigenvalues are 5.8×10⁻⁵ to 3.8×10⁻⁴, at N = 4000. These are small enough that discretisation error or near-zero modes cannot be ruled out without an N-sequence (fix N13). CONDITIONAL, agree.
- **u-normalisation.**
  - S7-type e/n values are u-free. Counts carry 1/u and are given for both u = 1 and u = 2.
  - Every count line in postproc.log (A, B, C, D) and the UV line 6506.7/(2u) scale correctly with u.
  - The (C) single-block criterion u·e(n) − n is correct: the block charge n offsets n M5 units.
  - Y15-R2's "2–5 units (1.1–2.4 at u=1, twice at u=2)" against 4189.5 is short by ~10³ under either u. Agree.
  - Stage 1 fix 1 (both u values reported) is complied with.

## 6. Grade table
### Y14 stage 2 (20 items; S4-abstract is PP's own item and is not counted)
| item | NL | PP | note |
|---|---|---|---|
| T1 | PROVED | PROVED | |
| T2 | PROVED | PROVED | |
| T3 | CONDITIONAL | CONDITIONAL | S3 ansatz |
| T4 | PROVED | PROVED | c = 2^{−0.4} re-verified |
| T5 | PROVED | PROVED | definitions only; "which enters" belongs to S11-count (N8) |
| S2-1 | CONDITIONAL | CONDITIONAL | n=1 reproduced to every printed digit |
| S2-2 | PROVED | **CONDITIONAL** | W non-constant; numerical bog ≠ 0 (N10) |
| S2-3 | CONDITIONAL | CONDITIONAL | undisclosed T=22 status 1 runs (N5) |
| S4-applied | CONDITIONAL | CONDITIONAL | |
| Q0 | PROVED (in ansatz) | PROVED (in ansatz) | boundary term (N11) |
| Q0-out | OPEN | OPEN | |
| MP1 | PROVED | PROVED | |
| MP2 | PROVED | PROVED | |
| S11-real | REFUTED | REFUTED (scoped) | decoupled-block sums only (N9) |
| S11-count | CONDITIONAL | CONDITIONAL | arithmetic re-checked, both u |
| S12′ | CONDITIONAL | CONDITIONAL | ratios re-checked |
| S2-c | CONDITIONAL | CONDITIONAL | |
| ST1 | CONDITIONAL | CONDITIONAL | N13 |
| ST2 | OPEN | OPEN | |
| Y14 | CONDITIONAL (OPEN overall) | CONDITIONAL (OPEN overall) | |

### Y15 (8 items)
| item | NL | PP | note |
|---|---|---|---|
| Y15-1 | PROVED | PROVED | 6:8:8 and −2k/κ² re-derived |
| I1 | PROVED | PROVED | needs no x-legs / 4D Poincaré; counterexample otherwise (N6) |
| I2 | PROVED | PROVED | holds for any YM field, σ ≥ 0 |
| Y15-trace | PROVED | PROVED | not independent of I1 (N7) |
| Y15-IR | REFUTED | REFUTED | by I2 alone; scope is IR side kept, σ ≥ 0 |
| Y15-int | CONDITIONAL | CONDITIONAL | 398-face scan is I2 only (N12) |
| Y15-R2 | CONDITIONAL | CONDITIONAL | |
| J7-src | OPEN | OPEN | |

## 7. Rollups
| file | NL P/C/O/R | PP P/C/O/R | change |
|---|---|---|---|
| Y14 stage 2 | 8 / 9 / 2 / 1 (20) | **7 / 10 / 2 / 1 (20)** | S2-2 PROVED → CONDITIONAL |
| Y15 | 4 / 2 / 1 / 1 (8) | **4 / 2 / 1 / 1 (8)** | none (wording fixes only) |
| combined | 12 / 11 / 3 / 2 (28) | **11 / 12 / 3 / 2 (28)** | |
PP-own items (not part of NL's rollup):
- PP-NEC corollary, k_v ≤ k_x: PROVED.
- I1 counterexample with x-legs: PROVED.
- y15 rerun byte-identical: PROVED.
- Provenance (N1–N4): findings, not grades.
PENDING: 0.

## 8. Numbered fixes for NL
1. **N1.** Make the 1945 draft's supersession discoverable on its own. Add a new dated pointer file, or list it in an index. Do not edit the draft.
2. **N2.** Filename times must not be later than the actual write time. State the real write times (19:43:33, 19:43:50, 19:44:43) in a new erratum.
3. **N3.** Describe the 19:44:53 script and log sidecars as post-run integrity sidecars, not frozen-before-run. Future runs should freeze the .py sidecar before execution.
4. **N4.** Cite or disclaim stab_q0*.log (run, run2, run3) and q0_newton.{py,log}.
5. **N5.** Disclose the T=22 status-1 rows in run_bign_Tcheck.log.
6. **N6.** I1: state the hypothesis "no x-legs (4D Poincaré invariance of the wall field)", and give the general form T^a_a − T^x_x = |F(e_a,·)|². Note that I2 needs no such hypothesis.
7. **N7.** Y15-trace: drop "independent". It uses I1's required value, which already forces ε_Σ < 0.
8. **N8.** T5: change "e_u is what enters the integrated 4D Israel tuning" to "e_u is what enters P3c's dvol₄-integrated count". Note that any positive fibre measure gives a valid necessary condition (e for √h, an x-warp-weighted version for 4D units), and none is sufficient.
9. **N9.** S11-real: scope the refutation to decoupled commuting-block sums with additive energy. State that multi-centre U(1)-equivariant configurations within one block are not covered (Q0-out / ST2).
10. **N10.** S2-2: downgrade to CONDITIONAL, or supply a proof that rules out dW∧⋆F cancelling the twist source for a self-dual F. Cite the Bogomolny residual (0.01308 at n = 1) as numerical support.
11. **N11.** Q0 step 1: state that the boundary term [2Baa′] vanishes (a ~ t² at the S² orbit, a → 0 at the S¹ orbit).
12. **N12.** Y15-int: correct "both conditions on all 398 faces" to "I2 on all 398 faces; I1 on the 9 listed faces". Optionally extend the scan to count I1.
13. **N13.** ST1: report the lowest Hessian eigenvalues for an N-sequence (e.g. 2000/4000/8000), and identify any near-zero modes.
14. **N14.** Cite OW 90cec14c (t4415, S⁴ breathing-mode junction) next to 9bb1858c, since Y15 is the junction criterion that a breathing-mode candidate has to meet.

## 9. What Y15 means for the junction (OW 90cec14c), in plain terms
- At the odd HW-type ℤ₂ wall on the MN2 IR face (IR side kept), the Israel equations demand wall stress with **negative null energy**: S(ℓ,ℓ) = −2k/κ² for every null direction t̂ + v along Σ or the fibre.
- Every E₈ Yang–Mills field (any charge, single blocks, mirror pairs, twisted or not) and every positive-tension smeared M5 has non-negative null energy. **So no combination of them can close the junction.** This is a pointwise statement, so no count of pairs or tension total changes it. The stage-2 "count gap closes in magnitude" result does not help.
- The HW tr R² term is the only listed ingredient that can be negative. On the integrated bound it is ~10³ too small. A per-direction check is still owed (Y15 §7).
- The usable criterion for any candidate under OW 90cec14c, including the S⁴ breathing mode, is the PP corollary in §2:
  - **with NEC-respecting wall content, the face must satisfy k_v ≤ k_x pointwise for every Σ and fibre direction v.**
  - The unperturbed MN2 IR face has k_Σ = k_fib = 0 > k_x = −k everywhere.
  - So a breathing-mode solution must make the fibre (and Σ) extrinsic curvature at the wall at least as negative as the x-block's, on all of S⁴.
  - Otherwise the wall must carry a NEC-violating source: σ < 0 M5s, G₄ / worldvolume flux contributions of the right sign, or a tr R² stress far larger than Y16's bound.
  - The alternatives are a different face, or keeping the UV side (which needs negative wall energy).
- The junction status is **UNSOLVED**, with J7-src OPEN. Y15 is a proved no-go for this class of wall content, not a statement about the junction in general.

Tip at write time: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged).
Scratch: /workspace/pp_nl_2000 (e1.py 59f4e434…, e1.log 0f5a84b5…, y15_rerun.log d3021873…).
