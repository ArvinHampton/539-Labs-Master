"""All integer pairs (alpha, beta), 1<=|alpha|<=1000, 1<=|beta|<=5000, beta>0 (x->-x symmetry removes beta<0 duplicates:
f(alpha,beta) <-> f(alpha,-beta)), with disc = 256 alpha^5 + 3125 beta^4 a nonzero perfect square; then irreducibility + Galois group
(Frobenius cycle types p<=4000, cross-checked with PARI polgalois).  Group by k = beta/alpha."""
import os
os.environ["OMP_NUM_THREADS"] = "1"
from math import isqrt, gcd
from fractions import Fraction as Fr
from collections import defaultdict
from galois_tools import *
os.nice(10)
hits = []
for al in range(-1000, 1001):
    if al == 0: continue
    a5 = 256*al**5
    for be in range(1, 5001):
        d = a5 + 3125*be**4
        if d > 0:
            r = isqrt(d)
            if r*r == d: hits.append((al, be))
print("pairs with nonzero square discriminant (beta>0):", len(hits))
rows = []
for al, be in hits:
    irr = is_irreducible(al, be)
    if not irr: rows.append((al, be, "reducible", None)); continue
    ty, u = cycle_types(al, be)
    fr = classify_frobenius(al, be, True, ty)
    rows.append((al, be, fr, pari_group(al, be)))
from collections import Counter
print("classification (Frobenius):", Counter(r[2] for r in rows))
print("Frobenius vs PARI mismatches:", sum(1 for r in rows if r[2] not in ("reducible",) and r[2] != r[3]))
byk = defaultdict(list)
for al, be, fr, pg in rows:
    if fr == "A5": byk[Fr(be, al)].append((al, be))
multi = {k: v for k, v in byk.items() if len(v) >= 2}
print("A5 seeds:", sum(len(v) for v in byk.values()), " distinct ratios k:", len(byk), " ratios with >=2 seeds:", len(multi))
for k in sorted(multi): print("  k=%s: %s" % (k, multi[k]))
print("A5 seeds listing (alpha,beta):"); print(sorted((al, be) for v in byk.values() for al, be in v))
print("non-A5 rows:", [r for r in rows if r[2] != "A5"])
