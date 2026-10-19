# Item (1): x = a/p, p >= 5 prime, p | s(s-2)(7s-32)  (degenerate: p | Q2(u2)).  Claimed closed forms (from Lemma R, n = v = 1):
#   p | s       : H(c) = 2p e(a n_w^2 c^2 / p)               for all c       (n_w = -b^{-1} mod p)
#   p | s - 2   : H(c) = 0                                     (u2 isotropic, beta = s b/2 = b != 0 mod p)
#   p | 7s - 32 : H(c) = 2p e(a Q+(c w)/p) [c = c*],  c* = -s b (2 B(w,u2))^{-1} mod p,  B(w,u2)^2 = s(s-2) != 0 mod p
#   ea_r = 2^{1-r} sum_{c<p} H(c) Bt_r(c/p)   (H is p-periodic; distribution relation);  p | 7s-32: ea_r = 2^{2-r} p e(a Q+(c* w)/p) Bt_r(c*/p)
import math, json, sympy as sp
from latt import lat, Qp, Hcounts
def red(v): mn = min(v); return tuple(x - mn for x in v)
res = {}
for p in (5, 7, 11, 13, 17, 19, 23):
    bad = 0; tests = 0; cases = {'s': 0, 's-2': 0, '7s-32': 0}
    for s in range(5, 1200):
        if (s*(s-2)*(7*s-32)) % p: continue
        g, m, b, nw, kw = lat(s)
        Bw = 2*nw*m + s*(nw*b + kw*m) + s*kw*b
        for a in range(1, p):
            H = Hcounts(s, a, p)
            for c in range(2*p):
                v = [0]*p
                if s % p == 0:
                    v[(a*nw*nw*c*c) % p] += 2*p; key = 's'
                elif (s-2) % p == 0: key = 's-2'
                else:
                    key = '7s-32'
                    cs = (-s*b*pow(2*Bw, -1, p)) % p
                    if c % p == cs: v[(a*Qp(s, c*nw, c*kw)) % p] += 2*p
                tests += 1; cases[key] += 1
                if red(v) != red(H[c]): bad += 1
    res[p] = dict(tests=tests, mismatches=bad, cases=cases); print(p, res[p], flush=True)
json.dump(res, open('degenerate_p.json', 'w'), indent=1)
