#!/usr/bin/env python3
# MR2 adoption blockers (2026-11-09): (1) full Riemann invariants, (2) systole numbers, (3) full 11D EOM incl. G4 prefactor.
# Conventions = MR2 V2 (sha d6e9b1f1...): uplift units R_AdS7 = 1, S4 radius 1/2; physical metric = l^2 x this, l = 2 (pi N)^(1/3) l_p.
# 11D sugra: R_MN = (1/12)(G_MPQR G_N^PQR - (1/12) g_MN G^2),  d*G + (1/2) G^G = 0,  dG = 0.
# Candidate metric: 1112.5487 (8)-(9) / 1203.0303 (3.8),(4.1)-(4.4). Flux ansatz: CLP hep-th/9903214 (4.2) / 1203.0303 (4.5) with the
# last-term coefficient LAMBDA left FREE and solved from d*G4 = 0.
import sympy as sp, mpmath as mp, itertools, time, math
T0 = time.time()
N = 4880; gg = 2
ell = 2*(mp.pi*N)**(mp.mpf(1)/3)
# ---------- fixed points (same formulas as V2) ----------
zs = sp.symbols('z')
X1_5 = (1+7*zs+7*zs**2+33*zs**3-(1+4*zs+19*zs**2)*sp.sqrt(1+3*zs**2))/(4*zs*(1-zs)**2)
ratio = (1+zs)/(2*zs+sp.sqrt(1+3*zs**2))
def fixed_point(zv):
    zv = sp.Integer(zv)
    x15 = sp.limit(X1_5, zs, zv) if zv in (0, 1) else X1_5.subs(zs, zv)
    X1 = sp.nsimplify(x15)**sp.Rational(1,5) if zv in (0,1) else x15**sp.Rational(1,5)
    X2 = X1/ratio.subs(zs, zv)
    return dict(z=zv, X1=X1, X2=X2, a1=(1+zv)/sp.Integer(2), a2=(1-zv)/sp.Integer(2))
CANDS = {"MN1(z=0)":0, "MN2(z=1)":1, "BBBW(z=2)":2, "BBBW(z=3)":3}
FP = {k: fixed_point(v) for k, v in CANDS.items()}
# ---------- generic geometry ----------
def geometry(G, coords, dep):
    n = len(coords)
    Gi = G.inv(method='LU').applyfunc(sp.simplify)
    dg = {}
    for a in range(n):
        for b in range(n):
            if G[a,b] != 0:
                for c in range(n):
                    if coords[c] in dep: dg[(a,b,c)] = sp.diff(G[a,b], coords[c])
    dG = lambda a,b,c: dg.get((a,b,c), 0)
    Gam = {}
    for a in range(n):
        for b in range(n):
            for c in range(b, n):
                s = sum(Gi[a,d]*(dG(d,b,c)+dG(d,c,b)-dG(b,c,d)) for d in range(n) if Gi[a,d] != 0)
                s = sp.together(s/2)
                if s != 0: Gam[(a,b,c)] = s
    dGam = {}
    for (a,b,c), e in Gam.items():
        for d in range(n):
            if coords[d] in dep:
                de = sp.diff(e, coords[d])
                if de != 0: dGam[(a,b,c,d)] = de
    return Gi, Gam, dGam
def lamb(args, exprs):
    return sp.lambdify(args, exprs, 'mpmath')
