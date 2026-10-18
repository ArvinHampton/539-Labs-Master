# Eisenstein vs cusp content of the ray-class theta (Cat B test).
# r(N) = #ideals of norm N in the ray class K  (= #nu in F cap (a+Z^2) with 20 Q2(nu) = N).
# If the class indicator of K were a combination of characters factoring through the norm (genus/Eisenstein type),
# r(p) for primes p would be a function of p mod (conductor). We test p mod 280, 560, 840, 1120, 1680.
import numpy as np, sympy as sp
from collections import defaultdict
from uvec import cone_pts
from family import G
Nmax=400000
q,ph=cone_pts(np.array([49,-14]),np.array([0,0]),(1,0),tuple(G@np.array([1,0])),1,Nmax/20,Bx=340)
Nn=np.rint(20*q).astype(np.int64)
r=np.bincount(Nn,minlength=Nmax+1)
out=[f"ideals of norm <= {Nmax} in K: {r.sum()}  (first norms: {np.nonzero(r)[0][:12].tolist()})"]
primes=[p for p in sp.primerange(2,Nmax) if r[p]>0 or p%20==13]
for mod in (280,560,840,1120,1680,3360):
    vals=defaultdict(set)
    for p in primes:
        if p%20==13: vals[p%mod].add(int(r[p]))
    amb=sum(1 for v in vals.values() if len(v)>1)
    out.append(f"mod {mod}: {len(vals)} residue classes of primes p=13 mod 20; classes where r(p) is NOT constant: {amb}")
cnt=defaultdict(int)
for p in primes:
    if p%20==13: cnt[int(r[p])]+=1
out.append(f"distribution of r(p) over primes p=13 mod 20: {dict(cnt)}")
print("\n".join(out)); open("split_test.txt","w").write("\n".join(out)+"\n")
# full test (composite norms too): pure genus <=> r(n) = h(n mod M) * R_O(n), R_O(n) = sum_{d|n} (35/d)  (gcd(n,70)=1)
from sympy import jacobi_symbol, divisors
out2=[]
for M in (280,560):
    h=defaultdict(set)
    for n in range(13,60000,20):
        if np.gcd(n,70)!=1: continue
        RO=sum(jacobi_symbol(35,d) for d in divisors(n))
        if RO==0:
            if r[n]!=0: h['RO=0 but r>0'].add(n)
            continue
        h[n%M].add(sp.Rational(int(r[n]),RO))
    bad=[k for k,v in h.items() if len(v)>1]
    out2.append(f"composite test n<60000, M={M}: residue classes with non-constant r(n)/R_O(n): {len(bad)}  (values per class e.g. {sorted(list(h[list(h)[0]]))})")
print("\n".join(out2)); open("split_test.txt","a").write("\n".join(out2)+"\n")
