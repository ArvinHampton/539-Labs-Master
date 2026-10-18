# Item (1): which Gauss-Bernoulli 'atomic' sums of the proved expansion vanish at x = 1/2 for odd s?
#   T0 = sum_p phi(p);  TE_beta[r] = sum_p phi(p) Bt_r(beta_p);  TE_alpha[r] = sum_p phi(p) Bt_r(alpha_p);  TC[r,r'] = sum phi Bt_r(al) Bt_r'(be)
import math, sympy as sp, json, sys
from fractions import Fraction as Fr
def bern(r, c):
    if r == 1 and c == 0: return Fr(0)
    v = sp.bernoulli(r, sp.Rational(c.numerator, c.denominator)); return Fr(int(v.p), int(v.q))
def atomic(s, a, N, R=6):
    g = math.gcd(24, s-8); m = 3*s//g; b = (s-8)//g; P = 2*N
    pieces = []
    for n in range(P*m):
        be = Fr(n, P*m); kmin = math.ceil(Fr(b*n, m))
        for k in range(kmin, kmin+P+1):
            al = Fr(k - Fr(b*n, m), P)
            if 0 <= al < 1: pieces.append((al, be, n*n + s*n*k + s*k*(k+1)//2, n*n + s*n*k + s*k*(k-1)//2))
    res = {}
    for sg, idx in (('+', 2), ('-', 3)):
        # phases are N-th roots of unity: keep exact as dict exponent -> rational coefficient
        def S(f):
            acc = {}
            for p in pieces:
                e = (a*p[idx]) % N; acc[e] = acc.get(e, 0) + f(p)
            return {e: v for e, v in acc.items() if v != 0}
        res[sg] = dict(T0=S(lambda p: 1),
                       TEb={r: S(lambda p, r=r: bern(r, p[1])) for r in range(1, R+1)},
                       TEa={r: S(lambda p, r=r: bern(r, p[0])) for r in range(1, R+1)},
                       TC={(r1, r2): S(lambda p, r1=r1, r2=r2: bern(r1, p[0])*bern(r2, p[1])) for r1 in range(1, R+1) for r2 in range(1, R+1)})
    return res
if __name__ == "__main__":
    for s in (7, 9, 11, 13, 6, 10):
        r = atomic(s, 1, 2, 5)
        def nz(d):   # for N = 2: value = coeff(e=0) - coeff(e=1)
            return d.get(0, 0) - d.get(1, 0)
        out = {sg: dict(T0=str(nz(r[sg]['T0'])),
                        TEb=[str(nz(r[sg]['TEb'][k])) for k in range(1, 6)],
                        TEa=[str(nz(r[sg]['TEa'][k])) for k in range(1, 6)],
                        TC_nonzero=sum(1 for k, v in r[sg]['TC'].items() if nz(v) != 0)) for sg in r}
        print(s, json.dumps(out))
