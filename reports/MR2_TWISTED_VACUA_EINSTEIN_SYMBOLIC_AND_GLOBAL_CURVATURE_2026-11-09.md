# MR2: exact 11D Einstein check and global curvature maxima. MN N=2 first; MN1 and BBBW z=2, z=3 are secondary (2026-11-09)
Header written at 18:43 CST (from `date`). The file mtime is authoritative.

**Authority and scope**
- OW ff8a1670 (t4358), plus the parent steering of 17:49, 17:54, 18:06 and 18:07 CST.
- **Adoption record:** OW 19a88b19 (…t4383_LIFT_VACUUM_HOLD_ADOPT_MN_N2_CONDITIONAL_2026-11-09_1806.md, sha 19a88b1958753ecaaa999e0ce763bca7fd449069278dd4bdb87cea002613ee03, verified).
  - The Owner adopted **MN N=2 as the working vacuum, status CONDITIONAL**, and the hold is lifted.
  - This is an adopted working vacuum. It is **not proved**.
  - No earlier MR2 label is changed because of it.
- Γ := Bolza (OW 7ff8299d, verified).
- **Still open:** the junction, the KK spectrum, and the "warping lengthens the systole" claim (withdrawn in ERRATUM2).

**Constraints held:** additive only, with a sidecar for every file and each .py frozen (chmod a-w) before its log. Tip 7cddb188… untouched. No CERT, no Gemini, nothing sent.

**PP gate audit:** 384096a8… verified. All 8 PP fixes are applied in MR2_ERRATUM2_PER_PP_GATE_AUDIT_FULL11D_2026-11-09.md (sha 7b9ebdaf9d7656931e65c361cd1cce740479db91352969da4b54ff72ac84b720).

## Files (reports/, prefix … = MR2_TWISTED_VACUA_EINSTEIN_SYMBOLIC_AND_GLOBAL_CURVATURE_2026-11-09)
| file | sha256 | content |
|---|---|---|
| ….py | d0191f02b1b5596f2a7212e784fef2fd64a0d3f7c55ce2d2b1ea2d93c5b082ab | (A) exact Einstein. Modes: `points` (randomized exact) and `symbolic` |
| ….log | 01d6e4cd963d0fe0877d84e242a93f0f6f123ca520e642e3a6c0f350d65306cd | Points runs for all 4 candidates, controls, and symbolic-run status |
| …_MN2_SYMBOLIC_REDUCED.py | 3cfbe7da8726048f330f6eaec72e6aa11b11ce42fad8552f0c2c821a3f5e7a59 | MN2 full-symbolic variant over Q(X1, s_a, s_b). **Still running; no log filed** (see A.3) |
| …_GLOBAL_CURVATURE.py | d9388162a5886d62a66482f4c66c1e6c796d94d8ca45f7ea5e8ab73036920bba | (B) global maxima |
| …_GLOBAL_CURVATURE_MN2z1.log | 4893f1d2e40890b2c49cb681c824e9687d9b351befe16bc6e58ee9ceccf68cf2 | MN2 (primary) |
| …_GLOBAL_CURVATURE_MN1z0.log / _BBBWz2.log / _BBBWz3.log | aa28c625… / 1dae84ad… / 7d4d44d2… | Secondary candidates |
| …_FRAME_EINSTEIN_AND_DG4_CONTROL.py / .log | dd952331d4c1ec989f92774efb3c4ff7fc5f9435f7c3bac587760b2af29cc7e6 / 604aa979f656cf38ca238fdf2a83ab5280b2674b57156a9e806d425a35e5f024 | PP fixes 4–6: frame residuals for all 4 candidates (incl. z=2), and a dG₄ control that can fail |

Housekeeping note: a failed copy loop at about 18:27 CST created, for a few seconds, a sidecar for a not-yet-existing MN2 log. I removed that stray sidecar (my own file, just made) before the real log and sidecar were written. Nothing else was deleted.

## (A) Exact Einstein equations, all 66 components (λ = 1/16 as derived)
**Method.** Every step is exact and uses no tolerances.

*Exact geometry*
- Write g = Δ^{−2/3} ĝ with ĝ rational, and use the coordinates s_a = tan(α/2), s_b = tan(β/2).
- Get R_MN(g) from R_MN(ĝ) through the exact conformal formula (n = 11, ω = −⅓ ln Δ).
- The flux enters quadratically, so only |det ĝ| appears: E_MN = R_MN − Δ⁴|det ĝ|(X_MN − ĝ_MN Y/12)/12.
- All arithmetic is in the exact rational-function field Q(X₁, X₂[, s_a, s_b]).

