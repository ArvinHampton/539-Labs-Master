# Pursue That Which Is Open (2026-08-08)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure A · ZLA · no model constants  
**Mandate:** Pursue all ten open resolution gates  
**Does not prove:** RH · O-TL · B_θ · Form C · κ p>1 · Iso_H · DH · GO · SOC strong · AFE-Moll

**Results:** `rh_pursue_open_gates_results.json`  
**Priors:** ZEFB theory · pursue-all · gap analysis · MA8 dual

---

## Scoreboard (this round)

| Gate | Before | After | Advance |
|------|--------|-------|---------|
| Form C | OPEN | **OPEN** | Zero-aware sketch; needs Iso_H or new tech |
| κ p>1 | OPEN | **OPEN** | Path split away/approach; `Kappa_away` template |
| Iso_H | OPEN | **OPEN** | Ceiling reconfirmed; no new tech |
| DH | OPEN | **OPEN** | No moderate-σ polylog |
| GO | OPEN | **OPEN** | Necessity for κ approach arcs reaffirmed |
| SOC strong+off | OPEN | **OPEN** | Typical still only closed partial |
| AFE-Moll | OPEN | **OPEN** | Objective = Euler phase, not zero-count |
| B_θ | OPEN | **OPEN** | No OR-input closed |
| O-TL | OPEN | **OPEN** | No AND-arm closed |
| RH | OPEN | **OPEN** | Superordinate |

**Newly closed this round: 0**  
**Unconditional resolutions: 0**

---

## Gate-by-gate pursuit

### 1. Form C

**Zero-aware sketch:** residual form (Thm 4.1) + control \(\varepsilon_{\mathrm{other}}\) + local Hadamard factor at \(\rho_\star\).  
Self \(\log\log\) already cancelled; remainder is global.  
Under **Iso_H**, same-abscissa \(\varepsilon_{\mathrm{other}}\) controlled (template EO(Iso_H)).  
Unconditional Form C still fenced by **FFML + ZEFB**.

**Closed?** No.

### 2. κ (p>1)

**Segmented path analysis (MA8 dual):**
```text
path = away-from-zeros  ∪  approach arcs
         │                      │
    classical |ζ′/ζ|         needs dist(s,zeros)
    may bound far U          = GO input
```
Named partial template: **Kappa_away** (away segments only — not full M1.2).  
Full-path κ with \(p>1\): **open**.

### 3. Iso_H

Tools rechecked: finite height, FE, density (dead), half-isolation, Hyp F, Ivić.  
**No new isolation technology.**

### 4. DH

Ingham-shape \(T\)-powers remain positive at moderate \(\sigma\).  
Polylog only near \(\sigma=1\) edge.  
Implication (RM)+DH⇒B_θ intact and conditional.

### 5. GO

Joint (hybrid Ω ∧ wide gap) still missing.  
Structural role upgraded: **required input** for κ approach arcs (MA8).

### 6. SOC strong + off-line

| Piece | Status |
|-------|--------|
| Typical \(\sqrt{\log\log}\) | **CLOSED** (prior) |
| Strong \(\log\log\) | **OPEN** |
| Off-line transfer | **OPEN** (path + M1.2) |

### 7. AFE-Moll

Design sharpened: a mollifier \(M\) contributes \(\arg M+\arg\zeta\); boosting \(\theta_X=\operatorname{Im}\log P_X\) needs correlation with **partial Euler phase**, not full-\(\zeta\) zero detection.  
Construction still **empty**. Levinson remains forbidden.

### 8–10. B_θ, O-TL, RH

```text
B_θ  ◄── OR(Form_C, Iso_H, DH)     all inputs OPEN
O-TL ◄── AND(κ, GO, SOC, AFE-Moll) all arms OPEN
RH   ◄── O-TL                      OPEN
```

---

## Partial advances worth keeping

1. **Kappa_away** — conditional control on zero-free path segments via MA8 + classical \(|\zeta'/\zeta|\).  
2. **Zero-aware Form C sketch** — routes through Iso_H for \(\varepsilon_{\mathrm{other}}\); no free/generic Diophantine.  
3. **AFE-Moll objective** — Euler-phase correlation, not zero-count.  
4. **GO ↔ κ** — approach arcs make GO a structural necessity for full-path κ.

---

## What not to do next

- Almost-all-\(\gamma\) Diophantine as Form C (ZEFB)  
- Free-\(t\) resonance as Form C (FFML)  
- Absolute far / c1 cosmetics as κ  
- Levinson as O-Moll  
- Residual algebra as RH (ZLA)  
- Re-derive closed identities  

---

## One-liner

> All ten open gates pursued; none closed; partial templates `Kappa_away` and zero-aware Form C sketch recorded; OR-cut and AND-cut remain fully open; RH/O-TL open.

**Status code:** `RH_PURSUE_OPEN_GATES_2026-08-08`

*Per aspera ad astra.*
