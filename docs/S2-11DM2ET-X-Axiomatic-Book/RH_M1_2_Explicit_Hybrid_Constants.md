# Explicit tracking of hybrid constants \(c_1,c_2,c_3\) (fixed \(f\), \(K\))

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. No model constants.  
**Does not prove** RH, the target lemma, or M1.2.  
**Does:** track the GHK error shape to **effective symbolic majorants** for fixed weight data; record what remains free.

**Companions:**  
`RH_Moments_FunctionField_Constants_Survey.md` (§3 honesty freeze),  
`RH_Akatsuka_GHK_Survey.md` (M1.2-GHK),  
`RH_M1_2_Remainder_Bound_Strategy.md`.  
**Probe:** `scripts/rh_GHK_hybrid_diagnostic.py` (`--U-mode e1` / `full`).

**Source for the identity:**  
S. M. Gonek, C. P. Hughes, J. P. Keating, *A hybrid Euler–Hadamard product for the Riemann zeta function*, Duke Math. J. **136** (2007), 507–549; arXiv:math/0511182, Theorem 1 and §2.

---

## 0. Fixed data (choose once)

| Symbol | Meaning | Standing choice in this note |
|--------|---------|------------------------------|
| \(K\) | Integration-by-parts order | \(K=2\) (matches schematic \(X^4/(|t|\log X)^2\)) |
| \(f\) | \(C^\infty\) bump on \([0,1]\), \(f\ge 0\), \(\int_0^1 f=1\) | Any fixed such \(f\); derivatives enter only via \(M_j\) |
| \(X\ge 2\) | Hybrid mediator | Free parameter |
| \(s=\sigma+it\) | Evaluation point | \(\sigma\ge 0\), \(\lvert t\rvert\ge 2\) |

Define the GHK weight from \(f\) (as in GHK §2):
\[
u(x)
=
\frac{X}{x}\,f\bigl(X\log(x/e)+1\bigr),
\qquad
\operatorname{supp}u\subset\bigl[e^{1-1/X},e\bigr],
\quad
\int_0^\infty u=1.
\]
Then
\[
U(z)=\int_0^\infty u(x)\,E_1(z\log x)\,dx,
\qquad
v(t)=\int_t^\infty u(x)\,dx.
\]
Set
\begin{equation}
M_j
:=
\max_{x\in[0,1]}\bigl\lvert f^{(j)}(x)\bigr\rvert
\quad(j=0,\ldots,K).
\tag{C-data}
\end{equation}
These are **finite, absolute numbers** once \(f\) is fixed.  
**Named bump \(f_\star\) and numerical \(M_j\), \(c_1,c_2\) upper bounds:** `RH_M1_2_Named_f_ci_Bounds.md`, `scripts/rh_named_f_M_K_probe.py`.

---

## 1. What GHK actually bounds

Theorem 1 (GHK) states, for \(\sigma\ge 0\), \(\lvert t\rvert\ge 2\),
\begin{equation}
\zeta(s)
=
P_X(s)\,Z_X(s)
\Biggl(
1
+
O_u\Biggl(\frac{X^{K+2}}{(\lvert s\rvert\log X)^{K}}\Biggr)
+
O\bigl(X^{-\sigma}\log X\bigr)
\Biggr),
\tag{GHK}
\end{equation}
with \(P_X,Z_X\) as in the survey. The \(O_u\) depends only on \(u\) (hence only on \(f,K,X\) through \(M_K\) and the support scaling).

Passing to logarithms on a region where \(\lvert\mathrm{err}\rvert\le 1/2\),
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
\bigl\lvert\mathcal{E}_{\mathrm{GHK}}(s;X,K)\bigr\rvert
\le
C_{\mathrm{mul}}\cdot
\Biggl(
c_1^{\mathrm{shape}}\frac{X^{K+2}}{(\lvert s\rvert\log X)^{K}}
+
c_2^{\mathrm{shape}} X^{-\sigma}\log X
\Biggr)
\tag{E-bound}
\end{equation}
whenever the parenthesis is \(\le 1/(2C_{\mathrm{mul}})\). Here \(C_{\mathrm{mul}}\) comes from \(\lvert\log(1+w)\rvert\le 2\lvert w\rvert\) for \(\lvert w\rvert\le 1/2\).

**Target form for the programme** (\(K=2\)):
\begin{equation}
\bigl\lvert\operatorname{Im}\mathcal{R}_X^{(\mathrm{EP})}(s)\bigr\rvert
\le
c_1\frac{X^{4}}{(\lvert t\rvert\log X)^{2}}
+
c_2 X^{-\sigma}\log X
+
c_3,
\tag{M1.2-const}
\end{equation}
where \(c_3\) absorbs (i) contributions of distant zeros after peeling the local factor, (ii) archimedean / pole terms already folded into GHK’s first \(O\), and (iii) any fixed zero-density package on a bounded path. The pure GHK multiplicative error supplies \(c_1,c_2\); \(c_3\) needs the M1.2 remainder split.

