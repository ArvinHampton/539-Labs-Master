# NL DERIVED: analytic sweep of PP's Y15 NEC escape list on MN2 with the odd HW-type ℤ₂ wall
2026-11-09, 20:29 CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED**, unchanged. J7-src remains **OPEN**. The count-gap status is unchanged.

Authority: **OW t4426** OWNER_WRITE_MAINCHAT_t4426_PURSUE_ALL_OPEN_JUNCTION_ROUTES_2026-11-09_1956.md = d5eaeef3f6b53270bd09e30053f6cdbf442d191c58a0a9fda30daff83907ffb3 (item 7 of the go: PP's NEC escape list). **OW t4431** f700141d… (90% stop lifted; usage still reported). OW f825dfff (odd HW-type ℤ₂, IR side kept); OW 19a88b19 (MN N=2 working vacuum, CONDITIONAL; junction UNSOLVED); OW 90cec14c (breathing-mode GO, not adoption); OW 36683379 (citations checked, never upgrade alone); OW f1d167d1 (where the algebra is named it is "resonant algebra"; it is not named in this file).
Source of the list: FINDINGS_PP_AUDIT_NL_Y14_STAGE2_Y15_FIBRE_ISRAEL_2026-11-09_1953.md = 077e417d…, §9, as restated in E17 §2. Also used, and not edited: Y15 86a46df7…, Y16 7270a6b3…, 1859 (L1–L3, A4) 9987bdcd…, 1948/E18 K4, the per-direction file NL_DERIVED_Y15_TRR2_PER_DIRECTION_NULL_2026-11-09_2026.md (21045043…), B12 f8801bff…, and Erratum 18-B12 92dded27… (the D4 constant; cite as "Erratum 18-B12" per the 2020 numbering note).
Limits: additive only. No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before and after. Usage 78.2% at the start of this item.

χ-smearing is not decided (OW t4426). The **χ-uniform [χU]** and **χ-smeared [χS]** branches are labelled separately wherever the choice matters.

**Tally: PROVED 5 · CONDITIONAL 3 · OPEN 3 · REFUTED 1 · total 12**

The list (PP 077e417d §9): a candidate must either (E1) make k_v ≤ k_x pointwise on S⁴ for every Σ and fibre direction v, or bring an NEC-violating source — (E2) σ < 0 M5s, (E3) G₄ / worldvolume flux of the right sign, or (E4) a tr R² stress far larger than Y16's bound — or else use (E5) a different face, or (E6) keep the UV side (which needs negative wall energy). For each: does a known M-theory ingredient realize it on MN2 with the odd HW ℤ₂?

## E1. k_v ≤ k_x pointwise on S⁴

This is a condition on the *face kinematics*, not on a source (E17-NEC: S(ℓ_v,ℓ_v) = −(2/κ²)(k_v − k_x), so NEC-respecting content needs k_v ≤ k_x).

- **E1-IR (PROVED).** On the unperturbed MN2 IR face, k_Σ = k_fib = 0 and k_x = −k < 0 at every point of S⁴, so k_v − k_x = k > 0 in every Σ and fibre direction. The kinematic escape fails everywhere, with margin k. This is independent of n(χ): it holds for both **[χU]** and **[χS]**. No source, of any kind, can change the K of a *fixed* exact-MN2 face.

- **E1-C4 (PROVED, algebra; K4 restated for this list).** The breathing C4 face data (k_Σ = k_x, k_fib = −2k_x) give k_fib ≤ k_x iff k_x ≥ 0, and k_Σ = k_x with equality. So C4 data with **k_x ≥ 0** realize E1 in every fibre and Σ direction, pointwise, for both **[χU]** and **[χS]** (the statement is pointwise in χ). This is face algebra, not a bulk solution. K4 does not establish k_x > 0 for any actual solution, and "tension = charge" on the twisted S⁴ remains OPEN (E16-F3).

- **E1-ex (OPEN).** No 11D solution on MN2 with the odd HW ℤ₂ and C4 (or other) face data satisfying E1 is on record. In the decided BPS classes, B12 D3 excludes every face of a W-flow in the CGR (φ, λ) sector, and D4 (as corrected by Erratum 18-B12: D2 fails for δ < ½ min_{S⁴} ε/L) excludes any face within a uniform δ of the exact MN2 IR face, in both **[χU]** and **[χS]**. Finite-amplitude χ-dependent BPS walls remain OPEN (B12 D6), as does a non-BPS C4 shoot (1948 K6 is OPEN; K6′ is only a heuristic).

## E2. σ < 0 (negative-tension objects)

- **E2-need (PROVED; 1859 L1 and L2, algebra rechecked).** For any 4D-Poincaré wall stress, NEC along t̂ + ê gives τ := −Σ_{e=1}^{6} P_e / ρ ≤ 6. The exact MN2 IR wall needs P_e = −8k/κ² on all six internal directions and ρ = 6k/κ², so τ = 8. Thus **no NEC-satisfying source of any kind closes the exact-MN2 wall**. Equivalently (L2), objects with worldvolume ℝ^{1,3} × (p_i internal directions), p_i ≤ 6, and tensions σ_i of either sign, must satisfy Σ(p_i − 8)σ_i = 0, hence **some σ_i < 0**. This is the reason E2 appears on the list if one stays on the exact MN2 face. Both **[χU]** and **[χS]** (smearing does not change the pointwise 6:8:8 requirement on this face).

- **E2-MO5 (REFUTED, by the L3 counterexample, rechecked).** The claim "some mix of 6D-worldvolume objects (M5, anti-M5, MO5-type ℝ⁵/ℤ₂ planes, any signs, any smearing) supplies 6:8:8" fails: every such object has p = 2, so the internal trace is −2ρ = −12 (in units k/κ², ρ = 6), not −48.

- **E2-obj (OPEN; 1859 A4, still).** Bookkeeping solutions with some σ < 0 and p ≠ 2 exist as stress tensors (A1–A3). Whether M-theory has any negative-tension object with p ≠ 2, or a positive wall-filling tension on an HW wall, is OPEN. The HW action has no bare boundary cosmological term (hep-th/9603142, cited, not re-derived). A negative-tension Taub-NUT is singular. No candidate object is known. So E2 is **not realized by a known M-theory ingredient**.

## E3. G₄ / worldvolume flux of the right sign

- **E3-NEC (PROVED, given L1).** If the flux contribution itself satisfies NEC, L1 still applies on the exact MN2 IR face: no NEC-satisfying source, "branes with worldvolume flux" included, can supply τ = 8. So NEC-respecting flux does **not** realize E3 on that face, in either χ-branch.

- **E3-viol (OPEN).** A wall-localized G₄ / M5 worldvolume flux whose *own* stress violates NEC in the needed directions (S(ℓ,ℓ) < 0 with the 6:8:8 pattern, or enough of it to close after adding the other content) is not constructed here and is not on record as a consistent, odd-HW-ℤ₂-compatible configuration on MN2. Ordinary bulk G₄ of 11D supergravity is already present in the MN2 solution; its jump is the M5 charge already counted in f825dfff, and it is not an extra wall source of the needed sign. J7-src remains OPEN. Both **[χU]** and **[χS]**.

## E4. A tr R² stress far larger than Y16's bound

- **E4-HW (CONDITIONAL: on the hypotheses of the 2026 per-direction file — algebraic fibre-intrinsic part, n = 24 grid, ∇∇R and the twist omitted; both u).** The known ingredient is the HW −½ tr R² term. On the exact MN2 IR face it has the needed sign in every sampled fibre direction, but not the needed size: the best pointwise ratio |S_R|/|S_req| is 3.49×10⁻³ at u = 2 (shortfall 286) and 1.75×10⁻³ at u = 1 (shortfall 572). Warp mixing is a few-percent correction (6 max|H|² / max I_fib = 0.0385). The UV end is worse (shortfall 1627 at u = 2). So the HW term does **not** realize "far larger than Y16's bound". Both **[χU]** and **[χS]** (R2-chi: the curvature is a property of the face metric).

- **E4-higher (CONDITIONAL, given Y16 Q7 / J1).** Other four-derivative corrections (bulk R⁴, C₃ ∧ X₈, one-loop wall terms) are O(1/N) of the deficit on every face, the same scaling as the HW term (Q14 leaves their exact coefficients OPEN, but not the power of N). They do not realize a 10²–10³ enhancement. A coefficient error of that size would lie outside the derivative expansion (Y16 Q11b).

## E5. A different face

- **E5-int (CONDITIONAL; Y15-int, I2 on 398 faces).** The interior constant-r faces of the unperturbed MN2 flow (no breathing) fail I2 at every sampled S⁴ grid point, with min margin +2.01×10⁻² ℓ_P⁻¹, including the UV limit of that flow (k_fib → 0, k_x → −1/L₇). Those faces do **not** realize E5 as a working kinematic escape. Both χ-branches: this is a statement about K of the background faces, not about n(χ).

- **E5-C4 (OPEN as a realized solution; the kinematics are E1-C4, PROVED).** The only different face on record whose kinematics realize E1 is the breathing C4 family with k_x ≥ 0 (or a finite-distance-from-MN2 face with k_x ≥ 0, as B12 D4 requires of any BPS wall). No such solution is constructed. This is the live kinematic route under OW 90cec14c, and it remains unsolved.

## E6. The UV side kept

- **E6-sign (PROVED, given the opposite normal).** If the UV side is kept instead of the IR side, every Israel value flips sign. I2 becomes satisfiable by NEC-respecting content, but the wall energy density becomes ρ = −6k/κ² < 0, which needs negative wall energy (σ < 0 or an equivalent NEC-violating ingredient). Thus E6 does not evade E2; it reduces to it, with the opposite orientation. Both χ-branches.

- **E6-record (record, no mathematical grade).** Standing Owner record f825dfff keeps the IR side. E6 is not available under that record unless the Owner changes it. This is not a mathematical refutation.

## Wrap-up

A known M-theory ingredient realizes an escape in only one kinematic sense: **C4 face data with k_x ≥ 0 realize E1 / E5** (E1-C4, PROVED as algebra). No known object realizes E2; E2-MO5 is REFUTED; E3 is not realized by NEC-respecting flux and is OPEN for a violating configuration; E4 is not realized by the HW term or by other O(1/N) corrections; E6 reduces to E2 and conflicts with f825dfff. **The junction remains UNSOLVED. The count gap is unchanged.** J7-src remains OPEN.

## Tally (header checked)

| label | count | items |
|---|---|---|
| PROVED | 5 | E1-IR, E1-C4, E2-need, E3-NEC, E6-sign |
| CONDITIONAL | 3 | E4-HW, E4-higher, E5-int |
| OPEN | 3 | E1-ex, E2-obj, E3-viol |
| REFUTED | 1 | E2-MO5 |

Check: 5 + 3 + 3 + 1 = 12. E5-C4 is the same OPEN existence as E1-ex and is not counted twice. E6-record is a record reading, not a mathematical claim.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
