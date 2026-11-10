# NL DERIVED: t552u non-BPS cluster: an exact necessary condition for an 11D-NEC face on any 3-scalar truncation flow (Z2 corner / S2-13, non-BPS Z2, non-BPS S5)
2026-11-10, 1209 CST (America/Chicago). **NL derived proposal.** Resonant algebra. Additive only. No existing file is edited, renamed, deleted or chmod-ed. The 2057 and 1110 scripts and logs are read only. This file re-types the frozen face formulas; it does not import or edit them.
Authority: OW t552u "Pursue all for resolution." (eae1b39d635c69966a2b32642d395ae402d3c33fcf64db7f0b77cad2d8c60db2 = sidecar), pursuit only; OW 1117 geometry-first (bff79185…); standing t4436 (32881263…); OW 1108 (c6375f85…), OW 1130 (945d81bb…), t4431 (f700141d…), f825dfff. t552u cancels none of these.
Frozen parents: Z2 corner (101467fc…), S5 of 2026-11-09 (3ceb0605…), Erratum 24 (60bbc718…), Erratum 25 (01b7141f…; PP confirm 5dd9a6cd…), PP resume audit (b39c7756…), E1 (2f33b65d…); face definitions /workspace/nl-bps-d6-2057/z2_centre_flow_faces.py (21bcbc3f…, as cited in the Z2 corner file).
**Nothing adopted. Junction: UNSOLVED. No candidate wall. No CERT.** No Gemini, no Ops, nothing sent, no agent messaged. Not in scope (sister job): the non-BPS tension-charge gap (D-B3 / A6–A16), GA9, S4.
Premises carried for the record: (h0) = Erratum 24 (h2), x-independent Poincaré supercharges; listed because BPS items are referred to. It is not used by the NEC items, which are non-BPS. (ii) is the D1 HW hypothesis Γ^nε = ε (not S6; S6 is the odd-HW record f825dfff). It is likewise not used by the NEC items.
Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91: checked 11:47:21 CST, 12:06:04 CST, 12:09:21 CST (immediately before this write). The after-write check is reported to NL.

Script (/workspace/nl-bps-t552-1110/; sidecar frozen before the run, log sealed after; all four files mode 444):
| file | sha256 | time (CST) |
|---|---|---|
| z2_nec_necessary_exact_2026-11-10.py | 5d342df45b11605781d94a19540b8aeb02bb6a938c70b126ef047188359193b2 | sidecar frozen 12:06:04 |
| z2_nec_necessary_exact_2026-11-10.log | 718cc019dfc994e321c1842c7ccbe32c351d64f399cbcbb96a1622e4d26c1efb | sealed 12:06:06; **7 passed, 0 failed, exit 0** |
Exact sympy; tests are expand(...)==0 or exact Rational comparisons. (A dry run of a copy was made in /tmp before freezing. A first draft used simplify(...)==0 in one cross-check; it was replaced by an expand identity **before** the freeze. Neither dry run supports any claim.)

**Tally: PROVED 3 · CONDITIONAL 0 · OPEN 2 · REFUTED 0 · total 5.**

## 0. Geometry demands algebra (lead section; summary of B1–B3, no new claims)
The Z2 fixed plane with a doubled Israel jump needs a wall stress obeying the NEC: k_v − k_x ≤ 0 for every unit internal direction v at every point of the face (PP Y15, as in the frozen face()). This is a pointwise geometric demand, so it can be tested at the three axis points μ = e₁, e₃, e₅ of the S⁴ fibre and along Σ, where the shape operator is diagonal. Doing so forces two algebraic conditions on the 7D flow data **at the face**, with no reference to the IR:
- the dilaton-type scalar must run fast: 2φ′ ≤ A′ (< 0);
- the potential must be subdominant: |V| ≤ (3/8)·12A′², that is, the face must sit in a kinetic-dominated region.
Near the MN2 IR, or anywhere velocities are small, neither holds. So the geometry rules out NEC faces there, and leaves only kinetic-dominated faces as candidates.

## 1. Claims
- **T552-B1 (PROVED; exact). Axis-point margins.** In the frozen face conventions (eps = Δ^{−1/6}e^{2φ} > 0; k_x = eps(A′ − 2φ′ + D′/6); k_S = eps(3φ′ + D′/6); fibre K = ½ eps g^{−1}ġ), with ′ = d/dr as in the code:
  - (k_S − k_x)/eps = 5φ′ − A′ at every point (D′ cancels) (log Z-N1).
  - At μ = e_i the fibre shape operator is diagonal in the e_j (j ≠ i). The margins m(e_i; e_j) := (k_{e_j} − k_x)/eps are (2φ′ − A′) plus:
    - μ = e₁: e₂: 6λ′; e₃, e₄: λ′ − w′/2; e₅: λ′ + w′.
    - μ = e₃: e₁, e₂: λ′ − w′/2; e₄: −4λ′ − w′; e₅: −4λ′ + w′/2.
    - μ = e₅: e₁, e₂: λ′ + w′; e₃, e₄: −4λ′ + w′/2.
    (log Z-N2). This is cross-checked against the frozen (χ,θ,ψ) chart at μ = e₃ (exact identity, Z-N4a/b).