class NumGeom:
    def __init__(self, G, coords, dep, params):
        t1 = time.time()
        Gi, Gam, dGam = geometry(G, coords, dep)
        self.n = len(coords); self.coords = coords
        self.gk = [(i,j) for i in range(self.n) for j in range(self.n) if G[i,j] != 0]
        self.gik = [(i,j) for i in range(self.n) for j in range(self.n) if Gi[i,j] != 0]
        self.Gk = list(Gam.keys()); self.dGk = list(dGam.keys())
        args = list(params) + list(dep)
        self.f = lamb(args, [G[i,j] for i,j in self.gk] + [Gi[i,j] for i,j in self.gik] + [Gam[k] for k in self.Gk] + [dGam[k] for k in self.dGk])
        self.dep = dep
        print(f"   geometry built: {len(self.Gk)} Christoffels, {len(self.dGk)} derivatives [{time.time()-t1:.0f}s]", flush=True)
    def at(self, par, pt):
        v = self.f(*(list(par)+list(pt))); n = self.n
        g = mp.zeros(n); gi = mp.zeros(n); i0 = 0
        for (i,j) in self.gk: g[i,j] = v[i0]; i0 += 1
        for (i,j) in self.gik: gi[i,j] = v[i0]; i0 += 1
        Gam = {}
        for k in self.Gk:
            a,b,c = k; Gam[(a,b,c)] = v[i0]; Gam[(a,c,b)] = v[i0]; i0 += 1
        dGam = {}
        for k in self.dGk:
            a,b,c,d = k; dGam[(a,b,c,d)] = v[i0]; dGam[(a,c,b,d)] = v[i0]; i0 += 1
        # Riemann R^a_{bcd} = d_c Gam^a_{db} - d_d Gam^a_{cb} + Gam^a_{ce} Gam^e_{db} - Gam^a_{de} Gam^e_{cb}
        G1 = {}
        for (a,b,c), val in Gam.items(): G1.setdefault((a,b), {})[c] = val
        Riem = {}
        idx = range(n)
        for a in idx:
            for b in idx:
                for c in idx:
                    for d in range(c+1, n):
                        s = dGam.get((a,d,b,c), 0) - dGam.get((a,c,b,d), 0)
                        Ace = G1.get((a,c), {}); Ade = G1.get((a,d), {})
                        for e, x in Ace.items():
                            y = Gam.get((e,d,b));  s += x*y if y is not None else 0
                        for e, x in Ade.items():
                            y = Gam.get((e,c,b));  s -= x*y if y is not None else 0
                        if s != 0: Riem[(a,b,c,d)] = s
        return g, gi, Riem
def invariants(g, gi, Riem, n):
    # R^{ab}_{cd} = g^{be} R^a_{ecd}
    up = {}
    for (a,e,c,d), val in Riem.items():
        for b in range(n):
            if gi[b,e] != 0:
                up[(a,b,c,d)] = up.get((a,b,c,d), 0) + gi[b,e]*val
    K = 0
    for (a,b,c,d), val in up.items():   # c<d stored; full sum = 4 * sum over c<d, a<b ... use: sum_{all} = 2*sum_{c<d}
        w = up.get((c,d,a,b));
        if w is None:
            w2 = up.get((c,d,b,a)) if False else None
        # need R^{cd}_{ab} with a,b free order: get with a<b else minus
        if a < b: w = up.get((c,d,a,b), 0)
        elif a > b: w = -up.get((c,d,b,a), 0)
        else: w = 0
        K += val*w
    K = 2*K
    # Ricci R_bd = R^a_{bad}
    Ric = mp.zeros(n)
    for (a,b,c,d), val in Riem.items():
        if c == a: Ric[b,d] += val
        if d == a: Ric[b,c] -= val
    Rmix = gi*Ric
    R = sum(Rmix[i,i] for i in range(n))
    RR = sum(Rmix[i,j]*Rmix[j,i] for i in range(n) for j in range(n))
    D = n
    W2 = K - 4*RR/(D-2) + 2*R**2/((D-1)*(D-2))
    # curvature operator on Lambda^2: M[(a,b),(c,d)] = R^{ab}_{cd} (a<b, c<d); eigenvalues are frame-independent
    import numpy as np
    pairs = list(itertools.combinations(range(n), 2)); pid = {p_: i for i, p_ in enumerate(pairs)}
    Mq = np.zeros((len(pairs), len(pairs)))
    for (a,b,c,d), val in up.items():
        if a < b: Mq[pid[(a,b)], pid[(c,d)]] += float(val)
    ev = np.linalg.eigvals(Mq)
    return K, RR, W2, R, Ric, float(np.max(np.abs(ev))), float(np.max(np.abs(ev.imag)))
# ---------- forms ----------
def perm_sign(seq):
    seq = list(seq); s = 1
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]: s = -s
            elif seq[i] == seq[j]: return 0
    return s
def hodge_num(Om, g, gi, n, p):
    """Om: dict sorted p-tuple -> mp value (lower). returns dict sorted (n-p)-tuple -> value of *Om
       (*Om)_{A} = (1/p!) sqrt|g| Om^{B} eps_{B A}"""
    detg = mp.det(g); sq = mp.sqrt(abs(detg))
    Cs = [c for c in Om if Om[c] != 0]
    out = {}
    for B in itertools.combinations(range(n), p):
        up = 0
        for C in Cs:
            M = mp.matrix([[gi[b,c] for c in C] for b in B])
            dm = mp.det(M)
            if dm != 0: up += dm*Om[C]
        if up != 0:
            A = tuple(x for x in range(n) if x not in B)
            out[A] = out.get(A, 0) + perm_sign(B+A)*sq*up
    return out
