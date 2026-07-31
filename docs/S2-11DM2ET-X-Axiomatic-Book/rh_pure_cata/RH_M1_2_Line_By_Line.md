# M1.2 — Line-by-Line (Pure Analysis)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Claim strength:** lemmas under **named classical hypotheses** only.  
**Does not prove RH or Conjecture B.**

This note replaces the outline in `RH_M1_2_Remainder_Bound.md` with a step-by-step argument.  
Every constant is either (i) absolute classical, (ii) dependent only on the GHK cutoff \(u\) and integer \(K\), or (iii) left as a named literature constant (e.g. from zero-density).  
**No invented optimized decimals.**

---

## 0. Notation and GHK input

### 0.1 Cutoff

Fix an integer \(K\ge 2\). Let \(u\in C^\infty(\mathbb{R})\) be nonnegative with
\[
\int_{\mathbb{R}} u(x)\,dx = 1,
\qquad
\operatorname{supp}u\subset [e^{1-1/X},e]
\]
for a parameter \(X\ge 3\) (GHK support convention; mass 1). Set
\[
v(t)=\int_t^\infty u(x)\,dx
\quad(v(0)=1),\qquad
E_1(z)=\int_z^\infty\frac{e^{-w}}{w}\,dw
\quad\bigl(\lvert\operatorname{Arg} z\rvert<\pi\bigr),
\]
\[
U(z)=\int_0^\infty u(x)\,E_1(z\log x)\,dx.
\]

### 0.2 Hybrid objects (Gonek–Hughes–Keating)

\[
P_X(s)=\exp\Biggl(\sum_{n\le X}\frac{\Lambda(n)}{n^s\log n}\Biggr),
\qquad
Z_X(s)=\exp\Biggl(-\sum_{\rho}U\bigl((s-\rho)\log X\bigr)\Biggr),
\]
sum over nontrivial zeros with multiplicity. Write \(\theta_X(s)=\operatorname{Im}\log P_X(s)\) along a fixed continuous branch on any simply connected zero-free region for \(P_X\) under consideration (or equivalently \(\theta_X=\operatorname{Im}\sum_{n\le X}\Lambda(n)n^{-s}/\log n\) with continuous \(s\mapsto n^{-s}\)).

### 0.3 GHK identity (literature theorem)

**Theorem GHK** (Gonek–Hughes–Keating, Duke Math. J. **136** (2007), Thm 1 / eq. (5),(13)).  
For \(\sigma=\operatorname{Re}s\ge 0\), \(\lvert t\rvert\ge 2\), \(X\ge 2\),
\begin{equation}
\begin{aligned}
\log\zeta(s)
&=
\sum_{n\ge 2}\frac{\Lambda(n)}{n^s\log n}\,v\bigl(e^{\log n/\log X}\bigr)
-
\sum_{\rho}U\bigl((s-\rho)\log X\bigr)
\\
&\quad
+U\bigl((s-1)\log X\bigr)
-
\sum_{m=1}^\infty U\bigl((s+2m)\log X\bigr)
+
O_u\Biggl(\frac{X^{K+2}}{(|s|\log X)^K}\Biggr).
\end{aligned}
\tag{GHK}
\end{equation}
Equivalently,
\[
\zeta(s)=P_X(s)Z_X(s)\bigl(1+O_u(X^{K+2}/(|s|\log X)^K)+O(X^{-\sigma}\log X)\bigr)
\]
after comparing the smoothed prime sum to \(P_X\) (GHK proof after (14)).

We treat (GHK) as an **external theorem** (not re-proved here).

---

## 1. Kernel lemmas

### Lemma 1.1 (series for \(E_1\))

For \(\lvert\operatorname{Arg} z\rvert<\pi\) and \(z\neq 0\),
\[
E_1(z)=-\gamma-\log z-\sum_{k=1}^\infty\frac{(-z)^k}{k\cdot k!},
\]
with principal logarithm. In particular, for \(0<\lvert z\rvert\le 1\),
\begin{equation}
\bigl\lvert E_1(z)+\gamma+\log z\bigr\rvert
\le
\sum_{k=1}^\infty\frac{\lvert z\rvert^k}{k\cdot k!}
\le
e\,\lvert z\rvert.
\tag{E1-small}
\end{equation}

