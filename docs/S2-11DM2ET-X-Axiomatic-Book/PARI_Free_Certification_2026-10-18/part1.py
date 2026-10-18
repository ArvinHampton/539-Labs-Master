# Part (1): PARI-free certification of the ray-class structure of all 140 components, modulus p2^3 p5 p7 oo1 oo2.
import numpy as np, math, json, pickle, sys, time
from collections import defaultdict, Counter
sys.dont_write_bytecode = True
import rc, ideals, comp
QMAX = 400
R = rc.Ray(3); I = ideals.Ideals(R, 60000); CNT = I.counts()
LABELS = comp.labels()
CH = R.characters()
E = R.elems; NC = len(E)
X = np.array([[np.exp(2j*np.pi*float(R.chival(c, x))) for x in E] for c in CH])     # X[chi, class]
sig = np.array([R.idx[R.sigma(x)] for x in E])
# character types: infinity type from sign coordinates (values on iota(-1 at one place)); sigma-invariance; conductor
def chi_on_r(c, r): return R.chival(c, R.cl(r, 0))
info = []
for c in CH:
    t = (int(2*chi_on_r(c, (0,0,0,1,0))) % 2, int(2*chi_on_r(c, (0,0,0,0,1))) % 2)
    inv = all((R.chival(c, R.sigma(x)) - R.chival(c, x)) % 1 == 0 for x in E)
    # finite conductor exponents: p2: trivial on (O/p2^3)^x -> 0; on 1+p2^2 = <-1 at p2> = <2 in Z/4> trivial -> 2; else 3
    if chi_on_r(c, (1,0,0,0,0)) == 0: f2 = 0
    elif chi_on_r(c, (2,0,0,0,0)) == 0: f2 = 2
    else: f2 = 3
    f5 = int(chi_on_r(c, (0,1,0,0,0)) != 0); f7 = int(chi_on_r(c, (0,0,1,0,0)) != 0)
    info.append(dict(type=t, inv=inv, cond=(f2, f5, f7)))
t0 = time.time()
res = {}; Fs_all = {}; Fraw_all = {}
for idx, (al, be) in enumerate(LABELS):
    n1, n2, q, ph = comp.points(al, be, QMAX)
    rec = {}
    for sgn in (1, -1):
        s = np.sign(q) == sgn
        a_, b_, qq, pp = (2*n1+7*n2)[s], n2[s], np.abs(q[s]), ph[s]
        coef = defaultdict(complex)
        for N, v in zip(qq.tolist(), pp.tolist()): coef[N] += v
        nz = [N for N, v in coef.items() if abs(v) > 1e-9]
        if not nz: rec[sgn] = None; continue
        g = 0
        for N in nz: g = math.gcd(g, N)
        D, delta, _ = ideals.ramified_divisor(g)
        nmax = (19600*QMAX*98//100)//g
        # per-nu class assignment; W[class][n] accumulates weight*phase
        W = defaultdict(complex); hit = defaultdict(set)
        for A, Bv, N, v in zip(a_.tolist(), b_.tolist(), qq.tolist(), pp.tolist()):
            n = N//g
            if N % g or n > nmax or math.gcd(n, 70) != 1: continue
            x = ideals.class_of_quotient(R, (A, Bv), D, delta, I.g13)
            W[(R.idx[x], n)] += v
        # class function: F(cl) = W(cl,n)/I(cl,n), must be independent of n
        F = np.zeros(NC, complex); seen = np.zeros(NC, bool); spread = 0.0
        for (ci, n), v in W.items():
            cnt = CNT[n][E[ci]]
            assert cnt > 0, "lattice vector in a class with no ideal of that norm"
            val = v/cnt
            if not seen[ci]: F[ci] = val; seen[ci] = True
            else: spread = max(spread, abs(val - F[ci]))
        # theta identity against the independent ideal enumeration: c(g n) = sum_cl F(cl) I(cl, n), all n <= nmax coprime to 70
        resid = 0.0
        for n in range(1, nmax+1):
            if math.gcd(n, 70) != 1: continue
            pred = sum(F[R.idx[x]]*k for x, k in CNT[n].items())
            resid = max(resid, abs(pred - coef.get(g*n, 0)))
        Fs = (F + F[sig])/2
        Fh = X.conj() @ Fs / NC
        eis = sum(abs(Fh[i])**2 for i in range(NC) if info[i]['inv'])
        cusp = sum(abs(Fh[i])**2 for i in range(NC) if not info[i]['inv'] and info[i]['type'][0] == info[i]['type'][1])
        mix = sum(abs(Fh[i])**2 for i in range(NC) if not info[i]['inv'] and info[i]['type'][0] != info[i]['type'][1])
        rec[sgn] = dict(g=g, spread=spread, resid=resid, eis=eis, cusp=cusp, mixed=mix, nhit=int(seen.sum()))
        Fs_all[(idx, sgn)] = Fs; Fraw_all[(idx, sgn)] = F
    res[idx] = rec
    if idx % 20 == 0: print(idx, {k: (v and {kk: (round(vv, 4) if isinstance(vv, float) and kk in ('eis','cusp') else vv) for kk, vv in v.items()}) for k, v in rec.items()}, f"{time.time()-t0:.0f}s", flush=True)
pickle.dump(dict(res=res, Fs=Fs_all, F=Fraw_all, info=info, elems=E, chars=CH), open('part1.pkl', 'wb'))
print("done", time.time()-t0)
