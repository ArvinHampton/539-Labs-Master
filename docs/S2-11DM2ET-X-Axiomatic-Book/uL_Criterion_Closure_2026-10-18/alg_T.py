# Exact, bound-free computation of the c-part class sets T_c of u_L (no enumeration bound B).
# Facts used (proved in the report, Section 3):
#  (i)  admissible beta = beta(X), X in X0 + dZ^2, are exactly B = beta0 + L, L = Z*2d + Z*d(s+c sqrt D0), beta >> 0 in the cone F
#       (every element of B with positive norm is a unit multiple eps^k of exactly one cone element);
#  (ii) M*O_K is contained in L, and for c-part c with I = D'*c the class of (beta)/I in G = Cl^+_{M oo1 oo2}
#       depends only on beta mod N = M*I (beta exact valuation v_P(I) at P | M) and on the signs (beta >> 0).
# So T_c = { cls((beta)/I) : beta in (beta0 + L)/N, v_P(beta) = v_P(I) for all P | M }, lifted to beta >> 0 by adding k*M*N(I).
import cypari2, numpy as np, math, sys, json, itertools
pari = cypari2.Pari(); pari.allocatemem(4*10**9)
from uL_rayclass_exact import sqfree
def setup(s):
    D2 = s*s - 2*s; D0, c = sqfree(D2); d = 2*(s-2)
    K = pari(f'bnfinit(x^2-{D0},1)'); w = pari(f'Mod(x,x^2-{D0})')
    beta = lambda X1, X2: (2*X1 + s*X2) + c*X2*w
    X0 = (s, -2); b0 = beta(*X0); l1 = beta(d, 0); l2 = beta(0, d)
    Dp = pari.idealadd(K, pari.idealadd(K, pari.idealhnf(K, b0), l1), l2)
    M = 2*d*c
    bnr = pari.bnrinit(K, pari(f'[{M},[1,1]]'), 1)
    cyc = [int(z) for z in pari('(b)->b.cyc')(bnr)]; gens = pari('(b)->b.gen')(bnr)
    cls = lambda I: tuple(int(z) for z in pari.bnrisprincipal(bnr, I, 0))
    sig = [z for z in pari.nfgaloisconj(K) if str(z) != 'x'][0]
    Sigma = np.array([list(cls(pari.nfgaloisapply(K, sig, gens[i]))) for i in range(len(cyc))], dtype=np.int64)
    jv = np.array(cls(pari(M-1)), dtype=np.int64)
    mprimes = [int(p) for p in pari.factor(M)[0]]
    Ps = [P for p in mprimes for P in pari.idealprimedec(K, p)]
    key = lambda P: (int(pari('(P)->P.p')(P)), str(pari('(P)->P.gen[2]')(P)))
    tob = lambda a: [int(z) for z in pari.nfalgtobasis(K, a)]
    Lmat = np.array([tob(l1), tob(l2)], dtype=object).T          # columns = l1, l2 in zk coords
    return dict(s=s, D0=D0, c=c, d=d, K=K, w=w, beta=beta, b0=b0, l1=l1, l2=l2, Dp=Dp, M=M, bnr=bnr, cyc=cyc, cls=cls,
                Sigma=Sigma, jv=jv, mprimes=mprimes, Ps=Ps, key=key, tob=tob, Lmat=Lmat, sig=sig, G=int(np.prod(cyc)))
def ideal_of(E, expo):
    K = E['K']; I = E['Dp']
    for P in E['Ps']:
        e = expo.get(E['key'](P), 0)
        if e: I = pari.idealmul(K, I, pari.idealpow(K, P, e))
    return I
def T_c(E, expo, return_count=False):
    K = E['K']; I = ideal_of(E, expo); M = E['M']
    N = pari.idealmul(K, pari.idealhnf(K, M), I)
    Nm = np.array([[int(pari.idealhnf(K, N)[i, j]) for j in range(2)] for i in range(2)], dtype=object)
    # coordinates of N's basis in the L basis (must be integral: N subset M O_K subset L)
    Lm = pari.matrix(2, 2, [int(E['Lmat'][0,0]), int(E['Lmat'][0,1]), int(E['Lmat'][1,0]), int(E['Lmat'][1,1])])
    C = pari.matsolve(Lm, pari.matrix(2, 2, [int(Nm[0,0]), int(Nm[0,1]), int(Nm[1,0]), int(Nm[1,1])]))
    for i in range(2):
        for j in range(2): assert str(pari.type(C[i, j])) == 't_INT', 'N not in L'
    H = pari.mathnf(C); a, t, b = int(H[0, 0]), int(H[0, 1]), int(H[1, 1])   # columns (a,0),(t,b)
    vI = [int(pari.idealval(K, I, P)) for P in E['Ps']]
    nI = int(pari.idealnorm(K, I)); n = M*nI
    T = set(); cnt = 0
    for y in range(b):
        for x in range(a):
            be = E['b0'] + x*E['l1'] + y*E['l2']
            if any(int(pari.nfeltval(K, be, P)) != v for P, v in zip(E['Ps'], vI)): continue
            cnt += 1
            emb = [abs(float(z)) for z in pari.nfeltembed(K, be)]
            k = int(max(emb)/n) + 2
            bp = be + k*n
            T.add(E['cls'](pari.idealdiv(K, bp, I)))
    return (T, cnt, a*b) if return_count else T
