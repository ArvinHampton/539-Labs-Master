# order60 RG47b/RG47c. PREREG sha in ../PREREG.sha256
import os,json,math,numpy as np
B='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'; here=os.path.dirname(os.path.abspath(__file__))
os.chdir(B+'order54/scripts'); exec(open('rg45c.py').read().split('TS=[')[0]); os.chdir(here)
from fractions import Fraction as F
import sympy as sp
res={}
# RG47b-i symbolic prefactor
Q=sp.symbols('Q',positive=True); r=sp.simplify((sp.sqrt(sp.pi)/(2*sp.sqrt(Q)))/((sp.sqrt(sp.pi)/2)/sp.sqrt(Q)))
res['RG47b_i']=dict(ratio=str(r),Q1=str(r.subs(Q,1)),Q72=str(r.subs(Q,sp.Rational(7,2))),PASS=bool(r==1))
res['RG47b_ii']='SKIP: no written ray->sawtooth map'; res['RG47b_iii']='SKIP: no Eichler normalisation/constants/eval points for order6 shadows'
res['RG47b']='SKIP' if res['RG47b_i']['PASS'] else 'FAIL'
P=np.load(B+'order3/data/parts.npz'); R56=np.load(B+'order56/data/rg46_raw.npy'); R58=np.load(B+'order58/data/rg47a_raw.npy')
H=P['A1']-R56[:,0,:,0]+R56[:,0,:,1]; HS=P['S_A1']-R56[:,1,:,0]+R56[:,1,:,1]
xs=np.array([abs(float(x)) for x in XS])
def rk(M): s=np.linalg.svd(M,compute_uv=False); return int((s/s[0]>1e-9).sum())
def t(Fm,FS,w): a=rk(Fm); j=rk(np.hstack([Fm,(xs**w)[:,None]*FS])); return dict(rank=a,joint=j,excess=j-a,closed=a==j)
out={}
for name,sub in (('Ahat',None),('R_Q1',[0]),('R_Q72',[1]),('R_both',[0,1])):
    A,AS=H.copy(),HS.copy()
    if sub:
        for j in sub: A=A-R58[:,0,:,j]; AS=AS-R58[:,1,:,j]
    out[name]={str(w):t(A,AS,w) for w in (0.5,1.0)}
res['rank']=out
g=out['Ahat']; res['gate']=bool(g['0.5']['rank']==75 and g['0.5']['joint']==148 and g['1.0']['joint']==150)
red=lambda n:max(out['Ahat'][w]['excess']-out[n][w]['excess'] for w in ('0.5','1.0'))
res['reduction']={n:red(n) for n in ('R_Q1','R_Q72','R_both')}
if not res['gate']: v='INVALID'
elif any(out['R_Q1'][w]['closed'] for w in ('0.5','1.0')): v='PASS'
elif res['reduction']['R_Q1']>=10 and res['reduction']['R_Q1']>res['reduction']['R_Q72']: v='PARTIAL'
else: v='FAIL'
res['RG47c']=v
print(json.dumps(res,indent=1)); json.dump(res,open('../data/rg47.json','w'),indent=1)
