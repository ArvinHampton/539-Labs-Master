# NL derived proposal - non-BPS makeup of the tension-minus-charge gap (2026-11-10, 1130 pursuit)
# Exact tests only: zero tests are sp.expand(...)==0 on polynomials, polynomial remainders
# modulo exact Groebner bases (sin^2+cos^2-1), or exact Rational/Fraction comparisons.
# No simplify()==0, no allclose, no floats in any test.
import sympy as sp
from fractions import Fraction as Fr

ok_all = True; npass = 0; ntot = 0
def check(name, cond):
    global ok_all, npass, ntot
    c = bool(cond); ntot += 1; npass += c; ok_all = ok_all and c
    print(f"[{'PASS' if c else 'FAIL'}] {name}")
def Z(e): return sp.expand(e) == 0
def nonneg_coeffs(expr, gens):
    P = sp.Poly(sp.expand(expr), *gens)
    return all(sp.Rational(co) >= 0 for co in P.coeffs())

# ---------------- B: bookkeeping, sign and range (any M5/anti-M5 mix, signed n) ----------------
Np, Nm, n, m, d, v, w, Q = sp.symbols("Np Nm n m delta v w Q", nonnegative=True)
u = sp.Symbol("u", positive=True)
def T_of(nnet, e_u, uu): return Np + Nm + uu*e_u            # tension in M5 units
# charge: Np - Nm + nnet = Q
# B1 signed identity: T - Q = 2Nm + (u-1) n + eps, eps := u (e_u - n)
nn, eu = sp.symbols("nn e_u", real=True)
Tg = Np + Nm + u*eu; Qg = Np - Nm + nn; epsg = u*(eu - nn)
check("B1 T - Q = 2N_minus + (u-1) n + eps_ex, eps_ex = u(e_u - n) (signed n, any M5/anti-M5 mix)",
      Z(Tg - Qg - (2*Nm + (u-1)*nn + epsg)))
# B2 u >= 1 (u = 1+v): n >= 0 with e_u = n + delta, and n = -m <= 0 with e_u = m + delta
e1 = (Tg - Qg).subs({u: 1+v, nn: n, eu: n+d}); e2 = (Tg - Qg).subs({u: 1+v, nn: -m, eu: m+d})
check("B2 [u>=1] T - Q is a polynomial with nonnegative coefficients in (N-,n|m,delta,v) => N_req >= Q",
      nonneg_coeffs(e1, [Nm, n, d, v]) and nonneg_coeffs(e2, [Nm, m, d, v]))
# B3 [u=1, no anti-M5]: T - Q = eps_ex exactly; eps_ex >= 0
check("B3 [u=1, N-=0] T - Q = eps_ex (gap equals non-BPS excess exactly)",
      Z((Tg - Qg).subs({u: 1, Nm: 0}) - epsg.subs(u, 1)))
# B4 [u<1] (u = 1-w, 0<=w<=1): T - uQ = w N+ + (2-w) N- + (1-w)(e_u - n), each term >= 0
e3 = (Tg - u*Qg).subs(u, 1-w)
check("B4 [u<1] T - u Q = w N+ + (2-w) N- + (1-w)(e_u - n) => N_req >= u Q necessary",
      Z(e3 - (w*Np + (2-w)*Nm + (1-w)*(eu - nn))))
# B5 closure target per branch: eps_ex = Delta_N - (u-1) n  (N- = 0)
DN = sp.Symbol("Delta_N", real=True)
check("B5 closure T = Q + Delta_N  <=>  eps_ex = Delta_N - 2N- - (u-1) n",
      Z((Tg - (Qg + DN)) - (epsg - (DN - 2*Nm - (u-1)*nn))))

# ---------------- P: pointwise Bogomolny both signs (4D fibre) ----------------
g = sp.symbols("g12 g13 g14 g23 g24 g34", real=True)
G = {(1,2):g[0],(1,3):g[1],(1,4):g[2],(2,3):g[3],(2,4):g[4],(3,4):g[5]}
def Fv(i,j): return G[(i,j)] if i<j else (-G[(j,i)] if i>j else 0)
rho4 = sp.Rational(1,2)*sum(x**2 for x in G.values())
q4 = 2*(Fv(1,2)*Fv(3,4) - Fv(1,3)*Fv(2,4) + Fv(1,4)*Fv(2,3))
sd = sum((Fv(*p) - Fv(*s))**2 for p,s in [((1,2),(3,4)),((1,3),(4,2)),((1,4),(2,3))])
asd = sum((Fv(*p) + Fv(*s))**2 for p,s in [((1,2),(3,4)),((1,3),(4,2)),((1,4),(2,3))])
check("P1 rho - q/2 = 1/2 sum (F - *F)^2 and rho + q/2 = 1/2 sum (F + *F)^2  => rho >= |q|/2 pointwise",
      Z(rho4 - q4/2 - sd/2) and Z(rho4 + q4/2 - asd/2))

