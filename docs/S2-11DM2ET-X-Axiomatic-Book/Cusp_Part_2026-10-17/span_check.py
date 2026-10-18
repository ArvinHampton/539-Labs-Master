# Is every component u_c an SL2(Z)-translate combination of u_L?  If so, u_L,cusp=0 forces u_cusp=0 for ALL 140 components.
import numpy as np, sys
sys.path.insert(0,"../2026-10-17-psi-conditions")
S=np.load("../2026-10-17-psi-conditions/S_matrix.npy"); T=np.load("../2026-10-17-psi-conditions/T_matrix.npy")
labels=open("../2026-10-17-psi-conditions/labels.txt").read().split("\n")
from family import IDX
n=S.shape[0]
P=S@S
w,V=np.linalg.eig(P); inv=np.abs(w-1)<1e-8
# projector onto the P-fixed space (P is a permutation-type matrix of finite order)
Pi=(np.eye(n)+P)/2 if np.allclose(P@P,np.eye(n)) else None
rkPi=np.linalg.matrix_rank(Pi,1e-9)
iL=[i for i,(al,be) in enumerate(__import__("family").LABELS) if (int(al[0])%70,int(al[1])%70)==(49,56) and (int(be[0])%70,int(be[1])%70)==(0,0)][0]
print("P^2=I:",np.allclose(P@P,np.eye(n)),"rank Pi:",rkPi,"index of u_L:",iL)
# Krylov row span of e_L under right mult by S,T
basis=[]; 
def add(v):
    global basis
    M=np.array(basis+[v]); 
    if np.linalg.matrix_rank(M,1e-8)>len(basis): basis.append(v); return True
    return False
e=np.zeros(n,complex); e[iL]=1
queue=[e]; add(e)
while queue:
    v=queue.pop()
    for M in (S,T):
        x=v@M
        if add(x): queue.append(x)
W=np.array(basis)
r1=np.linalg.matrix_rank(W@Pi,1e-8); r2=np.linalg.matrix_rank(np.vstack([W@Pi,Pi]),1e-8)
out=f"Krylov span of e_L: dim {len(basis)}; rank(W Pi)={r1}; rank([W Pi; Pi])={r2}; rank Pi={rkPi}\n=> every component u_c = e_c Pi u lies in span{{u_L o gamma}}: {r1==r2}"
print(out); open("span_check.txt","w").write(out+"\n")
