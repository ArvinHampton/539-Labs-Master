# Exact: with c2 = primitive(-s,2) (wall k=0), Cmixed := P - H - Caxis - Cthird == 0 (through q^N, s=5..13; proof in report §6).
# Also: frozen Cmixed (c2=(-4,1)) == H^{axes} - H^{(-4,1)}, first term at Q+(3s/g... ) wall point.
import json, math
from fractions import Fraction as F
sgn=lambda x:(x>0)-(x<0)
out={}
for s in range(5,14):
    N=600
    B=lambda c,v: 2*c[0]*v[0]+s*(c[0]*v[1]+c[1]*v[0])+s*c[1]*v[1]
    Q=lambda n,k: n*n+s*n*k+(s*k*(k+1))//2
    Qm=lambda n,k: n*n+s*n*k+(s*k*(k-1))//2
    g=math.gcd(s,2); cax=(-s//g,2//g)
    base=[F(0)]*(N+1)
    for n in range(60):
        for k in range(60):
            if Q(n,k)<=N: base[Q(n,k)]+=1
            if n>=1 and k>=1 and Qm(n,k)<=N: base[Qm(n,k)]-=1
    base[0]-=F(3,2)
    for n in range(1,60):
        if n*n<=N: base[n*n]-=1
        if s*n*(n+1)//2<=N: base[s*n*(n+1)//2]-=1
    def cm(c2):
        c=base[:]
        for n in range(-60*s,60*s+1):
            for k in range(-90,91):
                q=Q(n,k)
                if 0<=q<=N:
                    w=F(sgn(B((-1,1),(n,k)))-sgn(B(c2,(n,k))),2)
                    if w: c[q]-=w
        return c
    ca=cm(cax); cf=cm((-4,1))
    out[s]=dict(c_axes=cax,Cmixed_axes_zero=all(x==0 for x in ca),frozen_first_nonzero=next((q for q in range(N+1) if cf[q]),None))
    print(s,out[s],flush=True)
json.dump(out,open('axes_cmixed.json','w'),indent=1)
