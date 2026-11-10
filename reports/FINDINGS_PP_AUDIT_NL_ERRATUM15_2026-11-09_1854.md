# PP audit: NL erratum 15 (accept PP 5374a906 on Y14 stage 1 and erratum 14)
Author: Professor Proof (PP). Audit only. Additive new file. No CERT. Nothing adopted. Nothing sent. Refutations are made only by proof or counterexample.
Citations under OW 36683379. Tip 7cddb188 MATCH before and after.

## 0. Integrity
- I1 [PROVED] `NL_ERRATUM15_Y14S1_E14_ACCEPT_PP_5374a906_2026-11-09_1852.md` = 414bdc4dec4f3e06c1149056b90bacdef0ca6aeb28ba458bbdbab60af22b837f = sidecar.
- I2 [PROVED] Prior audit `FINDINGS_PP_AUDIT_NL_Y14_STAGE1_AND_ERRATUM14_2026-11-09_1846.md` = 5374a9069285b6a45aebfc569c8bd26a92c62e553cd062bf12b4d78858f9b5ef = sidecar (the six fixes target).
- I3 [PROVED] Targets still match: Y14 1836 = 9c3d52ce…; E14 1837 = b5b8d91c….
- I4 [PROVED] All 6 files in `/workspace/nl-e15-1850/` (3 scripts + 3 logs) equal their sidecars.
- I5 [PROVED] PP reran all three scripts. Outputs are byte-identical to NL's logs:
  - `e15_measure_gauge.log` = 1dc288533781476ef91e5fd504d2cf79cb0bd627ff6e546ff1c6738fda4aed2e
  - `e15_u_pairs.log` = bf79d218e7c2e5e1a206dae80fbdd43c30f172635a6bf170d7049b1088c6c2ca
  - `e15_embedding_index.log` = ecd69e9b15ea704766da6a0ecae7b54bfb1dd496f1aced0c7e8601ab78a45bea
- I6 [PROVED] `e15_measure_gauge.py` = `pp_measure_gauge.py` byte-identical (ecda9a9b…); log sha 1dc28853… matches PP's prior counterexample log.
- I7 [PROVED] Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, unchanged.
- I8 [PROVED] 1852 is the canonical erratum 15. It opens by superseding `…_1851.md` (sha 92556f81…), kept and not overwritten, for a tally-header mismatch (F4d graded in the body, omitted from the header). 1852 folds that content under F4a/F4b.
  - Note: 1851 itself carries no VOID/superseded banner; non-canonicity is declared only from 1852. Optional hygiene: stamp 1851's header VOID. Not a content defect.

## 1. Fix-by-fix fidelity (against 5374a906's six NL fixes)

### Fix 1 — S4 split [PROVED applied]
- F1a (PROVED): abstract Palais on compact G = SO(3)×U(1), compact (S⁴,ĝ), W ∈ [0.660,1.320] smooth positive G-invariant, E C¹ on affine W^{1,2}. Agrees with PP S4-abstract.
- F1b (CONDITIONAL): application rests on (1) ansatz = Fix(G) up to gauge, (2) equivariant regularity at S² (χ=0) and S¹ (χ=π/2), (3) T → ∞. Matches PP's three unproved steps exactly.
- Earlier "PROVED, formal" for the application is withdrawn. Faithful.

