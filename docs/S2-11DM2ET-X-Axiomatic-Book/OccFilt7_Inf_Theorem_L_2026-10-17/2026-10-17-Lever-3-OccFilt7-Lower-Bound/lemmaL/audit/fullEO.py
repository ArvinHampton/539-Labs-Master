"""AUDIT (Cat B, long double): E_d, O_d at target d via a_n(m) = sum_i N_n(i) H_n(m-i),
N_n = prod_{odd j<=n}(1+x^j) (built incrementally, positive ops only),
H_n = prod_{k=floor(n/2)+1}^{n} (1-x^{2k})^{-1} (positive cumsums; incremental removal of one factor
per two steps, re-anchored from scratch every ANCH steps; drift measured at each anchor)."""
import numpy as np, math, sys, json
LD = np.longdouble
def div1m(c, a):          # c/(1-x^a), positive
    M = len(c); R = -(-M//a); b = np.zeros(R*a, dtype=LD); b[:M] = c
    return np.cumsum(b.reshape(R, a), axis=0).reshape(-1)[:M].copy()
def mul1m(c, a):          # c*(1-x^a)  (removal of a denominator factor)
    o = c.copy(); o[a:] -= c[:-a]; return o
def mul1p(c, a):
    o = c.copy(); o[a:] += c[:-a]; return o
def H_scratch(n, M):
    h = np.zeros(M, dtype=LD); h[0] = 1
    for k in range(n//2+1, n+1): h = div1m(h, 2*k)
    return h
ds = [int(x) for x in sys.argv[1].split(',')]; ANCH = int(sys.argv[2]) if len(sys.argv) > 2 else 16
NLO = int(sys.argv[4]) if len(sys.argv) > 4 else 0; NHI = int(sys.argv[5]) if len(sys.argv) > 5 else None
M = (max(ds)-NLO*NLO)//7 + 2; N = math.isqrt(max(ds)) if NHI is None else NHI
Nn = np.zeros(M, dtype=LD); Nn[0] = 1; H = np.zeros(M, dtype=LD); H[0] = 1
E = {d: LD(0) for d in ds}; O = {d: LD(0) for d in ds}; terms = {d: {} for d in ds}; drift = []
if NLO > 0:
    for j in range(1, NLO+1, 2): Nn = mul1p(Nn, j)
    H = H_scratch(NLO, M)
for n in range(NLO, N+1):
    if n > NLO:
        if n % 2 == 1: Nn = mul1p(Nn, n)
        if n % ANCH == 0:
            Hs = H_scratch(n, M)
            # incremental H for comparison
            Hi = div1m(H, 2*n) if True else None
            if n % 2 == 0: Hi = mul1m(Hi, n)   # k=n/2 leaves the range when n even
            mask = Hs > 0
            drift.append((n, float(np.max(np.abs(Hi[mask]/Hs[mask]-1)))))
            H = Hs
        else:
            H = div1m(H, 2*n)
            if n % 2 == 0: H = mul1m(H, n)
    for d in ds:
        if n*n <= d and (d-n*n) % 7 == 0:
            m = (d-n*n)//7
            v = np.dot(Nn[:m+1], H[m::-1]) if m > 0 else Nn[0]*H[0]
            terms[d][n] = float(np.log(v)) if v > 0 else None
            if n % 2 == 0: E[d] += v
            else: O[d] += v
    if n % 200 == 0: print('n', n, 'drift', drift[-1:] , flush=True)
out = dict(ds=ds, ratio={d: float(E[d]/O[d]) for d in ds}, logE={d: float(np.log(E[d])) for d in ds},
           logO={d: float(np.log(O[d])) for d in ds}, maxdrift=max(x[1] for x in drift) if drift else None,
           drift=drift, logterms=terms)
for d in ds: print(d, 'E/O =', out['ratio'][d], 'log O =', out['logO'][d])
print('max relative drift of incremental H at anchors:', out['maxdrift'])
json.dump(out, open(sys.argv[3] if len(sys.argv) > 3 else 'fullEO.json', 'w'))
