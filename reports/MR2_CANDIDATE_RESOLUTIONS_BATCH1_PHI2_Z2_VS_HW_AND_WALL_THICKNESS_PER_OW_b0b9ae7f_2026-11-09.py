#!/usr/bin/env python3
# MR2 2026-11-09, OW b0b9ae7f batch 1: (A) pointwise Pontryagin 4-form tr R^R on the C3 fixed set of phi2 -> -phi2 in MN2
# (10D induced metric = V2 cand_metric with the phi2 row/col removed; totally geodesic, g_{phi2,*} = 0 at a2 = 0);
# (B) wall-thickness scales; (C) NEC-deficit magnitude. Routines exec'd from frozen V2 .py (sha ad134752...), banner suppressed.
import hashlib, io, contextlib, itertools, time
T00 = time.time()
V2 = '/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
raw = open(V2,'rb').read(); h = hashlib.sha256(raw).hexdigest()
assert h == 'ad134752da79e3064e209cd840b0aec53e004e3fa0fec8bbc9299eb12940eb85', h
with contextlib.redirect_stdout(io.StringIO()):
    exec(raw.decode().split('# ======================= MAIN =======================')[0])
import numpy as np
mp.mp.dps = 40
def P(s): print(s, flush=True)
P("== MR2 batch-1 candidate resolutions: computations (dps 40) ==")
P(f"V2 routines sha256 verified: {h}")
fp = FP["MN2(z=1)"]; X1, X2 = fp['X1'], fp['X2']; X0 = (X1*X2)**-2
PARs = [X1, X2, X0**-2, X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2), 1, 0]
PAR = [mp.mpf(sp.N(x_, 60)) for x_ in PARs]
P("\n== (A) C3 fixed set {phi2 = 0} (beta in (0,pi) covers mu2 = sin(al) sin(be) of both signs): tr R^R of the induced 10D metric ==")
GC = cand_metric().subs(a2s, 0)
assert all(sp.simplify(GC[10,j]) == 0 for j in range(10)), "phi2 cross terms"
G10 = GC[:10,:10]; G10[0,0] = -G10[0,0]   # Euclidean continuation t -> i t (nonvanishing of tr R^R unaffected)
coords10 = [t,x1,x2,x3,r,u,v,al,be,p1]
NG = NumGeom(G10, coords10, dep, PARAMS)
def ptr(a_, b_):
    g_, gi_, Rm = NG.at(PAR, [mp.mpf(1), mp.mpf(1), mp.mpf(a_), mp.mpf(b_)])
    n = 10
    g = np.array([[float(g_[i,j]) for j in range(n)] for i in range(n)])
    Rud = np.zeros((n,n,n,n))
    for (a,b,c,d), val in Rm.items(): Rud[a,b,c,d] = float(val); Rud[a,b,d,c] = -float(val)
    Rdd = np.einsum('ak,kbcd->abcd', g, Rud)
    L = np.linalg.cholesky(g); E = np.linalg.inv(L)          # orthonormal frame: e_i = E_i^m dx_m-dual
    Rh = np.einsum('im,jn,ka,lb,mnab->ijkl', E, E, E, E, Rdd)
    sym = np.max(np.abs(Rh + np.transpose(Rh, (1,0,2,3))))
    pr = np.max(np.abs(Rh - np.transpose(Rh, (2,3,0,1))))
    # Pontryagin 4-form P_{abcd} = sum_{ij} R_{ij[ab} R_{ji cd]} * (4!/(2!2!)) -> components a<b<c<d
    Pm = 0.0; arg = None; Pn2 = 0.0
    for (a,b,c,d) in itertools.combinations(range(n), 4):
        s = 0.0
        for (p_, q_, r_, s_, sg) in [(a,b,c,d,1),(a,c,b,d,-1),(a,d,b,c,1)]:
            s += sg*2*np.sum(Rh[:,:,p_,q_]*Rh[:,:,r_,s_].T)
        Pn2 += s*s
        if abs(s) > Pm: Pm = abs(s); arg = (a,b,c,d)
    K = float(np.sum(Rh*Rh))
    return Pm, arg, np.sqrt(Pn2), K, sym, pr
