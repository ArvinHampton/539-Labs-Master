# PP independent exact checks for NL gap filing debc7d52 (t552u). Audit-side checks only; not a first proof.
# Tools: sympy expand()==0, together/as_numer_denom on rational functions, sympy Matrix rank/nullspace on exact
# integer/symbolic matrices, and fractions.Fraction. No simplify, no nsimplify, no floats, no numpy, no allclose.
import sympy as sp
from fractions import Fraction as Fr
res = []
def chk(name, cond):
    c = bool(cond); res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {name}")
def Z(e): return sp.expand(e) == 0
def ZR(e):  # rational function zero test: numerator of together() expands to 0
    return sp.expand(sp.together(e).as_numer_denom()[0]) == 0

# ---- H1 (general, not instance): SO(3) generators L_i x = e_i x x ; [x]_x has adj = x x^T, det 0 => rank 2 for x != 0
x = sp.Matrix(sp.symbols("x1:4", real=True))
Xc = sp.Matrix([[0,-x[2],x[1]],[x[2],0,-x[0]],[-x[1],x[0],0]])
Ls = [sp.Matrix([[0,0,0],[0,0,-1],[0,1,0]]), sp.Matrix([[0,0,1],[0,0,0],[-1,0,0]]), sp.Matrix([[0,-1,0],[1,0,0],[0,0,0]])]
M = sp.Matrix.hstack(*[Li*x for Li in Ls])
chk("PG1 H1: [L1x L2x L3x] = -[x]_x ; det = 0 ; adj([x]_x) = x x^T (so rank exactly 2 iff x != 0) ; nullspace of stacked L_i is {0} ; J z = 0 iff z = 0 (det J = 1)",
    all(Z(e) for e in (M + Xc)) and Z(Xc.det()) and all(Z(e) for e in (Xc.adjugate() - x*x.T))
    and sp.Matrix.vstack(*Ls).nullspace() == [] and sp.Matrix([[0,-1],[1,0]]).det() == 1)

# ---- P1 / GB2 pointwise Bogomolny (premise of H2): per Lie-algebra component, orthonormal 4-frame
f = sp.symbols("f12 f13 f14 f23 f24 f34", real=True); f12,f13,f14,f23,f24,f34 = f
two_eps = sum(v**2 for v in f)                       # 2*eps per component = sum_{a<b} F_ab^2
pf = 2*(f12*f34 - f13*f24 + f14*f23)                 # = (1/4) eps^{abcd}F_ab F_cd * 2 (q density per component, up to the common unit)
chk("PG2 P1: sum F_ab^2 -/+ 2(F12F34 - F13F24 + F14F23) = (F12-/+F34)^2 + (F13+/-F24)^2 + (F14-/+F23)^2 (so eps >= |q|/2 pointwise)",
    Z(two_eps - pf - ((f12-f34)**2 + (f13+f24)**2 + (f14-f23)**2)) and Z(two_eps + pf - ((f12+f34)**2 + (f13-f24)**2 + (f14+f23)**2)))
W, Wm, e_, q_ = sp.symbols("W W_min eps q", real=True)
chk("PG3 H2 identity W eps - W_min q/2 = (W-W_min) eps + W_min (eps - q/2)", Z(W*e_ - Wm*q_/2 - (W-Wm)*e_ - Wm*(e_ - q_/2)))

# ---- H4 Riccati, with derivatives as independent symbols (b1 = beta', s1 = psi'), multiplied by p
p, q, ps, b, b1, s1 = sp.symbols("p q psi beta beta1 psi1", real=True)
lhs = p*b1**2 + q*b**2 - (s1*b**2 + 2*ps*b*b1)
rhs = p*(b1 - ps*b/p)**2 + (q - ps**2/p - s1)*b**2
chk("PG4 H4 Riccati identity (times p, polynomial): p b'^2 + q b^2 - (psi b^2)' = p(b'-psi b/p)^2 + (q - psi^2/p - psi')b^2", Z(sp.expand(p*(lhs - rhs))))

