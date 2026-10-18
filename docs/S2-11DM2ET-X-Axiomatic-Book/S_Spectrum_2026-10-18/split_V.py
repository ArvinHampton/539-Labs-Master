# Function space V = span of values u(w) in C^140 = column space of the Fourier coefficient matrix C (labels x modes).
import sys, numpy as np, pickle
from collections import defaultdict
CP="../2026-10-17-cusp-part"; sys.path.insert(0,CP); sys.path.insert(0,'.')
from family import Smatrix,Tmatrix,LABELS
import uvec
S=Smatrix(); T=Tmatrix(); I=np.eye(140); out=[]
cols=defaultdict(lambda: np.zeros(140,complex))
for i,(al,be) in enumerate(LABELS):
    q,ph,c=uvec.vectors(al,be,Qmax=int(sys.argv[1]) if len(sys.argv)>1 else 25)
    cols['const'][i]+=c
    for qq,p in zip(np.rint(19600*q).astype(np.int64),ph): cols[int(qq)][i]+=p
C=np.array(list(cols.values())).T; out.append(f"C: 140 x {C.shape[1]} modes")
def basis(M,tol=1e-8):
    U,s,_=np.linalg.svd(M,full_matrices=False); r=int((s>tol*s[0]).sum()); return U[:,:r],s
V,s=basis(C); out.append(f"dim V = rank C = {V.shape[1]} (sv gap {s[V.shape[1]-1]:.2e} -> {s[V.shape[1]]:.2e})")
K,_=basis(np.eye(140)-V@V.conj().T)   # relations kernel = V^perp (x with x^T C=0, up to conj)
Kr=np.linalg.svd(C.T)[2][V.shape[1]:].conj().T # exact left kernel of C: x^T C = 0
def inv(M,W): R=np.linalg.pinv(W)@M@W; return R, abs(M@W-W@R).max()
out.append(f"relations kernel (dim {Kr.shape[1]}): S^T-invariance resid {inv(S.T,Kr)[1]:.1e}, T^T {inv(T.T,Kr)[1]:.1e}")
out.append(f"V itself: S-inv resid {inv(S,V)[1]:.1e}, T-inv {inv(T,V)[1]:.1e}")
P=S@S; out.append(f"V vs Fix(P): |PV-V| = {abs(P@V-V).max():.1e}  (V subset of Fix(P))")
pc=pickle.load(open(f"{CP}/fitF.pkl","rb"))['per_comp']
Cu=sorted({i for i,r in pc.items() for x in r.values() if x and x['cusp']>1e-12}); E=[i for i in range(140) if i not in Cu]
out.append(f"pure-cusp labels: {len(Cu)}, max Eis content on them {max(x['eis'] for i in Cu for x in pc[i].values() if x):.1e}; max cusp content on others {max(x['cusp'] for i in E for x in pc[i].values() if x):.1e}")
parts={}
for nm,rows in (("Eis",E),("cusp",Cu)):
    Cp=np.zeros_like(C); Cp[rows]=C[rows]   # character projection = row restriction (components are pure)
    W,_=basis(Cp); R,eS=inv(S,W); R2,eT=inv(T,W)
    t=np.trace(R); d=W.shape[1]; parts[nm]=(W,R,R2)
    ev=np.linalg.eigvals(R2); r=np.rint(np.angle(ev)/(2*np.pi)*840)%840
    from fractions import Fraction as F; from collections import Counter
    cnt=Counter(F(int(x),840) for x in r)
    out.append(f"{nm}: dim {d}, inside V resid {abs(V@V.conj().T@W-W).max():.1e}; S-inv resid {eS:.1e}, T-inv {eT:.1e}; |R_S^2-I|={abs(R@R-np.eye(d)).max():.1e}; tr S={t.real:.12f}{t.imag:+.0e}i -> n+={round((d+t.real)/2)}, n-={round((d-t.real)/2)}")
    out.append(f"  T spectrum e(r) r:mult: "+", ".join(f"{k}:{m}" for k,m in sorted(cnt.items())))
W=np.hstack([parts['Eis'][0],parts['cusp'][0]]); out.append(f"Eis+cusp rank = {np.linalg.matrix_rank(W,1e-8)}")
print("\n".join(out)); open("split_V.txt","w").write("\n".join(out)+"\n")
