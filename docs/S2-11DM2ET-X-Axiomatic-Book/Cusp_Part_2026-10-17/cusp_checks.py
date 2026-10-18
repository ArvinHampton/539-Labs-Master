import numpy as np, pickle, math, uvec
from collections import defaultdict
from uvec import vectors
from family import LABELS
_o=uvec.cone_pts; uvec.cone_pts=lambda a,b,r1,r2,s,Q,Bx=40:_o(a,b,r1,r2,s,Q,Bx=420)
d=pickle.load(open("fitF.pkl","rb")); pc=d['per_comp']
C=sorted({i for i,rec in pc.items() for s,r in rec.items() if r and r['cusp']>1e-12})
E=[i for i in range(140) if i not in C]
out=[]
mx=0; tot=0
for i in C:
    al,be=LABELS[i]; q,ph,c=vectors(al,be,Qmax=200)
    N=np.rint(19600*np.abs(q)).astype(np.int64); coef=defaultdict(complex)
    for n,v,s in zip(N,ph,np.sign(q)): coef[(int(n),int(s))]+=v
    for (n,s),v in coef.items():
        assert n%140==0
        if math.gcd(n//140,70)>1: mx=max(mx,abs(v)); tot+=1
out.append(f"cusp components: max |coefficient| at N(beta)/140 not coprime to 70 = {mx:.1e} over {tot} frequencies (=> chi(a)=0 convention exact; all coefficients are ideal sums twisted by the conductor-(2 sqrt35) characters)")
S=np.load("../2026-10-17-psi-conditions/S_matrix.npy"); T=np.load("../2026-10-17-psi-conditions/T_matrix.npy")
for nm,Mx in (("S",S),("T",T)):
    out.append(f"{nm}: max|{nm}[cusp,Eis]| = {np.abs(Mx[np.ix_(C,E)]).max():.1e}, max|{nm}[Eis,cusp]| = {np.abs(Mx[np.ix_(E,C)]).max():.1e}")
P=S@S; Pi=(np.eye(140)+P)/2
out.append(f"dim of cusp part of the 72-dim P-invariant representation = rank(Pi[cusp rows]) = {np.linalg.matrix_rank(Pi[C],1e-9)}; Eisenstein part = {np.linalg.matrix_rank(Pi[E],1e-9)}")
open("cusp_checks.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
json_out={"cusp_components":C}
