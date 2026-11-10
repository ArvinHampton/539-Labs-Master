# FINDINGS — PP gate audit of MR2 full-11D EOM / Riemann / systole file (9ab8f0a6) + erratum (2efef556) — 2026-11-09 18:05 CST (America/Chicago)
Auditor: PP (Professor Proof). Pure math. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING; refutation only by proof or counterexample.
Limits: new file only; nothing edited or overwritten. No CERT. No Gemini. Nothing sent to anyone. Outside reads: public arXiv only (BBBW arXiv:1203.0303 PDF §3–4 read for its eqs (3.5), (4.2), (4.5); every citation CONDITIONAL). **Nothing adopted.**
Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — MATCH at start and at write time (untouched).
Follows PP fc5e0156 (FINDINGS_PP_AUDIT_MR2_V2_JOINT_TABLE_EFT_REAUDIT_2026-11-09_1733.md).

## 0. Authority records (PROVED: on disk, sidecars MATCH, wording quoted)
- **OW 587eca0c** (OWNER_WRITE_MAINCHAT_t4365_VACUUM_HOLD_UNTIL_MR2_FULL11D_CURVATURE_SYSTOLE_PP_AUDIT_2026-11-09_1737.md, sha 587eca0c108f39b15c8d2f372861087ed03796dc28f9a49449f95db0dead7fcf). Owner's words: "As mine: keep the vacuum on hold until MR2's full 11D equations, curvature invariant and systole file lands and PP audits it." Release condition as recorded: MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09.md (+ .py/.log/sidecars) filed, then a PP audit of it. This hold extends aaadb280.
- **OW 7ff8299d** (OWNER_WRITE_MAINCHAT_t4377_QUEUE_JOBS_NL_E8_STRESS_MR2_WALL_CURVATURE_BOLZA_GAMMA_2026-11-09_1753.md, sha 7ff8299dbcaf3b526936b40a9e24d8b9e58edf13fd9a9a93e822a92ca82a16ac, mtime 17:54:02 CST). Owner's words: "As mine: approve both queue jobs (NL E₈ instanton stress-energy, MR2 wall-boundary curvature for MN N=2) and adopt Bolza for Γ. Nothing else from the pasted text." Adopted item 3: "Γ := Bolza surface (genus 2) for Σ." The same OW also restates: "Vacuum on HOLD (587eca0c) pending PP's audit of MR2 9ab8f0a6."

## 1. MR2 files (PROVED: all MATCH their sidecars)
| file (reports/) | sha256 prefix |
|---|---|
| MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09.md | 9ab8f0a6 |
| …_FULL_EOM_2026-11-09.py (superseded v1) / .log | e2a1f02d / 71227fdb |
| …_V2.py / _V2.log | ad134752 / 49d0562c |
| …_V2_PERPOINT_DIAG.py / .log | 31e40b87 / 4af22ea5 |
| …_V2_POLE_PRECISION_CONVERGENCE.py / .log | 784585e4 / 4b2a36d6 |
| …_V2_SYMBOLIC_MAXWELL.py / .log | b28db23b / 72665f47 |
| MR2_ERRATUM_PER_PP_V2_JOINT_EFT_REAUDIT_2026-11-09.md | 2efef556 |
PP scratch is in /workspace/pp_gate_1750 (sha256 prefixes):
- scripts: pp_maxwell_sym.py dd4e01920da86656, pp_maxwell_exact.py 6730c30d42990538, pp_einstein.py c1a5a8e682dd2e08, pp_controls.py 53b29433c95661c8, pp_curvmax.py 0b2090a2846ee443, pp_bolza.py 8acd93fa5b71cce2, pp_riemann.py fd1486cdb422cdb2
- logs: einstein60.log 1706f8ae0ef10707, einstein90.log dc7e147b6f91057c, controls.log 723a4dc867191d10, curvmax_*.log (MN1 41bb8a0a…, MN2 0a811739…, z2 5a1fee66…, z3 e67605ff…)

