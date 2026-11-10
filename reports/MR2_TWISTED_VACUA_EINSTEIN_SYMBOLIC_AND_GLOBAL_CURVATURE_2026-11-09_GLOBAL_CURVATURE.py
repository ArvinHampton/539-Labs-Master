#!/usr/bin/env python3
# MR2 2026-11-09 (OW ff8a1670, item B): global maxima over the internal space of K=Riem^2, Ric^2, Weyl^2 and of the curvature-operator
# spectral radius (bound on |K_sec|), MN1, MN2, BBBW z=2, z=3. Reuses the frozen blocker V2 code (sha ad134752...) verbatim up to MAIN.
# Invariants depend only on (alpha, beta) (AdS5 x H2 homogeneity). Fundamental domain: alpha in [0, pi/2] (alpha -> pi - alpha is the
# isometry mu0 -> -mu0), beta in [0, pi/2] (mu1, mu2 >= 0 up to the phi_i -> phi_i + pi isometries). Gamma (the genus-2 modulus) does not
# enter: Sigma = H2/Gamma is locally H2 and the metric is smooth, so all local invariants are Gamma-independent.
import sys, time, itertools
import sympy as sp, mpmath as mp, numpy as np
SRC = '/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
src = open(SRC).read(); exec(src[:src.index('# ======================= MAIN')])
def P(s): print(s, flush=True)
T0 = time.time()
GC = cand_metric(); NC = NumGeom(GC, coords, dep, PARAMS)
def fpar_hp(fp):
    X1 = fp['X1']; X2 = fp['X2']; X0 = (X1*X2)**-2
    ef = 1/X0; e2g = X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2)
    return [mp.mpf(sp.N(x_, 120)) for x_ in (X1, X2, ef**2, e2g, fp['a1'], fp['a2'])]
def inv_hp(par, a_, b_, want_eig=False, mpeig=False):
    g_, gi_, Rm = NC.at(par, [mp.mpf(1), mp.mpf(1), a_, b_]); n = 11
    up = {}
    for (a,e,c,d), val in Rm.items():
        for b in range(n):
            if gi_[b,e] != 0: up[(a,b,c,d)] = up.get((a,b,c,d), 0) + gi_[b,e]*val
    K = 0
    for (a,b,c,d), val in up.items():
        if a < b: w = up.get((c,d,a,b), 0)
        elif a > b: w = -up.get((c,d,b,a), 0)
        else: w = 0
        K += val*w
    K = 2*K
    Ric = mp.zeros(n)
    for (a,b,c,d), val in Rm.items():
        if c == a: Ric[b,d] += val
        if d == a: Ric[b,c] -= val
    Rmix = gi_*Ric; R = sum(Rmix[i,i] for i in range(n)); RR = sum(Rmix[i,j]*Rmix[j,i] for i in range(n) for j in range(n))
    W2 = K - 4*RR/9 + 2*R**2/90
    Q = None
    if want_eig:
        pairs = list(itertools.combinations(range(n), 2)); pid = {p_: i for i, p_ in enumerate(pairs)}
        if mpeig:
            # restrict to the rows/cols that are nonzero (block-sparse) for mp.eig
            Mq = {}
            for (a,b,c,d), val in up.items():
                if a < b: Mq[(pid[(a,b)], pid[(c,d)])] = Mq.get((pid[(a,b)], pid[(c,d)]), 0) + val
            act = sorted(set(i for i, j in Mq) | set(j for i, j in Mq)); ix = {p: k for k, p in enumerate(act)}
            M = mp.zeros(len(act))
            for (i, j), val in Mq.items(): M[ix[i], ix[j]] = val
            ev = mp.eig(M, left=False, right=False)
            Q = max(abs(x) for x in ev)
        else:
            Mq = np.zeros((len(pairs), len(pairs)))
            for (a,b,c,d), val in up.items():
                if a < b: Mq[pid[(a,b)], pid[(c,d)]] += float(val)
            Q = float(np.max(np.abs(np.linalg.eigvals(Mq))))
    return dict(K=K, RR=RR, W2=W2, R=R, Q=Q)
ell = 2*(mp.pi*4880)**(mp.mpf(1)/3)
# --- cross-check of the exact (item A) conformal Ricci scalar against these numerics (z=2, s_a=2/9, s_b=7/5) ---
mp.mp.dps = 40
fp = FP["BBBW(z=2)"]; par = fpar_hp(fp)
a_c, b_c = 2*mp.atan(mp.mpf(2)/9), 2*mp.atan(mp.mpf(7)/5)
Rn = inv_hp(par, a_c, b_c)['R']
Dc = (par[0]*par[1])**-2*mp.cos(a_c)**2 + par[0]*(mp.sin(a_c)*mp.cos(b_c))**2 + par[1]*(mp.sin(a_c)*mp.sin(b_c))**2
P(f"cross-check: z=2 at (s_a,s_b)=(2/9,7/5): V2-numeric R = {mp.nstr(Rn, 25)} ; Delta = {mp.nstr(Dc, 25)} ; R*Delta^(-2/3) = {mp.nstr(Rn*Dc**(-mp.mpf(2)/3), 25)} (item-A exact route printed 4.79894282723861209339590479980)")
INV = ['K', 'RR', 'W2', 'Q']
NG = int(sys.argv[2]) if len(sys.argv) > 2 else 17
# Precision note (measured in the blocker V2 checks): pole-adjacent cancellations cost ~ 5.7*log10(1/eps) digits, so
# seeds use eps = 1e-5 at dps 50, refinement is confined to [1e-5, pi/2 - 1e-5] at dps 60, and box faces / poles are
# evaluated as LIMITS by Richardson extrapolation v(eps) = L + c eps^2 + O(eps^4) from eps = 1e-7, 1e-8 at dps 110.
EPS = mp.mpf('1e-5')
def face_limit(par, q, x, faces):
    mp.mp.dps = 110
    def at(off):
        aa = off if faces[0] == 0 else (mp.pi/2 - off if faces[0] == 1 else x[0])
        bb = off if faces[1] == 0 else (mp.pi/2 - off if faces[1] == 1 else x[1])
        return inv_hp(par, aa, bb, want_eig=(q == 'Q'), mpeig=(q == 'Q'))[q]
    v7 = at(mp.mpf('1e-7')); v8 = at(mp.mpf('1e-8'))
    L = (100*v8 - v7)/99
    mp.mp.dps = 60
    return L, abs(v8 - v7)
