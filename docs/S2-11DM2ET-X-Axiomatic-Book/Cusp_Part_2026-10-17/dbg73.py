import numpy as np, math, uvec
from collections import defaultdict
from uvec import vectors
from family import LABELS
from sympy import isprime
_o=uvec.cone_pts; uvec.cone_pts=lambda a,b,r1,r2,s,Q,Bx=40:_o(a,b,r1,r2,s,Q,Bx=420)
al,be=LABELS[73]; q,ph,c=vectors(al,be,Qmax=400)
sel=q>0; N=np.rint(19600*q[sel]).astype(np.int64); P=ph[sel]
coef=defaultdict(complex)
for n,v in zip(N,P): coef[int(n)]+=v
tab=defaultdict(list)
for p in range(11,int(19600*400*.98)//140):
    if isprime(p): v=coef.get(140*p,0); tab[p%3360].append((p,round(v.real,4),round(v.imag,4)))
for r,l in tab.items():
    if len(set(x[1:] for x in l))>1: print(r, l[:8])
