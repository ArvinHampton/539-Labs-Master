#!/usr/bin/env python3
"""
HQCC Ternary Map (T3) - SymPy / pure Python rendering.
Canonical integer map used throughout the workspace.
"""

import sympy as sp
from sympy import Piecewise, Eq, Mod, symbols, pprint

n = symbols('n', integer=True, nonnegative=True)

# Canonical T3 (integer arithmetic form)
# r = 0: n // 3
# r = 1: (4*n + 2) // 3
# r = 2: (2*n + 1) // 3
t3_expr = Piecewise(
    (n // 3, Eq(Mod(n, 3), 0)),
    ((4 * n + 2) // 3, Eq(Mod(n, 3), 1)),
    ((2 * n + 1) // 3, Eq(Mod(n, 3), 2)),
    (0, True)
)

def t3(n: int) -> int:
    """Pure Python integer implementation of the canonical T3 map."""
    if n == 0:
        return 0
    r = n % 3
    if r == 0:
        return n // 3
    elif r == 1:
        return (4 * n + 2) // 3
    else:
        return (2 * n + 1) // 3


if __name__ == "__main__":
    print("Canonical T3 (SymPy Piecewise):")
    pprint(t3_expr)
    print()
    print("Examples (Python):")
    for seed in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(f"  T3({seed}) = {t3(seed)}")
