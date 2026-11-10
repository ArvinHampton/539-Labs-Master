# Audit of OWNER_WRITE_THETA_P_PI_FAST_PIPELINE_V3 (88410ea5...). Read-only. No CERT.
import sympy as sp, numpy as np, itertools
from sympy.ntheory import jacobi_symbol, legendre_symbol
from sympy.functions.combinatorial.numbers import kronecker_symbol as kr
P=list(sp.primerange(2,400))
print("== F1 epsilon ==")
print("odd p<400 with (35/p)!=(140/p):",[p for p in P if p>2 and kr(35,p)!=kr(140,p)])
print("p=2: (35/2)=",kr(35,2),"(140/2)=",kr(140,2))
# 'mod 35' reading: table keyed by p mod 35
bad=[(p,q) for p in P for q in P if p<q and p%35==q%35 and kr(140,p)!=kr(140,q)]
print("pairs p≡q mod35 with different (140/.) (first 8):",bad[:8])
print("37 vs 2: (140/37)=",kr(140,37)," (140/2)=",kr(140,2)," (35/2)=",kr(35,2))
print("periodic mod 140 check:",all(kr(140,p)==kr(140,q) for p in P for q in P if p%140==q%140 and p>7 and q>7))
print("reversed Jacobi (p/35) != (35/p) for p<100:",[p for p in P if p>7 and p<100 and jacobi_symbol(p,35)!=kr(35,p)])
print("== F2 Theta in M2(T) ==")
T1,T2,a,b=sp.symbols('T1 T2 pi1 pi2',commutative=True)
M=lambda T,pi: sp.Matrix([[0,T],[pi*T,0]])
C=M(T1,a)*M(T2,b)-M(T2,b)*M(T1,a); print("[M_p,M_q]=",sp.simplify(C))
print("M^2=",M(T1,a)**2," eigenvalues:",M(T1,a).eigenvals())
print("== F3 pi_p in Q3 ==")
for p in [2,3,5,7,11,13,37]:
    print(p,"(140/p)=",kr(140,p),"v_3(p)=",sp.multiplicity(3,p),"35 square mod 3?",legendre_symbol(35%3,3)==1 if 35%3 else None)
print("== F4 U_t unitarity (Λ=diag(1,-1), and qutrit diag(1,0,-1)) ==")
for Lam in (np.diag([1,-1]),np.diag([1,0,-1])):
  for M_ in (3,):
    z=np.exp(2j*np.pi/M_)
    for t in range(M_):
        c=z**t-1; U=np.diag(np.exp(1j*c*np.diag(Lam)))
        print("M",M_,"t",t,"c=",np.round(c,4),"||UU*-I||=",round(np.linalg.norm(U@U.conj().T-np.eye(len(U))),6))
print("== F5 trace of Pi_fast ==")
def ad(X):
    n=len(X); I=np.eye(n); return np.kron(X,I)-np.kron(I,X.T)
def Ad(U): return np.kron(U,np.linalg.inv(U).T)
for n,Lam in [(2,np.diag([1,-1])),(3,np.diag([1,0,-1])),(16,np.diag([1]*8+[-1]*8))]:
  for M_ in (3,5):
    z=np.exp(2j*np.pi/M_); I=np.eye(n*n)
    avgad=sum(ad((z**t-1)*Lam) for t in range(M_))/M_
    P1=sum((I-avgad)@ad((z**t-1)*Lam) for t in range(M_))/M_  # (Id-avg)∘ad, discrete
    P2=sum(Ad(np.diag(np.exp(1j*(z**t-1)*np.diag(Lam)))) for t in range(M_))/M_  # conjugation average
    print(f"n={n} M={M_} Tr[(Id-avg)ad]={np.round(np.trace(P1),6)} Tr[conj avg]={np.round(np.trace(P2),4)} idem? {np.allclose(P2@P2,P2)}")
print("Tr of projector onto commutant of diag(1^a,-1^b) = a^2+b^2; =128 iff (a,b)=(8,8):",[(x,y) for x in range(13) for y in range(x,13) if x*x+y*y==128])
