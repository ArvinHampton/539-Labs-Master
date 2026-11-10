# PP independent exact checks for Local dff4b879 (resolution pass). Professor Proof (PP), Soft SF audit, 2026-11-10 America/Chicago.
# Exact only: sympy expand/rem/Poly with algebraic symbols r (r^2=2), q (q^2=-2); Python ints/Fractions. No float, no nsimplify, no simplify==0, no PARI.
import sympy as sp
from fractions import Fraction as Fr
from itertools import product
x,t,u,v,r,q = sp.symbols('x t u v r q')
P=[0]; F=[]
def chk(name, ok):
    P[0]+=1
    print(("PASS " if ok else "FAIL ")+name)
    if not ok: F.append(name)
def red(e, s=r, m=2):  # reduce a polynomial expression in s modulo s^2 - m, after clearing to numerator
    return sp.expand(sp.rem(sp.expand(e), s**2 - m, s))
def zero_rat(e, s=r, m=2):  # rational function in x,t,... with algebraic s: numerator reduced mod s^2-m must vanish
    n,d = sp.fraction(sp.cancel(sp.together(e)))
    return red(n, s, m) == 0
f = x**5 - x
m = (x+1)/(x-1)
print("== A. Bolza involution s(x,y)=((x+1)/(x-1), 2r*y/(x-1)^3), r^2=2 ==")
chk("A1 f(m(x))*(x-1)^6 - 8 f(x) == 0 (expand)", sp.expand(sp.cancel(f.subs(x,m)*(x-1)**6) - 8*f) == 0)
chk("A2 m(m(x)) == x (cancel)", sp.cancel(m.subs(x,m) - x) == 0)
# y-coefficient c(x) = 2r/(x-1)^3; s^2 on y: c(m(x))*c(x) must be 1
cx = 2*r/(x-1)**3
chk("A3 s^2 = id on y: c(m)*c(x) - 1 == 0 mod r^2-2", zero_rat(cx.subs(x,m)*cx - 1))
chk("A4 s != id and s != iota (m(x) != x)", sp.cancel(m - x) != 0)
# s^*(g dx/y) = g(m) m' /c(x) dx/y
mp = sp.diff(m, x)
w1 = sp.cancel(mp/cx); w2 = sp.cancel(m*mp/cx)
# w1, w2 must be polynomials of degree <= 1 in x (with r); rationalise 1/r = r/2
w1 = sp.expand(sp.cancel(w1*r/r).subs(1/r, r/2)); w2 = sp.expand(sp.cancel(w2).subs(1/r, r/2))
w1 = red(sp.expand(sp.cancel(mp*(x-1)**3)*r/4)); w2 = red(sp.expand(sp.cancel(m*mp*(x-1)**3)*r/4))  # 1/(2r) = r/4
chk("A5 s^*(dx/y) = -(r/2)(x-1) dx/y", sp.expand(w1 - (-(r/2)*(x-1))) == 0)
chk("A6 s^*(x dx/y) = -(r/2)(x+1) dx/y", sp.expand(w2 - (-(r/2)*(x+1))) == 0)
M = sp.Matrix([[sp.Poly(w1,x).coeff_monomial(1), sp.Poly(w2,x).coeff_monomial(1)],[sp.Poly(w1,x).coeff_monomial(x), sp.Poly(w2,x).coeff_monomial(x)]])
M2 = (M*M).applyfunc(lambda e: red(e))
chk("A7 (s^*)^2 = I on H0(Omega^1)", M2 == sp.eye(2))
chk("A8 tr s^* = 0, det s^* = -1 (eigenvalues +1,-1 once each)", red(M.trace())==0 and red(M.det()) == -1)
# eigenvectors: (M - I)v=0 has 1-dim kernel; (M+I) too
chk("A9 rank(M-I)=rank(M+I)=1 (exact, via det=0 and nonzero entry)", red((M-sp.eye(2)).det())==0 and red((M+sp.eye(2)).det())==0 and M[0,1]!=0)
print("== B. t-coordinate, quotient models ==")
al, be = 1+r, 1-r
xt = (al - be*t)/(1 - t)
chk("B1 m(x(t)) - x(-t) == 0 mod r^2-2", zero_rat(m.subs(x,xt) - xt.subs(t,-t)))
chk("B2 x(t) - 1 = r(1+t)/(1-t)", zero_rat(xt - 1 - r*(1+t)/(1-t)))
Fn = red(sp.cancel(sp.together(f.subs(x,xt)*(1-t)**6)))
Fexp = (40-28*r)*t**6 + (-40+20*r)*t**4 + (-40-20*r)*t**2 + (40+28*r)
chk("B3 F(t) = f(x(t))(1-t)^6 equals logged even sextic", sp.expand(Fn - Fexp) == 0)
chk("B4 F even: F(-t)-F(t)==0", sp.expand(Fexp.subs(t,-t) - Fexp) == 0)
# s on Y = y(1-t)^3: Y' = c(x(t)) * y * (1+t)^3 ; ratio Y'/Y = c(x(t))(1+t)^3/(1-t)^3 must be 1
chk("B5 s: Y -> +Y exactly (Y = y(1-t)^3)", zero_rat(cx.subs(x,xt)*(1+t)**3/(1-t)**3 - 1))
chk("B6 v1 diagnostic reproduced: dividing by y/(1-t)^3 instead gives (1-t)^6 (Local's v1 bug description)", zero_rat(cx.subs(x,xt)*(1+t)**3*(1-t)**3 - (1-t)**6))
G = (40-28*r)*u**3 + (-40+20*r)*u**2 + (-40-20*r)*u + (40+28*r)
chk("B7 G(t^2) == F(t)", sp.expand(G.subs(u,t**2) - Fexp) == 0)
Hm = red(sp.expand(sp.cancel(v**3*G.subs(u,1/v))))
chk("B8 E_minus: (uG(u))*v^4 at u=1/v equals v^3 G(1/v), a cubic", zero_rat((1/v)*G.subs(u,1/v)*v**4 - Hm) and sp.Poly(Hm,v).degree()==3)
def ainv(Pc, var):
    Pp = sp.Poly(Pc, var); a,b,c,d = [Pp.coeff_monomial(var**k) for k in (3,2,1,0)]
    return a, (b, a*c, a*a*d)   # Y'^2 = X^3 + b X^2 + ac X + a^2 d with X = a*var, Y' = a*Y
