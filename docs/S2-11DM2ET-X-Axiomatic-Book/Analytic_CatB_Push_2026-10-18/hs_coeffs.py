# exact (symbolic) radial coefficients c_e(s, x) of H_s(e(x) e^{-t}) from the universal form + exact Gauss data.
import pickle, sympy as sp, math
from sym_engine import s as S, g as Gs
from gauss_data import data
_U = {}
def U(P, K):
    if (P, K) not in _U: _U[(P, K)] = pickle.load(open('sym_universal_P%d_K%d.pkl' % (P, K), 'rb'))
    return _U[(P, K)]
def coeffs(s, a, N, K=13):
    P = 2*N if N > 1 else 1
    if N == 1:
        Bt = lambda r: sp.Integer(0) if r == 1 else sp.bernoulli(r, 0)
        d = dict(g=math.gcd(24, s-8), gamma0=sp.Integer(1), eb={r: Bt(r) for r in range(1, K+4)}, ea={r: Bt(r) for r in range(1, K+4)})
    else:
        d = data(s, a, N, R=K + 3)
    out = {}
    for e, (A, Yc, Xc) in U(P, K).items():
        val = d['gamma0']*A + sum(d['eb'][k]*Yc[k] for k in Yc) + sum(d['ea'][k]*Xc[k] for k in Xc)
        out[e] = val.subs({S: s, Gs: d['g']})
    return out
