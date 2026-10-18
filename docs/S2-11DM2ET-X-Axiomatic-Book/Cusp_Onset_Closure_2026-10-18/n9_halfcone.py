# N9 mechanism test.  At s = 2m^2 the automorph gamma has a rational square root g = (gamma + I)/(2m) in SO(A)(Q)
# (g^T A g = A, g^2 = gamma; g <-> eta = m + sqrt(m^2-1), eps_s = eta^2).  Split each cone [r, gamma r) = [r, g r) u g[r, g r)
# for r = e1, f.  Then each coset theta T_r(x) = sum over Lambda-cosets of half-cone thetas h_r(y), Lambda = Z^2 cap g^{-1}Z^2 = mZ+Z.
# Treating the h_r(y) as formal symbols gives an EXACT upper bound  dim V <= rank(incidence matrix)  (h's need not be independent,
# so this can only over-count).  Combined with the exact rational-rank lower bound (vrank.py) it certifies dim V when they meet.
import sys, json, numpy as np, flint
from fractions import Fraction as Fr
from family_s import Family
def run(s):
    m = int(round((s/2)**0.5)); assert 2*m*m == s
    F = Family(s); D = F.D
    G = np.array([[-1, -s], [2, 2*s-1]])
    els = sorted({(al[0] % D, al[1] % D) for al in F.ALS})
    act = lambda g, x: ((g[0][0]*x[0] + g[0][1]*x[1]) % D, (g[1][0]*x[0] + g[1][1]*x[1]) % D)
    orb = {}; reps = []
    for x in els:
        if x in orb: continue
        comp = {x, act([[-1, 0], [0, -1]], x), act(G.tolist(), x), act((-G).tolist(), x)}
        for y in comp: orb[y] = len(reps)
        reps.append(sorted(comp))
    gin = lambda y: (2*m*y[0] + m*y[1], -y[0]/m)          # g^{-1}
    red = lambda y: (y[0] % m, y[1] % 1)                    # mod Lambda = mZ + Z
    sym = {}
    def col(key):
        if key not in sym: sym[key] = len(sym)
        return sym[key]
    rows = []
    for O in reps:
        row = {}
        for x in O:
            for sg in (1, -1):
                X = (sg*Fr(x[0], D), sg*Fr(x[1], D))
                for r in ('e', 'f'):
                    ys = [red((X[0] + i, X[1])) for i in range(m)]
                    gx = gin(X); ys += [red((gx[0] + 2*m*j, gx[1] - Fr(j, m))) for j in range(m)]
                    for y in ys:
                        c = col((r, y)); row[c] = row.get(c, 0) + 1
        if all(v == 0 for v in O[0]) or O == [(0, 0)]:
            c = col('const'); row[c] = row.get(c, 0) + 1
        rows.append(row)
    M = flint.fmpz_mat(len(rows), len(sym))
    for i, row in enumerate(rows):
        for c, v in row.items(): M[i, c] = v
    rk = M.rank()
    return dict(s=s, m=m, n_orbits=len(reps), n_symbols=len(sym), halfcone_rank_upper=int(rk), predicted_gap=m*(m-1), gap=len(reps)-int(rk))
if __name__ == "__main__":
    out = [run(int(a)) for a in sys.argv[1:]]
    for r in out: print(json.dumps(r), flush=True)
    json.dump(out, open('n9_halfcone_' + '_'.join(sys.argv[1:]) + '.json', 'w'), indent=1)
