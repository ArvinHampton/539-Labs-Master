#!/usr/bin/env python3
# V2 (supersedes MR2_TWISTED_SUSY_VACUA_MN2_MN1_BBBW_COMPARE_2026-11-09.py, sha 4562c8a1...; and the audited draft aa16d54e, not on disk).
# V2 change: section 6 evaluates the symbolic Ricci in mpmath (dps 50) at every grid point (float64 lost precision near the
# coordinate poles alpha=0,pi / beta=0,pi/2), and validates the routine first on exact product cases.
# MR2 check script: twisted SUSY AdS5 x_w Sigma_2 x S4 vacua (MN N=2, MN N=1, BBBW) at N=4880, g=2.
# Sources (pinned in the .md): hep-th/0007018 eqs (26),(28),(29); 0904.4466 eqs (2.1),(2.5),(2.7),(2.8);
# 1203.0303 eqs (2.6),(2.12)-(2.23),(3.5),(3.8),(4.1)-(4.7),(4.9),(D.47)-(D.51); 1112.5487 eqs (8),(9).
# Units: metric written with l = R_AdS7 = 1 (uplift units); physical metric = l^2 * (this), l = 2 (pi N)^(1/3) l_p.
import sympy as sp, mpmath as mp, time, itertools
mp.mp.dps = 30
N = 4880; g = 2
aD = sp.Rational(8,81)*sp.sqrt(6)*(g-1)*N**3
print("== 0. constants ==")
print("a_D = c_D (KR direct product (D)) =", sp.N(aD, 12))
ell = 2*(mp.pi*N)**(mp.mpf(1)/3)
print("l/l_p = 2 (pi N)^(1/3) =", mp.nstr(ell, 12), "; l^2/l_p^2 =", mp.nstr(ell**2, 10))
print("check l^3 = 8 pi N l_p^3 :", mp.nstr(ell**3/(8*mp.pi*N), 15))
# Freund-Rubin AdS7xS4 flux check at X=1: S4 radius l/2, F4 = 3/(l/2) vol = (6/l) * (l/2)^4 * vol(unit S4)=... 
vol_S4 = 8*mp.pi**2/3
flux = (6/ell)*(ell/2)**4*vol_S4   # in l_p^3 units
print("AdS7xS4 flux / (2 pi)^3 N =", mp.nstr(flux/((2*mp.pi)**3*N), 15))

print("\n== 1. twist parameters at g=2 (1203.0303 (2.12)-(2.13)) ==")
for n in range(-3,4):
    p, q = (1+n)*(g-1), (1-n)*(g-1)
    print(f"z={n:+d}: (p,q)=({p},{q}), p+q={p+q}=2g-2", "MN2" if abs(n)==1 else ("MN1" if n==0 else "BBBW |z|>1"))
print("0<|z|<1 needs z=n/(g-1) non-integer: impossible at g=2 (g-2 = 0 such points)")

print("\n== 2. BBBW IR fixed point (1112.5487 (8)-(9) / 1203.0303 (3.8)) ==")
zs = sp.symbols('z', real=True)
X1_5 = (1+7*zs+7*zs**2+33*zs**3-(1+4*zs+19*zs**2)*sp.sqrt(1+3*zs**2))/(4*zs*(1-zs)**2)
ratio = (1+zs)/(2*zs+sp.sqrt(1+3*zs**2))
def fixed_point(zv):
    zv = sp.nsimplify(zv)
    if zv == 0:
        x15 = sp.limit(X1_5, zs, 0)
    elif zv == 1:
        x15 = sp.limit(X1_5, zs, 1)
    else:
        x15 = sp.simplify(X1_5.subs(zs, zv))
    X1 = sp.real_root(sp.nsimplify(x15), 5) if x15.is_rational else x15**sp.Rational(1,5)
    X2 = X1/ratio.subs(zs, zv)
    X0 = (X1*X2)**-2
    ef = 1/X0
    e2g = X1*X2/8*((1-zv)*X1+(1+zv)*X2)
    return dict(z=zv, X0=X0, X1=X1, X2=X2, ef=ef, e2g=e2g, a1=(1+zv)/sp.Integer(2), a2=(1-zv)/sp.Integer(2))
