# Goal 2 (Cat A): exact t^{11/2}, t^{13/2} coefficients from the universal symbolic form of the proved expansion.
#   x = 0   : c_e = sqrt(2 pi s) [ R_e(s) + S_e(s,g) sqrt(D) ],  D = (s-2)(7s-32)          (gamma0 = 1, eb = ea = Bt_r(0))
#   x = 1/2 : even s: c_e = sqrt(2 pi s) [ Rh_e(s) + [16|s] Sh_e(s,g) sqrt(D) ]; odd s: 0 (Prop. O)
# Method: the symbolic universal coefficient (exact, in s and g) is evaluated EXACTLY at integer s with D non-square
# (g kept as a symbol); the rational part and the sqrt(D) part separate uniquely; each is interpolated in s with the
# known denominator and the interpolant is re-checked exactly at further s values (all exact rational arithmetic).
import pickle, sympy as sp, math, sys, json
from sym_engine import s, g
Bt0 = lambda r: sp.Integer(0) if r == 1 else sp.bernoulli(r, 0)
Bt = lambda r, u: sp.Integer(0) if (r == 1 and u == 0) else sp.bernoulli(r, u)
P = int(sys.argv[1]); E = [int(z) for z in sys.argv[2].split(',')]
U = pickle.load(open('sym_universal_P%d_K13.pkl' % P, 'rb'))
if P == 1: gam, eb, ea = 1, {r: Bt0(r) for r in range(1, 20)}, {r: Bt0(r) for r in range(1, 20)}
else:      # x = 1/2, even s, 16 | s variant gives the sqrt(D) part; 16 !| s has ea = 0
    gam = 0; eb = {r: 4*sum((-1)**j*Bt(r, sp.Rational(j, 4)) for j in range(4)) for r in range(1, 20)}; ea = eb
def coeff(e):
    A, Yc, Xc = U[e]
    return gam*A + sum(eb[k]*Yc[k] for k in Yc) + sum(ea[k]*Xc[k] for k in Xc)
def is_sq(n): r = math.isqrt(n); return r*r == n
svals = [v for v in range(30, 400) if not is_sq((v-2)*(7*v-32))]
res = {}
for e in E:
    ce = coeff(e)/sp.sqrt(2*sp.pi*s)
    kR = (e + 3)//2
    pts = []
    for sv in svals[:2*e + 40]:
        v = sp.expand(sp.radsimp(sp.expand(ce.subs(s, sv))))
        rD = sp.sqrt(sp.Integer((sv-2)*(7*sv-32)))
        R_ = sum((t for t in sp.Add.make_args(v) if not t.has(sp.Pow) or t.is_Rational), sp.Integer(0))
        Sd = sp.expand(sp.radsimp((v - R_)/rD))
        assert not Sd.has(sp.sqrt(2)) and all(not a.is_irrational for a in sp.Poly(Sd, g).coeffs()), (e, sv, Sd)
        assert R_.is_Rational, (e, sv, R_)
        pts.append((sv, R_, sp.Poly(Sd, g)))
    nfit = len(pts) - 10
    Rnum = sp.interpolate([(sv, R_*(sv-2)**kR) for sv, R_, _ in pts[:nfit]], s)
    Rexp = sp.factor(Rnum/(s-2)**kR)
    okR = all(sp.simplify(Rexp.subs(s, sv) - R_) == 0 for sv, R_, _ in pts[nfit:])
    # S: per g-power coefficient, denominator (s-2)^kR (7s-32)^kR
    degs = sorted({m[0] for _, _, Sp in pts for m in Sp.monoms()})
    Sexp = 0; okS = True
    for dg in degs:
        f = lambda Sp: Sp.as_dict().get((dg,), sp.Integer(0))
        num = sp.interpolate([(sv, f(Sp)*(sv-2)**kR*(7*sv-32)**kR) for sv, _, Sp in pts[:nfit]], s)
        term = num/((s-2)**kR*(7*s-32)**kR)
        okS &= all(sp.simplify(term.subs(s, sv) - f(Sp)) == 0 for sv, _, Sp in pts[nfit:])
        Sexp += sp.factor(term)*g**dg
    res[e] = dict(R=str(Rexp), S=str(Sexp), R_check=bool(okR), S_check=bool(okS), R_numdeg=int(sp.degree(sp.numer(sp.together(Rexp)), s)))
    print('e =', e, 'R =', Rexp, '\n  checks R/S on 10 held-out s:', okR, okS, flush=True)
    pickle.dump(dict(R=Rexp, S=Sexp), open('closed_P%d_e%d_lowK13.pkl' % (P, e), 'wb'))
json.dump(res, open('closed_P%d_K13_low.json' % P, 'w'), indent=1)
