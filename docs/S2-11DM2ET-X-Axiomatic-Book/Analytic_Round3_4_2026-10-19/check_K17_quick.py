# quick exact parts of the K17 checks: c17(5) = 0 and K17 (e<=13) vs the independent K13 run, 60 digits at s = 6,7,13,32
import pickle, sympy as sp, math, json
from sym_engine import s, g
Bt0 = lambda r: sp.Integer(0) if r == 1 else sp.bernoulli(r, 0)
U17 = pickle.load(open('sym_universal_P1_K17.pkl', 'rb')); U13 = pickle.load(open('sym_universal_P1_K13.pkl', 'rb'))
def val(U, e, sv):
    A, Yc, Xc = U[e]; return (A + sum(Bt0(k)*Yc[k] for k in Yc) + sum(Bt0(k)*Xc[k] for k in Xc)).subs({s: sv, g: math.gcd(24, sv-8)})
o = dict(c17_at_5=str(sp.simplify(val(U17, 17, 5))),
         K17_vs_K13_maxdiff=str(max(abs(sp.N(val(U17, e, sv) - val(U13, e, sv), 60)) for e in U13 for sv in (6, 7, 13, 32))))
print(o); json.dump(o, open('check_K17_quick.json', 'w'))
