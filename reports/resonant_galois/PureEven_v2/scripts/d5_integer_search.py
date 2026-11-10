"""(a) Search lambda=p/q (|p|,q <= H) for D5/reducible fibres with INTEGER m on the three slices (m = k^2 M(lambda)).
   (b) Extended integer scan 1<=m<=5000: irreducible? sextic resolvent rational root?  (even + irreducible + no rational root => A5)."""
import os, sys
os.environ["OMP_NUM_THREADS"] = "1"
from fractions import Fraction as Fr
from math import gcd
from common import *
from galois_tools import is_irreducible, resolvent_rational_root
os.nice(10)
H = 1200
found = {}
for q in range(1, H+1):
    for p in range(-H, H+1):
        if gcd(p, abs(q)) != 1 and not (p == 0 and q == 1): continue
        Dn = 512*q*q*(p+q)**2*(p*p+2*p*q+5*q*q)
        if Dn == 0: continue
        Nn = -(p**3-15*p*p*q-25*p*q*q-25*q**3)*(p**3+5*p*p*q+25*p*q*q+25*q**3)
        Mv = Fr(Nn, Dn)
        for kv in (Fr(-8,5), Fr(-4), Fr(4,5)):
            mv = kv*kv*Mv
            if mv != 0 and mv.denominator == 1:
                found.setdefault((str(kv), abs(int(mv))), (p, q))
print("(a) integer-m D5/reducible-type fibres found, lambda height <=", H)
for key in sorted(found, key=lambda z: (z[0], z[1])):
    print("   k=%s m=%d  (lambda=%d/%d)" % (key[0], key[1], *found[key]))
print("(b) extended integer scan 1<=m<=5000")
for kv in (Fr(-8,5), Fr(-4), Fr(4,5)):
    nred = nd5 = na5 = 0
    for mm in range(1, 5001):
        a, b = bj(mm, kv); A, B, t = clear_denominators(a, b)
        if not is_irreducible(A, B): nred += 1; continue
        if resolvent_rational_root(A, B): nd5 += 1
        else: na5 += 1
    print(f"   k={kv}: irreducible with no resolvent root (=> A5): {na5}; reducible: {nred}; irreducible with resolvent root (=> D5): {nd5}")
