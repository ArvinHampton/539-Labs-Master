# MR2 · MN2 · KK Group A: scalar and vector masses (CGR consistent truncation, exact sympy)
# Inputs (stated premises):
#   CGR = Cheung-Gauntlett-Rosen arXiv:1906.08900v2, LaTeX source (e-print sha256 of gunzipped tex
#   c8dac903...), eqs (ellkin),(ellpot) [N=4 7D->5D on Sigma_2] and (afredfnrwo) [N=2 SO(2)_D truncation].
#   Vacuum (CGR 6.1): l=-1, e^{30 phi}=2, e^{10 lambda}=2, T=1, psi=0; g^2 L^2 = 2^{4/3} (checked below).
# Conventions: Lagrangian L = R - K_ij d x^i d x^j - V,  V = -(L_pot coefficient of vol5).
#   AdS5: V0 = -12/L^2.  Scalar masses: eig((2K)^{-1} Hess V).  Vector: eig(a^{-1} M).
# Memory-light: exact rationals/radicals only, no big symbolic simplify.
import sympy as sp, itertools, cmath, math, sys
print("python", sys.version.split()[0], "sympy", sp.__version__)
g = sp.Symbol('g', positive=True)
l = -1
two = sp.Integer(2)

# ---------------- [N4] full N=4 potential over phi, lambda, T (5), psi (6) ----------------
ph, la = sp.symbols('phi lam', real=True)
t = sp.symbols('t1:6', real=True)           # traceless symmetric generator of T = exp(tm)
p = sp.symbols('p1:7', real=True)           # psi^{a alpha}: a=1,2 ; alpha=1..3
tm = sp.Matrix([[t[0], t[2], t[3]], [t[2], t[1], t[4]], [t[3], t[4], -t[0]-t[1]]])
# T to second order (enough for Hessian at t=0): T = 1 + tm + tm^2/2 ; T^{-1} = 1 - tm + tm^2/2
I3 = sp.eye(3)
T = I3 + tm + tm*tm/2
Ti = I3 - tm + tm*tm/2
psi = [sp.Matrix([p[0], p[1], p[2]]), sp.Matrix([p[3], p[4], p[5]])]   # psi^a as 3-vectors
eps2 = [[0, 1], [-1, 0]]
psi2 = sum(x**2 for x in p)
psiTpsi = sum((psi[a].T*T*psi[a])[0] for a in range(2))
psiTipsi = sum((psi[a].T*Ti*psi[a])[0] for a in range(2))
quart = 0
for a, b, c, d in itertools.product(range(2), repeat=4):
    e = eps2[a][b]*eps2[c][d]
    if e: quart += e*(psi[a].T*Ti*psi[c])[0]*(psi[b].T*Ti*psi[d])[0]
trT = T.trace(); trT2 = (T*T).trace()
Lpot = g**2*(-sp.Rational(1, 2)*sp.exp(12*la-16*ph)*(l-psi2)**2
             - sp.exp(-8*la-16*ph)*quart
             + sp.exp(-10*ph)*(2*(l+psi2) - sp.exp(10*la)*psiTpsi - sp.exp(-10*la)*psiTipsi)
             + sp.Rational(1, 2)*sp.exp(-4*ph)*(sp.exp(8*la)*trT**2 - 2*sp.exp(8*la)*trT2 + 4*sp.exp(-2*la)*trT))
V4 = -Lpot
vars4 = [ph, la] + list(t) + list(p)
vac4 = {ph: sp.log(2)/30, la: sp.log(2)/10}
vac4.update({x: 0 for x in list(t)+list(p)})
def ev(e): return sp.nsimplify(sp.simplify(e.subs(vac4)))
V0 = ev(V4)
L2 = sp.simplify(-12/V0)
print("[N4] V0 =", V0, "  L^2 =", L2, "  g^2 L^2 =", sp.simplify(g**2*L2), " target 2^(4/3):", sp.simplify(g**2*L2 - two**sp.Rational(4, 3)) == 0)
grad = [ev(sp.diff(V4, x)) for x in vars4]
print("[N4] gradient at vacuum (all 13 must be 0):", grad, all(x == 0 for x in grad))
H = sp.zeros(13, 13)
for i in range(13):
    di = sp.diff(V4, vars4[i])
    for j in range(i, 13):
        H[i, j] = H[j, i] = ev(sp.diff(di, vars4[j]))
# kinetic K at vacuum: phi,lam: 30 each; T: (1/4) tr(dT dT) at T=1 -> (1/4)tr(dtm^2); psi: e^{2lam-6phi} delta
dt = sp.symbols('d1:6')
dtm = tm.subs(dict(zip(t, dt)))
Kt = sp.expand(sp.Rational(1, 4)*(dtm*dtm).trace())
K = sp.zeros(13, 13); K[0, 0] = 30; K[1, 1] = 30
for i in range(5):
    for j in range(5):
        K[2+i, 2+j] = sp.Rational(1, 2)*sp.diff(Kt, dt[i], dt[j])
