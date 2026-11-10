# order37 RG34. PREREG hashed first. Stored arrays only.
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
kap=np.vdot(X.ravel(),S.ravel())/np.vdot(X.ravel(),X.ravel())
r=np.array([n(S[i]-kap*X[i])/n(S[i]) for i in range(216)]); rglob=float(n(S-kap*X)/n(S))
den=np.array([Fr(x).denominator for x in XS]); num=np.array([abs(Fr(x).numerator) for x in XS])
i1=XS.index(Fr(1)); c=r[i1]; pred=c/den**2.0; mask=np.arange(216)!=i1
e=np.abs(r-pred)/r; em=float(np.median(e[mask])); e90=float(np.percentile(e[mask],90))
v='PASS' if (em<=0.10 and e90<=0.25) else ('FAIL' if em>=0.5 else 'inconclusive')
canc={int(d):float(np.median(r[den==d]*d*d/c)) for d in sorted(set(den))}
p_hat=float(-np.polyfit(np.log(den[mask]),np.log(r[mask]),1)[0]); mx=np.maximum(den,num)
p_hat_mx=float(-np.polyfit(np.log(mx[mask]),np.log(r[mask]),1)[0])
out=dict(kappa=[kap.real,kap.imag],r_global=rglob,c=float(c),median_e=em,p90_e=e90,verdict=v,cancellation_by_den=canc,
  spearman_den=float(spearmanr(r,den)[0]),spearman_num=float(spearmanr(r,num)[0]),spearman_max=float(spearmanr(r,mx)[0]),p_hat_den=p_hat,p_hat_max=p_hat_mx,
  per_point=[dict(x=str(x),den=int(a),r=float(b),r_pred=float(cc),e=float(ee)) for x,a,b,cc,ee in zip(XS,den,r,pred,e)])
json.dump(out,open('../data/o37.json','w'),indent=1)
print(json.dumps({k:v_ for k,v_ in out.items() if k!='per_point'},indent=1))
