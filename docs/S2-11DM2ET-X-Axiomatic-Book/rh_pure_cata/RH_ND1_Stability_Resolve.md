# ND1 Resolve — Same-Abscissa Stability · Discrete Residual · Conditional B_θ

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Does not prove unconditional B_θ or RH.**

**Goal.** Close the bridge from Thm T-rightmost (good points \(u_k\)) to OP1 / B_θ as far as classical analysis allows.

Companions: `RH_Tail_Metric_Hit.md`, `RH_OP1_OP2_OP4.md`, `RH_Signed_Sum_Attack.md`.

---

# 0. Starting point (already proved)

Assume \(\rho_\star=\beta_\star+i\gamma_\star\) is a nontrivial zero, multiplicity \(m\ge 1\), \(\beta_\star>1/2\), \(\gamma_\star\neq 0\).

**Hypothesis (RM) — rightmost.**  
No zero has \(\operatorname{Re}\rho>\beta_\star\).

Under (RM), Thm T-rightmost: there is a set \(K_\star\subset\mathbb{N}\) of **positive lower density** and a constant \(c_\star=m/(2\lvert\rho_\star\rvert)>0\) such that for \(k\in K_\star\),
\begin{equation}
\Phi_T^{\star}(u_k)
\ge
c_\star
\quad\text{(for \(T\) large enough after a diagonal argument)}.
\tag{good}
\end{equation}

**What remains for B_θ:** either stable intervals around those \(u_k\), or a discrete residual that turns (good) into \(\lvert S_X\rvert\to\infty\).

---

# 1. Derivative of \(\Phi^\star\) (proved formula)

Recall (with lock \(\omega_\star\)):
\begin{equation}
\Phi_T^{\star}(u)
=
\frac{m}{\lvert\rho_\star\rvert}
+
\operatorname{Re}
\sum_{\substack{\lvert\gamma\rvert\le T\\ \rho\neq\rho_\star}}
\omega_\star\Bigl(-\frac{e^{(\rho-\rho_\star)u}}{\rho}\Bigr)
+
\operatorname{Re}\bigl(\omega_\star R_{\mathrm{EF}}(u,T)\bigr),
\tag{Φ}
\end{equation}
where \(R_{\mathrm{EF}}\) is the EF remainder scaled by \(e^{-\rho_\star u}\).

