# Light read-only check (REVIEW_PARALLEL). Reuses recorded arrays; no new series evaluation.
import numpy as np, json
from fractions import Fraction as Fr
from math import gcd
XS=sorted({Fr(h,m) for m in range(1,16) for h in range(1,3*m+1) if gcd(h,m)==1}); xs=np.array([float(x) for x in XS])
p=np.load('../../order3/data/parts.npz'); q=np.load('../../order4b/data/A2.npz')
def nr(M):
    s=np.linalg.svd(M,compute_uv=False); s=s/s[0]; return int((s>1e-9).sum())
def resid(T,B):
    Qm,_=np.linalg.qr(B); 
    U,s,Vh=np.linalg.svd(B,full_matrices=False); r=(s/s[0]>1e-9).sum(); U=U[:,:r]
    R=T-U@(U.conj().T@T); return float(max(np.linalg.norm(R[:,j])/max(np.linalg.norm(T[:,j]),1e-300) for j in range(T.shape[1]) if np.linalg.norm(T[:,j])>1e-12))
out={}
assert np.allclose(p['A1'],q['A1'])
for k in ['A0','A1','D','R']:
    out[k]={str(w):[nr(p[k]),nr(np.hstack([p[k],(xs**w)[:,None]*p['S_'+k]]))] for w in (-1,-0.5,0,0.5,1,1.5)}
out['A2']={str(w):[nr(q['A2']),nr(np.hstack([q['A2'],(xs**w)[:,None]*q['S_A2']]))] for w in (-1,-0.5,0,0.5,1)}
# weight-1 holomorphic radial ansatz: A2(-1/x) in span[|x| A2, A0, |x|^{1/2}A1, |x|^0 A1]
A0,A1,A2=q['A0'],q['A1'],q['A2']
X=lambda w:(xs**w)[:,None]
for name,B in {'[|x|A2,A0]':np.hstack([X(1)*A2,A0]),'[|x|A2,A0,A1]':np.hstack([X(1)*A2,A0,A1]),'[A2,|x|^.5A1,|x|A0] (order4b T1 rows216)':np.hstack([A2,X(.5)*A1,X(1)*A0])}.items():
    out['mixed '+name]={'rankB':nr(B),'eps':resid(q['S_A2'],B)}
out['A1(-1/x) in span[A1,|x|^-.5... ] w0+w.5']={'rankB':nr(np.hstack([A1,X(-.5)*A1])),'eps':resid(p['S_A1'],np.hstack([A1,X(-0.5)*A1]))}
json.dump(out,open('../data/weight_scan.json','w'),indent=1); print(json.dumps(out,indent=0))
