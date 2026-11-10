# MR2 — Twisted-vacua adoption blockers: full Riemann invariants, Σ systole, full 11D EOM (MN1, MN2, BBBW z=2, z=3; N=4880, g=2)
Written 2026-11-09 ~17:50 CST by MR2 (executor). Per Owner voice OW ff8a1670… (t4358 "pursue all open items to resolution"), plus the 17:36 steering (PP audit fc5e0156…).
Additive file. No existing file was edited. The protected tip 7cddb188… was re-verified unchanged at 17:45 CST.
No CERT, no Gemini, nothing sent outside. **Nothing is adopted.** The junction stays **OPEN**. I take no stance on DP-a or Layer2.
Conventions are those of MR2 V2 (sha d6e9b1f1…): uplift units with R_AdS7 = 1 and S⁴ radius ½. The physical metric is ℓ²×(uplift), with ℓ = 2(πN)^{1/3} ℓ_p = 49.6843822 ℓ_p.
Equations: R_MN = (1/12)(G_MPQR G_N^PQR − g_MN G²/12), d*G + ½G∧G = 0, dG = 0.

## Files (reports/)
| file | sha256 | role |
|---|---|---|
| …_FULL_EOM_2026-11-09.py | e2a1f02d16f8810c761934f1fc647b7ad71f2a430ae1fec0b2bbb326e50737a6 | V1, frozen. **Superseded**: it crashed in the Einstein section. |
| …_FULL_EOM_2026-11-09.log | 71227fdb43716c83f7e0b555c12c5abfe52d212164da12d48a3525a98b004efd | V1 log. Validations and the λ solve are complete, then a TypeError traceback. |
| …_FULL_EOM_2026-11-09_V2.py | ad134752da79e3064e209cd840b0aec53e004e3fa0fec8bbc9299eb12940eb85 | The only change is that mp.det on singular g⁻¹ minors is replaced by an exact-pivot `sdet` (mpmath LU throws on an all-zero pivot column). No physics, grid or tolerance change. |
| …_FULL_EOM_2026-11-09_V2.log | 49d0562c08d8dc65a0baf64214795e49e4a88ec0adb675653e2dc61e5867051c | Main results. exit 0, 149 s. |
| …_V2_PERPOINT_DIAG.py / .log | 31e40b874f638d01dcc55dc421d42812e3a43116f9cb8f26cbabdc01bd26a9b6 / 4af22ea5a1a1aa78f90dd508b4c513f28019fa64e82b3fb0085f46fa3753caf8 | Einstein residual at each grid point |
| …_V2_POLE_PRECISION_CONVERGENCE.py / .log | 784585e4a338f34b2c53cee6d1a3fba34c6dceb166a07be349be5a7306588643 / 4b2a36d69b77c6e443051790254ee5d383a4cabbac04157a6b9f818982607029 | Pole corners at dps 40/60/90 |
| …_V2_SYMBOLIC_MAXWELL.py / .log | b28db23bda3d521bea77caa5d7df370bd9e3517fc746c4701d3b0d34f83d6e9d / 72665f4794d87916e37fe9e5cc8f1696684c6883e61c2db06e4a59adcaf78600 | Exact sympy simplify of d*G₄ |
Every file has a `.sha256` sidecar, and each .py was frozen (chmod a-w) before its log was written.
Cosmetic label slips in the code, which I did not edit: the V2 control prints "LAMBDA=14/4", but the value used is 14/16 = 0.875. In the precision log, β = 1e-6 rows print as "pi/2-1.57".

## 0. Validations (PROVED: own numerics against exact closed forms)
**AdS₇×S⁴ with the true Freund–Rubin flux**
- max|E^M_N| = 5.5e-40 at a generic point and 7.2e-22 at a near-pole point (θ₁ = 1e-6).
- A **wrong-flux ×1.1** control gives 2.52, so it **FAILS as required**.
- K = 468 (exact), Ric² = 828, R = 6, and max|eig| of the curvature operator = 4 (exact).

**(D) product AdS₅×H²×S⁴ inside the candidate ansatz** (X = 1, a = 0, e^{2f} = 4/9 so that L_AdS5 = 2/3, e^{2g} = 1/6)
- K = 618, Ric² = 828, R = 6 and max|eig Q| = 6, all exact, including at (α, β) = (1e-6, 1e-6).

