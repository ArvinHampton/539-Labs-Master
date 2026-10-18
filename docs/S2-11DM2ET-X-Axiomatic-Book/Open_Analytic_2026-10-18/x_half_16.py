# x = 1/2, 16 | s: extract the deviation from the generic even-s polynomial and fit the sqrt(Delta) structure.
import mpmath as mp, json, math, sympy as sp
from asym_engine import expansion
mp.mp.dps = 40
gen = {1: lambda s: -mp.mpf(1)/8, 3: lambda s: mp.mpf(s-4)/64, 5: lambda s: -mp.mpf(31*s*s-168*s+192)/3072}
out = []
import sys
SS = [int(z) for z in sys.argv[1].split(',')] if len(sys.argv) > 1 else [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192]
for s in SS:
    c = expansion(s, 1, 2, 7); r = mp.sqrt(2*mp.pi*s); g = math.gcd(24, s-8); D = (s-2)*(7*s-32)
    row = dict(s=s, g=g)
    for e in (1, 3, 5, 7):
        v = (c[e]/r).real
        row[f'h{e}'] = mp.nstr(v, 30)
        if e in gen: row[f'dev{e}_times_sqrtD'] = mp.nstr((v - gen[e](s))*mp.sqrt(D), 30)
    out.append(row); print(json.dumps(row), flush=True)
json.dump(out, open('x_half_16.json' if len(sys.argv) == 1 else 'x_half_16_more.json', 'w'), indent=1)
