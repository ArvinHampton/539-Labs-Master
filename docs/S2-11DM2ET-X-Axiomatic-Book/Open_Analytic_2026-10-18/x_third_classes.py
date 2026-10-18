# Item (3): classify the x = 1/3 Gauss data.  gamma0, eb depend on s mod 3 only (proved: G(j) is a sum over k mod 6 of e(Q+(j,k)/3)).
# ea depends on H(c) = sum_{y<6} e(Q+(c w + y u2)/3); find the smallest modulus M with ea a function of s mod M (s = 5..240).
import sympy as sp, json
from gauss_data import data
rows = {}
for s in range(5, 241):
    if s == 8 or True:
        d = data(s, 1, 3, R=8)
        key = tuple(sp.nsimplify(sp.expand(d['ea'][r])) for r in range(1, 9))
        rows[s] = dict(g=d['g'], gamma0=sp.nsimplify(d['gamma0']), eb=tuple(sp.nsimplify(d['eb'][r]) for r in range(1, 9)), ea=key)
def func_of(mod, field):
    seen = {}
    for s, r in rows.items():
        k = s % mod
        if k in seen and seen[k] != r[field]: return False
        seen[k] = r[field]
    return True
res = {}
for field in ('gamma0', 'eb', 'ea'):
    for M in (3, 6, 9, 18, 36, 72, 144):
        if func_of(M, field): res[field] = M; break
    else: res[field] = None
print('minimal modulus:', res)
out = {'minimal_modulus': res}
M = res['ea'] or 72
tab = {}
for s, r in rows.items():
    k = s % M
    if k not in tab: tab[k] = dict(example_s=s, ea=[str(sp.simplify(v)) for v in r['ea'][:6]])
out['ea_by_class_mod_%d' % M] = {str(k): tab[k] for k in sorted(tab)}
out['gamma0_eb_by_s_mod_3'] = {str(k): dict(gamma0=str(rows[s]['gamma0']), eb=[str(sp.simplify(v)) for v in rows[s]['eb'][:7]]) for k, s in ((0, 6), (1, 7), (2, 5))}
json.dump(out, open('x_third_classes.json', 'w'), indent=1)
for k in sorted(tab): print(k, tab[k])
print(out['gamma0_eb_by_s_mod_3'])
