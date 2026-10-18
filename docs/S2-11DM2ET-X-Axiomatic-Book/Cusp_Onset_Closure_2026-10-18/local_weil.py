# A(2): local cyclic spans W(Delta) = span{rho(g) delta_0} for finite quadratic modules Delta.
#  lower bound: exact rank over F_l (l = 1 mod m) of Krylov vectors;  upper bound: dim Fix(O(Delta)) = #O(Delta)-orbits on Delta
#  (O(Delta) acts by permutations commuting with the Weil representation and fixes delta_0).
import numpy as np, itertools, math, sys, json, flint, sympy
from fractions import Fraction as Fr
def module(cyc, qfun, bfun):
    els = list(itertools.product(*[range(c) for c in cyc])); idx = {e: i for i, e in enumerate(els)}
    return els, idx
def weil_modl(els, q, b, l, m):
    g = sympy.primitive_root(l); z = pow(g, (l-1)//m, l); N = len(els)
    zp = lambda fr: pow(z, int((fr % 1)*m) % m, l)
    S = flint.nmod_mat(N, N, l); T = flint.nmod_mat(N, N, l)
    for i, x in enumerate(els):
        T[i, i] = zp(q(x))
        for j, y in enumerate(els): S[i, j] = zp(-b(x, y))
    return S, T
def rows_of(M): return [list(r) for r in M.table()]
def krylov(S, T, i0, l):
    N = S.nrows(); X = flint.nmod_mat(N, 1, l); X[i0, 0] = 1
    while True:
        rows = rows_of(X.transpose()) + rows_of((S*X).transpose()) + rows_of((T*X).transpose())
        R, rk = flint.nmod_mat(rows, l).rref()
        if rk == X.ncols(): return rk
        X = flint.nmod_mat(rows_of(R)[:rk], l).transpose()
def orbits_O(cyc, els, idx, q, b):
    # brute-force O(Delta): images of the standard generators
    gens = [tuple(1 if j == i else 0 for j in range(len(cyc))) for i in range(len(cyc))]
    add = lambda x, y: tuple((x[i] + y[i]) % cyc[i] for i in range(len(cyc)))
    mul = lambda k, x: tuple((k*x[i]) % cyc[i] for i in range(len(cyc)))
    order = lambda x: next(k for k in range(1, 10**6) if mul(k, x) == tuple(0 for _ in cyc))
    cands = [[y for y in els if order(y) == c and q(y) % 1 == q(gens[i]) % 1] for i, c in enumerate(cyc)]
    autos = []
    for imgs in itertools.product(*cands):
        ok = all((b(imgs[i], imgs[j]) - b(gens[i], gens[j])) % 1 == 0 for i in range(len(cyc)) for j in range(i+1, len(cyc)))
        if not ok: continue
        phi = {}
        for x in els:
            y = tuple(0 for _ in cyc)
            for i in range(len(cyc)): y = add(y, mul(x[i], imgs[i]))
            phi[x] = y
        if len(set(phi.values())) != len(els): continue
        if all((q(phi[x]) - q(x)) % 1 == 0 for x in els): autos.append(phi)
    # orbits
    seen = set(); norb = 0
    for x in els:
        if x in seen: continue
        norb += 1; seen |= {phi[x] for phi in autos}
    return len(autos), norb
def find_prime(m, lo=2**40):
    k = lo // m + 1
    while not sympy.isprime(k*m + 1): k += 1
    return k*m + 1
def cyclic_odd(p, e, u):
    qn = p**e; cyc = [qn]
    q = lambda x: Fr(u*x[0]*x[0], qn); b = lambda x, y: Fr(2*u*x[0]*y[0], qn)
    return cyc, q, b, qn
def two_adic_even_s(k, u):
    # A1 (+) C_{2^k}(u):  q(x0,x1) = x0^2/4 + u x1^2 / 2^{k+1}
    cyc = [2, 2**k]
    q = lambda x: Fr(x[0]*x[0], 4) + Fr(u*x[1]*x[1], 2**(k+1))
    b = lambda x, y: Fr(x[0]*y[0], 2) + Fr(u*x[1]*y[1], 2**k)
    return cyc, q, b, 2**(k+2)
def two_adic_odd_s(eps):
    # A1(eps) (+) A1(eps), eps = +-1 : q = eps(x0^2 + x1^2)/4
    cyc = [2, 2]
    q = lambda x: Fr(eps*(x[0]**2 + x[1]**2), 4); b = lambda x, y: Fr(eps*(x[0]*y[0] + x[1]*y[1]), 2)
    return cyc, q, b, 8
def analyse(cyc, q, b, m):
    els, idx = module(cyc, q, b); l = find_prime(m)
    S, T = weil_modl(els, q, b, l, m); lo = krylov(S, T, idx[tuple(0 for _ in cyc)], l)
    nO, norb = orbits_O(cyc, els, idx, q, b)
    return dict(order=len(els), W_lower=lo, O_size=nO, W_upper_orbits=norb, certified=(lo == norb))
if __name__ == "__main__":
    out = {'odd_s_2adic': {}, 'even_s_2adic': {}, 'odd_prime_powers': {}}
    for eps in (1, -1): out['odd_s_2adic'][eps] = analyse(*two_adic_odd_s(eps)); print('oddS2', eps, out['odd_s_2adic'][eps], flush=True)
    for k in range(2, 7):
        for u in (1, 3, 5, 7):
            r = analyse(*two_adic_even_s(k, u)); out['even_s_2adic'][f'k={k},u={u}'] = r; print('evenS2', k, u, r, flush=True)
    for p, e in [(3, 1), (5, 1), (3, 2), (3, 3), (5, 2), (7, 2), (3, 4), (11, 2), (13, 2), (5, 3)]:
        for u in sorted({1, int(sympy.npartitions(1)) * 0 + next(a for a in range(2, p) if sympy.legendre_symbol(a, p) == -1) if p > 2 else 1}):
            r = analyse(*cyclic_odd(p, e, u)); out['odd_prime_powers'][f'{p}^{e},u={u}'] = dict(r, formula=(p**e+1)//2); print('odd', p, e, u, r, flush=True)
    json.dump(out, open('local_weil.json', 'w'), indent=1, default=str)
