# MR2 erratum 2: fixes requested by the PP gate audit of the full-11D / Riemann / systole file (2026-11-09)
Header written at 18:28 CST. The file's own mtime is authoritative; see item 8.
- **Responds to:** PP FINDINGS_PP_AUDIT_MR2_FULL11D_EOM_RIEMANN_SYSTOLE_GATE_2026-11-09_1805.md (sha256 384096a8581c1b29bb59768877f36f7fd6caa10f72a23528ea8d058e1253cc19, verified, §14 items 1–8).
- **Additive:** nothing is edited. The affected files keep their hashes:
  - md 9ab8f0a6…
  - erratum 2efef556…
  - V2 .py/.log ad134752… / 49d0562c…
  - PERPOINT 31e40b87… / 4af22ea5…
- **Constraints:** tip 7cddb188… untouched. No CERT, no Gemini, nothing sent.
- **Adoption record:**
  - OW 19a88b19 (OWNER_WRITE_MAINCHAT_t4383_LIFT_VACUUM_HOLD_ADOPT_MN_N2_CONDITIONAL_2026-11-09_1806.md, sha 19a88b1958753ecaaa999e0ce763bca7fd449069278dd4bdb87cea002613ee03, verified): the Owner adopted **MN N=2 as the working vacuum, status CONDITIONAL**, and lifted the hold. This is an Owner adoption, not a proof. No earlier MR2 label changes because of it.
  - OW 7ff8299d (sha 7ff8299d…, verified): Γ := Bolza.
- **Scope:** the junction stays OPEN. The KK spectrum stays OPEN. The "warping lengthens the systole" claim is OPEN (withdrawn, item 3).
- **New evidence** is in MR2_TWISTED_VACUA_EINSTEIN_SYMBOLIC_AND_GLOBAL_CURVATURE_2026-11-09.md and its .py/.log files (shas listed there).

## 1. (D) prose, md 9ab8f0a6 §0: CORRECTED (the code was right)
The md wrote "e^{2f} = 4/9 so that L_AdS5 = 2/3". The correct statement:
- e^{2f} = F0 = **2/3**, so **L²_AdS5 = 2/3** and L = √(2/3) ≈ 0.8165.
- Then K ⊃ 40/L⁴ = 40·9/4 = 90.
- With e^{2g} = 1/6 and S⁴ radius ½, the totals are K = 90 + 144 + 384 = 618 and Ric² = 828. PROVED (arithmetic, matches the code).

## 2. Location of the curvature maximum: CORRECTED, and the global scan CONFIRMS PP
The md 9ab8f0a6 §1 phrase "maxima sit on the β = π/2−1e-6 / α-pole edges" is **withdrawn**.

**Scan method** (GLOBAL_CURVATURE runs):
- A 13×13 seed grid at dps 50 on the fundamental domain [0, π/2]².
- Golden-section refinement at dps 60.
- Box faces and poles handled as **limits**: Richardson extrapolation from offsets of 1e-7 and 1e-8 at dps 110.

**Results:**

| candidate | where the maximum is |
|---|---|
| MN2 (adopted working vacuum) | the **μ₁ = 1 pole** (α = π/2, β → 0) |
| BBBW z=2 | the μ₁ = 1 pole |
| BBBW z=3 | the μ₁ = 1 pole |
| MN1 | the **whole μ₀ = 0 circle** (α = π/2, any β) |

- The maximum sits at the same place for K, Ric², Weyl² and the curvature-operator spectral radius.
- For MN1 the invariants are constant along that circle to every printed digit, as expected from the X₁ = X₂, a₁ = a₂ symmetry rotating (μ₁, μ₂). So "μ₁ = 1 or μ₂ = 1" is a special case of the circle.

Limit values for MN2: K = 3408, Ric² = 3312, Weyl² = 1939.2 and max|eig Q| = 40/3, each to 28+ digits.

Status:
- Location and values: **PROVED at the evaluated points / limits** (numeric, 60 digits).
- **Global sup: CONDITIONAL** (numerical optimisation; no monotonicity proof).

## 3. "Warping makes the 11D systole longer": WITHDRAWN (OPEN); warp-safe thresholds and Bolza values
- The claim in md 9ab8f0a6 §2 is withdrawn. It is **OPEN** and unsupported.
- **The bound (PROVED given the metric):**
  - Along Σ the warp factor is Δ^{1/6}, and Δ = Σ X_α μ_α² ∈ [min X, max X].
  - The fibre terms are PSD. So every non-contractible loop satisfies sys₁₁ ≥ (min_α X_α)^{1/6}·ρ·sys_hyp.
  - The μ₀ = 1 section, which has no fibre term, gives sys₁₁ ≤ X₀^{1/6}·ρ·sys_hyp.
  - min X^{1/6} = 0.99046 / 0.93303 / 0.91347 / 0.90455 (MN1 / MN2 / z=2 / z=3) is < 1, so warping can shorten loops by up to ~10%.
- **Warp-safe thresholds** for sys₁₁ ≥ 2πℓ_p: sys_hyp ≥ 2π/(min X^{1/6}·ρ) = **0.2784 / 0.2529 / 0.2163 / 0.1905**, i.e. 0.19–0.28. This replaces the unwarped 0.17–0.28 in erratum 2efef556 E-3.
- **Bolza (Γ adopted):** sys_hyp = 2 arccosh(1+√2) = 3.05714183896.
  - The value is CONDITIONAL as literature (Jenni 1984; arXiv:2302.02540).
  - PP also re-derived it computer-assisted in floating point (384096a8 §10). The arithmetic is PROVED.