def full_low(F, n, p):
    T = {}
    for A, val in F.items():
        for P in itertools.permutations(A):
            T[P] = perm_sign(P)*val
    return T
def einstein_residual(G4, g, gi, Ric, n):
    # raise all indices of G4 (sorted comps)
    Gup = {}
    Cs = list(G4.keys())
    for B in itertools.combinations(range(n), 4):
        s = 0
        for C in Cs:
            dm = mp.det(mp.matrix([[gi[b,c] for c in C] for b in B]))
            if dm != 0: s += dm*G4[C]
        if s != 0: Gup[B] = s
    G2 = 24*sum(G4[A]*Gup.get(A, 0) for A in G4)
    # GG_MN = 6 sum_{T sorted triple} G_{M T} G_N^{T}, with G_N^{T} = g_{NS} G^{S T}
    def comp(F, M, T):  # F_{M T} with T sorted triple
        if M in T: return 0
        key = tuple(sorted((M,)+T)); val = F.get(key, 0)
        return perm_sign((M,)+T)*val if val != 0 else 0
    triples = list(itertools.combinations(range(n), 3))
    lowM = [[comp(G4, M, T) for T in triples] for M in range(n)]
    upS = [[comp(Gup, S, T) for T in triples] for S in range(n)]
    E = mp.zeros(n)
    for M in range(n):
        for Nn in range(n):
            s = 0
            for ti in range(len(triples)):
                x = lowM[M][ti]
                if x == 0: continue
                y = sum(g[Nn,S]*upS[S][ti] for S in range(n) if g[Nn,S] != 0 and upS[S][ti] != 0)
                s += x*y
            GG = 6*s
            E[M,Nn] = Ric[M,Nn] - (GG - g[M,Nn]*G2/12)/12
    Emix = gi*E
    scale = max(abs(x) for x in (gi*Ric))
    return max(abs(x) for x in Emix), scale, G2
def ext_d_num(Ffun, pt, depidx, n, p, h):
    """numerical exterior derivative of a p-form given as function(pt)->dict(sorted tuple->val); returns max |dF| comp"""
    base = Ffun(pt)
    der = {}
    for k, ci in enumerate(depidx):
        pp = list(pt); pm = list(pt); pp[k] += h; pm[k] -= h
        Fp = Ffun(pp); Fm = Ffun(pm)
        keys = set(Fp) | set(Fm)
        der[ci] = {A: (Fp.get(A,0)-Fm.get(A,0))/(2*h) for A in keys}
    dF = {}
    for ci, D in der.items():
        for A, val in D.items():
            if ci in A or val == 0: continue
            B = tuple(sorted((ci,)+A))
            dF[B] = dF.get(B, 0) + perm_sign((ci,)+A)*val
    return max([abs(x) for x in dF.values()] + [mp.mpf(0)]), max(abs(x) for x in base.values())
print("== MR2 adoption blockers: Riemann / systole / full EOM ==", flush=True)
# ---------- candidate metric (symbolic params) ----------
t,x1,x2,x3,r,u,v,al,be,p1,p2 = sp.symbols('t x1 x2 x3 r u v alpha beta phi1 phi2', real=True)
coords = [t,x1,x2,x3,r,u,v,al,be,p1,p2]; dep = [r,v,al,be]; DEPIDX = [4,6,7,8]
X1s, X2s, F0s, G0s, a1s, a2s = sp.symbols('X1 X2 F0 G0 a1 a2', positive=True)
PARAMS = [X1s, X2s, F0s, G0s, a1s, a2s]
m0, m1, m2 = sp.cos(al), sp.sin(al)*sp.cos(be), sp.sin(al)*sp.sin(be)
def cand_metric():
    X1, X2 = X1s, X2s; X0 = 1/(X1*X2)**2
    D = X0*m0**2+X1*m1**2+X2*m2**2
    G = sp.zeros(11); w7 = D**sp.Rational(1,3)
    for i, s_ in enumerate([-1,1,1,1,1]): G[i,i] = w7*F0s*s_/r**2
    G[5,5] = w7*G0s/v**2; G[6,6] = w7*G0s/v**2
    c = D**sp.Rational(-2,3)/4
    dm = [[sp.diff(m, al), sp.diff(m, be)] for m in (m0, m1, m2)]; Xs = [X0, X1, X2]
    for i in range(2):
        for j in range(2):
            G[7+i,7+j] += c*sum(dm[k][i]*dm[k][j]/Xs[k] for k in range(3))
    for k,(ph,ai,mu) in enumerate([(9,a1s,m1),(10,a2s,m2)]):
        fac = c*mu**2/Xs[k+1]
        G[ph,ph] += fac; G[ph,5] += fac*ai/v; G[5,ph] += fac*ai/v; G[5,5] += fac*ai**2/v**2
    return G.applyfunc(sp.simplify)
