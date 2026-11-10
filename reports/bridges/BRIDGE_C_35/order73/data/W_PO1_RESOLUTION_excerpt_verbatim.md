# W-PO-1 Resolution: Consistent Q_s, H_s Definition, and Linear-Term Alignment
**Date:** 2026-10-24  
**Status:** Resolution of sign discrepancy and undefined H_s (Category A discrete).  
**Hygiene:** Residual-flux provenance under Principle (S) mandatory. CORE_FREEZE intact. Residual law for C remains open. Maps kept separate.

## Locked definitions (from residual manuscript)

Gram matrix of the indefinite lattice:
\[
M = \begin{pmatrix} 2 & s \\ s & s \end{pmatrix}, \qquad \det M = -s(s-2).
\]

Path quadratic form (orthant and cone):
\[
Q_s(n,k) = n^2 + s\, n k + \frac{s}{2} k(k+1).
\]

Orthant path-count series:
\[
\hat{P}_{\rm orth}(q) = P_s = \sum_{n,k \geq 0} q^{Q_s(n,k)}.
\]

Cone series (signed full-lattice sum):
\[
H_s = \sum_{v \in \mathbb{Z}^2} w(v)\, q^{Q_s(v)},
\]
where the residual sign weight is
\[
w(v) = \frac12\bigl(\operatorname{sgn} B(c_1,v) - \operatorname{sgn} B(c_2,v)\bigr)
\]
and the locked negative-norm cones for \(s=7\) are \(c_1 = (-1,1)\), \(c_2 = (-4,1)\).

Bridge Series:
\[
C := \hat{P}_{\rm orth} - H_s.
\]
Locked identity: \(P_s = H_s + C\).

## Linear-term resolution

The orthant form uses the triangular factor \(k(k+1)\), giving linear contribution \(+\frac{s}{2}k\) after expansion.

The third-quadrant piece of \(C\) is
\[
C_{\rm third} = \sum_{n,k\geq 1} q^{n^2 + 7nk + \frac72 k(k-1)}.
\]
Completion of the square on this exponent yields
\[
n^2 + 7nk + \frac72 k(k-1) = \Bigl(n + \frac72 k\Bigr)^2 - \frac{35}{4}k^2 - \frac72 k.
\]
The linear term \(-\frac72 k\) is therefore an identity of the third-quadrant rewrite only; it does not alter the orthant form \(Q_s\) used in \(\hat{P}_{\rm orth}\) and \(H_s\).

Both expressions are consistent under the locked residual packaging. The sign difference is structural (orthant triangular factor versus third-quadrant index shift), not a contradiction.

## Status

- \(H_s\) is now defined.
- Linear-term alignment is recorded.
- Local numeric evaluation of \(C = \hat{P}_{\rm orth} - H_s\) is unblocked for the residual lattice.

**Pin status:** W-PO-1 resolved as of 2026-10-24.  
**CORE_FREEZE:** Intact.
