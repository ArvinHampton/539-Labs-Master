#!/usr/bin/env python3
# PP independent checks for MR2 erratum 7d8fb406 (L-GN, Gaussian-normal structure lemma) -- PP's own code,
# no MR2 routine imported. Exact SymPy only: zero tests are expand(..)==0, Poly(..).is_zero, Rational equality,
# numerator-of-together expand==0. No simplify/nsimplify, no floats, no numpy.
import hashlib, datetime, sys, itertools
from zoneinfo import ZoneInfo
_me = open(__file__, 'rb').read()
print("RUN_START_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z (America/Chicago)"))
print("SCRIPT_SHA256", hashlib.sha256(_me).hexdigest())
import sympy as sp
from sympy import Rational as Q, Matrix, expand, Poly, symbols
print("sympy", sp.__version__); sys.stdout.flush()
NPASS = 0; NFAIL = 0
def chk(lbl, c):
    global NPASS, NFAIL
    if c: NPASS += 1
    else: NFAIL += 1
    print(("PASS " if c else "FAIL ") + lbl); sys.stdout.flush()
def iszero(e):
    e = expand(e)
    return e == 0
def numzero(e):
    n, d = sp.fraction(sp.together(e))
    return expand(n) == 0

# ---------------------------------------------------------------------------------------------
# Part A: point-jet, Gamma route (R^r_smn = d_m G^r_ns - d_n G^r_ms + G^r_ml G^l_ns - G^r_nl G^l_ms),
# general constant h0 (non-diagonal, chosen signature), fully general first and second jets of h.
# index 0 = y; tangent indices 1..n.
def signature_LDL(M):
    L, Dm = M.LDLdecomposition(hermitian=False)
    d = [Dm[i, i] for i in range(M.shape[0])]
    return sum(1 for v in d if v < 0), sum(1 for v in d if v > 0), d

