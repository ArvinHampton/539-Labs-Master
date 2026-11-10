#!/usr/bin/env python3
# MR2 2026-11-10 -- erratum to f4ee61f2 per PP 976e5621: machine check of L-GN (Gaussian-normal structure lemma)
# on fully general jets (non-diagonal, x-dependent, all second jets symbolic) in D = 4, 5, 6; general-[K] delta^2
# coefficients in D = 5 incl. time-space entries; profile nits (I2, Cauchy-Schwarz). Exact SymPy only.
import hashlib, datetime, sys, itertools
from zoneinfo import ZoneInfo
_me = open(__file__, 'rb').read()
print("RUN_START_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z (America/Chicago)"))
print("SCRIPT_SHA256", hashlib.sha256(_me).hexdigest(), __file__.split('/')[-1])
sys.stdout.flush()
import sympy as sp
from sympy import Rational as Q, symbols, Matrix, zeros, expand, Poly
print("sympy", sp.__version__)
ok_all = True
def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + label); sys.stdout.flush()

def riemann_at_point(g, X, P):
    n = len(X)
    g0 = g.subs(P)
    dg = [[[expand(sp.diff(g[i, j], X[k]).subs(P)) for j in range(n)] for i in range(n)] for k in range(n)]
    cache = {}
    def d2(k, l, i, j):
        key = (min(k, l), max(k, l), i, j)
        if key not in cache:
            cache[key] = expand(sp.diff(g[i, j], X[k], X[l]).subs(P))
        return cache[key]
    gi = g0.inv()
    Gl = [[[Q(1, 2)*(dg[b][e][c] + dg[c][e][b] - dg[e][b][c]) for c in range(n)] for b in range(n)] for e in range(n)]
    Gu = [[[expand(sum(gi[e, f]*Gl[f][b][c] for f in range(n))) for c in range(n)] for b in range(n)] for e in range(n)]
    R = {}
    for a, b, c, d in itertools.product(range(n), repeat=4):
        if a == b or c == d:
            R[(a, b, c, d)] = 0; continue
        val = Q(1, 2)*(d2(b, c, a, d) + d2(a, d, b, c) - d2(b, d, a, c) - d2(a, c, b, d))
        val += sum(g0[e, f]*(Gu[e][b][c]*Gu[f][a][d] - Gu[e][b][d]*Gu[f][a][c]) for e in range(n) for f in range(n) if g0[e, f] != 0)
        R[(a, b, c, d)] = expand(val)
    return R, g0, gi

# validation
x1, x2 = symbols('x1 x2')
R, g0, gi = riemann_at_point(Matrix([[1 - Q(1,3)*x2**2, Q(1,3)*x1*x2], [Q(1,3)*x1*x2, 1 - Q(1,3)*x1**2]]), [x1, x2], {x1: 0, x2: 0})
check("V unit S^2 jet: R_1212 = 1 (sign convention: sphere positive)", R[(0, 1, 0, 1)] == 1)