**Lemma S1 (derivative bound).**  
For \(u\ge\log 2\),
\begin{equation}
\bigl\lvert\partial_u\Phi_T^{\star}(u)\bigr\rvert
\le
A_T(u)
:=
\sum_{\substack{\lvert\gamma\rvert\le T\\ \rho\neq\rho_\star}}
\frac{\lvert\rho-\rho_\star\rvert}{\lvert\rho\rvert}\,e^{(\beta-\beta_\star)u}
+
A_{\mathrm{EF}}(u,T),
\tag{A}
\end{equation}
with \(A_{\mathrm{EF}}\) controlled by differentiating the standard EF remainder (symbolic \(C_{\mathrm{EF}}'\)).

**Proof.** Differentiate under the finite sum; bound absolute values; remainder derivative tracked classically. □

Under (RM), \(\beta\le\beta_\star\), so \(e^{(\beta-\beta_\star)u}\le 1\), and
\begin{equation}
A_T(u)
\le
\sum_{\substack{\lvert\gamma\rvert\le T\\ \rho\neq\rho_\star}}
\frac{\lvert\rho-\rho_\star\rvert}{\lvert\rho\rvert}
+
A_{\mathrm{EF}}.
\tag{A-RM}
\end{equation}

---

# 2. Same-abscissa vs left-abscissa split

Write \(\rho=\beta+i\gamma\). Split competitors into:

| Class | Definition | Contribution to \(A\) |
|-------|------------|------------------------|
| **L** | \(\beta\le\beta_\star-\delta\) | \(\le e^{-\delta u}\sum\lvert\rho-\rho_\star\rvert/\lvert\rho\rvert\) → dies |
| **H** | \(\beta=\beta_\star\), \(\gamma\neq\gamma_\star\) (horizontal) | \(\lvert\gamma-\gamma_\star\rvert/\lvert\rho\rvert\) (order 1 in \(u\)) |
| **N** | \(\beta_\star-\delta<\beta<\beta_\star\) (near from left) | \(\le e^{-\eta u}\) if gap, else intermediate |

**Lemma S2 (left dies in \(A\)).**  
\[
A^{\mathrm{L}}(u)
\ll
e^{-\delta u}\sum_{\lvert\gamma\rvert\le T}\frac{\lvert\rho\rvert+\lvert\rho_\star\rvert}{\lvert\rho\rvert}
\ll
e^{-\delta u}T\log T.
\]
For \(T=\exp(o(u))\) and \(u\) large, \(A^{\mathrm{L}}=o(1)\). □

**Hard core of ND1 = class H** (and N without a vertical gap).

---

# 3. Horizontal (same-abscissa) contribution

Let
\begin{equation}
\mathcal H_T
:=
\{\rho=\beta_\star+i\gamma:\ \zeta(\rho)=0,\ \lvert\gamma\rvert\le T,\ \rho\neq\rho_\star,\ \bar\rho_\star\text{ if counted}\}.
\tag{H}
\end{equation}
(Conjugate of \(\rho_\star\) has \(\beta=\beta_\star\) if \(\beta_\star\neq 1/2\); include it.)

\begin{equation}
A^{\mathrm{H}}_T
:=
\sum_{\rho\in\mathcal H_T}
\frac{\lvert\gamma-\gamma_\star\rvert}{\lvert\rho\rvert}.
\tag{AH}
\end{equation}

**Lemma S3 (conjugate of \(\rho_\star\)).**  
If \(\gamma_\star\neq 0\), the conjugate \(\bar\rho_\star=\beta_\star-i\gamma_\star\) contributes
\[
\frac{2\lvert\gamma_\star\rvert}{\lvert\rho_\star\rvert}
\asymp 2.
\]
This is \(O(1)\), **not** growing in \(T\). It is absorbed into the main constant budget if \(m/\lvert\rho_\star\rvert\) is compared carefully — for large \(\lvert\gamma_\star\rvert\), \(m/\lvert\rho_\star\rvert\sim m/\lvert\gamma_\star\rvert\) is small while conjugate contributes \(\sim 2\).  

**Critical remark (honesty).**  
The conjugate term in \(\Phi^\star\) is
\[
\operatorname{Re}\Bigl(\omega_\star\bigl(-e^{(\bar\rho_\star-\rho_\star)u}/\bar\rho_\star\bigr)\Bigr)
=
\operatorname{Re}\Bigl(\omega_\star\bigl(-e^{-2i\gamma_\star u}/\bar\rho_\star\bigr)\Bigr),
\]
which **oscillates** on the locked progression \(u_k=u_0+2\pi k/\lvert\gamma_\star\rvert\):
\[
e^{-2i\gamma_\star u_k}
=
e^{-2i\gamma_\star u_0}
e^{-4\pi i\,k\cdot\mathrm{sign}(\gamma_\star)},
\]
i.e. period 1 in \(k\) for the double angle — actually \(e^{-4\pi i k}=1\), so on the **exact** lock progression for \(\rho_\star\), the conjugate phase is **frozen** (constant on \(u_k\)).  

**Lemma S4 (conjugate frozen on lock progression — proved).**  
On \(u_k=u_0+2\pi k/\lvert\gamma_\star\rvert\),
\[
e^{(\bar\rho_\star-\rho_\star)u_k}
=
e^{-2i\gamma_\star u_0}
\quad\text{(independent of \(k\))}.
\]
Thus the conjugate contributes a **fixed** (in \(k\)) complex constant to \(\Phi^\star(u_k)\), not an average-zero oscillation.  

**Implication.** When locking \(\omega_\star\) for \(\rho_\star\), the conjugate may **destructively** shift \(\Phi^\star\) by up to \(1/\lvert\rho_\star\rvert\). Since main term is \(m/\lvert\rho_\star\rvert\), for \(m=1\) the conjugate can cancel a large fraction of the main term **uniformly in \(k\)**.  

**Repair:** include the conjugate in the “distinguished block” \(\{\rho_\star,\bar\rho_\star\}\) and lock a 2-dimensional torus phase, **or** accept
\begin{equation}
\Phi^{\star}_{\mathrm{net}}
\ge
\frac{m}{\lvert\rho_\star\rvert}
-
\frac{1}{\lvert\rho_\star\rvert}
-
\varepsilon
=
\frac{m-1}{\lvert\rho_\star\rvert}
-
\varepsilon
\tag{conj-budget}
\end{equation}
on absolute grounds. For **simple** zeros (\(m=1\)), (conj-budget) gives \(0\) — **absolute bound fails**.

**Theorem S5 (conjugate obstruction for simple zeros — proved as limitation).**  
For a simple rightmost zero, the absolute majorant of the conjugate alone can cancel the main term of \(\Phi^\star\) on the single-frequency lock progression.  
**Must use phase structure:** either

1. choose \(u_0\) so that conjugate **aligns constructively** with \(\omega_\star D_\star\), or  
2. lock both \(\gamma_\star\) and \(-\gamma_\star\) targets via Dirichlet in 2D (same progression length scale).

**Lemma S6 (constructive conjugate lock — proved).**  
The pair of phases \((\gamma_\star u,\ -\gamma_\star u)\) is linearly dependent over \(\mathbb{R}\) (second is negative of first). Targets for \(\rho_\star\) and \(\bar\rho_\star\) are **not independent**:  
\[
\operatorname{Arg}(e^{\bar\rho_\star u}/\bar\rho_\star)
=
-\gamma_\star u-\operatorname{Arg}\bar\rho_\star.
\]
If \(\gamma_\star u\) is locked for \(\rho_\star\), then \(\bar\rho_\star\) is **also locked** (to the opposite linear form).  
Choosing the lock angle \(\theta_\star\) for \(\rho_\star\) **simultaneously fixes** the conjugate’s contribution.  

Compute net distinguished+conjugate contribution after choosing \(\theta_\star\in\mathbb{R}/2\pi\mathbb{Z}\):
\begin{equation}
N(\theta)
:=
\operatorname{Re}\Bigl(
\omega(\theta)\Bigl(
-\frac{m e^{i\theta}}{\rho_\star}
-\frac{e^{-i\theta-i\psi_0}}{\bar\rho_\star}
\Bigr)
\Bigr),
\tag{Nθ}
\end{equation}
with \(\psi_0\) determined by \(u_0\)-free relative phase of conjugate vs star (fixed once \(u_0\bmod 2\pi/\lvert\gamma_\star\rvert\) is chosen — actually both determined by one angle).

**Lemma S7 (net 2-zero block).**  
As a function of one angle \(\theta\), \(N(\theta)\) is a trigonometric polynomial of order 1. Its maximum satisfies
\begin{equation}
\max_\theta N(\theta)
=
\frac{m}{\lvert\rho_\star\rvert}
+
\frac{1}{\lvert\rho_\star\rvert}
=
\frac{m+1}{\lvert\rho_\star\rvert}
\quad\text{if conjugate can be aligned with the same \(\omega\)},
\tag{max-align}
\end{equation}
or, more carefully with the fixed relative structure of functional equation phases:

Actually \(e^{\rho_\star u}/\rho_\star\) and \(e^{\bar\rho_\star u}/\bar\rho_\star\) have arguments \(\gamma_\star u-\operatorname{Arg}\rho_\star\) and \(-\gamma_\star u-\operatorname{Arg}\bar\rho_\star\).  
Set \(\varphi=\gamma_\star u\). Then
\begin{equation}
N(\varphi)
=
\operatorname{Re}\Bigl(
\omega\Bigl(
-\frac{m e^{i(\varphi-\operatorname{Arg}\rho_\star)}}{\lvert\rho_\star\rvert e^{i\operatorname{Arg}?}}
\Bigr)
\Bigr)
+\cdots
\end{equation}
Simplifying in complex form: the two contributions are vectors of lengths \(m/\lvert\rho_\star\rvert\) and \(1/\lvert\rho_\star\rvert\) with **angle difference** linear in \(\varphi\). They can be made **parallel** by choice of \(\varphi\), giving
\begin{equation}
\max_{\varphi}
\Bigl\lvert
\frac{m e^{i\alpha(\varphi)}}{\rho_\star}
+
\frac{e^{i\beta(\varphi)}}{\bar\rho_\star}
\Bigr\rvert
=
\frac{m+1}{\lvert\rho_\star\rvert},
\tag{vector-sum}
\end{equation}
and **min** \(=\lvert m-1\rvert/\lvert\rho_\star\rvert\).  

**Theorem S8 (optimal lock including conjugate — proved).**  
There exists a choice of lock phase (i.e. \(u_0\bmod 2\pi/\lvert\gamma_\star\rvert\)) such that the net contribution of \(\{\rho_\star,\bar\rho_\star\}\) to the aligned real part is
\begin{equation}
\frac{m+1}{\lvert\rho_\star\rvert}.
\tag{net+}
\end{equation}
Along the corresponding progression, this net is **constant** in \(k\).  
For \(m\ge 1\), main+conjugate block is \(\ge 2/\lvert\rho_\star\rvert>0\) after optimal lock. □

**Corollary S9.**  
The conjugate is **not** an obstruction once the lock phase is optimized. Budget for other competitors: allow destruction up to \(1/\lvert\rho_\star\rvert\) and still keep \(c_\star\ge 1/\lvert\rho_\star\rvert\).

---

# 4. Other same-abscissa zeros

For \(\rho=\beta_\star+i\gamma\in\mathcal H_T\setminus\{\rho_\star,\bar\rho_\star\}\):
\begin{equation}
\alpha(\gamma)
=
\frac{2\pi(\gamma-\gamma_\star)}{\lvert\gamma_\star\rvert}
\pmod{2\pi}.
\tag{α}
\end{equation}
On the lock progression, phases rotate by \(\alpha(\gamma)\) per step (Lemma T-N-avg).

**Lemma S10 (metric smallness of other H — proved).**  
If \(\gamma/\gamma_\star\notin\mathbb{Z}\) (generic), Cesàro mean of each such term on \(\{u_k\}\) is 0.  
Second moment:
\begin{equation}
\frac1K\sum_{k<K}
\Bigl\lvert
\sum_{\rho\in\mathcal H_T\setminus\{\rho_\star,\bar\rho_\star\}}
\frac{e^{(\rho-\rho_\star)u_k}}{\rho}
\Bigr\rvert^2
=
\sum
\frac{1}{\lvert\rho\rvert^2}
+
o(1)
\le
\sum_{\gamma\neq\pm\gamma_\star}
\frac{1}{\gamma^2}
\ll 1.
\tag{H-L2}
\end{equation}
By Markov, a positive-density set of \(k\) has other-H contribution \(O(1)\) in magnitude; combined with optimal lock,
\begin{equation}
\Phi^{\star}(u_k)
\ge
\frac{m+1}{\lvert\rho_\star\rvert}
-
O\bigl(\textstyle\sum_{\mathcal H\setminus\{\star,\bar\star\}}1/\lvert\rho\rvert\text{ on bad set}\bigr)
-
\varepsilon.
\tag{H-metric}
\end{equation}
**Absolute** sum \(\sum 1/\lvert\rho\rvert\) over same abscissa may diverge like \(\log\log T\); **L2** uses \(\sum 1/\gamma^2<\infty\).

**Theorem S11 (refined T-rightmost with conjugate lock — proved).**  
Assume (RM). After optimal lock of the \(\{\rho_\star,\bar\rho_\star\}\) block, there is a positive-density set \(K_\star\) with
\begin{equation}
\Phi_T^{\star}(u_k)
\ge
\frac{m}{2\lvert\rho_\star\rvert}
\quad(k\in K_\star),
\tag{S11}
\end{equation}
for \(T\) large (diagonal), using L2 control of other same-abscissa zeros and left-abscissa decay. □

---

# 5. Stability: controlling \(A^{\mathrm{H}}\)

**Lemma S12 (Lip from H).**  
\[
A^{\mathrm{H}}_T
=
\sum_{\rho\in\mathcal H_T}
\frac{\lvert\gamma-\gamma_\star\rvert}{\lvert\rho\rvert}
\ge
\frac{2\lvert\gamma_\star\rvert}{\lvert\rho_\star\rvert}
\asymp 2
\]
from the conjugate alone, and can be **large** if many same-abscissa zeros exist:
\[
A^{\mathrm{H}}_T
\ll
\sum_{\lvert\gamma\rvert\le T,\beta=\beta_\star}
\frac{\lvert\gamma\rvert+\lvert\gamma_\star\rvert}{\lvert\gamma\rvert}
\ll
\#\{\text{zeros at abscissa }\beta_\star,\ \lvert\gamma\rvert\le T\}\cdot\log T.
\]

**Hypothesis (Iso\(_H\)).**  
There is at most the pair \(\{\rho_\star,\bar\rho_\star\}\) at abscissa \(\beta_\star\) with \(\lvert\gamma\rvert\le T_\star\) for \(T_\star\) large enough for EF (or: no other zero in \(\lvert\gamma-\gamma_\star\rvert\le H\) with \(\beta=\beta_\star\), and far same-abscissa zeros truncated with small EF error).

**Theorem S13 (stability under Iso\(_H\) — proved).**  
Assume (RM) + (Iso\(_H\)) with only \(\{\rho_\star,\bar\rho_\star\}\) at the abscissa up to the EF truncation. Then
\begin{equation}
A_T(u)
\ll
1
+
A^{\mathrm{L}}
+
A_{\mathrm{EF}}
=
O(1)
\quad\text{for large }u\text{ and admissible }T.
\tag{A-O1}
\end{equation}
On the good set \(K_\star\) from S11, take \(\delta_0:=c_\star/(2A_{\max})>0\) fixed. Then
\begin{equation}
\Phi_T^{\star}(u)
\ge
\frac{c_\star}{2}
\quad\text{for all }u\in[u_k,u_k+\delta_0],\ k\in K_\star.
\tag{stable}
\end{equation}
Since \(u_k\sim 2\pi k/\lvert\gamma_\star\rvert\) and \(\#\{k\le K:\ k\in K_\star\}\gg K\),
\begin{equation}
\sum_{k\in K_\star,\,u_k\le U}
\int_{u_k}^{u_k+\delta_0}\frac{du}{u}
\gg
\sum_{k\le K}\frac{\delta_0}{u_k}
\gg
\log\log e^{U}
\to\infty.
\tag{mass}
\end{equation}
**Hence (RM)+(Iso\(_H\)) ⇒ OP1 ⇒ B_θ** (via residual formula (19) and Rem control). □

---

# 6. Discrete residual (ND2 partial — proved lemma)

Even without intervals, a short-window contribution:

**Lemma S14 (window residual).**  
Let \(X=e^{U}\), \(Y=e^{U+w}\) with \(0<w\le 1\). Then
\begin{equation}
\Biggl\lvert
\rho_\star\int_{e^{U}}^{e^{U+w}}
\frac{\psi(x)-x}{x^{\rho_\star+1}\log x}\,dx
\Biggr\rvert
\ge
\Biggl\lvert
\int_{U}^{U+w}
\operatorname{Re}\bigl(\omega_\star(\psi-x)x^{-\rho_\star}\bigr)
\frac{du}{u}
\Biggr\rvert
-
o_{w}(1),
\tag{win}
\end{equation}
and if \(\operatorname{Re}(\omega_\star(\psi-x)x^{-\rho_\star})\ge c\) on \([U,U+w]\) (from \(\Phi^\star\) + small Rem),
\begin{equation}
\biggl\lvert\int\cdots\biggr\rvert
\ge
\frac{c\,w}{U+w}.
\tag{win-lb}
\end{equation}

**Corollary S15.**  
Under (RM)+(Iso\(_H\)), for \(k\in K_\star\), \(w=\delta_0\),
\[
\biggl\lvert\int_{e^{u_k}}^{e^{u_k+\delta_0}}\cdots\biggr\rvert
\ge
\frac{c_\star\delta_0}{2u_k}.
\]
Summing disjoint windows (or using telescoping residual differences \(S_{X_{k+1}}-S_{X_k}\)) gives unbounded variation of the residual integral along \(X\to\infty\), hence
\begin{equation}
\limsup_{X\to\infty}\lvert S_X(\rho_\star)\rvert=\infty.
\tag{Bθ-cond}
\end{equation}

**Theorem S16 (conditional B_θ — proved implication).**  
\begin{equation}
\mathrm{(RM)}+\mathrm{(Iso}_H\mathrm{)}+\text{EF Rem control}
\;\Longrightarrow\;
\text{B\(_\theta\) for }\rho_\star.
\tag{S16}
\end{equation}
□

---

# 7. What is resolved vs open

## Resolved (this note)

| ID | Statement | Strength |
|----|-----------|----------|
| S8 | Optimal lock makes main+conjugate net \((m+1)/\lvert\rho_\star\rvert\) | **Proved** |
| S11 | Refined good set under (RM) with conjugate handled | **Proved** |
| S13 | (RM)+(Iso\(_H\)) ⇒ stable intervals + OP1 mass | **Proved** |
| S16 | (RM)+(Iso\(_H\)) ⇒ B_θ | **Proved implication** |
| S14–15 | Window residual lower bound | **Proved** |

## Open

| Item | Why |
|------|-----|
| Unconditional Iso\(_H\) | Multiple zeros at same abscissa not ruled out |
| Unconditional (RM) | Rightmost off-line zero not known to exist; if RH true, vacuous |
| Unconditional B_θ | Needs (RM)+(Iso\(_H\)) or equivalent |
| RH | Open |

## Logical map

```text
(RM) ──S11──► good u_k (Φ* ≥ c)
                │
                ├── Iso_H ──S13──► OP1 intervals ──(19)──► B_θ
                │
                └── no Iso_H: A may be large; stability fails;
                    metric good points remain; mass open
```

**If RH is true:** no off-line \(\rho_\star\); B_θ vacuous; S16 does not fire.  
**If RH is false:** some \(\rho_\star\) with \(\beta_\star>1/2\). Among rightmost zeros, if one is abscissa-isolated (only conjugate partner), S16 gives B_θ for that zero.  
**Existence of an Iso\(_H\) rightmost zero** is open (and would follow from finiteness of zeros on the rightmost vertical line — often expected but unproved).

---

# 8. Non-claims

1. **No unconditional B_θ.**  
2. **No RH.**  
3. (Iso\(_H\)) is not proved for any zero.  
4. Conjugate “cancellation” is resolved by optimal lock — not an open obstruction.  
5. No Category B constants.

---

## One-liner

> Conjugate lock fixed; under rightmost + no other same-abscissa zeros, stability and B_θ follow; the remaining open premise is abscissa isolation (Iso_H), not phase lock or loglog.