cands = {"MN1(z=0)":0, "MN2(z=1)":1, "BBBW(z=2)":2, "BBBW(z=3)":3, "BBBW(z=-2) mirror":-2}
FP = {}
for k, zv in cands.items():
    fp = fixed_point(zv); FP[k] = fp
    print(k, {kk: (sp.N(vv, 12) if kk not in ('z',) else vv) for kk, vv in fp.items()})
# exact checks
fp = FP["MN2(z=1)"]
print("MN2: X1 - 2^(-3/5) =", sp.N(fp['X1']-2**sp.Rational(-3,5), 20), "; X2 - X0 =", sp.N(fp['X2']-fp['X0'], 20), "(SO(3) condition)")
fp = FP["MN1(z=0)"]
print("MN1: X1^5 - 3/4 =", sp.N(fp['X1']**5-sp.Rational(3,4), 20), "; MN (28): e^{5phi}=4/3 -> X1=e^{-phi}; X0=e^{4phi}: ",
      sp.N(fp['X0'] - (sp.Rational(4,3))**sp.Rational(4,5), 20), "; MN (28) e^{-2g-3phi}=4 with e^{2g}=e^{2g0}, e^{-3phi}=X1^3:", sp.N(fp['X1']**3/fp['e2g'], 20))

print("\n== 3. large-N a=c (1203.0303 (4.6),(4.7), kappa=-1) ==")
def c_tilde(zv):
    zv = sp.nsimplify(zv)
    if zv == 0: return sp.Rational(9,32)   # z->0 limit of (4.7): (9+9/2)/48 = 9/32
    return (-1+9*zv**2+(1+3*zv**2)**sp.Rational(3,2))/(48*zv**2)
LN = {}
for k, fp in FP.items():
    e = fp['ef']**3*fp['e2g']
    a46 = sp.Rational(8,3)*(g-1)*e          # (4.6) with kappa=-1: 8(1-g)/(3 kappa) = 8(g-1)/3
    a47 = (g-1)*c_tilde(fp['z'])
    LN[k] = a47
    print(f"{k}: e^(3f0+2g0)={sp.N(e,15)}  a/N^3 via (4.6)={sp.N(a46,15)}  via (4.7)={sp.N(a47,15)}  a(N=4880)={sp.N(a47*N**3,12)}  ratio to a_D={sp.N(a47*N**3/aD,10)}")
print("MN1/MN2 large-N ratio =", sp.N(LN["MN1(z=0)"]/LN["MN2(z=1)"]), "(27/32 =", sp.N(sp.Rational(27,32)), ")")
print("(4.9) large-z asymptote c~(sqrt3/16)z+3/16 at z=3:", sp.N(sp.sqrt(3)/16*3+sp.Rational(3,16)), "vs", sp.N(c_tilde(3)))

print("\n== 4. exact finite-N a, c via a-maximization (1203.0303 (2.6),(2.16)) for A_{N-1} ==")
eps = sp.symbols('epsilon', real=True)
def exact_ac(zv, Nv, gv=2, kappa=-1):
    r_, d_, h_ = Nv-1, Nv**2-1, Nv
    TR3 = (gv-1)*((r_+d_*h_)*(1+zv*eps**3) - d_*h_*(eps**2+zv*eps))
    TR1 = (gv-1)*r_*(1+zv*eps)
    a = sp.Rational(3,32)*(3*TR3-TR1); c = sp.Rational(1,32)*(9*TR3-5*TR1)
    sols = sp.solve(sp.diff(a, eps), eps)
    best = max([s for s in sols if s.is_real], key=lambda s: float(a.subs(eps, s)))
    assert float(sp.diff(a, eps, 2).subs(eps, best)) < 0
    # (2.17)-(2.20) closed form
    eta = h_*(1+h_); zeta = sp.sqrt(eta**2+(1+4*eta+3*eta**2)*zv**2)
    if zv != 0:
        e217 = (eta+kappa*zeta)/(3*(1+eta)*zv)
        a220 = (gv-1)*r_*(zeta**3+kappa*eta**3-kappa*(1+eta)*(9+21*eta+9*eta**2)*zv**2)/(48*(1+eta)**2*zv**2)
        c220 = (gv-1)*r_*(zeta**3+kappa*eta**3-kappa*(1+eta)*(6-kappa*zeta+17*eta+9*eta**2)*zv**2)/(48*(1+eta)**2*zv**2)
    else:
        e217 = a220 = c220 = None
    return best, a.subs(eps, best), c.subs(eps, best), e217, a220, c220
