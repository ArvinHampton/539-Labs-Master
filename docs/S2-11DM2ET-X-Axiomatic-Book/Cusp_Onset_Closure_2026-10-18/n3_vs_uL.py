# Cross-Review N3 vs the u_L-level verdicts: family cusp (V - W, local / Weil parity) against the u_L verdict (class group).
import json, sympy
def W_odd(s):
    w = 3
    for p, e in sympy.factorint(s*(s-2)).items():
        if p != 2: w *= (p**e + 1)//2
    return w
def W_even(s):
    t = s//2; v = 2*t*(t-1); k = 0
    while v % 2 == 0: v //= 2; k += 1
    m = v
    W2 = 2**(k-1) + (4 if k % 2 == 0 else (6 if m % 4 == 1 else 5))
    w = W2
    for p, e in sympy.factorint(m).items(): w *= (p**e + 1)//2
    return w
rows = []
for s in (5, 7, 13, 15, 14, 17, 18, 22, 23, 19, 21, 25, 29, 20, 16, 24):
    r = json.load(open(f'uL_rayclass_{s}_M1.json')); r = r[0] if isinstance(r, list) else r
    V = s*(s-1) if s % 2 else (s//2)*(s//2+1)
    W = W_odd(s) if s % 2 else W_even(s)
    rows.append(dict(s=s, V_orbit_bound=V, W=W, family_cusp_bound=V-W, uL_verdict=r['uL_verdict'], Gbar=r['crit']['Gbar'], Hbar=r['crit']['Hbar'],
                     criterion=r['crit']['criterion_predicts'], M=r['M'], primes_of_s_in_M=[p for p in sympy.primefactors(s) if r['M'] % p == 0]))
    print(rows[-1])
json.dump(rows, open('n3_vs_uL.json', 'w'), indent=1)
