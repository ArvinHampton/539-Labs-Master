# v2: fixes the Y-normalisation line of v1 (v1 kept as written). Local-derived evidence, 2026-11-10 (America/Chicago). Light exact arithmetic only.
# B1: Bolza Jac decomposition + j-invariants + explicit sqrt(-2) endomorphism (sympy, exact).
# B2: AL-product constraint bookkeeping; chi_140 values; Gamma0(140) element with d=3.
# B3: Gamma1-only counterexample to weakened JM (trivial check).
import sympy as sp
x,y,t,u,v,X,Y = sp.symbols('x y t u v X Y')
r2 = sp.sqrt(2)
f = x**5 - x
print("== B1 Bolza ==")
m = (x+1)/(x-1)
# s: (x,y) -> (m, 2*sqrt2*y/(x-1)^3)
chk = sp.simplify(sp.together(f.subs(x,m) - 8*f/(x-1)**6))
print("f(m(x)) - 8 f(x)/(x-1)^6 =", chk)
print("m(m(x)) =", sp.simplify(m.subs(x,m)))
ys = 2*r2*y/(x-1)**3
ys2 = sp.simplify((2*r2*ys/(m-1)**3))
print("s^2 on y:", ys2)
# action on differentials dx/y, x dx/y : pullback s^*(g(x)dx/y) = g(m) m' dx / ys
mp = sp.diff(m,x)
for name,g in [("dx/y",1),("x dx/y",x)]:
    pb = sp.simplify(sp.together((g if g==1 else g.subs(x,m))*mp/(2*r2/(x-1)**3)))
    print("s^*(",name,") = (",sp.factor(pb),") dx/y")
# matrix of s^* on basis (1, x) (coefficients of dx/y)
w1 = sp.expand(sp.simplify(1*mp/(2*r2/(x-1)**3)))
w2 = sp.expand(sp.simplify(m*mp/(2*r2/(x-1)**3)))
M = sp.Matrix([[sp.Poly(w1,x).coeff_monomial(1), sp.Poly(w2,x).coeff_monomial(1)],
               [sp.Poly(w1,x).coeff_monomial(x), sp.Poly(w2,x).coeff_monomial(x)]])
M = sp.simplify(M); print("s^* matrix on (dx/y, x dx/y):", M, " eigenvalues:", M.eigenvals())
# coordinate t with s acting as t -> -t
al, be = 1+r2, 1-r2
xt = (al - be*t)/(1 - t)
print("check m(x(t)) = x(-t):", sp.simplify(m.subs(x,xt) - xt.subs(t,-t)))
F = sp.factor(sp.simplify(f.subs(x,xt)*(1-t)**6))
Fp = sp.Poly(sp.expand(F), t)
print("F(t) = f(x(t))(1-t)^6 =", Fp.as_expr())
print("F even in t:", sp.simplify(Fp.as_expr().subs(t,-t) - Fp.as_expr()) == 0)
# lifted s in (t,Y) with y = Y/(1-t)^3 : Y -> c*Y; compute c
Yimg = sp.simplify(ys.subs(x,xt)*(1-(-t))**3 / (y*(1-t)**3))  # v2 fix: Y = y(1-t)^3
print("s on Y: Y ->", sp.simplify(Yimg), "* Y")
G = sp.expand(Fp.as_expr().subs(t, sp.sqrt(u)))
G = sp.Poly(sp.expand(G), u); print("G(u) with Y^2=G(u), u=t^2:", G.as_expr())
def jcubic(P, var):
    P = sp.Poly(sp.expand(P), var); a,b,c,d = [P.coeff_monomial(var**k) for k in (3,2,1,0)]
    a2,a4,a6 = b, a*c, a*a*d   # Y^2 = X^3 + a2 X^2 + a4 X + a6 after X=a*var, Y'=a*Y
    b2,b4,b6 = 4*a2, 2*a4, 4*a6
    b8 = a2*b6/4*4/4 if False else (4*a2*a6 - a4**2)  # a1=a3=0: b8 = 4a2a6 - a4^2
    c4 = b2**2 - 24*b4
    D = -b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6
    return sp.nsimplify(sp.simplify(c4**3/D)), sp.simplify(D)
