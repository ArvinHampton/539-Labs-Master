# M1.3-bis — Paths Toward \(\log\log X\) Scale Growth

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Strength:** pure design + conditional reductions.  
**Does not prove Conjecture B or RH.**

Companion: `RH_M1_3_Path_Design.md` (P1–P4 taxonomy), `RH_M1_2_Line_By_Line.md` (remainder).

---

## 0. Why P1 is not enough

From M1.2 line-by-line: on an isolated semicircle about \(\rho_\star\),
\[
\bigl\lvert\Delta\theta_X-m\pi\bigr\rvert
\le
2\sup R_{\mathrm{bound}}.
\]
Classically \(R_{\mathrm{bound}}\gg\log|\gamma|\) is possible from the medium sum, so
\[
m\pi-2R_{\mathrm{bound}}
\]
need **not** be positive at large height.  
Even if \(R_{\mathrm{bound}}=O(1)\) under strong spacing, one only gets an **\(X\)-independent** jump of size \(\asymp m\).  
Conjecture B asks for growth in \(X\) (or unboundedness along a sequence \(X_n\to\infty\)).

**M1.3-bis** = mechanisms that can produce
\[
\bigl\lvert\theta_X(s_\star)\bigr\rvert
\quad\text{or}\quad
\bigl\lvert A_X(\beta,\gamma)\bigr\rvert
\to\infty
\quad(X\to\infty)
\]
at an off-line zero \(\rho_\star=\beta+i\gamma\).

---

## 1. Three pure mechanisms

### Mechanism α — Multi-\(X\) monodromy family (primary candidate)

For each \(X\ge 3\), let \(\Gamma_X\) be a semicircle of radius \(r_X=c_r/\log X\) about \(\rho_\star\) (Hypothesis (Iso\(_X\)): no other zero in the \(2r_X\)-disk).

If M1.2′ gives \(R_{\mathrm{bound}}(X,\cdot)\le\varepsilon_0<m\pi/4\) uniformly on \(\Gamma_X\) for all large \(X\), then
\begin{equation}
\bigl\lvert\Delta_{\Gamma_X}\theta_X\bigr\rvert\ge\tfrac12 m\pi
\quad\text{for all large \(X\)}.
\tag{α-jump}
\end{equation}
This still does **not** grow with \(X\). To upgrade:

**Observation (incomplete product drift).**  
As \(X\) increases, \(\theta_X=\operatorname{Im}\sum_{n\le X}\Lambda(n)n^{-s}/\log n\) gains new prime-power terms.  
At a **fixed** point \(s\) with \(\zeta(s)\neq 0\),
\[
\theta_{X'}(s)-\theta_X(s)
=
\operatorname{Im}\sum_{X<n\le X'}\frac{\Lambda(n)}{n^s\log n}.
\]
At a zero, \(\zeta(\rho_\star)=0\), so one cannot evaluate \(\log\zeta(\rho_\star)\). Work instead at a point \(s_X\) on \(\Gamma_X\), e.g. \(s_X=\rho_\star+r_X\).

**Conditional α-bis.**  
If there exists a sequence \(X_j\to\infty\) and points \(s_j\in\Gamma_{X_j}\) such that the increments
\[
\eta_j:=\theta_{X_{j+1}}(s_j)-\theta_{X_j}(s_j)
\]
have a **systematic bias** (e.g. \(\sum_{j=1}^J\eta_j\to\infty\)), then \(\theta_{X_J}(s_J)\) can grow.  
**Status:** no such bias theorem is known off the line without RH-strength input. On the line, Akatsuka-type results control **modulus**, not a growing argument.

### Mechanism β — Horizontal path + incomplete product (secondary)

At height \(\gamma\), path \(\sigma:\beta\to\beta-\delta\) with \(\delta>0\) small fixed, \(X\) large.

\[
\frac{\partial\theta_X}{\partial\sigma}
=
\operatorname{Im}\frac{\partial}{\partial\sigma}\log P_X
=
-\operatorname{Im}\sum_{n\le X}\frac{\Lambda(n)}{n^{\sigma+i\gamma}}.
\]
Integrating,
\[
\theta_X(\beta-\delta,\gamma)-\theta_X(\beta,\gamma)
=
-\operatorname{Im}\int_{\beta-\delta}^{\beta}\sum_{n\le X}\Lambda(n)\,n^{-\sigma-i\gamma}\,d\sigma.
\]
This is a **Dirichlet polynomial integral**. Large values of Dirichlet polynomials are classical (e.g. resonance method), but producing a lower bound **exactly at the ordinate of a zero** is a different problem (the zero constraint correlates \(n^{-i\gamma}\) with the zeros via the explicit formula).

**Status:** open as a pointwise lower bound at off-line zeros.

### Mechanism γ — Multi-scale smoothed phase \(A_X\) (O3 route)

Recall
\[
A_X(\sigma,t)=\int_1^2\theta_{X^v}(\sigma+it)\,\phi(v)\,dv.
\]
If \(\theta_x\) at \(x\in[X,X^2]\) stays within \(o(L)\) of a large base value \(L=\theta_X\), then \(A_X\) is large.

**Lemma (slow variation — pure, elementary).**  
For \(\sigma\ge \sigma_0>0\) and \(X\ge 3\),
\begin{equation}
\bigl\lvert\theta_{X^2}(s)-\theta_X(s)\bigr\rvert
\le
\sum_{X<n\le X^2}\frac{\Lambda(n)}{n^\sigma\log n}
\le
\sum_{X<p\le X^2}\frac{1}{p^\sigma\log p}
+
O\bigl(X^{-\sigma/2}\bigr).
\tag{slow}
\end{equation}
By partial summation / prime number theorem,
\begin{equation}
\sum_{X<p\le X^2}p^{-\sigma}
\ll
\begin{cases}
X^{1-\sigma}/((1-\sigma)\log X) & 0<\sigma<1,\\
\log\log X^2-\log\log X=\log 2 & \sigma=1,\\
X^{1-\sigma} & \sigma>1.
\end{cases}
\tag{prime-sum}
\end{equation}
Hence for **fixed** \(\beta>1/2\) and \(s=\beta+i\gamma\),
\begin{equation}
\bigl\lvert\theta_{X^2}-\theta_X\bigr\rvert
\ll_{\beta}
\frac{X^{1-\beta}}{\log X}.
\tag{slow-off}
\end{equation}
In particular, if \(\beta>1/2\) is fixed and \(X\to\infty\), the short-interval phase drift **tends to 0**.

**Corollary (O3 off-line).**  
If \(\beta>1/2\) is fixed and \(\lvert\theta_X(\beta,\gamma)\rvert\to\infty\) along a sequence \(X\to\infty\), then automatically \(\lvert A_X(\beta,\gamma)\rvert\to\infty\) along a subsequence (because (slow-off) \(\to 0\)).

**This reduces Conjecture B at fixed off-line abscissa to growth of \(\theta_X\) itself** — smoothing is free for \(\beta>1/2\).

For \(\beta=1/2\), (slow) only gives \(O(1)\) control of the short product (harmonic sum of \(p^{-1/2}\) over dyadic intervals grows like \(X^{1/2}/\log X\) — large). On-line smoothing is harder; that is Conjecture A territory.

---

## 2. M1.3-bis formal targets

### Target T1 (weak — order-\(m\) for all large \(X\))

Under (Iso\(_X\)) and \(R_{\mathrm{bound}}(X)\le\varepsilon_0<m\pi/4\) on \(\Gamma_X\) for all large \(X\),
\[
\bigl\lvert\Delta_{\Gamma_X}\theta_X\bigr\rvert\ge\tfrac12 m\pi.
\]
**Open** at large height because classical M1.2 medium sum is too big (see M1.2 line-by-line bottleneck).

### Target T2 (strong — growth in \(X\))

There exists \(c>0\) and \(X_n\to\infty\) with
\[
\bigl\lvert\theta_{X_n}(\beta,\gamma)\bigr\rvert
\ge
c\log\log X_n.
\]
**Open.** This is essentially Conjecture B before smoothing (and by O3, equivalent to Conjecture B for fixed \(\beta>1/2\)).

### Target T3 (structural)

Prove that \(\theta_X(\beta,\gamma)\) **cannot stay bounded** as \(X\to\infty\) if \(\zeta(\beta+i\gamma)=0\) and \(\beta\neq 1/2\).  
**Open.** Closest literature: Conrad–Goldfeld modulus asymptotics are on the **line** and are RH-strength when assumed; they do not give off-line argument blow-up.

---

## 3. What would close T1 (checklist)

| Requirement | Source |
|-------------|--------|
| Isolation at scale \(1/\log X\) for a sequence of \(X\) | Zero gap / multiplicity control — open in general |
| \(R_{\mathrm{bound}}=O(1)\) or \(o(1)\) on \(\Gamma_X\) | Needs \(\Sigma_{\mathrm{med}}\ll 1\), beyond classical \(O(\log|t|)\) |
| Branch control on \(\Gamma_X\) | Path design (doable) |
| GHK regime \(X=(\log|\gamma|)^{O(1)}\) | Compatible with isolation scale |

**Honest assessment:** T1 is a **standard-hard** analytic number theory problem (local zero spacing + hybrid remainder), not a formalism gap.

---

## 4. What would close T2 (checklist)

| Requirement | Source |
|-------------|--------|
| Either T1 for many \(X\) **plus** biased multi-\(X\) increments, **or** | Mechanism α |
| Direct lower bound for \(\lvert\sum_{n\le X}\Lambda(n)n^{-\rho_\star}/\log n\rvert\) | Dirichlet polynomial at a zero — open |
| Or resonance / mollifier forcing large \(\theta_X\) at \(\rho_\star\) | Related to O-Moll in older notes — open |

No classical theorem currently supplies T2.

---

## 5. Reduction diagram

```text
Conjecture B (β>1/2 fixed)
        │
        │  O3 (proved: slow variation → 0)
        ▼
  |θ_X(β,γ)| → ∞          ←── Target T2 / T3
        │
        ├──?── multi-X increments (α)     open
        ├──?── Dirichlet poly lower bound (β) open
        └──?── hybrid + spacing (T1 then grow) open

M1.2 classical ──► R_bound ≫ log|t| ──► blocks naive T1 at large height
M1.2 + (ZD)+gaps ──► possible T1 ──► still not T2 without X-growth
```

---

## 6. Non-claims

1. M1.3-bis does **not** prove Conjecture B.  
2. O3 off-line slow variation **is** proved (elementary prime sums) for \(\beta>1/2\).  
3. No model constants.  
4. RH open.

---

## One-liner

**For fixed off-line \(\beta>1/2\), smoothing is free (O3); Conjecture B reduces to \(\lvert\theta_X\rvert\to\infty\), which no classical path (P1 half-turn, multi-\(X\), or horizontal Dirichlet polynomial) currently delivers.**
