# Independent route to the x = 0 closed forms (incl. t^{9/2}): universal symbolic form (sym_engine, P = 1) with
# gamma0 = 1, eb_r = ea_r = Bt_r(0), compared with H_closed4 (H_em4 route) -- exact symbolic difference and 40-digit values.
import pickle, sympy as sp, math
from sym_engine import s, g
U = pickle.load(open('sym_universal_P1_K9.pkl', 'rb'))
res = pickle.load(open('H_closed4.pkl', 'rb'))
s_, g_ = sp.symbols('s g', positive=True)
Bt = lambda r: sp.Integer(0) if r == 1 else sp.bernoulli(r, 0)
out = []
for e, (A, Yc, Xc) in U.items():
    v1 = A + sum(Bt(k)*Yc[k] for k in Yc) + sum(Bt(k)*Xc[k] for k in Xc)
    if e not in res: continue
    a2, b2 = res[e]
    v2 = (sp.sqrt(2*sp.pi*s_)*(a2 + b2*sp.sqrt((s_ - 2)*(7*s_ - 32)))).subs({s_: s, g_: g})
    nums = []
    for sv in (5, 6, 7, 9, 13, 16, 32, 101):
        gv = math.gcd(24, sv - 8)
        nums.append(abs(sp.N((v1 - v2).subs({s: sv, g: gv}), 40)))
    out.append('t^{%d/2}: max |route1 - route2| over s in {5,6,7,9,13,16,32,101} = %s ; value at s=5: %s' % (e, max(nums), sp.N(v1.subs({s: 5, g: 3}), 20)))
    print(out[-1], flush=True)
open('check_x0_two_routes.txt', 'w').write('\n'.join(out) + '\n')
