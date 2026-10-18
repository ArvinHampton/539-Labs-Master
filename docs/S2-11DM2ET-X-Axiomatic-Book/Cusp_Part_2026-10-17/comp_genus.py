# Genus (Eisenstein) test for EVERY one of the 140 components u_{al,be}:
# coefficient at frequency Q (both signs) is c(Q)=sum of phases; N:=19600|Q| is the integer norm N(beta).
# For a pure Eisenstein (genus-character) form, c at N=g*p (p prime, g the content) is a function of p mod M.
# A dihedral CUSP form contributes chi(P)+chi(P') which is NOT periodic in p.  We test with M=3360.
import numpy as np, sys, math, json
from collections import defaultdict
import uvec
from uvec import vectors
from family import LABELS
from sympy import isprime
QMAX=float(sys.argv[1]) if len(sys.argv)>1 else 300
BX=int(sys.argv[2]) if len(sys.argv)>2 else 330
_orig=uvec.cone_pts
uvec.cone_pts=lambda a,b,r1,r2,s,Q,Bx=40:_orig(a,b,r1,r2,s,Q,Bx=BX)
M=3360
res=[]; summary=defaultdict(int)
for idx,(al,be) in enumerate(LABELS):
    q,ph,c=vectors(al,be,Qmax=QMAX)
    for sgn in (1,-1):
        sel=(np.sign(q)==sgn)
        N=np.rint(19600*np.abs(q[sel])).astype(np.int64); P=ph[sel]
        coef=defaultdict(complex)
        for n,v in zip(N,P): coef[int(n)]+=v
        coef={n:v for n,v in coef.items() if abs(v)>1e-9}
        if not coef: res.append((idx,sgn,0,"empty")); summary["empty"]+=1; continue
        g=0
        for n in coef: g=math.gcd(g,n)
        # restrict to N=g*p with p prime, p>7, and with N comfortably inside the (cone-complete) range
        Nlim=int(19600*QMAX*0.98)
        tab=defaultdict(set); cnt2=defaultdict(int)
        for p_ in range(11, Nlim//g+1):
            if not isprime(p_): continue
            v=coef.get(g*p_,0)
            tab[p_%M].add((round(v.real,6),round(v.imag,6))); cnt2[p_%M]+=1
        nonper=[r for r,s in tab.items() if len(s)>1]
        verdict="periodic" if not nonper else "NON-PERIODIC"
        summary[verdict]+=1
        res.append((idx,sgn,g,verdict,len(nonper),sum(1 for r in cnt2 if cnt2[r]>1),len(tab)))
    if idx%10==0: print(idx,res[-2:],flush=True)
open("comp_genus.txt","w").write(f"QMAX={QMAX} BX={BX} M={M}\nsummary {dict(summary)}\n"+"\n".join(map(str,res))+"\n")
print(dict(summary))
