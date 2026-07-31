# M1 — Explicit-formula remainder for \(\log\zeta\), \(P_x\), and \(\arg P_x\)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A** only — no model constants.  
**RH:** open; workstream active.  
**Role:** Mechanism **M1** from `RH_Target_Lemma_Sketch_Literature_L5.md`: pass from zero structure to continuous argument \(\theta_x\) / smoothed \(A_X\) via a **named** remainder.

**Companions:** `RH_L1_Phase_Functional_CatA.md`, `RH_Akatsuka_Theorem_Extract.md`.

**Standard references for named formulae:**  
Davenport, *Multiplicative Number Theory* (3rd ed.), Ch. 17;  
Titchmarsh, *The Theory of the Riemann Zeta-Function* (2nd ed., Heath-Brown), Ch. IX;  
Ivić, *The Riemann Zeta-Function*, Ch. 12;  
Ingham, *The Distribution of Prime Numbers*.

---

## 0. Goal of M1

Write a rigorous **identity**
\[
\log\zeta(s)
=
\log P_x(s)
+
\mathcal{R}_x(s)
\]
(meromorphic, on a fixed branch off the zeros and the pole), with \(\mathcal{R}_x\) expressed through a **named explicit-formula remainder**, so that:

1. \(\log P_x = L_x^{\mathrm{EP}}\) is elementary (primes \(\le x\));  
2. zeros of \(\zeta\) appear only inside \(\mathcal{R}_x\) (or in a principal Hadamard term moved into \(\mathcal{R}_x\));  
3. \(\theta_x=\arg P_x=\operatorname{Im}\log P_x\) is isolated;  
4. growth of \(\lvert\theta_x\rvert\) or \(\lvert A_X\rvert\) can be attacked by estimating \(\mathcal{R}_x\).

**This note defines the split and the remainder. It does not claim the target lemma is proved.**

---

## 1. Elementary partial products and prime sums

### 1.1 Euler partial product (L1)

For \(x\ge 2\) and \(s\in\mathbb{C}\),
\[
P_x(s)
=
\prod_{p\le x}(1-p^{-s})^{-1},
\qquad
\log P_x(s)
=
\sum_{p\le x}\sum_{k\ge 1}\frac{p^{-ks}}{k}
=
\sum_{\substack{n=p^k\\ p\le x}}\frac{\Lambda(n)}{n^{s}\log n}.
\]
(The inner sum runs over all powers of primes \(p\le x\), including \(p^k>x\).)  
\(P_x(s)\neq 0\) for all finite \(x\); \(\log P_x\) is entire in \(s\).

### 1.2 Truncated von Mangoldt Dirichlet series

\[
L_x^{\Lambda}(s)
:=
\sum_{n\le x}\frac{\Lambda(n)}{n^{s}\log n}.
\]
Difference from \(\log P_x\):
\begin{equation}
\label{eq:EP-vs-Lambda}
\log P_x(s)
-
L_x^{\Lambda}(s)
=
\sum_{p\le x}\sum_{\substack{k\ge 1\\ p^k>x}}\frac{p^{-ks}}{k}
=
:
E_x^{\mathrm{pow}}(s).
\end{equation}
For \(\sigma=\operatorname{Re}s\ge \sigma_0>0\) and \(x\ge 2\),
\[
\bigl|E_x^{\mathrm{pow}}(s)\bigr|
\le
\sum_{p\le x}\sum_{k>\log x/\log p}\frac{p^{-k\sigma_0}}{k}
\ll_{\sigma_0}
x^{-\sigma_0}\frac{\pi(x)}{\log x}
+
\sum_{p\le\sqrt{x}}\frac{p^{-\sigma_0\lfloor\log x/\log p\rfloor}}{1-p^{-\sigma_0}}
\ll_{\sigma_0}
\frac{x^{1-\sigma_0}}{\log x}
\]
(standard bound; any \(\sigma_0>0\)).  
Thus on compact sets in \(\operatorname{Re}s\ge\sigma_0>0\), \(E_x^{\mathrm{pow}}\to 0\) as \(x\to\infty\), and for fixed \(x\) it is holomorphic and small compared to main terms of size \(\log\log x\).

**Convention.** For M1 we work primarily with \(L_x^{\Lambda}\); transferring estimates to \(\log P_x\) costs only \(E_x^{\mathrm{pow}}\).

---

## 2. Named kernel: the truncated explicit formula for \(\zeta'/\zeta\)

### 2.1 Statement (Ingham–von Mangoldt truncated form)

