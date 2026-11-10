# NL DERIVED: Y14 stage 2. Twisted non-BPS E₈ fields on the MN2 fibre: Σ-twist coupling, charge-0 search, mirror pairs, interior faces, second variation
Author: Non Local Path (NL). Everything below is an **NL derived proposal**. Nothing is adopted.

Authority: OW 9bb1858c (Y14, Y15); OW b0b9ae7f (t4407, "Pursue all for resolutions", sha b0b9ae7f… = sidecar, checked 18:43 CST); OW 19a88b19 (MN N=2 working vacuum, CONDITIONAL; junction UNSOLVED); OW 36683379 (any source, math checked; citation alone never PROVED); OW 49b04146 (KK scope: Bolza- and wall-ℤ₂-invariant modes; scope choice, not a result; no KK modes are used here); OW f1d167d1 naming rule (no affected names appear here).
Input: stage 1, NL_DERIVED_Y14_NONBPS_E8_EXISTENCE_MN2_STAGE1_2026-11-09_1836.md (9c3d52ce… = sidecar). PP audit 5374a906 fixes are applied here: (1) both u values everywhere, (2) Palais split, (3) converged runs only.
Limits: new file only. No CERT, no Gemini, nothing sent, no agent messaged. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188… before and after.
Usage: 51% at start, 56% at midpoint.

Scripts and logs, all with sidecars, in /workspace/nl-junction-1851/:
- y14s2.py (twisted reduced functional, BVP), run_ir.py/.log (IR face n=1–3, T=12/16/20/24), run_ir_n45.py/.log (n=4,5), run_ir_bign.py/.log (n up to 160), run_bign_Tcheck.py/.log, run_faces.py/.log (interior faces), disc.py + stab_q0.py/stab_q0_run3.log (second variation), postproc.py/.log (counts), y15.py/y15_run.log (used by the Y15 file).
- Kept, not used for results: stab_q0.log (empty first launch), stab_q0_run.log and stab_q0_run2.log (duplicate launches, killed), q0_newton.py/.log (killed before output). In stab_q0_run3.log the charge-0 seed line is an L-BFGS stop at the iteration limit, **not** a critical point; the charge-0 result below is analytic.
- Only status-0 (converged) runs are cited. The T=22 lines in run_bign_Tcheck.log are status 1 and are not used.

