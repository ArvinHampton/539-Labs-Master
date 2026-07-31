# M1.2 — Remainder bound strategy, zero sums, and lemma sketch

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A** only — no model constants.  
**RH:** open; workstream active.  
**Goal:** written statement of **M1.2** with explicit error-term shape (possibly conditional on zero-density / height range), plus an implementation sketch.

**Companions:**  
`RH_M1_Explicit_Formula_Remainder.md` (named \(R_{\mathrm{IvM}}\), \(\mathcal{R}_x^{\mathrm{EP}}\)),  
`RH_O1_Akatsuka_M1_Package.md`,  
`RH_L1_Phase_Functional_CatA.md`.  
**Probe:** `scripts/rh_M1_2_remainder_diagnostic.py` → `rh_M1_2_remainder_diagnostic_results.json`.

---

## 1. Goal of M1.2

Bound the imaginary part of the Euler-product remainder so that continuous \(\theta_x(s)=\arg P_x(s)\) (or smoothed \(A_X\)) is forced by the **local zero contribution** \(m\arg(s-\rho)\), not by uncontrolled oscillation in the remainder.

### 1.1 Split (M1-EP)

\[
\log\zeta(s)
=
\log P_x(s)
+
\mathcal{R}_x^{\mathrm{EP}}(s),
\]
with \(P_x(s)=\prod_{p\le x}(1-p^{-s})^{-1}\) and \(\mathcal{R}_x^{\mathrm{EP}}\) as in `RH_M1_Explicit_Formula_Remainder.md` (path-integrated Ingham–von Mangoldt remainder minus \(E_x^{\mathrm{pow}}\)).

Continuous imaginary parts (branches fixed as in L1 / M1):
\begin{equation}
\theta_x(s)
=
\arg P_x(s)
=
\arg\zeta(s)
-
\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}(s).
\tag{M1.2-split}
\end{equation}

Near a zero \(\rho=\beta+i\gamma\) of multiplicity \(m\),
\begin{equation}
\theta_x(s)
=
m\arg(s-\rho)
-
\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}(s)
+
\operatorname{Im} H_\rho(s),
\tag{M1.2-local}
\end{equation}
with \(H_\rho\) holomorphic and non-vanishing at \(\rho\).

### 1.2 Target inequality (M1.2)

**M1.2 (working form).**  
There exist absolute \(c_0\in(0,1)\) and a height range / density hypothesis (stated below) such that: for a zero \(\rho=\beta+i\gamma\) of multiplicity \(m\ge 1\) with \(\beta=Y:=\sup\operatorname{Re}\rho'\) (or, diagnostically, a numerical off-line local minimum of \(\lvert\zeta\rvert\) with \(\sigma\ge 0.60\)), there is a truncation \(x=x(\gamma)\) and a path \(\gamma_{\mathrm{path}}\) in a small disk about \(\rho\) on which
\begin{equation}
\boxed{
\sup_{s\in\gamma_{\mathrm{path}}}
\bigl\lvert\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}(s)\bigr\rvert
\le
c_0\,m\cdot
\sup_{s\in\gamma_{\mathrm{path}}}
\lvert\arg(s-\rho)\rvert
}
\tag{M1.2}
\end{equation}
(or the weaker form \(\le \tfrac12 m\log\log x\) when the path is designed so that \(\sup\lvert\arg(s-\rho)\rvert\ge\log\log x\)).

If (M1.2) holds and \(\sup\lvert\arg(s-\rho)\rvert\ge\pi\) (semicircle about \(\rho\)), then \(\theta_x\) changes by at least \((1-c_0)m\pi\) along the path, giving a lower bound of target-lemma type after smoothing (M1.3–M1.4).

**Status of (M1.2):** **open** as a completed theorem; this note freezes the **strategy and error-term bookkeeping**.

---

## 2. Strategy outline

1. **Local isolation.** Fixed-height disk/rectangle containing at most one zero of maximal real part \(Y\) (or one diagnostic minimum). Radius \(r\asymp 1/\log\gamma\).  
2. **Truncation.** Choose \(x\) large relative to \(\lvert t\rvert\) so the prime-power tail after \(x\) is small for \(\sigma\) in the right half-strip.  
3. **Contour move.** Explicit formula for \(-\zeta'/\zeta\) or path-integrated \(\log\zeta\); pick up residues at zeros.  
4. **Isolate local factor.** Peel \(m/(s-\rho)\) or \(m\log(s-\rho)\); put all other zeros into the remainder.  
5. **Bound integrals.** Horizontal/vertical integrals after shifting → bulk of \(\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}\).  
6. **Path design (M1.3).** Angular sector / arc about \(\rho\) making \(m\arg(s-\rho)\) large while remainder stays \(O(1)\) or \(o(\log\log x)\).  
7. **Smoothing (M1.4).** Transfer to \(A_X\) via slow variation on \([X,X^2]\).