| candidate | ρ (ℓ_p) | sys₁₁ range [min X^{1/6}, X₀^{1/6}]·ρ·3.0571 (ℓ_p) | warp-safe threshold sys_hyp | Bolza margin |
|---|---|---|---|---|
| **MN2 (adopted, CONDITIONAL)** | 26.625201 | [75.95, 85.25] | 0.2529 | **12.1×** |
| MN1 | 22.788108 | [69.00, 72.39] | 0.2784 | 11.0× |
| BBBW z=2 | 31.807700 | [88.83, 102.46] | 0.2163 | 14.1× |
| BBBW z=3 | 36.455162 | [100.81, 117.82] | 0.1905 | 16.0× |

These agree with PP 384096a8 §10.

**Σ KK scale (CONDITIONAL estimate; the KK spectrum stays OPEN):**
- λ₁(Bolza) ≈ 3.838887258, from Strohmaier–Uski 2013 numerics as quoted in Kravchuk–Mazáč–Pal arXiv:2111.12716 §1.
- Note: **3.8388976481 is the KMP rigorous upper bound** for all genus-2 surfaces (their Thm 1.1(2)). It is not the Bolza value itself.
- Unwarped estimate: m²L₅² ≈ λ₁·e^{2f₀−2g₀} = 11.5 / **7.68** / 5.00 / 3.66 (MN1 / MN2 / z=2 / z=3). For MN2, e^{2f₀−2g₀} = 2 exactly.
- Wilson-line moduli and spin structure are not fixed by Γ, which is one more reason the KK spectrum is OPEN.

## 4. PERPOINT log lacks BBBW z=2 rows: DISCLOSED and SUPPLIED
- The frozen …_V2_PERPOINT_DIAG.log (4af22ea5…) covers only MN1, MN2 and z=3. That is a gap in that file.
- The new …_FRAME_EINSTEIN_AND_DG4_CONTROL.log (sha 604aa979f656cf38ca238fdf2a83ab5280b2674b57156a9e806d425a35e5f024; .py dd952331d4c1ec989f92774efb3c4ff7fc5f9435f7c3bac587760b2af29cc7e6) has **all four candidates, including z=2**.
- Each candidate gets 20 points: the V2 17-point grid, plus 2 near μ₁ = 1 and 1 near μ₂ = 1. Precision is dps 60.

## 5. dG₄ control that can fail: ADDED and RUN (same log)
Central finite difference, h = 1e-25, dps 60, at two generic points per candidate:

| case | max\|dG₄\| | verdict |
|---|---|---|
| λ = 1/16 | 3.6e-38 to 7.8e-37 | |
| **CONTROL λ = 0** | 2.5e-3 to 0.207 | ≈ \|G₄\|; **FAILS** |
| **CONTROL λ = (1/16)(1+1e-6)** | 2.5e-9 to 2.1e-7 | = 1e-6·\|G₄\|; **FAILS, linear response detected** |

- Bianchi is discriminating. dG₄ = 0 at the sampled points is PROVED.
- As PP notes, X₁×1.1 and flux×1.1 pass Bianchi by construction, so they are not dG controls.

## 6. Frame-normalized Einstein residuals: ADDED (same log)
- Measure: rel = ‖E‖_frame/‖Ric‖_frame (Frobenius norm over orthonormal-frame components; frame-invariant).
- Results at dps 60:

| candidate | generic points | near μ₁ = 1 / μ₂ = 1 | doubly-near-pole corners (round-off) |
|---|---|---|---|
| **MN2** | ≤ 3e-60 | ≤ 1.4e-50 | ≤ 1.9e-26 |
| MN1 | ≤ 4.5e-60 | ≤ 9.3e-51 | ≤ 2.1e-26 |
| BBBW z=2 | ≤ 3.4e-60 | ≤ 8.1e-52 | ≤ 6.5e-27 |
| BBBW z=3 | ≤ 3.3e-60 | ≤ 8.6e-51 | ≤ 1.2e-26 |

- Every point with only a single pole proximity is ≤ 4.5e-38.
- **Frame-normalized controls** (z=2, generic point), against 2.7e-60 for the true solution:
  - λ = 0: 0.295
  - λ = 14/16: 57.5
  - **λ(1+1e-6): 5.9e-7**
  - flux ×1.1: 0.21
  - X₁×1.1 (f, g recomputed): 0.164
- These **replace** the coordinate-mixed control numbers in md 9ab8f0a6 §3 (1.66e5 / 4.62e5 / 4.29e8 / 2.2e6) as the meaningful measure.

## 7. Symbolic Einstein, "all points": see the new symbolic/global md
- Status and labels are in MR2_TWISTED_VACUA_EINSTEIN_SYMBOLIC_AND_GLOBAL_CURVATURE_2026-11-09.md.
- Until a full symbolic zero is shown there, "all points" stays **CONDITIONAL**: CLP consistent truncation plus BBBW's 7D BPS solution (literature), plus the randomized exact test.

## 8. Cosmetics: CORRECTED here (the original files are not edited)
- V2 control label "LAMBDA=14/4" → the value used is **λ = 14/16 = 0.875** (code `mp.mpf(14)/4/4`).
- POLE_PRECISION_CONVERGENCE rows printed "pi/2-1.57" → these are **β = 1e-6** (the label printed π/2 − β).
- Erratum 2efef556 / md 9ab8f0a6 "6.8e-11" → **(ℓ_p/ℓ)⁶ = 6.65e-11** (6.648e-11).
- **Header times later than mtimes:**
  - md 9ab8f0a6 says "~17:50"; mtime 17:48:27 CST.
  - erratum 2efef556 says "~17:52"; mtime 17:48:52 CST.
  - From now on MR2 headers state "header written at" only from the clock (`date`), and the mtime is authoritative.
