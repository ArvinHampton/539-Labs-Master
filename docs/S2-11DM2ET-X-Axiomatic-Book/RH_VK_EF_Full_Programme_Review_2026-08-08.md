# Vinogradov–Korobov Bounds, Explicit Formula Techniques, and Full-Programme Review (2026-08-08)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure A · ZLA · no model constants  
**Does not prove:** RH · Form C · B_θ · O-TL · κ with p>1  
**Does:** deepen VK and explicit-formula ledgers; audit the whole pure-Cat-A RH stack for missed angles, patterns, and correlations

**Results:** `rh_vk_ef_full_review_results.json`  
**Avoid list still in force:** absolute far cosmetics · RW-only κ as theorem · free-t resonance as Form C · Levinson as O-Moll · residual⇒RH

---

# Part A — Vinogradov–Korobov bounds

## A.1 Zero-free form

For large \(|t|\) and some absolute \(c>0\),
\[
\zeta(\sigma+it)\ne 0
\quad\text{whenever}\quad
\sigma \ge 1 - \frac{c}{(\log|t|)^{2/3}(\log\log|t|)^{1/3}}.
\]
Asymptotically wider near \(\sigma=1\) than the classical de la Vallée Poussin cusp \(1-c'/\log|t|\). Explicit modern constants exist in the literature (Ford; later refinements) — this note freezes **shape and role**, not a single certified decimal \(c\).

## A.2 Consequence for \(\psi-x\) (PNT error)

VK-quality zero-free regions yield prime-number theorem error terms of schematic shape
\[
\frac{|\psi(x)-x|}{x}
\ll
\exp\Bigl(-c\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}\Bigr)
\]
(up to standard logarithmic factors and the precise exponent pair from the zero-free width). Classical zero-free regions give the weaker \(\exp(-c\sqrt{\log x})\) envelope.

## A.3 Consequence for the signed residual / Form C **upper** bound

From signed-sum Theorem 5.1 style estimates,
\[
\Biggl|
\rho_\star\int_2^X\frac{\psi(x)-x}{x^{\rho_\star+1}\log x}\,dx
\Biggr|
\]
is majorized by inserting the PNT error. VK **shrinks the upper envelope** relative to classical ZF, but the envelope still tends to infinity for \(\beta_\star<1\). Therefore:

| Claim | VK status |
|-------|-----------|
| Better unconditional **upper** bound on \(|S_X|\) | **Yes** (quality improvement) |
| Proof of Form C (\(\limsup|S_X|=\infty\)) | **No** |
| Dissolution of FFML | **No** |
| Iso_H at moderate \(\beta_\star\) | **No** |

## A.4 Interaction with height

VK free region is still a **neighborhood of \(\sigma=1\)**. A putative rightmost zero at moderate \(\beta_\star\in(1/2,1)\) is constrained only when \(\beta_\star\) tries to approach 1 at large \(|t|\). The bulk of the Form C / Iso_H difficulty at moderate \(\beta_\star\) is untouched by VK.

## A.5 Verdict (VK)

VK is a **classical strength upgrade on the upper-bound side** of the ledger. It does not open any lower-bound gate (Form C, SOC strong, GO) or isolation gate (Iso_H).

---

# Part B — Explicit formula techniques

## B.1 Inventory of EF-type tools in the programme

| Form | Role | Status |
|------|------|--------|
| **Truncated von Mangoldt EF** \(\psi(x)=x-\sum_{\lvert\gamma\rvert\le T}x^\rho/\rho-\cdots+R(x,T)\) | Literature input to signed residual | **Used; classical** |
| **Stieltjes identity** for \(S_X=\int d\psi/(x^{\rho_\star}\log x)\) | Master start of B_θ note | **Proved** |
| **Signed residual Thm 4.1** \(S_X=\rho_\star\int(\psi-x)\cdots+B+E\) | Eliminates signed zero sum | **Proved** |
| **Self \(\log\log\) cancel** | Removes naive monodromy-style loglog | **Proved** |
| **GHK hybrid** \(\zeta=P_XZ_X(1+E)\) | Phase split / M1.2 / OPC | **Classical + programme** |
| **Theorem E1** on \(E_1\) | \(C_U=1\) for Re\(w\ge0\) | **Proved** |
| **Weil / Guinand test-function EF** | Smooth weights on primes ↔ zeros | **Under-used (MA1)** |