def c4D(a2,a4,a6):
    b2,b4,b6,b8 = 4*a2, 2*a4, 4*a6, 4*a2*a6 - a4**2
    return sp.expand(b2**2 - 24*b4), sp.expand(-b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6)
def normr(e):  # norm Q(r)/Q of e = A + B r
    e = red(e); A = e.subs(r,0); B = sp.expand((e - A)/r); return sp.expand(A**2 - 2*B**2)
for name, Pc, var in [("E_plus", G, u), ("E_minus", Hm, v)]:
    a,(a2,a4,a6) = ainv(Pc, var)
    c4,D = c4D(a2,a4,a6)
    chk("C %s: leading coeff a != 0 (norm %s)" % (name, normr(a)), normr(a) != 0)
    chk("C %s: Delta != 0 (norm over Q = %s)" % (name, normr(D)), normr(D) != 0)
    chk("C %s: c4^3 - 8000*Delta == 0 mod r^2-2  (j = 8000, no nsimplify)" % name, red(c4**3 - 8000*D) == 0)
    print("   %s Delta = %s" % (name, red(D)))
# E0
c40, D0 = c4D(sp.Integer(4), sp.Integer(2), sp.Integer(0))
chk("C E0: c4=160, Delta=512, c4^3 = 8000*Delta", c40==160 and D0==512 and c40**3 == 8000*D0)
print("== D. explicit Qbar-isomorphisms E_pm -> E0 (instance of AEC III.1.4(b), verified, not cited) ==")
def shortAB(a2,a4,a6):
    return sp.expand(a4 - a2**2/3), sp.expand(2*a2**3/27 - a2*a4/3 + a6)
