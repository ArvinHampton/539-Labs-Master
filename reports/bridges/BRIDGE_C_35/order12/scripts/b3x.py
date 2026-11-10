# B3 preregistered high-precision leg: exact integer phase reduction + longdouble trig, x in {1/2, 1/3} (and negatives)
import sys; sys.dont_write_bytecode=True
from common import pairs, S_rows, LL, Fr
import numpy as np, json, math
ld=np.longdouble; tp=2*ld(np.pi) if False else ld('6.283185307179586476925286766559')
M=np.zeros((105,105),dtype=np.clongdouble)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for e in es: a=tp*ld(e)/ld(LL); M[j,kk]+=np.cos(a)+1j*np.sin(a)
def g(x):
    x=Fr(x); N=2*70*x.denominator; n,k=np.meshgrid(np.arange(N,dtype=np.int64),np.arange(N,dtype=np.int64),indexing='ij'); out=[]
    for al,be in pairs:
        D=math.lcm(2*al[0].denominator**2*al[1].denominator**2*x.denominator, 2*al[0].denominator*be[0].denominator*be[1].denominator*al[1].denominator)
        D=math.lcm(D,x.denominator*2*al[0].denominator*al[1].denominator*70)
        # nu_i = (p_i + d_i n)/d_i
        d1,d2=al[0].denominator,al[1].denominator; p1=al[0].numerator+d1*n; p2=al[1].numerator+d2*k
        # Q*x = (p1^2/d1^2 + 7 p1 p2/(d1 d2) + 7/2 p2^2/d2^2) * x
        xq=Fr(x); terms=[(Fr(1,d1*d1)*xq,p1*p1),(Fr(7,d1*d2)*xq,p1*p2),(Fr(7,2*d2*d2)*xq,p2*p2),
              (Fr(2*be[0]+7*be[1],d1),p1),(Fr(7*be[0]+7*be[1],d2),p2)]
        Dd=math.lcm(*[c.denominator for c,_ in terms]); acc=np.zeros_like(n)
        for c,arr in terms: acc=(acc+ (c.numerator*(Dd//c.denominator))%Dd * (arr%Dd))%Dd
        cnt=np.bincount(acc.ravel(),minlength=0); r=np.nonzero(cnt)[0]
        a=tp*r.astype(ld)/ld(Dd); out.append(((np.cos(a)+1j*np.sin(a))*cnt[r].astype(ld)).sum()/ld(N*N))
    return np.array(out,dtype=np.clongdouble)
res={}
for xs in ('1/2','1/3','-1/2','-1/3'):
    x=Fr(xs); gx=g(x); gs=g(-1/x); s35=np.sqrt(ld(35))
    ra=float(np.abs(gs-ld(abs(1/x).numerator)/ld(abs(1/x).denominator)/s35*(M@gx)).max()/np.abs(gs).max())
    rs=float(np.abs(gs-ld((1/x).numerator)/ld((1/x).denominator)/s35*(M@gx)).max()/np.abs(gs).max())
    res[xs]=dict(abs_law=ra,signed_law=rs); print(xs,res[xs],flush=True)
json.dump(res,open('../data/b3x.json','w'),indent=1)
