# task (a): P1, P2, line checks, completed-law tests on XS216 (float SVD, threshold 1e-9)
import sys, pickle, json, glob, math; sys.dont_write_bytecode=True
import numpy as np
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from lib2 import XS
from symbols import S_rows, L as LL
D={}
for f in glob.glob('../data/a_chunk_*.pkl'): D.update(pickle.load(open(f,'rb')))
assert len(D)==432
names=['full','orth','fullneg','F','UH','UO']
G={}
for s in ('x','S'):
    for ni,n in enumerate(names):
        for o in range(3): G[(s,n,o)]=np.array([[D[(i,s)][j][ni][o] for j in range(105)] for i in range(216)])
np.savez('../data/a_arrays.npz',**{'%s_%s_%d'%k:v for k,v in G.items()})
g=lambda s,n,o: G[(s,n,o)]
res={}
res['P1_max_A2H']=float(max(np.abs(g(s,'full',2)-g(s,'orth',2)).max() for s in 'xS'))
res['P2_max']=float(max(np.abs(g(s,'full',2)-g(s,'fullneg',2)-g(s,'F',2)).max() for s in 'xS'))
res['lines_A2_max']=float(max(np.abs(g(s,n,2)).max() for s in 'xS' for n in ('UH','UO')))
res['scale_A2']=float(np.abs(g('x','full',2)).max())
v=lambda r:'pass' if r<=1e-11 else ('FAIL' if r>1e-6 else 'inconclusive')
res['P1']=v(res['P1_max_A2H']); res['P2']=v(res['P2_max'])
xs=np.array([abs(float(x)) for x in XS])
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for e in es: M[j,kk]+=np.exp(2j*np.pi*e/LL)
def rk(A): s=np.linalg.svd(A,compute_uv=False); return int((s/s[0]>1e-9).sum())
def t(F,FS,w,fixed=True):
    r=rk(F); j=rk(np.hstack([F,(xs**w)[:,None]*FS])); d=dict(rank=r,joint=j,closed=r==j)
    if fixed:
        pred=(xs**-w)[:,None]*(F@M.T)/math.sqrt(35); d['fixed_resid']=float(np.abs(FS-pred).max()/np.abs(FS).max())
    return d
res['ctrl_w1']=t(g('x','full',0),g('S','full',0),1.0); res['ctrl_wm1']=t(g('x','full',0),g('S','full',0),-1.0)
res['control_pass']=res['ctrl_w1']['rank']==36 and res['ctrl_w1']['closed'] and not res['ctrl_wm1']['closed']
obj={}
for s in 'xS':
    obj[('A1c',s)]=g(s,'orth',1)+g(s,'UH',1)
    obj[('A2c',s)]=g(s,'orth',2)
    obj[('A1c_odd',s)]=-g(s,'UO',1)+2*g(s,'UH',1)+g(s,'F',1)
    obj[('A2c_odd',s)]=g(s,'F',2)
    obj[('A1',s)]=g(s,'full',1); obj[('A2',s)]=g(s,'full',2)
for name,ws in (('A1',(0.5,1.0)),('A1c',(0.5,1.0)),('A1c_odd',(0.5,1.0)),('A2',(0.0,0.5)),('A2c',(0.0,0.5)),('A2c_odd',(0.0,0.5))):
    for w in ws: res['%s_w%s'%(name,w)]=t(obj[(name,'x')],obj[(name,'S')],w,fixed=not name.endswith('odd'))
print(json.dumps(res,indent=1)); json.dump(res,open('../data/atest.json','w'),indent=1)
