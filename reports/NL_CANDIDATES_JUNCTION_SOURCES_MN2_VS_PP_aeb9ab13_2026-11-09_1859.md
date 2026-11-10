# NL CANDIDATES: junction-source options for MN N=2, listed against PP's no-go aeb9ab13 — 2026-11-09 18:59 CST (America/Chicago)
Author: Non Local Path (NL). **Everything below is an NL derived proposal. Nothing is adopted; the Owner chooses.**

**Tally: PROVED 11 · CONDITIONAL 4 · OPEN 3 · REFUTED 3 (total 21).** Item lists in §6.

Authority (sidecars checked this run):
- OW b0b9ae7f (OWNER_WRITE_MAINCHAT_t4407_PURSUE_ALL_OPEN_ITEMS_FOR_RESOLUTIONS_2026-11-09_1843.md, sha MATCH). Owner's words: "Pursue all for resolutions". Scope per that record: NL owns "junction source options for MN2 (alongside Y14/Y15)".
- Records in force: f825dfff (odd HW-type ℤ₂ wall, N_M5 + n_inst = 2N_flux), 7ff8299d (Σ = Bolza; b OPEN), 19a88b19 (MN N=2 working vacuum, CONDITIONAL; junction UNSOLVED; no source adopted), 49b04146 (KK scope: Bolza × wall-ℤ₂ invariant modes), 36683379 (any citation, math checked; a citation never makes a claim PROVED).
- Audited input: PP FINDINGS_PP_AUDIT_MR2_MN2_Z2_WALL_CURVATURE_E8_2026-11-09_1840.md (aeb9ab13). Also NL 1655, 1711 (+erratum 7), Y14 stage 1 (1836), Y16 (1813).
Limits: new file only. No CERT, no Gemini, nothing sent. Tip 7cddb188 checked at start.
Scripts: /workspace/nl-cand-1854/ (each with .sha256):
- clp_face_lemma.py 4bf4ed0d…, log clp_face_lemma.log 2cdd6e37….

## 0. The no-go and its premises
PP aeb9ab13 §3: at the MN2 wall the Israel stress is S = −(1/κ²)(6k h^x + 8k h^int), i.e. 6:8:8, with ρ_w = 6k/κ² > 0. S(k,k) = −2k/κ² < 0 along t+fibre and t+Σ. No E₈ + M5 content can supply it. Premises:
- N1 thin-wall Israel at two derivatives;
- N2 source content E₈ fields + M5s (tr R² treated in Y16);
- N3 the bulk next to the wall is exact MN2 (PP: "localized backreaction is OPEN");
- N4 ℤ₂ wall with the IR side kept on both sides (f825dfff).
Each candidate below drops one premise. Units below are k/κ² unless stated.

