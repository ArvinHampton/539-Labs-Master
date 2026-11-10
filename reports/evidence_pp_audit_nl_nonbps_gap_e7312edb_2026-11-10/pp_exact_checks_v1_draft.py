# PP independent exact checks for NL e7312edb (non-BPS tension-minus-charge gap), 2026-11-10.
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
q = R(1,4)*sum(Fc(a,b)*star(a,b) for a in range(4) for b in range(4))   # F^*F density, = Pf * 2 /2 ...
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

# ---------- Q5: Weyl tensor of the MN2-type fibre via Weierstrass rational parametrization ----------
tc, tth = sp.symbols('tc tth', real=True)   # tan(chi/2), tan(theta/2)
Xa, Xb = sp.symbols('Xa Xb', positive=True)
sch, cch = 2*tc/(1+tc**2), (1-tc**2)/(1+tc**2)
sth = 2*tth/(1+tth**2)
# coordinates (chi, theta, phi, psi); d/dchi = (1+tc^2)/2 d/dtc, d/dtheta = (1+tth^2)/2 d/dtth
def dchi(e): return sp.cancel((1+tc**2)/2*sp.diff(e, tc))
def dth(e):  return sp.cancel((1+tth**2)/2*sp.diff(e, tth))
Dop = [dchi, dth, lambda e: 0, lambda e: 0]
def weyl_all(gd):
    N = 4
    ginv = [sp.cancel(1/x) for x in gd]
    Gam = [[[sp.cancel(R(1,2)*ginv[a]*((Dop[c](gd[a]) if a==b else 0) + (Dop[b](gd[a]) if a==c else 0) - (Dop[a](gd[b]) if b==c else 0)))
             for c in range(N)] for b in range(N)] for a in range(N)]
    def Rud(a,b,c,dd):
        e = Dop[c](Gam[a][dd][b]) - Dop[dd](Gam[a][c][b]) + sum(Gam[a][c][k]*Gam[k][dd][b] - Gam[a][dd][k]*Gam[k][c][b] for k in range(N))
        return sp.cancel(e)
    Rl = {}
    for a,b,c,dd in itertools.product(range(N), repeat=4):
        Rl[(a,b,c,dd)] = sp.cancel(gd[a]*Rud(a,b,c,dd)) if (a<b and c<dd) else None
    def RL(a,b,c,dd):
        if a==b or c==dd: return 0
        s = 1
        if a>b: a,b,s = b,a,-s
        if c>dd: c,dd,s = dd,c,-s
        return s*Rl[(a,b,c,dd)]
    Ric = [[sp.cancel(sum(ginv[k]*RL(k,a,k,b) for k in range(N))) for b in range(N)] for a in range(N)]
    Rs = sp.cancel(sum(ginv[a]*Ric[a][a] for a in range(N)))
    gm = lambda a,b: gd[a] if a==b else 0
    def C(a,b,c,dd):
        return sp.cancel(RL(a,b,c,dd) - R(1,2)*(gm(a,c)*Ric[b][dd] - gm(a,dd)*Ric[b][c] - gm(b,c)*Ric[a][dd] + gm(b,dd)*Ric[a][c])
                         + Rs/6*(gm(a,c)*gm(b,dd) - gm(a,dd)*gm(b,c)))
    return C, Rs
gA = sch**2/Xb + cch**2/Xa; gB = cch**2/Xb; gC = sch**2/Xa
C, Rs = weyl_all([gA, gB, gB*sth**2, gC])
pairs = [(a,b) for a in range(4) for b in range(a+1,4)]
allC = {(p,q_): C(*p,*q_) for p in pairs for q_ in pairs if p <= q_}
chk("Q5a X_a=X_b: all 21 independent Weyl components vanish identically (rational-parametrization cancel)",
    all(iz(e.subs(Xa, Xb)) for e in allC.values()))
# point sin chi = 3/5 -> tan(chi/2) = 1/3 ; sin theta = 3/5 -> tan(theta/2) = 1/3
pt = {tc: R(1,3), tth: R(1,3)}
v0303 = sp.cancel(C(0,3,0,3).subs({Xa:1, Xb:2}).subs(pt))
print("   C_0303 at Xa=1,Xb=2, sin chi = sin theta = 3/5:", v0303)
chk("Q5b C_0303 = 48/1025 (NL C2 value, same R^a_bcd convention), nonzero rational", v0303 == R(48,1025))
# orthonormal-frame scalar invariant |C|^2 = C_abcd C^abcd as function of r = Xb/Xa (Xa = 1)
r = sp.Symbol('r', positive=True)
gdv = [gA, gB, gB*sth**2, gC]
Csq = 0
for (p,q_), e in allC.items():
    w = 1 if p == q_ else 2
    Csq += w*4*e**2/(gdv[p[0]]*gdv[p[1]]*gdv[q_[0]]*gdv[q_[1]])
Csq_r = sp.factor(sp.cancel(Csq.subs({Xa:1, Xb:r})))
print("   |Weyl|^2 (Xa=1, Xb=r) factored:", Csq_r)
num_r, den_r = sp.fraction(Csq_r)
chk("Q5c |Weyl|^2 numerator has factor (r-1)^2 and is independent of theta (cohomogeneity one)",
    sp.Poly(num_r, r).rem(sp.Poly((r-1)**2, r)).is_zero and tth not in Csq_r.free_symbols)
