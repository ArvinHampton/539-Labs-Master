# Item (2): x = 1/2 closed forms (Cat A) from the universal symbolic form + proved Gauss data:
#   odd s: gamma0 = eb = ea = 0;  even s: gamma0 = 0, eb_r = 4 sum_j (-1)^j Bt_r(j/4), ea_r = [16|s] eb_r
import pickle, sys, sympy as sp
from sym_engine import s, g
K = int(sys.argv[1]) if len(sys.argv) > 1 else 5
U = pickle.load(open('sym_universal_P4_K%d.pkl' % K, 'rb'))
Bt = lambda r, u: sp.Integer(0) if (r == 1 and u == 0) else sp.bernoulli(r, u)
eb = {r: 4*sum((-1)**j*Bt(r, sp.Rational(j, 4)) for j in range(4)) for r in range(1, K + 4)}
print('eb_r:', {r: eb[r] for r in eb})
D = (s - 2)*(7*s - 32)
lines = []
for e, (A, Yc, Xc) in U.items():
    base = sp.factor(sp.simplify(sum(eb[k]*Yc[k] for k in Yc)/sp.sqrt(2*sp.pi*s)))
    extra = sp.simplify(sum(eb[k]*Xc[k] for k in Xc)/sp.sqrt(2*sp.pi*s))
    # write extra as poly(s,g) * sqrt(D) / denominators
    ex2 = sp.factor(sp.simplify(extra/sp.sqrt(D)))
    lines.append('t^{%d/2}: H = sqrt(2 pi s) * [ %s  +  [16|s] * sqrt((s-2)(7s-32)) * ( %s ) ]' % (e, base, ex2))
    print(lines[-1], flush=True)
open('x_half_closed_K%d.txt' % K, 'w').write('\n'.join(lines) + '\n')