names = ['t','x1','x2','x3','r','u','v','al','be','p1']
for (a_, b_) in [('0.37','1.11'), ('2.01','0.23'), ('1.2','2.5'), ('0.8','0.6')]:
    Pm, arg, Pn, K, sym, pr = ptr(a_, b_)
    P(f"  (alpha,beta)=({a_},{b_}): max|tr(R^R)_abcd| (orthonormal) = {Pm:.6e} at {[names[i] for i in arg]}; |tr R^R| (sum over a<b<c<d) = {Pn:.6e}; induced Riem^2 = {K:.6f}; antisym/pair-sym checks {sym:.1e}/{pr:.1e}")
P("\n== (B) wall-thickness scales at N = 4880 (l_p = 1) ==")
N_ = mp.mpf(N); ell = 2*(mp.pi*N_)**(mp.mpf(1)/3); RS4 = (mp.pi*N_)**(mp.mpf(1)/3)
P(f"  AdS7xS4 radii for N M5s: R_S4 = (pi N)^(1/3) = {mp.nstr(RS4,10)}; R_AdS7 = 2 R_S4 = l = {mp.nstr(ell,10)}")
P(f"  flux check: int_S4 G4 with G4 = 3 R^3 vol(unit S4) = 3 R^3 * 8pi^2/3 = 8 pi^2 R^3 = {mp.nstr(8*mp.pi**2*RS4**3,15)} vs (2pi)^3 N = {mp.nstr((2*mp.pi)**3*N_,15)}")
F0 = PAR[2]; wmin = PAR[0]**(mp.mpf(1)/3)*F0; wmax = PAR[1]**(mp.mpf(1)/3)*F0
kmax = 1/(ell*mp.sqrt(wmin)); kmin = 1/(ell*mp.sqrt(wmax))
P(f"  wall curvature k in [{mp.nstr(kmin,8)}, {mp.nstr(kmax,8)}]; 1/k in [{mp.nstr(1/kmax,8)}, {mp.nstr(1/kmin,8)}]; L5 = l sqrt(F0) = {mp.nstr(ell*mp.sqrt(F0),8)}")
for eps in [1, 3, 10, RS4]:
    P(f"  eps_y = {mp.nstr(eps,5)}: k*eps_y in [{mp.nstr(kmin*eps,4)}, {mp.nstr(kmax*eps,4)}] (thin wall needs << 1); EFT factor (k l_p)(l_p/eps)^m, m=1: [{mp.nstr(kmin/eps,3)}, {mp.nstr(kmax/eps,3)}], m=3: [{mp.nstr(kmin/eps**3,3)}, {mp.nstr(kmax/eps**3,3)}]")
P("\n== (C) NEC deficit: required S(k,k) = -2k/kappa^2 along every internal null k = t+e; rho_w = 6k/kappa^2 <-> N_req M5 units ==")
for lbl, lo, hi in [("horizontal, warp range", mp.mpf('1.08418'), mp.mpf('1.72103')), ("fixed-phi, warp range", mp.mpf('0.883006'), mp.mpf('1.40168'))]:
    Nlo = lo*2*N_; Nhi = hi*2*N_
    P(f"  {lbl}: N_req in [{mp.nstr(Nlo,6)}, {mp.nstr(Nhi,6)}]; min negative energy |sigma| >= rho_w/3 <-> [{mp.nstr(Nlo/3,6)}, {mp.nstr(Nhi/3,6)}] M5 units; OM5-type planes (charge/tension -1/2 each) needed >= [{mp.nstr(2*Nlo/3,6)}, {mp.nstr(2*Nhi/3,6)}]")
P(f"\nDONE {time.time()-T00:.0f}s")
