# A(2)+A(4): exact lower bound for dim V as the RATIONAL rank of an integer matrix (no floating point, no cyclotomics).
#   Delta-picture (odd s: Delta = L0'/L0, L0={n2 even}; even s: Delta = L'/Z^2): v_x(q) = N_O(q)/|O|, O = <gamma,-1>-orbit of x,
#   N_O(q) = #{nu in the four cones +-[e1, g e1), +-[f, g f) : class(nu) in O, Q(nu) = q};  constant column = delta_{O={0}}.
#   rank_Q [N_O(q)] <= dim V <= #orbits (upper bound proved in the report).  Equality certifies dim V exactly.
import numpy as np, math, sys, json, time, flint
from fractions import Fraction as Fr
from family_s import Family
def run(s, Qmax):
    t0 = time.time(); F = Family(s); D = F.D; A = F.A; odd = s % 2 == 1
    mod = (D, 2*D) if odd else (D, D)
    G = np.array([[-1, -s], [2, 2*s-1]])
    if odd: els = sorted({(al[0] % D, (al[1] + eps*D) % (2*D)) for al in F.ALS for eps in (0, 1)})
    else: els = sorted({(al[0] % D, al[1] % D) for al in F.ALS})
    act = lambda g, x: (int((g[0, 0]*x[0] + g[0, 1]*x[1]) % mod[0]), int((g[1, 0]*x[0] + g[1, 1]*x[1]) % mod[1]))
    orb = {}; no = 0
    for x in els:
        if x in orb: continue
        comp = {x, act(-np.eye(2, dtype=int), x), act(G, x), act(-G, x)}
        for y in comp: orb[y] = no
        no += 1
    counts = {}   # (orbit, 2D^2 Q) -> count
    e1 = np.array([1, 0]); f = np.array([1, -1])
    for r1 in (e1, f):
        r2 = G@r1; det = int(r1[0]*r2[1] - r1[1]*r2[0]); sg = 1 if det > 0 else -1
        Q1 = abs(r1@A@r1)/2; Q2 = abs(r2@A@r2)/2; Xm = math.sqrt(Qmax/min(Q1, Q2)) + 1
        corners = np.array([[0, 0], r1*Xm, r2*Xm, (r1+r2)*Xm])
        for al in F.ALS:
            a1, a2 = al
            n = np.arange(math.floor(corners[:, 0].min() - a1/D) - 1, math.ceil(corners[:, 0].max() - a1/D) + 2)
            k = np.arange(math.floor(corners[:, 1].min() - a2/D) - 1, math.ceil(corners[:, 1].max() - a2/D) + 2)
            NN, KK = np.meshgrid(n, k, indexing='ij'); X1 = a1 + D*NN.ravel(); X2 = a2 + D*KK.ravel()
            xs = (X1*r2[1] - X2*r2[0])*sg; ys = (r1[0]*X2 - r1[1]*X1)*sg
            m = (xs > 0) & (ys >= 0); X1, X2 = X1[m], X2[m]
            Qi = 2*X1*X1 + 2*s*X1*X2 + s*X2*X2
            keep = (np.abs(Qi) <= 2*D*D*Qmax) & (Qi != 0); X1, X2, Qi = X1[keep], X2[keep], Qi[keep]
            for sgn in (1, -1):
                for x1, x2, qq in zip(sgn*X1, sgn*X2, Qi):
                    x = (int(x1 % mod[0]), int(x2 % mod[1])); key = (orb[x], int(qq))
                    counts[key] = counts.get(key, 0) + 1
    modes = sorted({k[1] for k in counts}); mi = {q: i for i, q in enumerate(modes)}
    Mx = [[0]*(len(modes)+1) for _ in range(no)]
    for (o, q), c in counts.items(): Mx[o][mi[q]] = c
    Mx[orb[(0, 0)]][-1] = 1
    rk = flint.fmpz_mat(Mx).rank()
    return dict(s=s, Qmax=Qmax, n_orbits=no, n_modes=len(modes), rank_Q=rk, certified_V=(rk == no), time=round(time.time()-t0, 1))
if __name__ == "__main__":
    out = []
    Q = float(sys.argv[2]) if len(sys.argv) > 2 else 40
    for s in [int(z) for z in sys.argv[1].split(',')]:
        r = run(s, Q); print(json.dumps(r), flush=True); out.append(r)
    json.dump(out, open('vrank_%s.json' % sys.argv[1].replace(',', '_'), 'w'), indent=1)
