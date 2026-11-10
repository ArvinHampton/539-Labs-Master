# NL DERIVED: junction setup on constant-radius faces — MN N=2, MN N=1, BBBW (z=2 worked) at N = 4880, g = 2 — 2026-11-09 16:55 CST (America/Chicago)
Author: Non Local Path (NL). Everything below is an **NL derived proposal**.
Authority:
- OW 48102805 (OWNER_WRITE_MAINCHAT_t4339_NL_JUNCTION_DERIVATION_GO_THREE_CANDIDATES_2026-11-09_1646.md, sha verified 4810280562b2…): GO to set up the junction for the three candidates. b stays free and OPEN.
- OW f283cffd (t4337, 16:44): brane := stack of N wrapped M5-branes; face := 10D matching hypersurface where the near-throat M5 geometry meets the asymptotic background.
- OW aaadb280: vacuum choice on HOLD. **No vacuum is adopted. The three candidates are shown side by side.**
Limits: new additive file. No MR2 curvature numbers used (all geometry derived here). No CERT. Nothing sent outside; arXiv text already on the box (BBBW 1203.0303, CLP hep-th/9903214, MN hep-th/0007018) was read. Tip 7cddb188… checked before and after.
Inputs: NL 1620 (418e4e50) as corrected by erratum 4 (e58cede8). Started 16:46:52 CST.

## 0. Conventions (J0, PROVED by arithmetic)
- Standard 11D sugra (G = ½T^(EH), OW 2d1e877e), quantum (2πℓ_P)³N, N = 4880, genus 2, κ = −1.
- κ₁₁² = 8πG₁₁ = 128π⁸ ℓ_P⁹. T_M5 = 1/((2π)⁵ℓ_P⁶). So κ₁₁²T_M5 = 4π³ ℓ_P³ = 124.0251 ℓ_P³.
- BBBW units have L₇ = 1. Physically L₇ = 2(πN)^{1/3} ℓ_P = 49.684382 ℓ_P. The S⁴ radius is L₇/2, so the CLP gauge coupling is g_c = 2/L₇.

## 1. Flow ansatz (J1, CONDITIONAL on CLP uplift and BBBW (A.15) BPS equations; hep-th/9903214, 1203.0303 App. A)
- 7D, in the h = f gauge: ds₇² = e^{2f(r)}(dx²_{1,3} + dr²) + e^{2g(r)} ds²(H²/Γ), with scalars λ₁(r), λ₂(r), X_i = e^{2λ_i}, X₀ = (X₁X₂)^{−2}.
- Twist gauge fields: F⁽¹⁾ = (1+z)/8 vol_H², F⁽²⁾ = (1−z)/8 vol_H². They are r-independent, and A_r = 0.
- BPS system (A.15):
  - f′ + λ₁′ + λ₂′ + E = 0
  - g′ + λ₁′ + λ₂′ − ⅛(1+z)e^{f−2g−2λ₁} − ⅛(1−z)e^{f−2g−2λ₂} + E = 0
  - 3λ₁′ + 2λ₂′ + 2E − 2e^{f+2λ₁} − ⅛(1+z)e^{f−2g−2λ₁} = 0
  - 2λ₁′ + 3λ₂′ + 2E − 2e^{f+2λ₂} − ⅛(1−z)e^{f−2g−2λ₂} = 0
  - Here E = e^{f−4(λ₁+λ₂)}.
- 11D uplift: ds₁₁² = Δ̃^{1/3} ds₇² + g_c^{−2} Δ̃^{−2/3} [X₀^{−1}dμ₀² + Σ_i X_i^{−1}(dμ_i² + μ_i² Dφ_i²)], with Δ̃ = Σ_a X_a μ_a².
- **UV** (r → r*): locally AdS₇×S⁴ throat. λ_i → 0, e^f(r − r*) → 1, and f − g → const.
- **IR** (r → ∞): AdS₅×Σ₂, BBBW (3.8).
- **J1a (PROVED, numerical).**
  - The IR fixed points solve (A.15): residual ≤ 2×10⁻¹⁶. L₅ reproduces NL 1620.
  - Linearization exponents ν, with δ ∝ r^ν:

    | candidate | ν |
    |---|---|
    | MN2 | {−1, −2, 2, 4} |
    | MN1 | {−1, −(√7−1), 2, 1+√7} |
    | z=2 | {−1, −2.224042, 2, 4.224042} |
    | z=3 | {−1, −2.330565, 2, 4.330565} |

  - ν = −1 is the r-translation gauge mode. The other negative ν equals 4 − Δ for the irrelevant operator: Δ = 6, 3+√7, 6.2240 and 6.3306. These are exactly the masses in 1620 B1–B3, so the two computations cross-check.
