# NL derived proposal - t552u pursuit: GA9 (what supplies S(k,k) < 0 at O(N)), S4 (C ^ X8 at the odd wall), A15 (limited) (2026-11-10)
# Exact tests only: sp.expand(...)==0 on polynomials or exact Rational/Fraction comparisons.
# No simplify()==0, no allclose, no floats in any test.
import sympy as sp
from fractions import Fraction as Fr

ok_all = True; npass = 0; ntot = 0
def check(name, cond):
    global ok_all, npass, ntot
    c = bool(cond); ntot += 1; npass += c; ok_all = ok_all and c
    print(f"[{'PASS' if c else 'FAIL'}] {name}")
def Z(e): return sp.expand(e) == 0

# ---------------- GA9: block-averaged source model and exact LP certificates ----------------
# types (sig, fib): smeared object with worldvolume R^{1,3} x (sig Sigma dirs) x (fib fibre dirs), tension T (any sign):
#   rho = T, tr_Sigma S = -sig T, tr_fib S = -fib T.  (2,4) = wall-filling Lambda.
# magnetic Y6 YM (1142 F1): rho = (Pff + Pm + Pss)/2, tr_Sigma S = Pss - Pff, tr_fib S = -Pm - 2 Pss, P's >= 0.
types = [(s_, f_) for s_ in range(3) for f_ in range(5)]
def columns():
    cols = []
    for (s_, f_) in types: cols.append(("T+", (s_, f_), (Fr(1), Fr(-s_), Fr(-f_)), Fr(0)))
    for (s_, f_) in types: cols.append(("T-", (s_, f_), (Fr(-1), Fr(s_), Fr(f_)), Fr(1)))
    cols.append(("Pff", None, (Fr(1,2), Fr(-1), Fr(0)), Fr(0)))
    cols.append(("Pm",  None, (Fr(1,2), Fr(0), Fr(-1)), Fr(0)))
    cols.append(("Pss", None, (Fr(1,2), Fr(1), Fr(-2)), Fr(0)))
    return cols
COLS = columns()
# YM block formulas checked against an explicit field (10D, legs on Y6 = Sigma(4,5) + fibre(6..9))
D10 = 10; eta = sp.diag(-1, *([1]*9)); SIG = [4,5]; FIB = [6,7,8,9]; Y6 = SIG + FIB
F = sp.zeros(D10, D10); Pff = 0; Pm = 0; Pss = 0
for i, a in enumerate(Y6):
    for b in Y6[i+1:]:
        x = sp.Symbol(f"F{a}{b}", real=True); F[a,b] = x; F[b,a] = -x
        if a in FIB and b in FIB: Pff += x**2
        elif a in SIG and b in SIG: Pss += x**2
        else: Pm += x**2
Fup = eta*F*eta
F2t = sum(F[a,b]*Fup[a,b] for a in range(D10) for b in range(D10))
S = sp.Matrix(D10, D10, lambda a,b: sum(F[a,c]*F[b,dd]*eta[c,dd] for c in range(D10) for dd in range(D10)) - sp.Rational(1,4)*eta[a,b]*F2t)
rho = sp.Rational(1,4)*F2t
check("J0 YM block data: rho = (Pff+Pm+Pss)/2, tr_Sigma S = Pss - Pff, tr_fib S = -Pm - 2Pss",
      Z(rho - (Pff+Pm+Pss)/2) and Z(sum(S[a,a] for a in SIG) - (Pss - Pff)) and Z(sum(S[a,a] for a in FIB) + Pm + 2*Pss))
def lp_cert(b, primal, y):
    # primal: dict index->value (>=0); dual y: A^T y <= c componentwise, b.y = c.x  => exact optimality
    Ax = [sum(COLS[j][2][r]*v for j, v in primal.items()) for r in range(3)]
    feas = all(v >= 0 for v in primal.values()) and Ax == list(b)
    dual_ok = all(sum(col[2][r]*y[r] for r in range(3)) <= col[3] for col in COLS)
    cx = sum(COLS[j][3]*v for j, v in primal.items()); by = sum(b[r]*y[r] for r in range(3))
    return feas and dual_ok and cx == by, cx
