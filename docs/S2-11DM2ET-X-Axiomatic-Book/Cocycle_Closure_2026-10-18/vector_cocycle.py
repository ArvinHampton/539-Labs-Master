# Numerical test of the vector boundary cocycle
#   kh(g x) = |cx+d| M [kh(x) + (2/pi) P(x)] - (1/pi)(|cx+d| M b - b),
#   u o g = M u,  P(x) = int_r^{i oo} [u, R_x^{1/2}],  r = g^{-1} oo,  kh = radial const of f_u (all 140 rows).
# g = S T^k S = [[-1,0],[k,-1]], M = S_lab T_lab^k S_lab.
import sys, json, math, numpy as np
from fractions import Fraction as Fr
import uvec
sys.path.insert(0,'../2026-10-17-psi-cocycle'); import fastkappa as fk
F=uvec.F; S=F.Smatrix(); T=F.Tmatrix(); Ti=np.conj(T.T); N=F.N
assert np.max(np.abs(T@Ti-np.eye(N)))<1e-13
U=uvec.U(16.0); b=U.b
GI=uvec.GI
kcache={}
def kF(al,be,x):
    key=(al,be,x)
    if key not in kcache: kcache[key]=complex(fk.cone_terms(al,be,x)[1])
    return kcache[key]
def fr(v): return (Fr(int(v[0]),70),Fr(int(v[1]),70))
def khat(x):
    out=np.zeros(N,complex)
    for i,(al,be) in enumerate(F.LABELS):
        al=np.array(al); be=np.array(be); s=0
        for sg in (1,-1):
            s+=kF(fr(sg*al),fr(sg*be),x)+kF(fr(sg*(GI@al)),fr(sg*(GI@be)),x)
        out[i]=0.5*s
    return out
def gl(a,c,n):
    t,w=np.polynomial.legendre.leggauss(n); return 0.5*(c-a)*t+0.5*(c+a),0.5*(c-a)*w
def nodes(n):
    br=[0,0.02,0.08,0.2,0.4,0.7,1.0]; T_=[];W_=[]
    for a,c in zip(br[:-1],br[1:]):
        t,w=gl(a,c,n); T_.append(t);W_.append(w)
    return np.concatenate(T_),np.concatenate(W_)
def period(k,x,n=60):
    r=1.0/k; c=k; d=-1; s0=1.0/k
    Ninv=S@np.linalg.matrix_power(Ti,k)@S
    x=float(x); tot=np.zeros(N,complex)
    tau,wt=nodes(n)
    for t,wq in zip(tau,wt):
        if t==0: continue
        for part in (0,1):
            if part==0: s=s0/t; ds=s0/t**2      # upper, direct
            else:       s=s0*t; ds=s0           # lower, transported
            w=r+1j*s
            if part==0: u,uw=U.ev(w)
            else:
                wpp=(-w)/(c*w+d); u2,uw2=U.ev(wpp)
                u=Ninv@u2; uw=Ninv@uw2/(c*w+d)**2
            R=s/abs(w-x)**2; v=math.sqrt(R); vwb=(1j/(2*(w.conjugate()-x)**2))/(2*v)
            tot+=wq*ds*(1j*uw*v-1j*u*vwb)
    return tot
def run(k,xs,n=60):
    M=S@np.linalg.matrix_power(T,k)@S; res=[]
    for x in xs:
        x=Fr(x); gx=(-x)/(k*x-1); cxd=abs(float(k*x-1))
        P=period(k,x,n); kx=khat(x); kg=khat(gx)
        rhs=cxd*M@(kx+(2/math.pi)*P)-(1/math.pi)*(cxd*M@b-b)
        err=np.max(np.abs(kg-rhs)); scale=np.max(np.abs(kg))
        # also the L-row and R-row (u_L = u_{a,0}, u_R = sum_p u_{p,-a})
        iL=F.IDX[(tuple(F.a70%70),(0,0))]
        res.append(dict(k=k,x=str(x),gx=str(gx),sign_cx_d=int(np.sign(k*x-1)),maxerr_140=float(err),
                        max_abs_kappa=float(scale),L_err=float(abs(kg[iL]-rhs[iL]))))
        print(res[-1],flush=True)
        with open('vector_cocycle.jsonl','a') as fh: fh.write(json.dumps(res[-1])+'\n')
    return res
if __name__=='__main__':
    k=int(sys.argv[1]); n=int(sys.argv[2]); xs=sys.argv[3:]
    run(k,xs,n)
