# POST-HOC (after o26.py verdicts recorded): exact Γ_h for h=[[1,7],[0,-1]] (=−σ), B=hK.
import sys,json; sys.dont_write_bytecode=True
from cornerlib import *
h=[[1,7],[0,-1]]; ident=0; perm=[]
for j,(al,be) in enumerate(pairs):
    ha=tuple(sum(Fr(h[r][c])*al[c] for c in range(2)) for r in range(2)); hb=tuple(sum(Fr(h[r][c])*be[c] for c in range(2)) for r in range(2))
    kk,e=reduce(ha,hb); perm.append(kk); ident+= (kk==j and e%L==0)
out=dict(Gamma_h_identity_entries=ident,of=105,exact_identity=ident==105)
print(out); json.dump(out,open('../data/o26_posthoc.json','w'))
