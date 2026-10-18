# Exact per-s cross-check of the proved c = 1 statements (odd s, s(s-2) squarefree):
#  |Gbar| = h*phi(s-2), |Gbar^sigma| = 2^omega(s)*phi(s-2), x-bar = 0, only the coprime part occurs (every residue has exact valuation),
#  Chevalley-Gras: |Cl^+_{(s-2)oo1oo2}(K)^sigma| = 2^omega(s)*phi(s-2)  (unit-norm index 1),  and 2-rank of Cl(K) = t - 2.
import sys, json, math, numpy as np
from alg_T import *
def fixed_size(E2cyc, Sig):
    cycv = np.array(E2cyc); r = len(cycv)
    H = closure([tuple(((np.eye(r, dtype=np.int64)[i] - Sig[i]) % cycv).tolist()) for i in range(r)], cycv)
    return int(np.prod(cycv))//len(H)
out = []
for s in range(5, int(sys.argv[1]) + 1, 2):
    D = s*(s-2)
    if not pari.issquarefree(D): continue
    E = setup(s); m = s - 2
    T, cnt, tot = T_c(E, {}, True); cr, S, SJ = crit(E, T)
    K = E['K']; h = int(pari('(K)->K.clgp.no')(K)); cl = [int(z) for z in pari('(K)->K.clgp.cyc')(K)]
    two_rank = sum(1 for z in cl if z % 2 == 0); t = len(pari.factor(4*D)[0])
    om = len(pari.factor(s)[0]) if s > 1 else 0; ph = int(pari.eulerphi(m))
    bnr = pari.bnrinit(K, pari(f'[{m},[1,1]]'), 1); cyc = [int(z) for z in pari('(b)->b.cyc')(bnr)]; gens = pari('(b)->b.gen')(bnr)
    Sig = np.array([[int(z) for z in pari.bnrisprincipal(bnr, pari.nfgaloisapply(K, E['sig'], gens[i]), 0)] for i in range(len(cyc))], dtype=np.int64)
    fixm = fixed_size(cyc, Sig)
    rec = dict(s=s, h=h, omega_s=om, phi=ph, t=t, two_rank=two_rank, Gbar=cr['Gbar'], Gbar_sigma=cr['Gbar']//cr['Hbar'], x_trivial=cr['x_trivial'],
               only_coprime=(cnt == tot), chev_fixed=fixm,
               ok=(cr['Gbar'] == h*ph and cr['Gbar']//cr['Hbar'] == 2**om*ph and cr['x_trivial'] and cnt == tot and fixm == 2**om*ph and two_rank == t-2),
               eis=(cr['Hbar'] == 1), eis_pred=(h == 2**om), pure=genus_pure(E, T) if E['G'] <= 300000 else None)
    print(json.dumps(rec), flush=True); out.append(rec)
json.dump(out, open('c1_check.json', 'w'), indent=1)
print('ALL_OK', all(r['ok'] for r in out), 'n', len(out), 'Eis at', [r['s'] for r in out if r['eis']])
