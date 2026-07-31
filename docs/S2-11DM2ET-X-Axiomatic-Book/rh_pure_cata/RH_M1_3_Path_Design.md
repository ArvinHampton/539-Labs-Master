# M1.3 — Path Design for Large \(m\arg(s-\rho)\)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Strength:** design note + conditional inequality form.  
**Not claimed:** existence of a path that proves Conjecture B or RH.

---

## 1. Goal

Given a putative zero \(\rho_\star=\beta+i\gamma\) with multiplicity \(m\ge 1\) and \(\beta\neq 1/2\), produce a rectifiable path \(\Gamma\) in the strip such that

\[
\Delta_\Gamma\theta_X
:= \int_\Gamma d\theta_X
= m\,\Delta_\Gamma\arg(s-\rho_\star)
- \Delta_\Gamma\operatorname{Im}\mathcal R_X^{(\mathrm{EP})}
+ O\bigl(\mathrm{length}\cdot\lVert\varepsilon_X\rVert_\infty\bigr)
\]

satisfies

\[
\bigl\lvert\Delta_\Gamma\theta_X\bigr\rvert
\ge
c\,m\log\log X
\quad\text{(target scale)}
\]

or at least

\[
\bigl\lvert\Delta_\Gamma\theta_X\bigr\rvert
\ge
\tfrac12 m\pi
\quad\text{(order-\(m\) half-turn; weaker)}.
\]

Then pass to smoothed \(A_X\) by slow variation of \(\theta_x\) for \(x\in[X,X^2]\) (O3).

**Conditional engine:** if M1.2 gives \(\lvert\operatorname{Im}\mathcal R\rvert\le R_{\mathrm{bound}}\) uniformly on \(\Gamma\) and

\[
m\bigl\lvert\Delta_\Gamma\arg(s-\rho_\star)\bigr\rvert
> 2\sup_\Gamma R_{\mathrm{bound}} + 1,
\]

then \(\lvert\Delta_\Gamma\theta_X\rvert\ge 1\) (or better).

---

## 2. Candidate paths

### Path P1 — Small circle about \(\rho_\star\)

\[
\Gamma_\circ:
\quad
s(\varphi)=\rho_\star + r e^{i\varphi},
\quad
\varphi:0\to\pi
\quad\text{(semicircle)},
\quad
r\asymp \frac{1}{\log(|\gamma|+2)}.
\]

| Pros | Cons |
|------|------|
| \(\Delta\arg(s-\rho_\star)=\pi\) (half-turn) exactly for simple geometry | Radius must avoid other zeros |
| Local \(m\Delta\arg=m\pi\) | Only order-\(m\) jump — **not** yet \(\log\log X\) scale |
| Classic argument principle flavour | Medium zeros in \(r\)-neighbourhood kill the bound if cluster |

**Conditional lemma form (P1).**  
If \(r=c_r/\log(|\gamma|+2)\), no other zero in \(\lvert s-\rho_\star\rvert\le 2r\), and

\[
\sup_{s\in\Gamma_\circ}R_{\mathrm{bound}}(X,s)\le \varepsilon_0 < m\pi/4,
\]

then

\[
\bigl\lvert\Delta_{\Gamma_\circ}\theta_X\bigr\rvert \ge m\pi - 2\varepsilon_0 \ge \tfrac12 m\pi.
\]

**Honesty:** this gives a **fixed** angular jump of order \(m\), independent of \(X\).  
It is **not** yet the full \(\log\log X\) target for Conjecture B.  
Needs **M1.3-bis** (long path / many windings / growth of incomplete product) or **M1.4** smoothing over a family of \(X\).

### Path P2 — Horizontal segment toward the critical line

\[
\Gamma_{\mathrm{h}}:
\quad
s(\sigma)=\sigma+i\gamma,
\quad
\sigma:\beta\to\tfrac12
\quad\text{(or \(\beta\to\beta-\delta\))}.
\]

| Pros | Cons |
|------|------|
| Connects off-line zero to line | \(\arg(s-\rho_\star)\) change is **not** automatically large |
| Compatible with functional equation symmetry | Remainder may accumulate over long segment |
| Natural for comparing Conjecture A vs B at same height | Needs careful continuous branch of \(\theta_X\) |

**Use:** comparative diagnostics (L5) more than primary M1.3 engine.

### Path P3 — Vertical segment at fixed \(\sigma=\beta\)

\[
\Gamma_{\mathrm{v}}:
\quad
s(t)=\beta+it,
\quad
t:\gamma-H\to\gamma+H.
\]

Useful for average phase drift; weaker for single-zero forcing.

### Path P4 — “Log-spiral” / expanding radius (M1.3-bis candidate)

\[
s(\varphi)=\rho_\star + r(\varphi)e^{i\varphi},
\quad
r(\varphi)=r_0 e^{\kappa\varphi},
\quad
\varphi:0\to\Phi.
\]

Designed so that \(m\Phi\) grows while M1.2 still controls \(\operatorname{Im}\mathcal R\) on the spiral.  
**Open:** whether GHK errors allow \(\Phi\to\infty\) slowly with \(X\).

