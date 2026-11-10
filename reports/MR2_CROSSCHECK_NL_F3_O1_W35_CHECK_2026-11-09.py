# MR2 cross-check script (NL F3), 2026-11-09 America/Chicago. Arithmetic only.
import sympy as sp
R0, m0, k, c, N = sp.symbols('R0 m0 k c N', positive=True)
# KR hep-th/0003281 eq (13): L^2 = 2R0^2/3 (AdS5), rho^2 = R0^2/6 (H2), r^2 = R0^2/4 (S4)
L2, rho2, r2 = 2*R0**2/3, R0**2/6, R0**2/4
Ric = {'AdS5': -4/L2, 'H2': -1/rho2, 'S4': 3/r2}
print("KR(13) Ricci eigenvalues:", {b: sp.simplify(v) for b, v in Ric.items()})
# KR eq (2): R_MN = (1/12)(F_M..F_N.. - (1/12) g F^2); FR (4): F = q * eps(S4), q = 6 m0
q = sp.symbols('q', positive=True)
rhs_ext = sp.Rational(1,12)*(0 - sp.Rational(1,12)*24*q**2)
rhs_S4  = sp.Rational(1,12)*(6*q**2 - sp.Rational(1,12)*24*q**2)
print("KR(2) on FR ansatz: ext =", rhs_ext, " S4 =", rhs_S4, "(KR (5): -6m0^2, 12m0^2 with q=6m0 ->", rhs_ext.subs(q,6*m0), rhs_S4.subs(q,6*m0), ")")
qsol = sp.solve(sp.Eq(rhs_S4, Ric['S4']), q)[0]; print("frame amplitude required by (2)+(13): q =", qsol, "; check ext:", sp.simplify(rhs_ext.subs(q,qsol) - Ric['AdS5']), sp.simplify(rhs_ext.subs(q,qsol) - Ric['H2']))
print("=> m0 = q/6 =", sp.simplify(qsol/6))
# Printed (14): F = 6 R0^3 Omega4. If Omega4 = unit-S4 volume form, vol(S4_r) = r^4 Omega4 -> frame amplitude 6R0^3/r^4
amp14 = sp.simplify(6*R0**3/r2**2); print("(14) read with unit-sphere Omega4: frame amplitude =", amp14, "; ratio to required =", sp.simplify(amp14/qsol))
print("correct unit-sphere coefficient: F =", sp.simplify(qsol*r2**2/R0**3), "* R0^3 * Omega4")
# match to (D): L = 1/k -> R0
R0D = sp.solve(sp.Eq(L2, 1/k**2), R0)[0]; print("(D): R0 =", R0D, "; q(R0) =", sp.simplify(qsol.subs(R0,R0D)), "vs q0 = 2 sqrt6 k:", sp.simplify(qsol.subs(R0,R0D) - 2*sp.sqrt(6)*k))
print("  r =", sp.simplify(sp.sqrt(r2).subs(R0,R0D)), " rho =", sp.simplify(sp.sqrt(rho2).subs(R0,R0D)), " R0 = L7 = 2r:", sp.simplify(R0D - 2*sp.sqrt(r2).subs(R0,R0D)))
kN = sp.sqrt(sp.Rational(3,8))*(sp.pi*N)**sp.Rational(-1,3)
print("  N=4880: R0 =", sp.N(R0D.subs(k,kN).subs(N,4880),10), " lp; flux check q*Vol(S4_r)/(2pi)^3 =", sp.N((qsol*sp.Rational(8,3)*sp.pi**2*r2**2).subs(R0,R0D).subs(k,kN).subs(N,4880)/(2*sp.pi)**3,10))
# NL Q1: Phi = c*G.G with G.G = 576k^2 on (D). L7a: G_ext = -Phi/96 ; lock: k^2 = Phi/1728
Gext = -6*k**2; Phi = c*576*k**2
print("L7a holds iff c =", sp.solve(sp.Eq(Gext, -Phi/96), c), "; lock holds iff c =", sp.solve(sp.Eq(k**2, Phi/1728), c), "-> no c satisfies both")
print("Phi-2 (c=3): G_ext + Phi/96 =", sp.simplify((Gext + Phi/96).subs(c,3)))
# NL Q5: fundamental unit of Q(sqrt35): smallest Pell solution
sol = next((x,y) for y in range(1,100) for x in [int(sp.sqrt(35*y*y+1))] if x*x-35*y*y==1)
print("Pell x^2-35y^2=1 minimal:", sol, "; x^2-35y^2=-1 solvable? no (7|35, 7=3 mod 4); regulator ln(6+sqrt35) =", sp.N(sp.log(6+sp.sqrt(35)),12))
print("dims: W35 =", sp.binomial(7,4), " V35(Owner lock) = 14, V35(RTA Def 33.2, per NL) = 36")
