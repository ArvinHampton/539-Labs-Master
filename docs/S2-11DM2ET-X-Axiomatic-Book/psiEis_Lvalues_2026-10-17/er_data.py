import numpy as np, math, uvec
from collections import defaultdict
from uvec import vectors
from family import LABELS
_o=uvec.cone_pts; uvec.cone_pts=lambda a,b,r1,r2,s,Q,Bx=40:_o(a,b,r1,r2,s,Q,Bx=200)
# u_R = sum_p u_{p,-a}: labels with alpha in L'/Z^2 (alpha70 = 0 mod 2? i.e. not in a+L') and beta=-a
idx=[i for i,(al,be) in enumerate(LABELS) if tuple(int(t)%70 for t in be)==(21,14) and i<70]
print(len(idx),[LABELS[i] for i in idx[:3]])
coef=defaultdict(complex)
for i in idx:
    q,ph,c=vectors(*LABELS[i],Qmax=30)
    for n,v in zip(np.rint(19600*q).astype(np.int64),ph): coef[int(n)]+=v
pos={n:v for n,v in coef.items() if n>0 and abs(v)>1e-9}; neg={-n:v for n,v in coef.items() if n<0 and abs(v)>1e-9}
g=0
for n in list(pos)+list(neg): g=math.gcd(g,n)
print("g",g)
print("pos",[(n//g,np.round(pos[n],4)) for n in sorted(pos)[:25]])
print("neg",[(n//g,np.round(neg[n],4)) for n in sorted(neg)[:25]])
