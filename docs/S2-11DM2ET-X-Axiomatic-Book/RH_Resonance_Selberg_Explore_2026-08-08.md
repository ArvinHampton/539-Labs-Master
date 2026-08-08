# Multiplicative Resonance and Selberg Symmetry — Gap Feed Analysis (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** PAO · κ · O-TL · B_θ · RH  
**Score alphabet:** **−1** blocks / false friend / dual opposition · **0** neutral · **+1** feeds tip or infrastructure  
**Input gaps:** dependency graph cut analysis · H1–H5  
**Results:** `rh_resonance_selberg_explore_results.json`

---

## 0. Mandate and reading of (−1, 0, +1)

Score every classical technique against each open gap tip:

| Score | Meaning |
|------:|---------|
| **+1** | Directly feeds the tip or is the correct identity surface to attack it |
| **0** | No material feed (or only heuristic) |
| **−1** | Actively opposed / false friend / dual conflict |

Goals scored: PAO, κ, Iso_H, DH, GO, SOC (on-line strong / off-line), O-Moll, O-TL.

---

## Part I — Multiplicative resonance techniques

### I.1 Inventory and scores

| ID | Technique | PAO | κ | SOC on | SOC off | O-Moll | GO |
|----|-----------|----:|--:|-------:|--------:|-------:|---:|
| MR1 | Soundararajan short resonator | 0 | 0 | **+1** | 0 | 0 | 0 |
| MR2 | Kronecker prime-angle torus | 0 | **−1** | **+1** | 0 | 0 | 0 |
| MR3 | Littlewood Ω (zero alignment at x) | **+1** | 0 | 0 | 0 | 0 | 0 |
| MR4 | Bondarenko–Seip long resonator | 0 | 0 | **+1** | 0 | 0 | 0 |
| MR5 | Random multiplicative {−1,0,+1} models | 0 | 0* | 0 | 0 | 0 | 0 |
| MR6 | EF resonance at fixed γ⋆ (PAO attack) | **+1** | **−1** | 0 | 0 | 0 | 0 |

\*MR5 predicts RW κ ∼ J^{−1/2}, which arithmetic shows is **insufficient** for the M1.2 joint window — heuristic ceiling, not a +1.

### I.2 Mechanism map

**A. t-variable resonance (Soundararajan / Bondarenko–Seip / Kronecker)**

Free variable: height \(t\).  
Object: large \(|\zeta(1/2+it)|\) or large \(\operatorname{Im} D_X(t)\).  
Engine: multiplicative coefficients \(r(n)\) or phase choice \(t\log p \bmod 2\pi\).

**Programme status:** already used for **accepted on-line strong** model \(\operatorname{Im} D_X\) at fixed \(X\) (`RH_Resonance_Discrepancy_Attack.md`).  
**Does not give:** PAO (wrong free variable \(t\) vs \(x\)), off-line SOC, κ, Iso_H, DH, GO.

**B. x-variable Ω (Littlewood / explicit formula)**

Free variable: real \(x\).  
Object: \(\psi(x)-x=\Omega(x^{\beta})\).  
Engine: align zero phases \(x^{\rho}/\rho\) by Dirichlet approximation on ordinates.

**Programme status:** amplitude half of PAO — **classical**.  
**Missing half:** lock the large values to the single phase \(e^{i\gamma_⋆\log x}\) of the residual weight on sets of log-measure \(\gg 1\) (or \(\to\infty\)).

**C. Dual conflict (MR2 / MR6 vs κ)**

Any technique that **aligns** phases to force a large signed sum is **hostile** to a κ **upper** bound:

```text
resonance alignment  ──(+1)──►  PAO / on-line large Im D_X
                     ──(−1)──►  kappa (needs cancellation)
```

This is the dual gap of the dependency analysis, now seen at the level of method.

### I.3 Random multiplicative ceiling {−1, 0, +1}

Steinhaus / Rademacher / character-like models assign independent \(X(p)\in\{-1,0,+1\}\) or unit-circle laws and predict:

- large values of random Euler products at the usual scales;
- **square-root cancellation** for signed sums of many terms.

**Consequence for κ:** the “default multiplicative randomness” predicts \(\kappa\sim J^{-1/2}\), which **fails** the numerical bar \(p\gtrsim 1.12\) (safer \(p\sim 2\)).  
So either κ is false (then M1.2 joint window stays closed under real \(c_1\)), or zeta far-sums have **stronger-than-random structure** — not something resonance methods currently prove.

### I.4 Resonance → PAO: exact remaining gap

Littlewood + EF give (schematic):

\[
\limsup_{x\to\infty}\frac{|\psi(x)-x|}{x^{\beta_⋆}/|\rho_⋆|}\ge 1-\varepsilon_{\mathrm{other}}.
\]

PAO needs, on a set of positive log-measure (or infinite total measure),

\[
\operatorname{Re}\Bigl(e^{-i\gamma_⋆\log x}(\psi(x)-x)\,x^{-\beta_⋆}\Bigr)\ge c>0.
\]

**Obstruction:** the \(x\) that align **many** zeros for amplitude Ω need not be the \(x\) that align with **one** fixed frequency \(\gamma_⋆\). If Iso_H fails, other same-abscissa zeros contaminate the phase (links PAO difficulty to Iso_H, without an edge that density can fix).

**Verdict Part I:** Resonance explores cleanly; **no tip closed**. Best feeds: SOC on-line (**+1**), PAO amplitude (**+1**). Dual **−1** on κ.

---

## Part II — Selberg symmetry methods

### II.1 Inventory and scores

