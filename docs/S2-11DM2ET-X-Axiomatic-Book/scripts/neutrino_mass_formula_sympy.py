#!/usr/bin/env python3
"""
Neutrino mass formula and related symbolic expressions.
Pure SymPy rendering of the puncture / golden-ratio scaling expression.
"""

import sympy as sp
from sympy import symbols, sqrt, Rational, exp, I, pi, pprint, N

# Golden ratio
phi = (1 + sqrt(5)) / 2

# Symbolic mass expression (base scale)
# m_nu = (61 / 1001) * (phi**7 / 539.9)
m_nu_base = (Rational(61, 1001)) * (phi**7 / Rational(5399, 10))

# Cube roots of unity (flavor phases)
omega = exp(2 * pi * I / 3)
flavors = [1, omega, omega**2]

# Numerical evaluation helper
def numerical_base(digits=12):
    return N(m_nu_base, digits)


if __name__ == "__main__":
    print("Neutrino mass base expression:")
    pprint(m_nu_base)
    print()
    print("Numerical base scale (eV):")
    print(numerical_base())
    print()
    print("Flavor phases {1, omega, omega**2}:")
    for f in flavors:
        pprint(f)
        print("  ->", N(f, 8))
