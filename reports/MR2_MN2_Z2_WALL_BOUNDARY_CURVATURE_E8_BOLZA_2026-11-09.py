#!/usr/bin/env python3
# MR2 2026-11-09: wall-boundary curvature check, MN N=2 (z=1) 11D vacuum, N=4880, g=2, Gamma = Bolza (OW 7ff8299d),
# face = Z2 fixed plane / HW-type wall with odd G4 (OW f825dfff). Additive; nothing adopted.
# Routines (geometry, NumGeom, invariants, sdet, hodge_num, cand_metric, Omega_sym, fixed points) are exec'd VERBATIM from the
# frozen blocker V2 .py (sha ad134752...), everything before its MAIN marker. sha is verified below before exec.
import hashlib, multiprocessing as mpc, time
V2 = '/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
raw = open(V2,'rb').read(); h = hashlib.sha256(raw).hexdigest()
assert h == 'ad134752da79e3064e209cd840b0aec53e004e3fa0fec8bbc9299eb12940eb85', h
exec(raw.decode().split('# ======================= MAIN =======================')[0])
import numpy as np
mp.mp.dps = 40
def P(s): print(s, flush=True)
P(f"V2 routines sha256 verified: {h}")
ell = 2*(mp.pi*N)**(mp.mpf(1)/3)
def fpar(fp):
    X1 = fp['X1']; X2 = fp['X2']; X0 = (X1*X2)**-2
    ef = 1/X0; e2g = X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2)
    return [mp.mpf(sp.N(x_, 45)) for x_ in (X1, X2, ef**2, e2g, fp['a1'], fp['a2'])]
# ======================================================================================
# V. VALIDATION of the wall routine on known cases
# ======================================================================================
P("\n== V1. flat-space HW-type wall in 11D: ds^2 = dy^2 + e^{2A(y)} eta_10, A = -k*eps*ln cosh(y/eps) (closed forms) ==")
yy, kk, ee = sp.symbols('y k_w eps_w', real=True)
xs = sp.symbols('w0:10', real=True)
Aw = -kk*ee*sp.log(sp.cosh(yy/ee))
GV = sp.zeros(11); GV[0,0] = -sp.exp(2*Aw)
for i in range(1,10): GV[i,i] = sp.exp(2*Aw)
GV[10,10] = 1
NV = NumGeom(GV, list(xs)+[yy], [yy], [kk, ee])
def closed(k, e, y, n=10):
    A1 = -k*mp.tanh(y/e); A2 = -(k/e)*mp.sech(y/e)**2
    K = 4*n*(A2+A1**2)**2 + 2*n*(n-1)*A1**4
    RR = n**2*(A2+A1**2)**2 + n*(A2+n*A1**2)**2
    R = -2*n*A2 - n*(n+1)*A1**2
    return K, RR, R
for (k, e, y) in [(mp.mpf('0.7'), mp.mpf('1e-3'), mp.mpf(0)), (mp.mpf('0.7'), mp.mpf('1e-3'), mp.mpf('0.3')),
                  (mp.mpf('0.7'), mp.mpf('1e-3'), mp.mpf('-0.3')), (mp.mpf(0), mp.mpf('1e-3'), mp.mpf(0))]:
    g_, gi_, Rm = NV.at([k, e], [y]); K, RR, W2, R, Ric, Qm, Qi = invariants(g_, gi_, Rm, 11)
    Kc, RRc, Rc = closed(k, e, y)
    P(f"  k={mp.nstr(k,3)} eps={mp.nstr(e,3)} y={mp.nstr(y,3)}: Riem^2={mp.nstr(K,15)} (closed {mp.nstr(Kc,15)}), Ric^2={mp.nstr(RR,15)} (closed {mp.nstr(RRc,15)}), R={mp.nstr(R,15)} (closed {mp.nstr(Rc,15)}), Weyl^2={mp.nstr(W2,8)}"
      + ("   [k=0 NO-SOURCE control: flat]" if k == 0 else ""))
