# Item (3): exact ea_r (r = 1..6) and eb_r at x = 1/4 for each nonzero class s mod 16 (from gauss_data.data, exact)
import json, sympy as sp
from gauss_data import data
out = {}
for s in (16, 20, 24, 28, 32, 36, 40, 44):
    d = data(s, 1, 4, R=6)
    out[s] = dict(cls=s % 16, g=d['g'], ea=[str(sp.nsimplify(sp.expand_complex(d['ea'][r]))) for r in range(1, 7)],
                  eb=[str(sp.nsimplify(sp.expand_complex(d['eb'][r]))) for r in range(1, 7)], H=[str(sp.expand_complex(h)) for h in d['H']])
    print(s, out[s]['cls'], out[s]['ea'][:4], '| eb', out[s]['eb'][:4], flush=True)
json.dump(out, open('ea_N4.json', 'w'), indent=1)
