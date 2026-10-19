# s=7: general primitive c=(-a,b), b<=6, negative norm; Cmixed first nonzero degree (exact, through q^N);
# also c1 alternatives with c2=(-4,1).
import json, math
from fractions import Fraction as F
s=7; N=700
sgn=lambda x:(x>0)-(x<0)
B=lambda c,v: 2*c[0]*v[0]+s*(c[0]*v[1]+c[1]*v[0])+s*c[1]*v[1]
Q=lambda n,k: n*n+s*n*k+(s*k*(k+1))//2
Qm=lambda n,k: n*n+s*n*k+(s*k*(k-1))//2
pts=[(n,k,Q(n,k)) for n in range(-3000,3001) for k in range(-150,151) if 0<=Q(n,k)<=N]
base=[F(0)]*(N+1)
for n in range(40):
  for k in range(40):
    if Q(n,k)<=N: base[Q(n,k)]+=1
base[0]-=F(3,2)
for n in range(1,40):
  if n*n<=N: base[n*n]-=1
for k in range(1,40):
  if 7*k*(k+1)//2<=N: base[7*k*(k+1)//2]-=1
for n in range(1,40):
  for k in range(1,40):
    if Qm(n,k)<=N: base[Qm(n,k)]-=1
def first(c1,c2):
  c=base[:]
  for n,k,q in pts:
    w=F(sgn(B(c1,(n,k)))-sgn(B(c2,(n,k))),2)
    if w: c[q]-=w
  nz=[q for q in range(N+1) if c[q]!=0]
  return nz[0] if nz else None
res=[]
for b in range(1,7):
  for a in range(1,7*b):
    if math.gcd(a,b)!=1: continue
    c=(-a,b); q2=2*a*a-2*s*a*b+s*b*b
    if q2>=0 or B((-1,1),c)>=0: continue
    r=dict(c=c,ratio=str(F(a,b)),Q=str(F(q2,2)),Q_over_b2=str(F(q2,2*b*b)),orthant_inside=bool(s*b-2*a<0 and s*(b-a)<0),
           M_image=(a-s*b,b),cmixed_first_nonzero=first((-1,1),c))
    res.append(r); print(r,flush=True)
alt=[]
for c1 in [(-1,1),(-2,1),(-3,1),(-7,2),(-6,1),(-1,2) ,(-2,3)]:
  q2=2*c1[0]**2+2*s*c1[0]*c1[1]+s*c1[1]**2
  if q2>=0: continue
  r=dict(c1=c1,Q=str(F(q2,2)),cmixed_first_nonzero_with_c2_m4_1=first(c1,(-4,1))); alt.append(r); print(r,flush=True)
json.dump(dict(c2_rays=res,c1_alternatives=alt),open('rays_s7.json','w'),indent=1)
