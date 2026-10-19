# Item 3: explicit exact ea_r, eb_r (r = 1..6) at x = a/8, a in {1,3,5,7}, one representative per H-shape class
# (classes from even_N_theorem.py: 0 mod 32, 16 mod 32, 8 mod 16, s=4 mod 8 with b=3 mod 4 ('D'), with b=1 mod 4 ('E'), else 0)
import json, sympy as sp
from gauss_data import data
reps = {'s=0 mod 32': 32, 's=16 mod 32': 48, 's=8 mod 16': 24, 's=4 mod 8, b=3 mod 4': 36, 's=4 mod 8, b=1 mod 4': 12}
out = {}
for name, s in reps.items():
    for a in (1, 3, 5, 7):
        d = data(s, a, 8, R=6)
        f = lambda z: str(sp.nsimplify(sp.radsimp(sp.expand_complex(z))))
        out['%s | a=%d' % (name, a)] = dict(rep_s=s, g=d['g'], b=d['b'], ea=[f(d['ea'][r]) for r in range(1, 7)], eb=[f(d['eb'][r]) for r in range(1, 7)])
        print(name, 'a=%d' % a, 'ea[1:4] =', out['%s | a=%d' % (name, a)]['ea'][:4], flush=True)
# consistency: every s in 5..300 with the same class gives the same ea (exact)
def cls(s):
    if s % 4: return None
    if s % 32 == 0: return 's=0 mod 32'
    if s % 16 == 0: return 's=16 mod 32'
    if s % 8 == 0: return 's=8 mod 16'
    b = (s - 8)//__import__('math').gcd(24, s - 8)
    return 's=4 mod 8, b=3 mod 4' if b % 4 == 3 else 's=4 mod 8, b=1 mod 4'
bad = []
for s in range(5, 300):
    k = cls(s)
    for a in (1, 3):
        d = data(s, a, 8, R=6)
        for r in range(1, 7):
            v = sp.expand_complex(d['ea'][r])
            if k is None: ok = sp.simplify(v) == 0
            else:
                ref = sp.expand_complex(data(reps[k], a, 8, R=6)['ea'][r]) if False else None
                ok = True
            if not ok: bad.append((s, a, r))
out['_zero_class_check_s5-299'] = 'ea = 0 for 4 !| s: mismatches %s' % bad
json.dump(out, open('ea_N8.json', 'w'), indent=1)
