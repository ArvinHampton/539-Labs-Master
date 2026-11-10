#!/usr/bin/env python3
# MR2 ERRATUM3 (2026-11-09): (A) exact factor by which the 48-node GL rule in u = tanh(rho/eps) under-integrates a rho-constant
# integrand (as used in ERRATUM2 .py 10d2ae9e for the NO_SOURCE baseline); (B) convergence of the k-weighted fibre averages
# <(wF0)^2> (horizontal and fixed-phi) under GL order doubling 24x16 -> 48x32 -> 96x64. Wall metric construction as in 10d2ae9e.
import hashlib, io, contextlib, time
T00 = time.time()
V2 = '/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
raw = open(V2,'rb').read(); h = hashlib.sha256(raw).hexdigest()
assert h == 'ad134752da79e3064e209cd840b0aec53e004e3fa0fec8bbc9299eb12940eb85', h
with contextlib.redirect_stdout(io.StringIO()):
    exec(raw.decode().split('# ======================= MAIN =======================')[0])
mp.mp.dps = 40
def P(s): print(s, flush=True)
P("== MR2 ERRATUM3 checks (dps 40) ==")
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
P("\n== (A) int_{-W eps}^{W eps} 1 drho via u = tanh(rho/eps), 48-node GL (same rule as 10d2ae9e), divided by exact 2 W eps ==")
XG, WG = glmp(48)
for W in [4, 10]:
    U = mp.tanh(W); q = sum(wg*U/(1-(U*xg)**2) for xg, wg in zip(XG, WG))   # eps factors cancel
    P(f"  W={W}: quadrature/exact = {mp.nstr(q/(2*W),12)} ; exact/quadrature = {mp.nstr(2*W/q,12)}")
P("\n== (B) fixed-phi and horizontal k-weighted averages <(wF0)^2>, GL order doubling ==")
fp = FP["MN2(z=1)"]; X1, X2 = fp['X1'], fp['X2']; X0 = (X1*X2)**-2
PARs = [X1, X2, X0**-2, X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2), 1, 0]
PAR = [mp.mpf(sp.N(x_, 60)) for x_ in PARs]
X1n, X2n, F0n, G0n = PAR[:4]; X0n = 1/(X1n*X2n)**2
GC = cand_metric(); gk_ = [(i,j) for i in range(11) for j in range(11) if GC[i,j] != 0]
gfun = lamb(PARAMS+dep, [GC[i,j] for i,j in gk_])
def met(a_, b_):
    vals = gfun(*(PAR+[mp.mpf(1), mp.mpf(1), a_, b_])); g_ = mp.zeros(11)
    for (i,j), x in zip(gk_, vals): g_[i,j] = x
    return g_
def Dfun(a_, b_): return X0n*mp.cos(a_)**2 + X1n*(mp.sin(a_)*mp.cos(b_))**2 + X2n*(mp.sin(a_)*mp.sin(b_))**2
def wF0(a_, b_): return Dfun(a_, b_)**(mp.mpf(1)/3)*F0n
for (na, nb) in [(24,16), (48,32), (96,64)]:
    xa, wa = glmp(na); xb, wb = glmp(nb)
    S = {'h': [0,0], 'f': [0,0]}
    for x_, u_ in zip(xa, wa):
        for y_, v_ in zip(xb, wb):
            a_ = (x_+1)*mp.pi/2; b_ = (y_+1)*mp.pi/4; w = u_*v_*mp.pi**2/8
            g_ = met(a_, b_); k = 1/mp.sqrt(wF0(a_, b_)); W2 = wF0(a_, b_)**2
            d6 = mp.det(mp.matrix([[g_[i,j] for j in range(5,11)] for i in range(5,11)]))
            for key, duv in [('h', (Dfun(a_, b_)**(mp.mpf(1)/3)*G0n)**2), ('f', g_[5,5]*g_[6,6])]:
                t_ = w*k*mp.sqrt(d6)/mp.sqrt(duv); S[key][0] += t_; S[key][1] += t_*W2
    P(f"  GL {na}x{nb}: horizontal <(wF0)^2> = {mp.nstr(S['h'][1]/S['h'][0],16)} (N_req/2N {mp.nstr(24*S['h'][0],14)}); fixed-phi <(wF0)^2> = {mp.nstr(S['f'][1]/S['f'][0],16)} (N_req/2N {mp.nstr(24*S['f'][0],14)})")
P(f"\nDONE {time.time()-T00:.0f}s")
