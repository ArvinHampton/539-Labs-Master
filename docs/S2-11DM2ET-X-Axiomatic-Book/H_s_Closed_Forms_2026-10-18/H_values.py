# Exact per-s H_s radial coefficients from H_em (symbolic EM), s = 5..20,25,30,41 (+ more for fits).
import sympy as sp, pickle, sys
from H_em import H_coeffs
big = len(sys.argv) > 1 and sys.argv[1] == 'big'
S = sorted(set(list(range(5, 21)) + [25, 30, 41] + (list(range(21, 301)) if big else []))); out = {}
for sv in S:
    c, (gv, mv, bv), d = H_coeffs(sv)
    out[sv] = {k: str(v) for k, v in c.items()}; out[sv]['g'] = gv
    if not big: print(f"s={sv} g={gv} m={mv}: " + "; ".join(f"t^{sp.Rational(k,2)}: {sp.N(v,15)}" for k, v in c.items()), flush=True)
pickle.dump(out, open('H_values%s.pkl' % ('_big' if big else ''), 'wb'))
