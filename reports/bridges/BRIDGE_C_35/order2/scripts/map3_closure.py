# Map 3 (Category B): order-2 vector-valued closure test for the 105 companions, with the leading-order control.
from lib2 import *
import json
I=math.log(6+math.sqrt(35))/(2*math.sqrt(35))
P=[x for x in XS if x.denominator<=12]
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
A0=np.zeros((len(P),105),complex); A1=np.zeros_like(A0); B0=np.zeros_like(A0); B1m=np.zeros_like(A0)
for ix,x in enumerate(P):
    for j,(al,be) in enumerate(pairs):
        A0[ix,j],A1[ix,j]=A01_float(al,be,x); B0[ix,j],B1m[ix,j]=A01_float(al,be,-1/x)
    print(ix,x,flush=True)
np.savez('../data/map3_profiles.npz',A0=A0,A1=A1,B0=B0,B1=B1m,xs=np.array([float(x) for x in P]))
def nrank(M):
    s=np.linalg.svd(M,compute_uv=False); s=s/s[0]; r=int((s>1e-9).sum())
    gap=(s[r-1]/s[r]) if r<len(s) else float('inf')
    return r,float(gap)
xs=np.array([abs(float(x)) for x in P])
out={}
for name,(Aa,Bb) in {'leading':(A0,B0),'order2':(A1,B1m)}.items():
    rA=nrank(Aa); out[name]={'rank_A':rA}
    for w in (0.5,1.0):
        for conv,e in (('prereg_|x|^-w',-w),('corrected_|x|^+w',w)):
            r=nrank(np.hstack([Aa,(xs**e)[:,None]*Bb])); out[name][f'{conv}_w{w}']=r
    print(name,out[name],flush=True)
json.dump(out,open('../data/map3_closure.json','w'),indent=1)
