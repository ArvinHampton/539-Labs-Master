# A(1): conductor of the E-class set: smallest rational modulus m' | M (with both infinite places) such that
#   ker(Cl^+_M -> Cl^+_{m'}) = S (the stabiliser of T); then Gbar = Cl^+_{m'} / <j>.  Also tests prime-ideal moduli.
import cypari2, json, sys, numpy as np
pari = cypari2.Pari(); pari.allocatemem(4*10**9)
from uL_rayclass_exact import sqfree
def run(s, fn):
    r = json.load(open(fn))[0]; c = r['crit']
    D2 = s*s - 2*s; D0, cc = sqfree(D2); M = r['M']
    K = pari(f'bnfinit(x^2-{D0},1)')
    bnr = pari.bnrinit(K, pari(f'[{M},[1,1]]'), 1); gens = pari('(b)->b.gen')(bnr); cyc = [int(z) for z in pari('(b)->b.cyc')(bnr)]
    assert cyc == r['cyc']
    S = [np.array(v) for v in c['S_elems']]
    res = []
    for mp in sorted(int(d) for d in pari.divisors(M)):
        b2 = pari.bnrinit(K, pari(f'[{mp},[1,1]]'), 1); cyc2 = [int(z) for z in pari('(b)->b.cyc')(b2)]
        img = np.array([[int(z) for z in pari.bnrisprincipal(b2, gens[i], 0)] for i in range(len(cyc))], dtype=object) if cyc2 else None
        G2 = int(np.prod(cyc2)) if cyc2 else 1
        if G2 * len(S) != r['G']: continue
        if cyc2:
            ok = all(all(int(x) % cc2 == 0 for x, cc2 in zip(np.dot(v, img), cyc2)) for v in S)
        else: ok = True
        if ok: res.append((mp, cyc2)); break
    return dict(s=s, M=M, S_size=len(S), conductor_rational=res[0][0] if res else None, cyc_mE=res[0][1] if res else None, Gbar=c['Gbar'], Hbar=c['Hbar'], hplus=c['hplus'])
if __name__ == "__main__":
    for s in [int(z) for z in sys.argv[1].split(',')]:
        print(json.dumps(run(s, f'uL_rayclass_{s}_M1.json')), flush=True)
