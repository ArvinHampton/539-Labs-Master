# Omega-type lower bound for the hybrid discrepancy

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. Axiom **ZLA**. No model constants.  
**Does not prove RH or the target lemma.**  
**Does:** prove a rigorous **Omega** lower bound for \(\lvert\theta_X\rvert\) and \(\lvert\Delta_X\rvert=\lvert\arg\zeta-\arg Z_X\rvert\) of size \(\gg\sqrt{\log\log X}\) on the critical line; freeze the typical vs strong-scale distinction.

**Companions:** `RH_OPC_Partial_Resolution.md`, `RH_OPC_Conversion_Gap.md`, `RH_Remaining_Analytic_Obligations.md`.

---

## 0. Status freeze (as stated)

| Fact | Standing claim |
|------|----------------|
| Omega results for \(S(t)\) on the critical line | **Classical** (Montgomery, Titchmarsh, Soundararajan, …) |
| Analogous Omega for \(\arg\zeta-\arg Z_X\) (on or off the line) prior to this note | **Not** a standard named theorem in the programme ledger |
| Typical size (heuristic / \(L^2\)) | \(\asymp\sqrt{\log\log X}\) |
| Strong target-lemma scale | \(\gg\log\log X\) — **larger**; needs stronger Omega points or a **revised target** |
| O-PC / O-TL / RH | **Remain open** at strong scale |
| Distinction typical vs Omega | **Explicit** in the programme: remaining core for O-TL is **strong** Omega, not typical size |

---

## 1. Notation

For \(X\ge 3\) and \(t\in\mathbb{R}\),
\begin{equation}
D_X(t)
:=
\sum_{n\le X}
\frac{\Lambda(n)}{n^{1/2}\log n}\,
e^{-it\log n}
=
\log P_X\bigl(\tfrac12+it\bigr),
\tag{Ω-D}
\end{equation}
so
\[
\theta_X\bigl(\tfrac12+it\bigr)
=
\operatorname{Im} D_X(t)
\]
with the continuous branch of \(\arg P_X\) equal to \(\operatorname{Im}\log P_X\) (entire zero-free \(P_X\)).

With continuous GHK branches as in `RH_OPC_Partial_Resolution.md`,
\begin{equation}
\Delta_X\bigl(\tfrac12+it\bigr)
:=
\arg\zeta\bigl(\tfrac12+it\bigr)
-
\arg Z_X\bigl(\tfrac12+it\bigr)
=
\theta_X\bigl(\tfrac12+it\bigr)
+
\operatorname{Im}\mathcal{E}_{\mathrm{GHK}}\bigl(\tfrac12+it;X,K\bigr).
\tag{Ω-Δ}
\end{equation}

---

## 2. Mean-square of the partial product log

**Lemma Ω-MS.**  
For \(X\ge 3\),
\begin{equation}
\lim_{T\to\infty}
\frac1T
\int_0^T
\bigl\lvert D_X(t)\bigr\rvert^2\,dt
=
\sum_{n\le X}
\frac{\Lambda(n)^2}{n\,(\log n)^2}.
\tag{Ω-MS}
\end{equation}
In particular, writing \(a_n=\Lambda(n)/(n^{1/2}\log n)\),
\[
\sum_{n\le X}a_n^2
=
\sum_{n\le X}
\frac{\Lambda(n)^2}{n\,(\log n)^2}
\ge
\sum_{p\le X}
\frac1p
\sim
\log\log X.
\]

**Proof.**  
Expand \(\lvert D_X\rvert^2=\sum_{n,m\le X}a_n\overline{a_m}\,e^{-it(\log n-\log m)}\).  
Integrate in \(t\in[0,T]\) and let \(T\to\infty\): off-diagonal terms \(n\neq m\) average to \(0\) because \(\log n\neq\log m\). Diagonal terms give \(\sum a_n^2\).  
For primes, \(\Lambda(p)^2/(p(\log p)^2)=1/p\). Mertens: \(\sum_{p\le X}1/p=\log\log X+O(1)\). □

**Lemma Ω-MS-Im.**  
Under the same hypotheses,
\begin{equation}
\lim_{T\to\infty}
\frac1T
\int_0^T
\bigl(\operatorname{Im} D_X(t)\bigr)^2\,dt
=
\frac12
\sum_{n\le X}
\frac{\Lambda(n)^2}{n\,(\log n)^2}.
\tag{Ω-MS-Im}
\end{equation}
(The same holds for \(\operatorname{Re} D_X\).)