## 1. Full Riemann invariants on a pole-reaching grid (V2 log)
**Grid**
- α ∈ {1e-6, π/4+d, π/2+d, 3π/4+d, π−1e-6} × β ∈ {1e-6, π/4+d, π/2−1e-6}, with d = 1.234e-3 (PP shift), plus 2 generic points.
- That is 17 points at dps 40. The invariants depend only on (α, β).

| candidate | K = Riem² range (1/ℓ⁴) | Ric² max | Weyl² range | ℓ_p²√K max | ℓ_p²√Ric² max | ℓ_p²√W² max | max\|eig Q\| (1/ℓ²) | ℓ_p² max\|K_sec\| ≤ | R⁴: (ℓ_p²\|K_sec\|)³ | R⁴: (ℓ_p²√K)³ |
|---|---|---|---|---|---|---|---|---|---|---|
| MN1 z=0 | [375.807, 910.370] | 1061.54 | [209.69, 439.66] | 1.2223e-2 | 1.3199e-2 | 8.494e-3 | 6.629019 | 2.6854e-3 | 1.94e-8 | 1.8e-6 |
| MN2 z=1 | [511.808, 3407.981] | 3311.98 | [297.90, 1939.19] | 2.3649e-2 | 2.3313e-2 | 1.7839e-2 | 13.333308 | 5.4013e-3 | 1.58e-7 | 1.3e-5 |
| BBBW z=2 | [501.091, 5755.361] | 5086.01 | [311.98, 3499.84] | 3.0732e-2 | 2.8890e-2 | 2.3965e-2 | 18.849233 | 7.6358e-3 | 4.45e-7 | 2.9e-5 |
| BBBW z=3 | [507.266, 7318.506] | 6203.87 | [322.59, 4567.26] | 3.4655e-2 | 3.1907e-2 | 2.7377e-2 | 21.890290 | 8.8677e-3 | 6.97e-7 | 4.2e-5 |

- **Status: PROVED at sampled points; the global maximum is CONDITIONAL.** The maxima sit on the β = π/2−1e-6 / α-pole edges of the grid. A finer or optimised scan is still to do.
- These **CONFIRM PP fc5e0156 §7a** to every printed digit: Riem² max 910.4 / 3408 / 5755.4 / 7318.5 /ℓ⁴, max|eig Q| 6.629 / 13.333 / 18.849 / 21.890, and ℓ_p²|K_sec| 2.685e-3 / 5.401e-3 / 7.636e-3 / 8.868e-3.
- The sectional-curvature bound |K_sec| ≤ max|eig| of the curvature operator is a linear-algebra fact. It is exact for the Riemannian internal block and used as a bound overall.
- **R⁴ correction size: CONDITIONAL** on the standard scaling of the ℓ_p⁶R⁴ term.
  - It is ~2e-8 to 7e-7 measured by sectional curvature, and ~2e-6 to 4e-5 measured by the coarser √K.
  - Either way it is far above the old (ℓ_p/ℓ)⁶ ≈ 6.8e-11 estimate, and still ≪ 1. The supergravity EFT is controlled.

## 2. Σ systole (genus 2)
**Bolza number — CONDITIONAL (literature)**
- The maximal systole of a genus-2 hyperbolic surface (curvature −1) is 2 arccosh(1+√2) = 3.057141838962. It is attained uniquely by the Bolza surface.
- Sources: Jenni, Comment. Math. Helv. 59 (1984) [Jen84]. Restated as the optimal genus-2 bound ≈ 3.057142 in Fortier Bourque–Petri, arXiv:2302.02540 §6.2, and in arXiv:1812.05341 (introduction).
- The arithmetic 2acosh(1+√2) is **PROVED** (own mpmath).

**What is fixed and what depends on Γ**
- **Fixed** (Gauss–Bonnet and the BPS fixed point):
  - the curvature radius ρ = ℓe^{g₀};
  - the area 4πρ² = 6525.7 / 8908.3 / 12713.8 / 16700.4 ℓ_p²;
  - the mass of an M2 wrapped on all of Σ.
- **Γ-dependent** (genus-2 modulus, 6 real parameters):
  - the systole, the length spectrum and the diameter;
  - **λ₁(Σ), and so the masses of the KK modes on Σ.**
