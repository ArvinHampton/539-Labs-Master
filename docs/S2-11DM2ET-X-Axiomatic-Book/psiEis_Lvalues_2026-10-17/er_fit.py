# Fit the positive and negative Fourier coefficients of u_R (frequency n/70) as combinations of divisor sums (psi1*psi2)(n/d)
import numpy as np, math, uvec, itertools, pickle
from collections import defaultdict
from uvec import vectors
from family import LABELS
import cypari2; pari=cypari2.Pari()
_o=uvec.cone_pts; uvec.cone_pts=lambda a,b,r1,r2,s,Q,Bx=40:_o(a,b,r1,r2,s,Q,Bx=300)
QM=60; NM=int(QM*70*0.97)
idx=[i for i,(al,be) in enumerate(LABELS) if tuple(int(t)%70 for t in be)==(21,14) and i<70]
coef=defaultdict(complex); const=0
for i in idx:
    q,ph,c=vectors(*LABELS[i],Qmax=QM); const+=c
    for n,v in zip(np.rint(70*q).astype(np.int64),ph): coef[int(n)]+=v
print("constant term of u_R:",const)
kr={d:np.array([0]+[int(pari(f'kronecker({d},{n})')) for n in range(1,NM+1)]) for d in (-4,-7,8)}
def chi5(e):
    lg={1:0,2:1,4:2,3:3}; return np.array([0]+[ (1j**(e*lg[n%5]) if n%5 else 0) for n in range(1,NM+1)])
def psi(e5,s4,s7): 
    v=chi5(e5).astype(complex)
    if s4: v=v*kr[-4]
    if s7: v=v*kr[-7]
    return v
GEN={(0,0):(0,0,0),(0,1):(0,1,0),(2,0):(3,1,0),(2,1):(3,0,0),(4,0):(2,0,0),(4,1):(2,1,0),(6,0):(1,1,0),(6,1):(1,0,0)}
chi140=psi(2,1,1)
def conv(a,b):
    out=np.zeros(NM+1,complex)
    for d in range(1,NM+1):
        if a[d]!=0: out[d::d]+=a[d]*b[1:NM//d+1]
    return out
basis=[];names=[]
divs=[d for d in range(1,281) if 280%d==0]
for k,(e5,s4,s7) in GEN.items():
    p=psi(e5,s4,s7); pp=p*chi140
    for (A,B,nm) in ((p.conj(),pp.conj(),"conj(psi),conj(psi')"),(pp.conj(),p.conj(),"conj(psi'),conj(psi)"),(p,pp,"psi,psi'"),(pp,p,"psi',psi")):
        cv=conv(A,B)
        for d in divs:
            f=np.zeros(NM+1,complex); f[d::d]=cv[1:NM//d+1]
            if np.abs(f).max()>0: basis.append(f[1:]); names.append((k,nm,d))
Bm=np.array(basis).T
res={}
for sgn in (1,-1):
    y=np.array([coef.get(sgn*n,0) for n in range(1,NM+1)])
    x,*_=np.linalg.lstsq(Bm,y,rcond=None)
    r=np.abs(Bm@x-y).max()
    print("sign",sgn,"basis",Bm.shape,"max residual",r, "rank",np.linalg.matrix_rank(Bm,1e-8))
    res[sgn]=(x,r)
pickle.dump(dict(names=names,res=res,const=const),open("er_fit.pkl","wb"))