P("  bulk |y|>>eps closed form = AdS11: Riem^2 = 2n(n+1)k^4 = 220 k^4 = " + mp.nstr(220*mp.mpf('0.7')**4, 12))
P("\n== V2. LOSW 5D domain wall (hep-th/9803235): ds^2 = a^2 eta_4 + b^2 dy^2, a = H^(1/2), b = H^2, H = c0 + h*eps*ln cosh(y/eps) ==")
c0s, hs = sp.symbols('c0 h_w', positive=True); ys5 = sp.symbols('q0:4', real=True)
Hs = c0s + hs*ee*sp.log(sp.cosh(yy/ee))
G5 = sp.zeros(5); G5[0,0] = -Hs
for i in range(1,4): G5[i,i] = Hs
G5[4,4] = Hs**4
N5 = NumGeom(G5, list(ys5)+[yy], [yy], [c0s, hs, ee])
def gl(nq):
    xg, wg = np.polynomial.legendre.leggauss(nq); return [mp.mpf(float(a)) for a in xg], [mp.mpf(float(b)) for b in wg]
XG, WG = gl(32)
def layer_integral(fun, e, Delta):
    # int_{-Delta}^{Delta} fun(y) dy with u = tanh(y/e): dy = e du/(1-u^2)
    U = mp.tanh(Delta/e); tot = None
    for xg, wg in zip(XG, WG):
        u = U*xg; y = e*mp.atanh(u); val = fun(y)*e/(1-u**2)*U*wg
        tot = val if tot is None else tot + val
    return tot
c0v, hv = mp.mpf('1.3'), mp.mpf('0.4')
for e in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')]:
    def Rb(y):
        g_, gi_, Rm = N5.at([c0v, hv, e], [y]); K, RR, W2, R, Ric, Qm, Qi = invariants(g_, gi_, Rm, 5)
        return R*mp.sqrt(g_[4,4])
    I = layer_integral(Rb, e, 10*e)
    g_, gi_, Rm = N5.at([c0v, hv, e], [mp.mpf(0)]); K0 = invariants(g_, gi_, Rm, 5)[0]
    P(f"  eps={mp.nstr(e,2)}: int R dY over [-10eps,10eps] = {mp.nstr(I,12)}  (thin-wall prediction -8h/c0^3 = {mp.nstr(-8*hv/c0v**3,12)});  eps^2*Riem^2(0) = {mp.nstr(e**2*K0,10)}")
P(f"  thin-wall centre prediction eps^2 Riem^2(0) -> 4n (h/(2 c0^5))^2 = 4 h^2/c0^10 = {mp.nstr(4*hv**2/c0v**10,10)}")
# ======================================================================================
# MN2 wall geometry: AdS5 radial coordinate rho = ln r ; Z2 glue at rho = delta with smoothed |.|
#   g_xx = w F0 exp(-2 sigma(rho)),  g_rhorho = w F0,  sigma = s*eps*ln cosh((rho-delta)/eps) + c*rho
#   KINK s=+1,c=0 : MN2 region r > r_b kept on both sides (orbifold glue);  WRONG-SIGN s=-1 : region r < r_b kept
#   NO-SOURCE s=0,c=1 : smooth MN2, no wall;  MISPLACED : s=+1, delta=0.3, wall presumed at rho=0
# ======================================================================================
rho = sp.symbols('rho', real=True); EPS, SG, DL, CC = sp.symbols('epsilon s_sign delta c_lin', real=True)
sig = SG*EPS*sp.log(sp.cosh((rho-DL)/EPS)) + CC*rho
def wall_metric():
    X1, X2 = X1s, X2s; X0 = 1/(X1*X2)**2
    D = X0*m0**2+X1*m1**2+X2*m2**2
    G = sp.zeros(11); w7 = D**sp.Rational(1,3)
    for i, s_ in enumerate([-1,1,1,1]): G[i,i] = w7*F0s*s_*sp.exp(-2*sig)
    G[4,4] = w7*F0s
    G[5,5] = w7*G0s/v**2; G[6,6] = w7*G0s/v**2
    c = D**sp.Rational(-2,3)/4
    dm = [[sp.diff(m, al), sp.diff(m, be)] for m in (m0, m1, m2)]; Xs = [X0, X1, X2]
    for i in range(2):
        for j in range(2):
            G[7+i,7+j] += c*sum(dm[k][i]*dm[k][j]/Xs[k] for k in range(3))
    for k,(ph,ai,mu) in enumerate([(9,a1s,m1),(10,a2s,m2)]):
        fac = c*mu**2/Xs[k+1]
        G[ph,ph] += fac; G[ph,5] += fac*ai/v; G[5,ph] += fac*ai/v; G[5,5] += fac*ai**2/v**2
    return G
