# RH N1 — Non-Absolute Far-Sum: Radius vs J and Signed Cancellation (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** O-M1.2 · kappa theorem · O-TL · RH  
**Vessel:** `RH_Signed_Sum_Attack.md` (Sigma_X residual; lower bound open)  
**Results:** `rh_execute_next5_results.json`

---

## 1. Absolute baseline (E1 + 2-pi R-vM)

far = C_U (J+1) log(gamma) / (pi log X), C_U = 1 from Theorem E1.

Under GHK-feasible X (E <= 0.1 at c1 = 1), absolute far remains O(10^1), never <= 0.4.

---

## 2. Path radius vs J

r = c_r / log gamma. Larger c_r reduces J and absolute far, but:

| c_r | mean_gap / r = 2 pi / c_r | Isolation viable? |
|----:|--------------------------:|-------------------|
| 0.25 | ~25 | Yes (many gaps fit) |
| 1.0 | ~6.3 | Marginal |
| 5.0 | ~1.3 | Poor |
| 10 | ~0.63 | **No** — r exceeds mean gap |

**Resolve:** radius enlargement is not a free lunch; c_r >> 1 breaks local isolation.

---

## 3. Cancellation models vs joint window (c1 = 1, E <= 0.1, far_signed <= 0.4)

Define far_signed = kappa * far_abs.

| Model | kappa | Opens joint (c1=1)? | Opens (c1=291)? |
|-------|-------|---------------------|-----------------|
| Absolute | 1 | No | No |
| Mild 1/log J | 1/log J | No | No |
| Random walk 1/sqrt(J) | J^{-1/2} | **No** (0/105 cells) | No |
| Strong 1/J | J^{-1} | **No** (0/105) | No |
| Square 1/J^2 | J^{-2} | **Yes** (105/105) | No |
| 1/J^3 | J^{-3} | Yes | No |

Best cell under c1=1: c_r=10.0, logX=14.80, far_abs=27.79,  
**kappa_need = 0.0144** (need kappa <= this).  
Random-walk kappa ~ 0.1508 — **not enough**. Strong 1/J ~ 0.02274 — **not enough**.  
Square 1/J^2 ~ 0.0005172 — enough.

**c1=291:** no model in the scan opens E<=0.1 and far<=0.4 simultaneously (GHK window empty or far still large).

---

## 4. Frozen conclusion

> Only **strong coherent signed cancellation** at the ~1/J^2 level (far stronger than random-walk) can open numerical M1.2 under real executable c1.  
> The classical vessel is the signed-sum residual Sigma_X. A proved kappa bound is **open**.  
> Absolute majorants and mild cancellation are dead ends for the joint window.

**Status code:** `RH_N1_NONABSOLUTE_FAR_SUM_2026-08-08`

*Per aspera ad astra.*