# ---- H5a-b against y14s2.py stage-2 density (unweighted = weighted/W): fib/W = s[a'^2/(2G)+h'^2/gtt+(n-a)^2h^2/gpp+(1-h^2)^2/2], tw/W = s(c/2)R2^2(n-a)^2/W^2, G = s^2
n, s, gtt, gpp, c, R2, Wv = sp.symbols("n s gtt gpp c R2 Wv", positive=True)
a, a1, h, h1, be, be1 = sp.symbols("a a1 h h1 beta beta1", real=True)
weighted = s*Wv*(a1**2/(2*s**2) + h1**2/gtt + (n-a)**2*h**2/gpp + (1-h**2)**2/2) + s*(c/2)*R2**2*(n-a)**2/Wv
unw = weighted/Wv
kept = a1**2/(2*s) + s*(c/2)*R2**2*(n-a)**2/Wv**2
chk("PG5 H5a unweighted y14s2 density - kept = s[h'^2/gtt + (n-a)^2 h^2/gpp + (1-h^2)^2/2] (>= 0)",
    ZR(unw - kept - s*(h1**2/gtt + (n-a)**2*h**2/gpp + (1-h**2)**2/2)))
P_ = 1/(2*s); Q_ = (c/2)*s*R2**2/Wv**2
chk("PG6 H5b a = n(1-beta): kept = n^2 (p beta'^2 + q beta^2); H5c (sqrt(c)/2 R2/W)^2 = p q",
    ZR(kept.subs({a1: -n*be1, a: n*(1-be)}) - n**2*(P_*be1**2 + Q_*be**2)) and ZR((sp.sqrt(c)/2*R2/Wv)**2 - P_*Q_))
# Bogomolny normalization of y14s2 units (untwisted, W=1): fib - (s/2)(a'/s-(1-h^2))^2 - s(h'/sqrt(gtt)-(n-a)h/sqrt(gpp))^2 = d/dt[a(1-h^2)+n h^2]
sg, sp_ = sp.symbols("sgtt sgpp", positive=True)   # sqrt(gtt), sqrt(gpp); s = sgtt*sgpp
ss = sg*sp_
fib1 = ss*(a1**2/(2*ss**2) + h1**2/sg**2 + (n-a)**2*h**2/sp_**2 + (1-h**2)**2/2)
bogsq = (ss/2)*(a1/ss - (1-h**2))**2 + ss*(h1/sg - (n-a)*h/sp_)**2
total_deriv = a1*(1-h**2) + a*(-2*h*h1) + n*2*h*h1
chk("PG7 units: untwisted unweighted density = Bogomolny squares + d/dt[a(1-h^2) + n h^2]; with a(0)=0,h(0)=0,a(inf)=n,h(inf)=1 BPS e_u = n (so n^2/20 is in the same units as n)",
    ZR(fib1 - bogsq - total_deriv))

# ---- H5d
th, ph, ph1, dph, pp, qq = sp.symbols("theta phi phi1 dphi pp qq", real=True)
psi_ = -th*(ph - ph1); dpsi = -th*dph
# use phi^2 = pp*qq by substituting qq = phi^2/pp
e1 = (qq - psi_**2/pp - dpsi) - ((1 - th**2)*qq + th*dph + th**2*ph1*(2*ph - ph1)/pp)
chk("PG8 H5d with q = phi^2/p: q - psi^2/p - psi' = (1-theta^2)q - theta|phi'| + theta^2 phi1(2phi - phi1)/p  (phi' = -|phi'|)",
    ZR(e1.subs(qq, ph**2/pp)))

