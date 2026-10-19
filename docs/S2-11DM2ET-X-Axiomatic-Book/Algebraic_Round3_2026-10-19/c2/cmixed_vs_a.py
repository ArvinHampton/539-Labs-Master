# s=7: Cmixed^{(a)} = P - H^{(a)} - Caxis - Cthird for each admissible c=(-a,1); first nonzero degree (exact).
import json
from fractions import Fraction as F
s=7; N=1200
sgn=lambda x:(x>0)-(x<0)
B=lambda c,v: 2*c[0]*v[0]+s*(c[0]*v[1]+c[1]*v[0])+s*c[1]*v[1]
Q=lambda n,k: n*n+s*n*k+(s*k*(k+1))//2
Qm=lambda n,k: n*n+s*n*k+(s*k*(k-1))//2
base=[F(0)]*(N+1)
for n in range(0,40):
  for k in range(0,40):
    if Q(n,k)<=N: base[Q(n,k)]+=1          # P
base[0]-=F(3,2)
for n in range(1,40):
  if n*n<=N: base[n*n]-=1
for k in range(1,40):
  if 7*k*(k+1)//2<=N: base[7*k*(k+1)//2]-=1
for n in range(1,40):
  for k in range(1,40):
    if Qm(n,k)<=N: base[Qm(n,k)]-=1        # Cthird
out={}
for a in range(2,7):
  c=base[:]
  for n in range(-2500,2501):
    for k in range(-130,131):
      q=Q(n,k)
      if 0<=q<=N:
        w=F(sgn(B((-1,1),(n,k)))-sgn(B((-a,1),(n,k))),2)
        if w: c[q]-=w
  nz=[q for q in range(N+1) if c[q]!=0]
  out[a]=dict(Q_c=str(F(2*a*a-2*s*a+s,2)),orthant_inside=bool(s-2*a<0),first_nonzero=nz[0] if nz else None,first_coeffs=[(q,str(c[q])) for q in nz[:4]])
  print(a,out[a],flush=True)
json.dump(out,open('cmixed_vs_a_s7.json','w'),indent=1)