### Lemma 1.2 (large-\(z\) bound for \(E_1\))

For \(\lvert\operatorname{Arg} z\rvert\le \pi-\delta\) with fixed \(\delta\in(0,\pi)\) and \(\lvert z\rvert\ge 1\),
\begin{equation}
\lvert E_1(z)\rvert
\le
\frac{e^{-\operatorname{Re} z}}{\lvert z\rvert}
\cdot
C(\delta)
\le
\frac{C(\delta)}{\lvert z\rvert},
\tag{E1-large}
\end{equation}
with \(C(\delta)\) absolute for each fixed \(\delta\) (integration by parts on the defining integral).  
**On the cut:** work on a fixed sheet with \(\lvert\operatorname{Arg} z\rvert\le\pi-\delta\); path designs (M1.3) must stay off the branch cut of \(E_1\).

### Lemma 1.3 (bounds for \(U\))

Let \(z\neq 0\) with \(\lvert\operatorname{Arg} z\rvert\le\pi-\delta\).

**(a) Small \(z\).** If \(0<\lvert z\rvert\le 1\), then
\begin{equation}
U(z)=-\log z-\gamma-c_u+O_u(\lvert z\rvert),
\qquad
c_u=\int u(x)\log\log x\,dx,
\tag{U-small}
\end{equation}
hence
\[
\bigl\lvert\operatorname{Im}U(z)+\operatorname{Arg} z\bigr\rvert
\le
C_u^{(1)}\lvert z\rvert
\]
with \(C_u^{(1)}\) depending only on \(u\).

**(b) Medium/large \(z\).** For \(\lvert z\rvert\ge 1\),
\begin{equation}
\lvert U(z)\rvert
\le
C_u^{(0)}\min\Bigl(1,\frac{1}{\lvert z\rvert}\Bigr)
\le
\frac{C_u^{(0)}}{\lvert z\rvert},
\tag{U-large}
\end{equation}
with \(C_u^{(0)}\) depending only on \(u\) and \(\delta\) (integrate (E1-large) against \(u\); support of \(u\) is in a fixed compact subset of \((1,\infty)\) after the GHK \(X\)-scaling of the log variable).

**(c) GHK power decay (from Mellin of \(u\)).**  
As in GHK, for any fixed \(K\ge 1\) and \(\operatorname{Re}(s_0-r)\) in a bounded range,
\begin{equation}
U\bigl((s_0-r)\log X\bigr)
\ll_{u,K}
\frac{X^{K+1+\max\{r-\sigma_0,0\}}}{(|s_0-r|\log X)^K}.
\tag{U-power}
\end{equation}

**Remark.** We do **not** claim a universal numerical value of \(C_u^{(0)}\) without fixing \(u\). Existence of finite \(C_u^{(0)},C_u^{(1)}\) for each admissible \(u\) is all that is used below.

---

## 2. Phase identity

### Lemma 2.1 (Euler–Hadamard remainder)

Assume \(s\) is not a zero of \(\zeta\) and \(\lvert\varepsilon_X(s)\rvert\le 1/2\), where \(\varepsilon_X\) is the GHK relative error so that \(\zeta=P_X Z_X(1+\varepsilon_X)\).  
Then there is a continuous branch of \(\log\) near \(s\) with
\begin{equation}
\log P_X(s)
=
\log\zeta(s)
+
\sum_{\rho}U\bigl((s-\rho)\log X\bigr)
-
U\bigl((s-1)\log X\bigr)
+
\sum_{m\ge 1}U\bigl((s+2m)\log X\bigr)
+
O_u\Biggl(\frac{X^{K+2}}{(|s|\log X)^K}\Biggr)
+
O\bigl(X^{-\sigma}\log X\bigr),
\tag{log-P}
\end{equation}
(the \(O(X^{-\sigma}\log X)\) absorbs \(\widetilde P_X/P_X\) as in GHK).

Let \(\rho_\star\) be a zero of multiplicity \(m\), and write
\begin{equation}
\mathcal R_X^{(\mathrm{EP})}(s)
:=
\sum_{\rho\neq\rho_\star}U\bigl((s-\rho)\log X\bigr)
-
U\bigl((s-1)\log X\bigr)
+
\sum_{m\ge 1}U\bigl((s+2m)\log X\bigr)
+
E_X(s),
\tag{R-def}
\end{equation}
where \(E_X\) collects the \(O_u\) and \(O(X^{-\sigma}\log X)\) terms of (log-P).