def partA(D, h0, tag):
    n = D - 1
    pairs = [(a, b) for a in range(n) for b in range(a, n)]
    sym = lambda nm, p: symbols(f'{nm}{p[0]}{p[1]}')
    C = {p: sym('c', p) for p in pairs}                              # d_y h
    Bx = {(p, i): symbols(f'b{p[0]}{p[1]}_{i}') for p in pairs for i in range(n)}  # d_i h
    G = {p: sym('gg', p) for p in pairs}                             # (1/2) d_y^2 h  (coefficient of y^2)
    Fm = {(p, i): symbols(f'f{p[0]}{p[1]}_{i}') for p in pairs for i in range(n)}  # d_y d_i h
    Ex = {(p, i, j): symbols(f'e{p[0]}{p[1]}_{i}{j}') for p in pairs for i in range(n) for j in range(i, n)}
    P = lambda a, b: (min(a, b), max(a, b))
    # jets of h at the point (exact): h, dh[k], ddh[k][l] with k,l in 0..n (0 = y)
    def dh(k, a, b):
        p = P(a, b)
        return C[p] if k == 0 else Bx[(p, k-1)]
    def ddh(k, l, a, b):
        p = P(a, b)
        if k == 0 and l == 0: return 2*G[p]
        if k == 0: return Fm[(p, l-1)]
        if l == 0: return Fm[(p, k-1)]
        i, j = min(k-1, l-1), max(k-1, l-1)
        return Ex[(p, i, j)] * (2 if i == j else 1)
    # full metric jets
    g0 = sp.zeros(D, D); g0[0, 0] = 1
    for a in range(n):
        for b in range(n): g0[a+1, b+1] = h0[a, b]
    gi = g0.inv()
    def dg(k, i, j):
        if i == 0 or j == 0: return 0
        return dh(k, i-1, j-1)
    def ddg(k, l, i, j):
        if i == 0 or j == 0: return 0
        return ddh(k, l, i-1, j-1)
    R_ = range(D)
    # Christoffel of first kind and its first derivative at the point
    G1 = {(s, m, v): Q(1, 2)*(dg(m, s, v) + dg(v, s, m) - dg(s, m, v)) for s in R_ for m in R_ for v in R_}
    dG1 = {(l, s, m, v): Q(1, 2)*(ddg(l, m, s, v) + ddg(l, v, s, m) - ddg(l, s, m, v)) for l in R_ for s in R_ for m in R_ for v in R_}
    dgi = {l: -gi*Matrix(D, D, lambda i, j: dg(l, i, j))*gi for l in R_}   # d_l g^{-1} at point (exact)
    Gam = {(r, m, v): expand(sum(gi[r, s]*G1[(s, m, v)] for s in R_)) for r in R_ for m in R_ for v in R_}
    dGam = {(l, r, m, v): expand(sum(dgi[l][r, s]*G1[(s, m, v)] + gi[r, s]*dG1[(l, s, m, v)] for s in R_))
            for l in R_ for r in R_ for m in R_ for v in R_}
    # --- Christoffel checks (values and first derivatives at the point) ---
    hi0 = h0.inv()
    K0 = Matrix(n, n, lambda a, b: Q(1, 2)*dh(0, a, b))
    dK = lambda l, a, b: Q(1, 2)*ddh(l, 0, a, b)
    dhi = lambda l: -hi0*Matrix(n, n, lambda a, b: dh(l, a, b))*hi0
    T = range(1, D)
    ok1 = all(iszero(Gam[(0, a, b)] + K0[a-1, b-1]) for a in T for b in T) and \
          all(iszero(dGam[(l, 0, a, b)] + dK(l, a-1, b-1)) for l in R_ for a in T for b in T)
    Kup0 = hi0*K0
    ok2 = all(iszero(Gam[(a, 0, b)] - Kup0[a-1, b-1]) and iszero(Gam[(a, b, 0)] - Kup0[a-1, b-1]) for a in T for b in T) and \
          all(iszero(dGam[(l, a, 0, b)] - (dhi(l)*K0 + hi0*Matrix(n, n, lambda c, d: dK(l, c, d)))[a-1, b-1]) for l in R_ for a in T for b in T)
    # gamma[h]: n-dim Christoffel of h using only tangent derivatives (its y-derivative uses d_y h, d_y d_x h only)
    gam = lambda a, b, c: sum(hi0[a, d]*Q(1, 2)*(dh(b+1, d, c) + dh(c+1, d, b) - dh(d+1, b, c)) for d in range(n))
    dgam = lambda l, a, b, c: sum(dhi(l)[a, d]*Q(1, 2)*(dh(b+1, d, c) + dh(c+1, d, b) - dh(d+1, b, c))
                                 + hi0[a, d]*Q(1, 2)*(ddh(l, b+1, d, c) + ddh(l, c+1, d, b) - ddh(l, d+1, b, c)) for d in range(n))
    ok3 = all(iszero(Gam[(a, b, c)] - gam(a-1, b-1, c-1)) for a in T for b in T for c in T) and \
          all(iszero(dGam[(l, a, b, c)] - dgam(l, a-1, b-1, c-1)) for l in R_ for a in T for b in T for c in T)
    Gs = list(G.values())
    noG = lambda e: all(sp.diff(e, s) == 0 for s in Gs)
    ok3g = all(noG(dGam[(l, a, b, c)]) for l in R_ for a in T for b in T for c in T)  # d gamma[h] never carries d_y^2 h
    ok4 = all(Gam[k] == 0 for k in [(0, 0, 0)] + [(0, 0, a) for a in T] + [(0, a, 0) for a in T] + [(a, 0, 0) for a in T]) and \
          all(dGam[(l,) + k] == 0 for l in R_ for k in [(0, 0, 0)] + [(0, 0, a) for a in T] + [(0, a, 0) for a in T] + [(a, 0, 0) for a in T])
    chk(f"A1 {tag}: Gamma^y_ab = -K_ab (value and all first derivatives at the point)", ok1)
    chk(f"A2 {tag}: Gamma^a_yb = Gamma^a_by = K^a_b = h^ac K_cb (value and all first derivatives)", ok2)
    chk(f"A3 {tag}: Gamma^a_bc = gamma^a_bc[h] (value and all first derivatives)", ok3)
    chk(f"A3g {tag}: every first derivative of gamma[h] (incl. d_y) is free of d_y^2 h", ok3g)
    chk(f"A4 {tag}: Gamma^y_yy = Gamma^y_ya = Gamma^a_yy = 0 (value and first derivatives)", ok4)
    # Riemann, first index up, Gamma route
    Rup = {}
    for r, s, m, v in itertools.product(R_, repeat=4):
        if m == v: Rup[(r, s, m, v)] = 0; continue
        e = dGam[(m, r, v, s)] - dGam[(v, r, m, s)] + sum(Gam[(r, m, l)]*Gam[(l, v, s)] - Gam[(r, v, l)]*Gam[(l, m, s)] for l in R_)
        Rup[(r, s, m, v)] = expand(e)
    Rdn = {k: expand(sum(g0[k[0], a]*Rup[(a,) + k[1:]] for a in R_)) for k in Rup}
    # second, independent route: R_abcd = 1/2(g_ad,bc + g_bc,ad - g_ac,bd - g_bd,ac) + g_ef(G^e_bc G^f_ad - G^e_bd G^f_ac)
    ok_routes = True
    for a, b, c, d in itertools.product(R_, repeat=4):
        e = Q(1, 2)*(ddg(b, c, a, d) + ddg(a, d, b, c) - ddg(b, d, a, c) - ddg(a, c, b, d)) + \
            sum(g0[e1, f1]*(Gam[(e1, b, c)]*Gam[(f1, a, d)] - Gam[(e1, b, d)]*Gam[(f1, a, c)]) for e1 in R_ for f1 in R_ if g0[e1, f1] != 0)
        if not iszero(e - Rdn[(a, b, c, d)]): ok_routes = False; break
    chk(f"A5 {tag}: Gamma-route R (lowered with g) = metric-jet formula R_abcd, every component (two independent routes agree)", ok_routes)
    # (a) Gauss, (b) Codazzi all placements, (c) Ricci equation
    chk(f"L-GN(a) {tag}: R_abcd (all tangent) free of every d_y^2 h symbol", all(noG(Rdn[(a, b, c, d)]) for a in T for b in T for c in T for d in T))
    codaz = [Rdn[(0, a, b, c)] for a in T for b in T for c in T] + [Rup[(0, a, b, c)] for a in T for b in T for c in T] + \
            [Rup[(a, 0, b, c)] for a in T for b in T for c in T] + [Rup[(a, b, 0, c)] for a in T for b in T for c in T] + \
            [Rup[(a, b, c, 0)] for a in T for b in T for c in T]
    chk(f"L-GN(b) {tag}: Codazzi R_yabc and mixed placements R^y_abc, R^a_ybc, R^a_byc, R^a_bcy free of d_y^2 h (d_x d_y h allowed)", all(noG(e) for e in codaz))
    KhK = K0*hi0*K0
    okc = all(iszero(Rdn[(0, a, 0, b)] - (-dK(0, a-1, b-1) + KhK[a-1, b-1])) for a in T for b in T)
    okc2 = all(iszero(Rup[(0, a, 0, b)] - (-dK(0, a-1, b-1) + KhK[a-1, b-1])) for a in T for b in T)
    chk(f"L-GN(c) {tag}: R_yayb = -d_y K_ab + K_ac K^c_b exactly (lowered with g_yy = 1)", okc)
    chk(f"L-GN(c') {tag}: R^y_ayb = same expression (index lowering by g_yy = 1 is trivial)", okc2)
    # (d) exhaustive: d_y^2 h enters every component exactly through the (c) pattern
    Gz = {s: 0 for s in Gs}
    def pred_dn(r, s, m, v):
        Gm = lambda a, b: G[P(a-1, b-1)]
        if r == 0 and m == 0 and s != 0 and v != 0: return -Gm(s, v)
        if r == 0 and v == 0 and s != 0 and m != 0: return Gm(s, m)
        if s == 0 and m == 0 and r != 0 and v != 0: return Gm(r, v)
        if s == 0 and v == 0 and r != 0 and m != 0: return -Gm(r, m)
        return 0
    okd = all(iszero(sp.S(Rdn[k]) - sp.S(Rdn[k]).subs(Gz) - pred_dn(*k)) for k in Rdn)
    okd_up = all(iszero(sp.S(Rup[k]) - sp.S(Rup[k]).subs(Gz) - sum(gi[k[0], a]*pred_dn(a, *k[1:]) for a in R_)) for k in Rup)
    chk(f"L-GN(d) {tag}: all {D**4} lowered components: G-part = (c) pattern under Riemann symmetries, else 0", okd)
    chk(f"L-GN(d') {tag}: all {D**4} first-index-raised components: G-part = g^-1 x (c) pattern, else 0", okd_up)
    nsym = len(C) + len(Bx) + len(G) + len(Fm) + len(Ex)
    print(f"  {tag}: {nsym} free jet symbols; h0 = {list(h0)}")
    return

