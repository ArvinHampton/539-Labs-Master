# PP independent exact checks v2 (SEALED/FINAL) for NL e7312edb (non-BPS tension-minus-charge gap), 2026-11-10.
# v2 fixes v1_draft: (i) Q2 charge density normalization bug in PP's own code (q was the Pfaffian, not 2*Pfaffian);
# (ii) Q5 restructured (v1 Weyl with two symbolic X's and |Weyl|^2 did not finish in 10 min; killed).
# Independent implementations (not NL code). Zero tests: Poly(...).is_zero / cancel numerator expand,
# exact Rational/Fraction. No simplify()==0, no floats, no allclose, no nsimplify.
import sympy as sp, itertools
from fractions import Fraction as Fr
R = sp.Rational
npass = ntot = 0; ok = True
def chk(name, c):
    global npass, ntot, ok
    c = bool(c); ntot += 1; npass += c; ok = ok and c
    print(f"[{'PASS' if c else 'FAIL'}] {name}")
def iz(e):  # exact zero test for rational expressions
    num, den = sp.fraction(sp.cancel(sp.together(e)))
    return sp.Poly(sp.expand(num), *sorted(num.free_symbols, key=str) or [sp.Symbol('dummy')]).is_zero

# ---------- Q1: bookkeeping from scratch ----------
Np, Nm, n, eu, u, DN = sp.symbols('Np Nm n e_u u Delta_N', real=True)
T = Np + Nm + u*eu; Q = Np - Nm + n; eps = u*(eu - n)
chk("Q1a T-Q = 2N- + (u-1)n + eps_ex", iz(T - Q - (2*Nm + (u-1)*n + eps)))
# u>=1: substitute u=1+v, e_u = |n| + delta for both signs of n; check every monomial coefficient >= 0
v, d, m = sp.symbols('v delta m', nonnegative=True)
for sgn, sub in (("n>=0", {n: m, eu: m + d}), ("n<=0", {n: -m, eu: m + d})):
    P = sp.Poly(sp.expand((T - Q).subs(sub).subs(u, 1 + v)), Nm, m, d, v)
    chk(f"Q1b [u>=1, {sgn}] T-Q has only nonnegative integer coeffs in (N-,|n|,delta,v-1): {P.as_expr()}",
        all(c >= 0 for c in P.coeffs()) and Np not in P.as_expr().free_symbols)
# u<1 witness: A1's u>=1 scope is sharp (negative gap kinematically closable when u<1)
wit = (T - Q).subs({u: R(1,2), Nm: 0, Np: 0, eu: n}).subs(n, 9760)
chk("Q1c [u<1 witness] u=1/2, all charge in one BPS block (n=Q, N+-=0): T-Q = -Q/2 < 0 (so A1 cannot extend below u=1)",
    wit == -4880)
chk("Q1d [u<1] T-uQ = (1-u)N+ + (1+u)N- + u(e_u-n) (A2 form)", iz(T - u*Q - ((1-u)*Np + (1+u)*Nm + u*(eu - n))))
# closure condition, and the GB8 g(b) sign
clos = T - Q - DN
g_filed = u*eu - n - 2*Nm - DN
g_corr = u*eu - n + 2*Nm - DN
chk("Q1e closure T-Q-Delta_N equals u e_u - n + 2N- - Delta_N (PLUS 2N-)", iz(clos - g_corr))
chk("Q1f GB8's filed g = u e_u - n - 2N- - Delta_N differs from closure by -4N- (sign error unless N-=0)",
    iz(g_filed - clos + 4*Nm) and not iz(g_filed - clos))
# A5 at n<0: floor eps_ex >= 2u|n| defeats 'every target >= 0'
uu, nn, DNv = 2, -1, 0
target = DNv - (uu - 1)*nn; floor = 2*uu*abs(nn)
chk(f"Q1g A5 literal [u!=1] overclaim for n<0: u=2,n=-1,Delta_N=0 gives target {target} < Bogomolny floor {floor}",
    target >= 0 and target < floor)

# ---------- Q2: Bogomolny with * from the Levi-Civita symbol ----------
idx = [(a,b) for a in range(4) for b in range(a+1,4)]
Fs = {p: sp.Symbol(f"F{p[0]}{p[1]}", real=True) for p in idx}
def Fc(a,b):
    if a == b: return 0
    return Fs[(a,b)] if a < b else -Fs[(b,a)]
