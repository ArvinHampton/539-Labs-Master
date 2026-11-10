#!/usr/bin/env python3
# PP (Professor Proof) independent exact checks for MR2 filing 9811de14 (backreacted jet / 9760-free delta^2).
# Own code; no MR2 routine imported. Exact SymPy only: expand(...)==0, Poly(...).is_zero, Rational, exact LDL. No floats, no simplify.
import hashlib, datetime, sys, itertools
from zoneinfo import ZoneInfo
_me = open(__file__, 'rb').read()
print("RUN_START_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z"))
print("SCRIPT_SHA256", hashlib.sha256(_me).hexdigest()); sys.stdout.flush()
import sympy as sp
from sympy import Rational as Q, Matrix, zeros, eye, expand, Poly, symbols, diff
print("sympy", sp.__version__)
NP = 0; NF = 0
def check(lbl, c):
    global NP, NF
    c = bool(c)
    if c: NP += 1
    else: NF += 1
    print(("PASS " if c else "FAIL ") + lbl); sys.stdout.flush()

def curvature(g, X, P):
    """PP code: R^a_bcd = d_c G^a_db - d_d G^a_cb + G^a_ce G^e_db - G^a_de G^e_cb at point P (Christoffel-derivative route)."""
    n = len(X)
    g0 = g.subs(P); gi = g0.inv()
    dg = [g.diff(X[k]).subs(P) for k in range(n)]
    d2g = [[g.diff(X[k], X[l]).subs(P) for l in range(n)] for k in range(n)]
    Gl = [[[Q(1,2)*(dg[b][f,c] + dg[c][f,b] - dg[f][b,c]) for c in range(n)] for b in range(n)] for f in range(n)]
    dGl = [[[[Q(1,2)*(d2g[d][b][f,c] + d2g[d][c][f,b] - d2g[d][f][b,c]) for c in range(n)] for b in range(n)] for f in range(n)] for d in range(n)]
    Gu = [[[expand(sum(gi[a,f]*Gl[f][b][c] for f in range(n))) for c in range(n)] for b in range(n)] for a in range(n)]
    dgi = [-gi*dg[d]*gi for d in range(n)]
    dGu = [[[[expand(sum(dgi[d][a,f]*Gl[f][b][c] + gi[a,f]*dGl[d][f][b][c] for f in range(n))) for c in range(n)] for b in range(n)] for a in range(n)] for d in range(n)]
    R = {}
    for a, b, c, d in itertools.product(range(n), repeat=4):
        if c >= d: continue
        v = dGu[c][a][d][b] - dGu[d][a][c][b] + sum(Gu[a][c][e]*Gu[e][d][b] - Gu[a][d][e]*Gu[e][c][b] for e in range(n))
        v = expand(v)
        if v != 0:
            R[(a,b,c,d)] = v; R[(a,b,d,c)] = -v
    Rf = lambda a,b,c,d: R.get((a,b,c,d), 0)
    Ric = Matrix(n, n, lambda b, d: expand(sum(Rf(a,b,a,d) for a in range(n))))
    Rs = expand(sum(gi[b,d]*Ric[b,d] for b in range(n) for d in range(n)))
    return dict(R=Rf, Ric=Ric, Rs=Rs, g0=g0, gi=gi, Gu=Gu, dg=dg)

# ---- V: validation with a coordinate system different from MR2's (stereographic) ----
print("\n== V ==")
x, z = symbols('x z')
gst = (4/(1 + x**2 + z**2)**2)*eye(2)
check("V1 stereographic unit S^2: R = 2 (PP code)", curvature(gst, [x, z], {x: Q(1,3), z: Q(-1,2)})['Rs'] == 2)
gH = eye(2)/z**2  # hyperbolic plane R = -2
check("V2 upper half plane: R = -2 (PP code)", curvature(gH, [x, z], {x: 0, z: Q(3,2)})['Rs'] == -2)

