"""Shared helpers (exact arithmetic only).  Run with OMP_NUM_THREADS=1."""
from fractions import Fraction as Fr
from math import gcd, isqrt
import sympy as sp

def is_square_rat(q):
    q = Fr(q)
    if q < 0: return False
    n, d = q.numerator, q.denominator
    return isqrt(n)**2 == n and isqrt(d)**2 == d

def sqrt_rat(q):
    q = Fr(q); return Fr(isqrt(q.numerator), isqrt(q.denominator))

def alpha(m, k):
    m, k = Fr(m), Fr(k)
    return 256*m*m - Fr(3125)*k**4/256

def bj(m, k):
    a = alpha(m, k); return a, Fr(k)*a

def disc_bj(a, b):
    return 256*Fr(a)**5 + 3125*Fr(b)**4

def clear_denominators(a, b):
    """x^5+a x+b with a,b rational -> integer (a',b') = (a t^4, b t^5) with t minimal
    positive integer making both integral; polynomial x^5+a'x+b' is t^5 f(x/t),
    hence has the same splitting field / Galois group."""
    a, b = Fr(a), Fr(b)
    t = 1
    from sympy import factorint
    dens = {}
    for q, e in ((a, 4), (b, 5)):
        if q.denominator > 1:
            for p, v in factorint(q.denominator).items():
                need = -(-(v) // e)  # ceil(v/e)
                dens[p] = max(dens.get(p, 0), need)
    for p, v in dens.items(): t *= p**v
    A, B = a*t**4, b*t**5
    assert A.denominator == 1 and B.denominator == 1
    return int(A), int(B), t