---

## 2. Tracking the first error term (pole + trivial zeros + Mellin decay)

### 2.1 Mellin transform of \(u\)

Integrating by parts \(K\) times (GHK (11)):
\[
\bigl\lvert\widetilde u(z)\bigr\rvert
\le
\max_x\bigl\lvert u^{(K)}(x)\bigr\rvert
\cdot
\frac{e^{\max\{\operatorname{Re}z+K,0\}}}{(1+\lvert z\rvert)^{K}}.
\]
With \(u(x)=X f(X\log(x/e)+1)/x\) and \(\operatorname{supp}f\subset[0,1]\),
\[
\max_x\bigl\lvert u^{(K)}(x)\bigr\rvert
\le
A_K\,M_K\,X^{K+1},
\]
where \(A_K\) is an absolute combinatorial factor from Faà di Bruno / product rule on \(X/x\) and the chain rule (depends only on \(K\), not on \(X\) or \(s\)).  
**Symbolic majorant:**
\begin{equation}
\max\lvert u^{(K)}\rvert
\le
A_K M_K X^{K+1}.
\tag{C-uK}
\end{equation}
A crude admissible choice is \(A_K=(2K)!\) (far from optimal; any larger fixed majorant is allowed).

### 2.2 Bound for \(U((s-r)\log X)\) at real \(r\)

GHK integrates \(\widetilde u/(s-r)\) from \(s\) to \(+\infty\). For \(\lvert t\rvert\ge 2\), \(\sigma\ge 0\), and \(r\in\mathbb{R}\),
\[
\bigl\lvert U((s-r)\log X)\bigr\rvert
\le
B_K
\frac{A_K M_K\,X^{K+1+\max\{r-\sigma,0\}}}{(\lvert s-r\rvert\log X)^{K}},
\]
where \(B_K\) bounds
\[
\int_{\sigma}^\infty\frac{d\alpha}{\lvert(\alpha-r)+it\rvert^{K+1}}
\cdot
(\log X)^{0}
\]
after the change of variables in the Mellin variable. For \(\lvert t\rvert\ge 2\) and \(K\ge 1\),
\[
\int_{-\infty}^\infty\frac{d\alpha}{(\alpha^2+t^2)^{(K+1)/2}}
\le
\frac{C_K^{\mathrm{int}}}{\lvert t\rvert^{K}},
\]
with e.g. \(C_K^{\mathrm{int}}=\pi\) for \(K=1\) and \(C_K^{\mathrm{int}}\le 2\) for \(K\ge 2\) (standard arctan / comparison). Absorbing \(\lvert s-r\rvert\ge\lvert t\rvert/2\) when \(\lvert r\rvert\le\lvert t\rvert/2\) or using \(\lvert s-r\rvert\ge\lvert t\rvert\) for the pole \(r=1\) when \(\lvert t\rvert\ge 2\), GHK packages
\begin{equation}
\bigl\lvert U((s-1)\log X)\bigr\rvert
+
\sum_{m=1}^\infty\bigl\lvert U((s+2m)\log X)\bigr\rvert
\le
D_K A_K M_K
\frac{X^{K+2}}{(\lvert s\rvert\log X)^{K}}.
\tag{C-arch}
\end{equation}
Here the extra power of \(X\) is \(\max\{1-\sigma,0\}\le 1\) on \(\sigma\ge 0\), giving \(X^{K+1+1}=X^{K+2}\).  
**Symbolic:** \(D_K\) is absolute (e.g. \(D_K=4C_K^{\mathrm{int}}\) is admissible for \(K\ge 1\), \(\lvert t\rvert\ge 2\); not optimized).

### 2.3 Contribution to \(\log\zeta\) before exponentiation

From the integrated explicit formula (GHK (13)–(14)), after removing archimedean terms into the \(O\),
\[
\log\zeta(s)
=
\sum_{n\le X}\frac{\Lambda(n)}{n^s\log n}\,v(e^{\log n/\log X})
-
\sum_\rho U((s-\rho)\log X)
+
R_{\mathrm{arch}}(s;X,K),
\]
with \(\lvert R_{\mathrm{arch}}\rvert\) bounded by (C-arch). Thus the **additive** error before replacing \(\widetilde P\) by \(P\) is already of shape
\begin{equation}
c_1^{\mathrm{add}}(f,K)
\frac{X^{K+2}}{(\lvert s\rvert\log X)^{K}},
\qquad
c_1^{\mathrm{add}}(f,K)
:=
D_K A_K M_K.
\tag{C-c1-add}
\end{equation}

