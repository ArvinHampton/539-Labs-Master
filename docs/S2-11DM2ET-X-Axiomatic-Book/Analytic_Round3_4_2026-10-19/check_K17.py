# t^{17/2} at x=0 checks: (a) K17 pickle reproduces K13 run (independent) exactly at e<=13 (values at several s, 60 digits);
# (b) c_17(5) = 0 exactly (H_5 = 0); (c) universal form vs independent engine asym_engine.py at e = 17.
import pickle, sympy as sp, math, json
from sym_engine import s, g
from asym_engine import expansion
Bt0 = lambda r: sp.Integer(0) if r == 1 else sp.bernoulli(r, 0)
U17 = pickle.load(open('sym_universal_P1_K17.pkl', 'rb')); U13 = pickle.load(open('sym_universal_P1_K13.pkl', 'rb'))  # e<=15 entries of K17 are inherited from K15 by construction; compare with the independent K13 run
def val(U, e, sv):
    A, Yc, Xc = U[e]; ex = A + sum(Bt0(k)*Yc[k] for k in Yc) + sum(Bt0(k)*Xc[k] for k in Xc)
    return ex.subs({s: sv, g: math.gcd(24, sv - 8)})
out = {}
out['K17_vs_K13_maxdiff'] = str(max(abs(sp.N(val(U17, e, sv) - val(U13, e, sv), 60)) for e in U13 for sv in (6, 7, 13, 32)))
out['c17(5)'] = str(sp.nsimplify(sp.simplify(val(U17, 17, 5))))
rows = []
for sv in (6, 7, 9):
    eng = expansion(sv, 0, 1, 17); v = complex(sp.N(val(U17, 17, sv), 30))
    rows.append(dict(s=sv, sym=str(v), engine=str(complex(eng[17])), absdiff=abs(v - complex(eng[17])))); print(rows[-1], flush=True)
out['engine'] = rows
print(out); json.dump(out, open('check_K17.json', 'w'), indent=1)
