# Exact table of dim V, dim W, cusp = V - W for s = 5..51 (and 72, 98 where available).
# V: exact rational rank (vrank_*) = upper bound (orbit bound, or half-cone bound n9_halfcone.py at s = 2m^2).
# W: local formula (odd s: 3 prod (p^e+1)/2; even s: W_2(k,u) prod (p^e+1)/2), certified local factors listed per s.
import json, glob, sympy
from n3_vs_uL import W_odd, W_even
V = {}
for f in glob.glob('vrank_*.json') + glob.glob('vrank_*.log'):
    txt = open(f).read()
    try:
        d = json.loads(txt); L = d if isinstance(d, list) else [d]
    except Exception:
        L = []
        for line in txt.splitlines():
            if line.startswith('{') and 'rank_Q' in line: L.append(json.loads(line))
    for x in L:
        if isinstance(x, dict) and 'rank_Q' in x: V[x['s']] = max(V.get(x['s'], 0), x['rank_Q'])
hc = {}
for f in glob.glob('n9_halfcone*.json'):
    for x in json.load(open(f)): hc[x['s']] = x['halfcone_rank_upper']
CERT_ODD = {9, 27, 25, 49}            # certified p^e with e >= 2 (local_weil.json); e = 1 by hand proof
rows = []
for s in sorted(V):
    up = hc.get(s, s*(s-1) if s % 2 else (s//2)*(s//2+1))
    if s % 2:
        W = W_odd(s); loc = {p**e for p, e in sympy.factorint(s*(s-2)).items() if e >= 2}
        Wcert = loc <= CERT_ODD; note = f"odd; e>=2 local factors {sorted(loc)}"
    else:
        W = W_even(s); t = s//2; v = 2*t*(t-1); k = 0
        while v % 2 == 0: v //= 2; k += 1
        loc = {p**e for p, e in sympy.factorint(v).items() if e >= 2}
        Wcert = (k <= 5) and loc <= CERT_ODD; note = f"even; k={k}, u=-{v} mod 8={(-v) % 8}; odd e>=2 factors {sorted(loc)}"
    rows.append(dict(s=s, V_lower_exact=V[s], V_upper=up, V_certified=(V[s] == up), W=W, W_local_certified=Wcert, cusp=V[s]-W if V[s] == up else None, note=note))
    print(rows[-1])
json.dump(rows, open('certified_table.json', 'w'), indent=1)