We use the following **named** formula (standard truncated explicit formula for \(\zeta'/\zeta\); cf. Davenport, Ch. 17; Titchmarsh §9.6; Ivić §12.1).

**Theorem (IvM truncated formula).**  
Let \(s=\sigma+it\) with \(\sigma\ge \sigma_0>0\), \(\lvert t\rvert\ge 2\), and let parameters \(x\ge 2\), \(T\ge 2\) satisfy \(x\le t^{2}\) (or any fixed power range stated in the reference). Then
\begin{equation}
\label{eq:IvM}
\frac{\zeta'}{\zeta}(s)
=
-
\sum_{n<x}\frac{\Lambda(n)}{n^{s}}
+
\frac{x^{1-s}}{1-s}
-
\sum_{\substack{\rho\\ \lvert\Im\rho\rvert\le T}}
\frac{x^{\rho-s}}{\rho-s}
+
R_{\mathrm{IvM}}(s;x,T),
\tag{IvM}
\end{equation}
where the sum over \(\rho\) runs over nontrivial zeros of \(\zeta\), and the **named remainder**
\[
R_{\mathrm{IvM}}(s;x,T)
\]
is the **Ingham–von Mangoldt remainder**, collecting:

- trivial-zero contributions truncated,  
- horizontal and vertical contour integrals from the proof,  
- the discrepancy between \(\sum_{n<x}\) and a smooth cutoff if used,  
- the error from truncating the zero sum at height \(T\).

### 2.2 Standard size of \(R_{\mathrm{IvM}}\) (reference form)

A usable bound (shape as in Davenport / Titchmarsh; constants absolute or depending only on \(\sigma_0\)) is of the type
\begin{equation}
\label{eq:IvM-bound}
R_{\mathrm{IvM}}(s;x,T)
\ll_{\sigma_0}
\frac{x^{1-\sigma}\log(x\lvert t\rvert)}{\lvert t\rvert}
+
\frac{x^{\sigma_0-\sigma}\log^{2}(xT)}{T}
+
\log^{2}(\lvert t\rvert x)
\cdot
\Bigl(
\frac{x^{-\sigma}}{T}
+
\frac{1}{x^{\sigma}}
\Bigr)
+
\frac{\log x}{x^{\sigma}},
\tag{IvM-bd}
\end{equation}
for \(s\) in a fixed vertical strip \(\sigma_0\le\sigma\le 2\), after adjusting absolute constants and the precise power of logarithms to the edition used.

**Naming.**  
Whenever M1 refers to “the remainder,” it means **\(R_{\mathrm{IvM}}(s;x,T)\)** as in (IvM), with size controlled by (IvM-bd) or any sharper published substitute (e.g. with a smooth weight \(\phi\), **Weil–Guinand explicit formula remainder** \(R_{\mathrm{WG}}(\phi)\) — see §6).

### 2.3 Smooth-weight variant (optional, cleaner for \(A_X\))

Let \(\phi\in C_c^{\infty}((0,\infty))\) with \(\operatorname{supp}\phi\subset[1/X,X]\) or Mellin-transform decay. The **Weil–Guinand explicit formula** reads schematically
\begin{equation}
\label{eq:WG}
\sum_{n\ge 1}\frac{\Lambda(n)}{n^{1/2}}\phi(\log n)
+
\phi_{\mathrm{arch}}
=
\sum_{\rho}\widehat\phi\Bigl(\frac{\rho-\tfrac12}{i}\Bigr)
+
R_{\mathrm{WG}}(\phi),
\tag{WG}
\end{equation}
with **\(R_{\mathrm{WG}}(\phi)\)** the **Weil–Guinand remainder** (often zero for ideal test functions; otherwise controlled by archimedean factors).  
For the RH track, (IvM) is enough to define M1; (WG) is preferred when passing to the smoothed \(A_X\).

---

## 3. Integrated form: logarithm and the M1 remainder \(\mathcal{R}_x\)

### 3.1 From \(\zeta'/\zeta\) to \(\log\zeta\)

Fix a base point \(s_\star\) with \(\operatorname{Re}s_\star>1\) (e.g. \(s_\star=2\)) and a polygonal path \(\Gamma\) from \(s_\star\) to \(s\) that avoids zeros and the pole \(s=1\). Then
\begin{equation}
\label{eq:log-path}
\log\zeta(s)
=
\log\zeta(s_\star)
+
\int_{\Gamma}\frac{\zeta'}{\zeta}(w)\,dw,
\end{equation}
with the continuous branch along \(\Gamma\).

Insert (IvM) under the integral (justified on compact segments away from poles of the summands, then by continuity):
\begin{align}
\log\zeta(s)
&=
\log\zeta(s_\star)
-
\int_{\Gamma}\sum_{n<x}\frac{\Lambda(n)}{n^{w}}\,dw
+
\int_{\Gamma}\frac{x^{1-w}}{1-w}\,dw
-
\sum_{\lvert\Im\rho\rvert\le T}
\int_{\Gamma}\frac{x^{\rho-w}}{\rho-w}\,dw
+
\int_{\Gamma}R_{\mathrm{IvM}}(w;x,T)\,dw.
\label{eq:log-split}
\end{align}

### 3.2 Prime sum vs \(L_x^{\Lambda}\)

For \(\operatorname{Re}w>1\),
\[
\int^{s}\sum_{n<x}\frac{\Lambda(n)}{n^{w}}\,dw
=
\sum_{n<x}\frac{\Lambda(n)}{n^{s}\log n}
-
\sum_{n<x}\frac{\Lambda(n)}{n^{s_\star}\log n}
=
L_x^{\Lambda}(s)
-
L_x^{\Lambda}(s_\star),
\]
and the identity extends by analytic continuation in \(s\) (finite sum).  
Thus
\begin{equation}
\label{eq:M1-identity}
\log\zeta(s)
=
L_x^{\Lambda}(s)
+
\mathcal{R}_{x,T}^{\mathrm{IvM}}(s),
\tag{M1}
\end{equation}
where the **named M1 remainder** is
\begin{equation}
\label{eq:RxT}
\begin{aligned}
\mathcal{R}_{x,T}^{\mathrm{IvM}}(s)
&:=
\log\zeta(s_\star)
-
L_x^{\Lambda}(s_\star)
+
\int_{\Gamma}\frac{x^{1-w}}{1-w}\,dw
-
\sum_{\lvert\Im\rho\rvert\le T}
\int_{\Gamma}\frac{x^{\rho-w}}{\rho-w}\,dw
+
\int_{\Gamma}R_{\mathrm{IvM}}(w;x,T)\,dw.
\end{aligned}
\tag{M1-rem}
\end{equation}

**Definition (M1 remainder for the Euler product).**  
\[
\mathcal{R}_x^{\mathrm{EP}}(s)
:=
\log\zeta(s)
-
\log P_x(s)
=
\mathcal{R}_{x,T}^{\mathrm{IvM}}(s)
-
E_x^{\mathrm{pow}}(s)
+
\bigl(L_x^{\Lambda}(s)-\text{adjustment if }n<x\text{ vs }n\le x\bigr).
\]
Equivalently,
\begin{equation}
\label{eq:EP-split}
\boxed{
\log\zeta(s)
=
\log P_x(s)
+
\mathcal{R}_x^{\mathrm{EP}}(s),
}
\tag{M1-EP}
\end{equation}
with
\[
\mathcal{R}_x^{\mathrm{EP}}(s)
=
\mathcal{R}_{x,T}^{\mathrm{IvM}}(s)
-
E_x^{\mathrm{pow}}(s)
+
O\bigl(x^{-\sigma}\bigr)
\]
(the \(O\) absorbs \(\le\) vs \(<\) conventions).

**Name.** \(\mathcal{R}_x^{\mathrm{EP}}\) is the **Euler–explicit remainder** (partial product form of the Ingham–von Mangoldt remainder after path integration).

### 3.3 Zero principal part

Among terms in \(\mathcal{R}_{x,T}^{\mathrm{IvM}}\), isolate a single zero \(\rho_0=\beta+i\gamma\) of multiplicity \(m\):
\begin{equation}
\label{eq:zero-piece}
Z_{x,T}(s;\rho_0)
=
-
m\int_{\Gamma}\frac{x^{\rho_0-w}}{\rho_0-w}\,dw
=
-
m\int_{\Gamma}x^{\rho_0-w}\,d\log(\rho_0-w)^{-1},
\end{equation}
so that if \(\Gamma\) ends at \(s\) near \(\rho_0\),
\[
Z_{x,T}(s;\rho_0)
=
m\log(s-\rho_0)
+
m(\rho_0-s)\log x\cdot F(x,s,\rho_0)
+
\cdots
\]
(the exact elementary antiderivative of \(x^{\rho-w}/(\rho-w)\) is standard: involving the incomplete exponential integral / \(x^{\rho-s}\) factors).

Thus near \(\rho_0\),
\begin{equation}
\label{eq:near-zero}
\log\zeta(s)
=
m\log(s-\rho_0)
+
H_{\rho_0}(s)
=
\log P_x(s)
+
\mathcal{R}_x^{\mathrm{EP}}(s),
\end{equation}
with \(H_{\rho_0}\) holomorphic and non-vanishing at \(\rho_0\).

**Structural identity for M1:**
\begin{equation}
\label{eq:M1-structure}
\log P_x(s)
=
m\log(s-\rho_0)
+
H_{\rho_0}(s)
-
\mathcal{R}_x^{\mathrm{EP}}(s).
\tag{M1-struct}
\end{equation}

---

## 4. Continuous argument \(\theta_x\) from M1

### 4.1 Definition (consistent with L1)

\[
\theta_x(\sigma,t)
=
\operatorname{Im}\log P_x(\sigma+it)
\]
along the continuous prime-by-prime branch of L1 (equivalently \(\operatorname{Im}\) of the continuous integral of \(\partial_s\log P_x\)).

### 4.2 Argument split

From (M1-EP), off zeros of \(\zeta\) and for a continuous branch of \(\log\zeta\),
\begin{equation}
\label{eq:arg-split}
\theta_x(\sigma,t)
=
\operatorname{Im}\log\zeta(\sigma+it)
-
\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}(\sigma+it).
\end{equation}
At a point **near** a zero \(\rho_0=\beta+i\gamma\), using (M1-struct),
\begin{equation}
\label{eq:arg-near}
\theta_x(s)
=
m\arg(s-\rho_0)
+
\operatorname{Im} H_{\rho_0}(s)
-
\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}(s).
\end{equation}

### 4.3 What must be proved for the target lemma (open)

**Proposition (M1 reduction — conditional on remainder bounds).**  
Suppose there exist a path \(s_x\to\rho_0\) with \(\operatorname{Re}s_x=\beta\) (or \(\operatorname{Re}s_x\to\beta\)), a sequence \(x_n\to\infty\), and constants \(c_1,c_2>0\) such that along this path
\begin{align}
\bigl\lvert m\arg(s_{x_n}-\rho_0)\bigr\rvert
&\ge
c_1\,m\log\log x_n,
\label{eq:arg-path}
\\
\bigl\lvert\operatorname{Im} H_{\rho_0}(s_{x_n})\bigr\rvert
&\le
\tfrac14 c_1\,m\log\log x_n,
\\
\bigl\lvert\operatorname{Im}\mathcal{R}_{x_n}^{\mathrm{EP}}(s_{x_n})\bigr\rvert
&\le
\tfrac14 c_1\,m\log\log x_n.
\label{eq:rem-small}
\end{align}
Then
\[
\bigl\lvert\theta_{x_n}(s_{x_n})\bigr\rvert
\ge
\tfrac12 c_1\,m\log\log x_n.
\]
If in addition \(s_{x_n}\to\rho_0\) slowly enough that \(\theta_{x_n}(s_{x_n})\) and \(\theta_{x_n}(\rho_0)\) (limit of continuous extension of \(\arg P_{x_n}\) as \(s\to\rho_0\)) differ by \(o(m\log\log x_n)\), the same lower bound passes to \(\theta_{x_n}(\beta,\gamma)\).

**Status:**  
- (eq:arg-path) is a **path design** problem (how to approach \(\rho_0\) so that \(\arg(s-\rho_0)\) accumulates \(\log\log x\) scale — typically linked to the phase of \(x^{\rho-s}\) in the explicit formula, not free).  
- (eq:rem-small) is an **estimate of \(\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}\)** from (IvM-bd) + zero-sum truncation, using zero-density estimates; **open as a completed theorem** at the strength needed for the target lemma.  
- Passing to smoothed \(A_X\) uses the smoothing lemma in `RH_Target_Lemma_Sketch_Literature_L5.md` §I.5.

---

## 5. Parameter choice (working range)

For \(s=\sigma+it\) in the strip \(1/2\le\sigma\le 1\), \(\lvert t\rvert\ge 2\):

| Parameter | Typical choice | Role |
|-----------|----------------|------|
| \(x\) | \(\lvert t\rvert^{A}\) or \(\exp(c\sqrt{\log\lvert t\rvert})\) | Balance prime sum and zero sum |
| \(T\) | \(x\) or \(\lvert t\rvert\) | Truncate zeros in (IvM) |
| Path \(\Gamma\) | Horizontal then vertical, avoiding zeros by \(\asymp 1/\log\log\lvert t\rvert\) | Define \(\log\zeta\) |

**Named bound package:**  
Say “under the **Davenport range** \(2\le x\le t^{2}\), \(T=x\)” when invoking (IvM-bd).

---

## 6. Link to Akatsuka (★\(_\mathrm{line}\)) and the target lemma

### 6.1 Critical line (Akatsuka)

On \(s=\tfrac12+i\tau\) at a zero of order \(m\), [Aka17] (via DRH literature) controls a **renormalized** \(\zeta_x(s)\), equivalent to a statement about \(\log P_x+\text{pole renormalizer}+m\log\log x\).  
That renormalizer is an archimedean / pole cousin of the \(\int x^{1-w}/(1-w)\,dw\) term inside \(\mathcal{R}_{x,T}^{\mathrm{IvM}}\).  
Thus Akatsuka’s critical-line theory is compatible with M1: it is a refined analysis of \(\mathcal{R}_x^{\mathrm{EP}}+m\log(s-\rho)\) on \(\mathrm{Re}s=\tfrac12\).

### 6.2 Off-line target lemma

The target lemma asks for growth of \(\lvert A_X(\beta,\gamma)\rvert\) at \(\beta=Y>1/2\).  
M1 reduces this to (eq:arg-path)+(eq:rem-small).  
[Aka24, Prop. 7.1]-style \(\Omega_+\) estimates address **real** prime sums when zeros lie to the right of \(\kappa\); extending those methods to **\(\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}\)** at complex \(s=\beta+i\gamma\) is the analytic core still open.

