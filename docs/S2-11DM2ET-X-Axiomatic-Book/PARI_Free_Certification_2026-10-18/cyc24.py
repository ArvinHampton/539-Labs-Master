# exact arithmetic in Q(zeta24): elements = length-8 Fraction vectors in the basis 1, z, ..., z^7, z^8 = z^4 - 1 (Phi24 = x^8 - x^4 + 1)
from fractions import Fraction as Fr
def red(c):
    c = list(c)
    for d in range(len(c)-1, 7, -1):          # z^d = z^(d-4) - z^(d-8)
        v = c[d]; c[d] = 0
        if v: c[d-4] += v; c[d-8] -= v
    return tuple(Fr(x) for x in c[:8])
def zpow(k):
    k %= 24; c = [0]*24; c[k] = 1; return red(c)
def add(a, b): return tuple(x+y for x, y in zip(a, b))
def scal(s, a): return tuple(s*x for x in a)
def mul(a, b):
    c = [Fr(0)]*15
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): c[i+j] += x*y
    return red(c)
ZERO = tuple([Fr(0)]*8); ONE = zpow(0)
I = zpow(6); SQRT3 = add(zpow(2), zpow(22))      # sqrt3 = zeta12 + zeta12^-1
def const(q): return scal(Fr(q), ONE)
def to_complex(a):
    import cmath, math
    return sum(float(x)*cmath.exp(2j*math.pi*k/24) for k, x in enumerate(a))
def in_Z_zeta12(a): return all(x.denominator == 1 for x in a) and all(x == 0 for x in a[1::2])
def fmt(a):
    """write a in the Z-basis 1, zeta12, zeta12^2, zeta12^3 (zeta12 = z^2) when possible"""
    if all(x == 0 for x in a[1::2]):
        return " + ".join(f"({a[2*k]})*z12^{k}" for k in range(4) if a[2*k] != 0) or "0"
    return " + ".join(f"({x})*z24^{k}" for k, x in enumerate(a) if x != 0)
