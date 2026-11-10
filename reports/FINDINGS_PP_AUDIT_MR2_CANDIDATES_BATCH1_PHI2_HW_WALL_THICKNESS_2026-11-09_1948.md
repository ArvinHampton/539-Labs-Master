# FINDINGS — PP audit of MR2 candidate resolutions batch 1 (OW b0b9ae7f): φ₂ ℤ₂ vs HW, and the wall-thickness premise — 2026-11-09 (America/Chicago)
Auditor: Professor Proof (PP). Target: MR2_CANDIDATE_RESOLUTIONS_BATCH1_PHI2_Z2_VS_HW_AND_WALL_THICKNESS_PER_OW_b0b9ae7f_2026-11-09.md. Pure math; labels PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only results are CONDITIONAL. A citation alone never makes a result PROVED (OW 3f160803 + 36683379). **Nothing adopted. Junction: UNSOLVED.** Recommendations are the lane's opinion, and PP grades only the math. No CERT, no sends, no Gemini. Tip 7cddb188 read-only. Lock 96f8d42e §4 stays purged. Nomenclature per OW 81b74a31.

## 0. Integrity and reproduction
- .md 425b4e67… = sidecar. .py 56c05c23… and .log 88d2d7fb… match their sidecars.
- PP reran the .py: the log reproduced identically, apart from timing lines.
- Cross-checked against:
  - NL JS-A (A1–A3, L5);
  - NL JS-C: 1935, 1936, 1942, 1943, and PP's audits of them (1944 and addendum 1947);
  - PP aeb9ab13 (Israel convention, 6:8:8);
  - MR2 ERRATUM2 5511845e;
  - PP fc93b8c0 (Pin⁺/KK erratum audit);
  - MR2 Pin⁺ 8399be55;
  - OWs 8b26c786 (Group A), 90cec14c (breathing GO) and b0b9ae7f (this task).

## 1. Lemmas
- **L1:**
  - Restriction argument — PROVED. F₁₀ is totally geodesic, and the normal leg is ℤ₂-odd, so R_{nacd}|_{F₁₀} = 0. The restricted 11D tr R∧R therefore equals the intrinsic one.
  - "tr R∧R ≢ 0 on F₁₀" — CONDITIONAL. The evidence is float-only at 4 sample points, with a large margin (|·| ≈ 52–78 against 2.4e-15 noise).
  - "Pointwise nonzero everywhere on F₁₀" — OPEN. This is an overclaim, since 4 points cannot establish "everywhere".
  - Upgrade path: an exact symbolic or rational evaluation at one point would make ≢ 0 PROVED.
- **L2 — PROVED.** The topology is AdS₅ × Σ × S³. The twist has degree 2 (even), so w₂ = 0 and the bundle is stably trivial, giving p₁ = 0. tr R∧R is therefore exact, and every 4-cycle has zero integral.
  - **L1 and L2 are consistent:** an exact, nonzero 4-form can have vanishing periods.
- **L3 — PROVED** under its stated hypotheses (thin wall, exact-MN2 constant-r face on both sides, sources of brane type plus NEC-respecting).
  - Proof check: the step-by-step argument holds. S_req(k,k) = −2k/κ² follows from 6:8:8 (aeb9ab13), and a brane part contributes σ(1 − |ê_∥|²) ≥ −|σ| for σ < 0. Hence Σ|σ_neg| ≥ 2k/κ² = ρ_w/3.
  - The numeric bounds (≥ 2873–5599 M5 units) are exactly N_req/3 for the corresponding measures. They are **CONDITIONAL** on the measure (ERRATUM2 fix 6).
  - **Sharpness:** NL JS-A candidate A1 has |σ₀| = 2 = ρ_w/3, so **it saturates L3**. A2 and A3 satisfy it. L3 therefore strengthens JS-A: no brane-type source can do better than A1.

## 2. Item 1 — φ₂ ℤ₂ vs HW
**(1a) HW wall at the radial face**
- Definitional match: PROVED (definitional).
- N = 4880 and charge 9760: PROVED (carried from ERRATUM2).
- Pin⁺ A × W: CONDITIONAL (8399be55; consistent with fc93b8c0).
- HW anomaly inflow: CONDITIONAL (citation only; correctly labelled).
- Pure closure with exact MN2 + thin wall + E₈/M5: REFUTED. This agrees with aeb9ab13 and ERRATUM2 fix 3.
- **Breathing rescue: OPEN — the row needs updating (fix B6).**
  - The local face Israel closure is PROVED: PP 1935, item N1, with γ = −½ allowed.
  - Realizing it with a uniform breathing ansatz on MN2 is REFUTED: NL 1942 P2, reproduced by PP, forces β′ ≡ 0.
  - The remaining route is the H-invariant cohomogeneity-two sector, which is proved consistent (NL 1943 T7, PP 1947). Its solution is OPEN (T10).
- Non-YM wall stress: OPEN.
- Count gap: CONDITIONAL. It overlaps NL's (1.255, 1.667), so it is not decisive.

**(1b) Smooth parity P**
- The following rows are PROVED:
  - P is a symmetry;
  - F₁₀ is totally geodesic and has the stated topology;
  - G₄ has one normal leg, so wall charge 0;
  - (b-i) needs no E₈ sector.