# ---------------- K: off-shell kinematics: energy unbounded above along A + t a ----------------
y1,y2,t = sp.symbols("y1 y2 t", real=True); phi = sp.Function("phi")(y1,y2)
I = sp.I
T1 = -I/2*sp.Matrix([[0,1],[1,0]]); T2 = -I/2*sp.Matrix([[0,-I],[I,0]]); T3 = -I/2*sp.Matrix([[1,0],[0,-1]])
check("K0 su(2) basis [T1,T2] = T3, -2 tr(Ti Tj) = delta_ij",
      all(Z(x) for x in (T1*T2 - T2*T1 - T3)) and Z(-2*(T3*T3).trace() - 1) and Z((T1*T2).trace()))
a1 = phi*T1; a2 = phi*T2
F12 = t*(sp.diff(a2, y1) - sp.diff(a1, y2)) + t**2*(a1*a2 - a2*a1)
dens = sp.expand(-2*(F12*F12).trace())
check("K1 energy density of t*a is polynomial in t with t^4 coefficient phi^4 > 0 (quartic growth)",
      sp.degree(dens, t) == 4 and Z(sp.Poly(dens, t).coeff_monomial(t**4) - phi**4))
# general bundle: F(A+ta) = F_A + t D_A a + t^2 a^a ; t^4 coefficient of |F|^2 is |a^a|^2 independent of A
A1,A2 = sp.Matrix(2,2,sp.symbols("p0:4")), sp.Matrix(2,2,sp.symbols("q0:4"))
FA = sp.Matrix(2,2,sp.symbols("f0:4")); DAa = sp.Matrix(2,2,sp.symbols("r0:4"))
Ft = FA + t*DAa + t**2*(a1*a2 - a2*a1)
dens2 = sp.expand(-2*(Ft*Ft).trace())
check("K2 any background A: t^4 coefficient of -2tr F12(t)^2 is phi^4 (unbounded above in every bundle)",
      Z(sp.Poly(dens2, t).coeff_monomial(t**4) - phi**4))

# ---------------- W: weighted static equation D(W *F) = 0 ----------------
# W1 off-shell identity d_a(W t_ab) + 1/4 |F|^2 d_b W - F^i_bc (D_a(W F_ac))^i = 0, su(2), flat chart
ys = sp.symbols("x1:5", real=True); Wf = sp.Function("W")(*ys)
Afun = [[sp.Function(f"A{a}_{i}")(*ys) for i in range(3)] for a in range(4)]
eps3 = lambda i,j,k: sp.LeviCivita(i,j,k)
def Fc(a,b,i):
    return sp.diff(Afun[b][i], ys[a]) - sp.diff(Afun[a][i], ys[b]) + sum(eps3(i,j,k)*Afun[a][j]*Afun[b][k] for j in range(3) for k in range(3))
FF = [[[Fc(a,b,i) for i in range(3)] for b in range(4)] for a in range(4)]
F2 = sum(FF[a][b][i]**2 for a in range(4) for b in range(4) for i in range(3))
def tt(a,b): return sum(FF[a][c][i]*FF[b][c][i] for c in range(4) for i in range(3)) - sp.Rational(1,4)*(1 if a==b else 0)*F2
def DW(c,i):   # (D_a (W F_ac))^i
    return sum(sp.diff(Wf*FF[a][c][i], ys[a]) + sum(eps3(i,j,k)*Afun[a][j]*Wf*FF[a][c][k] for j in range(3) for k in range(3)) for a in range(4))
okW1 = True
for b in range(4):
    expr = sum(sp.diff(Wf*tt(a,b), ys[a]) for a in range(4)) + sp.Rational(1,4)*F2*sp.diff(Wf, ys[b]) \
           - sum(FF[b][c][i]*DW(c,i) for c in range(4) for i in range(3))
    okW1 = okW1 and Z(expr)
check("W1 off-shell: d^a(W t_ab) = -1/4|F|^2 d_b W + F_bc.D^a(W F_ac) (non-abelian su(2), flat chart)", okW1)
check("W2 t_ab is traceless in 4D (so t.grad X = 0 for every conformal Killing X)",
      Z(sum(tt(a,a) for a in range(4))))
# W3 round S^4 height h = cos(al): Hess h = -h g in g = dal^2 + sin^2 al g_S3 (warped-product Hessian)
s_, c_ = sp.symbols("s c", real=True)
def Dal(f): return sp.diff(f, s_)*c_ + sp.diff(f, c_)*(-s_)
h = c_; GB = [s_**2+c_**2-1]
red = lambda e: sp.reduced(sp.numer(sp.together(sp.expand(e))), GB, s_, c_)[1]
check("W3 round S^4: h=cos(al) has Hess h = -h g (f''=-f, f' sin cos = -f sin^2) => grad h conformal Killing",
      red(Dal(Dal(h)) + h) == 0 and red(Dal(h)*s_*c_ + h*s_**2) == 0)
