import json,hashlib
from fractions import Fraction as F
h=open('PREREG.sha256').read().split()[0]; assert hashlib.sha256(open('PREREG.md','rb').read()).hexdigest()==h
Ai=[[F(-1,5),F(1,5)],[F(1,5),F(-2,35)]]; a=(F(7,10),F(-1,5)); al={}
for x in range(70):
  for y in range(70):
    v=(Ai[0][0]*x+Ai[0][1]*y,Ai[1][0]*x+Ai[1][1]*y)
    for s in (0,1): al[((v[0]+s*a[0])%1,(v[1]+s*a[1])%1)]=s
assert len(al)==70
Q=lambda u,v:u*u+7*u*v+F(7,2)*v*v
m=[F(0)]*8; coset={0:set(),1:set()}
for A,s in al.items():
  for n1 in range(8):
    for n2 in range(8):
      e=140*Q(A[0]+n1,A[1]+n2); assert e.denominator==1
      m[int(e)%8]+=F(2,140*64); coset[s].add(int(e)%8)
d=json.load(open('data/explore.json')); assert [str(x) for x in m]==d['POOL_ALL140']
r=[F(x,32) for x in (1,8,3,0,7,8,5,0)]
out=dict(prereg_sha=h,rho_mod=[str(x) for x in m],rho_res=[str(x) for x in r],P1=m==r,
 TV=str(sum(abs(x-y) for x,y in zip(m,r))/2),mass_3_7=str(m[3]+m[7]),
 supp_mod=[i for i in range(8) if m[i]],supp_res=[i for i in range(8) if r[i]],
 coset_Lprime_fibres=sorted(coset[0]),coset_a_fibres=sorted(coset[1]),verdict='PASS' if m==r else 'FAIL')
print(json.dumps(out)); json.dump(out,open('data/test.json','w'),indent=1)
