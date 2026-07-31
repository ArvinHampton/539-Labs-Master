# Finite products · Ivić multiplicity · Mass-with-A criteria

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. Axiom **ZLA**.  
**No claim** of (Iso_H), Mass-with-A, B_θ, or RH.

**Companions:**  
`RH_ND1_Stability_Resolve.md`,  
`RH_Iso_H_Classical_Constraints.md`,  
`RH_Akatsuka_GHK_Survey.md`,  
`RH_M1_2_Effective_Density.md`.

---

## 0. Status freeze

Three pure tasks completed in this pass. ND1 acceptance remains locked.  
Primary obligation **not** closed. Unconditional B_θ and RH **open**.

---

## 1. Finite-product approximation off the line

### Classical hybrid (GHK), unconditional for \(\sigma\ge 0\), \(\lvert t\rvert\ge 2\)

\[
\zeta(s)
=
P_X(s)\,Z_X(s)
\Biggl(
1
+
O\Biggl(
\frac{X^{K+2}}{(\lvert s\rvert\log X)^{K}}
+
X^{-\sigma}\log X
\Biggr)
\Biggr).
\]

- \(P_X\): truncated Euler product (primes / von Mangoldt).  
- \(Z_X\): truncated Hadamard factor over zeros, built from the same \(E_1\) / \(U\) kernel already used in residual and M1.2 estimates.

### Gonek finite Euler products

Gonek’s finite Euler products approximate \(\zeta\) in the critical strip. Under RH the approximation is strong to the right of the critical line; a partial converse says that a good approximation forces at most finitely many zeros far to the right. The approximating functions themselves satisfy an “RH” (all but finitely many zeros on \(\operatorname{Re}=1/2\)), with simple, repelling zeros when the truncation is not too long.

### Role in the programme

Finite products control the **prime side** and justify the shape of the residual formula.  

They **do not** bound the Lip constant \(A(u_k)\) of \(\Phi^\star\). That constant is driven by the **zero side** (same-abscissa and near-abscissa competitors).

**Standing:** classical infrastructure — **recorded**, not a new theorem.

---

## 2. Ivić multiplicity bounds

**Source:** Ivić, arXiv:math/0501434 (and related multiplicity literature).

For \(1/2<\beta<1\),
\begin{equation}
m(\beta+i\gamma)
\le
\frac{1}{\log\bigl(1/(2-2\beta)\bigr)}
\Bigl(
\max\log\lvert\zeta\rvert
+
O(\log\log\gamma)
\Bigr).
\tag{Ivić-local}
\end{equation}

Uniformly,
\begin{equation}
m(\beta+i\gamma)
\ll
(1-\beta)^{3/2}\log\gamma
+
\log\log\gamma.
\tag{Ivić-unif}
\end{equation}

If \(m/\log\log\gamma\to\infty\), then \(\beta\) is forced left of the classical zero-free region shape:
\begin{equation}
\beta
\le
1
-
C\Biggl(\frac{m}{\log\gamma}\Biggr)^{2/3}.
\tag{Ivić-left}
\end{equation}

Near \(\sigma=1\) (\(\beta\ge 1-(\log\gamma)^{-\delta}\)),
\begin{equation}
m
\ll_\delta
\frac{\log\gamma}{\log\log\gamma}.
\tag{Ivić-near1}
\end{equation}

### What this controls for Mass-with-A

Each zero contributes a term multiplied by its **multiplicity** in the Lip sum \(A\). Ivić therefore **rules out a single enormous term** when \(\beta_\star\) is not close to \(1\).

### What it does **not** control

The **number of distinct ordinates** on the vertical line \(\operatorname{Re}=\beta_\star\).  
Many moderate **simple** zeros at the same abscissa remain the open threat to \(A\).

**Standing:** classical — **recorded**. Single-term size in \(A\) controlled by Ivić — **proved as a consequence** for Mass-with-A bookkeeping.

---

## 3. Mass-with-A divergence condition (clarified)

### Setup

Under **(RM)** alone, S11 already supplies a positive-density set \(K_\star\) of locked points with
\[
\Phi^\star(u_k)\ge c_\star>0.
\]
Stability length:
\begin{equation}
\delta_k
=
\frac{c_\star}{2\max\bigl(A(u_k),1\bigr)}.
\tag{δ}
\end{equation}

**Mass-with-A** asks whether
\begin{equation}
\sum_{\substack{k\in K_\star\\ u_k\le U}}
\frac{\delta_k}{u_k}
\tag{Mass-A}
\end{equation}
**diverges** as \(U\to\infty\).

### Sufficient conditions (proved as **implications**)

| Criterion | Hypothesis | Conclusion |
|-----------|------------|------------|
| **A (polylog Lip)** | \(A(u_k)=O((\log u_k)^{C})\) on a positive-density subset of \(K_\star\) | Mass-with-A (since \(\sum 1/(k(\log k)^{C})\) diverges for every \(C\)) |
| **B (power Lip)** | \(A\ll u_k^{\theta}\) for some \(\theta<1\) on a positive-density subset | Mass-with-A |
| **C (Iso_H)** | \(A=O(1)\) on the good set | recovers ND1; Mass-with-A immediate |
| **D (average Lip)** | Average of \(A\) over \(K_\star\) up to \(K\) is \(O((\log K)^{C})\) and a second-moment bound prevents concentration | Markov ⇒ positive-density polylog subset ⇒ Criterion A |

### Open core

A **polylog** (or **average-polylog**) bound on \(A\) along the good locked set.

L2 control of phases (\(\sum 1/\gamma^{2}<\infty\)) is already in S11; **upgrading that to average control of \(A\)** is the sharpest pure next step.

### Logical map after this pass

```text
(RM)
  → S11: good locked points
  → polylog A on a positive-density subset  → Mass-with-A  → B_θ
  → Iso_H                                   → Mass-with-A  → B_θ
```

Both implications after the polylog / Iso_H hypothesis are **proved**.  
The hypotheses themselves remain **open**.

---

## 4. Scoreboard

| Item | Standing |
|------|----------|
| GHK hybrid / Gonek finite products | Classical |
| Ivić multiplicity bounds | Classical |
| Single-term size in \(A\) controlled by Ivić | **Proved** (bookkeeping consequence) |
| Number of distinct ordinates on \(\operatorname{Re}=\beta_\star\) | **Open** |
| Polylog \(A\) on positive-density subset of \(K_\star\) | **Open** |
| (RM)+(Mass-with-A) ⇒ B_θ | **Proved implication** |
| (RM)+(Iso_H) ⇒ B_θ | **Proved implication** (ND1) |
| Unconditional B_θ / RH | **Open** |

---

## 5. Next pure attack

**Upgrade L2 phase control on the good locked set to average or pointwise polylog control of the Lip constant \(A\).**

(Equivalently: prove Criterion A or D under (RM) alone.)

---

## One-liner

**Finite products control the prime side but not Lip \(A\); Ivić controls multiplicity but not ordinate count on \(\operatorname{Re}=\beta_\star\); Mass-with-A follows from polylog \(A\) on a positive-density subset of good locks — that polylog bound is the open core.**

*Per aspera ad astra.*
