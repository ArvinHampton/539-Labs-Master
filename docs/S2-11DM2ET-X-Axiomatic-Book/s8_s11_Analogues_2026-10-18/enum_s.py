# Fourier coefficients of family components (same conventions as content_s.py / raw_rank.py / s=7 uvec.py):
# u_{al,be} = sqrt(y)[log eps*[al in Z^2] + sum over gamma^2-fundamental domains of S+,S-,T+,T- (weight 1/2) e(B(nu,be)) K0(2pi|Q|y)e(Qx)]
import numpy as np, math
from collections import defaultdict
from family_s import Family
def coeffs(s,Qmax,combo,F=None):
    """combo: list of (label_index, complex weight). Returns dict {Fraction-like key 2D^2Q (int): coefficient} (signed frequencies)."""
    F=F or Family(s); D=F.D; A=F.A; G1=F.G
    def cone_mask(X,r1,r2):
        det=r1[0]*r2[1]-r1[1]*r2[0]
        sv=(X[:,0]*r2[1]-X[:,1]*r2[0])*np.sign(det); tv=(r1[0]*X[:,1]-r1[1]*X[:,0])*np.sign(det)
        return (sv>0)&(tv>=0)
    e1=np.array([1,0]); f=np.array([1,-1]); M=Qmax*D*D
    alset={tuple(int(z) for z in F.LABELS[i][0]) for i,_ in combo}
    resid=alset|{tuple(int(z)%D for z in F.GI@np.array(a_)) for a_ in alset}
    by2=defaultdict(list)
    for r1_,r2_ in resid: by2[r2_].append(r1_)
    def rows(r1,r2,sgn):
        th=np.linspace(0,1,2001); V=np.outer(1-th,r1)+np.outer(th,r2); V=V/np.linalg.norm(V,axis=1)[:,None]
        lam=np.min(np.abs(V[:,0]**2+s*V[:,0]*V[:,1]+(s/2)*V[:,1]**2)); R=int(math.sqrt(M/lam))+2; out=[]
        for x2 in range(-R,R+1):
            if (sgn*x2)%D not in by2: continue
            res1=np.array(sorted(by2[(sgn*x2)%D]))
            dis1=(s*s-2*s)*x2*x2+4*M
            lo=math.floor((-s*x2-math.sqrt(dis1))/2)-1; hi=math.ceil((-s*x2+math.sqrt(dis1))/2)+1
            dis2=(s*s-2*s)*x2*x2-4*M
            if dis2>0:
                a1=math.ceil((-s*x2-math.sqrt(dis2))/2)+1; b1=math.floor((-s*x2+math.sqrt(dis2))/2)-1
                segs=[(lo,a1),(b1,hi)] if a1<b1 else [(lo,hi)]
            else: segs=[(lo,hi)]
            for p,q in segs:
                base=np.arange(p//D-1,q//D+2)*D
                cand=(base[:,None]+((sgn*res1)%D)[None,:]).ravel(); x1=cand[(cand>=p)&(cand<=q)]
                if len(x1): out.append(np.stack([x1,np.full_like(x1,x2)],1))
        X=np.concatenate(out); X=X[cone_mask(sgn*X,r1,r2)]
        Q=(X[:,0]**2+s*X[:,0]*X[:,1]+(s/2)*X[:,1]**2)/(D*D); X=X[(np.abs(Q)<=Qmax)&(Q!=0)]
        assert np.max(np.abs(X))<R-1; return X
    X=np.concatenate([rows(r1,G1@r1,sg) for r1,sg in ((e1,1),(e1,-1),(f,1),(f,-1))]); GX=X@G1.T
    Qn=(2*X[:,0]**2+2*s*X[:,0]*X[:,1]+s*X[:,1]**2)
    out=defaultdict(complex)
    for li,wt in combo:
        al,be=F.LABELS[li]; al=np.array(al); be=np.array(be)
        m1=np.all((X%D)==al,axis=1); m2=np.all((GX%D)==al,axis=1)
        v=0.5*(m1*np.exp(2j*np.pi*((X@A@be)%(D*D))/(D*D))+m2*np.exp(2j*np.pi*((GX@A@be)%(D*D))/(D*D)))*wt
        for q,val in zip(Qn[m1|m2],v[m1|m2]): out[int(q)]+=val
    return dict(out), 2*D*D
def LR(s,F=None):
    F=F or Family(s); iL=F.IDX[(tuple(int(z) for z in F.a%F.D),(0,0))]
    combR=[]
    for p in F.LP:
        j,ph=F.reduce(p,(-F.a)%F.D); combR.append((j,ph))
    return F,[(iL,1.0)],combR
