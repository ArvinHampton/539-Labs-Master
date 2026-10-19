# consistency (Cat A-level bookkeeping check): universal symbolic form (K=13) + exact Gauss data vs the independent
# exact-term engine asym_engine.py (copied unchanged) at orders t^{11/2}, t^{13/2}.  Engine area term: 40-digit quadrature.
import sys, json, time, mpmath as mp, sympy as sp
from hs_coeffs import coeffs
from asym_engine import expansion
a, N = (int(z) for z in sys.argv[1].split('/')); ss = [int(z) for z in sys.argv[2:]]
for s in ss:
    t0 = time.time()
    C = coeffs(s, a, N, 13); eng = expansion(s, a, N, 13)
    row = dict(s=s, x='%d/%d' % (a, N))
    for e in (9, 11, 13):
        v = complex(sp.N(C[e], 30)); w = complex(eng[e])
        row['e%d' % e] = dict(sym=str(v), engine=str(w), absdiff=abs(v - w))
    row['sec'] = round(time.time() - t0, 1)
    print(json.dumps(row), flush=True)
