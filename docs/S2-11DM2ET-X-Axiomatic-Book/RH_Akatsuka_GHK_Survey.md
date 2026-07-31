# Akatsuka expansions and Gonek–Hughes–Keating hybrid formula

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A** survey for the phase programme.  
**No model constants.** RH open; infrastructure only — not a proof of the target lemma.

**Companions:** `RH_O1_Akatsuka_M1_Package.md`, `RH_M1_2_Remainder_Bound_Strategy.md`, `RH_M1_Explicit_Formula_Remainder.md`.  
**Probe (hybrid numeric):** `scripts/rh_GHK_hybrid_diagnostic.py`.

---

## 1. Akatsuka (2017) — pointwise partial Euler products in the right half-strip

**Source.**  
H. Akatsuka, *The Euler product for the Riemann zeta-function in the critical strip*,  
Kodai Mathematical Journal **40** (2017), 79–101.  
DOI: [10.2996/kmj/1490083225](https://doi.org/10.2996/kmj/1490083225) · MR3626575.

### Setting

Let \(c(x)=\sum_{n\le x}\Lambda(n)\) (Chebyshev’s \(\psi\)-function). Write
\[
Y=\sup\{\operatorname{Re}\rho:\zeta(\rho)=0\}.
\]
Classically \(\tfrac12\le Y\le 1\); RH is exactly \(Y=\tfrac12\).

### Main results (schematic, aligned with O1 / DRH literature)

**Theorem on the critical line (\(\sigma_0=\tfrac12\)).**  
The following are equivalent:

- \(c(x)=x+o(x^{1/2}\log x)\),  
- the normalised partial product
  \[
  (\log x)^{m}\prod_{p\le x}(1-p^{-s_0})^{-1}
  \]
  (with a suitable polar renormaliser) tends to a nonzero limit for some (equivalently every) height \(t_0\),  
- and the same for every \(t_0\).

When the limit exists it equals an explicit constant involving \(\zeta^{(m)}(s_0)/m!\) and a \(\sqrt{2}\) factor at the real point.  
(Full line-by-line: `RH_Akatsuka_Theorem_Extract.md`, `RH_O1_Akatsuka_M1_Package.md`.)

**Theorem for fixed \(\sigma_0\in(\tfrac12,1)\).**  
Equivalence between the prime-sum estimate \(c(x)=x+O(x^{\sigma_0})\) and the existence of a nonzero limit for the same normalised partial product at heights \(s_0=\sigma_0+it_0\).

**Theorem under \(Y<1\).**  
Let \(s_0=\sigma_0+it_0\) with \(Y\le\sigma_0<1\) and \(m=\) multiplicity of a zero at \(s_0\) (possibly \(m=0\)). Then
\begin{align*}
&\sum_{n\le x}\frac{\Lambda(n)}{n^{s_0}\log n}
-
\lim_{\varepsilon\downarrow 0}\int_{1+\varepsilon}^{x}\frac{du}{u^{s_0}\log u}
+
m\log\log x
\\
&\qquad=
\lim_{s\to s_0}\bigl(\log\zeta(s)-m\log(s-s_0)+\log(s-1)\bigr)
+(1-m)c_E
+
\frac{c(x)-x}{x^{s_0}\log x}
+
O\Bigl(\frac{1}{x^{\sigma_0-Y}\log x}\Bigr).
\end{align*}
The LHS is essentially the logarithm of the partial Euler product after polar renormalisation.  
**The term \(m\log\log x\) is real** — it enlarges the **modulus** of the partial product and does **not** by itself force growth of continuous \(\theta_x=\arg P_x\).  
Hence O1 concluded that **argument growth still requires M1 remainder analysis**.

### Use for the phase programme

Akatsuka supplies the exact asymptotic dictionary between prime-power sums and partial Euler products at fixed height in the right half-strip. Natural input for O1 and for the **real-part** side of the target lemma. The **imaginary / argument** side must still come from the same identities or from a hybrid formula.

---

## 2. Gonek–Hughes–Keating (2007) — smoothed hybrid Euler–Hadamard product

**Source.**  
S. M. Gonek, C. P. Hughes, J. P. Keating, *A hybrid Euler–Hadamard product for the Riemann zeta function*,  
Duke Mathematical Journal **136** (2007), 507–549.  
arXiv: [math/0511182](https://arxiv.org/abs/math/0511182).

### Main identity (Theorem 1 of GHK)

Let \(s=\sigma+it\) with \(\sigma\ge 0\) and \(\lvert t\rvert\ge 2\), let \(X\ge 2\), and let \(K\) be any fixed positive integer.  
Let \(u(x)\) be a nonnegative \(C^\infty\) function of mass 1, supported on \([e^{1-1/X},e]\), and set
\[
U(z)
=
\int_0^\infty u(x)\,E_1(z\log x)\,dx,
\]
where \(E_1(z)=\int_z^\infty e^{-w}/w\,dw\) is the exponential integral.

Then
\begin{equation}
\boxed{
\zeta(s)
=
P_X(s)\,Z_X(s)
\Biggl(
1
+
O\Biggl(\frac{X^{K+2}}{(\lvert s\rvert\log X)^{K}}\Biggr)
+
O(X^{-\sigma}\log X)
\Biggr)
}
\tag{GHK}
\end{equation}
with constants depending only on \(u\) and \(K\). Here
\begin{align}
P_X(s)
&=
\exp\Biggl(\sum_{n\le X}\frac{\Lambda(n)}{n^{s}\log n}\Biggr),
\tag{GHK-\(P\)}
\\
Z_X(s)
&=
\exp\Biggl(
-
\sum_{\rho}U\bigl((s-\rho)\log X\bigr)
\Biggr).
\tag{GHK-\(Z\)}
\end{align}
The sum runs over nontrivial zeros. The weight \(U\) is concentrated so that only zeros with \(\lvert s-\rho\rvert\asymp 1/\log X\) contribute appreciably to \(Z_X\).

**Unconditional** — no RH required for (GHK).  
(A variant replaces \(P_X\) by a smoothed \(\widetilde P_X\) with weight \(v\) and drops the second error term.)

### Interpretation

| Factor | Role |
|--------|------|
| \(P_X\) | Smoothed partial Euler product (arithmetic side; primes \(\le X\)) |
| \(Z_X\) | Smoothed partial Hadamard product (spectral side; local zeros) |
| \(X\) | Mediator: larger \(X\) → more primes, fewer zeros in the window |

Near height \(T\), \(Z_X\) behaves like a polynomial of degree \(\asymp\log T/\log X\).

### Relation to random-matrix models and moments

Modelling \(Z_X\) by characteristic polynomials of unitary matrices recovers Keating–Snaith moment conjectures; \(P_X\) produces the arithmetic constant \(a(k)\). Same hybrid used for discrete moments of \(\zeta'(\rho)\). **Heuristic for moments; the identity (GHK) itself is rigorous.**

### Use for the phase programme

Taking logarithms and imaginary parts (continuous branches),
\begin{equation}
\arg\zeta(s)
=
\arg P_X(s)
+
\arg Z_X(s)
+
O(\text{error}),
\tag{GHK-arg}
\end{equation}
with
\[
\arg Z_X(s)
=
-
\sum_{\rho}
\operatorname{Im} U\bigl((s-\rho)\log X\bigr).
\]
The term \(\arg Z_X\) is a **smoothed sum of local arguments** \(\arg(s-\rho)\) (via the phase of \(\exp(-U)\)).  
Isolating a single off-line zero of multiplicity \(m\) and controlling all other zeros is exactly **M1.2–M1.3**.  
Error terms are already explicit and of the shape needed once a zero-density / spacing hypothesis is supplied.

**Gonek (2012).** Finite Euler products (Trans. Amer. Math. Soc.): good approximation by short Euler products in a region of the right half-strip forces only finitely many zeros there — independent motivation for studying \(\arg P_x\) off the line.

---

## 3. How the two papers fit together for M1.2

| Source | Contribution |
|--------|----------------|
| **Akatsuka** | Precise asymptotic of \(\log P_x\) (or \(\sum\Lambda(n)/(n^{s_0}\log n)\)) at fixed height; real \(m\log\log x\) when a zero sits at that height |
| **GHK** | Smoothed, globally valid hybrid \(\zeta=P_X Z_X(1+\mathrm{err})\) with explicit errors; \(Z_X\) isolates nearby zeros |

**Combining them:**
\begin{equation}
\log\zeta(s)
=
\log P_X(s)
+
\log Z_X(s)
+
\mathcal{E}_{\mathrm{GHK}}(s;X,K),
\tag{GHK-log}
\end{equation}
with
\begin{equation}
\mathcal{E}_{\mathrm{GHK}}(s;X,K)
\ll
\frac{X^{K+2}}{(\lvert s\rvert\log X)^{K}}
+
X^{-\sigma}\log X
\tag{GHK-err}
\end{equation}
(for \(\sigma\ge 0\), \(\lvert t\rvert\ge 2\); absolute constants depending on \(u,K\)).

Move the local zero contribution out of \(Z_X\):
\[
\log Z_X(s)
=
-
m\,U\bigl((s-\rho)\log X\bigr)
-
\sum_{\rho'\neq\rho}
U\bigl((s-\rho')\log X\bigr).
\]
For \(s\) near \(\rho\), \(U((s-\rho)\log X)\sim -\log\bigl((s-\rho)\log X\bigr)-\gamma+\cdots\), so
\[
-
m\,U\bigl((s-\rho)\log X\bigr)
\sim
m\log(s-\rho)
+
m\log\log X
+
m\gamma
+
\cdots.
\]
Thus
\begin{equation}
\begin{aligned}
\log P_X(s)
&=
\log\zeta(s)
+
m\,U\bigl((s-\rho)\log X\bigr)
+
\sum_{\rho'\neq\rho}
U\bigl((s-\rho')\log X\bigr)
-
\mathcal{E}_{\mathrm{GHK}}
\\
&=
m\log(s-\rho)
+
\underbrace{
\log\zeta(s)
-
m\log(s-\rho)
+
\sum_{\rho'\neq\rho}
U(\cdots)
+
m\log\log X
+
\cdots
-
\mathcal{E}_{\mathrm{GHK}}
}_{\displaystyle \widetilde{\mathcal{R}}_{X,\rho}^{\mathrm{GHK}}(s)}.
\end{aligned}
\tag{M1.2-GHK}
\end{equation}

**M1.2 (GHK form).**  
Bound
\[
\bigl\lvert\operatorname{Im}\widetilde{\mathcal{R}}_{X,\rho}^{\mathrm{GHK}}(s)\bigr\rvert
\]
on a path about \(\rho\) so that it is \(\le c_0\,m\sup\lvert\arg(s-\rho)\rvert\) with \(c_0<1\).

This is the concrete analytic content of M1.2 in hybrid language (parallel to \(\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}\) in IvM language).

---

## 4. Precise M1.2 statement with GHK error terms

**Lemma M1.2-GHK (conditional sketch).**  
Let \(\rho=\beta+i\gamma\) be a zero of multiplicity \(m\ge 1\) with \(\beta=Y=\sup\operatorname{Re}\rho'\). Fix \(K\ge 1\) and a GHK weight \(u\). Choose \(X\ge 2\) with
\[
\frac{X^{K+2}}{(\lvert\gamma\rvert\log X)^{K}}
+
X^{-\beta}\log X
=
o(1)
\quad\text{as }\gamma\to\infty
\]
(e.g. \(X=(\log\gamma)^{A}\) for fixed \(A\), or \(X=\gamma^{\theta}\) with \(\theta\) small enough vs \(K\)).  
Assume a density/spacing package **HD** ensuring
\[
\sum_{\rho'\neq\rho}
\bigl\lvert\operatorname{Im} U\bigl((s-\rho')\log X\bigr)\bigr\rvert
=
o\bigl(m\log\log X\bigr)
\]
uniformly for \(s\) on a path \(\gamma_{\mathrm{path}}\subset D(\rho,r)\), \(r\asymp 1/\log\gamma\), free of other zeros.

Then there exists \(c_0\in(0,1)\) such that for large \(\gamma\),
\[
\sup_{s\in\gamma_{\mathrm{path}}}
\bigl\lvert\operatorname{Im}\widetilde{\mathcal{R}}_{X,\rho}^{\mathrm{GHK}}(s)\bigr\rvert
\le
c_0\,m\cdot
\sup_{s\in\gamma_{\mathrm{path}}}
\lvert\arg(s-\rho)\rvert
+
O\bigl(\lvert\mathcal{E}_{\mathrm{GHK}}\rvert\bigr).
\]

**Corollary.** Along a semicircle with \(\arg:0\to\pi\), if the \(O(\lvert\mathcal{E}_{\mathrm{GHK}}\rvert)\) and distant-\(U\) terms are \(\le\tfrac14 m\pi\), then \(\Delta\arg P_X\ge\tfrac12 m\pi\).

**Status:** sketch with **explicit GHK-err**; full proof open under HD.

---

## 5. Numerical hybrid probe

Evaluate at L5-style off-line minima and near first zeros:

\[
\operatorname{Im}\log Z_X^{\mathrm{trunc}}(s)
:=
-
\sum_{\lvert\gamma_n-t\rvert\le C/\log X}
\operatorname{Im} U\bigl((s-\rho_n)\log X\bigr)
\]
(approximate \(Z_X\) by nearby Odlyzko zeros), compare to \(m\arg(s-\rho_{\mathrm{proxy}})\), and compare \(\arg\zeta-\arg P_X\) to \(\arg Z_X^{\mathrm{trunc}}\).

**Script:** `scripts/rh_GHK_hybrid_diagnostic.py`  
**Results:** `rh_GHK_hybrid_diagnostic_results.json`  
**Status:** diagnostic only; does not prove M1.2.

### 5.1 Executed run (no proof claim)

Parameters: \(X=200\), primes to \(x_{\max}=15000\), \(U(z)\sim-\log z-\gamma\) (local GHK leading term), \(Z_X\) truncated to zeros with \(\lvert t-\gamma\rvert\le 3\pi/\log X\).

| Regime | mean \(\lvert\arg\zeta-(\arg P_X+\arg Z^{\mathrm{trunc}})\rvert\) | mean \(\lvert\operatorname{Im}(\log\zeta-\log P_X)\rvert\) | mean \(\lvert\operatorname{Im}\log Z^{\mathrm{trunc}}\rvert\) |
|--------|------------------------------------------------------------------:|-------------------------------------------------------------:|---------------------------------------------------------------:|
| Near critical zeros (6 ordinates, \(\Delta t=0.02\)) | \(\approx 0.19\) | \(\approx 1.38\) | \(\approx\pi/2\) (local factor dominant) |
| Off-line \(\lvert\zeta\rvert\) minima (\(\sigma\ge 0.60\)) | \(\approx 0.059\) | \(\approx 0.064\) | \(\approx 0.048\) |

**Reading (diagnostic only):**
- Hybrid check \(\arg\zeta\approx\arg P_X+\arg Z^{\mathrm{trunc}}\) holds at the \(O(10^{-1})\) level near the first zeros and tighter off-line at \(\sigma=0.60\) (where no true zero sits).
- On-line, \(\operatorname{Im}\log Z^{\mathrm{trunc}}\approx\pi/2\) tracks the local \(\arg(s-\rho)\) after a small imaginary offset; \(\operatorname{Im}(\log\zeta-\log P_X)\) is large because the remainder absorbs the zero — consistent with M1.2 bookkeeping.
- Off-line minima at \(\sigma=0.60\) are **not** zeros: both \(\operatorname{Im} R\) and \(\operatorname{Im}\log Z\) stay small; the hybrid error is modest. This is a **control**, not an off-line zero experiment.
- Full \(U\) (smoothed \(E_1\) with compact \(u\)) and denser zero lists would tighten the on-line error; the present \(U\sim-\log-\gamma\) is the singular leading term only.

---

## 6. Status reminder

| Item | Status |
|------|--------|
| RH | **Open** |
| Akatsuka expansions | Classical infrastructure (O1) |
| GHK hybrid identity | Classical, unconditional |
| M1.2 with GHK errors | **Stated (conditional)**; proof open |
| Hybrid numeric probe | **Executed** (diagnostic; no proof claim) |
| Target lemma | **Open** |

**Next increments:** prove M1.2-GHK under HD-low (first zeros); strengthen hybrid numeric with full \(U=E_1\) weight and denser zero lists; M1.3 path design.

---

## One-liner

**Akatsuka gives the exact real \(m\log\log x\) dictionary for partial products at fixed height; GHK gives \(\zeta=P_X Z_X(1+\mathrm{err})\) with explicit errors so that \(\arg\zeta=\arg P_X+\arg Z_X+O(\mathrm{err})\) and M1.2 becomes a bound on \(\operatorname{Im}\) of distant zeros plus GHK error after peeling \(m\log(s-\rho)\).**

*Per aspera ad astra.*
