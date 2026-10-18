# Numerical check of the u-level S- and T-laws on all 140 rows:  u(-1/w) = M u(w),  u(w+1) = T u(w).
import numpy as np, math
import family as F, uvec as U
M=F.Smatrix(); T=F.Tmatrix()
V=[U.vectors(al,be) for al,be in F.LABELS]
out=[]
for w in [complex(0.2,0.9),complex(-0.35,0.95),complex(0.05,1.02)]:
    uw=np.array([U.ueval(v,w) for v in V]); us=np.array([U.ueval(v,-1/w) for v in V])
    out.append(f"S-law w={w}: max_rows |u(-1/w) - M u(w)| = {np.abs(us-M@uw).max():.2e}   (max |u| = {np.abs(uw).max():.2f})")
w=complex(0.3,1.1)
uw=np.array([U.ueval(v,w) for v in V]); ut=np.array([U.ueval(v,w+1) for v in V])
out.append(f"T-law w={w}: max_rows |u(w+1) - T u(w)| = {np.abs(ut-T@uw).max():.2e}")

print("\n".join(out)); open("slaw_check.txt","w").write("\n".join(out)+"\n")
P=np.zeros_like(M)
for i,(al,be) in enumerate(F.LABELS):
    j,ph=F.reduce(-np.array(al),-np.array(be)); P[i,j]+=ph
out2=[f"M unitary: {np.abs(M@M.conj().T-np.eye(len(M))).max():.1e};  T unitary: {np.abs(T@T.conj().T-np.eye(len(M))).max():.1e}",
      f"M^2 = P (nu->-nu): {np.abs(M@M-P).max():.1e};   (M T)^3 = P: {np.abs(np.linalg.matrix_power(M@T,3)-P).max():.1e}",
      f"P u = u on all rows (u_(-al,-be)=u_(al,be)): {np.abs(P@uw-uw).max():.1e}"]
print("\n".join(out2)); open("slaw_check.txt","a").write("\n".join(out2)+"\n")
R3=np.linalg.matrix_power(M@T,3)
Pi=(np.eye(len(M))+P)/2
out3=[f"on the P-invariant subspace (where the u live): |((MT)^3 - I) Pi| = {np.abs((R3-np.eye(len(M)))@Pi).max():.1e};  |(M^2 - I) Pi| = {np.abs((M@M-np.eye(len(M)))@Pi).max():.1e}",
      f"applied to the actual vector u(w): |(MT)^3 u - u| = {np.abs(R3@uw-uw).max():.1e}",
      f"dimension of P-invariant subspace = {int(round(np.trace(Pi).real))}"]
print("\n".join(out3)); open("slaw_check.txt","a").write("\n".join(out3)+"\n")