*Imposing the fixed point exactly*
- Set X₂ = X₁(2z+w)/(1+z) and eliminate w = √(1+3z²) through BBBW (3.8).
- Reduce each numerator modulo the **minimal polynomial of X₁ over Q**:
  - MN2: 8X₁⁵ − 1
  - MN1: 4X₁⁵ − 3
  - z=2: 16X₁¹⁰ − 1228X₁⁵ + 81
  - z=3: 3X₁¹⁰ − 122X₁⁵ + 6
- A zero remainder means the value at the true algebraic fixed point is exactly zero (Galois). Denominators are checked to be nonzero.

*Reduction to r = v = 1*
- The metric and Ω are invariant under (t, x, r) → λ(t, x, r) and under the H² isometries (u, v) → (λu + c, λv).
- These act transitively on r × H², so it suffices to check r = v = 1.

*Built-in consistency checks*
- ĝ·Δ^{−2/3} equals the V2 `cand_metric()` symbolically: True.
- The exact-route Ricci scalar R·Δ^{−2/3} = 4.798942827238612093395905 at z=2, (s_a, s_b) = (2/9, 7/5). It matches the independent V2 numerics to all 25 printed digits (GLOBAL_CURVATURE log, first line).

### A.1 Results by candidate: randomized exact test, 8 random rational points (r, v, s_a, s_b), 66 components each
| candidate | components identically 0 in Q(X₁,X₂) | remaining components reducing EXACTLY to 0 mod minpoly | label |
|---|---|---|---|
| **MN2 (adopted working vacuum)** | 53/66 at every point | **13/13 at all 8 points** | **CONDITIONAL (randomized exact test)** |
| MN1 (secondary) | 52/66 | 14/14 at all 8 points | CONDITIONAL (randomized exact test) |
| BBBW z=2 (secondary) | 52/66 | 14/14 at all 8 points | CONDITIONAL (randomized exact test) |
| BBBW z=3 (secondary) | 52/66 | 14/14 at all 8 points | CONDITIONAL (randomized exact test) |

Each of these 32 point-checks is an exact proof that E_MN = 0 at that point (PROVED pointwise, exact). The statement for all points is a randomized identity test, so it is **CONDITIONAL** and not a full symbolic zero.

### A.2 Exact controls (z=2, rational point (3/7, 5/11, 2/9, 7/5))
| control | result |
|---|---|
| λ = 1/8 | 15 components not zero |
| λ = 0 | 15 components not zero |
| flux × 11/10 | 15 components not zero |
| X₁ × 1.1 (X₂ fixed) | max\|E_MN\| = 8.18 |

All four **FAIL, as required** (PROVED).

### A.3 Full symbolic zero: NOT finished within the cap, so it stays OPEN
- Symbolic mode in the field Q(X₁, X₂, s_a, s_b) was started at 18:00 CST for all four candidates.
- MN1, z=2 and z=3 were **killed at about 18:08 CST** to free CPU for MN2, per the Owner priority.
- MN2 is still running in two variants:
  - the general field;
  - the reduced …_MN2_SYMBOLIC_REDUCED.py over Q(X₁, s_a, s_b) with X₂ = 2X₁. That one also has a λ = 1/8 control.
- At 18:43 CST neither had finished building E_MN, and neither has printed anything past its header.
- Their scratch logs are /workspace/scratch/mr2_1750/sym_MN2z1.log and symred_MN2.log. Their timeouts end at about 18:55 and 19:08 CST.
- No log for the reduced variant has been filed in reports/. If it completes, its result must be filed as a new dated log plus sidecar, and checked for the line "MN2 FULL SYMBOLIC ZERO … True".
- **Honest remaining path:**
  1. Let the reduced MN2 run finish. If sparse-field gcds remain the bottleneck, a CAS with faster multivariate gcd (Singular, Maxima) could be installed instead.
  2. Alternatively, upgrade the randomized test to a proof with an explicit degree bound in (s_a, s_b) on the numerators, then check on a grid of (d+1)² points.
  3. ETA is 1–3 h of compute. It is not claimed here.
