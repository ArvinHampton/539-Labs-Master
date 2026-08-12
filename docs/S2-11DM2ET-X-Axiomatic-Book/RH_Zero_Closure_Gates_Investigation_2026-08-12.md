# RH Zero-Closure Gates — Investigation (2026-08-12)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category A analysis only. ZLA. No model constants. No RH claim.**  
**Source:** re-executed open-gates / priority-4 / ranked-hopes / rational-4 / diagnostics (execute-all passes 1–2).

---

## 0. What “zero-closure” means

After the full attack battery, **newly_closed = []**. Ten named gates remain OPEN. This note states, for each gate:

- definition / role in the debt argument  
- what is already proved or templated  
- the specific blocker  
- dependency on other gates  
- quantitative signal from the latest runs  

No gate is closed by this investigation.

---

## 1. Dependency sketch

```
                    Iso_H ──► EO(Iso_H) ──► Form_C (uncond hard)
                      │                        │
                      ▼                        ▼
        DH (polylog) ─┴──► B_θ (OR of inputs) ──► O-TL pieces
                      │
GO ◄── approach arcs of M1.3 path ──► kappa_p>1 ──► O-TL (AND)
                      │
SOC_strong_offline ─── offline phase lower bound ──► O-TL
                      │
AFE_Moll ──────────── mollified Euler phase ──────► O-Moll / O-TL
                      │
Form_C ────────────── PAO / fixed-frequency large values ─► B_θ / O-TL
                      │
RH ════════════════ superordinate (all primary arms open)
```

OR-cut to B_θ needs **any** of: strong Form_C / PAO, DH+RM, Iso_H+RM.  
AND-cut to O-TL needs path package (kappa) **and** phase lower bound (SOC / Form_C class).  
RH needs O-TL (or equivalent) at the program’s chosen strength.

---

## 2. Gate-by-gate investigation

### 2.1 Form_C — Fixed-frequency multiplicative large values

**Definition.**  
Form C: \(\limsup_{X\to\infty} \big|\sum_{n\le X} \Lambda(n)\, n^{-\rho^*}/(\log n)\big| = \infty\)  
at a rightmost zero \(\rho^*=\beta^*+i\gamma^*\) (fixed frequency \(\gamma^*\)).

**Role.** Equivalent (under signed residual Thm 4.1) to Form B residual integral large values; core of PAO after star loglog cancellation.

**Proved / closed pieces.**  
- Form B ↔ Form C (equivalence closed).  
- Self loglog cancellation of pure star contribution.  
- Conditional EO(Iso_H): same-abscissa \(\varepsilon_{\mathrm{other}}\) controlled under Iso_H.

**Blocker.**  
Unconditional Form C is blocked by **FFML** (fixed-frequency multiplicative large-value barrier) + **ZEFB** for free/generic methods. After star removal, the remaining sum is a Dirichlet polynomial at **fixed** complex frequency — harder than free-\(t\) resonance. Local Hadamard factor only recovers the already-cancelled self loglog; the remainder is global.

**Quant.** Priority-4 P1: resolution_today = false. Rational-4 T1 (FFML): False.

**Standing:** OPEN. Partial: zero-aware sketch recorded.

---

### 2.2 kappa_p_gt_1 — Path far-sum decay better than absolute

**Definition.**  
A power-saving bound on the far GHK/U sum along M1.3-type paths: effective \(\kappa\) with \(p>1\) (signed/cancelled far sum \(\ll J^{-p}\) or equivalent), not merely absolute \(\kappa=1\).

**Role.** Controls the error arm of O-M1.2 / path package so that phase lower bounds can win at O-TL scale.

