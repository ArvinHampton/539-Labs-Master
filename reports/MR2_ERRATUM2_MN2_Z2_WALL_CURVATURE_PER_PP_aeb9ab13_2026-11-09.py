#!/usr/bin/env python3
# MR2 ERRATUM2 checks (2026-11-09) for PP audit aeb9ab13 of MR2 bd47ff5e / 2368ffbd. Additive; nothing adopted by this script.
# Routines (NumGeom, invariants, hodge_num, cand_metric, Omega_sym, FP) exec'd verbatim from the frozen V2 .py (sha ad134752...),
# everything before its MAIN marker, with its stdout banner SUPPRESSED (fix 10: stale banner). mp.dps = 60 throughout.
import hashlib, io, contextlib, multiprocessing as mpc, time
T00 = time.time()
V2 = '/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
raw = open(V2,'rb').read(); h = hashlib.sha256(raw).hexdigest()
assert h == 'ad134752da79e3064e209cd840b0aec53e004e3fa0fec8bbc9299eb12940eb85', h
with contextlib.redirect_stdout(io.StringIO()):
    exec(raw.decode().split('# ======================= MAIN =======================')[0])
import numpy as np
mp.mp.dps = 60
def P(s): print(s, flush=True)
P("== MR2 ERRATUM2 checks per PP aeb9ab13 (MN2 Z2-wall curvature), dps=60 ==")
P(f"V2 routines sha256 verified: {h} (V2 prelude stdout suppressed)")
def fpar(fp):
    X1 = fp['X1']; X2 = fp['X2']; X0 = (X1*X2)**-2
    ef = 1/X0; e2g = X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2)
    return [X1, X2, ef**2, e2g, fp['a1'], fp['a2']]
fp = FP["MN2(z=1)"]; PARs = fpar(fp)
P(f"\n== H. exact fixed-point data (sympy) ==")
P(f"  X1 = {sp.nsimplify(PARs[0])}, X2 = {sp.nsimplify(PARs[1])}, X0 = {sp.simplify((PARs[0]*PARs[1])**-2)}, F0 = {sp.simplify(PARs[2])}, G0 = {sp.simplify(PARs[3])}")
X1e, X2e, F0e = PARs[0], PARs[1], PARs[2]
wmin = sp.simplify(X1e**sp.Rational(1,3)*F0e); wmax = sp.simplify(X2e**sp.Rational(1,3)*F0e)
P(f"  min wF0 = X1^(1/3) F0 = {wmin} ; max wF0 = X2^(1/3) F0 = {wmax} = {sp.N(wmax,20)} ; (wF0)^2 in [{sp.simplify(wmin**2)}, {sp.N(wmax**2,12)}]")
PAR = [mp.mpf(sp.N(x_, 80)) for x_ in PARs]
X1n, X2n, F0n, G0n, a1n, a2n = PAR; X0n = 1/(X1n*X2n)**2
N_ = N
# ---------------- mp Gauss-Legendre ----------------
def glmp(n):
    xs, ws = [], []
    for i in range(1, n+1):
        x = mp.cos(mp.pi*(i-mp.mpf(1)/4)/(n+mp.mpf(1)/2))
        for _ in range(100):
            p0, p1 = mp.mpf(1), x
            for k in range(2, n+1): p0, p1 = p1, ((2*k-1)*x*p1-(k-1)*p0)/k
            dp = n*(x*p1-p0)/(x**2-1); dx = p1/dp; x -= dx
            if abs(dx) < mp.mpf(10)**(-mp.mp.dps+5): break
        p0, p1 = mp.mpf(1), x
        for k in range(2, n+1): p0, p1 = p1, ((2*k-1)*x*p1-(k-1)*p0)/k
        dp = n*(x*p1-p0)/(x**2-1)
        xs.append(x); ws.append(2/((1-x**2)*dp**2))
    return xs, ws