cases = []
h0L4 = Matrix([[-2, 1, 0, Q(1, 2)], [1, 3, -1, 0], [0, -1, 2, 1], [Q(1, 2), 0, 1, 5]])
h0E4 = Matrix([[2, 1, 0, 0], [1, 3, 1, 0], [0, 1, 4, -1], [0, 0, -1, 2]])
h0S4 = Matrix([[-1, 1, 0, 0], [1, 2, 0, 1], [0, 0, -3, 1], [0, 1, 1, 1]])
h0E3 = Matrix([[3, 1, -1], [1, 2, 0], [-1, 0, 4]])
h0L5 = Matrix([[-3, 1, 0, 0, 1], [1, 2, 1, 0, 0], [0, 1, 3, -1, 0], [0, 0, -1, 2, 1], [1, 0, 0, 1, 4]])
for D, h0, tag, want in [(4, h0E3, "D=4 Euclidean non-diag h0", (0, 3)), (5, h0L4, "D=5 Lorentzian non-diag h0", (1, 3)),
                         (5, h0E4, "D=5 Euclidean non-diag h0", (0, 4)), (5, h0S4, "D=5 split (2,2) non-diag h0", (2, 2)),
                         (6, h0L5, "D=6 Lorentzian non-diag h0", (1, 4))]:
    neg, pos, d = signature_LDL(h0)
    chk(f"SIG {tag}: exact LDL pivots {d} give (neg,pos) = {(neg, pos)}", (neg, pos) == want and h0.det() != 0 and h0 == h0.T)
    partA(D, h0, tag)

