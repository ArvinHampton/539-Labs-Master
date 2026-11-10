# NL derived proposal - t552u pursuit: non-BPS tension-minus-charge gap, fixed face / flow / profile (2026-11-10)
# Exact tests only: sp.expand(...)==0 on polynomials, polynomial remainders modulo the exact Groebner basis
# {sin^2+cos^2-1}, or exact Rational/Fraction comparisons. No simplify()==0, no allclose, no floats in any test.
import sympy as sp
from fractions import Fraction as Fr

ok_all = True; npass = 0; ntot = 0
def check(name, cond):
    global ok_all, npass, ntot
    c = bool(cond); ntot += 1; npass += c; ok_all = ok_all and c
    print(f"[{'PASS' if c else 'FAIL'}] {name}")
def Z(e): return sp.expand(e) == 0

# ---------------- H1: SO(3)xU(1) on S^4 in R^3 (+) R^2 has no fixed point; every orbit has dim >= 1 ----------------
L = [sp.Matrix([[0,0,0],[0,0,-1],[0,1,0]]), sp.Matrix([[0,0,1],[0,0,0],[-1,0,0]]), sp.Matrix([[0,-1,0],[1,0,0],[0,0,0]])]
J = sp.Matrix([[0,-1],[1,0]])
stack = sp.Matrix.vstack(*L)
check("H1a so(3) generators stacked have rank 3 on R^3 (common fixed vector only x=0); det J = 1 (U(1) fixes only z=0)",
      stack.rank() == 3 and J.det() == 1)
x1,x2,x3,z1,z2 = sp.symbols("x1 x2 x3 z1 z2", real=True)
X = sp.Matrix([x1,x2,x3]); Zv = sp.Matrix([z1,z2])
# generic orbit tangent: Gram determinant of {L_i x} is |x|^2-type; minimal case checks at the two singular orbits
def orbit_rank(xv, zv):
    cols = [sp.Matrix.vstack(Li*xv, sp.zeros(2,1)) for Li in L] + [sp.Matrix.vstack(sp.zeros(3,1), J*zv)]
    return sp.Matrix.hstack(*cols).rank()
check("H1b orbit dims: (e1,0) -> 2 (S^2 orbit), (0,e1) -> 1 (S^1 orbit), (x,z) generic rational point -> 3; fixed point would need x=0 and z=0, not on S^4",
      orbit_rank(sp.Matrix([1,0,0]), sp.Matrix([0,0])) == 2 and orbit_rank(sp.Matrix([0,0,0]), sp.Matrix([1,0])) == 1
      and orbit_rank(sp.Matrix([sp.Rational(3,5),0,0]), sp.Matrix([sp.Rational(4,5),0])) == 3)

# ---------------- H2: strict weighted Bogomolny decomposition ----------------
Wd, Wm, eps_, q_ = sp.symbols("W W_min epsilon q", real=True)
check("H2 W*eps - W_min*q/2 = (W - W_min)*eps + W_min*(eps - q/2)  (each term >= 0 by P1 and W >= W_min)",
      Z(Wd*eps_ - Wm*q_/2 - ((Wd - Wm)*eps_ + Wm*(eps_ - q_/2))))

# ---------------- H4: Riccati lemma ----------------
t = sp.Symbol("t", real=True)
p, q, psi, beta = [sp.Function(nm)(t) for nm in ("p","q","psi","beta")]
lhs = p*sp.diff(beta,t)**2 + q*beta**2 - sp.diff(psi*beta**2, t)
rhs = p*(sp.diff(beta,t) - psi*beta/p)**2 + (q - psi**2/p - sp.diff(psi,t))*beta**2
check("H4 Riccati identity: p b'^2 + q b^2 - (psi b^2)' = p(b' - psi b/p)^2 + (q - psi^2/p - psi') b^2",
      Z(sp.together(lhs - rhs).as_numer_denom()[0]))

# ---------------- H5: the stage-2 reduced unweighted e_u functional, twist lower bound ----------------
# density (y14s2.py, unweighted = weighted/W): s[a'^2/(2G) + h'^2/gtt + (n-a)^2 h^2/gpp + (1-h^2)^2/2] + s(c/2) R2^2 (n-a)^2 / W^2, G = gtt*gpp = s^2
n_, s, gtt, gpp, c, R2, W = sp.symbols("n s g_tt g_pp c R2 W", positive=True)
a1, h, h1 = sp.symbols("a1 h h1", real=True)     # a1 = a', h1 = h'
a_ = sp.Symbol("a", real=True)
dens = s*(a1**2/(2*s**2) + h1**2/gtt + (n_-a_)**2*h**2/gpp + (1-h**2)**2/2) + s*(c/2)*R2**2*(n_-a_)**2/W**2
kept = a1**2/(2*s) + s*(c/2)*R2**2*(n_-a_)**2/W**2
check("H5a e_u density - [a'^2/(2s) + s(c/2)R2^2(n-a)^2/W^2] = s[h'^2/gtt + (n-a)^2h^2/gpp + (1-h^2)^2/2] (sum of squares, dropped)",
      Z(dens - kept - s*(h1**2/gtt + (n_-a_)**2*h**2/gpp + (1-h**2)**2/2)))
