#!/usr/bin/env python3
"""
Lagrangian and Hamiltonian symbolic forms.
SymPy rendering of the core structural expressions.
"""

import sympy as sp
from sympy import (
    symbols, Function, sqrt, pi, exp, Rational, pprint
)

# Core symbols
t = symbols('t', real=True)
g = symbols('g', real=True)
R = symbols('R', real=True)
G = symbols('G', positive=True)

# Lagrangian density pieces
L_M = symbols(r'\mathcal{L}_M')
L_11D = symbols(r'\mathcal{L}_{11D}')
L_ET = symbols(r'\mathcal{L}_{ET}')

# 11D sector
g_11 = symbols('g_{11}', real=True)
Phi = Function(r'\Phi')
psi = Function(r'\psi')
T_M2 = symbols(r'T_{M2}', real=True)
M2 = Function('M2')
T_M5 = symbols(r'T_{M5}', real=True)
M5 = Function('M5')

# Energy-transfer sector
kappa_dark = symbols(r'\kappa_{dark}', positive=True)
delta = Function(r'\delta')
v_0 = symbols('v_0', positive=True)
f_energy = symbols(r'f_{energy}', real=True)
rho_DM = symbols(r'\rho_{DM}', positive=True)
delta_a_mu = symbols(r'\delta a_\mu^{-U}', real=True)
g_minusU = symbols('g_{-U}', real=True)
m_mu = symbols(r'm_\mu', positive=True)
M_minusU = symbols(r'M_{-U}', positive=True)
beta_PBH = Rational(18, 100)
M_PBH = symbols(r'M_{PBH}', positive=True)
k_B = symbols('k_B', positive=True)
T_rad = symbols(r'T_{rad}', positive=True)

# Full Lagrangian density
L = sqrt(-g) * (R / (16 * pi * G) + L_M + L_11D + L_ET)

L_11D_expr = g_11 * Phi(psi(t)) + T_M2 * M2(t) + T_M5 * M5(t)

L_ET_expr = (
    kappa_dark * sqrt(delta(t)) * v_0 * f_energy * (1 + rho_DM / 10)
    + delta_a_mu * (g_minusU**2 * m_mu**2) / (8 * pi**2 * M_minusU**2)
    + beta_PBH * rho_DM * exp(-M_PBH / (k_B * T_rad))
)

# Hamiltonian (Legendre form + explicit structural sum)
pi_sym = symbols(r'\pi', real=True)
q_dot = symbols(r'\dot{q}', real=True)
E_cosmos = symbols(r'E_{cosmos}', real=True)
F_friction = symbols(r'F_{friction}', real=True)
mu = symbols(r'\mu', real=True)
S_over_N = symbols('S/N', real=True)

H = pi_sym * q_dot - L
H_explicit = E_cosmos + F_friction + mu * S_over_N


if __name__ == "__main__":
    print("Lagrangian density:")
    pprint(L)
    print()
    print("L_11D:")
    pprint(L_11D_expr)
    print()
    print("L_ET:")
    pprint(L_ET_expr)
    print()
    print("Hamiltonian (Legendre):")
    pprint(H)
    print()
    print("Hamiltonian (explicit structural form):")
    pprint(H_explicit)