- Γ is the Owner's open choice.
- **Status: OPEN.** The actual systole cannot be computed until Γ is fixed.

**Physical systole range, sys_phys = sys_hyp·ρ** (unwarped; arithmetic PROVED)

| candidate | ρ (ℓ_p) | L₅ = ℓe^{f₀} (ℓ_p) | range (0, Bolza] (ℓ_p) | min sys_hyp for sys_phys ≥ ℓ_p | min sys_hyp for sys_phys ≥ 2πℓ_p | min sys_hyp: wrapped-M2 string √T ≥ 1/L₅ |
|---|---|---|---|---|---|---|
| MN1 | 22.788108 | 39.470162 | (0, 69.666] | 0.04388 | 0.2757 | 0.00111 |
| MN2 | 26.625201 | 37.653721 | (0, 81.397] | 0.03756 | 0.2360 | 0.00105 |
| z=2 | 31.807700 | 36.305054 | (0, 97.241] | 0.03144 | 0.1975 | 0.00094 |
| z=3 | 36.455162 | 35.600612 | (0, 111.449] | 0.02743 | 0.1724 | 0.00085 |

- Warping makes the 11D systole longer. PP's warped bounds are sys₁₁ ∈ [22.6, 23.7] / [24.8, 27.9] / [29.1, 33.5] / [33.0, 38.5] × sys_hyp ℓ_p. With that warping, PP's 2πℓ_p thresholds become 0.278 / 0.253 / 0.216 / 0.191. I carry those **as PP's (CONDITIONAL on PP's warp bound)**. Mine above are the unwarped ρ-only values.
- **Binding condition.** Winding and wrapped-M2 modes stay above the KK scale when sys_hyp ≳ 0.2–0.28. This uses the conservative 2πℓ_p criterion, which is the one PP uses; the ℓ_p criterion gives only 0.03–0.04.
- The wrapped-M2-string criterion is much weaker (about 1e-3).
- The Bolza surface (3.057) satisfies every criterion by more than 10×. A Γ near a degeneration (a pinched cycle) would violate them.
- **Criterion choice: CONDITIONAL** (it is a convention). **Actual Σ systole: OPEN.**

