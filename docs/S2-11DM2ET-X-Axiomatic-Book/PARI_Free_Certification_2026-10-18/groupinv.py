# invariant factors of the PARI-free ray class groups from element-order counts
import sys; sys.dont_write_bytecode = True
from collections import Counter
import rc, itertools
def inv(R):
    def order(x):
        y = x; k = 1
        z = R.cl(tuple([0]*5), 0)
        while y != z: y = R.add(y, x); k += 1
        return k
    return Counter(order(x) for x in R.elems)
def cnt_of(cyc):
    els = itertools.product(*[range(c) for c in cyc])
    from math import gcd
    def o(v):
        l = 1
        for a, c in zip(v, cyc):
            oo = c//gcd(a, c); l = l*oo//gcd(l, oo)
        return l
    return Counter(o(v) for v in els)
out = []
for e2 in (2, 3):
    R = rc.Ray(e2); c = inv(R)
    cands = [cy for cy in ([24, 2, 2], [12, 2, 2, 2], [24, 4], [48, 2], [12, 4, 2], [8, 6, 2], [6, 4, 4], [96], [12, 8]) if cnt_of(cy) == c]
    out.append(f"e2={e2}: order {R.order}, element-order counts {sorted(c.items())}; matches Z/{' x Z/'.join(map(str, cands[0]))}" if cands else f"e2={e2}: {sorted(c.items())} no candidate")
print("\n".join(out)); open('groupinv.txt', 'w').write("\n".join(out)+"\n")
