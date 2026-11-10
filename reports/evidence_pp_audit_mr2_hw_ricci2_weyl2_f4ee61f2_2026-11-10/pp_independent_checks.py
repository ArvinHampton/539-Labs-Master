#!/usr/bin/env python3
# PP independent exact checks for MR2 filing f4ee61f2 (HW plane Ricci^2/Weyl^2). Audit only. Nothing adopted. Junction UNSOLVED.
# Own code; does not import MR2's curvature routine. Exact SymPy rationals; zero tests are Poly(...).is_zero or Rational/Integer equality. No simplify, no floats.
import sys, hashlib, datetime, itertools, re
from zoneinfo import ZoneInfo
print("RUN_START_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z"))
print("SCRIPT_SHA256", hashlib.sha256(open(__file__,'rb').read()).hexdigest())
import sympy as sp
from sympy import Rational as Q, Poly, Matrix, symbols, Function, diff, expand, Integer
print("sympy", sp.__version__)
ok=True
def chk(lbl, c):
    global ok; c=bool(c); ok&=c; print(("PASS " if c else "FAIL ")+lbl); sys.stdout.flush()
def zero(e, gens): return Poly(expand(e), *gens).is_zero

# ---------- P2: 11D diagonal warped metric, own Christoffel/Riemann from full functions A_a(y) ----------
print("\n== P2 own curvature for g = dy^2 + sum_a eta_a e^{2A_a(y)} dx_a^2, D=11 ==")
D=11; n=10
y=symbols('y'); X=[y]+list(symbols('x0:10'))
A=[Function(f'A{a}')(y) for a in range(n)]
eta=[-1]+[1]*9
gd=[Integer(1)]+[eta[a]*sp.exp(2*A[a]) for a in range(n)]   # diagonal metric
gi=[1/x for x in gd]
# Christoffel Gamma^i_{jk} for diagonal metric, only y-dependence
def Gam(i,j,k):
    # Gamma^i_jk = 1/2 g^ii (d_j g_ik + d_k g_ij - d_i g_jk) diag
    def dg(m,a,b): return diff(gd[a],X[m]) if a==b else 0
    return sp.Rational(1,2)*gi[i]*(dg(j,i,k)+dg(k,i,j)-dg(i,j,k))
G=[[[sp.expand(Gam(i,j,k)) for k in range(D)] for j in range(D)] for i in range(D)]
# Riemann R^i_{jkl} = d_k G^i_lj - d_l G^i_kj + G^i_km G^m_lj - G^i_lm G^m_kj ; lower R_ijkl = g_ii R^i_jkl
def Rup(i,j,k,l):
    v=diff(G[i][l][j],X[k])-diff(G[i][k][j],X[l])
    v+=sum(G[i][k][m]*G[m][l][j]-G[i][l][m]*G[m][k][j] for m in range(D))
    return sp.expand(v)
R={}
for i,j,k,l in itertools.product(range(D),repeat=4):
    if i==j or k==l: continue
    if not ({i,j}=={k,l}):  # check off-pattern components vanish (computed below for a subset)
        continue
    R[(i,j,k,l)]=sp.expand(gd[i]*Rup(i,j,k,l))
# verify off-pattern components vanish on a sample of index sets (all with distinct pair sets involving y)
offz=all(sp.expand(gd[i]*Rup(i,j,k,l))==0 for (i,j,k,l) in [(0,1,0,2),(0,1,1,2),(1,2,1,3),(0,3,2,3),(1,2,3,4),(0,1,2,3)])
chk("P2.0 sample off-pattern Riemann components vanish (diagonal curvature operator)", offz)
p=symbols('p0:10'); q=symbols('q0:10'); k=symbols('k0:10'); r=symbols('r0:10'); w=symbols('w')
def jet(e):
    # replace A'' -> q, A' -> p, exp(2A) consistent: invariants are exp-free after full contraction
    e=e.subs({diff(A[a],y,2):q[a] for a in range(n)}).subs({diff(A[a],y):p[a] for a in range(n)})
    return sp.expand(e)