# ---------------------------------------------------------------------------------------------
# Part B: fully functional (not jets) check in D = 3 and D = 4: h_ab(y, x) arbitrary functions, non-diagonal.
def partB(n):
    y = symbols('y'); xs = list(symbols(f'u1:{n+1}')); X = [y] + xs; D = n + 1
    h = Matrix(n, n, lambda a, b: sp.Function(f'h{min(a,b)}{max(a,b)}')(*X))
    g = sp.zeros(D, D); g[0, 0] = 1
    for a in range(n):
        for b in range(n): g[a+1, b+1] = h[a, b]
    det = h.det(); adj = h.adjugate()
    hi = adj/det
    gi = sp.zeros(D, D); gi[0, 0] = 1
    for a in range(n):
        for b in range(n): gi[a+1, b+1] = hi[a, b]
    R_ = range(D)
    Gam = {(r, m, v): sp.together(sum(gi[r, s]*Q(1, 2)*(sp.diff(g[s, v], X[m]) + sp.diff(g[s, m], X[v]) - sp.diff(g[m, v], X[s])) for s in R_))
           for r in R_ for m in R_ for v in R_}
    K = Matrix(n, n, lambda a, b: Q(1, 2)*sp.diff(h[a, b], y))
    T = range(1, D)
    chk(f"B1 D={D} functional: Gamma^y_ab = -K_ab, Gamma^a_yb = K^a_b, Gamma^y_yy = Gamma^y_ya = Gamma^a_yy = 0",
        all(numzero(Gam[(0, a, b)] + K[a-1, b-1]) for a in T for b in T) and
        all(numzero(Gam[(a, 0, b)] - (hi*K)[a-1, b-1]) for a in T for b in T) and
        all(Gam[k] == 0 for k in [(0, 0, 0)] + [(0, 0, a) for a in T] + [(a, 0, 0) for a in T]))
    def Rup(r, s, m, v):
        e = sp.diff(Gam[(r, v, s)], X[m]) - sp.diff(Gam[(r, m, s)], X[v]) + sum(Gam[(r, m, l)]*Gam[(l, v, s)] - Gam[(r, v, l)]*Gam[(l, m, s)] for l in R_)
        return e
    def yorder(e):
        mx = 0
        for dd in e.atoms(sp.Derivative):
            mx = max(mx, sum(c for v, c in dd.variable_count if v == y))
        return mx
    gauss = [sum(g[a, e]*Rup(e, b, c, d) for e in R_) for a in T for b in T for c in T for d in T if c < d]
    chk(f"B2 D={D} functional L-GN(a): every R_abcd has y-derivative order <= 1 in h", max(yorder(sp.expand(e)) for e in gauss) <= 1)
    cod = [Rup(0, a, b, c) for a in T for b in T for c in T if b < c] + [Rup(a, 0, b, c) for a in T for b in T for c in T if b < c] + \
          [Rup(a, b, 0, c) for a in T for b in T for c in T]
    chk(f"B3 D={D} functional L-GN(b): R^y_abc, R^a_ybc, R^a_byc have y-derivative order <= 1 in h", max(yorder(sp.expand(e)) for e in cod) <= 1)
    KhK = K*hi*K
    chk(f"B4 D={D} functional L-GN(c): R^y_ayb (= R_yayb, g_yy = 1, g^ya = 0) = -d_y K_ab + K_ac K^c_b (numerator expand == 0)",
        all(numzero(Rup(0, a, 0, b) - (-sp.diff(K[a-1, b-1], y) + KhK[a-1, b-1])) for a in T for b in T))
