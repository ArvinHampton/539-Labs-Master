import numpy as np, json
d=np.load('data/my_matrices.npz'); z=np.exp(2j*np.pi/140)
def m(E,s=1.0): return np.where(E>=0, z**np.where(E>=0,E,0), 0)*s
S=m(d['ES'],1/np.sqrt(35)); T=m(d['ET']); P=m(d['EP']); I=np.eye(len(S))
rS=np.linalg.inv(S); e=lambda A,B: float(np.abs(A-B).max()); mp=np.linalg.matrix_power
r={'T1_unitary':e(S@S.conj().T,I),'T2_S2=P':e(S@S,P),'T3_P2=I':e(P@P,I),'T4_rhoS4=I':e(mp(rS,4),I),
 'T5_(rhoS T)^3=rhoS^2':e(mp(rS@T,3),rS@rS),'C1_(Slab T)^3=Slab^2':e(mp(S@T,3),S@S),'C2_P-I':e(P,I)}
tol=1e-9; ok=all(r[k]<tol for k in r if k[0]=='T') and r['C1_(Slab T)^3=Slab^2']>tol and r['C2_P-I']>tol
r['RG49']='PASS' if ok else 'FAIL'; print(json.dumps(r,indent=1)); json.dump(r,open('data/rg49.json','w'),indent=1)
