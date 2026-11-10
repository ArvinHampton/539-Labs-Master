#!/usr/bin/env python3
# MR2 2026-11-10 (second filing) -- HW Z2 plane: near-plane backreacted jet / constraint structure, and the
# covering-space delta^2 claim restated without the 9760 value. Exact SymPy only. Labelled, unadopted pursuit.
import hashlib, datetime, sys, itertools
from zoneinfo import ZoneInfo
_me = open(__file__, 'rb').read()
print("RUN_START_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z (America/Chicago)"))
print("SCRIPT_SHA256", hashlib.sha256(_me).hexdigest(), __file__.split('/')[-1])
sys.stdout.flush()
import sympy as sp
from sympy import Rational as Q, Poly, symbols, Matrix, zeros, expand
print("sympy", sp.__version__)

ok_all = True
def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + label); sys.stdout.flush()

def curv(g, X, P):
    """Own code: exact R_abcd, Ric, R at point P from the 2-jet of g (convention: unit S^2 has R = +2)."""
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
    R = [[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a, b, c, d in itertools.product(range(n), repeat=4):
        if a == b or c == d:
            continue
        val = Q(1, 2)*(d2(b, c, a, d) + d2(a, d, b, c) - d2(b, d, a, c) - d2(a, c, b, d))
        val += sum(g0[e, f]*(Gu[e][b][c]*Gu[f][a][d] - Gu[e][b][d]*Gu[f][a][c]) for e in range(n) for f in range(n) if g0[e, f] != 0)
        R[a][b][c][d] = expand(val)
    Ric = Matrix(n, n, lambda b, d: expand(sum(gi[a, c]*R[a][b][c][d] for a in range(n) for c in range(n))))
    Rs = expand(sum(gi[b, d]*Ric[b, d] for b in range(n) for d in range(n)))
    return dict(R=R, Ric=Ric, Rs=Rs, g0=g0, gi=gi)

# ---------------- V. validation ----------------
print("\n== V. validation ==")
x1, x2, x3 = symbols('x1 x2 x3')
gS2 = Matrix([[1 - Q(1,3)*x2**2, Q(1,3)*x1*x2], [Q(1,3)*x1*x2, 1 - Q(1,3)*x1**2]])
check("V1 unit S^2 jet: R = 2", curv(gS2, [x1, x2], {x1: 0, x2: 0})['Rs'] == 2)
gS3 = Matrix(3, 3, lambda i, j: (1 if i == j else 0)) - Q(1,3)*Matrix(3, 3, lambda i, j:
      (x1**2 + x2**2 + x3**2 if i == j else 0) - [x1, x2, x3][i]*[x1, x2, x3][j])
check("V2 unit S^3 jet: R = 6", curv(gS3, [x1, x2, x3], {x1: 0, x2: 0, x3: 0})['Rs'] == 6)

# ---------------- J1-J3. Gaussian-normal structure of the Einstein equations off the plane ----------------
print("\n== J1-J3. g = dy^2 + h_ab(y,u,v), a,b in (t,u,v) Lorentzian; h = h0 + y h1 + y^2 h2; point y=0,u=1/3,v=1/5 ==")
y, t, u, v = symbols('y t u v')
c = symbols('c0:6')  # free second-y-jet entries h2 (symbolic)
h0 = Matrix([[-(1 + u**2/7 + v/9), u*v/13, v/17], [u*v/13, 1 + u/5 + v**2/3, u/11], [v/17, u/11, 2 + u**2/3 - v/7]])
h1 = Matrix([[Q(1,3) + v/5, u/7, u/9], [u/7, u/2 + v**2, Q(1,5) + u*v], [u/9, Q(1,5) + u*v, -Q(1,7) + v/3]])
h2 = Matrix([[c[0], c[1], c[2]], [c[1], c[3], c[4]], [c[2], c[4], c[5]]])
h = h0 + y*h1 + y**2*h2
g = zeros(4, 4); g[0, 0] = 1
for i in range(3):
    for j in range(3):
        g[i+1, j+1] = h[i, j]
P = {y: 0, t: 0, u: Q(1, 3), v: Q(1, 5)}
C = curv(g, [y, t, u, v], P)
Ric, Rs, g0 = C['Ric'], C['Rs'], C['g0']
Ein = Matrix(4, 4, lambda a, b: expand(Ric[a, b] - Q(1, 2)*g0[a, b]*Rs))
free_c = lambda e: all(sp.diff(e, ci) == 0 for ci in c)
check("J1a constraints: G_yy contains no second y-derivative of h (independent of h2)", free_c(Ein[0, 0]))
check("J1b constraints: G_ya (a = t,u,v) contain no second y-derivative of h", all(free_c(Ein[0, a]) for a in range(1, 4)))
lin = all(expand(Ric[a+1, b+1] + h2[a, b] - Ric[a+1, b+1].subs({ci: 0 for ci in c})) == 0 for a in range(3) for b in range(3))
check("J1c evolution: R_ab = -(1/2) d_y^2 h_ab + (terms without h2), i.e. d_y^2 h is solved for algebraically (unit coefficient)", lin)
# Gauss: 2 G_yy = -r[h0] + (tr K)^2 - tr K^2, with K_ab = (1/2) d_y h_ab = (1/2) h1 at the point
tan = curv(h0, [t, u, v], {t: 0, u: Q(1, 3), v: Q(1, 5)})
r0 = tan['Rs']; hi = tan['gi']
K = h1.subs(P)/2
Kmix = hi*K
trK = Kmix.trace(); trK2 = (Kmix*Kmix).trace()
check("J2 Gauss constraint exact: 2 G_yy = -r[h] + (tr K)^2 - tr(K^2)", expand(2*Ein[0, 0] - (-r0 + trK**2 - trK2)) == 0)
# Codazzi: G_ya = +/-(D_b K^b_a - D_a K); compute D_b K^b_a on the plane from h0(u,v), K(u,v) = h1(u,v)/2
Xt = [t, u, v]
Kf = h1/2
h0i = h0.inv()
Gam = [[[sum(h0i[e, f]*Q(1, 2)*(sp.diff(h0[f, b], Xt[cc]) + sp.diff(h0[f, cc], Xt[b]) - sp.diff(h0[b, cc], Xt[f])) for f in range(3))
         for cc in range(3)] for b in range(3)] for e in range(3)]
Kup = h0i*Kf  # K^b_a  (row b, col a)
def DK(b, a):  # D_b K^b_a summed later; D_m K^b_a = d_m K^b_a + Gam^b_{m e} K^e_a - Gam^e_{m a} K^b_e
    return sp.diff(Kup[b, a], Xt[b]) + sum(Gam[b][b][e]*Kup[e, a] for e in range(3)) - sum(Gam[e][b][a]*Kup[b, e] for e in range(3))
trKf = Kup.trace()
cod = [expand((sum(DK(b, a) for b in range(3)) - sp.diff(trKf, Xt[a])).subs({t: 0, u: Q(1, 3), v: Q(1, 5)})) for a in range(3)]
sgn_p = all(expand(Ein[0, a+1] - cod[a]) == 0 for a in range(3))
sgn_m = all(expand(Ein[0, a+1] + cod[a]) == 0 for a in range(3))
print("  Codazzi sign found:", "+" if sgn_p else ("-" if sgn_m else "none"))
check("J3 Codazzi constraint exact: G_ya = s (D_b K^b_a - D_a K), s = +1 or -1 fixed by convention", sgn_p or sgn_m)

# ---------------- J4. Z2 + Israel on the 10D plane: K+ from S, and the quadratic stress form ----------------
print("\n== J4. Israel (PP/NL convention) with Z2: [K] = 2K+, K+_ab - h_ab K+ = -(kappa^2/2) S_ab, n = 10 ==")
sv = symbols('s0:10'); kap2 = symbols('kappa2', positive=True)
trS = sum(sv)
Kp = [-(kap2/2)*(sv[a] - trS/9) for a in range(10)]
trKp = sum(Kp)
check("J4a inversion: K+ - h tr K+ = -(kappa^2/2) S (eigenvalue-wise, diagonalisable premise)", all(expand(Kp[a] - trKp + (kap2/2)*sv[a]) == 0 for a in range(10)))
check("J4b tr K+ = kappa^2 tr S / 18", expand(trKp - kap2*trS/18) == 0)
quad = expand(trKp**2 - sum(k_**2 for k_ in Kp))
check("J4c (tr K+)^2 - tr(K+^2) = (kappa^4/4)((tr S)^2/9 - tr S^2)  [exact]", expand(quad - (kap2**2/4)*(trS**2/9 - sum(s_**2 for s_ in sv))) == 0)

# ---------------- J5. 4-form stress normal-normal component ----------------
print("\n== J5. T_yy = (1/12)(G_yPQR G_y^PQR - (1/8) g_yy G^2) with G = G_t + dy^H, Lorentzian D = 6 generic ==")
D = 6
etaD = [1, -1, 1, 1, 1, 1]  # index 0 = y (normal, spacelike), index 1 = time
comps = {}
for idx in itertools.combinations(range(D), 4):
    comps[idx] = symbols('G_' + ''.join(map(str, idx)))
def Gc(*ix):
    if len(set(ix)) < 4: return 0
    perm = sorted(range(4), key=lambda k_: ix[k_]); srt = tuple(sorted(ix))
    # sign of permutation
    p_ = list(perm); sgn = 1
    for i_ in range(4):
        while p_[i_] != i_:
            j_ = p_[i_]; p_[i_], p_[j_] = p_[j_], p_[i_]; sgn = -sgn
    return sgn*comps[srt]
G2 = expand(sum(Gc(*ix)**2*etaD[ix[0]]*etaD[ix[1]]*etaD[ix[2]]*etaD[ix[3]] for ix in itertools.product(range(D), repeat=4)))
Gy2 = expand(sum(Gc(0, *ix)**2*etaD[ix[0]]*etaD[ix[1]]*etaD[ix[2]] for ix in itertools.product(range(D), repeat=3)))
Tyy = expand(Q(1, 12)*(Gy2 - Q(1, 8)*G2))
HH = expand(sum(Gc(0, *ix)**2*etaD[ix[0]]*etaD[ix[1]]*etaD[ix[2]] for ix in itertools.product(range(1, D), repeat=3)))  # full contraction H.H
GtGt = expand(sum(Gc(*ix)**2*etaD[ix[0]]*etaD[ix[1]]*etaD[ix[2]]*etaD[ix[3]] for ix in itertools.product(range(1, D), repeat=4)))
check("J5 T_yy = H.H/24 - G_t.G_t/96 (full index contractions; exact)", expand(Tyy - (HH/24 - GtGt/96)) == 0)

# ---------------- J6. pointwise Gauss constraint on the plane; both signs realisable ----------------
print("\n== J6. Gauss on the Z2 plane:  H.H/24 = -r/2 + (kappa^4/8)((trS)^2/9 - trS^2) + J.J/384   (G_t(0+) = J/2) ==")
r_, j_ = symbols('r j', real=True)
# 10D orthonormal frame on the plane: 0 = t, 1..3 = x, 4,5 = Sigma, 6..9 = fibre. Poincare-invariant magnetic E8 field on fibre (one generator)
etaw = [-1] + [1]*9
f1, f2 = symbols('f1 f2', real=True)
F = zeros(10, 10)
F[6, 7] = f1; F[7, 6] = -f1; F[8, 9] = f2; F[9, 8] = -f2
Fup = Matrix(10, 10, lambda a, b: etaw[a]*etaw[b]*F[a, b])
FF = sum(F[a, b]*Fup[a, b] for a in range(10) for b in range(10))
# mixed S^a_b = F^a_c F_b^c - (1/4) delta F.F  (positive trace normalised to 1/lambda^2 = 1)
Smix = Matrix(10, 10, lambda a, b: expand(sum(Fup[a, c_]*F[b, c_] for c_ in range(10)) - (Q(1, 4)*FF if a == b else 0)))
tau = symbols('tau', nonnegative=True)
SM5 = Matrix(10, 10, lambda a, b: (-tau if (a == b and a <= 5) else 0))
Stot = Smix + SM5
trS_ = Stot.trace(); trS2_ = (Stot*Stot).trace()
JJ = 24*j_**2  # J = j e^6789 on the fibre
rhs = expand(-r_/2 + (kap2**2/8)*(trS_**2/9 - trS2_) + JJ/384)
print("  H.H/24 required =", sp.factor(rhs))
ex_bad = rhs.subs({r_: 1, kap2: 1, f1: 1, f2: 1, tau: 0, j_: 0})
ex_good = rhs.subs({r_: -1, kap2: 1, f1: 1, f2: 1, tau: 0, j_: 0})
print("  example A (r=+1, kappa^2=1, f1=f2=1, tau=0, j=0):", ex_bad, "  example B (r=-1, same):", ex_good)
check("J6a the Gauss constraint is a genuine inequality on plane data (example A: required H.H < 0, no real H on Riemannian Y6)", ex_bad < 0)
check("J6b and is satisfiable (example B: required H.H > 0) -> no pointwise algebraic rule-out", ex_good > 0)
# S(k,k) for k = t + e_i  (lowered S_ab = eta_a S^a_b)
Slow = Matrix(10, 10, lambda a, b: etaw[a]*Stot[a, b])
def Skk(i):
    kv = [0]*10; kv[0] = 1; kv[i] = 1
    return expand(sum(kv[a]*kv[b]*Slow[a, b] for a in range(10) for b in range(10)))
check("J6c null-positivity of this content: S(k,k) >= 0 for k = t + e_i, all i (sums of squares / tau >= 0)",
      all(sp.Poly(Skk(i), f1, f2, tau).coeffs() and all(cf >= 0 for cf in sp.Poly(Skk(i), f1, f2, tau).coeffs()) for i in range(1, 10)))

# ---------------- K. covering-space delta^2 without the 9760 value (re-derived here, not taken from f4ee61f2) ----------------
print("\n== K. 11D thin-wall delta^2 coefficients (re-derived), Israel map, null-positivity lemma ==")
yy = symbols('y'); xs = symbols('x0:10'); p = symbols('p0:10'); q = symbols('q0:10')
eta = [-1] + [1]*9
g11 = zeros(11, 11); g11[0, 0] = 1
for a in range(10):
    g11[a+1, a+1] = eta[a]*(1 + 2*p[a]*yy + (2*p[a]**2 + q[a])*yy**2)
P11 = {yy: 0}; P11.update({xx: 0 for xx in xs})
C11 = curv(g11, [yy] + list(xs), P11)
gi11 = C11['gi']; R11 = C11['R']; Ric11 = C11['Ric']; Rs11 = C11['Rs']; g011 = C11['g0']
n = 11
riem2 = expand(sum(R11[a][b][c_][d]**2*gi11[a, a]*gi11[b, b]*gi11[c_, c_]*gi11[d, d] for a, b, c_, d in itertools.product(range(n), repeat=4) if R11[a][b][c_][d] != 0))
ric2 = expand(sum(Ric11[a, a]**2*gi11[a, a]**2 for a in range(n)) + sum(Ric11[a, b]**2*gi11[a, a]*gi11[b, b] for a in range(n) for b in range(n) if a != b))
W = {}
for a, b, c_, d in itertools.product(range(n), repeat=4):
    val = R11[a][b][c_][d] - Q(1, n-2)*(g011[a, c_]*Ric11[b, d] - g011[a, d]*Ric11[b, c_] - g011[b, c_]*Ric11[a, d] + g011[b, d]*Ric11[a, c_]) \
          + Rs11*Q(1, (n-1)*(n-2))*(g011[a, c_]*g011[b, d] - g011[a, d]*g011[b, c_])
    val = expand(val)
    if val != 0: W[(a, b, c_, d)] = val
weyl2 = expand(sum(val**2*gi11[a, a]*gi11[b, b]*gi11[c_, c_]*gi11[d, d] for (a, b, c_, d), val in W.items()))
w = symbols('w'); k = symbols('k0:10'); rr = symbols('r0:10')
sub = {q[a]: -k[a]*w + rr[a] for a in range(10)}
T2 = sum(x_**2 for x_ in k); T1 = sum(k)
co = lambda e: Poly(expand(e.subs(sub)), w).coeff_monomial(w**2)
gens = list(k) + list(p) + list(rr)
check("K1 Ric_MN Ric^MN delta^2 coeff = tr k^2 + (tr k)^2", Poly(expand(co(ric2) - (T2 + T1**2)), *gens).is_zero)
check("K2 Riem^2 delta^2 coeff = 4 tr k^2", Poly(expand(co(riem2) - 4*T2), *gens).is_zero)
check("K3 Weyl^2 delta^2 coeff = (32/9)(tr k^2 - (tr k)^2/10)", Poly(expand(co(weyl2) - Q(32, 9)*(T2 - T1**2/10)), *gens).is_zero)
check("K4 Ric^2 coefficient form I + 11^T is positive definite (zero iff k = 0)", (sp.eye(10) + sp.ones(10, 10)).is_positive_definite)
jv = symbols('j0:10')
Sj = [-(jv[a] - sum(jv))/kap2 for a in range(10)]
check("K5 Israel: [K] = 0 iff S = 0, and traceless [K]~ = -kappa^2 S~",
      all(expand((jv[a] - sum(jv)/10) + kap2*(Sj[a] - sum(Sj)/10)) == 0 for a in range(10)) and expand(sum(jv) - kap2*sum(Sj)/9) == 0)
Dw = 10; etaw2 = [-1] + [1]*9
Fs = {(a, b): symbols(f'F_{a}_{b}') for a in range(Dw) for b in range(a+1, Dw)}
Fc = lambda a, b: 0 if a == b else (Fs[(a, b)] if a < b else -Fs[(b, a)])
tot = 0
for i in range(1, Dw):
    for sg in (1, -1):
        kv = [0]*Dw; kv[0] = 1; kv[i] = sg
        Fk = [sum(kv[a]*Fc(a, c_) for a in range(Dw)) for c_ in range(Dw)]
        tot += sum(etaw2[c_]*Fk[c_]**2 for c_ in range(Dw))
Hm = sp.hessian(expand(tot), list(Fs.values()))/2
Lm, Dm = Hm.LDLdecomposition()
check("K6 sum over null k = t +- e_i of |F(k,.)|^2 is positive definite (exact LDL): S_YM(k,k)=0 for all null k forces F = 0", all(Dm[i, i] > 0 for i in range(Dm.shape[0])))

print("\nALL_CHECKS", "PASS" if ok_all else "FAIL")
print("RUN_END_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z"))
