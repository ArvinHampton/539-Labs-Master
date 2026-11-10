# NL CANDIDATES: b and J7 — MN N=2, odd HW-type ℤ₂ wall — 2026-11-09 (America/Chicago)
Author: Non Local Path (NL). **Everything below is an NL derived proposal. Nothing is adopted; the Owner chooses.**

**Tally: PROVED 7 · CONDITIONAL 3 · OPEN 2 · REFUTED 3 (total 15).** Item lists in §4.

Authority: OW b0b9ae7f ("Pursue all for resolutions"; NL items include b and J7), sidecar MATCH. In force: f825dfff, 7ff8299d (b OPEN), 19a88b19 (no source and no b adopted), 49b04146, 36683379.
Companion: NL_CANDIDATES_JUNCTION_SOURCES_MN2_VS_PP_aeb9ab13_2026-11-09_1859.md (sha 9987bdcd…), cited as "JS".
Scripts: /workspace/nl-cand-1854/clp_face_lemma.py (4bf4ed0d…), log 2cdd6e37….
Limits: new file only. No CERT, no Gemini, nothing sent.
Not used as Owner text: the t4363 entry "J7 REJECTED" (recorded, not adopted, in that OW), and the pasted "b at the E₈ density peak" (t4396u; not adopted per OW 49b04146).

## 1. What the record defines
- **b.** There are two on-record meanings.
  - PP 9dde377d B2: the separation of two faces, at y = 0 (+U) and y = b (−U), in ds² = e^{−2A(y)}g₄ + dy² + e^{2B}ĝ₆. It gives V₇eff = V̂₆e^{6B}(1 − e^{−2kb})/(2k).
  - NL 1655 J6 / OW 48102805: the face position r_b on the flow, with the map b ↔ R_Σ(b) never defined.
  - The record never fixes which meaning is intended. NL treats both below.
- **J7.** NL 1655 §4: "What extra face stress closes the junction: fibre pressure, anisotropic Σ tension, G₄ legs on Σ or worldvolume flux … no source for them is defined. Whether such a face can preserve the 4 (or 8) supercharges is also OPEN." The standing status is OPEN.

## 2. b — candidates
### b-1 Single wall (RS2 reading)
**Definition.** f825dfff has one ℤ₂ plane with the IR kept on both sides, so there is no second face. Set b := u_b = ln(R_Σ(r_b)/R_Σ^IR) ∈ (0, ∞), a gauge-invariant wall position (J1c), and take the y-interval as infinite.
- **b1a (PROVED, limit of 9dde377d B2).** V₇eff → V̂₆e^{6B}/(2k), which is finite.
- **b1b (CONDITIONAL, P3c numerics).** Under pure M5/E₈ tuning, N_b(u_b) runs over [12568.6, 16266.7). It never equals 9760, so no u_b is selected.
**Compatibility.** Matches f825dfff (one fixed plane). It adopts nothing.

### b-2 Two-wall HW interval (RS1 reading)
**Definition.** b := the proper distance between the f825dfff wall and a second ℤ₂ plane deeper in the IR (an S¹/ℤ₂ interval).
- **b2a (PROVED).** G is odd at both planes, and ∮dG = 0 on the covering circle, so the second plane carries charge −2N_flux = −9760.
- **b2b (PROVED at the end faces, given J1; NL 1711 E3).** The second plane has the bulk on its UV side, so its energy density is negative. That makes it a negative-tension, negative-charge object of O-plane type, which ties b-2 to JS-A.
- **b2c (OPEN).** What stabilizes b. There is no stabilizing potential on record.
**Compatibility.** f825dfff defines only one face, so b-2 adds an object the record does not have.

### b-3 Dynamical b
**Definition.** b := the wall position at which the full junction system (Israel, any scalar junction conditions, Hamiltonian constraint) has a solution.
- **b3a (REFUTED, by proof).** Claim: "b-3 has a solution with an exact-MN2 bulk and NEC-satisfying sources at the IR end face" (JS L1: τ = 8 > 6). On interior faces the same failure is CONDITIONAL (1711 E2).
- **b3b (REFUTED, by proof).** Claim: "b-3 has a solution with any CLP-truncation bulk and an M5/E₈-fibre wall" (JS C1).
- **b3c (CONDITIONAL, JS C8).** With the S⁴ breathing mode, the counting gives isolated solutions, so b is derived, not chosen.

**Remark (REFUTED, by proof).** Claim: "b := the radius where the E₈ instanton density peaks". The E₈ fields live on the face r = r_b, so their density is a function on Σ × S⁴. Its peak picks a point of the face, not a radius.

**NL recommendation for b.** b-3. Use b-1's u_b as the label in the meantime. Take b-2 only if the Owner wants a two-wall HW interval, which brings a negative-tension second wall (b2b).

## 3. J7 — candidates
### J7-1 The deficit tensor (bookkeeping)
**Definition.** J7 := Δ_ab = S_ab(required) − S_ab(charge sector). The charge sector is 9760 BPS units on x×Σ (σ_M = 6/1.28777).
- **J7a (CONDITIONAL on the 1.288 horizontal measure, PP's warp caveat).** At the MN2 IR wall, Δ = extra tension (x 1.341, Σ 3.341, fibre 8.000) in units k/κ².
- **J7b (PROVED).** Given J7a, Δ violates NEC: ρ+P = −2.000 along Σ and −6.659 along the fibre.
**Compatibility.** It defines J7 without adopting a source (19a88b19).

### J7-2 G₄ legs or worldvolume flux
**Definition.** J7 := the stress from G₄ legs on or crossing the face, or worldvolume H₃ on the M5s.
- **J7c (REFUTED, by proof).** Claim: "J7-2 closes the exact-MN2 wall". G₄ jumps give no δ-stress (1711 G1, PROVED), and brane-localized charges and fields satisfy NEC, so τ ≤ 6 < 8 (JS L1).

### J7-3 J7 = 0 with near-wall backreaction
**Definition.** J7 := 0. The bulk next to the wall deforms (JS-C with the breathing mode) so that the BPS charge sector alone satisfies Israel.
- **J7d (PROVED, JS C4).** It closes locally.
- **J7e (OPEN, JS C7).** Global existence.

**NL recommendation for J7.** Take J7-1 as the definition, since it is what J7 always meant, now explicit at the adopted vacuum and wall. Pursue J7-3 as the resolution. Close J7-2 as REFUTED.

## 4. Tally (header checked)
| label | count | items |
|---|---|---|
| PROVED | 7 | §1 record readings (b two meanings; J7 wording), b1a, b2a, b2b, J7b, J7d |
| CONDITIONAL | 3 | b1b, b3c, J7a |
| OPEN | 2 | b2c, J7e |
| REFUTED | 3 | b3a, b3b, J7c |
The E₈-peak remark is REFUTED but is listed as a remark and not counted. Counting it as well gives REFUTED 4, total 16.
PROVED is counted as 7: the §1 record readings count as 2 (b, J7), plus b1a, b2a, b2b, J7b and J7d.
Check: 7 + 3 + 2 + 3 = 15.

Tip: 7cddb188 unchanged at start. No CERT. Nothing sent.