# ---- P1: L-GN corroboration in a D = 5 instance (Lorentzian, non-diagonal, t- AND x-dependent, symbolic h2) ----
print("\n== P1. D=5 instance: g = dy^2 + h(y,t,u,v,w), h = h0 + y h1 + y^2 h2, h2 fully symbolic (10 entries) ==")
y, t, u, v, w = symbols('y t u v w')
X5 = [y, t, u, v, w]; Xt = [t, u, v, w]
c = symbols('c0:10')
h0 = Matrix([[-(1 + t*u/3 + v**2/5), t/7 + u*w/11, v/13, w*t/3],
             [t/7 + u*w/11, 1 + t**2/2 + w/9, u*v/5, Q(1,17)+t/19],
             [v/13, u*v/5, 2 + u*t/7 - w**2/3, v*w/23],
             [w*t/3, Q(1,17)+t/19, v*w/23, 3 + t*v/2 + u**2/29]])
h1 = Matrix([[Q(1,2) + t*v/3, u/5 + w/7, t/11, Q(1,13)],
             [u/5 + w/7, t*u - Q(1,3), v/2, w*t/5],
             [t/11, v/2, Q(2,7) + w*u, t**2/3],
             [Q(1,13), w*t/5, t**2/3, -Q(1,9) + v/4]])
idx = [(i, j) for i in range(4) for j in range(i, 4)]
h2 = zeros(4, 4)
for k_, (i, j) in enumerate(idx):
    h2[i, j] = c[k_]; h2[j, i] = c[k_]
h = h0 + y*h1 + y**2*h2
g5 = zeros(5, 5); g5[0, 0] = 1
g5[1:, 1:] = h
P5 = {y: 0, t: Q(1,2), u: Q(1,3), v: Q(1,5), w: Q(1,7)}
C5 = curvature(g5, X5, P5)
G5 = Matrix(5, 5, lambda a, b: expand(C5['Ric'][a, b] - Q(1,2)*C5['g0'][a, b]*C5['Rs']))
freec = lambda e: all(diff(e, ci) == 0 for ci in c)
check("P1.1 D=5: G_yy free of d_y^2 h", freec(G5[0, 0]))
check("P1.2 D=5: G_ya free of d_y^2 h (a = t,u,v,w)", all(freec(G5[0, a]) for a in range(1, 5)))
Ric0 = C5['Ric'].subs({ci: 0 for ci in c})
check("P1.3 D=5: R_ab = -(1/2) d_y^2 h_ab + (h2-free), unit coefficient", all(expand(C5['Ric'][a+1, b+1] - Ric0[a+1, b+1] + h2[a, b]) == 0 for a in range(4) for b in range(4)))
# Gauss
Ct = curvature(h0, Xt, {t: Q(1,2), u: Q(1,3), v: Q(1,5), w: Q(1,7)})
Pt = {t: Q(1,2), u: Q(1,3), v: Q(1,5), w: Q(1,7)}
hi0 = Ct['gi']
K0 = (h1/2).subs(Pt)
Km = hi0*K0
check("P1.4 D=5 Gauss: 2 G_yy = -r[h] + (tr K)^2 - tr K^2", expand(2*G5[0, 0] - (-Ct['Rs'] + Km.trace()**2 - (Km*Km).trace())) == 0)
# Codazzi with x-dependent K: D_b K^b_a - D_a K at the point
Kx = h1/2
h0i_x = None
dh0 = [h0.diff(Xt[k]).subs(Pt) for k in range(4)]
dK = [Kx.diff(Xt[k]).subs(Pt) for k in range(4)]
dhi = [-hi0*dh0[k]*hi0 for k in range(4)]
Gt = Ct['Gu']  # Gamma^a_bc of h0 at point
Kup = hi0*K0                      # K^b_a  (row b, col a)
dKup = [dhi[k]*K0 + hi0*dK[k] for k in range(4)]   # d_k K^b_a
def divK(a):
    return expand(sum(dKup[b][b, a] for b in range(4)) + sum(Gt[b][b][e]*Kup[e, a] for b in range(4) for e in range(4))
                  - sum(Gt[e][b][a]*Kup[b, e] for b in range(4) for e in range(4)))
dtrK = [expand(dKup[a].trace()) for a in range(4)]
cod = [expand(divK(a) - dtrK[a]) for a in range(4)]
check("P1.5 D=5 Codazzi, sign +: G_ya = D_b K^b_a - D_a K (exact, t- and x-dependent K)", all(expand(G5[0, a+1] - cod[a]) == 0 for a in range(4)))
# P6 (row 6b, B-3): Codazzi with Israel-substituted S. S^b_a = -(2/kappa^2)(K^b_a - delta tr K); D_b delta^b_a trK = d_a trK
kap2 = symbols('kappa2', positive=True)
Sup = -(2/kap2)*(Kup - eye(4)*Kup.trace())
dSup = [-(2/kap2)*(dKup[k] - eye(4)*dKup[k].trace()) for k in range(4)]
def divS(a):
    return expand(sum(dSup[b][b, a] for b in range(4)) + sum(Gt[b][b][e]*Sup[e, a] for b in range(4) for e in range(4))
                  - sum(Gt[e][b][a]*Sup[b, e] for b in range(4) for e in range(4)))
