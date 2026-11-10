# M3: character-twisted fixed S-law with one free scalar, on order7 data (660 tau)
import sys, json, math, numpy as np; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order7/scripts')
from lib7 import M
res={}
for k in ('H','ThE','E'):
    d=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order7/data/W_%s.npz'%k); V,W,T=d['V'],d['W'],d['T']
    X=(T/math.sqrt(35))[:,None]*(V@M.T)
    c=np.vdot(X.ravel(),W.ravel())/np.vdot(X.ravel(),X.ravel())
    r=float(np.abs(W-c*X).max()/max(1,np.abs(W).max()))
    res[k]=dict(c=[c.real,c.imag],r=r,dist_to_i=float(min(abs(c-1j),abs(c+1j))),dist_to_1=float(abs(c-1)))
res['control']='pass' if res['H']['r']<=1e-10 and res['H']['dist_to_1']<=1e-8 else 'FAIL'
for k in ('ThE','E'):
    v=res[k]; res['M3_'+k]='pass' if (v['r']<=1e-10 and v['dist_to_i']<=1e-8) else ('FAIL' if v['r']>1e-4 else 'inconclusive')
print(json.dumps(res,indent=1)); json.dump(res,open('../data/m3.json','w'),indent=1)
