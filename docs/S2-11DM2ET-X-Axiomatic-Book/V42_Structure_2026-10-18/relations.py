# Explicit generators of the 98-dim relations kernel: zero labels + proportional pairs (u_b = c u_a); R-symmetry; P-relations.
import sys, pickle, numpy as np
sys.path.insert(0,'.'); from family import Smatrix, LABELS, reduce, D
S=Smatrix(); P=S@S; N=140; I=np.eye(N)
r=pickle.load(open("rel.pkl","rb")); prop,zero=r['prop'],r['zero']
Rel=[I[i] for i in zero]+[I[b]-c*I[a] for a,b,c in prop]; Rel=np.array(Rel)
out=[f"zero labels: {zero} -> alpha*70 = {[LABELS[i][0] for i in zero]}, beta = {[LABELS[i][1] for i in zero]}",
     f"rank(zero + pair relations) = {np.linalg.matrix_rank(Rel,1e-8)} (kernel dim 98)"]
Rm=np.array([[1,7],[0,-1]]); M=np.zeros((N,N),complex)
for i,(al,be) in enumerate(LABELS):
    j,ph=reduce((Rm@np.array(al))%D,Rm@np.array(be)); M[j,i]=ph
Pt=np.array([I[i]-P.T[:,i]*0 for i in range(N)])
relP=(I-P); relR=(I-M.T)
out.append(f"rank P-relations (I-P) = {np.linalg.matrix_rank(relP,1e-8)}, rank R-relations (I-M_R^T) = {np.linalg.matrix_rank(relR,1e-8)}, rank P+R = {np.linalg.matrix_rank(np.vstack([relP,relR]),1e-8)}, rank P+R+zero = {np.linalg.matrix_rank(np.vstack([relP,relR]+[I[i][None] for i in zero]),1e-8)}")
# orbits of labels under the pair relations
par=list(range(N))
def f(x):
    while par[x]!=x: x=par[x]
    return x
for a,b,_ in prop: par[f(b)]=f(a)
from collections import Counter
cls=Counter(f(i) for i in range(N) if i not in zero); out.append(f"nonzero labels fall into {len(cls)} proportionality classes, sizes {sorted(Counter(cls.values()).items())}")
print("\n".join(out)); open("relations.txt","w").write("\n".join(out)+"\n")
