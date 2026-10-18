# Dump the 140 labels and the S, T matrices; sanity check that the (a,0) row reproduces the old psi (Phi = 2 psi).
import numpy as np, math, json
from fractions import Fraction as Fr
import family as F
from kappa_all import allcoef
M=F.Smatrix(); T=F.Tmatrix()
np.save("S_matrix.npy",M); np.save("T_matrix.npy",T)
with open("labels.txt","w") as fh:
    fh.write("# index : alpha (x70)  beta (x70)\n")
    for i,(al,be) in enumerate(F.LABELS): fh.write(f"{i:3d} : {al} {be}\n")
i0=F.IDX[((49,56),(0,0))]
cx=allcoef(Fr(1)); cs=allcoef(Fr(-1))
Phi=cs[:,2]-(M@cx[:,2])
lines=[f"(a,0) row index {i0}: Phi(1)/2 = {Phi[i0]/2:.13f}   (old psi(1) = 0.0068839937604-0.0382597122170j)",
       f"row (a,0) of S has {np.count_nonzero(np.abs(M[i0])>1e-12)} nonzero entries, all of modulus {np.unique(np.round(np.abs(M[i0][np.abs(M[i0])>1e-12]),12))}",
       f"S entries: modulus 1/sqrt35 = {1/math.sqrt(35):.12f}; nonzeros per row: {sorted(set(np.count_nonzero(np.abs(M)>1e-12,axis=1)))}",
       f"T is monomial: nonzeros per row {sorted(set(np.count_nonzero(np.abs(T)>1e-12,axis=1)))}"]
print("\n".join(lines)); open("dump_matrices.txt","w").write("\n".join(lines)+"\n")
