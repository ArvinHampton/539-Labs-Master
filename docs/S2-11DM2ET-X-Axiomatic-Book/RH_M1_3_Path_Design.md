# M1.3 — Path design for argument lower bounds

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. No model constants.  
**Does not prove** RH or the target lemma.  
**Does:** freeze a concrete path geometry so that \(m\arg(s-\rho)\) is large while M1.2 / M1.2-GHK remains applicable.

**Companions:**  
`RH_M1_2_Remainder_Bound_Strategy.md`,  
`RH_Akatsuka_GHK_Survey.md` (M1.2-GHK),  
`RH_M1_2_Named_f_ci_Bounds.md` (admissible \(c_1,c_2\)),  
`RH_L1_Phase_Functional_CatA.md` (target lemma).

---

## 1. Goal of M1.3

From M1 (or GHK form), near a zero \(\rho=\beta+i\gamma\) of multiplicity \(m\ge 1\),
\[
\theta_x(s)
=
\arg P_x(s)
=
m\arg(s-\rho)
+
\operatorname{Im}\mathcal{R}
+
\operatorname{Im} H_\rho(s),
\]
with \(\mathcal{R}\) the Euler–explicit / hybrid remainder after peeling the local factor.

**M1.2** bounds \(\lvert\operatorname{Im}\mathcal{R}\rvert\) on a path.  
**M1.3** chooses the path so that
\begin{equation}
\sup_{s\in\gamma_{\mathrm{path}}}
\lvert m\arg(s-\rho)\rvert
\quad\text{is large},
\tag{M1.3-goal}
\end{equation}
while the path stays inside the region where M1.2 applies (no other zeros of real part \(\ge\beta\) in a fixed neighbourhood; hybrid error small).

If M1.2 holds with \(c_0<1\) and
\[
\Delta_{\gamma_{\mathrm{path}}}\arg(s-\rho)
=
\pi
\quad\text{(semicircle)},
\]
then
\[
\Delta\theta_x
\ge
(1-c_0)m\pi
-
O(\lvert\operatorname{Im} H_\rho\rvert),
\]
which after smoothing (M1.4) feeds the target lemma scale when combined with modulus / \(\log\log\) control.

---

## 2. Geometry (fixed recipe)

### 2.1 Local disk