riem2=0
for (i,j,kk,l),v in R.items():
    riem2+=v**2*gi[i]*gi[j]*gi[kk]*gi[l]
riem2=jet(sp.expand(sp.powsimp(sp.expand(riem2))))
Ric=[sp.expand(sum(gi[i]*R.get((i,a,i,a),0) for i in range(D))) for a in range(D)]
Rs=sp.expand(sum(gi[a]*Ric[a] for a in range(D)))
ric2=jet(sp.expand(sp.powsimp(sp.expand(sum(gi[a]**2*Ric[a]**2 for a in range(D))))))
Rsj=jet(sp.powsimp(Rs))
# Weyl explicitly: C_abab = R_abab - 1/(D-2)(g_aa R_bb + g_bb R_aa) + R/((D-1)(D-2)) g_aa g_bb  (a!=b; diagonal case)
weyl2=0
for a in range(D):
    for b in range(D):
        if a==b: continue
        C=R[(a,b,a,b)]-Q(1,D-2)*(gd[a]*Ric[b]+gd[b]*Ric[a])+Rs*Q(1,(D-1)*(D-2))*gd[a]*gd[b]
        weyl2+=2*C**2*gi[a]**2*gi[b]**2   # C_abab, C_abba, C_baba, C_baab: factor 4 over ordered (a,b) pairs counted once each -> 2 per ordered pair
weyl2=jet(sp.expand(sp.powsimp(sp.expand(weyl2))))
for nm,e in [('riem2',riem2),('ric2',ric2),('weyl2',weyl2),('R',Rsj)]:
    chk(f"P2.1 {nm} is exp-free polynomial in (p,q)", not e.has(sp.exp) and not any(isinstance(x,sp.Float) for x in sp.preorder_traversal(e)))
pred=4*sum((q[a]+p[a]**2)**2 for a in range(n))+2*sum((p[a]*p[b])**2 for a in range(n) for b in range(n) if a!=b)
chk("P2.2 Riem^2 = 4 sum(A''+A'^2)^2 + 2 sum_{a!=b}(A'_aA'_b)^2  [MR2 A0]", zero(riem2-pred, list(p)+list(q)))
sub={q[a]:-k[a]*w+r[a] for a in range(n)}
T2=sum(x**2 for x in k); T1=sum(k)
gens=list(k)+list(p)+list(r)
def c2(e): return Poly(expand(e.subs(sub)),w).coeff_monomial(w**2)
cR=c2(riem2); cRic=c2(ric2); cW=c2(weyl2); cRR=c2(sp.expand(Rsj**2)); cGB=c2(sp.expand(riem2-4*ric2+Rsj**2))
chk("P2.3 Riem^2 w^2-coeff = 4 tr k^2", zero(cR-4*T2,gens))
chk("P2.4 Ric^2 w^2-coeff = tr k^2 + (tr k)^2", zero(cRic-(T2+T1**2),gens))
chk("P2.5 R^2 w^2-coeff = 4 (tr k)^2", zero(cRR-4*T1**2,gens))
chk("P2.6 Weyl^2 (explicit Weyl tensor) w^2-coeff = (32/9)(tr k^2 - (tr k)^2/10)", zero(cW-Q(32,9)*(T2-T1**2/10),gens))
chk("P2.7 Gauss-Bonnet w^2-coeff = 0", zero(cGB,gens))
for nm,e in [('riem2',riem2),('ric2',ric2),('weyl2',weyl2)]:
    chk(f"P2.8 {nm} degree in w <= 2", Poly(expand(e.subs(sub)),w).degree()<=2)
# Weyl decomposition identity (own Weyl vs identity) as a cross-check
chk("P2.9 own Weyl^2 = Riem^2 - (4/9)Ric^2 + (1/45)R^2 (D=11 identity, exact)", zero(weyl2-(riem2-Q(4,9)*ric2+Q(2,90)*Rsj**2), list(p)+list(q)))