---

## 3. Branch and continuity rules

1. Fix \(\theta_X(s)\) continuous along \(\Gamma\) by integrating \(d\arg P_X=\operatorname{Im}(P_X'/P_X)\,ds\).  
2. Equivalent discrete construction: product over primes with cumulative principal log, updated continuously in \(s\).  
3. Do **not** use \(\operatorname{Arg}(\prod_p)\) recomputed independently at each point (branch jumps).  
4. Record monodromy around \(\rho_\star\): expected \(+m\) in \(\frac1{2\pi}\Delta\arg\zeta\), split between \(P_X\) and \(Z_X\).

---

## 4. From path jump to \(A_X\) (O3 sketch)

Suppose for a sequence \(X_n\to\infty\) there exist paths \(\Gamma_n\) with

\[
\bigl\lvert\Delta_{\Gamma_n}\theta_{X_n}\bigr\rvert\ge L_n\to\infty.
\]

If \(\theta_x(s)\) varies slowly for \(x\in[X,X^2]\) at each fixed \(s\in\Gamma_n\) — e.g.

\[
\bigl\lvert\theta_{X^v}-\theta_X\bigr\rvert\le \eta_n,
\quad v\in[1,2],
\quad \eta_n=o(L_n),
\]

then

\[
\bigl\lvert A_X(\sigma,t)\bigr\rvert
\]

is large at some point of \(\Gamma_n\) (mean-value / integral of continuous phase).  

**Slow-variation estimate** is part of M1.4 / O3: difference \(\theta_{X^2}-\theta_X\) is a short Euler product over \(X<p\le X^2\), size

\[
\ll \sum_{X<p\le X^2}p^{-\sigma}
\ll
\begin{cases}
X^{1/2-\sigma}(\log X)^{-1}\text{-scale heuristics},\\
\text{rigorous: prime-number theorem bounds.}
\end{cases}
\]

Off-line with \(\sigma=\beta>1/2\), the short product is smaller; on \(\sigma<1/2\) larger — track carefully.

---

## 5. Conditional package (M1.2 + P1)

> **Proposition (conditional, not proved end-to-end).**  
> Assume Lemma M1.2 with \(R_{\mathrm{bound}}\le\varepsilon_0\) on the semicircle \(\Gamma_\circ\) of radius \(r=c_r/\log(|\gamma|+2)\) about a zero \(\rho_\star\) of multiplicity \(m\), and assume no other zero in the \(2r\)-disk.  
> Then \(\lvert\Delta_{\Gamma_\circ}\theta_X\rvert\ge\tfrac12 m\pi\).  
> In particular \(\theta_X\) cannot stay uniformly small in a neighbourhood of an off-line zero.

**Gap to RH:**  
- Needs uniform M1.2 on \(\Gamma_\circ\) **without** assuming RH.  
- Order-\(m\) jump ≠ contradiction yet; need global comparison with on-line Conjecture A and functional equation, or growth \(\to\infty\) along \(X\to\infty\) (M1.3-bis).  
- Zero isolation at scale \(1/\log\gamma\) fails if zeros are too clustered (density / multiplicity issues).

---

## 6. Recommended analytic order

```text
1. Prove M1.2 on compact sets away from zeros          [medium+far only]
2. Prove M1.2 on P1 semicircle under isolation          [local+medium]
3. Establish isolation scale for simple zeros           [zero gaps / density]
4. Upgrade P1 → P4 or multi-X family for loglog growth  [M1.3-bis]
5. Slow variation → A_X                                 [O3 / M1.4]
6. Compare to Conjecture A on the line                  [functional eq]
```

---

## 7. Numeric path probe (diagnostic only)

Planned script: `scripts/rh_M1_3_path_diagnostic.py` (stub parameters in L5 / M1.2 scripts for now).

| Probe | Method |
|-------|--------|
| Semicircle about first zero height at \(\sigma=0.6\) (non-zero) | Integrate continuous \(d\theta_X\) |
| Semicircle about true zero at \(\sigma=1/2\) | Expect order-\(m\) interaction with \(Z_X\) |
| Compare \(\Delta\theta_X\) vs crude \(R_{\mathrm{bound}}\) | Sanity check M1.2 majorants |

**Policy:** `NO_RH_CLAIM`. Finite \(X\) only.

---

## 8. Relation to classical \(S(t)\)

Horizontal argument change of \(\zeta\) itself near an off-line zero is classical (argument principle).  
M1.3 is **not** that statement: it concerns **\(\arg P_X\)**, the Euler factor in the GHK split.  
Conflating \(S(t)\) with \(\theta_X\) is a category error in this programme.

---

## 9. Bottom line for M1.3

| Deliverable | Standing |
|-------------|----------|
| Path taxonomy P1–P4 | Written |
| Conditional P1 half-turn | Schematic |
| Full \(\log\log X\) growth path | **Open** (M1.3-bis) |
| Numeric path diagnostic | Pending / partial via M1.2 sketch |
| RH | **Open** |