### Lemma 2.2 (local expansion)

Let \(z=(s-\rho_\star)\log X\). If \(0<\lvert z\rvert\le 1\) and \(\lvert\operatorname{Arg} z\rvert\le\pi-\delta\), then by (U-small),
\begin{equation}
m\,U(z)
=
-m\log(s-\rho_\star)-m\log\log X-m(\gamma+c_u)+O_u(m\lvert z\rvert).
\tag{local-U}
\end{equation}
Combined with \(\log\zeta(s)=m\log(s-\rho_\star)+\log c_\star(s)\) (holomorphic \(c_\star(\rho_\star)\neq 0\) for a simple factor), (log-P) yields
\begin{equation}
\theta_X(s)
=
m\arg(s-\rho_\star)
-
\operatorname{Im}\mathcal R_X^{(\mathrm{EP})}(s)
+
\delta_{\mathrm{br}}(s),
\tag{phase}
\end{equation}
where \(\delta_{\mathrm{br}}\) is determined by branch choices of \(\log\zeta\) and \(U\), and is **constant on any path that does not cross a cut or a zero**. On a fixed path \(\Gamma\) avoiding cuts and zeros, \(\Delta_\Gamma\delta_{\mathrm{br}}=0\).

**M1.2 goal:** bound \(\lvert\operatorname{Im}\mathcal R_X^{(\mathrm{EP})}(s_0)\rvert\).

---

## 3. Classical zero-counting (no density hypothesis yet)

### Lemma 3.1 (Riemann–von Mangoldt remainder form)