---

## 3. Tracking the second error term (\(P_X\) vs smoothed \(\widetilde P_X\))

GHK: \(v\equiv 1\) on \(n\le X^{1-1/X}\), and
\[
\frac{\widetilde P_X(s)}{P_X(s)}
=
\exp\Biggl(
\sum_{X^{1-1/X}\le n\le X}
\frac{\Lambda(n)}{n^s\log n}\bigl(v(\cdots)-1\bigr)
\Biggr).
\]
Since \(\lvert v-1\rvert\le 1\) and \(\Lambda(n)/\log n\le 1\),
\[
\Biggl\lvert
\sum_{X^{1-1/X}\le n\le X}
\frac{\Lambda(n)}{n^s\log n}(v-1)
\Biggr\rvert
\le
\sum_{X^{1-1/X}\le n\le X} n^{-\sigma}
\le
X^{-\sigma}\cdot\#\{n\in[X^{1-1/X},X]\}
\le
X^{-\sigma}\cdot X
\cdot X^{-1+1/X}
\le
e\,X^{1-\sigma-1+1/X}
\]
(crude). The standard GHK estimate is sharper:
\begin{equation}
\sum_{X^{1-1/X}\le n\le X}n^{-\sigma}
\le
C_{\mathrm{tail}}\,X^{-\sigma}\log X
\tag{C-tail}
\end{equation}
with an absolute \(C_{\mathrm{tail}}\) (e.g. \(C_{\mathrm{tail}}=2\) works for \(X\ge 3\), \(\sigma\ge 0\), by comparing to an integral over an interval of logarithmic length \(O(1)\)). Hence
\[
\biggl\lvert\log\frac{\widetilde P_X}{P_X}\biggr\rvert
\le
C_{\mathrm{tail}}\,X^{-\sigma}\log X,
\]
and for the multiplicative factor in (GHK),
\begin{equation}
c_2^{\mathrm{shape}}
:=
C_{\mathrm{tail}}
\quad\text{(e.g. }2\text{)},
\qquad
\bigl\lvert\widetilde P_X/P_X-1\bigr\rvert
\le
\exp\bigl(c_2^{\mathrm{shape}} X^{-\sigma}\log X\bigr)-1
\le
2\,c_2^{\mathrm{shape}} X^{-\sigma}\log X
\tag{C-c2}
\end{equation}
whenever \(X^{-\sigma}\log X\le 1/2\).

---

## 4. From additive \(\log\)-error to (M1.2-const)

### 4.1 Pure hybrid error (\(c_1,c_2\))

Take \(K=2\). Set
\begin{align}
c_1
&:=
2\,C_{\mathrm{mul}}\,c_1^{\mathrm{add}}(f,2)
=
2\,C_{\mathrm{mul}}\,D_2 A_2 M_2,
\tag{C-c1}
\\
c_2
&:=
2\,C_{\mathrm{mul}}\,c_2^{\mathrm{shape}}
=
2\,C_{\mathrm{mul}}\,C_{\mathrm{tail}},
\tag{C-c2-final}
\end{align}
with \(C_{\mathrm{mul}}=2\) admissible when \(\lvert\mathrm{err}\rvert\le 1/2\). Then, on the region where the right-hand side of (E-bound) is \(\le 1/2\),
\[
\bigl\lvert\mathcal{E}_{\mathrm{GHK}}(s;X,2)\bigr\rvert
\le
c_1\frac{X^{4}}{(\lvert s\rvert\log X)^{2}}
+
c_2 X^{-\sigma}\log X.
\]
Using \(\lvert s\rvert\ge\lvert t\rvert\), one may replace \(\lvert s\rvert\) by \(\lvert t\rvert\) at the cost of the same \(c_1\).

**Status of numerical decimals for \(c_1,c_2\):**  
They are **effective** once \(f\) (hence \(M_2\)) and the crude majorants \(A_2,D_2,C_{\mathrm{tail}},C_{\mathrm{mul}}\) are fixed.  
A **fully optimized** decimal table requires computing \(M_2\) for a named \(f\) and tightening \(A_2,D_2\). Until that optimization is done, the correct report is the **symbolic form (C-c1)–(C-c2-final)**, not an invented float.