**Proved / templated.**  
- Absolute \(\kappa=1\) only (proved package).  
- E1 model local bound near a zero.  
- **Kappa_away** template: away-from-zeros segments may be controllable by MA8 + classical \(|\zeta'/\zeta|\) bounds (conditional/partial — not full M1.2).  
- Optimized majorants: \(c_1\le 290.959\), \(c_2\le 8\) (453× improvement over crude \(c_1\sim 1.3\cdot 10^5\)) — still too large for joint windows.

**Blocker.**  
**Approach arcs** near zeros require distance-to-zeros control = **GO** input. Absolute far sums on grids never hit far ≤ 0.4 jointly with GHK at realistic \(c_1\). L2 proxies give heuristic \(p_{\mathrm{eff}}\sim 1.07\)–1.5 but are **not** uniform path theorems.  
Execute-all: away_cells_U_le_0.4 = 0; zf_cells_U_le_0.4 = 0; joint hits by \(c_1\) all 0.

**Standing:** OPEN. Partial: Kappa_away named; approach = GO-blocked.

---

### 2.3 Iso_H — Isolation of height at rightmost abscissa

**Definition.**  
Isolation hypothesis / technology: control of other zeros at the same abscissa \(\beta^*\) (so \(\varepsilon_{\mathrm{other}}\) vanishes up to the conjugate).

**Role.** Unlocks EO(Iso_H) → cleaner Form_C / PAO; with (RM) implies B_θ (proved implication only).

**Tools rechecked (no new tech).**  
- Finite-height verification — only up to \(T_0\).  
- FE conjugate — only \(\bar\rho^*\).  
- Density theorems — **dead edge** to isolation (density vs isolation locked distinction).  
- Half-isolation / Hyp F / Ivić — local or conditional only.

**Blocker.** No known unconditional isolation method for an arbitrary rightmost zero. Density cannot promote to isolation.

**Standing:** OPEN. new_technology = false.

---

### 2.4 DH — Density hypothesis at moderate \(\beta^*\)

**Definition.**  
A density bound strong enough that vertical counts are **polylog** (or otherwise usable) at moderate \(\beta^*\in(1/2,1)\), feeding Mass-with-A / B_θ under (RM).

**Role.** Alternate OR-input to B_θ with Iso_H; Step C templates conditional Mass-with-A under DH(\(\beta^*,C\)).

**Blocker.** Classical CS/Ingham-type bounds retain **positive T-power** for \(\beta^*\in[0.55,0.98]\) (Step B density gap table frozen). Polylog \(N_{\mathrm{vert}}\) **open**.  
Ranked hope H3: at \(\sigma=0.7\), schematic Ingham T-exponent > 0 ⇒ not polylog.

**Standing:** OPEN. Implication DH⇒B_θ remains conditional.

---

### 2.5 GO — Gap / isolation geometry on approach arcs

**Definition.**  
Zero-gap / local spacing control sufficient to run approach arcs of M1.3 paths without uncontrolled near-zero contamination (input to kappa on approach).

**Role.** Structural necessity for full-path \(\kappa_{p>1}\); without GO, only away segments are candidates.

**Blocker.** Joint with other path requirements still missing. No unconditional GO at the scale needed for O-TL. Mean-gap vs isolation-radius tension: large \(c_r\) improves absolute far but isolation radius \(r=c_r/\log\gamma\) becomes large vs mean gap \(2\pi/\log\gamma\) (at \(c_r=10\), mean_gap/r ≈ 0.63).

**Standing:** OPEN. Necessity for kappa approach arcs reaffirmed.

---

### 2.6 SOC_strong_offline — Strong off-line phase lower bound

**Definition.**  
Strong oscillatory / phase lower bound off the critical line at scale \(\asymp \log\log X\) (or the program’s strong target), not merely typical \(\sqrt{\log\log X}\) on-line size.

**Role.** Phase arm of O-TL; offline transfer from on-line \(\Omega\).

**Blocker.** No strong loglog offline. Transfer still blocked by the **path package** (needs kappa-quality error control).  
L5 diagnostic: mean peak \(|A|/\log\log X\) on/off ≈ 0.325 / 0.316 — finite-range, **inconclusive**, not support for strong SOC.  
OPC diagnostic: mean \(|\theta|/\log\log \ll 1\) in sampled range — loglog scale not seen.

**Standing:** OPEN.

---

### 2.7 AFE_Moll — Phase-oriented mollifier

**Definition.**  
A genuinely phase-oriented mollifier aimed at the **Euler-product / prime phase**, not at counting zeros (O-Moll).

**Role.** O-Moll arm; possible route to phase lower bounds without full SOC.

**Proved / sharpened.**  
Design constraint sharpened: mollify Euler phase, **not** zeta zeros. Dual-sum AFE templates exist as design only.

**Blocker.** Construction still **empty** — no concrete mollifier with proved phase gain at O-TL scale. Shelf match in next5: none.

**Standing:** OPEN. Partial: objective sharpened.

---

### 2.8 B_θ — Phase / argument lower-bound gate

**Definition.**  
The B_θ-type lower bound on a phase/argument object in the debt argument (OR of admissible inputs).

**Role.** Intermediate OR-gate: any one of Form_C/PAO, DH+(RM), Iso_H+(RM) can feed it (as recorded implications).

**Blocker.** **No OR-input closed this round.** All of Form_C (uncond), DH, Iso_H remain open.

**Standing:** OPEN.

---

### 2.9 O_TL — Target lemma (primary analytic obligation)

**Definition.**  
Target lemma: \(|A_X(Y,\gamma)| \ge c\, m \log\log X_n\) (or the program’s maximal-abscissa form) — primary obligation among O-M1.2, O-M1.3bis, O-PC, O-Moll, O-TL.

**Role.** Main analytic engine toward RH in this debt architecture.

**Blocker.** **No AND-arm closed.** Needs simultaneous error control (kappa / path package) and phase lower bound (SOC / Form_C / mollifier class). Kappa segmented analysis is partial only (away template). Joint far≤0.4 windows empty for all scanned \(c_1\).

**Standing:** OPEN (primary).

---

### 2.10 RH — Superordinate gate

**Definition.**  
Riemann Hypothesis (program claim strength as in debt argument — not a residual-algebra lemma about \(\zeta\)).

**Role.** Superordinate: not attacked directly; requires O-TL (or equivalent closed architecture).

**Blocker.** All primary arms open; zero tip closures in execute-all passes.

**Standing:** OPEN.  
**Explicit:** residual discrete algebra does **not** imply RH; ZLA in force; no model constants.

---

## 3. Quantitative barrier summary (latest runs)

| Quantity | Value | Gate impact |
|----------|-------|-------------|
| newly_closed | [] | all 10 open |
| c1_upper (optimized) | ≤ 290.959 | still too large for joint GHK+far |
| best stacked c1 (caveats) | ~148.1 | joint hits still 0 |
| joint hits far≤0.4 over c1 grid | 0 | kappa / O-M1.2 |
| away_cells U≤0.4 | 0 | kappa_away not yet numerical |
| H2 easiest κ_need (c1=1, logX=14.8) | ~0.014 | needs p>1 cancellation |
| DH moderate β* | positive T-power | no polylog |
| L5 \|A\|/loglog on vs off | ~0.325 vs 0.316 | no strong offline signal |
| M1.3 mean semi Δarg P | ~0.026 | no monodromy accumulation |
| open gates count | 10 | Form_C … RH |

---

## 4. Partial advances (not closures)

1. **Form_C:** zero-aware sketch; EO(Iso_H) named conditional.  
2. **kappa:** path split away/approach; Kappa_away template; absolute majorants optimized 453×.  
3. **AFE_Moll:** objective = Euler phase, not zero-count.  
4. **GO:** structural necessity for approach arcs reaffirmed (design clarity, not a theorem).

---

## 5. Hard barriers (do not pretend otherwise)

| Barrier | Affects |
|---------|---------|
| FFML / fixed-frequency large values | Form_C, PAO |
| Density ↛ isolation | Iso_H, EO, uncond Form_C |
| Classical density positive T-power | DH, polylog Mass-with-A |
| Approach arcs need GO | kappa_p>1 full path |
| Absolute far sum too large vs GHK c1 | joint O-M1.2 windows |
| No strong offline loglog | SOC, O-TL phase arm |
| Empty phase mollifier construction | AFE_Moll, O-Moll |

---

## 6. Honest next levers (still open research)

Ordered by dependency honesty (not a promise of closure):

1. **New Iso_H technology** or accept conditional EO(Iso_H) only.  
2. **Signed/cancelled far-sum theorem** (true p>1) on away segments — then face GO on approach.  
3. **Polylog density** at some moderate β* — currently blocked classically.  
4. **Concrete AFE-Moll construction** with proved phase gain.  
5. **Do not** dilute O-TL to √(log log X) without an explicit program amendment.

---

## 7. Explicit non-claims

- No RH, O-TL, Iso_H, B_θ, PAO, kappa p>1, DH polylog, or unconditional Form_C.  
- No residual-algebra proof about \(\zeta\).  
- Diagnostics are finite-range and do not support RH.  
- Optional P⁺ / residual Category A stack is independent of these gates.

---

## 8. One-liner

All ten zero-closure gates remain open for structural reasons: Form_C is FFML-blocked; kappa is GO-blocked on approach arcs; Iso_H and DH are classical isolation/density ceilings; SOC and AFE_Moll lack strong offline / mollifier constructions; B_θ has no closed OR-input; O-TL and RH stay open as AND/superordinate gates.

*Per aspera ad astra.*