- **J1b (CONDITIONAL, numerical integration of (A.15), rtol 10⁻¹²).** Each candidate has one flow, up to the gauge freedoms of x-rescaling and r-shift. It leaves the IR along the irrelevant mode.
  - One sign reaches AdS₇: λ ~ 10⁻¹⁶, e^f(r − r*) = 1.000000, f − g constant.
  - The other sign runs into a scalar singularity.
- **J1c (CONDITIONAL, numerical).** g(r) increases strictly toward the UV on every flow. So the face is labeled gauge-invariantly by the 7D-frame Σ radius R_Σ(b) = L₇e^{g(r_b)} ∈ (R_Σ^IR, ∞).
  - R_Σ^IR = 26.624 ℓ_P (MN2), 22.788 ℓ_P (MN1), 31.807 ℓ_P (z=2), 36.455 ℓ_P (z=3).
  - Check: 4πR_Σ² equals the Area in 1620.
  - The map R_Σ(b) ↔ b is not defined (see J6).

## 2. Face and induced metric (J2, PROVED as the restriction of the J1 metric; it inherits J1's condition)
- The face is r = r_b:
  h = Δ̃^{1/3}[e^{2f_b} dx²_{1,3} + e^{2g_b} ds²_Σ] + g_c^{−2} Δ̃^{−2/3} [X₀^{−1}dμ₀² + Σ X_i^{−1}(dμ_i² + μ_i² Dφ_i²)], with all functions evaluated at r_b.
- It is 10D: ℝ^{1,3} × (S⁴ fibred over Σ₂ by the twist). It is warped over S⁴ through Δ̃(μ).
- **J2a (PROVED).** The face is static and 4D-Poincaré invariant, since the flow depends only on r and A_r = 0. So there is no time-dependence obstruction.

## 3. Extrinsic curvature (J3, PROVED: symbolic check verify_sym.py, residual 0; finite-difference check on the flows, relative error ≤ 6×10⁻⁸)
- Unit normal: n = Δ̃^{−1/6} e^{−f} ∂_r, pointing toward the IR. There is no shift, so K_ab = ½ n^r ∂_r h_ab.
- In the r-independent frame (dx, e_Σ, dμ, Dφ_i), with D′/D := ∂_r ln Δ̃:
  - k_x (4 directions) = n^r (f′ + D′/(6D))
  - k_Σ (2 directions) = n^r (g′ + D′/(6D))
  - k_{φ_i} = n^r (−D′/(3D) − λ_i′)
  - k_μ (2 directions) = n^r [−D′/(3D) + eig(½ Ĝ^{−1}∂_rĜ)], with Ĝ = Σ_a X_a^{−1} dμ_a² on S².
  - K = 4k_x + 2k_Σ + k_{φ₁} + k_{φ₂} + Σ k_μ.
- **J3a (PROVED, limits).**
  - IR face, exact AdS₅×Σ: k_x = −Δ̃^{−1/6}/L₅, k_Σ = k_fib = 0, K = 4k_x.
  - UV face, AdS₇ throat: k_x = k_Σ → −1/L₇, k_fib → 0, K → 6k_x.
  - Numbers at the IR face, ⟨k_x⟩ over S⁴ in ℓ_P⁻¹: −2.6508e-2 (MN2), −2.5331e-2 (MN1), −2.7454e-2 (z=2). For comparison, 1/L₅ = 2.6558e-2, 2.5336e-2 and 2.7544e-2.
  - Full profiles at R_Σ/R_Σ^IR = 1.001, 1.1, 1.5, 3 and 10 are in face.log.

