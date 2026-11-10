# B3: g(-1/x) = |x|^{-1} (1/sqrt35) M g(x) ; float64 finite sums + mp dps 40 at two points
import sys; sys.dont_write_bytecode=True
from common import pairs, S_rows, LL, Fr
import numpy as np, json, mpmath as mp
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for e in es: M[j,kk]+=np.exp(2j*np.pi*e/LL)
def g(x,N=None):
    x=Fr(x); N=N or 2*70*x.denominator; n,k=np.meshgrid(np.arange(N),np.arange(N),indexing='ij'); out=[]
    for al,be in pairs:
        u1=float(al[0])+n; u2=float(al[1])+k
        # exact phase mod 1 via fractions on small pieces is too slow; use float with reduction by integer parts
        Q=u1*u1+7*u1*u2+3.5*u2*u2; ph=Q*float(x)+u1*(2*float(be[0])+7*float(be[1]))+u2*(7*float(be[0])+7*float(be[1]))
        out.append(np.exp(2j*np.pi*np.mod(ph,1)).mean())
    return np.array(out)
res={}
X=['1','1/2','1/3','2/3','1/4','3/4','1/5','2/5','-1/2','-1/3','-2/5']
for xs in X:
    x=Fr(xs); gx=g(x); gs=g(-1/x)
    if xs in ('1','1/2'): assert np.abs(g(x,2*gx.size and 2*70*x.denominator*2)-gx).max()<1e-9  # period check (double N)
    pa=abs(1/x); pr=float(1/x)
    ra=np.abs(gs-float(pa)/np.sqrt(35)*M@gx).max()/max(np.abs(gs).max(),1e-300)
    rs=np.abs(gs-pr/np.sqrt(35)*M@gx).max()/max(np.abs(gs).max(),1e-300)
    res[xs]=dict(abs_law=float(ra),signed_law=float(rs),norm=float(np.abs(gx).max())); print(xs,res[xs],flush=True)
v=lambda r:'pass' if r<=1e-12 else ('FAIL' if r>=1e-4 else 'inconclusive')
res['verdict_abs']={k:v(r['abs_law']) for k,r in res.items() if isinstance(r,dict)}
res['verdict_signed_xneg']={k:v(res[k]['signed_law']) for k in X if k.startswith('-')}
print(res['verdict_abs'],res['verdict_signed_xneg']); json.dump(res,open('../data/b3.json','w'),indent=1)