check("P6.1 row 6b LHS (D=5 instance): G_ya(0+) = -(kappa^2/2) D_b S^b_a under K+ - h trK+ = -(kappa^2/2) S", all(expand(G5[0, a+1] + (kap2/2)*divS(a)) == 0 for a in range(4)))

# ---- P3: Israel inversion for a GENERIC (non-diagonal, even non-symmetric) 10x10 mixed S ----
print("\n== P3. Israel/Z2 inversion, generic 10x10 ==")
Sg = Matrix(10, 10, lambda i, j: symbols(f's_{i}_{j}'))
trS = Sg.trace()
Kp = -(kap2/2)*(Sg - eye(10)*trS/9)
check("P3.1 K+ - 1 trK+ = -(kappa^2/2) S (matrix identity, generic)", (Kp - eye(10)*Kp.trace() + (kap2/2)*Sg).applyfunc(expand) == zeros(10, 10))
check("P3.2 tr K+ = kappa^2 trS/18", expand(Kp.trace() - kap2*trS/18) == 0)
check("P3.3 (trK+)^2 - tr K+^2 = (kappa^4/4)((trS)^2/9 - tr S^2), generic", expand(Kp.trace()**2 - (Kp*Kp).trace() - (kap2**2/4)*(trS**2/9 - (Sg*Sg).trace())) == 0)
jg = Matrix(10, 10, lambda i, j: symbols(f'j_{i}_{j}'))   # [K] generic
Sj = -(jg - eye(10)*jg.trace())/kap2
check("P3.4 [K] = 0 <=> S = 0: inverse map [K] = -kappa^2 (S - 1 trS/9) recovers [K]", (-kap2*(Sj - eye(10)*Sj.trace()/9) - jg).applyfunc(expand) == zeros(10, 10))
check("P3.5 traceless parts: [K]~ = -kappa^2 S~ (generic)", ((jg - eye(10)*jg.trace()/10) + kap2*(Sj - eye(10)*Sj.trace()/10)).applyfunc(expand) == zeros(10, 10))

# ---- P4: 4-form stress components in D = 11 (y spacelike normal, one time) ----
print("\n== P4. T_yy, T_ya in D = 11 with G = G_t + dy^H (own index code) ==")
D = 11
eta = [1, -1] + [1]*9
comb = list(itertools.combinations(range(D), 4))
Gs = {cmb: symbols('g_' + '_'.join(map(str, cmb))) for cmb in comb}
def perm_sign(seq):
    s = 1; seq = list(seq)
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]: s = -s
    return s
def G(*ix):
    if len(set(ix)) < 4: return 0
    return perm_sign(ix)*Gs[tuple(sorted(ix))]
def full(ix): return eta[ix[0]]*eta[ix[1]]*eta[ix[2]]*eta[ix[3]]
# ordered-sum contractions via 4! / 3! multiplicities computed explicitly from ordered tuples over combinations
G2 = expand(sum(full(cm)*Gs[cm]**2 for cm in comb)*24)
HH = expand(sum(eta[cm[1]]*eta[cm[2]]*eta[cm[3]]*Gs[cm]**2 for cm in comb if cm[0] == 0)*6)
GtGt = expand(sum(full(cm)*Gs[cm]**2 for cm in comb if cm[0] != 0)*24)
# direct ordered triple sum for G_yPQR G_y^PQR
Gy2 = expand(sum(G(0, *pq)**2*eta[pq[0]]*eta[pq[1]]*eta[pq[2]] for pq in itertools.permutations(range(1, D), 3)))
check("P4.0 G^2 = G_t.G_t + 4 H.H (D=11, exact)", expand(G2 - GtGt - 4*HH) == 0)
check("P4.1 G_yPQR G_y^PQR = H.H (ordered sum, D=11)", expand(Gy2 - HH) == 0)
Tyy = expand(Q(1,12)*(Gy2 - Q(1,8)*G2))
check("P4.2 row 5 in D=11: T_yy = H.H/24 - G_t.G_t/96", expand(Tyy - HH/24 + GtGt/96) == 0)
okya = True
for a in (1, 2, 7, 10):
    full_sum = expand(sum(G(0, *pq)*G(a, *pq)*eta[pq[0]]*eta[pq[1]]*eta[pq[2]] for pq in itertools.permutations(range(D), 3)))
    tan_sum = expand(sum(G(0, *pq)*G(a, *pq)*eta[pq[0]]*eta[pq[1]]*eta[pq[2]] for pq in itertools.permutations(range(1, D), 3)))
    okya &= (expand(full_sum - tan_sum) == 0) and (full_sum != 0)