PP's Einstein, Maxwell and Bolza code is my own. Only the metric (mr2_core = MR2 V2 lines 1–187, audited in fc5e0156) is shared with MR2.

## 2. Validations — PROVED
- AdS₇×S⁴ (R_AdS = 1, S⁴ radius ½): MR2 prints K = 468, Ric² = 828, R = 6 and max|eig Q| = 4. I re-derived each exact value:
  - K = 2·7·6 + 2·4·3·16 = 84 + 384 = 468
  - Ric² = 7·6² + 4·12² = 252 + 576 = 828
  - R = −42 + 48 = 6
  - max|eig| = 1/(½)² = 4, with the AdS eigenvalues at −1
  - The wrong-flux ×1.1 control gives 2.52 at both points (it fails).
- (D) product: K = 618, Ric² = 828, R = 6 and max|eig Q| = 6. These are exact, including at (1e-6, 1e-6). My own code gives Riem² = 618 and eig Q ∈ [−6, 4] at all 60 points (fc5e0156).
- Cosmetic: md §0 says "e^{2f} = 4/9 so that L_AdS5 = 2/3". The code uses F0 = e^{2f} = 2/3, i.e. L² = 2/3, and the exact value 40·9/4 = 40/L⁴ has L⁴ = 4/9. The numbers are right; the sentence is wrong.

## 3. Last G₄ coefficient and the normalization map — PROVED (arithmetic; citations CONDITIONAL)
- MR2 normalization: Dφ_i = dφ_i + a_i du/v, F̂^i = a_i du∧dv/v².
- CLP hep-th/9903214 (4.2), with g = 2: Dφ_i = dφ_i + gA^i, so A_CLP = a_i du/(2v) and F_CLP = F̂/2. The coefficient 1/(2g²) = 1/8 times *₇F_CLP is the same as **1/16 times *₇F̂**.
- BBBW 1203.0303:
  - (4.2) has dφ_i + 4A^(i) and (4.5) has coefficient ¼ (rendered "14" in the PDF text), with F = dA.
  - (3.5) gives F^(1)_{x₁x₂} = p/(8(g−1)x₂²), with p = (1+z)(g−1) = 2a₁(g−1), so F_BBBW = (a₁/4) dx∧dy/y² = F̂/4.
  - Hence ¼·*₇F_BBBW = (1/16)·*₇F̂.
- **ours 1/16 = CLP 1/8 = BBBW ¼: all three agree.** MR2's claim is CONFIRMED.
- PP self-correction to fc5e0156 §4: there I wrote that BBBW's ¼ "looks inconsistent". It is correct in BBBW's own conventions (A_BBBW = A_CLP/2 = a/4). The only defect was carrying ¼ into MR2's F̂ normalization, which MR2 has now fixed.
- I also checked the other terms against BBBW (4.2)/(4.5): U = 4Σ(X²μ² − ΔX) + 2ΔX₀, the warp ¼Δ^{-2/3}ds₄², and e^{f₀} = (X₁X₂)².

## 4. Maxwell and G∧G — PROVED identically (independent)
- I built Ω = *G₄ myself from CLP (4.2), with λ_CLP free, using my own wedge and d code. dΩ has exactly 2 components, (0–6,α) and (0–6,β).
- Symbolically, Maxwell is equivalent to two polynomial identities in (X₁, X₂, G₀, a_i, λ_CLP), shown in the pp_maxwell_sym output.
- Substituting the exact BBBW (3.8) fixed point and **λ_CLP = 1/8**, sympy gives **0 exactly** for every coefficient, for all four candidates (pp_maxwell_exact). For MN1 the β component vanishes identically (X₁ = X₂, a₁ = a₂), as MR2 reports.
- λ_CLP = 0, 1/16 and 1/4 leave O(10⁻²–1) residuals.
- So Maxwell both forces λ and reproduces the fixed-point relations, which is a non-trivial cross-check.
- G∧G ≡ 0: every G₄ component has legs only in the 6 internal directions (5–10) (my Hodge code), and an 8-form on 6 directions vanishes.