# ---------- 7-form Omega = *G4 (symbolic exterior algebra) ----------
LAM, KAP = sp.symbols('LAMBDA kappa_flux')
def wedge(A, B):
    out = {}
    for ka, va in A.items():
        for kb, vb in B.items():
            if set(ka) & set(kb): continue
            key = ka+kb; s = perm_sign(key); sk = tuple(sorted(key))
            out[sk] = out.get(sk, 0) + s*va*vb
    return {k: v_ for k, v_ in out.items() if v_ != 0}
def dform(A):
    out = {}
    for ka, va in A.items():
        for ci, c_ in enumerate(coords):
            dv = sp.diff(va, c_)
            if dv == 0 or ci in ka: continue
            key = (ci,)+ka; s = perm_sign(key); sk = tuple(sorted(key))
            out[sk] = out.get(sk, 0) + s*dv
    return {k: sp.simplify(v_) for k, v_ in out.items() if sp.simplify(v_) != 0}
def one(i, f=1): return {(i,): f}
def Omega_sym():
    X1, X2 = X1s, X2s; X0 = 1/(X1*X2)**2
    Xa = [X0, X1, X2]; mus = [m0, m1, m2]
    D = sum(Xa[k]*mus[k]**2 for k in range(3))
    U = 4*sum(Xa[k]**2*mus[k]**2 - D*Xa[k] for k in range(3)) + 2*D*X0
    ef, eg = sp.sqrt(F0s), sp.sqrt(G0s)
    vol5 = {(0,1,2,3,4): ef**5/r**5}            # unit-AdS5 volume x e^{5 f0}
    volS = {(5,6): G0s/v**2}                      # e^{2 g0} du^dv / v^2
    eps7 = wedge(vol5, volS)
    Om = {k: KAP*U*val for k, val in eps7.items()}
    # *_7 Fhat^i, Fhat^i = a_i du^dv/v^2  ->  (a_i / e^{2g0}) * vol5   (orientation eps7 = vol5^volS)
    for (ph, ai, mu, X) in [(9, a1s, m1, X1), (10, a2s, m2, X2)]:
        dmu2 = {(7,): sp.diff(mu**2, al), (8,): sp.diff(mu**2, be)}
        oneform = {(ph,): 1, (5,): ai/v}
        star7F = {k: ai/G0s*val for k, val in vol5.items()}
        term = wedge(wedge(dmu2, oneform), star7F)
        for k, val in term.items(): Om[k] = Om.get(k, 0) + KAP*LAM*X**-2*val
    return {k: sp.simplify(val) for k, val in Om.items() if sp.simplify(val) != 0}, U
