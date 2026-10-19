# Goal 1: conceptual rule for the x = 1/3 edge data ea_r, verified EXACTLY (sympy, algebraic numbers) against
# the defining Gauss-Bernoulli sums of gauss_data.py (copied unchanged from 2026-10-18-Open-Analytic/).
# Theorem (proved in the report):  with g2 = gcd(8,s), eps = g2 mod 3 in {+1,-1}  (eps = (-1)^{v2(gcd(s,8))}),
#   b = (s-8)/g,  omega = e(1/3):
#   s = 0,1 mod 3 : ea_r = eb_r if b = 2 mod 3, ea_r = (-1)^r eb_r if b = 1 mod 3   [b = eps (s=0), b = -eps (s=1)]
#   s = 2 mod 9   : ea = 0
#   s = 5 mod 9   : ea_r = eb_r (eps = -1) or (-1)^r eb_r (eps = +1)
#   s = 8 mod 9   : ea_r = 2^{2-r} i sqrt3 sum_{c=0}^{2} omega^{-eps c} Bt_r(c/3)
import sympy as sp, math, json, sys
from gauss_data import data
Bt = lambda r, u: sp.Integer(0) if (r == 1 and u == 0) else sp.bernoulli(r, u)
w = sp.exp(2*sp.pi*sp.I/3)
R = 10
X = sp.Symbol('X')
def predict(s, eb):
    g = math.gcd(24, s - 8); b = (s - 8)//g; eps = 1 if math.gcd(8, s) % 3 == 1 else -1
    tw = {r: (-1)**r*eb[r] for r in eb}
    if s % 3 in (0, 1):
        assert b % 3 == (eps if s % 3 == 0 else -eps) % 3
        return eb if b % 3 == 2 else tw
    if s % 9 == 2: return {r: sp.Integer(0) for r in eb}
    if s % 9 == 5: return eb if eps == -1 else tw
    return {r: sp.Integer(2)**(2 - r)*sp.I*sp.sqrt(3)*sum(w**(-eps*c)*Bt(r, sp.Rational(c, 3)) for c in range(3)) for r in eb}
lo, hi = int(sys.argv[1]), int(sys.argv[2])
bad = []; n = 0
for s in range(lo, hi + 1):
    d = data(s, 1, 3, R=R)
    pr = predict(s, d['eb'])
    for r in range(1, R + 1):
        diff = sp.expand(sp.expand_complex(d['ea'][r] - pr[r]))
        re_, im_ = [sp.radsimp(sp.nsimplify(v) if False else v) for v in diff.as_real_imag()]
        if not (sp.minimal_polynomial(re_, X) == X and sp.minimal_polynomial(im_, X) == X): bad.append((s, r))
    n += 1
print('checked s = %d..%d (%d values), r = 1..%d: mismatches = %s' % (lo, hi, n, R, bad))
# explicit V vectors (s = 8 mod 9)
for eps in (1, -1):
    print('eps=%+d V_r:' % eps, [sp.radsimp(sp.expand_complex(sp.Integer(2)**(2 - r)*sp.I*sp.sqrt(3)*sum(w**(-eps*c)*Bt(r, sp.Rational(c, 3)) for c in range(3)))) for r in range(1, 7)])