## 4. Israel condition and side pairings
- Condition: [K_ab − h_ab K] = −κ₁₁² S_ab, with [X] = X(IR side) − X(UV side) and the normal as in §3.
- Source: N_b M5-branes on ℝ^{1,3}×Σ₂, smeared over the S⁴ fibre of the face with unit-normalized density ρ(y). The stress is S_ab = −N_b T_M5 ρ(y) P^{wv}_ab, where P^{wv} projects onto the 6 worldvolume directions (x, Σ). The fibre components are zero.

### P1. Smooth pairing (both sides are the same flow)
- **PROVED.** [K] = 0, so S = 0. A stack with N_b ≠ 0 cannot sit on a regular face of a single smooth flow.

### P2. Interior = throat flow (r < r_b), exterior = exact AdS₅×Σ₂
- **PROVED: no solution.** Continuity of h_ab requires (g, λ₁, λ₂)(r_b) = (g₀, λ*). f is matched by x-rescaling. (A.15) is autonomous and has the (x, r)-rescaling symmetry, so by ODE uniqueness the flow would then equal the fixed point identically, which contradicts the AdS₇ UV.
- **P2′ (OPEN).** Gluing to a non-BPS exterior with the same h_ab was not studied.

### P3. Z₂ orbifold
- Keep the IR side (r > r_b) and excise the throat, as in RS2. Keeping the UV side flips the sign.
- Then S_ab = −(2/κ²)(K_ab − h_ab K).
- With the smeared M5 source this needs:
  - (a) k_Σ = k_x pointwise;
  - (b) every fibre eigenvalue equals K, i.e. zero fibre stress;
  - (c) N_b T_M5 ρ = (2/κ²)|k_x − K|.
- **P3a (REFUTED, by proof at the two end faces).** Claim tested: "Israel with smeared-M5 tension alone holds on the AdS₅×Σ face or the AdS₇ throat face."
  - IR: (a) gives 0 ≠ k_x, and (b) gives 0 ≠ 4k_x.
  - UV: (b) gives 0 ≠ 6k_x.
