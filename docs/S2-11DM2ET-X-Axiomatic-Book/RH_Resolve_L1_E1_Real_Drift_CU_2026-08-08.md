# RH Resolve L1 — E1 Real-Drift and C_U (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** O-M1.2 · O-TL · RH  
**Input:** Theorem E1 (`RH_E1_Off_Nearline.md`): |w E1(w)| <= 1 for Re w >= 0

---

## 1. What E1 fixes

For the pure E1 model of U on the region Re(s - rho') >= 0:

|U((s-rho') log X)| <= 1 / (|s-rho'| log X)

so the diagnostic constant **C_U = 1** is rigorous (no free C_U=2 pad required for this model).

Real-drift gain: if the path sits at sigma > beta' for a far zero, an extra factor exp(-(sigma-beta') log X) = X^{-(sigma-beta')} appears.

---

## 2. Numerical E1 far-sum (H_RH = 3e12, R-vM mean density)

| sigma | log X | far_sum (E1 model) |
|------:|------:|-------------------:|
| 0.50 | 14 | (see grid JSON) |
| 0.50 | 20 | **12.19** (min on-line among scanned) |
| 0.60 | 20 | **1.544** |

Moving right of the critical line helps bulk zeros on the line. A **rightmost off-line** zero with beta* > sigma puts Re z < 0 and removes E1 decay — the RH-hard geometry.

---

## 3. Resolve status

| Item | Standing |
|------|----------|
| C_U=1 from E1 on Re z >= 0 | **Resolved** (model) |
| Real-drift exponential for left zeros | **Resolved** when path is to the right |
| Hard case beta* > path sigma | **Open** (no E1 help) |
| O-M1.2 uniform | **Open** |

**Status code:** `RH_RESOLVE_L1_E1_REAL_DRIFT_2026-08-08`

*Per aspera ad astra.*