- **So the Einstein equations for all points remain CONDITIONAL** for every candidate, MN2 included. The basis is CLP/BBBW literature plus this randomized exact test, plus PROVED exact zeros at 32 points and numeric zeros at 29+20 points.

### A.4 Frame-normalized numerics (PP fix 6) and the dG₄ control (PP fix 5)
Source: FRAME log, dps 60, 20 points per candidate, rel = ‖E‖_frame/‖Ric‖_frame.

| candidate | generic | near μ₁=1 / μ₂=1 | doubly-near-pole corners (round-off) |
|---|---|---|---|
| **MN2** | ≤ 3.0e-60 | ≤ 1.4e-50 | 1.9e-26 |
| MN1 | ≤ 4.5e-60 | ≤ 9.3e-51 | 2.1e-26 |
| BBBW z=2 (rows previously missing) | ≤ 3.4e-60 | ≤ 8.1e-52 | 6.5e-27 |
| BBBW z=3 | ≤ 3.3e-60 | ≤ 8.6e-51 | 1.2e-26 |

**Frame-normalized controls (z=2):**

| case | rel |
|---|---|
| true | 2.7e-60 |
| λ = 0 | 0.295 |
| λ = 14/16 | 57.5 |
| λ(1+1e-6) | 5.9e-7 |
| flux ×1.1 | 0.21 |
| X₁×1.1 | 0.164 |

**dG₄ (FD, h = 1e-25):**
- At λ = 1/16: ≤ 7.8e-37.
- **Control λ = 0:** ≈ |G₄| (up to 0.207), so it **FAILS**.
- **Control λ(1+1e-6):** 1e-6·|G₄|, so it **FAILS**.
- Label: PROVED at the sampled points.

## (B) Global maxima over the internal space (60+ digits)
**Method**
- Fundamental domain α, β ∈ [0, π/2], using the isometries α → π−α and φᵢ → φᵢ+π.
- 13×13 seed grid at dps 50 (offset 1e-5 from the faces).
- Golden-section refinement at dps 60.
- **Faces and poles evaluated as limits:** Richardson extrapolation (v = L + cε² + O(ε⁴); the invariants are even in the distance to each face) from ε = 1e-7 and 1e-8 at dps 110.
- The curvature-operator spectral radius is computed with mpmath `eig`.
- **Γ-independence:** the scan does not depend on Γ. Σ = H²/Γ is locally H² and the metric is smooth, so every local invariant is the same for any Γ, Bolza included.

| candidate | location of max (all four invariants) | Riem² max (1/ℓ⁴) | Ric² max | Weyl² max | max\|eig Q\| (1/ℓ²) | ℓ_p²√Riem² | ℓ_p²√Ric² | ℓ_p²√Weyl² | ℓ_p² max\|K_sec\| ≤ | (ℓ_p²\|K_sec\|)³ |
|---|---|---|---|---|---|---|---|---|---|---|
| **MN2** | **μ₁ = 1 pole** (α=π/2, β→0) | **3408** (3407.999…9984) | **3312** | **1939.2** | **40/3** (13.33…332) | 0.023648848835 | 0.023313387176 | 0.017839041403 | **5.4013080741e-3** | 1.576e-7 |
| MN1 | whole μ₀ = 0 circle (constant along it) | 910.37168945107 | 1061.5446988600 | 439.66271020234 | 6.6290206204046 | 0.012222768437 | 0.013198645219 | 0.008494152005 | 2.6854036950e-3 | 1.937e-8 |
| BBBW z=2 | μ₁ = 1 pole | 5755.4015839793 | 5086.0476042105 | 3499.8677696553 | 18.849276792155 | 0.030732509759 | 0.028890191632 | 0.023965474403 | 7.6358063196e-3 | 4.452e-7 |
| BBBW z=3 | μ₁ = 1 pole | 7318.5634802628 | 6203.9185271593 | 4567.3024479509 | 21.890345523905 | 0.034655577020 | 0.031907535060 | 0.027377267412 | 8.8677375017e-3 | 6.973e-7 |

- These **confirm PP 384096a8 §8**: the maximum is at μ₁ = 1 (for MN1, on the full μ₀=0 circle, which contains μ₁=1 and μ₂=1). They also correct MR2's earlier "edges" phrasing; see ERRATUM2 item 2.
- The face-limit consistency |v(1e-8) − v(1e-7)| is 1e-10 to 1e-14, as expected for an O(ε²) approach. The Richardson extrapolation removes that error.
- The values agree with the earlier grid maxima to below 1e-5 relative.
- **Labels**
  - The value at the located point/limit is **PROVED** (numeric, 60 digits, Richardson limit).
  - The location being the **global** max is **CONDITIONAL**: dense seed grid plus local optimisation.
