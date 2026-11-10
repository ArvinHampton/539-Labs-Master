#!/usr/bin/env python3
# MR2 2026-11-09 (PP gate 384096a8 fixes 4,5,6): frame-normalized Einstein residuals for ALL FOUR candidates (incl. BBBW z=2, absent
# from the V2 PERPOINT log), on the V2 17-point grid + near-mu1=1 / near-mu2=1 points, dps 60; and a dG4 control that CAN fail.
# Imports frozen blocker V2 code (sha ad134752...) verbatim up to MAIN. Frame-normalized residual:
#   rel = sqrt|tr(E^M_N E^N_M)| / sqrt|tr(R^M_N R^N_M)|  = (Frobenius norm of orthonormal-frame components of E)/(same for Ric),
#   frame-invariant; E_{tM} = 0 for M != t so the Lorentzian trace equals the Euclidean Frobenius sum.
import sys, time, itertools
import sympy as sp, mpmath as mp
SRC = '/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
src = open(SRC).read(); exec(src[:src.index('# ======================= MAIN')])
def P(s): print(s, flush=True)
T0 = time.time()
GC = cand_metric(); NC = NumGeom(GC, coords, dep, PARAMS)
Om_s, U_s = Omega_sym(); Om_keys = list(Om_s.keys())
Om_f = lamb(PARAMS+[LAM, KAP]+dep, [Om_s[k] for k in Om_keys])
gk = [(i,j) for i in range(11) for j in range(11) if GC[i,j] != 0]
g_f = lamb(PARAMS+dep, [GC[i,j] for i,j in gk])
def metric_at(par, pt):
    vals = g_f(*(list(par)+list(pt))); g_ = mp.zeros(11)
    for (i,j), x in zip(gk, vals): g_[i,j] = x
    return g_
def G4_at(par, lam, kap, pt):
    g_ = metric_at(par, pt); gi_ = g_**-1
    ov = Om_f(*(list(par)+[lam, kap]+list(pt))); Om = {k: x for k, x in zip(Om_keys, ov) if x != 0}
    return hodge_num(Om, g_, gi_, 11, 7)
def fpar_hp(fp):
    X1 = fp['X1']; X2 = fp['X2']; X0 = (X1*X2)**-2
    ef = 1/X0; e2g = X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2)
    return [mp.mpf(sp.N(x_, 120)) for x_ in (X1, X2, ef**2, e2g, fp['a1'], fp['a2'])]
def einstein_frame(par, lam, kap, pt):
    g_, gi_, Rm = NC.at(par, pt)
    Ric = mp.zeros(11)
    for (a,b,c,d), val in Rm.items():
        if c == a: Ric[b,d] += val
        if d == a: Ric[b,c] -= val
    ov = Om_f(*(par+[lam, kap]+pt)); Om = {kk: x for kk, x in zip(Om_keys, ov) if x != 0}
    G4 = hodge_num(Om, g_, gi_, 11, 7)
    # reproduce einstein_residual's E_MN but keep the matrix
    Gup = {}
    for B in itertools.combinations(range(11), 4):
        s = 0
        for C in G4:
            dm = sdet(mp.matrix([[gi_[b,c] for c in C] for b in B]))
            if dm != 0: s += dm*G4[C]
        if s != 0: Gup[B] = s
    G2 = 24*sum(G4[A]*Gup.get(A, 0) for A in G4)
    def comp(F, M, T):
        if M in T: return 0
        key = tuple(sorted((M,)+T)); val = F.get(key, 0)
        return perm_sign((M,)+T)*val if val != 0 else 0
    triples = list(itertools.combinations(range(11), 3))
    lowM = [[comp(G4, M, T) for T in triples] for M in range(11)]
    upS = [[comp(Gup, S, T) for T in triples] for S in range(11)]
    E = mp.zeros(11)
    for M in range(11):
        for Nn in range(11):
            s = 0
            for ti in range(len(triples)):
                x = lowM[M][ti]
                if x == 0: continue
                y = sum(g_[Nn,S]*upS[S][ti] for S in range(11) if g_[Nn,S] != 0 and upS[S][ti] != 0)
                s += x*y
            E[M,Nn] = Ric[M,Nn] - (6*s - g_[M,Nn]*G2/12)/12
    Em = gi_*E; Rmx = gi_*Ric
    fe = mp.sqrt(abs(sum(Em[i,j]*Em[j,i] for i in range(11) for j in range(11))))
    fr = mp.sqrt(abs(sum(Rmx[i,j]*Rmx[j,i] for i in range(11) for j in range(11))))
    return fe, fr, max(abs(x) for x in Em)
