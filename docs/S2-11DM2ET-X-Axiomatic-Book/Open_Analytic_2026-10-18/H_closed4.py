# Path B closure: closed forms in s (and g = gcd(24, s-8)) of H_s radial coefficients at t^{3/2}, t^{5/2} (x = 0).
import sympy as sp, pickle, sys
from math import gcd
s, g, t, X, Y, mu, w = sp.symbols('s g t X Y mu w', positive=True)
lam = s/2; m = 3*s/g; b = (s-8)/g
Q2 = lambda n, k: n**2 + s*n*k + s/2*k**2
q = sp.expand(Q2(m*Y, X + b*Y)); al, be2, ga = q.coeff(X, 2), q.coeff(X, 1).coeff(Y, 1), q.coeff(Y, 2)
coef = pickle.load(open('H_generic4.pkl', 'rb'))
Qm = ga*mu**2 + be2*mu + al
def ang(j):
    r = sp.symbols(f'r0:{j+1}'); R = sum(r[i]*mu**i for i in range(j+1))
    num = sp.expand(sp.diff(R, mu)*Qm - sp.Rational(j, 2)*R*sp.diff(Qm, mu) - (1 + b*mu)**j)
    sol = sp.solve(sp.Poly(num, mu).all_coeffs(), r, dict=True); assert len(sol) == 1
    Rs = R.subs(sol[0]); F = Rs/Qm**sp.Rational(j, 2)
    assert sp.simplify(sp.diff(F, mu) - (1 + b*mu)**j/Qm**(1+sp.Rational(j, 2))) == 0
    lead = sp.Poly(Rs, mu).coeff_monomial(mu**j); val = lead/ga**sp.Rational(j, 2) - Rs.subs(mu, 0)/al**sp.Rational(j, 2)
    return sp.simplify(val)
gen = {sp.Symbol('Sx1'): 0, sp.Symbol('Sy1'): 0}
for p in range(2, 11):
    gen[sp.Symbol(f'Sx{p}')] = m**(1-p)*sp.bernoulli(p); gen[sp.Symbol(f'Sy{p}')] = m**(1-p)*sp.bernoulli(p)
res = {}
out = []
for k, A in ((-1, 'ANG1'), (1, 'ANG3'), (3, 'ANG5'), (5, 'ANG7'), (7, 'ANG9'), (9, 'ANG11')):
    Aj = ang(int(A[3:]))
    val = sp.simplify(coef[k].subs(sp.Symbol(A), Aj).subs(gen))
    # normal form: sqrt(2 pi s) * (A + B sqrt(Delta)),  Delta = (s-2)(7s-32);  substitute s = sig^2, sqrt(Delta) -> r
    sig, r = sp.symbols('sig r', positive=True); Dl = (s-2)*(7*s-32)
    e = sp.expand(sp.powsimp(sp.powdenest((val/sp.sqrt(2*sp.pi*s)).subs(s, sig**2), force=True), force=True))
    e = e.subs(sp.sqrt(7*sig**4 - 46*sig**2 + 64), r).subs(sp.sqrt(sig**2 - 2)*sp.sqrt(7*sig**2 - 32), r)
    e = sp.together(e); num, den = sp.fraction(e)
    numr = sp.rem(sp.Poly(sp.expand(num), r), sp.Poly(r**2 - Dl.subs(s, sig**2), r)).as_expr()
    denr = sp.rem(sp.Poly(sp.expand(den), r), sp.Poly(r**2 - Dl.subs(s, sig**2), r)).as_expr()
    assert not sp.Poly(denr, r).degree() > 0 or True
    # rationalise denominator if it contains r
    if sp.Poly(denr, r).degree() > 0:
        d0, d1 = sp.Poly(denr, r).coeff_monomial(1), sp.Poly(denr, r).coeff_monomial(r)
        numr = sp.expand(numr*(d0 - d1*r)); denr = sp.expand(d0**2 - d1**2*Dl.subs(s, sig**2))
        numr = sp.rem(sp.Poly(numr, r), sp.Poly(r**2 - Dl.subs(s, sig**2), r)).as_expr()
    Pn = sp.Poly(numr, r); A = sp.factor(sp.simplify((Pn.coeff_monomial(1)/denr).subs(sig, sp.sqrt(s))))
    Bc = sp.factor(sp.simplify((Pn.coeff_monomial(r)/denr).subs(sig, sp.sqrt(s))))
    assert not A.has(r) and not Bc.has(r)
    res[k] = (A, Bc)
    out.append(f"H_{{{sp.Rational(k,2)}}} = sqrt(2 pi s) * [ {A}  +  ({Bc}) * sqrt((s-2)(7s-32)) ]")
    print(out[-1], flush=True)
for k in (0, 2, 4, 6, 8):
    val = sp.simplify(coef[k].subs(gen)); out.append(f"edge/area part of t^{k//2} (corner terms excluded) = {val}"); print(out[-1])
pickle.dump(res, open('H_closed4.pkl', 'wb'))
open('H_closed4.txt', 'w').write("\n".join(out) + "\n")
