# Which c=(-a,1) (negative norm, Zwegers-admissible with c1=(-1,1)) give C=P_s-H_s with coefficients in {0,1,1.5}? exact (Fractions)
import json, math, sys
from fractions import Fraction as F
def sgn(x): return (x>0)-(x<0)
def run(s,a,N=300):
    B=lambda c,v: 2*c[0]*v[0]+s*(c[0]*v[1]+c[1]*v[0])+s*c[1]*v[1]
    c1=(-1,1); c2=(-a,1)
    Q=lambda n,k: n*n+s*n*k+s*k*(k+1)//2
    coef={}
    R=4*int(math.isqrt(N))+3*N//s+60
    for n in range(-R*s,R*s+1):
        for k in range(-R,R+1):
            q=Q(n,k)
            if q<0 or q>N: continue
            w=F(sgn(B(c1,(n,k)))-sgn(B(c2,(n,k))),2)
            P=1 if (n>=0 and k>=0) else 0
            d=P-w
            if d: coef[q]=coef.get(q,0)+d
    vals=sorted(set(coef.values()))
    return dict(s=s,a=a,Q_c2=str(F(2*a*a-2*s*a+s,2)),values=[str(v) for v in vals],ok=set(vals)<= {F(1),F(3,2)})
out=[]
for s in (5,6,7,8,9,11,13):
    for a in range(2,s):
        if 2*a*a-2*s*a+s<0:
            r=run(s,a,200 if s>9 else 300); out.append(r); print(r,flush=True)
json.dump(out,open('c2_choice.json','w'),indent=1)
