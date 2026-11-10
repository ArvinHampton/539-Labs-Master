import json,hashlib
from fractions import Fraction as F
h=open('PREREG.sha256').read().split()[0]; assert hashlib.sha256(open('PREREG.md','rb').read()).hexdigest()==h
d=json.load(open('data/explore.json')); r=[F(x,32) for x in (1,8,3,0,7,8,5,0)]
c=[cl for cl in d['ST']['classes'] if cl['size']==105][0]
out={'prereg_sha':h,'rho_res':[str(x) for x in r]}
for n,v in (('PST1',d['uniform_push_T']),('PST2',c['push_T'])):
  m=[F(x) for x in v]; assert sum(m)==1
  out[n]=dict(push=v,equal=m==r,TV=str(sum(abs(x-y) for x,y in zip(m,r))/2),verdict='PASS' if m==r else 'FAIL')
out['any_stationary_mass_on_2_6']=d['ST']['any_mass_on_2_6']
print(json.dumps(out,indent=1)); json.dump(out,open('data/test.json','w'),indent=1)
