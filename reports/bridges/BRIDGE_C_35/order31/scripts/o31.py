# order31: RG25a/b, RG26. PREREG hashed first. Reads order30/order28 arrays read-only.
import sys, math, json, ast, numpy as np
sys.dont_write_bytecode=True
from cornerlib import *
from symbols import S_rows
N=105; n=np.linalg.norm; k=1/math.sqrt(35); out={}; B='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'
d=np.load(B+'order18/data/a2_arrays.npz'); CO,SCO=d['CO'],d['SCO']
Z=np.load(B+'order27/data/o27_arrays.npz'); GCO,SGCO=Z['g^1h^0'],Z['Sg^1h^0']
C30=np.load(B+'order30/data/o30_cones.npz'); C28=np.load(B+'order28/data/o28_arrays.npz')
M=np.zeros((N,N),complex)
for j,dd in enumerate(S_rows()):
    for kk,es in dd.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
xs=np.array([float(x) for x in XS])
vtx=np.array([1.0 if (Fr(al[0]).denominator==1 and Fr(al[1]).denominator==1) else 0.0 for al,be in pairs])
V1=np.tile(vtx,(216,1)).astype(complex)
stk=lambda Y,SY: np.concatenate([Y.ravel(),SY.ravel()])
Qw,_=np.linalg.qr(np.stack([stk(CO,SCO),stk(GCO,SGCO),stk(V1,V1)],1))
def dist(Y,SY): v=stk(Y,SY); return float(n(v-Qw@(Qw.conj().T@v))/n(v))
def fam(Y,S):
    res={}
    for w in (-1,-0.5,0,0.5,1):
        X=(xs**-w)[:,None]*k*(Y@M.T); kap=np.vdot(X,S)/np.vdot(X,X); res[w]=(float(n(S-kap*X)/n(S)),complex(kap))
    return res
Am=np.array([[2,7],[7,7]]); Qf=lambda u:0.5*np.array(u)@Am@np.array(u)
ell=lambda u,v: math.acosh((np.array(u)@Am@np.array(v))/(2*math.sqrt(Qf(u)*Qf(v))))
out['C1']=float(max(np.abs(C30['(1, 0)_(0, 1)']-CO).max(),np.abs(C30['S(1, 0)_(0, 1)']-SCO).max()))
out['C2_relerr']=abs(float(n(SCO-xs[:,None]*k*(CO@M.T)))-54.4056376674763)/54.4056376674763
out['C3']=abs(math.acosh(math.sqrt(3.5))-0.5*math.log(6+math.sqrt(35)))
rows=[]
for key in C30.files:
    if key.startswith('S'): continue
    a,b=key.split('_'); u=ast.literal_eval(a); v=ast.literal_eval(b)
    Y,S=C30[key],C30['S'+key]; f=fam(Y,S); ws=min(f,key=lambda w:f[w][0]); r,kap=f[-1]
    dv=dist(Y,S); ok=(ws==-1 and abs(kap-1)<=0.01 and r<=0.10)
    rows.append(dict(cone=key,ell=ell(u,v),maxnorm=max(abs(t) for t in u+v),r=r,kappa=[kap.real,kap.imag],wstar=ws,r_all={str(w):f[w][0] for w in f},nonvac_d=dv,criterion=bool(ok)))
out['cones']=rows
nv=[r for r in rows if r['nonvac_d']>1e-3]; viol=[r for r in nv if not r['criterion']]
out['RG25a']=dict(n_nonvac=len(nv),n_violate=len(viol),violators=[(r['cone'],r['wstar'],r['kappa'],r['r']) for r in viol],verdict='PASS' if not viol else ('FAIL' if len(viol)>0.25*len(nv) else 'inconclusive'))
sub=[r for r in rows if r['cone']!='(1, 0)_(0, 1)']
from scipy.stats import pearsonr, spearmanr
R_=np.array([r['r'] for r in sub]); E=np.array([r['ell'] for r in sub]); MX=np.array([r['maxnorm'] for r in sub])
rp=float(pearsonr(R_,E)[0]); rs=float(spearmanr(R_,E)[0]); c=float(R_@E/(E@E)); fitres=float(n(R_-c*E)/n(R_))
v='proportional' if (rp>=0.9 and fitres<=0.1) else ('independent' if abs(rs)<=0.3 else 'intermediate')
out['RG25b']=dict(n=len(sub),pearson=rp,spearman=rs,c=c,fit_relres=fitres,spearman_vs_maxnorm=float(spearmanr(R_,MX)[0]),r_range=[float(R_.min()),float(R_.max())],ell_range=[float(E.min()),float(E.max())],verdict=v)
g={}
for a,bk in (('K2','(1, 1)_(0, 1)'),('K1','(1, 0)_(1, 1)')):
    jj={'K2':'J1','K1':'J2'}[a]; f1=fam(C30[bk],C30['S'+bk])[-1]; f2=fam(C28[jj],C28['S'+jj])[-1]
    g[a+'_vs_'+jj]=dict(dr=abs(f1[0]-f2[0]),dk=abs(f1[1]-f2[1]))
mx=max(max(t['dr'],t['dk']) for t in g.values())
out['RG26']=dict(pairs=g,max=mx,verdict='PASS' if mx<=1e-12 else ('FAIL' if mx>1e-9 else 'inconclusive'))
json.dump(out,open('../data/o31.json','w'),indent=1)
print(json.dumps({k:v for k,v in out.items() if k!='cones'},indent=1))
for r in rows: print(r['cone'],round(r['ell'],4),round(r['r'],4),[round(t,4) for t in r['kappa']],r['wstar'],round(r['nonvac_d'],4),r['criterion'])
