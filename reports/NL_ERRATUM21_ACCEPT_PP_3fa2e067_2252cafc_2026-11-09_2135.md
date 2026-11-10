# NL ERRATUM 21 — accepting PP 3fa2e067 (audit of five t4426 light-queue files) and PP 2252cafc (audit of Erratum 20 and the D6 checkpoint)
2026-11-09, 2135 CST (America/Chicago). **NL derived proposal.** Additive only: no target file is edited. Authority: OW t4426 d5eaeef3 ("Pursue all open"); the 90% usage stop is lifted per OW t4431 (record f700141d…). Nothing adopted. **Junction: UNSOLVED. Count gap: unchanged.**
Sources (sidecars OK):
- FINDINGS_PP_AUDIT_NL_t4426_FIVE_FILES_2026-11-09_2122.md (3fa2e0673fcdfcc140eb0688bc89c3e9e538d6744ae0d908656f50ce5c4a20ef)
- FINDINGS_PP_AUDIT_NL_E20_AND_D6_2026-11-09_2123.md (2252cafc7b2281372dce5f30d71b1d62dc0977f64ffd2ab2e91bdc76aafb6eb3)

Targets (sidecars OK; none edited):
- NL_DERIVED_F9_MAP_CHECKS_CONJUGATE_C2_2026-11-09_2006.md (78332e74…)
- NL_DERIVED_Y15_TRR2_PER_DIRECTION_NULL_2026-11-09_2026.md (21045043…)
- NL_DERIVED_Y15_NEC_ESCAPE_LIST_MN2_2026-11-09_2029.md (b2b14488…)
- NL_DERIVED_A2_CGR_26_CLP_MN2_4FORM_2026-11-09_2049.md (ed2aa562…)
- NL_ERRATUM18_ADDENDUM_PP_CONFIRM_E17_c90b4fba_2026-11-09_2010.md (eaef6139…)
- NL_NUMBERING_NOTE_ERRATUM18_COLLISION_2026-11-09_2020.md (81d52ae0…)
- NL_ERRATUM18_B12_D4_CONSTANT_2026-11-09_2019.md (92dded27…; cite as "Erratum 18-B12")
- NL_ERRATUM20_ACCEPT_PP_8c57e68b_0a82cf18_2026-11-09_2056.md (6b10854d…)
- NL_DERIVED_BPS_D6_NONLINEAR_RCHI_KSE_2026-11-09_2100.md (ff2c74bc…)

Scripts, new dated directory `/workspace/nl-e21-2132/`. Each `.py` sidecar was frozen before its run; each `.log` sidecar was written after the run (disclosed).
- e21_checks_2026-11-09_2132.py = 6067be4cba08815fba50455c98c5ae24b563e9bd7e510f3c3abcc232c109b89c, log 964cb5770b0595cba0c62bcf6e027df70693f3608627a0b0c2654753966e43bc
- e21_z1_check_exponents_2026-11-09_2132.py = a3847a2c144db119046f5f1d2d4c834b7aa98771f046ac487f4c3c8e41ec73d8, log 434a2e727b5a370e6ce200ebaf31c194d77fc5f8540f464aa57d3250a69572e1
- e21_a2_identities_2026-11-09_2132.py = a1ecf72125253fa6a46e0f6668a53d0126782a608cdb9f7b5f52e6c30fcd2bfe, log a2bbd5463056275f0192d8b2f3b4d5f9baf11f5a9ec8eff1d3f179b0483fa8cb
The original `/workspace/nl-e20-z1/z1_check.py` is not edited. PP's exact scripts are cited, not copied: `/workspace/pp-a2-exact-2026-11-09/pp_a2_frame_exact_2026-11-09_2120.py` (8a3e4c6c…, log 1e40f493…), `pp_a2_flux_fix_2026-11-09_2124.py` (83772b5b…, log 6b7e0663…), `/workspace/pp-d6-exact-2026-11-09/pp_d6_exact_2026-11-09_2112.py` (c39b3a85…, log de12f16e…).
Limits: no CERT, no Gemini, nothing sent, no agent messaged. Naming per OW f1d167d1: where the algebra is named it is "resonant algebra" (it is not named in this file). Tip 7cddb188… checked before and after. PP's math was re-checked where it is used here; no item was disagreed with.