jp, Dp = jcubic(G.as_expr(), u)
print("E_plus: Y^2 = G(u); j =", jp, " Delta =", Dp)
# E_minus: W = tY, W^2 = u G(u); v = 1/u, W' = W v^2 : W'^2 = v^3 G(1/v)
Hm = sp.expand(sp.simplify(v**3*G.as_expr().subs(u,1/v)))
jm, Dm = jcubic(Hm, v)
print("E_minus: W'^2 =", Hm, "; j =", jm, " Delta =", Dm)
print("== B1b explicit [sqrt(-2)] on E0: y^2 = x^3+4x^2+2x ==")
E0 = lambda X_,Y_: Y_**2 - (X_**3 + 4*X_**2 + 2*X_)
print("j(E0) =", jcubic(x**3+4*x**2+2*x, x)[0])
s2 = sp.sqrt(-2)
phx = -(x**2 + 4*x + 2)/(2*x)
phy = y*(x**2 - 2)/(2*s2*x**2)
on = sp.simplify(sp.together(E0(phx,phy)).subs(y**2, x**3+4*x**2+2*x))
print("phi(P) on E0 (should be 0):", sp.simplify(on))
# phi(phi(P)) vs [-2]P
ppx = sp.simplify(phx.subs(x,phx)); ppy = sp.simplify(phy.subs({x:phx, y:phy}, simultaneous=True))
lam = (3*x**2 + 8*x + 2)/(2*y)
dx = lam**2 - 4 - 2*x; dy = -(y + lam*(dx - x))
ex = sp.simplify(sp.together(ppx - dx).subs(y**2, x**3+4*x**2+2*x))
ey = sp.simplify(sp.together(sp.expand(ppy + dy)))
ey = sp.simplify(sp.together(ey).subs(y**2, x**3+4*x**2+2*x))
print("x(phi^2 P) - x(2P) =", ex)
print("y(phi^2 P) + y(2P) (phi^2 = [-2] iff 0):", sp.simplify(ey))
print("== B2 ==")
from sympy.ntheory import legendre_symbol
from sympy.functions.combinatorial.numbers import jacobi_symbol
def kron(D,n):
    # Kronecker symbol (D/n), n>0 odd or handle 2
    res=1
    while n%2==0:
        n//=2
        if D%2==0: return 0
        res *= 1 if D%8 in (1,7) else -1
    return res*jacobi_symbol(D % n, n) if n>1 else res
print("chi140(3) =", kron(140,3), " chi140(1) = 1;  chi_-7(23) =", kron(-7,23), " chi140(23) =", kron(140,23), " chi_-20(23) =", kron(-20,23))
g = sp.Matrix([[47,1],[140,3]]); print("gamma =",g.tolist()," det =", g.det(), " in Gamma0(140):", g[1,0]%140==0, " d mod 140 =", g[1,1]%140)
print("chi_-7(-1) = -1 (D<0); chi140(-1)=+1; chi_-20(-1)=-1; chi140 = chi_-7 * chi_-20 pointwise check:",
      all(kron(140,n)==kron(-7,n)*kron(-20,n) for n in range(1,2000)))
print("AL product bookkeeping: w16*w25*w49 = w19600 (multiplicativity); PARI eps_p table (-1,+1,-1) product =", (-1)*(1)*(-1))
print("All-three-minus pattern product =", (-1)**3, "!= +1 => 'odd -> -1 on every prime-power W' impossible given w19600=+1")
print("== B3 == Gamma1(140)-only equivariance: J: C e0 -> C (trivial Gamma0 rep), J=id. For gamma in Gamma1(140), d=1 so chi140(d)=1 = trivial: equivariant on Gamma1;")
print("   for gamma=[[47,1],[140,3]]: chi140(3) =", kron(140,3), "!= 1 => not Gamma0-equivariant; image line carries trivial char != chi140.")
