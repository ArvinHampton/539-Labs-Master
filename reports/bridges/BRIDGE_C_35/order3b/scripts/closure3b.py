import numpy as np, json, sys
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS
P=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order3/data/parts.npz'); Rs=np.load('../data/rays_split.npz')
xs=np.array([abs(float(x)) for x in XS])
res={}
res['map1_max']=float(max(abs(Rs['R7']+Rs['R595']-P['R']).max(),abs(Rs['S_R7']+Rs['S_R595']-P['S_R']).max()))
assert res['map1_max']<=1e-12, res
def rk(M):
    s=np.linalg.svd(M,compute_uv=False); return int((s/s[0]>1e-9).sum())
def test(F,FS,w,cols=slice(None)):
    F=F[:,cols];FS=FS[:,cols]; r=rk(F); rj=rk(np.hstack([F,(xs**w)[:,None]*FS])); return dict(rank=r,joint=rj,closed=rj==r)
c1=test(P['A0'],P['S_A0'],1.0); c2=test(P['A0'],P['S_A0'],-1.0)
res['control']=[c1,c2]; res['control_pass']=c1['rank']==36 and c1['closed'] and c2['joint']>36
print('control',res['control'],res['control_pass'],flush=True)
G={'G[1]':(P['W1'],P['S_W1']),'G[7/2]':(P['W7_2']+Rs['R7'],P['S_W7_2']+Rs['S_R7']),
   'G[595/2]':(P['W595_2']+Rs['R595'],P['S_W595_2']+Rs['S_R595']),'G[D]':(P['D'],P['S_D']),'A1':(P['A1'],P['S_A1'])}
TH={'Theta1(K2+K3)':slice(0,70),'Theta2(K4)':slice(70,105)}
for k,(F,FS) in G.items():
    for w in (0.5,1.0):
        res[f'{k}|w{w}']=test(F,FS,w); print(k,w,res[f'{k}|w{w}'],flush=True)
        for t,cs in TH.items():
            res[f'{k}|{t}|w{w}']=test(F,FS,w,cs); print('  ',t,res[f'{k}|{t}|w{w}'],flush=True)
for t,cs in TH.items(): res[f'A0|{t}|w1']=test(P['A0'],P['S_A0'],1.0,cs); print('A0',t,res[f'A0|{t}|w1'])
json.dump(res,open('../data/closure3b.json','w'),indent=1)
