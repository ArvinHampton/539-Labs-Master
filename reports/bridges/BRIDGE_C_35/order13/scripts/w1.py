# W1: exact certificate (M T)^3 = s P, s^2 = 35^3, over all 3360 embeddings of Z[e(1/9800)]
import sys, json, math, numpy as np; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from symbols import FAM, sym_pair, S_rows, T_rows, L as LL, reduce
Sr=S_rows(); Tr=T_rows(); neg=lambda v:(-v[0],-v[1])
Pe=[reduce(neg(al),neg(be)) for al,be in (sym_pair(f,i) for f in FAM for i in range(35))]
def mat(rows,g):
    X=np.zeros((105,105),complex)
    for j,d in enumerate(rows):
        for k,es in d.items():
            for e in es: X[j,k]+=np.exp(2j*np.pi*((g*e)%LL)/LL)
    return X
mo=md=mq=0.0; s_id=None
for g in (g for g in range(1,LL) if math.gcd(g,LL)==1):
    M=mat(Sr,g); T=mat(Tr,g); P=np.zeros((105,105),complex)
    for j,(k,e) in enumerate(Pe): P[j,k]=np.exp(2j*np.pi*((g*e)%LL)/LL)
    Y=np.linalg.matrix_power(M@T,3); Z=Y@P.conj().T
    off=Z-np.diag(np.diag(Z)); mo=max(mo,np.abs(off).max()); md=max(md,np.abs(np.diag(Z)-Z[0,0]).max()); mq=max(mq,abs(Z[0,0]**2-35**3))
    if g==1: s_id=Z[0,0]
res=dict(max_offdiag=mo,max_diag_spread=md,max_s2_minus_35cubed=mq,s_identity=[s_id.real,s_id.imag],s_over_35sqrt35=(s_id/(35*math.sqrt(35))).real,
         W1='pass' if max(mo,md,mq)<0.5 else 'FAIL')
print(res); json.dump(res,open('../data/w1.json','w'),indent=1)