## 5. Einstein, all components — PROVED at the sampled points; "all points" CONDITIONAL
- I used my own Christoffels, Ricci, Ω and a block Hodge star (Euclidean t; E^M_N is unchanged by the Wick rotation because G₄ is internal). The residual is frame-normalized: max|E| in an orthonormal frame divided by the frame max|Ric|.
- 12 points per candidate:
  - 4 generic points
  - 3 near μ₁ = 1: (π/2+1e-3, 1e-3), (π/2−1e-4, 1e-5), (π/2+2e-2, 1e-2)
  - 1 near μ₂ = 1
  - 4 corners: (1e-6, π/2−1e-6), (π−1e-5, π/2−1e-5), (1e-4, 1e-4), (π−1e-6, 1e-6)

| candidate | generic (dps 60) | near μ₁=1 (dps 60) | worst corner (1e-6, π/2−1e-6): dps 60 → 90 |
|---|---|---|---|
| MN1 | ≤ 1.0e-59 rel | ≤ 1.5e-51 rel | 3.5e-26 rel (dps 60) |
| MN2 | ≤ 1.3e-59 | ≤ 6.3e-52 | 2.7e-26 |
| BBBW z=2 | ≤ 1.6e-59 | ≤ 1.7e-52 → 3.4e-82 (dps 90) | 9.3e-27 → 2.0e-56 |
| BBBW z=3 | ≤ 7.4e-60 | ≤ 2.1e-52 → 4.5e-82 (dps 90) | 1.7e-26 → 1.8e-56 |

- This independently reproduces MR2's precision ladder: about 3e-5 at dps 40 (MR2), about 2–4e-25 absolute at dps 60, and about 2–5e-55 at dps 90. The residual is round-off at the coordinate poles.
- **"All points" stays CONDITIONAL.** It rests on the CLP consistent-truncation theorem plus BBBW's 7D BPS solution (both literature), or on a future symbolic simplification of E_MN.
- Gap in MR2: the PERPOINT_DIAG log has **no BBBW z=2 rows** (only MN1, MN2, z=3), even though the md describes per-point coverage. My run covers z=2.

