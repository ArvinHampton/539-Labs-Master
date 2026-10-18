# Item (3): x = 1/3 closed forms.  c_e(s) = gamma0 * A_e(s) + sum_r eb_r Y_{e,r}(s) + sum_r ea_r X_{e,r}(s,g)
# gamma0, eb: functions of s mod 3 (proved); ea: function of s mod 144, in fact of s mod 72 (proved + exhaustive table, x_third_classes.json)
import pickle, sys, json, sympy as sp
from sym_engine import s, g
from gauss_data import data
K = int(sys.argv[1]) if len(sys.argv) > 1 else 5
U = pickle.load(open('sym_universal_P6_K%d.pkl' % K, 'rb'))
rt = sp.sqrt(2*sp.pi*s); D = (s - 2)*(7*s - 32)
Rs = sp.Symbol('sqrtDelta', positive=True); DE = sp.expand(D)
def toR(e):
    e = sp.expand(sp.simplify(e))
    for k in range(25, 0, -1):
        e = e.subs(DE**sp.Rational(k, 2), Rs**k).subs(D**sp.Rational(k, 2), Rs**k)
    e = sp.expand(e).subs(Rs**2, DE)
    e = sp.expand(e)
    for k in range(25, 1, -1):
        e = e.subs(Rs**k, DE**(k//2)*Rs**(k % 2))
    e = sp.expand(e)
    P = sp.factor(e.coeff(Rs, 0)); Qc = sp.factor(e.coeff(Rs, 1))
    return '%s + (%s)*sqrt((s-2)(7s-32))' % (P, Qc)
out = []
for cls, rep in ((0, 6), (1, 7), (2, 5)):
    d = data(rep, 1, 3, R=K + 3)
    out.append('### s = %d mod 3: gamma0 = %s' % (cls, sp.nsimplify(d['gamma0'])))
    for e, (A, Yc, Xc) in U.items():
        g0 = sp.nsimplify(d['gamma0']); ebs = {k: sp.nsimplify(sp.expand(d['eb'][k])) for k in Yc}
        re_ = toR((sp.re(g0)*A + sum(sp.re(ebs[k])*Yc[k] for k in Yc))/rt)
        im_ = toR((sp.im(g0)*A + sum(sp.im(ebs[k])*Yc[k] for k in Yc))/rt)
        out.append('  t^{%d/2}: [gamma0, eb part] / sqrt(2 pi s) = (%s) + i*(%s)' % (e, re_, im_))
        print(out[-1], flush=True)
out.append('### ea part: c_e += sum_r ea_r X_{e,r}(s,g); X_{e,r} / sqrt(2 pi s):')
for e, (A, Yc, Xc) in U.items():
    out.append('  t^{%d/2}: ' % e + '; '.join('X_%d = %s' % (k, toR(Xc[k]/rt)) for k in sorted(Xc)))
open('x_third_closed_K%d.txt' % K, 'w').write('\n'.join(out) + '\n')
