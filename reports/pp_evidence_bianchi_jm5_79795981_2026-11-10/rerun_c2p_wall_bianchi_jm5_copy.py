# FROZEN before run (MR2, 2026-11-10). B1-c2' / 1a wall: pointwise fibre component of the wall Bianchi identity and the sign of J_M5
# for the lifted E8 candidates E-0, E-T, E-Lambda+/-, E-S+/- (none adopted). Routines exec'd VERBATIM from the frozen V2 .py
# (sha ad134752..., same as bd47ff5e) before its MAIN marker; MN2 metric = cand_metric() (11D), Y6 = its (u,v,alpha,beta,phi1,phi2) block,
# fibre = its (alpha,beta,phi1,phi2) block. Charge units: Q = (1/16pi^2)(tr F^2 - 1/2 tr R^2) (tr = Tr_248/30 = tr_16), p1 = -(1/8pi^2) tr R^R.
import hashlib, time
V2 = '/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
raw = open(V2,'rb').read(); h = hashlib.sha256(raw).hexdigest()
assert h == 'ad134752da79e3064e209cd840b0aec53e004e3fa0fec8bbc9299eb12940eb85', h
exec(raw.decode().split('# ======================= MAIN =======================')[0])
import numpy as np
mp.mp.dps = 40
def P(s): print(s, flush=True)
P(f"V2 routines sha256 verified: {h}")
def fpar(fp):
    X1 = fp['X1']; X2 = fp['X2']; X0 = (X1*X2)**-2
    ef = 1/X0; e2g = X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2)
    return [mp.mpf(sp.N(x_, 45)) for x_ in (X1, X2, ef**2, e2g, fp['a1'], fp['a2'])]
PAR = fpar(FP["MN2(z=1)"]); X1n, X2n, F0n, G0n, a1n, a2n = PAR; X0n = 1/(X1n*X2n)**2
P(f"MN2: X1={mp.nstr(X1n,15)} X2={mp.nstr(X2n,15)} X0={mp.nstr(X0n,15)} F0={mp.nstr(F0n,15)} G0={mp.nstr(G0n,15)} a1={a1n} a2={a2n}")
# exact U on S^4 at MN2 (X0 = X2 = p, X1 = p/2, s = mu1^2): U = -p^2 (4 - s)
pp_, s_ = sp.symbols('p s', positive=True)
Dsym = pp_*(1-s_) + pp_/2*s_
Usym = 4*(pp_**2*(1-s_) + (pp_/2)**2*s_ - Dsym*(pp_+pp_/2+pp_)) + 2*Dsym*pp_
P(f"[U] exact: X0 = X2: {sp.simplify(1/(FP['MN2(z=1)']['X1']*FP['MN2(z=1)']['X2'])**2 - FP['MN2(z=1)']['X2']) == 0}, X1 = X2/2: {sp.simplify(FP['MN2(z=1)']['X1'] - FP['MN2(z=1)']['X2']/2) == 0};  U = {sp.factor(sp.expand(Usym))}  (s = mu1^2 in [0,1] => U in [-4p^2, -3p^2] < 0)")
GC = cand_metric()
G6 = GC[5:11, 5:11]; c6 = [u, v, al, be, p1, p2]
G4f = GC[7:11, 7:11]; c4 = [al, be, p1, p2]
P(f"[F] fibre block has no u,v mixing: {all(GC[i,j] == 0 for i in range(7,11) for j in (5,6) if i != 9) } ; g_(phi1,u) present (Dphi1): {GC[9,5] != 0}")
N6 = NumGeom(G6, c6, [v, al, be], PARAMS)
N4 = NumGeom(G4f, c4, [al, be], PARAMS)
PI2 = mp.pi**2
def trRR(Riem, n, idx):
    i0, i1, i2, i3 = idx
    def T(c, d, e, f):
        s = 0
        for a in range(n):
            for b in range(n):
                x = Riem.get((a, b, c, d)); y = Riem.get((b, a, e, f))
                if x is not None and y is not None: s += x*y
        return s
    return 2*(T(i0,i1,i2,i3) - T(i0,i2,i1,i3) + T(i0,i3,i1,i2))
