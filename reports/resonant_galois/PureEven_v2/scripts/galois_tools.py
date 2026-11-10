"""Frobenius cycle-type classification of x^5 + A x + B (A, B integers), cross-checked with PARI polgalois."""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
from flint import fmpz_poly, nmod_poly
from sympy import primerange
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9, silent=True) if False else None
PRIMES = list(primerange(7, 4001))     # Frobenius primes used: 7 <= p <= 4000  (p=2,3,5 skipped)
POL_ORDER = {120: "S5", 60: "A5", 20: "F20", 10: "D5", 5: "C5"}

def cycle_types(A, B, primes=PRIMES):
    """Return dict cycle-type -> count, over primes p not dividing disc."""
    d = 256*A**5 + 3125*B**4
    types = {}
    used = 0
    for p in primes:
        if d % p == 0: continue
        f = nmod_poly([B % p, A % p, 0, 0, 0, 1], p)
        fac = f.factor()[1]
        if any(e > 1 for _, e in fac): continue
        ct = tuple(sorted((g.degree() for g, e in fac), reverse=True))
        types[ct] = types.get(ct, 0) + 1
        used += 1
    return types, used

def classify_frobenius(A, B, irreducible, types):
    if not irreducible: return "reducible"
    if (3, 1, 1) in types: return "A5"
    allowed = {(1, 1, 1, 1, 1), (5,), (2, 2, 1)}
    if (2, 2, 1) in types and set(types) <= allowed: return "D5"
    return "undetermined"

def pari_group(A, B):
    P = pari(f"x^5 + ({A})*x + ({B})")
    if not pari.polisirreducible(P): return "reducible"
    g = pari.polgalois(P)
    return POL_ORDER[int(g[0])]

def is_irreducible(A, B):
    return bool(fmpz_poly([B, A, 0, 0, 0, 1]).factor()[1].__len__() == 1 and fmpz_poly([B, A, 0, 0, 0, 1]).factor()[1][0][1] == 1)

def resolvent_rational_root(A, B):
    """Does the sextic resolvent R(X;A,B) have a rational root?  (R squarefree iff B != 0 and disc != 0)"""
    a, b = A, B
    R = pari(f"x^6 - 40*({a})*x^5 + 880*({a})^2*x^4 - 8960*({a})^3*x^3 + 44800*({a})^4*x^2 "
             f"- 1024*(106*({a})^5 + 3125*({b})^4)*x + 102400*({a})^6")
    return len(pari.nfroots(None, R)) > 0
