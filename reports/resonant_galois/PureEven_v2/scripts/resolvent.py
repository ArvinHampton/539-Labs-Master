"""Derive the sextic (F20-)resolvent R(X; a, b) of x^5+a x+b.

Roots of R: theta_j = (sum_i x_i x_{i+1} - sum_i x_i x_{i+2})^2 over the six cosets of F20 in S5
(indices mod 5, applied to an ordering of the roots).  theta_j are algebraic integers, so the
coefficients of R are polynomials in Z[a,b], weighted-homogeneous (wt a=4, wt b=5, wt theta=4).
Method: high-precision (300 digit) root finding at integer points (a,b), rounding the coefficients to
integers (error checked < 1e-100), then exact linear algebra over Q for the unknown integer polynomial
coefficients, using MORE points than unknowns, followed by an independent check at fresh points.
Output: data/sextic_resolvent.txt
"""
import itertools, random, json
import mpmath as mp
import sympy as sp
mp.mp.dps = 300
random.seed(12345)

def theta(xs, perm):
    y = [xs[p] for p in perm]
    s1 = sum(y[i]*y[(i+1) % 5] for i in range(5))
    s2 = sum(y[i]*y[(i+2) % 5] for i in range(5))
    return (s1 - s2)**2

def numeric_resolvent_coeffs(A, B):
    roots = mp.polyroots([1, 0, 0, 0, A, B], maxsteps=2000, extraprec=2000)
    vals = []
    for perm in itertools.permutations(range(5)):
        th = theta(roots, perm)
        for v in vals:
            if abs(v - th) < mp.mpf(10)**(-100): break
        else:
            vals.append(th)
    assert len(vals) == 6, len(vals)
    # elementary symmetric functions of the 6 thetas
    c = [mp.mpf(1)] + [mp.mpf(0)]*6
    poly = [mp.mpc(1)]
    for v in vals:
        new = poly + [mp.mpc(0)]
        for i in range(len(poly)):
            new[i+1] -= v*poly[i]
        poly = new
    ints = []
    for z in poly:
        r = mp.nint(z.real)
        assert abs(z - r) < mp.mpf(10)**(-100), z
        ints.append(int(r))
    return ints   # [1, c1, ..., c6]: X^6 + c1 X^5 + ... + c6

a_, b_ = sp.symbols('a b')
def monos(n):  # exponents (i,j) with 4i+5j = 4n
    return [(i, j) for j in range(0, 4*n//5+1) for i in range(0, n+1) if 4*i+5*j == 4*n]

pts = []
while len(pts) < 60:
    A, B = random.randint(-30, 30), random.randint(-30, 30)
    if (A, B) in pts or 256*A**5+3125*B**4 == 0: continue
    pts.append((A, B))
data = {p: numeric_resolvent_coeffs(*p) for p in pts}
coef = {}
for n in range(1, 7):
    ms = monos(n)
    assert len(ms) + 5 < len(pts)
    M = sp.Matrix([[A**i*B**j for (i, j) in ms] for (A, B) in pts[:len(ms)+8]])
    rhs = sp.Matrix([data[p][n] for p in pts[:len(ms)+8]])
    sol, params = M.gauss_jordan_solve(rhs)   # overdetermined: raises if inconsistent
    assert len(params) == 0
    coef[n] = sum(sol[i]*a_**ms[i][0]*b_**ms[i][1] for i in range(len(ms)))
X = sp.symbols('X')
Rpoly = X**6 + sum(coef[n]*X**(6-n) for n in range(1, 7))
# independent check at the remaining points
for p in pts:
    got = [int(Rpoly.coeff(X, 6-n).subs({a_: p[0], b_: p[1]})) for n in range(1, 7)]
    assert got == data[p][1:], p
# extra fresh points, never used to fit
for _ in range(10):
    A, B = random.randint(-200, 200), random.randint(-200, 200)
    if 256*A**5+3125*B**4 == 0: continue
    dd = numeric_resolvent_coeffs(A, B)
    got = [int(Rpoly.coeff(X, 6-n).subs({a_: A, b_: B})) for n in range(1, 7)]
    assert got == dd[1:]
open('../data/sextic_resolvent.txt', 'w').write(
    "R(X;a,b) = X^6 + sum_{n=1}^6 c_n(a,b) X^{6-n}\n" +
    "\n".join(f"c{n} = {sp.factor(coef[n])}" for n in range(1, 7)) +
    "\n\nexpanded: " + str(sp.expand(Rpoly)) + "\n")
print(open('../data/sextic_resolvent.txt').read())
# discriminant of R in terms of a,b
dR = sp.factor(sp.discriminant(Rpoly, X))
print("disc_X(R) =", dR)
open('../data/sextic_resolvent.txt', 'a').write("\ndisc_X(R) = "+str(dR)+"\n")