---

## 3. Explicit-formula zero sums (classical engine)

### 3.1 von Mangoldt explicit formula

\[
\psi_0(x)
=
x
-
\sum_{\rho}\frac{x^{\rho}}{\rho}
-
\log(2\pi)
-
\frac12\log(1-x^{-2}),
\]
(sum over nontrivial zeros with multiplicity; \(\psi_0\) the usual symmetric Chebyshev function). Controls prime-power sums after differentiation / partial summation.

### 3.2 Logarithmic derivative (Hadamard / partial fractions)

\[
\frac{\zeta'}{\zeta}(s)
=
B
-
\frac{1}{s-1}
+
\frac12\log\pi
-
\frac12\frac{\Gamma'}{\Gamma}\Bigl(\frac s2+1\Bigr)
+
\sum_{\rho}\Bigl(\frac{1}{s-\rho}+\frac{1}{\rho}\Bigr).
\]
Path integration yields \(\log\zeta(s)\). Truncating the Euler product at \(x\) and rearranging is the hybrid representation underlying M1.

### 3.3 IvM truncated form (named remainder already in M1)

\[
\frac{\zeta'}{\zeta}(s)
=
-
\sum_{n<x}\frac{\Lambda(n)}{n^{s}}
+
\frac{x^{1-s}}{1-s}
-
\sum_{\lvert\Im\rho\rvert\le T}
\frac{x^{\rho-s}}{\rho-s}
+
R_{\mathrm{IvM}}(s;x,T).
\tag{IvM}
\]
\(R_{\mathrm{IvM}}\) = **Ingham–von Mangoldt remainder** (Davenport Ch. 17; Titchmarsh §9.6).

### 3.4 Smoothed / GHK-type errors

Smoothed hybrids (Gonek–Hughes–Keating and relatives) give error shapes of the form
\[
O\Biggl(\frac{X^{K+2}}{(\lvert s\rvert\log X)^{K}}\Biggr)
+
O\bigl(X^{-\sigma}\log X\bigr)
\]
for fixed \(K\), away from poles/zeros already accounted for. Useful for \(A_X\) (width \(\asymp 1/\log X\)).

### 3.5 Akatsuka specialisation (O1)

On the critical line, [Aka17] gives the **renormalized** limit package (O1-A)/(O1-A-log): factor \((\log x)^{-m}\) after pole renormalizer \(R_{\mathrm{pole}}\). That mass is essentially **real** (modulus). Argument growth off the line is **not** given by Akatsuka; it must come from \(\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}\) control + path design (this note).

### 3.6 Zero-density / \(N(T)\)

Standard \(N(T)\sim(T/2\pi)\log(T/2\pi)\) and zero-density estimates bound how many zeros can sit in a height window and feed the distant-zero sum
\[
\sum_{\rho'\notin D}\frac{1}{\lvert s-\rho'\rvert}.
\]

---

## 4. Decomposition of \(\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}\)

Write, for \(s\) near \(\rho\) with \(\lvert\Im s\rvert\le T\) and truncation \(x\),
\begin{equation}
\begin{aligned}
\mathcal{R}_x^{\mathrm{EP}}(s)
&=
\underbrace{m\log(s-\rho)-\log\zeta(s)+H_\rho^{\mathrm{reg}}(s)}_{\text{local zero cancelled into structure}}
\\
&\quad
+
\underbrace{
\sum_{\substack{\lvert\Im\rho'\rvert\le T\\ \rho'\neq\rho}}
I_x(s;\rho')
}_{Z_{\mathrm{far}}(s;x,T)}
+
\underbrace{
\int_{\Gamma}R_{\mathrm{IvM}}(w;x,T)\,dw
}_{I_{\mathrm{IvM}}(s;x,T)}
\\
&\quad
+
\underbrace{
\int_{\Gamma}\frac{x^{1-w}}{1-w}\,dw
-
R_{\mathrm{pole}}^{\mathrm{norm}}(s;x)
}_{P_{\mathrm{arch}}(s;x)}
-
E_x^{\mathrm{pow}}(s)
+
O(x^{-\sigma}).
\end{aligned}
\tag{M1.2-dec}
\end{equation}
Here \(I_x(s;\rho')\) denotes the path-integrated term \(x^{\rho'-w}/(\rho'-w)\) from (IvM), and \(R_{\mathrm{pole}}^{\mathrm{norm}}\) is any fixed normalization of the pole contribution (cf. O1-pole on the line).

**M1.2 reduces to bounding**
\[
\bigl\lvert\operatorname{Im} Z_{\mathrm{far}}\bigr\rvert
+
\bigl\lvert\operatorname{Im} I_{\mathrm{IvM}}\bigr\rvert
+
\bigl\lvert\operatorname{Im} P_{\mathrm{arch}}\bigr\rvert
+
\bigl\lvert\operatorname{Im} E_x^{\mathrm{pow}}\bigr\rvert.
\]

### 4.1 Elementary prime-power tail

For \(\sigma\ge\sigma_0>0\),
\[
\bigl\lvert E_x^{\mathrm{pow}}(s)\bigr\rvert
\ll_{\sigma_0}
\frac{x^{1-\sigma_0}}{\log x}
\quad\text{(M1)}.
\]
**Uniform on compacta in \(\operatorname{Re}s\ge\sigma_0\).** Negligible vs \(\log\log x\) once \(x\to\infty\).

### 4.2 Distant zeros \(Z_{\mathrm{far}}\)

On a disk \(D=D(\rho,r)\) with \(r\asymp 1/\log\gamma\) containing no other zeros,
\[
\sum_{\rho'\notin D}
\Bigl\lvert\operatorname{Im}\frac{1}{s-\rho'}\Bigr\rvert
\le
\sum_{\rho'\notin D}
\frac{1}{\lvert s-\rho'\rvert}
\qquad(s\in D).
\]
**Average** size \(O(\log\gamma)\) is classical; **pointwise** \(O(1)\) or \(o(\log\log x)\) after removing a sparse set of bad heights is standard zero-density technology (Montgomery / Huxley type — **hypothesis package HD** below).

### 4.3 IvM contour remainder \(I_{\mathrm{IvM}}\)

Under the **Davenport range** \(2\le x\le t^{2}\), \(T\asymp x\), the reference bound (IvM-bd) in M1 gives
\[
R_{\mathrm{IvM}}(s;x,T)
\ll_{\sigma_0}
\frac{x^{1-\sigma}\log(xt)}{\lvert t\rvert}
+
\frac{\log^{2}(xt)}{T}
+
\cdots
\]
Path length \(O(1+\lvert t\rvert)\) multiplies; parameters must be tuned so \(\operatorname{Im} I_{\mathrm{IvM}}=o(\log\log x)\) on the path.

### 4.4 Archimedean / pole piece \(P_{\mathrm{arch}}\)

On the critical line this is essentially Akatsuka’s \(R_{\mathrm{pole}}\) (slowly varying in \(x\)). Off the line it remains **smooth in \(s\)** on \(D\) once the pole at \(s=1\) is far; bound \(O(1)\) or \(O(\log\log x)\) depending on normalization — must stay below the main \(m\arg\) term.

---

## 5. Formal lemma sketch (conditional)

### Hypothesis package **HD** (height / density)

Either:

- **(HD-low)** \(\lvert\gamma\rvert\le T_0\) with \(T_0\) fixed and all zeros in \(\lvert t\rvert\le T_0+2\) verified by existing tables (Odlyzko et al.), **or**  
- **(HD-dens)** a zero-density estimate of the form \(N(\sigma,T)\ll T^{a(1-\sigma)}\log^{b} T\) for \(\sigma\ge \sigma_1>1/2\), sufficient to bound \(Z_{\mathrm{far}}\) by \(o(\log\log x)\) outside a set of measure \(o(T)\) in height.

### Truncation package **TR**

\[
x
=
\gamma^{\theta}
\quad\text{or}\quad
x
=
\exp\Bigl(c\frac{\log\gamma}{\log\log\gamma}\Bigr),
\qquad
\theta\in(0,1),\ c>0
\]
to be optimised; \(T=x\) or \(T=\gamma\).

### Lemma M1.2 (conditional sketch)

**Assume HD and TR.** Let \(\rho=\beta+i\gamma\) be a zero of multiplicity \(m\) with \(\beta=Y\), and let \(D=D(\rho,r)\) with \(r=c_r/\log\gamma\) contain no other zeros. Then there exist \(c_0\in(0,1)\) and a path \(\gamma_{\mathrm{path}}\subset D\) from a base point with \(\arg(s-\rho)=0\) to a point with \(\arg(s-\rho)=\pi\) such that
\[
\sup_{s\in\gamma_{\mathrm{path}}}
\bigl\lvert\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}(s)\bigr\rvert
\le
c_0\,m\pi
\]
for all sufficiently large \(\gamma\) (under HD-dens) or for all tabulated \(\rho\) with \(\lvert\gamma\rvert\le T_0\) (under HD-low).

**Corollary (feeds target lemma).**  
Along that path, \(\lvert\Delta\theta_x\rvert\ge (1-c_0)m\pi\). After smoothing (M1.4) one obtains a sequence with \(\lvert A_{X_n}(\beta,\gamma)\rvert\gg m\) (or \(\gg m\log\log X_n\) if the path/geometry is strengthened).

**Proof obligations still open:** uniform bound on \(Z_{\mathrm{far}}+I_{\mathrm{IvM}}+P_{\mathrm{arch}}\) on \(\gamma_{\mathrm{path}}\); construction of \(\gamma_{\mathrm{path}}\) (M1.3).

---

## 6. Implementation sketch

### Step A — Local isolation

- Analytic: disk radius \(r\asymp 1/\log\gamma\).  
- Numeric (low height): take Odlyzko zero or L5 off-line \(\lvert\zeta\rvert\) minimum with \(\sigma\ge 0.60\); verify no other zero in a small box by grid + known spacing.

### Step B — Truncation

- Set \(x=\min(x_{\max},\gamma^{\theta})\) with \(\theta\in\{0.5,0.75,1\}\) in probes.  
- Compute \(P_x(s)\) and \(\theta_x(s)\) as in L5 (mpmath, dps scaled with \(\lvert t\rvert\)).

### Step C — Explicit remainder (numeric definition)

\[
\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}(s)
:=
\operatorname{Im}\bigl(\log\zeta(s)-\log P_x(s)\bigr)
\]
with continuous branches: \(\log\zeta\) via mpmath log along a short path from a base point with \(\operatorname{Re}>1\); \(\log P_x\) via L1 prime path.

**This is the diagnostic stand-in for the full IvM expansion** at low height (where direct \(\zeta\) is reliable).

### Step D — Path design (numeric M1.3)

- Circular arc \(s=\rho+\varepsilon e^{i\alpha}\), \(\alpha:0\to\pi\), \(\varepsilon=r/2\).  
- Sample \(N_{\mathrm{arc}}\) points; record \(\theta_x\), \(\operatorname{Im}\mathcal{R}\), \(m\arg(s-\rho)\).  
- Check whether \(\sup\lvert\operatorname{Im}\mathcal{R}\rvert\le \tfrac12 m\pi\).

### Step E — Smoothing

- As in L5: \(A_X=\int_1^2\theta_{X^v}\phi(v)\,dv\).  
- Compare \(\lvert A_X\rvert\) to \(\sup\lvert\operatorname{Im}\mathcal{R}\rvert\) on the arc.

### Logical chain

```text
Explicit formula / Hadamard
  → hybrid Euler–Hadamard (M1-EP)
  → isolate m log(s-ρ)
  → bound Im R_x^EP          (M1.2)  ← this note
  → path with m arg dominates (M1.3)
  → lower bound θ_x, A_X
  → target lemma
  → (+ FE + zero-free near Re=1) RH strategy
```

---

## 7. Numerical probe (diagnostic only)

**Script:** `scripts/rh_M1_2_remainder_diagnostic.py`

| Check | Meaning |
|-------|---------|
| \(\sup\lvert\operatorname{Im}\mathcal{R}\rvert\) on arc about first zeros | size of remainder vs \(m\pi\) |
| same about L5-style off-line \(\lvert\zeta\rvert\) minima | off-line diagnostic |
| \(\sup\lvert\operatorname{Im}\mathcal{R}\rvert / \sup\lvert m\arg(s-\rho)\rvert\) | ratio; want \(<c_0<1\) |
| **Never** claim RH or claim M1.2 proved |

---

## 8. Error-term ledger (names fixed)

| Symbol | Meaning |
|--------|---------|
| \(R_{\mathrm{IvM}}(s;x,T)\) | Ingham–von Mangoldt truncated remainder |
| \(\mathcal{R}_x^{\mathrm{EP}}(s)\) | Euler–explicit remainder (M1) |
| \(Z_{\mathrm{far}}\) | distant zero sum |
| \(I_{\mathrm{IvM}}\) | path integral of \(R_{\mathrm{IvM}}\) |
| \(P_{\mathrm{arch}}\) | pole / archimedean integrated term |
| \(E_x^{\mathrm{pow}}\) | prime-power discrepancy \(\log P_x-L_x^{\Lambda}\) |
| \(R_{\mathrm{pole}}\) | Akatsuka pole renormalizer (critical line, O1) |
| **HD** | height/density hypothesis package |
| **TR** | truncation package |

---

## 9. Status

| Item | Status |
|------|--------|
| Strategy + decomposition (M1.2-dec) | **Written** |
| Conditional lemma sketch | **Written** (not proved) |
| Numeric diagnostic | **Implemented** |
| Full proof of (M1.2) | **Open** |
| Target lemma / RH | **Open** |

---

## One-liner

**M1.2 is the bound \(\lvert\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}\rvert\ll m\lvert\arg(s-\rho)\rvert\) near an off-line zero, obtained by isolating the local Hadamard factor in the IvM explicit formula and controlling distant zeros, contour integrals, and the prime-power tail; the open work is uniform control of that remainder on a path that makes \(m\arg(s-\rho)\) large.**

*Per aspera ad astra.*