kpsi = sp.nsimplify(sp.simplify(sp.exp(2*la-6*ph).subs(vac4)))
for i in range(6): K[7+i, 7+i] = kpsi
M2 = sp.simplify((2*K).inv()*H*L2)
blocks = {'phi,lam': [0, 1], 'T(5)': list(range(2, 7)), 'psi(6)': list(range(7, 13))}
# block-diagonality check (no singlet/5-plet/psi mixing)
off = [M2[i, j] for i in range(13) for j in range(13)
       if not any(i in b and j in b for b in blocks.values())]
print("[N4] off-block mass-matrix entries all zero:", all(sp.simplify(x) == 0 for x in off))
for name, idx in blocks.items():
    sub = M2.extract(idx, idx)
    evs = sub.eigenvals()
    print("[N4] block", name, "m^2 L^2 eigenvalues {value: mult}:", {sp.nsimplify(sp.simplify(k)): v for k, v in evs.items()})
sub = M2.extract([0, 1], [0, 1])
for val, mult, vecs in sub.eigenvects():
    v = vecs[0]; r = sp.simplify(v[0]/v[1]) if v[1] != 0 else 'inf'
    D = 2 + sp.sqrt(4 + val)
    print("[N4] (phi,lam) eigen m2L2 =", sp.simplify(val), " Delta =", sp.simplify(D), " direction dphi:dlam =", r, " falloff exponents {Delta-4? i.e. 4-Delta, -Delta}:", sp.simplify(4-D), ",", sp.simplify(-D))

# ---------------- [N2] SO(2)_D truncation (CGR afredfnrwo) incl. w and Z1 control ----------------
S, O, vp, z1, z2 = sp.symbols('Sigma Omega varphi z1 z2', positive=True)
zz = z1**2 + z2**2
br = (2*l*sp.exp(2*vp)*O*S**3 - sp.Rational(1, 2)*sp.exp(4*vp)*(l-2*zz)**2 - 2*sp.exp(4*vp)*O**2*S**6*zz**2
      - sp.Rational(1, 2)*sp.exp(4*vp)*O**4 + 4*O*S**3 + 2*sp.exp(2*vp)*O**2 + 2*sp.exp(2*vp)*O**3*S**3
      - 2*sp.exp(2*vp)*(1-O*S**3)**2*zz)
V2 = -g**2*O**-2*S**-2*br
vars2 = [S, O, vp, z1, z2]
vac2 = {S: two**sp.Rational(-1, 3), O: 1, vp: 0, z1: 0, z2: 0}
V20 = sp.nsimplify(sp.simplify(V2.subs(vac2)))
print("[N2] V0 =", V20, " equals N4 V0:", sp.simplify(V20 - V0) == 0)
g2 = [sp.simplify(sp.diff(V2, x).subs(vac2)) for x in vars2]
print("[N2] gradient (z-derivs taken at z->0):", g2)
H2 = sp.Matrix(5, 5, lambda i, j: sp.simplify(sp.diff(V2, vars2[i], vars2[j]).subs(vac2)))
K2 = sp.diag(3*S**-2, O**-2, 2, 2*sp.exp(2*vp), 2*sp.exp(2*vp)).subs(vac2)
M22 = sp.simplify((2*K2).inv()*H2*L2)
print("[N2] scalar m^2L^2 {value: mult}:", {sp.nsimplify(sp.simplify(k)): v for k, v in M22.eigenvals().items()})
# translate to (phi,lam,w): Sigma=e^{-(phi+3lam)}, Omega=e^{3phi-lam-w}, varphi=lam-3phi-w/2
f, lm, w = sp.symbols('f lm w', real=True)
sub3 = {S: sp.exp(-(f+3*lm)), O: sp.exp(3*f-lm-w), vp: lm-3*f-w/2, z1: 0, z2: 0}
V3 = V2.subs(sub3)
vac3 = {f: sp.log(2)/30, lm: sp.log(2)/10, w: 0}
Hw = [sp.nsimplify(sp.simplify(sp.diff(V3, a, b).subs(vac3))) for a, b in [(w, w), (w, f), (w, lm)]]
print("[Z1] d2V/dw2, d2V/dw dphi, d2V/dw dlam at MN2:", Hw)
# kinetic for w from N=2 kinetic terms: Omega^-2 dOmega^2 + 2 dvarphi^2 restricted to dw: 1 + 2*(1/4) = 3/2
Kw = sp.Rational(1) + 2*sp.Rational(1, 4)
mw = sp.simplify(Hw[0]/(2*Kw)*L2)
print("[Z1] w kinetic coeff K_ww =", Kw, " m_w^2 L^2 =", mw, " Delta =", 2+sp.sqrt(4+mw), " exponents {4-Delta? Delta-? }: second-order exponents {0, 4}:", (0, 4) if mw == 0 else 'n/a')
d3 = sp.nsimplify(sp.simplify(sp.diff(V3, w, 3).subs(vac3)))
print("[Z1] d3V/dw3 at MN2 =", d3, "  PP value -24*2^(2/3) g^2 ; ratio =", sp.nsimplify(sp.simplify(d3/(-24*two**sp.Rational(2, 3)*g**2))))
print("[Z1] cross-check vs N4: w = diag(e^w,e^w,e^-2w) means tm=diag(w,w,-2w); N4 T-block mass 0 above")

