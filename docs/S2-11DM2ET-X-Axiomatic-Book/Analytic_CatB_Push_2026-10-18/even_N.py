# Item (3): even N.  Exact minimal periods (equality in Z[zeta_L]) of s -> H_{a/N}(.) and of s -> ea_r, and class tables.
import math, json, sympy as sp
from gauss_local import H_brute, Cyc
from latt import lat
def Hkey(s, a, N, C, L): return tuple(C.red(H_brute(s, a, N, c, L)) for c in range(2*N))
out = {}
for N, a in [(2, 1), (4, 1), (4, 3), (6, 1), (8, 1), (8, 3)]:
    L = math.lcm(8, N); C = Cyc(L); Pd = 48*N
    keys = {s: Hkey(s, a, N, C, L) for s in range(5, 5 + 2*Pd)}
    per = min(d for d in range(1, Pd + 1) if Pd % d == 0 and all(keys[s] == keys[s + d] for s in range(5, 5 + Pd)))
    zero = sorted({s % per for s in range(5, 5 + per) if all(all(x == 0 for x in k) for k in keys[s])})
    nonzero = sorted({s % per for s in range(5, 5 + per)} - set(zero))
    out['%d/%d' % (a, N)] = dict(proved_period_bound=Pd, minimal_period=per, H_identically_zero_classes=zero, nonzero_classes=nonzero)
    print(a, N, out['%d/%d' % (a, N)], flush=True)
json.dump(out, open('even_N.json', 'w'), indent=1)
