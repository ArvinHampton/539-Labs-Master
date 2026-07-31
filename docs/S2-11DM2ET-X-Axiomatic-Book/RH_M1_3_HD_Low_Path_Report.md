# M1.3 under concrete HD-low — path report

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. No model constants.  
**Does not prove** RH, M1.2, or M1.3.  
**Does:** freeze a concrete finite-height HD package, run isolation + path diagnostics, and correct the monodromy statement for \(\arg P_X\).

**Companions:**  
`RH_M1_3_Path_Design.md`,  
`RH_M1_2_Optimized_ci_Bounds.md`,  
`RH_Akatsuka_GHK_Survey.md`.  
**Probe:** `scripts/rh_M1_3_path_diagnostic.py` → `rh_M1_3_path_diagnostic_results.json`.

---

## 1. Concrete HD-low package

| Ingredient | Choice |
|------------|--------|
| Zero list | First \(N\) Odlyzko ordinates (table in script; \(N\ge 15\) for neighbours) |
| Isolation | Disk \(D(\rho,2r)\) contains only \(\rho\) among tabulated zeros |
| Radius | \(r=c_r/\log(2+\lvert\gamma\rvert)\), default \(c_r=0.35\) |
| Mediator | \(X=(\log(2+\gamma))^3\) (or fixed via flag) |
| Kernel | \(U=E_1\) |
| Scope | **Finite height only** — non-circular for tabulated zeros; does **not** prove RH |

**Executed:** all 6 tested zeros (first six ordinates) are **HD-isolated** at the chosen \(r\) (nearest gap \(\gg 2r\)).

---

## 2. Two geometries

### 2.1 Semicircle monodromy (control)

\[
s(\varphi)=\rho+r e^{i\varphi},\qquad \varphi\in[0,\pi].
\]
By construction \(\Delta\arg(s-\rho)=\pi\).

**Structural fact:** the finite hybrid factor
\[
P_X(s)=\exp\Bigl(\sum_{n\le X}\frac{\Lambda(n)}{n^s\log n}\Bigr)
\]
is **entire and zero-free**. Therefore continuous \(\arg P_X\) has **no monodromy** about a zero of \(\zeta\). One must have
\[
\Delta_{\mathrm{semi}}\arg P_X = O(r\cdot \lVert\nabla\arg P\rVert)=o(1)
\quad\text{as }r\to 0,
\]
not order \(m\pi\).

**Diagnostic (6 zeros, \(X=(\log(2+\gamma))^3\)):**
\[
\operatorname{mean}\Delta_{\mathrm{semi}}\arg P_X \approx 0.026
\qquad(\ll m\pi\approx 3.14).
\]

**Naive peel** \(R_{\mathrm{peel}}=\log P_X-m\log(s-\rho)\):
\[
\operatorname{mean}\max\lvert\operatorname{Im} R_{\mathrm{peel}}\rvert \approx 3.09 \approx \pi.
\]
So \(\operatorname{Im} R_{\mathrm{peel}}\) tracks \(-m\arg(s-\rho)\) and has size \(m\pi\): the form \(\lvert\operatorname{Im} R_{\mathrm{peel}}\rvert\le c_0 m\lvert\arg\rvert\) with \(c_0<1\) **fails** for this naive peel. The correct remainder must cancel the local Hadamard / \(\log\zeta\) singularity (GHK \(Z_X\) or IvM local factor), not subtract \(m\log(s-\rho)\) from zero-free \(P_X\) alone.

### 2.2 Approach path (correct phase geometry)

\[
s(\sigma)=\sigma+i\gamma,\qquad \sigma:1.5\to \tfrac12+r.
\]
Continuous \(\arg P_X\) along this horizontal segment is the natural object for gradual phase accumulation.

**Diagnostic:**
\[
\operatorname{mean}\Delta_{\mathrm{app}}\arg P_X \approx 0.026
\]
at these low heights / moderate \(X\) — small, as expected for smooth \(P_X\) on a short segment far from the pole at \(s=1\). Large target-lemma scale \(\log\log X\) is **not** seen on a single short approach at the first zeros.

### 2.3 Hybrid residual and distant zeros

| Quantity | Mean over 6 zeros |
|----------|------------------:|
| \(\max\lvert\mathcal{E}\rvert\) on semicircle | \(\approx 3.25\) (large at some heights; window/truncation) |
| \(\max\lvert\operatorname{Im}\log Z_{\mathrm{far}}\rvert\) | \(\approx 0.050\) |
| HD isolated | **6 / 6** |

Distant \(U\) in the window is small; hybrid \(\lvert\mathcal{E}\rvert\) still needs tighter \(X\), fuller zero lists, or smoothed \(\widetilde P_X\) for uniform smallness.

---

## 3. Corrected M1.3 standing statements

| Prior sketch | Corrected status |
|--------------|------------------|
| Semicircle \(\Rightarrow\Delta\arg P\ge \tfrac12 m\pi\) | **False** for zero-free \(P_X\); monodromy is in \(Z_X/\zeta\), not \(P_X\) |
| HD-low isolation at first zeros | **Verified** diagnostically (6/6) |
| Approach path for continuous \(\theta_X\) | **Correct geometry**; low-height \(\Delta\) small |
| Naive \(R_{\mathrm{peel}}=\log P-m\log(s-\rho)\) | **Order \(m\pi\)** — cannot use \(c_0<1\) without regularisation |
| Target \(\log\log X\) scale | **Still open** (needs long path / varying \(X\) / M1.4) |

**Revised M1.3 goal:**  
Construct a path \(\gamma_{\mathrm{path}}\) (typically an approach from \(\operatorname{Re}s\gg 1\) toward \(\rho\), possibly with slow \(X=X(s)\)) on which continuous \(\theta_X=\arg P_X\) becomes large, while a **regularised** remainder (after removing the local \(Z_X\) factor, not after a bare \(m\log(s-\rho)\) peel from \(P\)) stays controlled by M1.2-GHK + admissible \(c_1,c_2\).

---

## 4. Status

| Item | Status |
|------|--------|
| HD-low definition | **Frozen** |
| Isolation at first 6 zeros | **Pass** (diagnostic) |
| Semicircle monodromy of \(\arg P\) | \(\approx 0\) — **as predicted** |
| Approach \(\Delta\arg P\) at low height | **Small** |
| Regularised M1.2 on approach path | **Open** |
| M1.3 proof / target lemma | **Open** |
| RH | **Open** |

---

## One-liner

**Under HD-low, first zeros are isolated at the M1.3 radius; semicircle monodromy of zero-free \(P_X\) is \(\approx 0\) (so the old \(\Delta\theta\ge m\pi/2\) claim is withdrawn for bare \(\arg P\)); approach paths are the correct phase geometry; regularised remainder bounds and \(\log\log X\) growth remain open.**

*Per aspera ad astra.*
