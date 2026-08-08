# RH Step B — Classical Density Gap Table at Moderate σ (2026-08-08)
**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** Iso_H · Mass-with-A · B_θ · O-TL · RH  
**Source:** Chourasiya–Simonič arXiv:2507.15184 (CS) / classical Ingham shape; Guth–Maynard comparison.
**Companion results:** `rh_stepA_stepB_results.json`, `scripts/rh_stepA_m12_gamma1_arithmetic.py`.

---

## Goal

Record, for each moderate abscissa β⋆, the best classical leading power of T in N(β⋆,T) and the gap to a polylog count O((log T)^C).

---

## Gap table

| β⋆ | θ_CS/Ingham = 3(1−β)/(2−β) | θ_GM = A(β)(1−β), A=15/(5β+3) | CS B1 | Zone | Polylog N_vert? |
|----|---------------------------:|------------------------------:|------:|------|-----------------|
| 0.55 | 0.9310 | 1.1739 | 8.604 | CS low [0.50,0.625] | **No** |
| 0.60 | 0.8571 | 1.0000 | 8.604 | CS low [0.50,0.625] | **No** |
| 0.65 | 0.7778 | 0.8400 | 22.44 | CS mid [0.625,0.875] | **No** |
| 0.70 | 0.6923 | 0.6923 | 22.44 | CS mid [0.625,0.875] | **No** |
| 0.75 | 0.6000 | 0.5556 | 22.44 | CS mid [0.625,0.875] | **No** |
| 0.80 | 0.5000 | 0.4286 | 22.44 | CS mid [0.625,0.875] | **No** |
| 0.85 | 0.3913 | 0.3103 | 22.44 | CS mid [0.625,0.875] | **No** |
| 0.90 | 0.2727 | 0.2000 | — | beyond CS; Bellotti-type near 1 | **No** |
| 0.95 | 0.1429 | 0.0968 | — | beyond CS; Bellotti-type near 1 | **No** |
| 0.98 | 0.0588 | 0.0380 | — | beyond CS; Bellotti-type near 1 | **No** |

**Reading.** Every tabulated β⋆ ≤ 0.98 retains a **positive** power of T under CS/Ingham. Guth–Maynard improves some mid-range exponents but does not reach polylog. Near σ → 1 the exponent → 0 (Bellotti-type territory); that is not moderate σ.

---

## Implication for Solid Direction 1

```
N_vert ≤ M(T)  ⇒  A ≪ M log T
polylog M      ⇒  polylog A  ⇒  Mass-with-A  ⇒  B_θ   [implication only under (RM)]
```

At moderate σ the classical M(T) is still a positive power of T. **Step B barrier stands:** polylog StripDens / polylog N_vert at moderate σ remains open.

---

## Explicit non-claims

- No Iso_H from density.
- No Mass-with-A unconditional.
- No RH.

**Status code:** `RH_STEP_B_DENSITY_GAP_TABLE_2026-08-08`

*Per aspera ad astra.*