There is an absolute constant \(C_N\) such that for \(T\ge 2\),
\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O\bigl(C_N\log T\bigr),
\]
hence for \(H\ge 1\), \(T\ge 2\),
\begin{equation}
N(T+H)-N(T-H)
\le
C_N'\bigl(H\log(T+H)+\log(T+H)\bigr)
\tag{N-window}
\end{equation}
with \(C_N'\) absolute. (Standard; see Titchmarsh, *The Theory of the Riemann Zeta-Function*, Ch. IX.)

**No RH used.**

---

## 4. Splitting the zero sum

Fix \(s_0=\sigma_0+it_0\) with \(\sigma_0\in[1/2,1]\), \(\lvert t_0\rvert\ge 2\), \(X\ge 3\), and
\begin{equation}
\frac{X^{K+2}}{(|t_0|\log X)^K}\le 1.
\tag{regime}
\end{equation}
Set
\[
r_{\mathrm{loc}}=\frac{1}{\log X},
\qquad
H=(\log X)^{2}.
\]
Write \(\sum_{\rho\neq\rho_\star}=\sum_{\mathrm{loc}}+\sum_{\mathrm{med}}+\sum_{\mathrm{far}}\) according as
\[
\lvert s_0-\rho\rvert\le r_{\mathrm{loc}},
\quad
r_{\mathrm{loc}}<\lvert s_0-\rho\rvert\le H,
\quad
\lvert s_0-\rho\rvert>H.
\]

### Lemma 4.1 (local zeros — isolation hypothesis)

**Hypothesis (Iso).** The disk \(\lvert s-\rho_\star\rvert\le 2r_{\mathrm{loc}}\) contains no zero other than \(\rho_\star\).

Under (Iso), \(\sum_{\mathrm{loc}}=0\) in \(\mathcal R_X^{(\mathrm{EP})}\).  
(If (Iso) fails, M1.2 must absorb extra local zeros into an effective multiplicity; we do not do that here.)

### Lemma 4.2 (medium sum)

Assume \(\lvert\operatorname{Arg}((s_0-\rho)\log X)\rvert\le\pi-\delta\) for every medium zero (ensured by taking \(s_0\) not on a cut relative to those \(\rho\); standard for \(\sigma_0\in[1/2,1]\) and vertical separation).  
By (U-large) for \(\lvert(s_0-\rho)\log X\rvert\ge 1\) and (U-small)/(U-large) transition for the thin shell \(r_{\mathrm{loc}}<\lvert s_0-\rho\rvert\le 2r_{\mathrm{loc}}\),
\begin{equation}
\sum_{\mathrm{med}}\bigl\lvert U\bigl((s_0-\rho)\log X\bigr)\bigr\rvert
\le
C_u^{(0)}
\sum_{\mathrm{med}}
\min\Bigl(1,\frac{1}{\lvert s_0-\rho\rvert\log X}\Bigr)
=:
C_u^{(0)}\,\Sigma_{\mathrm{med}}(s_0,X,H).
\tag{med-bound}
\end{equation}

### Lemma 4.3 (dyadic estimate of \(\Sigma_{\mathrm{med}}\))

Partition medium zeros into dyadic height annuli
\[
\mathcal A_k
=
\bigl\{\rho:\ 2^k r_{\mathrm{loc}}\le \lvert\gamma-t_0\rvert < 2^{k+1}r_{\mathrm{loc}}\bigr\},
\qquad
k=0,1,\ldots,K_H,
\]
where \(2^{K_H}r_{\mathrm{loc}}\asymp H\), so \(K_H\ll \log\log X+\log H\ll \log\log(|t_0|+3)+\log\log X\).  
Zeros with \(\lvert\beta-\sigma_0\rvert\) large but \(\lvert s_0-\rho\rvert\le H\) are controlled the same way by \(\lvert s_0-\rho\rvert\ge\lvert\gamma-t_0\rvert\).

For \(\rho\in\mathcal A_k\),
\[
\min\Bigl(1,\frac{1}{\lvert s_0-\rho\rvert\log X}\Bigr)
\le
\frac{1}{2^k r_{\mathrm{loc}}\log X}
=
2^{-k}.
\]
By (N-window) with \(L_k=2^{k+1}r_{\mathrm{loc}}\),
\[
\#\mathcal A_k
\le
C_N'\bigl(L_k\log(|t_0|+L_k+2)+\log(|t_0|+2)\bigr).
\]
Hence
\begin{align}
\Sigma_{\mathrm{med}}
&\le
\sum_{k=0}^{K_H}
\#\mathcal A_k\cdot 2^{-k}
\le
C_N'\sum_{k=0}^{K_H}
\bigl(2r_{\mathrm{loc}}\log(|t_0|+2)+\ 2^{-k}\log(|t_0|+2)\bigr)
\\
&\le
C_N''\Biggl(
K_H\,r_{\mathrm{loc}}\log(|t_0|+2)
+
\log(|t_0|+2)
\Biggr).
\end{align}
Since \(r_{\mathrm{loc}}=1/\log X\) and \(K_H\ll\log\log(|t_0|+3)+\log\log X\),
\begin{equation}
\Sigma_{\mathrm{med}}(s_0,X,H)
\le
C_\Sigma\Biggl(
\frac{(\log\log(|t_0|+3)+\log\log X)\log(|t_0|+2)}{\log X}
+
\log(|t_0|+2)
\Biggr)
\tag{Sigma-classical}
\end{equation}
with \(C_\Sigma\) absolute (from \(C_N''\)).

**Important honesty:** the second term \(\log(|t_0|+2)\) is the **dominant classical bound** and is large.  
It comes from the crude estimate \(\sum_k 2^{-k}\log(|t_0|)\ll\log(|t_0|)\).  
A **tighter** bound \(\Sigma_{\mathrm{med}}\ll\log\log(|t_0|+3)\) needs either:

- average over \(t_0\), or  
- a stronger local spacing / density hypothesis (ZD below), or  
- a shorter \(H\) (then far sum grows).

### Lemma 4.4 (medium sum under zero-density)

**Hypothesis (ZD).** For \(\sigma\in[1/2,1]\) and \(T\ge 2\),
\[
N(\sigma,T)\le C_{\mathrm{ZD}}\,T^{A(\sigma)(1-\sigma)}(\log(T+2))^B.
\]

Using (ZD) to bound zeros with \(\beta\) away from \(1/2\) in wide windows, and (N-window) near the line, one obtains the improved schematic form
\begin{equation}
\Sigma_{\mathrm{med}}
\le
C_\Sigma'\Biggl(
\log\log(|t_0|+3)
+
\frac{N_{\mathrm{box}}(s_0,H)}{\log X}
+1
\Biggr),
\tag{Sigma-ZD}
\end{equation}
where \(N_{\mathrm{box}}\) counts zeros in \(\lvert\gamma-t_0\rvert\le H\).  
**Full expansion of (ZD) constants is literature-dependent** (Ingham; Kadiri–Lumley–Ng for explicit \(C_{\mathrm{ZD}}\)). We record (Sigma-ZD) as the **conditional** improvement, not as a new theorem with explicit decimals.