def lgn(D):
    n = D - 1
    y = symbols('y'); xs = list(symbols(f'x1:{n+1}'))
    X = [y] + xs
    eta = [-1] + [1]*(n - 1)
    pairs = [(a, b) for a in range(n) for b in range(a, n)]
    def S(name):
        return {p: symbols(f'{name}_{p[0]}{p[1]}') for p in pairs}
    C = S('C'); G = S('G')
    B = {(p, i): symbols(f'B_{p[0]}{p[1]}_{i}') for p in pairs for i in range(n)}
    Fm = {(p, i): symbols(f'F_{p[0]}{p[1]}_{i}') for p in pairs for i in range(n)}
    E = {(p, i, j): symbols(f'E_{p[0]}{p[1]}_{i}{j}') for p in pairs for i in range(n) for j in range(i, n)}
    def ent(a, b):
        p = (min(a, b), max(a, b))
        e = (eta[a] if a == b else 0) + C[p]*y + G[p]*y**2 + sum(B[(p, i)]*xs[i] for i in range(n)) \
            + sum(Fm[(p, i)]*y*xs[i] for i in range(n)) + sum(E[(p, i, j)]*xs[i]*xs[j] for i in range(n) for j in range(i, n))
        return e
    g = zeros(D, D); g[0, 0] = 1
    for a in range(n):
        for b in range(n):
            g[a+1, b+1] = ent(a, b)
    P = {y: 0}; P.update({xx: 0 for xx in xs})
    R, g0, gi = riemann_at_point(g, X, P)
    Gs = list(G.values())
    noG = lambda e: all(sp.diff(e, s) == 0 for s in Gs)
    T = range(1, D)
    gauss = all(noG(R[(a, b, c, d)]) for a in T for b in T for c in T for d in T)
    cod = all(noG(R[(0, a, b, c)]) for a in T for b in T for c in T)
    Gm = Matrix(n, n, lambda a, b: G[(min(a, b), max(a, b))])
    Cm = Matrix(n, n, lambda a, b: C[(min(a, b), max(a, b))])
    K = Cm/2; dK = Gm  # K_ab = (1/2) d_y h_ab ; d_y K_ab = (1/2) d_y^2 h_ab = G_ab at the point
    hinv = Matrix(n, n, lambda a, b: (eta[a] if a == b else 0))
    KK = K*hinv*K
    ric = all(expand(R[(0, a+1, 0, b+1)] - (-dK[a, b] + KK[a, b])) == 0 for a in range(n) for b in range(n))
    nsym = len(C) + len(G) + len(B) + len(Fm) + len(E)
    print(f"  D={D}: {nsym} free jet symbols (h(0) = eta by a constant linear change of x, which preserves the GN form)")
    check(f"L-GN(a) D={D}: Gauss components R_abcd independent of every second y-jet G_ab", gauss)
    check(f"L-GN(b) D={D}: Codazzi components R_yabc independent of every second y-jet G_ab", cod)
    check(f"L-GN(c) D={D}: R_yayb = -d_y K_ab + K_ac K^c_b exactly (K = d_y h / 2), fully general non-diagonal x-dependent jet", ric)
    return R, g0, gi, Gm, G, n

print("\n== L-GN machine check on fully general jets ==")
for D in (4, 5, 6):
    out = lgn(D)

print("\n== general-[K] delta^2 coefficients, D = 5, all 10 entries of kappa symbolic (incl. time-space) ==")
# (D=5 recomputed below with G = w*kappa + r)
# recompute D=5 and substitute G = w*kappa + regular
D = 5; n = 4
y = symbols('y'); xs = list(symbols('x1:5')); X = [y] + xs
eta = [-1, 1, 1, 1]
w = symbols('w')
kap = {(a, b): symbols(f'k_{a}{b}') for a in range(n) for b in range(a, n)}
rg = {(a, b): symbols(f'r_{a}{b}') for a in range(n) for b in range(a, n)}
cC = {(a, b): symbols(f'c_{a}{b}') for a in range(n) for b in range(a, n)}
bB = {(a, b, i): symbols(f'b_{a}{b}_{i}') for a in range(n) for b in range(a, n) for i in range(n)}
g = zeros(D, D); g[0, 0] = 1
for a in range(n):
    for b in range(n):
        p = (min(a, b), max(a, b))
        g[a+1, b+1] = (eta[a] if a == b else 0) + cC[p]*y + (w*kap[p] + rg[p])*y**2 + sum(bB[p + (i,)]*xs[i] for i in range(n))
P = {y: 0}; P.update({xx: 0 for xx in xs})
R, g0, gi = riemann_at_point(g, X, P)
etaD = [1] + eta
gens = list(kap.values()) + list(rg.values()) + list(cC.values()) + list(bB.values())
affine = all(Poly(R[key], w).degree() <= 1 for key in R if R[key] != 0)
check("GK0 D=5 every Riemann component is affine in w (= 1/eps): R = R0 + w R1", affine)
# exact: w^2-coefficient of any square of an affine tensor = square of its w-coefficient; R1 depends on kappa only
R1 = {key: (Poly(R[key], w).coeff_monomial(w) if R[key] != 0 else 0) for key in R}
check("GK0b D=5 the w-coefficient R1 involves kappa only (no regular jet symbols)",
      all(all(sp.diff(R1[key], z) == 0 for z in list(rg.values()) + list(cC.values()) + list(bB.values())) for key in R1 if R1[key] != 0))