b_, b1 = sp.symbols("b b1", real=True)
P_ = 1/(2*s); Q_ = (c/2)*s*R2**2/W**2
check("H5b with a = n(1-beta): kept density = n^2 [p beta'^2 + q beta^2], p = 1/(2s), q = (c/2) s R2^2/W^2",
      Z(kept.subs({a1: -n_*b1, a_: n_*(1-b_)}) - n_**2*(P_*b1**2 + Q_*b_**2)))
phi_ = sp.sqrt(c)/2*R2/W
check("H5c phi := (sqrt c/2) R2/W satisfies phi^2 = p q exactly (s cancels)", Z(phi_**2 - P_*Q_))
# psi = -theta(phi - phi1):  q - psi^2/p - psi' - [(1-theta^2) q - theta |phi'|] = theta^2 phi1 (2 phi - phi1)/p  (>= 0 for 0 <= phi1 <= phi)
th, ph, ph1, dph = sp.symbols("theta phi phi1 dphi", real=True)   # dphi = phi' (<= 0), |phi'| = -dphi
pp, qq = sp.symbols("pp qq", positive=True)
psi_ = -th*(ph - ph1); dpsi = -th*dph
expr = (qq - psi_**2/pp - dpsi) - ((1 - th**2)*qq - th*(-dph))
check("H5d psi = -theta(phi-phi1): q - psi^2/p - psi' = (1-theta^2)q - theta|phi'| + theta^2 phi1(2phi-phi1)/p, using phi^2 = pq",
      Z(sp.expand(expr*pp).subs(ph**2, pp*qq) - sp.expand(th**2*ph1*(2*ph - ph1)).subs(ph**2, pp*qq)))
# geometry: chi' = cos chi (cos chi = sech t); s^2 = gtt*gpp_eff, gtt = sin^2+r cos^2, gpp_eff = r tan^2; R2/W = 1/(Xb(Xa tan^2 + Xb))
sn, cs = sp.symbols("sn cs", real=True); GBc = [sn**2 + cs**2 - 1]
Xa, Xb = sp.symbols("Xa Xb", positive=True); r = Xb/Xa
def Dt(f): return sp.diff(f, sn)*cs*cs + sp.diff(f, cs)*(-sn*cs)      # d/dt with chi' = cos chi
def red(e):
    nu = sp.numer(sp.together(sp.expand(e)))
    return sp.reduced(sp.expand(nu), GBc, sn, cs)[1]
gtt_e = (sn**2/Xb + cs**2/Xa)*cs**2/(cs**2/Xb)    # gcc * dchi^2 / R2 with dchi/dt = cos chi
check("H5e conformal fibre data: g_tt = sin^2 chi + r cos^2 chi, R2/W = 1/(Xb(Xa tan^2 chi + Xb)) (mod sin^2+cos^2-1)",
      red(gtt_e - (sn**2 + r*cs**2)) == 0 and
      red((cs**2/Xb)/(Xa*sn**2 + Xb*cs**2) - 1/(Xb*(Xa*sn**2/cs**2 + Xb))) == 0)
phi_g = sp.sqrt(c)/2/(Xb*(Xa*sn**2/cs**2 + Xb))
s2_g = (sn**2 + r*cs**2)*r*sn**2/cs**2
q_g2 = (c/2)**2*s2_g*(1/(Xb*(Xa*sn**2/cs**2 + Xb)))**4        # q^2 (q > 0)
dphi_g = Dt(phi_g)
target2 = c*cs**2*r*(sn**2 + r*cs**2)/(4*Xa**2*Xb**2)
check("H5f (q/|phi'|)^2 = c cos^2chi r (sin^2chi + r cos^2chi)/(4 Xa^2 Xb^2)  (mod sin^2+cos^2-1)",
      red(q_g2 - target2*dphi_g**2) == 0)
# phi' sign: d phi/dt = -(sqrt c/2) Xa * d(tan^2)/dt / (Xb (Xa tan^2+Xb)^2), d(tan^2)/dt = 2 sin chi / cos^2 chi
check("H5g phi' = -(sqrt c/2) Xa (2 sin chi/cos^2 chi) / (Xb (Xa tan^2 + Xb)^2)  (<= 0 on [0, pi/2))",
      red(dphi_g + sp.sqrt(c)/2*Xa*(2*sn/cs**2)/(Xb*(Xa*sn**2/cs**2 + Xb)**2)) == 0)

# ---------------- H6: MN2 IR face (J1 data, CONDITIONAL inputs): Xa = 2^(-3/5), Xb = 2^(2/5), c = 2^(-2/5) ----------------
XaI, XbI, cI = sp.Integer(2)**sp.Rational(-3,5), sp.Integer(2)**sp.Rational(2,5), sp.Integer(2)**sp.Rational(-2,5)
check("H6a IR data: Xb/Xa = 2, Xa^2 Xb^3 = 1 (X0 = Xb), sqrt(c)/(Xa Xb) = 1, phi(0) = sqrt(c)/(2 Xb^2) = 1/4",
      (XbI/XaI) == 2 and (XaI**2*XbI**3) == 1 and sp.sqrt(cI)/(XaI*XbI) == 1 and sp.sqrt(cI)/(2*XbI**2) == sp.Rational(1,4))
