import sys,json,numpy as np; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order3c/scripts')
from lib3c import *
D={n:np.zeros((216,105),complex) for n in ('A0','A1','A2','S_A0','S_A1','S_A2')}
for k in range(8):
    c=np.load('../data/chunk_%d.npz'%k)
    for n in D: D[n][c['idx']]=c[n]
np.savez('../data/A2.npz',**D)
res={}
ref=json.load(open('../../order3c/data/mapN_1.json'))['A2']
_,_,a2=A012(a,(Fr(0),Fr(0)),Fr(1)); res['anchor_diff']=abs(a2-complex(*ref)); assert res['anchor_diff']<1e-12
xs=np.array([abs(float(x)) for x in XS])
def rk(M): s=np.linalg.svd(M,compute_uv=False); return int((s/s[0]>1e-9).sum())
def t(F,FS,w): r=rk(F); j=rk(np.hstack([F,(xs**w)[:,None]*FS])); return dict(rank=r,joint=j,closed=r==j)
res['ctrl_w1']=t(D['A0'],D['S_A0'],1.0); res['ctrl_w0']=t(D['A0'],D['S_A0'],0.0)
res['control_pass']=res['ctrl_w1']['rank']==36 and res['ctrl_w1']['closed'] and not res['ctrl_w0']['closed']
for w in (0.0,0.5,1.0): res['A2_w%s'%w]=t(D['A2'],D['S_A2'],w)
span=np.hstack([D['A2'],(xs**0.5)[:,None]*D['A1'],xs[:,None]*D['A0']]); rs=rk(span)
res['T1']=dict(span_rank=rs,joint=rk(np.hstack([span,D['S_A2']])),inconclusive=rs>=216)
res['T1']['closed']=res['T1']['joint']==rs
print(json.dumps(res,indent=1)); json.dump(res,open('../data/test4b.json','w'),indent=1)