**Tally: PROVED 5 · CONDITIONAL 1 · OPEN 0 · REFUTED 0 · total 6**
(Bookkeeping, wording, coverage and disclosure rows in §§1–7 are hygiene and carry no label. Revised tallies of the target files are recorded in §8 and are not re-counted.)

## 1. F9 map (2006): wording fix F9-1
- **E21-1 (PROVED; exact 2×2 algebra).** T1 = (A₀⊗P₂)∘K, with P₂ = diag(0,1), is **antilinear but not antiunitary**: rank P₂ = 1, so T1 has a nontrivial kernel and is not invertible, and "T1⁻¹" is undefined on the whole space. The F9-b result is the intertwining **T1 U(θ) = U(−θ) T1**. The phrase "T1 U T1⁻¹ = U(−θ) on the range of T1" is dropped. "Commutant" means the solution set of P₂Ū = UP₂. F9-cex and F9-b stay PROVED. The 2006 tally stays **2/0/0/0**.

## 2. tr R² per direction (2026): grade change and exact UV supply
- **E21-2 (CONDITIONAL; accept PP T2-1).** R2-Y16 is moved from PROVED to **CONDITIONAL**: ∫Riem² = 1038.933973 and the 3.2896 M5-unit figure are n = 24 Gauss–Legendre quadrature (float). A float reproduction of a float number remains float-only. R2-round and R2-chi stay PROVED. The revised 2026 tally is **PROVED 2 · CONDITIONAL 6 · OPEN 1 · REFUTED 0**.
- Hygiene (no label), accepting T2-2, T2-3, T2-4:
  - R2-C4 is a restatement of K4 and carries **no label** (the 2026 tally already excluded it; the in-text "(PROVED, given K4 …)" is dropped).
  - "Smoothness of the curvature on the compact S⁴ precludes a jump by 10² in the last 1% of Δ̃" is a **heuristic, not a bound**. The I-value at the X₁ pole was not evaluated analytically.
  - The pointwise UV comparison uses an **approximate** k in |S_req| ≈ 2/(L₇ κ²).
- **E21-3 (PROVED; exact; accept T2-5, independently re-derived).** On the unit (or any-radius) round S⁴, ∫Riem² dvol = 24·(8π²/3) = 64π². With c = 1/(8λ²) and λ² = (2π)⁷·(2/u), one has c = u/(16(2π)⁷). With T_M5 = (2π)⁻⁵,
  c·64π²/T_M5 = [u/(16(2π)⁷)]·64π²·(2π)⁵ = u.
  The signed UV integrated supply is therefore **exactly −u M5 units**. (The 2026 text already stated the value −u; this is the exact derivation.) The pointwise UV ratio stays CONDITIONAL (R2-UV), because of the approximate k.

## 3. NEC escape list (2029): wording; tally unchanged 5/3/3/1
Hygiene (no label); the 2029 claims keep their grades. Accepting N3-1..4.
- **E2-MO5** stays REFUTED, now presented as a **proof**, not a counterexample. Premise: thin-brane stress (ρ_i = σ_i, P = −σ_i along the worldvolume, 0 transverse); worldvolume-flux stress belongs to E3. Every 6D-worldvolume object filling ℝ^{1,3} has p = 2 internal directions, so the internal trace is −2Σσ_i = −2ρ, against the −8ρ required by P_e = −8k/κ² and ρ = 6k/κ² (equivalently −12 versus −48 in units k/κ²). This fails for every choice of signs and smearings, since ρ ≠ 0.
- **E6-sign** stays PROVED, reworded: if the UV side is kept, ρ = −6k/κ² and P_e = +8k/κ², so **ρ + P_e = +2k/κ² ≥ 0 and NEC holds**. The obstruction is ρ < 0, a violation of the **weak** energy condition (WEC), not of NEC. In constituent form some σ_i < 0, so the escape still reduces to E2.
- **E1-C4:** k_x = 0 makes every K vanish (a trivial face). A nontrivial E1 realization needs **k_x > 0**.
- **Z2** is covered by E20-6 (the 2029 file predates Z2; this is not an error in 2029).

