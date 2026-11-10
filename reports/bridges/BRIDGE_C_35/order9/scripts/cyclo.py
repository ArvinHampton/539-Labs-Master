# Exact check of M^2 = 35 P in Z[zeta_9800]: an algebraic integer whose conjugates all have |.|<1 is 0.
# Evaluate D = M^2 - 35P under every embedding zeta -> zeta^g, gcd(g,9800)=1; max|D| < 0.5 for all g proves D = 0.
import sys, json, math, numpy as np; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from symbols import FAM, sym_pair, S_rows, L as LL, reduce
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
rows=S_rows(); neg=lambda v:(-v[0],-v[1])
Pe=[reduce(neg(al),neg(be)) for al,be in pairs]
gs=[g for g in range(1,LL) if math.gcd(g,LL)==1]
mx=0.0
for g in gs:
    M=np.zeros((105,105),complex)
    for j,d in enumerate(rows):
        for kk,es in d.items():
            for e in es: M[j,kk]+=np.exp(2j*np.pi*((g*e)%LL)/LL)
    P=np.zeros((105,105),complex)
    for j,(k,e) in enumerate(Pe): P[j,k]=np.exp(2j*np.pi*((g*e)%LL)/LL)
    mx=max(mx,float(np.abs(M@M-35*P).max()))
res=dict(L=LL,n_embeddings=len(gs),max_abs_over_all_embeddings=mx,exact_identity_proved=mx<0.5)
print(res); json.dump(res,open('../data/cyclo.json','w'),indent=1)