A0,B0 = shortAB(sp.Integer(4),sp.Integer(2),sp.Integer(0))
chk("D0 E0 short form A=-10/3, B=56/27", A0==sp.Rational(-10,3) and B0==sp.Rational(56,27))
for name, Pc, var in [("E_plus", G, u), ("E_minus", Hm, v)]:
    a,(a2,a4,a6) = ainv(Pc, var); A1,B1 = shortAB(a2,a4,a6)
    chk("D %s: A,B nonzero (norms)" % name, normr(A1)!=0 and normr(B1)!=0)
    chk("D %s: B1^2*A0^3 - B0^2*A1^3 == 0 (iso condition)" % name, red(B1**2*A0**3 - B0**2*A1**3) == 0)
    # lam = mu^2 = (B1/B0)/(A1/A0); then lam^2 = A1/A0 and lam^3 = B1/B0 exactly => (X,Y) -> (X/lam, Y/mu^3) maps E_pm(short) to E0(short) over Q(r, mu)
    lam_num = red(B1*A0); lam_den = red(B0*A1)
    chk("D %s: lam^2 = A1/A0  <=>  (B1 A0)^2 A0 - A1 (B0 A1)^2 == 0" % name, red(lam_num**2*A0 - A1*lam_den**2) == 0)
    chk("D %s: lam^3 = B1/B0  <=>  (B1 A0)^3 B0 - B1 (B0 A1)^3 == 0" % name, red(lam_num**3*B0 - B1*lam_den**3) == 0)
print("== E. phi on E0: y^2 = g(x) = x^3+4x^2+2x, phi=( -(x^2+4x+2)/(2x), y(x^2-2)/(2 q x^2) ), q^2=-2 ==")
g = lambda X: X**3 + 4*X**2 + 2*X
X1 = -(x**2+4*x+2)/(2*x)
# phy^2 = y^2 (x^2-2)^2/(4 q^2 x^4) = -g(x)(x^2-2)^2/(8 x^4)
chk("E1 phi maps E0 to E0: -g(x)(x^2-2)^2/(8x^4) - g(X1) == 0 (cancel, pure Q(x))", sp.cancel(-g(x)*(x**2-2)**2/(8*x**4) - g(X1)) == 0)
lam2 = (3*x**2+8*x+2)**2/(4*g(x)); x2 = lam2 - 4 - 2*x
chk("E2 x(phi^2 P) == x(2P) (cancel)", sp.cancel(X1.subs(x,X1) - x2) == 0)
# y(phi^2 P)/y = (x^2-2)(X1^2-2)/((2q)^2 x^2 X1^2) = -(x^2-2)(X1^2-2)/(8 x^2 X1^2);  y(2P)/y = -(1 + (3x^2+8x+2)(x2-x)/(2g))
yphi2 = -(x**2-2)*(X1**2-2)/(8*x**2*X1**2); y2P = -(1 + (3*x**2+8*x+2)*(x2-x)/(2*g(x)))
chk("E3 y(phi^2 P) == -y(2P), so phi^2 = [-2] (cancel)", sp.cancel(yphi2 + y2P) == 0)
# phi^*(dx/y) = X1'(x) dx / (y (x^2-2)/(2 q x^2)) = -q dx/y  -> under F0-2, phi |-> -sqrt(-2)
d1 = sp.cancel(sp.diff(X1,x)*2*x**2/(x**2-2))   # = phi^*ω/ω divided by q
chk("E4 phi^*(dx/y) = -q dx/y (F0-2 image -sqrt(-2))", d1 == -1)
chk("E5 phi(O)=O: deg num X1 > deg den X1", sp.degree(sp.numer(sp.together(X1)),x) > sp.degree(sp.denom(sp.together(X1)),x))
print("== F. O_{Q(sqrt-7)} inside M_2(Z) (bears on Local R4c claim) ==")
Mo = sp.Matrix([[0,1],[-2,1]]); Ms = sp.Matrix([[0,1],[-7,0]])
chk("F1 Mo^2 - Mo + 2I = 0 (omega=(1+sqrt-7)/2 acts on E0^2 by an integer matrix)", Mo**2 - Mo + 2*sp.eye(2) == sp.zeros(2))
chk("F2 Ms^2 = -7 I", Ms**2 == -7*sp.eye(2))
print("== G. Atkin-Lehner matrix algebra ==")
a,b,c,d,a_,b_,c_,d_,Q,Qp,K = sp.symbols('a b c d a_ b_ c_ d_ Q Qp K', integer=True)
N = Q*Qp*K
W = sp.Matrix([[Q*a,b],[N*c,Q*d]]); Wp = sp.Matrix([[Qp*a_,b_],[N*c_,Qp*d_]])
Pm = W*Wp
chk("G1 (WQ WQ')[0,0] = QQ'(aa' + K b c')", sp.expand(Pm[0,0] - Q*Qp*(a*a_ + K*b*c_))==0)
chk("G2 (WQ WQ')[1,1] = QQ'(dd' + K c b')", sp.expand(Pm[1,1] - Q*Qp*(d*d_ + K*c*b_))==0)
chk("G3 (WQ WQ')[1,0] = N(Q' c a' + Q d c')", sp.expand(Pm[1,0] - N*(Qp*c*a_ + Q*d*c_))==0)
chk("G4 det(WQ WQ') = det WQ * det WQ' (=QQ')", sp.expand(Pm.det() - W.det()*Wp.det())==0)
# Two W_Q matrices differ by Gamma0(N): W1*adj(W2)/Q with N = Q*L
L = sp.symbols('L', integer=True); x1,y1,z1,u1,x2,y2,z2,u2 = sp.symbols('x1 y1 z1 u1 x2 y2 z2 u2', integer=True)
W1 = sp.Matrix([[Q*x1,y1],[Q*L*z1,Q*u1]]); W2 = sp.Matrix([[Q*x2,y2],[Q*L*z2,Q*u2]])
adj2 = sp.Matrix([[Q*u2,-y2],[-Q*L*z2,Q*x2]])
R = (W1*adj2)/Q
R = R.applyfunc(sp.expand)
chk("G5 W1 W2^{-1} entries: [0,0]=Q x1 u2 - L y1 z2, [0,1]=y1 x2 - x1 y2, [1,0]=N(z1 u2 - u1 z2), [1,1]=Q u1 x2 - L z1 y2 (integral, c div by N)",
    sp.expand(R[0,0]-(Q*x1*u2 - L*y1*z2))==0 and sp.expand(R[0,1]-(y1*x2 - x1*y2))==0 and sp.expand(R[1,0]-Q*L*(z1*u2-u1*z2))==0 and sp.expand(R[1,1]-(Q*u1*x2 - L*z1*y2))==0)
