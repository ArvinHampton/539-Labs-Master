# Is r_K(N) = #{a in K : Na = N} a "genus" (Eisenstein) function h(N mod M) * sum_{d|N} chi_140(d) for ALL N (incl. 7 | N)?
import numpy as np, math
from fractions import Fraction as Fr
from collections import defaultdict
d = np.load('series.npz'); E = d['E']; NMAX = 20*(len(E)-1) - 7
def kron140(n):
    if n % 2 == 0: return 0
    a, m, t = 35 % n, n, 1
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5): t = -t
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3: t = -t
        a %= m
    return t if m == 1 else 0
chi = [kron140(i) for i in range(141)]
sig = np.zeros(NMAX+1, np.int64)
for dd in range(1, NMAX+1):
    c = chi[dd % 140] if dd % 140 else chi[140] if False else kron140(dd % 140) if dd % 140 else 0
    if c: sig[dd::dd] += c
r = np.zeros(NMAX+1, np.int64)
for e in np.nonzero(E)[0]: r[20*e-7] = E[e]
out = []
for M in (280, 560, 1120):
    h = defaultdict(set); bad0 = 0
    for N in range(1, NMAX+1):
        if sig[N] == 0:
            if r[N] != 0: bad0 += 1
            continue
        h[N % M].add(Fr(int(r[N]), int(sig[N])))
    incons = [k for k, v in h.items() if len(v) > 1]
    out.append(f"M={M}: residues with inconsistent ratio r/sigma: {len(incons)}; N with sigma=0 but r != 0: {bad0}; ratio values {sorted(set().union(*h.values()))}")
    if not incons and not bad0:
        hh = {k: next(iter(v)) for k, v in h.items()}
        nz = sorted(k for k, v in hh.items() if v)
        out.append(f"  h = 1/2 exactly on residues {nz[:40]}{'...' if len(nz)>40 else ''} ({len(nz)} residues); h(N)!=0 => N = 13 mod 20: {all(k % 20 == 13 for k in nz)}")
        import pickle; pickle.dump(hh, open(f'genus_h_{M}.pkl', 'wb'))
        break
print("\n".join(out)); open('genus.txt', 'w').write(f"N <= {NMAX}\n" + "\n".join(out) + "\n")