check("P6.2 row 6b RHS index count (D=11): T_ya = (1/12) G_yPQR G_a^PQR = (1/12) H_bcd G_t,a^bcd (y-legs drop; g_ya = 0)", okya)

# ---- P5: row 6 algebra ----
print("\n== P5. Row 6 algebra ==")
r_, HHs, JJs, trS_, trS2_ = symbols('r HH JJ trS trS2', real=True)
QK = (kap2**2/4)*(trS_**2/9 - trS2_)
Gyy = (-r_ + QK)/2                      # Gauss + Israel/Z2 (row 3 + row 4)
sol = sp.solve(sp.Eq(Gyy, HHs/24 - (JJs/4)/96), HHs)[0]   # Einstein G_yy = T_yy (P-G, unit bulk coupling), G_t.G_t = J.J/4
check("P5.1 row 6: H.H/24 = -r/2 + (kappa^4/8)((trS)^2/9 - trS^2) + J.J/384", expand(sol/24 - (-r_/2 + (kap2**2/8)*(trS_**2/9 - trS2_) + JJs/384)) == 0)
check("P5.2 row 6 inequality: (kappa^4/4)(...) + J.J/192 - r = H.H/12 identically (so H.H>=0 <=> r <= ...)", expand((kap2**2/4)*(trS_**2/9 - trS2_) + JJs/192 - r_ - sol/12) == 0)
tau = symbols('tau', nonnegative=True)
Sm5 = [-tau]*6 + [0]*4
check("P5.3 smeared M5 S = -tau h^(6): (trS)^2/9 - trS^2 = -2 tau^2", expand(sum(Sm5)**2/9 - sum(s**2 for s in Sm5) + 2*tau**2) == 0)

# ---- P7: row 7 examples, own YM stress, and the J coupling ----
print("\n== P7. Row 7 examples ==")
f1, f2, j, lam = symbols('f1 f2 j lam', real=True)
e10 = [-1] + [1]*9
F = zeros(10, 10); F[6, 7], F[7, 6], F[8, 9], F[9, 8] = f1, -f1, f2, -f2
FF = sum(e10[a]*e10[b]*F[a, b]**2 for a in range(10) for b in range(10))
Smix = Matrix(10, 10, lambda a, b: expand(sum(e10[a]*e10[cc]*F[a, cc]*F[b, cc] for cc in range(10)) - (Q(1,4)*FF if a == b else 0)))
Stot = Smix + Matrix(10, 10, lambda a, b: (-tau if (a == b and a <= 5) else 0))
quad = expand(Stot.trace()**2/9 - (Stot*Stot).trace())
rhs = expand(-r_/2 + (kap2**2/8)*quad + 24*j**2/384)
logged = -(3*f1**4*kap2**2 - 2*f1**2*f2**2*kap2**2 + 4*f1**2*kap2**2*tau + 3*f2**4*kap2**2 + 4*f2**2*kap2**2*tau - j**2 + 4*kap2**2*tau**2 + 8*r_)/16
check("P7.1 own YM+M5 stress reproduces MR2's logged H.H/24 polynomial exactly", expand(rhs - logged) == 0)
A = rhs.subs({r_: 1, kap2: 1, f1: 1, f2: 1, tau: 0, j: 0}); B = rhs.subs({r_: -1, kap2: 1, f1: 1, f2: 1, tau: 0, j: 0})
check("P7.2 example A = -3/4, example B = +1/4 (j decoupled)", A == Q(-3,4) and B == Q(1,4))
# J contains c tr F^F proportional to f1 f2 on e^6789 under P-HWbc (grav density off): j = lam f1 f2
Bl = expand(rhs.subs({r_: -1, kap2: 1, f1: 1, f2: 1, tau: 0, j: lam}))
Al = expand(rhs.subs({r_: 1, kap2: 1, f1: 1, f2: 1, tau: 0, j: lam}))
check("P7.3 B robust: with j = lam f1 f2, required H.H/24 = 1/4 + lam^2/16 >= 1/4 for all lam", expand(Bl - Q(1,4) - lam**2/16) == 0)
check("P7.4 A NOT robust: with j = lam f1 f2, required H.H/24 = -3/4 + lam^2/16 (positive for lam^2 > 12)", expand(Al + Q(3,4) - lam**2/16) == 0 and Al.subs(lam, 4) > 0)
Ap = rhs.subs({r_: 1, kap2: 1, f1: 1, f2: 0, tau: 0, j: 0})
check("P7.5 A' (f2 = 0, so tr F^F = 0 and j = 0 is consistent): required H.H/24 = -11/16 < 0", Ap == Q(-11,16))
Slow = Matrix(10, 10, lambda a, b: e10[a]*Stot[a, b])
okn = True
for i in range(1, 10):
    kv = [0]*10; kv[0] = 1; kv[i] = 1
    skk = Poly(expand(sum(kv[a]*kv[b]*Slow[a, b] for a in range(10) for b in range(10))), f1, f2, tau)
    for mon, cf in skk.terms():
        okn &= (cf >= 0) and (mon[0] % 2 == 0) and (mon[1] % 2 == 0)
