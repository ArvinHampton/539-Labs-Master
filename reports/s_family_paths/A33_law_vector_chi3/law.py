# A33: build candidate 35-component law vectors (leading radial profiles) and test Weil law vs A32 rho35.
import json, numpy as np, math
from fractions import Fraction as Fr
from math import gcd
A=np.array([[2,7],[7,7]]); A32='/workspace/quantum-comp/reports/s_family_paths/A32_35_to_rho7/'
ev=json.load(open(A32+'exact_verify.json')); R=[tuple(r) for r in ev['reps_mu_times_minus35']]; n=35
MU=[(Fr(-r[0],35)%1,Fr(-r[1],35)%1) for r in R]          # mu = r/(-35)
b=lambda r1,r2: Fr(int(np.array(r1)@A@np.array(r2)),35*35)%1
qv=[Fr((18*int(b(r,r)*35))%35,35) for r in R]
def rho(k,dual=False):
    S=np.array([[1j*np.exp(-2j*np.pi*float(b(R[i],R[j]))) for j in range(n)] for i in range(n)])/math.sqrt(35)
    T=np.diag([np.exp(2j*np.pi*float(qq)) for qq in qv])
    S=S*(-1j)**k; T=T*np.exp(2j*np.pi*k/12)
    return (S.conj(),T.conj()) if dual else (S,T)
a=(Fr(7,10),Fr(-1,5)); Z=(Fr(0),Fr(0))
def G(al,be,x):
    x=Fr(x); m=x.denominator; L=4*m
    nu0=np.array([int(al[0]*70),int(al[1]*70)]); assert all(Fr(int(al[i]*70),70)==al[i] for i in range(2))
    be70=np.array([int(be[0]*70),int(be[1]*70)])
    i,j=np.meshgrid(np.arange(L),np.arange(L),indexing='ij')
    v0=nu0[0]+70*i; v1=nu0[1]+70*j                      # 70*nu
    Q2=(2*v0*v0+14*v0*v1+7*v1*v1)                       # = 2*Q(70nu)= 4900*2Q(nu)
    Bn=(v0*(2*be70[0]+7*be70[1])+v1*(7*be70[0]+7*be70[1]))   # 4900*B(nu,be)
    N=9800*m
    ph=(x.numerator*Q2 + 2*m*Bn) % N                    # (xQ + B)*N
    return np.exp(2j*np.pi*ph/N).mean()
def add(u,v): return ((u[0]+v[0]),(u[1]+v[1]))
CANDS={'K1':lambda mu:(add(a,mu),a),'K2':lambda mu:(add(a,mu),Z),'K3':lambda mu:(mu,a),'K4':lambda mu:(mu,Z)}
xs=sorted({Fr(h,m) for m in range(1,13) for h in range(1,3*m+1) if gcd(h,m)==1})
def vec(c,x): return np.array([G(*CANDS[c](mu),x) for mu in MU])
if __name__=='__main__':
    out={}
    for c in CANDS:
        g={x:vec(c,x) for x in xs}; gS={x:vec(c,-1/x) for x in xs}; gT={x:vec(c,x+1) for x in xs}
        np.save(f'g_{c}.npy',np.array([g[x] for x in xs]))
        best=None
        for dual in (False,True):
            for k in range(12):
                S,T=rho(k,dual)
                for w in (-1,1):
                    eS=max(np.abs(gS[x]-float(x)**w*S@g[x]).max() for x in xs)
                    eT=max(np.abs(gT[x]-T@g[x]).max() for x in xs)
                    r=(eS+eT,dual,k,w,eS,eT)
                    if best is None or r<best: best=r
        tot,dual,k,w,eS,eT=best
        P=np.array([np.abs(g[x]).max() for x in xs])
        out[c]=dict(best_dual=dual,best_k=k,best_w=w,errS=eS,errT=eT,max_abs=float(P.max()))
        print(c,out[c],flush=True)
    json.dump(out,open('weil_fit.json','w'),indent=1)