## B.2 Truncated EF — parameter tension \((X,T)\)

Remainder schematic:
\[
|R(x,T)|
\ll
\frac{x\log(xT)}{T}+\log x.
\]
In the residual error \(E_X(T)\), terms of size
\[
|\rho_\star|\,\frac{X^{1-\beta_\star}\log(XT)}{T\log X}
\]
appear. Large \(T\) helps the remainder but:

- enumerating zeros to height \(T\) is the EF truncation cost;
- hybrid far-sum bookkeeping at height \(\sim|\gamma_\star|\) is a different \(T\)-scale;
- VK improves \(\psi-x\) independently of \(T\), which **relaxes** pressure on \(T\) for **upper** bounds.

**No choice of \((X,T)\) converts upper bounds into Form C.**

## B.3 What EF has already resolved

1. Off-diagonal signed zero sum → weighted \(\psi-x\) integral (no RH).  
2. Exact cancellation of pure self \(\log\log\).  
3. Clean split of open problem into Form C / phase-aligned prime-side large values.  
4. Hybrid phase identity for OPC (GHK).

## B.4 What EF has not resolved

1. Lower bound for \(S_X(\rho_\star)\) at fixed off-line \(\rho_\star\) (Form C).  
2. Uniform κ for far hybrid \(U\)-sums (M1.2).  
3. Strong off-line OPC-Core.  
4. Weil-smoothed dual forms of Form C (not yet written as theorems).

## B.5 Duality remark (EF ↔ hybrid)

```text
Near-line Off_X  --EF-->  prime integral (Form C side)     [signed-sum attack]
Far hybrid U-sum --???-->  dual prime expression?          [MA8 under-used]
```

The programme fully dualized the **near-line signed sum**. The **far hybrid κ** problem is still mostly on the zero/U side (absolute majorants + E1). An EF-style duality for far \(U\) is a missed angle (below).

## B.6 Verdict (EF)

Explicit formulae are the **identity backbone** of the pure track. Remaining difficulty is **frozen-parameter estimation**, not missing Stieltjes bookkeeping.

---

# Part C — Full-programme review: correlations

## C.1 Strongest proved correlations

| Pair | Link |
|------|------|
| Form C ↔ B_θ | Equivalence via Thm 4.1 |
| Form C ↔ EF | Bridge primes ↔ zeros |
| Iso_H / DH → B_θ | Proved implications under (RM) |
| E1 → absolute κ | \(C_U=1\) |
| typical Ω → O-PC partial | Proved on-line scale |
| VK ↔ EF | Better \(\psi-x\) in residual uppers |
| GHK identity ↔ OPC | Phase peel |

## C.2 Dual / negative correlations

| Pair | Link |
|------|------|
| Form C ↔ κ | Lower vs upper phase demands (**dual**) |
| residual A ↔ RH | ZLA **forbidden** |
| density ↔ Iso_H | **Dead edge** |
| free-t resonance ↔ Form C | **FFML** |

## C.3 Correlated **open** pairs (not proved links)

| Pair | Nature |
|------|--------|
| GO ↔ SOC | Shared need for large hybrid times; GO adds gaps |
| ε_other ↔ Iso_H | Adjacent for amplitude-Ω path |
| κ ↔ EF dual (MA8) | Speculative conversion route |

---

# Part D — Structural patterns (six)

### P1. Upper-vs-lower asymmetry
Classical strength (VK, ZF, absolute majorants, GHK \(E\)) is mostly **upper** bounds. Open resolution gates are **lower** bounds (Form C, strong SOC, GO joint) or **isolation** (Iso_H).

