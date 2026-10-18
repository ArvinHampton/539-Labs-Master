# mod-l lower bounds (exact lower bounds) for W(A1 (+) C_{2^k}(u)), larger k
import sys, json
from local_weil import two_adic_even_s, module, weil_modl, krylov, find_prime
out = {}
for k in range(2, 10):
    for u in (1, 3, 5, 7):
        cyc, q, b, m = two_adic_even_s(k, u); els, idx = module(cyc, q, b); l = find_prime(m)
        S, T = weil_modl(els, q, b, l, m); out[f'{k},{u}'] = krylov(S, T, idx[(0, 0)], l); print(k, u, out[f'{k},{u}'], flush=True)
json.dump(out, open('lower_2adic.json', 'w'), indent=1)
