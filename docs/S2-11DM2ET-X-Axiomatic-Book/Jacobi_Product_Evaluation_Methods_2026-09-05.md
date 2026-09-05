Jacobi product evaluation methods
2026-09-05

Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds.
This note catalogues methods that evaluate products of j(x; q).
It does not compute the y to q^8 limit.
It does not occupy Slash_two, Object B, OccFilt_7, C, or g_s.
Twin Prime and Riemann Hypothesis unclaimed.

j(x; q) equals (x; q)_infty times (q over x; q)_infty times (q; q)_infty.
Jbar_{n, m} equals j(minus q^n; q^m).
Target remainder is theta_{2,8,8}(q, y, q) over Jbar_{0,24} Jbar_{0,6}. Sixteen terms. Denominator independent of y.

Theorem identities.
Zero locus: j vanishes iff x is an integer power of q.
Translation, inversion, splitting, power, four-term addition, two-factor product-to-sum.
Jbar_{0,24} and Jbar_{0,6} are holomorphic in y and nonzero as functions of y.

Numerical recipes.
Truncated Pochhammer. Truncated bilateral sum. First-order expansion at a simple zero. Coefficient checks, not closed forms.

Method order for U7, not executed this pass.
Read vanishing of the sixteen terms at y equals q^8. Keep lowest-order survivors. Reduce by translation and splitting. Or run a coefficient window.
Occupancy of U7 is the value of the full quotient in the limit, not the observation that some terms vanish.

These methods are not C, not Slash_two, not Convention A versus B.
No new residual-flux object.
CORE_FREEZE unchanged.