## 1. The twist coupling
- **T1 (PROVED).** For a U(1)_{φ₁}-equivariant connection with moment map Φ (dΦ = −ι_ξF in a covariant sense), the connection induced on the twisted fibration S⁴ → M → Σ has curvature F_tot = F_fib^hor + Φ·π*F_tw, with no mixed fibre–Σ legs when F_tw is constant and the field is the same on every fibre. (Standard equivariant/Cartan construction; checked directly: the horizontal lift dφ₁ → Dφ₁ = dφ₁ + A_tw gives F_tot = F^hor + (ι_ξA − Λ)dA_tw.)
- **T2 (PROVED, topological).** For the MN2 twist the normal bundle carrying φ₁ is K_Σ, degree 2g−2. With H² of curvature −1, Area(H²/Γ) = 4π(g−1) = 2π(2g−2), so F_tw = vol_{H²} exactly. (This also matches J1's F⁽¹⁾ = (1+z)/8·vol with Dφ = dφ + 2g_c A at z=1.)
- **T3 (CONDITIONAL on S3, the Witten ansatz).** In the ansatz, A ⊃ ½a(t)x̂·τ dφ₁ and the lift of weight n is −½n x̂·τ, so Φ = ½(a − n)x̂·τ. Smoothness forces Φ = −n at the S² orbit (t=0, where ξ vanishes) and Φ → 0 at the S¹ orbit. The lift weight equals the charge n, so there is no freedom to remove Φ.
- **T4 (PROVED, from the J2 face metric).** Using h = Δ̃^{1/3}[e^{2f}dx² + R_Σ² ds²_{H²}] + (L₇/2)²Δ̃^{−2/3}ĝ, the weighted energy density gains
  s·(c/2)·R⁴(n − a)²/W, with c = ((L₇/2)/R_Σ)⁴ = (2e^{g})^{−4} (L₇ = 1), W = Δ̃, R² = cos²χ/X_b.
  - At the MN2 IR face c = 2^{−0.4} = 0.757858. Along the flow c falls to 0.518 (R/R₀ = 1.1), 0.150 (1.5), 0.0094 (3), 8×10⁻⁵ (10), and → 0 at the UV, where stage 1's untwisted validation applies.
- **T5 (PROVED).** Two energy integrals are needed and are different:
  - the weighted energy e = ∫W·ε dvol (the functional whose critical points solve D(W⋆F) = 0 with the twist source), and
  - the unweighted x-tension e_u = ∫ε dvol₄, which is what enters the integrated 4D Israel tuning (P3c N_req = (2/κ²T)∫|k_x − K|dvol₄) since S^x_x = −ε locally.
  - Stage 1 counted with e. Both are given below. Each is in instanton units; multiply by u for M5 units (PP 5374a906 fix 1).

## 2. MN2 IR face, twist on (run_ir.log; all status 0, rms ≤ 1e-8 at T=12,16 and ≤ 7e-7 at T=20,24; values identical to 7 digits for T=12–24)
| n | e/n (stage-1 model, c=0) | e/n twisted | of which twist | e_u/n twisted |
|---|---|---|---|---|
| 1 | 1.1128744 | 1.1743084 | 0.059452 | 1.0660517 |
| 2 | 0.9900399 | 1.1418220 | 0.145053 | 1.1442263 |
| 3 | 0.9149776 | 1.1681720 | 0.239979 | 1.2291673 |
| 4 | — | 1.2251954 | 0.338676 | 1.3200442 |
| 5 | — | 1.2995830 | 0.439268 | 1.4154555 |
- **S2-1 (CONDITIONAL; S3, S4-applied, S6).** Twisted static critical points exist on the MN2 IR face for n = 1–5, converged and T-independent. The c=0 rows reproduce stage 1 exactly (with converged T=20, 24 runs, replacing stage 1's status-1 evidence).
- **S2-2 (PROVED).** With the twist these are non-self-dual for every n ≥ 1: the twist term sources D(W⋆F_fib) ≠ 0 wherever Φ ≠ 0, and Φ ≠ 0 is forced (T3, S5). So no twisted charged solution is BPS on the fibre.
- **S2-3 (CONDITIONAL; S2-1).** The twist reverses stage 1's trend. e/n no longer falls with n; it rises for n ≥ 2, and the twist share grows about linearly (≈ 0.1n per unit charge). Large n (run_ir_bign.log, status 0, n = 5…160, T=12 vs 16 agree to 1e-7 at n = 20, 80, 110, 160): e(n) ≈ 0.114n² at large n, e.g. e(100) = 1195.04, e_u(100) = 1180.61.

## 3. Palais step (PP fix 2)
- **S4-abstract (PROVED, per PP 5374a906).**
- **S4-applied (CONDITIONAL)** on (a) the 2-function ansatz being all of Fix(G) up to gauge, (b) smooth extension across the S² and S¹ orbits, (c) T → ∞. The twist term is G-invariant and smooth on S⁴, so it does not change this.

## 4. Charge-0 single-block search
- **Q0 (PROVED within the ansatz; the ansatz itself is S4-applied (a), CONDITIONAL).** In the charge-0 sector (lift weight 0, so Φ = a), the only critical point is the vacuum.
  - Step 1: the a-equation is (2Ba′)′ = 2(Ch² + T_t)a with B, C, T_t > 0 and a(0) = a(∞) = 0. Multiply by a and integrate: ∫2Ba′² + 2(Ch² + T_t)a² = 0, so a ≡ 0.
  - Step 2: with a = 0, write ℓ for proper length on B̃ and ρ = W√g_φφ. Then (ρh_ℓ)_ℓ = −ρh(1−h²). Put E = ½h_ℓ² + U(h), U = ½h² − ¼h⁴. Then dE/dℓ = −(ρ_ℓ/ρ)h_ℓ². If ρ is increasing, E falls from U(h(0)) < ¼ and cannot reach U(1) = ¼ at the S¹ orbit unless h ≡ ±1. Smoothness at the S¹ orbit fixes h(∞) = 1, so h ≡ 1.
  - Step 3: ρ ∝ X_b sinχcosχ + X_a sin²χ tanχ, and dρ/dχ ∝ f(σ) := r − 2(r−1)σ + σ/(1−σ), with σ = sin²χ and r = X_b/X_a. Put q = r − 1. For q < ½ the minimum is f(0) = r > 0. For q ≥ ½ it is at 1−σ = 1/√(2q), where f = −q + 2√(2q), which is ≥ 0 exactly when q ≤ 8. So ρ is increasing whenever r ≤ 9. On the MN2 flow r ∈ [1, 2] (run_faces.log; r = 2 at the IR point), so ρ is increasing on every face.
- **Q0-out (OPEN).** Charge-0 saddles with a different symmetry, e.g. Sibner–Sibner–Uhlenbeck-type U(1) actions of cohomogeneity 2, are not covered. SSU (PNAS 86 (1989) 8610) is cited for the round S⁴ only, and its math is not checked here.
- **Consequence.** A charge-0 single block cannot supply chargeless tension in this class; the chargeless tension must come from mirror pairs.

## 5. Mirror pairs, recomputed
- **MP1 (PROVED).** The mirror block (pull-back by φ₁ → −φ₁, weight −n) has Φ′ = −Φ, so |Φ′| = |Φ| and the twist energy is the same. A mirror pair (n, −n) is still a critical point (commuting blocks decouple), with e = 2e(n) and e_u = 2e_u(n).
- **MP2 (PROVED).** At most 8 mutually commuting SU(2)s fit in E₈: commuting SU(2)s have commuting Cartan generators spanning a torus of dimension equal to their number, and rank E₈ = 8. SO(16) ⊃ SO(4)⁴ ⊃ SU(2)⁸ realizes 8, each of Dynkin index 1 (16 → 2·**2** + 12·**1** per SU(2), as PP checked). So a fibre-uniform E₈ field carries at most 4 mirror pairs.
- **S11-real (REFUTED as a description of a realizable configuration; proof = MP2 + S5).** Stage 1's "1262 to 2923 pairs" (u=1; PP: 631–1462 at u=2) assumes independent charge-1 pairs added together. A static fibre-uniform field is equivariant (S5), each SU(2) block is one equivariant connection, and there are at most 4 pairs (MP2). So more than 4 separate pairs cannot occur. Their sum is kept below only as a comparison figure.
- **S11-count (CONDITIONAL; S2-1, S2-3, and P3c's 4D-only tuning, which is itself not a solution).** The counts needed to meet the MN2 excess, in both normalizations:

| how the excess is met | u = 1 (Conrad/Lü) | u = 2 (HW printed λ²) |
|---|---|---|
| comparison only: independent n=1 twisted pairs, fixed IR pair energy 2.348617 (e) / 2.132103 (e_u), excess 2808.6 → 6506.7 | 1196 → 2770 (e); 1317 → 3052 (e_u) | 598 → 1385 (e); 659 → 1526 (e_u) |
| comparison only: per-face pair energy (run_faces.log), IR → UV | 1196 → 3253 (e); 1317 → 3253 (e_u) | 598 → 1627 (e); 659 → 1627 (e_u) |
| stage-1 numbers, untwisted pair 2.2257 (PP fix 1) | 1262 → 2923 | 631 → 1462 |
| **one mirror pair (n, −n) at the IR face, 2u·e(n) = 2808.6** | n ∈ (105, 110] (e and e_u) | n ∈ (75, 80] (e and e_u) |
| **four equal mirror pairs at the IR face** | n ∈ (50, 55] | n ∈ (36, 37] |
| one block of charge n plus 9760 − n M5s, u·e(n) − n = 2808.6 | n ∈ (155, 160] (e); n > 160 (e_u, just beyond the computed range) | n ∈ (110, 115] |
| UV end (round, c → 0, BPS, e = e_u = n): one mirror pair | n = 3253 | n = 1627 |

  - Interior faces (run_faces.log, status 0 everywhere): N_req(x) − 9760 = 2817.7 (R/R₀ = 1.001), 3590.5 (1.1), 5096.7 (1.5), 6184.4 (3.0), 6480.0 (10), → 6506.7 (UV). The n=1 pair energy falls from 2.3475 to 2.0000 over the same range.
- **S12′ (CONDITIONAL; replaces stage-1 S12, which was in the untwisted model).** With the twist, the single-block tension/charge ratio u·e_u/n is 1.066, 1.144, 1.229, 1.320, 1.415 for n = 1…5 at u=1. It passes the IR threshold 1.288 at n = 4. At u=2 every n exceeds it. So in magnitude the count gap closes on the MN2 IR face, with a few blocks of moderate charge, under either u.

## 6. Interior flow faces (run_faces.log)
- **S2-c (CONDITIONAL; J1b flow, S3, S4-applied).** Twisted critical points exist for n = 1, 2, 3 on every face sampled (R/R₀ = 1.001, 1.1, 1.5, 3, 10). The twist share falls with c: e(1) = 1.1737, 1.1264, 1.0420, 1.0030, 1.0000. X₀ = X₂ holds to the printed digits on every face, so the SO(3)×U(1) reduction applies unchanged.

## 7. Second variation (stab_q0_run3.log; discrete midpoint functional with analytic Hessian, N = 4000, T = 12)
- **ST1 (CONDITIONAL; discretization, (h, a) sector only).** At the twisted IR solutions n = 1, 2, 3, the untwisted IR solutions and the round BPS solutions, the discrete relaxation leaves E unchanged to 6 digits (max |Δh| ≤ 3×10⁻⁴), and the four lowest L²-normalized Hessian eigenvalues are all positive (5.8×10⁻⁵ … 3.8×10⁻⁴ on MN2; 1×10⁻⁴ … 8×10⁻⁴ round). There are no negative modes in the equivariant (h, a) sector. The smallest eigenvalues are far-end a-modes and approach 0 as T grows, which is a cutoff effect, not instability.
- **ST2 (OPEN).** Stability outside this sector is not checked: the phase/a_t sector, non-equivariant modes, and the off-block E₈ modes of the pair in (2,2)⊗**12** and (2,1)⊗**32**, (1,2)⊗**32′**. Bourguignon–Lawson-type results on S⁴ ([F⁺, F⁻] = 0 for stable fields) are recalled but not checked and do not apply directly to the weighted, twisted problem.

## 8. Existence status
- **Y14 (CONDITIONAL; stage-2 model with twist).** Non-BPS static E₈ fields exist on the MN2 IR face and on every interior face sampled, for n = 1–5 (IR, up to 160), in one SU(2) block, and as mirror pairs of every charge. They are stable in the equivariant (h, a) sector. Y14 stays **OPEN** overall until S4-applied (a)–(c), S6 and ST2 are settled. Stage 2 does not kill existence, so Y15 is run (separate file).

## 9. Effect on the gap and the junction
- **Count gap.** It closes in magnitude (CONDITIONAL, S11-count, S12′), but not as stage 1 described it: a few large-charge mirror pairs, not ~10³ unit pairs. Both u values are given above.
- **Junction (unchanged, UNSOLVED).** PP 5374a906 confirms the fibre-NEC no-go for every E₈ field, pairs included. The twist adds only Σ-legs, which make it worse (see Y15).

## 10. Next steps and ETAs
- S4-applied (a)–(c): ansatz completeness and regularity, 2–3 h.
- ST2, off-block and phase-sector stability of the pair, 3–4 h.
- Q0-out, SSU-type charge-0 saddles on the weighted fibre, 3–5 h.
- Σ-non-uniform (Bolza-invariant, OW 49b04146 scope) configurations: days.

## Tally (header checked against the item lists)
| label | count | items |
|---|---|---|
| PROVED | 8 | T1, T2, T4, T5, S2-2, Q0 (within the ansatz), MP1, MP2 |
| CONDITIONAL | 9 | T3, S2-1, S2-3, S4-applied, S11-count, S12′, S2-c, ST1, Y14 |
| OPEN | 2 | Q0-out, ST2 |
| REFUTED | 1 | S11-real |

Check: 8 + 9 + 2 + 1 = 20. S4-abstract is PP's PROVED item (5374a906), restated and not re-counted.

Supersedes NL_DERIVED_Y14_NONBPS_E8_EXISTENCE_MN2_STAGE2_2026-11-09_1945.md (same content; that draft had a garbled Q0 step-3 formula and a malformed tally block; kept, not overwritten).

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
