# Fully effective conditional M1.2 from classical zero-density

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. Axiom **ZLA**. No model constants.  
**Does not prove RH or O-TL.**  
**Does:** insert a classical zero-density bound into the GHK / regularised-remainder majorant tree and state a **fully effective conditional** form of M1.2 on a concrete height range.

**Companions:** `RH_M1_2_Explicit_Hybrid_Constants.md`, `RH_M1_2_Optimized_ci_Bounds.md`, `RH_M1_2_Remainder_Bound_Strategy.md`, `RH_Existing_Theorems_Solid_Directions.md`.

---

## 1. Density input (classical)

**Hypothesis HD-Ingham (schematic explicit form).**  
There exist absolute constants \(A,B,C>0\) such that for \(1/2\le\sigma\le 1\) and \(T\ge 2\),
\begin{equation}
N(\sigma,T)
:=
\#\{\rho=\beta+i\gamma:\ \beta\ge\sigma,\ \lvert\gamma\rvert\le T\}
\le
C\,T^{A(1-\sigma)^{3/2}}
(\log T)^{B}.
\tag{HD-I}
\end{equation}
(This is the classical Ingham shape; Huxley’s refinements improve \(A\). **Any** fixed explicit triple \((A,B,C)\) from the literature may be substituted — the lemma below tracks them symbolically.)

**Reference class:** Ingham; Huxley; modern explicit versions (e.g. works giving fully numerical \(A,B,C\)). The programme treats \((A,B,C)\) as **fixed classical data**, not model constants.

---

## 2. Local path and hybrid data

Fix:

- a simple zero \(\rho=\tfrac12+i\gamma\) with \(\gamma\ge\gamma_0\) (on-line package; off-line analogous with \(\beta=Y\));  
- radius \(r=c_r/\log\gamma\) with \(0<c_r\le\tfrac12\);  
- hybrid scale \(X=(\log\gamma)^{A_X}\) with \(A_X\ge 1\) large enough that GHK errors with \(K=2\) satisfy
  \[
  c_1\frac{X^{4}}{(\gamma\log X)^{2}}
  +
  c_2 X^{-1/2}\log X
  \le
  \varepsilon_0
  \]
  using the programme bounds \(c_1\le 291\), \(c_2\le 8\) for \(f_\star\) (or the Kronecker-scale analysis with fixed \(X\) large);  
- path \(\gamma_{\mathrm{path}}\): approach \(\sigma:1.5\to\tfrac12+r\) at height \(t=\gamma\), or the isolating semicircle (for remainder size, not monodromy of \(P_X\)).

