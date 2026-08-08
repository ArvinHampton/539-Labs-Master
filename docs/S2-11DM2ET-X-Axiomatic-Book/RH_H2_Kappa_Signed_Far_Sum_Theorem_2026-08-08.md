# RH H2 — κ ∼ J^{-p} Signed Far-Sum Theorem (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** κ theorem · O-M1.2 · RH  
**Links:** N1 non-absolute far-sum · E1 · L2 2π formula

---

## 1. Definition

\[
\mathrm{far}_{\mathrm{abs}}
=
C_U\frac{(J+1)\log\gamma}{\pi\log X},
\qquad C_U=1\ (\mathrm{E1}),
\qquad
\mathrm{far}_{\mathrm{signed}}
\le
\kappa\cdot\mathrm{far}_{\mathrm{abs}}.
\]

**Target:** far_signed ≤ 0.4 with E_GHK ≤ 0.1 under real c1.

---

## 2. Quantitative need (H_RH = 3×10¹²)

Easiest cell with c1=1 GHK window:

| Quantity | Value |
|----------|------:|
| c_r | 5.0 |
| log X | 14.80 |
| J | 44.97 |
| far_abs | 28.41 |
| **κ_need** | **0.01408** |
| **J-power need p** | **1.120** (need κ ≤ J^{-p}) |
| random walk J^{-1/2} | 0.1491 — **not enough** |
| strong J^{-1} | 0.02224 — **not enough** |
| square J^{-2} | 0.0004945 — enough (overkill at this cell) |

**c1=291:** no joint GHK window (E≤0.1) in the scan — κ cannot help until c1 is reduced or X-window opens.

Note: c_r=5 makes r comparable to mean gap (isolation marginal). Safer c_r=0.25 needs **larger p** (closer to 2).

---

## 3. Theorem status

| Claim | Status |
|-------|--------|
| κ=1 (absolute) | **Proved** (triangle inequality) |
| κ ≤ J^{-1/2} (random walk) | **Not proved** (and insufficient if true) |
| κ ≤ J^{-p} for p≥1.12 | **Not proved** |
| Vessel | Hybrid far U-sum / signed Σ structure |

---

## 4. Resolution today

**False.** Model shows p≳1.12 (safer p∼2) is the numerical bar; no κ theorem.

**Status code:** `RH_H2_KAPPA_SIGNED_FAR_SUM_2026-08-08`

*Per aspera ad astra.*
