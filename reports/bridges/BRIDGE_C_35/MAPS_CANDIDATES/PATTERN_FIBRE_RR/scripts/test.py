import json,hashlib
from fractions import Fraction as F
h=open('PREREG.sha256').read().split()[0]; assert hashlib.sha256(open('PREREG.md','rb').read()).hexdigest()==h
d=json.load(open('data/explore.json'))
# recompute independently
Ai=[[F(-1,5),F(1,5)],[F(1,5),F(-2,35)]]; a=(F(7,10),F(-1,5)); al=set()
for x in range(70):
  for y in range(70):
    v=(Ai[0][0]*x+Ai[0][1]*y,Ai[1][0]*x+Ai[1][1]*y)
    for s in (0,1): al.add(((v[0]+s*a[0])%1,(v[1]+s*a[1])%1))
labels=[(A,b) for A in al for b in (0,1)]; assert len(labels)==140
m=[F(0)]*8
for A,b in labels:
  for n in range(8):
    e=40*F(5,2)*(A[0]+n)**2; assert e.denominator==1; m[int(e)%8]+=F(1,8*140)
assert [str(x) for x in m]==d['POOL_ALL140_Nmin']
r=[F(x,32) for x in (1,8,3,0,7,8,5,0)]
out=dict(prereg_sha=h,rho_mod=[str(x) for x in m],rho_res=[str(x) for x in r],P1=m==r,
 TV=str(sum(abs(x-y) for x,y in zip(m,r))/2),zero_3_7=m[3]==0 and m[7]==0,
 supp_mod=[i for i in range(8) if m[i]],supp_res=[i for i in range(8) if r[i]],verdict='PASS' if m==r else 'FAIL')
print(json.dumps(out)); json.dump(out,open('data/test.json','w'),indent=1)
