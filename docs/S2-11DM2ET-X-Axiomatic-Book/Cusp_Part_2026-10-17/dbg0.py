import numpy as np, uvec, math
from collections import defaultdict
from uvec import vectors
from family import LABELS
_o=uvec.cone_pts; uvec.cone_pts=lambda a,b,r1,r2,s,Q,Bx=40:_o(a,b,r1,r2,s,Q,Bx=420)
for idx in (0,20,70):
    al,be=LABELS[idx]; q,ph,c=vectors(al,be,Qmax=60)
    sel=q>0; N=np.rint(19600*q[sel]).astype(np.int64)
    coef=defaultdict(complex)
    for n,v in zip(N,ph[sel]): coef[int(n)]+=v
    g=0
    for n in coef: g=math.gcd(g,n)
    print(idx,LABELS[idx],g,[(n//g,np.round(coef[n],3)) for n in sorted(coef)[:14]])
