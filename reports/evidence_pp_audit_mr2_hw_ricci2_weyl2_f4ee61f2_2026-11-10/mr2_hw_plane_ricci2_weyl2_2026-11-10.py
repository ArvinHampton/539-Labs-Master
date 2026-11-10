#!/usr/bin/env python3
# MR2 2026-11-10 -- HW fixed-plane boundary matching: delta^2 structure of Riem^2, Ric^2, R^2, Weyl^2, GB.
# Exact algebra only (SymPy rationals/polynomials; zero tests are canonical expanded-polynomial/rational comparisons, no simplify, no floats). Labelled, unadopted pursuit. No adoption. Junction UNSOLVED.
import hashlib, datetime, sys, itertools
from zoneinfo import ZoneInfo
_me = open(__file__, 'rb').read()
print("RUN_START_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z (America/Chicago)"))
print("SCRIPT_SHA256", hashlib.sha256(_me).hexdigest(), __file__.split('/')[-1])
sys.stdout.flush()
import sympy as sp
from sympy import Rational as Q, Poly, expand, symbols, Matrix, zeros
print("sympy", sp.__version__)

def curvature_at_point(g, X, P):
    """Exact R_abcd, Ric_ab, R, Weyl_abcd and squares at point P from the 2-jet of g. Own code."""
    n = len(X)
    g0 = g.subs(P)
    dg = [[[sp.expand(sp.diff(g[i, j], X[k]).subs(P)) for j in range(n)] for i in range(n)] for k in range(n)]
    ddg = {}
    def d2(k, l, i, j):
        key = (min(k, l), max(k, l), i, j)
        if key not in ddg:
            ddg[key] = sp.expand(sp.diff(g[i, j], X[k], X[l]).subs(P))
        return ddg[key]
    gi = g0.inv()
    Gl = [[[sp.Rational(1, 2)*(dg[b][e][c] + dg[c][e][b] - dg[e][b][c]) for c in range(n)] for b in range(n)] for e in range(n)]
    Gu = [[[sp.expand(sum(gi[e, f]*Gl[f][b][c] for f in range(n) if gi[e, f] != 0)) for c in range(n)] for b in range(n)] for e in range(n)]
    R = [[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a, b, c, d in itertools.product(range(n), repeat=4):
        if a == b or c == d:
            continue
        val = sp.Rational(1, 2)*(d2(b, c, a, d) + d2(a, d, b, c) - d2(b, d, a, c) - d2(a, c, b, d))
        val += sum(g0[e, f]*(Gu[e][b][c]*Gu[f][a][d] - Gu[e][b][d]*Gu[f][a][c])
                   for e in range(n) for f in range(n) if g0[e, f] != 0)
        R[a][b][c][d] = sp.expand(val)
    Ric = Matrix(n, n, lambda b, d: sp.expand(sum(gi[a, c]*R[a][b][c][d] for a in range(n) for c in range(n) if gi[a, c] != 0)))
    Rs = sp.expand(sum(gi[b, d]*Ric[b, d] for b in range(n) for d in range(n) if gi[b, d] != 0))
    W = [[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a, b, c, d in itertools.product(range(n), repeat=4):
        W[a][b][c][d] = sp.expand(R[a][b][c][d]
            - sp.Rational(1, n-2)*(g0[a, c]*Ric[b, d] - g0[a, d]*Ric[b, c] - g0[b, c]*Ric[a, d] + g0[b, d]*Ric[a, c])
            + Rs*sp.Rational(1, (n-1)*(n-2))*(g0[a, c]*g0[b, d] - g0[a, d]*g0[b, c]))
    diag = all(gi[i, j] == 0 for i in range(n) for j in range(n) if i != j)
    def sq4(T):
        if diag:
            return sp.expand(sum(T[a][b][c][d]**2*gi[a, a]*gi[b, b]*gi[c, c]*gi[d, d]
                                 for a, b, c, d in itertools.product(range(n), repeat=4) if T[a][b][c][d] != 0))
        U = T
        for slot in range(4):
            V = [[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
            for idx in itertools.product(range(n), repeat=4):
                s = 0
                for m in range(n):
                    if gi[idx[slot], m] == 0:
                        continue
                    j = list(idx); j[slot] = m
                    s += gi[idx[slot], m]*U[j[0]][j[1]][j[2]][j[3]]
                V[idx[0]][idx[1]][idx[2]][idx[3]] = sp.expand(s)
            U = V
        return sp.expand(sum(U[a][b][c][d]*T[a][b][c][d] for a, b, c, d in itertools.product(range(n), repeat=4)))
    RicUp = gi*Ric*gi
    ric2 = sp.expand(sum(RicUp[a, b]*Ric[a, b] for a in range(n) for b in range(n)))
    riem2 = sq4(R); weyl2 = sq4(W)
    gb = sp.expand(riem2 - 4*ric2 + Rs**2)
    return dict(R=R, Ric=Ric, Rs=Rs, riem2=riem2, ric2=ric2, weyl2=weyl2, gb=gb)

def same(a, b, gens):
    return Poly(sp.expand(a - b), *gens).is_zero

ok_all = True
def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + label); sys.stdout.flush()

# ---------- V. validations of own curvature routine ----------
print("\n== V. validation (exact) ==")
th, ph = symbols('th ph')
# unit S^2 via 2-jet of round metric at th=1/2 is transcendental; use stereographic-free polynomial check instead:
# S^2 of radius 1 in Riemann-normal-like jet: g = dx^2+dy^2 - (1/3)(x dy - y dx)^2 at origin -> K=1
x1, x2, x3 = symbols('x1 x2 x3')
gS2 = Matrix([[1 - Q(1,3)*x2**2, Q(1,3)*x1*x2], [Q(1,3)*x1*x2, 1 - Q(1,3)*x1**2]])
c = curvature_at_point(gS2, [x1, x2], {x1: 0, x2: 0})
check("S^2 normal-coord jet: R = 2, Riem^2 = 4, Weyl^2 n/a(2D)", c['Rs'] == 2 and c['riem2'] == 4)
gH2 = Matrix([[1 + Q(1,3)*x2**2, -Q(1,3)*x1*x2], [-Q(1,3)*x1*x2, 1 + Q(1,3)*x1**2]])
c = curvature_at_point(gH2, [x1, x2], {x1: 0, x2: 0})
check("H^2 normal-coord jet: R = -2", c['Rs'] == -2)
gS3 = Matrix(3, 3, lambda i, j: (1 if i == j else 0)) - Q(1,3)*Matrix(3, 3, lambda i, j:
      (sum([x1, x2, x3][k]**2 for k in range(3)) if i == j else 0) - [x1, x2, x3][i]*[x1, x2, x3][j])
c = curvature_at_point(gS3, [x1, x2, x3], {x1: 0, x2: 0, x3: 0})
check("S^3 normal-coord jet: R = 6, Ric^2 = 12, Riem^2 = 12, Weyl^2 = 0 (conformally flat)",
      c['Rs'] == 6 and c['ric2'] == 12 and c['riem2'] == 12 and c['weyl2'] == 0)

# ---------- A. 11D Gaussian-normal diagonal wall model, generic point ----------
print("\n== A. 11D wall model g = dy^2 + sum_a eta_a e^{2A_a(y)} dx_a^2 (a = 0..9, eta_0 = -1), 2-jet at y0 ==")
y = symbols('y')
xs = symbols('x0:10')
p = symbols('p0:10')  # A_a'(y0)
q = symbols('q0:10')  # A_a''(y0)
eta = [-1] + [1]*9
X = [y] + list(xs)
g = zeros(11, 11); g[0, 0] = 1
for a in range(10):
    g[a+1, a+1] = eta[a]*(1 + 2*p[a]*y + (2*p[a]**2 + q[a])*y**2)  # exact 2-jet of eta e^{2A}, e^{2A(y0)} scaled to 1
P0 = {y: 0}; P0.update({xx: 0 for xx in xs})
cA = curvature_at_point(g, X, P0)
gens = list(p) + list(q)
riem_pred = 4*sum((q[a] + p[a]**2)**2 for a in range(10)) + 2*sum((p[a]*p[b])**2 for a in range(10) for b in range(10) if a != b)
check("A0 Riem^2 = 4 sum(A''+A'^2)^2 + 2 sum_{a!=b}(A'_a A'_b)^2 (exact polynomial identity)", same(cA['riem2'], riem_pred, gens))
w = symbols('w')  # w = 1/eps ; A_a'' = -k_a * w * phi + r_a, at wall centre phi = 1 (sech^2 profile)
k = symbols('k0:10'); r = symbols('r0:10')
sub = {q[a]: -k[a]*w + r[a] for a in range(10)}
T2 = sum(kk**2 for kk in k); T1 = sum(k)
coef = {}
for name in ['riem2', 'ric2', 'weyl2', 'gb']:
    e = sp.expand(cA[name].subs(sub))
    coef[name] = Poly(e, w).coeff_monomial(w**2)
    print(f"  w^2 coefficient of {name}: {sp.factor(coef[name])}")
eR2 = Poly(sp.expand((cA['Rs']**2).subs(sub)), w).coeff_monomial(w**2)
print(f"  w^2 coefficient of R^2: {sp.factor(eR2)}")
kg = list(k)
check("A1 Riem^2 delta^2-coefficient = 4 tr[k^2], independent of A', regular A''", same(coef['riem2'], 4*T2, kg + list(p) + list(r)))
check("A2 Ric_MN Ric^MN delta^2-coefficient = tr k^2 + (tr k)^2", same(coef['ric2'], T2 + T1**2, kg + list(p) + list(r)))
check("A3 R^2 delta^2-coefficient = 4 (tr k)^2", same(eR2, 4*T1**2, kg + list(p) + list(r)))
check("A4 Weyl^2 delta^2-coefficient = (32/9)(tr k^2 - (tr k)^2/10) = (32/9) tr(k~^2)", same(coef['weyl2'], Q(32,9)*(T2 - T1**2/10), kg + list(p) + list(r)))
check("A5 Gauss-Bonnet delta^2-coefficient = 0 identically", same(coef['gb'], 0, kg + list(p) + list(r)))
# degree in w: invariants are quadratic in q -> at most w^2
for name in ['riem2', 'ric2', 'weyl2']:
    check(f"A6 {name} has degree <= 2 in 1/eps (no worse than delta^2)", Poly(sp.expand(cA[name].subs(sub)), w).degree() <= 2)

# ---------- B. 4D Lorentzian, x-dependent, non-diagonal kink (generic [K]) ----------
print("\n== B. 4D model g = dy^2 + h_ab(y,u), a,b in (t,u,v); h = h0(u) + y h1(u) + y^2 (h2 + w kappa), point y=0,u=1/2 ==")
t, u, v = symbols('t u v')
k0, k1, k2, k12, k01 = symbols('k0 k1 k2 k12 k01')
h0 = Matrix([[-(1 + u**2/7), u/13, 0], [u/13, 1 + u/5, u/11], [0, u/11, 2 + u**2/3]])
h1 = Matrix([[Q(1,3), 0, u/9], [0, u/2, Q(1,5)], [u/9, Q(1,5), -Q(1,7)]])
h2 = Matrix([[u, Q(1,4), 0], [Q(1,4), Q(2,3), u**2], [0, u**2, -Q(1,2)]])
kap = Matrix([[k0, k01, 0], [k01, k1, k12], [0, k12, k2]])
h = h0 + y*h1 + y**2*(h2 + w*kap)
gB = zeros(4, 4); gB[0, 0] = 1
for i in range(3):
    for j in range(3):
        gB[i+1, j+1] = h[i, j]
PB = {y: 0, t: 0, u: Q(1, 2), v: 0}
cB = curvature_at_point(gB, [y, t, u, v], PB)
M = h0.subs(PB).inv()*kap
trM = M.trace(); trM2 = (M*M).trace()
gensB = [k0, k1, k2, k12, k01]
def wc(expr, deg):
    return Poly(sp.expand(expr), w).coeff_monomial(w**deg)
check("B1 Riem^2 w^2-coeff = 4 tr(M^2), M = h0^{-1} kappa (non-diagonal, Lorentzian, x-dependent)", same(wc(cB['riem2'], 2), 4*trM2, gensB))
check("B2 Ric^2 w^2-coeff = tr M^2 + (tr M)^2", same(wc(cB['ric2'], 2), trM2 + trM**2, gensB))
check("B3 R w-coeff = -2 tr M (R^2 w^2-coeff = 4 (tr M)^2)", same(wc(cB['Rs'], 1), -2*trM, gensB))
check("B4 Weyl^2 w^2-coeff (D=4) = (4(D-3)/(D-2))(tr M^2 - (tr M)^2/(D-1)) = 2(trM^2 - trM^2/3)", same(wc(cB['weyl2'], 2), 2*(trM2 - trM**2/3), gensB))
check("B5 GB w^2-coeff = 0", same(wc(cB['gb'], 2), 0, gensB))
# pulled-back curvature 2-form on the plane: tangent-legged components carry no 1/eps
Rt = cB['R']
nodelta = all(Poly(sp.expand(Rt[a][b][c][d]), w).degree() <= 0 for a in range(1, 4) for b in range(1, 4) for c in range(4) for d in range(4))
check("B6 R_{ab MN} with both FORM legs a,b tangent (Gauss R_abcd and Codazzi R_ab y c) contain no 1/eps term", nodelta)
hasdelta = any(Poly(sp.expand(Rt[0][a][0][b]), w).degree() == 1 for a in range(1, 4) for b in range(1, 4))
check("B7 only R_{y a y b} carries the 1/eps (delta) term", hasdelta)

# ---------- B'. Z2 parity of one-sided limits (exact, two polynomial sides) ----------
print("\n== B'. Z2-even metric h(-y) = h(y): one-sided limits at the plane ==")
H1 = h1; H2 = h2
hp = h0 + y*H1 + y**2*H2
hm = h0 - y*H1 + y**2*H2
def side(hh):
    G = zeros(4, 4); G[0, 0] = 1
    for i in range(3):
        for j in range(3):
            G[i+1, j+1] = hh[i, j]
    return curvature_at_point(G, [y, t, u, v], PB)
cp, cm = side(hp), side(hm)
gauss_even = all((cp['R'][a][b][c][d] - cm['R'][a][b][c][d]) == 0 for a in range(1,4) for b in range(1,4) for c in range(1,4) for d in range(1,4))
codazzi_odd = all((cp['R'][0][a][b][c] + cm['R'][0][a][b][c]) == 0 for a in range(1,4) for b in range(1,4) for c in range(1,4))
codazzi_nonzero = any(cp['R'][0][a][b][c] != 0 for a in range(1,4) for b in range(1,4) for c in range(1,4))
check("B'1 Gauss components R_abcd: one-sided limits EQUAL (Z2-even, single-valued on the plane)", gauss_even)
check("B'2 Codazzi components R_yabc: one-sided limits OPPOSITE (Z2-odd), nonzero here", codazzi_odd and codazzi_nonzero)
check("B'3 Riem^2, Ric^2, R, Weyl^2 one-sided limits EQUAL (finite, single-valued)",
      all(cp[n_] == cm[n_] for n_ in ['riem2', 'ric2', 'Rs', 'weyl2']))
# HW boundary density tr R^2 built from pulled-back 2-form: R_ab^{MN} R_cd_{MN}: even (Gauss^2 + Codazzi^2)
print("  one-sided Riem^2 at plane (rational, model):", cp['riem2'])

# ---------- C. smoothing profile: delta^2 is non-integrable ----------
print("\n== C. profile integrals (exact) ==")
T = symbols('T')  # T = tanh(s); d/ds T = 1 - T^2 ; sech^2 = 1 - T^2
F4 = T - T**3/3
check("C1 d/ds (tanh - tanh^3/3) = sech^4  (polynomial identity in T)", expand(sp.diff(F4, T)*(1 - T**2) - (1 - T**2)**2) == 0)
I4 = F4.subs(T, 1) - F4.subs(T, -1); I2 = 2
print("  int sech^4 ds =", I4, " int sech^2 ds =", I2)
check("C2 phi_eps = sech^2(y/eps)/(2 eps): int phi = 1, int phi^2 = (1/(4 eps^2)) * eps * 4/3 = 1/(3 eps)", I4 == Q(4,3))
print("  => int Q dy over the wall ~ Q_delta2 / (3 eps) -> infinity unless Q_delta2 = 0 ; Cauchy-Schwarz: any mollifier with support 2L eps has int phi^2 >= 1/(2 L eps)")

# ---------- D. Israel map [K] <-> S on the 10D plane ----------
print("\n== D. Israel: S^a_b = -(1/kappa^2)([K]^a_b - delta [K]), n = 10 ==")
j = symbols('j0:10'); kq = symbols('kappa2', positive=True)
S = [-(j[a] - sum(j))/kq for a in range(10)]
trS = sum(S); Stl = [S[a] - trS/10 for a in range(10)]; jtl = [j[a] - sum(j)/10 for a in range(10)]
check("D1 traceless parts: [K]~ = -kappa^2 S~ (exact)", all(sp.expand(jtl[a] + kq*Stl[a]) == 0 for a in range(10)))
check("D2 tr[K] = (kappa^2/9) tr S", sp.expand(sum(j) - kq*trS/9) == 0)
check("D3 Weyl^2 delta^2-coeff = (32/9) kappa^4 tr(S~^2): zero iff S proportional to h",
      sp.expand(Q(32,9)*sum(x_**2 for x_ in jtl) - Q(32,9)*kq**2*sum(s_**2 for s_ in Stl)) == 0)
check("D4 Ric^2 delta^2-coeff tr[K]^2 + (tr[K])^2 is a positive-definite form (diagonalisable [K]): zero iff [K]=0 iff S=0",
      Matrix(10, 10, lambda a, b: (1 if a == b else 0) + 1).is_positive_definite)

# ---------- E. instances ----------
print("\n== E. instances (11D, w^2 coefficients in units a^2, eigenvalues of -[K]/2 per smoothing) ==")
def inst(kv):
    s_ = {k[i]: kv[i] for i in range(10)}
    return [sp.nsimplify(coef[n_].subs(s_)) for n_ in ['riem2', 'ric2', 'weyl2', 'gb']] + [eR2.subs(s_)]
a_ = symbols('a')
mn2 = inst([a_]*4 + [0]*6)
print("  MN2 kink (x-block bends, k=(a,a,a,a,0^6)) [Riem2, Ric2, Weyl2, GB, R2]:", mn2)
check("E1 reproduces filed PP-PROVED coefficients 16, 20, 128/15, R^2 64 (aeb9ab13 section 4)", mn2 == [16*a_**2, 20*a_**2, Q(128,15)*a_**2, 0, 64*a_**2])
umb = inst([a_]*10)
check("E2 umbilic wall (k = a h): Weyl^2 delta^2 = 0, Riem^2 = 40 a^2 (filed V1)", umb[2] == 0 and umb[0] == 40*a_**2)
# BPS-type 1:1:0 stress (6D worldvolume x+Sigma, fibre 0): S = -tau diag(1^6, 0^4) -> [K]
tau = symbols('tau', positive=True)
Sb = [-tau]*6 + [0]*4
Kb = [-kq*(Sb[a_i] - sum(Sb)/9) for a_i in range(10)]
s_ = {k[i]: Kb[i] for i in range(10)}
wb = sp.factor(coef['weyl2'].subs(s_))
print("  BPS-type 1:1:0 stress: Weyl^2 delta^2-coeff =", wb)
check("E3 BPS-type 1:1:0 wall stress has nonzero Weyl^2 delta^2 for tau > 0", wb != 0)

# ---------- F. uniqueness of the delta^2-free quadratic combination ----------
print("\n== F. alpha Riem^2 + beta Ric^2 + gamma R^2 free of delta^2 for every wall ==")
al, be, ga = symbols('alpha beta gamma')
sol = sp.solve([4*al + be, be + 4*ga], [be, ga], dict=True)
print("  solution:", sol)
check("F1 unique up to scale: (alpha, beta, gamma) = (1, -4, 1) = Gauss-Bonnet", sol == [{be: -4*al, ga: al}])

# ---------- G. NEC content lemma on the 10D Lorentzian plane ----------
print("\n== G. sum over null k = t +- e_i of T_YM(k,k) is positive definite in F (D_wall = 10) ==")
Dw = 10
etaw = [-1] + [1]*(Dw - 1)
Fs = {}
for a1 in range(Dw):
    for b1 in range(a1+1, Dw):
        Fs[(a1, b1)] = symbols(f'F_{a1}_{b1}')
def Fc(a1, b1):
    if a1 == b1: return 0
    return Fs[(a1, b1)] if a1 < b1 else -Fs[(b1, a1)]
tot = 0
for i in range(1, Dw):
    for sgn in (1, -1):
        kvec = [0]*Dw; kvec[0] = 1; kvec[i] = sgn
        Fk = [sum(kvec[a1]*Fc(a1, c1) for a1 in range(Dw)) for c1 in range(Dw)]
        tot += sum(etaw[c1]*Fk[c1]**2 for c1 in range(Dw))
tot = sp.expand(tot)
vars_ = list(Fs.values())
Hm = sp.hessian(tot, vars_)/2
Lm, Dm = Hm.LDLdecomposition()
check("G1 quadratic form sum_k |F(k,.)|^2 positive definite (exact LDL, all pivots > 0) => T_YM(k,k)=0 for all null k forces F=0",
      all(Dm[i_, i_] > 0 for i_ in range(len(vars_))))
print("  LDL pivots (distinct):", sorted(set(Dm[i_, i_] for i_ in range(len(vars_)))))

print("\nALL_CHECKS", "PASS" if ok_all else "FAIL")
print("RUN_END_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z"))