pairs4 = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
comb = [((0,1),(2,3),1),((0,2),(1,3),-1),((0,3),(1,2),1),((1,2),(0,3),1),((1,3),(0,2),-1),((2,3),(0,1),1)]
def fibre4(g, Riem):
    L = mp.cholesky(g)            # g = L L^T ; orthonormal coframe theta = L^T dx
    LT = L.T; LTi = LT**-1
    Rh = {}
    for (i, j) in pairs4:
        M = mp.matrix(4, 4)
        for a in range(4):
            for b in range(4): M[a, b] = Riem.get((a, b, i, j), 0)
        Rh[(i, j)] = LT*M*LTi       # endomorphism in ON frame (antisymmetric)
    asym = max(abs(Rh[k][a, b] + Rh[k][b, a]) for k in Rh for a in range(4) for b in range(4))
    # Euler density component (alpha,beta,phi1,phi2)
    eu = 0
    for a, b, c, d in itertools.permutations(range(4)):
        sgn = perm_sign((a, b, c, d))
        for (A, B, s) in comb: eu += sgn*s*Rh[A][a, b]*Rh[B][c, d]
    eu = eu/(32*PI2)
    # Lambda^2 +/- : induced action and Hodge star in ON basis (orientation = coordinate orientation, det L > 0)
    star = {(0,1): ((2,3), 1), (0,2): ((1,3), -1), (0,3): ((1,2), 1), (1,2): ((0,3), 1), (1,3): ((0,2), -1), (2,3): ((0,1), 1)}
    S = mp.matrix(6, 6)
    for k, pk in enumerate(pairs4):
        q, s = star[pk]; S[pairs4.index(q), k] = s
    def ad(M):
        out = mp.matrix(6, 6)
        for k, (a, b) in enumerate(pairs4):
            # M(e_a ^ e_b) = (M e_a) ^ e_b + e_a ^ (M e_b)
            for c in range(4):
                for (x, y, w) in ((c, b, M[c, a]), (a, c, M[c, b])):
                    if x == y or w == 0: continue
                    if x < y: out[pairs4.index((x, y)), k] += w
                    else: out[pairs4.index((y, x)), k] -= w
        return out
    adR = {k: ad(Rh[k]) for k in Rh}
    res = {}
    for sg in (1, -1):
        Pm = (mp.eye(6) + sg*S)/2
        t = lambda A, B: sum((Pm*adR[A]*adR[B])[i, i] for i in range(6))
        res[sg] = -(2*(t((0,1),(2,3)) - t((0,2),(1,3)) + t((0,3),(1,2))))/(8*PI2)
    p1f = -trRR(Riem, 4, (0,1,2,3))/(8*PI2)
    return p1f, eu, res[1], res[-1], asym, float(max(abs(x) for x in (S*S + mp.eye(6))))
def Dn(a_, b_): return X0n*mp.cos(a_)**2 + X1n*(mp.sin(a_)*mp.cos(b_))**2 + X2n*(mp.sin(a_)*mp.sin(b_))**2
def Un(a_, b_):
    m = [mp.cos(a_), mp.sin(a_)*mp.cos(b_), mp.sin(a_)*mp.sin(b_)]; Xa = [X0n, X1n, X2n]; D_ = Dn(a_, b_)
    return 4*sum(Xa[k]**2*m[k]**2 - D_*Xa[k] for k in range(3)) + 2*D_*X0n
def point(a_, b_, vv=mp.mpf(1)):
    g6, gi6, R6 = N6.at(PAR, [vv, a_, b_])
    g4, gi4, R4 = N4.at(PAR, [a_, b_])
    sq = mp.sqrt(mp.det(g4))
    p16 = -trRR(R6, 6, (2,3,4,5))/(8*PI2)
    p1f, eu, pLp, pLm, asym, starchk = fibre4(g4, R4)
    wJ = abs(Un(a_, b_))*Dn(a_, b_)**(-mp.mpf(7)/6)*sq        # |G4_(alpha beta phi1 phi2)| (uplift units, kappa = 1), see [J]
    return dict(sq=sq, p16=p16, p1f=p1f, eu=eu, pLp=pLp, pLm=pLm, asym=asym, starchk=starchk, wJ=wJ, U=Un(a_, b_))