EX = {}
for k, zv in cands.items():
    if zv == -2: continue
    e_, a_, c_, e217, a220, c220 = exact_ac(sp.Integer(zv), N)
    EX[k] = (a_, c_)
    line = f"{k}: eps*={sp.N(e_,15)} a={sp.N(a_,15)} c={sp.N(c_,15)} a/c={sp.N(a_/c_,15)}"
    if e217 is not None:
        line += f" | (2.17) eps={sp.N(e217,15)} (2.20) a-diff={sp.N(a220-a_,5)} c-diff={sp.N(c220-c_,5)}"
    print(line)
    print(f"    a/a_largeN-1={sp.N(a_/(LN[k]*N**3)-1,6)}  ratio a/a_D={sp.N(a_/aD,12)}  c/a_D={sp.N(c_/aD,12)}")
a_mn2_gm = sp.Rational(g-1,24)*(8*N**3-3*N-5); c_mn2_gm = sp.Rational(g-1,6)*(2*N**3-N-1)
print("MN2 GM (2.5) check: a_GM=", a_mn2_gm, " a_amax-a_GM=", sp.simplify(EX["MN2(z=1)"][0]-a_mn2_gm),
      " c_GM=", c_mn2_gm, " c_amax-c_GM=", sp.simplify(EX["MN2(z=1)"][1]-c_mn2_gm))
Nn = sp.symbols('N', positive=True, integer=True)
# symbolic MN2/MN1 exact
for zv, nm in [(1,'MN2'),(0,'MN1')]:
    r_, d_, h_ = Nn-1, Nn**2-1, Nn
    TR3 = (g-1)*((r_+d_*h_)*(1+zv*eps**3) - d_*h_*(eps**2+zv*eps)); TR1=(g-1)*r_*(1+zv*eps)
    a = sp.expand(sp.Rational(3,32)*(3*TR3-TR1)); c = sp.expand(sp.Rational(1,32)*(9*TR3-5*TR1))
    es = sp.solve(sp.diff(a,eps), eps)
    es = [s for s in es if s.subs(Nn, 10).is_real]
    best = max(es, key=lambda s: float(a.subs(eps,s).subs(Nn,10)))
    print(f"{nm} symbolic: eps*={sp.factor(best)}  a={sp.factor(sp.simplify(a.subs(eps,best)))}  c={sp.factor(sp.simplify(c.subs(eps,best)))}")
print("GM (2.5) a factor:", sp.factor((8*Nn**3-3*Nn-5)/24), " c factor:", sp.factor((2*Nn**3-Nn-1)/6))
for k,(a_,c_) in EX.items():
    print(f"bound (2.23) 1/2<=a/c<=3/2 {k}:", bool(sp.Rational(1,2) <= a_/c_ <= sp.Rational(3,2)))

print("\n== 5. holographic normalization: a = (g-1) N^3 e^(3f0+2g0) J / pi^2, J = int Delta^-1/2 sqrt(h4) ==")
al, be, p1, p2 = sp.symbols('alpha beta phi1 phi2', real=True)
X0s, X1s, X2s = sp.symbols('X0 X1 X2', positive=True)
m0, m1, m2 = sp.cos(al), sp.sin(al)*sp.cos(be), sp.sin(al)*sp.sin(be)
h = sp.zeros(4)
dm = [[sp.diff(m, al), sp.diff(m, be)] for m in (m0, m1, m2)]
Xl = [X0s, X1s, X2s]
for i in range(2):
    for j in range(2):
        h[i,j] = sum(dm[k][i]*dm[k][j]/Xl[k] for k in range(3))