for n in (2, 3):
    partB(n)

# ---------------------------------------------------------------------------------------------
# Part C: sign validation on unit S^2 and unit S^3 in Gaussian-normal form
y, th = symbols('y theta')
def riem_func(g, X):
    D = len(X); gi = g.inv()
    Gam = {(r, m, v): sum(gi[r, s]*Q(1, 2)*(sp.diff(g[s, v], X[m]) + sp.diff(g[s, m], X[v]) - sp.diff(g[m, v], X[s])) for s in range(D))
           for r in range(D) for m in range(D) for v in range(D)}
    def Rup(r, s, m, v):
        return sp.diff(Gam[(r, v, s)], X[m]) - sp.diff(Gam[(r, m, s)], X[v]) + sum(Gam[(r, m, l)]*Gam[(l, v, s)] - Gam[(r, v, l)]*Gam[(l, m, s)] for l in range(D))
    return Rup
g2 = sp.diag(1, sp.sin(y)**2); R2 = riem_func(g2, [y, th])
K2 = sp.sin(y)*sp.cos(y)
form = -sp.diff(K2, y) + K2*K2/sp.sin(y)**2
chk("C1 unit S^2 (dy^2 + sin^2 y dth^2): R_y th y th = sin^2 y > 0 and equals -d_y K + K K^c (exact, expand == 0)",
    iszero(R2(0, 1, 0, 1) - sp.sin(y)**2) and iszero(form - sp.sin(y)**2))
ph = symbols('phi')
g3 = sp.diag(1, sp.sin(y)**2, sp.sin(y)**2*sp.sin(th)**2); R3 = riem_func(g3, [y, th, ph])
chk("C2 unit S^3 GN (x-dependent h): R_yayb = sin^2 y * h~_ab (sectional curvature +1), Codazzi R^y_abc = 0",
    iszero(R3(0, 1, 0, 1) - sp.sin(y)**2) and iszero(R3(0, 2, 0, 2) - sp.sin(y)**2*sp.sin(th)**2) and R3(0, 1, 0, 2) == 0 and
    all(iszero(R3(0, a, b, c)) for a in (1, 2) for b in (1, 2) for c in (1, 2)))