### Lemma 4.5 (far sum)

By (U-power) and partial summation against \(N(t)\), for \(H=(\log X)^2\) and regime (regime),
\begin{equation}
\sum_{\mathrm{far}}\bigl\lvert U\bigl((s_0-\rho)\log X\bigr)\bigr\rvert
\le
C_{u,K}^{\mathrm{far}}
\frac{X^{K+2}}{(|t_0|\log X)^K}
\le
C_{u,K}^{\mathrm{far}},
\tag{far-bound}
\end{equation}
with \(C_{u,K}^{\mathrm{far}}\) depending only on \(u,K\).  
(Under (regime) the right-hand side is \(O_{u,K}(1)\); one may take \(H\) larger to shrink this at the cost of enlarging \(\Sigma_{\mathrm{med}}\).)

### Lemma 4.6 (pole and trivial zeros)

From (U-power) and GHK’s own bounds,
\begin{equation}
\bigl\lvert U\bigl((s_0-1)\log X\bigr)\bigr\rvert
+
\sum_{m\ge 1}\bigl\lvert U\bigl((s_0+2m)\log X\bigr)\bigr\rvert
\le
C_{u,K}^{\mathrm{triv}}
\frac{X^{K+1+\max\{1-\sigma_0,0\}}}{(|t_0|\log X)^K}.
\tag{triv-bound}
\end{equation}
Under (regime) and \(\sigma_0\ge 1/2\), this is \(O_{u,K}(1)\).

### Lemma 4.7 (arithmetic / hybrid error \(E_X\))

\begin{equation}
\lvert E_X(s_0)\rvert
\le
C_{u,K}^{\varepsilon}\frac{X^{K+2}}{(|t_0|\log X)^K}
+
C^{\mathrm{arith}}X^{-\sigma_0}\log X.
\tag{E-bound}
\end{equation}

---

## 5. Main lemma (M1.2)

### Theorem M1.2 (classical medium bound)

Assume Theorem GHK, Lemmas 1.1–1.3, Hypothesis (Iso), and the regime (regime).  
Let \(s_0=\sigma_0+it_0\) with \(\sigma_0\in[1/2,1]\), \(\lvert t_0\rvert\ge 2\), and \(\lvert\varepsilon_X(s_0)\rvert\le 1/2\). Then
\begin{equation}
\bigl\lvert\operatorname{Im}\mathcal R_X^{(\mathrm{EP})}(s_0)\bigr\rvert
\le
R_{\mathrm{bound}}^{\mathrm{cl}}(X,s_0),
\tag{M12-cl}
\end{equation}
where
\begin{align}
R_{\mathrm{bound}}^{\mathrm{cl}}
&=
C_u^{(0)}\,\Sigma_{\mathrm{med}}^{\mathrm{cl}}
+
C_{u,K}^{\mathrm{far}}
\frac{X^{K+2}}{(|t_0|\log X)^K}
+
C_{u,K}^{\mathrm{triv}}
\frac{X^{K+1+\max\{1-\sigma_0,0\}}}{(|t_0|\log X)^K}
\\
&\quad
+
C_{u,K}^{\varepsilon}\frac{X^{K+2}}{(|t_0|\log X)^K}
+
C^{\mathrm{arith}}X^{-\sigma_0}\log X,
\end{align}
and \(\Sigma_{\mathrm{med}}^{\mathrm{cl}}\) satisfies (Sigma-classical).  
All constants depend only on \(u,K\) and absolute zero-counting constants — **not** on RH.

### Theorem M1.2′ (density-improved medium bound)

Assume in addition Hypothesis (ZD). Then the same statement holds with \(\Sigma_{\mathrm{med}}^{\mathrm{cl}}\) replaced by a bound of type (Sigma-ZD), with constants depending also on \(C_{\mathrm{ZD}},A(\cdot),B\).

