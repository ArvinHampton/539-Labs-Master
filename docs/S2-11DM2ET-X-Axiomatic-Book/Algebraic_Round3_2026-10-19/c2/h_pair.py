# exact q-series check (through q^N): H^{(a)} == H^{(s-a)} for admissible c=(-a,1), several s; and first degree of difference to a=4.
import json
from fractions import Fraction as F
sgn=lambda x:(x>0)-(x<0)
def H(s,a,N):
    B=lambda c,v: 2*c[0]*v[0]+s*(c[0]*v[1]+c[1]*v[0])+s*c[1]*v[1]
    h=[F(0)]*(N+1)
    for n in range(-60*s,60*s+1):
        for k in range(-80,81):
            q=n*n+s*n*k+(s*k*(k+1))//2
            if 0<=q<=N:
                w=F(sgn(B((-1,1),(n,k)))-sgn(B((-a,1),(n,k))),2)
                if w: h[q]+=w
    return h
out={}
for s,N in ((7,800),(8,800),(9,800),(11,600),(13,600)):
    adm=[a for a in range(2,s) if 2*a*a-2*s*a+s<0]
    Hs={a:H(s,a,N) for a in adm}
    pairs={a:all(Hs[a][q]==Hs[s-a][q] for q in range(N+1)) for a in adm if (s-a) in Hs}
    diff4={a:next((q for q in range(N+1) if Hs[a][q]!=Hs[4][q]),None) for a in adm} if 4 in Hs else {}
    out[s]=dict(N=N,admissible=adm,H_a_eq_H_s_minus_a=pairs,first_diff_vs_a4=diff4)
    print(s,out[s],flush=True)
json.dump(out,open('h_pair.json','w'),indent=1)