# ---------------------------------------------------------------------------------------------
# Part D: coefficient extraction. D1: affine-in-w on a FULL general D=5 jet (Lorentzian non-diag h0) with
# d_y^2 h /2 = w*kappa + r; w-part identified as the algebraic tensor R1 with R1_yayb = -kappa_ab.
def build_R1(D, h0, kap):
    n = D - 1; R1 = {}
    for k in itertools.product(range(D), repeat=4):
        r, s, m, v = k; val = 0
        if r == 0 and m == 0 and s and v: val = -kap[s-1, v-1]
        elif r == 0 and v == 0 and s and m: val = kap[s-1, m-1]
        elif s == 0 and m == 0 and r and v: val = kap[r-1, v-1]
        elif s == 0 and v == 0 and r and m: val = -kap[r-1, m-1]
        R1[k] = val
    return R1

def jetR_with_w(D, h0):
    # own jet build with G = w*kappa + r (others fully general), lowered Riemann via metric-jet formula + Gamma at point
    n = D - 1; w = symbols('w')
    pairs = [(a, b) for a in range(n) for b in range(a, n)]; P = lambda a, b: (min(a, b), max(a, b))
    kap = {p: symbols(f'k{p[0]}{p[1]}') for p in pairs}; rr = {p: symbols(f'r{p[0]}{p[1]}') for p in pairs}
    C = {p: symbols(f'c{p[0]}{p[1]}') for p in pairs}
    Bx = {(p, i): symbols(f'b{p[0]}{p[1]}_{i}') for p in pairs for i in range(n)}
    Fm = {(p, i): symbols(f'f{p[0]}{p[1]}_{i}') for p in pairs for i in range(n)}
    Ex = {(p, i, j): symbols(f'e{p[0]}{p[1]}_{i}{j}') for p in pairs for i in range(n) for j in range(i, n)}
    def dg(k, i, j):
        if i == 0 or j == 0: return 0
        p = P(i-1, j-1); return C[p] if k == 0 else Bx[(p, k-1)]
    def ddg(k, l, i, j):
        if i == 0 or j == 0: return 0
        p = P(i-1, j-1)
        if k == 0 and l == 0: return 2*(w*kap[p] + rr[p])
        if k == 0: return Fm[(p, l-1)]
        if l == 0: return Fm[(p, k-1)]
        a, b = min(k-1, l-1), max(k-1, l-1); return Ex[(p, a, b)]*(2 if a == b else 1)
    g0 = sp.zeros(D, D); g0[0, 0] = 1
    for a in range(n):
        for b in range(n): g0[a+1, b+1] = h0[a, b]
    gi = g0.inv(); R_ = range(D)
    Gam = {(r, m, v): sum(gi[r, s]*Q(1, 2)*(dg(m, s, v) + dg(v, s, m) - dg(s, m, v)) for s in R_) for r in R_ for m in R_ for v in R_}
    Rd = {}
    for a, b, c, d in itertools.product(R_, repeat=4):
        e = Q(1, 2)*(ddg(b, c, a, d) + ddg(a, d, b, c) - ddg(b, d, a, c) - ddg(a, c, b, d)) + \
            sum(g0[e1, f1]*(Gam[(e1, b, c)]*Gam[(f1, a, d)] - Gam[(e1, b, d)]*Gam[(f1, a, c)]) for e1 in R_ for f1 in R_ if g0[e1, f1] != 0)
        Rd[(a, b, c, d)] = expand(e)
    km = Matrix(n, n, lambda a, b: kap[P(a, b)])
    return Rd, w, km, list(rr.values()) + list(C.values()) + list(Bx.values()) + list(Fm.values()) + list(Ex.values())

Rd, w, km, regs = jetR_with_w(5, h0L4)
chk("D1 D=5 full general jet (incl. d_x d_y h, d_x^2 h), Lorentzian non-diag h0: every R component affine in w",
    all(Poly(Rd[k], w).degree() <= 1 for k in Rd if Rd[k] != 0))
R1j = {k: (Poly(Rd[k], w).coeff_monomial(w) if Rd[k] != 0 else 0) for k in Rd}
R1p = build_R1(5, h0L4, km)
chk("D1b D=5: w-coefficient of every lowered component = R1 pattern (R1_yayb = -kappa_ab; zero off pattern), kappa-only",
    all(iszero(R1j[k] - R1p[k]) for k in Rd) and all(all(sp.diff(R1j[k], z) == 0 for z in regs) for k in Rd if R1j[k] != 0))