**Illustrative (non-optimal) majorant package** — admissible but crude:
\[
A_2=24,\quad D_2=16,\quad C_{\mathrm{tail}}=2,\quad C_{\mathrm{mul}}=2.
\]
Then
\[
c_1\le 2\cdot 2\cdot 16\cdot 24\cdot M_2=1536\,M_2,
\qquad
c_2\le 2\cdot 2\cdot 2=8.
\]
**Named \(f_\star\):** \(M_2^\sharp\le 88.237\) (5% grid safety) \(\Rightarrow\) \(c_1\le 1.36\cdot 10^5\), \(c_2\le 8\). See `RH_M1_2_Named_f_ci_Bounds.md`. **Not claimed as GHK’s sharp implied constants** — only as a worked majorant tree.

### 4.2 The constant \(c_3\) (local zero peeled)

After writing
\[
\log Z_X(s)
=
-
m\,U\bigl((s-\rho)\log X\bigr)
-
\sum_{\rho'\neq\rho}U\bigl((s-\rho')\log X\bigr)
\]
and expanding \(U((s-\rho)\log X)\sim -\log((s-\rho)\log X)-\gamma+\cdots\), the M1.2 remainder \(\widetilde{\mathcal{R}}_{X,\rho}^{\mathrm{GHK}}\) contains
\[
\sum_{\rho'\neq\rho}U\bigl((s-\rho')\log X\bigr)
+
\mathcal{E}_{\mathrm{GHK}}
+
\text{(regular holomorphic pieces)}.
\]
Hence
\begin{equation}
c_3
=
c_3^{\mathrm{far}}(f,K;\mathrm{HD})
+
c_3^{\mathrm{reg}},
\tag{C-c3}
\end{equation}
where:

- \(c_3^{\mathrm{reg}}\) is absolute on a fixed compact path free of other poles (bound of \(\lvert\operatorname{Im}\log H_\rho\rvert\), etc.);  
- \(c_3^{\mathrm{far}}\) requires a **height/density package HD** controlling
  \[
  \sum_{\rho'\neq\rho}\bigl\lvert U((s-\rho')\log X)\bigr\rvert
  \]
  for \(s\) on the M1.3 path. Without HD, \(c_3\) is not a pure absolute constant independent of height.

**Honest status:** \(c_3\) is effective **conditional on HD** (and on the path). Unconditional absolute \(c_3\) for all heights is **not** claimed.

---

## 5. Standing statements (frozen)

| Claim | Status |
|-------|--------|
| \(c_1=c_1(f,K)\) finite effective via (C-c1) | **Yes** (symbolic majorant tree from GHK §2) |
| \(c_2=c_2(K)\) finite effective via (C-c2-final) | **Yes** (essentially independent of \(f\)) |
| \(c_3\) finite absolute for all \(t\) without HD | **No claim** |
| \(c_3\) effective under HD + fixed path | **Yes** (symbolic) |
| Published / optimized decimals \(c_1=17.3\), etc. | **Not available**; do not invent |
| Crude package \(c_2\le 8\), \(c_1\le 1536 M_2\) | **Admissible majorant**, not sharp |
| Proves M1.2 or RH | **No** |

---

## 6. Link to numerics (full \(U=E_1\))

The identity uses the **smoothed** \(U=\int u\,E_1(\cdot)\). Two nested diagnostics:

1. **Local:** \(U_{\mathrm{loc}}(z)=-\log z-\gamma\) (singular part of \(E_1\)).  
2. **\(E_1\):** \(U_{E_1}(z)=E_1(z)\) (support collapsed to \(\{e\}\)).  
3. **Full:** \(U(z)=\int u(x)E_1(z\log x)\,dx\) with fixed \(f\).

Script: `scripts/rh_GHK_hybrid_diagnostic.py` with `--U-mode {local,e1,full}`.  
Low-height values of \(\lvert\log\zeta-\log P_X-\log Z_X^{\mathrm{trunc}}\rvert\) give **diagnostic lower bounds** on how large any admissible \(c_i\) must be at those points; they do **not** certify global \(c_i\).

---

## 7. Next analytic work (still Cat A)

1. Choose a named \(f\) (e.g. rescaled smooth bump), compute \(M_0,\ldots,M_K\) numerically to high precision, and replace \(A_K,D_K\) by tighter contour estimates → **optimized numerical upper bounds** for \(c_1,c_2\).  
2. Under a concrete HD (e.g. zeros known up to height \(T_0\), or classical density), produce an explicit \(c_3(T_0)\).  
3. Feed (C-c1)–(C-c3) into Lemma M1.2-GHK on a fixed path.

---

## One-liner

**For fixed bump \(f\) and order \(K\), GHK §2 yields effective symbolic majorants \(c_1=2C_{\mathrm{mul}}D_K A_K M_K\) and \(c_2=2C_{\mathrm{mul}}C_{\mathrm{tail}}\) for the hybrid log-error; \(c_3\) needs a density/path package and stays symbolic; no invented decimals and no RH claim.**

*Per aspera ad astra.*