**Proof.**  
Write \(D_X=\sum a_n e^{-it\lambda_n}\) with \(a_n\in\mathbb{R}\), \(\lambda_n=\log n\).  
Then \(\operatorname{Im} D_X=-\sum a_n\sin(t\lambda_n)\), and
\[
\frac1T\int_0^T\sin(t\lambda_n)\sin(t\lambda_m)\,dt
\to
\tfrac12\delta_{nm}
\]
for \(\lambda_n\neq 0\) (all \(n\ge 2\)). Cross terms vanish; diagonal gives \(\tfrac12\sum a_n^2\). □

---

## 3. Omega for \(\theta_X\) at typical scale (proved)

**Theorem Ω-θ (Omega for the partial-product phase).**  
For every fixed \(X\ge 3\),
\begin{equation}
\limsup_{t\to\infty}
\bigl\lvert\theta_X\bigl(\tfrac12+it\bigr)\bigr\rvert
\ge
\Biggl(
\frac12
\sum_{n\le X}
\frac{\Lambda(n)^2}{n\,(\log n)^2}
\Biggr)^{1/2}
\gg
\sqrt{\log\log X}.
\tag{Ω-θ}
\end{equation}
More precisely: there is an absolute \(c>0\) such that for all \(X\ge 3\),
\[
\limsup_{t\to\infty}
\bigl\lvert\theta_X\bigl(\tfrac12+it\bigr)\bigr\rvert
\ge
c\sqrt{\log\log X}.
\]

**Proof.**  
Let \(M_X^2:=\tfrac12\sum_{n\le X}\Lambda(n)^2/(n(\log n)^2)\).  
By Lemma Ω-MS-Im, the mean square of \(\theta_X(\tfrac12+it)\) equals \(M_X^2\).  
If \(\lvert\theta_X(\tfrac12+it)\rvert\le M_X-\varepsilon\) for all large \(t\), the mean square would be \(\le(M_X-\varepsilon)^2\), contradiction.  
Hence \(\limsup\lvert\theta_X\rvert\ge M_X\).  
Mertens gives \(M_X\gg\sqrt{\log\log X}\). □

**Remark.**  
This is an **Omega** result (liminf of the max is large), not a typical-pointwise lower bound for almost every \(t\). The \(L^2\) mass is consistent with **typical** size \(\asymp\sqrt{\log\log X}\). The theorem asserts that the function **attains** at least that scale infinitely often (in the limsup sense).

---

## 4. Omega for the discrepancy \(\Delta_X\) (proved on the line)

**Theorem Ω-Δ (Omega for hybrid discrepancy on the critical line).**  
Fix an integer \(K\ge 1\) and a GHK weight \(u\). There exists \(X_0=X_0(u,K)\) such that for every fixed \(X\ge X_0\),
\begin{equation}
\limsup_{t\to\infty}
\bigl\lvert\Delta_X\bigl(\tfrac12+it\bigr)\bigr\rvert
\gg
\sqrt{\log\log X}.
\tag{Ω-Δ}
\end{equation}
Equivalently (Lemma OPC-Id),
\[
\limsup_{t\to\infty}
\bigl\lvert
\arg\zeta\bigl(\tfrac12+it\bigr)
-
\arg Z_X\bigl(\tfrac12+it\bigr)
\bigr\rvert
\gg
\sqrt{\log\log X},
\]
for continuous branches along the critical line with GHK cuts avoided by a standard limiting procedure (average of vertical approaches, as in GHK).

**Proof.**  
From (Ω-Δ) in §1 and GHK,
\[
\Delta_X\bigl(\tfrac12+it\bigr)
=
\theta_X\bigl(\tfrac12+it\bigr)
+
\operatorname{Im}\mathcal{E}_{\mathrm{GHK}}\bigl(\tfrac12+it;X,K\bigr).
\]
For \(\sigma=\tfrac12\), \(\lvert t\rvert\ge 2\),
\[
\bigl\lvert\mathcal{E}_{\mathrm{GHK}}\bigr\rvert
\le
C_{u,K}
\Biggl(
\frac{X^{K+2}}{(\lvert t\rvert\log X)^{K}}
+
X^{-1/2}\log X
\Biggr)
\]
(using \(\lvert\log(1+w)\rvert\le 2\lvert w\rvert\) when the multiplicative error is \(\le\tfrac12\); for large \(\lvert t\rvert\) the first summand is \(<\tfrac14\), and the second is independent of \(t\)).