w = sp.Symbol("w", positive=True)     # w = cos^2 chi
phi_w = (sp.sqrt(cI)/2)/(XbI*(XaI*(1-w)/w + XbI))
m2_w = cI*w*2*((1-w) + 2*w)/(4*XaI**2*XbI**2)
check("H6b at IR: phi = w/(2(1+w)) and (q/|phi'|)^2 = w(1+w)/2, w = cos^2 chi (both increasing in w, w decreasing in chi)",
      Z(sp.together(phi_w - w/(2*(1+w))).as_numer_denom()[0]) and Z(m2_w - w*(1+w)/2)
      and Z(sp.together(sp.diff(w/(2*(1+w)), w)*(2*(1+w)**2) - 1).as_numer_denom()[0]) and Z(sp.diff(w*(1+w)/2, w) - (1+2*w)/2))
thI, w1 = Fr(3,10), Fr(1,5)
check("H6c theta = 3/10, cos^2 chi1 = 1/5: (theta/(1-theta^2))^2 = 900/8281 <= w1(1+w1)/2 = 3/25 (Riccati condition on [0, chi1])",
      (thI/(1 - thI**2))**2 <= w1*(1+w1)/2 and (thI/(1 - thI**2))**2 == Fr(900,8281) and w1*(1+w1)/2 == Fr(3,25))
kap = thI*(Fr(1,4) - w1/(2*(1+w1)))
check("H6d kappa_IR = theta (phi(0) - phi(chi1)) = (3/10)(1/4 - 1/12) = 1/20  =>  e_u >= n^2/20 in the ansatz at the MN2 IR face",
      kap == Fr(1,20))
# consistency only (stage-2 printed floats, CONDITIONAL; not evidence): e_u/n at n=1..5 and e_u(100)
st2 = {1: Fr("1.0660517"), 2: Fr("1.1442263"), 3: Fr("1.2291673"), 4: Fr("1.3200442"), 5: Fr("1.4154555")}
check("H6e consistency (not evidence): stage-2 prints satisfy e_u >= n^2/20 (n = 1..5 and e_u(100) = 1180.61 >= 500)",
      all(v*k >= Fr(k*k,20) for k,v in st2.items()) and Fr("1180.61") >= Fr(100*100,20))

# ---------------- A6/G-c: finite candidate charges at a fixed IR face (Delta_N(IR) = 2808.6, CONDITIONAL test target) ----------------
DIR = Fr("2808.6"); DUV = Fr(19520,3)
def nmax(uu, D):
    k = 0
    while uu*Fr(k*k,20) - k <= D: k += 1
    return k - 1
check("Gc1 single block, any N- >= 0: closure needs u n^2/20 - n <= Delta_N(IR): n <= 247 at u=1, n <= 172 at u=2",
      nmax(1, DIR) == 247 and nmax(2, DIR) == 172)
check("Gc2 multi-block (<= 8 commuting SU(2), MP2): each block has n_i^2/20 - |n_i| >= -5, so |n_i| <= 248 at u=1 (Delta + 35 bound)",
      min(Fr(k*k,20) - k for k in range(0, 400)) == -5 and nmax(1, DIR + 35) == 248)

# ---------------- A9-T: endpoint signs, any u in [1, 1 + Delta_UV/n) ----------------
nstar = nmax(1, DIR) + 1
gIR_lb = lambda nn, uu: uu*Fr(nn*nn,20) - nn - DIR
gUV = lambda nn, uu: (uu - 1)*nn - DUV
check("A9a n* = 248: g_IR >= n^2/20 - n - 2808.6 > 0 for all n >= 248 and all u >= 1 (no float enters the IR sign)",
      nstar == 248 and gIR_lb(248, 1) > 0 and gIR_lb(247, 1) <= 0 and all(gIR_lb(k, 1) > 0 for k in range(248, 9761)))
check("A9b g_UV = (u-1)n - 19520/3 < 0: u=1 all n; u=2 for 248 <= n <= 6506; u < 1 + (19520/3)/248 for n=248; n* <= Q = 9760",
      gUV(9760, 1) < 0 and gUV(248, 2) < 0 and gUV(6506, 2) < 0 and gUV(6507, 2) > 0
      and gUV(248, 1 + DUV/248) == 0 and 248 <= 9760)

# ---------------- A12-a: x-block profile closure with smeared anti-M5 density (F = 0) ----------------
qt, Dl = sp.symbols("q_tot Delta", real=True)
qm = Dl/2; qp = qt + Dl/2
check("A12a F=0, q- = Delta/2, q+ = q_tot + Delta/2: charge q+ - q- = q_tot and tension q+ + q- = q_tot + Delta = rho_req/T_M5",
      Z((qp - qm) - qt) and Z((qp + qm) - (qt + Dl)))

print(f"{npass}/{ntot} PASS")
print("ALL PASS" if ok_all else "SOME FAIL")
raise SystemExit(0 if ok_all else 1)