# ---------------- [VEC] vectors in N=2 truncation: (A, A12, B=Ascr - l*A12) ----------------
# -1/2 a *F^F == -1/4 a F_{mn}F^{mn}; mass term -1/2 e^{4varphi} g^2 Ascr^2, Ascr = B + l*A12
a = sp.diag(S**-4, S**2*O**2, S**2*O**-2).subs(vac2)
vv = sp.Matrix([0, l, 1])
Mv = (g**2*sp.exp(4*vp)).subs(vac2)*vv*vv.T
mv = sp.simplify(a.inv()*Mv*L2)
print("[VEC] vector m^2L^2 {value: mult}:", {sp.simplify(k): v for k, v in mv.eigenvals().items()})
print("[VEC] null vectors (massless):", [list(x) for x in mv.nullspace()])
print("[VEC] CGR (6.3) massive triplet: 2^{5/3} g^2 L^2 =", sp.simplify(two**sp.Rational(5, 3)*g**2*L2))
print("[VEC] Delta = 2+sqrt(1+m2L2) for m2L2=0,8:", [2+sp.sqrt(1+xx) for xx in (0, 8)])
print("[VEC] N4: A^{alpha beta} mass terms come only from D T and D psi; at T=1, psi=0: g(A^{ab}+A^{ba})=0 (antisym) -> massless triplet; A(1) couples only via D psi, D K -> massless at psi=K=0")

# ---------------- [DOF] counting ----------------
print("[DOF] scalars: phi,lam(2)+T(5)+psi(6)=13 physical + 3 Stueckelberg xi^alpha = 16 = 1 + 3*5 (N=4 gravity + 3 vector multiplets):", 2+5+6+3 == 1+3*5)
print("[DOF] vector-like: A(1)+A^alpha(3)+chi^alpha(3)+K^a(2) = 9 = 6 + 3:", 1+3+3+2 == 6+3)

# ---------------- [G] Aut+ on H^{1,0} and H^0(K^2) ----------------
# Curve y^2 = x^5 - x.  Lifts (exact check below): g1: x->i x, y->zeta8*y ; g2: x->(x+1)/(1-x), y-> 2*sqrt(2)*I*y/(1-x)^3 ; J: y->-y
# (dry-run note: a first draft used 2*sqrt(2) without I; the exact curve check below rejects it, and it generated 96 matrices incl. iI.)
x, y = sp.symbols('x y')
f_ = lambda u: u**5 - u
z8 = sp.exp(sp.I*sp.pi/4)
lifts = {'g1': (sp.I*x, z8), 'g2': ((x+1)/(1-x), 2*sp.sqrt(2)*sp.I/(1-x)**3)}
for nm, (xm, yc) in lifts.items():
    chk = sp.simplify(sp.expand((yc**2)*f_(x) - f_(xm)))
    print("[G] exact curve check y'^2 - f(x') = 0 on curve for", nm, ":", chk == 0)
    assert chk == 0
bad = sp.simplify(sp.expand((2*sp.sqrt(2)/(1-x)**3)**2*f_(x) - f_((x+1)/(1-x))))
print("[G] draft lift without I fails the curve check:", bad != 0)
def pullback(xmap, ycoef_expr):
    cols = []
    for k in range(2):
        e = sp.expand(sp.cancel(sp.simplify(xmap**k*sp.diff(xmap, x)/ycoef_expr)))
        P = sp.Poly(e, x); assert P.degree() <= 1, e
        cols.append([P.coeff_monomial(1), P.coeff_monomial(x)])
    return sp.Matrix(cols).T
