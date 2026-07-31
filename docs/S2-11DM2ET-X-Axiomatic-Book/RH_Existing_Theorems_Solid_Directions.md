# Existing theorems and solid research directions

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. Axiom **ZLA** in force. No model constants.  
**None of the works below closes O-TL or RH.**

**Companions:**  
`RH_Remaining_Analytic_Obligations.md`,  
`RH_OPC_Omega_Discrepancy.md`,  
`RH_OPC_Partial_Resolution.md`,  
`RH_Akatsuka_GHK_Survey.md`.

---

## 0. Standing status

| Item | Status |
|------|--------|
| O-TL (target lemma) | **Open — primary** |
| Strong O-PC (\(\gg\log\log X\)) | **Open** |
| Typical Omega \(\gg\sqrt{\log\log X}\) for \(\theta_X,\Delta_X\) on the line | **Proved** (programme) |
| RH | **Open** |
| Programme label | `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` |

---

## 1. Argument of zeta and Omega theorems for \(S(t)\)

Classical and modern Omega results for \(S(t)=\frac1\pi\arg\zeta(\tfrac12+it)\) supply the model for extreme phase behaviour on the critical line.

- **Montgomery-type Omega results**, improved by **Bondarenko–Seip** and by **Chirre–Mahatab**: under RH one has forms of the strength
  \[
  S(t)
  =
  \Omega_\pm\Biggl(
  \frac{\log t\cdot\log\log\log t}{\log\log t}
  \Biggr)
  \]
  (schematic; see the cited works for exact ranges and constants).
- **Explicit upper bounds** for \(S(t)\) and \(S_1(t)\) under RH (Goldston–Gonek; Carneiro–Littmann–Vaaler; later explicit work).

**Role in the programme.**  
These control the argument of \(\zeta\) itself. Transferring them to the hybrid discrepancy \(\arg\zeta-\arg Z_X\) or to \(\theta_X\) **off the line** is still open, but the methods (resonance, extremal majorants, explicit formulae) are the natural toolkit for strengthening Theorem Ω-Δ beyond \(\sqrt{\log\log X}\).

---

## 2. Large values of Dirichlet polynomials and resonance

**Soundararajan’s resonance method** produces large values of \(\lvert\zeta(\tfrac12+it)\rvert\) and of central \(L\)-values. The same idea applies to finite Dirichlet polynomials
\[
D(t)=\sum_{n\le X}a_n n^{-it}.
\]

Mean-square and higher-moment estimates for such polynomials are classical (Montgomery–Vaughan, Huxley, Bourgain, Jutila, and recent large-value estimates). The modest Omega result already recorded in the programme
\[
\limsup_{t\to\infty}\bigl\lvert\theta_X(\tfrac12+it)\bigr\rvert
\gg
\sqrt{\log\log X}
\quad\text{(fixed \(X\))}
\]
is of this type (`RH_OPC_Omega_Discrepancy.md`).

**Direction.**  
Strengthen the resonance or the moment method so that the same polynomials yield Omega results of size \(\gg\log\log X\), or yield large discrepancy at points where \(\lvert\zeta\rvert\) is small.

---

## 3. Finite Euler products and hybrid formulae

- **Gonek**, *Finite Euler products and the Riemann Hypothesis*: short truncations of the Euler product approximate \(\zeta\) well in much of the right half-strip under RH; conversely, good approximation forces only finitely many zeros in the region. Constructed model functions satisfy an RH of their own and exhibit repulsion.
- **Gonek–Hughes–Keating** hybrid Euler–Hadamard product: the precise splitting
  \[
  \zeta=P_X Z_X\bigl(1+O(\varepsilon_X)\bigr)
  \]
  already used throughout the programme.
- **Akatsuka**: pointwise asymptotics of partial Euler products in the right half-strip, including the real \(m\log\log x\) term on the line (modulus / renormalization).

