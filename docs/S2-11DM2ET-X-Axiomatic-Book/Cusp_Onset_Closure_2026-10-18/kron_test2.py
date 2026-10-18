# A(2): CRT split with odd coordinate xo = (n+1)*(al + lam*be) (mod Z^2), 2-coordinate (n*al, be). Test Kronecker factorization of S,T.
import numpy as np, sys
from family_s import Family
def test(s, lam):
    F=Family(s); S=F.Smatrix(); T=F.Tmatrix(); n=s*(s-2); D=F.D
    keys=[((tuple((n*np.array(al))%D),be), tuple(((n+1)*(np.array(al)+lam*np.array(be)))%D)) for (al,be) in F.LABELS]
    t2=sorted({k[0] for k in keys}); to=sorted({k[1] for k in keys})
    if len(t2)*len(to)!=F.N or len(set(keys))!=F.N: return None
    i2={k:i for i,k in enumerate(t2)}; io={k:i for i,k in enumerate(to)}
    perm=np.array([i2[k[0]]*len(to)+io[k[1]] for k in keys]); P=np.zeros((F.N,F.N)); P[perm,np.arange(F.N)]=1
    out={}
    for name,Mx in (('S',S),('T',T)):
        Mp=P@Mx@P.T; a,b=len(t2),len(to)
        R=Mp.reshape(a,b,a,b).transpose(0,2,1,3).reshape(a*a,b*b)
        sv=np.linalg.svd(R,compute_uv=False); out[name]=round(sv[1]/sv[0],12)
    return out
s=int(sys.argv[1]); n=s*(s-2)
for lam in [0,1,-1,(n+1)//2,-(n+1)//2,2,-2]:
    print(lam,test(s,lam))
