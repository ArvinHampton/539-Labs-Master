"""Exact verification of the algebraic statements in the note (sympy + Fraction)."""
import sympy as sp
from fractions import Fraction as Fr
from common import *
x, a, b, m, k, u, t, al = sp.symbols('x a b m k u t alpha')
R = sp.Rational
out = []
def say(s): print(s); out.append(s)

# disc formula
f = x**5 + a*x + b
assert sp.expand(sp.discriminant(f, x) - (256*a**5 + 3125*b**4)) == 0
say("disc(x^5+ax+b) = 256 a^5 + 3125 b^4 : OK")

# (2) equivalence identity
alpha_m = 256*m**2 - R(3125)*k**4/256
assert sp.expand((256*alpha_m + 3125*k**4) - 65536*m**2) == 0
d = (256*a**5+3125*b**4).subs({a: alpha_m, b: k*alpha_m})
assert sp.simplify(d - (256*alpha_m**2*m)**2) == 0
assert sp.expand(sp.discriminant(x**5+al*x+k*al, x) - al**4*(256*al+3125*k**4)) == 0
say("disc(x^5+alpha x+k alpha)=alpha^4(256 alpha+3125 k^4); with alpha=alpha(m,k): disc=(256 alpha^2 m)^2 : OK")
# alpha(m,k) != 0 for all rational (m,k), k!=0 : 65536 m^2 = 3125 k^4  <=> 5 = (256 m/(25 k^2))^2*... irrational
say("alpha(m,k)=0 iff 65536 m^2 = 3125 k^4 iff 5 = (256 m / (25 k^2))^2 -> impossible over Q (k!=0): so alpha(m,k)!=0 always.")
# alpha=0 => disc = 3125 b^4 = 5*(25 b^2)^2 never a square for b != 0
say("alpha=0: disc(x^5+b)=3125 b^4 = 5 (25 b^2)^2, never a rational square for b!=0.")
# scaling: f_{m,k}(x) -> t^5 f(x/t) = f_{t^2 m, t k}
fa = lambda mm, kk: x**5 + alpha_m.subs({m: mm, k: kk})*x + kk*alpha_m.subs({m: mm, k: kk})
lhs = sp.expand(t**5*fa(m, k).subs(x, x/t))
rhs = sp.expand(fa(t**2*m, t*k))
assert sp.simplify(lhs - rhs) == 0
say("Scaling: t^5 f_{m,k}(x/t) = f_{t^2 m, t k}(x) : OK  => f_{m,k} ~ f_{m/k^2, 1}")
# x -> -x : (m,k) -> (m,-k)
assert sp.simplify(sp.expand((-1)**5*fa(m, k).subs(x, -x)) - fa(m, -k)) == 0
say("x -> -x:  -f_{m,k}(-x) = f_{m,-k}(x) : OK")

# (3) cross-k paths
def chk(name, mm, kk, target):
    A, B = bj(mm, kk); assert (A, B) == target, (name, A, B)
    say(f"  {name}: m={mm}, k={kk}: alpha={A}, beta={B}  (target {target})")
say("Cross-k paths:")
chk("flagship", Fr(5,16), Fr(-8,5), (-55, 88))
chk("classical", Fr(5,16), Fr(4,5), (20, 16))
chk("LSW", Fr(55,16), Fr(-4), (-100, 400))
chk("D5 example", Fr(5,8), Fr(-8,5), (20, -32))
# symbolic paths
def path(name, kexpr, mexpr, p0, p1):
    for uu, tgt in ((0, p0), (1, p1)):
        mm, kk = Fr(str(mexpr.subs(u, uu))), Fr(str(kexpr.subs(u, uu)))
        chk(f"{name} u={uu}", mm, kk, tgt)
    A = alpha_m.subs({m: mexpr, k: kexpr})
    dd = sp.simplify((256*A**5 + 3125*(kexpr*A)**4) - (256*A**2*mexpr)**2)
    assert dd == 0
    say(f"  {name}: disc = (256 alpha(u)^2 m(u))^2 identically in u: OK;  alpha(u) = {sp.factor(sp.expand(A))}")
path("flagship->classical (m const)", R(-8,5)+R(12,5)*u, R(5,16)+0*u, (-55,88), (20,16))
path("flagship->LSW", R(-8,5)-R(12,5)*u, R(5,16)+R(50,16)*u, (-55,88), (-100,400))
path("LSW->classical", -4+R(24,5)*u, R(55,16)-R(50,16)*u, (-100,400), (20,16))

# (4) exact height formula:  disc = 2^48 m^10 (1-eps)^4, eps = 3125 k^4/(65536 m^2)
eps = R(3125)*k**4/(65536*m**2)
assert sp.simplify((256*alpha_m**2*m)**2 - 2**48*m**10*(1-eps)**4) == 0
say("disc(f_m) = 2^48 m^10 (1 - eps)^4, eps = 3125 k^4/(65536 m^2) : OK  (exact identity)")
# numeric check of expansion: log|disc| - (10 log|m| + 48 log 2) = 4 log(1-eps) = -4 eps - 2 eps^2 - ...
import mpmath as mp
mp.mp.dps = 60
for kv, mv in [(Fr(-8,5), Fr(300)), (Fr(-4), Fr(1000)), (Fr(4,5), Fr(7,3)*1000)]:
    d = disc_bj(*bj(mv, kv))
    lhs = mp.log(abs(mp.mpf(d.numerator)/d.denominator)) - 10*mp.log(abs(mp.mpf(mv.numerator)/mv.denominator)) - 48*mp.log(2)
    e = mp.mpf(3125)*mp.mpf(kv.numerator)**4/kv.denominator**4/(65536*(mp.mpf(mv.numerator)/mv.denominator)**2)
    assert abs(lhs - 4*mp.log(1-e)) < mp.mpf(10)**-50
    tail = lhs - (-4*e)
    say(f"  k={kv}, m={mv}: correction = {mp.nstr(lhs,12)}; -4eps = {mp.nstr(-4*e,12)}; remainder/eps^2 = {mp.nstr(tail/e**2,8)} (-> -2)")
# normal form:  f_{m,k}(x) = k^5 g_mu(x/k),  g_mu(y) = y^5 + a(mu)(y+1), a(mu) = 256 mu^2 - 3125/256, mu = m/k^2
mu = sp.symbols('mu'); y = sp.symbols('y')
g = y**5 + (256*mu**2 - R(3125)/256)*(y+1)
assert sp.simplify(sp.expand(k**5*g.subs(mu, m/k**2).subs(y, x/k)) - fa(m, k)) == 0
say("Normal form: f_{m,k}(x) = k^5 g_mu(x/k), g_mu(y)=y^5+(256 mu^2-3125/256)(y+1), mu=m/k^2 : OK")
open("../data/verify_algebra_log.txt", "w").write("\n".join(out) + "\n")