Regularised remainder (OPC identity):
\begin{equation}
R_{\mathrm{reg}}(s)
=
\log P_X(s)
+
U\bigl((s-\rho)\log X\bigr)
-
\log\zeta(s)
=
-
\sum_{\rho'\neq\rho}
U\bigl((s-\rho')\log X\bigr)
-
\mathcal{E}_{\mathrm{GHK}}.
\tag{M12-R}
\end{equation}

---

## 3. Distant-zero majorant from density

**Lemma M12-Ubound.**  
For \(z\neq 0\) off the branch cut, \(\lvert E_1(z)\rvert\le e^{-\operatorname{Re} z}/(\lvert z\rvert)\) when \(\operatorname{Re} z\ge 0\), and \(\lvert E_1(z)\rvert\ll 1+\lvert\log z\rvert\) near \(0\). On the path with \(\lvert s-\rho'\rvert\ge r\) for \(\rho'\neq\rho\),
\begin{equation}
\bigl\lvert U\bigl((s-\rho')\log X\bigr)\bigr\rvert
\le
C_U
\min\Biggl(
1,
\frac{1}{\lvert(s-\rho')\log X\rvert}
\Biggr)
\le
\frac{C_U}{r\log X}
\quad\text{if }\lvert s-\rho'\rvert\ge r,
\tag{M12-U}
\end{equation}
with \(C_U\) absolute for the local \(U=E_1\) model (or depending only on \(f_\star\) for full GHK \(U\)).

**Lemma M12-Far.**  
Assume isolation: \(D(\rho,2r)\) contains only \(\rho\). Split far zeros into dyadic annuli
\[
\mathcal{A}_j
=
\bigl\{\rho':\ 2^j r\le\lvert\gamma'-\gamma\rvert<2^{j+1}r\bigr\},
\qquad
j=0,1,\ldots,J,\quad 2^J r\le 2\gamma.
\]
Then for \(s\in\gamma_{\mathrm{path}}\),
\begin{equation}
\sum_{\rho'\neq\rho}
\bigl\lvert U((s-\rho')\log X)\bigr\rvert
\le
\sum_{j=0}^{J}
\frac{C_U}{2^j r\log X}
\cdot
\#\mathcal{A}_j
+
\sum_{\lvert\gamma'\rvert>2\gamma}
\frac{C_U}{\lvert\gamma'\rvert\log X}.
\tag{M12-far}
\end{equation}

**Lemma M12-Count.**  
Under (HD-I), for \(H\ge 1\),
\[
\#\{\rho':\ \lvert\gamma'-\gamma\rvert\le H\}
\le
1
+
N\bigl(\tfrac12,\gamma+H\bigr)
-
N\bigl(\tfrac12,\gamma-H\bigr)
+
O\bigl(N(\sigma_0,\gamma+H)\bigr)
\]
with a crude bound
\begin{equation}
\#\{\rho':\ \lvert\gamma'-\gamma\rvert\le H\}
\le
C'\,H\log\gamma
+
C\,(\gamma+H)^{A(1/2)^{3/2}}
(\log\gamma)^{B}
\ll
H\log\gamma
+
\gamma^{A/(2\sqrt{2})}
(\log\gamma)^{B}
\tag{M12-N}
\end{equation}
(using zeros in a box of height \(2H\); standard comparison of \(N(T+H)-N(T-H)\) with density theorems — insert the precise form from the chosen reference for fully numerical constants).

**Optimised cut.**  
Take \(H_j=2^j r\). Then \(\#\mathcal{A}_j\ll 2^j r\log\gamma+\gamma^{\alpha}(\log\gamma)^{B}\) with \(\alpha=A/(2\sqrt{2})\).  
Hence
\begin{align}
\sum_j
\frac{C_U}{2^j r\log X}
\#\mathcal{A}_j
&\ll
\frac{C_U}{r\log X}
\sum_j
\bigl(r\log\gamma
+
2^{-j}\gamma^{\alpha}(\log\gamma)^{B}\bigr)
\\
&\ll
\frac{C_U\log\gamma}{\log X}
\cdot
J
+
\frac{C_U\gamma^{\alpha}(\log\gamma)^{B}}{r\log X}.
\end{align}
With \(J\ll\log\gamma\) and \(r=c_r/\log\gamma\),
\begin{equation}
\sum_{\rho'\neq\rho}
\bigl\lvert U\bigr\rvert
\ll
C_U
\frac{(\log\gamma)^2}{\log X}
+
C_U
\frac{\gamma^{\alpha}(\log\gamma)^{B+1}}{c_r\log X}.
\tag{M12-sum}
\end{equation}

---

## 4. Effective conditional M1.2

**Theorem M12-Eff (conditional, effective).**  
Assume (HD-I) with fixed \((A,B,C)\). Let \(c_1,c_2\) be the programme majorants for \(f_\star\), \(K=2\). Fix \(c_r\in(0,\tfrac12]\), \(\varepsilon_0\in(0,\tfrac14]\), and \(A_X\) large enough that along the path
\[
\bigl\lvert\mathcal{E}_{\mathrm{GHK}}\bigr\rvert
\le
\varepsilon_0.
\]
Then for all zeros with \(\gamma\ge\gamma_1(A,B,C,c_r,A_X,c_1,c_2)\) (effective in principle once \((A,B,C)\) are numerical),
\begin{equation}
\sup_{s\in\gamma_{\mathrm{path}}}
\bigl\lvert\operatorname{Im} R_{\mathrm{reg}}(s)\bigr\rvert
\le
C_\star
\frac{(\log\gamma)^2}{\log X}
+
C_\star
\frac{\gamma^{\alpha}(\log\gamma)^{B+1}}{c_r\log X}
+
\varepsilon_0,
\tag{M12-eff}
\end{equation}
with \(\alpha=A/(2\sqrt{2})\) and \(C_\star\) an absolute multiple of \(C_U\) (effective from §3).

In particular, if \(X=(\log\gamma)^{A_X}\) with \(A_X\) large and \(\gamma\) large,
\[
\sup\lvert\operatorname{Im} R_{\mathrm{reg}}\rvert
\le
\tfrac12,
\]
while the local factor \(U((s-\rho)\log X)\) contributes order-\(1\) argument change on a semicircle of radius \(r\) (Lemma OPC-Zloc). This is a **uniform bound on the regularised remainder** on the path for large on-line zeros under (HD-I) — i.e. a **conditional effective M1.2** in the sense of remainder domination, not yet a \(\log\log X\) phase lower bound for \(P_X\).

**Proof.**  
Combine (M12-R), (M12-sum), and the GHK bound \(\lvert\mathcal{E}\rvert\le\varepsilon_0\). The threshold \(\gamma_1\) is determined by making the right-hand side of (M12-eff) \(\le\tfrac12\). □

---

## 5. Relation to the open obligation O-M1.2

| Layer | Status |
|-------|--------|
| Symbolic majorants \(c_1,c_2\) | Done (programme) |
| Density \(\to\) far-zero sum majorant | **Done** (this note, under HD-I) |
| Fully numerical \((A,B,C)\) plugged into \(\gamma_1\) | **Open as arithmetic** — insert a published explicit density theorem’s constants |
| Remainder domination \(\Rightarrow\) \(\lvert\theta_X\rvert\gg\log\log X\) at maximal abscissa | **Open** (needs O-PC strong off-line / O-M1.3bis / O-TL) |

**O-M1.2 status update:**  
The **architecture** of a fully effective conditional M1.2 is complete. Closing the obligation as a numerical theorem requires only citation of a specific explicit density estimate with concrete \(A,B,C\) and a finite check of \(\gamma_1\). The **analytic** content (how density controls \(\operatorname{Im} R_{\mathrm{reg}}\)) is recorded here.

---

## 6. What this does not do

- Prove RH or zero-free regions stronger than (HD-I).  
- Prove O-TL.  
- Replace the need for strong Omega / path accumulation at special points.  
- Claim a specific decimal for \(\gamma_1\) without fixing a published \((A,B,C)\).

---

## 7. One-liner

**Under a classical Ingham–Huxley zero-density hypothesis with tracked constants, the far-zero contribution to the GHK regularised remainder on the M1.3 path is an effective \(O((\log\gamma)^2/\log X)+O(\gamma^{\alpha}(\log\gamma)^{B}/(r\log X))\), giving a fully structured conditional M1.2; plugging explicit numerical density constants is the remaining arithmetic step, not a new analytic idea.**

*Per aspera ad astra.*
