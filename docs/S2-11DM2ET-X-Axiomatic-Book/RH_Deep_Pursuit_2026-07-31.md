# Deep rigorous pursuit — four solid directions (2026-07-31)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. Axiom **ZLA**. No model constants.  
**Does not prove RH or O-TL.**  
**Master context:** tip after `9ae3428`; this note freezes deeper pursuit of Directions 1–4.

**Companions:**  
`RH_Existing_Theorems_Solid_Directions.md`,  
`RH_M1_2_Effective_Density.md`,  
`RH_Resonance_Discrepancy_Attack.md`,  
`RH_Remaining_Analytic_Obligations.md`.

---

## 0. Standing status

| Item | Status |
|------|--------|
| On-line strong Omega (fixed \(X\), line) | **Accepted** |
| Conditional M1.2 architecture | **Accepted** |
| Concrete density constants plugged for M1.2 | **This note — Direction 2 advanced** |
| Off-line resonance / Gonek-arg / path continuation | **Open lemmas stated** |
| O-TL / RH | **Open** |

---

## Direction 2 — Concrete density inputs (advanced)

Published explicit Ingham-type bounds supply fully numerical majorants for the conditional M1.2 architecture.

### 2.1 Chourasiya–Simonič (2025) — explicit Ingham form

Source: arXiv:2507.15184 (explicit form of Ingham’s zero-density estimate).  
Range: \(T\ge H_{\mathrm{RH}}=3\cdot 10^{12}\).

**Working statements (usable now):**

- For \(\sigma\in[0.500,0.625]\):
  \[
  N(\sigma,T)
  \le
  8.604\,T^{3(1-\sigma)/(2-\sigma)}\log^3 T
  +
  9.461\log^2 T
  +
  167.8\log T.
  \]

- For \(\sigma\in[0.625,0.875]\):
  \[
  N(\sigma,T)
  \le
  22.44\,T^{3(1-\sigma)/(2-\sigma)}\log^3 T
  +
  8.290\log^2 T
  +
  147.0\log T.
  \]

Finer interval-by-interval constants \((B_1,B_2,B_3)\) of width \(1/32\) are tabulated in the same work (e.g. \(B_1=5.360\) on \([0.500,0.53125]\); \(B_1\) grows toward \(\sigma\to 1\)).

### 2.2 Alternative explicit shapes

- **Ramaré / Kadiri–Lumley–Ng:** forms with exponent \(\frac83(1-\sigma)\) and fully numerical leading coefficients on \(T\ge 3\cdot 10^{10}\) (or \(T\ge 2000\) in Ramaré’s form). Reference: arXiv:2101.12263 / J. Math. Anal. Appl. 465 (2018).
- **Near \(\sigma=1\):** Bellotti-type bounds \(N(\sigma,T)\le C'T^{B(1-\sigma)^{3/2}}(\log T)^{C''}\) for \(\sigma\ge 0.98\) with explicit \(C',B,C''\).

### 2.3 Insertion procedure into M1.2 (rigorous bookkeeping)

1. Fix one published bound, e.g. Chourasiya–Simonič with \(B_1=8.604\), log-power \(3\), secondary \(9.461,167.8\), on \(\sigma\in[1/2,0.625]\), \(T\ge 3\cdot 10^{12}\).
2. Along an isolating path of radius \(r\asymp 1/\log\gamma\) about a point of height \(\gamma\ge 3\cdot 10^{12}\), partition far zeros into dyadic annuli \(|s-\rho|\in[2^k r,2^{k+1}r]\).
3. On each annulus majorize the zero count by the explicit \(N(\sigma_k,\cdot)\) formulae.
4. Sum the geometric series of \(U\)-contributions (as in `RH_M1_2_Effective_Density.md` Lemmas M12-Ubound / M12-Far / M12-Count).
5. Outcome: a fully numerical upper bound on the far-zero part of \(\operatorname{Im} R_{\mathrm{reg}}\), conditional only on the cited density theorem and \(\gamma\ge 3\cdot 10^{12}\).

**Status of Direction 2 after this note:**  
Architecture **+** concrete constants **available**. Remaining arithmetic step: compute a specific numerical threshold \(\gamma_1\) for one fixed \((B_1,B_2,B_3)\) triple and one fixed \((c_r,A_X,\varepsilon_0)\). That computation is finite and does **not** produce phase; it only controls the remainder.

**Does not close O-M1.2 as a uniform theorem for all heights below \(3\cdot 10^{12}\)** without additional density bounds on lower ranges.

---

## Direction 1 — Off-line resonance (precise open lemma)

