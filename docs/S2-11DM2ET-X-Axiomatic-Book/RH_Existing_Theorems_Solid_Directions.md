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

## 6. Most solid near-term directions (current ranking)

**On-line Kronecker / model-\(\operatorname{Im} D_X\) Omega is accepted** (`RH_Resonance_Discrepancy_Attack.md`).  
The remaining solid directions are those that move **off the line**, make M1.2 **numerical**, or **continue** from the known on-line Omega toward O-TL.

| Rank | Direction | Obligation | Status |
|------|-----------|------------|--------|
| **1** | **Mass-with-A under (RM) only** (polylog \(A\) on \(K_\star\)) | unconditional B_θ without full Iso_H | **Open** — preferred |
| **2** | **StripDens** | weakens Lip \(A\) | **Open** |
| **3** | **Resonance off the line** | O-PC / O-TL | **Open** |
| **4** | **Effective density constants** \((A,B,C)\) | O-M1.2 | Architecture accepted |

**Recorded:** finite products; Ivić; Criteria A–D. Secondary: Iso_H; path continuation.

### ND1 bridge (locked)

**(RM)+(Iso_H) ⇒ B_θ** proved. Barrier: unconditional **(Iso_H)** or **Mass-with-A**.

**None of 1–4 is known to succeed.** All stay inside **ZLA**.

### Already executed (not re-listed as open solid work)

1. On-line resonance/Diophantine Omega — **accepted** (`RH_Resonance_Discrepancy_Attack.md`).  
2. Conditional M1.2 **architecture** — **accepted** (`RH_M1_2_Effective_Density.md`); only numerical \((A,B,C)\) remain.

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
**Solid directions (updated):** (1) Mass-with-A under (RM) only; (2) StripDens; (3) resonance off the line; (4) effective density constants.

**RH remains open.**

---

## One-liner

**Solid pure-Cat-A directions are Mass-with-A under (RM), StripDens, off-line resonance, and effective density constants — none yet closes O-TL or RH.**

*Per aspera ad astra.*
