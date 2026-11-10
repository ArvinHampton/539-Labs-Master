# t809u E1–E3 geometric residual-smallness hunt — ABSENT-with-gap (2026-10-25)
This is a corpus-only search. Locks: invent-ban; CORE_FREEZE; SF-W7-3; no order78; 4da09dec… NOT revived; #7–#9 HOLD. No E-schema is invented. Relates to t808u 6cb605e1… and leaves it standing.
Search terms: cusp width, Fricke orbit, Herglotz, positive real part, majorant, regulator bound, contour deformation. Searched BRIDGE_C_35 (order46/49/51, NOTES*, deduce_*), papers, theorems, maths.

## Geometric Written items found and how each was judged
- Cusp width / Fricke-orbit bounds / regulator bound / positive-real-part bound: 0 Written hits in that sense.
- Herglotz (e7967dde s09_herglotz.tex; t761u E-α MX-β): this gives the ψ boundary value / co-shift extension to x+iε. It is an identity or extension, not a bound. No smallness.
- Truncation-tail majorant (t722u PREREG 36b663d3… (B1); RESULTS 9aa52f19…): T(ε) ≤ Σ_{ν>106} M(ν)(2ν)^{-1/2}e^{-2πνε}. It is analytic, so it is independent of order46, but it bounds the truncation tail and not the residual. On the same contour, F1 FAILS: |δ_ε| ≫ tol at every ε. F3 shows the residual is controlled only regularized at ε≥0.02, and the majorant diverges at ε=0. The E-α contour geometry (t761u accept) therefore gives no smallness. It actually shows δ≠0, and δ≡0 is a dead end anyway.
- order2/order3c Taylor majorants: these are area-term asymptotics, not a residual bound.

## Verdict
ABSENT-with-gap. 0 Written geometric residual-smallness levers are independent of order46.
Gaps: (i) as in t808u, E1–E3 is never defined as a residual-smallness track; (ii) there is no Written geometric bound on the k≠0 phase sum that could replace order46/51's phase-aware Σ; (iii) there is no ε→0 control (AB-β is Written-ABSENT).
Bridge PARTIAL; READY NO; residual-C OPEN; B1 open; no order78.
