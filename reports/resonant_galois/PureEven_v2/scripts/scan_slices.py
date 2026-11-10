"""Slice scan: for k in {-8/5, -4, 4/5}:
   (i) all integers m with 1 <= m <= 300  (f_m = f_{-m}); (ii) reduced fractions m=p/q, 2<=q<=10, 0<p/q<=10.
For each: clear denominators, test irreducibility, classify Galois group by Frobenius cycle types
(primes 7..4000), cross-check with PARI polgalois, and with the sextic-resolvent rational-root criterion."""
import os, sys, json, math
os.environ["OMP_NUM_THREADS"] = "1"
from fractions import Fraction as Fr
from multiprocessing import Pool
from common import *
from galois_tools import *

SLICES = [Fr(-8, 5), Fr(-4), Fr(4, 5)]
INT_RANGE = range(1, 301)
RAT = sorted({Fr(p, q) for q in range(2, 11) for p in range(1, 10*q+1) if math.gcd(p, q) == 1})

def work(job):
    k, mm = job
    a, b = bj(mm, k)
    A, B, t = clear_denominators(a, b)
    assert is_square_rat(disc_bj(a, b))
    irr = is_irreducible(A, B)
    types, used = cycle_types(A, B) if irr else ({}, 0)
    fro = classify_frobenius(A, B, irr, types)
    pg = pari_group(A, B)
    rr = resolvent_rational_root(A, B) if irr else None
    return dict(k=str(k), m=str(mm), A=str(A), B=str(B), t=t, irr=irr, frob=fro, pari=pg, res_root=rr,
                nprimes=used, types={str(c): n for c, n in types.items()})

if __name__ == "__main__":
    os.nice(10)
    jobs = [(k, Fr(m)) for k in SLICES for m in INT_RANGE] + [(k, m) for k in SLICES for m in RAT]
    with Pool(4) as pool:
        res = pool.map(work, jobs, chunksize=8)
    json.dump(res, open("../data/scan_results.json", "w"))
    print(len(res), "polynomials processed")