# ======================= MAIN =======================
mp.mp.dps = 40
def P(s): print(s, flush=True)
P(f"l/l_p = {mp.nstr(ell,10)}, l^2 = {mp.nstr(ell**2,10)} l_p^2")
# ---- validation geometry A: AdS7 x S4 (R_AdS7 = 1, S4 radius 1/2) ----
P("\n== V. validation ==")
ty = sp.symbols('y1:6', real=True); th = sp.symbols('th1:5', real=True)
cA = [t]+list(ty)+[r]+list(th)
GA = sp.zeros(11)
GA[0,0] = -1/r**2
for i in range(1,7): GA[i,i] = 1/r**2
s4 = [1, sp.sin(th[0])**2, (sp.sin(th[0])*sp.sin(th[1]))**2, (sp.sin(th[0])*sp.sin(th[1])*sp.sin(th[2]))**2]
for i in range(4): GA[7+i,7+i] = s4[i]/4
NA = NumGeom(GA, cA, [r, th[0], th[1], th[2]], [])
ptsA = [(mp.mpf('1.3'), mp.mpf('0.4'), mp.mpf('1.1'), mp.mpf('2.0')), (mp.mpf('0.7'), mp.mpf('1e-6'), mp.mpf('1.5'), mp.mpf('3.1415'))]
for pt in ptsA:
    g_, gi_, Rm = NA.at([], pt); K, RR, W2, R, Ric, Qmax, Qim = invariants(g_, gi_, Rm, 11)
    # flux G4 = 6 vol(S4 radius 1/2)  (Freund-Rubin; *G = -6 eps7)
    vol = mp.sqrt(abs(mp.det(mp.matrix([[g_[i,j] for j in range(7,11)] for i in range(7,11)]))))
    for kap, lbl in [(1, "true flux"), (mp.mpf('1.1'), "WRONG flux x1.1")]:
        G4 = {(7,8,9,10): kap*6*vol}
        res, sc, G2 = einstein_residual(G4, g_, gi_, Ric, 11)
        P(f"AdS7xS4 pt={[mp.nstr(x,4) for x in pt]} {lbl}: max|E^M_N|={mp.nstr(res,3)} (scale {mp.nstr(sc,4)})")
    P(f"   curvature-operator max|eig| = {Qmax:.12f} (exact 4 from S4; AdS7 -1), max|Im eig| = {Qim:.1e}")
    P(f"   K={mp.nstr(K,20)} (exact 2*7*6 + 2*4*3*16 = 468), RicSq={mp.nstr(RR,15)} (exact 7*36+4*144=828), R={mp.nstr(R,15)} (exact -42+48=6), Weyl^2={mp.nstr(W2,15)}")
# ---- candidates geometry ----
P("\n== building candidate geometry (symbolic Christoffels + derivatives) ==")
GC = cand_metric()
NC = NumGeom(GC, coords, dep, PARAMS)
Om_s, U_s = Omega_sym()
dOm_s = dform(Om_s)
Om_keys = list(Om_s.keys())
Om_f = lamb(PARAMS+[LAM, KAP]+dep, [Om_s[k] for k in Om_keys])
gk = [(i,j) for i in range(11) for j in range(11) if GC[i,j] != 0]
g_f = lamb(PARAMS+dep, [GC[i,j] for i,j in gk])
def metric_at(par, pt):
    vals = g_f(*(list(par)+list(pt))); g_ = mp.zeros(11)
    for (i,j), x in zip(gk, vals): g_[i,j] = x
    return g_
def G4_at(par, lam, kap, pt):
    g_ = metric_at(par, pt); gi_ = g_**-1
    ov = Om_f(*(list(par)+[lam, kap]+list(pt)))
    Om = {k: x for k, x in zip(Om_keys, ov) if x != 0}
    return hodge_num(Om, g_, gi_, 11, 7)
# product validation inside the candidate ansatz: X=1, a=0, F0=2/3, G0=1/6  (KR (D) metric)
parD = [mp.mpf(1), mp.mpf(1), mp.mpf(2)/3, mp.mpf(1)/6, mp.mpf(0), mp.mpf(0)]
for pt in [(1, 1, mp.mpf('0.7'), mp.mpf('0.4')), (1, 1, mp.mpf('1e-6'), mp.mpf('1e-6'))]:
    g_, gi_, Rm = NC.at(parD, [mp.mpf(x) for x in pt]); K, RR, W2, R, Ric, Qmax, Qim = invariants(g_, gi_, Rm, 11)
    P(f"(D) product AdS5(F0=2/3)xH2(G0=1/6)xS4(1/2) pt={[mp.nstr(mp.mpf(x),3) for x in pt]}: K={mp.nstr(K,20)} (exact 40*9/4+4*36+384 = 618), RicSq={mp.nstr(RR,15)} (exact 828), R={mp.nstr(R,15)} (exact 6), max|eig Q|={Qmax:.12f} (exact 6)")
