# G_pred Rank-1 Grid — Eliminate G as Input (Pre-Registered)

**Date lock:** 2026-07-31  
**Protocol:** Invert torsion/clock eigenvalue for the coupling; particle scales + locked integers only; **no \(\ell_{\mathrm{Pl}}\)** on the predicting side  
**Success criterion:** unique or sharply discrete \(G_{\mathrm{pred}}\) within 1% of CODATA from the **pre-registered** set  
**Residual firewall:** Architecture A0–A5⁺, Option 3, No-Go, packaging under (S) **unchanged** — residual does not output \(G\)

---

## 1. Pre-registered predicting formulas (no \(G\), no \(\ell_{\mathrm{Pl}}\))

### Shared inputs (not containing \(G\))

| Symbol | Value | Role |
|--------|--------|------|
| \(c\) | CODATA | SI |
| \(\hbar\) | CODATA | SI |
| \(m_p\) | CODATA | particle mass |
| \(\lambda_p=\hbar/(m_p c)\) | \(2.103\times 10^{-16}\,\mathrm{m}\) | particle length |
| \(\Gamma_\beta=1/\tau_n\) | \(\tau_n=879.4\,\mathrm{s}\) | weak rate |
| \(G_4\) | \(539.90\,\mathrm{s}\) | model clock period |
| \(\omega=2\pi/G_4\) | | angular frequency |
| Locked integers | 3, 11, 14, 18, 61, 118, 243, 521, 539, 4880, … | residual/packaging skeleton |

**Comparison only (never on RHS):** \(G_{\mathrm{CODATA}}=6.67430\times 10^{-11}\)

### Law families

**A.** Continuum-style invert with \(G_7=\pi c^4/(2 G_4^2\langle J\rangle)\), \(\langle J\rangle=(w/\lambda_p^3)\Gamma_\beta\langle N{-}2Z\rangle\), \(G=G_7/(N\lambda_p)^7\)  
*(Note: continuum \(/c^4\) + rate density has unit tension; retained as pre-registered literal.)*

**B.** Same as A with \(V_7=\lambda_p^7 N_{\mathrm{flux}}^p\|P\|^q 3^r\), \((p,q,r)\) small integers.

**C (unit-consistent 4D).**  
\[
G_{\mathrm{pred}}
=
\frac{\omega^2}{\kappa\,\rho_{\mathrm{eff}}},
\qquad
\rho_{\mathrm{eff}}
=
\frac{m_p}{\lambda_p^3}\,w\,\langle N{-}2Z\rangle\,\xi,
\qquad
\kappa\in\{4\pi,8\pi\}
\]

**D (unit-consistent 7D).**  
\(G_7=\omega^2/(4\pi\rho_{\mathrm{eff}})\), \(G=G_7/(N\lambda_p)^7\).

Pre-registered \(w\), \(N\), \(\langle N{-}2Z\rangle\), \(\xi\): finite locked rationals only (see JSON).

---

## 2. Grid sizes

| Grid | Evaluations |
|------|-------------|
| A | 2 700 |
| B | 3 888 |
| C | 2 160 |
| D | 21 600 |
| **Total** | **30 348** |

---

## 3. Hits vs CODATA (pre-registered only)

| Tolerance | A | B | C | D |
|-----------|---|---|---|---|
| 50% | 0 | 0 | 0 | 0 |
| 10% | 0 | 0 | 0 | 0 |
| 1% | 0 | 0 | 0 | 0 |
| within \(10^{\pm 2}\) | 0 | 0 | 0 | 0 |
| within \(10^{\pm 6}\) | 0 | 0 | 0 | 0 |

### Best of each grid (still failures)

| Grid | Best \(\log_{10}(G_{\mathrm{pred}}/G_{\mathrm{CODATA}})\) | ratio |
|------|------------------------------------------------------|-------|
| A | \(+74.8\) | \(\sim 10^{75}\) too large |
| B | \(+88.4\) | \(\sim 10^{88}\) too large |
| **C** | **\(-7.01\)** | **\(\sim 10^{-7}\) too small** (closest) |
| D | \(+65.1\) | \(\sim 10^{65}\) too large |

---

## 4. Verdict (pre-registered protocol)

\[
\boxed{\texttt{NEGATIVE\_NO\_PRE\_REGISTERED\_HIT\_WITHIN\_2\_ORDERS}}
\]

**\(G\) is not eliminated as an input by the pre-registered Rank-1 integer skeleton under laws A–D.**

No unique or discrete \(G_{\mathrm{pred}}\) comparable to CODATA was obtained. Residual firewall intact: residual algebra constrained the integer set; it did not and does not produce \(G\).

---

## 5. Inverse diagnostic (not a success claim)

Under unit-consistent **Law C** (\(\kappa=4\pi\)):

