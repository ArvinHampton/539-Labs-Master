# RH Execute A — c1 / U Tightening Levers (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** O-M1.2 · O-TL · RH  
**Companions:** `RH_M1_2_Optimized_ci_Bounds.md`, `RH_StepA_M12_Numerical_Arithmetic_2026-08-08.md`  
**Results:** `rh_execute_all_c1_P3_R4_results.json` · `scripts/rh_execute_all_c1_P3_R4.py`

---

## 1. Baseline and lever catalogue

| Package | c1 | c2 | Notes |
|---------|---:|---:|-------|
| Optimized f_star (prior) | <= 291 | <= 8 | A2~0.169, D2~5.02, M2~85.7, C_mul=2 |
| Raw A2 (no 10% safety) | ~265 | 8 | grid max, not safety-padded |
| D2 pole-only 4.5 | ~261 | 8 | drops trivial-zero pad |
| C_mul=1.25 (shrunk err region) | ~182 | 5 | needs tighter err region |
| Stacked best-executed-style | ~**148** | ~5 | caveats stacked; still not certified |

Formula unchanged: c1 = 2 C_mul D2 A2 M2.

---

## 2. Structural joint-window arithmetic at H_RH = 3e12

Far-sum model (R-vM local density): far ~ C_U (J+1) log gamma / log X with J ~ log2(gamma/r).

GHK: E <= c1 X^4/(gamma^2 (log X)^2) + c2 X^{-sigma} log X.

### Minimum E_GHK over X (sigma = 1/2, c2 = 8)

| c1 | min E | at log X ~ |
|---:|------:|-----------:|
| 291 | **0.159** | 13.2 |
| 148 | 0.149 | 13.4 |
| 50 | 0.134 | 13.6 |
| 10 | 0.114 | 14.0 |
| 1 | **0.091** | 14.6 |
| 0.1 | 0.072 | 15.1 |

**Headline:** under c1 = 291, **no X achieves E_GHK <= 0.1**. A GHK<=0.1 window opens only for c1 <= 1 (far below any executed majorant).

### Min far_sum in windows where E <= eps

| c1 | eps | min far (C_U=2) |
|---:|----:|----------------:|
| 291 | 0.1 | **no window** |
| 291 | 0.5 | ~ 206 |
| 1 | 0.1 | ~ 195 |
| 1e-6 | 0.1 | ~ 155 |

To push far <= 0.4 at the best c1=1 / eps=0.1 point requires **C_U <= 0.004** (about 500x better U-decay / path geometry than C_U=2).

---

## 3. Frozen conclusion

> **c1 factor tuning alone cannot open a joint M1.2 numerical window at far<=0.4 under R-vM.**  
> Even unrealistically small c1 only lowers min far into the ~150-200 range with C_U=2.  
> Closing far<=0.4 needs a structural improvement of the far-zero majorant (smaller C_U via better U decay, larger isolation radius, or average-case cancellation) — not just A2/D2 cosmetics.

---

## 4. Legitimate next levers (still Cat A)

1. **U-decay / C_U:** use |E1(z)| <= e^{-Re z}/|z| on paths with positive real drift; optimize path radius r vs J.
2. **Average-case far sum** instead of absolute annulus majorants.
3. **Weaker remainder targets** (e.g. o(log log X) instead of 1/2) matched to O-TL scale.
4. Interval-certified A2 (open) — will not move c1 by the required orders of magnitude.

---

## Explicit non-claims

- No completed numerical gamma1 theorem.
- No O-TL / RH.
- Stacked c1~148 is **not** interval-certified.

**Status code:** `RH_EXECUTE_A_C1_U_STRUCTURAL_OBSTRUCTION_2026-08-08`

*Per aspera ad astra.*