# ---- grid ----
eps_ = mp.mpf('1e-6')
dl = mp.mpf('1.234e-3')  # PP fc5e0156: avoid exact pi/2 multiples (0/0 rounding in simplified expressions)
ALS = [eps_, mp.pi/4+dl, mp.pi/2+dl, 3*mp.pi/4+dl, mp.pi-eps_]; BES = [eps_, mp.pi/4+dl, mp.pi/2-eps_]
GRID = [(a_, b_) for a_ in ALS for b_ in BES] + [(mp.mpf('0.37'), mp.mpf('1.11')), (mp.mpf('2.01'), mp.mpf('0.23'))]
P(f"grid: {len(GRID)} points (alpha in {{1e-6, pi/4+d, pi/2+d, 3pi/4+d, pi-1e-6}} x beta in {{1e-6, pi/4+d, pi/2-1e-6}}, d=1.234e-3 + 2 generic); dps={mp.mp.dps}")
def fpar(fp, x1fac=1):
    X1 = fp['X1']*x1fac; X2 = fp['X2']; X0 = (X1*X2)**-2
    ef = 1/X0; e2g = X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2)
    # NOTE control: e2g/ef recomputed from the perturbed X1 (same formulas), so the control is 'wrong X1, consistent formulas'
    return [mp.mpf(sp.N(x_, 45)) for x_ in (X1, X2, ef**2, e2g, fp['a1'], fp['a2'])]
RES = {}
cases = [(k, fp, 1, 1, mp.mpf(1)/16) for k, fp in FP.items()]
cases += [("CONTROL X1*1.1 (z=2)", FP["BBBW(z=2)"], sp.Rational(11,10), 1, mp.mpf(1)/16),
          ("CONTROL wrong flux x1.1 (z=2)", FP["BBBW(z=2)"], 1, mp.mpf('1.1'), mp.mpf(1)/16),
          ("CONTROL LAMBDA=14/4 'garbled 14' reading (z=2)", FP["BBBW(z=2)"], 1, 1, mp.mpf(14)/4/4),
          ("CONTROL LAMBDA=0 (no gauge-field term) (z=2)", FP["BBBW(z=2)"], 1, 1, mp.mpf(0))]
P("\n== closure d*G4 = 0 (G^G = 0 identically: G4 has legs only on the 6 internal directions), exact symbolic with LAMBDA free ==")
for k, fp in FP.items():
    X1 = fp['X1']; X2 = fp['X2']; X0 = (X1*X2)**-2
    sub = {X1s: X1, X2s: X2, F0s: X0**-2, G0s: X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2), a1s: fp['a1'], a2s: fp['a2'], KAP: 1}
    lam_vals = []
    for key, val in dOm_s.items():
        for A_, B_ in [(sp.Rational(3,10), sp.Rational(1,5)), (sp.Rational(11,10), sp.Rational(7,10)), (2, sp.Rational(13,10))]:
            e = val.subs(sub).subs({al: A_, be: B_, r: 1, v: 1})
            A0 = sp.N(e.subs(LAM, 0), 50); B0 = sp.N(sp.diff(e, LAM), 50)
            if abs(B0) > 1e-40: lam_vals.append(A0/(-B0))
            else: lam_vals.append(('identically', sp.N(A0, 5)))
    res16 = max(abs(sp.N(val.subs(sub).subs(LAM, sp.Rational(1,16)).subs({al: A_, be: B_, r: 1, v: 1}), 50))
                for val in dOm_s.values() for A_, B_ in [(sp.Rational(3,10), sp.Rational(1,5)), (sp.Rational(11,10), sp.Rational(7,10)), (sp.Rational(1,10**6), sp.Rational(1,10**6))])
    P(f"{k}: LAMBDA solving d*G=0 at 3 pts x {len(dOm_s)} components: {[sp.N(x_,22) if not isinstance(x_, tuple) else x_ for x_ in lam_vals]}; residual |d*G| at LAMBDA=1/16: {sp.N(res16,3)}")