### P2. Free-parameter vs frozen-parameter
Tools that **choose** \(t\), pretentious character, or path radius fail when the parameter is **frozen** by a zero (γ⋆, local isolation). FFML is the flagship instance; path-radius vs mean gap is another.

### P3. Vacuous-if-RH
Form C, Iso_H at β⋆>1/2, off-line DH, off-line B_θ are **idle under RH**. They are RH-**failure** engines. On-line O-TL is the RH-**compatible** primary.

### P4. OR-cut vs AND-cut
B_θ = OR of {Form C, Iso_H, DH}. O-TL = AND of {κ, GO, SOC, AFE-Moll}. Strategy: a single B_θ gate can be cheaper than the full O-TL stack — still not RH.

### P5. Identity-rich, estimate-poor
Proved: residual formula, hybrid identity, E1, self cancel, typical Ω. Open: estimates of frozen objects. Do not re-derive identities.

### P6. False-friend pattern
Right classical tool, wrong target: Levinson≠O-Moll, Soundararajan≠Form C, density≠Iso_H, monodromy of \(P_X\)≠phase engine.

---

# Part E — Missed angles (twelve)

| ID | Angle | Priority | Notes |
|----|-------|----------|-------|
| **MA1** | Weil/Guinand test-function EF | medium | Under-used; smoothed dual of Form C |
| **MA2** | Guinand–Weil on the line | low | On-line alternative bookkeeping |
| **MA3** | Joint (X,T) optimization under VK+EF | medium hygiene | Better uppers only |
| **MA4** | Landau–Ingham Ω coefficient precision | medium | ε_other bookkeeping |
| **MA5** | Pair correlation → variance of Form C | medium | Typical size ≠ limsup |
| **MA6** | Metric Diophantine for \(\{\gamma_\star\log p/2\pi\}\) | **high long-shot** | n-aspect alignment |
| **MA7** | Smoothed Form C | medium | Easier analysis risk hiding limsup |
| **MA8** | EF dual of far hybrid U for κ | **high structural** | Completes dual to Form C |
| **MA9** | Bombieri–Vinogradov averages | low for Form C | Averaging ≠ fixed ρ⋆ |
| **MA10** | Strategic use of OR vs AND | strategic | Effort allocation |
| **MA11** | Vacuous-if-RH global lock | conceptual | Hygiene |
| **MA12** | Dual lower/upper global lock | conceptual | Hygiene |

**Highest-value missed angles for continued work:**  
1. **MA8** — dualize far \(U\) (κ) the way near-line Off was dualized to primes.  
2. **MA6** — Diophantine n-aspect at fixed γ⋆ (faces FFML head-on with zero-ordinate structure).  
3. **MA1** — Weil smooth weights (new identity surface, not free-t resonance).

---

# Part F — What is *not* missed (do not reopen)

- Signed residual formula and self loglog cancel  
- E1 and absolute \(C_U=1\)  
- Typical on-line Ω and hybrid phase identity  
- Density vs isolation separation  
- A4⁺/A5⁺ residual stack (ZLA firewall)  
- Dead routes list (monodromy, Levinson-as-O-Moll, residual⇒RH, …)

---

# Part G — Global verdict

| Domain | Outcome of this review |
|--------|------------------------|
| VK bounds | Upper-bound upgrade only; Form C/FFML untouched |
| Explicit formulae | Backbone complete; Weil form + far-U dual under-used |
| Patterns | Six structural patterns locked |
| Missed angles | Twelve listed; top: MA8, MA6, MA1 |
| Correlations | Dual Form C/κ and EF/VK pairing strongest |
| Unconditional resolutions | **0** |
| RH / O-TL | **Open** |

---

## One-liner

> VK and EF sharpen the **upper-bound and identity** side of the ledger; the open resolution surface remains **frozen-parameter lower bounds and isolation**, with the most interesting missed angles being EF-dual κ (MA8), n-aspect Diophantine at fixed γ⋆ (MA6), and Weil-smoothed Form C (MA1).

**Status code:** `RH_VK_EF_FULL_REVIEW_2026-08-08`

*Per aspera ad astra.*
