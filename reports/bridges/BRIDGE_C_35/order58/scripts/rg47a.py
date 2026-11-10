# order58 RG47a. PREREG sha in ../PREREG.sha256. Reuses order56 orth() sample (same 216x105 at x,-1/x).
import os,sys,json,math,numpy as np
from multiprocessing import Pool
B='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'
here=os.path.dirname(os.path.abspath(__file__))
os.chdir(B+'order54/scripts'); exec(open('rg45c.py').read().split('TS=[')[0]); os.chdir(here)
from lib2 import PIECES, piece_data, J, SQPI
def parts(al,be,x):
    sg,c,U=PIECES[0]; d=piece_data(al,be,x,c,U); N=d['N']; f=np.exp(2j*np.pi*d['k']/d['M'])
    mf=f.mean(); w1=(f*(d['z1']/N-0.5)).sum()/N; w2=(f*(d['z2']/N-0.5)).sum()/N; Ja,Jb=J(d['p'],d['q'],d['r'])
    corner=float(sg)*(-mf*(float(d['l1'])*Ja+float(d['l2'])*Jb))
    ax_e2=float(sg)*(-(SQPI/2)*w1/math.sqrt(float(d['r'])))   # Gaussian along e2 (Q=7/2), sawtooth B1 in z1
    ax_e1=float(sg)*(-(SQPI/2)*w2/math.sqrt(float(d['p'])))   # Gaussian along e1 (Q=1), sawtooth B1 in z2
    return (ax_e1,ax_e2,corner)
def row(i):
    x=XS[i]; return [[parts(al,be,X) for al,be in pairs] for X in (x,-1/x)]
if __name__=='__main__':
    with Pool(8) as p: R=np.array(p.map(row,range(216)))  # 216,2,105,3
    O=np.load(B+'order56/data/rg46_raw.npy')[...,2]          # A1(P_orth) from order56
    sc=np.maximum(np.abs(O),1e-300); S=R.sum(-1); W=-R[...,0]-R[...,1]+R[...,2]
    res=dict(resid_rel=float((abs(O-S)/np.maximum(abs(O),1)).max()),
             resid_rel_strict=float((abs(O-S)/sc).max()),
             ctrl_wrongsign_rel=float((abs(O-W)/np.maximum(abs(O),1)).max()))
    for j,n in enumerate(('axis_Q1','axis_Q7/2','corner_EVEN')):
        r=abs(R[...,j])/np.maximum(abs(O),1e-12)
        res[n]=dict(max_abs=float(abs(R[...,j]).max()),median_ratio=float(np.median(r)),max_ratio=float(r.max()),
                    frac_dominant=float((abs(R[...,j])>=abs(R).max(-1)-1e-15).mean()))
    res['RG47a_PASS']=bool(res['resid_rel']<=1e-6 and res['ctrl_wrongsign_rel']>1e-4)
    print(json.dumps(res,indent=1)); json.dump(res,open('../data/rg47a.json','w'),indent=1); np.save('../data/rg47a_raw.npy',R)
