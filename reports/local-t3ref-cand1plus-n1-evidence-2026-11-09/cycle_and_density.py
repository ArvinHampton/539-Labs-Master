#!/usr/bin/env python3
"""Exact (mpmath, 60 digits) cycle-length lower bound and residue-vector density table for
T(3k)=k, T(3k+1)=4k+2, T(3k+2)=2k+1. Evidence/arithmetic only."""
import mpmath as mp
from math import comb, log
mp.mp.dps = 60
L = mp.log(3)/mp.log(2)
for N in (10**7, 10**10):
    c = -mp.log(1 - mp.mpf(1)/(2*(N+1)))/mp.log(2)
    p = 1
    while True:
        d = abs(p*L - mp.nint(p*L))
        if d <= p*c: break
        p += 1
    print({"N": N, "min_cycle_length_allowed": p, "u": int(mp.nint(p*L)), "dist": mp.nstr(d, 10), "bound": mp.nstr(p*c, 10)})
for j in (10, 20, 40, 80):
    bad = sum(comb(j, c1)*comb(j-c1, c2) for c1 in range(j+1) for c2 in range(j+1-c1)
              if c1*log(4) + c2*log(2) - j*log(3) >= 0)
    print({"j": j, "fraction_of_residue_classes_mod_3^j_with_lambda_ge_1": bad/3**j})
