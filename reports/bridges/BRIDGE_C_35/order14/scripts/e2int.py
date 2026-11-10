# E2-int: g(x) is P-even (b3x method, read-only import of order12 b3x g)
import sys, json, numpy as np; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order12/scripts')
exec(open('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order12/scripts/b3x.py').read().split('res={}')[0])
from symbols import FAM, sym_pair, reduce
P=np.zeros((105,105),dtype=np.clongdouble)
for j,(al,be) in enumerate(pairs):
    k,e=reduce((-al[0],-al[1]),(-be[0],-be[1])); a_=tp*ld(e)/ld(LL); P[j,k]=np.cos(a_)+1j*np.sin(a_)
res={}
for xs in ('1/2','1/3','-1/2','2/5'):
    gx=g(Fr(xs)); r=float(np.abs(gx-P@gx).max()/np.abs(gx).max()); res[xs]=r; print(xs,r,flush=True)
res['verdict']='pass' if max(res.values())<=1e-15 else 'FAIL'; print(res); json.dump(res,open('../data/e2int.json','w'),indent=1)
