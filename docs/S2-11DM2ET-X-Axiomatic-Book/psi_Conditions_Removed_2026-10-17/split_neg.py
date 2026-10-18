# Negative-frequency coefficients of u_L (vectors in the T-cone [f, gamma f), f=(1,-1)):  r''(n) = #{nu : 20|Q2(nu)| = n}
# genus (Eisenstein-only) test as for the positive part:  r''(n) = h''(n mod M) * R_O(n) ?
import numpy as np, sympy as sp
from collections import defaultdict
from sympy import jacobi_symbol, divisors
from uvec import cone_pts
from family import G
Nmax=120000
q,ph=cone_pts(np.array([49,-14]),np.array([0,0]),(1,-1),tuple(G@np.array([1,-1])),1,Nmax/20,Bx=300)
Nn=np.rint(-20*q).astype(np.int64); Nn=Nn[Nn>0]
r=np.bincount(Nn,minlength=Nmax+1)
out=[f"negative-norm vectors with 20|Q|<= {Nmax}: {r.sum()}; first norms {np.nonzero(r)[0][:12].tolist()}"]
for M in (280,560):
    h=defaultdict(set); amb=[]
    for n in range(1,40000):
        if r[n]==0 and n%20 not in (7,): continue
        if np.gcd(n,70)!=1: continue
        RO=sum(jacobi_symbol(35,d) for d in divisors(n))
        if RO==0:
            if r[n]: amb.append(n)
            continue
        h[n%M].add(sp.Rational(int(r[n]),RO))
    bad=[(k,sorted(v)) for k,v in h.items() if len(v)>1]
    out.append(f"M={M}: residue classes with non-constant r''(n)/R_O(n): {len(bad)} of {len(h)}; examples {bad[:3]}; r''>0 with R_O=0: {amb[:5]}")
# examples of split primes
ex=[(p,int(r[p])) for p in sp.primerange(2,3000) if p%20==7]
out.append("r''(p) for primes p=7 mod 20 (<3000): "+str(ex[:25]))
print("\n".join(out)); open("split_neg.txt","w").write("\n".join(out)+"\n")
