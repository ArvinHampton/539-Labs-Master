# A(3): deep bad-prime c-parts.  For a c-part  c = prod P^{e_P}  (P | M), enumerate ONLY nu with c | a(nu), i.e.
#   X = d nu in X0 + d Z^2 with beta(X) in c*Dp  (a coset union of a sublattice), up to N(a/c) <= B, so every class of
#   G = Cl^+_M is observable for that c-part (completeness), then test genus-purity (H-invariance of the pure f~_c) exactly
#   as in uL_rayclass_exact.py, and record T_c to test periodicity in the exponents.
import cypari2, numpy as np, math, sys, json, itertools
from fractions import Fraction as Fr
from collections import Counter, defaultdict
pari = cypari2.Pari(); pari.allocatemem(6*10**9)
from uL_rayclass_exact import sqfree
def setup(s, B):
    D2 = s*s - 2*s; D0, c = sqfree(D2); d = 2*(s-2)
    K = pari(f'bnfinit(x^2-{D0},1)'); w = pari(f'Mod(x,x^2-{D0})')
    beta = lambda X1, X2: (2*X1 + s*X2) + c*X2*w
    X0 = (s, -2)
    Dp = pari.idealhnf(K, beta(*X0))
    for gg in (beta(d, 0), beta(0, d)): Dp = pari.idealadd(K, Dp, gg)
    NDp = int(pari.idealnorm(K, Dp)); M = 2*d*c
    bnr = pari.bnrinit(K, pari(f'[{M},[1,1]]'), 1)
    cyc = [int(z) for z in pari('(b)->b.cyc')(bnr)]; G = int(np.prod(cyc)); gens = pari('(b)->b.gen')(bnr)
    cls = lambda I: tuple(int(z) for z in pari.bnrisprincipal(bnr, I, 0))
    sig = [z for z in pari.nfgaloisconj(K) if str(z) != 'x'][0]
    Sigma = np.array([list(cls(pari.nfgaloisapply(K, sig, gens[i]))) for i in range(len(cyc))], dtype=np.int64)
    jv = np.array(cls(pari(M-1)), dtype=np.int64)
    mprimes = [int(p) for p in pari.factor(M)[0]]
    L = pari.ideallist(K, B); byclass = defaultdict(Counter)
    for nn in range(1, B+1):
        if any(nn % p == 0 for p in mprimes): continue
        for J in L[nn-1]: byclass[cls(J)][nn] += 1
    zk = str(pari('(K)->K.zk')(K))
    return dict(s=s, D0=D0, c=c, d=d, K=K, beta=beta, X0=X0, Dp=Dp, NDp=NDp, M=M, cyc=cyc, G=G, cls=cls, Sigma=Sigma, jv=jv,
                mprimes=mprimes, byclass=byclass, zk=zk, B=B)
def coords(E, A0, A1):     # A0 + A1 sqrt(D0) in zk basis
    if E['zk'] == '[1, x]': return A0, A1
    if E['zk'] == '[1, 1/2*x - 1/2]': return A0 + A1, 2*A1
    raise ValueError(E['zk'])
def tests(E, T):
    cyc = E['cyc']; cycv = np.array(cyc); shape = tuple(cyc); G = E['G']
    idx = np.indices(shape).reshape(len(cyc), -1).T
    flat = lambda arr: np.ravel_multi_index(arr.T, shape)
    sig_perm = flat((idx @ E['Sigma']) % cycv); j_perm = flat((idx + E['jv']) % cycv)
    Hgen = [(np.eye(len(cyc), dtype=np.int64)[i] - E['Sigma'][i]) % cycv for i in range(len(cyc))]
    Hperms = [flat((idx + h) % cycv) for h in Hgen]
    arr = np.zeros(G)
    for g in T: arr[np.ravel_multi_index(g, shape)] = 1.0
    ft = arr + arr[sig_perm]; fpure = ft + ft[j_perm]
    return all(np.abs(fpure[pm] - fpure).max() < 1e-9 for pm in Hperms)
