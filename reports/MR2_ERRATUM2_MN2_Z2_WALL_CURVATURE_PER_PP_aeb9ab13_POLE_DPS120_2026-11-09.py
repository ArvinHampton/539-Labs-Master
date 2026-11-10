#!/usr/bin/env python3
# MR2 ERRATUM2 supplement (2026-11-09): the 49x25 global scan in MR2_ERRATUM2_..._2026-11-09.py (sha 10d2ae9e...) returned
# Riem^2 ~1.0e10 at the alpha = 1e-9 pole row at dps 60. Riem^2 is a smooth scalar on compact S^4, so this must be either
# real or cancellation loss in the polar coordinates (terms ~ alpha^-8 ~ 1e72 > 10^60). Test: same grid at dps 60 vs 120. Nothing tuned.
import hashlib, io, contextlib, multiprocessing as mpc, time
T00 = time.time()
V2 = '/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
raw = open(V2,'rb').read(); h = hashlib.sha256(raw).hexdigest()
assert h == 'ad134752da79e3064e209cd840b0aec53e004e3fa0fec8bbc9299eb12940eb85', h
with contextlib.redirect_stdout(io.StringIO()):
    exec(raw.decode().split('# ======================= MAIN =======================')[0])
def P(s): print(s, flush=True)
P("== MR2 ERRATUM2 supplement: pole-row precision test, smooth MN2 (r-coords, cand_metric of V2) ==")
fp = FP["MN2(z=1)"]
X1, X2 = fp['X1'], fp['X2']; X0 = (X1*X2)**-2
PARs = [X1, X2, X0**-2, X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2), fp['a1'], fp['a2']]
GC = cand_metric()
NG = NumGeom(GC, [t,x1,x2,x3,r,u,v,al,be,p1,p2], dep, PARAMS)
def ev(args):
    dps, a_, b_ = args
    mp.mp.dps = dps
    PAR = [mp.mpf(sp.N(x_, dps+20)) for x_ in PARs]
    g_, gi_, Rm = NG.at(PAR, [mp.mpf(1), mp.mpf(1), mp.mpf(a_), mp.mpf(b_)])
    K = invariants(g_, gi_, Rm, 11)[0]
    return K
def pmap(argl):
    with mpc.get_context('fork').Pool(8) as pool: return pool.map(ev, argl)
mp.mp.dps = 130
pi = mp.pi
for (a_, b_) in [('1e-9', pi/2-mp.mpf('1e-12')), ('1e-9', '1e-12'), ('1e-7', pi/2-mp.mpf('1e-12')), ('1e-6', pi/2-mp.mpf('1e-12')), ('1e-3', pi/2-mp.mpf('1e-12'))]:
    a_ = mp.mpf(a_); b_ = mp.mpf(b_)
    vals = pmap([(d, a_, b_) for d in (40, 60, 90, 120)])
    P(f"  (alpha,beta)=({mp.nstr(a_,3)},{mp.nstr(b_,8)}): Riem^2 at dps 40/60/90/120 = {[mp.nstr(x,15) for x in vals]}")
GA = [mp.mpf('1e-9')] + [pi*i/48 + mp.mpf('1.234e-3') for i in range(1,48)] + [pi-mp.mpf('1e-9')]
GB = [mp.mpf('1e-12')] + [pi/2*j/24 + mp.mpf('1.234e-3') for j in range(1,24)] + [pi/2-mp.mpf('1e-12')]
SC = [(a_, b_) for a_ in GA for b_ in GB]
out = pmap([(120, a_, b_) for a_, b_ in SC])
iK = max(range(len(out)), key=lambda i: out[i])
P(f"  global {len(GA)}x{len(GB)} = {len(SC)} pts at dps 120 (same points as main .py): Riem^2 max {mp.nstr(out[iK],25)} at {[mp.nstr(x,6) for x in SC[iK]]}; min {mp.nstr(min(out),12)}")
P(f"  |max - 3408| = {mp.nstr(abs(out[iK]-3408),5)}")
P(f"\nDONE {time.time()-T00:.0f}s")
