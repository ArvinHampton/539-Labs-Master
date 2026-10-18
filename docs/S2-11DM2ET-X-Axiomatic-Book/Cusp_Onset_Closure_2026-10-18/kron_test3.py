# A(2): search a diagonal phase gauge g(al,be) and CRT split making S and T exact Kronecker products rho_2 (x) rho_odd.
import numpy as np, sys, itertools, math
from fractions import Fraction as Fr
from family_s import Family
def make(F, lam):
    n=F.s*(F.s-2); D=F.D
    keys=[((tuple((n*np.array(al))%D),be), tuple(((n+1)*(np.array(al)+lam*np.array(be)))%D)) for (al,be) in F.LABELS]
    t2=sorted({k[0] for k in keys}); to=sorted({k[1] for k in keys})
    if len(t2)*len(to)!=F.N or len(set(keys))!=F.N: return None
    i2={k:i for i,k in enumerate(t2)}; io={k:i for i,k in enumerate(to)}
    perm=np.array([i2[k[0]]*len(to)+io[k[1]] for k in keys]); P=np.zeros((F.N,F.N)); P[perm,np.arange(F.N)]=1
    return P,len(t2),len(to)
def r1(Mp,a,b):
    R=Mp.reshape(a,b,a,b).transpose(0,2,1,3).reshape(a*a,b*b); sv=np.linalg.svd(R,compute_uv=False); return sv[1]/sv[0]
s=int(sys.argv[1]); F=Family(s); S=F.Smatrix(); T=F.Tmatrix(); n=s*(s-2)
terms={'Bab':lambda al,be:F.B(np.array(al),np.array(be)),'Qb':lambda al,be:F.Q(np.array(be)),'Bbw':lambda al,be:F.B(np.array(be),F.WC),'Baw':lambda al,be:F.B(np.array(al),F.WC)}
coefs=[Fr(0),Fr(1),Fr(-1),Fr(1,2),Fr(-1,2)]
best=[]
for lam in [0,1,-1]:
    mk=make(F,lam)
    if mk is None: continue
    P,a,b=mk
    for cs in itertools.product(coefs,repeat=len(terms)):
        g=np.array([np.exp(2j*np.pi*float(sum(c*f(al,be) for c,f in zip(cs,terms.values()))%1)) for (al,be) in F.LABELS])
        G=np.diag(g); Gi=np.diag(1/g)
        rs=r1(P@G@S@Gi@P.T,a,b); rt=r1(P@G@T@Gi@P.T,a,b)
        best.append((rs+rt,lam,cs,rs,rt))
best.sort(key=lambda x:x[0])
for x in best[:6]: print(x)
