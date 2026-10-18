# A(2)/A(4): exact characteristic-0 cyclic span of delta_0 for 2-adic modules Delta_2 = A1 (+) C_{2^k}(u) (even s),
#   computed over Q(zeta_m), m = 2^{k+2}, Phi_m = x^{m/2}+1, by realification: v in Z[zeta]^N -> rows {zeta^j v} in Z^{N*m/2};
#   dim_{Q(zeta)} span = rank_Q / (m/2).  Krylov closure is exact: stops when S v, T v of every basis vector lie in the span.
import numpy as np, sys, json, flint, itertools
from fractions import Fraction as Fr
from local_weil import two_adic_even_s, module
def run(k, u):
    cyc, q, b, m = two_adic_even_s(k, u); els, idx = module(cyc, q, b); N = len(els); h = m//2
    Se = np.array([[int((-b(x, y) % 1)*m) for y in els] for x in els]); Te = np.array([int((q(x) % 1)*m) for x in els])
    def mulz(e, v):   # multiply Z[zeta] element v (length h, negacyclic) by zeta^e
        e %= m; sgn = 1
        if e >= h: e -= h; sgn = -1
        return sgn*np.concatenate([-v[h-e:], v[:h-e]]) if e else sgn*v.copy()
    def applyS(V):
        W = [np.zeros(h, dtype=object) for _ in range(N)]
        for i in range(N):
            acc = np.zeros(h, dtype=object)
            for j in range(N):
                if any(V[j]): acc = acc + mulz(Se[i, j], V[j])
            W[i] = acc
        return W
    def applyT(V): return [mulz(Te[i], V[i]) for i in range(N)]
    def realify(V): return [np.concatenate([mulz(j, V[i]) for i in range(N)]) for j in range(h)]
    def rank(rows): return flint.fmpz_mat([[int(x) for x in r] for r in rows]).rank()
    v0 = [np.zeros(h, dtype=object) for _ in range(N)]; v0[idx[(0, 0)]][0] = 1
    basis = [v0]; rows = realify(v0); r = rank(rows); queue = [v0]
    while queue:
        v = queue.pop(0)
        for w in (applyS(v), applyT(v)):
            g = [int(np.gcd.reduce([int(x) for x in np.concatenate(w)] + [0]))]; gg = max(g[0], 1)
            w = [x//gg for x in w]
            nr = rows + realify(w); r2 = rank(nr)
            if r2 > r: rows, r = nr, r2; basis.append(w); queue.append(w)
    assert r % h == 0
    return dict(k=k, u=u, N=N, dimW_exact=r//h)
if __name__ == "__main__":
    out = []
    for arg in sys.argv[1:]:
        k, u = map(int, arg.split(',')); res = run(k, u); print(json.dumps(res), flush=True); out.append(res)
    json.dump(out, open('exact_local2_%s.json' % '_'.join(a.replace(',', '-') for a in sys.argv[1:]), 'w'), indent=1)