def cpart_run(E, expo):
    """expo: dict {(p, gen_str): e} ; returns T_c and checks"""
    K = E['K']; d = E['d']; s = E['s']
    I = E['Dp']; Nc = 1; Pl = []
    for P in sum([list(pari.idealprimedec(K, p)) for p in E['mprimes']], []):
        key = (int(pari('(P)->P.p')(P)), str(pari('(P)->P.gen[2]')(P)))
        e = expo.get(key, 0); Pl.append((P, key, e))
        if e: I = pari.idealmul(K, I, pari.idealpow(K, P, e)); Nc *= int(pari.idealnorm(K, P))**e
    H = [[int(x) for x in row] for row in pari.mattranspose(pari.idealhnf(K, I))]   # rows = basis vectors? use matrix directly
    Hm = np.array([[int(pari.idealhnf(K, I)[i, j]) for j in range(2)] for i in range(2)], dtype=object)
    det = int(Hm[0, 0]*Hm[1, 1] - Hm[0, 1]*Hm[1, 0]); adj = np.array([[Hm[1, 1], -Hm[0, 1]], [-Hm[1, 0], Hm[0, 0]]], dtype=object)
    # solution lattice of  adj(H) (v0 + Phi Y) = 0 mod det :  Y = x + U z   (PARI matsolvemod, flag 1)
    X0 = E['X0']
    v0 = coords(E, 2*X0[0] + s*X0[1], E['c']*X0[1])
    c1 = coords(E, 2*d, 0); c2 = coords(E, s*d, E['c']*d)          # Phi columns: images of Y = e1, e2
    C = [[int(adj[i, 0]*c1[0] + adj[i, 1]*c1[1]), int(adj[i, 0]*c2[0] + adj[i, 1]*c2[1])] for i in range(2)]
    b = [int(-(adj[i, 0]*v0[0] + adj[i, 1]*v0[1])) for i in range(2)]
    sol = pari.matsolvemod(pari.matrix(2, 2, [C[0][0], C[0][1], C[1][0], C[1][1]]), pari(f'[{abs(det)},{abs(det)}]~'), pari(f'[{b[0]},{b[1]}]~'), 1)
    if str(sol) == '0': return dict(expo={f'{k[0]}:{k[1]}': v for k, v in expo.items() if v}, Nc=Nc, n_nu=0, n_classes=0, complete=None, genus_pure=None, T=[])
    x = np.array([int(sol[0][0]), int(sol[0][1])]); U = np.array([[int(sol[1][i, j]) for j in range(2)] for i in range(2)])
    # U columns generate the homogeneous solution lattice (may be non-reduced; bounds below handle it)
    Qmax = Fr(E['B']*Nc*E['NDp'], 4*d*d); Bx = int(6*math.sqrt(float(Qmax))) + 3      # |Y| <= Bx (nu-units)
    Ui = np.linalg.inv(U.astype(float)); corners = np.array([[a, b_] for a in (-Bx, Bx) for b_ in (-Bx, Bx)]) - x
    zc = corners @ Ui.T; zlo = np.floor(zc.min(0)) - 1; zhi = np.ceil(zc.max(0)) + 1
    Z1, Z2 = np.meshgrid(np.arange(zlo[0], zhi[0]+1, dtype=np.int64), np.arange(zlo[1], zhi[1]+1, dtype=np.int64), indexing='ij')
    Yv = x[None, :] + np.stack([Z1.ravel(), Z2.ravel()], 1) @ U.T
    X1 = X0[0] + d*Yv[:, 0]; X2 = X0[1] + d*Yv[:, 1]
    m = ((2*X1 + X2) > 0) & (X2 >= 0); X1, X2 = X1[m], X2[m]
    Q4 = 2*X1*X1 + 2*s*X1*X2 + s*X2*X2
    keep = Q4 <= 2*d*d*Qmax
    T = Counter(); npts = 0
    for x1, x2 in zip(X1[keep], X2[keep]):
        A = pari.idealdiv(K, E['beta'](int(x1), int(x2)), E['Dp'])
        ok = True; Ap = A
        for P, key, e in Pl:
            if int(pari.idealval(K, A, P)) != e: ok = False; break
            if e: Ap = pari.idealdiv(K, Ap, pari.idealpow(K, P, e))
        if not ok: continue
        npts += 1; T[E['cls'](Ap)] += 1
    obs = sum(1 for g, cn in E['byclass'].items() if any(nn <= E['B'] for nn in cn))
    return dict(expo={f'{k[0]}:{k[1]}': v for k, v in expo.items() if v}, Nc=Nc, n_nu=npts, n_classes=len(T), complete=(obs == E['G']),
                genus_pure=(tests(E, T) if T else None), T=sorted(T))
if __name__ == "__main__":
    s = int(sys.argv[1]); B = int(sys.argv[2]); emax = int(sys.argv[3]); p0 = int(sys.argv[4])
    E = setup(s, B)
    Ps = [(int(pari('(P)->P.p')(P)), str(pari('(P)->P.gen[2]')(P))) for P in pari.idealprimedec(E['K'], p0)]
    out = []
    for es in itertools.product(range(emax+1), repeat=len(Ps)):
        expo = dict(zip(Ps, es))
        r = cpart_run(E, expo)
        if r['n_nu'] == 0: continue
        print(json.dumps({k: v for k, v in r.items() if k != 'T'}), flush=True); out.append(r)
    # periodicity: identical T sets across exponent vectors
    groups = defaultdict(list)
    for r in out: groups[tuple(map(tuple, r['T']))].append(r['expo'])
    summ = dict(s=s, B=B, p=p0, G=E['G'], n_cparts=len(out), all_complete=all(r['complete'] for r in out),
                all_genus_pure=all(r['genus_pure'] for r in out), distinct_T_sets=len(groups), T_classes=[v for v in groups.values()])
    print(json.dumps(summ), flush=True)
    json.dump(dict(summary=summ, cparts=out), open(f'deep_cparts_s{s}_p{p0}.json', 'w'), indent=1)
