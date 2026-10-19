# x = 1/4 and 1/6: t^{11/2}, t^{13/2} closed forms = gamma0 A_e(s) + sum eb_r Y_{e,r}(s) + sum ea_r X_{e,r}(s,g)  (P = 8, 12 universal
# pickles, K = 13), with the exact class constants below.  Classes: gamma0, eb depend on s mod 2N; ea on s mod 16 (N=4), 144 (N=6).
import json, sympy as sp, pickle
from gauss_data import data
from hs_coeffs import coeffs
out = {}
for (N, reps) in ((4, range(5, 21)), (6, [s for s in range(5, 149) if s % 16 == 0] + list(range(5, 17)))):
    for s in reps:
        d = data(s, 1, N, R=16)
        f = lambda z: str(sp.nsimplify(sp.radsimp(sp.expand_complex(z))))
        C = coeffs(s, 1, N, 13)
        out['N=%d s=%d' % (N, s)] = dict(gamma0=f(d['gamma0']), eb=[f(d['eb'][r]) for r in range(1, 7)], ea=[f(d['ea'][r]) for r in range(1, 7)],
            c11=str(sp.N(C[11], 25)), c13=str(sp.N(C[13], 25)))
        print(N, s, out['N=%d s=%d' % (N, s)]['c11'], flush=True)
json.dump(out, open('class_data_N4_N6.json', 'w'), indent=1)
