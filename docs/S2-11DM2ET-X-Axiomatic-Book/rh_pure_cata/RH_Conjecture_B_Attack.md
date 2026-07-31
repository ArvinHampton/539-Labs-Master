# Attack on Conjecture B\(_\theta\) — Pure Analysis

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Object:** lower bounds for
\[
\theta_X(\rho)
:=
\operatorname{Im}\sum_{n\le X}\frac{\Lambda(n)}{n^{\rho}\log n}
\quad\text{at an off-line zero }\rho=\beta+i\gamma,\ \beta\neq\tfrac12.
\]
(Well-defined as a finite Dirichlet sum; no \(\log\zeta(\rho)\).)

Does **not** prove Conjecture B. Records what pure methods give and where they stop.

---

## 0. Setup

By Corollary 3.2 of `RH_Conjecture_B.md`, for fixed \(\beta>1/2\),
\[
\text{Conjecture B}
\quad\Leftrightarrow\quad
\limsup_{X\to\infty}\lvert\theta_X(\rho)\rvert=\infty.
\]
Write
\begin{equation}
S_X(\rho)
:=
\sum_{n\le X}\frac{\Lambda(n)}{n^{\rho}\log n}
=
\sum_{n\le X}\frac{\Lambda(n)}{n^{\beta}\log n}\,n^{-i\gamma},
\qquad
\theta_X=\operatorname{Im}S_X.
\tag{S}
\end{equation}

---

## 1. Trivial upper bounds (for orientation)

For \(\beta>1/2\),
\begin{equation}
\lvert S_X(\rho)\rvert
\le
\sum_{n\le X}\frac{\Lambda(n)}{n^{\beta}\log n}
\le
\sum_{p\le X}\frac{1}{p^{\beta}\log p}
+
O_\beta(1)
\ll_{\beta}
\begin{cases}
X^{1-\beta}/((1-\beta)\log X) & \beta<1,\\
\log\log X & \beta=1.
\end{cases}
\tag{upper}
\end{equation}
So if \(\beta\) is fixed \(>1/2\), \(S_X\) is **bounded as \(X\to\infty\)** by a convergent prime series when \(\beta>1\), and by a **finite** limit of the incomplete sum when \(\beta\le 1\):
\[
S_\infty(\rho)
:=
\sum_{n=2}^\infty\frac{\Lambda(n)}{n^{\rho}\log n}
=
-\log\bigl(1-p^{-\rho}\bigr)\text{-sum}
=
\log\zeta(\rho)
\quad(\operatorname{Re}\rho>1).
\]
**Critical remark:** for \(\beta\le 1\), the series \(\sum\Lambda(n)n^{-\rho}/\log n\) is the analytic continuation of \(\log\zeta\) only away from zeros and the pole.  
**At a zero \(\rho\),** \(\zeta(\rho)=0\), so \(\log\zeta\) has a logarithmic singularity: one **cannot** pass \(X\to\infty\) inside \(\log\zeta\).  
The partial sums \(S_X(\rho)\) at a zero are a different object — they need not converge.

---

## 2. Partial summation form

Let \(\psi(x)=\sum_{n\le x}\Lambda(n)\). Then
\begin{equation}
S_X(\rho)
=
\int_{2-}^{X}\frac{1}{x^{\rho}\log x}\,d\psi(x)
=
\frac{\psi(X)}{X^{\rho}\log X}
+
\int_{2}^{X}\psi(x)\,\frac{d}{dx}\Bigl(\frac{1}{x^{\rho}\log x}\Bigr)^{-1\text{ parts}}.
\tag{PS}
\end{equation}
More carefully (Stieltjes):
\begin{equation}
S_X(\rho)
=
\frac{\psi(X)}{X^{\rho}\log X}
+
\int_2^X\psi(x)\Biggl(
\frac{\rho}{x^{\rho+1}\log x}
+
\frac{1}{x^{\rho}(\log x)^2 x}
\Biggr)dx.
\tag{PS2}
\end{equation}
Using \(\psi(x)=x+O(x\exp(-c\sqrt{\log x}))\) (classical zero-free region) does **not** apply directly to produce a lower bound of \(S_X\) at a zero, because the main terms
\[
\int_2^X x\cdot\frac{\rho}{x^{\rho+1}\log x}\,dx
=
\rho\int_2^X\frac{dx}{x^{\rho}\log x}
\]
are related to the logarithmic integral in the \(\rho\)-direction and cancel against the structure that makes \(\zeta(\rho)=0\) only after full explicit formula input.