# ======================================================================================
# 1. flux integral at 60 digits, GL orders 12x8 (old), 24x16, 40x40, 60x60
# ======================================================================================
P("\n== 1. int_{S4} G4 (uplift, lambda=1/16, kappa=1) vs pi^2 at dps 60 ==")
GC = cand_metric(); Om_s, U_s = Omega_sym(); Om_keys = list(Om_s.keys())
Om_f = lamb(PARAMS+[LAM, KAP]+dep, [Om_s[kk_] for kk_ in Om_keys])
gkc = [(i,j) for i in range(11) for j in range(11) if GC[i,j] != 0]
gcf = lamb(PARAMS+dep, [GC[i,j] for i,j in gkc])
P(f"  metric symbols: {sorted(str(s) for s in GC.free_symbols)} (phi1, phi2 absent => cyclic); g[phi2,u] = {GC[10,5]} -> at a2=0: {GC[10,5].subs(a2s,0)}")
def G4at(ab):
    a_, b_ = ab
    vals = gcf(*(PAR+[mp.mpf(1), mp.mpf(1), a_, b_])); g_ = mp.zeros(11)
    for (i,j), x in zip(gkc, vals): g_[i,j] = x
    ov = Om_f(*(PAR+[mp.mpf(1)/16, 1]+[mp.mpf(1), mp.mpf(1), a_, b_])); Om = {kk_: x for kk_, x in zip(Om_keys, ov) if x != 0}
    return hodge_num(Om, g_, g_**-1, 11, 7)
FL = {}
for (na, nb) in [(12, 8), (24, 16), (40, 40), (60, 60)]:
    xa, wa = glmp(na); xb, wb = glmp(nb)
    pts = [((x+1)*mp.pi/2, (y+1)*mp.pi/4) for x in xa for y in xb]; wts = [u*mp.pi/2*v*mp.pi/4 for u in wa for v in wb]
    with mpc.get_context('fork').Pool(8) as pool: Gs = pool.map(G4at, pts)
    fl = abs(4*mp.pi**2*sum(w*G.get((7,8,9,10), 0) for w, G in zip(wts, Gs)))
    FL[(na,nb)] = fl
    keys = set().union(*[set(kk_ for kk_, x in G.items() if abs(x) > mp.mpf(10)**-50) for G in Gs])
    P(f"  GL {na}x{nb}: |flux| = {mp.nstr(fl,40)} ; flux/pi^2 - 1 = {mp.nstr(fl/mp.pi**2-1,5)} ; N = {mp.nstr(fl/mp.pi**2*N_,30)}")
P(f"  pi^2              = {mp.nstr(mp.pi**2,40)}")
P(f"  nonzero G4 index sets (t,x1,x2,x3,r,u,v,al,be,p1,p2=0..10): {sorted(keys)}; each has exactly one phi2 (10) leg: {all(sum(1 for i in kk_ if i==10)==1 for kk_ in keys)}; none has r (4): {all(4 not in kk_ for kk_ in keys)}")
# ======================================================================================
# wall geometry (same construction as bd47ff5e .py), rebuilt here
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
def Dfun(a_, b_): return X0n*mp.cos(a_)**2 + X1n*(mp.sin(a_)*mp.cos(b_))**2 + X2n*(mp.sin(a_)*mp.sin(b_))**2
def wF0(a_, b_): return Dfun(a_, b_)**(mp.mpf(1)/3)*F0n
CASES = {"KINK": (1,0,0), "NO_SOURCE": (0,1,0)}
def ev(args):
    case, e, r_, a_, b_ = args; s_, c_, d_ = CASES[case]
    g_, gi_, Rm = NW.at(PAR+[e, s_, d_, c_], [r_, mp.mpf(1), a_, b_])
    K, RR, W2, R, Ric, Qm, Qi = invariants(g_, gi_, Rm, 11)
    Rmix = gi_*Ric
    Gd = [Rmix[i,i] - R/2 for i in range(11)]
    off = max(abs(Rmix[i,j]) for i in range(11) for j in range(11) if i != j)
    return dict(K=K, RR=RR, W2=W2, R=R, Q=Qm, Gd=Gd, off=off, sqrtgrr=mp.sqrt(g_[4,4]))
def pmap(argl):
    with mpc.get_context('fork').Pool(8) as pool: return pool.map(ev, argl)