---

## 7. Smoothing to \(A_X\)

Recall
\[
A_X(\sigma,t)
=
\int
\theta_{e^u}(\sigma,t)\,
\phi\Bigl(\frac{u}{\log X}\Bigr)
\frac{du}{\log X}.
\]
Under M1,
\[
A_X(\sigma,t)
=
\int
\operatorname{Im}\log\zeta(\sigma+it)\,
\mu_X(du)
-
\int
\operatorname{Im}\mathcal{R}_{e^u}^{\mathrm{EP}}(\sigma+it)\,
\mu_X(du),
\]
with \(\mu_X\) the probability measure \(\phi(u/\log X)\,du/\log X\) on \(u\in[\log X,2\log X]\).

**Named smoothed remainder:**
\[
\mathcal{R}_X^{A}(\sigma,t)
:=
\int
\operatorname{Im}\mathcal{R}_{e^u}^{\mathrm{EP}}(\sigma+it)\,
\phi\Bigl(\frac{u}{\log X}\Bigr)
\frac{du}{\log X}.
\]
Target-lemma quality bounds need \(\lvert\mathcal{R}_X^{A}\rvert=o(m\log\log X)\) (or \(\le \tfrac14 c\,m\log\log X\)) along a subsequence, together with path/zero contributions of size \(\ge c\,m\log\log X\).

