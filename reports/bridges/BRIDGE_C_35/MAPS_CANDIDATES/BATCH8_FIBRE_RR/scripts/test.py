import json
from fractions import Fraction as F
pre=open('PREREG.sha256').read().split()[0]
import hashlib; assert hashlib.sha256(open('PREREG.md','rb').read()).hexdigest()==pre
mod=[F(0)]*8
for n in range(8): mod[(170*n*n)%8]+=F(1,8)
res=[F(x,32) for x in (1,8,3,0,7,8,5,0)]
eq=mod==res
tv=sum(abs(a-b) for a,b in zip(mod,res))/2
out=dict(prereg_sha=pre,rho_res_mod=[str(x) for x in mod],rho_res=[str(x) for x in res],
 P1_exact_equal=eq,TV=str(tv),mod_zero_on_3_7=(mod[3]==0 and mod[7]==0),
 support_mod=[i for i in range(8) if mod[i]],support_res=[i for i in range(8) if res[i]],
 verdict='PASS' if eq else 'FAIL')
print(json.dumps(out,indent=1)); json.dump(out,open('data/test.json','w'),indent=1)
