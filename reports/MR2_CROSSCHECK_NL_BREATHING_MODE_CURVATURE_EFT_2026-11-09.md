# MR2 cross-check of NL's S⁴ breathing-mode work on MN2: curvature, breathing mass, EFT (OW d5eaeef3 "Pursue all open", OW 90cec14c)

Date: 2026-11-09, America/Chicago. Author: MR2 (resonant algebra project, Quantum Comp). This file is additive. No existing file was edited, and the tip 7cddb188 was not touched.

Grades are PROVED / COND / OPEN / REF, under PP's convention: an implication that states its premise is graded as an implication, a premise used but not stated makes the claim COND, float-only evidence is COND, and a citation alone is never PROVED.

## Inputs (every sha matched its sidecar before use)
- NL 1935 ebdda4b6, NL 1936 358c4b09, NL 1942 59a4f05e, NL 1943 b103f08f, NL 1948 9a29b6da.
- PP 1944 3982a4b8, PP 1947 fb515bef, PP 1956 99593076.
- OW d5eaeef3.
- KK ecee2668, irrep labels ed0e5bd6, frozen V2 routines ad134752.

## Artifacts
| file | sha256 |
|---|---|
| `MR2_CROSSCHECK_NL_BREATHING_MODE_CURVATURE_EFT_2026-11-09.py` | c82a524d349e98dc09ac38fe3dceb0105babbe7da16fbf19c133177d77251845 |
| `…_2026-11-09.log` | 435c340f2a325ba6aa7972f4e1ae9df69c04dd8977c83c31f49bbf2f85dcc970 |
| `…_PART2_E4_NUMERIC.py` | 098bf6fce90848e713f25815ed8f223cc586bd7f18a0d75359054bb03404a05b |
| `…_PART2_E4_NUMERIC.log` | cc90c88826f01e0693a377d57e350eebc18b79c718f2d94add9c7fe1faf85889 |

- Each `.py` was frozen before it ran.
- The first script finished (a1) and (b). Its (a2) step, a symbolic NumGeom build with exp(2γβ(r)), was killed for running out of memory. The log records this as `EXIT 137`.
- PART2 redoes (a2) and (d) with a self-contained numeric Ricci: mpmath at dps 50, with derivatives of the analytic metric. Its control reproduces the V2 (D) product scalar curvature, R = 5.99999999999999075 against 6.
- Separate note: `MR2_NOTE_9ab8f0a6_LINE27_D_PRODUCT_F0_2026-11-09.md` (sha 553a8a4a…, see §5).

