# Named test function \(f_\star\) and admissible numerical bounds for \(c_1,c_2\)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. No model constants.  
**Does not prove** RH, M1.2, or the target lemma.  
**Does:** fix one \(C^\infty\) bump, compute numerical upper bounds on \(M_j\), and feed the majorant tree of `RH_M1_2_Explicit_Hybrid_Constants.md` to obtain **admissible** (crude, not sharp) numerical upper bounds on \(c_1,c_2\) for \(K=2\).

**Companions:**  
`RH_M1_2_Explicit_Hybrid_Constants.md`,  
`RH_Moments_FunctionField_Constants_Survey.md` (honesty freeze),  
`RH_M1_3_Path_Design.md` (next analytic step).  
**Probe:** `scripts/rh_named_f_M_K_probe.py` → `rh_named_f_M_K_results.json`.

---

## 1. Named bump \(f_\star\)

Define the standard non-analytic-at-endpoints smooth bump on \((0,1)\):
\[
f_{\mathrm{raw}}(t)
=
\begin{cases}
\exp\!\bigl(-1/(t(1-t))\bigr) & t\in(0,1),\\
0 & t\notin(0,1),
\end{cases}
\qquad
f_\star(t)
=
\frac{f_{\mathrm{raw}}(t)}{\displaystyle\int_0^1 f_{\mathrm{raw}}}.
\]
Then \(f_\star\ge 0\), \(\operatorname{supp}f_\star\subset[0,1]\), \(\int_0^1 f_\star=1\), and \(f_\star\in C^\infty(\mathbb{R})\) after extension by zero.

This is the same family used in the full-\(U\) mode of `rh_GHK_hybrid_diagnostic.py`.

**Mass (trapezoid, dense grid):**
\[
\int_0^1 f_{\mathrm{raw}}
\approx
0.0070298584066.
\]

---

## 2. Numerical upper bounds on \(M_j=\max\lvert f_\star^{(j)}\rvert\)

Computed by high-precision differentiation (`mpmath`) on a dense interior grid, then multiplied by a **5% safety factor** for possible grid undershoot. These are therefore **upper bounds**, not claims of exact maxima.

| \(j\) | \(M_j\) upper (with 5% safety; probe output) |
|------:|---------------------------------------------:|
| 0 | \(\le 2.73567\) |
| 1 | \(\le 11.5873\) |
| 2 | \(\le 88.237\) |
| 3 | \(\le 1249.5\) |
| 4 | \(\le 30104\) |

Exact floats frozen in `rh_named_f_M_K_results.json`.

For the \(K=2\) hybrid shape one needs only \(M_2\).

---

## 3. Admissible majorant package (unchanged, crude)

From `RH_M1_2_Explicit_Hybrid_Constants.md` (not optimized):
\[
A_2=24,\quad D_2=16,\quad C_{\mathrm{tail}}=2,\quad C_{\mathrm{mul}}=2.
\]
Then
\begin{align}
c_1
&\le
2\,C_{\mathrm{mul}}\,D_2\,A_2\,M_2
=
1536\,M_2,
\tag{B-c1}
\\
c_2
&\le
2\,C_{\mathrm{mul}}\,C_{\mathrm{tail}}
=
8.
\tag{B-c2}
\end{align}

---

## 4. Numerical conclusions for \(f_\star\), \(K=2\)

Using the probe’s \(M_2\) upper bound (denote it \(M_2^\sharp\); see JSON):

\begin{equation}
\boxed{
c_2(f_\star,K=2)
\le
8,
\qquad
c_1(f_\star,K=2)
\le
1536\,M_2^\sharp
}.
\tag{B-num}
\end{equation}

With the executed probe value \(M_2^\sharp=88.237\) (JSON),
\[
c_1
\le
1536\times 88.237
=
135531.99\ldots
\quad\text{(JSON: }c_1^{\mathrm{upper}}=135531.987\ldots\text{)}.
\]
So, for this package and \(f_\star\),
\[
c_1\le 1.36\cdot 10^5,
\qquad
c_2\le 8
\]
are admissible (crude) numerical upper bounds.

**Honesty (frozen):**
- These are **admissible upper bounds** for this named \(f_\star\) under the **crude** majorant tree.  
- They are **not** claimed to be the best possible constants in GHK, nor the true implied constants of any particular proof write-up.  
- They are **not invented** in the sense of random decimals: every factor is either fixed by the majorant package or computed from \(f_\star\).  
- \(c_3\) remains **symbolic under HD** (unchanged).

---

## 5. Use in M1.2-GHK

On the region where
\[
c_1\frac{X^{4}}{(\lvert t\rvert\log X)^{2}}
+
c_2 X^{-\sigma}\log X
\le
\tfrac12,
\]
one may use (B-num) to control \(\lvert\mathcal{E}_{\mathrm{GHK}}\rvert\) for the weight built from \(f_\star\) at \(K=2\). Combined with a path and an HD package controlling distant zeros, this is the input shape for Lemma M1.2-GHK. **Closing M1.2 still requires the path (M1.3) and the distant-zero bound.**

---

## 6. Status

| Item | Status |
|------|--------|
| Named \(f_\star\) | **Fixed** |
| \(M_j\) upper bounds | **Computed** (probe + 5% safety) |
| \(c_2\le 8\) | **Admissible** for this package |
| \(c_1\le 1536 M_2^\sharp\) | **Admissible** for this package |
| Sharp / optimized \(c_i\) | **Open** |
| \(c_3\) numerical | **Open** (needs HD) |
| M1.2 / RH | **Open** |

---

## One-liner

**For the named bump \(f_\star\), the programme now has explicit admissible bounds \(c_2\le 8\) and \(c_1\le 1536 M_2^\sharp\) with \(M_2^\sharp\) computed numerically; these are crude majorants, not sharp GHK constants, and do not prove M1.2 or RH.**

*Per aspera ad astra.*
