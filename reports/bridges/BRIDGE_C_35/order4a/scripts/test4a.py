import numpy as np, json, itertools, sys
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS
P=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order3/data/parts.npz')
xs=np.array([abs(float(x)) for x in XS])
def rk(M): s=np.linalg.svd(M,compute_uv=False); return int((s/s[0]>1e-9).sum())
def t(F,FS,w): r=rk(F); j=rk(np.hstack([F,(xs**w)[:,None]*FS])); return dict(rank=r,joint=j,closed=r==j)
res={'ctrl_w1':t(P['A0'],P['S_A0'],1.0),'ctrl_wrong':t(P['A0'],P['S_A0'],-1.0)}
res['control_pass']=res['ctrl_w1']['rank']==36 and res['ctrl_w1']['closed'] and res['ctrl_wrong']['joint']>36
print(res,flush=True)
W=['W1','W7_2','W595_2']
for e in itertools.product((0,1),repeat=3):
    F=P['A1']-sum(e[i]*P[W[i]] for i in range(3)); FS=P['S_A1']-sum(e[i]*P['S_'+W[i]] for i in range(3))
    for w in (0.5,1.0): res['eps%s_w%s'%(''.join(map(str,e)),w)]=t(F,FS,w); print(e,w,res['eps%s_w%s'%(''.join(map(str,e)),w)])
json.dump(res,open('../data/test4a.json','w'),indent=1)
