# Local-derived. O4 follow-up 2: inspect numerical solutions of t t* = 1 on K90 (11 variables) and test exact recognition.
import numpy as np, itertools, math
from scipy.optimize import least_squares
import sympy as sp
K90 = [3,11,37,41,47,53,61,71,79,83,89]; inv = lambda x: pow(x,-1,140)
coll = {}
for k,l in itertools.permutations(range(11),2):
    coll.setdefault((K90[k]*inv(K90[l]))%140, []).append((k,l))
f = lambda a: [sum(x*x for x in a)-1] + [sum(a[k]*a[l] for k,l in pr) for pr in coll.values()]
rng = np.random.default_rng(1)
sols = []
for _ in range(400):
    s = least_squares(f, rng.normal(size=11), xtol=1e-15, ftol=1e-15, gtol=1e-15)
    if np.linalg.norm(s.fun) < 1e-10: sols.append(s.x)
def exact_check(alpha_dict):
    prod = {}
    for p,a in alpha_dict.items():
        for q,b in alpha_dict.items():
            g = (p*inv(q))%140; prod[g] = sp.nsimplify(prod.get(g,0) + a*b)
    return {g:v for g,v in prod.items() if v != 0} == {1:1}
shown = 0; exact_found = []
for x in sols:
    nzi = [i for i in range(11) if abs(x[i]) > 1e-6]
    if len(nzi) == 1: continue
    vals = {K90[i]: x[i] for i in nzi}
    rec = {p: sp.nsimplify(v, [sp.sqrt(2), sp.sqrt(3), sp.sqrt(5), sp.sqrt(6)], tolerance=1e-9) for p,v in vals.items()}
    ok = exact_check(rec)
    if shown < 8:
        print("support", len(nzi), {p: round(v,10) for p,v in vals.items()}, " recognised:", rec, " exact tt*=1:", ok); shown += 1
    if ok: exact_found.append(rec)
print("numerical non-monomial solutions:", sum(1 for x in sols if np.sum(np.abs(x)>1e-6)>1), " exact-recognised:", len(exact_found))
if exact_found: print("first exact non-monomial solution:", exact_found[0])