def closure(gens, cycv):
    r = len(cycv); Sg = {tuple([0]*r)}; fr = list(Sg)
    while fr:
        nw = []
        for xx in fr:
            for h in gens:
                y = tuple(((np.array(xx) + np.array(h)) % cycv).tolist())
                if y not in Sg: Sg.add(y); nw.append(y)
        fr = nw
    return Sg
def stab(T, cycv):
    T = set(T); t0 = np.array(next(iter(T)))
    return {tuple(((np.array(tt) - t0) % cycv).tolist()) for tt in T
            if all(tuple(((np.array(u) + np.array(tt) - t0) % cycv).tolist()) in T for u in T)}
def Hgens(E):
    cycv = np.array(E['cyc']); r = len(cycv)
    return [tuple(((np.eye(r, dtype=np.int64)[i] - E['Sigma'][i]) % cycv).tolist()) for i in range(r)]
def genus_pure(E, T):
    cyc = E['cyc']; cycv = np.array(cyc); shape = tuple(cyc); G = E['G']
    idx = np.indices(shape).reshape(len(cyc), -1).T
    flat = lambda arr: np.ravel_multi_index(arr.T, shape)
    sig_perm = flat((idx @ E['Sigma']) % cycv); j_perm = flat((idx + E['jv']) % cycv)
    Hperms = [flat((idx + np.array(h)) % cycv) for h in Hgens(E)]
    arr = np.zeros(G, dtype=np.int64)
    for g in T: arr[np.ravel_multi_index(g, shape)] = 1
    ft = arr + arr[sig_perm]; fpure = ft + ft[j_perm]
    return bool(all((fpure[pm] == fpure).all() for pm in Hperms))
def crit(E, T0):
    cycv = np.array(E['cyc']); S = stab(T0, cycv)
    SJ = closure(list(S) + [tuple((E['jv'] % cycv).tolist())], cycv)
    HSJ = closure(list(SJ) + Hgens(E), cycv)
    t0 = np.array(next(iter(T0))); xv = tuple((((t0 @ E['Sigma']) - t0) % cycv).tolist())
    return dict(T=len(T0), S=len(S), single_coset=(len(S) == len(T0)), Gbar=E['G']//len(SJ), Hbar=len(HSJ)//len(SJ),
                x_trivial=(xv in SJ)), S, SJ

def _sol_lattice(E, I, rhs_zero=False):
    """{(x,y) in Z^2 : [b0 +] x l1 + y l2 in I}: returns (particular solution or None, 2x2 kernel basis U) via matsolvemod."""
    K = E['K']; Hm = pari.idealhnf(K, I)
    det = int(pari.matdet(Hm)); adj = pari.matadjoint(Hm)
    c1 = pari.mattranspose(pari.Mat(pari(E['tob'](E['l1'])))); c2 = pari.mattranspose(pari.Mat(pari(E['tob'](E['l2']))))
    A = adj * pari.matconcat([c1, c2])
    v0 = pari.mattranspose(pari.Mat(pari(E['tob'](E['b0'])))) if not rhs_zero else pari.matrix(2, 1, [0, 0])
    b = -(adj * v0)
    sol = pari.matsolvemod(A, pari(f'[{abs(det)},{abs(det)}]~'), pari.matconcat([b])[0] if False else pari(f'[{int(b[0,0])},{int(b[1,0])}]~'), 1)
    if str(sol) == '0': return None, None
    X = (int(sol[0][0]), int(sol[0][1])); U = sol[1]
    U = pari.mathnf(U)   # full-rank 2x2 basis
    return X, U
def T_c_fast(E, expo, return_count=False):
    """Same set as T_c, enumerating only beta in (beta0+L) cap I modulo N = M*I (count [U:U_N], independent of the exponents' size)."""
    K = E['K']; I = ideal_of(E, expo); M = E['M']
    N = pari.idealmul(K, pari.idealhnf(K, M), I)
    X, U = _sol_lattice(E, I)
    if X is None: return (set(), 0, 0) if return_count else set()
    _, UN = _sol_lattice(E, N, rhs_zero=True)
    C = pari.matsolve(U, UN); H = pari.mathnf(C)
    a, t, b = int(H[0, 0]), int(H[0, 1]), int(H[1, 1])
    vI = [int(pari.idealval(K, I, P)) for P in E['Ps']]
    n = M*int(pari.idealnorm(K, I)); T = set(); cnt = 0
    U00, U01, U10, U11 = int(U[0,0]), int(U[0,1]), int(U[1,0]), int(U[1,1])
    for z2 in range(b):
        for z1 in range(a):
            x = X[0] + U00*z1 + U01*z2; y = X[1] + U10*z1 + U11*z2
            be = E['b0'] + x*E['l1'] + y*E['l2']
            if be == 0 or any(int(pari.nfeltval(K, be, P)) != v for P, v in zip(E['Ps'], vI)): continue
            cnt += 1
            emb = [abs(float(zz)) for zz in pari.nfeltembed(K, be)]
            k = int(max(emb)/n) + 2
            T.add(E['cls'](pari.idealdiv(K, be + k*n, I)))
    return (T, cnt, a*b) if return_count else T
