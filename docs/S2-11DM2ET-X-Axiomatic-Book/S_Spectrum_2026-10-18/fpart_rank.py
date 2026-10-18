# Step 1(b) (partial): rank of the label vectors of positive-/negative-frequency Fourier data separately.
import sys, numpy as np
from collections import defaultdict
sys.path.insert(0,"../2026-10-17-cusp-part"); import uvec
from family import LABELS, Smatrix
cols=defaultdict(lambda: np.zeros(140,complex))
for i,(al,be) in enumerate(LABELS):
    q,ph,c=uvec.vectors(al,be,Qmax=60)
    for qq,p in zip(np.rint(19600*q).astype(np.int64),ph): cols[int(qq)][i]+=p
pos=np.array([v for k,v in cols.items() if k>0]).T; neg=np.array([v for k,v in cols.items() if k<0]).T
r=lambda M: np.linalg.matrix_rank(M,1e-8*np.linalg.norm(M,2))
out=[f"rank C(q>0) = {r(pos)}, rank C(q<0) = {r(neg)}, rank [C(q>0) C(q<0)] = {r(np.hstack([pos,neg]))}",
     "If f_{al,be} := positive-frequency part of u_{al,be}, its label span lies in V (dim 42) and cannot supply the missing 30 dims."]
print("\n".join(out)); open("fpart_rank.txt","w").write("\n".join(out)+"\n")