# Concrete instance at N = 19600
NN = 19600
def WQ(Qv):
    Mq = NN//Qv
    # Qv*a*d - Mq*b*c = 1 with c=1, d=1: Qv*a - Mq*b = 1
    av = pow(Qv, -1, Mq); bv = (Qv*av - 1)//Mq
    Wm = sp.Matrix([[Qv*av, bv],[NN, Qv]])
    assert Wm.det() == Qv
    return Wm
def isW(Wm, Qv):
    return Wm.det()==Qv and Wm[0,0]%Qv==0 and Wm[1,1]%Qv==0 and Wm[1,0]%NN==0
W16,W25,W49 = WQ(16),WQ(25),WQ(49)
Prod = W16*W25*W49
chk("G6 W16,W25,W49 explicit, each W_Q-shape at N=19600", isW(W16,16) and isW(W25,25) and isW(W49,49))
chk("G7 W16*W25*W49 has W_19600 shape (det 19600)", isW(Prod, NN))
Fr_ = sp.Matrix([[0,-1],[NN,0]])
g_ = Prod*Fr_.inv()
chk("G8 (W16 W25 W49) * Fricke^{-1} in Gamma0(19600): integral, det 1, c = 0 mod N", all(e.is_integer for e in g_) and g_.det()==1 and g_[1,0]%NN==0)
pats = [p for p in product([1,-1],repeat=3) if p[0]*p[1]*p[2]==1]
chk("G9 sign patterns (w16,w25,w49) with product +1: exactly 4", len(pats)==4)
chk("G10 all-minus pattern product = -1", (-1)**3 == -1)
print("== H. Kronecker symbols (own implementation via Euler criterion) ==")
def leg(aa,p):
    aa%=p
    if aa==0: return 0
    return 1 if pow(aa,(p-1)//2,p)==1 else -1
def kron(D,n):
    assert n>0
    res=1
    while n%2==0:
        n//=2
        if D%2==0: return 0
        res *= 1 if D%8 in (1,7) else -1
    pf = sp.factorint(n)
    for p,e in pf.items():
        res *= leg(D,p)**e
    return res
chk("H1 chi140(3) = -1", kron(140,3)==-1)
chk("H2 chi_-7(23)=chi140(23)=chi_-20(23)=+1", kron(-7,23)==1 and kron(140,23)==1 and kron(-20,23)==1)
chk("H3 chi140 = chi_-7 chi_-20 for 1<=n<10000", all(kron(140,n)==kron(-7,n)*kron(-20,n) for n in range(1,10000)))
chk("H4 periodic mod |D| and chi_D(|D|-1) = sign D: chi140(-1)=+1, chi_-20(-1)=-1, chi_-7(-1)=-1",
    all(kron(D,n)==kron(D,n+abs(D)) for D in (140,-20,-7) for n in range(1,400)) and kron(140,139)==1 and kron(-20,19)==-1 and kron(-7,6)==-1)
gm = sp.Matrix([[47,1],[140,3]])
chk("H5 gamma=[[47,1],[140,3]]: det 1, c=0 mod 140, d=3", gm.det()==1 and gm[1,0]%140==0 and gm[1,1]==3)
chk("H6 chi140 is a character on (Z/140)^x: multiplicative on units (all pairs)", all(kron(140,(i*j)%140)==kron(140,i)*kron(140,j) for i in range(1,140) for j in range(1,140) if sp.gcd(i,140)==1 and sp.gcd(j,140)==1))
inv = [dd for dd in range(1,140) if sp.gcd(dd,140)==1 and (dd*dd)%140==1]
neg = [dd for dd in inv if kron(140,dd)==-1]
print("   d with d^2=1 mod 140:", inv, "; of these chi140(d)=-1:", neg)
chk("H7 some d with d^2 = 1 (mod 140) has chi140(d) = -1 (so chi(d)=-1 is compatible with J^2=1 on the e0 line)", len(neg)>0)
# torsion of Gamma0(140): trace 0 needs a^2 = -1 mod 140 (impossible mod 4); trace +-1 needs a^2 -+ a + 1 = 0 mod 140 (impossible mod 2)
chk("H8 no a with a^2 = -1 mod 4; no a with a^2 - a + 1 = 0 or a^2 + a + 1 = 0 mod 2 (Gamma0(140) torsion = {+-I})",
    all((aa*aa+1)%4 != 0 for aa in range(4)) and all((aa*aa-aa+1)%2!=0 and (aa*aa+aa+1)%2!=0 for aa in range(2)))
print("== I. Twist identity R_chi140 f = R_chi-20 f on 49a1 coefficients (corroboration of adopted 2c; n<=3000) ==")
# a_p of 49a1: y^2 + xy = x^3 - x^2 - 2x - 1 ; count points
def ap49(p):
    if p==7: return 0
    cnt=0
    for X in range(p):
        rhs = (X**3 - X**2 - 2*X - 1)
        # y^2 + X y - rhs = 0 -> disc = X^2 + 4 rhs
        if p==2:
            cnt += sum(1 for Y in range(2) if (Y*Y + X*Y - rhs)%2==0)
        else:
            cnt += 1 + leg(X*X + 4*rhs, p)
    return p - cnt
Nmax=3000
primes = list(sp.primerange(2,Nmax+1)); ap = {p:ap49(p) for p in primes}
chk("I1 a_p(49a1)=0 for every p<=3000 with (-7/p)=-1", all(ap[p]==0 for p in primes if kron(-7,p)==-1))
an=[0]*(Nmax+1); an[1]=1
for n in range(2,Nmax+1):
    pf=sp.factorint(n); val=1
    for p,e in pf.items():
        # a_{p^e}: good p: a_{p^{k+1}} = a_p a_{p^k} - p a_{p^{k-1}}; p=7: a_7=0 => 0
        A=[1,ap[p]]
        for k in range(1,e): A.append(ap[p]*A[k] - (0 if p==7 else p)*A[k-1])
        val*=A[e]
    an[n]=val
chk("I2 a_n chi140(n) == a_n chi_-20(n) for all n<=3000", all(an[n]*kron(140,n)==an[n]*kron(-20,n) for n in range(1,Nmax+1)))
print("CHECKS", P[0], "FAIL", len(F), F)
print("ALL_CHECKS PASS (%d)" % P[0] if not F else "SOME_FAIL")