---

## 3. Explicit formula route

### 3.1 Explicit formula for \(\psi\)

For \(x>1\) not a prime power, the explicit formula reads schematically
\begin{equation}
\psi(x)
=
x
-
\sum_{\lvert\gamma\rvert\le T}\frac{x^{\rho}}{\rho}
-
\log(2\pi)
+
O\Bigl(\frac{x\log(xT)}{T}+\log x\Bigr),
\tag{EF}
\end{equation}
(with standard truncated forms; see Davenport, Ch. 17).

### 3.2 Substitution into (PS2)

Inserting (EF) into (PS2) produces three pieces:

| Piece | Schematic contribution to \(S_X(\rho_\star)\) |
|-------|-----------------------------------------------|
| Main \(x\) | \(\rho_\star\int_2^X x^{-\rho_\star}/(\log x)\,x^{-1}\cdot x\,dx=\rho_\star\int_2^X dx/(x^{\rho_\star}\log x)\) |
| Zero sum | \(-\sum_{\rho}\int_2^X (x^{\rho}/{\rho})\cdot(\rho_\star/(x^{\rho_\star+1}\log x))\,dx+\cdots\) |
| Error | Controlled for \(T,X\) linked |

The **self-term** \(\rho=\rho_\star\) in the zero sum is special:
\[
\int_2^X\frac{x^{\rho_\star}}{\rho_\star}\cdot\frac{\rho_\star}{x^{\rho_\star+1}\log x}\,dx
=
\int_2^X\frac{dx}{x\log x}
=
\log\log X-\log\log 2.
\]
So the self-contribution is order \(\log\log X\) **before** coefficients and truncations are balanced against the main term.

### 3.3 Formal self-term heuristic (not a proof)

Schematically,
\begin{equation}
S_X(\rho_\star)
\;\text{“}=\text{”}\;
\underbrace{\rho_\star\int_2^X\frac{dx}{x^{\rho_\star}\log x}}_{\text{main}}
-
\underbrace{\log\log X}_{\text{self}}
-
\sum_{\rho\neq\rho_\star}(\cdots)
+
O(\mathrm{trunc}).
\tag{heur}
\end{equation}
For \(\beta_\star>1/2\), the main integral converges as \(X\to\infty\):
\[
\int_2^\infty\frac{dx}{x^{\beta_\star}\log x}
<\infty
\quad(\beta_\star>1)\quad\text{or grows slowly for }\beta_\star\le 1.
\]
Actually \(\int_2^X x^{-\beta}/(\log x)\,dx\) for \(\beta>1\) converges; for \(1/2<\beta\le 1\) it grows like a truncated logarithmic integral in the \(\beta\)-scale.

The **self-term \(\log\log X\)** is the same shape as the Conrad–Goldfeld / Akatsuka on-line modulus phenomenon, but here it appears in the **phase sum at a zero**.

**Honesty freeze:** turning (heur) into a theorem requires:

1. Justified truncation of (EF) with explicit error.  
2. Proof that the sum over \(\rho\neq\rho_\star\) does **not** cancel the self \(\log\log X\).  
3. Control of the main term vs self-term coefficients (signs, complex factors \(1/\rho\)).  
4. Care that \(\rho_\star\) off the line makes \(x^{\rho_\star}=x^{\beta}x^{i\gamma}\) grow or decay.

