# Narrow form class number h+ (primitive forms of discriminant D>0, nonsquare) via cycles of Gauss-reduced forms,
# and #genera = |Cl+/Cl+^2| = |Cl+[2]| (ambiguous classes: cycle closed under (a,b,c)->(c,b,a), the inverse class).
import math, sys
from math import gcd, isqrt
def reduced_forms(D):
    r = math.sqrt(D); out = []
    for b in range(1, isqrt(D)+1):
        if (D - b*b) % 4: continue
        if b*b >= D: continue
        ac = (b*b - D)//4   # a c = (b^2-D)/4 < 0
        for a in range(1, int(r)+2):
            for sa in (a, -a):
                if ac % sa: continue
                c = ac//sa
                if gcd(gcd(abs(sa), b), abs(c)) != 1: continue
                if r - b < 2*abs(sa) < r + b: out.append((sa, b, c))
    return set(out)
def rho(f, D):
    a, b, c = f; r = math.sqrt(D)
    # (a,b,c) -> (c, b', a') with b' = -b mod 2c, sqrt(D)-2|c| < b' < sqrt(D)
    m = 2*abs(c); bp = (-b) % m
    while bp > r: bp -= m
    while bp < r - m: bp += m
    ap = (bp*bp - D)//(4*c)
    return (c, bp, ap)
def classgroup(D):
    R = reduced_forms(D); seen = set(); cycles = []
    for f in sorted(R):
        if f in seen: continue
        cyc = []; g = f
        while g not in cyc:
            cyc.append(g); g = rho(g, D)
        # proper cycle = rho^2 orbit (even steps); narrow classes = rho^2-orbits
        for start in range(min(2, len(cyc))):
            pass
        cycles.append(cyc); seen.update(cyc)
    # narrow classes: rho changes the sign of 'a' alternately; proper equivalence classes = orbits of rho^2
    narrow = []; seen = set()
    for f in sorted(R):
        if f in seen: continue
        orb = []; g = f
        while g not in orb:
            orb.append(g); g = rho(g, D)   # rho is an SL2(Z) step: rho-cycles = proper (narrow) classes
        narrow.append(set(orb)); seen.update(orb)
    amb = sum(1 for C in narrow if any(((c, b, a) in C) for (a, b, c) in C))
    return len(narrow), amb
if __name__ == "__main__":
    for s in [int(x) for x in sys.argv[1].split(',')]:
        D = s*(s-2)
        if D % 4 not in (0, 1): D *= 4
        h, g = classgroup(D)
        print(f"s={s} D={D} h+={h} genera(|Cl+[2]|)={g} |Cl+^2|={h//g}")
