# PP audit evidence, 2026-11-10 (America/Chicago). Exact checks only; floats not used as grounds.
import sympy as sp, cypari2, itertools
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
from fractions import Fraction as Fr
print("== X1: V9 matrix identity, exact (cancel each entry, is_zero) ==")
N,r,u,v = sp.symbols('N r u v', nonzero=True)
L = sp.Matrix([[1,u/r],[0,1]])*sp.Matrix([[0,-1],[N*r**2,0]])
gam = sp.Matrix([[r,-v],[-N*u,(1+N*u*v)/r]])
R = r*sp.Matrix([[0,-1],[N,0]])*gam*sp.Matrix([[1,v/r],[0,1]])
print("entries cancel(LHS-RHS):", [sp.cancel(sp.together(x)) for x in (L-R)], " all is_zero:", all(sp.cancel(sp.together(x)).is_zero for x in (L-R)))
print("det gamma_u expand:", sp.expand(gam.det()))
# integrality of (1+Nuv)/r and v = chi(-N) chi(u) bookkeeping, for N=19600 and the 11 r
Nn=19600; Ds=[-3,-11,13,-19,-23,29,33,-31,37,-43,41]
ok=True
for D in Ds:
    rr=abs(D)
    for uu in range(1,rr):
        if sp.gcd(uu,rr)!=1: continue
        vv=(-pow(Nn*uu,-1,rr))%rr
        ok &= ((1+Nn*uu*vv)%rr==0) and (int(pari.kronecker(D,vv))==int(pari.kronecker(D,-Nn))*int(pari.kronecker(D,uu)))
print("V9 bookkeeping (integral gamma_u entry; chi(v)=chi(-N)chi(u)) for N=19600, 11 r:", ok)
print("== X2: primitive Gauss-sum identity sum_u chi(u)e(nu/r) = chi(n) g(chi), exact in Q(zeta_r), all n mod r, 11 r ==")
ok=True
for D in Ds:
    rr=abs(D); z=pari('Mod(x,polcyclo(%d))'%rr)
    g=sum(int(pari.kronecker(D,uu))*z**uu for uu in range(rr))
    for n in range(rr):
        lhs=sum(int(pari.kronecker(D,uu))*z**((n*uu)%rr) for uu in range(rr))
        ok &= (lhs - int(pari.kronecker(D,n))*g)==0
print("all match:", ok)
print("== X3: exact Milgram for D(N2): sum e(q) = G(chi140) (= sqrt140) in Q(zeta_280) ==")
N2=sp.Matrix([[2,14],[14,28]]); Gi=N2.inv(); qs={}
for a in range(140):
  for b in range(140):
    w=Gi*sp.Matrix([a,b]); key=(w[0]%1,w[1]%1)
    if key in qs: continue
    qs[key]=sp.Rational(1,2)*(w.T*N2*w)[0] % 1
print("#D(N2) =",len(qs)," denominators of q:", sorted(set(sp.fraction(q)[1] for q in qs.values())))
M=280; z=pari('Mod(x,polcyclo(%d))'%M)
S=sum(z**int(q*M) for q in qs.values())
G=sum(int(pari.kronecker(140,n))*z**(2*n) for n in range(140))  # zeta_140 = zeta_280^2
print("S - G == 0:", (S-G)==0, "  G^2 == 140:", (G**2-140)==0, " => e(sig/8)=1 exactly, sig(N2)=0 consistent")
print("== X4: even unimodular summands, exact ==")
E8=sp.Matrix([[2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,-1],[0,0,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,0],[0,0,0,0,-1,2,-1,0],[0,0,0,0,0,-1,2,0],[0,0,-1,0,0,0,0,2]])
H=sp.Matrix([[0,1],[1,0]])
for name,U in [("E8",E8),("II11",H)]:
    print(name,"det",U.det(),"even diag",all(U[i,i]%2==0 for i in range(U.shape[0])),"inverse integral",all(x.is_integer for x in U.inv()), "sig", sum(1 for e,m in U.eigenvals().items() for _ in range(m) if sp.N(e)>0)-sum(1 for e,m in U.eigenvals().items() for _ in range(m) if sp.N(e)<0))
L=sp.diag(N2,E8); Li=L.inv()
# dual of N2+E8 = N2' + E8 : check Li block-diagonal with E8 block integral
print("(N2+E8)^-1 block diag, E8 block integral:", Li[:2,2:].is_zero_matrix and Li[2:,:2].is_zero_matrix and all(x.is_integer for x in Li[2:,2:]), " |det| =", abs(L.det()))
print("== X5: L2 instances, PARI exact ==")
E=pari.ellinit([1,-1,0,-2,-1]); Xi=pari.ellinit(pari.elltwist(E,140))
print("Xi: cond",pari.ellglobalred(Xi)[0]," eps",pari.ellrootno(Xi))
for D in Ds:
    T=pari.ellinit(pari.elltwist(Xi,D)); cond=pari.ellglobalred(T)[0]; eps=int(pari.ellrootno(T))
    ap_ok=all(int(pari.ellap(T,p))==int(pari.kronecker(D,p))*int(pari.ellap(Xi,p)) for p in pari.primes(400) if 19600*D*D % int(p)!=0)
    print(f"D={D:4d} cond==19600D^2:{cond==19600*D*D} eps={eps:+d} -eps={-eps:+d} chi_D(-1)={int(pari.kronecker(D,-1)):+d} match={-eps==int(pari.kronecker(D,-1))} a_p twist law p<400 good: {ap_ok}")