def star(a,b): return sum(R(1,2)*sp.LeviCivita(a,b,c,dd)*Fc(c,dd) for c in range(4) for dd in range(4))
rho = R(1,4)*sum(Fc(a,b)**2 for a in range(4) for b in range(4))        # = 1/2 sum_{a<b}
q = R(1,2)*sum(Fc(a,b)*star(a,b) for a in range(4) for b in range(4))   # = sum_{a<b} F_ab (*F)_ab = 2 Pf(F)  [v2 fix]
chk("Q2a q = 2(F01F23 - F02F13 + F03F12) (Pfaffian form)", iz(q - 2*(Fc(0,1)*Fc(2,3) - Fc(0,2)*Fc(1,3) + Fc(0,3)*Fc(1,2))))
chk("Q2b ** = 1 on 2-forms in 4D Euclidean", all(iz(sum(R(1,2)*sp.LeviCivita(a,b,c,dd)*star(c,dd) for c in range(4) for dd in range(4)) - Fc(a,b)) for a,b in idx))
m_ = R(1,8)*sum((Fc(a,b) - star(a,b))**2 for a in range(4) for b in range(4))
p_ = R(1,8)*sum((Fc(a,b) + star(a,b))**2 for a in range(4) for b in range(4))
chk("Q2c rho - q/2 = (1/8) sum_ordered (F-*F)^2 = 1/4 sum_{a<b}; rho + q/2 = (1/8) sum (F+*F)^2", iz(rho - q/2 - m_) and iz(rho + q/2 - p_))

# ---------- Q3: W5 for SD and ASD (orientation/trace-convention independence) ----------
def wedge1_2(vv, om):  # (v^om)_{ijk}, i<j<k
    out = []
    for (i,j,k) in itertools.combinations(range(4),3):
        out.append(vv[i]*om(j,k) - vv[j]*om(i,k) + vv[k]*om(i,j))
    return out
a_, b_, c_ = sp.symbols('a b c', real=True)
vs = sp.symbols('v0:4', real=True)
for lab, sgn in (("SD", 1), ("ASD", -1)):
    base = {(0,1): a_, (0,2): b_, (0,3): c_}
    def om(i,j, sgn=sgn):
        if i == j: return 0
        if i > j: return -om(j,i)
        if (i,j) in base: return base[(i,j)]
        # (2,3)=sgn*a, (1,3)=-sgn*b, (1,2)=sgn*c  from *e01=e23, *e02=-e13, *e03=e12
        return {(2,3): sgn*a_, (1,3): -sgn*b_, (1,2): sgn*c_}[(i,j)]
    # verify (anti)self-duality with star built from epsilon
    okd = all(iz(sum(R(1,2)*sp.LeviCivita(i,j,k,l)*om(k,l) for k in range(4) for l in range(4)) - sgn*om(i,j)) for i in range(4) for j in range(4) if i<j)
    Mw = sp.Matrix([[sp.diff(e, vv) for vv in vs] for e in wedge1_2(vs, om)])
    chk(f"Q3 {lab}: omega is {lab} and det(v -> v^omega) = (a^2+b^2+c^2)^2 (up to sign) => injective for omega!=0",
        okd and (iz(Mw.det() - (a_**2+b_**2+c_**2)**2) or iz(Mw.det() + (a_**2+b_**2+c_**2)**2)))

# ---------- Q4: dW != 0 on a dense open set of S^4 for W = X_b + (X_a - X_b)|y|^2 ----------
x1,x2,x3,y1,y2 = sp.symbols('x1 x2 x3 y1 y2', real=True)
P5 = sp.Matrix([x1,x2,x3,y1,y2]); f = y1**2 + y2**2
grad = sp.Matrix([sp.diff(f, z) for z in P5]); tang = grad - (grad.dot(P5))*P5   # on |P|=1
r2y = y1**2+y2**2
expected = sp.Matrix([-2*r2y*x1, -2*r2y*x2, -2*r2y*x3, 2*(1-r2y)*y1, 2*(1-r2y)*y2])
chk("Q4 tangential grad of |y|^2 on S^4 = 2(-|y|^2 x, (1-|y|^2) y): zero set {y=0} U {x=0} (an S^2 and an S^1; empty interior)",
    all(iz((tang - expected)[i].subs(x1**2, 1 - x2**2 - x3**2 - r2y)) or iz(sp.expand((tang-expected)[i]).subs(x1**2, 1-x2**2-x3**2-r2y)) for i in range(5)))

