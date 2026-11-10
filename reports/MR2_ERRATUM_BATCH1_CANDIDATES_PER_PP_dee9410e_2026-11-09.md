# MR2 erratum to batch-1 candidate resolutions (425b4e67…) per PP audit dee9410e — 2026-11-09, written 19:50 CST (America/Chicago)
Author: MR2. Text-only and additive: the batch-1 file is not edited, and no new computation was run. Nothing is adopted; the Owner chooses. The junction stays **UNSOLVED**. Tip 7cddb188 untouched. No CERT, no Gemini, nothing sent. Nomenclature per OW 81b74a31: "resonant algebra" (this file has no occasion to use the old term).

Inputs (sha = sidecar, verified at 19:50 CST):
- PP audit FINDINGS_PP_AUDIT_MR2_CANDIDATES_BATCH1_PHI2_HW_WALL_THICKNESS_2026-11-09_1948.md, dee9410e90bcd6eb3e5df436314a0ba98d791bea938bc53968d5baf388ca059c.
- Target MR2_CANDIDATE_RESOLUTIONS_BATCH1_PHI2_Z2_VS_HW_AND_WALL_THICKNESS_PER_OW_b0b9ae7f_2026-11-09.md, 425b4e67e5cc58ac8607d9f0c668f2e5d48f3d2bc3363e011ebd194800ecd85a (.py 56c05c23…, .log 88d2d7fb…).

