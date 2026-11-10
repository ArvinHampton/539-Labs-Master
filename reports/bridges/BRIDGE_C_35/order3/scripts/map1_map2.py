from lib3 import *
import json
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
keys=['A0','D','R','W1','W7/2','W595/2','A1']
P=XS
F={k:np.zeros((216,105),complex) for k in keys}; FS={k:np.zeros((216,105),complex) for k in keys}
maxdiff=0
for ix,x in enumerate(P):
    for j,(al,be) in enumerate(pairs):
        o=parts(al,be,x); oS=parts(al,be,-1/x)
        _,a1=A01_float(al,be,x); maxdiff=max(maxdiff,abs(a1-o['A1']))
        for k in keys: F[k][ix,j]=o[k]; FS[k][ix,j]=oS[k]
    if ix%20==0: print(ix,x,flush=True)
np.savez('../data/parts.npz',**{k.replace('/','_'):F[k] for k in keys},**{'S_'+k.replace('/','_'):FS[k] for k in keys})
xs=np.array([abs(float(x)) for x in P])
def nrank(M):
    s=np.linalg.svd(M,compute_uv=False); s=s/s[0]; return int((s>1e-9).sum()), float(s[min(len(s)-1,int((s>1e-9).sum()))])
res={'map1_max_abs_diff_parts_vs_A1':maxdiff}
def test(k,w): 
    r=nrank(F[k])[0]; rw=nrank(np.hstack([F[k],(xs**w)[:,None]*FS[k]]))[0]; return dict(rank=r,rank_joint=rw,closed=(rw==r),inconclusive=(r>=216))
res['control_A0_w1']=test('A0',1.0); res['control_A0_wrongsign']=test('A0',-1.0)
ctrl=res['control_A0_w1']['rank']==36 and res['control_A0_w1']['closed'] and res['control_A0_wrongsign']['rank_joint']>36
res['control_pass']=ctrl
print('control',res['control_A0_w1'],res['control_A0_wrongsign'],ctrl,flush=True)
for k,ws in (('D',(1.0,0.5)),('R',(0.5,1.0)),('W1',(0.5,1.0)),('W7/2',(0.5,1.0)),('W595/2',(0.5,1.0)),('A1',(0.5,1.0))):
    for w in ws: res[f'{k}_w{w}']=test(k,w); print(k,w,res[f'{k}_w{w}'],flush=True)
W=F['W1']+F['W7/2']+F['W595/2']; WS=FS['W1']+FS['W7/2']+FS['W595/2']
for w in (0.5,1.0):
    r=nrank(W)[0]; rw=nrank(np.hstack([W,(xs**w)[:,None]*WS]))[0]; res[f'W_total_w{w}']=dict(rank=r,rank_joint=rw,closed=rw==r,inconclusive=r>=216); print('Wtot',w,res[f'W_total_w{w}'])
json.dump(res,open('../data/map1_map2.json','w'),indent=1)
