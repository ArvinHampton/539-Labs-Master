# PP AUDIT — MR2 wall Bianchi / J_M5 density filing 79795981 and status note 27c61e09
2026-11-10, written 10:57:57 CST (America/Chicago; this is the write time and equals the file mtime). Author: Professor Proof (PP), Soft SF audit, Project Quantum Comp. Additive file; no existing file edited; MR2's frozen 444 files untouched. **Nothing in this filing is adopted.** Junction **UNSOLVED**. **No CERT.** Wording: resonant algebra.

## 0. Authority and adoption scope
- Owner t433u ("Send report. Then adopt all proved from Professor Proof", OW 3df3878860906386276ce33cecac17019124ae1671b5d2d330709cc0058dcf47; PP confirm eebd7dd7…) covers only results that were already PP-PROVED at that time. This filing was not yet audited then.
- **Every grade in this file, including the PROVED grades PP accepts or upgrades below, stays UNADOPTED** until a later Owner word says otherwise.
- Not adopted: 1a (not as the physical wall), B1-c2′ overall (stays COND), any E₈ candidate as the physical 1a datum (OPEN). 8399be55 stays COND. Group A stays the chosen KK scope. Literal c2 stays REFUTED (scoped). t4436 unchanged for the remaining open paths.
- Lift-existence results for E-0, E-Λ±, E-S± (scoped), E-T (731cef3c / 513fdf49 / dd5a3a25; 7d1f7c80 / e30d8694 / e7bc37a1) are not reopened.