# ---------- Q5 (v2): Weyl tensor of the MN2-type fibre, Weierstrass rational parametrization ----------
# metric (Xa = 1 by constant rescaling, r = Xb/Xa): (s^2/r + c^2) dchi^2 + (c^2/r) dOmega_2^2 + s^2 dpsi^2
tc, tth = sp.symbols('tc tth', real=True)   # tan(chi/2), tan(theta/2)
r = sp.Symbol('r', positive=True)
sch, cch = 2*tc/(1+tc**2), (1-tc**2)/(1+tc**2); sth = 2*tth/(1+tth**2)
def dchi(e): return sp.cancel((1+tc**2)/2*sp.diff(e, tc))
def dth(e):  return sp.cancel((1+tth**2)/2*sp.diff(e, tth))
Dop = [dchi, dth, lambda e: 0, lambda e: 0]
def weyl(gd):
    N=4; gd=[sp.cancel(x) for x in gd]; ginv=[sp.cancel(1/x) for x in gd]
    Gam=[[[sp.cancel(R(1,2)*ginv[a]*((Dop[c](gd[a]) if a==b else 0)+(Dop[b](gd[a]) if a==c else 0)-(Dop[a](gd[b]) if b==c else 0))) for c in range(N)] for b in range(N)] for a in range(N)]
    cache={}
    def RL(a,b,c,d):
        if a==b or c==d: return 0
        s=1
        if a>b: a,b,s=b,a,-s
        if c>d: c,d,s=d,c,-s
        k=(a,b,c,d)
        if k not in cache:
            e=Dop[c](Gam[a][d][b])-Dop[d](Gam[a][c][b])+sum(Gam[a][c][j]*Gam[j][d][b]-Gam[a][d][j]*Gam[j][c][b] for j in range(N))
            cache[k]=sp.cancel(gd[a]*e)
        return s*cache[k]
    Ric=[[sp.cancel(sum(ginv[k]*RL(k,a,k,b) for k in range(N))) for b in range(N)] for a in range(N)]
    Rs=sp.cancel(sum(ginv[a]*Ric[a][a] for a in range(N)))
    gm=lambda a,b: gd[a] if a==b else 0
    def C(a,b,c,d):
        return sp.cancel(RL(a,b,c,d)-R(1,2)*(gm(a,c)*Ric[b][d]-gm(a,d)*Ric[b][c]-gm(b,c)*Ric[a][d]+gm(b,d)*Ric[a][c])+Rs/6*(gm(a,c)*gm(b,d)-gm(a,d)*gm(b,c)))
    return C
pairs=[(a,b) for a in range(4) for b in range(a+1,4)]
C1 = weyl([sch**2+cch**2, cch**2, cch**2*sth**2, sch**2])
chk("Q5a r = 1 (X_a = X_b): all 21 independent Weyl components are identically 0 (exact cancel, no trig identity used)",
    all(iz(C1(*p,*q_)) for p in pairs for q_ in pairs if p <= q_))
Cr = weyl([sch**2/r+cch**2, cch**2/r, cch**2*sth**2/r, sch**2])
c0303 = Cr(0,3,0,3)
closed = 4*tc**2*(r-1)**2*(tc**2-1)**2/(3*(tc**2+1)**2*(r*(1-tc**2)**2 + 4*tc**2))
print("   C_0303(r, chi) =", sp.factor(c0303))
chk("Q5b C_0303 = 4 t^2 (r-1)^2 (1-t^2)^2 / (3 (1+t^2)^2 (r(1-t^2)^2 + 4t^2)), t = tan(chi/2): factor (r-1)^2, positive denominator",
    iz(c0303 - closed))
v = c0303.subs({r: 2, tc: R(1,3)})
chk(f"Q5c at r = 2, sin chi = 3/5 (t = 1/3): C_0303 = {v} = 48/1025 = NL C2 value", v == R(48,1025))
chk("Q5d for every r != 1 C_0303 != 0 at t = 1/3 (so the fibre is conformally flat iff r = 1 on this family)",
    sp.Poly(sp.fraction(sp.cancel(c0303.subs(tc, R(1,3))))[0], r).rem(sp.Poly((r-1)**2, r)).is_zero
    and sp.degree(sp.fraction(sp.cancel(c0303.subs(tc, R(1,3))))[0], r) == 2)