for k in (sys.argv[1].split(",") if len(sys.argv) > 1 else list(FP)):
    t1 = time.time(); par = fpar_hp(FP[k]); mp.mp.dps = 50
    A = [EPS + (mp.pi/2 - 2*EPS)*i/(NG-1) for i in range(NG)]; B = A
    best = {q: (-1, None) for q in INV}; table = {}
    for i, a_ in enumerate(A):
        for j, b_ in enumerate(B):
            d = inv_hp(par, a_, b_, want_eig=True); table[(i, j)] = d
            for q in INV:
                if d[q] > best[q][0]: best[q] = (d[q], (i, j))
    P(f"\n## {k}: {NG}x{NG} seed grid on [1e-5, pi/2-1e-5]^2, dps 50 [{time.time()-t1:.0f}s]")
    for q in INV:
        val, (i, j) = best[q]; P(f"   seed max {q}: {mp.nstr(val, 15)} at (alpha, beta) = ({mp.nstr(A[i], 6)}, {mp.nstr(B[j], 6)})  [grid idx {i},{j}]")
    for q in INV:
        P(f"   grid profile {q}: beta=pi/2 edge vs alpha: {[mp.nstr(table[(i, NG-1)][q], 6) for i in range(0, NG, max(1, NG//8))]}")
        P(f"   grid profile {q}: alpha=pi/2 edge vs beta: {[mp.nstr(table[(NG-1, j)][q], 6) for j in range(0, NG, max(1, NG//8))]}")
        P(f"   grid profile {q}: alpha=1e-5 (pole) vs beta: {[mp.nstr(table[(0, j)][q], 6) for j in range(0, NG, max(1, NG//8))]}")
    mp.mp.dps = 60
    for q in INV:
        val, (i, j) = best[q]; x = [A[i], B[j]]
        f = lambda xx: inv_hp(par, xx[0], xx[1], want_eig=(q == 'Q'))[q]
        lo_b, hi_b = EPS, mp.pi/2 - EPS
        step = (mp.pi/2)/(NG-1); gr = (mp.sqrt(5)-1)/2
        for sweep in range(4):
            for c in range(2):
                lo = max(x[c]-step, lo_b); hi = min(x[c]+step, hi_b)
                a1 = hi - gr*(hi-lo); b1 = lo + gr*(hi-lo)
                xa = list(x); xa[c] = a1; xb = list(x); xb[c] = b1; fa = f(xa); fb = f(xb)
                for it in range(30):
                    if fa > fb: hi = b1; b1 = a1; fb = fa; a1 = hi - gr*(hi-lo); xa = list(x); xa[c] = a1; fa = f(xa)
                    else: lo = a1; a1 = b1; fa = fb; b1 = lo + gr*(hi-lo); xb = list(x); xb[c] = b1; fb = f(xb)
                xc = list(x); xc[c] = (a1+b1)/2
                xl = list(x); xl[c] = lo_b; xh = list(x); xh[c] = hi_b
                x = max([(f(xc), xc), (f(xl), xl), (f(xh), xh), (f(x), list(x))], key=lambda o: o[0])[1]
            step = step/4
        faces = [0 if x[0] <= lo_b*(1+mp.mpf('1e-9')) else (1 if x[0] >= hi_b - mp.mpf('1e-15') else None),
                 0 if x[1] <= lo_b*(1+mp.mpf('1e-9')) else (1 if x[1] >= hi_b - mp.mpf('1e-15') else None)]
        if faces[0] is None and faces[1] is None:
            vmax = f(x); err = mp.mpf(0)
            if q == 'Q':
                mp.mp.dps = 60; vmax = inv_hp(par, x[0], x[1], want_eig=True, mpeig=True)['Q']
        else:
            vmax, err = face_limit(par, q, x, faces)
        lab = [('alpha->0 (pole mu0=1)' if faces[0] == 0 else ('alpha=pi/2 (mu0=0)' if faces[0] == 1 else f'alpha={mp.nstr(x[0], 15)}')),
               ('beta->0 (mu2=0)' if faces[1] == 0 else ('beta->pi/2 (mu1=0)' if faces[1] == 1 else f'beta={mp.nstr(x[1], 15)}'))]
        sc = (lambda y: mp.sqrt(y)/ell**2) if q != 'Q' else (lambda y: y/ell**2)
        P(f"   GLOBAL max {q} = {mp.nstr(vmax, 30)} /l^{4 if q != 'Q' else 2} at {lab}  (face-limit |v(1e-8)-v(1e-7)| = {mp.nstr(err, 3)}); "
          f"l_p^2 x {('sqrt(' + q + ')') if q != 'Q' else 'max|eig Q|'} = {mp.nstr(sc(vmax), 20)}" + (f" ; (l_p^2 max|eig Q|)^3 = {mp.nstr(sc(vmax)**3, 6)}" if q == 'Q' else ''))
    P(f"## {k} done [{time.time()-t1:.0f}s]")
P(f"DONE {time.time()-T0:.0f}s")