Let \(\rho=\beta+i\gamma\) with \(\beta=Y=\sup\operatorname{Re}\rho'\) (or, diagnostically, a numerical off-line local minimum of \(\lvert\zeta\rvert\) with \(\sigma\ge 0.60\) — **not** a theorem input).

Choose radius
\begin{equation}
r
=
\frac{c_r}{\log(2+\lvert\gamma\rvert)},
\qquad
0<c_r\le \tfrac12,
\tag{M1.3-r}
\end{equation}
so that:
- the mean vertical gap between zeros at height \(\gamma\) is \(\asymp 2\pi/\log\gamma\), hence a disk of radius \(r\) with small \(c_r\) typically contains at most one zero (under HD / known tables at low height);
- GHK’s local weight \(U((s-\rho)\log X)\) is appreciable when \(\lvert s-\rho\rvert\asymp 1/\log X\); match scales by taking
  \[
  X
  =
  (\log(2+\lvert\gamma\rvert))^{A}
  \quad\text{or}\quad
  X=\lvert\gamma\rvert^{\theta}
  \]
  with \(A,\theta\) small enough that \(\mathcal{E}_{\mathrm{GHK}}\) is \(o(1)\) via the admissible \(c_1,c_2\) of `RH_M1_2_Named_f_ci_Bounds.md`.

### 2.2 Semicircle path (principal choice)

Let
\begin{equation}
\gamma_{\mathrm{path}}
:
s(\varphi)
=
\rho
+
r e^{i\varphi},
\qquad
\varphi\in[0,\pi]
\quad\text{(upper semicircle in the right half relative to the vertical line through \(\rho\))}.
\tag{M1.3-semi}
\end{equation}
More carefully: take the semicircle in \(\operatorname{Re}(s-\rho)\ge 0\) if one approaches from the right half-strip, or the full circle if a continuous branch of \(\arg(s-\rho)\) of total variation \(2\pi\) is needed. For a lower bound of order \(m\pi\), the semicircle
\[
\varphi:0\to\pi
\qquad\Rightarrow\qquad
\Delta\arg(s-\rho)=\pi
\]
is the standard choice.

**Avoid:** the branch cut of \(\log(s-\rho)\) and of \(E_1((s-\rho)\log X)\). Implement continuous argument by tracking \(\varphi\) explicitly along the parametrization (no principal-value jumps).

### 2.3 Rectangular detour (optional)

If a pure semicircle hits another zero or a large horizontal integral:
1. vertical segment at \(\operatorname{Re}s=\beta+\delta\),  
2. horizontal to height \(\gamma\pm r\),  
3. short arc about \(\rho\).

Bookkeeping is heavier; semicircle first.

---

## 3. Matching with M1.2-GHK

On \(\gamma_{\mathrm{path}}\), require (for large \(\lvert\gamma\rvert\)):

\begin{align}
&\bigl\lvert\operatorname{Im}\widetilde{\mathcal{R}}_{X,\rho}^{\mathrm{GHK}}(s)\bigr\rvert
\le
c_0\,m\cdot\sup\lvert\arg(s-\rho)\rvert
+
O\bigl(\lvert\mathcal{E}_{\mathrm{GHK}}\rvert\bigr),
\tag{M1.3-M12}
\\
&\lvert\mathcal{E}_{\mathrm{GHK}}\rvert
\le
c_1\frac{X^{K+2}}{(\lvert t\rvert\log X)^{K}}
+
c_2 X^{-\sigma}\log X
\le
\varepsilon_0,
\tag{M1.3-E}
\end{align}
with \(c_1,c_2\) from the named-\(f\) bounds, \(K=2\), \(\varepsilon_0\le\tfrac14 m\pi\), and \(c_0\le\tfrac12\).

**Corollary (conditional).**  
If (M1.3-M12)–(M1.3-E) hold and \(\Delta\arg(s-\rho)=\pi\), then
\begin{equation}
\Delta_{\gamma_{\mathrm{path}}}\theta_X
\ge
\tfrac12 m\pi.
\tag{M1.3-cor}
\end{equation}

**Status:** (M1.3-cor) is **conditional** on M1.2-GHK + HD (no other zeros in the disk; distant \(U\) controlled). Not proved.

---

## 4. HD-low package (concrete, non-circular at finite height)

For **diagnostics and finite-height theorems** (not RH):

| Ingredient | Choice |
|------------|--------|
| Zero list | Odlyzko / LMFDB ordinates up to height \(T_0\) |
| Isolation | Verify \(D(\rho,r)\) contains only \(\rho\) among tabulated zeros |
| Distant \(U\) | Sum \(U((s-\rho')\log X)\) over \(\lvert\gamma'-\gamma\rvert\le C\log\gamma\) numerically; bound the tail by \(N(T)\) density |
| \(c_3^{\mathrm{far}}\) | Explicit finite sum + tail majorant at height \(\le T_0\) |

This yields a **rigorous finite-height** check of (M1.3-cor) for known on-line zeros (where \(\beta=1/2\)) and a diagnostic for off-line \(\lvert\zeta\rvert\) minima (not zeros).

---

## 5. Relation to the target lemma

Target lemma (L1): at a zero of **maximal** real part \(Y\),
\[
\lvert A_{X_n}(Y,\gamma)\rvert
\ge
c\,m\log\log X_n.
\]
M1.3 as stated gives an \(O(1)\) (or \(O(m)\)) lower bound on \(\Delta\theta\) along a short path of radius \(r\to 0\). That is **enough to force nontrivial argument motion** near \(\rho\), but **not** by itself the full \(\log\log X\) scale.

To reach \(\log\log X\):
- either enlarge the path / vary \(X\) so that the local factor and the modulus interaction (Akatsuka real \(m\log\log\)) couple into the continuous argument (open analysis),  
- or combine many short paths / a slow radial approach \(s\to\rho\) with \(x=x(s)\) (M1.3-bis, open),  
- then smooth to \(A_X\) (M1.4).

**Honest split:**  
M1.3-semicircle \(\Rightarrow\) order-\(m\) argument jump (conditional).  
Target lemma scale \(\log\log X\) \(\Rightarrow\) still open (needs more than a fixed semicircle).

---

## 6. Implementation sketch (diagnostic)

1. Fix \(\rho\) = first critical zero (or L5 off-line minimum as control).  
2. Choose \(r=c_r/\log\gamma\), \(X=(\log\gamma)^{A}\).  
3. Sample \(s(\varphi)=\rho+r e^{i\varphi}\), \(\varphi\in[0,\pi]\).  
4. Compute continuous \(\arg P_X(s)\), \(\arg Z_X^{\mathrm{trunc}}(s)\), \(\arg\zeta(s)\) with \(U=E_1\).  
5. Report \(\Delta\arg P_X\) vs \(m\pi\) and max \(\lvert\operatorname{Im}\mathcal{E}\rvert\).

Script target: `scripts/rh_M1_3_path_diagnostic.py` (to be implemented).

---

## 7. Status

| Item | Status |
|------|--------|
| Path geometry (semicircle + radius recipe) | **Written** |
| Conditional corollary (M1.3-cor) | **Stated** |
| Proof under HD | **Open** |
| Numeric path diagnostic | **Pending** (`rh_M1_3_path_diagnostic.py`) |
| Full \(\log\log X\) target scale from path alone | **Open** (needs M1.3-bis / M1.4) |
| RH | **Open** |

---

## One-liner

**M1.3 freezes a semicircular path of radius \(\asymp 1/\log\gamma\) about a zero so that \(m\arg(s-\rho)\) contributes order \(m\pi\) while M1.2-GHK and admissible \(c_1,c_2\) control the remainder; the conditional jump \(\Delta\theta\ge\tfrac12 m\pi\) is stated, the \(\log\log X\) target scale and the proof remain open.**

*Per aspera ad astra.*