Ric1 = Matrix(D, D, lambda b, d: expand(sum(etaD[a]*R1[(a, b, a, d)] for a in range(D))))
Rs1 = expand(sum(etaD[b]*Ric1[b, b] for b in range(D)))
riem2_c = expand(sum(R1[(a, b, c, d)]**2*etaD[a]*etaD[b]*etaD[c]*etaD[d] for a, b, c, d in itertools.product(range(D), repeat=4) if R1[(a, b, c, d)] != 0))
ric2_c = expand(sum(Ric1[a, b]**2*etaD[a]*etaD[b] for a in range(D) for b in range(D)))
W2c = 0
for a, b, c, d in itertools.product(range(D), repeat=4):
    val = R1[(a, b, c, d)] - Q(1, D-2)*(g0[a, c]*Ric1[b, d] - g0[a, d]*Ric1[b, c] - g0[b, c]*Ric1[a, d] + g0[b, d]*Ric1[a, c]) \
          + Rs1*Q(1, (D-1)*(D-2))*(g0[a, c]*g0[b, d] - g0[a, d]*g0[b, c])
    val = expand(val)
    if val != 0:
        W2c += val**2*etaD[a]*etaD[b]*etaD[c]*etaD[d]
W2c = expand(W2c)
km = Matrix(n, n, lambda a, b: kap[(min(a, b), max(a, b))])
M = Matrix(n, n, lambda a, b: eta[a]*km[a, b])  # mixed M^a_b = h^{ac} kappa_cb at the point
t1 = M.trace(); t2 = (M*M).trace()
kg = list(kap.values())
check("GK1 D=5 Riem^2 w^2-coeff = 4 tr M^2 (general symmetric kappa incl. kappa_tv)", Poly(expand(riem2_c - 4*t2), *kg).is_zero)
check("GK2 D=5 Ric^2 w^2-coeff = tr M^2 + (tr M)^2", Poly(expand(ric2_c - (t2 + t1**2)), *kg).is_zero)
check("GK3 D=5 R w-coeff = -2 tr M", Poly(expand(Rs1 + 2*t1), *kg).is_zero)
check("GK4 D=5 Weyl^2 w^2-coeff = (4(D-3)/(D-2))(tr M^2 - (tr M)^2/(D-1)) = (8/3)(trM^2 - trM^2/4)", Poly(expand(W2c - Q(8, 3)*(t2 - t1**2/4)), *kg).is_zero)
check("GK5 D=5 Gauss-Bonnet w^2-coeff = 0", Poly(expand(riem2_c - 4*ric2_c + Rs1**2), *kg).is_zero)

print("\n== profile nits (C2) ==")
T = symbols('T'); s = symbols('s')
check("C2a int sech^2 ds = [tanh] = 2 (d/ds tanh = 1 - T^2 = sech^2; limits T = +-1)", (T.subs(T, 1) - T.subs(T, -1)) == 2)
F4 = T - T**3/3
check("C2b int sech^4 ds = 4/3 (d/ds(T - T^3/3) = (1-T^2)^2)", expand(sp.diff(F4, T)*(1 - T**2) - (1 - T**2)**2) == 0 and F4.subs(T, 1) - F4.subs(T, -1) == Q(4, 3))
L, eps = symbols('L epsilon', positive=True)
phi_box = 1/(2*L*eps)
check("C2c Cauchy-Schwarz equality case: box mollifier on [-L eps, L eps] has int phi^2 = 1/(2 L eps)", sp.integrate(phi_box**2, (s, -L*eps, L*eps)) == 1/(2*L*eps))
phi_b = (1 - (s/(L*eps))**2)**2
nrm = sp.integrate(phi_b, (s, -L*eps, L*eps))
I = sp.integrate((phi_b/nrm)**2, (s, -L*eps, L*eps))
check("C2d bump (1-(s/(L eps))^2)^2 normalised: int phi^2 = 5/(7 L eps) >= 1/(2 L eps) (exact rational comparison)", sp.cancel(I*L*eps) == Q(5, 7) and Q(5, 7) >= Q(1, 2))

print("\nALL_CHECKS", "PASS" if ok_all else "FAIL")
print("RUN_END_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z"))
