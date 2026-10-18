# Local, class-group-free test of the condition that implies the coset property for EVERY c-part at a given s:
#   for each prime p | M:  R_p = W_p,  where
#   R_p = { beta/beta_1 mod* p^v : beta in beta0 + L, v_P(beta) = v_P(D') for all P | p }   (ratio set of coprime-part residues)
#   W_p = { u in (O/p^v)^x : (u-1)beta0 in L + p^v O and u L in L + p^v O }                (multiplicative stabiliser of beta0+L)
# (v = v_p(M)).  R = W  ==>  T_0 = t0 + psi(W)  ==>  S0 = Stab(T_0) = psi(W)  ==>  every T_c is a union of S0-cosets (report Sec. 4).
import sys, json, itertools
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
from uL_rayclass_exact import sqfree
def run(s):
    D2 = s*s - 2*s; D0, c = sqfree(D2); d = 2*(s-2); M = 2*d*c
    K = pari(f'nfinit(x^2-{D0})'); w = pari(f'Mod(x,x^2-{D0})')
    beta = lambda X1, X2: (2*X1 + s*X2) + c*X2*w
    b0 = beta(s, -2); l1 = beta(d, 0); l2 = beta(0, d)
    Dp = pari.idealadd(K, pari.idealadd(K, pari.idealhnf(K, b0), l1), l2)
    tob = lambda a: [int(z) for z in pari.nfalgtobasis(K, a)]
    sig = [z for z in pari.nfgaloisconj(K) if str(z) != 'x'][0]
    res = dict(s=s, D0=D0, c=c, M=M, primes={})
    for p in [int(q) for q in pari.factor(M)[0]]:
        v = int(pari.valuation(M, p)); q = p**v
        Ps = list(pari.idealprimedec(K, p)); vD = [int(pari.idealval(K, Dp, P)) for P in Ps]
        # N^(p) = q * prod P^{vD}; residues of beta0 + L modulo N^(p)
        Np = pari.idealhnf(K, q)
        for P, e in zip(Ps, vD):
            if e: Np = pari.idealmul(K, Np, pari.idealpow(K, P, e))
        Hm = pari.idealhnf(K, Np)
        # reduce a vector modulo the lattice Hm (upper-triangular HNF, columns basis)
        a00, a01, a11 = int(Hm[0,0]), int(Hm[0,1]), int(Hm[1,1])
        def rd(x0, x1):
            k = x1 // a11; x1 -= k*a11; x0 -= k*a01; x0 %= a00; return (x0, x1)
        g1 = rd(*tob(l1)); g2 = rd(*tob(l2))
        sub = {(0, 0)}; fr = [(0, 0)]
        while fr:
            nw = []
            for z in fr:
                for g in (g1, g2):
                    y = rd(z[0] + g[0], z[1] + g[1])
                    if y not in sub: sub.add(y); nw.append(y)
            fr = nw
        B0 = tob(b0)
        resid = [rd(B0[0] + z[0], B0[1] + z[1]) for z in sub]
        zk1 = pari.nfbasistoalg(K, pari('[0,1]~'))
        elt = lambda t: t[0] + t[1]*zk1
        good = [r for r in resid if r != (0, 0) and all(int(pari.nfeltval(K, elt(r), P)) == e for P, e in zip(Ps, vD))]
        r1 = elt(good[0]); r1s = pari.nfgaloisapply(K, sig, r1); n1 = int(pari.norm(r1)); k = int(pari.valuation(n1, p)); n1p = n1 // p**k
        inv = int(pari.lift(pari.Mod(n1p, q)**-1))
        R = set()
        for r in good:
            num = tob(elt(r)*r1s)
            assert num[0] % p**k == 0 and num[1] % p**k == 0
            R.add(((num[0]//p**k)*inv % q, (num[1]//p**k)*inv % q))
        # W_p
        Lq = pari.mathnf(pari.matconcat([pari.matrix(2, 2, [tob(l1)[0], tob(l2)[0], tob(l1)[1], tob(l2)[1]]), pari.matdiagonal([q, q])]))
        c00, c01, c11 = int(Lq[0,0]), int(Lq[0,1]), int(Lq[1,1])
        def inLq(t):
            x0, x1 = t
            if x1 % c11: return False
            x0 -= (x1 // c11)*c01; return x0 % c00 == 0
        W = set()
        for a0 in range(q):
            for a1 in range(q):
                u = elt((a0, a1))
                if int(pari.norm(u)) % p == 0: continue
                if inLq(tob((u-1)*b0)) and inLq(tob(u*l1)) and inLq(tob(u*l2)): W.add((a0, a1))
        res['primes'][p] = dict(v=v, n_resid=len(resid), n_good=len(good), R=len(R), W=len(W), W_sub_R=W <= R, R_eq_W=(R == W))
    res['all_R_eq_W'] = all(x['R_eq_W'] for x in res['primes'].values())
    return res
if __name__ == "__main__":
    lo, hi = int(sys.argv[1]), int(sys.argv[2]); out = []
    for s in range(lo, hi+1):
        r = run(s); print(json.dumps(r), flush=True); out.append(r)
    json.dump(out, open(f'local_orbit_{lo}_{hi}.json', 'w'), indent=1)
