import json,hashlib
from fractions import Fraction as F
h=open('PREREG.sha256').read().split()[0]; assert hashlib.sha256(open('PREREG.md','rb').read()).hexdigest()==h
d=json.load(open('data/explore_R200.json'))
r=[F(x,32) for x in (1,8,3,0,7,8,5,0)]; out={'prereg_sha':h,'rho_res':[str(x) for x in r]}
for name,key in (('PBR1','A_unsigned_pool140'),('PBR2','T_pool140')):
  m=[F(x) for x in d[key]]; assert sum(m)==1
  out[name]=dict(rho=[str(x) for x in m],equal=m==r,TV=str(sum(abs(x-y) for x,y in zip(m,r))/2),
    mass_3_7=str(m[3]+m[7]),supp=[i for i in range(8) if m[i]],verdict='PASS' if m==r else 'FAIL')
print(json.dumps(out,indent=1)); json.dump(out,open('data/test.json','w'),indent=1)