**This is the pure core of a B\(_\theta\) attack — open.**

---

## 4. Conditional lemma form (what would suffice)

### Lemma form Bθ-1 (conditional — **not proved**)

> Assume a truncated explicit formula with error \(E(X,T)\) and
> \[
> \Biggl\lvert
> \sum_{\substack{\rho\neq\rho_\star\\ \lvert\gamma\rvert\le T}}
> \int_2^X\frac{x^{\rho-\rho_\star}}{\rho\,x\log x}\,dx
> \Biggr\rvert
> \le
> \tfrac12\log\log X
> \]
> for a sequence \(X\to\infty\) with \(T=T(X)\) admissible.  
> Then
> \[
> \lvert S_X(\rho_\star)\rvert
> \ge
> c\log\log X
> \]
> for some \(c>0\) and infinitely many \(X\).

**Status:** the displayed off-diagonal bound is **precisely the open estimate**. It is comparable in difficulty to standard problems about zeros’ vertical distribution (and may encode near-RH information if mishandled — L4 firewall: do not assume RH to prove B to prove RH).

### L4 non-circularity rule for this attack

| Allowed | Forbidden |
|---------|-----------|
| Classical zero-free regions | Assuming all zeros on the line to cancel off-diagonal |
| Density theorems (KLN, Ingham) | Assuming pair correlation that already encodes RH-scale spacing as a black box without tracking dependence |
| Explicit formula with classical remainder | Using \(\zeta(\rho_\star)=0\) to replace \(S_X\) by \(-\log Z\) without error control |

---

## 5. Alternative: resonance / Dirichlet polynomials

The sum
\[
D_X(t)=\sum_{n\le X}\frac{\Lambda(n)}{n^{\beta}\log n}\,n^{-it}
\]
at \(t=\gamma\) is a weighted Dirichlet polynomial.  
Classical resonance (Soundararajan, etc.) produces large values on **positive proportion** of \(t\in[T,2T]\), not necessarily at a zero ordinate.

**Obstruction:** zero ordinates are a thin set (density \(0\)). Resonance lower bounds do not automatically transfer to \(\{γ\}\).

**Mollified variant:** construct a mollifier \(M(s)\) so that \(M(\rho)S_X(\rho)\) is large on average over zeros off the line.  
This is essentially a **zero-detection / amplification** problem.  
**Status:** open; related to classical zero-density technology but with a phase objective.

---

## 6. What is unconditional today

| Statement | Status |
|-----------|--------|
| \(\lvert S_X(\rho)\rvert\ll_\beta X^{1-\beta}/\log X\) (\(\beta<1\)) | Proved (trivial) |
| \(S_X(\rho)\) need not converge as \(X\to\infty\) at a zero | Observation |
| Self-term \(\log\log X\) appears formally from EF | Heuristic bookkeeping |
| Off-diagonal cancellation bound | **Open** |
| Resonance at zero ordinates | **Open** |
| Conjecture B\(_\theta\) | **Open** |
| RH | **Open** |

---

## 7. Recommended pure sequence from here

```text
1. Write a fully rigorous truncated EF → S_X identity with explicit error
   (bookkeeping; classical)
2. Isolate self-term coefficient exactly (complex factor 1/ρ_★)
3. Bound off-diagonal under (ZD) only — see how much of loglog survives
4. If a positive proportion of loglog survives under (ZD), obtain
   conditional B_θ under density (still not RH)
5. Never feed RH into step 3
```

---

## 8. Non-claims

1. This note does **not** prove Conjecture B or B\(_\theta\).  
2. The self-term heuristic is **not** a theorem.  
3. No Category B constants.  
4. No RH.

---

## One-liner

> B\(_\theta\) attacks reduce to showing that the explicit-formula self-term \(\log\log X\) in \(S_X(\rho_\star)\) is not cancelled by other zeros; that off-diagonal estimate is the open pure problem.
