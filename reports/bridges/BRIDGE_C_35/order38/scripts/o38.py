# order38 RG35/RG35b. PREREG hashed first. Stored arrays only.
import sys, math, json, numpy as np
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS, Fr
from symbols import S_rows, L
from scipy.stats import spearmanr
Z=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order19/data/rg5_arrays.npz'); Y,S=Z['C'][2],Z['SC'][2]
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
n=np.linalg.norm; xs=np.array([float(x) for x in XS]); X=xs[:,None]*(Y@M.T)/math.sqrt(35)
kap=np.vdot(X.ravel(),S.ravel())/np.vdot(X.ravel(),X.ravel()); Rm=S-kap*X; rm=float(n(Rm)/n(S))
def proj(B):
    U,s,_=np.linalg.svd(B,full_matrices=False); rk=int((s/s[0]>1e-9).sum()); U=U[:,:rk]; return U,rk
out={'r_meas':rm,'kappa':[kap.real,kap.imag]}
Uv,rkv=proj(np.hstack([xs[:,None]*Y,S])); lv=float(n(S-Uv@(Uv.conj().T@S))/n(S))
out['vacuity_control']=dict(rank=rkv,leftover=lv,note='S columns are in the span by construction')
U,rk=proj(xs[:,None]*Y); P=S-U@(U.conj().T@S); rb=float(n(P)/n(S))
ratio=rb/rm
pp_r=[float(n(Rm[i])/n(S[i])) for i in range(216)]; pp_l=[float(n(P[i])/n(S[i])) for i in range(216)]
out['RG35']=dict(rank_WB=rk,r_B=rb,ratio=ratio,spearman_pp=float(spearmanr(pp_r,pp_l)[0]),verdict='PASS' if ratio>=1-1e-6 else ('FAIL' if ratio<=0.9 else 'inconclusive'))
num=np.array([abs(Fr(x).numerator) for x in XS]); g={}
for v in sorted(set(num)):
    m=num==v
    if m.sum()>=3: g[int(v)]=dict(n=int(m.sum()),median_r=float(np.median(np.array(pp_r)[m])))
ks=list(g); rho=float(spearmanr(ks,[g[k]['median_r'] for k in ks])[0])
out['RG35b']=dict(groups=g,spearman=rho,verdict='PASS' if rho<=-0.9 else ('FAIL' if rho>=-0.5 else 'inconclusive'))
out['per_point']=[dict(x=str(x),r=a,leftover=b) for x,a,b in zip(XS,pp_r,pp_l)]
json.dump(out,open('../data/o38.json','w'),indent=1)
print(json.dumps({k:v for k,v in out.items() if k!='per_point'},indent=1))