# ---------- Q6: W1 virial identity, independent matrix su(2) implementation ----------
xs=sp.symbols('x1:5',real=True); Wf=sp.Function('W')(*xs); I=sp.I
Tg=[-I/2*sp.Matrix([[0,1],[1,0]]), -I/2*sp.Matrix([[0,-I],[I,0]]), -I/2*sp.Matrix([[1,0],[0,-1]])]
A=[sum((sp.Function(f'a{a}{i}')(*xs)*Tg[i] for i in range(3)), sp.zeros(2)) for a in range(4)]
dd=lambda M,a: M.applyfunc(lambda e: sp.diff(e,xs[a]))
F=[[dd(A[b],a)-dd(A[a],b)+A[a]*A[b]-A[b]*A[a] for b in range(4)] for a in range(4)]
ip=lambda X,Y: sp.expand(-2*(X*Y).trace())
F2=sum(ip(F[a][b],F[a][b]) for a in range(4) for b in range(4))
tt=lambda a,b: sum(ip(F[a][c],F[b][c]) for c in range(4)) - (R(1,4)*F2 if a==b else 0)
J=[sum((dd(Wf*F[a][c],a)+A[a]*(Wf*F[a][c])-(Wf*F[a][c])*A[a] for a in range(4)), sp.zeros(2)) for c in range(4)]
okW=all(sp.expand(sum(sp.diff(Wf*tt(a,b),xs[a]) for a in range(4)) + R(1,4)*F2*sp.diff(Wf,xs[b]) - sum(ip(F[b][c],J[c]) for c in range(4)))==0 for b in range(4))
chk("Q6a W1: d^a(W t_ab) = -1/4|F|^2 d_bW + <F_bc, D^a(W F_ac)> (matrix su(2), D = d + [A, .]; expand==0 on derivative polynomials)", okW)
chk("Q6b t_ab traceless in 4D", sp.expand(sum(tt(a,a) for a in range(4)))==0)

# ---------- Q7: round S^4 height function (GB5 / W3, W4) ----------
al = sp.Symbol('alpha', real=True); h = sp.cos(al)
chk("Q7a h'' = -h and Hess_S3-part: sin(al)cos(al) h' = -h sin^2(al)  (Hess h = -h g)",
    sp.expand(sp.diff(h,al,2) + h) == 0 and sp.expand(sp.sin(al)*sp.cos(al)*sp.diff(h,al) + h*sp.sin(al)**2) == 0)
tq = sp.Symbol('tq', real=True)   # |grad h|^2 = sin^2 = 1 - h^2 via t = tan(al/2)
chk("Q7b |grad h|^2 = 1 - h^2 (rational parametrization)", iz((2*tq/(1+tq**2))**2 - (1 - ((1-tq**2)/(1+tq**2))**2)))

# ---------- Q8: fibre-trace inequality, general 10D field incl. electric and x-legs; branes ----------
D=10; eta=sp.diag(-1,*([1]*9)); FIB=[6,7,8,9]
Fm=sp.zeros(D,D); comps={}
for a in range(D):
    for b in range(a+1,D):
        s_=sp.Symbol(f"f{a}_{b}",real=True); Fm[a,b]=s_; Fm[b,a]=-s_; comps[(a,b)]=s_
Fup=eta*Fm*eta
F2t=sum(Fm[a,b]*Fup[a,b] for a in range(D) for b in range(D))
Smat=lambda a,b: sum(Fm[a,c]*Fm[b,c2]*eta[c,c2] for c in range(D) for c2 in range(D)) - R(1,4)*eta[a,b]*F2t
rhoG=sp.expand(Smat(0,0)); trf=sp.expand(sum(Smat(a,a) for a in FIB))
qf=sp.Poly(sp.expand(trf+4*rhoG), *comps.values())
diag_only = all(sum(mo)==2 and max(mo)==2 for mo in qf.monoms())
coeffs = {str(list(comps.values())[mo.index(2)]): c for mo,c in zip(qf.monoms(), qf.coeffs())}
neg = {k:c for k,c in coeffs.items() if c < 0}
print("   tr_fib S + 4 rho, general 45-component field: negative-coefficient components:", neg)
chk("Q8a magnetic Y6 restriction (legs only in 4..9): tr_fib S + 4 rho = 2 P_ff + P_mixed (diagonal, >= 0)",
    all((c >= 0) for k,c in coeffs.items() if all(int(z) >= 4 for z in k[1:].split('_'))))
