# Part (2): PARI-free Shintani values at s = 0.
#  (a) exact partial zeta values zeta(0, c) for every narrow ray class c mod f = (2 sqrt35) oo1 oo2 (Ray(2)) and mod m = p2^3 p5 p7 oo1 oo2 (Ray(3)),
#      binned also by N(a) mod 140 (needed for the genus test and the k=1 twists);
#  (b) validations: sum_c zeta(0,c) = 0 (zeta_K(0)=0), L(0,chi) = 0 unless chi is totally odd, genus characters psi o N against
#      Dirichlet B_1 values;
#  (c) exact L(0, chi) in Q(zeta24) for all 96 characters mod f; the 12 totally odd non-sigma-invariant characters of conductor f
#      against the claimed values.
import numpy as np, math, pickle, sys, itertools, json
from fractions import Fraction as Fr
from collections import defaultdict, Counter
sys.dont_write_bytecode = True
import rc, shintani as sh, cyc24 as Z
def class_table(R):
    n = R.n; tab = {}
    zero = tuple([0]*5)
    shiftN = R.add(R.neg(R.cl(R.i13, 0)), R.cl(zero, 1))     # [a] = [mu] - [p13'] = iota(mu) - iota(13) + [p13]
    TP = np.full(tuple(n), -1, dtype=np.int64); TN = np.full(tuple(n), -1, dtype=np.int64)
    for r in itertools.product(*[range(k) for k in n]):
        TP[r] = R.idx[R.cl(r, 0)]; TN[r] = R.idx[R.add(R.cl(r, 0), shiftN)]
    return TP, TN