Thus as \(t\to\infty\) with \(X\) fixed,
\[
\limsup_{t\to\infty}
\bigl\lvert\Delta_X\bigr\rvert
\ge
\limsup_{t\to\infty}
\bigl\lvert\theta_X\bigr\rvert
-
C_{u,K}\,X^{-1/2}\log X.
\]
By Theorem Ω-θ, the first term is \(\ge c\sqrt{\log\log X}\).  
Choose \(X_0\) large enough that for \(X\ge X_0\),
\[
c\sqrt{\log\log X}
>
2\,C_{u,K}\,X^{-1/2}\log X
\]
(possible because \(\sqrt{\log\log X}/(X^{-1/2}\log X)\to\infty\)).  
Then \(\limsup\lvert\Delta_X\rvert\ge\tfrac12 c\sqrt{\log\log X}\). □

**Corollary Ω-θ-E.**  
Under the same hypotheses, \(\limsup_{t\to\infty}\lvert\theta_X(\tfrac12+it)\rvert\gg\sqrt{\log\log X}\) already gives the phase lower bound for \(P_X\) at the **typical Omega scale**, without passing through zeros of maximal abscissa.

---

## 5. What this does **not** prove

| Claim | Status |
|-------|--------|
| \(\limsup\lvert\Delta_X\rvert\gg\log\log X\) (strong / target-lemma scale) | **Open** |
| Omega **off** the critical line at \(\sigma\ge Y-\varepsilon\) | **Open** (target-lemma location) |
| Omega at a **deterministic** sequence of off-line \(\lvert\zeta\rvert\)-minima | **Open** |
| \(\lvert A_X\rvert\gg\log\log X\) along a sequence for O-TL | **Open** |
| RH | **Open** |

**Why strong scale is harder.**  
\(L^2\) methods give \(\sqrt{\sum a_n^2}\asymp\sqrt{\log\log X}\).  
A lower bound \(\gg\log\log X\asymp\sum_{p\le X}1/p\) would require near-perfect alignment of all prime phases \(t\log p\) — a resonance / large-values problem beyond mean square. Classical Omega results for \(S(t)\) reach intermediate powers of \(\log t\), still not automatically \(\log\log X\) for the **discrepancy** at linked \((t,X)\).

---

## 6. Typical vs Omega (programme distinction)

```
L² / typical size of θ_X, Δ_X     ∼  √(log log X)     [heuristic + mean square]
Omega (this note)                 ≫  √(log log X)     [proved limsup on the line]
Strong / O-TL scale               ≫  log log X        [open; needs stronger Omega or revised target]
Classical Omega for S(t)          Ω( (log t)^θ … )    [classical; not the same as Δ_X]
```

**Refined O-PC residual:**

| Sub-obligation | Status |
|----------------|--------|
| OPC-Core at **typical Omega scale** \(\sqrt{\log\log X}\) on the line | **Discharged** by Theorem Ω-Δ |
| OPC-Core at **strong scale** \(\log\log X\) | **Open** |
| OPC-Core off-line / at maximal abscissa | **Open** |

---

## 7. Relation to \(S(t)\)

On the critical line, \(\arg\zeta(\tfrac12+it)=\pi S(t)\) (continuous).  
Thus \(\Delta_X=\pi S(t)-\arg Z_X\).  
Classical Omega theorems for \(S(t)\) control \(\arg\zeta\), not \(\Delta_X\), unless \(\arg Z_X\) is shown smaller or non-cancelling at the same \(t\).  
Theorem Ω-Δ **bypasses** that cancellation issue by using the **arithmetic** side \(\theta_X=D_X\) and the identity \(\Delta_X=\theta_X+\operatorname{Im}\mathcal{E}\), with \(\mathcal{E}\to O(X^{-1/2}\log X)\) as \(t\to\infty\).

---

## 8. Optional revised target (not adopted)

A **revised** target lemma at scale \(\sqrt{\log\log X}\) would be closer to Theorems Ω-θ / Ω-Δ, but would **not** match the classical Akatsuka / modulus \(m\log\log X\) scale used in O-TL.  
The programme **keeps** O-TL at \(\gg m\log\log X\) and records that this is a **strong Omega** problem. No silent weakening.

---

## 9. One-liner

**On the critical line, \(\limsup\lvert\arg\zeta-\arg Z_X\rvert\gg\sqrt{\log\log X}\) (and the same for \(\lvert\arg P_X\rvert\)) is proved by mean-square Omega for the finite prime polynomial; the strong scale \(\log\log X\) needed for the target lemma, and all off-line Omega, remain open — so O-PC/O-TL/RH stay open.**

*Per aspera ad astra.*