P("\n== full Einstein (all 66 components), dG4 = 0, Riemann invariants ==")
for (k, fp, x1fac, kap, lam) in cases:
    t1 = time.time(); par = fpar(fp, x1fac)
    maxE = 0; maxsc = 0; Kmax = 0; RRmax = 0; W2max = 0; W2min = mp.inf; Kmin = mp.inf; maxdG = 0; maxG = 0; Qm = 0
    for ii, (A_, B_) in enumerate(GRID):
        pt = [mp.mpf(1), mp.mpf(1), A_, B_]
        g_, gi_, Rm = NC.at(par, pt)
        K, RR, W2, R, Ric, Qmax, Qim = invariants(g_, gi_, Rm, 11)
        ov = Om_f(*(par+[lam, kap]+pt)); Om = {kk: x for kk, x in zip(Om_keys, ov) if x != 0}
        G4 = hodge_num(Om, g_, gi_, 11, 7)
        res, sc, G2 = einstein_residual(G4, g_, gi_, Ric, 11)
        maxE = max(maxE, res); maxsc = max(maxsc, sc)
        Kmax = max(Kmax, K); Kmin = min(Kmin, K); RRmax = max(RRmax, RR); W2max = max(W2max, W2); W2min = min(W2min, W2); Qm = max(Qm, Qmax)
        if ii % 4 == 0 and 'LAMBDA' not in k:
            dG, Gs = ext_d_num(lambda q: G4_at(par, lam, kap, q), pt, DEPIDX, 11, 4, mp.mpf('1e-12'))
            maxdG = max(maxdG, dG); maxG = max(maxG, Gs)
    RES[k] = dict(maxE=maxE, sc=maxsc, Kmax=Kmax, Kmin=Kmin, RRmax=RRmax, W2max=W2max, Qm=Qm, W2min=W2min, maxdG=maxdG, maxG=maxG)
    P(f"{k}: max_grid max_MN |E^M_N| = {mp.nstr(maxE,3)}  (curvature scale max|R^M_N| = {mp.nstr(maxsc,5)});  PASS(1e-10)={bool(maxE<1e-10)}  [{time.time()-t1:.0f}s]")
    if 'LAMBDA' not in k:
        P(f"    dG4 (central FD h=1e-12, every 4th grid pt): max|dG| = {mp.nstr(maxdG,3)}  (max|G| comp {mp.nstr(maxG,4)})")
    if 'CONTROL' not in k:
        P(f"    K = R_MNPQ R^MNPQ in [{mp.nstr(Kmin,10)}, {mp.nstr(Kmax,10)}] /l^4 ; RicSq max {mp.nstr(RRmax,10)} ; Weyl^2 in [{mp.nstr(W2min,10)}, {mp.nstr(W2max,10)}]")
        P(f"    l_p^2 sqrt(K)_max = {mp.nstr(mp.sqrt(Kmax)/ell**2,6)} ; l_p^2 sqrt(RicSq)_max = {mp.nstr(mp.sqrt(RRmax)/ell**2,6)} ; l_p^2 sqrt(Weyl^2)_max = {mp.nstr(mp.sqrt(W2max)/ell**2,6)}")
        P(f"    curvature operator max|eig| = {Qm:.6f} /l^2 -> l_p^2 max|K_sec| <= {Qm/float(ell)**2:.4e} ; R^4 estimate (l_p^2 max|K|)^3 = {(Qm/float(ell)**2)**3:.2e}")
# ---------- systole ----------
P("\n== systole (Bolza bound, CONDITIONAL literature; arithmetic PROVED) ==")
sysB = 2*mp.acosh(1+mp.sqrt(2))
P(f"sys_max(genus 2) = 2 arccosh(1+sqrt2) = {mp.nstr(sysB,15)}")
Tm2 = 1/((2*mp.pi)**2)   # T_M2 = 1/((2 pi)^2 l_p^3)
for k, fp in FP.items():
    X1 = fp['X1']; X2 = fp['X2']; X0 = (X1*X2)**-2
    eg = mp.sqrt(mp.mpf(sp.N(X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2), 40))); ef = mp.mpf(sp.N(X0**-1, 40))
    rho = ell*eg; L5 = ell*ef
    smin_geo = 1/rho                          # sys_phys >= l_p   (curvature-1 units)
    smin_m2 = (2*mp.pi)**2/(L5**2)/rho        # T_M2 * sys_phys >= 1/L5^2  -> sys_phys >= (2pi)^2 l_p^3 / L5^2
    P(f"{k}: rho_Sigma = l e^g0 = {mp.nstr(rho,8)} l_p ; L5 = {mp.nstr(L5,8)} l_p ; Bolza sys_phys = {mp.nstr(sysB*rho,8)} l_p ; "
      f"range (0, {mp.nstr(sysB*rho,8)}] l_p ; min sys (unit) for sys_phys>=l_p: {mp.nstr(smin_geo,6)} ; for wrapped-M2 string tension >= 1/L5^2: {mp.nstr(smin_m2,6)} ; "
      f"for M2-on-geodesic string scale >= 1/rho (KK on Sigma): {mp.nstr((2*mp.pi)**2/rho**3, 6)}")
P(f"\nDONE total {time.time()-T0:.0f}s")
