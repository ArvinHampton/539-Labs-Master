# Local-derived (t4436, branches H-1/H-2/H-3, O5-1/O5-2/O5-3). Exact sympy fibre algebra + one numerical illustration.
import sympy as sp, itertools, numpy as np
I=sp.I
s0=sp.eye(2); sx=sp.Matrix([[0,1],[1,0]]); sy=sp.Matrix([[0,-I],[I,0]]); sz=sp.Matrix([[1,0],[0,-1]])
Pl=[s0,sx,sy,sz]
kron=lambda A,B: sp.kronecker_product(A,B)
eta=sp.diag(1,-1,-1,-1)
def cliff_ok(G): return all(sp.simplify(G[a]*G[b]+G[b]*G[a]-2*eta[a,b]*sp.eye(4))==sp.zeros(4) for a in range(4) for b in range(4))
# Majorana rep: exhaustive search over purely imaginary Pauli products (as c4b, now exact)
cands=[]
for i in range(4):
    for j in range(4):
        for c in (1,I):
            M=c*kron(Pl[i],Pl[j])
            if all(sp.re(x)==0 for x in M): cands.append(M)
maj=None
for G in itertools.permutations(cands,4):
    if cliff_ok(list(G)): maj=list(G); break
dirac=[kron(sz,s0)]+[kron(I*sy,Pl[k]) for k in (1,2,3)]
print("exact Clifford: Majorana", cliff_ok(maj), ", Dirac", cliff_ok(dirac), "; Majorana purely imaginary:", all(sp.re(x)==0 for M in maj for x in M))
p1,p2,p3,m,V=sp.symbols('p1 p2 p3 m V',real=True)
def fibre(G,mass):
    g0=G[0]; al=[g0*g for g in G[1:]]
    return g0, al, al[0]*p1+al[1]*p2+al[2]*p3+mass*g0
# A = gamma0 K Pi.  On the momentum fibre (K and Pi both send p -> -p, so A preserves p): H(p) -> g0 conj(H(p)) g0^-1.
# On a multiplication operator M(x): M(x) -> g0 conj(M(-x)) g0^-1; for an EVEN M we may drop the x -> -x.
for name,G in [("Majorana",maj),("Dirac",dirac)]:
    g0,al,H=fibre(G,m)
    Ad=lambda X: sp.simplify(g0*X.conjugate()*g0.inv())
    print(f"[{name}] A H_D(m) A^-1 + H_D(m) = 0 : {sp.simplify(Ad(H)+H)==sp.zeros(4)}")
    H0=fibre(G,0)[2]
    print(f"[{name}] m=0 (O5-2): A H_D(0) A^-1 + H_D(0) = 0 : {sp.simplify(Ad(H0)+H0)==sp.zeros(4)}")
    print(f"[{name}] scalar even V (O5-3a): A V A^-1 = +V : {sp.simplify(Ad(V*sp.eye(4))-V*sp.eye(4))==sp.zeros(4)}  -> A(H_D+V)A^-1 = -H_D + V")
    print(f"[{name}] beta-type even V (O5-3b): A (beta V) A^-1 = -(beta V) : {sp.simplify(Ad(V*g0)+V*g0)==sp.zeros(4)}")
    print(f"[{name}] => A(H_D + beta V)A^-1 = -(H_D + beta V) : {sp.simplify(Ad(H+V*g0)+H+V*g0)==sp.zeros(4)}")
    print(f"[{name}] gamma0 conj(gamma0) =", sp.simplify(g0*g0.conjugate())[0,0], "(times identity)")
# H^2 cross term for H = alpha.p + beta M(x): {alpha_k p_k, beta M} = -i alpha_k beta (d_k M): check alpha_k beta = -beta alpha_k exactly
g0,al,_=fibre(maj,m)
print("alpha_k beta + beta alpha_k = 0 for k=1,2,3 :", all(sp.simplify(a*g0+g0*a)==sp.zeros(4) for a in al))
# H-2: any antiunitary C = U K on C^n with C^2 = +1 is unitarily conjugate to K (Takagi): illustration n=35 with a random symmetric unitary U
rng=np.random.default_rng(7); n=35
X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); Q,_=np.linalg.qr(X); U=Q@Q.T          # symmetric unitary (U = Q Q^T)
print("H-2 illustration: U symmetric unitary:", np.abs(U-U.T).max()<1e-12, np.abs(U@U.conj().T-np.eye(n)).max()<1e-12,
      "; C^2 = U conj(U) = 1 err", np.abs(U@U.conj()-np.eye(n)).max(), "; C = W K W^-1 with W = Q: Q conj(Q)^-1 = U err", np.abs(Q@np.linalg.inv(Q.conj())-U).max())
# H-2 / H-3: antiunitary with square -1 needs even dimension: det(V Vbar) = |det V|^2 > 0 vs det(-1_n) = (-1)^n
print("odd-n obstruction: det(-1_35) =", (-1)**35, "< 0 <= |det V|^2")
