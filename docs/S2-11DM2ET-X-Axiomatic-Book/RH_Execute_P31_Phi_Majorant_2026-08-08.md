# RH Execute P3.1 — Path-Continuation Majorant Phi (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** O-M1.3bis · path continuation · O-TL · RH  
**Direction:** Solid Direction 3  
**Results JSON:** `rh_execute_all_c1_P3_R4_results.json`

---

## 1. Object

Along a path from 1/2+it_* toward sigma_*+it_*:

partial_sigma Delta_X = Re(zeta'/zeta - P_X'/P_X)   (up to hybrid bookkeeping)

**Target majorant:** |partial_sigma Delta_X| <= Phi(sigma, t, X)

**Continuation criterion:** integral_{1/2}^{sigma*} Phi d sigma < |Delta_X(1/2+it_*)| / 2

---

## 2. Analytic split of Phi (recorded)

| Piece | Majorant |
|-------|----------|
| Phi_P | sum_{n<=X} Lambda(n) n^{-sigma} << X^{1-sigma}/(1-sigma) for sigma<1 |
| Phi_zeros far | dyadic R-vM: << (log t) * log(t/r) |
| Phi_local | m / dist(s, nearest zero) — path geometry |
| Phi_arch | O(log(|t|+2)) |
| Phi_GHK | derivative of hybrid error (secondary) |

---

## 3. Numerical sketch (absolute crude Phi)

Fixed illustration: t = 10^6, X = e^{10} ~ 2.2e4, r0 = 1/log t.

On-line reservoir model: sqrt(X) / log X ~ **14.84**

| Integral of crude Phi | Value | < 1/2 reservoir? |
|-----------------------|------:|:-----------------|
| to sigma=0.60 | 56.37 | False |
| to sigma=0.70 | 101.7 | False |
| to sigma=0.80 | 142.3 | False |
| to sigma=0.90 | 181 | False |

**Reading:** absolute crude Phi (especially the 1/r0 local spike) makes integral Phi exceed the on-line reservoir. This is an obstruction for **naive absolute** majorants, not a no-go for average-case or zero-free-tube paths.

---

## 4. Status of P3.1

| Item | Status |
|------|--------|
| Phi structure split | **Recorded** |
| Crude numerical integral vs reservoir | **Executed** — absolute path loses |
| Zero-free tube / average-case Phi | **Open** (P3.2 direction) |
| O-M1.3bis | **Open** |

**Status code:** `RH_EXECUTE_P31_PHI_MAJORANT_2026-08-08`

*Per aspera ad astra.*