mp.mp.dps = 60
eps_ = mp.mpf('1e-6'); dl = mp.mpf('1.234e-3')
ALS = [eps_, mp.pi/4+dl, mp.pi/2+dl, 3*mp.pi/4+dl, mp.pi-eps_]; BES = [eps_, mp.pi/4+dl, mp.pi/2-eps_]
GRID = [(a_, b_) for a_ in ALS for b_ in BES] + [(mp.mpf('0.37'), mp.mpf('1.11')), (mp.mpf('2.01'), mp.mpf('0.23'))]
GRID += [(mp.pi/2+mp.mpf('1e-3'), mp.mpf('1e-3')), (mp.pi/2-mp.mpf('1e-4'), mp.mpf('1e-5')), (mp.pi/2+mp.mpf('1e-3'), mp.pi/2-mp.mpf('1e-3'))]
LBL = ['grid']*17 + ['near mu1=1', 'near mu1=1', 'near mu2=1']
P(f"== frame-normalized Einstein residual, dps {mp.mp.dps}, {len(GRID)} points per candidate (17 = V2 grid; +2 near mu1=1, +1 near mu2=1) ==")
for k, fp in FP.items():
    par = fpar_hp(fp); worst = 0; worst_reg = 0; t1 = time.time()
    for (A_, B_), lb in zip(GRID, LBL):
        fe, fr, mc = einstein_frame(par, mp.mpf(1)/16, 1, [mp.mpf(1), mp.mpf(1), A_, B_])
        rel = fe/fr
        corner = (min(A_, mp.pi-A_) < mp.mpf('1e-5')) and (min(B_, mp.pi/2-B_) < mp.mpf('1e-5'))
        worst = max(worst, rel)
        if not corner: worst_reg = max(worst_reg, rel)
        P(f"  {k} (alpha,beta)=({mp.nstr(A_,8)}, {mp.nstr(B_,8)}) [{lb}{', pole corner' if corner else ''}]: frame |E|/|Ric| = {mp.nstr(rel,3)}  (coord-mixed max|E^M_N| = {mp.nstr(mc,3)})")
    P(f"  {k} SUMMARY: max frame-rel residual = {mp.nstr(worst,3)} overall; {mp.nstr(worst_reg,3)} excluding doubly-near-pole corners  [{time.time()-t1:.0f}s]")
P("\n== frame-normalized controls (z=2, generic point (0.37,1.11)) ==")
fp = FP["BBBW(z=2)"]; par = fpar_hp(fp); pt = [mp.mpf(1), mp.mpf(1), mp.mpf('0.37'), mp.mpf('1.11')]
for lab, pr, lam, kap in [("true", par, mp.mpf(1)/16, 1), ("LAMBDA=0", par, 0, 1), ("LAMBDA=14/16", par, mp.mpf(14)/16, 1),
                          ("LAMBDA x (1+1e-6)", par, mp.mpf(1)/16*(1+mp.mpf('1e-6')), 1), ("flux x1.1", par, mp.mpf(1)/16, mp.mpf('1.1'))]:
    fe, fr, mc = einstein_frame(pr, lam, kap, pt); P(f"  {lab}: frame |E|/|Ric| = {mp.nstr(fe/fr, 4)}")
X1w = fp['X1']*sp.Rational(11,10); X2 = fp['X2']; X0w = (X1w*X2)**-2
parw = [mp.mpf(sp.N(x_, 120)) for x_ in (X1w, X2, (1/X0w)**2, X1w*X2/8*((1-2)*X1w+(1+2)*X2), fp['a1'], fp['a2'])]
fe, fr, mc = einstein_frame(parw, mp.mpf(1)/16, 1, pt); P(f"  X1 x 1.1 (f,g recomputed): frame |E|/|Ric| = {mp.nstr(fe/fr, 4)}")
P("\n== dG4 = 0 with a control that CAN fail (central FD, h = 1e-25, dps 60) ==")
for k, fp in FP.items():
    par = fpar_hp(fp)
    for pt in [[mp.mpf(1), mp.mpf(1), mp.mpf('0.37'), mp.mpf('1.11')], [mp.mpf(1), mp.mpf(1), mp.mpf('2.01'), mp.mpf('0.23')]]:
        row = []
        for lab, lam in [("LAMBDA=1/16", mp.mpf(1)/16), ("CONTROL LAMBDA=0", mp.mpf(0)), ("CONTROL LAMBDA=1/16(1+1e-6)", mp.mpf(1)/16*(1+mp.mpf('1e-6')))]:
            dG, Gs = ext_d_num(lambda q: G4_at(par, lam, 1, q), pt, DEPIDX, 11, 4, mp.mpf('1e-25'))
            row.append(f"{lab}: max|dG4| = {mp.nstr(dG, 3)} (max|G4| {mp.nstr(Gs, 3)})")
        P(f"  {k} (alpha,beta)=({mp.nstr(pt[2],3)},{mp.nstr(pt[3],3)}): " + " ; ".join(row))
P(f"DONE {time.time()-T0:.0f}s")
