# Appendix — Moments, RMT, CFKRS (Cat A background)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Role:** background for on-line modulus means. **Not** an arg lower bound. **Not** an RH proof.

---

## 1. Keating–Snaith

Characteristic polynomials of random unitary matrices model \(\zeta(1/2+it)\).  
Leading moment:

\[
\frac{1}{T}\int_0^T\bigl\lvert\zeta(\tfrac12+it)\bigr\rvert^{2k}\,dt
\sim a_k g_k (\log T)^{k^2},
\]

with arithmetic factor \(a_k\) and RMT factor \(g_k=G^2(k+1)/G(2k+1)\).

---

## 2. CFKRS recipe (schematic)

Conrey–Farmer–Keating–Rubinstein–Snaith: approximate functional equation → diagonal and off-diagonal combinatorial sums → residue integrals yielding a polynomial \(P_k\) of degree \(k^2\) in \(\log T\).

| \(k\) | Standing for full main term |
|-------|-----------------------------|
| \(k=1\) (2nd moment) | Classical theorem |
| \(k=2\) (4th moment) | Theorem (Ingham leading; Heath-Brown / CFKRS full \(P_2\)) |
| \(k\ge 3\) | Conjectural in number field; theorems in many function-field settings |

---

## 3. GHK moments of \(P_X\)

Unconditionally (GHK Thm 2), for \(1/2\le\sigma\le 1\) and suitable \(X\),

\[
\frac1T\int_T^{2T}\lvert P_X(\sigma+it)\rvert^{2k}\,dt
\sim a(k,\sigma)F_X(k,\sigma).
\]

On the line, \(F_X(k,1/2)=(e^\gamma\log X)^{k^2}\).  
This supports **mean** control of \(U_X=\log\lvert P_X\rvert\), not pointwise \(\theta_X\).

---

## 4. Function-field analogs

Katz–Sarnak monodromy philosophy: low-lying zeros of families follow classical compact groups.  
In function fields, many moment and equidistribution statements are **theorems**.  
**No automatic transfer** to RH for \(\zeta_{\mathbb{Q}}\).

---

## 5. Use in this programme

| Use | Do not use |
|-----|------------|
| Motivation for Conjecture A (on-line control) | As proof of Conjecture B |
| Choice of \(X=(\log t)^{O(1)}\) scales | As substitute for M1.2 |
| Cross-check L5 modulus \(U_x\) | As RH announcement |

---

## Citations

- J. P. Keating, N. C. Snaith, *Random matrix theory and \(\zeta(1/2+it)\)*, Comm. Math. Phys. **214** (2000), 57–89.
- J. B. Conrey et al., *Integral moments of \(L\)-functions*, Proc. London Math. Soc. **91** (2005), 33–104 (CFKRS).
- S. M. Gonek, C. P. Hughes, J. P. Keating, Duke Math. J. **136** (2007), 507–549.
- N. M. Katz, P. Sarnak, *Random matrices, Frobenius eigenvalues, and monodromy*, AMS Colloquium Publications **45**, 1999.
