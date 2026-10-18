# Period-integral closed form of psi, verified against the exact Bernoulli-sum values.
#   psi(x) = -(1/pi) [ (x/sqrt35)(log(eps)/2 - J_R(x)) + J_L(-1/x) ],
#   J(z) = int_i^{i inf} [u, R_z^{1/2}],  [u,v] = u_w v dw + u v_wbar dwbar,  R_z(w) = Im w/((w-z)(wbar-z)).
# u on the path w=it does not depend on x, so it is tabulated once on Gauss-Legendre nodes.
import numpy as np, math, cmath, pickle
from fractions import Fraction as Fr
from collections import defaultdict
from scipy.special import k0, k1
import maass_lift as M
from fastkappa import psi as psi_exact
out=[]
# (1) S+ and S- give the same positive Fourier coefficients (=> f_u = 2E for u_L and u_R)
def regions(kind,Qmax,B):
    Sp=defaultdict(complex); Sm=defaultdict(complex)
    for m1 in range(-B,B+1):
        for m2 in range(-B,B+1):
            if kind=='L': v=(Fr(7,10)+m1,Fr(-1,5)+m2); ph=Fr(0)
            else:
                if m1==0 and m2==0: continue
                v=(M.Ainv[0][0]*m1+M.Ainv[0][1]*m2, M.Ainv[1][0]*m1+M.Ainv[1][1]*m2); ph=-(Fr(7,10)*m1+Fr(-1,5)*m2)
            q=M.Q2(v)
            if 0<q<=Qmax:
                if M.in_cone(v,M.e1,M.gv(M.e1)): Sp[q]+=cmath.exp(2j*math.pi*float(ph))
                if M.in_cone((-v[0],-v[1]),M.e1,M.gv(M.e1)): Sm[q]+=cmath.exp(2j*math.pi*float(ph))
    return max(abs(Sp[q]-Sm[q]) for q in set(Sp)|set(Sm)), len(Sp)
for kind,B in (('L',50),('R',70)):
    d,n=regions(kind,25,B)
    out.append(f"u_{kind}: max over {n} positive norms <= 25 of |coef(S+) - coef(S-)| = {d:.2e}")
VL,VR=M.vectors('L',11,45),M.vectors('R',11,66)
LOGEPS=math.log(6+math.sqrt(35))
def nodes(n):
    xs,ws=np.polynomial.legendre.leggauss(n); T=[];W=[]
    for a,b in [(0,0.1),(0.1,0.3),(0.3,1.0)]:
        T.append((b-a)/2*xs+(a+b)/2); W.append((b-a)/2*ws)
    tau=np.concatenate(T); w=np.concatenate(W)
    return 1/tau, w/tau**2
def tab(vecs,const,t):
    q=np.array([v[0] for v in vecs]); ph=np.exp(2j*np.pi*np.array([v[1] for v in vecs]))
    a=2*np.pi*np.abs(q)[None,:]; T=t[:,None]
    K0=k0(a*T); K1=k1(a*T)
    u=np.sqrt(t)*(const+ (ph*K0).sum(1))
    ux=np.sqrt(t)*((2j*np.pi*q*ph*K0).sum(1))
    uy=const/(2*np.sqrt(t)) + (ph*(K0/(2*np.sqrt(T))-np.sqrt(T)*a*K1)).sum(1)
    return u,0.5*(ux-1j*uy)
def J(tabd,t,wts,z):
    u,uw=tabd; w=1j*t; wb=-1j*t
    R=t/((w-z)*(wb-z)); v=np.sqrt(R+0j); vwb=0.5/v*1j/(2*(wb-z)**2)
    return np.sum(wts*1j*(uw*v-u*vwb))
def make(n):
    t,wts=nodes(n); return t,wts,tab(VL,0.0,t),tab(VR,LOGEPS,t)
def psi_period(x,data):
    t,wts,TL,TR=data
    return -(1/math.pi)*((x/math.sqrt(35))*(LOGEPS/2-J(TR,t,wts,x))+J(TL,t,wts,-1/x))
D1,D2=make(80),make(160)
if __name__=="__main__":
    xs=[Fr(1),Fr(1,3),Fr(2),Fr(3,7),Fr(5,8),Fr(13,17),Fr(55,89),Fr(7,3),Fr(1,9),Fr(-1),Fr(-2,5),Fr(-13,4)]
    worst=0
    for x in xs:
        pe=psi_exact(x); p1=psi_period(float(x),D1); p2=psi_period(float(x),D2)
        worst=max(worst,abs(pe-p2))
        out.append(f"x={str(x):6}: exact Bernoulli-sum psi={pe:.13f}   period integral={p2:.13f}   |diff|={abs(pe-p2):.1e}  (quadrature change {abs(p1-p2):.0e})")
    out.append(f"max |diff| over {len(xs)} rationals = {worst:.2e}")
    for x in [math.sqrt(2),math.pi/3,0.01,0.05,10.0,100.0]:
        out.append(f"x={x:.6f}: period-integral psi = {psi_period(x,D2):.13f}")
    print("\n".join(out)); open("psi_period.txt","w").write("\n".join(out)+"\n")
    pickle.dump(None,open("/dev/null","wb"))