## 4. A2 4-form (2049): exact basis; tally unchanged 2/0/3/0
The 2049 PROVED labels now rest on exact symbolic proofs, not on the 3.5×10⁻¹⁵ component match or the 36×36 quadrature (those remain float cross-checks). Sign and orientation: in the coframe with Φ₁ = dφ₁ + du/v (a determinant-1 shear, so Hodge duals and orientation are unchanged), and on the fundamental domain α∈[0,π], β∈[0,π/2], φ_i∈[0,2π),
**∫_{S⁴} G₄(CGR) = −8π²/g³**
(= −π² at g = 2), and the CLP side is +8π²/g³ by A2-comp. This is the signed value, not only the magnitude.
- **E21-4 (PROVED; exact, independently re-derived).** The fibre component is G = U Δ⁻² sin³α sinβ cosβ / g³, with det[μ|J] = −sin³α sinβ cosβ (exact; e21_a2_identities). Δ and U depend only on s = μ₁²: Δ = b−(b−a)s, U = 2(a²s + b²(1−s)) − Δ(2a+3b), a = 2⁻³/⁵, b = 2²/⁵. The angular measure pushes forward by the change of variables t = cos²β, x = cos α, s = (1−x²)t, which gives
  ½∫_{-1}^{1}∫_0^{1-x²} F(s) ds dx = ∫_0^1 F(s)√(1−s) ds
  for every integrable F (switch the order: |x| ≤ √(1−s)). Substituting s = 1−v², the integrand is exactly −4v²(v²+3)/(v²+1)², whose integral is
  −4[1 + π/4 − 2(π/8 + 1/4)] = −2.
  Hence ∫_{S⁴} G₄(CGR) = (2π)²·(−2)/g³ = −8π²/g³. The same integral equals −2 for every ratio k = X₀/X₁ on the X₀ = X₂ line. A direct 2D quadrature of the (α,β) integrand also returns −2.0, and (2π)²(−2)/g³ matches −8π²/g³ to the printed digits. (A side note, not a disagreement: PP's `pp_a2_flux_fix` sympy test of the push-forward on F = 1/(1+s) printed False; the identity holds for that F by the change of variables and by a 2D quadrature with residual 0.0. PP's integral evaluation itself is correct.)
- A2-comp is accepted as **PROVED (exact, PP)**, as the basis of the existing 2049 label, and is not re-counted here. PP's Groebner reduction shows CGR (2.6) + ⋆₁₁ CLP (4.2) = 0 on all four frame components, for all (z, v, u) and all angles in the fundamental domain, modulo Y⁶ = Δ and sin²+cos²=1, in the coframe Φ₁ = dφ₁+du/v. Supporting identities were re-derived here and hold exactly: U_CLP = g U_CGR at MN2; det[μ|J] = −sin³α sinβ cosβ; Δ and U are functions of s = μ₁² only. The full component Groebner was not re-implemented in this erratum; it is cited from pp_a2_frame_exact (8a3e4c6c… / 1e40f493…). The first flux line of that script used a wrong push-forward constant 2/3 and is superseded by pp_a2_flux_fix and by E21-4.
- Hygiene (no label), accepting A2-a, A2-d, A2-e:
  - The 2048 flux "log" (68357b21…) has **no script** on disk; it is a hand-written summary of interactive runs and is not reproducible. The exact proof above replaces it.
  - The 2035 and 2040 compile-failed drafts have **no sidecars**.
  - The 2041 `.py` sidecar was written at 20:49, after the 20:41 run (the `.py` mtime is 20:40:19). "Frozen before execution" in 2049 rests on that mtime only; the sidecar is a **post-run** integrity sidecar.

## 5. E18 Addendum (2010) and Numbering note (2020): faithful; timestamp nits
Hygiene (no label). Both files are faithful. Two metadata nits, no grade effect:
- **B-1.** The Numbering note's header says 20:19 CST, against filename `_2020` and mtime 20:20:08 CST (America/Chicago).
- **B-2.** Erratum 18-B12 is named `_2019` but was written at 20:18:22 CST (America/Chicago).

## 6. Erratum 20 (2056): faithful; distinct tally 2/0/1/0; μ exponents printed
Hygiene (no label), accepting E20-a and E20-b. Erratum 20 is faithful to H1–H4, Z1, Z2 and the re-scoping. Its printed 6/0/1/0 is arithmetically correct as a row count. The distinct new mathematical claims are **PROVED 2 · CONDITIONAL 0 · OPEN 1 · REFUTED 0** (E20-5, E20-7; E20-6):
- E20-1, E20-2 and E20-4 are bookkeeping and now carry **no PROVED label**.
- E20-3 restates E19-15 and is not re-counted.
The μ exponents were re-derived and printed in e21_z1_check_exponents (the original z1_check.py is untouched). From μ² − 4μ − m²L² = 0:
- m²L² = 12: μL ∈ {−2, 6};
- m²L² = −4: μL ∈ {2} (double root);
- m²L² = 0: **μL ∈ {0, 4}**.
This confirms E20-5 and is not a new claim.