check("P7.6 J6c: every S(k,k) monomial has nonnegative coefficient and even powers of f1, f2 (so the sign test is valid)", okn)

# ---- P8: row 11 delta^2 coefficients, 11D diagonal wall (PP code), GB = 0 ----
print("\n== P8. 11D diagonal thin wall, delta^2 coefficients (PP code) ==")
ys = symbols('y'); xs = symbols('x0:10'); p = symbols('p0:10'); s = symbols('s0:10'); k = symbols('k0:10'); W = symbols('W')
e11 = [1, -1] + [1]*9
g11 = zeros(11, 11); g11[0, 0] = 1
for a in range(10):
    g11[a+1, a+1] = e11[a+1]*(1 + 2*p[a]*ys + (2*p[a]**2 + s[a] + k[a]*W)*ys**2)   # exp(2A), A' = p, A'' = s + k W  (W = delta weight)
P11 = {ys: 0}; P11.update({xx: 0 for xx in xs})
C11 = curvature(g11, [ys] + list(xs), P11)
gi = C11['gi']; g0 = C11['g0']; Rf = C11['R']; Ric = C11['Ric']; Rs = C11['Rs']
n = 11
Rl = lambda a, b, cc, d: g0[a, a]*Rf(a, b, cc, d)
riem2 = expand(sum(Rl(a, b, cc, d)**2*gi[a, a]*gi[b, b]*gi[cc, cc]*gi[d, d] for a, b, cc, d in itertools.product(range(n), repeat=4) if Rf(a, b, cc, d) != 0))
ric2 = expand(sum(Ric[a, b]**2*gi[a, a]*gi[b, b] for a in range(n) for b in range(n)))
Wt = lambda a, b, cc, d: (Rl(a, b, cc, d) - Q(1, n-2)*(g0[a, cc]*Ric[b, d] - g0[a, d]*Ric[b, cc] - g0[b, cc]*Ric[a, d] + g0[b, d]*Ric[a, cc])
                          + Rs*Q(1, (n-1)*(n-2))*(g0[a, cc]*g0[b, d] - g0[a, d]*g0[b, cc]))
weyl2 = 0
for a, b in itertools.combinations(range(n), 2):
    for cc, d in itertools.combinations(range(n), 2):
        val = expand(Wt(a, b, cc, d))
        if val != 0:
            weyl2 += 4*val**2*gi[a, a]*gi[b, b]*gi[cc, cc]*gi[d, d]