idx = {(col[0], col[1]): j for j, col in enumerate(COLS)}
wS_UV, wF_UV, wS_IR, wF_IR = Fr(-1), Fr(-6,5), Fr(-4,3), Fr(-4,3)
# IR-kept pairing (rho_req > 0), per unit rho_req: b = (1, 2 w_Sigma, 4 w_fib)
okU, vU = lp_cert((Fr(1), 2*wS_UV, 4*wF_UV), {idx[("T-",(0,0))]: Fr(1,5), idx[("T+",(0,4))]: Fr(1,5), idx[("T+",(2,4))]: Fr(1)}, (Fr(-1), Fr(0), Fr(-1,4)))
okI, vI = lp_cert((Fr(1), 2*wS_IR, 4*wF_IR), {idx[("T-",(0,0))]: Fr(1,3), idx[("T+",(2,4))]: Fr(4,3)}, (Fr(-1), Fr(0), Fr(-1,4)))
check("J1 IR-kept: minimal negative tension = |1 + w_fib| rho_req exactly: 1/5 (UV end), 1/3 (IR end); exact primal + dual certificate",
      okU and okI and vU == Fr(1,5) and vI == Fr(1,3))
# UV-kept pairing (rho_req < 0): b = -(1, 2 w_Sigma, 4 w_fib)
okU2, vU2 = lp_cert((Fr(-1), -2*wS_UV, -4*wF_UV), {idx[("T+",(0,0))]: Fr(1,5), idx[("T-",(1,4))]: Fr(2,5), idx[("T-",(2,4))]: Fr(4,5)}, (Fr(0), Fr(0), Fr(1,4)))
okI2, vI2 = lp_cert((Fr(-1), -2*wS_IR, -4*wF_IR), {idx[("T+",(0,0))]: Fr(1,3), idx[("T-",(2,4))]: Fr(4,3)}, (Fr(0), Fr(0), Fr(1,4)))
check("J2 UV-kept: minimal negative tension = |w_fib| |rho_req|: 6/5 (UV end), 4/3 (IR end); exact primal + dual certificate",
      okU2 and okI2 and vU2 == Fr(6,5) and vI2 == Fr(4,3))
# fibre-NEC sum identity behind J1: sum_{j in fib} (rho + p_j) = sum_types T (4 - fib) + 2Pff + Pm
Tsym = {ty: sp.Symbol(f"T_{ty[0]}{ty[1]}", real=True) for ty in types}
rho_tot = sum(Tsym.values()) + (Pff+Pm+Pss)/2
trF_tot = sum(-ty[1]*Tsym[ty] for ty in types) - Pm - 2*Pss
check("J3 4 rho + tr_fib S = sum_types T (4 - n_fib) + 2Pff + Pm  (so negative tension with few fibre legs is the only fibre-NEC supply)",
      Z(4*rho_tot + trF_tot - (sum((4-ty[1])*Tsym[ty] for ty in types) + 2*Pff + Pm)))
# wall-filling Lambda is NEC-neutral: S = -Lambda h, h(k,k) = 0 for null k = t + e_j
Lam = sp.Symbol("Lambda", real=True)
kv = sp.Matrix([1] + [0]*9); okL = True
for j in range(1, 10):
    k = kv.copy(); k[j] = 1
    okL = okL and Z((k.T*(-Lam*eta)*k)[0])
check("J4 wall-filling tension Lambda (either sign): S(k,k) = -Lambda h(k,k) = 0 for every null k = t + e_j (NEC-neutral)", okL)

# ---------------- scaling (J1 flow scaling L = l N^(1/3); exponent arithmetic) ----------------
l, N, kk = sp.symbols("ell N k", positive=True)
Lsc = l*N**sp.Rational(1,3)
def m5_units(coeff_pow_l, deriv):    # wall term coefficient l^p, 2k derivatives -> stress l^p L^(-2k); x fibre L^4; / T_M5 = l^-6
    return sp.powsimp(sp.expand_power_base(l**coeff_pow_l * Lsc**(-deriv) * Lsc**4 * l**6, force=True), force=True)
req = sp.powsimp(sp.expand_power_base(l**-9 * Lsc**-1 * Lsc**4 * l**6, force=True), force=True)
check("J5 requirement (1/kappa^2) K x fibre / T_M5 ~ N; wall terms l^(2k-10) R^k: k=0 ~ N^(4/3) (Lambda), k=1 ~ N^(2/3), k=2 ~ N^0, k=3 ~ N^(-2/3)",
      req == N and m5_units(-10, 0) == N**sp.Rational(4,3) and m5_units(-8, 2) == N**sp.Rational(2,3)
      and m5_units(-6, 4) == 1 and m5_units(-4, 6) == N**sp.Rational(-2,3))
