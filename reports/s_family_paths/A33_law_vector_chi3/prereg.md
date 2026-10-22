# A33 preregistration (written before any computation in this folder)

Source of the "35-component law" (called B3 in Bridge_C_Residual_Law_2026-10-17.md line 173; B2 in
CatB_Notes_Bridge_C_Residual_Law_2026-10-17.md): the vector of leading (1/t) radial profiles
G_{al,be}(x) = mean_{nu in al+Z^2} e(x Q(nu) + B(nu,be)), Q(nu)=nu^T A nu/2, A=[[2,7],[7,7]], x in Q,
"expected to transform by the weight-1 Weil representation" (singular parts only; cone sums themselves not modular).
Exact S-law (from P_s_Structure A5): G_{a,b}(-1/x) = (1/(sqrt35 x)) e(B(a,b)) sum_p G_{b+p,-a}(x), a=(7/10,-1/5).

The source does not fix which 35 (al,be) pairs form "the" vector. Candidates (mu over D = A^{-1}Z^2/Z^2):
- K1: g_mu = G_{a+mu, a}
- K2: g_mu = G_{a+mu, 0}
- K3: g_mu = G_{mu, a}
- K4: g_mu = G_{mu, 0}
Test for each: does there exist k in 0..11, rho in {rho35, rho35*} (A32 conventions, eps=i), weight factor x^{-1} or x^{+1},
and a fixed sign/label identification mu <-> A32 label r = -35 mu mod 35 (also tried: mu -> -mu, which is S^2 up to scalar),
such that g(-1/x) = x^{w} chi^k(S) rho(S) g(x) and g(x+1) = chi^k(T) rho(T) g(x) on all test rationals
(h/m, 1<=m<=12, 0<h<=3m, gcd=1)? Pass threshold 1e-10 (float, Cat B); exact Z[zeta] check at selected x for the decisive claims.
Then: P_{--} g (projector (1-Z5)(1-Z7)/4), and Phi(g) with A32 X_chi3.
Decision rule: "lands" iff some candidate that passes the Weil test has P_{--} g != 0 (certified exactly at >=1 rational)
AND its multiplier is rho35 (x) chi^3 or can be made so by a weight-3 eta^6 twist that is defined on the object;
"does not land" iff all passing candidates have P_{--} g == 0 identically on tests (and proved);
otherwise "undetermined".