## 3. Full 11D equations of motion
**G₄ last-term prefactor λ — PROVED** (exact, own symbolic computation; this settles the PP item)
- Ω = *G₄ = κ[U ε₇ + λ Σᵢ Xᵢ⁻² d(μᵢ²)∧(dφᵢ + aᵢ du/v)∧(aᵢ e^{−2g₀}) vol₅]. Ansatz: CLP hep-th/9903214 (4.2) / BBBW 1203.0303 (4.5), with λ left free.
- G₄ has legs only in the 6 internal directions, so G∧G ≡ 0 and Maxwell reduces to dΩ = 0.
- Solving dΩ = 0 gives **λ = 1/16 exactly for all four candidates**: 0.0625000… in every non-trivial component (MN1's β-component vanishes identically). The V2_SYMBOLIC_MAXWELL log shows that sympy `simplify` of both components of dΩ at λ = 1/16 returns **0 identically in (α, β, r, v)** for all four candidates.
- **Controls**
  - λ = 0 gives dΩ = (−0.1015, +0.1631) at (1.1, 0.7), and λ = 1/8 gives (+0.1015, −0.1631). Both are nonzero.
  - In the Einstein runs, λ = 0 gives max|E| = 2.2e6 and λ = 14/16 gives 4.3e8. Both **FAIL**.
- **What this means for each normalization**
  - In our normalization (F̂ᵢ = aᵢ du∧dv/v²), λ = **1/16**. This **CONFIRMS PP fc5e0156**.
  - It is equivalent to **1/8 in CLP's F = dA (g = 2) normalization**.
  - It is equivalent to **¼ in BBBW's normalization** (A_BBBW = a/4, "dφ+4A"), so BBBW (4.5)'s ¼ is correct in its own conventions (CONDITIONAL citation, own-checked).

**Einstein equations, all 66 components of E^M_N — PROVED at sampled points; global CONDITIONAL**

| case | max over grid of max\|E^M_N\| | verdict |
|---|---|---|
| MN1 / MN2 / z=2 / z=3, λ = 1/16 | 1.36e-6 / 6.15e-6 / 1.38e-5 / 3.01e-5 (dps 40, raw) | see the precision analysis below |
| CONTROL X₁×1.1 (z=2; e^{f}, e^{g} recomputed consistently) | **1.66e+5** | FAILS, as required |
| CONTROL wrong flux κ = 1.1 (z=2) | **4.62e+5** | FAILS, as required |
| CONTROL λ = 14/16 (z=2) | 4.29e+8 | FAILS |
| CONTROL λ = 0 (z=2) | 2.2e+6 | FAILS |

**Per-point diagnosis** (PERPOINT_DIAG log)
- At the generic and interior points the residual is ≤ 5e-38. The raw maxima come only from the doubly near-pole corners (α ∈ {1e-6, π−1e-6}, β = π/2−1e-6), with 1e-16 to 1e-17 at singly near-pole points.

**Precision convergence** (POLE_PRECISION_CONVERGENCE log, same code, parameters to 120 digits)

| corner (α, β) | dps 40 | dps 60 | dps 90 |
|---|---|---|---|
| (1e-6, π/2−1e-6) | 1.4e-6 – 3.0e-5 | 1.7e-25 – 4.4e-25 | 1.1e-55 – 4.5e-55 |
| (1e-6, 1e-6) | 1.3e-16 – 3.6e-16 | ~1e-36 | ~1e-66 |
| (1e-3, π/2−1e-3) | ~1e-23 | ~1e-43 | ~1e-73 |

- The residual falls as 10^{−(dps−34)}. That is pure round-off from 1/ε-type cancellations, not a physical violation.
- After this precision check, every sampled point has a residual consistent with 0, for all four candidates.
- Scales: max|R^M_N| ≈ 8–56 at regular points. It reaches ~1e6 at near-pole points because of mixed components along the shrinking φ circles.

**dG₄ = 0 — PROVED at sampled points**
- The central finite difference (h = 1e-12, dps 40, every 4th grid point) gives max|dG₄| = 4.8e-26 / 2.0e-25 / 3.9e-25 / 5.7e-25, against max|G| components of 0.0625 / 0.125 / 0.1875 / 0.25.
- That is at the FD truncation floor O(h²).

**Upgrade.** "MN1, MN2, BBBW z=2, z=3 at the V2 fixed points solve 11D sugra":
- the Maxwell equation and G∧G are **PROVED identically**, by exact symbolic computation;
- Einstein and Bianchi are **PROVED at the 17 sampled points per candidate**, with pole-corner round-off resolved by dps convergence;
- the statement **for all points stays CONDITIONAL** on the literature (BBBW/CLP consistent truncation) plus interpolation.
- **Resolution path for the global claim:** symbolic simplification of E_MN (66 components) to 0 at λ = 1/16, using the same NumGeom symbolic Ricci. Honest ETA: about 1–2 h of compute and debugging. Not done in this cap.

## 4. Labels summary
| item | label |
|---|---|
| Validations (AdS₇×S⁴, (D) product; wrong-flux control fails) | PROVED |
| Riemann / Ric² / Weyl² / curvature-operator maxima on the grid; PP §7a confirmed | PROVED at sampled points; global max CONDITIONAL |
| R⁴ size ~1e-8 to 1e-6 (sec.) or ≲4e-5 (√K) | CONDITIONAL (R⁴ scaling) |
| Bolza 2acosh(1+√2) = 3.0571 as the genus-2 maximum | CONDITIONAL (Jenni 1984; arXiv:2302.02540) |
| sys_phys ranges and min-systole thresholds (arithmetic) | PROVED; the criterion is CONDITIONAL |
| Actual Σ systole, λ₁(Σ) (Γ unfixed) | OPEN |
| λ = 1/16 (ours) = 1/8 (CLP) = ¼ (BBBW) | PROVED |
| d*G₄ + ½G∧G = 0 | PROVED (identically) |
| Einstein all components; dG₄ = 0 | PROVED at sampled points; global CONDITIONAL |
| Controls X₁×1.1, wrong flux, λ = 0, λ = 14/16 | all FAIL as required (PROVED) |
| Junction | OPEN |
| Adoption | none; nothing adopted |