# S4: T_M2 ~ l^-3, G ~ l^3 N / L^4, R^3 ~ L^-6 (smooth) or (delta(0)[K])^3 ~ (l^-1 L^-1)^3 (worst case, delta(0) ~ 1/l)
s4_smooth = sp.powsimp(sp.expand_power_base(l**-3 * (l**3*N*Lsc**-4) * Lsc**-6 * Lsc**4 * l**6, force=True), force=True)
s4_delta = sp.powsimp(sp.expand_power_base(l**-3 * (l**3*N*Lsc**-4) * (l**-1*Lsc**-1)**3 * Lsc**4 * l**6, force=True), force=True)
G_orth = sp.powsimp(sp.expand_power_base(l**3*N*Lsc**-4, force=True), force=True)
check("J6 S4 scaling: G ~ 1/L; C^X8 delta-stress ~ N^-1 M5 units (smooth R), ~ N^0 (delta(0) ~ 1/l_P); relative to requirement N: N^-2, N^-1",
      sp.powsimp(G_orth*Lsc, force=True) == 1 and s4_smooth == 1/N and s4_delta == 1
      and sp.powsimp(s4_smooth/req, force=True) == N**-2 and sp.powsimp(s4_delta/req, force=True) == N**-1)

# ---------------- S4: Chern-Weil transgression (representative degree 2, su(2), 4D flat chart) ----------------
ys = sp.symbols("y1:5", real=True); ep = sp.Symbol("epsilon", real=True)
A = [[sp.Function(f"A{a}_{i}")(*ys) for i in range(3)] for a in range(4)]
dA = [[sp.Function(f"dA{a}_{i}")(*ys) for i in range(3)] for a in range(4)]
e3 = lambda i,j,k: sp.LeviCivita(i,j,k)
def Fc(AA, a, b, i):
    return sp.diff(AA[b][i], ys[a]) - sp.diff(AA[a][i], ys[b]) + sum(e3(i,j,k)*AA[a][j]*AA[b][k] for j in range(3) for k in range(3))
Ae = [[A[a][i] + ep*dA[a][i] for i in range(3)] for a in range(4)]
import itertools
perms = [(pm, sp.LeviCivita(*pm)) for pm in itertools.permutations(range(4)) if sp.LeviCivita(*pm) != 0]
FA = [[[Fc(A, a, b, i) for i in range(3)] for b in range(4)] for a in range(4)]
Pe = sum(sg*sum(Fc(Ae, a, b, i)*Fc(Ae, c, d, i) for i in range(3)) for (a,b,c,d), sg in perms)
dP = sp.diff(Pe, ep).subs(ep, 0)
Y3 = sum(sp.diff(sg*sum(FA[a][b][i]*dA[d][i] for i in range(3)), ys[c]) for (a,b,c,d), sg in perms)
check("J7 transgression: delta[eps^abcd F_ab.F_cd] = 4 d_c[eps^abcd F_ab.dA_d] (Bianchi + ad-invariance; so delta of a characteristic form is exact)",
      Z(dP - 4*Y3))

# ---------------- A15: any-face Israel criterion (diagonal K, Poincare along t,x) ----------------
kap2, kx = sp.symbols("kappa2 k_x", real=True)
Ks = sp.symbols("K_s1 K_s2", real=True); Kf = sp.symbols("K_f1:5", real=True)
Kdiag = [-kx, kx, kx, kx, Ks[0], Ks[1], *Kf]      # K_tt = -k_t with k_t = k_x
Ktr = sum(Kdiag[a]*eta[a,a] for a in range(10))   # K = h^ab K_ab
Sd = [-(2/kap2)*(Kdiag[a] - eta[a,a]*Ktr) for a in range(10)]
rho_s = Sd[0]                                     # S_tt
check("J8 any static Poincare face: rho = (2/kappa^2)(k_x - K), and tr_fib S + 4 rho = -(2/kappa^2) sum_f (K_ff - k_t)",
      Z(rho_s - (2/kap2)*(kx - Ktr)) and Z(sum(Sd[a] for a in FIB) + 4*rho_s + (2/kap2)*sum(Kf[i] - kx for i in range(4))))
check("J9 null k = t + e_j: S(k,k) = rho + S_jj = -(2/kappa^2)(K_jj - k_t) for every j (so DEC/NEC sources need K_jj <= k_t on every face)",
      all(Z(rho_s + Sd[j] + (2/kap2)*(Kdiag[j] - kx)) for j in range(1, 10)))

print(f"{npass}/{ntot} PASS")
print("ALL PASS" if ok_all else "SOME FAIL")
raise SystemExit(0 if ok_all else 1)
