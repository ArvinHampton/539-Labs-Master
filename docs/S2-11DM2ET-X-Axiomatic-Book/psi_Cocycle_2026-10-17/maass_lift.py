# The weight-0, lambda=1/4 Maass forms attached to the E-vector (Siegel theta lift over the gamma-circle)
#   u_L(w) = sqrt(y) * sum_{nu in (a+Z^2)/<gamma>}            K0(2pi|Q2(nu)|y) e(Q2(nu) x)
#   u_R(w) = sqrt(y) * [ log(eps) + sum_{0!=nu in A^{-1}Z^2/<gamma>} e(B(nu,-a)) K0(2pi|Q2|y) e(Q2 x) ]
# and the closed form of psi as a period integral (Lewis-Zagier mechanism):
#   psi(x) = -(1/pi) * [ (x/sqrt35)(log(eps)/2 - J_R(x)) + J_L(-1/x) ],
#   J_R(x) = int_{i}^{i inf} [u_R, R_x^{1/2}],  J_L(z') = int_i^{i inf} [u_L, R_{z'}^{1/2}].
import mpmath as mp, math
from fractions import Fraction as Fr
mp.mp.dps=20
eps=6+mp.sqrt(35); LOGEPS=mp.log(eps)
Ainv=[[Fr(-1,5),Fr(1,5)],[Fr(1,5),Fr(-2,35)]]
g=[[-1,-7],[2,13]]
def Q2(v): return v[0]**2+7*v[0]*v[1]+Fr(7,2)*v[1]**2
def gv(v): return (g[0][0]*v[0]+g[0][1]*v[1], g[1][0]*v[0]+g[1][1]*v[1])
def in_cone(v,r1,r2):
    det=r1[0]*r2[1]-r1[1]*r2[0]
    s=(v[0]*r2[1]-v[1]*r2[0])/det; t=(r1[0]*v[1]-r1[1]*v[0])/det
    return s>0 and t>=0
e1=(1,0); f=(1,-1)
CONES=[(e1,gv(e1),1),(f,gv(f),1),(e1,gv(e1),-1),(f,gv(f),-1)]
def fd(v):
    for r1,r2,sg in CONES:
        if in_cone((sg*v[0],sg*v[1]),r1,r2): return True
    return False
def vectors(kind,Qmax,B=60):
    out=[]
    for m1 in range(-B,B+1):
        for m2 in range(-B,B+1):
            if kind=='L':
                v=(Fr(7,10)+m1, Fr(-1,5)+m2); ph=Fr(0)
            else:
                if m1==0 and m2==0: continue
                v=(Ainv[0][0]*m1+Ainv[0][1]*m2, Ainv[1][0]*m1+Ainv[1][1]*m2)
                ph=-(Fr(7,10)*m1+Fr(-1,5)*m2)
            q=Q2(v)
            if q!=0 and abs(q)<=Qmax and fd(v): out.append((float(q), float(ph%1)))
    return out
def ufun(vecs,const,w,deriv=False):
    x,y=w.real,w.imag
    u=const*mp.sqrt(y); ux=0; uy=const/(2*mp.sqrt(y))
    for q,ph in vecs:
        a=2*mp.pi*abs(q); e=mp.expjpi(2*(ph+q*x))
        k0=mp.besselk(0,a*y)
        T=mp.sqrt(y)*k0*e; u+=T
        if deriv:
            ux+=2j*mp.pi*q*T; uy+=e*(k0/(2*mp.sqrt(y))-mp.sqrt(y)*a*mp.besselk(1,a*y))
    return (u,ux,uy) if deriv else u
def J(vecs,const,z):
    def f(t):
        w=mp.mpc(0,t); u,ux,uy=ufun(vecs,const,w,True)
        uw=0.5*(ux-1j*uy)
        R=t/((w-z)*(mp.conj(w)-z)); v=mp.sqrt(R)
        vwb=0.5/v*1j/(2*(mp.conj(w)-z)**2)
        return 1j*(uw*v-u*vwb)
    return mp.quad(f,[1,2,4,mp.inf])
if __name__=="__main__":
    import pickle
    VL=vectors('L',9,40); VR=vectors('R',9,60)
    pickle.dump((VL,VR),open("maass_vectors.pkl","wb"))
    out=[f"#vectors |Q2|<=9 mod gamma: u_L {len(VL)}, u_R {len(VR)}"]
    out.append("positive-norm reps (u_L): "+str(sorted(q for q,_ in VL if q>0)[:8]))
    out.append("negative-norm reps (u_L): "+str(sorted((q for q,_ in VL if q<0),reverse=True)[:8]))
    for w in [mp.mpc(0.2,0.9),mp.mpc(-0.35,0.95),mp.mpc(0.05,1.0)]:
        lhs=ufun(VL,0,-1/w); rhs=ufun(VR,LOGEPS,w)/mp.sqrt(35)
        out.append(f"S-law test w={complex(w)}: u_L(-1/w)={mp.nstr(lhs,14)}  u_R(w)/sqrt35={mp.nstr(rhs,14)}  diff={mp.nstr(abs(lhs-rhs),3)}")
    w=mp.mpc(0.3,1.2)
    out.append(f"T-law test: u_L(w+1)/u_L(w)={mp.nstr(ufun(VL,0,w+1)/ufun(VL,0,w),14)}  e(13/20)={mp.nstr(mp.expjpi(2*0.65),14)}")
    print("\n".join(out)); open("maass_lift.txt","w").write("\n".join(out)+"\n")
