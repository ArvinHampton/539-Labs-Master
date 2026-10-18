# Fourier data of the Maass components u_{al,be} (weight 0, lambda=1/4), any label, via gamma^k-orbit reps:
#   u = sqrt(y)[ log(eps)*[al in Z^2] + (1/k) sum_{i<k} sum_{cones C in {F,-F,T,-T}} sum_{nu in C cap (g^-i al + Z^2)} e(B(nu,g^-i be)) K0(2pi|Q|y)e(Qx) ]
import numpy as np, math
from family import A, D, G, GI, LABELS
LOGEPS=math.log(6+math.sqrt(35)); K=2
def cone_pts(al70, be70, r1, r2, sgn, Qmax, Bx=40):
    # nu = sgn*mu, mu in cone[r1,r2) (r1 incl., r2 excl.), nu in al+Z^2
    m=np.arange(-Bx,Bx+1)
    M1,M2=np.meshgrid(m,m,indexing='ij')
    N1=(sgn*al70[0])%D + D*M1.ravel(); N2=(sgn*al70[1])%D + D*M2.ravel()   # mu*70, mu in sgn*al + Z^2
    det=r1[0]*r2[1]-r1[1]*r2[0]
    s=(N1*r2[1]-N2*r2[0])*np.sign(det); t=(r1[0]*N2-r1[1]*N1)*np.sign(det)
    ok=(s>0)&(t>=0)
    N1=N1[ok];N2=N2[ok]
    q=(2*N1*N1+14*N1*N2+7*N2*N2)/(2*D*D)
    k=(np.abs(q)<=Qmax)&(q!=0)
    N1=N1[k];N2=N2[k];q=q[k]
    # nu=sgn*mu ; phase e(B(nu,be)) = e(sgn*B(mu,be))
    bb=N1*(2*be70[0]+7*be70[1])+N2*(7*be70[0]+7*be70[1])
    ph=np.exp(2j*np.pi*((sgn*bb)%(D*D))/(D*D))
    return q,ph
e1=(1,0); ge1=tuple(G@np.array(e1)); f=(1,-1); gf=tuple(G@np.array(f))
def vectors(al70,be70,Qmax=11):
    al70=np.array(al70); be70=np.array(be70)
    Q=[];P=[]
    a_,b_=al70.copy(),be70.copy()
    for i in range(K):
        for r1,r2 in ((e1,ge1),(f,gf)):
            for sgn in (1,-1):
                q,ph=cone_pts(a_,b_,r1,r2,sgn,Qmax)
                Q.append(q);P.append(ph/K)
        a_=GI@a_; b_=GI@b_
    const=LOGEPS if np.all(al70%D==0) else 0.0
    return np.concatenate(Q),np.concatenate(P),const
def ueval(V,w):
    from scipy.special import k0
    q,ph,c=V; x,y=w.real,w.imag
    return math.sqrt(y)*(c+np.sum(ph*k0(2*np.pi*np.abs(q)*y)*np.exp(2j*np.pi*q*x)))
