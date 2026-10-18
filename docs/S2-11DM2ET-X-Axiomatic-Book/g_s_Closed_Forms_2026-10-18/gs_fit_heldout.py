# Step (2): fit c_k(s) as degree<=k polynomials on s in {3..7} (pre-registered fit set), recognise rationals, test held-out s.
import json, sympy as sp
from mpmath import mp, mpf
mp.dps = 40
d = json.load(open('gs_numeric.json')); s = sp.symbols('s')
FIT = [3, 4, 5, 6, 7]; HELD = [k for k in map(int, d) if k not in FIT]
out = []
for k in range(5):
    pts = [(si, sp.nsimplify(sp.Float(d[str(si)]['c'][k], 25), rational=True, tolerance=1e-9)) for si in FIT]
    poly = sp.expand(sp.interpolate(pts, s))
    out.append(f"c_{k}(s) = {poly}   [degree {sp.degree(poly, s) if poly != 0 else 0}]")
    worst = 0; worst_s = None
    for si in HELD:
        num = mpf(d[str(si)]['c'][k]); pred = mpf(str(sp.N(poly.subs(s, si), 40)))
        rel = abs(num - pred)/max(1, abs(pred))
        if rel > worst: worst, worst_s = rel, si
    out.append(f"   held-out {HELD}: worst rel. dev {float(worst):.2e} at s={worst_s}  (num. stability of that s: {d[str(worst_s)]['stability']})")
print("\n".join(out)); open('gs_fit_heldout.txt', 'w').write("\n".join(out) + "\n")