# ---- H5e-g in w = cos^2 chi (independent of the sin/cos Groebner route). T = tan^2 = (1-w)/w ; dT/dt = 2 sin chi/cos^2 chi, so (dT/dt)^2 = 4(1-w)/w^2
w = sp.Symbol("w", positive=True); Xa, Xb = sp.symbols("Xa Xb", positive=True); r = Xb/Xa
T = (1-w)/w
gcc = (1-w)/Xb + w/Xa; R2w = w/Xb; Wf = Xa*(1-w) + Xb*w
gtt_w = gcc*w/R2w             # dchi/dt = cos chi => dchi^2 = w dt^2
gpp_w = ((1-w)/Xa)/R2w
chk("PG9 H5e: g_tt = (1-w) + r w ; g_pp,eff = r T ; R2/W = 1/(Xb(Xa T + Xb))",
    ZR(gtt_w - ((1-w) + r*w)) and ZR(gpp_w - r*T) and ZR(R2w/Wf - 1/(Xb*(Xa*T + Xb))))
Tt = sp.Symbol("T", positive=True)
phiT = sp.sqrt(c)/2/(Xb*(Xa*Tt + Xb))
dphidT = sp.diff(phiT, Tt)
chk("PG10 H5g: dphi/dT * Xb (Xa T + Xb)^2 = -(sqrt c/2) Xa  (< 0) ; dT/dchi = 2 tan chi sec^2 chi >= 0 on [0,pi/2) => phi' <= 0",
    ZR(dphidT*Xb*(Xa*Tt + Xb)**2 + sp.sqrt(c)/2*Xa))
s2 = gtt_w*gpp_w
q2 = (c/2)**2*s2*(1/(Xb*(Xa*T + Xb)))**4
dphi2 = (dphidT.subs(Tt, T))**2*4*(1-w)/w**2
chk("PG11 H5f: q^2 / phi'^2 = c w r ((1-w) + r w)/(4 Xa^2 Xb^2)", ZR(q2 - dphi2*c*w*r*((1-w) + r*w)/(4*Xa**2*Xb**2)))

# ---- H6 at J1 IR data (CONDITIONAL inputs): Xa = 2^(-3/5), Xb = 2^(2/5), c = 2^(-2/5). Exponent arithmetic in Fractions.
eXa, eXb, ec = Fr(-3,5), Fr(2,5), Fr(-2,5)
chk("PG12 H6a exponents: r = 2^(eXb-eXa) = 2^1 ; Xa^2 Xb^3 = 2^0 ; sqrt(c)/(Xa Xb) = 2^0 ; sqrt(c)/(2 Xb^2) = 2^(-2) = 1/4",
    eXb - eXa == 1 and 2*eXa + 3*eXb == 0 and ec/2 - eXa - eXb == 0 and ec/2 - 1 - 2*eXb == -2)
sig = sp.Symbol("sigma", positive=True)   # sigma = sqrt(c) = Xa Xb ; Xb^2 = 2 sigma (2^(4/5) = 2*2^(-1/5)) ; r = 2
chk("PG13 exponent of Xb^2 vs 2 sqrt(c): 2 eXb == 1 + ec/2", 2*eXb == 1 + ec/2)
phi_IR = (sig/2)/(sig*T + 2*sig)          # Xb(Xa T + Xb) = (Xa Xb) T + Xb^2
m2_IR = sp.Integer(1)*w*2*((1-w) + 2*w)/4  # c/(Xa Xb)^2 = 1, r = 2
chk("PG14 H6b: phi = w/(2(1+w)) ; (q/|phi'|)^2 = w(1+w)/2 ; both strictly increasing in w (derivatives 1/(2(1+w)^2) and (1+2w)/2)",
    ZR(phi_IR - w/(2*(1+w))) and ZR(m2_IR - w*(1+w)/2) and ZR(sp.diff(w/(2*(1+w)), w) - 1/(2*(1+w)**2)) and Z(sp.diff(w*(1+w)/2, w) - (1+2*w)/2))
thI, w1 = Fr(3,10), Fr(1,5)
lhs_c = (thI/(1-thI**2))**2
chk("PG15 H6c: 1 - theta^2 > 0 ; (theta/(1-theta^2))^2 = 900/8281 < 3/25 = min over w in [1/5,1] of w(1+w)/2 (monotone) ; phi >= phi1 > 0 on [0,chi1]",
    1 - thI**2 > 0 and lhs_c == Fr(900,8281) and lhs_c < w1*(1+w1)/2 and w1*(1+w1)/2 == Fr(3,25) and w1/(2*(1+w1)) > 0)
