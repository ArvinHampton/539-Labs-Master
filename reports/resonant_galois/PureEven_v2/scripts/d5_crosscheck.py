"""Cross-check: D5 fibres found by the Frobenius/PARI scan == points of the parametrisation m = +-k^2 M(lambda) inside the scanned set."""
import json, math, os
from fractions import Fraction as Fr
H = 600
res = json.load(open("../data/scan_results.json"))
scanned = {(r['k'], r['m']) for r in res}
d5 = {(r['k'], r['m']) for r in res if r['frob'] == 'D5'}
param = {}
for q in range(1, H+1):
    for p in range(-H, H+1):
        if math.gcd(p, q) != 1: continue
        Dn = 512*q*q*(p+q)**2*(p*p+2*p*q+5*q*q)
        Nn = -(p**3-15*p*p*q-25*p*q*q-25*q**3)*(p**3+5*p*p*q+25*p*q*q+25*q**3)
        if Dn == 0: continue
        Mv = abs(Fr(Nn, Dn))
        for kv in (Fr(-8,5), Fr(-4), Fr(4,5)):
            mv = kv*kv*Mv
            key = (str(kv), str(mv))
            if key in scanned: param.setdefault(key, (p, q))
print("scanned points hit by the parametrisation (lambda height <= %d):" % H, sorted(param))
print("scan D5 set:", sorted(d5))
print("EQUAL" if set(param) == d5 else "MISMATCH")
