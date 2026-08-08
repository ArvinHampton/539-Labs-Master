# Zero-Free Regions, Grand Riemann Hypothesis, and FFML Clarification (2026-08-08)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure A · ZLA · no model constants  
**Does not prove:** RH · GRH · Form C · B_θ · O-TL · Iso_H  
**Does:** map specific classical zero-free regions; state GRH and its programme role; formalize FFML

**Results:** `rh_zfr_grh_ffml_results.json`  
**Companions:** `RH_T1_Form_C_Fixed_Rho_Star_2026-08-08.md`, signed-sum attack, density vs isolation

---

## Part I — Specific zero-free regions

### I.1 Classical (de la Vallée Poussin type)

**Shape.** There exists \(c>0\) such that
\[
\zeta(\sigma+it)\ne 0
\quad\text{for}\quad
\sigma \ge 1 - \frac{c}{\log(|t|+2)}.
\]
Explicit \(c\) appear in Stechkin, Rosser–Schoenfeld, Ford, et al. (values improve over time; this note freezes the **shape**, not a single decimal \(c\)).

**Geometry.** A cusp toward \(\sigma=1\) as \(|t|\to\infty\). Width \(1-\beta \asymp 1/\log|t|\).

### I.2 Vinogradov–Korobov

**Shape.** For some \(c>0\) and large \(|t|\),
\[
\zeta(\sigma+it)\ne 0
\quad\text{for}\quad
\sigma \ge 1 - \frac{c}{(\log|t|)^{2/3}(\log\log|t|)^{1/3}}.
\]
Asymptotically **wider** than classical near \(\sigma=1\). Modern explicit forms: Ford; recent refinements (Bellotti and others).

**Geometry.** Still a neighborhood of the line \(\sigma=1\), **not** a strip down to \(\sigma=1/2+\delta\).

### I.3 Finite-height verification (computational)

All nontrivial zeros with \(|\gamma|\le T_0\) lie on the critical line for large verified \(T_0\).  
**Programme use:** finite-height statements only. **Does not** give unbounded Iso_H for hypothetical \(\beta_\star>1/2\) at arbitrary height.

### I.4 Schematic widths \(1-\beta\) (illustrative constants only)

| \(|t|\) | Classical \(\sim c/\log t\) (c=1/5.7) | VK \(\sim 1/(C(\log t)^{2/3}(\log\log t)^{1/3})\) (C=57.54) |
|--------:|--------------------------------------:|----------------------------------------------------------:|
| 1e+02 | 0.03793 | 0.005452 |
| 1e+06 | 0.0127 | 0.002188 |
| 1e+12 | 0.006349 | 0.001275 |
| 3e+12 | 0.006107 | 0.001237 |
| 1e+30 | 0.00254 | 0.000638 |

Constants are **illustrative** for shape comparison, not interval-certified claims.

### I.5 Zero density is not zero-free

Bounds \(N(\sigma,T)\ll T^{A(1-\sigma)}(\log T)^{O(1)}\) control **counts**, not a zero-free region (`RH_Density_vs_Isolation.md`).

### I.6 Programme feed map

| Feeds | Does not feed |
|-------|----------------|
| PNT / \(\psi-x\) **upper** bounds | Form C **lower** bound |
| Signed residual **upper** envelope | Unconditional Iso_H at moderate \(\beta_\star\) |
| Edge geometry near \(\sigma=1\) | \(\kappa\) with \(p>1\) |
| Constraint on how close \(\beta_\star\) can sit to 1 | O-TL / RH |

If an off-line \(\rho_\star=\beta_\star+i\gamma_\star\) exists, ZF forces \(\beta_\star\) **left** of the free boundary — Form C lives in the allowed band, not inside the free region.

---

## Part II — Grand Riemann Hypothesis

*(Standard spelling: **Grand Riemann Hypothesis**, not “Reimann.”)*

### II.1 Definitions

| Name | Statement |
|------|-----------|
| **RH** | Nontrivial zeros of \(\zeta(s)\) have \(\operatorname{Re}=1/2\) |
| **GRH (Dirichlet)** | Nontrivial zeros of all Dirichlet \(L(s,\chi)\) have \(\operatorname{Re}=1/2\) |
| **Grand RH (automorphic)** | Nontrivial zeros of all automorphic \(L\)-functions have \(\operatorname{Re}=1/2\) |
| **Modified Grand RH** | Same, allowing real-line zeros where appropriate |

RH is the \(\zeta\) special case. Grand RH packages critical-line statements over a large class of \(L\)-functions.

### II.2 Classical consequences (literature)