# ---------- P2L: log-printed coefficient polynomials parsed literally ----------
print("\n== P2L parse MR2 log lines and compare ==")
L=open(sys.argv[1]).read()
def grab(tag):
    m=re.search(r"w\^2 coefficient of "+re.escape(tag)+r": (.*)", L); return sp.parse_expr(m.group(1), local_dict={f'k{i}':k[i] for i in range(10)})
lw=grab('weyl2'); lr=grab('ric2'); lR=grab('riem2'); lRR=grab('R^2'); lgb=grab('gb')
chk("P2L.1 parsed log polynomials contain no Float", not any(isinstance(x,sp.Float) for e in [lw,lr,lR,lRR] for x in sp.preorder_traversal(e)))
chk("P2L.2 log Weyl^2 16(...)/45 == (32/9) tr k~^2 (Poly.is_zero)", zero(lw-Q(32,9)*(T2-T1**2/10), list(k)))
chk("P2L.3 log Weyl^2 polynomial == PP own Weyl^2 coefficient", zero(lw-cW, gens))
chk("P2L.4 log Ric^2 2(...) == tr k^2 + (tr k)^2", zero(lr-(T2+T1**2), list(k)))
chk("P2L.5 log Riem^2 == 4 tr k^2 ; log R^2 == 4 (tr k)^2 ; log GB == 0", zero(lR-4*T2,list(k)) and zero(lRR-4*T1**2,list(k)) and lgb==0)

# ---------- P3D: general-D Weyl decomposition algebra (rational function identity in D) ----------
print("\n== P3D general-D algebra (GIVEN Riem^2,Ric^2,R^2 delta^2 coefficients 4t2, t2+t1^2, 4t1^2) ==")
Dd,t1,t2=symbols('D t1 t2')
lhs=4*t2-4/(Dd-2)*(t2+t1**2)+8/((Dd-1)*(Dd-2))*t1**2
rhs=4*(Dd-3)/(Dd-2)*(t2-t1**2/(Dd-1))
num,den=sp.fraction(sp.together(lhs-rhs))
chk("P3D.1 4t2 - 4/(D-2)(t2+t1^2) + 8/((D-1)(D-2)) t1^2 == 4(D-3)/(D-2)(t2 - t1^2/(D-1))  (numerator Poly zero)", Poly(expand(num),Dd,t1,t2).is_zero)
chk("P3D.2 D=4 value 2(t2-t1^2/3) [MR2 B4], D=11 value (32/9)(t2-t1^2/10) [MR2 A4]",
    Poly(expand(rhs.subs(Dd,4)*1-2*(t2-t1**2/3)),t1,t2).is_zero and Poly(expand(rhs.subs(Dd,11)-Q(32,9)*(t2-t1**2/10)),t1,t2).is_zero)

# ---------- P5: profile integrals ----------
print("\n== P5 profile integrals (exact; s=y/eps, T=tanh s, ds sech^2 = dT) ==")
T=symbols('T'); eps=symbols('epsilon',positive=True); Lr=symbols('L',positive=True)
I2=sp.integrate(Integer(1),(T,-1,1)); I4=sp.integrate(1-T**2,(T,-1,1))
chk("P5.1 int sech^2 ds = 2, int sech^4 ds = 4/3 (Rational)", I2==2 and I4==Q(4,3))
phi1=eps*I2/(2*eps); phi2=eps*I4/(4*eps**2)
chk("P5.2 int phi_eps = 1 and int phi_eps^2 = 1/(3 eps) exactly", phi1==1 and sp.expand(phi2-1/(3*eps))==0)
# Cauchy-Schwarz: (int phi)^2 <= |supp| int phi^2 -> int phi^2 >= 1/(2 L eps). Equality case: uniform phi=1/(2L eps)
chk("P5.3 CS equality case (uniform on [-L eps, L eps]) gives exactly 1/(2 L eps)", sp.expand((1/(2*Lr*eps))**2*2*Lr*eps - 1/(2*Lr*eps))==0)
# with A'' = -k sech^2(y/eps)/eps (MR2 script normalisation: centre value -k/eps), [K] = int A'' = -2k ; delta^2 integral = c(k)*(4/3)/eps = c([K])/(3 eps)
kk=symbols('kk')
chk("P5.4 normalisation: c(k)*4/(3eps) with k=-[K]/2 equals c([K])/(3 eps) for homogeneous quadratic c", sp.expand(( (kk/2)**2)*Q(4,3)/eps - kk**2/(3*eps))==0)