# ======================================================================================
# 5. global maximum: the beta -> 0 edge (mu1 -> 1 at alpha = pi/2), smooth MN2 (NO_SOURCE, rho=0)
# ======================================================================================
P("\n== 5. beta -> 0 edge of the MN2 bulk invariants (NO_SOURCE = smooth MN2, rho=0, eps irrelevant) ==")
e0 = mp.mpf('1e-4')
bl = [mp.mpf(10)**-k for k in range(2, 16, 1)]
out = pmap([("NO_SOURCE", e0, mp.mpf(0), mp.pi/2, b_) for b_ in bl])
for b_, o in zip(bl, out):
    P(f"  alpha=pi/2, beta=1e{int(mp.log10(b_))}: Riem^2 = {mp.nstr(o['K'],30)} (-3408: {mp.nstr(o['K']-3408,5)}); max|eig Q| = {mp.nstr(o['Q'],25)} (-40/3: {mp.nstr(o['Q']-mp.mpf(40)/3,5)})")
bE = mp.mpf('1e-12')
AL = [mp.mpf('1e-6') + (mp.pi-mp.mpf('2e-6'))*i/180 for i in range(181)]
out = pmap([("NO_SOURCE", e0, mp.mpf(0), a_, bE) for a_ in AL])
iK = max(range(len(out)), key=lambda i: out[i]['K']); iQ = max(range(len(out)), key=lambda i: out[i]['Q'])
P(f"  edge beta=1e-12, 181 alpha in (0,pi): Riem^2 max {mp.nstr(out[iK]['K'],20)} at alpha={mp.nstr(AL[iK],8)}; max|eig Q| max {mp.nstr(out[iQ]['Q'],20)} at alpha={mp.nstr(AL[iQ],8)}")
loc = [(mp.pi/2 + mp.mpf(i)/50, mp.mpf(10)**-12 + mp.mpf(j)/50) for i in range(-10, 11) for j in range(0, 11)]
out = pmap([("NO_SOURCE", e0, mp.mpf(0), a_, b_) for a_, b_ in loc])
iK = max(range(len(out)), key=lambda i: out[i]['K']); iQ = max(range(len(out)), key=lambda i: out[i]['Q'])
P(f"  local 21x11 grid alpha in pi/2+[-0.2,0.2], beta in [1e-12,0.2]: Riem^2 max {mp.nstr(out[iK]['K'],20)} at {[mp.nstr(x,6) for x in loc[iK]]}; max|eig Q| max {mp.nstr(out[iQ]['Q'],20)} at {[mp.nstr(x,6) for x in loc[iQ]]}")
GA = [mp.mpf('1e-9')] + [mp.pi*i/48 + mp.mpf('1.234e-3') for i in range(1,48)] + [mp.pi-mp.mpf('1e-9')]
GB = [mp.mpf('1e-12')] + [mp.pi/2*j/24 + mp.mpf('1.234e-3') for j in range(1,24)] + [mp.pi/2-mp.mpf('1e-12')]
out = pmap([("NO_SOURCE", e0, mp.mpf(0), a_, b_) for a_ in GA for b_ in GB])
SC = [(a_, b_) for a_ in GA for b_ in GB]
iK = max(range(len(out)), key=lambda i: out[i]['K']); iQ = max(range(len(out)), key=lambda i: out[i]['Q'])
P(f"  global {len(GA)}x{len(GB)} = {len(SC)} pts incl. edges at 1e-9/1e-12: Riem^2 max {mp.nstr(out[iK]['K'],20)} at {[mp.nstr(x,6) for x in SC[iK]]}; max|eig Q| {mp.nstr(out[iQ]['Q'],20)} at {[mp.nstr(x,6) for x in SC[iQ]]}")
ell = 2*(mp.pi*N_)**(mp.mpf(1)/3)
P(f"  l/l_p = {mp.nstr(ell,15)}; l_p^2 sqrt(3408)/l^2 = {mp.nstr(mp.sqrt(3408)/ell**2,10)}; l_p^2 (40/3)/l^2 = {mp.nstr(mp.mpf(40)/3/ell**2,10)}")
# ======================================================================================
# 7. Israel weights as KINK - NO_SOURCE, two windows, two eps, 48-node mp-GL in u = tanh(rho/eps)
# ======================================================================================
P("\n== 7. int G^a_a dy_proper over rho in [-W, W] (dy = sqrt(wF0) drho), reported /k, k = 1/sqrt(wF0); Israel: x -6, rhorho 0, internal -8 ==")
XG, WG = glmp(48)
for (a_, b_) in [(mp.mpf('0.37'), mp.mpf('1.11')), (mp.mpf('2.01'), mp.mpf('0.23'))]:
    k = 1/mp.sqrt(wF0(a_, b_))
    for e in [mp.mpf('1e-5'), mp.mpf('1e-7')]:
        for nW in [4, 10]:
            W = nW*e; UU = mp.tanh(W/e); res = {}
            for case in ["KINK", "NO_SOURCE"]:
                argl = []; wts = []
                for xg, wg in zip(XG, WG):
                    uq = UU*xg; y = e*mp.atanh(uq); argl.append((case, e, y, a_, b_)); wts.append(e/(1-uq**2)*UU*wg)
                out = pmap(argl)
                res[case] = ([sum(o['Gd'][i]*o['sqrtgrr']*w for o, w in zip(out, wts))/k for i in range(11)], max(o['off'] for o in out))
            dK = [res['KINK'][0][i] - res['NO_SOURCE'][0][i] for i in range(11)]
            P(f"  (a,b)=({mp.nstr(a_,3)},{mp.nstr(b_,3)}) eps={mp.nstr(e,2)} window rho in [-{nW}eps,{nW}eps]:")
            P(f"     raw KINK diag/k      = {[mp.nstr(x,9) for x in res['KINK'][0]]}")
            P(f"     raw NO_SOURCE diag/k = {[mp.nstr(x,6) for x in res['NO_SOURCE'][0]]}")
            P(f"     KINK - NO_SOURCE     = {[mp.nstr(x,9) for x in dK]}")
            P(f"     residual vs Israel: x {mp.nstr(max(abs(dK[i]+6) for i in range(4)),3)}, rhorho {mp.nstr(abs(dK[4]),3)}, internal {mp.nstr(max(abs(dK[i]+8) for i in range(5,11)),3)}; max pointwise |offdiag G| (KINK) {mp.nstr(res['KINK'][1],3)}")
