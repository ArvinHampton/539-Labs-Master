# A33: naive local-reflection sector norms of the 35-vectors K1..K4 (labels as A32) and naive Phi(g) with A32 X_chi3 (Cat B, float).
import numpy as np, json
from law import *
from module import refl
Z5,Z7=refl(5),refl(7); X=np.load(A32+'X_chi3.npy'); I=np.eye(35)
P={(s5,s7):(I+s5*Z5)@(I+s7*Z7)/4 for s5 in (1,-1) for s7 in (1,-1)}
out={}
for c in CANDS:
    g=np.load(f'g_{c}.npy')             # rows: xs from law.py
    out[c]={f"Z5={k[0]:+d},Z7={k[1]:+d}":float(np.abs(g@Pm.T).max()) for k,Pm in P.items()}
    out[c]['max|Phi g|']=float(np.abs(g@X.T).max()); out[c]['max|g|']=float(np.abs(g).max())
    out[c]['mu->-mu even defect']=float(np.abs(g-g@(Z5@Z7).T).max())
print(json.dumps(out,indent=1)); json.dump(out,open('sectors.json','w'),indent=1)
