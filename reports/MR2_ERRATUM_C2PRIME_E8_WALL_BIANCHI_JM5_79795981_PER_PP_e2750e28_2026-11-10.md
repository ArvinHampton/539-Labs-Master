# Erratum to the wall Bianchi / J_M5 filing 79795981, per PP audit e2750e28
2026-11-10, written 11:00:38 CST (America/Chicago; this is the write time, matching the file's mtime). Author: MR2. Additive erratum only; 79795981 and note 27c61e09 are not edited. No new computation in this file. Nothing in this filing is adopted. Junction UNSOLVED. Wording: resonant algebra. No CERT.

# Erratum to the wall Bianchi / J_M5 filing 79795981, per PP audit e2750e28

Target: MR2_BRANCH_ATTEMPT_BATCH1_C2PRIME_E8_WALL_BIANCHI_JM5_DENSITY_2026-11-10.md, sha256 797959812aeaafc3e1d3c4d59573bc4f315b03936c74121b1138af5c4f877048 = sidecar, written 10:30:58 CST, header = mtime. Status note 27c61e0984c30ba0d2ecfc74f6f764e1da59986088ef6d4419f3aecabd6d8cd4.

PP audit: FINDINGS_PP_AUDIT_MR2_WALL_BIANCHI_JM5_79795981_2026-11-10_1057.md, sha256 e2750e28457254d661757acb6ebef857f6999153f605db24fd625837a60a8b5f = sidecar, written 10:57:57 CST, header = mtime. Evidence under /workspace/quantum-comp/reports/pp_evidence_bianchi_jm5_79795981_2026-11-10/ (each sha = sidecar, mode 444), including exact checks C1–C7 (pp_exact_checks.py 749916501cc35e3d9c700703f6f48ec809d5554613b59d4ee10dfa4c37480ede / log 00bd3bea5b74eb72e6cba85353c8e5b08f991d599300f47e326d2c19f8a9effc, exit 0) and the Gauss–Bonnet certificate (pp_exact_gb_verify.py f412ff8488b2583a80737d6d6a5ab8ac365c307adba529e0c06987413400b142 / log d9228c095de365c341de20a7f34fcb96012502954a25a14b752295b7947ad8db, exit 0). All twelve fixes in §8 are accepted. This file cites those checks; it does not re-run them.

Authority and adoption. Owner t433u covers only results already PP-PROVED at that time. Every grade below, including the upgrades, stays unadopted until a later Owner word says otherwise. 1a is not adopted as the physical wall. B1-c2′ stays COND overall and is not the KK scope. Group A stays the chosen KK scope. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH at this write.

## Fix 1 (priority). Premise Or₊

Or is accepted as a new stated premise only with the alignment clause **Or₊**: Or, and the Or orientation of Σ is the one in which ∫_{S⁴} J = +2N (M5 charge sign agrees with the MN flux sign). Rows 3, 8, 9, 10, 13 and parent 22a are implications of Or₊ (together with the other premises named for each row). Or₊ is weaker than BPS/calibrated positivity, and is not proved.

## Fix 2 (priority). Row 1 grounds

Withdraw simplify==0 and the 25-digit two-point Hodge match as grounds for PROVED (corroboration only). Row 1 stays **PROVED** on PP C1–C5: lim X₁⁵ = 1/8, hence X₀ = X₂ = p := 2^{2/5}, X₁ = p/2, a₁ = 1, a₂ = 0; U − p²(s − 4) and D − p(1 − s/2) expand to 0, so U ∈ [−4p², −3p²] < 0; the block-structure Hodge argument gives G₄_{αβφ₁φ₂} = ±κ U D^{−7/6} √det g_fib exactly; det h reduces as in C5. "Nowhere zero" is the density J_fib / vol_fib = ±κ U D^{−7/6}; the coordinate component vanishes only on the chart degeneracies sin α · μ₁μ₂ = 0.

## Fix 3 (priority). Row 7 grounds

Withdraw the 8.6e-42 pointwise defect as grounds. Row 7 stays **PROVED** as the exact invariant-polynomial identity p₁(Λ²±) = p₁ ± 2e (PP C7, expand == 0 for both signs; ⋆² = +1 on Λ² exactly). The GL integrals (2, ±4, 0) are float, agree with χ(S⁴) = 2 and σ(S⁴) = 0, and are not grounds.

## Fix 4 (priority). Row 2 grounds

Row 2 stays **PROVED**. Cite ∫ G₄_fib = −π² exactly (PP C6 / hand reduction), independent of 5511845e; 2N = 9760 is the in-repo wall charge (bd47ff5e / 5511845e). The 2.7e-11 reproduction is not grounds.

## Fix 5 (priority). Row 10 regrade and exact j*

Replace the scan value j\* = 2484.4903873687 by the exact **j\* = 8784√2/5 ≈ 2484.490386377**, attained on the circle μ₁ = 1. The scan overshot by about 9.9×10^{-7}; since j is an integer, the integer bound **j ≤ 2484** is unchanged. Row 10 is regraded **COND → PROVED as an implication** of HW, the unbackreacted wall, Or₊, and the fixed SO(3) ⊂ E₈ of index j with the index-normalisation premise Q_gauge,fib = −(j/4) p₁(Λ²±)_fib (tr = Tr₂₄₈/30). Exact: e_fib > 0 everywhere; sup (e_fib/2)/ρ_J = 5√2/17568 at μ₁ = 1 (PP GB certificate). Favourable pairing: no bound. The cited E₈ index facts remain in row 11 (COND).

## Fix 6 (priority). Row 13 regrade and exact adverse minimum

Row 13 is regraded **COND → PROVED as an implication** of HW, the unbackreacted wall, Or₊, and the E-S± index-1 normalisation Q_gauge,fib = −(1/4) p₁(Λ²±)_fib. The exact adverse minimum of J_M5/ρ_J is **1 − 5√2/17568**, attained on μ₁ = 1. Favourable pairing: J_M5/ρ_J = 1 + R_j > 1 everywhere. The float favourable "minimum" 1.00001423041894 is dropped as grounds (it was a scan value and is not graded).

## Fix 7. Row 4 premise

Row 4 is **PROVED as an implication**. The premise is dG₄ = 0 for the MN2 uplift (MN2 as an 11D solution; standing, not re-proved). V2's numerical dG check is not grounds. The content is definitional: J_M5 is closed, and M-s solves the pointwise Bianchi equation by construction.

## Fix 8. Row 14 and parent row 18

Row 14 stays **PROVED as an implication** of the unbackreacted wall. It does not conflict with cc21b272 row 18 (the f-invariance of symmetric M-loc stacks and charge preservation, not a solution of the smooth pointwise equation). M-loc with localized backreaction is OPEN. No candidate is dropped (M-s survives).

## Fix 9. Tally of this filing

PP tally, graded rows 1–17: **12 PROVED / 2 CONDITIONAL / 3 OPEN / 0 REFUTED = 17**, plus 1 bookkeeping row. PROVED: rows 1–10, 13, 14. COND: rows 11, 12. OPEN: rows 15–17. Differences from the original 10/4/3/0: rows 10 and 13, COND → PROVED as implication, on PP exact grounds.

## Fix 10. Row-22 split and parent tally

The proposed split is accepted, and is recorded as decided in e2750e28:
- **22a** "some candidate solves the pointwise wall Bianchi equation (M-s) with J_M5 ≥ 0": **PROVED as an implication** of HW (structural form and normalisation), the unbackreacted wall, and Or₊. Witnesses: E-0 and E-T (rows 8–9); also E-S± (row 13) and E-Λ± for integer j ≤ 2484 (row 10). Per-candidate details stay in 79795981 as amended here; they are not parent rows.
- **22b** "some candidate is SUSY / BPS-calibrated, and the smeared J_M5 is realised by actual oriented M5 curves": **OPEN** (rows 15–16).
- cc21b272 row 23 (physical datum) stays OPEN. 12′ remains a scoped sub-statement.
- **Parent tally of cc21b272 as amended: 18 PROVED / 2 CONDITIONAL / 4 OPEN / 0 REFUTED = 24**, plus 1 bookkeeping row. The extra graded row is 22a; 22b keeps row 22's OPEN slot. The two COND rows remain D4 and row 8; the four OPEN rows remain 16, 19, 22b, 23.
- 22a is not adopted. None of this filing is adopted under t433u.

## Fix 11. Stale lift-status lines

Carry forward from 27c61e09: report lines 8, 72 and 133 ("E-S± and E-T lift restorations still pending PP") were already out of date at the 10:30:58 write (confirms dd5a3a25 at 10:22:17 and e7bc37a1 at 10:29:10). Status only; no grade is affected. The filing uses the lifts only to list candidates.

## Fix 12. Process, no grade effect

Accepted for future runs: print a wall-clock timestamp and the script's own sha256 at the start of the log, so "run started after freeze" is provable from the log; freeze and sidecar the wrapper .exit file, or stop writing it. The log of 79795981 has no wall-clock stamps; PP's timing inference is consistent with a start about 2 s after the sidecar, and is not a proof from the log itself. Log = complete exit-0 run of that exact script was confirmed by PP's byte-identical re-run (identical modulo timers).

## Unchanged branch status

B1-c2′ stays COND overall, not adopted. 8399be55 stays COND. Whether any E₈ candidate is the physical 1a datum stays OPEN. 1a is not adopted (pure form REF; rescues OPEN). Group A stays the chosen KK scope. Literal c2 stays REFUTED (scoped). t4436 is unchanged for remaining open paths. Junction UNSOLVED. Tip untouched.
