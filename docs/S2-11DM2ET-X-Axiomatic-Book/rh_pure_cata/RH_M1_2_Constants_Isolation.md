# M1.2 Constants, Classical Σ, Zero-Density Insertion, Isolation

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
Companion: `RH_E1_Off_Nearline.md` (E1 proof + Off estimates).

---

## 1. Kernel constants (updated)

### \(C_u^{(1)}\) — rigorous
\[
C_u^{(1)}\le e
\quad(\lvert z\rvert\le 1).
\]

### \(C_u^{(0)}\) — **now rigorous** (was working)

**Theorem E1** (`RH_E1_Off_Nearline.md`): for \(\operatorname{Re}w\ge 0\), \(w\neq 0\),
\[
\lvert w\,E_1(w)\rvert\le 1.
\]
**Proof idea:** \(E_1(w)=e^{-w}\int_0^\infty e^{-s}/(w+s)\,ds\) and \(\lvert w+s\rvert\ge\lvert w\rvert\) for \(s\ge 0\).

**Corollary:** for \(\operatorname{Re}z\ge 0\), \(\lvert z\rvert\ge 1\), GHK support \(\log x\ge 1-1/X\),
\[
\lvert U(z)\rvert\le\frac{1}{\lvert z\rvert(1-1/X)}.
\]
For \(X\ge 10\):
\[
\boxed{C_u^{(0),\operatorname{Re}\ge 0}\le\frac{10}{9}<1.12}\quad\text{\textbf{rigorous}.}
\]

Left half-plane (\(\beta>\sigma_0\)): use GHK power / density, not \(C_u^{(0)}\).

```text
C_u1 = e
C_u0_Re_ge_0 = 10/9   # rigorous for X>=10
```

---

## 2. Classical \(\Sigma_{\mathrm{med}}\)

Under published \(A_0\) in \(N(T)\) remainder:
\[
\Sigma_{\mathrm{med}}\le 4A_0\log\lvert t\rvert+o(\log\lvert t\rvert).
\]
Placeholder \(A_0=0.34\) ⇒ \(4A_0\le 1.36\). Bottleneck: \(\asymp\log\lvert t\rvert\).

---

## 3. KLN + far-right Off

KLN table (arXiv:2101.12263) as before.  
**Theorem FR:** far-right \(\lvert\mathrm{Off}_X^{\mathrm{far}}\rvert\) bounded under KLN (see `RH_E1_Off_Nearline.md` Part II).  
**Tension:** FR small and EF remainder small are not free simultaneously for large \(X\).

---

## 4. Isolation / GHK tension

GHK-log \(X=(\log\gamma)^{O(1)}\): \(r_{\mathrm{loc}}\gg\) mean gap ⇒ (Iso) fails typically.  
Iso needs large \(X\); GHK power error wants small \(X\).

---

## 5. Near-line Off

Absolute majorant \(\ll (X^{1-\beta_\star}/\log X)\log T\log(\lvert\gamma_\star\rvert+T)\) — **too large**.  
Signed cancellation = open hard core of B\(_\theta\).

---

## One-liner

> \(C_u^{(0)}\) is rigorous on \(\operatorname{Re}z\ge 0\); far-right Off has a KLN bound; near-line signed Off remains open.