def invariants(D, h0, km):
    n = D - 1
    g0 = sp.zeros(D, D); g0[0, 0] = 1
    for a in range(n):
        for b in range(n): g0[a+1, b+1] = h0[a, b]
    gi = g0.inv(); R_ = range(D)
    R1 = build_R1(D, h0, km)
    # raise all four indices stepwise (exact)
    def raise_idx(Tt, pos):
        out = {}
        for k in itertools.product(R_, repeat=4):
            s = 0
            for a in R_:
                kk = list(k); kk[pos] = a; kk = tuple(kk)
                if gi[k[pos], a] != 0 and Tt[kk] != 0: s += gi[k[pos], a]*Tt[kk]
            out[k] = expand(s)
        return out
    Rup = R1
    for pos in range(4): Rup = raise_idx(Rup, pos)
    riem2 = expand(sum(R1[k]*Rup[k] for k in R1 if R1[k] != 0))
    Ric = Matrix(D, D, lambda b, d: expand(sum(gi[a, c]*R1[(a, b, c, d)] for a in R_ for c in R_ if gi[a, c] != 0)))
    Ricu = gi*Ric*gi
    ric2 = expand(sum(Ric[a, b]*Ricu[a, b] for a in R_ for b in R_))
    Rs = expand(sum(gi[a, b]*Ric[a, b] for a in R_ for b in R_))
    Wl = {}
    for a, b, c, d in itertools.product(R_, repeat=4):
        Wl[(a, b, c, d)] = expand(R1[(a, b, c, d)] - Q(1, D-2)*(g0[a, c]*Ric[b, d] - g0[a, d]*Ric[b, c] - g0[b, c]*Ric[a, d] + g0[b, d]*Ric[a, c])
                                  + Rs*Q(1, (D-1)*(D-2))*(g0[a, c]*g0[b, d] - g0[a, d]*g0[b, c]))
    Wu = Wl
    for pos in range(4): Wu = raise_idx(Wu, pos)
    w2 = expand(sum(Wl[k]*Wu[k] for k in Wl if Wl[k] != 0))
    M = h0.inv()*km; t1 = M.trace(); t2 = expand((M*M).trace())
    ks = sorted(km.free_symbols, key=str)
    z = lambda e: Poly(expand(e), *ks).is_zero
    chk(f"D2 D={D} Riem^2 coefficient = 4 tr M^2 (M = h0^-1 kappa, non-diag h0, all kappa symbolic)", z(riem2 - 4*t2))
    chk(f"D3 D={D} Ric^2 coefficient = tr M^2 + (tr M)^2", z(ric2 - (t2 + t1**2)))
    chk(f"D4 D={D} R delta-coefficient = -2 tr M", z(Rs + 2*t1))
    chk(f"D5 D={D} Weyl^2 (explicit Weyl tensor) = 4(D-3)/(D-2) (tr M^2 - (tr M)^2/(D-1))", z(w2 - Q(4*(D-3), D-2)*(t2 - t1**2/(D-1))))
    chk(f"D6 D={D} Gauss-Bonnet coefficient = 0", z(riem2 - 4*ric2 + Rs**2))
    chk(f"D7 D={D} Weyl tensor of R1 is traceless (all contractions exact zero)",
        all(iszero(sum(gi[a, c]*Wl[(a, b, c, d)] for a in R_ for c in R_ if gi[a, c] != 0)) for b in R_ for d in R_))

def kapmat(n):
    return Matrix(n, n, lambda a, b: symbols(f'q{min(a,b)}{max(a,b)}'))
invariants(5, h0L4, km)
for D, h0 in [(3, Matrix([[-1, 1], [1, 2]])), (4, h0E3), (6, h0L5),
              (7, Matrix([[-2, 1, 0, 0, 0, 1], [1, 3, 0, 1, 0, 0], [0, 0, 2, 1, 0, 0], [0, 1, 1, 4, 0, 0], [0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 3]])),
              (11, sp.diag(-1, *[1]*9) + Matrix(10, 10, lambda a, b: 1 if abs(a-b) == 1 and a + b < 4 else 0))]:
    invariants(D, h0, kapmat(D-1))