Under Dirichlet GRH: strong errors for primes in AP, improved effective Chebotarev in many settings.  
Under broader Grand RH: optimal errors in many automorphic PNTs; symmetric-power packages linked to Sato–Tate-type statements.

### II.3 Role in this programme

| Question | Under GRH/RH |
|----------|----------------|
| Off-line \(\rho_\star\) with \(\beta_\star>1/2\)? | **None** — off-line Form C / B_θ **vacuous** |
| Does GRH prove Form C? | **No** (no off-line zero) |
| Does GRH prove Iso_H for \(\beta_\star>1/2\)? | Vacuous |
| Does GRH close O-TL? | **Not automatically** |
| ZLA-admissible? | **Yes** as a **named hypothesis** |
| Does assuming Grand RH prove RH? | It *includes* RH; assuming the package assumes the part — not an unconditional proof |

### II.4 Verdict on Grand RH

Legitimate conditional axiom. Makes off-line Form C **vacuous rather than solved**. Does **not** unconditionally close RH or O-TL.

---

## Part III — FFML barrier, clarified

### III.1 Name

**FFML** = **Fixed-Frequency Multiplicative Large-Value Barrier**

### III.2 Setup

\[
S(X;\rho_\star)
:=
\sum_{n\le X}
\frac{\Lambda(n)}{n^{\rho_\star}\log n},
\qquad
\rho_\star=\beta_\star+i\gamma_\star,\ \beta_\star\in(1/2,1).
\]

**Form C:** \(\limsup_{X\to\infty}|S(X;\rho_\star)|=\infty\).

### III.3 Formal barrier statement

> **FFML.** The following standard method classes do **not**, by themselves, constitute a proof of Form C for a **fixed** off-line \(\rho_\star\):
>
> 1. **Free-frequency large values** — some \(t\in[T,2T]\) with large \(|\sum a_n n^{-it}|\) (Soundararajan, Bondarenko–Seip, …).  
> 2. **Pretentious / Halász** — large values when \(f\) pretends to be \(n^{it}\) for a **chosen** \(t\).  
> 3. **Mean-value in \(t\)** — integrals implying some \(t\) is large.  
> 4. **Absolute triangle inequality** on \(\sum|\Lambda(n)n^{-\beta_\star}/\log n|\) — wrong (unsigned) object.

**One-line mechanism:** those methods **vary or average** frequency; Form C **freezes** frequency to the zero ordinate \(\gamma_\star\).

### III.4 What FFML is **not**

| Not a claim that… |
|-------------------|
| Form C is false |
| Form C is unprovable |
| Free-\(t\) resonance is useless (it feeds on-line SOC) |
| Anything under RH (no off-line \(\rho_\star\); FFML idle) |

### III.5 What FFML **is**

- Programme-level **method barrier** for free-frequency technology vs Form C  
- Dual of “resonance works for free \(t\), not fixed \(\gamma_\star\) in the \(n\)-aspect”  
- Compatible with ZF (ZF limits \(\beta_\star\); does not dissolve FFML)  
- Compatible with GRH (under GRH, off-line Form C vacuous; FFML active only if an off-line zero exists)

### III.6 Escape hatches (open)

1. Methods using that \(\gamma_\star\) **is a zero ordinate** (EF feedback)  
2. Named conditional Form C (not mislabeled free-\(t\) resonance)  
3. Bypass via **Iso_H** or **DH** gates to B_θ  

### III.7 Diagram

```text
Free-t resonance ──(+1)──► on-line SOC / |zeta| large
                 ──(FFML)──/ Form C at fixed gamma*

Zero-free regions ──► upper bounds on psi-x / |S|
                  ──► constrain beta* near sigma=1
                  ──X──► Form C lower bound
                  ──X──► dissolve FFML

GRH/RH true ──► no off-line rho* ──► Form C vacuous; FFML idle
RH false + off-line rho* ──► Form C meaningful; FFML = method barrier
```

---

## Part IV — Scoreboard

| Item | Standing |
|------|----------|
| Classical + VK ZF | **Recorded** |
| ZF → Form C lower bound | **No** |
| Grand RH | **Recorded**; hypothesis only |
| Grand RH → unconditional RH/O-TL | **No** |
| FFML | **Formally clarified** |
| Form C | **Open** |
| Unconditional resolutions | **0** |

---

## One-liner

> Zero-free regions strengthen near-\(\sigma=1\) upper bounds only; Grand RH vacates off-line Form C rather than proving it; FFML is a **method-class barrier** (free frequency vs fixed \(\gamma_\star\)), not a proof that Form C is false.

**Status code:** `RH_ZFR_GRH_FFML_2026-08-08`

*Per aspera ad astra.*