chk("Q8b general field: tr_fib S + 4 rho is a diagonal quadratic form; report which components enter with negative sign",
    diag_only)
TB=sp.Symbol('T',positive=True)
chk("Q8c positive-tension brane with k in {0..4} fibre directions in its worldvolume: tr_fib T = -k T >= -4T = -4 rho_brane",
    all(-k*TB + 4*TB >= 0 for k in range(5)))
w=sp.Symbol('w', real=True); rr=sp.Symbol('rho', positive=True)
chk("Q8d contradiction: tr_fib S_src >= -4 rho and tr_fib S_req = 4 w rho with w < -1, rho > 0 => S_src - S_req >= -4rho(1+w) > 0",
    iz((-4*rr - 4*w*rr) - (-4*rr*(1+w))) and all(-4*(1+Fr(x)) > 0 for x in (Fr(-6,5), Fr(-4,3))) and 4*Fr(-6,5)==Fr(-24,5) and 4*Fr(-4,3)==Fr(-16,3))

# ---------- Q9: K kinematics on a curved chart ----------
g11,g12,g22,phi,tp = sp.symbols('g11 g12 g22 phi t', real=True)
# a = phi(T1 dy1 + T2 dy2); t^4 term of |F|^2_g = 2 g^{11}g^{22}|[a1,a2]|^2 - 2 (g^{12})^2 |[a1,a2]|^2 ... use F_ab F_cd g^ac g^bd
ginv2=sp.Matrix([[g11,g12],[g12,g22]])
comm=(phi*Tg[0])*(phi*Tg[1])-(phi*Tg[1])*(phi*Tg[0])
F12=tp**2*comm; Fab=[[sp.zeros(2),F12],[-F12,sp.zeros(2)]]
dens=sp.expand(sum(ginv2[a,c]*ginv2[b,d_]*ip(Fab[a][b],Fab[c][d_]) for a in range(2) for b in range(2) for c in range(2) for d_ in range(2)))
chk("Q9 t^4 coefficient of |F|^2_g along t*a is 2 phi^4 det(g^-1) > 0 for any positive-definite metric (unbounded above)",
    iz(sp.Poly(dens,tp).coeff_monomial(tp**4) - 2*phi**4*(g11*g22-g12**2)))

# ---------- Q10: A9 / I arithmetic as labelled CONDITIONAL test targets ----------
Qt=9760; DIR=Fr(28086,10); DUV=Fr(5,3)*Qt-Qt
chk("Q10a Delta_N(UV) = (5/3 - 1)*9760 = 19520/3; Delta_N(IR) = 14043/5 (test targets, CONDITIONAL, unadopted)", DUV==Fr(19520,3) and DIR==Fr(14043,5))
chk("Q10b [u=2] UV BPS endpoint g = n - 19520/3 < 0 iff n <= 6506", all((n_-DUV<0)==(n_<=6506) for n_ in (115,6506,6507)))
ub = (DUV+115)/2
chk(f"Q10c [u=2,n=115] UV endpoint sign needs only 2e_u - 115 < 19520/3, i.e. e_u(UV) < {ub} (branch must land below this; not proved)", ub==Fr(19865,6))
chk("Q10d [u=2,n=115] IR closure excess eps_ex = Delta_N(IR) - n = 13468/5 > 0 (consistency, B5)", DIR-115==Fr(13468,5))
chk("Q10e Z1 ratio neutrality of doubling (exact rationals)", all(Fr(2*k-2*e,2*g_)==Fr(k-e,g_) and Fr(2*e,2*g_)==Fr(e,g_) for k,e,g_ in ((7,3,5),(11,2,13))))

print(f"{npass}/{ntot} PASS"); print("ALL PASS" if ok else "SOME FAIL")
raise SystemExit(0 if ok else 1)
