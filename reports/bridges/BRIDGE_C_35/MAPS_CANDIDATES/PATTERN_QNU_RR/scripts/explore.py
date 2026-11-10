# Q(nu)=nu1^2+7nu1nu2+(7/2)nu2^2 (rev8 l.134) on alpha+Z^2, 140 written labels (rev8 l.137-143, l.272).
# Does not read the residual law. Exact: integer arithmetic on 70*nu.
import json, numpy as np
from fractions import Fraction as F
from math import lcm, gcd
Ai=[[F(-1,5),F(1,5)],[F(1,5),F(-2,35)]]; a=(F(7,10),F(-1,5)); al=set()
for x in range(70):
  for y in range(70):
    v=(Ai[0][0]*x+Ai[0][1]*y,Ai[1][0]*x+Ai[1][1]*y)
    for s in (0,1): al.add(((v[0]+s*a[0])%1,(v[1]+s*a[1])%1))
al=sorted(al); labels=[(A,b) for A in al for b in (0,1)]; assert len(labels)==140
# Q in units of 1/(2*70^2): with X=70nu1, Y=70nu2 integers: 2*4900*Q = 2X^2+14XY+7Y^2
def Qnum(X,Y): return 2*X*X+14*X*Y+7*Y*Y   # Q = Qnum/9800
# least N with N*Q integral on all labels: N = 9800/gcd(9800, all Qnum values)
g=0
for A in al:
  X0,Y0=int(70*A[0]),int(70*A[1])
  for n1 in range(4):
    for n2 in range(4): g=gcd(g,Qnum(X0+70*n1,Y0+70*n2))
N=9800//gcd(9800,g); scale_den=9800//N  # N*Q = Qnum/scale_den
print('N_min_scale',N)
# period: N*Q(alpha+n) mod 8 is periodic in n mod P; find P by test
def dist(A,P):
  X0,Y0=int(70*A[0]),int(70*A[1])
  n1,n2=np.meshgrid(np.arange(P),np.arange(P),indexing='ij')
  q=Qnum(X0+70*n1.astype(np.int64),Y0+70*n2.astype(np.int64))
  assert (q%scale_den==0).all()
  e=(q//scale_den)%8
  return np.bincount(e.ravel(),minlength=8)
for P in (8,16):
  ok=all((dist(A,P)*(16//P)**2==dist(A,16)).all() for A in al)
  print('period',P,'consistent with 16:',ok)
P=16
res={'N_min_scale':N,'period_box':P,'density':'uniform over n mod P (= natural density on expanding boxes)'}
pool=[F(0)]*8; per={}
for A in al:
  c=dist(A,P); m=[F(int(x),P*P) for x in c]; per[f'{A[0]},{A[1]}']=[str(x) for x in m]
  for b in (0,1): pool=[p+x/140 for p,x in zip(pool,m)]
res['POOL_ALL140']=[str(x) for x in pool]
res['support_pool']=[i for i in range(8) if pool[i]]
res['per_alpha']=per
sub=[A for A in al if 70*A[0] in (7,21,49,63)]
sp=[F(0)]*8
for A in sub:
  c=dist(A,P); sp=[p+F(int(x),P*P*len(sub)) for p,x in zip(sp,c)]
res['POOL_70a1_7_21_49_63']=[str(x) for x in sp]
print(json.dumps({k:v for k,v in res.items() if k!='per_alpha'},indent=1))
json.dump(res,open('data/explore.json','w'),indent=1)