## 7. D6 checkpoint (2100): exact D2 and leading-order c; tally unchanged 4/2/2/0 PARTIAL
- **E21-5 (PROVED; exact).** For the D6-2 data, tr M = −2(α+β₁+β₂) = −12k_x, so **D2 (K_int = −6k_x) holds identically** for all (α, β₁, β₂). Equivalently NEC ⇔ β₁+β₂ ≥ 0 and α+βᵢ ≥ 0 (i=1,2), and the sum of the three NEC combinations is 12k_x. In the example α = β₁ = β₂ = b > 0, the relation b = 2k_x **holds identically**; it is not an extra condition. D6-2/3 stay PROVED. Local data remain consistent and are still not a wall.
- **E21-6 (PROVED, leading order; independently re-derived).** The slow-manifold coefficient is
  c = −(L/4)·(1/3)·(½)∂³_wV = 2^{2/3}g² L = **2^{4/3} g > 0**
  (2.5198 at g = 1). Only w < 0 creeps into MN2 (w(r) = −1/(c r − 1/w₀) is global and tends to 0⁻ for w₀ < 0; for w₀ > 0 it blows up at r = 1/(c w₀)). The slaved shift is **exactly (δφ, δλ) = (1/5, 13/30) w²**. D6-6 stays PROVED as this leading-order reduction. Existence of genuine second-order flows with this asymptotics rests on the **centre-manifold theorem as a cited premise**; that part is not proved here.
- Hygiene (no label), accepting D6-a, D6-d, D6-e:
  - The Z2 scan stays CONDITIONAL and does not close Z2 (E20-6 remains OPEN). "48 flows" is **36 real flows** on z2_scan_v3 (4×13 = 52 grid points, 16 skipped for non-real A') plus **12 flows** on z2_centre_flow_faces, a different grid (w₀ ∈ {−0.02, −0.05, −0.10, −0.20}, d₆ ∈ {−0.02, 0, +0.02}). The 2100 text's grid describes only the 36. The crashed z2_scan_wide (9 flows before the crash) is not in the 48.
  - D6-8 stays OPEN. The clause "Within the truncation that family fails the 11D NEC (D3, D6-7)" **mixes a PROVED result (D3, W-flows) with float-only evidence (D6-7, Z2 flows)**. The two must be stated separately.
  - The kept z2_scan_wide log is **stdout only**. It does not contain the RuntimeWarning or the ValueError traceback ("initial state y0 must be finite").

## 8. Revised tallies of the audited files
| file | before | revised | change |
|---|---|---|---|
| F9 map (2006) | 2/0/0/0 | **2/0/0/0** | wording only (E21-1) |
| tr R² (2026) | 3/5/1/0 | **2/6/1/0** | R2-Y16 → CONDITIONAL; R2-C4 unlabelled |
| NEC escape list (2029) | 5/3/3/1 | **5/3/3/1** | wording (MO5 as proof; E6 = WEC; k_x > 0); Z2 via E20-6 |
| A2 4-form (2049) | 2/0/3/0 | **2/0/3/0** | both PROVED now exactly; signed flux |
| E18 Addendum (2010) | 1/0/0/0 | **1/0/0/0** | faithful |
| Numbering note (2020) | 0/0/0/0 | **0/0/0/0** | faithful; nits B-1, B-2 |
| Erratum 20 (2056), distinct | 6/0/1/0 (row count) | **2/0/1/0** distinct | E20-1/2/4 unlabelled bookkeeping; E20-3 = E19-15 |
| D6 checkpoint (2100) | 4/2/2/0 PARTIAL | **4/2/2/0 PARTIAL** | D2 an identity; c and slaving exact at leading order; Z2 count 36+12 |

## 9. Junction / gap
No change. **Junction UNSOLVED; count gap unchanged.** Nothing adopted. D6 and Z2 stay OPEN. No item of PP 3fa2e067 or 2252cafc was disagreed with.

## 10. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 5 | E21-1, E21-3, E21-4, E21-5, E21-6 |
| CONDITIONAL | 1 | E21-2 (R2-Y16 grade) |
| OPEN | 0 | — |
| REFUTED | 0 | — |

Check: 5 + 1 + 0 + 0 = 6.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
