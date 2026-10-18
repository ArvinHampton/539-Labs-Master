# A(2)+A(4): exact two-sided certification of dim W (and helpers for dim V) for the S/T family of A_s.
#  Lower bounds: ranks over F_l (l prime, l = 1 mod m, zeta_m -> fixed element of order m) of integral vectors in Z[zeta_m];
#     rank over F_l <= rank over Q(zeta_m)  (reduction mod a prime above l is a ring map), so these are exact lower bounds.
#  Upper bounds: W lies in the fixed space of explicit monomial operators U_g (g = k*I, k^2 = 1 mod 2D) that commute
#     with S and T (checked entrywise; all entries are single roots of unity times a common scalar, so a numerical
#     check to 1e-9 is an exact check) and fix c.  dim Fix(G) = (1/|G|) sum_g tr U_g (an integer).
import numpy as np, math, sys, json, time, flint, sympy
from fractions import Fraction as Fr
from family_s import Family
class XF(Family):
    def reduce_fr(self, al, be):
        al = np.array(al); be = np.array(be)
        for b0 in self.BES:
            mu = be - np.array(b0)
            if self.inLp(mu): return self.IDX[(tuple(al % self.D), b0)], self.B(al, mu)
        raise ValueError
    def S_exp(self):
        E = {}
        for i, (al, be) in enumerate(self.LABELS):
            al = np.array(al); be = np.array(be); pre = self.B(al, be)
            for p in self.LP:
                j, ph = self.reduce_fr(p - be, al); assert (i, j) not in E; E[(i, j)] = (pre + ph) % 1
        return E
    def T_exp(self):
        E = {}
        for i, (al, be) in enumerate(self.LABELS):
            al = np.array(al); be = np.array(be)
            j, ph = self.reduce_fr(al, al + be + self.WC); E[i] = (j, (-self.Q(al) - self.B(al, self.WC) + ph) % 1)
        return E
    def U_exp(self, g):   # (al,be) -> (g al, g be) reduced
        perm = np.zeros(self.N, int); ph = []
        for i, (al, be) in enumerate(self.LABELS):
            a2 = (g @ np.array(al)) % self.D
            try: j, f = self.reduce_fr(a2, g @ np.array(be))
            except (ValueError, KeyError): return None
            perm[i] = j; ph.append(f % 1)
        if len(set(perm)) != self.N: return None
        return perm, ph
def find_prime(m, lo=2**40):
    k = lo // m + 1
    while not sympy.isprime(k*m + 1): k += 1
    return k*m + 1
def setup(s):
    F = XF(s); SE = F.S_exp(); TE = F.T_exp()
    m = 1
    for v in list(SE.values()) + [v[1] for v in TE.values()]: m = math.lcm(m, v.denominator)
    return F, SE, TE, m
def modmats(F, SE, TE, m, l):
    g = sympy.primitive_root(l); z = pow(g, (l-1)//m, l)
    zp = lambda fr: pow(z, int(fr*m) % m, l)
    N = F.N; Sm = flint.nmod_mat(N, N, l); Tm = flint.nmod_mat(N, N, l)
    for (i, j), fr in SE.items(): Sm[i, j] = zp(fr)
    for i, (j, fr) in TE.items(): Tm[i, j] = zp(fr)
    return Sm, Tm, zp
def rows_of(M): return [list(r) for r in M.table()]
def krylov_rank(Sm, Tm, v, l):
    N = Sm.nrows(); X = flint.nmod_mat(N, 1, l)
    for i, x in enumerate(v): X[i, 0] = x % l
    while True:
        rows = rows_of(X.transpose()) + rows_of((Sm*X).transpose()) + rows_of((Tm*X).transpose())
        R, rk = flint.nmod_mat(rows, l).rref()
        if rk == X.ncols(): return rk
        X = flint.nmod_mat(rows_of(R)[:rk], l).transpose()
def numeric_U(F, perm, ph):
    U = np.zeros((F.N, F.N), complex); U[perm, np.arange(F.N)] = np.exp(2j*np.pi*np.array([float(x) for x in ph]))
    return U
def symmetry_group(F, S, T, cvec, cands):
    mats = []
    for name, g in cands:
        r = F.U_exp(np.array(g))
        if r is None: continue
        U = numeric_U(F, *r)
        ok = np.abs(U@S - S@U).max() < 1e-9 and np.abs(U@T - T@U).max() < 1e-9
        fixc = np.abs(U@cvec - cvec).max() < 1e-9
        mats.append((name, U, ok, fixc))
    return mats
def closure(gens):
    G = [np.eye(gens[0].shape[0], dtype=complex)]; frontier = list(G)
    while frontier:
        new = []
        for A in frontier:
            for B in gens:
                C = A@B
                if not any(np.abs(C - X).max() < 1e-9 for X in G): G.append(C); new.append(C)
        frontier = new
        if len(G) > 4096: raise RuntimeError('group too big')
    return G
def run(s, l=None):
    t0 = time.time(); F, SE, TE, m = setup(s)
    l = l or find_prime(m); Sm, Tm, zp = modmats(F, SE, TE, m, l)
    cvec = np.zeros(F.N); cvec[[F.IDX[((0, 0), b)] for b in F.BES]] = 1
    W_lo = krylov_rank(Sm, Tm, [int(x) for x in cvec], l)
    S = F.Smatrix(); T = F.Tmatrix()
    D = F.D; cands = []
    for k in range(1, 4*D):
        if math.gcd(k, D) == 1 and (k*k) % (2*D) == 1: cands.append((f'k={k}', [[k, 0], [0, k]]))
    sym = symmetry_group(F, S, T, cvec, cands)
    good = [U for (nm, U, ok, fc) in sym if ok and fc]
    G = closure(good) if good else [np.eye(F.N)]
    Pi = sum(G)/len(G); W_hi = int(round(np.trace(Pi).real))
    out = dict(s=s, N=F.N, m=m, l=l, W_lower_mod_l=W_lo, W_upper_fix_O=W_hi, n_sym_k=len(good), group_order=len(G),
               W_certified=(W_lo == W_hi), time=round(time.time()-t0, 1))
    return out, F, S, T, G
if __name__ == "__main__":
    res = []
    for s in [int(z) for z in sys.argv[1].split(',')]:
        out = run(s)[0]; print(json.dumps(out), flush=True); res.append(out)
    json.dump(res, open(f"cert_W_{sys.argv[1].replace(',', '_')}.json", 'w'), indent=1)