phi0, phi1 = Fr(1,2)/2, w1/(2*(1+w1))
chk("PG16 H6d: boundary term -psi(0) beta(0)^2 with beta(0)=1, psi = 0 for chi >= chi1: theta(phi(0)-phi1) = (3/10)(1/4 - 1/12) = 1/20",
    phi0 == Fr(1,4) and phi1 == Fr(1,12) and thI*(phi0 - phi1) == Fr(1,20))

# ---- A6-n / A9 with the CONDITIONAL unadopted test targets 2808.6 = 14043/5 and 19520/3 (exact rationals; not adopted values)
D_IR = Fr(14043,5); D_UV = Fr(19520,3)
chk("PG17 test-target encodings: Fr('2808.6') == 14043/5 ; 20*D_IR = 56172", Fr("2808.6") == D_IR and 20*D_IR == 56172)
qd = lambda u, nn, D: u*nn*nn - 20*nn - 20*D     # 20*(u n^2/20 - n - D); convex in n, vertex n = 10/u
chk("PG18 Gc1 closed form: u=1 roots bracket 247|248 (q(247) = -103 <= 0 < q(248) = 372); u=2: q(172) = -444 <= 0 < q(173) = 226; convexity => n <= 247 / n <= 172 exactly",
    qd(1,247,D_IR) == -103 and qd(1,248,D_IR) == 372 and qd(2,172,D_IR) == -444 and qd(2,173,D_IR) == 226)
chk("PG19 Gc2: min over integers of n^2/20 - n is -5 (vertex n = 10, real min also -5); u=1 with D+35: q(248) <= 0 < q(249) => |n_i| <= 248",
    Fr(100,20) - 10 == -5 and qd(1,248,D_IR+35) <= 0 < qd(1,249,D_IR+35))
chk("PG20 A9a: for u >= 1 and n >= 248 > 10, u n^2/20 - n - D_IR >= n^2/20 - n - D_IR, increasing in n, = 93/5 > 0 at n = 248 (all n, not only n <= 9760); at u=2 already n >= 173 suffices",
    Fr(248*248,20) - 248 - D_IR == Fr(93,5) and 2*Fr(173*173,20) - 173 - D_IR > 0 and 2*Fr(172*172,20) - 172 - D_IR <= 0)
chk("PG21 A9b: (u-1)n < 19520/3 ; u=2 <=> n <= 6506 (3*6506 = 19518 < 19520 < 19521) ; u = 1 + D_UV/n gives equality",
    3*6506 < 19520 < 3*6507 and (Fr(1) + D_UV/248 - 1)*248 - D_UV == 0)
# ---- A12a
qt, Dl = sp.symbols("q_tot Delta", real=True)
chk("PG22 A12a: (qt + D/2) - D/2 = qt ; (qt + D/2) + D/2 = qt + D", Z((qt + Dl/2) - Dl/2 - qt) and Z((qt + Dl/2) + Dl/2 - qt - Dl))
# ---- bookkeeping used for N- <= Delta_N/2 (1142 B1, unaudited; checked here only as algebra): Q = N+ - N- + n, T = N+ + N- + u e  =>  T - Q = 2N- + (u e - n)
Np, Nm, nn_, u_, e_u = sp.symbols("Np Nm n u e_u", real=True)
chk("PG23 B1 algebra: (N+ + N- + u e) - (N+ - N- + n) = 2N- + (u e - n)", Z((Np + Nm + u_*e_u) - (Np - Nm + nn_) - (2*Nm + u_*e_u - nn_)))
print(f"{sum(res)}/{len(res)} PASS")
print("ALL PASS" if all(res) else "SOME FAIL")
raise SystemExit(0 if all(res) else 1)
