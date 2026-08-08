# RH Step A — M1.2 Numerical Majorant Arithmetic (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** O-M1.2 as a finished theorem for all heights · O-TL · RH  
**Architecture:** `RH_M1_2_Effective_Density.md` (accepted)  
**Constants:** Chourasiya–Simonič recorded in `RH_Deep_Pursuit_2026-07-31.md`  
**Script:** `scripts/rh_stepA_m12_gamma1_arithmetic.py` → `rh_stepA_stepB_results.json`

---

## What was computed

1. Closed-form M12 far-zero sum under R-vM local density:
   - #zeros in height H ≪ H log γ
   - annulus sum ⇒ far_sum ≍ C_U (J+1) log γ / log X with J ≍ log(γ/r)
2. GHK hybrid error majorant with programme c1 ≤ 291, c2 ≤ 8 for f_★:
   - E_GHK ≍ c1 X⁴ / (γ log X)² + c2 X^{−1/2} log X
3. Joint scan over X-strategies at H_RH = 3·10¹²:
   - polylog X = (log γ)^{A_X}
   - exp-log-power X = exp(c (log γ)^a)
   - power X = γ^δ

---

## Headline arithmetic result

- Required log X for far_sum ≤ 0.4 at γ = 3e12: **7224.44**
- E_GHK at that X: **inf** (term X⁴ explodes)
- Joint successes (far_ok ∧ ghk_ok) among scanned strategies: **0**
- far_only / ghk_only: 0 / 0

**Tension (frozen):** far-sum wants large log X; GHK wants small X relative to γ. Under current c1 = 291 the joint window at H_RH is **empty** across the scanned families.

### Top tradeoffs (score = max(far/0.4, E_GHK/0.1))

| type | params | log X | far_sum | E_GHK | far_ok | ghk_ok |
|------|--------|------:|--------:|------:|:------:|:------:|
| polylog_X | 4 | 13.4 | 215 | 0.168792359573312 | False | False |
| power_X | 0.2 | 5.75 | 503 | 2.598591069168597 | False | False |
| power_X | 0.15 | 4.31 | 671 | 3.996936386687618 | False | False |
| exp_log_power | 0.3333333333333333 | 3.06 | 944 | 5.298276649186837 | False | False |
| power_X | 0.1 | 2.87 | 1.01e+03 | 5.464670851411726 | False | False |
| exp_log_power | 0.5 | 2.68 | 1.08e+03 | 5.6139700246868065 | False | False |

---

## Status of O-M1.2 after Step A

| Layer | Status |
|-------|--------|
| Symbolic majorants c1,c2 | Done |
| Density → far-zero architecture | Done (accepted) |
| Concrete density constants | Done (CS 2025) |
| Joint numerical γ1 under c1=291 | **Not closed** — obstruction recorded |
| Phase / O-TL | Open |

**Honest next levers (still pure Cat A):**
1. Tighten c1 via better GHK weight / U decay (weight optimisation track already started in corpus).
2. Use a weaker remainder target than 1/2 if path design only needs o(log log X).
3. Restrict to heights where stronger zero-density or zero-spacing inputs are available.

---

## Explicit non-claims

- No claim that M1.2 is numerically finished.
- No O-TL, no RH.
- No model constants in the majorants.

**Status code:** `RH_STEP_A_M12_ARITHMETIC_OBSTRUCTION_2026-08-08`

*Per aspera ad astra.*
