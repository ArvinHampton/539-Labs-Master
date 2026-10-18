# Step (1)/(2): numerical asymptotic coefficients c_k(s) of g_s(e^-t), k=0..4, from high-precision direct evaluation + polynomial fit in t.
from mpmath import mp, mpf, exp, matrix, lu_solve, nstr
import json
mp.dps = 80
def g(s, t):
    q = exp(-t); tot = mpf(0); den = mpf(1); n = 0
    while True:
        term = q**(n*n)/den; tot += term
        n += 1; den *= 1 + q**(s*n)
        if n > 20 and term < mpf(10)**(-75): break
    return tot
def coeffs(s, K=4, deg=16, u0=mpf('0.0005'), u1=mpf('0.006')):
    ts = [(u0 + (u1-u0)*i/deg)/max(s, 1) for i in range(deg+1)]
    A = matrix([[t**j for j in range(deg+1)] for t in ts]); b = matrix([g(s, t) for t in ts])
    c = lu_solve(A, b); return [c[j] for j in range(K+1)]
S_ALL = [1, 2] + list(range(3, 21)) + [25, 30, 41]
res = {}
for s in S_ALL:
    c1 = coeffs(s); c2 = coeffs(s, deg=18, u0=mpf('0.0003'), u1=mpf('0.005'))
    stab = max(abs(a-b) for a, b in zip(c1, c2))
    res[s] = dict(c=[nstr(x, 30) for x in c1], stability=nstr(stab, 3))
    print(s, [nstr(x, 18) for x in c1], 'stab', nstr(stab, 3), flush=True)
json.dump(res, open('gs_numeric.json', 'w'), indent=1)
