# Test: Psi(z) := E_{a,0}(-1/z) - K z sum_p E_{p,-a}(z) on the upper half-plane
# (holomorphic there) extends analytically to the real axis and its boundary values are the
# exact rational-point psi(x) of fastkappa.py (Lewis-Zagier mechanism).
import numpy as np, math, cmath
from fractions import Fraction as Fr
from fastkappa import REPS, a, ma, zero, psi
def points(al, Qmax):
    """nu in F cap (al+Z^2) with Q2(nu)<=Qmax, F = C0 u rho2 C0."""
    out=[]
    for which in (0,1):
        if which==0:
            u0=float(Fr(al[0])%1) or 1.0; w0=float(Fr(al[1])%1)
        else:
            u0=float((Fr(al[1])+2*Fr(al[0]))%1) or 1.0; w0=float((-Fr(al[0]))%1)
        U=u0+np.arange(0,int(math.sqrt(Qmax))+3); 
        for u in U:
            if (u*u if which==0 else 3.5*u*u) > Qmax: break
            W=w0+np.arange(0,int(math.sqrt(Qmax/1.0))+3)
            if which==0: q=u*u+7*u*W+3.5*W*W; n1=u+0*W; n2=W
            else: q=3.5*u*u+7*u*W+W*W; n1=-W; n2=u+2*W
            k=q<=Qmax
            out.append(np.stack([n1[k],n2[k],q[k]],1))
    return np.concatenate(out)
CACHE={}
def Efun(al,be,tau,Qmax):
    key=(al,be,Qmax)
    if key not in CACHE:
        P=points(al,Qmax); b=np.array([2*float(be[0])+7*float(be[1]),7*float(be[0])+7*float(be[1])])
        CACHE[key]=(P[:,2], np.exp(2j*np.pi*(P[:,0]*b[0]+P[:,1]*b[1])))
    q,ph=CACHE[key]
    return np.sum(ph*np.exp(2j*np.pi*tau*q))
def Psi(z,K):
    y1=(-1/z).imag; y2=z.imag
    Q1=40/(2*math.pi*y1); Q2=40/(2*math.pi*y2)
    Q1=math.ceil(Q1/50)*50; Q2=math.ceil(Q2/50)*50
    return Efun(a,zero,-1/z,Q1) - K*z*sum(Efun(p,ma,z,Q2) for p in REPS)
if __name__=="__main__":
    out=[]
    for K,name in [(1/math.sqrt(35),"1/sqrt35"),(1j/math.sqrt(35),"i/sqrt35"),(-1j/math.sqrt(35),"-i/sqrt35")]:
        v=[Psi(complex(1,y),K) for y in (0.08,0.04,0.02)]
        out.append(f"K={name}: Psi(1+iy) for y=.08,.04,.02: "+"  ".join(f"{w:.5f}" for w in v))
    print("\n".join(out))
    open("lz_K.txt","w").write("\n".join(out)+"\n")
