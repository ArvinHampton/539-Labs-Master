import sys, math, json, numpy as np
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS, phase_ints, Fr
from symbols import FAM, sym_pair, S_rows, L
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for k,es in d.items():
        for e in es: M[j,k]+=np.exp(2j*np.pi*e/L)
xs=np.array([float(x) for x in XS]); n=np.linalg.norm
Z=np.load('../data/rg5_arrays.npz'); C,SC=Z['C'][2],Z['SC'][2]
def fit(A,S):
    Y=xs[:,None]*(A@M.T)/math.sqrt(35); k=np.vdot(Y,S)/np.vdot(Y,Y); return float(n(S-k*Y)/n(S)),[k.real,k.imag]
def gm(al,be,x):
    from math import lcm
    N=2*Fr(x).denominator
    for m in (1,2,5,7,10,14,35,70):
        P=N*m; i=np.arange(P); V=np.stack(np.meshgrid(i,i,indexing='ij'),-1).reshape(-1,2)
        k0,Mm=phase_ints(al,be,x,V); k1,_=phase_ints(al,be,x,V+np.array([P,0])); k2,_=phase_ints(al,be,x,V+np.array([0,P]))
        if (k0==k1).all() and (k0==k2).all(): return np.exp(2j*np.pi*k0/Mm).sum()
G=np.array([[gm(al,be,x) for (al,be) in pairs] for x in XS]); SG=np.array([[gm(al,be,-1/x) for (al,be) in pairs] for x in XS])
r6,k6=fit(C,SC); r6p,k6p=fit(C-G/6,SC-SG/6)
out=dict(RG6=dict(rel=r6,kappa=k6,verdict='PASS' if r6<=1e-8 else ('FAIL' if r6>=1e-3 else 'inconclusive')),
 RG6p=dict(rel=r6p,kappa=k6p,verdict='PASS (no law)' if r6p>=1e-3 else ('FAIL (law holds)' if r6p<=1e-8 else 'inconclusive')),
 note='Sum f_r over N^2 classes uses the period found per case; C2b used its own lcm period: constant-term normalisation may differ if periods differ')
print(out); json.dump(out,open('../data/rg6.json','w'),indent=1)