P("\n== building MN2 wall geometry ==")
coordsW = [t,x1,x2,x3,rho,u,v,al,be,p1,p2]
GW = wall_metric()
NW = NumGeom(GW, coordsW, [rho,v,al,be], PARAMS+[EPS,SG,DL,CC])
fp = FP["MN2(z=1)"]; PAR = fpar(fp)
X1n, X2n, F0n, G0n, a1n, a2n = PAR; X0n = 1/(X1n*X2n)**2
P(f"MN2 fixed point: X1={mp.nstr(X1n,15)} X2={mp.nstr(X2n,15)} X0={mp.nstr(X0n,15)} e^(2f0)=F0={mp.nstr(F0n,15)} e^(2g0)=G0={mp.nstr(G0n,15)} a1={a1n} a2={a2n}; l/l_p={mp.nstr(ell,10)}")
def Dfun(a_, b_): return X0n*mp.cos(a_)**2 + X1n*(mp.sin(a_)*mp.cos(b_))**2 + X2n*(mp.sin(a_)*mp.sin(b_))**2
def wF0(a_, b_): return Dfun(a_, b_)**(mp.mpf(1)/3)*F0n
CASES = {"KINK": (1,0,0), "WRONG_SIGN": (-1,0,0), "NO_SOURCE": (0,1,0), "MISPLACED(delta=0.3)": (1,0,mp.mpf('0.3'))}
def ev(args):
    case, e, r_, a_, b_ = args; s_, c_, d_ = CASES[case]
    g_, gi_, Rm = NW.at(PAR+[e, s_, d_, c_], [r_, mp.mpf(1), a_, b_])
    K, RR, W2, R, Ric, Qm, Qi = invariants(g_, gi_, Rm, 11)
    Rmix = gi_*Ric
    Gmix = [[Rmix[i,j] - (R/2 if i == j else 0) for j in range(11)] for i in range(11)]
    return dict(K=K, RR=RR, W2=W2, R=R, Q=Qm, Gmix=Gmix, sqrtgrr=mp.sqrt(g_[4,4]))
def pmap(argl):
    with mpc.get_context('fork').Pool(8) as pool: return pool.map(ev, argl)