**Direction.**  
Push the Gonek finite-product approximation **off** the critical line at points of large \(1/\lvert\zeta\rvert\), and convert approximation quality into a lower bound on \(\lvert\arg P_X\rvert\) or on the discrepancy.

---

## 4. Zero-density estimates

**Ingham**, **Huxley**, and later **explicit** versions bound \(N(\sigma,T)\). These are the classical input needed for a uniform M1.2 remainder (control of distant zeros). Recent explicit forms of Ingham’s estimate make the constants **effective**.

**Direction.**  
Feed a concrete density theorem into the majorant tree for \(c_3\) and close a **conditional uniform M1.2** on a range of heights (O-M1.2).

---

## 5. Pair correlation and almost-all consequences

**Montgomery’s PCC**, **Gallagher–Mueller**, and recent work (Goldston–Lee–Schettler–Suriajaya and related) show that a usable form of pair correlation forces asymptotically **100 %** of zeros to be simple and on the critical line (under the stated hypotheses). This is the strongest almost-all horizontal statement currently available from vertical correlation hypotheses.

**Direction.**  
Convert almost-all isolation into an almost-all lower bound on the hybrid discrepancy along a sparse set of points, then upgrade to an Omega statement if possible. This remains part of **O-PC** (strong / off-line layers still open).

---

## 6. Most solid near-term directions (ranked by proximity to existing technology)

| Rank | Direction | Obligation touched |
|------|-----------|--------------------|
| **1** | **Resonance / large-value method for the hybrid discrepancy** — adapt Soundararajan resonance or Dirichlet-polynomial large-value estimates to \(\operatorname{Im}(\log\zeta-\log Z_X)\) or \(\operatorname{Im}\log P_X\); seek Omega **stronger than** \(\sqrt{\log\log X}\) | O-PC strong |
| **2** | **Conditional uniform M1.2 via explicit zero-density** — insert an explicit Ingham–Huxley bound into the existing majorant tree; fully effective remainder on a concrete height range | O-M1.2 |
| **3** | **Off-line finite-Euler-product approximation (Gonek style)** — extend the region where short products approximate \(\zeta\); measure argument of the ratio at numerical minima of \(\lvert\zeta\rvert\) | O-PC / O-M1.3bis |
| **4** | **Path accumulation (M1.3-bis)** — once a local angular increment \(\gg\sqrt{\log\log X}\) (or larger) is available, design a path or sequence of truncations that accumulates to \(\gg\log\log X\) | O-M1.3bis |
| **5** | **Phase-oriented mollifier** — optimise a Dirichlet polynomial for **argument** rather than modulus; use as a detector of large discrepancy | O-Moll |

**None of these is known to succeed.** All stay inside **ZLA**.

### Most concrete next analytic steps (programme decision)

1. A **resonance attack** on the hybrid discrepancy.  
2. A **fully effective conditional M1.2** from classical density theorems.

---

## 7. What is **not** a solid direction inside the pure programme

- Model constants, Resonant Algebra packaging, or 539-step claims used as lemmas about zeros of \(\zeta\).  
- Function-field theorems treated as **proofs** for the classical zeta function.  
- **Weakening O-TL** to the typical scale \(\sqrt{\log\log X}\) without an **explicit** decision to change the target.

---

## 8. Summary

The strongest existing technology for the open obligations lies in:

- Omega and large-value methods for Dirichlet polynomials and for \(S(t)\),  
- the Gonek finite-product and GHK hybrid machinery,  
- explicit zero-density estimates,  
- and the almost-all consequences of pair correlation.

**The primary obligation O-TL remains open.**  
The most concrete next analytic steps are a **resonance attack on the hybrid discrepancy** and a **fully effective conditional M1.2** from classical density theorems.

**RH remains open.**

---

## One-liner

**Solid near-term pure-Cat-A work is resonance/large values for the discrepancy and effective density-based M1.2; classical \(S(t)\) Omega, GHK/Gonek/Akatsuka, and PCC almost-all results are the toolkit — none of them yet closes O-TL or RH.**

*Per aspera ad astra.*