check("W4 |grad h|^2 = 1 - h^2 (so X(W) = w'(h)(1-h^2) >= 0 for monotone w, zero only at poles)",
      red(Dal(h)**2 - (1 - h**2)) == 0)
# W5 SD nondegeneracy: v -> v ^ omega injective for SD omega != 0 (det = (a^2+b^2+c^2)^2)
A_,B_,C_ = sp.symbols("a b cc", real=True)
om = {(1,2):A_,(3,4):A_,(1,3):B_,(4,2):B_,(2,4):-B_,(1,4):C_,(2,3):C_}
def omv(i,j):
    if (i,j) in om: return om[(i,j)]
    if (j,i) in om: return -om[(j,i)]
    return 0
# (v ^ omega)_{ijk} = v_i om_jk + v_j om_ki + v_k om_ij ; components ijk in {123,124,134,234}
trip = [(1,2,3),(1,2,4),(1,3,4),(2,3,4)]
M = sp.zeros(4,4)
for r,(i,j,k) in enumerate(trip):
    for l in range(1,5):
        M[r,l-1] = (1 if l==i else 0)*omv(j,k) + (1 if l==j else 0)*omv(k,i) + (1 if l==k else 0)*omv(i,j)
check("W5 SD omega: det(v -> v^omega) = (a^2+b^2+c^2)^2 => dW^F = 0, F SD != 0 forces dW = 0",
      Z(M.det() - (A_**2+B_**2+C_**2)**2) or Z(M.det() + (A_**2+B_**2+C_**2)**2))

# ---------------- C: conformal flatness of the MN2-type fibre g = A dchi^2 + B dOmega^2 + C dpsi^2 ----------------
Xa, Xb = sp.symbols("Xa Xb", positive=True)
st, ct = sp.symbols("st ct", real=True)
GB2 = [s_**2+c_**2-1, st**2+ct**2-1]
def red2(e):
    nu = sp.numer(sp.together(sp.expand(e)))
    return sp.reduced(sp.expand(nu), GB2, s_, c_, st, ct)[1]
def Dchi(f): return sp.diff(f, s_)*c_ - sp.diff(f, c_)*s_
def Dth(f):  return sp.diff(f, st)*ct - sp.diff(f, ct)*st
def weyl(gA, gB, gC):
    gd = [gA, gB, gB*st**2, gC]       # coords: chi, theta, phi, psi ; metric depends on chi (s,c) and theta (st,ct)
    D = [Dchi, Dth, lambda f: 0, lambda f: 0]
    dim = 4
    Gam = [[[0]*dim for _ in range(dim)] for _ in range(dim)]
    for a in range(dim):
        for b in range(dim):
            for c in range(dim):
                val = 0
                if a == b: val += D[c](gd[a])
                if a == c: val += D[b](gd[a])
                if b == c: val -= D[a](gd[b])
                Gam[a][b][c] = sp.together(val/(2*gd[a]))
    def Rup(a,b,c,d):
        r = D[c](Gam[a][d][b]) - D[d](Gam[a][c][b])
        r += sum(Gam[a][c][e]*Gam[e][d][b] - Gam[a][d][e]*Gam[e][c][b] for e in range(dim))
        return sp.together(r)
    Rl = lambda a,b,c,d: gd[a]*Rup(a,b,c,d)
    Ric = [[sp.together(sum(Rup(c,a,c,b) for c in range(dim))) for b in range(dim)] for a in range(dim)]
    Rs = sp.together(sum(Ric[a][a]/gd[a] for a in range(dim)))
    gm = lambda a,b: gd[a] if a==b else 0
    def C(a,b,c,d):
        return Rl(a,b,c,d) - sp.Rational(1,2)*(gm(a,c)*Ric[b][d] - gm(a,d)*Ric[b][c] - gm(b,c)*Ric[a][d] + gm(b,d)*Ric[a][c]) \
               + Rs/6*(gm(a,c)*gm(b,d) - gm(a,d)*gm(b,c))
    return C
