# K=15 variant of sym_engine.py: identical mathematics; sp.simplify wrapped so that a sympy heuristic-gcd failure keeps the exact unsimplified expression.
# Items (1)-(3): symbolic (in s, g) form of the proved expansion at any rational x = a/N, after the two exact reductions
#   (R1) corners cancel between Q+ and Q- (nu -> -nu maps Q- to Q+, alpha,beta -> 1-alpha,1-beta, B_r(1-u) = (-1)^r B_r(u));
#   (R2) S0_- = S0_+, TEb_-[r] = (-1)^r TEb_+[r], TEa_-[r] = (-1)^r TEa_+[r] (same map).
# Then, with lam = s/2, gamma0 = S0/(P^2 m), TEb[r] = m^{1-r} eb_r, TEa[r] = m^{1-r} ea_r (distribution relation, proved in report):
#   c_e = sum_{i odd, i-2=e}  -2 lam^i/i! * gamma0 * J_i
#       - sum_{i+r even, i-1+r=e} 2(-lam)^i/(i!(r+1)!) * [IY_{i,r} m^{-r} eb_{r+1} + IX_{i,r} m^{-r} ea_{r+1}]
#   J_i = int int_{cone in (n,k)} k^i e^{-Q2} dn dk,  IY/IX = edge integrals of l^i e^{-q} in U-coordinates (U_i = P u_i).
import sympy as sp, pickle, sys
_simp = sp.simplify
def _safe(e, *a, **k):
    try: return _simp(e, *a, **k)
    except Exception: return e      # sympy HeuristicGCDFailed at K=15: keep the (exact) unsimplified expression
sp_simplify = _safe
s, g, X, Y, mu = sp.symbols('s g X Y mu', positive=True)
m = 3*s/g; b = (s - 8)/g; lam = s/2
Delta = (s - 2)*(7*s - 32)
A2 = s*Delta/(2*g**2)
assert sp_simplify(m**2 + s*m*b + s*b**2/2 - A2) == 0
def gauss_mono(j, a):           # int_0^oo X^j e^{-a X^2} dX
    return sp.gamma(sp.Rational(j + 1, 2))/(2*a**sp.Rational(j + 1, 2))
def edge_integrals(i, r, P):
    q = P**2*(s/2*X**2 + s*(m + b)*X*Y + A2*Y**2); l = P*(X + b*Y)
    out = []
    for var, other, a in ((Y, X, P**2*s/2), (X, Y, P**2*A2)):
        # d_var^r (l^i e^{-q}) at var = 0  = poly(other) * e^{-a other^2}
        expr = sp.diff(l**i*sp.exp(-q), var, r).subs(var, 0)
        poly = sp.expand(sp_simplify(expr*sp.exp(a*other**2)))
        pl = sp.Poly(poly, other)
        out.append(sp_simplify(sum(cf*gauss_mono(mon[0], a) for mon, cf in zip(pl.monoms(), pl.coeffs()))))
    return out  # IY, IX
def J(i):                       # area integral over the real cone, i odd
    j = sp.Rational(i + 1, 2)
    a0, h2, c0 = s/2, 4*s*(s - 2), s*Delta/2
    D = a0 + h2*mu + c0*mu**2
    Nm = sp.expand((1 + (s - 8)*mu)**i)
    R = sp.symbols('R0:%d' % (i + 1)); Rp = sum(R[k]*mu**k for k in range(i + 1))
    eq = sp.Poly(sp.expand(sp.diff(Rp, mu)*D - (j - sp.Rational(1, 2))*Rp*sp.diff(D, mu) - Nm), mu).all_coeffs()
    sol = sp.solve(eq, R, dict=True)[0]
    val = sol[R[i]]/c0**sp.Rational(i, 2) - sol[R[0]]/a0**sp.Rational(i, 2)
    return sp_simplify(3*s*sp.gamma(sp.Rational(i + 2, 2))/2*val)
def universal(P, K):
    """returns dict e -> (A_e, {r+1: Y_coef}, {r+1: X_coef}) so that c_e = gamma0*A_e + sum eb_k Y_k + sum ea_k X_k"""
    U = {}
    for e in range(-1, K + 1, 2):
        A = 0; Yc = {}; Xc = {}
        i = e + 2
        if i % 2 == 1: A = -2*lam**i/sp.factorial(i)*J(i)
        for i in range(0, e + 2):
            r = e + 1 - i
            if r < 0 or (i + r) % 2: continue
            IY, IX = edge_integrals(i, r, P)
            f = -2*(-lam)**i/(sp.factorial(i)*sp.factorial(r + 1))
            Yc[r + 1] = sp_simplify(Yc.get(r + 1, 0) + f*IY*m**(-r)); Xc[r + 1] = sp_simplify(Xc.get(r + 1, 0) + f*IX*m**(-r))
        U[e] = (sp_simplify(A), Yc, Xc)
    return U
if __name__ == "__main__":
    P = int(sys.argv[1]); K = int(sys.argv[2])
    U = universal(P, K)
    pickle.dump(U, open('sym_universal_P%d_K%d.pkl' % (P, K), 'wb'))
    for e, (A, Yc, Xc) in U.items():
        print('e =', e, 'A =', A); print('  Y:', Yc); print('  X:', Xc, flush=True)
