# Exact (exponent arithmetic mod K) commutation of label maps with S and T, in BOTH conventions:
#  'vecfam' X[j(i),i]=z^ph_i  (used in commutant.py, vecfam.maps, sec_sparse, sec_valid)   vs   'P' Y[i,j(i)]=z^ph_i (= Family.Pmatrix convention, Y_neg = S^2).
import sys, json, numpy as np
sys.path.insert(0,'/workspace/quantum-comp/reports/heavy-daily/2026-10-18-Open-Algebraic')
from vecfam import VF
def mono_from(E):  # E exponent matrix of vecfam map (E[j,i]=ph): return j(i), ph(i)
    N=E.shape[0]; jj=np.argmax(E>=0,axis=0); ph=E[jj,np.arange(N)]; assert np.all((E>=0).sum(0)==1); return jj,ph
def commutes(M,jj,ph,K,conv):
    N=M.shape[0]; inv=np.argsort(jj)
    # conv 'P': Y[i,jj[i]]=ph[i].  (YM)[i,:]=ph[i]+M[jj[i],:] ; (MY)[:,k] = M[:,m]+ph[m] with jj[m]=k
    if conv=='P':
        YM=np.where(M[jj,:]>=0,(M[jj,:]+ph[:,None])%K,-1)
        MY=np.where(M[:,inv]>=0,(M[:,inv]+ph[inv][None,:])%K,-1)
    else: # X[jj[i],i]=ph[i]: (XM)[jj[i],:]=ph[i]+M[i,:] ; (MX)[:,jj[i]]=M[:,i]+ph[i]
        XM=np.full_like(M,-1); XM[jj,:]=np.where(M>=0,(M+ph[:,None])%K,-1); YM=XM
        MX=np.full_like(M,-1); MX[:,jj]=np.where(M>=0,(M+ph[None,:])%K,-1); MY=MX
    return bool(np.array_equal(YM,MY))
out={}
for s in map(int,sys.argv[1].split(',')):
    v=VF(s); K=v.K; S=v.S_exp(); T=v.T_exp(); r={}
    for k,E in v.maps().items():
        jj,ph=mono_from(E)
        r[str(k)]={c:{'S':commutes(S,jj,ph,K,c),'T':commutes(T,jj,ph,K,c)} for c in ('vecfam','P')}
    out[s]=r; print(s,r,flush=True)
json.dump(out,open('/workspace/quantum-comp/reports/heavy-daily/2026-10-18-Symmetry-Audit/exact_commute.json','w'),indent=1)