gA = s_**2/Xb + c_**2/Xa; gBB = c_**2/Xb; gC = s_**2/Xa
Cw = weyl(gA, gBB, gC)
comps = [(0,1,0,1),(0,3,0,3),(1,3,1,3),(1,2,1,2)]
Csym = {k: sp.together(Cw(*k)) for k in comps}
round_ok = all(red2(Csym[k].subs({Xa: Xb})) == 0 for k in comps)
check("C1 X_a = X_b (round fibre): Weyl components C_0101, C_0303, C_1313, C_1212 reduce to 0 mod sin^2+cos^2-1", round_ok)
pt = {s_: sp.Rational(3,5), c_: sp.Rational(4,5), st: sp.Rational(3,5), ct: sp.Rational(4,5)}
vals = {k: sp.cancel(Csym[k].subs({Xa: 1, Xb: 2}).subs(pt)) for k in comps}
print("   Weyl at X_b/X_a = 2, sin chi = 3/5, sin theta = 3/5:", {str(k): str(vv) for k,vv in vals.items()})
check("C2 X_b/X_a = 2 (MN2 IR ratio): Weyl C_0303 is a nonzero rational at a rational point => fibre not conformally flat",
      vals[(0,3,0,3)].is_Rational and vals[(0,3,0,3)] != 0)
# C3: factor (Xb - Xa) in C_0303 numerator
num0303 = red2(Csym[(0,3,0,3)])
check("C3 numerator of C_0303 (reduced) vanishes identically at X_a = X_b (factor of X_b - X_a)",
      Z(num0303.subs(Xa, Xb)) and not Z(num0303))

# ---------------- F: fibre-trace identity and end-face demand ----------------
D10 = 10; eta = sp.diag(-1, *([1]*9)); SIG = [4,5]; FIB = [6,7,8,9]; Y6 = SIG+FIB
F = sp.zeros(D10,D10); Pff=0; Pm=0; Pss=0
for i,a in enumerate(Y6):
    for b in Y6[i+1:]:
        x = sp.Symbol(f"F{a}{b}", real=True); F[a,b]=x; F[b,a]=-x
        if a in FIB and b in FIB: Pff += x**2
        elif a in SIG and b in SIG: Pss += x**2
        else: Pm += x**2
Fup = eta*F*eta
F2t = sum(F[a,b]*Fup[a,b] for a in range(D10) for b in range(D10))
S = sp.Matrix(D10,D10, lambda a,b: sum(F[a,c]*F[b,dd]*eta[c,dd] for c in range(D10) for dd in range(D10)) - sp.Rational(1,4)*eta[a,b]*F2t)
rho = sp.Rational(1,4)*F2t
trfib = sum(S[a,a] for a in FIB)
check("F1 magnetic Y6 field: tr_fib S = -P_mixed - 2 P_SigmaSigma, and tr_fib S + 4 rho = 2 P_ff + P_mixed >= 0",
      Z(trfib + Pm + 2*Pss) and Z(trfib + 4*rho - (2*Pff + Pm)))
wUV, wIR = Fr(-6,5), Fr(-4,3)
check("F2 end-face demand (J1, CONDITIONAL inputs): tr_fib S_req / rho_req = 4 w_fib = -24/5, -16/3 < -4",
      4*wUV < -4 and 4*wIR < -4 and 4*wUV == Fr(-24,5) and 4*wIR == Fr(-16,3))

# ---------------- Z: odd Z2 doubling acts on eps and Delta_N alike ----------------
Kp, Gp, ep = sp.symbols("Kp Gp ep", positive=True)
check("Z1 doubling [K]=2K+, [S]=2S+ (incl. eps), [G]=2G+: (Delta_N/Q) and (eps/Q) unchanged",
      Z((2*Kp - 2*ep)/(2*Gp) - (Kp - ep)/Gp) and Z((2*ep)/(2*Gp) - ep/Gp))

# ---------------- I: IVT closure bookkeeping on on-record CONDITIONAL test targets ----------------
Qt = 9760; DN_IR, DN_UV = Fr("2808.6"), Fr(10*4880,3) - Qt   # UV: N_req = (5/3) Q exactly (1120 C4e)
check("I1 on-record CONDITIONAL test targets: Delta_N(IR) = 2808.6 > 0 and Delta_N(UV) = 19520/3 > 0 (sign condition B2 met)",
      DN_IR > 0 and DN_UV > 0 and DN_UV == Fr(19520,3))
# UV end round BPS: e_u = n => g_UV(n,u) = u n - n - Delta_N(UV)
gUV = lambda nn_, uu: uu*nn_ - nn_ - DN_UV
check("I2 g_UV < 0: u=1 any n; u=2 for n = 115 (stage-2 IR bracket (110,115]) and all n < 19520/3",
      gUV(115,1) < 0 and gUV(160,1) < 0 and gUV(115,2) < 0 and gUV(6506,2) < 0 and gUV(6507,2) > 0)
check("I3 [u=2] closure needs n <= Delta_N (eps_ex >= 0 in B5): 115 <= 2808.6", Fr(115) <= DN_IR)

print(f"{npass}/{ntot} PASS")
print("ALL PASS" if ok_all else "SOME FAIL")
raise SystemExit(0 if ok_all else 1)
