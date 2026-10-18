# Path B: closed forms in s of the H_s radial coefficients (s>=5) from the generic EM expansion (H_em.py) + exact angular integrals.
import sympy as sp, pickle
from math import gcd
from H_em import coef, s, g, mu, al, be2, ga, b, Sx, Sy, Sxy, bern_sums
out = []
def check(name, z):
    ok = sp.simplify(z) == 0; out.append(f"[{'PASS' if ok else 'FAIL'}] {name}"); print(out[-1]); return ok
# angular integrals int_0^oo (1+b mu)^j / Q(mu)^{1+j/2}, Q = ga mu^2 + be2 mu + al, via exact antiderivatives R(mu)/Q^{j/2}
Qm = ga*mu**2 + be2*mu + al
def ang(j):
    r = sp.symbols(f'r0:{j+1}'); R = sum(r[i]*mu**i for i in range(j+1))
    num = sp.expand(sp.diff(R, mu)*Qm - sp.Rational(j, 2)*R*sp.diff(Qm, mu) - (1 + b*mu)**j)
    sol = sp.solve(sp.Poly(num, mu).all_coeffs(), r, dict=True); assert len(sol) == 1
    Rs = R.subs(sol[0]); val = sp.limit(Rs/Qm**sp.Rational(j, 2), mu, sp.oo) - (Rs/Qm**sp.Rational(j, 2)).subs(mu, 0)
    # check antiderivative
    assert sp.simplify(sp.diff(Rs/Qm**sp.Rational(j, 2), mu) - (1 + b*mu)**j/Qm**(1+sp.Rational(j, 2))) == 0
    return sp.simplify(val)
A1, A3 = ang(1), ang(3)
# generic Bernoulli sums: complete residue systems, averaged endpoints
gen = {}
for p in Sx:
    val = 0 if p == 1 else (3*s/g)**(1-p)*sp.bernoulli(p)
    gen[Sx[p]] = val; gen[Sy[p]] = val
out.append("Generic sums: Sx_p = Sy_p = m^{1-p} B_p (p>=2), 0 (p=1) [distribution relation; averaged endpoint]; "
           "Sxy12 = Sxy21 = 0 [j -> m-j symmetry: B1 odd, B2 even about 1/2]")
gen[Sxy[(1, 2)]] = 0; gen[Sxy[(2, 1)]] = 0
H = {k: sp.simplify(c.subs({sp.Symbol('ANG1'): A1, sp.Symbol('ANG3'): A3}).subs(gen)) for k, c in coef.items()}
for k in H: H[k] = sp.simplify(sp.radsimp(H[k]))
names = {-2: 't^-1', -1: 't^-1/2', 0: 't^0', 1: 't^1/2', 2: 't^1'}
out.append("\nH_s closed forms (s >= 5; g = gcd(24, s-8)):")
for k in H: out.append(f"  {names[k]}: {H[k]}")
check("H t^-1 = 0 (Lemma 2)", H[-2]); check("H t^0 = 0", H[0]); check("H t^1 = 0", H[2])
out.append(f"  g-dependence of t^-1/2: {sp.simplify(sp.diff(H[-1], g)) == 0} (False means depends on g)")
out.append(f"  g-dependence of t^1/2: d/dg = {sp.simplify(sp.diff(H[1], g))}")
# check the symbolic Sxy symmetry and complete-residue sums against exact per-s sums
bad = []
for sv in list(range(5, 61)) + [99, 100, 151, 223, 300]:
    d, gv, mv, bv = bern_sums(sv)
    for key, val in d.items():
        exp_ = gen.get(key, None)
        if exp_ is not None and sp.simplify(sp.sympify(exp_).subs({s: sv, g: gv}) - val) != 0: bad.append((sv, key))
out.append(f"[{'PASS' if not bad else 'FAIL'}] exact per-s Bernoulli sums (s=5..60, 99, 100, 151, 223, 300) equal the generic values for all sums used: mismatches {bad[:5]}")
pickle.dump({'H': H, 'A1': A1, 'A3': A3}, open('H_closed.pkl', 'wb'))
open('H_closed.txt', 'w').write("\n".join(out) + "\n"); print("\n".join(out))