## 1. Integrity
| file | sha256 (= sidecar) | mtime CST | mode | check |
|---|---|---|---|---|
| report MR2_BRANCH_ATTEMPT_BATCH1_C2PRIME_E8_WALL_BIANCHI_JM5_DENSITY_2026-11-10.md | 797959812aeaafc3e1d3c4d59573bc4f315b03936c74121b1138af5c4f877048 | 10:30:58.828 | 644 | header 10:30:58 = mtime ✓ |
| note MR2_NOTE_WALL_BIANCHI_JM5_79795981_WRITE_STATUS_2026-11-10.md | 27c61e0984c30ba0d2ecfc74f6f764e1da59986088ef6d4419f3aecabd6d8cd4 | 10:35:22.599 (sidecar 10:35:22.603) | 644 | header 10:35:22 = mtime ✓ |
| script /workspace/mr2-c2e8-1010/c2p_wall_bianchi_jm5_2026-11-10_1030.py | 2a4339e26c97f3c4ca83db71291418e7e3dd4beaaf9b5c4649bcc1791d0c7336 | 10:24:37.413 (sidecar 10:24:42.853) | 444 | reports/ copy cmp-equal ✓ |
| log /workspace/mr2-c2e8-1010/c2p_wall_bianchi_jm5_2026-11-10_1030.log | ef281a27920832a323e0e61bee572b44b73e38284f40be7b2ec5b37c00837a21 | 10:27:09.825 (sidecar 10:29:48.257) | 444 | reports/ copy cmp-equal ✓ |
| wrapper .exit ("exit 0", 7 bytes) | — (no sidecar) | 10:27:09.993 | 644 | not frozen; nit only |
| V2 routines (exec'd prefix) | ad134752da79e3064e209cd840b0aec53e004e3fa0fec8bbc9299eb12940eb85 | — | — | asserted in-script and in PP checkers ✓ |

**Freeze vs run.**
- The log carries **no wall-clock stamps**, so "run started at or after the 10:24:42.853 sidecar" is **not provable from the log itself**.
- Timing inference (consistent, not proof): the log's own timers total 57 + 4 + 81 = 142 s. PP's re-run of the byte-identical script took 137.54 s wall (10:44:49.52 → 10:47:07.07 CST) against timers 52 + 4 + 79 = 135 s, so the un-timed prefix is ≈ 2.5 s. MR2's run therefore took ≈ 144.5 s, implying a start ≈ 10:24:45 CST, about 2 s after the sidecar and 8 s after the script mtime. Consistent with MR2's claim.
- **Log = complete exit-0 run of that exact script: confirmed.** PP re-ran a byte-identical copy (sha 2a4339e2…, exit 0, empty stderr); every line of PP's output is byte-identical to MR2's log except the five timer values (diff modulo timers: IDENTICAL).

**Tip** /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, MATCH before this audit (10:39) and re-hashed after this write (see sidecar-time line at the end of the report back; untouched by PP).

## 2. PP evidence (new directory, all files frozen 444 with .sha256 sidecars)
Directory: /workspace/quantum-comp/reports/pp_evidence_bianchi_jm5_79795981_2026-11-10/
| file | sha256 | role |
|---|---|---|
| rerun_c2p_wall_bianchi_jm5_copy.py | 2a4339e26c97f3c4ca83db71291418e7e3dd4beaaf9b5c4649bcc1791d0c7336 | byte-identical copy of MR2's script |
| rerun.log | 8336e160e62b5b8ae236af8b2d0ecbd3d2088d705e595d1d72604e8a08e0347a | PP re-run output (identical to MR2 log modulo timers) |
| rerun_timing.txt | ac73db6475ac9bbd122127079444a89948c4129da4f755e8ec898924b4488c03 | start/end/exit of PP re-run |
| pp_exact_checks.py | 749916501cc35e3d9c700703f6f48ec809d5554613b59d4ee10dfa4c37480ede | exact checks C1–C7 |
| pp_exact_checks.log | 00bd3bea5b74eb72e6cba85353c8e5b08f991d599300f47e326d2c19f8a9effc | all True, exit 0 |
| pp_exact_gb_verify.py | f412ff8488b2583a80737d6d6a5ab8ac365c307adba529e0c06987413400b142 | exact Gauss–Bonnet density + polynomial certificate (rational functions, sp.cancel) |
| pp_exact_gb_verify.log | d9228c095de365c341de20a7f34fcb96012502954a25a14b752295b7947ad8db | all True, exit 0 |
| pp_exact_euler_ratio.py | c0b85c5a25fc376ab9302dfa8b8b7c342e74ea9730896be9da9a078b6c210770 | discovery only (sp.simplify); not grounds |
| pp_exact_euler_ratio.log | a3577438de240e44deed700d718fef0208179e0b5d9d8e11c17506320cf764a0 | discovery output |

Exact checks (all zero tests are expand / cancel on polynomials or rational functions, or exact Rational comparisons):
- **C1.** MN2 fixed point: lim X₁⁵ = 1/8 exactly, X₂/X₁ = 2, hence X₀ = (X₁X₂)⁻² = X₂ = p := 2^{2/5}, X₁ = p/2; a₁ = 1, a₂ = 0.
- **C2.** U − p²(s − 4) and D − p(1 − s/2) expand to 0 (s = μ₁², μ₀² = 1 − s − μ₂²). So U ∈ [−4p², −3p²] < 0 and D > 0.
- **C3.** Generic metric of the V2 block shape (AdS₅ diagonal, Σ, fibre (α,β) block, φ₁, φ₂, shifts dφ_k + b_k du): det G = ∏A · S² · det g_fib; row v of G⁻¹ is S⁻¹e_v; det(G^{B,B}) = 1/(∏A·S²) for B = (0..6); every non-ε₇ component of V2's Ω omits index v. Hence (⋆Ω)_{αβφ₁φ₂} receives only the κUε₇ term, and the warp factors give **G₄_{αβφ₁φ₂} = ±κ U D^{−7/6} √det g_fib exactly** (hand: (D^{1/3})^{−7/2}).
- **C4.** V2 cand_metric: g_{φ_k u} = g_{φ_kφ_k} a_k / v (expand), g_{φ₂u} = 0 at a₂ = 0, nonzero pattern {(i,i), (5,9), (5,10), (7,8)}, no φ₁, φ₂, u dependence. So P: φ₂ ↦ −φ₂ is an exact isometry of the 11D metric at MN2, preserving the wall and Y₆; ∂_{φ₁}, ∂_{φ₂} are Killing.
- **C5.** det h = D sin²α μ₁²μ₂² /(X₀X₁²X₂²) (polynomial reduction mod cos² + sin² = 1, generic X's) and X₀X₁²X₂² = 1, so √det g_fib = (1/16) D^{−5/6} sinα |μ₁μ₂|.
- **C6.** ∫_{fibre} G₄_fib (κ = 1) = **−π² exactly** (hand: with x = cos α, t = cos²β, U/D² = 4(s−4)/(2−s)², the double integral reduces to ∫_{−1}^{1}[−2 ln(2/(1+x²)) − 2(1−x²)/(1+x²)] dx = −4; sympy exact integration agrees).
- **C7.** p₁(Λ²±) = p₁ ± 2e as an identity of invariant polynomials, with 36 independent symbols for the six curvature 2-form matrices, using the script's own `ad`, ⋆ and Pfaffian conventions (expand == 0 for both signs); ⋆² = +1 on Λ² exactly.
- **GB (cohomogeneity one).** With X₀ = X₂, h = p⁻¹|dy|²_{ℝ³} + 2p⁻¹|dz|²_{ℝ²}; put |y| = cos θ, |z| = sin θ, c = cos²θ ∈ [0,1], so s = 1 − c, D = (p/2)(1 + c). With W⁶ = 1 + c and p = 2K³ all metric data are rational; the Gauss–Bonnet scalar GB = |Rm|² − 4|Ric|² + R² (Euler density E = GB/32π² per unit volume) satisfies, by sp.cancel == 0,
  GB = −(1024/27) K¹⁰ N(c) / (1+c)^{14/3}, N(c) = 37c³ + 93c² − 25c − 225.
  On [0,1]: −N(c) ≥ 225 − 130 = 95 > 0, so **E > 0 everywhere (exact)**.
  Per unit j, R_j := (e_fib/2)/ρ_J = GB·D^{7/6}/(64·9760·|U|) = √2 (225 + 25c − 93c² − 37c³) / (263520 (1+c)^{7/2}(3+c)).
  Certificate: 75(1+c)³(c+3) − (225 + 25c − 93c² − 37c³) = 725c + 993c² + 487c³ + 75c⁴ ≥ 0 (expand), and (1+c)^{7/2} ≥ (1+c)³, so **sup R_j = R_j(0) = 5√2/17568**, attained exactly on the circle μ₁ = 1 (c = 0). R_j(1) = 1/70272. Both match MR2's scan extremes (4.02497029e-4, 1.42304189e-5), which cross-checks orientation and normalisation.
  Hence the exact adverse threshold is **j\* = 8784√2/5 = 2484.49038637705…**

## 3. Premise Or
- **What it says.** M5 worldvolumes are ℝ^{1,3} × C, and every tangent 2-plane of C has π*vol_Σ ≥ 0; vertical and mixed planes are allowed in either orientation.
- **Status.** Or is a **new premise**. It does not follow from the premises already accepted in cc21b272 and its audits (HW normalisation, twist model, r an involution, ℝ^{1,3}-invariance, unbackreacted wall, fixed SO(3) ⊂ E₈). PP accepts it **as a stated premise**; everything that uses it is graded as an implication.
- **Missing clause (load-bearing).** Or as written fixes "the MN wrapping orientation over Σ" but does not say that this orientation is the one in which ∫_{S⁴} J = +2N. MR2 uses this tacitly ("in the orientation where ∫J_fib = +9760"). With the opposite alignment, (J_M5)_fib = −|ρ_J| < 0 for E-0 and E-T and every positivity result fails. PP writes **Or₊ := Or + (M5 charge sign agrees with the MN flux sign: the Or orientation of Σ has ∫_{S⁴}J = +2N)**. All implications below are of Or₊. Physically this is the statement that the wall M5s are branes, not anti-branes, relative to the MN flux; it is a premise, not proved.
- Or₊ is weaker than BPS/calibrated positivity. Under it, "J_M5 ≥ 0" is exactly the sign of one component.

## 4. Row-by-row grades
| # | item | MR2 | PP | PP grounds / notes |
|---|---|---|---|---|
| 1 | U = −p²(4−s) < 0; G₄_fib = ±κUD^{−7/6}√det g_fib; J_fib nowhere zero | PROVED | **PROVED** (grounds replaced) | C1, C2, C3, C4, C5 exact plus hand algebra. MR2's simplify==0 and the 25-digit two-point Hodge match are **withdrawn as grounds** (corroboration only). "Nowhere zero" holds for the density J_fib / vol_fib = ±κ U D^{−7/6}; the coordinate component vanishes only on the chart degeneracies sin α·μ₁μ₂ = 0. |
| 2 | ∫J_fib = 9760 | PROVED (in-repo) | **PROVED** | C6: ∫G₄_fib = −π² exactly (hand + exact integration), independent of 5511845e; 2N = 9760 is the in-repo wall charge (bd47ff5e / 5511845e). The 2.7e-11 reproduction is not grounds. |
| 3 | under Or, J_M5 ≥ 0 ⇔ (J_M5)_{αβφ₁φ₂} ≥ 0 | PROVED as implication of Or | **PROVED as implication of Or₊** | Hand proof checked: ω ∈ K* vanishes on simple vertical and mixed bivectors, which span Λ²V ⊕ H⊗V, so K* = ℝ_{≥0}·π*vol_Σ; K contains ± that subspace's duals plus one strictly positive element, so K is the closed half-space (no closure gap). Sign identification needs the Or₊ alignment clause. |
| 4 | J_M5 closed; M-s solves the pointwise Bianchi equation by construction | PROVED | **PROVED as implication** | Premise dG₄ = 0 for the MN2 uplift (MN2 as an 11D solution; standing premise, not re-proved; V2's numerical dG check is not grounds). The content is definitional. |
| 5 | P-lemma: natural 4-forms have zero pure-fibre component | PROVED as implication of [M] | **PROVED as implication** | C4 makes [M] exact here (a₂ = 0). Pontryagin forms are natural under every isometry; with ∂_{φ₂} Killing, h(Px) = h(x) and P*ν = ν force h ≡ 0. The Euler form flips under orientation reversal and survives. Log zeros are corroboration only. |
| 6 | Gauss: fibre component of the V_vert curvature = intrinsic fibre curvature | PROVED | **PROVED** | Standard: the tangential projection of the ambient LC connection is the induced LC connection; pull-back of curvature = curvature of the pulled-back connection. g_fib = GC[7:11,7:11] is the induced metric on {u, v const}. |
| 7 | p₁(Λ²±) = p₁ ± 2e at form level | PROVED | **PROVED** (grounds replaced) | C7 exact invariant-polynomial identity. The 8.6e-42 pointwise defect is **withdrawn as grounds**. The GL integrals (2, ±4, 0) are float; they agree with χ(S⁴) = 2 and σ(S⁴) = 0 but are not graded. |
| 8 | E-0: M-s, J_M5 ≥ 0, N_M5 = 9760 | PROVED as implication | **PROVED as implication** (HW, unbackreacted wall, Or₊) | Q_fib ≡ 0 (row 5), so (J_M5)_fib = ρ_J > 0 (rows 1–3). Independent of σ and of the value of c. |
| 9 | E-T: same | PROVED as implication | **PROVED as implication** (HW, unbackreacted wall, Or₊, Emb-T) | F = R_{Y₆} is natural, so Q_fib ≡ 0 for gauge and gravity parts. |
| 10 | E-Λ±: Q_fib = ∓(j/2)e_fib; adverse pairing J_M5 ≥ 0 iff j ≤ j\*; favourable: no bound | COND (float scan) | **PROVED as implication — GRADE CHANGE, with corrected j\*** | Premises: HW, unbackreacted wall, Or₊, fixed SO(3) ⊂ E₈ of index j with Q_gauge,fib = −(j/4)p₁(Λ²±)_fib (index normalisation tr = Tr₂₄₈/30 stated as premise). Exact: e_fib > 0 everywhere; sup (e_fib/2)/ρ_J = 5√2/17568 at μ₁ = 1; **j\* = 8784√2/5 = 2484.490386377…**. MR2's scan value 2484.4903873687 overshoots by ≈ 9.9e-7 (binding point β = 1e-5, not the exact maximum), so the filed "iff" is false for j ∈ (2484.49038637…, 2484.49038737…]. Since j is an integer, the integer statement **j ≤ 2484** is unchanged; not REFUTED, but the number must be replaced. |
| 11 | E-Λ± index unfixed; j ≥ 2, j ≤ 1240 | COND | **COND** | Cited E₈ facts (doublets in 248 under the root SU(2); conjugacy of index-1 SU(2)s; principal index 1240). |
| 12 | E-Λ±: J_M5 ≥ 0 for every admissible j, both σ | COND | **COND** | Exact once j ≤ 2484 (row 10); "admissible j ≤ 1240" is cited (row 11). Margin j\*/1240 ≈ 2.0036. |
| 13 | E-S± (j = 1): J_M5 ≥ 0 | COND (float scan) | **PROVED as implication — GRADE CHANGE** | Premises: HW, unbackreacted wall, Or₊, E-S± index-1 normalisation Q_gauge,fib = −(1/4)p₁(Λ²±)_fib. Exact adverse minimum of J_M5/ρ_J = 1 − 5√2/17568 = 0.99959750297…, attained on μ₁ = 1. Favourable pairing: J_M5/ρ_J = 1 + R_j > 1 everywhere. MR2's favourable "min 1.00001423041894" is a scan value and is not graded. |
| 14 | M-loc obstructed (N_M5 ≠ 0) | PROVED as implication of unbackreacted wall | **PROVED as implication** | A smooth form equal to a current supported on finitely many surfaces vanishes identically; N_M5 = 9760 − n ≠ 0 since \|n\| ≤ 1240 (that bound is cited, but the second argument, J_fib > 0 vs Q_fib = 0 or ∝ e_fib, does not need it for E-0/E-T). **No conflict with cc21b272 row 18**: row 18 (PROVED, bd47ff5e index sets) is the f-invariance of symmetric M-loc stacks and charge preservation, not a solution of the smooth pointwise equation. The obstruction is to M-loc under the unbackreacted wall; M-loc with localized backreaction is OPEN. No candidate is dropped (M-s survives). |
| 15 | global realisation by actual oriented M5 curves | OPEN | **OPEN** | |
| 16 | BPS/calibrated positivity and wall SUSY | OPEN | **OPEN** | |
| 17 | which candidate is the physical 1a datum | OPEN | **OPEN** (nothing adopted) | |
| — | σ unfixed; both signs reported | bookkeeping | bookkeeping | All PP exact results cover both σ. |

**Accepted claims:** rows 1–9, 14 (with grounds/premise corrections above); rows 10 and 13 upgraded on PP exact grounds; rows 11–12, 15–17 as filed.
**Rejected as grounds (not as results):** simplify==0 on the two [U] identities; the 25-digit Hodge match; the 8.6e-42 defect; the 2.7e-11 normalisation reproduction; the float j\* value; the float favourable E-S± minimum.

## 5. Tally (this filing, graded rows 1–17)
- **PP: PROVED 12** (rows 1–10, 13, 14) · **COND 2** (rows 11, 12) · **OPEN 3** (rows 15–17) · **REF 0** = 17, plus 1 bookkeeping row.
- MR2 claimed 10 / 4 / 3 / 0 = 17. Differences: rows 10 and 13, COND → PROVED as implication (PP exact grounds). No REF.

## 6. Status note 27c61e09
- Stale "lifts pending PP" lines (report lines 8, 72, 133): confirmed stale (513fdf49 confirmed in dd5a3a25 at 10:22:17; 52ba1eea confirmed in e7bc37a1 at 10:29:10). The filing uses the lifts only to list candidates. **No grade is affected.**
- The t433u scope paragraph is correct: nothing in 79795981 is adopted.
- The two nits are resolved in rows 1 and 7: the float/simplify grounds are withdrawn and replaced by PP's exact grounds; the grades stand.
- MR2's self-disclosed nits (name vs mtime, wrapper .exit, V2 prefix line, [F] artefact, mislabelled ⋆² check, unused U_s, timers) are verified; none affects a grade. C7 confirms ⋆² = +1 exactly.

## 7. Proposed split of cc21b272 row 22: ACCEPTED (explicitly adds one graded parent row)
- Row 22 bundles two claims. PP splits it:
  - **22a** "some candidate solves the pointwise wall Bianchi equation (M-s) with J_M5 ≥ 0": **PROVED as an implication** of HW (structural form and normalisation), the unbackreacted wall, and the **new premise Or₊**. Witnesses: E-0 and E-T (rows 8–9); per this audit also E-S± (row 13) and E-Λ± for integer j ≤ 2484 (row 10). Per-candidate details stay in this file; they are not parent rows.
  - **22b** "some candidate is SUSY / BPS-calibrated, and the smeared J_M5 is realised by actual oriented M5 curves": **OPEN** (rows 15–16).
- No COND or OPEN parent item is upgraded other than through 22a, whose grade rests on a new stated premise. Row 23 (physical datum) stays OPEN.
- **Parent tally of cc21b272 as amended: was 17 PROVED / 2 COND / 4 OPEN / 0 REF = 23 (+1 bookkeeping); now 18 / 2 / 4 / 0 = 24 (+1 bookkeeping).** The extra graded row is 22a; 22b keeps row 22's OPEN slot. The 2 COND rows remain D4 and row 8; the 4 OPEN rows remain 16, 19, 22b, 23. 12′ remains a scoped sub-statement.
- PP does not edit cc21b272 or any parent file. **22a is not adopted.**

## 8. Numbered fixes for MR2 (additive erratum; do not edit 79795981)
1. **priority:true.** State Or₊: add the alignment clause (the Or orientation of Σ is the one with ∫_{S⁴}J = +2N). Rows 3, 8, 9, 10, 13 and parent 22a depend on it.
2. **priority:true.** Row 1: withdraw simplify==0 and the 25-digit Hodge match as grounds. Cite exact grounds (X₁⁵ = 1/8; U by expand; the block-structure Hodge argument; PP C1–C5). State "nowhere zero" for the density relative to vol_fib.
3. **priority:true.** Row 7: replace the 8.6e-42 defect by the exact invariant-polynomial identity (PP C7). Do not use the GL integrals as grounds.
4. **priority:true.** Row 2: cite ∫G₄_fib = −π² exactly (PP C6 / hand reduction) instead of the 2.7e-11 reproduction.
5. **priority:true.** Row 10: replace j\* = 2484.4903873687 by the exact j\* = 8784√2/5 ≈ 2484.490386377 (maximum on the circle μ₁ = 1), integer form j ≤ 2484. Regrade COND → PROVED as implication, with the index-normalisation premise written out. Keep the cited E₈ index facts in row 11.
6. **priority:true.** Row 13: regrade COND → PROVED as implication. Report the exact adverse minimum 1 − 5√2/17568, and drop (or prove) the float favourable minimum.
7. Row 4: name dG₄ = 0 for the MN2 uplift as the premise.
8. Row 14: add that it does not conflict with cc21b272 row 18 (f-symmetry of stacks), and that M-loc with localized backreaction is OPEN.
9. Tally line: 12 / 2 / 3 / 0 = 17, plus 1 bookkeeping.
10. Branch status: record the row-22 split as decided here (22a PROVED as implication of Or₊ etc., 22b OPEN; parent 18 / 2 / 4 / 0 = 24 + 1 bookkeeping), and that none of it is adopted.
11. Carry the stale lift-status correction from 27c61e09 into the erratum (lines 8, 72, 133).
12. Process (no grade effect): print a wall-clock timestamp and the script's own sha256 at the start of future logs, so "run started after freeze" is provable from the log; freeze and sidecar the wrapper .exit file or stop writing it.

## 9. Branch status
- B1-c2′ stays **COND overall**, not adopted. 8399be55 stays COND.
- Whether any E₈ candidate is the physical 1a datum: **OPEN**. 1a not adopted (pure form REF fe0c3d92; rescues OPEN).
- Group A stays the chosen KK scope. Literal c2 stays REFUTED (scoped). t4436 unchanged for the remaining open paths.
- Nothing in this filing is adopted under t433u; a later Owner word would be needed.
- Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (not touched by PP). Junction **UNSOLVED**. **No CERT.**

**Sha of this findings file:** see its .sha256 sidecar (written after the header time was confirmed equal to the mtime).
