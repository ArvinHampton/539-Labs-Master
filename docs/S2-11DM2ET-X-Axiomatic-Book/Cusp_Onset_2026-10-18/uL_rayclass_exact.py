# Path A (cusp onset), exact ray-class genus test for u_L, all s (PARI; no prime-periodicity statistics).
# E_L = sum over nu in F=[e1, gamma e1) cap (a+Z^2) of q^{Q(nu)}; ideal a(nu) = (beta(X))/d', X = d nu, d = 2(s-2),
#   beta(X) = (2X1+sX2) + c X2 sqrt(D0),  s^2-2s = c^2 D0,  N(beta) = 4 Q2(X).
# Modulus m = M*oo1*oo2. Write a(nu) = cpart * a' with a' coprime to M; f_c(g) = #{nu : cpart = c, [a'] = g in G = Cl_m^+}.
# (1) union-of-classes check: for every n <= Nmax: #{nu: N a = n} == mu * sum_{(c,g) hit} #{b in g : N b = n/Nc}.
# (2) genus test: u_L Eisenstein <=> for every c, f~_c = f_c + f_c o sigma is constant on cosets of K_N = ker(N: G -> (Z/M)^x).
#     Pure (Maass, infinity types (0,0),(1,1)) part: f_c + f_c(j.) with j = [(M-1)]; mixed part: f_c - f_c(j.).
# (3) character content by FFT on G: non-genus pure characters chi with |f^_c(chi) + f^_c(chi o sigma)| > tol, per c.
import cypari2, numpy as np, math, sys, json, itertools
from fractions import Fraction as Fr
from collections import Counter, defaultdict
pari = cypari2.Pari(); pari.allocatemem(6*10**9)
def sqfree(n):
    f = pari.factor(n); D0, c = 1, 1
    for p, e in zip(f[0], f[1]):
        p, e = int(p), int(e); D0 *= p**(e % 2); c *= p**(e//2)
    return D0, c
def run(s, Mmult=1, Nmax=6000, verbose=True):
    D2 = s*s - 2*s; D0, c = sqfree(D2); d = 2*(s-2)
    K = pari(f'bnfinit(x^2-{D0},1)'); w = pari(f'Mod(x,x^2-{D0})')
    beta = lambda X1, X2: (2*X1 + s*X2) + c*X2*w
    X0 = (s, -2)                                   # d*a, a = (s/(2(s-2)), -1/(s-2))
    Dp = pari.idealhnf(K, beta(*X0))
    for gg in (beta(d, 0), beta(0, d)): Dp = pari.idealadd(K, Dp, gg)
    NDp = int(pari.idealnorm(K, Dp))
    M = 2*d*c*Mmult
    bnr = pari.bnrinit(K, pari(f'[{M},[1,1]]'), 1)
    cyc = [int(z) for z in pari('(b)->b.cyc')(bnr)]; G = int(np.prod(cyc)) if cyc else 1
    gens = pari('(b)->b.gen')(bnr)
    mprimes = [int(p) for p in pari.factor(M)[0]]
    cls = lambda I: tuple(int(z) for z in pari.bnrisprincipal(bnr, I, 0))
    sig = pari.nfgaloisconj(K)[1] if str(pari.nfgaloisconj(K)[0]) == 'x' else pari.nfgaloisconj(K)[0]
    Sigma = np.array([list(cls(pari.nfgaloisapply(K, sig, gens[i]))) for i in range(len(cyc))], dtype=np.int64)  # row i = sigma(gen_i)
    Nm = [int(pari.idealnorm(K, gens[i])) % M for i in range(len(cyc))]
    jv = np.array(cls(pari(M-1)), dtype=np.int64)
    # enumerate nu in F
    gr = (-1, 2)
    Qmax = Fr(Nmax*NDp, 4*d*d); B = int(6*math.sqrt(float(Qmax))) + 10
    pp = pari('(P)->P.p'); pg = pari('(P)->P.gen[2]')
    f = defaultdict(Counter); cnt_nu = Counter(); mult = Counter()
    for n in range(-B, B+1):
        for k in range(0, B+1):
            X1 = d*n + X0[0]; X2 = d*k + X0[1]
            if not ((X1*gr[1] - X2*gr[0]) > 0 and X2 >= 0): continue
            Q = Fr(X1*X1 + s*X1*X2, d*d) + Fr(s*X2*X2, 2*d*d)
            if Q > Qmax: continue
            assert abs(n) < B-2 and k < B-2
            A = pari.idealdiv(K, beta(X1, X2), Dp); nA = int(pari.idealnorm(K, A))
            assert Fr(nA) == 4*d*d*Q/NDp
            cnt_nu[nA] += 1; mult[str(pari.idealhnf(K, A))] += 1
            fa = pari.idealfactor(K, A); cp = []; Ap = A
            for i in range(len(fa[0])):
                P = fa[0][i]; e = int(fa[1][i])
                if int(pp(P)) in mprimes:
                    cp.append((int(pp(P)), str(pg(P)), e)); Ap = pari.idealdiv(K, Ap, pari.idealpow(K, P, e))
            f[tuple(sorted(cp))][cls(Ap)] += 1
    mu = max(Counter(mult.values()))
    # (1) union-of-classes check on n <= Nmax
    L = pari.ideallist(K, Nmax); byclass = defaultdict(Counter)
    for nn in range(1, Nmax+1):
        if any(nn % p == 0 for p in mprimes): continue
        for J in L[nn-1]: byclass[cls(J)][nn] += 1
    def Nc(cp):
        r = 1
        for p, gs, e in cp:
            P = [Pp for Pp in pari.idealprimedec(K, p) if str(pg(Pp)) == gs][0]; r *= int(pari.idealnorm(K, P))**e
        return r
    pred = Counter()
    for cp, fc in f.items():
        nc = Nc(cp)
        for g in fc:
            for nn, v in byclass[g].items():
                if nn*nc <= Nmax: pred[nn*nc] += v*mu
    dev = max(abs(pred[n] - cnt_nu[n]) for n in range(1, Nmax+1))
    # norm image / kernel size
    img = {1}; frontier = [1]
    while frontier:
        new = []
        for x in frontier:
            for gN in Nm:
                y = x*gN % M
                if y not in img: img.add(y); new.append(y)
        frontier = new
    KN = G // len(img)
    # (2)+(3) per c-part
    shape = tuple(cyc); res_c = []
    idx = np.indices(shape).reshape(len(cyc), -1).T          # all elements of G
    normval = np.ones(len(idx), dtype=object)
    lognorm = np.array([pow(1, 1, M)]*len(idx), dtype=object)
    # norm of element g = prod Nm_i^{g_i} mod M
    nv = np.array([int(np.prod([pow(Nm[i], int(g[i]), M) for i in range(len(cyc))]) % M) for g in idx], dtype=np.int64) if G <= 400000 else None
    sig_idx = (idx @ Sigma) % np.array(cyc)
    flat = lambda arr: np.ravel_multi_index(arr.T, shape)
    sig_perm = flat(sig_idx); j_perm = flat((idx + jv) % np.array(cyc))
    # character grid: chi_k(g) = e(sum k_i g_i / cyc_i); chi o sigma has k' with k'_i = sum_l Sigma[i,l] k_l cyc_i/cyc_l
    kidx = idx
    chi_j = np.exp(2j*np.pi*(kidx*jv/np.array(cyc)).sum(1))
    pure = np.abs(chi_j - 1) < 1e-8
    # genus characters = trivial on K_N <=> chi factors through norm: test chi constant on norm fibres -> use: chi trivial on K_N
    # genus characters = sigma-invariant characters = characters trivial on H = (1-sigma)G  (Tate: ker N = C_K^{1-sigma} for cyclic K/Q)
    cycv = np.array(cyc)
    Hgen = [(np.eye(len(cyc), dtype=np.int64)[i] - Sigma[i]) % cycv for i in range(len(cyc))]
    ph = np.stack([(kidx * h / cycv).sum(1) for h in Hgen], 1)
    genus = np.all(np.abs(np.exp(2j*np.pi*ph) - 1) < 1e-8, axis=1)
    Hperms = [flat((idx + h) % cycv) for h in Hgen]
    Hset = {tuple([0]*len(cyc))}; fr = list(Hset)
    while fr:
        nw = []
        for x in fr:
            for h in Hgen:
                y = tuple((np.array(x) + h) % cycv)
                if y not in Hset: Hset.add(y); nw.append(y)
        fr = nw
    Hsize = len(Hset)
    for cp, fc in sorted(f.items(), key=lambda kv: Nc(kv[0])):
        arr = np.zeros(G); 
        for g, v in fc.items(): arr[np.ravel_multi_index(g, shape)] = 1.0   # indicator of hit class set T_c (union-of-classes verified by count check)
        ft = arr + arr[sig_perm]                       # f~ = f + f o sigma   (as function: f~(g) = f(g) + f(sigma g))
        fpure = ft + ft[j_perm]; fmixed = ft - ft[j_perm]
        out = {'c': cp, 'Nc': Nc(cp), 'n_classes': len(fc), 'min_hits_per_class': min(fc.values())}
        if nv is not None:
            def is_genus(h):     # H-invariance
                return all(np.abs(h[pm] - h).max() < 1e-9 for pm in Hperms)
            out['genus_full'] = is_genus(ft); out['genus_pure'] = is_genus(fpure); out['genus_mixed'] = is_genus(fmixed)
            fh = np.fft.fftn(fpure.reshape(shape)).ravel()   # sum_g f(g) e(-k.g/cyc) = content on chi_k (up to conj)
            tol = 1e-7*max(1, np.abs(fh).max())
            nz = (np.abs(fh) > tol)
            out['nongenus_pure_chars'] = int((nz & pure & ~genus).sum())
            out['genus_pure_chars'] = int((nz & pure & genus).sum())
            fhm = np.fft.fftn(fmixed.reshape(shape)).ravel(); tolm = 1e-7*max(1, np.abs(fhm).max())
            out['nongenus_mixed_chars'] = int(((np.abs(fhm) > tolm) & ~pure & ~genus).sum())
            # conductor norms of non-genus pure chars present: report orders
            sel = np.nonzero(nz & pure & ~genus)[0]
            orders = Counter(int(np.lcm.reduce([cyc[i]//math.gcd(cyc[i], int(k[i])) for i in range(len(cyc))])) for k in kidx[sel])
            out['nongenus_pure_char_orders'] = dict(orders)
        nc_ = Nc(cp); obs = sum(1 for g, cn in byclass.items() if any(nn <= Nmax//nc_ for nn in cn))
        out['observable_classes'] = obs; out['complete'] = (obs == G)
        res_c.append(out)
    info = dict(s=s, D0=D0, c=c, M=M, cyc=cyc, G=G, normimage=len(img), K_N=KN, H=Hsize, mu=mu, Nmax=Nmax, count_check_maxdiff=dev,
                n_nu=sum(cnt_nu.values()), cparts=res_c)
    comp = [o for o in res_c if o['complete']]
    if any(not o.get('genus_pure', True) for o in comp): info['uL_verdict'] = 'CUSP'
    elif len(comp) == len(res_c): info['uL_verdict'] = 'Eis (all c-parts seen complete)'
    else: info['uL_verdict'] = 'Eis on complete c-parts; %d incomplete' % (len(res_c) - len(comp))
    info['uL_nongenus_pure_chars_complete'] = sum(o.get('nongenus_pure_chars', 0) for o in comp)
    if verbose: print(json.dumps(info, default=str), flush=True)
    return info
if __name__ == "__main__":
    SS = [int(z) for z in sys.argv[1].split(',')]; Mm = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    Nmax = int(sys.argv[3]) if len(sys.argv) > 3 else 6000
    allr = [run(s, Mm, Nmax) for s in SS]
    json.dump(allr, open(f"uL_rayclass_{'_'.join(map(str, SS))}_M{Mm}.json", 'w'), default=str, indent=1)