## (a) Reduced equations, kinetic sign and normalisation
**M1 (COND, float; concurs with PP's exact PROVED for E1).**
- Setup: ds² = e^{2A}dx²₁,₃ + dy² + e^{2B}ds²(H²) + e^{2C}dΩ₄², with G₄ = Q·dΩ₄ and q = Qe^{−4C}.
- I built the full 11D Ricci from the V2 NumGeom engine. The right-hand side is my own: R_MN = (1/12)(G_M···G_N··· − g_MN G²/12), which gives +q²/3·g on S⁴ and −q²/6·g on every other block.
- I inserted NL's A″, B″, C″ and took q² from NL's constraint, at two generic data points. Max |R_MN − RHS| was 9.2e-40 and 5.5e-40.
- Control: with q² × 1.1, so the constraint is violated, the residual becomes 2.87 and 0.35. So NL's constraint is exactly the yy equation.
- NL's fixed point (A′ = −1, e^{−2B} = 4, e^{−2C} = 8/3, q² = 24) gives a residual of 4.6e-41.

**M3 (PROVED, exact arithmetic).** NL's singlet fixed point is the V2/KR (D) product.
- e^{2B}/L² = 1/4 = G0/F0 = (1/6)/(2/3).
- e^{2C}/L² = 3/8 = (1/4)/(2/3).

**M4 (PROVED, exact sympy).** The breathing kinetic term has the right sign.
- Write a = A + w with w = (2B+4C)/3 and dy₅ = e^w dy. This is the 5D Einstein frame, since the internal volume is e^{2B+4C} and d − 2 = 3.
- NL's kinetic form becomes 6a′² − (5B′² + 8B′C′ + 14C′²)/3. There is no a′B′ or a′C′ cross term.
- Matching the constraint to 6ȧ² − ¼K_ij φ̇ⁱφ̇ʲ + ½V = 0, for L = R − ½K(∂φ)² − V, gives K = [[20/3, 16/3], [16/3, 56/3]].
- K has eigenvalues (38 ∓ 2√145)/3 = 4.64 and 20.69, so it is positive definite. There is no ghost.
- Pure S⁴ breathing has K_CC = 56/3 > 0, so the canonical field is φ = √(56/3)·C.
- Premise, stated: the singlet sector reduces to the standard 5D two-scalar form, which is NL E0–E2 (PROVED per PP). The implication itself is PROVED.

**M2 (COND, float; concurs with the closed-form E4 that PP and NL 1942 P1 grade PROVED).** I checked NL's E4 on our own V2 MN2 metric.
- Setup: X1 = 2^{−3/5}, X2 = X0 = 2^{2/5}, F0 = (X1X2)⁴, G0 = X1X2²/4, a1 = 1, a2 = 0. The 7D block is multiplied by e^{2γβ(r)}, and the whole S⁴ block, including the twist cross terms, by e^{2β(r)}.
- R_{r,α} / (3/2 β′∂_α ln D) = 1 and R_{r,β} / (3/2 β′∂_β ln D) = 1. This holds at 2 points, for γ ∈ {−1, −½, 0, ½} and two pairs (β′, β″). Max |ratio − 1| = 1.2e-15.
- Control: β′ = 0 with β″ = 0.7 gives R_{rα}, R_{rβ} ≈ 1e-16.
- So the identity does not depend on γ or β″, and it holds in both S⁴ angle directions. NL wrote only χ.

## (b) Effective-potential curvature and breathing-mode mass
**M5 (PROVED, exact sympy, given M4's stated premise).** Here V = 2U e^{−2w}, with U = e^{−2B} − 6e^{−2C} + Q²e^{−8C}/4 and Q fixed.
- At the (D)-type point, dV = 0 and V₀ = −12/L₅², where L₅ = e^w. This is exact.
- The eigenvalues of L₅²·K⁻¹ Hess V are:
  - m²L₅² = 8 (Δ = 2+2√3 = 5.4641), with eigenvector (δB : δC) = (1 : 0);
  - m²L₅² = 48 (Δ = 2+2√13 = 9.2111), with eigenvector (−4/5 : 1), which is mostly S⁴ breathing.
- These reproduce NL S1 (48, 8) exactly.

**M6 (PROVED, arithmetic comparison).** The toy masses are not MN2 masses, and the files make no such claim.
- The MN2 level-0 invariant scalars are m²L₅² = −4 and +12 (Δ = 2, 6). These come from NL K1 and match ecee2668 §7, where Δ = 6 mixes with the Σ breathing h.
- The lowest Group A (Aut⁺(Bolza)·48 × wall ℤ₂) spin-2 level above 0 is λ = 23.0786, giving m²L₅² = 46.157 (Δ = 9.082). Per ed0e5bd6 it is the trivial irrep I1, and it is the only Aut⁺-invariant level in (0, 25.5).
- The toy's 48 (Δ = 9.211) is close to 46.157, but this is a coincidence between different vacua. It is not a prediction.
- On MN2 the breathing-type invariant is the Δ = 6 (m²L₅² = 12) singlet. It is not a pure uniform S⁴ breathing, which is consistent with NL T4 and 1942 P1: uniform δβ sources R_rχ ≠ 0, so it is not an eigenmode.

## (c) Effect on our batch-1 results
**M12 (PROVED, scope implication).** NL's files change none of L3, B5 or the uniform/cohomogeneity-two split.
- **L3** (Σ|σ_neg| ≥ ρ_w/3, sharp because NL A1 saturates it; N_req/3 ≥ 2873–5599 COND): its premise is exact-MN2 face data.
  - NL K4 (PROVED per PP) closes the face with changed face data (C4) as a smeared 5-brane that satisfies the NEC.
  - That lies outside L3's premise, so it is no contradiction. It is exactly the "closure needs changed face data" branch.
- **B5 Stokes** (odd G₄ forces 2N = 9760 units of smeared charge in any smooth profile): breathing does not change the G₄ total (f825dfff fixes ∫(n_M5 + n_inst) = 9760). So it is unchanged, and K4's smeared source must carry that charge.

**M13 (REF, unchanged and strengthened).** "Uniform breathing closes the MN2 face" stays refuted.
- NL 1942 P1–P3 and PP 1947 show that β′ ≡ 0 is forced on MN2.
- My M2 numerics agree, independently of NL's code.

**M16 (OPEN, unchanged).** The cohomogeneity-two (r, χ) route stays open.
- T7 is a PROVED arena, but T9 (data-vs-codimension count) and T10 (the shoot) are still OPEN.
- K6 is OPEN per PP, and K6′ is COND.

## (d) EFT validity and truncation consistency
**M9 (PROVED, arithmetic).** At N = 4880, ℓ = 49.68438 ℓ_p and L₅ = 37.65372 ℓ_p.
- ℓ_p²R_max = 12/ℓ² = 4.861e-3.
- ℓ_p²·sup√(Riem²) = √3408/ℓ² = 0.023649.
- At the wall, ℓ_p·k ≤ 0.02846 and (ℓ_p k)² = 8.1e-4.

**M10 (COND, power counting with an O(1) R⁴ coefficient).**
- Higher-derivative corrections are about (ℓ_p²√Riem²)³ ≈ 1.3e-5 relative to the two-derivative terms.
- So the two-derivative EFT holds on MN2 and on the thin-wall face at leading order.

**M11 (OPEN).** I did not check curvature along NL's toy (S4) trajectories. NL reports that those runs go singular within about 1.5L, where the EFT must fail. This bears only on the toy, not on MN2.

**M7 (PROVED, comparison of stated values).** NL K1 (Δ = 2, 6) equals ecee2668 §7.

**M8 (PROVED, given the stated premise T7, which PP grades PROVED).** NL's mode counting is consistent with the KK truncation.
- Every T7/T0 field is Σ-constant up to the twist compensator, so it sits at the λ = 0 Bolza level.
- The next Group A-invariant level, 23.0786 (I1, spin-2 46.157), is not locally PSL(2,ℝ)-invariant, so it lies outside the T7 sector. Since T7 is consistent, setting it to zero is consistent.
- So NL's counting is consistent with ecee2668 and ed0e5bd6. The T7 sector is a proper subsector of the Group A scope, which agrees with PP A5 and K8.
- The T9 count must still say whether wall data source those modes. That remains OPEN under M16.

## Per-NL-claim verdicts (MR2)
No NL claim is proved false. MR2 concurs with PP's grade on every item.

| item | PP grade | MR2 verdict |
|---|---|---|
| E0 | PROVED | concur |
| E1 | PROVED | concur; independently confirmed (M1) |
| E2 | PROVED | concur (MN2 has X1 ≠ X2, so it is not an SO(5) singlet) |
| E3 | REF | concur; independently supported (M2, M13) |
| E4 | PROVED | concur; independently confirmed on the V2 metric, both angles, any γ (M2) |
| E5 | OPEN (narrowed) | concur |
| E6 | closed: premise REF (T2), superseded by T6 | concur |
| E7, E8, E9 | PROVED | concur (not rerun) |
| E10 | PROVED | concur (follows from E4, which I confirmed) |
| S1 | PROVED | concur; masses 48 and 8 reproduced exactly (M5) |
| S2 | PROVED | concur |
| S3 | COND (does not carry over to MN2) | concur |
| S4 | COND | concur |
| S5 | OPEN | concur |
| S6 | OPEN (superseded) | concur |
| T0, T1, T3, T4, T5, T7 | PROVED | concur. I did not recheck T1's citation part, and PP notes its flux sub-part is COND. T4 is consistent with M2/M6. T0/T7 are used in M8. |
| T2 | REF | concur |
| T6, T9, T10 | OPEN | concur |
| T8 | COND | concur |
| K1 | PROVED | concur; matches ecee2668 §7 (M7) |
| K2 | PROVED (Δ = 4 sub-clause COND) | concur |
| K3 | OPEN | concur |
| K4 | PROVED | concur; consistent with L3's scope (M12) |
| K5 | COND | concur |
| K6 | OPEN (K6′ COND) | concur |
| K7 | OPEN | concur |
| K8 | PROVED (wording fix) | concur; consistent with M8 |

## Tally (MR2's own claims M1–M16, excluding M14 and M15)
- **PROVED 8:** M3, M4, M5, M6, M7, M8, M9, M12.
- **COND 4:** M1, M2, M10, plus M15 below.
- **OPEN 2:** M11, M16.
- **REF 1:** M13.

That makes 15, plus M14 in §5 (PROVED), for a total of **16: 9/4/2/1** (PROVED/COND/OPEN/REF).

## Recommendation impact
**M15 (COND, on T9/T10 OPEN).** The face/wall recommendation does not change.
- **Item 1:** keep (1a), the HW E₈ wall, as the face. Pure exact-MN2 closure is REF (L3, plus uniform breathing REF in M13). The live closure route is changed face data in the T7 cohomogeneity-two sector (K4 shows the needed source is NEC-satisfying), and it stays OPEN until T9 and T10 are done.
- **Item 2:** keep (2a), the thin wall. The EFT numbers in M9 and M10 support it, and (2c′) still says thickness is not the lever.

## 5. M14: note on 9ab8f0a6, line 27 (PROVED; separate file, sha 553a8a4a…)
- The coded (D) control is F0 = e^{2f} = 2/3 = L²_AdS5, with G0 = 1/6. For this metric the V2 log gives K = 618, Ric² = 828 and R = 6.
- The md's "e^{2f} = 4/9 so that L_AdS5 = 2/3" is a text slip.
- No "4/9" appears in the V2 code. **The brief said 4/9 is the coded control value. It is not.**
- 9ab8f0a6 itself was not edited.
