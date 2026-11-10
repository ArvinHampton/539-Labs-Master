"""D5 locus on a slice (Theorem 6.x): parametrisation via the verified sextic resolvent.
With Y = X/alpha, a rational root of R forces  w^2 = 5 (Y^2 - 24 Y + 400)  and  m = 125 k^2 G(Y) / (256 w (Y-4)^2),
G(Y) = Y^3 - 20 Y^2 + 240 Y + 320.  Parametrise the conic through (Y,w)=(4,40): Y = 4 - 80(l+1)/(l^2-5), w = 40 + l (Y-4)."""
import sympy as sp
from fractions import Fraction as Fr
from math import gcd
from common import *
Y, w, l, m, k, X = sp.symbols('Y w l m k X')
G = Y**3 - 20*Y**2 + 240*Y + 320
P0 = Y**6 - 40*Y**5 + 880*Y**4 - 8960*Y**3 + 44800*Y**2 + 153600*Y + 102400
assert sp.expand(P0 - G**2) == 0
assert sp.expand(P0 - 2**18*Y - (Y-4)**4*(Y**2-24*Y+400)) == 0
# 1. resolvent in terms of alpha, k:  R(alpha*Y; alpha, k alpha) = alpha^6 * ( P0(Y) - 1024*(65536 m^2/alpha) * Y ) with alpha = 256 m^2 - 3125 k^4/256
al = 256*m**2 - sp.Rational(3125, 256)*k**4
Rpoly = sp.sympify(open('../data/sextic_resolvent.txt').read().split('expanded:')[1].split('\n')[0].strip().replace('^','**'),
                   locals={'X':X,'a':sp.Symbol('a'),'b':sp.Symbol('b')})
a_, b_ = sp.symbols('a b')
chk = sp.expand(Rpoly.subs({a_: al, b_: k*al}).subs(X, al*Y) - al**6*(P0 - 1024*(65536*m**2/al)*Y))
assert sp.simplify(chk) == 0
print("R(alpha Y) = alpha^6 (P0(Y) - 1024 s Y), s = 65536 m^2/alpha : OK")
# 2. conic parametrisation
Yl = 4 - 80*(l+1)/(l**2-5)
wl = 40 + l*(Yl-4)
assert sp.simplify(wl**2 - 5*(Yl**2-24*Yl+400)) == 0
Ml = sp.simplify(125*G.subs(Y, Yl)/(256*wl*(Yl-4)**2))
Ml = sp.factor(Ml); print("M(l) =", Ml)
num, den = sp.fraction(sp.together(Ml)); print("degree of M(l) as rational function:", max(sp.degree(num,l), sp.degree(den,l)))
# 3. check: for any l, (m,k) = (k^2 M(l), k) gives a quintic whose resolvent has rational root Y(l)
for lv in [Fr(1,2), Fr(2,3), Fr(3), Fr(7,5), Fr(-3,4), Fr(10,3)]:
    for kv in [Fr(-8,5), Fr(1), Fr(4,5)]:
        mv = kv**2 * Fr(str(Ml.subs(l, sp.Rational(lv.numerator, lv.denominator))))
        Yv = Fr(str(Yl.subs(l, sp.Rational(lv.numerator, lv.denominator))))
        s = Fr(65536)*mv*mv/alpha(mv, kv)
        assert P0.subs(Y, sp.Rational(Yv.numerator, Yv.denominator)) - 1024*sp.Rational(s.numerator, s.denominator)*sp.Rational(Yv.numerator, Yv.denominator) == 0
print("parametrised points satisfy R(alpha Y)=0 exactly: OK")
# 4. recover scan D5 fibres: find l with k^2 M(l) = m
for (kv, mv) in [(Fr(-8,5), Fr(5,8)), (Fr(-8,5), Fr(5,9)), (Fr(-4), Fr(7,2))]:
    target = sp.Rational((mv/kv**2).numerator, (mv/kv**2).denominator)
    sols = sp.Poly(sp.numer(sp.together(Ml - target)), l).ground_roots() if True else None
    sols_rat = [r for r in sols if r.is_rational]
    sols_rat += [r for r in sp.Poly(sp.numer(sp.together(Ml + target)), l).ground_roots() if r.is_rational]
    print(f"k={kv}, m={mv}: m/k^2 = {target}; rational l with M(l)=+-m/k^2: {sols_rat}")