# ======================================================================================
# 6. N_req with the x-block warp sqrt|g_x| = (wF0)^2
# ======================================================================================
P("\n== 6. N_req/(2N) with and without the x-block warp (wF0)^2 (24x16 mp-GL as in bd47ff5e) ==")
gk_ = [(i,j) for i in range(11) for j in range(11) if GW[i,j] != 0]
gfun = lamb(PARAMS+[EPS,SG,DL,CC]+[rho,v,al,be], [GW[i,j] for i,j in gk_])
def met(par, a_, b_):
    vals = gfun(*(list(par)+[mp.mpf('1e-3'),1,0,0]+[mp.mpf(0), mp.mpf(1), a_, b_])); g_ = mp.zeros(11)
    for (i,j), x in zip(gk_, vals): g_[i,j] = x
    return g_
xa, wa = glmp(24); xb, wb = glmp(16)
S = {'h': [0, 0], 'f': [0, 0]}; W2l = []
for x_, u_ in zip(xa, wa):
    for y_, v_ in zip(xb, wb):
        a_ = (x_+1)*mp.pi/2; b_ = (y_+1)*mp.pi/4; w = u_*v_*mp.pi**2/8
        g_ = met(PAR, a_, b_); k = 1/mp.sqrt(wF0(a_, b_)); W2 = wF0(a_, b_)**2
        d6 = mp.det(mp.matrix([[g_[i,j] for j in range(5,11)] for i in range(5,11)]))
        for key, duv in [('h', (Dfun(a_, b_)**(mp.mpf(1)/3)*G0n)**2), ('f', g_[5,5]*g_[6,6])]:
            S[key][0] += w*k*mp.sqrt(d6)/mp.sqrt(duv); S[key][1] += w*k*mp.sqrt(d6)/mp.sqrt(duv)*W2
