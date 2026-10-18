# Path B pre-registration: radial expansion of H_s at x = 0 (written before any H_s numerics or symbolic runs)

**Definition (Master, Residual_Bridge_Series_C_Definition.md lines 11-36):**
- H_s = sum_{v in Z^2} w(v) q^{Q_s(v)}, with Q_s(n,k) = n^2 + s n k + (s/2) k(k+1).
- w = (sgn B(c1,v) - sgn B(c2,v))/2, with B(c,v) = c^T M v, M = [[2,s],[s,s]], c1 = (-1,1), c2 = (-4,1).
- C := P_s - H_s.

**Disclosed hand derivation (done before this file).**
- B(c1,v) = (s-2)n and B(c2,v) = (s-8)n - 3sk.
- {w>0} is the cone K = {x r1 + y r2 : x, y > 0}, with r1 = (0,1) and r2 = (3s, s-8)/g, g = gcd(24, s-8). Both edges carry weight 1/2.
- w(-v) = -w(v), and Q_s(-v) = Q2(v) - (s/2)k.
- Hence H_s = sum_{w>0} w(v) e^{-tQ2(v)} (e^{-tsk/2} - e^{tsk/2}), which is odd in the linear term.
- The cosets of Z^2 / (Z r1 + Z r2) have index m = 3s/g. Their offsets are y0 = j/m and x0 = {-b j/m}, with b = (s-8)/g.
- A 2-D Euler-Maclaurin power count then gives the predictions below.

**Predictions (s >= 5, where Q(c2) < 0):**
- PB1. The t^{-1} coefficient is 0.
- PB2. The t^{-1/2} coefficient is -s * \int\int_K k e^{-Q2(v)} dv. This is algebraic in s, lies in sqrt(pi) Q(s, sqrt(2s), sqrt(2s(7s^2-46s+64))), and does not depend on g.
- PB3. The t^0 coefficient of H_s is 0 for all s >= 5.
- PB4. The t^{1/2} coefficient is algebraic and of the form A(s) + g^2 B(s), with A, B in sqrt(pi) Q(s, sqrt(2s), sqrt(...)). So it is quasi-algebraic: it depends on s mod 24 only through g.
- PB5. The t^1 coefficient is rational for each s. It is given by corner terms with Dedekind-Rademacher sums sum_j B2({-bj/m}) B1(j/m) (and with B1, B2 swapped). It is predicted to be a rational function of s on each residue class s mod 24 (by reciprocity), not one global rational function.
- PB6. For C = P_s - H_s:
  - C_{-1} = Res/2;
  - C_{-1/2} = P_{-1/2} - H_{-1/2}; the s=7 fitted value in 2026-10-17-Bridge-C B4 is about 0.8174;
  - C_0 = P_0 = (1+E_0)/2;
  - C_{1/2} = P_{1/2} - H_{1/2};
  - C_1 = E_1/2 - H_1.

**Protocol:**
1. Compute exact per-s coefficients by symbolic Euler-Maclaurin for s = 5..20, 25, 30, 41, plus s up to 300 for the fits.
2. Check numerically by direct summation at s = 5, 7, 8, 11, 13, 20.
3. Fit set for PB5 rational forms: s <= 150. Held out: 151..300 and every s in the standard list not used.
4. A closed form passes only if it is exact (rational equality) on every held-out s.