h[2,2] = m1**2/X1s; h[3,3] = m2**2/X2s
deth = sp.simplify(h.det())
Dl = X0s*m0**2+X1s*m1**2+X2s*m2**2
print("det h4 =", sp.factor(deth))
for k, fp in FP.items():
    sub = {X0s: fp['X0'], X1s: fp['X1'], X2s: fp['X2']}
    f = sp.lambdify((al, be), sp.sqrt(deth.subs(sub))/sp.sqrt(Dl.subs(sub)), 'mpmath')
    # mu1,mu2 >= 0 (phi1,phi2 carry the signs): beta in [0,pi/2]; mu0 in [-1,1]: alpha in [0,pi] = 2 x [0,pi/2]
    J = (2*mp.pi)**2*2*mp.quad(lambda A, B: f(A, B), [0, mp.pi/2], [0, mp.pi/2])
    e = float(fp['ef']**3*fp['e2g'])
    print(f"{k}: J/(8pi^2/3)={mp.nstr(J/(8*mp.pi**2/3),15)}  a/N^3 holo={mp.nstr((g-1)*e*J/mp.pi**2,15)} vs (4.7) {sp.N(LN[k],15) if k in LN else ''}")

print("\n== 6. 11D curvature: Einstein check R^t_t = -R (G4 has no AdS5 legs) and Phi = G.G = 144 R ==")
t,x1,x2,x3,r,u,v = sp.symbols('t x1 x2 x3 r u v', real=True)
coords = [t,x1,x2,x3,r,u,v,al,be,p1,p2]
X1s_, X2s_, F0s, G0s, a1s, a2s = sp.symbols('X1_ X2_ F0 G0 a1 a2', positive=True)
def build_symbolic():
    X1, X2 = X1s_, X2s_; X0 = 1/(X1*X2)**2
    D = X0*m0**2+X1*m1**2+X2*m2**2
    n = 11; G = sp.zeros(n); w7 = D**sp.Rational(1,3)
    for i, s_ in enumerate([-1,1,1,1,1]): G[i,i] = w7*F0s*s_/r**2
    G[5,5] = w7*G0s/v**2; G[6,6] = w7*G0s/v**2
    c = D**sp.Rational(-2,3)/4
    Xs = [X0,X1,X2]
    for i in range(2):
        for j in range(2):
            G[7+i,7+j] += c*sum(dm[k][i]*dm[k][j]/Xs[k] for k in range(3))
    for k,(ph,ai,mu) in enumerate([(9,a1s,m1),(10,a2s,m2)]):
        fac = c*mu**2/Xs[k+1]
        G[ph,ph] += fac; G[ph,5] += fac*ai/v; G[5,ph] += fac*ai/v; G[5,5] += fac*ai**2/v**2
    return G.applyfunc(sp.simplify)
def ricci(G):
    n = 11; dep = [r,v,al,be]
    Gi = G.inv(method='LU').applyfunc(sp.simplify)
    dg = {(a,b,cc): sp.diff(G[a,b],coords[cc]) for a in range(n) for b in range(n) for cc in range(n) if coords[cc] in dep and G[a,b]!=0}
    dG = lambda a,b,cc: dg.get((a,b,cc),0)
    Gam = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for cc in range(b,n):
                s_ = sum(Gi[a,d]*(dG(d,b,cc)+dG(d,cc,b)-dG(b,cc,d)) for d in range(n) if Gi[a,d]!=0)
                Gam[a][b][cc] = Gam[a][cc][b] = sp.together(s_/2)
    Ric = sp.zeros(n)
    for b in range(n):
        for cc in range(b,n):
            s_ = 0
            for a in range(n):
                if coords[a] in dep: s_ += sp.diff(Gam[a][b][cc], coords[a])
                if coords[cc] in dep: s_ -= sp.diff(Gam[a][b][a], coords[cc])
                for d in range(n):
                    s_ += Gam[a][a][d]*Gam[d][b][cc] - Gam[a][cc][d]*Gam[d][b][a]
            Ric[b,cc] = Ric[cc,b] = s_
    Rmix = Gi*Ric
    R = sum(Rmix[i,i] for i in range(n))
    RR = sum(Rmix[i,j]*Rmix[j,i] for i in range(n) for j in range(n))
    args = (X1s_,X2s_,F0s,G0s,a1s,a2s,r,v,al,be); exprs = [R, Rmix[0,0], Rmix[4,4], RR]
    return sp.lambdify(args, exprs, 'numpy'), sp.lambdify(args, exprs, 'mpmath')