Wmin = (X1n**(mp.mpf(1)/3)*F0n)**2; Wmax = (X2n**(mp.mpf(1)/3)*F0n)**2
for key, lbl in [('h', 'horizontal Sigma'), ('f', 'fixed-phi')]:
    base = 6/mp.pi**2*4*mp.pi**2*S[key][0]; avg = S[key][1]/S[key][0]
    P(f"  {lbl}: N_req/(2N) no warp = {mp.nstr(base,12)}; weighted fibre average <(wF0)^2> = {mp.nstr(avg,12)}")
    P(f"     warp factor <(wF0)^2>/(wF0)^2|_M5 over M5 location in [{mp.nstr(avg/Wmax,6)}, {mp.nstr(avg/Wmin,6)}] -> N_req/(2N) in [{mp.nstr(base*avg/Wmax,6)}, {mp.nstr(base*avg/Wmin,6)}]")
# ======================================================================================
# 8. Bolza systole: independent computer-assisted check (regular octagon, angles pi/4, opposite sides paired)
# ======================================================================================
P("\n== 8. Bolza systole: enumerate all group elements g with d(o, g o) <= L + 2R, L = 3.6 (complete by tile-chain argument, BFS bound L + 3R) ==")
ca = 1/mp.tan(mp.pi/8); a_ap = mp.acosh(ca); Rc = mp.acosh(ca**2)
P(f"  apothem a: cosh a = cot(pi/8) = {mp.nstr(ca,20)} (1+sqrt2 = {mp.nstr(1+mp.sqrt(2),20)}); circumradius R: cosh R = cot^2(pi/8) -> R = {mp.nstr(Rc,12)}; area check 8-gon (6pi - 8*pi/4) = 4pi = 2pi*|chi|")
gens = []
for kk in range(8):
    th = kk*np.pi/4; c = float(mp.cosh(a_ap)); s = float(mp.sinh(a_ap))
    gens.append(np.array([[c, np.exp(1j*th)*s], [np.exp(-1j*th)*s, c]]))
Lt = 3.6; Dmax = Lt + 3*float(Rc) + 0.05
I2 = np.eye(2, dtype=complex)
seen = {}; frontier = [I2]
def key(g): return tuple(np.round([g[0,0].real, g[0,0].imag, g[0,1].real, g[0,1].imag], 6))
seen[key(I2)] = I2
while frontier:
    nf = []
    for g in frontier:
        for s in gens:
            h2 = g @ s
            cd = 2*abs(h2[0,0])**2 - 1
            if cd > np.cosh(Dmax): continue
            kk_ = key(h2)
            if kk_ in seen: continue
            seen[kk_] = h2; nf.append(h2)
    frontier = nf
els = list(seen.values())
cand = [g for g in els if 2*abs(g[0,0])**2 - 1 <= np.cosh(Lt + 2*float(Rc))]
trs = sorted(set(round(abs(2*g[0,0].real), 9) for g in cand if abs(2*g[0,0].real) > 2 + 1e-9))
lens = [2*np.arccosh(t/2) for t in trs[:6]]
P(f"  BFS elements within Dmax={Dmax:.4f}: {len(els)}; candidates within L+2R: {len(cand)}; elliptic/parabolic non-identity: {sum(1 for g in cand if abs(2*g[0,0].real) <= 2+1e-9) - 1}")
P(f"  smallest |tr| > 2: {trs[:6]}  -> translation lengths {[round(x,10) for x in lens]}")
P(f"  2+2sqrt2 = {mp.nstr(2+2*mp.sqrt(2),15)}; 2 arccosh(1+sqrt2) = {mp.nstr(2*mp.acosh(1+mp.sqrt(2)),20)}; number of elements at min |tr|: {sum(1 for g in cand if abs(abs(2*g[0,0].real) - trs[0]) < 1e-7)}")
P(f"\nDONE {time.time()-T00:.0f}s")