- **Monotonicity is not proved.** The grid profiles show K, Ric², Weyl² and eig Q strictly decreasing in β along the α = π/2 edge for MN2 / z=2 / z=3, and constant along the α = 1e-5 and β = π/2 edges. That is evidence, not a proof, so it is not labelled PROVED.
- The R⁴ size (CONDITIONAL on the R⁴ coefficient) is unchanged: 1.6e-7 for MN2.

## (C) Bolza (Γ adopted, OW 7ff8299d): systole and Σ KK scale. Details in ERRATUM2 item 3
- sys_hyp = 2 arccosh(1+√2) = 3.05714183896. The value is CONDITIONAL as literature; PP also re-derived it computer-assisted. The arithmetic is PROVED.

| candidate | ρ (ℓ_p) | sys₁₁ range (ℓ_p) | warp-safe threshold sys_hyp | Bolza margin |
|---|---|---|---|---|
| **MN2** | 26.625 | **[75.95, 85.25]** | 0.2529 | **12.1×** |
| MN1 | 22.788 | [69.00, 72.39] | 0.2784 | 11.0× |
| z=2 | 31.808 | [88.83, 102.46] | 0.2163 | 14.1× |
| z=3 | 36.455 | [100.81, 117.82] | 0.1905 | 16.0× |

- The range bounds are PROVED given the metric: lower bound by the warp minimum, upper bound by the μ₀ = 1 section.
- The margin is PROVED arithmetic on a CONDITIONAL literature value.
- **Σ KK scale (CONDITIONAL estimate):**
  - λ₁(Bolza) ≈ 3.838887258. The parent's 3.8388976 is the KMP genus-2 **upper bound** (3.8388976481, arXiv:2111.12716 Thm 1.1). The Bolza value itself is 3.838887258 (Strohmaier–Uski, as quoted by KMP).
  - Unwarped m²L₅² ≈ λ₁e^{2f₀−2g₀} = **7.68 for MN2** (e^{2f₀−2g₀} = 2 exactly). The other candidates give 11.5 (MN1), 5.00 (z=2) and 3.66 (z=3).
  - The KK spectrum stays **OPEN** (warping, Wilson lines, spin structure).

## (D) Cosmetic flaws self-flagged in the earlier files (not edited; corrected in ERRATUM2 item 8)
- V2 label "LAMBDA=14/4" means **14/16**.
- The "pi/2-1.57" rows mean **β = 1e-6**.
- **6.8e-11** should be **6.65e-11**.
- Header times ran later than mtimes: 9ab8f0a6 "~17:50" vs 17:48:27; 2efef556 "~17:52" vs 17:48:52.
- Additional slips:
  - The V1 header line "#!/usr/bin/env python3" sits below the V2 header comment (harmless).
  - The ERRATUM2 header says 18:28 CST but its mtime is 18:32:30 CST, so the mtime is authoritative.
  - The V2 PERPOINT log lacks z=2 rows; they are supplied in the FRAME log.

## Label summary
| item | MN2 (adopted, CONDITIONAL vacuum) | MN1 / z=2 / z=3 (secondary) |
|---|---|---|
| Einstein at 8 random rational points, exact | PROVED (pointwise exact) | PROVED (pointwise exact) |
| Einstein, all points | **CONDITIONAL** (randomized exact test + CLP/BBBW) | CONDITIONAL |
| Full symbolic zero | OPEN (run in progress, not finished) | OPEN (runs killed for priority) |
| Maxwell, G∧G, λ = 1/16 | PROVED (identically; earlier files) | PROVED |
| dG₄ = 0, with failing controls | PROVED at sampled points | PROVED at sampled points |
| Frame residuals ≤ 3e-60 generic | PROVED at sampled points | PROVED at sampled points |
| Global curvature max values / location | values PROVED (numeric limit); global sup CONDITIONAL | same |
| Bolza systole margin | 12.1× (PROVED arithmetic; CONDITIONAL literature value) | 11.0× / 14.1× / 16.0× |
| KK spectrum; warping-lengthens-systole; junction | OPEN | OPEN |