# ---------- P7: Israel map, general (non-diagonal) mixed 10x10 [K] ----------
print("\n== P7 Israel S = -(1/kappa^2)([K] - I tr[K]), n=10, generic mixed matrix ==")
kap=symbols('kappa2',positive=True)
Km=Matrix(10,10,lambda i,j: symbols(f'K_{i}_{j}'))
I10=sp.eye(10)
Sm=-(Km-I10*Km.trace())/kap
trS=Sm.trace(); St=Sm-I10*trS/10; Kt=Km-I10*Km.trace()/10
gK=list(Km.free_symbols)
chk("P7.1 [K]~ = -kappa^2 S~ (all 100 entries exact)", all(zero(e,gK+[kap]) for e in (Kt+kap*St)))
chk("P7.2 tr[K] = (kappa^2/9) tr S", zero(Km.trace()-kap*trS/9, gK+[kap]))
chk("P7.3 tr([K]~^2) = kappa^4 tr(S~^2) (generic matrix)", zero((Kt*Kt).trace()-kap**2*(St*St).trace(), gK+[kap]))
# PD on real-diagonalisable: tr M^2 + (tr M)^2 = sum l^2 + (sum l)^2 ; Gram matrix I+J PD
Gm=sp.eye(10)+sp.ones(10,10)
chk("P7.4 I+J (10x10) positive definite: leading minors 2..11 exact", all(Gm[:m,:m].det()==m+1 for m in range(1,11)))
# Counterexample to positivity WITHOUT real diagonalisability: null M = sigma k k^T eta on R^{1,9}
etaM=sp.diag(*([-1]+[1]*9)); kv=Matrix([1,1]+[0]*8); sg=symbols('sigma',positive=True)
Mn=sg*kv*kv.T*etaM   # mixed tensor M^a_b = sigma k^a k_b
chk("P7.5 null stress M=sigma k^a k_b: M!=0, tr M = 0, tr M^2 = 0 => tr M^2+(tr M)^2 = 0 and tr M~^2 = 0 (P-Poinc/diagonalisability is load-bearing for strict positivity)",
    Mn!=sp.zeros(10,10) and Mn.trace()==0 and (Mn*Mn).trace()==0)

# ---------- P8: uniqueness ----------
print("\n== P8 alpha Riem^2 + beta Ric^2 + gamma R^2 delta^2-free ==")
al,be,ga=symbols('alpha beta gamma')
form=al*4*t2+be*(t2+t1**2)+ga*4*t1**2
cs=Poly(expand(form),t1,t2)
eqs=[cs.coeff_monomial(t2), cs.coeff_monomial(t1**2)]
chk("P8.1 t2=tr k^2 and t1^2=(tr k)^2 independent on 10D diagonal k: k=(1,-1,0..) gives (2,0), k=(1,0..) gives (1,1)", Matrix([[2,0],[1,1]]).det()!=0)
sol=sp.linsolve(eqs,[be,ga])
chk("P8.2 solution set {(beta,gamma)=(-4alpha, alpha)}", sol==sp.FiniteSet((-4*al,al)))

