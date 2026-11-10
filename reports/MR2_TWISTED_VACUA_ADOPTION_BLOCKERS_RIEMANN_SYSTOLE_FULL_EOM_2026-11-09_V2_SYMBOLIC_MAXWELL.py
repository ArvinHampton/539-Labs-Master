# frozen: V2 code verbatim (sha ad134752...) up to MAIN, then exact sympy simplify of d*G4 at LAMBDA=1/16 + controls
# V2 of MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09.py
# supersedes frozen V1 sha256 e2a1f02d16f8810c761934f1fc647b7ad71f2a430ae1fec0b2bbb326e50737a6
# ONLY change: mp.det on minors of g^-1 replaced by sdet() (exact Gaussian elimination w/ partial pivoting,
# returns 0 for an exactly-zero pivot column). V1 crashed (mpmath LU_decomp TypeError) on singular 7x7 / 4x4 minors
# of the block-structured candidate inverse metric. No physics, tolerance, grid or flux change.
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

def sdet(M):
    n = M.rows; A = [[M[i,j] for j in range(n)] for i in range(n)]; d = mp.mpf(1)
    for j in range(n):
        p = max(range(j, n), key=lambda i: abs(A[i][j]))
        if A[p][j] == 0: return mp.mpf(0)
        if p != j: A[j], A[p] = A[p], A[j]; d = -d
        d *= A[j][j]
        for i in range(j+1, n):
            f = A[i][j]/A[j][j]
            if f != 0:
                for k in range(j, n): A[i][k] -= f*A[j][k]
    return d
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
            dm = sdet(M)
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
            dm = sdet(mp.matrix([[gi[b,c] for c in C] for b in B]))
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

import time
Om_s, U_s = Omega_sym(); dOm_s = dform(Om_s)
print("components of dOmega:", list(dOm_s.keys()), flush=True)
for k, fp in FP.items():
    X1 = fp['X1']; X2 = fp['X2']; X0 = (X1*X2)**-2
    sub = {X1s: X1, X2s: X2, F0s: X0**-2, G0s: X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2), a1s: fp['a1'], a2s: fp['a2'], KAP: 1, LAM: sp.Rational(1,16)}
    for key, val in dOm_s.items():
        t1=time.time(); e = sp.simplify(sp.nsimplify(val.subs(sub)) if False else val.subs(sub))
        e2 = sp.simplify(sp.expand_trig(e).rewrite(sp.cos))
        e3 = sp.nsimplify(sp.N(e2, 60), tolerance=1e-50) if e2 != 0 else 0
        print(k, key, "simplify ->", e2 if len(str(e2))<200 else str(e2)[:200]+"...", "| numeric-coefficient cleanup ->", e3, f"[{time.time()-t1:.0f}s]", flush=True)

print("CONTROL LAMBDA=0 and LAMBDA=1/8 (must be nonzero):", flush=True)
fp = FP["BBBW(z=2)"]; X1 = fp['X1']; X2 = fp['X2']; X0 = (X1*X2)**-2
for lv in [0, sp.Rational(1,8)]:
    sub = {X1s: X1, X2s: X2, F0s: X0**-2, G0s: X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2), a1s: fp['a1'], a2s: fp['a2'], KAP: 1, LAM: lv}
    for key, val in dOm_s.items():
        e = val.subs(sub).subs({al: sp.Rational(11,10), be: sp.Rational(7,10), r: 1, v: 1})
        print("  LAMBDA=", lv, key, "value at (alpha,beta)=(1.1,0.7):", sp.N(e, 20), flush=True)