# D8: symbolic-D algebra (Weyl identity |W|^2 = |R|^2 - 4/(D-2)|Ric|^2 + 2/((D-1)(D-2)) R^2 applied to the coefficients)
Dsym, t1s, t2s = symbols('D t1 t2')
riem2s = 4*t2s; ric2s = t2s + t1s**2; Rss = -2*t1s
w2s = riem2s - Q(4)/(Dsym-2)*ric2s + Q(2)/((Dsym-1)*(Dsym-2))*Rss**2
chk("D8 symbolic D: 4t2 - 4/(D-2)(t2+t1^2) + 8 t1^2/((D-1)(D-2)) = 4(D-3)/(D-2)(t2 - t1^2/(D-1)) (numerator expand == 0)",
    numzero(w2s - 4*(Dsym-3)/(Dsym-2)*(t2s - t1s**2/(Dsym-1))))
chk("D9 symbolic: GB coefficient 4t2 - 4(t2 + t1^2) + 4 t1^2 = 0", iszero(riem2s - 4*ric2s + Rss**2))
# D10: null counterexample (P7.5) re-check: M = sigma k k^T eta, k null -> t1 = t2 = 0 although M != 0 (D=5, eta)
sig = symbols('sigma'); eta4 = sp.diag(-1, 1, 1, 1); kv = Matrix([1, 1, 0, 0])
kl = eta4*kv; kapN = sig*kl*kl.T; MN = eta4.inv()*kapN
chk("D10 P7.5 null stress: M != 0 but tr M = tr M^2 = 0 (zero-iff needs P-Poinc)", MN != sp.zeros(4, 4) and iszero(MN.trace()) and iszero((MN*MN).trace()))

# ---------------------------------------------------------------------------------------------
# Part E: C2 profile nits, exact
s = symbols('s', real=True); u = symbols('u'); L, eps = symbols('L epsilon', positive=True)
chk("E1 d/ds tanh = 1 - tanh^2 and 1 - tanh^2 = sech^2 (exp rewrite, numerator expand == 0); tanh -> +-1, so int sech^2 = 2",
    iszero(sp.diff(sp.tanh(s), s) - (1 - sp.tanh(s)**2)) and numzero((sp.sech(s)**2 - (1 - sp.tanh(s)**2)).rewrite(sp.exp))
    and sp.limit(sp.tanh(s), s, sp.oo) == 1 and sp.limit(sp.tanh(s), s, -sp.oo) == -1)
F4 = sp.tanh(s) - sp.tanh(s)**3/3
chk("E2 d/ds(tanh - tanh^3/3) = (1 - tanh^2)^2 = sech^4; limits give int sech^4 = 4/3",
    iszero(sp.diff(F4, s) - (1 - sp.tanh(s)**2)**2) and (Q(1) - Q(1, 3)) - (Q(-1) + Q(1, 3)) == Q(4, 3))
chk("E3 box mollifier height 1/(2 L eps) on width 2 L eps: int phi = 1, int phi^2 = 1/(2 L eps) (CS equality case)",
    iszero((1/(2*L*eps))*(2*L*eps) - 1) and iszero((1/(2*L*eps))**2*(2*L*eps) - 1/(2*L*eps)))
pb = Poly((1 - u**2)**2, u); I1 = pb.integrate().eval(1) - pb.integrate().eval(-1)
pb2 = Poly((1 - u**2)**4, u); I2 = pb2.integrate().eval(1) - pb2.integrate().eval(-1)
# s = L eps u: int phi ds = L eps I1, int (phi/nrm)^2 ds = L eps I2/(L eps I1)^2 = (I2/I1^2)/(L eps)
chk(f"E4 bump (1-u^2)^2, u = s/(L eps): I1 = {I1}, I2 = {I2}, normalised int phi^2 = (I2/I1^2)/(L eps) = 5/(7 L eps) >= 1/(2 L eps)",
    I1 == Q(16, 15) and I2 == Q(256, 315) and I2/I1**2 == Q(5, 7) and Q(5, 7) >= Q(1, 2))

print(f"\nPASS_COUNT {NPASS} FAIL_COUNT {NFAIL}")
print("ALL_CHECKS", "PASS" if NFAIL == 0 else "FAIL")
print("RUN_END_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z"))
