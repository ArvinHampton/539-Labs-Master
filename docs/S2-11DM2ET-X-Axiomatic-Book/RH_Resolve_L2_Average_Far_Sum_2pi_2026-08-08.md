# RH Resolve L2 — Average / R-vM Far-Sum with 2-pi (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** O-M1.2 · O-TL · RH

---

## 1. Corrected mean-density formula

Mean zero density on the critical line: (log gamma) / (2 pi) per unit height.

Annulus bookkeeping with |U| <= C_U / (|s-rho'| log X) yields

far ~ C_U (J+1) log(gamma) / (pi log X)

with J ~ log2(gamma/r). Average-case equals this mean — there is **no extra free factor** from "averaging" beyond R-vM.

E1 sets C_U = 1 (L1).

---

## 2. Improvement vs prior diagnostic

At log X = 14, H_RH:

| Formula | far_sum |
|---------|--------:|
| Old (C_U=2, dens ~ log gamma, no 2pi) | **206.4** |
| New (C_U=1, 2pi) annulus | **32.85** |
| New integral form | **22.32** |
| Improvement factor | **6.283** (~ pi * 2) |

---

## 3. Joint window after improvement

| c1 | eps | min far in GHK window |
|---:|----:|----------------------:|
| 291 | 0.1 | no window (prior) |
| 291 | 0.5 | ~ 32.85155882357489 |
| 1 | 0.1 | **31.08** at logX=14.8 |

**Both-hits for far <= 0.4 and E <= 0.1 at c1=1:** **none** in the scanned grid.

Net: ~6x better far-sum, still O(10) not O(0.1) under GHK-feasible X.

---

## 4. Resolve status

| Item | Standing |
|------|----------|
| 2pi density in far-sum | **Resolved** (formula correction) |
| Average-case = R-vM mean | **Resolved** (no free lunch) |
| Joint far<=0.4 + GHK<=0.1 under c1<=291 | **Still closed** (obstruction) |
| O-M1.2 | **Open** |

**Status code:** `RH_RESOLVE_L2_AVERAGE_FAR_2PI_2026-08-08`

*Per aspera ad astra.*
