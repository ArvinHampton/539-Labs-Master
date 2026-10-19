# consistency: the K = 13 universal pickles reproduce the archived K = 9 ones (orders t^{-1/2}..t^{9/2}) exactly
import pickle, sympy as sp
from sym_engine import s, g
for P in (1, 4, 6):
    A = pickle.load(open('sym_universal_P%d_K13.pkl' % P, 'rb')); B = pickle.load(open('../2026-10-18-Open-Analytic/sym_universal_P%d_K9.pkl' % P, 'rb'))
    bad = []
    for e in B:
        for i in range(3):
            x, y = A[e][i], B[e][i]
            if i == 0: d = [sp.simplify(x - y)]
            else: d = [sp.simplify(x.get(k, 0) - y.get(k, 0)) for k in set(x) | set(y)]
            if any(v != 0 for v in d): bad.append((e, i))
    print('P=%d: orders %s identical: %s' % (P, sorted(B), 'yes' if not bad else bad), flush=True)
