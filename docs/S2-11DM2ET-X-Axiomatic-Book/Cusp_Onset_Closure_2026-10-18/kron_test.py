# A(2): test whether the family rep (S,T) factors as rho_2 (x) rho_odd under the CRT label split (odd s).
import numpy as np, sys
from family_s import Family
def split(F):
    s=F.s; n=s*(s-2); D=F.D
    two=[]; odd=[]
    keys=[]
    for (al,be) in F.LABELS:
        al=np.array(al)
        a2=tuple((n*al)%D); ao=tuple(((n+1)*al)%D)
        keys.append(((a2,be),ao))
    t2=sorted({k[0] for k in keys}); to=sorted({k[1] for k in keys})
    return keys,t2,to
def test(s):
    F=Family(s); S=F.Smatrix(); T=F.Tmatrix()
    keys,t2,to=split(F); i2={k:i for i,k in enumerate(t2)}; io={k:i for i,k in enumerate(to)}
    assert len(t2)*len(to)==F.N, (len(t2),len(to),F.N)
    perm=np.array([i2[k[0]]*len(to)+io[k[1]] for k in keys]); P=np.zeros((F.N,F.N)); P[perm,np.arange(F.N)]=1
    out={}
    for name,Mx in (('S',S),('T',T)):
        Mp=P@Mx@P.T; a,b=len(t2),len(to)
        R=Mp.reshape(a,b,a,b).transpose(0,2,1,3).reshape(a*a,b*b)
        sv=np.linalg.svd(R,compute_uv=False); out[name]=(sv[0], sv[1]/sv[0])
    return len(t2),len(to),out
for s in [int(z) for z in sys.argv[1].split(',')]:
    print(s,test(s),flush=True)
