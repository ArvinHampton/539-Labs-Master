# Programme Baseline — Pure Cat A Objects

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
All definitions below are the **only** load-bearing objects for the pure track.

---

## 1. Partial Euler product

For \(s=\sigma+it\in\mathbb{C}\) and \(x\ge 2\),

\[
P_x(s)
:=\prod_{p\le x}\bigl(1-p^{-s}\bigr)^{-1},
\]

principal branch of \(\log\) starting from \(P_2\) with continuous cumulative argument along increasing primes:

\[
\theta_x(s)
:=\arg P_x(s)
=\sum_{p\le x}\arg\bigl(1-p^{-s}\bigr)^{-1}
\quad\text{(continuous in \(x\) via cumulative principal args of factors)}.
\]

\[
U_x(s)
:=\log\lvert P_x(s)\rvert
=\sum_{p\le x}\bigl(-\log\lvert 1-p^{-s}\rvert\bigr).
\]

**GHK-smoothed cousin** (when needed):

\[
P_X^{\mathrm{GHK}}(s)
=\exp\Biggl(\sum_{n\le X}\frac{\Lambda(n)}{n^s\log n}\Biggr)
\quad\text{or the \(v\)-smoothed \(\widetilde P_X\)}.
\]

The programme treats \(\theta_x\) from the literal Euler product as the primary L5 object; GHK \(P_X\) is the primary M1 analytic object. They differ by a controlled prime-power / smoothing discrepancy (to be tracked when comparing).

---

## 2. Smoothed phase \(A_X\)

Fix a \(C^\infty\) bump \(\phi\) supported on \((1,2)\) with \(\int_1^2\phi=1\), \(\phi\ge 0\).

\[
A_X(\sigma,t)
:=\int_1^2 \theta_{X^v}(\sigma+it)\,\phi(v)\,dv.
\]

Optional smoothed modulus:

\[
\mathcal U_X(\sigma,t)
:=\int_1^2 U_{X^v}(\sigma+it)\,\phi(v)\,dv.
\]

---

## 3. Conjectures (not theorems)

### Conjecture A (on-line control)

There exist \(C<\infty\) and a family of scales \(X=X(t)\) (e.g. \(X=(\log(|t|+3))^A\)) such that for all ordinates of interest,

\[
\bigl\lvert A_X\bigl(\tfrac12,t\bigr)\bigr\rvert \le C
\quad\text{or a slow envelope such as \(C\log\log\log(|t|+16)\).}
\]

(Exact envelope is part of the formalization — L1.)

### Conjecture B (off-line growth)

If \(\rho=\beta+i\gamma\) is a nontrivial zero with \(\beta\neq 1/2\), then there exists a sequence \(X_n\to\infty\) with

\[
\bigl\lvert A_{X_n}(\beta,\gamma)\bigr\rvert \to\infty
\]

(or at least \(\gg\log\log X_n\)).

---

## 4. Target lemma (schematic)

**Target.** Under Conjectures A/B + functional equation + classical zero-free technology, every nontrivial zero satisfies \(\beta=1/2\).

**Missing pure steps:** L1 definition hygiene; L2 on-line bounds; L3 off-line lower bound; L4 no circular RH.  
**Mechanism for L3:** M1 (explicit formula / GHK split) primary; M2 harmonic conjugate of \(U_x\); M3 complex phase of \(\log\log\) (weak).

---

## 5. GHK hybrid (literature theorem — input)

\[
\zeta(s)=P_X(s)Z_X(s)
\Biggl(1+O_K\Biggl(\frac{X^{K+2}}{(|s|\log X)^K}\Biggr)+O(X^{-\sigma}\log X)\Biggr),
\]

\[
Z_X(s)=\exp\Biggl(-\sum_{\rho}U\bigl((s-\rho)\log X\bigr)\Biggr),
\quad
U(z)=\int_0^\infty u(x)E_1(z\log x)\,dx.
\]

---

## 6. Forbidden baseline pollution

Do **not** place in definitions or lemma hypotheses:

- \(539.9\), \(\mu\), \(E_{\mathrm{leak}}\), brane/spin debit
- Resonant Algebra residual operators as zeta objects
- Experimental Loschmidt echo parameters

---

## 7. L5 policy

L5 code may compute \(\theta_x\), \(U_x\), \(A_X\), \(\lvert\zeta\rvert\) at finite points.  
Output status string must include `NO_RH_CLAIM`.  
Finite-range excesses (on vs off) are **not** evidence for Conjecture B.