- **P3b (CONDITIONAL on numerical sampling).** On interior faces (404 faces per candidate), the fibre residual ⟨|k_fib − K|⟩/⟨|k_x|⟩ lies in [4.000, 5.99]. It is never 0, so there are no solutions. The Σ residual goes to 0 only as R_Σ → ∞. **Number of solutions with a pure M5 source: 0 for every candidate.**
- **P3c (CONDITIONAL on smearing, the Z₂ factor 2 and §0 conventions).** The relation that the condition forces, if only the 4D components (a)–(c) are imposed (RS-style tuning, the components PP's earlier algebra used): N_b(r_b) = (2/(κ²T_M5)) ∫_{S⁴_b} |k_x − K| dvol₄.
  - N_b rises monotonically from the IR value to the UV value 10N/3:
    - MN2: 12568.6 → 16266.7
    - MN1: 12252.1 → 16266.7
    - z=2: 12812.2 → 16266.7
    - z=3: 12942.4 → 16266.7
  - **N_b = 4880 is reached on no face.** It would need N_b/N ∈ [2.51, 3.33]. The Σ components require 4/3 × the x value at the IR face, so the 4D-only tuning is not consistent either.
- **P3d (PROVED, analytic).** At the UV face, N_b → (2/(κ²T_M5)) · 5/L₇ · Vol(S⁴_{L₇/2}) = 5L₇³/(12π) = 10N/3 = 16266.67. The numerical value is 16268.6, a grid error of 1×10⁻⁴.
- **P3e (CONDITIONAL on the Z₂ parity of G₄; PP O1 is OPEN).** Charge from dG₄ = 2κ²T_M5 δ:
  - If G₄|_{S⁴} is odd, N_b = 2N = 9760.
  - If G₄|_{S⁴} is even, N_b = 0.
  - Either way, charge ≠ tension. Tension/charge (odd case) is 1.288 (MN2), 1.255 (MN1), 1.313 (z=2) and 1.326 (z=3) at the IR face, and 5/3 at the UV face.
  - So a Z₂ face with only M5 stress is not BPS. It breaks the flow's susy.

### Remaining items
- **J5 (OPEN).** Localized (unsmeared) M5s are codimension 5 inside the face, so the thin-shell Israel form does not apply directly.
- **J6 (OPEN).** b and the map b ↔ R_Σ(b). r_b was never fixed.
- **J7 (OPEN).** What extra face stress closes the junction: fibre pressure, anisotropic Σ tension, G₄ legs on Σ or worldvolume flux. Israel fixes the required values as S^{fib} = −(2/κ²)(k_fib − K) and S^Σ − S^x ∝ (2/κ²)(k_Σ − k_x), but no source for them is defined. Whether such a face can preserve the 4 (or 8) supercharges is also OPEN.

## 5. Comparison table (no vacuum adopted)
| | MN N=2 (z=1) | MN N=1 (z=0) | BBBW z=2 (worked) | BBBW z=3 |
|---|---|---|---|---|
| L₅ [ℓ_P] | 37.653721 | 39.470162 | 36.305054 | 35.600612 |
| R_Σ^IR [ℓ_P] | 26.624 | 22.788 | 31.807 | 36.455 |
| flow mode Δ (ν = 4−Δ) | 6 | 3+√7 | 6.2240 | 6.3306 |
| AdS₇→AdS₅ BPS flow | yes, unique up to gauge | yes | yes | yes |
| face static, Poincaré | yes | yes | yes | yes |
| P1 smooth / P2 fixed-pt exterior | no brane / no solution | same | same | same |
| P3 Z₂, pure smeared M5: solutions | 0 | 0 | 0 | 0 |
| N_b(r_b) from 4D tuning, IR → UV | 12568.6 → 16266.7 | 12252.1 → 16266.7 | 12812.2 → 16266.7 | 12942.4 → 16266.7 |
| N_b/N | 2.58 → 3.33 | 2.51 → 3.33 | 2.63 → 3.33 | 2.65 → 3.33 |
| tension/charge, IR face (odd G₄) | 1.288 | 1.255 | 1.313 | 1.326 |
| fibre residual range | [4.00, 4.64] | [4.00, 4.06] | [4.00, 5.57] | [4.00, 5.85] |

The z dependence is mild. For general z the structure is the same: J3 formulas, P1, P2, P3a and P3d are z-independent statements, while P3b and P3c are numerical per z.

## 6. Tally
| label | count | items |
|---|---|---|
| PROVED | 9 | J0, J1a, J2, J2a, J3, J3a, P1, P2, P3d |
| CONDITIONAL | 6 | J1, J1b, J1c, P3b, P3c, P3e |
| OPEN | 4 | P2′, J5, J6 (b), J7 |
| REFUTED | 1 | P3a (proof at the AdS₅ and AdS₇ end faces) |

## 7. Scripts and logs
All are in /workspace/nl-junction-1646/, each with a .sha256 sidecar.
- flowlin.py b72d22963c279baed4c5072442abe2f5eb33b45b9bcaa368dca3d2a8f04193c6: BPS system, fixed points, linearization.
- shoot.py 1f342987c6bacbafb6a9b6205805221e01c8efd496cad61e3043daaceed9b539: sign selection.
- face.py fd309c488678ba1d60ca37139dc048d5321ec2e1ebe67c426f4b273b11a7edc5: flows, induced metric, K, Israel residuals, N_b, finite-difference check. Log face.log 036955e77e6e8cbc8c67f2c982a14fb9cfcd0ebbdf23a0d280590e2748c2469f.
- scan.py cf7b3354201d9ca3c293fde153a32263f92d4b276a0d13651f0b9cae00ea7ec7: dense face scan. Log scan.log 16920e3c43cdae33c6ccb01dc632c312df6a08f7842cee8748d0c47e1a10816b.
- verify_sym.py 55bf13d615af7b464dcb5ca5d559b509c68a2575d472a5226b6a5b6071476a83: symbolic K check via Christoffels.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
