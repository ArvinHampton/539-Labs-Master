# MR2 candidate resolutions, batch 1 (OW b0b9ae7f): (1) smooth φ₂→−φ₂ ℤ₂ vs HW/orbifold gluing at the face; (2) the wall-thickness premise — 2026-11-09, written 19:26 CST (America/Chicago)
Author: MR2. **Nothing is adopted. The Owner chooses.** Labels: PROVED / COND (CONDITIONAL) / OPEN / REF (REFUTED). Additive only. Tip 7cddb188… untouched (verified). No CERT, no Gemini, nothing sent outside.

Authority and inputs (all sha = sidecar, verified 19:16 CST):
- OW b0b9ae7f (t4407, Owner's words: "Pursue all for resolutions").
- OW 8b26c786 (t4414, "Group A": Aut⁺(Bolza) × wall ℤ₂).
- OW f825dfff (face := ℤ₂ fixed plane, HW-type; G₄ odd; E₈ sector COND).
- OW f283cffd (brane := wrapped M5 stack; face := 10D matching hypersurface).
- OW 90cec14c (t4415, "S4 breathing mode. Pursue it." NL leads).
- MR2 8399be55 (Pin⁺: A × W consistent given HW).
- MR2 ERRATUM2 5511845e (fixes 3, 4, 6). PP aeb9ab13, PP fe0c3d92.

Files: this .md (sidecar); `MR2_CANDIDATE_RESOLUTIONS_BATCH1_PHI2_Z2_VS_HW_AND_WALL_THICKNESS_PER_OW_b0b9ae7f_2026-11-09.py` 56c05c236abb6820020ea3faf251f2e9907204a90ef60b6cb0adbf39d4072db2 (frozen before run); `.log` 88d2d7fb77d7295bdccd22c35c64002c3aebf8087e5008b29666a17898ae8a30 (exit 0, 76 s, dps 40; V2 routines sha ad134752 asserted).

## 0. Two lemmas used by both items
- **L1 (PROVED, log (A)). tr R∧R is pointwise nonzero on the φ₂ fixed set F₁₀ = AdS₅ × (twisted S³ bundle over Σ).**
  - Method: induced 10D metric (V2 cand_metric with the φ₂ row and column removed; g_{φ₂,·} = 0 at a₂ = 0), Euclidean t, orthonormal frame.
  - Result: max |tr(R∧R)_{abcd}| = 51.9 / 75.7 / 78.2 / 64.5 (ℓ⁻⁴ units) at 4 sample points, on the (u, v, α|β, φ₁) components; the induced Riem² there is 323–937. Antisymmetry checks pass at ≤ 2.4e-15.
  - F₁₀ is totally geodesic and the ℤ₂ is odd on the normal leg, so every 11D component R_{n a c d} with one normal index vanishes there. Hence the 11D tr R∧R restricted to F₁₀ equals the intrinsic one.
- **L2 (PROVED, cohomology). p₁(F₁₀) = 0.** F₁₀ ≅ AdS₅ × Σ × S³ topologically (ERRATUM2 fix 4). TΣ ⊕ ℝ is trivial and S³ is parallelizable, so T(Σ×S³) is stably trivial. Therefore tr R∧R is exact, and every 4-cycle (γ × S³, γ ∈ H₁(Σ)) has zero integral.
- **L3 (PROVED, given a thin-wall Israel junction at the exact-MN2 constant-r face and brane-type sources). Size of the NEC deficit.**
  - Statement: any source mix that supplies the required 6:8:8 stress must contain negative energy density Σ|σ| ≥ 2k/κ² = ρ_w/3.
  - Proof:
    - For each internal null k = t̂ + ê, S_req(k,k) = −2k/κ² (ERRATUM2 fix 3).
    - NEC-respecting parts contribute ≥ 0.
    - A brane-type part T = −σ h_wv contributes σ(1 − |ê_∥|²), which is ≥ −|σ| when σ < 0.
    - Summing gives Σ|σ| ≥ 2k/κ².
  - In M5 tension units (log (C), measure COND per ERRATUM2 fix 6): **≥ 3527–5599 (horizontal measure) or ≥ 2873–4560 (fixed-φ measure).**

## Item 1. Smooth φ₂ ℤ₂ versus HW/orbifold gluing at the face
### (1a) HW E₈ wall at the radial face, with wall charge 9760
**Definition.** The face of f283cffd (the 10D matching hypersurface at constant r) is the fixed plane of W: ρ → −ρ, C → −C on the doubled (kink) MN2. G₄ is odd. An E₈ wall sector sits on the plane with N_M5 + n_inst = 2N = 9760 (f825dfff).

| consequence | grade |
|---|---|
| Matches f283cffd and f825dfff by construction (radial 10D face; wrapped M5 charge N through S⁴) | PROVED (definitional) |
| N = 4880 and wall charge 9760 exact | PROVED (ERRATUM2 fix 1) |
| Pin⁺ / KK Group A: A × W consistent | COND (8399be55: X spin, descent, HW, FH Thm 2.2) |
| Anomaly inflow: E₈ on the fixed plane cancels the ℤ₂-boundary anomaly | COND (Hořava–Witten hep-th/9603142; inflow math not rederived) |
| NEC: exact MN2 on both sides + thin wall + E₈-YM/M5 content closes the junction | **REF** (no-go PROVED, fe0c3d92 Y3-ineq; ERRATUM2 fix 3) |
| Rescue by bulk deformation near the face (S⁴ breathing mode, NL) | OPEN (NL lead, OW 90cec14c; NL reports the local face equations close, PP audit pending) |
| Rescue by non-YM wall stress (HW −½ tr R², higher-derivative wall terms) | OPEN |
| Count gap: N_req/2N ∈ [1.084, 1.721] horizontal, [0.883, 1.402] fixed-φ | COND (measure and M5 location); overlaps NL's (1.255, 1.667), not decisive |

### (1b) Smooth φ₂ parity P: φ₂ → −φ₂, C → −C
**Definition.** P acts on smooth (undoubled) MN2. Its fixed set is F₁₀. There are two variants:
- (b-i) P is only a global symmetry, not gauged;
- (b-ii) P is gauged as an M-theory ℤ₂ orbifold, so F₁₀ becomes an HW-type plane.

| consequence | grade |
|---|---|
| P is a symmetry (isometry, φ*G₄ = −G₄, together with C → −C) | PROVED (ERRATUM2 fix 4) |
| F₁₀ totally geodesic, no Israel stress; topologically AdS₅×Σ×S³, metrically twisted | PROVED |
| G₄ has exactly one normal (φ₂) leg, so it is smooth across F₁₀; no Bianchi source, wall charge **0** | PROVED |
| P is the f283cffd/f825dfff face | **REF**: F₁₀ sits at fixed S⁴ position (a fibre wall) and does not separate a throat region from an asymptotic region in r. PROVED given those definitions. |
| (b-i) needs no E₈ sector or wall at all | PROVED, but it is not a face and does not touch the junction |
| (b-ii) HW condition: G_tangent\|F₁₀ = 0, so tr F² = ½ tr R² pointwise | PROVED given the HW boundary condition |
| (b-ii) a nontrivial E₈ field (F ≠ 0) is required | PROVED (L1) |
| (b-ii) net instanton number on every 4-cycle is 0, so cohomologically allowed | PROVED (L2) |
| (b-ii) existence of an E₈ connection with tr F² = ½ tr R² pointwise (e.g. a spin-connection-type embedding) | COND (E₈ trace normalisation and embedding not verified) |
| (b-ii) that E₈ field has NEC-positive stress but F₁₀ has K = 0, so this is consistent only at leading order in HW's κ^{2/3} expansion; backreaction | OPEN |
| P combined with the HW wall W of (1a) | **REF given HW (f825dfff)**: P reflects exactly one wall-tangent direction (φ₂), so it reverses the 10D wall orientation and maps the HW projection to the opposite chirality. This is the same argument as 8399be55 §B for r, and is incompatible with chiral E₈ wall content. |
| NEC no-go / count gap | not applicable; neither is addressed (charge 0, no Israel stress) |

### (1c) Hybrid or orientifold-like options (only well-defined ones)
- **(c1) W × P as a joint orbifold.**
  - The group action is well defined: the two maps commute and act on different coordinates (PROVED).
  - It is REF given HW, by the chirality argument in (1b).
  - The composite W∘P also has a codimension-2 ℝ²/ℤ₂ fixed locus with no known M-theory description (OPEN).
- **(c2) W × (P∘r)**, with r a Σ-reflection: this is 8399be55 cases (i′)/(ii′).
  - It reflects an even number of wall-tangent directions, is orientation-preserving, needs only a Spin lift, and commutes with W̃.
  - COND consistent (8399be55; not rederived here).
  - r ∉ Aut⁺, so this would change the Owner's Group A choice.
  - It is a symmetry option only; no effect on the NEC, the junction or the count.
- **(c3) OM5-type orientifold σ_O: (ρ, φ₁, φ₂) → (−ρ, φ₁+π, φ₂+π), C → −C, on the doubled geometry.**
  - Well defined (PROVED): the φ shifts are isometries commuting with the U(1) twist, ρ → −ρ is an isometry of the kink metric, the map is orientation-reversing in 11D, and G₄ must be ρ-odd (as in HW).
  - Fixed set {ρ = 0, μ₀ = ±1}: two 6D loci ℝ^{1,3} × Σ, i.e. local ℝ⁵/ℤ₂ OM5 planes (PROVED).
  - Each carries M5 charge and tension −½: COND. Witten hep-th/9512219 and Dasgupta–Mukhi hep-th/9512196; the T⁵/ℤ₂ tadpole arithmetic 32·(−½) + 16 = 0 was checked, the derivation was not.
  - Total negative tension is about −1 M5 unit, against a required ≥ 2873–5599 (L3). **REF as an NEC fix**, by more than 3 orders of magnitude (given thin-wall Israel; count normalisation COND).
  - It also leaves the δ-kink on all of ρ = 0, so it does not replace a 10D wall source.

### Item-1 recommendation
- **(1a)** is the only candidate consistent with f283cffd/f825dfff as the face. Its pure form (exact MN2, thin wall, E₈+M5 only) is REF. Recommend keeping (1a) as the face gluing, with closure delegated to NL's breathing-mode route (OPEN) or to a computation of non-YM wall stress (OPEN, ~1 h).
- Record **(1b-i)** P as a bulk-only global symmetry. Do not gauge it (b-ii) and do not combine it with the chiral HW wall (REF).
- Drop **(c1)** and **(c3)**. **(c2)** is available only if the Owner revisits Group A.

## Item 2. The premise that the wall thickness is ≳ ℓ_p
Log (B): R_S4 = (πN)^{1/3} ℓ_p = 24.842 ℓ_p. The flux check 8π²R³ = (2π)³N matches to 15 digits (PROVED, given 2κ² = (2π)⁸ℓ_p⁹, Dirac-consistent). 1/k ∈ [35.13, 39.43] ℓ_p, L₅ = 37.65 ℓ_p.

### (2a) Thin-wall idealization with the validity bound stated
**Definition.** The wall is the sharp ℤ₂ fixed plane (thickness 0, as for an HW boundary). Bulk fields are trusted in two-derivative sugra for structures probed at scales L ≳ few ℓ_p. The σ_ε smoothing is only a regulator.

| consequence | grade |
|---|---|
| Israel weights −6k / 0 / −8k exact; NEC no-go applies | PROVED (ERRATUM2) |
| The 1/ε² divergence is a regulator artefact, not physical | PROVED (finite for every ε; only the δ-weight is regulator-independent) |
| Corrections ~ (kℓ_p)(ℓ_p/L)^m, m ≥ 1: 0.025–0.028 at L = ℓ_p; 0.0085–0.0095 (m=1) and ~1e-3 (m=3) at 3ℓ_p | COND (power counting) |
| Sharpness of an HW fixed plane itself | PROVED as a definition (fixed set of a ℤ₂), COND as physics (HW) |
| The "≳ ℓ_p" premise is replaced by a stated coarse-graining scale | PROVED as bookkeeping |

### (2b) Resolved wall, thickness set by the M5/E₈ core
**Definition.** ε_y := R_S4 = (πN)^{1/3} ℓ_p (transverse size of the N-M5 throat), or the E₈ instanton size.

| consequence | grade |
|---|---|
| R_S4 = 24.842 ℓ_p; EFT factor ~1e-3 | PROVED (arithmetic) |
| kε_y = 0.630–0.707: **not thin** compared with 1/k (thin wall needs kε ≪ 1), so the Israel weights would get O(1) corrections | PROVED (scale comparison) |
| The E₈ instanton size is a modulus along the wall directions, and HW E₈ fields live on the boundary, so it sets no normal thickness | PROVED given HW (definitional) |
| "Wall thickness = R_S4": in MN2 the whole geometry is the wrapped-M5 near-horizon region, so the throat is not a wall | OPEN (no derivation; the identification is conceptually doubtful) |

### (2c) Thickness fixed dynamically by the S⁴ breathing mode (or another modulus)
**Definition.** The face is a smooth domain wall of the breathing scalar (NL, OW 90cec14c). ε_y is its gradient length, interpolating from the face data to the MN2 IR.

| consequence | grade |
|---|---|
| Existence of the profile; its width; joining to the MN2 IR | **OPEN (depends on NL's breathing-mode work; ETA per OW 90cec14c ~21:30 / ~23:30 CST)** |
| If it exists as a smooth solution: no δ-source, no Israel stress and no NEC deficit (the L3 bound applies only to thin walls) | COND (on existence) |
| Width ~ AdS scale (L₅ ≈ 37.7 ℓ_p ≫ ℓ_p) would put it well inside the EFT | OPEN (estimate only) |
| Then the thin-wall picture (2a) becomes the kε → 0 limit, valid only if the width ≪ 1/k ≈ 35–39 ℓ_p | PROVED (scale comparison), given existence |
| MR2 will cross-check the curvature and EFT of any NL solution | per OW 90cec14c |

### Item-2 recommendation
- Use **(2a)** now as the working idealization, with the stated bound (corrections ≤ (kℓ_p)(ℓ_p/L)^m, about 3% at L = ℓ_p) replacing the OPEN "≳ ℓ_p" premise.
- Treat **(2c)** as the candidate physical resolution, OPEN pending NL. If it succeeds, it also removes the NEC obstruction for (1a).
- Do not adopt **(2b)**: a throat-sized wall is not thin (kε ≈ 0.7), and the identification is unsupported.

## Rollup (this file's new claims; one label per atomic claim; Owner-definitional items excluded)
- **PROVED 15:**
  1. L1
  2. L2
  3. L3
  4. P symmetry
  5. F₁₀ geometry
  6. charge 0 for P
  7. P is not the face
  8. (b-ii) E₈ F ≠ 0 required
  9. (b-ii) zero net instanton number
  10. c1 group well-defined
  11. σ_O well-defined
  12. σ_O fixed set (OM5 loci)
  13. R_S4 / flux arithmetic
  14. kε_y = 0.63–0.71
  15. E₈ instanton size gives no normal thickness (given HW)
- **COND 7:**
  1. A × W Pin⁺
  2. HW anomaly inflow
  3. count-gap measure
  4. (b-ii) existence of an E₈ connection with tr F² = ½ tr R²
  5. OM5 charge −½
  6. (2a) power counting
  7. (c2) consistency
- **OPEN 7:**
  1. breathing-mode rescue of (1a) (NL)
  2. non-YM wall stress
  3. (b-ii) backreaction
  4. ℝ²/ℤ₂ locus of c1
  5. (2b) identification
  6. (2c) existence/width (NL)
  7. (2c) EFT width estimate
- **REF 4:**
  1. pure (1a) closure with E₈+M5
  2. P with the HW wall (and c1)
  3. P as the f283cffd face
  4. (c3) as an NEC fix
- Carried: junction **UNSOLVED**; full KK spectrum OPEN; MN N=2 CONDITIONAL (19a88b19).