| ID | Technique | PAO | κ | Iso_H | DH | SOC off | O-Moll |
|----|-----------|----:|--:|------:|---:|--------:|-------:|
| SS1 | ξ(s)=ξ(1−s) FE symmetry | 0 | 0 | 0 | 0 | 0 | 0 |
| SS2 | Approximate FE / Riemann–Siegel | 0 | 0 | 0 | 0 | 0 | **+1** |
| SS3 | Selberg–Levinson–Conrey mollifiers | 0 | 0 | 0 | 0 | 0 | **−1** |
| SS4 | Selberg-type zero density | 0 | 0 | 0 | 0 | 0 | 0 |
| SS5 | Selberg class axioms | 0 | 0 | 0 | 0 | 0 | 0 |
| SS6 | Path design via s↔1−s for arg | 0 | 0 | 0 | 0 | **+1** | 0 |
| SS7 | Hybrid GHK + FE (Akatsuka) | 0 | **+1** | 0 | 0 | 0 | 0 |

### II.2 Mechanism map

**A. FE / ξ symmetry (SS1)**  
Already fully used: conjugate lock, quartets, only forced same-abscissa partner is \(\bar\rho_⋆\) for rightmost \(\beta_⋆>1/2\).  
**Does not** yield Iso_H, DH, PAO, or κ. Score **0** across tips — completed asset, not a residual gap.

**B. Approximate FE (SS2)**  
Natural surface on which a **true** phase-oriented mollifier might be written (dual Dirichlet polynomials, asymmetric lengths).  
Score **+1 infrastructure** for O-Moll design only — **no construction exists** in the programme (N3).

**C. Classical mollifiers (SS3) — false friend**  
Selberg / Levinson / Conrey optimize **zeros on the critical line** via mollified second moments.  
That is a **different functional** from \(A_X\) or \(\theta_X\) at maximal abscissa.  
Score **−1** for O-Moll: misidentification is a documented non-route.

**D. Selberg density (SS4)**  
Improves \(N(\sigma,T)\) near \(\sigma=1/2\); Step B still shows **positive T-powers** at moderate \(\sigma\).  
Does not open DH polylog; does not open Iso_H.

**E. Path symmetry s↔1−s (SS6)**  
Weak **+1** for off-line bookkeeping: bounds on the left of the critical line transfer to the right via \(\chi(s)\).  
Does **not** create \(\log\log\) phase at \(\beta_⋆\) or replace GO.

**F. GHK hybrid (SS7)**  
Correct identity surface for **κ** (far \(U\sim E_1\) sums) and for OPC peeling.  
Score **+1 infrastructure** for κ — theorem still open. E1 \(C_U=1\) already extracted.

### II.3 Verdict Part II

Selberg symmetry methods are **mostly neutral** on the open tips.  
Two infrastructure +1’s (AFE for O-Moll design; GHK for κ surface).  
One dangerous **−1** (classical mollifiers as O-Moll).  
**No tip closed.**

---

## Part III — Combined matrix (best score per gap)

| Gap tip | Best resonance | Best Selberg | Best overall | Closed? |
|---------|---------------:|-------------:|-------------:|:-------:|
| PAO | +1 (MR3/MR6) | 0 | +1 feed, not proof | **No** |
| κ | −1 (dual) | +1 (GHK surface) | +1 infra only | **No** |
| Iso_H | 0 | 0 | 0 | **No** |
| DH | 0 | 0 | 0 | **No** |
| GO | 0 | 0 | 0 | **No** |
| SOC on-line strong | +1 | 0 | +1 (already used) | **Partial** (accepted model) |
| SOC off-line | 0 | +1 weak (FE path) | weak infra | **No** |
| O-Moll | 0 | +1 AFE / −1 false friend | design surface only | **No** |
| O-TL | 0 | 0 | 0 | **No** |

---

## Part IV — Structural conclusions

1. **Resonance is the right family for on-line large values** and for the **amplitude half of PAO**; it does not prove PAO(c,δ).  
2. **Resonance is dual-hostile to κ** (alignment vs cancellation).  
3. **Random multiplicative {−1,0,+1} heuristics predict insufficient κ** for M1.2 — reinforcing the N1 obstruction.  
4. **Selberg FE symmetry is already spent** on conjugate structure; not a new lever.  
5. **Classical Selberg mollifiers must not be mistaken for O-Moll.**  
6. **AFE + GHK are the correct design surfaces** for future O-Moll and κ proofs respectively — surfaces, not proofs.  
7. **Unconditional resolutions from this exploration: 0.**

---

## Part V — Recommended attack order (if continuing)

| Priority | Action | Not |
|----------|--------|-----|
| 1 | Direct PAO: control \(\varepsilon_{\mathrm{other}}\) + measure of \(x\) aligned to **single** γ⋆ (EF + Diophantine) | Re-running Soundararajan for |ζ| alone |
| 2 | κ on GHK/U surface: prove any κ ≤ J^{−p}, p>1, even conditional | Expecting resonance to cancel |
| 3 | Keep FE path bookkeeping for off-line transfer | Claiming FE ⇒ Iso_H |
| 4 | If designing O-Moll, start from AFE dual sums | Levinson zero-count mollifiers |

---

## One-liner

> Multiplicative resonance feeds on-line strong Ω and PAO’s amplitude half but fights κ; Selberg symmetry is largely spent or neutral, with classical mollifiers as false friends; AFE/GHK are design surfaces only — **no open tip closed**.

**Status code:** `RH_RESONANCE_SELBERG_EXPLORE_2026-08-08`

*Per aspera ad astra.*
