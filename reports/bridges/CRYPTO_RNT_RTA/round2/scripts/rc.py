import json
from fractions import Fraction as F
bd=[(1,0),(4,2),(2,-1)]
MIX={4:[0],8:[1],12:[0,4]}
def law(k,j):
    v=[0]*k; v[0]=1; p=1
    for i in range(j):
        w=[0]*k
        for c,x in enumerate(v):
            if x:
                for b,d in bd: w[(b*c+d*p)%k]+=x
        v=w; p=p*3%k
    return v
def lawB(k,j):
    v=[0]*k; v[1%k]=1
    for i in range(j):
        w=[0]*k
        for c,x in enumerate(v):
            for b,d in bd: w[b*c%k]+=x
        v=w
    return v
# self-check of R0 identity on integers
def T3(n):
    q,r=divmod(n,3); return (q,4*q+2,2*q+1)[r]
for n in range(0,3**7):
    B,C,u=1,0,n
    for i in range(7):
        r=u%3; b,d=bd[r]; C=b*C+d*3**i; B*=b; u=T3(u)
    assert 3**7*u==B*n+C
out={}
for j in (60,120):
    for k in (4,5,7,8,11,12,13):
        v=law(k,j); T=3**j; sq={x*x%k for x in range(k)}
        mass=[F(x,T) for x in v]
        e=float(sum(mass[c] for c in sq))-len(sq)/k
        lam=float(sum(mass[c] for c in range(k) if c not in sq))
        vb=lawB(k,j)
        out[f"{k}_{j}"]=dict(dist=[float(m) for m in mass],excess=e,leak=lam,weak=e>=0.02,strong=lam<=1e-6,
          mix={c:float(mass[c]) for c in MIX.get(k,[])},B_dist=[x/T for x in vb])
r={k:out[f"{k}_120"] for k in (4,5,7,8,11,12,13)}
nw=sum(v['weak'] for v in r.values()); ns=sum(v['strong'] for v in r.values())
out['verdict']=dict(weak_count=nw,strong_count=ns,confirmed=nw>=5 and ns>=1)
print(json.dumps(out,indent=1))
