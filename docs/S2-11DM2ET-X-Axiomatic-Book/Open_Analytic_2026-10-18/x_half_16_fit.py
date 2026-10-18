# Rational reconstruction of the 16|s correction at x = 1/2 (values from asym_engine):
#   dev_e := h_e(1/2)/sqrt(2 pi s) - generic_e(s);  per g-class (g = 8 or 24 when 16 | s) fit
#   dev_e * sqrt(Delta) * (s-2)^a (7s-32)^b = polynomial in s  (interpolate on deg+1 points, check the rest exactly),
#   then write it as A(s) + g^2 B(s)  (exact interpolation between the two classes).
import json, sympy as sp, mpmath as mp
mp.mp.dps = 40
d = json.load(open('x_half_16.json')) + json.load(open('x_half_16_more.json')); s, g = sp.symbols('s g')
out = []
for e, (a, b), deg in ((1, (1, 1), 1), (3, (1, 2), 3), (5, (2, 3), 6)):
    P = {}
    for gv in (8, 24):
        pts = [(r['s'], sp.Rational(sp.nsimplify(mp.mpf(r[f'dev{e}_times_sqrtD'])*(r['s']-2)**a*(7*r['s']-32)**b, rational=True, tolerance=1e-18)).limit_denominator(10**8)) for r in d if r['g'] == gv]
        poly = sp.expand(sp.interpolate(pts[:deg+1], s)); held = [sp.simplify(poly.subs(s, x) - y) == 0 for x, y in pts[deg+1:]]
        P[gv] = poly
        out.append(f"e={e} g={gv}: {sp.factor(poly)}   [deg {deg}, {len(pts)} pts, held-out exact {sum(held)}/{len(held)}]")
        print(out[-1])
    B = sp.expand((P[24] - P[8])/(576 - 64)); A = sp.expand(P[8] - 64*B)
    out.append(f"e={e} combined: dev*sqrt(Delta)*(s-2)^{a}*(7s-32)^{b} = {sp.factor(A)}  +  g^2*({sp.factor(B)})"); print(out[-1])
open('x_half_16_fit.txt', 'w').write("\n".join(out) + "\n")
