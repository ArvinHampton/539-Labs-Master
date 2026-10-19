# cheap structure of S_e(s,g) at x = 0 (e = 7..17 where available): g-powers present, and for each g-power coefficient
# the factorization of its numerator (exact sympy), plus the S value at s = 5 relation S sqrt(D) = -R.
import pickle, sympy as sp, sys, os
from sym_engine import s, g
files = [(11, 'closed_P1_e11.pkl'), (13, 'closed_P1_e13.pkl'), (15, 'closed_P1_e15_K15.pkl'), (17, 'closed_P1_e17_K17.pkl')]
for e, f in files:
    if not os.path.exists(f): continue
    d = pickle.load(open(f, 'rb')); S = sp.expand(d['S']); R = d['R']
    P = sp.Poly(sp.together(S*(s-2)**((e+3)//2)*(7*s-32)**((e+3)//2)).expand(), g)
    print('e=%d: g-powers %s' % (e, [m[0] for m in P.monoms()]))
    for (k,), c in zip(P.monoms(), P.coeffs()):
        fc = sp.factor_list(sp.Poly(c, s))
        print('   g^%d: content %s, factors %s' % (k, fc[0], [(str(p.as_expr())[:60] + ('...' if len(str(p.as_expr())) > 60 else ''), m) for p, m in fc[1]]))
    print('   leading g-power coefficient factorised:', sp.factor(P.coeffs()[0]))
    sys.stdout.flush()
