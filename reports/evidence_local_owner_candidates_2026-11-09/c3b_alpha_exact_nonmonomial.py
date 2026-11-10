# Local-derived. O4 follow-up: exhibit an EXACT non-monomial real alpha on K90 with t t* = 1 (so T preserves B).
import numpy as np, itertools, math
from scipy.optimize import least_squares
import sympy as sp
K90 = [3,11,37,41,47,53,61,71,79,83,89]
inv = lambda x: pow(x,-1,140)
def coll_of(S):
    c = {}
    for k,l in itertools.permutations(range(len(S)),2):
        c.setdefault((S[k]*inv(S[l]))%140, []).append((k,l))
    return c
rng = np.random.default_rng(7)
hits = []
for S in itertools.combinations(K90, 3):
    c = coll_of(S)
    f = lambda a: [sum(x*x for x in a)-1] + [sum(a[k]*a[l] for k,l in pr) for pr in c.values()]
    for _ in range(20):
        s = least_squares(f, rng.normal(size=3), xtol=1e-15, ftol=1e-15, gtol=1e-15)
        if np.linalg.norm(s.fun) < 1e-12 and np.all(np.abs(s.x) > 1e-6):
            hits.append((S, tuple(np.round(s.x, 12)))); break
print("3-element supports admitting a full-support real solution:", len(hits))
for S, x in hits[:6]: print("  S =", S, " alpha ~", x)
if hits:
    S, x = hits[0]
    # exact candidate: recognise values among {+-1/3, +-2/3}
    ex = [sp.nsimplify(v, [sp.Rational(1,3)]) for v in x]
    print("exact guess:", S, ex)
    t = {}
    for a,p in zip(ex,S): t[p] = t.get(p,0)+a
    prod = {}
    for p,a in t.items():
        for q,b in t.items():
            g = (p*inv(q))%140; prod[g] = prod.get(g,0) + a*b
    prod = {g:v for g,v in prod.items() if v != 0}
    print("exact t t* =", prod, " -> equals 1:", prod == {1: 1})
    # direct 48x48 exact check of R_t^T B R_t == B
    A = [g for g in range(1,140) if math.gcd(g,140)==1]; idx = {g:i for i,g in enumerate(A)}; n=len(A)
    Rt = sp.zeros(n,n); Bm = sp.zeros(n,n)
    for g in A:
        Bm[idx[g], idx[(-g)%140]] = 1
        for p,a in t.items(): Rt[idx[(p*g)%140], idx[g]] += a
    print("exact 48x48: Rt^T B Rt == B:", (Rt.T*Bm*Rt - Bm) == sp.zeros(n,n))
    print("quotient pattern of S:", {g:len(v) for g,v in coll_of(list(S)).items()})
