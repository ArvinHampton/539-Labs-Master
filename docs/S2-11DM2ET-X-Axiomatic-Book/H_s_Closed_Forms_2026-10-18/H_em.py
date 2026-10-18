# Path B: symbolic 2-D Euler-Maclaurin (cited F1, as in the zeta-curve / P_s proofs) for H_s(e^{-t}) at x=0, s>=5.
# H = sum_{w>0} w(v) e^{-tQ2(v)} (e^{-t lam k} - e^{t lam k}), lam = s/2; K = {x r1 + y r2^}, r1=(0,1), r2^=(m, b), m=3s/g, b=(s-8)/g.
# Cosets j=0..m-1: y0=j/m, x0={-bj/m}; half weights on edges via averaged Bernoulli Bt_p(0)=(B_p(0)+B_p(1))/2.
import sympy as sp
from fractions import Fraction as Fr
from math import gcd
s, g, t, X, Y, mu, w = sp.symbols('s g t X Y mu w', positive=True)
lam = s/2; m = 3*s/g; b = (s-8)/g
Q2 = lambda n, k: n**2 + s*n*k + s/2*k**2
q = sp.expand(Q2(m*Y, X + b*Y)); kk = X + b*Y
al, be2, ga = q.coeff(X, 2), q.coeff(X, 1).coeff(Y, 1), q.coeff(Y, 2)   # q = al X^2 + be2 X Y + ga Y^2
Pm = 4
Sx = {p: sp.Symbol(f'Sx{p}') for p in range(1, Pm+1)}; Sy = {p: sp.Symbol(f'Sy{p}') for p in range(1, Pm+1)}
Sxy = {(p, r): sp.Symbol(f'Sxy{p}{r}') for p in range(1, Pm+1) for r in range(1, Pm+1)}
def gint(n, c):   # int_0^oo y^n e^{-t c y^2} dy
    return sp.gamma(sp.Rational(n+1, 2))/(2*(t*c)**sp.Rational(n+1, 2))
def edge_int(expr, var, c):   # expr = polynomial(var) * e^{-t c var^2}; integrate var over (0,oo)
    pol = sp.expand(sp.simplify(expr*sp.exp(t*c*var**2)))
    P = sp.Poly(pol, var); return sum(coef*gint(e[0], c) for e, coef in P.terms())
total = 0
for j in (1, 3):
    F = -2*(t*lam*kk)**j/sp.factorial(j)*sp.exp(-t*q)
    # area: m * int int_{X,Y>0} F = m * (-2 (t lam)^j / j!) * t^{-1-j/2} * Gamma(1+j/2)/2 * int_0^oo k(1,mu)^j / q(1,mu)^{1+j/2} dmu
    kq = (1 + b*mu); qq = al + be2*mu + ga*mu**2
    ang = sp.Symbol(f'ANG{j}')   # angular integral, evaluated per s / in closed form below
    total += m*(-2*(t*lam)**j/sp.factorial(j))*t**(-1-sp.Rational(j, 2))*sp.gamma(1+sp.Rational(j, 2))/2*ang
    for p in range(1, Pm+1):
        total += -Sx[p]/sp.factorial(p)*edge_int(sp.diff(F, X, p-1).subs(X, 0), Y, ga)
        total += -Sy[p]/sp.factorial(p)*edge_int(sp.diff(F, Y, p-1).subs(Y, 0), X, al)
    for p in range(1, Pm+1):
        for r in range(1, Pm+1):
            total += Sxy[(p, r)]/(sp.factorial(p)*sp.factorial(r))*sp.diff(F, X, p-1, Y, r-1).subs({X: 0, Y: 0})
tw = sp.expand(sp.powsimp(sp.expand(total.subs(t, w**2)), force=True))
coef = {k: 0 for k in (-2, -1, 0, 1, 2)}
for term in sp.Add.make_args(tw):
    c_, e_ = term.as_coeff_exponent(w)
    assert c_.has(w) is False, term
    if e_ in coef: coef[e_] += c_
    elif e_ > 2: pass
    else: raise ValueError(('unexpected power', e_, term))
coef = {k: sp.simplify(v) for k, v in coef.items()}
def angint(j, sv):
    gv = gcd(24, sv-8); sub = {s: sv, g: gv}
    integrand = sp.simplify(((1 + b*mu)**j/(al + be2*mu + ga*mu**2)**(1+sp.Rational(j, 2))).subs(sub))
    return sp.nsimplify(sp.integrate(integrand, (mu, 0, sp.oo)))
def bern_sums(sv):
    gv = gcd(24, sv-8); mv = 3*sv//gv; bv = (sv-8)//gv
    def Bt(p, x):
        return (sp.bernoulli(p, 0) + sp.bernoulli(p, 1))/2 if x == 0 else sp.bernoulli(p, x)
    xs = [sp.Rational((-bv*jj) % mv, mv) for jj in range(mv)]; ys = [sp.Rational(jj, mv) for jj in range(mv)]
    d = {}
    for p in range(1, Pm+1):
        d[Sx[p]] = sum(Bt(p, x) for x in xs); d[Sy[p]] = sum(Bt(p, y) for y in ys)
        for r in range(1, Pm+1): d[Sxy[(p, r)]] = sum(Bt(p, x)*Bt(r, y) for x, y in zip(xs, ys))
    return d, gv, mv, bv
def H_coeffs(sv):
    d, gv, mv, bv = bern_sums(sv)
    sub = dict(d); sub.update({s: sv, g: gv, sp.Symbol('ANG1'): angint(1, sv), sp.Symbol('ANG3'): angint(3, sv)})
    return {k: sp.nsimplify(sp.radsimp(sp.simplify(c.subs(sub)))) for k, c in coef.items()}, (gv, mv, bv), d
if __name__ == "__main__":
    import sys, pickle
    print("generic structure (which Bernoulli sums enter each order):")
    for k, c in coef.items(): print(f"  t^{sp.Rational(k,2)}: free symbols {sorted(map(str, c.free_symbols))}")
    pickle.dump(coef, open('H_generic.pkl', 'wb'))