t0 = time.time()
# [J] check of the fibre-component formula against the V2 Hodge dual (bd47ff5e route) at two points
Om_s, U_s = Omega_sym(); Om_keys = list(Om_s.keys())
Om_f = lamb(PARAMS+[LAM, KAP]+dep, [Om_s[kk_] for kk_ in Om_keys])
gkc = [(i,j) for i in range(11) for j in range(11) if GC[i,j] != 0]
gcf = lamb(PARAMS+dep, [GC[i,j] for i,j in gkc])
for (a_, b_) in [(mp.mpf('0.37'), mp.mpf('1.11')), (mp.mpf('2.01'), mp.mpf('0.23'))]:
    vals = gcf(*(PAR+[mp.mpf(1), mp.mpf(1), a_, b_])); g_ = mp.zeros(11)
    for (i,j), x in zip(gkc, vals): g_[i,j] = x
    ov = Om_f(*(PAR+[mp.mpf(1)/16, 1]+[mp.mpf(1), mp.mpf(1), a_, b_])); Om = {kk_: x for kk_, x in zip(Om_keys, ov) if x != 0}
    G4 = hodge_num(Om, g_, g_**-1, 11, 7)
    pt_ = point(a_, b_)
    P(f"[J] (alpha,beta)=({a_},{b_}): V2 Hodge G4_(7,8,9,10) = {mp.nstr(G4.get((7,8,9,10),0),25)} ; formula U D^(-7/6) sqrt(det g_fib) = {mp.nstr(pt_['U']*Dn(a_,b_)**(-mp.mpf(7)/6)*pt_['sq'],25)}")
P(f"   elapsed {time.time()-t0:.0f}s")
# v-independence (Sigma homogeneity) of the Y6 fibre component
for vv in (mp.mpf(1), mp.mpf(3)):
    P(f"[V] v={vv}: p1(Y6) fibre comp at (0.37,1.11) = {mp.nstr(point(mp.mpf('0.37'), mp.mpf('1.11'), vv)['p16'], 25)}")
# Gauss-Legendre integrals over the fibre: alpha in [0,pi], beta in [0,pi/2], phi1, phi2 in [0,2pi)
def gl(nq):
    xg, wg = np.polynomial.legendre.leggauss(nq); return [mp.mpf(float(a)) for a in xg], [mp.mpf(float(b)) for b in wg]
QA = gl(24); QB = gl(16)
XA = [(x+1)*mp.pi/2 for x in QA[0]]; WA = [w*mp.pi/2 for w in QA[1]]
XB = [(x+1)*mp.pi/4 for x in QB[0]]; WB = [w*mp.pi/4 for w in QB[1]]
I = dict(wJ=0, p16=0, p1f=0, eu=0, pLp=0, pLm=0); pts = []
asym_max = 0; star_max = 0; idmax = 0
for a_, wa in zip(XA, WA):
    for b_, wb in zip(XB, WB):
        q = point(a_, b_); pts.append((a_, b_, q))
        for k in I: I[k] += 4*PI2*wa*wb*q[k]
        asym_max = max(asym_max, q['asym']); star_max = max(star_max, q['starchk'])
        idmax = max(idmax, abs(q['pLp'] - (q['p1f'] + 2*q['eu'])), abs(q['pLm'] - (q['p1f'] - 2*q['eu'])))
P(f"[I] GL 24x16 ({len(pts)} pts), elapsed {time.time()-t0:.0f}s")
P(f"   |int G4_fib| (kappa=1) = {mp.nstr(I['wJ'],20)}   pi^2 = {mp.nstr(PI2,20)}")
P(f"   int e(fibre) = {mp.nstr(I['eu'],20)}   int p1(fibre) = {mp.nstr(I['p1f'],12)}   int p1(Lambda2+) = {mp.nstr(I['pLp'],20)}   int p1(Lambda2-) = {mp.nstr(I['pLm'],20)}")
P(f"   int p1(TY6) fibre component = {mp.nstr(I['p16'],12)}")
P(f"   max antisymmetry defect of ON curvature = {mp.nstr(asym_max,5)} ; max |star^2+1| = {star_max} ; max |p1(L2+-) - (p1 +- 2e)| pointwise = {mp.nstr(idmax,5)}")
NU = 4880; ZJ = I['wJ']
# charge densities per unit fibre coordinate measure: rho_J = 2N * wJ/ZJ (int = 9760); Q-pieces from Chern-Weil forms
def ratios(q):
    rJ = 2*NU*q['wJ']/ZJ
    grav = q['p16']/4                 # -(1/2)(1/16pi^2) tr R^2 = +p1/4
    return dict(rJ=rJ,
        E0=grav/rJ,                                  # E-0: Q = +p1(Y6)/4
        ET=(-q['p16']/2 + grav)/rJ,                  # E-T: (1/16pi^2) tr_16 F^2 = -p1(Y6)/2 (F = R_Y6 via SO(6) < SO(16))
        Lp=(-q['pLp']/4)/rJ, Lm=(-q['pLm']/4)/rJ,    # per unit index j: Q_gauge = -(j/4) p1(Lambda2+-) (fibre component, Gauss formula)
        G=grav/rJ)
