# Local-derived evidence, 2026-11-10 (America/Chicago). Pure arithmetic; no physics input.
import sympy as sp, itertools, cmath
from fractions import Fraction as Fr
import cypari2; pari = cypari2.Pari()

print("== H1: discriminant form / Weil rep of N2 vs N2+E8 vs N2+Leech-rank stand-in ==")
N2 = sp.Matrix([[2,14],[14,28]])
E8 = sp.Matrix([[2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,-1],[0,0,-1,2,-1,0,0,0],
                [0,0,0,-1,2,-1,0,0],[0,0,0,0,-1,2,-1,0],[0,0,0,0,0,-1,2,0],[0,0,-1,0,0,0,0,2]])
print("det E8 =", E8.det(), " even:", all(E8[i,i]%2==0 for i in range(8)),
      " posdef:", all(E8[:k,:k].det()>0 for k in range(1,9)))
def disc_form(G):
    n=G.shape[0]; Gi=G.inv(); d=abs(G.det())
    # enumerate L'/L via representatives Gi*v, v in Z^n / G Z^n : use Smith form through pari
    M=pari.matrix(n,n,[int(x) for x in G]); D,U,V = pari.matsnf(M,1)
    return d
print("|D(N2)| =", abs(N2.det()), " |D(N2+E8)| =", abs(sp.diag(N2,E8).det()))
# q on D(N2): generators of N2'/N2
Gi=N2.inv()
reps=set(); vals={}
for a in range(140):
  for b in range(140):
    v=Gi*sp.Matrix([a,b]); key=(v[0]%1, v[1]%1)
    if key in vals: continue
    q=(sp.Rational(1,2)*(v.T*N2*v)[0])%1; vals[key]=q
print("#N2'/N2 =", len(vals))
# For N2+E8: dual = N2' + E8 (E8 unimodular), q(x+y)=q(x)+q(y), q(E8)⊂Z  => same (D,q)
# Verify E8 even & unimodular gives q(y) in Z on E8 = E8': exact since E8'=E8 (det 1) and even.
G=sum(cmath.exp(2j*cmath.pi*float(q)) for q in vals.values())/140**0.5
print("Milgram N2: sum e(q)/sqrt|D| =", complex(round(G.real,12),round(G.imag,12)), " => sig mod 8 = 0; sig(N2)=(1,1)->0, sig(N2+E8)=(9,1)->8≡0, N2+Leech (25,1)->24≡0")
ev=N2.eigenvals(); print("N2 eigen signs:", [sp.sign(sp.N(k)) for k in ev])

print("== H2: V9 matrix identity, symbolic ==")
N,r,u,v=sp.symbols('N r u v')
L=sp.Matrix([[1,u/r],[0,1]])*sp.Matrix([[0,-1],[N*r**2,0]])
gam=sp.Matrix([[r,-v],[-N*u,(1+N*u*v)/r]])
R=r*sp.Matrix([[0,-1],[N,0]])*gam*sp.Matrix([[1,v/r],[0,1]])
print("LHS-RHS =", sp.simplify(L-R).tolist(), " det(gamma_u) =", sp.simplify(gam.det()))

print("== H3: further quadratic twists of Xi: w19600*r^2 predicted = chi_D(-19600)*(+1) = chi_D(-1) ==")
E=pari.ellinit([1,-1,0,-2,-1]); Xi=pari.ellinit(pari.elltwist(E,140))
print("Xi cond", pari.ellglobalred(Xi)[0], " rootno", pari.ellrootno(Xi), " w=-eps =", -pari.ellrootno(Xi))
for D in [-3,5,-11,13,-19,-23,29,33,-31,37,-43,41]:
    if pari.gcd(D,140)!=1: continue
    T=pari.ellinit(pari.elltwist(Xi,D)); Nn=pari.ellglobalred(T)[0]; eps=int(pari.ellrootno(T))
    pred_w = int(pari.kronecker(D,-1))*int(pari.kronecker(D,19600))  # chi_D(-19600)
    print(f"D={D:4d} cond={Nn} (=19600*D^2? {Nn==19600*D*D})  eps={eps:+d}  w=-eps={-eps:+d}  predicted w={pred_w:+d}  match={-eps==pred_w}")

print("== H4: chi140 dictionary facts (independent re-check) ==")
chi=lambda n:int(pari.kronecker(140,n)); m20=lambda n:int(pari.kronecker(-20,n)); m7=lambda n:int(pari.kronecker(-7,n))
print("chi140 = chi-20*chi-7 on 1..140:", all(chi(n)==m20(n)*m7(n) for n in range(1,141)), " chi140(-1) =", chi(-1))
print("chi140(4880) =", chi(4880), " chi140(9760) =", chi(9760), "  gcd(4880,140) =", pari.gcd(4880,140), " (only listed to show the charge integers are not coprime to 140; no dictionary uses them)")