- "P is not the f283cffd face": REFUTED as a face candidate, given the definitions. **MR2 counts this twice**, as PROVED #7 and as REF #3. Count it once, as REF (fix B3).
- (b-ii) HW condition giving tr F² = ½ tr R² pointwise: PROVED given HW. The tangential G₄ vanishes because G₄ has exactly one normal leg.
- (b-ii) "F ≠ 0 required": **CONDITIONAL**, because it inherits L1's float status. It becomes PROVED once L1 is upgraded.
- (b-ii) zero net instanton number: PROVED (L2).
- (b-ii) existence of such an E₈ connection: CONDITIONAL (correct).
- (b-ii) backreaction: OPEN (correct).
- P combined with the HW wall: REFUTED given HW. Reflecting one wall-tangent direction reverses the chirality. This is consistent with 8399be55 §B and PP fc93b8c0.

**(1c) Hybrid options**
- (c1): the group action is well defined (PROVED). The option is REFUTED given HW. Its ℝ²/ℤ₂ locus is OPEN.
- (c2): CONDITIONAL (citation of 8399be55, not rederived). **It conflicts with the Owner's Group A (OW 8b26c786)**, because r ∉ Aut⁺. MR2 says so correctly, and it is the Owner's call.
- (c3): well defined, with the OM5 fixed loci (PROVED). The −½ charge is CONDITIONAL (citation). Total negative tension ≈ 2 × (−½) = −1 M5 unit, against ≥ 2873 required, so it is **REFUTED as an NEC fix**, given L3's hypotheses.

## 3. Item 2 — the wall-thickness premise
**(2a)**
- Israel weights exact: PROVED (ERRATUM2).
- The 1/ε² divergence is a regulator artefact: PROVED.
- Power counting: CONDITIONAL. The arithmetic checks: kℓ_p = 1/39.43 … 1/35.13 = 0.0254–0.0285.
- HW sharpness: PROVED as a definition, CONDITIONAL as physics.
- Bookkeeping replacement of the "≳ ℓ_p" premise: PROVED.

**(2b)**
- R_S4 and flux arithmetic: PROVED (8π²R³ = (2π)³N, given 2κ² = (2π)⁸ℓ_p⁹).
- **kε_y lies exactly in [2^{−2/3}, 2^{−1/2}] = [0.630, 0.707].** This is independent of N, because R_S4 and 1/k both scale as N^{1/3}ℓ_p. PROVED. State the closed form (fix B7).
- The E₈ instanton size sets no normal thickness: PROVED given HW.
- Identifying the wall thickness with R_S4: OPEN (correct).

**(2c)**
- Existence and width of the profile: OPEN (correct).
- **"Smooth solution, so no δ-source, no Israel stress and no NEC deficit" (MR2: COND on existence) — REFUTED as stated.**
  - G₄ is odd under the wall ℤ₂, so ∫_{S⁴} G₄ changes from +N to −N across the wall.
  - The S⁴ slices on the two sides are homologous. By Stokes, a source-free profile (dG₄ = 0) would keep that flux constant, which is a contradiction.
  - So any smooth profile must carry 2N = 9760 units of smeared M5/instanton charge density, and its stress must be accounted for.
  - Further, NL JS-A L5 shows that thick walls with a fixed internal metric still violate the NEC. So "L3 applies only to thin walls" is incomplete.
  - What evades L3 is dropping the exact-MN2 face data, through the breathing/internal deformation. Thickness alone does not evade it.
  - NL's JS-C route is itself a thin-wall construction. It evades L3 by changing the face data, not by smoothness.
- Width estimate: OPEN (correct).
- Thin limit kε → 0: PROVED as a scale comparison, given existence.

## 4. Rollup
- **MR2's tally:** PROVED 15 · COND 7 · OPEN 7 · REF 4.
- **PP's tally on MR2's list: PROVED 12 · COND 9 · OPEN 8 · REF 4.** The changes:
  - L1 moves from PROVED to COND (the ≢ 0 part), and its "everywhere" part is added as OPEN.
  - (b-ii) "F ≠ 0" moves from PROVED to COND.
  - "P is not the face" is removed from PROVED, as a double count with REF #3.
- **Graded rows that MR2's rollup omits**, which PP grades as:
  - PROVED 5: (b-i) needs no E₈; (b-ii) HW condition; regulator artefact; bookkeeping; thin limit given existence.
  - REFUTED 1: the (2c) smooth "no source, no NEC deficit" claim.
- Carried: junction **UNSOLVED**; full KK spectrum OPEN; MN N=2 CONDITIONAL (19a88b19).

## 5. Fix list for MR2
1. **B1:** relabel L1. "≢ 0" becomes CONDITIONAL (float, 4 points), and "pointwise nonzero everywhere" becomes OPEN or is dropped. Upgrade by an exact evaluation at one rational point.
2. **B2:** mark (b-ii) "F ≠ 0 required" as CONDITIONAL, inheriting from L1.
3. **B3:** remove the double count of "P is not the face" (PROVED #7 and REF #3).
4. **B4:** add the omitted graded rows to the rollup.
5. **B5:** replace the (2c) smoothness claim. Per the Stokes argument, a smooth profile still needs 2N units of smeared charge. Per NL L5, thickness at fixed internal metric does not evade the NEC. Evading L3 requires changing the face data.
6. **B6:** update the (1a) breathing row. Local Israel closure is PROVED (PP 1935 N1). The uniform bulk realization on MN2 is REFUTED (NL 1942 P2). The cohomogeneity-two route is OPEN (1943 T7/T10).
7. **B7:** state the exact N-independent range kε_y ∈ [2^{−2/3}, 2^{−1/2}].
8. **B8:** note that L3 is sharp, since NL A1 saturates it, and that L3's numbers equal N_req/3.
9. **B9:** flag (c2) explicitly as requiring an Owner revisit of Group A (8b26c786). No grade change.

Tip 7cddb188 untouched (read-only). No CERT. Nothing sent. Nothing adopted.
