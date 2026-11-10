# POST-HOC diagnostics (after recording order17 verdicts). Norms of pieces.
import numpy as np, sys
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
import lib2
from symbols import FAM, sym_pair, reduce, L
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
P=np.zeros((105,105),complex)
for j,(al,be) in enumerate(pairs):
    k,e=reduce((-al[0],-al[1]),(-be[0],-be[1])); P[j,k]=np.exp(2j*np.pi*e/L)
D=np.load('../../order3/data/parts.npz'); X=np.load('../data/k1t1_arrays.npz')
n=np.linalg.norm; ev=lambda A:0.5*(A+A@P.T); od=lambda A:0.5*(A-A@P.T)
r={k:float(n(v)) for k,v in dict(A1=D['A1'],LN=X['LN'],PO=X['PO'],evenPO=ev(X['PO']),evenA1=ev(D['A1']),oddA1=od(D['A1']),evenA1mLN=ev(D['A1']-X['LN']),D=D['D'],evenD=ev(D['D']),oddD=od(D['D']),A0=D['A0'],oddA0=od(D['A0'])).items()}
print(r); import json; json.dump(r,open('../data/diag_posthoc.json','w'),indent=1)
