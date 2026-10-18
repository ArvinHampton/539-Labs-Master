# Exact lower bound rank(C) >= 42: reduce the exact Fourier coefficient matrix (sums of 4900th roots of unity / K) modulo a prime l = 1 mod 4900.
import sys; sys.path.insert(0,'.'); sys.path.insert(1,'../2026-10-17-cusp-part')
import numpy as np
from collections import defaultdict
from family import LABELS, D, G, GI
import uvec
def cone_exp(al70,be70,r1,r2,sgn,Qmax,Bx=40):
    m=np.arange(-Bx,Bx+1); M1,M2=np.meshgrid(m,m,indexing='ij')
    N1=(sgn*al70[0])%D+D*M1.ravel(); N2=(sgn*al70[1])%D+D*M2.ravel()
    det=r1[0]*r2[1]-r1[1]*r2[0]; s=(N1*r2[1]-N2*r2[0])*np.sign(det); t=(r1[0]*N2-r1[1]*N1)*np.sign(det)
    ok=(s>0)&(t>=0); N1=N1[ok];N2=N2[ok]; q2=(2*N1*N1+14*N1*N2+7*N2*N2)   # = 2*D*D*q
    k=(np.abs(q2)<=Qmax*2*D*D)&(q2!=0); N1=N1[k];N2=N2[k];q2=q2[k]
    bb=N1*(2*be70[0]+7*be70[1])+N2*(7*be70[0]+7*be70[1]); return q2,(sgn*bb)%(D*D)
def vec_exp(al70,be70,Qmax):
    al70=np.array(al70); be70=np.array(be70); Q=[];E=[]; a_,b_=al70.copy(),be70.copy()
    for i in range(uvec.K):
        for r1,r2 in ((uvec.e1,uvec.ge1),(uvec.f,uvec.gf)):
            for sgn in (1,-1):
                q,e=cone_exp(a_,b_,r1,r2,sgn,Qmax); Q.append(q); E.append(e)
        a_=GI@a_; b_=GI@b_
    return np.concatenate(Q),np.concatenate(E)
# float cross-check against uvec
q,e=vec_exp(*LABELS[5],Qmax=10); qf,phf,_=uvec.vectors(*LABELS[5],Qmax=10)
assert np.allclose(np.sort(q/(2*D*D)),np.sort(qf))
l=None
for k in range(1,10**6):
    c=4900*k+1
    if all(c%p for p in range(2,int(c**.5)+1)): l=c; break
# primitive 4900th root mod l
def prim(l):
    fac=[2,5,7]; n=l-1
    pf=[]; m=n; p=2
    while p*p<=m:
        if m%p==0: pf.append(p); 
        while m%p==0: m//=p
        p+=1
    if m>1: pf.append(m)
    for gg in range(2,l):
        if all(pow(gg,n//p,l)!=1 for p in pf): return pow(gg,n//4900,l)
z=prim(l); zp=[pow(z,k,l) for k in range(4900)]; inv2=pow(2,-1,l)
cols=defaultdict(lambda: [0]*140)
for i,(al,be) in enumerate(LABELS):
    q,e=vec_exp(al,be,Qmax=25)
    for qq,ee in zip(q,e): cols[int(qq)][i]=(cols[int(qq)][i]+zp[int(ee)]*inv2)%l
M=np.array([cols[k] for k in cols],dtype=object).T
def rank_mod(M,l):
    M=[list(map(int,r)) for r in M]; r=0; nr=len(M); nc=len(M[0])
    for c in range(nc):
        piv=next((i for i in range(r,nr) if M[i][c]%l),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]; iv=pow(M[r][c],-1,l)
        M[r]=[(x*iv)%l for x in M[r]]
        for i in range(nr):
            if i!=r and M[i][c]%l:
                f=M[i][c]; M[i]=[(a-f*b)%l for a,b in zip(M[i],M[r])]
        r+=1
        if r==nr: break
    return r
rk=rank_mod(M,l)
s=f"prime l = {l} (= 1 mod 4900); exact Fourier matrix (|Q|<=25, {M.shape[1]} frequencies, constant term excluded) has rank {rk} over F_l  =>  rank over Q(zeta_4900) >= {rk}"
print(s); open("rank_modp.txt","w").write(s+"\n")
