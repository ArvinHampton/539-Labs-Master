# order62 RG47e. PREREG sha in ../PREREG.sha256. Inputs/rank method copied from order61 rg47d.py.
import os,json,numpy as np
from fractions import Fraction
B='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'; here=os.path.dirname(os.path.abspath(__file__))
os.chdir(B+'order54/scripts'); exec(open('rg45c.py').read().split('TS=[')[0]); os.chdir(here)
P=np.load(B+'order3/data/parts.npz'); R56=np.load(B+'order56/data/rg46_raw.npy'); R58=np.load(B+'order61/data/rg47a_bis_raw.npy')
H=P['A1']-R56[:,0,:,0]+R56[:,0,:,1]; HS=P['S_A1']-R56[:,1,:,0]+R56[:,1,:,1]
xs=np.array([abs(float(x)) for x in XS])
def rk(M,tol=1e-9): s=np.linalg.svd(M,compute_uv=False); return int((s/s[0]>tol).sum())
R=H-R58[:,0,:,0]-R58[:,0,:,1]; RS=HS-R58[:,1,:,0]-R58[:,1,:,1]; C=R58[:,0,:,2]; CS=R58[:,1,:,2]
R2=R-C; R2S=RS-CS
res={}
res['gate']={str(w):rk(np.hstack([R,(xs**w)[:,None]*RS]))-rk(R) for w in (0.5,1.0)}
gate=res['gate']=={'0.5':34,'1.0':2}
res['sanity_max_abs']=float(max(abs(R2).max(),abs(R2S).max()))
def span(w,tol=1e-9):
    W=(xs**w)[:,None]
    base=rk(np.hstack([R,C]),tol); full=rk(np.hstack([R,C,W*RS,W*CS]),tol)
    r2=rk(R2,tol); r2j=rk(np.hstack([R2,W*R2S]),tol) if r2>0 else 0
    # defect directions of R in span(W*CS)?
    U,s,_=np.linalg.svd(R,full_matrices=False); ra=int((s/s[0]>tol).sum()); Ur=U[:,:ra]
    Sb=W*RS; Res=Sb-Ur@(Ur.conj().T@Sb); Ue,se,_=np.linalg.svd(Res,full_matrices=False)
    k=rk(np.hstack([R,Sb]),tol)-ra; D=Ue[:,:k]
    Uc,sc,_=np.linalg.svd(W*CS,full_matrices=False); Uc=Uc[:,:int((sc/sc[0]>tol).sum())]
    din=float(np.linalg.norm(D-Uc@(Uc.conj().T@D))) if k else 0.0
    rows=(abs(D)**2).sum(1); top=np.argsort(-rows)[:8]
    return dict(rank_RC=base,joint=full,excess_proj=full-base,rank_R2=r2,excess_R2=r2j-r2,defect_k=k,
        defect_resid_outside_corner_S=din,
        top_rows=[dict(x=str(XS[i]),den=Fraction(str(XS[i])).denominator if '/' in str(XS[i]) else 1,weight=float(rows[i])) for i in top])
res['w']={str(w):span(w) for w in (0.5,1.0)}
res['sens']={str(t):{str(w):span(w,t)['excess_proj'] for w in (0.5,1.0)} for t in (1e-6,1e-12)}
p1=res['sanity_max_abs']<=1e-12; p2=res['w']['1.0']['excess_proj']<=0
res['PASS1']=p1; res['PASS2']=p2
res['RG47e']='INVALID' if not gate else ('PASS' if p1 and p2 else 'FAIL')
print(json.dumps(res,indent=1)); json.dump(res,open('../data/rg47e.json','w'),indent=1)