## 1. General lemmas (sharpen the no-go)
- **L1 (PROVED).** For any face stress with 4D Poincaré symmetry (S^x = −ρh^x) and internal pressures P_e, NEC along t+e is ρ + P_e ≥ 0. Summing over the 6 internal directions gives τ := −ΣP_e/ρ ≤ 6. The wall needs τ = 48/6 = **8**. So **no NEC-satisfying source of any kind** (branes, branes with worldvolume flux, E₈ fields of any self-duality, fluids) closes the exact-MN2 wall. This extends aeb9ab13 beyond E₈ + M5.
- **L2 (PROVED).** Take objects i with worldvolume ℝ^{1,3} × (p_i internal directions), tension σ_i of either sign, smeared. Then ρ = Σσ_i and the internal trace is −Σp_iσ_i. The wall needs Σ(p_i − 8)σ_i = 0 with every p_i ≤ 6, so **some σ_i < 0**. M2s cannot appear (3D worldvolume cannot contain ℝ^{1,3}).
- **L3 (REFUTED, by proof).** Claim: "some mix of 6D-worldvolume objects (M5, anti-M5, MO5-type ℝ⁵/ℤ₂ planes, any signs, any smearing) supplies 6:8:8". For p = 2 the internal trace is −2ρ = −12, not −48.
- **L5 (PROVED, within the warped family g = e^{2A(ρ)}η₄ + dρ² + g_int(y) used by MR2/PP).** For null k = e^{−A}∂_t + e, R(k,k) = A″ + 4A′² + Ric_int(e,e). With A′ = ±k on the two sides, ∫A″dρ = −2k whatever the smoothing. So a wall of thickness L carries ∫κ²T_src(k,k)dρ = −2k + O(L·(k² + |Ric_int|)). That is negative for L ≪ 1/k ≈ 37 ℓ_p. Thickening the wall does not remove the NEC violation; it only spreads it (consistent with PP's KINK − NO_SOURCE numerics).

## 2. Candidate JS-A: a negative-tension sector on the exact-MN2 wall (drops N2)
**Definition.** Add to the wall a set of smeared objects, at least one with negative tension, whose total stress with the charge sector equals 6:8:8. Sub-families, each the unique solution within the stated types (clp_face_lemma.log):
- **A1 (PROVED, arithmetic).** Wall-filling tension (p = 6) plus a p = 0 object: σ_w = 8, σ₀ = −2.
- **A2 (PROVED, arithmetic incl. the Σ/fibre split).** Wall-filling plus a p = 3 object wrapping 1 Σ direction and 2 fibre directions: σ_w = 10, σ₃ = −4. Then Σ: 10 − 4·½ = 8 and fibre: 10 − 4·(2/4) = 8.
- **A3 (CONDITIONAL on N_req/(2N_flux) = 1.288, horizontal measure; PP flags the warp measure).** Keep the f825dfff charge sector 9760 as BPS M5/self-dual E₈ (σ_M = 6/1.28777 = 4.659 on x×Σ). Then wall-filling σ_w = 3.341, x×(fibre 2-cycle) σ_f = 9.318, and p = 0 σ₀ = −11.318.
- **A4 (OPEN).** Whether M-theory has any negative-tension object with p ≠ 2, or a positive wall-filling tension on an HW wall. The HW action has no bare boundary cosmological term (hep-th/9603142; cited, not re-derived). A negative-tension Taub-NUT is singular. No candidate object is known to NL.
**Compatibility.** f825dfff: holds if the new objects carry no net M5 charge. 19a88b19: a proposal only, no source adopted. 36683379: no citation is used to upgrade.
**NL view.** Bookkeeping-complete, but it needs an object M-theory is not known to have.

## 3. Candidate JS-B: quantum or higher-derivative wall stress (drops N1)
**Definition.** The missing stress is supplied by tr R² (HW), one-loop/Casimir stress, or bulk R⁴-type terms.
- **B1 (REFUTED, by Y16 bound; PP 149be02a upheld).** Claim: "tr R² closes the MN2 junction at N = 4880". It is a fixed 2–5 M5 units (u = 2) or half that (u = 1). That is about 5×10⁻⁴ of the deficit for either u.
- **B2 (CONDITIONAL, order-of-magnitude; coefficient not computed).** Casimir/one-loop: ≤ 256/L₅¹⁰ ≈ 4.5×10⁻¹⁴ ℓ_p⁻¹⁰ against the required ρ_w ≈ 1.31×10⁻⁷ ℓ_p⁻¹⁰. That is ≲ 10⁻⁶ of the requirement and scales like N⁻³.
- **B3 (CONDITIONAL, scaling).** Bulk R⁴-type corrections are suppressed by (ℓ_p/L₅)⁶ ≈ 3.5×10⁻¹⁰.
**NL view.** Not viable at N = 4880.

## 4. Candidate JS-C: localized backreaction near the wall (drops N3)
**Definition.** The bulk next to the wall is not exact MN2. It is a deformation that tends to MN2 away from the wall, chosen so that a BPS-type wall (smeared M5s and/or E₈ with tension = charge = 9760) satisfies Israel with no NEC violation.
- **C1 (REFUTED, by proof; script check rank 4/4 at MN2, round and random X).** Claim: "some solution of the 7D U(1)² CLP truncation (BPS or not, any r_b) lets a constant-r ℤ₂ face be sourced by smeared M5s plus E₈ fields with F on the fibre only".
  - Proof: those sources need k_Σ = k_x and Σk_fib = 4K. With C2 this forces D′/D to be constant on S⁴, hence 2λ_a′ = c for a = 0, 1, 2. Since λ₀ = −2(λ₁+λ₂), c = 0. Then f′ = g′ = 0, all k vanish and ρ = 0.
  - So no deformation inside the CLP truncation rescues the wall.
- **C2 (PROVED, analytic; script error ≤ 3×10⁻¹⁵).** In the CLP uplift, Σk_fib = −(5/6)D′/D (the S⁴ volume density is Δ̃^{−5/6}), and k_x − K = −(3f′ + 2g′).
- **C3 (PROVED, example).** C1 does not exclude NEC-satisfying sources in general. For example f′ = λ′ = 0 and g′ < 0 gives w = (−1 on x and fibre, −½ on Σ). But that source is not M5/E₈-like.
- **C4 (PROVED, algebra; script).** Add the S⁴ breathing mode β (outside CLP: fibre ×e^{2β}, 7D block ×e^{2γβ}). Then the pure-M5 face equations have a one-parameter solution: λ′ = 0, g′ = f′, β′ = −2f′/(1+2γ), k_fib = −2k_x and ρ = 6k_x/κ². This holds for every γ tested.
- **C5 (PROVED, algebra).** ρ > 0 needs k_x > 0, so the 11D x-warp grows away from the wall. In 5D Einstein frame the warp gradient is −k_x, so the wall is RS-like there.
- **C6 (PROVED; standard harmonic-function solution, exponents checked).** The flat-fibre analogue, the M5 domain wall smeared over T⁴, ds² = H^{−1/3}(dx² + dΣ²) + H^{2/3}(dr² + dT⁴) with H = H₀ − c|r|, satisfies C4 exactly: k_Σ = k_x and k_fib = −2k_x. Its G₄ ∝ H′vol_fib is odd across the wall, as f825dfff requires.
- **C7 (OPEN).** Existence of an 11D solution that joins such a wall, with curved twisted S⁴ fibre and 9760 units, to the MN2 IR region.
- **C8 (CONDITIONAL; DeWolfe–Freedman–Gubser–Karch-type counting, hep-th/9909134, not re-derived).** The wall gives Israel for the warp, a junction condition for β′ and the Hamiltonian constraint. IR regularity then leaves isolated solutions, so **b would be fixed** (see the b file).
- **C9 (PROVED, invariance).** β is an SO(5) singlet, constant on Σ, with a ℤ₂-even profile. So it lies inside the 49b04146 KK scope.
- **C10 (OPEN).** Not covered by C1: E₈ fields with Σ legs (the twist coupling of Y14 S5), the full 14-scalar SL(5)/SO(5) truncation, and non-constant faces.
**Compatibility.** f825dfff: kept (odd G, charge 9760, tension = charge). 19a88b19: MN2 stays the far vacuum; the near-wall region is a deformation (CONDITIONAL). 49b04146: inside scope (C9).
**NL view.** This is the only candidate with no NEC-violating matter. It also explains why the count gap (1.255, 1.667) appears: that gap is defined relative to exact MN2 at the wall.

## 5. NL recommendation (nothing adopted)
1. Pursue **JS-C with the breathing mode** as the primary route. Next: derive the breathing-mode equations on the twisted S⁴ (≈ 2–3 h), then shoot from the C4 wall data to the MN2 IR (≈ 2 h).
2. Keep **JS-A** only as the explicit NEC-violating fallback. If chosen, the Owner would be adopting an object not known in M-theory (A4).
3. Drop **JS-B** (B1 REFUTED; B2 and B3 are negligible).

Bearing on the junction: still **UNSOLVED**. New facts:
- L1: every NEC source fails at an exact-MN2 wall.
- C1: no CLP-truncation deformation rescues an M5/E₈-fibre wall.
- C4: with the breathing mode the face equations do close locally.
The Y14 pairs (NEC-satisfying) cannot close the exact-MN2 wall (L1). Their role under JS-C is OPEN (C10).

## 6. Tally (header checked against these lists)
| label | count | items |
|---|---|---|
| PROVED | 11 | L1, L2, L5, A1, A2, C2, C3, C4, C5, C6, C9 |
| CONDITIONAL | 4 | A3, B2, B3, C8 |
| OPEN | 3 | A4, C7, C10 |
| REFUTED | 3 | L3, B1, C1 |
Check: 11 + 4 + 3 + 3 = 21.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (start). No CERT. Nothing sent.