def bins(R, Mp, K, exact):
    """Z[(class, N mod K)] = sum over ideals a coprime to 70 in that bin of zeta_cone(0) contributions (exact Fractions or float)"""
    TP, TN = class_table(R); out = defaultdict(Fr) if exact else defaultdict(float); npts = 0
    for (kind, sp) in sh.CONES:
        a, b, T1, T2, Nv = sh.cone_points(kind, sp, Mp)
        u = sh.unit70(a, b); a, b, T1, T2 = a[u], b[u], T1[u], T2[u]; npts += len(a)
        k2, k5, k7 = sh.iota_vec(a, b, R.e2)
        s2 = 0 if sp == '++' else 1
        cls = (TP if kind == 'P' else TN)[k2, k5, k7, 0, s2]
        Nn = np.abs(a*a - 35*b*b); Nn = Nn if kind == 'P' else Nn//13
        key = cls*K + (Nn % K)
        if exact:
            num = (4*T1.astype(object)*T2 + 12*T1.astype(object)**2 + 12*T2.astype(object)**2 - 14*Nv*(T1.astype(object)+T2) + 5*Nv*Nv)
            order = np.argsort(key, kind='stable'); ks = key[order]; nm = num[order]
            starts = np.r_[0, np.nonzero(np.diff(ks))[0]+1]
            sums = np.add.reduceat(nm, starts)
            for kk, s in zip(ks[starts].tolist(), sums.tolist()): out[(kk//K, kk % K)] += Fr(int(s), 4*Nv*Nv)
        else:
            w = sh.kernel_float(T1, T2, Nv)
            acc = np.bincount(key, weights=w, minlength=R.order*K)
            for kk in np.nonzero(acc)[0].tolist(): out[(kk//K, kk % K)] += acc[kk]
    return out, npts
def char_info(R, CH):
    E = R.elems; info = []
    for c in CH:
        on = lambda r: R.chival(c, R.cl(r, 0))
        t = (int(2*on((0,0,0,1,0))) % 2, int(2*on((0,0,0,0,1))) % 2)
        inv = all((R.chival(c, R.sigma(x)) - R.chival(c, x)) % 1 == 0 for x in E)
        if R.e2 == 3: f2 = 0 if on((1,0,0,0,0)) == 0 else (2 if on((2,0,0,0,0)) == 0 else 3)
        else: f2 = 0 if on((1,0,0,0,0)) == 0 else 2
        info.append(dict(type=t, inv=inv, cond=(f2, int(on((0,1,0,0,0)) != 0), int(on((0,0,1,0,0)) != 0))))
    return info
def Lexact(R, CH, zcl):
    out = []
    for c in CH:
        v = Z.ZERO
        for ci, z in zcl.items():
            if z: v = Z.add(v, Z.scal(z, Z.zpow(int(24*R.chival(c, R.elems[ci])))))
        out.append(v)
    return out
if __name__ == '__main__':
    lines = []; P = lambda s: (print(s, flush=True), lines.append(s))
    claimed = {  # Heavy-daily 2026-10-17 claims (PARI lfun), sigma-pairs; conjugates for the others
        'A': Z.add(Z.scal(-1, Z.add(Z.const(6), Z.scal(4, Z.SQRT3))), Z.mul(Z.add(Z.scal(6, Z.SQRT3), Z.const(-4)), Z.I)),
        'B': Z.add(Z.const(-12), Z.scal(4, Z.I)),
        'C': Z.add(Z.add(Z.scal(4, Z.SQRT3), Z.const(-6)), Z.scal(-1, Z.mul(Z.add(Z.const(4), Z.scal(6, Z.SQRT3)), Z.I)))}
    conj = lambda a: Z.red([a[0]] + [0]*15 + [a[k] for k in range(7, 0, -1)] + [0]) if False else None
    def cconj(a):
        c = [Fr(0)]*24
        for k, x in enumerate(a): c[(-k) % 24] += x
        return Z.red(c)
    claimed.update({k+'bar': cconj(v) for k, v in list(claimed.items())})
    res = {}
    for e2, Mp in ((2, 70), (3, 140)):
        R = rc.Ray(e2); CH = R.characters(); info = char_info(R, CH)
        zb, npts = bins(R, Mp, 140, exact=True)
        zcl = defaultdict(Fr)
        for (ci, n), z in zb.items(): zcl[ci] += z
        P(f"\n== modulus {'(2 sqrt35)' if e2 == 2 else 'p2^3 p5 p7'} oo1 oo2: |Cl| = {R.order}, Shintani cones at scale Mp = {Mp}, {npts} lattice points coprime to 70")
        P(f"  sum over classes of zeta(0,c) = {sum(zcl.values())}   (must be 0: zeta_K(0) = 0)")
        P(f"  denominators of zeta(0,c): {sorted(Counter(z.denominator for z in zcl.values()).items())}")
        # is N(a) mod 140 a function of the class?
        nmod = defaultdict(set)
        for (ci, n), z in zb.items(): nmod[ci].add(n)
        P(f"  N(a) mod 140 classes per ray class: max {max(len(s) for s in nmod.values())} residues")
        L = Lexact(R, CH, zcl)
        bad = [k for k, d in enumerate(info) if d['type'] != (1, 1) and L[k] != Z.ZERO]
        P(f"  L(0,chi) = 0 for all {sum(d['type'] != (1,1) for d in info)} characters that are not totally odd: {not bad}")
        sigpair = {k: next(j for j in range(len(CH)) if all((R.chival(CH[j], x) - R.chival(CH[k], R.sigma(x))) % 1 == 0 for x in R.elems)) for k in range(len(CH))}
        P(f"  L(0,chi) = L(0,chi o sigma) for all 96: {all(L[k] == L[sigpair[k]] for k in range(len(CH)))}")
        tgt = [k for k, d in enumerate(info) if d['type'] == (1, 1) and not d['inv'] and d['cond'] == (2, 1, 1)]
        P(f"  totally odd, non-sigma-invariant, conductor p2^2 p5 p7 = (2 sqrt35): {len(tgt)} characters")
        for k in tgt:
            hit = [n for n, v in claimed.items() if v == L[k]]
            P(f"    chi#{k:2d} (order {max(x.denominator for x in CH[k][0]+(CH[k][1],))}): L(0) = {Z.fmt(L[k])} = {Z.to_complex(L[k]):.12f}; in Z[zeta12]: {Z.in_Z_zeta12(L[k])}; equals claimed value {hit}")
        P(f"  multiset of claimed labels hit: {sorted(Counter(n for k in tgt for n, v in claimed.items() if v == L[k]).items())}")
        others = [(k, info[k]['cond'], info[k]['inv']) for k in range(len(CH)) if info[k]['type'] == (1, 1) and k not in tgt]
        P(f"  other totally odd characters (imprimitive / sigma-invariant), L_f(0): " + "; ".join(f"#{k} cond{c} inv={i}: {Z.to_complex(L[k]):.6f}" for k, c, i in others))
        # genus characters psi o N, psi mod 20
        def kron140(n):
            if n % 2 == 0 or n % 5 == 0 or n % 7 == 0: return 0
            a, m, t = 35 % n, n, 1        # Jacobi (35/n)
            while a:
                while a % 2 == 0:
                    a //= 2
                    if m % 8 in (3, 5): t = -t
                a, m = m, a
                if a % 4 == 3 and m % 4 == 3: t = -t
                a %= m
            return t if m == 1 else 0
        units20 = [a for a in range(20) if math.gcd(a, 20) == 1]
        gok = []; 
        for l3 in range(2):          # (Z/20)^x = <3> x <-1>... enumerate characters via values on generators 3 (order 4) and 11 (order 2)
            for l4 in range(4):
                psi = {}
                for i in range(4):
                    for j in range(2):
                        psi[(pow(3, i, 20)*pow(11, j, 20)) % 20] = Fr(i*l4, 4) + Fr(j*l3, 2)
                assert len(psi) == 8
                lhs = Z.ZERO
                for (ci, n), z in zb.items():
                    if z: lhs = Z.add(lhs, Z.scal(z, Z.zpow(int(24*psi[n % 20]))))
                L20 = Z.ZERO; L140 = Z.ZERO
                for a in range(1, 21):
                    if a in psi: L20 = Z.add(L20, Z.scal(Fr(-a, 20), Z.zpow(int(24*psi[a]))))
                for a in range(1, 141):
                    kr = kron140(a)
                    if kr: L140 = Z.add(L140, Z.scal(Fr(-a*kr, 140), Z.zpow(int(24*psi[a % 20]))))
                if l3 == 0 and l4 == 0: L20 = Z.ZERO      # trivial psi: zeta(0)-type, both sides 0 (pole-free here since 7-factor kills)
                f7 = Z.add(Z.ONE, Z.scal(-1, Z.zpow(int(24*psi[7]))))
                rhs = Z.mul(f7, Z.mul(L20, L140))
                gok.append((l3, l4, lhs == rhs, Z.to_complex(lhs)))
        P(f"  genus test sum_a psi(Na) |_(s=0) = (1-psi(7)) L_20(0,psi) L_140(0,psi chi_140) for all 8 psi mod 20: {all(g[2] for g in gok)}; values " + ", ".join(f"{g[3]:.4f}" for g in gok))
        res[e2] = dict(zb=dict(zb), zcl=dict(zcl), L=L, info=info, tgt=tgt, sigpair=sigpair)
    # consistency of the two independent runs: characters of conductor f via Ray(3) (Mp=140) vs Ray(2) (Mp=70)
    s2 = Counter(tuple(res[2]['L'][k]) for k in res[2]['tgt']); s3 = Counter(tuple(res[3]['L'][k]) for k in res[3]['tgt'])
    P(f"\nRay(3)/Mp=140 and Ray(2)/Mp=70 give the same multiset of the 12 L(0) values: {s2 == s3}")
    pickle.dump(res, open('part2.pkl', 'wb'))
    open('part2.txt', 'w').write("\n".join(lines)+"\n")
