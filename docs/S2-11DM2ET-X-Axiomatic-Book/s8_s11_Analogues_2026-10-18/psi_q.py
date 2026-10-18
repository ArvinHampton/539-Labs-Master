# Psi(z) = E_L(-1/z) - (z/sqrt|det|) E_R(z), with the s=7 conventions (psiEis report, complex_check.py):
#   E_L(tau) = sum_{nu in [e1, gamma e1) cap (a+Z^2)} e(Q2(nu) tau),  E_R(tau) = sum_{p in L'/Z^2} sum_{nu in [e1,gamma e1) cap (p+Z^2)} e(B(nu,-a)) e(Q2(nu) tau).
import numpy as np, math, sys
from family_s import Family
def cone_coeffs(F,al,be,Qmax):
    s=F.s; D=F.D; A=F.A; g=F.G
    r1=np.array([1,0]); r2=g@r1
    B=int(math.sqrt(Qmax)*12)+4
    n=np.arange(-B*4,B*4+1)
    N1,N2=np.meshgrid(n,n,indexing='ij'); X=np.stack([al[0]+D*N1.ravel(),al[1]+D*N2.ravel()],1)
    det=r1[0]*r2[1]-r1[1]*r2[0]
    sv=(X[:,0]*r2[1]-X[:,1]*r2[0])*np.sign(det); tv=(r1[0]*X[:,1]-r1[1]*X[:,0])*np.sign(det)
    X=X[(sv>0)&(tv>=0)]
    Q=(X[:,0]**2+s*X[:,0]*X[:,1]+(s/2)*X[:,1]**2)/(D*D)
    k=(Q<=Qmax)&(Q>0); X=X[k]; Q=Q[k]
    assert np.max(np.abs(X))<D*(B*4-2)
    ph=np.exp(2j*np.pi*((X@A@np.array(be))%(D*D))/(D*D))
    return Q,ph
def make(s,Qmax=70):
    F=Family(s); a=F.a%F.D
    QL,PL=cone_coeffs(F,a,(0,0),Qmax)
    QR=[];PR=[]
    for p in F.LP:
        q,ph=cone_coeffs(F,p,(-F.a)%F.D,Qmax); QR.append(q); PR.append(ph)
    QR=np.concatenate(QR); PR=np.concatenate(PR); sq=math.sqrt(abs(F.det))
    E=lambda Q,P,tau: np.sum(P*np.exp(2j*np.pi*Q*tau))
    Psi=lambda z: E(QL,PL,-1/z)-z/sq*E(QR,PR,z)
    return Psi,(QL,PL),(QR,PR)
if __name__=="__main__":
    s=int(sys.argv[1]); Psi,L,R=make(s)
    for z in (1+0.6j,2+1j): print(z, Psi(z))