\[
\rho_{\mathrm{req}}
=
\frac{\omega^2}{4\pi G_{\mathrm{CODATA}}}
\approx
1.61\times 10^{5}\,\mathrm{kg\,m^{-3}}
\]

\[
(w\cdot\langle N{-}2Z\rangle\cdot\xi)_{\mathrm{req}}
=
\frac{\rho_{\mathrm{req}}}{m_p/\lambda_p^3}
\approx
8.98\times 10^{-16}
\]

So the 4D clock law needs a **dimensionless dilution** \(\sim 10^{-15}\) relative to nuclear density \(m_p/\lambda_p^3\).

### Post-look integer products near that dilution (diagnostic only)

These were **not** in the pre-registered \(w,\xi\) sets. Reporting them does **not** upgrade the verdict.

| Expression | Value | \(\times\) vs required |
|------------|-------|-------------------------|
| \(1/N_{\mathrm{flux}}^4=1/4880^4\) | \(1.76\times 10^{-15}\) | \(1.96\) |
| \((1/4880^4)(118/539)\) | \(3.86\times 10^{-16}\) | \(0.43\) |
| \(1/539^6\) | \(4.08\times 10^{-17}\) | \(0.045\) |

If one **illegally** inserts \(w=1/4880^4\) into Law C after seeing \(\rho_{\mathrm{req}}\):

\[
G_{\mathrm{pred}}\approx 3.40\times 10^{-11}
\quad\Rightarrow\quad
G_{\mathrm{pred}}/G_{\mathrm{CODATA}}\approx 0.51
\]

That is a **post-hoc near miss (~factor 2)**, not a protocol hit. A second campaign may **pre-register** \(\{N_{\mathrm{flux}}^{-4}, N_{\mathrm{flux}}^{-4}\cdot 118/539,\ldots\}\) *before* any CODATA comparison and re-run under the same rules. Until then it is not frozen as elimination of \(G\).

### Inverse \(N_{\mathrm{geom}}\) (laws A/D)

Required \(N\sim 10^{13}\)–\(10^{15}\) vs largest locked \(N=14640\). No locked compactification integer is close (relative error \(\approx 1\)).

---

## 6. Structural conclusions

1. **Literal continuum invert (A/B) with proton volume and rate density overshoots \(G\) by \(\sim 10^{75+}\)** — wrong unit structure and/or wrong identification of \(\langle J\rangle\).
2. **Unit-consistent 7D reduction (D) still overshoots by \(\sim 10^{65}\)** — \((N\lambda_p)^7\) with locked \(N\le O(10^4)\) cannot supply the needed suppression.
3. **Unit-consistent 4D law (C) undershoots by \(\sim 10^{7}\)** with pre-registered dilutions — nearest systematic approach; needs \(\sim 10^{-15}\) weight, which locked **linear** packaging ratios do not provide.
4. **Residual integers as linear/rational weights are too coarse** at the nuclear-density scale; eliminating \(G\) requires either  
   - a **pre-registered higher composite** (e.g. flux fourth power) with independent geometric justification, or  
   - a **different particle scale / screening identity** fixed without CODATA tuning, or  
   - acceptance that \(G\) remains an external input (honest Cat B).
5. **Using \(\ell_{\mathrm{Pl}}\) remains forbidden** on the predicting side; it cannot be used to “fix” the gap without re-importing \(G\).

---

## 7. Status codes

| Code | Meaning |
|------|---------|
| `G_PRED_RANK1_NEGATIVE_2026-07-31` | Pre-registered grids A–D: no hit |
| `G_NOT_ELIMINATED_AS_INPUT` | Goal not met |
| `LAW_C_NEAREST_7_ORDERS_LOW` | Best pre-reg approach |
| `POSTHOC_FLUX4_FACTOR_TWO_NOT_A_HIT` | Diagnostic only |
| `RESIDUAL_FIREWALL_INTACT` | Cat A unchanged |

---

## 8. Allowed next steps (if continued)

1. **Pre-register** a finite list of higher composites *with geometric narrative fixed first* (e.g. why \(N_{\mathrm{flux}}^4\) is a 4-volume flux factor), then freeze and re-run Law C only.  
2. Replace nuclear density by a **pre-registered** multi-scale density (e.g. cosmological mean baryon density built from \(H_0\) would reintroduce non-model inputs — usually worse).  
3. Repair absolute \(E_{\mathrm{leak}}\) normalization and attempt Rank-3 energy matching — only after numerics are non-free.  
4. **Stop and keep \(G\) as input** in continuum equations; document that residual + present particle bridge does not determine \(G\).

Recommended default after this negative: **(4)** for honesty, with optional **(1)** as a single controlled second campaign.

---

## 9. Artifacts

- `G_pred_rank1_grid_results.json` — full top rows and summary  
- This report

*Per aspera ad astra.*