eps_ = mp.mpf('1e-6'); dl = mp.mpf('1.234e-3')
ALS = [eps_, mp.pi/4+dl, mp.pi/2+dl, 3*mp.pi/4+dl, mp.pi-eps_]; BES = [eps_, mp.pi/4+dl, mp.pi/2-eps_]
GRID = [(a_, b_) for a_ in ALS for b_ in BES] + [(mp.mpf('0.37'), mp.mpf('1.11')), (mp.mpf('2.01'), mp.mpf('0.23'))]
# ---------------- (i) one-sided bulk limits ----------------
P("\n== (i) one-sided bulk limits: KINK, eps=1e-4, rho = +0.5 and -0.5 (proper distance l*sqrt(wF0)*0.5 from the wall), 17-pt grid ==")
for rr in [mp.mpf('0.5'), mp.mpf('-0.5'), mp.mpf('0.01'), mp.mpf('-0.01')]:
    out = pmap([("KINK", mp.mpf('1e-4'), rr, a_, b_) for a_, b_ in GRID])
    Ks = [o['K'] for o in out]; RRs = [o['RR'] for o in out]; Ws = [o['W2'] for o in out]; Rs = [o['R'] for o in out]; Qs = [o['Q'] for o in out]
    P(f"  rho={mp.nstr(rr,3)}: Riem^2 in [{mp.nstr(min(Ks),10)}, {mp.nstr(max(Ks),10)}], Ric^2 max {mp.nstr(max(RRs),10)}, Weyl^2 in [{mp.nstr(min(Ws),10)}, {mp.nstr(max(Ws),10)}], R in [{mp.nstr(min(Rs),8)}, {mp.nstr(max(Rs),8)}], max|eig Q| {max(Qs):.6f}  (/l^4, /l^2)")
