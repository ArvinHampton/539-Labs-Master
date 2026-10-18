import numpy as np, json, pickle, sys
sys.path.insert(0,'.')
from family import Smatrix, Tmatrix, LABELS
S=Smatrix(); T=Tmatrix(); I=np.eye(140)
S0=np.load("../2026-10-17-psi-conditions/S_matrix.npy"); T0=np.load("../2026-10-17-psi-conditions/T_matrix.npy")
out=[f"rebuild vs stored: |S-S0|={abs(S-S0).max():.1e} |T-T0|={abs(T-T0).max():.1e}"]
P=S@S; out.append(f"|P^2-I|={abs(P@P-I).max():.1e}  |P-(ST)^3|={abs(P-np.linalg.matrix_power(S@T,3)).max():.1e}  |PT-TP|={abs(P@T-T@P).max():.1e}")
Pi=(I+P)/2
U,s,_=np.linalg.svd(Pi); V=U[:,:int((s>1e-8).sum())]; d=V.shape[1]; out.append(f"dim P-fixed = {d}")
def restr(M,W): # W orthonormal invariant (column) subspace
    R=W.conj().T@M@W; return R, abs(M@W-W@R).max()
Sr,eS=restr(S,V); Tr,eT=restr(T,V)
out.append(f"invariance resid S:{eS:.1e} T:{eT:.1e}; |Sr^2-I|={abs(Sr@Sr-np.eye(d)).max():.1e} |(SrTr)^3-I|={abs(np.linalg.matrix_power(Sr@Tr,3)-np.eye(d)).max():.1e}")
tr=np.trace(Sr); out.append(f"tr S|72 = {tr.real:.15f} {tr.imag:+.1e}i ; n+={round((d+tr.real)/2)} n-={round((d-tr.real)/2)}")
out.append(f"eigs S|72 max dist to ±1: {min(abs(np.linalg.eigvals(Sr)-1).max(),max(min(abs(x-1),abs(x+1)) for x in np.linalg.eigvals(Sr))):.1e}")
# Eis/cusp split
pc=pickle.load(open("../2026-10-17-cusp-part/fitF.pkl","rb"))['per_comp']
C=sorted({i for i,rec in pc.items() for s_,r in rec.items() if r and r['cusp']>1e-12}); E=[i for i in range(140) if i not in C]
for nm,rows in (("Eis",E),("cusp",C)):
  for side in ("col","row"):
    M=Pi[:,rows] if side=="col" else Pi[rows].conj().T  # columns=span
    U2,s2,_=np.linalg.svd(M); W=U2[:,:int((s2>1e-8).sum())]
    if side=="col": R,e1=restr(S,W); R2,e2=restr(T,W)
    else: R,e1=restr(S.conj().T,W); R2,e2=restr(T.conj().T,W); R=R.conj().T
    t=np.trace(R).real; out.append(f"{nm} ({side} span) dim {W.shape[1]}: inv resid S {e1:.1e} T {e2:.1e}; tr S={t:.12f} n+={round((W.shape[1]+t)/2)} n-={round((W.shape[1]-t)/2)}")
# T spectrum
ev=np.linalg.eigvals(Tr); k=np.angle(ev)/(2*np.pi)
N=2*3*4*5*7*2; num=np.rint(k*N)%N; out.append(f"T eig angle resid (denominator 840): {abs(k*N-np.rint(k*N)).max():.1e}, |ev|-1 max {abs(abs(ev)-1).max():.1e}")
from fractions import Fraction; from collections import Counter
cnt=Counter(Fraction(int(n),N) for n in num); out.append("T eigenvalues e(r), r: mult = "+", ".join(f"{r}:{m}" for r,m in sorted(cnt.items())))
import math; o=1
for r in cnt: o=o*r.denominator//math.gcd(o,r.denominator)
out.append(f"order of T|72 = {o}; |T^o - I| on 72 = {abs(np.linalg.matrix_power(Tr,o)-np.eye(d)).max():.1e}")
print("\n".join(out)); open("s_eig.txt","w").write("\n".join(out)+"\n")