t0 = time.time(); FR, FRmp = ricci(build_symbolic()); print(f"symbolic Ricci built in {time.time()-t0:.0f}s")
import numpy as np
AA, BB = np.meshgrid(np.linspace(0.02, np.pi-0.02, 61), np.linspace(0.02, np.pi/2-0.02, 31))  # float grid; edges done in mpmath below
EDGE = [(a_, b_) for a_ in ('1e-6','0.5','1.5707963','2.6','3.1415916') for b_ in ('1e-6','0.7853981','1.5707953')]
CURV = {}
def evalpt(par, rr, vv, A, B):
    return FRmp(*par, mp.mpf(rr), mp.mpf(vv), mp.mpf(A), mp.mpf(B))
GRID = [(mp.mpf(i)/8*mp.pi, mp.mpf(j)/4*mp.pi/2) for i in range(9) for j in range(5)]
GRID = [(A if A>0 else mp.mpf('1e-6'), B if B>0 else mp.mpf('1e-6')) for A,B in GRID]
GRID = [(A if A<mp.pi else mp.pi-mp.mpf('1e-6'), B if B<mp.pi/2 else mp.pi/2-mp.mpf('1e-6')) for A,B in GRID]
GRID += [(mp.mpf('0.37'), mp.mpf('1.11')), (mp.mpf('2.01'), mp.mpf('0.23')), (mp.mpf('1.3'), mp.mpf('0.9'))]
def run_case(k, par, expectR=None):
    mp.mp.dps = 60
    t1 = time.time()
    ev = [evalpt(par, 1, 1, A, B) for A, B in GRID]
    ev2 = [evalpt(par, '2.3', '0.7', A, B) for A, B in GRID[::7]]
    Rv = [e_[0] for e_ in ev]
    ein = max(abs(e_[1]+e_[0]) for e_ in ev); ein2 = max(abs(e_[2]+e_[0]) for e_ in ev)
    rind = max(abs(a_[0]-b_[0]) for a_, b_ in zip(ev[::7], ev2))
    Rmin, Rmax, RRmax = min(Rv), max(Rv), max(e_[3] for e_ in ev)
    line = (f"{k}: npts={len(GRID)} (incl. alpha,beta within 1e-6 of 0,pi/2,pi)  max|R^t_t+R|={mp.nstr(ein,3)}  max|R^r_r+R|={mp.nstr(ein2,3)}  "
            f"(r,v)-indep={mp.nstr(rind,3)}  R in [{mp.nstr(Rmin,10)},{mp.nstr(Rmax,10)}] (1/l^2)  max R_MN R^MN={mp.nstr(RRmax,10)}  [{time.time()-t1:.0f}s]")
    if expectR is not None: line += f"  |R-{expectR}|max={mp.nstr(max(abs(x_-expectR) for x_ in Rv),3)}"
    print(line, flush=True)
    mp.mp.dps = 30
    return ein, Rmin, Rmax, RRmax