G1 = pullback(*lifts['g1']); G2 = pullback(*lifts['g2']); GJ = -sp.eye(2)
print("[G] exact generator matrices on (dx/y, x dx/y):", sp.simplify(G1).tolist(), sp.simplify(G2).tolist(), GJ.tolist())
import numpy as np
from collections import Counter
gn = [np.array(sp.N(M, 30).tolist(), dtype=complex) for M in (G1, G2, GJ)]
keyf = lambda A: tuple(np.round(A, 9).flatten())
els = {keyf(np.eye(2)): np.eye(2, dtype=complex)}; fr = [np.eye(2, dtype=complex)]
while fr:
    nf = []
    for A in fr:
        for B in gn:
            C = A @ B
            if keyf(C) not in els: els[keyf(C)] = C; nf.append(C)
    fr = nf
def order(A):
    B = A; k = 1
    while not np.allclose(B, np.eye(2)): B = B @ A; k += 1
    return k
n = len(els)
print("[G] order of matrix group on H^{1,0} (float closure, entries in Q(zeta8)):", n,
      " element orders:", dict(sorted(Counter(order(A) for A in els.values()).items())), " (GL(2,3): {1:1,2:13,3:8,4:6,6:8,8:12})")
ch1 = np.mean([np.trace(A) for A in els.values()])
ch1r = np.mean([2*np.trace(A).real for A in els.values()])
ch2 = np.mean([(np.trace(A)**2 + np.trace(A @ A))/2 for A in els.values()])
print("[G] trivial multiplicity: H^{1,0}:", np.round(ch1, 12), " H^1(Sigma,R):", np.round(ch1r, 12), " H^0(K^2)=Sym^2 H^0(K):", np.round(ch2, 12))
print("[G] exact: J = -I on H^{1,0} => no J-invariant (hence no Aut+-invariant) vector in H^1; J acts as (+1) on Sym^2 (quadratic differentials)")

# ---------------- [JS] J-sign / weight table for Sigma-leg modes (S1) ----------------
# At a Weierstrass point (J-fixed) dJ = -1 on T_p Sigma. Canonical undressed lift: twisted bundle V ~ T Sigma acted on by dJ.
# A mode in K^m (x) V^q (complex weight m - q relative to functions) has fibre J-sign (-1)^(m-q) at fixed points.
rows = [("phi,lam,T,A(1),A^ab,chi^a ^vol, h^a (Sigma scalars / vol_Sigma)", 0, 0),
        ("psi^{a alpha} ebar^a (x) E_a  [T*Sigma (x) V, weight-0 part]", 1, 1),
        ("K^a_(2) ^ ebar^a  [T*Sigma (x) V, weight-0 part]", 1, 1),
        ("SO(5)(2,3) Sigma-leg, weight +-2 part  [K^2 (x) V^0 ...]", 2, 0),
        ("Wilson lines of SU(2)_R / U(1)_r along harmonic 1-forms [T*Sigma, untwisted index]", 1, 0),
        ("C3 with one Sigma leg along harmonic 1-form (untwisted)", 1, 0),
        ("g_{mu m} vectors from 1-forms on Sigma (untwisted)", 1, 0)]
for name, m, q in rows:
    print("[JS] %-85s weight m-q=%d  fibre J-sign %+d" % (name, m-q, (-1)**(m-q)))

# ---------------- [CGU] Chen-Gutperle-Uhlemann 1903.07109 universal spin-2 check ----------------
j = sp.Symbol('j', nonnegative=True, integer=True)
m2spin2 = 2*j*(j+3) + 2*j*(j+1)          # stage-1 formula at lambda_Sigma=0, ell=j, q=0
Dl2 = 2 + sp.sqrt(4 + m2spin2)
print("[CGU] stage-1 Delta_2(ell=j,n=0,q=0,lambda=0) - (2j+4) =", sp.simplify(sp.sqrt(sp.expand(4+m2spin2)) - (2*j+2)), "(sqrt(4j^2+8j+4) = 2j+2 for j>=0)", sp.factor(4+m2spin2))
for jj in range(4):
    D0 = 2+2*jj
    print("[CGU] j=%d: spin-2 m2L2=%d Delta=%d ; A2A2bar primary [0,0]^(2j;0) Delta0=%d m2L2=%d ; QQbar vector Delta=%d m2L2=%d" % (
        jj, 2*jj*(jj+3)+2*jj*(jj+1), 2*jj+4, D0, D0*(D0-4), D0+1, D0*(D0-2)))
print("[CGU] generic (non-universal) stage-1 levels, e.g. 20 (j=0, ell=2): Delta_2 = 2+2*sqrt(6) irrational -> not of CGU form 4+2l+n -> multiplet position OPEN")
print("[BF] min scalar m2L2 in N=4 truncation:", min([sp.nsimplify(k) for k in M2.eigenvals().keys()]), " BF bound -4; strict violation:", any(sp.N(k) < -4 for k in M2.eigenvals().keys()))
print("DONE")