- **T552-B2 (PROVED; exact). NEC ⇒ 2φ′ ≤ A′.**
  - m(e₁; e₂) + 2m(e₃; e₄) + 2m(e₅; e₁) = 5(2φ′ − A′) identically (log Z-N3).
  - NEC makes each margin ≤ 0 (eps > 0), so any nonnegative combination is ≤ 0. Hence **2φ′ − A′ ≤ 0** on every NEC face.
  - Then 5φ′ − A′ ≤ (3/2)A′ ≤ 0, so the Σ-direction margin is automatically compatible. The remaining conditions bound (λ′, w′) inside the polygon {6λ′, λ′ − w′/2, λ′ + w′, −4λ′ − w′, −4λ′ + w′/2} ≤ A′ − 2φ′.
- **T552-B3 (PROVED; exact). NEC faces are kinetic-dominated.**
  - With the frozen Hamiltonian constraint 12A′² = 30φ′² + 30λ′² + (3/2)w′² − V and A′ ≤ 0: B2 gives φ′ ≤ A′/2 ≤ 0, so φ′² ≥ A′²/4.
  - Hence **−V ≤ (9/2)A′² − 30λ′² − (3/2)w′²**, i.e. |V|/(12A′²) ≤ 3/8 (log Z-N5).
  - At zero scalar velocity the combination equals −5A′ > 0 (Z-N6), so no NEC face exists at or near the MN2 IR, or anywhere the potential dominates.
  - **Scope:** every face of every flow in the 3-scalar (φ,λ,w) truncation with the CGR uplift, BPS or not, with **any** IR (regular, singular, or not reaching MN2). So it applies to the Z2 corner (S2-13), to non-BPS Z2 walls, and to the truncation part of non-BPS S5 (S3b-4). It does not use the BVP labelling, the grid, R or any float.
  - This narrows the corner from "unbounded in d₆" to the analytic region 𝒩 = {2φ′ ≤ A′, |V| ≤ (3/8)·12A′², (λ′,w′) in the B2 polygon} at the face. Any corner orbit with an NEC face must enter 𝒩. This file neither uses nor regrades the Z-2 numerics (float, CONDITIONAL as filed).
- **T552-B4 (OPEN). Z2 corner / S2-13 and non-BPS Z2 walls.**
  - Whether any truncation orbit (Z2 centre flow with Δ6 admixture, any d₆ ≤ −0.20, or any other kinetic-dominated flow) reaches 𝒩 with **all** margins ≤ 0 at all points of S⁴ is not decided.
  - B2/B3 use only three axis points and Σ. The full NEC on the whole S⁴ is stronger, and was not used analytically.
  - A monotonicity argument for 2φ′ − A′ along second-order flows (A″ = −(30φ′² + 30λ′² + (3/2)w′²)/3 ≤ 0 from the constraint) was not completed: the φ-equation involves ∂_φV with no fixed sign.
- **T552-B5 (OPEN). Non-BPS S5 (S3b-4) outside the 3-scalar truncation.**
  - Non-BPS NEC walls on general (r, χ, θ, Σ)-dependent kept sides with a singular IR are not addressed. B3 covers only the truncation.

## 2. Branch register (t4436; not counted; nothing adopted)
- **[w]/Z2 non-BPS:** kept, OPEN (B4), narrowed to the kinetic-dominated face region 𝒩 by B2/B3, pending PP audit.
- **Non-BPS S5:** kept, OPEN (B5). Inside the truncation it is narrowed by B3 in the same way.
- **[χS], [χU]:** kept. The B-items are truncation statements; [χ] wall content enters only through the wall stress, which B1–B3 constrain pointwise.
- BPS items are in the companion BPS-cluster file of this time.
- S6 (odd HW ℤ₂, f825dfff) is a record premise, not a mathematical escape.

## 3. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 3 | B1, B2, B3 |
| CONDITIONAL | 0 | — |
| OPEN | 2 | B4, B5 |
| REFUTED | 0 | — |

Check: 3 + 0 + 2 + 0 = 5.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before this write, 12:09:21 CST; after-write check reported to NL).