# ---------- P9: null-positivity quadratic form ----------
print("\n== P9 sum_{k=t+-e_i} |F(k,.)|^2 on R^{1,9}, 45 components ==")
Dw=10; et=[-1]+[1]*9
Fs={(a,b):symbols(f'F_{a}_{b}') for a in range(Dw) for b in range(a+1,Dw)}
def Fc(a,b): return 0 if a==b else (Fs[(a,b)] if a<b else -Fs[(b,a)])
tot=0
for i in range(1,Dw):
    for s in (1,-1):
        kvec=[0]*Dw; kvec[0]=1; kvec[i]=s
        v=[sum(kvec[a]*Fc(a,c) for a in range(Dw)) for c in range(Dw)]
        tot+=sum(et[c]*v[c]**2 for c in range(Dw))
tot=expand(tot)
target=16*sum(Fs[(0,j)]**2 for j in range(1,Dw))+4*sum(Fs[(i,j)]**2 for i in range(1,Dw) for j in range(i+1,Dw))
chk("P9.1 form == 16 sum_j F_tj^2 + 4 sum_{i<j} F_ij^2 exactly (diagonal; 9 pivots 16, 36 pivots 4)", zero(tot-target, list(Fs.values())))
chk("P9.2 component count 45 = 9 + 36", len(Fs)==45)
# each single null k: |F(k,.)|^2 >= 0 (F(k,.) orthogonal to k)
kvec=[1,1]+[0]*8; v=[sum(kvec[a]*Fc(a,c) for a in range(Dw)) for c in range(Dw)]
chk("P9.3 F(k,.)_c k^c = 0 for null k=t+e1 (covector F(k,.) annihilates k, so it is spacelike or null)", expand(sum(v[c]*kvec[c] for c in range(Dw)))==0)
# M5: S_M5 = -tau P_wv (mixed: -tau on 6 worldvolume dirs incl t, 0 on 4 transverse); S(k,k) with k = t + e_transverse
tau=symbols('tau',positive=True)
Sl=sp.diag(*([tau]+[-tau]*5+[0]*4))  # lowered S_ab = eta_ac S^c_b : S^t_t=-tau -> S_tt = +tau ; spatial wv S_ii=-tau
kt=Matrix([1]+[0]*5+[1]+[0]*3)
chk("P9.4 M5 term S(k,k) = tau for k = t + transverse unit (=> S(k,k)=0 forces tau=0)", (kt.T*Sl*kt)[0,0]==tau)
kw=Matrix([1,1]+[0]*8)
chk("P9.5 M5 term S(k,k) = 0 for k = t + worldvolume direction (needs transverse k, as MR2 states)", (kw.T*Sl*kw)[0,0]==0)

# ---------- P11: instances via PP coefficient formulas ----------
print("\n== P11 instances ==")
def coefs(kl):
    s={k[i]:kl[i] for i in range(10)}
    return [expand(cR.subs(s)), expand(cRic.subs(s)), expand(cW.subs(s)), expand(cGB.subs(s)), expand(cRR.subs(s))]
a=symbols('a')
chk("P11.1 MN2 k=(a^4,0^6): [16,20,128/15,0,64] a^2", coefs([a]*4+[0]*6)==[16*a**2,20*a**2,Q(128,15)*a**2,0,64*a**2])
u=coefs([a]*10)
chk("P11.2 umbilic: Weyl^2 0, Riem^2 40a^2", u[2]==0 and u[0]==40*a**2)
Sb=[-tau]*6+[0]*4; Kb=[-kap*(Sb[i]-sum(Sb)/9) for i in range(10)]
wb=expand(cW.subs({k[i]:Kb[i] for i in range(10)}))
chk("P11.3 BPS 1:1:0: Weyl^2 delta^2-coeff (in [K] units) = (128/15) kappa^4 tau^2", zero(wb-Q(128,15)*kap**2*tau**2,[kap,tau]))
print("\nALL_CHECKS", "PASS" if ok else "FAIL")
print("RUN_END_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z"))
sys.exit(0 if ok else 1)
