import json,hashlib
from fractions import Fraction as F
h=open('PREREG.sha256').read().split()[0]; assert hashlib.sha256(open('PREREG.md','rb').read()).hexdigest()==h
d=json.load(open('data/explore.json')); m=[F(x) for x in d['cesaro_from_uniform_push_T']]
r=[F(x,32) for x in (1,8,3,0,7,8,5,0)]
cls={k:[F(x) for x in v['push_T']] for k,v in d['classes'].items()}
any_on_2_6=any(v[2]!=0 or v[6]!=0 for v in cls.values())
out=dict(prereg_sha=h,push=[str(x) for x in m],rho_res=[str(x) for x in r],equal=m==r,
 TV=str(sum(abs(x-y) for x,y in zip(m,r))/2),any_stationary_mass_on_2_or_6=any_on_2_6,
 any_stationary_can_match=False if not any_on_2_6 else 'check',verdict='PASS' if m==r else 'FAIL')
print(json.dumps(out)); json.dump(out,open('data/test.json','w'),indent=1)