---

## 8. What is proved in this note vs open

| Item | Status |
|------|--------|
| Identity (M1-EP): \(\log\zeta=\log P_x+\mathcal{R}_x^{\mathrm{EP}}\) | **Defined** via (IvM) + path integration |
| Name \(R_{\mathrm{IvM}}\), \(\mathcal{R}_{x,T}^{\mathrm{IvM}}\), \(\mathcal{R}_x^{\mathrm{EP}}\), \(\mathcal{R}_X^{A}\) | **Fixed** |
| Reference bound shape (IvM-bd) | **Standard**; pin constants to one textbook edition when proving lemmas |
| \(E_x^{\mathrm{pow}}\) negligible | **Standard** |
| Target lemma | **Open** |
| (eq:rem-small) at off-line zeros | **Open** |
| (eq:arg-path) design | **Open** |
| RH | **Open** |

---

## 9. Minimal lemma list continuing from M1

| ID | Lemma |
|----|--------|
| **M1.1** | Fix edition: state (IvM) + (IvM-bd) with explicit constants from Davenport or Titchmarsh |
| **M1.2** | Bound \(\lvert\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}(s)\rvert\) for \(s=\beta+i\gamma+\delta\), \(\lvert\delta\rvert\le 1/\log\log x\), under zero-density hypotheses |
| **M1.3** | Construct path \(s_x\to\rho_0\) with \(\lvert m\arg(s_x-\rho_0)\rvert\gg m\log\log x\) while keeping M1.2 |
| **M1.4** | Transfer to \(\theta_x(\rho_0)\) and to \(A_X\) (smoothing) |

---

## One-liner

**M1 is the identity \(\log\zeta=\log P_x+\mathcal{R}_x^{\mathrm{EP}}\), where \(\mathcal{R}_x^{\mathrm{EP}}\) is the path-integrated Ingham–von Mangoldt remainder \(R_{\mathrm{IvM}}\) minus an elementary prime-power error; zeros enter through \(\sum x^{\rho-s}/(\rho-s)\), and the target lemma reduces to making \(\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}\) small while \(m\arg(s-\rho)\) is large.**

*Per aspera ad astra.*