Grading convention (PP's): a row reading "PROVED with a CONDITIONAL premise" counts as CONDITIONAL, and float-only evidence is CONDITIONAL. Where batch 1 states a hypothesis as part of a theorem's statement ("given HW", "given existence"), I keep PP's own tally choice. See the note on the tally convention below.

## Fixes
- **B1 — ACCEPTED.**
  - L1 restriction argument: PROVED. F₁₀ is totally geodesic and the normal leg is ℤ₂-odd, so R_{nacd}|F₁₀ = 0.
  - "tr R∧R ≢ 0 on F₁₀": **CONDITIONAL**. The evidence is double-precision values at 4 sample points (52–78 against 2.4e-15 noise).
  - "Pointwise nonzero everywhere on F₁₀": **OPEN**. Batch 1's wording "pointwise nonzero" overclaimed and is withdrawn.
  - Upgrade path: an exact symbolic evaluation at one rational point. Not run, to save budget; ETA about 20 min if wanted.
- **B2 — ACCEPTED.** (b-ii) "a nontrivial E₈ field F ≠ 0 is required" is **CONDITIONAL**, inheriting from L1. It becomes PROVED if B1 is upgraded.
- **B3 — ACCEPTED.** "P is not the f283cffd face" is counted **once, as REFUTED** (P as a face candidate, given the f283cffd/f825dfff definitions). The PROVED #7 entry is removed.
- **B4 — ACCEPTED.** The six omitted graded rows are added to the rollup:
  - PROVED: (b-i) needs no E₈; (b-ii) HW condition tr F² = ½ tr R²; the 1/ε² regulator artefact; the bookkeeping replacement of "≳ ℓ_p"; the thin limit kε → 0 (given existence).
  - REFUTED: the old (2c) smoothness claim (B5).
- **B5 — ACCEPTED. The (2c) claim "a smooth solution has no δ-source, no Israel stress and no NEC deficit" is REFUTED as stated.**
  - Stokes argument, checked:
    - G₄ is odd under the wall ℤ₂ (f825dfff), so ∫_{S⁴} G₄ equals +N on one side of the wall and −N on the other.
    - The S⁴ slices on the two sides are homologous through the profile.
    - With dG₄ = 0 the two integrals would be equal, a contradiction.
    - So a smooth profile must carry 2N = 9760 units of smeared M5/instanton charge, whose stress must be included.
  - NL JS-A L5 (as graded by PP; not rederived by MR2): a thick wall with a fixed internal metric still violates the NEC.
  - Correct statement: **thickness alone does not evade L3. Evading it requires changing the face data** (the breathing or internal deformation). NL's JS-C route is itself thin-wall and evades L3 that way.
- **B6 — ACCEPTED** (carried from PP 1935 / NL 1942 / NL 1943 as audited by PP 1944 / 1947; not rederived by MR2). The (1a) breathing-rescue row now reads:
  - local face Israel closure PROVED (PP 1935 N1, γ = −½ allowed);
  - uniform breathing on MN2 REFUTED (NL 1942 P2: β′ ≡ 0);
  - the H-invariant cohomogeneity-two sector is consistent (NL 1943 T7, PP 1947), and **its solution is OPEN** (T10).
  - In the rollup this stays one OPEN row ("rescue of (1a)"). The sub-results belong to NL/PP files and are not recounted here.
- **B7 — ACCEPTED, checked by hand.**
  - R_S4 = ℓ/2 and k = 1/(ℓ√(wF₀)), so kε_y = 1/(2√(wF₀)), with wF₀ ∈ [1/2, 2^{1/3}/2] (exact, ERRATUM2).
  - Hence **kε_y ∈ [2^{−2/3}, 2^{−1/2}] = [0.6300, 0.7071] exactly, independent of N** (both scales go as N^{1/3}ℓ_p). PROVED. This matches log (B): 0.630, 0.7071.
- **B8 — ACCEPTED.**
  - L3 is **sharp**: NL JS-A candidate A1 has |σ₀| = 2 (in k/κ² units) = ρ_w/3, so it saturates the bound, and no brane-type source does better.
  - L3's M5-unit numbers (≥ 2873–5599) are exactly N_req/3 for the corresponding measures, and are CONDITIONAL on the measure (ERRATUM2 fix 6).
  - L3 itself is PROVED under its stated hypotheses.
- **B9 — ACCEPTED.** (c2) W × (P∘r) is CONDITIONAL (citation of 8399be55, not rederived) and **conflicts with the Owner's Group A (OW 8b26c786)**, since r ∉ Aut⁺(Bolza). It is offered only if the Owner revisits Group A. No grade change.

No fix is disputed.

## Final tally (batch 1 plus this erratum)
- PP's tally on batch 1's list is reproduced: **PROVED 12 / COND 9 / OPEN 8 / REF 4**.
  - B1: L1 goes PROVED → COND, and "everywhere" is added as OPEN.
  - B2: F ≠ 0 goes PROVED → COND.
  - B3: the double count is removed.
- Adding the six omitted rows (B4: +5 PROVED, +1 REF) gives the **final tally: PROVED 17 / COND 9 / OPEN 8 / REF 5 (39 rows)**.
  - **PROVED 17:**
    1. L2
    2. L3
    3. P symmetry
    4. F₁₀ geometry/topology
    5. wall charge 0 for P
    6. (b-ii) zero net instanton number
    7. c1 group well-defined
    8. σ_O well-defined
    9. σ_O OM5 fixed loci
    10. R_S4 / flux arithmetic
    11. kε_y ∈ [2^{−2/3}, 2^{−1/2}]
    12. E₈ instanton size gives no normal thickness (given HW)
    13. (b-i) no E₈
    14. (b-ii) HW condition (given HW)
    15. regulator artefact
    16. bookkeeping replacement
    17. thin limit (given existence)
  - **COND 9:**
    1. L1 ≢ 0
    2. (b-ii) F ≠ 0
    3. A × W Pin⁺
    4. HW anomaly inflow
    5. count-gap measure
    6. (b-ii) existence of an E₈ connection
    7. OM5 charge −½
    8. (2a) power counting
    9. (c2)
  - **OPEN 8:**
    1. L1 everywhere
    2. rescue of (1a) (cohomogeneity-two, NL)
    3. non-YM wall stress
    4. (b-ii) backreaction
    5. c1 ℝ²/ℤ₂ locus
    6. (2b) identification
    7. (2c) profile existence/width
    8. (2c) width estimate
  - **REF 5:**
    1. pure (1a) closure with E₈+M5
    2. P with the HW wall (and c1)
    3. P as the f283cffd face
    4. (c3) as an NEC fix
    5. (2c) smooth "no source / no NEC deficit"
- **Note on the tally convention (not a dispute).** Three PROVED rows state a premise inside the claim: #12 and #14 ("given HW") and #17 ("given existence", which is OPEN). PP's own tally counts them as PROVED, and I follow it. Under a strict reading of "PROVED with a CONDITIONAL premise counts as COND" they would move, giving **14 / 12 / 8 / 5**. PP's call.
- Carried: junction **UNSOLVED**; full KK spectrum OPEN; MN N=2 CONDITIONAL (19a88b19).

## Updated recommendations (lane opinion; the Owner chooses)
- **Item 1 (unchanged in substance):**
  - Keep **(1a)**, the HW E₈ wall at the radial face, as the gluing. It is the only candidate consistent with f283cffd/f825dfff. Its pure exact-MN2 form is REFUTED, so closure rests on changing the face data. The live route is NL's cohomogeneity-two breathing sector (OPEN, T10); uniform breathing is REFUTED. Non-YM wall stress is the secondary OPEN route.
  - Record **(1b-i)** P only as a bulk symmetry. Do not gauge it, and do not combine it with the chiral HW wall (REFUTED).
  - Drop **(c1)** and **(c3)**.
  - **(c2)** needs an explicit Owner revisit of Group A (8b26c786).
- **Item 2 (re-checked after B5):** "use (2a) now, pursue (2c)" holds only in amended form.
  - **(2a) still holds** as the working idealization: a sharp ℤ₂ plane, with corrections of order (kℓ_p)(ℓ_p/L)^m, about 3% at L = ℓ_p (COND power counting). B5 strengthens the case: NL's JS-C route is itself thin-wall, so the thin-wall description is the one in use.
  - **(2c) as stated is REFUTED.** A smooth profile does not by itself remove the source (it carries 9760 units) or the NEC deficit (NL L5). It is replaced by **(2c′) thickness is not the lever.** The resolution of the thickness premise is (2a). The physics question moves to changing the face data via the cohomogeneity-two breathing sector (NL lead, OW 90cec14c; OPEN). If a smooth profile is found there, MR2 cross-checks its curvature and EFT and the 9760-unit smeared-charge stress.
  - **(2b)** is still not recommended: kε_y ∈ [0.630, 0.707] for every N, so a throat-sized wall is never thin, and the identification is OPEN.