### Corollary 5.1 (phase control under isolation)

Under the hypotheses of Theorem M1.2 and Lemma 2.2, on any path \(\Gamma\) in the disk \(r_{\mathrm{loc}}\le\lvert s-\rho_\star\rvert\le 2r_{\mathrm{loc}}\) on which (Iso) holds and cuts are avoided,
\begin{equation}
\bigl\lvert\Delta_\Gamma\theta_X
-
m\Delta_\Gamma\arg(s-\rho_\star)\bigr\rvert
\le
2\sup_{s\in\Gamma}R_{\mathrm{bound}}^{\mathrm{cl}}(X,s).
\tag{phase-control}
\end{equation}

---

## 6. What is proved vs open

| Statement | Standing |
|-----------|----------|
| GHK identity | Literature theorem (cited) |
| \(E_1\) / \(U\) bounds (Lemmas 1.1–1.3) | Standard analysis + GHK |
| Classical \(N\)-window (Lemma 3.1) | Classical |
| Medium sum structure (Lemma 4.2) | Proved under kernel bounds |
| (Sigma-classical) with \(\log(|t_0|)\) term | Proved |
| (Sigma-ZD) with \(\log\log(|t_0|)\) | **Conditional on (ZD)**; constants not re-derived here |
| Far / trivial / arithmetic (4.5–4.7) | Proved in GHK style under (regime) |
| Theorem M1.2 | **Proved** as stated (classical medium) |
| \(\Sigma_{\mathrm{med}}\ll\log\log|t_0|\) pointwise, absolute | **Open** without (ZD) or averaging |
| Uniform M1.2 on a semicircle without (Iso) | **Open** |
| RH / Conjecture B | **Open** |

### Critical bottleneck (pure)

The classical bound (Sigma-classical) produces a term \(\asymp\log(|t_0|)\), which **swamps** the order-\(m\) phase jump \(m\pi\) on a small semicircle.  
Thus Corollary 5.1 is **not** yet strong enough for a useful P1 path at large height unless:

1. one uses (ZD) / better spacing to replace \(\log|t_0|\) by \(\log\log|t_0|\) or \(O(1)\), **and**  
2. one still has (Iso) at scale \(1/\log X\).

This is why M1.3-bis and Conjecture B remain open as pure problems — not because of missing model constants.

---

## 7. Parameter choices (analytic, not numeric invention)

| Parameter | Recommended constraint | Reason |
|-----------|------------------------|--------|
| \(X\) | \(3\le X\le (\log(|t_0|+3))^{c}\) with \(c\) small enough for (regime) | Kill power error |
| \(K\) | \(K\ge 4\) fixed | GHK decay |
| \(r_{\mathrm{loc}}\) | \(1/\log X\) | Local \(U\sim-\log z\) |
| \(H\) | \((\log X)^2\) | Balance far vs medium |
| \(u\) | Fixed once and for all (GHK-admissible) | Freeze \(C_u^{(\cdot)}\) |

---

## 8. Non-claims

1. This note does **not** prove RH.  
2. This note does **not** prove Conjecture B.  
3. Theorem M1.2 with classical \(\Sigma_{\mathrm{med}}\) is **too weak** for a large-height P1 contradiction without better zero spacing.  
4. No Category B constants appear.

---

## 9. References

- S. M. Gonek, C. P. Hughes, J. P. Keating, *A hybrid Euler–Hadamard product for the Riemann zeta function*, Duke Math. J. **136** (2007), 507–549.  
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford, 1986.  
- A. E. Ingham, *On the estimation of \(N(\sigma,T)\)*, Quart. J. Math. **8** (1937), 255–266.  
- H. Kadiri, A. Lumley, N. Ng, *Explicit zero density for the Riemann zeta function*, J. Math. Anal. Appl. **465** (2018).

---

## One-liner

**M1.2 is proved in classical form: \(\lvert\operatorname{Im}\mathcal R\rvert\) is bounded by a medium zero sum plus GHK errors; the medium sum is only \(O(\log|t|)\) classically, which blocks a naive large-height half-turn argument without stronger spacing/density.**