print("-- 6a. validation of the routine on exact cases (X1=X2=1, a1=a2=0: AdS5(radius^2 F0) x H2(radius^2 G0) x round S4(radius 1/2)) --")
# (D) KR product in units r_S4 = 1/2: k = sqrt6/(4 r_S4)... r_S4 = sqrt6/(4k) -> k = sqrt6/2, L^2 = 1/k^2 = 2/3, rho^2 = 1/(4k^2) = 1/6; R = 4k^2 = 6 exactly
run_case("VALID (D) KR product F0=2/3 G0=1/6 [exact R=6, must pass]", [mp.mpf(1),mp.mpf(1),mp.mpf(2)/3,mp.mpf(1)/6,mp.mpf(0),mp.mpf(0)], expectR=6)
# wrong product: R = -20 - 2 + 48 = 26, R^t_t = -4 -> residual exactly 22, must fail
run_case("VALID-NEG product F0=G0=1 [not a solution: R=26, R^t_t=-4, residual must be 22]", [mp.mpf(1)]*4+[mp.mpf(0)]*2, expectR=26)
print("-- 6b. candidates --")
tests = dict(FP)
bad = dict(FP["BBBW(z=2)"]); bad['X1'] = bad['X1']*sp.Rational(11,10); bad['X0'] = (bad['X1']*bad['X2'])**-2
tests["NEG-CONTROL z=2 with X1*1.1"] = bad
for k, fp in tests.items():
    if 'mirror' in k: continue
    mp.mp.dps = 60
    par = [mp.mpf(sp.N(x_,60)) for x_ in (fp['X1'],fp['X2'],fp['ef']**2,fp['e2g'],fp['a1'],fp['a2'])]
    ein, Rmin, Rmax, RRmax = run_case(k, par)
    CURV[k] = (Rmin, Rmax, RRmax)
    print(f"    Phi=144R in [{mp.nstr(144*Rmin,8)},{mp.nstr(144*Rmax,8)}] /l^2 ; l_p^2 R_max={mp.nstr(Rmax/ell**2,6)}  l_p^2 Phi_max={mp.nstr(144*Rmax/ell**2,6)}  "
          f"l_p^2 sqrt(R_MN R^MN)_max={mp.nstr(mp.sqrt(RRmax)/ell**2,6)}  PASS(1e-10)={bool(ein<1e-10)}")
    if 'NEG' not in k:
        L5 = mp.mpf(sp.N(fp['ef'],30)); Lsig = mp.sqrt(mp.mpf(sp.N(fp['e2g'],30)))
        print(f"    sizes (units l): L5=e^f0={mp.nstr(L5,8)}, H2 radius e^g0={mp.nstr(Lsig,8)}, ratio e^g0/e^f0={mp.nstr(Lsig/L5,6)}; S4 radius ~1/2 (x Delta^-1/3 warp)")
print("\n(D) reference: R=4k^2, Phi=576k^2 with k = sqrt(3/8)(pi N)^(-1/3)/l_p")
k_D = mp.sqrt(mp.mpf(3)/8)*(mp.pi*N)**(-mp.mpf(1)/3)
print("   l_p^2 R_D =", mp.nstr(4*k_D**2, 6), " l_p^2 Phi_D =", mp.nstr(576*k_D**2, 6))
print("\n== 7. cross-check vs NL 418e4e50 (G5 ratios; a ~ L5^3/G5) ==")
L5D = mp.mpf('40.567128')
NL = {"MN2(z=1)":('37.653721','5.4118e-7','0.5804'), "MN1(z=0)":('39.470162','7.3878e-7','0.7923'),
      "BBBW(z=2)":('36.305054','3.7920e-7','0.4067'), "BBBW(z=3)":('35.600612','2.8868e-7','0.3096')}
G5D = mp.mpf('9.324866e-7')
print("a_D from NL C3: pi L5^3/(8 G5) =", mp.nstr(mp.pi*L5D**3/(8*G5D)/N**3, 8), "N^3 ; MR2 (8/81)sqrt6 =", sp.N(sp.Rational(8,81)*sp.sqrt(6), 8))
for k,(L5s,G5s,rs) in NL.items():
    fp = FP[k]; L5 = ell*mp.mpf(sp.N(fp['ef'],20))
    aX = mp.mpf(sp.N(LN[k],20))*N**3
    pred = (L5/L5D)**3*(mp.mpf(sp.N(aD,20))/aX)
    G5 = mp.pi*L5**3/(8*aX)
    print(f"{k}: L5=l e^f0={mp.nstr(L5,9)} (NL {L5s}); G5=pi L5^3/(8a)={mp.nstr(G5,6)} (NL {G5s}); G5/G5_D=(L5/L5D)^3 a_D/a={mp.nstr(pred,5)} (NL {rs}); a_D/a={mp.nstr(mp.mpf(sp.N(aD,20))/aX,6)}")
    A = mp.mpf(sp.N(fp['e2g'],20))*ell**2*4*mp.pi*(g-1)
    print(f"    Area(Sigma)=l^2 e^(2g0) 4pi(g-1)={mp.nstr(A,8)} l_p^2")
print("\nDONE")
