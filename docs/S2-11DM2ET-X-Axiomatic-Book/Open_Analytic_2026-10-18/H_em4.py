# Path B closure: symbolic 2-D Euler-Maclaurin (cited F1) for H_s(e^{-t}) at x = 0, extended to t^{7/2}.
# Same set-up as 2026-10-18-H_s-Closed-Forms/H_em.py; sinh expansion terms j = 1,3,5,7; Bernoulli orders up to Pm = 6.
# Order bookkeeping (scaling X,Y ~ t^{-1/2}): area term of order j -> t^{j/2-1}; edge term (j,p) -> t^{(j+p-2)/2}; corner terms -> integer powers.
import sympy as sp, pickle, sys
s, g, t, X, Y, mu, w = sp.symbols('s g t X Y mu w', positive=True)
lam = s/2; m = 3*s/g; b = (s-8)/g
Q2 = lambda n, k: n**2 + s*n*k + s/2*k**2
q = sp.expand(Q2(m*Y, X + b*Y)); kk = X + b*Y
al, be2, ga = q.coeff(X, 2), q.coeff(X, 1).coeff(Y, 1), q.coeff(Y, 2)
Pm = 10; JS = (1, 3, 5, 7, 9, 11); KMAX = 9          # keep powers w^k, k <= KMAX  (w = t^{1/2})
Sx = {p: sp.Symbol(f'Sx{p}') for p in range(1, Pm+1)}; Sy = {p: sp.Symbol(f'Sy{p}') for p in range(1, Pm+1)}
def gint(n, c): return sp.gamma(sp.Rational(n+1, 2))/(2*(t*c)**sp.Rational(n+1, 2))
def edge_int(expr, var, c):
    pol = sp.expand(sp.simplify(expr*sp.exp(t*c*var**2)))
    P = sp.Poly(pol, var); return sum(coef*gint(e[0], c) for e, coef in P.terms())
total = 0
for j in JS:
    F = -2*(t*lam*kk)**j/sp.factorial(j)*sp.exp(-t*q)
    ang = sp.Symbol(f'ANG{j}')
    total += m*(-2*(t*lam)**j/sp.factorial(j))*t**(-1-sp.Rational(j, 2))*sp.gamma(1+sp.Rational(j, 2))/2*ang
    for p in range(1, Pm+1):
        if (j + p - 2) > KMAX: continue
        total += -Sx[p]/sp.factorial(p)*edge_int(sp.diff(F, X, p-1).subs(X, 0), Y, ga)
        total += -Sy[p]/sp.factorial(p)*edge_int(sp.diff(F, Y, p-1).subs(Y, 0), X, al)
    # corner terms contribute integer powers of t only (polynomial in t): omitted here (half-integer orders are the target)
tw = sp.expand(sp.powsimp(sp.expand(total.subs(t, w**2)), force=True))
coef = {}
for term in sp.Add.make_args(tw):
    c_, e_ = term.as_coeff_exponent(w)
    assert not c_.has(w), term
    if e_ <= KMAX: coef[e_] = coef.get(e_, 0) + c_
coef = {k: sp.simplify(v) for k, v in coef.items()}
pickle.dump(coef, open('H_generic4.pkl', 'wb'))
for k in sorted(coef): print(f"t^{sp.Rational(k,2)}: symbols {sorted(map(str, coef[k].free_symbols))}", flush=True)
