# Line-by-line extract: Akatsuka (2017) vs schematic (★)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A** literature extract — no model constants.  
**Purpose:** replace loose paraphrase of “Akatsuka’s \(m\log\log x\) term” with the **actual** theorem statements, then map honestly to \(A_X\) / target lemma.

**Primary source.**  
Hirotaka Akatsuka, *The Euler product for the Riemann zeta-function in the critical strip*,  
Kodai Mathematical Journal **40** (2017), no. 1, 79–101.  
DOI: [10.2996/kmj/1490083225](https://doi.org/10.2996/kmj/1490083225) · MR3626575 · zbMATH 06732079.

**Secondary sources quoting theorems in full** (used where the paywalled PDF is not line-extractable here):  
- Kaneko–Koyama–Kurokawa, *Towards the Deep Riemann Hypothesis for \(\mathrm{GL}_n\)*, arXiv:2206.02612v3, Theorem 3.2.  
- Koyama–Kurokawa, *Chebyshev’s Bias for Ramanujan’s \(\tau\)-function via the Deep Riemann Hypothesis*, arXiv:2203.12791, §1 (“Akatsuka’s Theorem”).  
- Akatsuka, *Maximal order for divisor functions…*, arXiv:2411.19259v1 (2024), Remark 1.1 on [1, Corollary 4.4] and related product formulae.

**Notation in this extract.**  
\[
\zeta_x(s)
:=
\prod_{p\le x}(1-p^{-s})^{-1}
=
P_x(s)
\quad\text{(L1 partial Euler product)}.
\]
\[
\psi(x)=\sum_{n\le x}\Lambda(n),\qquad
\vartheta(x)=\sum_{p\le x}\log p.
\]

---

## 0. Correction first (honest mapping to (★))

In `RH_Target_Lemma_Sketch_Literature_L5.md` the schematic
\[
\log P_x(\beta+i\gamma)
=
m\log\log x
+
C_0
+
E(x)
\tag{★}
\]
at an **off-line** zero of **maximal abscissa** was a **programme-level paraphrase**, not a verbatim theorem of [Aka17].

**What [Aka17] actually centers on (as quoted by the DRH literature):**

1. A **critical-line** equivalence relating  
   - a strong prime-number error \(\psi(x)=x+o(\sqrt{x}\log x)\),  
   - a **renormalized** limit of \((\log x)^m\zeta_x(s_0)\) at zeros \(s_0=\tfrac12+i\tau\) of \(\zeta\),  
   - and a Deep Riemann Hypothesis (DRH)–type statement for \(\zeta\).

2. Results linking **asymptotics of partial products** to **zero-free half-planes** \(\operatorname{Re}s>s_0\) (Theorem 2 in [Aka17], per Project Euclid abstract page text).

3. Related renormalized products \(E_1(X)\), \(E_2(X)\) on the critical line, with \(\sqrt{2}\) factors (Ramanujan / [Aka17, Corollary 4.4]).

So: [Aka17] is still the right literature for partial Euler products of \(\zeta\) in the strip, but the **load-bearing theorem is not “off-line zero \(\Rightarrow m\log\log x\) in \(\arg P_x\)”**. The \(m\log\log\)-type factor appears as the **power** \((\log x)^m\) **multiplying** \(\zeta_x(s_0)\) so that a finite nonzero limit can exist at a critical-line zero of order \(m\).

---

## 1. Main theorem (critical line) — line-by-line

The following is the statement as given in Kaneko–Koyama–Kurokawa [KKK, Thm 3.2] and Koyama–Kurokawa [KK, §1], attributed to Akatsuka [Aka17].

### Statement

Define
\[
\zeta_x(s)
:=
\prod_{p\le x}\bigl(1-p^{-s}\bigr)^{-1}.
\]

**Then the following are equivalent:**

**(1)** Let \(\psi(x):=\psi(x,\mathbf{1})\) for the trivial character. Then
\[
\psi(x)
=
x
+
o\bigl(\sqrt{x}\,\log x\bigr)
\qquad(x\to\infty).
\]

**(2)** There exists \(\tau\in\mathbb{R}\) such that
\[
\lim_{x\to\infty}
\frac
{(\log x)^{m}\,\zeta_x(s)}
{\displaystyle
\exp\!\Biggl(
\lim_{\varepsilon\downarrow 0}
\Biggl(
\int_{1+\varepsilon}^{x}
\frac{du}{u^{s}\log u}
-
\log\frac{1}{\varepsilon}
\Biggr)
\Biggr)
}
\]
converges to a **nonzero** value, where \(s=\tfrac12+i\tau\) and \(m\) is the order of vanishing of \(\zeta(s)\) at this point \(s=\tfrac12+i\tau\).

**(3)** The same limit exists and is nonzero **for every** \(\tau\in\mathbb{R}\).

**If** these conditions hold, then the **Riemann hypothesis holds**, and the limit in (2)–(3) equals
\[
\frac{(s-1)\,\zeta^{(m)}(s)}{e^{(m-1)\gamma}\,m!}
\times
\begin{cases}
\sqrt{2} & \text{if }\tau=0,\\
1 & \text{otherwise},
\end{cases}
\]
with \(\gamma\) the Euler–Mascheroni constant (form as in [KKK, Thm 3.2]; \(\tau=0\) case picks up the \(\sqrt{2}\) factor familiar from Goldfeld–Conrad).

### Line-by-line reading

| Piece | Meaning |
|-------|---------|
| \(\zeta_x(s)=P_x(s)\) | Exactly L1’s partial product. |
| (1) \(\psi(x)=x+o(\sqrt{x}\log x)\) | **Stronger** than RH’s classical \(\psi(x)=x+O(\sqrt{x}(\log x)^2)\). This is a **Deep RH**–scale error term. |
| (2) renormalizer \(\exp(\cdots)\) | Subtracts the **pole contribution** of \(\zeta\) at \(s=1\) as felt along the integral \(\int du/(u^s\log u)\). Without it, \(\zeta_x(s)\) cannot settle on the critical line because of the pole at \(s=1\). |
| \((\log x)^m\) | Compensates a zero of **order \(m\)** of \(\zeta\) at \(s=\tfrac12+i\tau\). This is the precise place \(m\) and \(\log\log\)-scale logarithms enter: if the renormalized \(\zeta_x\) stayed order \(1\), then \(\zeta_x\sim c/(\log x)^m\), so \(\log\zeta_x\sim -m\log\log x+\log c\). |
| “converges to nonzero” | DRH-type statement for \(\zeta\): a finite nonzero limiting value of the renormalized partial product at that critical-line point. |
| “\(\Rightarrow\) RH” | The DRH-scale condition implies RH (standard Conrad/DRH logic). MathSciNet note: DRH is **stronger** than RH; the review that called it “equivalent to RH” is **misleading** ([KK, footnote]). |
| \(\sqrt{2}\) at \(\tau=0\) | Second-moment / Goldfeld–Conrad factor on the central line. |

### Match to schematic (★)?

If the limit in (2) is a nonzero constant \(C\), then along the critical line at a zero of order \(m\),
\begin{equation}
\label{eq:star-line}
\zeta_x\bigl(\tfrac12+i\tau\bigr)
\sim
C
\cdot
\frac
{\displaystyle
\exp\!\Bigl(\text{pole renormalizer}\Bigr)
}
{(\log x)^{m}}
\qquad(x\to\infty).
\tag{★★}
\end{equation}
Taking logarithms,
\begin{equation}
\label{eq:log-line}
\log\zeta_x\bigl(\tfrac12+i\tau\bigr)
=
-m\log\log x
+
\log C
+
\text{(pole renormalizer)}
+
o(1).
\tag{★★★}
\end{equation}

**Comparison with (★):**

| (★) as previously written | Actual Akatsuka (critical line) |
|---------------------------|----------------------------------|
| Off-line zero \(\beta=Y>1/2\) | **On-line** zero \(s=\tfrac12+i\tau\) |
| Main term \(+m\log\log x\) in \(\log P_x\) | Main term **\(-m\log\log x\)** in \(\log\zeta_x\) after renormalization (product \(\sim(\log x)^{-m}\)) |
| No pole renormalizer | **Essential** pole integral in the denominator’s exponential |
| Claimed for \(\arg\) growth off-line | Statement is about a **complex limit** of a renormalized product; \(\arg\) is the argument of that limit’s approach |

So (★) should be **replaced** by (★★)–(★★★) when citing [Aka17].

---

## 2. Corollary 4.4 style product (critical line, no zero factor)

From Akatsuka’s later paper [Aka24, Remark 1.1], citing [Aka17, Corollary 4.4]:

Define
\[
E_2(X)
=
\frac
{\displaystyle\prod_{p\le X}(1-p^{-1/2})^{-1}}
{\exp\bigl[\mathrm{li}(X^{1/2})\bigr]}.
\]
Then
\[
E_2(X)\to -\sqrt{2}\,\zeta\bigl(\tfrac12\bigr)
\quad\text{as }X\to\infty
\]
is **equivalent** to
\[
\psi(X)=X+o\bigl(X^{1/2}\log X\bigr).
\]
(Compare RH \(\Leftrightarrow\psi(X)=X+O(X^{1/2}(\log X)^2)\).)

A related function with \(\vartheta\) instead of \(X\) appears as \(E_1(X)\) in [Aka24, Thm 3]: boundedness / convergence of \(E_1\) is **equivalent to RH** (not merely to DRH).

**Line-by-line:**

| Object | Role |
|--------|------|
| Numerator \(\prod(1-p^{-1/2})^{-1}\) | \(\zeta_X(1/2)=P_X(1/2)\) |
| Denominator \(\exp(\mathrm{li}(X^{1/2}))\) or \(\exp(\mathrm{li}(\vartheta(X)^{1/2}))\) | Removes prime-sum growth expected on the critical line |
| Limit \(-\sqrt{2}\zeta(1/2)\) | Explicit constant (Ramanujan / Goldfeld \(\sqrt{2}\)) |

This is **modulus/renormalized product** control on the line, not off-line \(\arg\) growth.

---

## 3. Theorem 2 of [Aka17] (zero-free half-plane) — abstract-level extract

From the Project Euclid article page text for [Aka17]:

> In Theorem 2 the asymptotic behavior of the partial Euler product is equivalent [to] \(\zeta(s)\) [being] zero-free in \(\operatorname{Re}(s)>s_0\), which is different from Theorem 1 …

**Programme reading (not a substitute for the PDF):**  
[Aka17, Thm 2] links a **partial-product asymptotic** at a real (or complex) height to **zero-freeness to the right of a vertical line**. That is the closest formal neighbour of “off-line zeros force product pathology,” but it is stated as an **equivalence with zero-free regions**, not as the target lemma’s \(\lvert A_X\rvert\ge c\,m\log\log X\).

**Action item:** when full PDF access is available, copy Theorem 1 and Theorem 2 **verbatim** into an appendix of this file (page numbers 79–101).

---

## 4. Related \(\Omega\)-estimate when zeros sit to the right (Akatsuka 2024)

Not identical to [Aka17], but the same author, and it makes the zero \(\Rightarrow\) product pathology direction explicit for **real** \(\kappa\in[1/2,1)\).

**Proposition 7.1 [Aka24].**  
Let \(\kappa\in[1/2,1)\). Assume there is a zero of \(\zeta(s)\) in \(\operatorname{Re}(s)>\kappa\). Let
\[
\Theta=\sup\{\operatorname{Re}\rho:\zeta(\rho)=0\}.
\]
Then for every \(\delta>0\),
\begin{equation}
\sum_{2\le n\le X}
\frac{\Lambda(n)}{n^{\kappa}\log n}
-
\mathrm{li}(X^{1-\kappa})
-
\frac{\psi(X)-X}{X^{\kappa}\log X}
=
\Omega_{+}\!\bigl(X^{\Theta-\kappa-\delta}\bigr)
\quad(X\to\infty).
\tag{Ω}
\end{equation}

**Connection to \(\log P_X(\kappa)\):**  
[Aka24, Lemma 4.1 / §4] writes the logarithm of the partial Euler product at real \(\kappa\) in terms of \(\sum\Lambda(n)/(n^{\kappa}\log n)\). Thus (Ω) is an **unbounded oscillation** statement for the **real** logarithm of the product (modulus scale), when zeros lie to the right of \(\kappa\).

**Match to target lemma:**

| Target lemma needs | (Ω) gives |
|--------------------|-----------|
| Off-line zero of maximal abscissa | Yes: \(\Theta>\kappa\) |
| Lower bound \(\gg m\log\log X\) for \(\lvert A_X\rvert\) (argument) | **No** — this is \(\Omega_+\) for a **real** weighted prime sum / \(\log\lvert P\rvert\)-scale object |
| Multiplicity \(m\) explicit | Appears in intermediate lemmas (e.g. local analysis of \(\zeta'/\zeta\) near \(\rho\)) but the displayed (Ω) is in \(\Theta-\kappa\), not \(m\log\log\) |

---

## 5. What this means for our Conjectures A/B and target lemma

### 5.1 What [Aka17] **does** give the programme

1. **Precise definition** of \(\zeta_x=P_x\) matching L1.  
2. **Critical-line** renormalized asymptotics (★★)–(★★★): zeros of order \(m\) force a factor \((\log x)^{-m}\) in a suitably renormalized product.  
3. **DRH-scale** prime error \(\Leftrightarrow\) product limit (stronger than RH).  
4. Philosophical support: partial Euler products of \(\zeta\) in the strip are a legitimate analytic object with deep links to zeros (Conrad–Goldfeld–Akatsuka line).

### 5.2 What [Aka17] does **not** give (gaps for the target lemma)

1. A ready-made theorem  
   \(\lvert A_X(\beta,\gamma)\rvert\ge c\,m\log\log X\)  
   at an off-line zero \(\beta+i\gamma\) with \(\beta=Y>1/2\).  
2. Automatic passage from real \(m\log\log\) (or \((\log x)^{-m}\)) to **argument** \(A_X\) (same issue as M1–M3 in the sketch note).  
3. An unconditional off-line growth theorem free of DRH-scale hypotheses.

### 5.3 Revised (★) for programme use

**Replace old (★) by:**

**Critical-line form (from [Aka17] via [KKK]/**  
If the DRH-type limit exists at a zero \(s_0=\tfrac12+i\tau\) of order \(m\), then
\[
\log\zeta_x(s_0)
=
-m\log\log x
+
R_{\mathrm{pole}}(x,s_0)
+
\log C
+
o(1),
\tag{★\(_\mathrm{line}\)}
\]
with \(R_{\mathrm{pole}}\) the explicit pole renormalizer of [Aka17].

**Off-line form (not a quote of [Aka17]; open):**  
If \(\rho=\beta+i\gamma\) has \(\beta=Y>1/2\) and order \(m\), prove either  
- a modulus statement \(\log\lvert P_x(\rho)\rvert=\Omega(m\log\log x)\) or \(\Omega(x^{\beta-1/2-\varepsilon})\), **or**  
- the target lemma for \(\lvert A_X(\beta,\gamma)\rvert\),  
using explicit formulae + [Aka24, Prop. 7.1]-style \(\Omega\) methods extended to complex \(s\).

---

## 6. Line-by-line checklist for the full PDF (when available)

Copy into an appendix with page numbers:

- [ ] Definition of \(\zeta_x(s)\) / partial product  
- [ ] Theorem 1 (statement + hypotheses)  
- [ ] Theorem 2 (zero-free equivalence — exact statement)  
- [ ] Theorem 3 / main critical-line equivalence  
- [ ] Corollary 4.4 (\(E_2\) / \(\psi\) equivalence)  
- [ ] Any lemma relating \(\log\zeta_x\) to \(\sum\Lambda(n)n^{-s}/\log n\)  
- [ ] Any explicit formula section (§3 in Project Euclid TOC snippet)  
- [ ] Error terms: ranges of \(\sigma\), \(t\), \(x\)

---

## 7. Immediate pure-math tasks after this extract

1. **O1′ (revised):** Work from (★\(_\mathrm{line}\)) and Conrad’s product \(\Rightarrow\) RH theorems; do **not** claim off-line (★) as Akatsuka.  
2. **O2:** Build M1 for **argument** using explicit formulae (Titchmarsh/Davenport), optionally guided by [Aka24, §4, §7] real-\(\kappa\) methods.  
3. **O3:** Smoothing \(\theta_x\to A_X\).  
4. Obtain full [Aka17] PDF and fill the checklist in §6.

---

## One-liner

**Akatsuka (2017) equates a DRH-scale prime error to a renormalized critical-line limit of \((\log x)^m\zeta_x(\tfrac12+i\tau)\); that is the exact \(m\log\log\) mechanism (as \((\log x)^{-m}\) in the product), not an off-line argument bound — the target lemma for \(A_X\) at \(Y>1/2\) remains open and must be proved separately.**

*Per aspera ad astra.*