# edge points (high dps) added to the scan
mp.mp.dps = 60
edges = []
for e_ in (mp.mpf('1e-3'), mp.mpf('1e-5')):
    for b_ in (e_, mp.pi/4, mp.pi/2 - e_):
        for a_ in (e_, mp.pi/2, mp.pi - e_, mp.mpf('0.7')):
            edges.append((a_, b_, point(a_, b_)))
mp.mp.dps = 40
allp = pts + edges
R = [(a_, b_, ratios(q)) for a_, b_, q in allp]
P(f"[R] ratio scan over {len(R)} points (GL grid + {len(edges)} edge points at dps 60), elapsed {time.time()-t0:.0f}s")
for key in ('E0', 'ET', 'Lp', 'Lm'):
    mx = max(R, key=lambda z: z[2][key]); mn = min(R, key=lambda z: z[2][key])
    P(f"   {key}: max Q/rho_J = {mp.nstr(mx[2][key],15)} at ({mp.nstr(mx[0],6)},{mp.nstr(mx[1],6)}) ; min = {mp.nstr(mn[2][key],15)} at ({mp.nstr(mn[0],6)},{mp.nstr(mn[1],6)})")
vol_dens = [(rz[2]['rJ']/q['sq'], a_, b_) for rz, (a_, b_, q) in zip(R, allp)]
vm = min(vol_dens, key=lambda z: z[0]); vM = max(vol_dens, key=lambda z: z[0])
P(f"   rho_J per unit fibre volume (rho_J/sqrt det g_fib): min {mp.nstr(vm[0],15)} at ({mp.nstr(vm[1],6)},{mp.nstr(vm[2],6)}), max {mp.nstr(vM[0],15)}")
# J_M5 fibre component / rho_J = 1 - sigma*(G + j*L) ; thresholds j* = min over points with sigma*L > 0 of (1 - sigma*G)/(sigma*L)
for key in ('Lp', 'Lm'):
    for sg in (1, -1):
        cand = [((1 - sg*z[2]['G'])/(sg*z[2][key]), z) for z in R if sg*z[2][key] > 0]
        if cand:
            js, z = min(cand, key=lambda c: c[0])
            P(f"   E-{'Lambda+' if key=='Lp' else 'Lambda-'} sigma={sg:+d}: J_M5 >= 0 at all scanned points iff j <= j* = {mp.nstr(js,15)} (binding point ({mp.nstr(z[0],6)},{mp.nstr(z[1],6)}))")
        else:
            P(f"   E-{'Lambda+' if key=='Lp' else 'Lambda-'} sigma={sg:+d}: sigma*L <= 0 at all scanned points (no upper bound on j from the scan)")
for key in ('E0', 'ET'):
    for sg in (1, -1):
        P(f"   {key} sigma={sg:+d}: min over scan of J_M5/rho_J = {mp.nstr(min(1 - sg*z[2][key] for z in R), 15)}")
for key in ('Lp', 'Lm'):
    for sg in (1, -1):
        P(f"   E-S{'+' if key=='Lp' else '-'} (j=1) sigma={sg:+d}: min over scan of J_M5/rho_J = {mp.nstr(min(1 - sg*(z[2]['G'] + z[2][key]) for z in R), 15)}")
P(f"done {time.time()-t0:.0f}s")
