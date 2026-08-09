# Soundararajan and Zero Density — Investigation (2026-08-09)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure A · ZLA  
**Does not prove:** DH · Iso_H · Form C · Mass-with-A · B_θ · RH  
**Mandate:** Investigate “Soundararajan zero density” and map it onto the programme density gate  

**Results:** `rh_soundararajan_zero_density_results.json`  
**Companions:** `RH_Density_vs_Isolation.md`, `RH_StepB_Density_Gap_Table_2026-08-08.md`, `RH_H3_…`, `RH_Resonance_Selberg_Explore_2026-08-08.md`

---

## 0. Clarification (important)

**Kannan Soundararajan is not the classical author of \(N(\sigma,T)\) exponent improvements.**

That lineage is roughly:

> Ingham → Huxley → Heath-Brown → … → **Guth–Maynard (2024)** large-values breakthrough  

Soundararajan’s signature zeta tools are:

| Contribution | Role |
|--------------|------|
| **Resonance method** (extreme values of \(\lvert\zeta(\tfrac12+it)\rvert\)) | Free-\(t\) large values |
| **Moments of \(\zeta\)** (2009 Annals; Harper refinements under RH) | Value distribution |
| **\(M(x)\) bounds under RH** | Conditional Mertens-function growth |
| **Ford–Soundararajan–Zaharescu** | Fractional parts of ordinates / pair correlation |
| Surveys on value distribution | Synthesis |

When people say “Soundararajan” next to “density,” they usually mean:

1. Resonance / large values as the **engine behind** zero-density technology, or  
2. Moment proofs that **use** zero-density estimates, or  
3. FSZ-type statistics **near** the critical line,  

**not** a theorem \(N(\beta_\star,T)=O((\log T)^C)\) at moderate \(\beta_\star\) (the programme’s **DH** gate).

---

## 1. Classical zero density

### 1.1 Definition

\[
N(\sigma,T)
=
\#\bigl\{\rho=\beta+i\gamma:\ \beta\ge\sigma,\ 0<\gamma\le T\bigr\}
\]
(count with multiplicity).

### 1.2 Density Hypothesis (standard form)

A common formulation:
\[
N(\sigma,T)
\ll_\varepsilon
T^{2(1-\sigma)+\varepsilon}
\qquad (\sigma\ge\tfrac12).
\]
Implied by RH; weaker than RH. Recent large-values work (Guth–Maynard and predecessors) improves exponents in ranges, but:

> At moderate \(\sigma\in(\tfrac12,1)\), bounds still allow a **positive power of \(T\)**.

### 1.3 Schematic \(T\)-powers (shape only)

| \(\sigma\) | Ingham-shape schematic | Density Hyp. \(2(1-\sigma)\) | Programme polylog? |
|-----------:|-----------------------:|-----------------------------:|:------------------:|
| 0.55 | 0.931 | 0.900 | no |
| 0.60 | 0.857 | 0.800 | no |
| 0.70 | 0.692 | 0.600 | no |
| 0.80 | 0.500 | 0.400 | no |
| 0.90 | 0.273 | 0.200 | no |
| 0.95 | 0.143 | 0.100 | no |

**Programme DH** (for Mass-with-A ⇒ B_θ) asks for **polylog** \(N(\beta_\star,T)=O((\log T)^C)\) at some usable moderate \(\beta_\star\).  
That is **stronger** than the standard Density Hypothesis (still a power of \(T\) when \(1-\sigma\) is fixed away from 0).

---

## 2. What Soundararajan’s methods do for density

### 2.1 Resonance ↔ large values ↔ zero density

Zero-density proofs typically go:

```text
large values of Dirichlet polynomials / zeta
        →  constraints on zeros
        →  bound N(sigma,T)
```

Soundararajan’s **resonance method** **produces** large values of \(\lvert\zeta(\tfrac12+it)\rvert\) on a positive-measure set of free \(t\). Scores:

| For | Score |
|-----|------:|
| On-line strong Ω / SOC (free \(t\)) | **+1** (already used) |
| Form C at fixed \(\gamma_\star\) | **FFML block** |
| Programme polylog DH | **0** |
| Iso_H | **0** (density ≠ isolation) |

### 2.2 Moments paper

Bounds moments of \(\lvert\zeta(\tfrac12+it)\rvert\) (sharp conditional forms via Harper under RH). Zero-density estimates appear as tools in the broader literature; moments theorems are **not** zero-density theorems.

### 2.3 Ford–Soundararajan–Zaharescu

Theme: fractional parts of \(\gamma\), pair correlation, primes in short intervals.  
Uses Selberg-type density **near** \(\operatorname{Re}=\tfrac12\), not moderate-\(\sigma\) polylog DH.

| Helps | Does not give |
|-------|----------------|
| Zero statistics; GO heuristics | GO theorem · Iso_H · programme DH |

---

## 3. Map onto programme gates

| Gate | Resonance | Classical \(N(\sigma,T)\) | FSZ / moments |
|------|:---------:|:------------------------:|:-------------:|
| SOC on-line | **+1** | 0 | partial |
| Form C | FFML | 0 | 0 |
| Programme DH (polylog) | 0 | 0 (\(T\)-powers) | 0 |
| Standard Density Hyp. | 0 | open/partial by range | 0 |
| Iso_H | 0 | 0 (dead edge) | 0 |
| Mass-with-A / B_θ / RH | no | no | no |

### Does Soundararajan close programme DH?

**No.** Even full standard Density Hypothesis at \(\beta_\star=0.6\) is like \(T^{0.8+\varepsilon}\), not \(O((\log T)^C)\).

### Density vs isolation

```text
N(sigma,T) small  =/=>  only two zeros on Re=sigma
```

Unchanged dead edge.

---

## 4. FFML / prior resonance scores

No revision: resonator still +1 SOC on-line, FFML-blocked for Form C, 0 for programme DH/Iso_H.

---

## 5. What Soundararajan-adjacent progress would need to be

| If one could prove… | Effect |
|---------------------|--------|
| Resonance → joint Ω ∧ wide gaps | Feed **GO** (open) |
| Strong \(\lvert\Delta_X\rvert\gg\log\log\) off-line | Feed **SOC strong** (open) |
| Large values → **polylog** \(N(\beta_\star,T)\) | Feed **programme DH** (far beyond current density) |
| Free-\(t\) only | Does **not** feed Form C |

None of these is a theorem from Soundararajan’s core published results.

---

## 6. Verdict

| Question | Answer |
|----------|--------|
| Soundararajan zero-density theorem closing programme DH? | **No** |
| Resonance helps on-line SOC? | **Yes** (already used) |
| Resonance proves Form C? | **No** (FFML) |
| Modern density (Guth–Maynard et al.) gives polylog at moderate σ? | **No** |
| Density ⇒ Iso_H? | **No** |
| Gates closed this investigation | **None** |

---

## One-liner

> Soundararajan’s strength is **resonance and moments** (free-\(t\) value distribution), not a polylog zero-density theorem; classical \(N(\sigma,T)\) bounds—even after modern large-values breakthroughs—still leave positive \(T\)-powers at moderate \(\sigma\), so DH / Iso_H / Form C stay open.

**Status code:** `RH_SOUNDARARAJAN_ZERO_DENSITY_2026-08-09`

*Per aspera ad astra.*