P("  reference 9ab8f0a6 (MN2, r-coords): Riem^2 in [511.808, 3407.981], Ric^2 max 3311.98, Weyl^2 in [297.90, 1939.19], max|eig Q| 13.333308")
# ---------------- (iii) thin-wall scaling at the wall centre ----------------
P("\n== (iii) wall centre rho=0: scaling with eps (KINK); thin-wall prediction from Israel kink: a = 1/(wF0*eps) ->")
P("   eps^2 Riem^2 -> 16/(wF0)^2, eps^2 Ric^2 -> 20/(wF0)^2, eps^2 R^2 -> 64/(wF0)^2, eps^2 Weyl^2 -> (128/15)/(wF0)^2, eps*R -> +8/(wF0) (s=+1), eps*maxeig -> 1/(wF0)")
EPSL = [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5')]
SC = {}
for e in EPSL:
    SC[e] = pmap([("KINK", e, mp.mpf(0), a_, b_) for a_, b_ in GRID])
worst = {}
for e in EPSL:
    devs = []
    for (a_, b_), o in zip(GRID, SC[e]):
        q = wF0(a_, b_)
        devs.append(max(abs(e**2*o['K']*q**2/16-1), abs(e**2*o['RR']*q**2/20-1), abs(e**2*o['R']**2*q**2/64-1),
                        abs(e**2*o['W2']*q**2/(mp.mpf(128)/15)-1), abs(e*o['R']*q/8-1), abs(e*o['Q']*float(q)-1)))
    worst[e] = max(devs)
    P(f"  eps={mp.nstr(e,2)}: max over grid of relative deviation from thin-wall coefficients = {mp.nstr(worst[e],4)}")
for i, (a_, b_) in enumerate([GRID[4], GRID[15]]):
    j = GRID.index((a_, b_))
    sl = [mp.log(SC[EPSL[n+1]][j]['K']/SC[EPSL[n]][j]['K'])/mp.log(EPSL[n+1]/EPSL[n]) for n in range(3)]
    slW = [mp.log(SC[EPSL[n+1]][j]['W2']/SC[EPSL[n]][j]['W2'])/mp.log(EPSL[n+1]/EPSL[n]) for n in range(3)]
    P(f"  log-log slopes at (alpha,beta)=({mp.nstr(a_,4)},{mp.nstr(b_,4)}): d ln Riem^2/d ln eps = {[mp.nstr(x,8) for x in sl]}; Weyl^2: {[mp.nstr(x,8) for x in slW]}")
# ---------------- controls at the centre ----------------
P("\n== controls at the presumed wall rho=0 (eps=1e-4 and 1e-5) ==")
for case in ["NO_SOURCE", "WRONG_SIGN", "MISPLACED(delta=0.3)"]:
    for e in [mp.mpf('1e-4'), mp.mpf('1e-5')]:
        out = pmap([(case, e, mp.mpf(0), a_, b_) for a_, b_ in GRID])
        P(f"  {case} eps={mp.nstr(e,2)} rho=0: max Riem^2 {mp.nstr(max(o['K'] for o in out),10)}, max Weyl^2 {mp.nstr(max(o['W2'] for o in out),10)}, R range [{mp.nstr(min(o['R'] for o in out),8)}, {mp.nstr(max(o['R'] for o in out),8)}]")
out = pmap([("MISPLACED(delta=0.3)", mp.mpf('1e-4'), mp.mpf('0.3'), a_, b_) for a_, b_ in GRID])
P(f"  MISPLACED eps=1e-4 at rho=0.3 (where the kink actually is): max Riem^2 {mp.nstr(max(o['K'] for o in out),6)}  (diverges there instead)")
# ---------------- (ii) distributional part: Israel ----------------
P("\n== (ii) distributional part: int G^a_b dy_proper across [-10eps, 10eps], eps=1e-5 (uplift units, dy = sqrt(wF0) drho) ==")
P("   Israel thin-wall prediction (s=+1): x-block (t,x1..x3) -6k, rho-rho 0, internal 6-block -8k * delta^a_b, k = 1/sqrt(wF0)")
PTS3 = [(mp.mpf('0.37'), mp.mpf('1.11')), (mp.mpf('2.01'), mp.mpf('0.23')), (mp.pi/2+dl, mp.pi/4+dl)]
e = mp.mpf('1e-5'); Delta = 10*e
UU = mp.tanh(Delta/e)
ISR = {}
for case in ["KINK", "WRONG_SIGN", "NO_SOURCE", "MISPLACED(delta=0.3)"]:
    for (a_, b_) in PTS3:
        argl = []; wts = []
        for xg, wg in zip(XG, WG):
            uq = UU*xg; y = e*mp.atanh(uq); argl.append((case, e, y, a_, b_)); wts.append(e/(1-uq**2)*UU*wg)
        out = pmap(argl)
        I = [[sum(o['Gmix'][i][j]*o['sqrtgrr']*w for o, w in zip(out, wts)) for j in range(11)] for i in range(11)]
        k = 1/mp.sqrt(wF0(a_, b_)); ISR[(case, a_, b_)] = (I, k)
        diag = [I[i][i]/k for i in range(11)]
        off = max(abs(I[i][j]) for i in range(11) for j in range(11) if i != j)/k
        P(f"  {case} (a,b)=({mp.nstr(a_,4)},{mp.nstr(b_,4)}): diag(int G^a_a dy)/k = {[mp.nstr(x,7) for x in diag]}; max offdiag/k = {mp.nstr(off,3)}")
# physical Israel stress, energy density, comparison with BPS M5/E8 count
P("\n== magnitudes at N=4880 (physical units l_p = 1; 2 kappa^2 = (2pi)^8 l_p^9, T_M5 = 1/((2pi)^5 l_p^6): CONDITIONAL standard normalisation) ==")
kap2 = (2*mp.pi)**8/2; TM5 = 1/(2*mp.pi)**5
QG = gl(24); XA = [(x+1)*mp.pi/2 for x in QG[0]]; WA = [w*mp.pi/2 for w in QG[1]]
QB = gl(16); XB = [(x+1)*mp.pi/4 for x in QB[0]]; WB = [w*mp.pi/4 for w in QB[1]]
gk_ = [(i,j) for i in range(11) for j in range(11) if GW[i,j] != 0]
gfun = lamb(PARAMS+[EPS,SG,DL,CC]+[rho,v,al,be], [GW[i,j] for i,j in gk_])
def met(par, a_, b_):
    vals = gfun(*(list(par)+[mp.mpf('1e-3'),1,0,0]+[mp.mpf(0), mp.mpf(1), a_, b_])); g_ = mp.zeros(11)
    for (i,j), x in zip(gk_, vals): g_[i,j] = x
    return g_
# measure validation: round S4 radius 1/2 inside the ansatz (X=1, a=0): int sqrt(det g_S4) = pi^2/6 ... (x 4pi^2 from phi's)
parD = [mp.mpf(1), mp.mpf(1), mp.mpf(2)/3, mp.mpf(1)/6, mp.mpf(0), mp.mpf(0)]
volD = 4*mp.pi**2*sum(wa*wb*mp.sqrt(mp.det(mp.matrix([[met(parD, a_, b_)[i,j] for j in range(7,11)] for i in range(7,11)])))
                      for a_, wa in zip(XA, WA) for b_, wb in zip(XB, WB))
P(f"  measure check: Vol(round S4, radius 1/2) = {mp.nstr(volD,15)} (exact pi^2/6 = {mp.nstr(mp.pi**2/6,15)})")
Nh = 0; Nf = 0; kmin = mp.inf; kmax = 0; Dmin = mp.inf; Dmax = 0; Dmin_mu1 = mp.inf
for a_, wa in zip(XA, WA):
    for b_, wb in zip(XB, WB):
        g_ = met(PAR, a_, b_); k = 1/mp.sqrt(wF0(a_, b_))
        d6 = mp.det(mp.matrix([[g_[i,j] for j in range(5,11)] for i in range(5,11)]))
        duv_f = g_[5,5]*g_[6,6]; duv_h = (Dfun(a_, b_)**(mp.mpf(1)/3)*G0n)**2
        Nh += wa*wb*k*mp.sqrt(d6)/mp.sqrt(duv_h); Nf += wa*wb*k*mp.sqrt(d6)/mp.sqrt(duv_f)
for a_ in [mp.mpf(i)/400*mp.pi for i in range(401)]:
    for b_ in [mp.mpf(j)/200*mp.pi/2 for j in range(201)]:
        D_ = Dfun(a_, b_); Dmin = min(Dmin, D_); Dmax = max(Dmax, D_)
    Dmin_mu1 = min(Dmin_mu1, Dfun(a_, mp.pi/2))
Dmin_mu1 = min(Dmin_mu1, Dfun(0, 0))
k_lo = 1/mp.sqrt(Dmax**(mp.mpf(1)/3)*F0n)/ell; k_hi = 1/mp.sqrt(Dmin**(mp.mpf(1)/3)*F0n)/ell
P(f"  D = X0 mu0^2 + X1 mu1^2 + X2 mu2^2 in [{mp.nstr(Dmin,10)}, {mp.nstr(Dmax,10)}] (401x201 scan)")
P(f"  physical k = 1/(l sqrt(w F0)) in [{mp.nstr(k_lo,8)}, {mp.nstr(k_hi,8)}] / l_p   (L5 = l e^f0 = {mp.nstr(ell*mp.sqrt(F0n),10)} l_p)")
P(f"  distributional Ricci scalar weight  int R dy = 16k in [{mp.nstr(16*k_lo,6)}, {mp.nstr(16*k_hi,6)}] / l_p")
P(f"  Israel wall energy density rho_w = 6k/kappa^2 in [{mp.nstr(6*k_lo/kap2,6)}, {mp.nstr(6*k_hi/kap2,6)}] l_p^-10 ; internal pressures p = -8k/kappa^2")
P(f"  thin-wall centre for physical thickness eps_y: l_p^2 sqrt(Riem^2) = 4 k l_p^2/eps_y -> at eps_y = l_p: [{mp.nstr(4*k_lo,6)}, {mp.nstr(4*k_hi,6)}]; reaches 1 at eps_y = 4k l_p^2 <= {mp.nstr(4*k_hi,6)} l_p")
P(f"  BPS M5/E8 comparison: N_req = (12N/pi^2) * 4pi^2 * int k sqrt(det g6)/sqrt(det g_Sigma) dalpha dbeta")
P(f"     horizontal Sigma measure: N_req/(2N) = {mp.nstr(6/mp.pi**2*4*mp.pi**2*Nh,10)} ; fixed-phi embedding measure: N_req/(2N) = {mp.nstr(6/mp.pi**2*4*mp.pi**2*Nf,10)}")
# flux through S4 at the wall and the odd-G4 jump
P("\n== odd G4 at the wall: flux integral and parity ==")
GC = cand_metric(); Om_s, U_s = Omega_sym(); Om_keys = list(Om_s.keys())
Om_f = lamb(PARAMS+[LAM, KAP]+dep, [Om_s[kk_] for kk_ in Om_keys])
gkc = [(i,j) for i in range(11) for j in range(11) if GC[i,j] != 0]
gcf = lamb(PARAMS+dep, [GC[i,j] for i,j in gkc])
def G4at(args):
    a_, b_ = args
    vals = gcf(*(PAR+[mp.mpf(1), mp.mpf(1), a_, b_])); g_ = mp.zeros(11)
    for (i,j), x in zip(gkc, vals): g_[i,j] = x
    ov = Om_f(*(PAR+[mp.mpf(1)/16, 1]+[mp.mpf(1), mp.mpf(1), a_, b_])); Om = {kk_: x for kk_, x in zip(Om_keys, ov) if x != 0}
    return hodge_num(Om, g_, g_**-1, 11, 7)
QG2 = gl(12); XA2 = [(x+1)*mp.pi/2 for x in QG2[0]]; WA2 = [w*mp.pi/2 for w in QG2[1]]
QB2 = gl(8); XB2 = [(x+1)*mp.pi/4 for x in QB2[0]]; WB2 = [w*mp.pi/4 for w in QB2[1]]
pts = [(a_, b_) for a_ in XA2 for b_ in XB2]; wts = [wa*wb for wa in WA2 for wb in WB2]
with mpc.get_context('fork').Pool(8) as pool: G4s = pool.map(G4at, pts)
flux = 4*mp.pi**2*sum(w*G.get((7,8,9,10), 0) for w, G in zip(wts, G4s))
keys = set().union(*[set(kk_ for kk_, x in G.items() if abs(x) > 1e-30) for G in G4s])
flux=abs(flux)
P(f"  |int_S4 G4| (uplift, lambda=1/16, kappa=1) = {mp.nstr(flux,15)}  (pi^2 = {mp.nstr(mp.pi**2,15)});  N = flux/pi^2 * 4880 = {mp.nstr(flux/mp.pi**2*N,12)}")
P(f"  odd extension: [G4] = 2 G4 -> wall charge int_S4 [G4]/(2 pi l_p)^3 = {mp.nstr(2*flux/mp.pi**2*N,12)} = 2N_flux")
P(f"  nonzero G4 index sets (coords t,x1,x2,x3,r,u,v,alpha,beta,phi1,phi2 = 0..10): {sorted(keys)}")
P(f"  every component tangent to a constant-r wall (no index 4): {all(4 not in kk_ for kk_ in keys)} ; every component carries a phi2 leg (index 10): {all(10 in kk_ for kk_ in keys)}")
P("  Bianchi controls (exact algebra on the odd profile G(rho) = sgn(rho) G_MN2): required source J = 2 G_MN2|wall delta(rho); residual charge int_S4(dG - J):")
for lbl, q in [("correct source", 2), ("NO source", 0), ("WRONG-SIGN source", -2)]:
    P(f"     {lbl}: residual = {(2-q)}*N = {(2-q)*N} units at the wall")
P(f"     MISPLACED source (at rho=0.3): residual {2*N} at rho=0 and {-2*N} at rho=0.3")
# ---------------- global scan (bulk invariants; Gamma-independent) ----------------
P("\n== global scan of bulk MN2 invariants (rho=0.5, KINK eps=1e-4 => exact MN2), 25 alpha x 13 beta incl. 1e-6 edges ==")
AS = [mp.mpf('1e-6')] + [mp.pi*i/24 + dl for i in range(1,24)] + [mp.pi-mp.mpf('1e-6')]
BS = [mp.mpf('1e-6')] + [mp.pi/2*j/12 + dl for j in range(1,12)] + [mp.pi/2-mp.mpf('1e-6')]
SCAN = [(a_, b_) for a_ in AS for b_ in BS]
out = pmap([("KINK", mp.mpf('1e-4'), mp.mpf('0.5'), a_, b_) for a_, b_ in SCAN])
iK = max(range(len(out)), key=lambda i: out[i]['K']); iQ = max(range(len(out)), key=lambda i: out[i]['Q'])
P(f"  {len(SCAN)} pts: Riem^2 max {mp.nstr(out[iK]['K'],10)} at {[mp.nstr(x,5) for x in SCAN[iK]]}; Ric^2 max {mp.nstr(max(o['RR'] for o in out),10)}; Weyl^2 max {mp.nstr(max(o['W2'] for o in out),10)}; |R| max {mp.nstr(max(abs(o['R']) for o in out),8)}; max|eig Q| {out[iQ]['Q']:.6f} at {[mp.nstr(x,5) for x in SCAN[iQ]]}")
Km = out[iK]['K']; Qm_ = out[iQ]['Q']
P(f"  l_p^2 sqrt(Riem^2)_max = {mp.nstr(mp.sqrt(Km)/ell**2,6)} ; l_p^2 max|K_sec| <= {Qm_/float(ell)**2:.4e}")
# 1D refinement along beta = pi/2 - 1e-6 and alpha edges
ref = [(mp.mpf(a_), mp.pi/2-mp.mpf('1e-6')) for a_ in np.linspace(1e-6, float(mp.pi)-1e-6, 121)] + [(mp.mpf('1e-6'), mp.mpf(b_)) for b_ in np.linspace(1e-6, float(mp.pi/2)-1e-6, 61)]
out2 = pmap([("KINK", mp.mpf('1e-4'), mp.mpf('0.5'), a_, b_) for a_, b_ in ref])
P(f"  edge refinement {len(ref)} pts: Riem^2 max {mp.nstr(max(o['K'] for o in out2),10)}; max|eig Q| {max(o['Q'] for o in out2):.6f}")
# ---------------- Bolza systole ----------------
P("\n== Sigma systole with Gamma = Bolza (OW 7ff8299d) ==")
sysB = 2*mp.acosh(1+mp.sqrt(2)); rhoS = ell*mp.sqrt(G0n)
P(f"  sys_hyp(Bolza) = 2 arccosh(1+sqrt2) = {mp.nstr(sysB,13)} (CONDITIONAL lit.); rho_Sigma = {mp.nstr(rhoS,10)} l_p; unwarped sys = {mp.nstr(sysB*rhoS,10)} l_p")
P(f"  warped 11D lower bound rho_Sigma*min D^(1/6)*sys = {mp.nstr(rhoS*Dmin**(mp.mpf(1)/6)*sysB,10)} l_p ; upper bound (closed lift on mu1=0 locus) rho_Sigma*min_mu1=0 D^(1/6)*sys = {mp.nstr(rhoS*Dmin_mu1**(mp.mpf(1)/6)*sysB,10)} l_p")
P(f"  warp factors D^(1/6) in [{mp.nstr(Dmin**(mp.mpf(1)/6),8)}, {mp.nstr(Dmax**(mp.mpf(1)/6),8)}]; rho_Sigma*D^(1/6) in [{mp.nstr(rhoS*Dmin**(mp.mpf(1)/6),6)}, {mp.nstr(rhoS*Dmax**(mp.mpf(1)/6),6)}] l_p (PP warped range for MN2: [24.8, 27.9])")
P(f"\nDONE {time.time()-T0:.0f}s")
