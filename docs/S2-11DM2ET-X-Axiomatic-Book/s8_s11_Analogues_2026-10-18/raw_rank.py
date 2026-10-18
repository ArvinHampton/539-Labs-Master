# Ground-truth dimension of the family: complex rank of the raw Fourier-coefficient matrix [component x (sign, frequency Q)],
# complete for |Q| <= Qmax (all lattice points of the gamma-fundamental domains are enumerated, as in content_s.py).
import numpy as np, math, sys, json
from collections import defaultdict
from family_s import Family
s=int(sys.argv[1]); Qmax=float(sys.argv[2]); F=Family(s); D=F.D; A=F.A; G1=F.G
def cone_mask(X,r1,r2):
    det=r1[0]*r2[1]-r1[1]*r2[0]
    sv=(X[:,0]*r2[1]-X[:,1]*r2[0])*np.sign(det); tv=(r1[0]*X[:,1]-r1[1]*X[:,0])*np.sign(det)
    return (sv>0)&(tv>=0)
e1=np.array([1,0]); f=np.array([1,-1]); M=Qmax*D*D; alset=set(map(tuple,np.array(F.ALS)))
def rows(r1,r2,sgn):
    th=np.linspace(0,1,2001); V=np.outer(1-th,r1)+np.outer(th,r2); V=V/np.linalg.norm(V,axis=1)[:,None]
    lam=np.min(np.abs(V[:,0]**2+s*V[:,0]*V[:,1]+(s/2)*V[:,1]**2)); R=int(math.sqrt(M/lam))+2; out=[]
    for x2 in range(-R,R+1):
        dis1=(s*s-2*s)*x2*x2+4*M
        lo=math.floor((-s*x2-math.sqrt(dis1))/2)-1; hi=math.ceil((-s*x2+math.sqrt(dis1))/2)+1
        dis2=(s*s-2*s)*x2*x2-4*M
        if dis2>0:
            a1=math.ceil((-s*x2-math.sqrt(dis2))/2)+1; b1=math.floor((-s*x2+math.sqrt(dis2))/2)-1
            segs=[(lo,a1),(b1,hi)] if a1<b1 else [(lo,hi)]
        else: segs=[(lo,hi)]
        for p,q in segs:
            x1=np.arange(p,q+1); out.append(np.stack([x1,np.full_like(x1,x2)],1))
    X=np.concatenate(out); X=X[cone_mask(sgn*X,r1,r2)]
    Q=(X[:,0]**2+s*X[:,0]*X[:,1]+(s/2)*X[:,1]**2)/(D*D); X=X[(np.abs(Q)<=Qmax)&(Q!=0)]
    assert np.max(np.abs(X))<R-1; return X
Xs=[]
for r1,sgn in ((e1,1),(e1,-1),(f,1),(f,-1)):
    Xr=rows(r1,G1@r1,sgn); GX=Xr@G1.T
    ok=np.array([((x%D,y%D) in alset) or ((u%D,v%D) in alset) for (x,y),(u,v) in zip(Xr,GX)]); Xs.append(Xr[ok])
X=np.concatenate(Xs); GX=X@G1.T
Qn=(2*X[:,0]**2+2*s*X[:,0]*X[:,1]+s*X[:,1]**2)   # = 2 D^2 Q, integer
freqs=sorted(set(Qn.tolist())); fi={q:i for i,q in enumerate(freqs)}; col=np.array([fi[q] for q in Qn])
Mx=np.zeros((F.N,len(freqs)),complex)
for li,(al,be) in enumerate(F.LABELS):
    al=np.array(al); be=np.array(be)
    m1=np.all((X%D)==al,axis=1); m2=np.all((GX%D)==al,axis=1)
    wt=0.5*(m1*np.exp(2j*np.pi*((X@A@be)%(D*D))/(D*D))+m2*np.exp(2j*np.pi*((GX@A@be)%(D*D))/(D*D)))
    np.add.at(Mx[li],col,wt)
# constant term log eps for al in Z^2
const=np.array([1.0 if np.all(np.array(al)%D==0) else 0.0 for al,be in F.LABELS])
Mfull=np.hstack([Mx,const[:,None]])
x=np.linalg.svd(Mfull,compute_uv=False); r=int(np.sum(x>1e-8*x[0]))
print(f"s={s}: Qmax={Qmax}, points {len(X)}, frequencies {len(freqs)}; complex rank of the family = {r}; sv[r-1]={x[r-1]:.2e}, sv[r]={x[r] if r<len(x) else 0:.2e}")
np.save(f"raw_{s}.npy",Mfull)
if len(sys.argv)>3:
    idx=json.load(open(sys.argv[3]))
    for name,ii in idx.items():
        y=np.linalg.svd(Mfull[ii],compute_uv=False); print(f"   rank of {name} components ({len(ii)}): {int(np.sum(y>1e-8*y[0]))}")