weyl2 = expand(weyl2)
T2 = sum(kk**2 for kk in k); T1 = sum(k)
cW = lambda e: Poly(e, W).coeff_monomial(W**2)
gens = list(k) + list(p) + list(s)
check("P8.1 Riem^2 delta^2 coeff = 4 tr k^2", Poly(expand(cW(riem2) - 4*T2), *gens).is_zero)
check("P8.2 Ric^2 delta^2 coeff = tr k^2 + (tr k)^2", Poly(expand(cW(ric2) - T2 - T1**2), *gens).is_zero)
check("P8.3 R^2 delta^2 coeff = 4 (tr k)^2", Poly(expand(cW(expand(Rs**2)) - 4*T1**2), *gens).is_zero)
check("P8.4 Weyl^2 (explicit Weyl tensor) delta^2 coeff = (32/9)(tr k^2 - (tr k)^2/10)", Poly(expand(cW(weyl2) - Q(32,9)*(T2 - T1**2/10)), *gens).is_zero)
check("P8.5 Gauss-Bonnet combination delta^2 coeff = 0", Poly(expand(cW(expand(riem2 - 4*ric2 + Rs**2))), *gens).is_zero)
check("P8.6 highest power of W in each square is 2 (delta^2, no higher)", all(Poly(e, W).degree() <= 2 for e in (riem2, ric2, weyl2)))
Lm, Dm = (eye(10) + sp.ones(10, 10)).LDLdecomposition()
check("P8.7 K4: I + 11^T exact LDL pivots all > 0 (Ric^2 form positive definite)", all(Dm[i, i] > 0 for i in range(10)))
# null-positivity (K6) with own construction, plus M5 piece
Fs = {(a, b): symbols(f'F{a}_{b}') for a in range(10) for b in range(a+1, 10)}
Fc = lambda a, b: 0 if a == b else (Fs[(a, b)] if a < b else -Fs[(b, a)])
tot = 0
for i in range(1, 10):
    for sg in (1, -1):
        kv = [0]*10; kv[0] = 1; kv[i] = sg
        Fk = [sum(kv[a]*Fc(a, cc) for a in range(10)) for cc in range(10)]
        tot += sum(e10[cc]*Fk[cc]**2 for cc in range(10))
tot = expand(tot)
Hm = sp.hessian(tot, list(Fs.values()))/2
Lm, Dm = Hm.LDLdecomposition()
piv = sorted(Dm[i, i] for i in range(Dm.shape[0]))
check("P8.8 K6: sum over k = t +- e_i of |F(k,.)|^2 positive definite; pivots 16 (x9) and 4 (x36)", piv == [4]*36 + [16]*9)
okm5 = True
for i in range(1, 10):
    kv = [0]*10; kv[0] = 1; kv[i] = 1
    sM = sum(kv[a]*kv[b]*(e10[a]*(-tau if (a == b and a <= 5) else 0)) for a in range(10) for b in range(10))
    okm5 &= expand(sM - (tau if i >= 6 else 0)) == 0
check("P8.9 M5 (worldvolume 0..5 incl. t): S(k,k) = tau for transverse k, 0 for worldvolume k", okm5)

# ---- P9: profile identity ----
print("\n== P9. profile integrals ==")
sv, eps = symbols('s epsilon', positive=True)
th = sp.tanh(sv)
dd = sp.diff(th - th**3/3, sv) - sp.sech(sv)**4
check("P9.1 d/ds(tanh - tanh^3/3) = sech^4 (exact, exp form)", expand(sp.together(dd.rewrite(sp.exp))) == 0)
check("P9.2 limits: [tanh - tanh^3/3] from -oo to oo = 4/3", sp.limit(th - th**3/3, sv, sp.oo) - sp.limit(th - th**3/3, sv, -sp.oo) == Q(4,3))
# phi_eps = sech^2(y/eps)/(2 eps): int phi = 1, int phi^2 = (1/(4 eps^2)) * eps * 4/3 = 1/(3 eps)
check("P9.3 int phi_eps = (1/(2eps)) * eps * 2 = 1 and int phi_eps^2 = (1/(4 eps^2)) * eps * 4/3 = 1/(3 eps)",
      (sp.limit(th, sv, sp.oo) - sp.limit(th, sv, -sp.oo))*eps/(2*eps) == 1 and expand(Q(4,3)*eps/(4*eps**2) - 1/(3*eps)) == 0)

print("\nPASS_COUNT", NP, "FAIL_COUNT", NF)
print("ALL_CHECKS", "PASS" if NF == 0 else "FAIL")
print("RUN_END_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z"))
