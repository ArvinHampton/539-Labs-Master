"""Appendix A seeds (irreducibility, square discriminant, cycle types, PARI group) and the Belyi negative control."""
import os
os.environ["OMP_NUM_THREADS"] = "1"
import sympy as sp
from fractions import Fraction as Fr
from common import *
from galois_tools import *
x = sp.symbols('x')
print("== Seeds ==")
for (A, B, lab) in [(-55, 88, "flagship"), (-100, 400, "LSW"), (20, 16, "classical"), (20, -32, "D5 fibre on flagship slice")]:
    d = 256*A**5 + 3125*B**4
    r = sp.integer_nthroot(d, 2)
    irr = is_irreducible(A, B)
    ty, used = cycle_types(A, B)
    k = Fr(B, A)
    mm = sqrt_rat(Fr(256*A + 3125*k**4) / 65536) if is_square_rat(Fr(256*A+3125*k**4)/65536) else None
    print(f"{lab}: x^5+({A})x+({B}); k={k}; m={mm}; disc={d}={sp.factorint(d)} ; sqrt={r}; irreducible={irr}; "
          f"Frobenius classification={classify_frobenius(A,B,irr,ty)} (primes used {used}); PARI={pari_group(A,B)}")
    print("    cycle types:", {str(c): n for c, n in sorted(ty.items(), reverse=True)})
    print("    sextic resolvent has rational root:", resolvent_rational_root(A, B), "; x^5+ax+b mod 2,3,5 factor patterns skipped (small primes)")
    assert r[1] and d == r[0]**2
print("\n== Belyi control ==")
y, t = sp.symbols('y t')
phi = 6*y**5 - 15*y**4 + 10*y**3
mon = sp.expand((phi - t)/6)
dd = sp.factor(sp.discriminant(mon, y))
print("disc_y(monic(phi - t)) =", dd)
assert sp.simplify(dd - 5*(sp.Rational(25,36)*t*(t-1))**2) == 0
print("matches 5*(25 t (t-1)/36)^2 : OK")
print("phi' =", sp.factor(sp.diff(phi, y)), " ; critical values 0, 1; poles: infinity (5-cycle)")
# integer model z = 6y : z^5 - 15 z^4 + 60 z^3 - 1296 t
def belyi_poly(tv):
    from flint import fmpz_poly
    return fmpz_poly([-1296*tv, 0, 0, 60, -15, 1])
assert sp.expand(6**5*mon.subs(y, x/6) - (x**5 - 15*x**4 + 60*x**3 - 1296*t)) == 0
def belyi_cycle_types(tv, primes=PRIMES):
    f = belyi_poly(tv); d = int(sp.discriminant(sp.Poly(x**5 - 15*x**4 + 60*x**3 - 1296*tv, x)))
    types = {}
    for p in primes:
        if d % p == 0: continue
        g = nmod_poly([int(c) % p for c in f.coeffs()], p)
        fac = g.factor()[1]
        if any(e > 1 for _, e in fac): continue
        ct = tuple(sorted((h.degree() for h, e in fac), reverse=True)); types[ct] = types.get(ct, 0)+1
    return types
for tv in [3]:
    ty = belyi_cycle_types(tv)
    P = pari(f"x^5-15*x^4+60*x^3-{1296*tv}")
    print(f"t={tv}: z^5-15z^4+60z^3-{1296*tv}: irreducible={bool(pari.polisirreducible(P))}; disc={int(sp.discriminant(sp.Poly(x**5-15*x**4+60*x**3-1296*tv,x)))}"
          f" = 5*({sp.integer_nthroot(int(sp.discriminant(sp.Poly(x**5-15*x**4+60*x**3-1296*tv,x)))//5, 2)[0]})^2 ; PARI polgalois = {POL_ORDER[int(pari.polgalois(P)[0])]}")
    print("   cycle types over primes 7..4000:", {str(c): n for c, n in sorted(ty.items(), reverse=True)})
cnt = {}; red_t = []
for tv in range(2, 101):
    P = pari(f"x^5-15*x^4+60*x^3-{1296*tv}")
    if not pari.polisirreducible(P): cnt["reducible"] = cnt.get("reducible", 0)+1; red_t.append(tv); continue
    g = POL_ORDER[int(pari.polgalois(P)[0])]; cnt[g] = cnt.get(g, 0)+1
print("PARI polgalois for t=2..100 (integer t):", cnt)
print("reducible t in 2..100:", red_t)
