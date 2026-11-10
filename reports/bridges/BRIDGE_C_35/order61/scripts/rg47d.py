# order61 RG47d. PREREG sha in ../PREREG.sha256. Rank method copied from order60 rg47.py.
import os,json,numpy as np
B='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'; here=os.path.dirname(os.path.abspath(__file__))
os.chdir(B+'order54/scripts'); exec(open('rg45c.py').read().split('TS=[')[0]); os.chdir(here)
P=np.load(B+'order3/data/parts.npz'); R56=np.load(B+'order56/data/rg46_raw.npy'); R58=np.load(B+'order61/data/rg47a_bis_raw.npy')
H=P['A1']-R56[:,0,:,0]+R56[:,0,:,1]; HS=P['S_A1']-R56[:,1,:,0]+R56[:,1,:,1]
xs=np.array([abs(float(x)) for x in XS])
def rk(M,tol=1e-9): s=np.linalg.svd(M,compute_uv=False); return int((s/s[0]>tol).sum())
def t(Fm,FS,w,tol=1e-9): a=rk(Fm,tol); j=rk(np.hstack([Fm,(xs**w)[:,None]*FS]),tol); return dict(rank=a,joint=j,excess=j-a)
def obj(sub):
    A,AS=H.copy(),HS.copy()
    for j in sub: A=A-R58[:,0,:,j]; AS=AS-R58[:,1,:,j]
    return A,AS
res={}; out={}
for name,sub in (('Ahat',[]),('R_Q1',[0]),('R_Q72',[1]),('R_both',[0,1])):
    A,AS=obj(sub); out[name]={str(w):t(A,AS,w) for w in (0.5,1.0)}
res['rank']=out
g=out['Ahat']; res['gate']=bool(g['0.5']['rank']==75 and g['0.5']['joint']==148 and g['1.0']['joint']==150)
A,AS=obj([0,1])
res['sens']={str(tol):{str(w):t(A,AS,w,tol) for w in (0.5,1.0)} for tol in (1e-6,1e-12)}
# characterization
ch={}
for w in (0.5,1.0):
    M=np.hstack([A,(xs**w)[:,None]*AS]); s=np.linalg.svd(M,compute_uv=False); sa=np.linalg.svd(A,compute_uv=False)
    ra=int((sa/sa[0]>1e-9).sum()); rj=int((s/s[0]>1e-9).sum())
    # excess directions: component of S-block orthogonal to col-space of A
    U,sv,_=np.linalg.svd(A,full_matrices=False); Ur=U[:,:ra]
    Sb=(xs**w)[:,None]*AS; Res=Sb-Ur@(Ur.conj().T@Sb)
    Ue,se,_=np.linalg.svd(Res,full_matrices=False); k=max(rj-ra,0)
    rows=np.abs(Ue[:,:k])**2 if k else np.zeros((len(xs),0))
    top=np.argsort(-rows.sum(1))[:8] if k else []
    ch[str(w)]=dict(sv_joint_rel_around_cut=[float(v) for v in (s/s[0])[max(rj-3,0):rj+3]],
        sv_A_rel_around_cut=[float(v) for v in (sa/sa[0])[max(ra-3,0):ra+3]],
        resid_sv_rel=[float(v) for v in (se/s[0])[:5]],
        top_rows=[dict(i=int(i),x=str(XS[i]),weight=float(rows[i].sum())) for i in top])
ch['corner_max_abs']=float(abs(R58[...,2]).max()); ch['R_both_max_abs']=float(abs(A).max()); ch['R_both_S_max_abs']=float(abs(AS).max())
res['char']=ch
ex=[out['R_both'][w]['excess'] for w in ('0.5','1.0')]
res['RG47d']='INVALID' if not res['gate'] else ('PASS' if max(ex)<=0 else 'FAIL')
print(json.dumps(res,indent=1)); json.dump(res,open('../data/rg47d.json','w'),indent=1)