## 6. Controls are discriminating — PROVED
At 2 generic points, frame-relative residuals:
- **True solution:** about 1e-60.
- **Large perturbations:**
  - λ_CLP = 0: 0.05–0.15
  - λ_CLP = 1/4 (BBBW's number misread): 0.15–0.44
  - λ_CLP = 1/16 (MR2's number misread): 0.04–0.11
  - flux κ = 1.1: 0.21
  - X₁×1.1 (f, g recomputed consistently): 0.10–0.13
- **Linear response:** λ×(1+1e-6) gives 1–3e-7, κ = 1+1e-6 gives 2.0e-6, and X₁×(1+1e-6) gives 1.3–1.6e-6.
- So a 10⁻⁶ deformation is detected about 53 orders of magnitude above the floor. The controls test the solution, not just "large" numbers. MR2's coordinate-mixed values (1.66e5 / 4.62e5 / 2.2e6 / 4.3e8) are large partly because coordinate components near the poles are about 1e6 in size. The frame-relative numbers above are the meaningful measure.

## 7. Bianchi dG₄ = 0 — PROVED at the sampled points; MR2's control is not discriminating
- My central finite difference (h = 1e-22, dps 60) at 3 points per candidate, including near μ₁ = 1 and a corner, gives max|dG| ≤ 3.9e-40, against |G| up to 0.21. That is the FD floor. MR2's ≤ 5.7e-25 (h = 1e-12, dps 40) is also at its floor: CONFIRMED.
- λ_CLP = 0 gives |dG| ≈ |G| (for example 0.102 for MN2 at (1, 0.5)), so Bianchi does depend on λ.
- X₁×1.1 **passes** Bianchi (≤ 6e-40), and so does flux ×1.1 (it is a pure rescaling). MR2's dG test therefore has no failing control: its λ controls skipped dG, and its X₁ and flux controls cannot fail it. **Fix needed.**

## 8. Curvature invariants and the global maximum
- MR2's maxima of ℓ_p²√Riem² (1.22e-2 / 2.36e-2 / 3.07e-2 / 3.47e-2), of max|eig Q| (6.629 / 13.333 / 18.849 / 21.890 per ℓ²) and of ℓ_p²|K_sec| (2.685e-3 / 5.401e-3 / 7.636e-3 / 8.868e-3) match mine to every digit. **PROVED at the sampled points.**
- **Location of the maximum.** A new PP scan (96-point 2D grid plus approach sequences to μ₀, μ₁, μ₂ = 1) puts the maximum **at the μ₁ = 1 pole (α = π/2, β → 0)** for MN2, z=2 and z=3, and at μ₁ = 1 or μ₂ = 1 for MN1 (symmetric). Limits:
  - MN1: Riem² → 910.3717, max|eig| → 6.62902
  - MN2: Riem² → 3408.000, max|eig| → 13.33333 (40/3)
  - z=2: 5755.4016 and 18.84928
  - z=3: 7318.5635 and 21.89035
  
  The change from the sampled maxima is below 1e-5 relative, and the Planck-unit values are unchanged at the quoted digits.
- MR2 md §1 says the maxima "sit on the β = π/2−1e-6 / α-pole edges". That is inaccurate. Fix.
- **Global sup: CONDITIONAL.** The numerical scan is strong evidence but not a proof.

## 9. Which estimator for higher-derivative corrections — the estimator choice is PROVED; the size is CONDITIONAL
- Every orthonormal-frame component satisfies |R_abcd| ≤ ‖Q‖ = max|eig Q|, since R_abcd = ⟨e_a∧e_b, Q e_c∧e_d⟩ (PROVED). So the parametric size of the ℓ_p⁶R⁴ correction relative to the two-derivative terms is **(ℓ_p² max|K_sec|)³ ≈ 1.9e-8 / 1.6e-7 / 4.5e-7 / 7.0e-7**.
- √Riem² is the Frobenius norm. It over-counts component multiplicity: √Riem²/max|eig| ≈ 4.5–7.9 here, so its cube is about 90–500× larger. It is a conservative envelope (1.8e-6 to 4.2e-5), not the right parametric estimate.
- Neither includes the numerical R⁴ coefficient or the index-contraction combinatorics, so the absolute size stays CONDITIONAL. The verdict does not change: corrections are ≪ 1 either way.
- Supporting calibration (CONDITIONAL): the exact finite-N a differs from large-N by −1.4e-8 to −2.4e-8 (V2 log §4). Those subleading terms come from the same eight-derivative sector, and they agree in order with the sectional-curvature estimate, not with √Riem².

## 10. Systole with Γ := Bolza (OW 7ff8299d) — no longer OPEN
- **Bolza systole = 2 arccosh(1+√2) = 3.05714183896: PROVED (computer-assisted).** Bolza is the regular hyperbolic octagon with interior angles π/4 and opposite sides paired. By the Poincaré polygon theorem (one vertex cycle, angle sum 2π, χ = −2) it is a genus-2 surface.
  - **Exact part:** cosh(inradius) = cos(π/8)/sin(π/8) = 1+√2, so each side pairing translates by 2 arccosh(1+√2). These closed geodesics give the upper bound.
  - **Lower bound:** every hyperbolic class has a representative γ with d(o, γo) ≤ ℓ(γ) + 2R, where cosh R = 3+2√2 is the circumradius. A BFS over tile adjacency within radius ℓ₀ + 3R gave 8185 elements and 760 with d ≤ ℓ₀ + 2R. Minimum translation length: 3.0571418390. There are no elliptic or parabolic elements. The next length is 4.896905 = 2 arccosh(3+2√2).
  - This agrees with the literature (Jenni 1984; Fortier Bourque–Petri arXiv:2302.02540): CONDITIONAL as citations, but no longer needed.
  - Caveat: the run is in double precision with a 1e-7 rounding key, so this is "PROVED (computer-assisted, floating point)".
- **Shortest non-contractible 11D loop: PROVED given the metric.** π₁(M₆) = π₁(Σ), because the S⁴ fibre is simply connected. The fibre terms are PSD, and the μ₀ = 1 section has Δ = X₀ with no fibre term. So with sys_hyp = 3.0571:

| candidate | sys₁₁ range (ℓ_p) | lower bound / 2πℓ_p |
|---|---|---|
| MN1 | [69.00, 72.39] | **11.0×** |
| MN2 | [75.95, 85.25] | **12.1×** |
| BBBW z=2 | [88.82, 102.46] | **14.1×** |
| BBBW z=3 | [100.81, 117.82] | **16.0×** |

  Every candidate clears 2πℓ_p by at least 11×. The thresholds were sys_hyp ≥ 0.278 / 0.253 / 0.216 / 0.191; Bolza exceeds them by 11–16×.
- **Mumford.** For any other Γ, the admissible set {sys_hyp ≥ 0.28} is the ε-thick part of moduli space, which is compact (Mumford). λ₁(Σ) is bounded below on it, so KK masses on Σ stay bounded away from zero (CONDITIONAL, literature). This is moot now that Γ = Bolza.
- **MR2 md §2 "Warping makes the 11D systole longer": OPEN (unsupported).** The warp factor Δ^{1/6} lies in [min X^{1/6}, max X^{1/6}], and min X^{1/6} = 0.990 / 0.933 / 0.913 / 0.904 < 1. So warping can shorten loops by up to about 10% unless proved otherwise. MR2's unwarped thresholds 0.17–0.28 (erratum E-3) should be the warped-safe 0.19–0.28. This is immaterial for Bolza.
- **Still not fixed by Γ := Bolza:** the flat-connection (Wilson-line) moduli of the twist line bundles (Jacobian of Bolza) and the spin structure. They do not change the local metric, curvature or systole. They do affect the charged KK spectrum (OPEN).

## 11. Erratum 2efef556 — PROVED: all six PP fixes applied
- E-1 coefficient (1/16 ours = 1/8 CLP = ¼ BBBW) ✓
- E-2 R⁴ estimate ✓ ((ℓ_p/ℓ)⁶ = 6.648e-11 confirmed; MR2 is right that 6.8e-11 was a misprint)
- E-3 relabel and add K_sec and systole ✓ (threshold range: see §10)
- E-4 dps note ✓
- E-5 aa16d54e disclosure ✓
- E-6 header times ✓

The self-flagged cosmetics are confirmed:
- The "14/4" label: the code uses 14/4/4 = 14/16 = 0.875.
- The "pi/2-1.57" rows are β = 1e-6; their values equal the (1e-6, 1e-6) per-point rows.
- 6.8e-11 → 6.65e-11.
- Header times again run later than mtimes: md "~17:50" vs mtime 17:48:27 CST; erratum "~17:52" vs 17:48:52 CST.

## 12. Per-candidate grades (adopt nothing)
| candidate | 11D solution validity | EFT validity | remaining |
|---|---|---|---|
| MN2 (z=±1) | **CONDITIONAL**: Maxwell, G∧G and λ PROVED identically; Einstein and Bianchi PROVED at 29 sampled points (17 MR2 + 12 PP) incl. poles; all-points CONDITIONAL | **CONDITIONAL**: ℓ_p²\|K\|max = 5.40e-3; R⁴ ~ 1.6e-7; systole (Bolza) ≥ 12.1×2πℓ_p PROVED; no singular loci | global curvature sup CONDITIONAL; R⁴ coefficient CONDITIONAL; BF ≥ −4 CONDITIONAL; KK spectrum OPEN |
| MN1 (z=0) | **CONDITIONAL** (same basis) | **CONDITIONAL**: 2.69e-3; 1.9e-8; ≥ 11.0× | same |
| BBBW z=±2 | **CONDITIONAL** (same basis; PP covers the z=2 points missing from MR2's PERPOINT log) | **CONDITIONAL**: 7.64e-3; 4.5e-7; ≥ 14.1× | same, plus CFT dual OPEN |
| BBBW z=±3 | **CONDITIONAL** (same) | **CONDITIONAL**: 8.87e-3; 7.0e-7; ≥ 16.0× | same, plus CFT dual OPEN |

None is REFUTED. Compared with fc5e0156, the systole condition is now discharged (Γ = Bolza) and the full 11D EOM are verified at points. The upgrade to PROVED is blocked only by the global ("all points") statements and the literature conditions.

**Recommendation (mathematical; adopt nothing): MN N=2 still stands.** Nothing in this audit discriminates against it. Every candidate passes every test by a wide margin. MN2 keeps N=2 SUSY, the exact GM a and c, and a known dual. MN1 has the lowest curvature. BBBW |z| ≥ 2 has the highest curvature and an unknown dual.

## 13. Hold-gate status (OW 587eca0c)
- The release condition recorded in 587eca0c ("MR2's full 11D equations, curvature invariant and systole file lands and PP audits it") is **met once this file is filed**. The MR2 file 9ab8f0a6 has landed with matching sidecars, and this is the PP audit of it.
- **No mathematical blocker found.** Nothing here prevents the Owner from lifting the hold. The open and conditional items are shared by all candidates and do not undermine the existence or EFT validity of the vacua.
- Lifting the hold and choosing a vacuum are the **Owner's** acts. PP adopts nothing and the hold is not lifted by this file.
- Non-blocking context for the Owner:
  - The approved MR2 wall-boundary curvature job for MN2 (OW 7ff8299d) is queued and concerns the E₈ wall, not vacuum validity.
  - The junction stays OPEN.
  - The E₈ wall sector is CONDITIONAL.

## 14. Fixes needed from MR2 (future additive file)
1. md §0: (D) wording should read e^{2f} = 2/3 (L² = 2/3), not "e^{2f} = 4/9, L = 2/3".
2. md §1: the maximum is at μ₁ = 1 (α = π/2, β → 0), not at the β = π/2 / α-pole edges. Optionally report the limit values (MN2 Riem² → 3408, max|eig| → 40/3).
3. md §2 and erratum E-3: drop "warping makes the systole longer", or prove it. Use the warped-safe thresholds 0.19–0.28. Update to the Bolza values (§10).
4. PERPOINT_DIAG: add the missing BBBW z=2 rows, or disclose that they are absent.
5. dG₄ test: add a discriminating control (λ = 0 or λ(1+δ)). Note that X₁ and flux controls pass Bianchi by construction.
6. Report frame-normalized Einstein residuals instead of coordinate-mixed max|E^M_N|, whose near-pole scale is about 1e6.
7. "All points": either finish the symbolic E_MN simplification (MR2 estimated 1–2 h) or keep it labelled CONDITIONAL with the CLP/BBBW citations.
8. Cosmetics: the "14/4" and "pi/2-1.57" labels, 6.8e-11, and header times later than mtimes (recurring).
No NL fixes in this scope.

## 15. Rollup
- **PROVED 16:**
  - authority records 587eca0c and 7ff8299d (2)
  - MR2 file hashes; tip
  - validations; λ normalization map; Maxwell identically; G∧G ≡ 0
  - Einstein at sampled points; controls discriminating; Bianchi at sampled points
  - curvature maxima at sampled points plus location; estimator choice
  - Bolza systole; 11D loop ≥ 11× 2πℓ_p
  - erratum six fixes and cosmetics
- **CONDITIONAL 13:**
  - Einstein/Bianchi at all points; global curvature sup; R⁴ absolute size; BF ≥ −4; CLP/BBBW/Jenni citations
  - 4 solution-validity grades; 4 EFT grades
- **OPEN 3:** KK spectrum (incl. Wilson lines and spin structure); BBBW |z| ≥ 2 CFT dual; MR2's "warping lengthens the systole" claim.
- **REFUTED 0. PENDING 0. Total 32.**

No CERT. Nothing adopted. Nothing sent.