**On-line fact (accepted).**  
For each fixed large \(X\), Kronecker density on the prime-angle torus yields
\[
\limsup_{t\to\infty}\bigl|\operatorname{Im} D_X(\tfrac12+it)\bigr|
\asymp
\sum_{p\le X}p^{-1/2}
\asymp
\frac{\sqrt X}{\log X},
\]
GHK error absorbed for fixed \(X\) as \(t\to\infty\).

**Open lemma (off-line resonance).**  
There exist absolute constants \(c_0,X_0>0\) and a sequence \(t_n\to\infty\) such that for every \(X\ge X_0\) and every \(\delta\in(0,\delta_0(X)]\),
\[
\bigl|\operatorname{Im} D_X(\tfrac12+\delta+it_n)\bigr|
\ge
c_0\frac{\sqrt X}{\log X}
\]
while
\[
\bigl|\mathcal{E}_{\mathrm{GHK}}(\tfrac12+\delta+it_n,X)\bigr|
\le
\tfrac12 c_0\frac{\sqrt X}{\log X}.
\]
Consequently the hybrid discrepancy satisfies the same lower bound.

**Obstacles (must be controlled rigorously):**

| Obstacle | Content |
|----------|---------|
| Hybrid error off the line | Growth of \(\mathcal{E}_{\mathrm{GHK}}\) as \(\sigma=\tfrac12+\delta\) |
| Nearby zeros | Contribution of zeros in a disk of radius \(\asymp 1/\log X\) about \(s_n\) |
| Branch vs principal value | Continuous \(\theta_X\) vs principal \(\operatorname{Im} D_X\) off the line |
| Correlation | Dependence between torus alignment maximising \(\operatorname{Im} D_X\) and nearby zeros |

**No proof claimed.** The on-line Kronecker argument does not transfer automatically.

---

## Direction 3 — Argument form of Gonek’s approximation (open lemma)

Gonek’s finite-product theorems give **modulus** approximation. The argument version needed for O-TL:

**Open lemma.**  
Let \(Y\) be the maximal real part of zeros up to height \(T\). For \(X=T^\theta\) with fixed \(\theta\in(0,1)\) and points \(s=\sigma+it\) with \(\sigma\ge Y-\varepsilon\), \(|t|\asymp T\), and \(|\zeta(s)|\le T^{-c}\), show that
\[
\bigl|\arg\zeta(s)-\arg P_X(s)\bigr|
=
o\bigl(|\arg\zeta(s)|\bigr)
\]
(or \(o\) of the hybrid discrepancy) along a short path to \(s\). Then a large lower bound for \(\arg\zeta\) transfers to \(\arg P_X\).

**Status:** Existing Gonek results control \(|\zeta/P_X|-1\); they do not yet control the **argument** difference at maximal abscissa.

---

## Direction 4 — Path continuation from on-line Omega (open differential bound)

**Known reservoir.**  
On the critical line, for fixed large \(X\), the hybrid discrepancy is infinitely often \(\gg\log\log X\) (model size \(\asymp\sqrt X/\log X\)).

**Open differential bound.**  
Along a horizontal or slightly inclined path from \(\tfrac12+it_*\) to \(\sigma_*+it_*\) (\(\sigma_*\) maximal abscissa),
\[
\biggl|\frac{\partial}{\partial\sigma}\Delta_X(\sigma+it_*)\biggr|
\le
\Phi(\sigma,t_*,X),
\]
where \(\Phi\) is an explicit majorant built from \(|\zeta'/\zeta|\) and the hybrid remainder. If
\[
\int_{1/2}^{\sigma_*}\Phi(\sigma,t_*,X)\,d\sigma
\]
is strictly smaller than the initial size of \(\Delta_X\), the large value survives the continuation.

\(\Phi\) must be estimated by the explicit formula plus the density bounds of Direction 2. **Open.**

---

## Synthesis — depth of the programme after this push

| Direction | After this note |
|-----------|-----------------|
| **2** Effective density | Concrete published constants **recorded**; insertion procedure **ready**; numerical \(\gamma_1\) still open as finite arithmetic |
| **1** Resonance off the line | Precise open lemma + obstacle list |
| **3** Gonek-style off the line | Precise open argument lemma |
| **4** Path continuation | Precise open differential bound |
| **O-TL** | **Open — primary** |
| **RH** | **Open** |

---

## Explicit non-claims

- No off-line phase lower bound near zeros of maximal real part.  
- No completion of O-TL.  
- No RH.  
- No silent weakening of O-TL to on-line limsup.  
- No model constants in theorem environments.

---

## One-liner

**Direction 2 now has concrete explicit density constants (Chourasiya–Simonič and alternatives) ready for M1.2 insertion; Directions 1, 3, 4 are stated as precise open lemmas with identified obstacles; O-TL and RH remain open.**

*Per aspera ad astra.*
