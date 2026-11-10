# order61 RG47a-bis. PREREG sha in ../PREREG.sha256. Pieces logic copied from order58 rg47a.py.
import os,json,math,numpy as np
from multiprocessing import Pool
B='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'
here=os.path.dirname(os.path.abspath(__file__))
os.chdir(B+'order54/scripts'); exec(open('rg45c.py').read().split('TS=[')[0]); os.chdir(here)
from lib2 import PIECES, piece_data, J, SQPI
def parts(al,be,x):
    sg,c,U=PIECES[0]; d=piece_data(al,be,x,c,U); N=d['N']; f=np.exp(2j*np.pi*d['k']/d['M'])
    mf=f.mean(); w1=(f*(d['z1']/N-0.5)).sum()/N; w2=(f*(d['z2']/N-0.5)).sum()/N; Ja,Jb=J(d['p'],d['q'],d['r'])
    corner=float(sg)*(-mf*(float(d['l1'])*Ja+float(d['l2'])*Jb))
    ax_e2=float(sg)*(-(SQPI/2)*w1/math.sqrt(float(d['r'])))
    ax_e1=float(sg)*(-(SQPI/2)*w2/math.sqrt(float(d['p'])))
    return (ax_e1,ax_e2,corner)
def row(i):
    x=XS[i]; return [[parts(al,be,X) for al,be in pairs] for X in (x,-1/x)]
if __name__=='__main__':
    with Pool(8) as p: R=np.array(p.map(row,range(216)))
    O=np.load(B+'order56/data/rg46_raw.npy')[...,2]
    R58=np.load(B+'order58/data/rg47a_raw.npy')
    S=R.sum(-1); W=-R[...,0]-R[...,1]+R[...,2]
    a=float(abs(O-S).max()); c=float(abs(O-W).max())
    res=dict(abs_resid=a,ctrl_abs=c,ctrl_ok=c>1e-4,pieces_vs_order58_maxdiff=float(abs(R-R58).max()))
    for j,n in enumerate(('axis_Q1','axis_Q7/2','corner_EVEN')):
        r=abs(R[...,j])/np.maximum(abs(O),1e-12)
        res[n]=dict(max_abs=float(abs(R[...,j]).max()),median_ratio=float(np.median(r)),
                    frac_dominant=float((abs(R[...,j])>=abs(R).max(-1)-1e-15).mean()),frac_zero=float((R[...,j]==0).mean()))
    res['RG47a_bis']='PASS' if (a<=1e-12 and c>1e-4) else ('FAIL(control)' if a<=1e-12 else 'FAIL')
    print(json.dumps(res,indent=1)); json.dump(res,open('../data/rg47a_bis.json','w'),indent=1); np.save('../data/rg47a_bis_raw.npy',R)