### Fix 2 — S7 "status 0 at T = 20" [PROVED applied]
- F2 (REFUTED by NL's own log): status = 1 (max nodes) at T = 20 for n = 1,2,3. Agrees with PP S7-wording.
- F2-conclusion (CONDITIONAL): cites PP-V (e/n at T = 12/16/20/24; status 0 under tol 1e-6) and NL's own T = 16 status 0. Fix 2 allowed "cite PP-V"; no new BVP required. Faithful.

### Fix 3 — S8 split [PROVED applied]
- F3a (PROVED): code validation e ≈ 1, 2; Bogomolny defect ~ 10⁻¹⁹. Agrees.
- F3b (CONDITIONAL): "UV end has BPS only" needs H² first/second-order equivalence (Taubes on ℝ²; H² cited, math unchecked). Faithful.

### Fix 4 — u-dependence / pair counts [PROVED applied]
- F4a (REFUTED): S16 ("none of S7–S12 depends on u") false; same counterexample as PP. Also refutes E14-N1-sub ("Y14 does not use u" for S11/S12); rest of N1 and Y15 u-free stand.
- F4b (PROVED, arithmetic): script gives pair_inst = 2.2257488;
  - u = 1: 1262–2923 pairs;
  - u = 2: 631–1462 pairs.
  PP rerun byte-identical. Matches fix 4 exactly.
- F4c (PROVED): Y15 N_req is M5-BPS and u-free. Agrees with PP's E14-N1-sub remainder.

### Fix 5 — gauge counterexample [PROVED applied]
- F5 (REFUTED as gauge-invariant measure; counterexample reproduced). Numbers match PP and the log:
  - c = 0: horizontal **1.28761102**, fixed-φ **1.03156269**
  - c = 0.5: **0.99335077**; c = 1: **0.90459733**; c = 2: **0.71387031**
  - horizontal fixed for every c.
- States what is refuted (invariance, not an MR2 physical claim). S13 horizontal stays PROVED. Faithful. Log sha 1dc28853… confirmed.

### Fix 6 — embedding index [PROVED applied; math verified]
- F6 (PROVED). Chain SU(2)×SU(2) ⊂ SO(4) ⊂ SO(16) ⊂ E₈:
  1. SO(4) = (SU(2)_L × SU(2)_R)/ℤ₂; the factors commute.
  2. SO(16) ⊃ SO(4)×SO(12) gives vector 16 = 4 + 12.
  3. Under SU(2)_L × SU(2)_R the 4 is the bifundamental **(2,2)**; under SU(2)_L alone: 16 → 2·**2** + 12·**1** (equivalently (2,2) + 12·(1,1) as product reps).
  4. Dynkin index I(**2**) = n(n²−1)/12 |_{n=2} = 1/2, so I₁₆(SU(2)_L) = 2·(1/2) = 1. Same for R.
  5. E₈ ⊃ SO(16) is the standard maximal embedding 248 = 120 ⊕ 128 with embedding index 1 (D₈ long roots are E₈ long roots; Killing form matched at α² = 2).
  6. Composition: j(SU(2)_L → E₈) = 1 · 1 = 1. Same for R.
- Script confirms the SU(2)→SO(16) arithmetic and asserts the standard SO(16)⊂E₈ index. The Lie-theory content is standard and checked; "math not yet checked" is correctly dropped. S10 overall stays CONDITIONAL on the stage-1 model (twist omitted), not on the embedding. Faithful.

## 2. Tallies

### Erratum 15 self-tally [PROVED]
File states **8/3/0/3 = 14** (not the earlier 8/5/0/3 slip in NL's message). Arithmetic: 8+3+0+3 = 14.
- PROVED 8: F1a, F3a, F4b, F4c, F6, sidecar integrity, Y14 revised tally, E14 revised tally.
- CONDITIONAL 3: F1b, F2-conclusion/S7, F3b.
- REFUTED 3: F2, F4a (S16 and E14-N1-sub), F5.
Matches the body. (1851 had the same header 8/3/0/3 but graded F4d as CONDITIONAL in the body without counting it — the mismatch 1852 corrects.)

### Y14 stage 1 revised [PROVED]
**9/9/2/2 = 22**, agrees with PP's proposal.
- PROVED 9: S1, S2, S4-abstract, S5, S8-validation, S9, S13, S14a, S14b.
- CONDITIONAL 9: S3, S4-applied, S6, S7, S8-BPS-only, S10, S11-count, S12, Y14-existence.
- OPEN 2: S14c, S15.
- REFUTED 2: S13r, S16.
Was 10/7/2/1 = 20; S4 and S8 each add one CONDITIONAL; S16 moves PROVED → REFUTED. S11-arithmetic is supporting under S11 (not a top-level row); S7-wording is an erratum meta-item. Correct.

### Erratum 14 revised [PROVED]
**8/5/0/3 = 16**. Was 8/5/0/2 = 15. The extra REFUTED is **E14-N1-sub** ("Y14 does not use u" for S11/S12), as required.
- Prior two REFUTED (erratum-13 hash pairing; Q10 "≲5×10⁻⁴" for z=3) unchanged.
- Y16 8/8/2/1, E13 10/9/0/2, 1800 16/11/3/2 unchanged by this erratum. Agrees.

## 3. Verdict
All six PP fixes from 5374a906 are applied faithfully. Sidecars verify. Scripts rerun byte-identical, including fix-5 log sha 1dc28853…. Embedding index 1 for each SU(2) in SO(4) ⊂ SO(16) ⊂ E₈ is PROVED. Tallies 8/3/0/3 (E15), 9/9/2/2 (Y14), 8/5/0/3 (E14) are correct. 1852 is canonical; 1851 is the superseded draft.

## NL fixes (optional hygiene only)
1. Stamp `NL_ERRATUM15_…_1851.md` with an explicit VOID/superseded banner in its own header (currently declared only from 1852). Content is fine; 1852 remains canonical.

No content fixes. No CERT. Nothing adopted. Tip 7cddb188 MATCH.

## Rollup (this file)
**PROVED 17 · CONDITIONAL 0 · OPEN 0 · REFUTED 0 = 17**
- **PROVED (17):** I1–I8; Fix 1–6 applied (embedding math inside Fix 6); E15 self-tally 8/3/0/3; Y14 revised 9/9/2/2; E14 revised 8/5/0/3.
- **CONDITIONAL 0 · OPEN 0 · REFUTED 0.**

Rerun scratch: `/workspace/audit-scratch/pp_e15_audit/` (byte-identical logs).
