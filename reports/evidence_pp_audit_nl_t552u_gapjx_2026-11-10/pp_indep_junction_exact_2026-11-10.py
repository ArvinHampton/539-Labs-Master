# PP independent exact checks for NL junction filing dff93e21 (t552u). Audit-side checks only; not a first proof.
# Tools: sympy expand()==0, exact Matrix algebra, fractions.Fraction (incl. an exact vertex-enumeration LP solve),
# exponent arithmetic in Fractions. No simplify, no powsimp, no nsimplify, no floats, no numpy, no allclose.
import sympy as sp, itertools
from fractions import Fraction as Fr
res = []
def chk(name, cond):
    c = bool(cond); res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {name}")
def Z(e): return sp.expand(e) == 0

# ---- J0: YM stress for a general magnetic Y6 field (independent re-implementation, mostly-plus eta, D = 10)
D = 10; eta = sp.diag(-1, *([1]*9)); SIG = [4,5]; FIB = [6,7,8,9]; Y6 = SIG + FIB
F = sp.zeros(D, D); Pff = Pm = Pss = 0
for a_, b_ in itertools.combinations(Y6, 2):
    v = sp.Symbol(f"G{a_}_{b_}", real=True); F[a_, b_] = v; F[b_, a_] = -v
    if a_ in FIB and b_ in FIB: Pff += v**2
    elif a_ in SIG and b_ in SIG: Pss += v**2
    else: Pm += v**2
Finv = eta.inv()
F2 = (F*Finv*F.T*Finv).trace()             # F_ab F^ab
Tm = F*Finv*F.T - sp.Rational(1,4)*eta*F2  # T_ab = F_ac F_b^c - 1/4 eta_ab F^2
chk("PJ0 J0: rho = T_tt = (Pff+Pm+Pss)/2 ; tr_Sigma T = Pss - Pff ; tr_fib T = -Pm - 2Pss ; T_tj = 0",
    Z(Tm[0,0] - (Pff+Pm+Pss)/2) and Z(sum(Tm[i,i] for i in SIG) - (Pss - Pff)) and Z(sum(Tm[i,i] for i in FIB) + Pm + 2*Pss)
    and all(Z(Tm[0,j]) for j in range(1,10)))

# ---- J3 identity (types (sig,fib), tension T of either sign)
types = [(s_, f_) for s_ in range(3) for f_ in range(5)]
Ts = {t: sp.Symbol(f"T{t[0]}{t[1]}", real=True) for t in types}
rho = sum(Ts.values()) + (Pff+Pm+Pss)/2
trf = sum(-t[1]*Ts[t] for t in types) - Pm - 2*Pss
trs = sum(-t[0]*Ts[t] for t in types) + Pss - Pff
chk("PJ1 J3: 4 rho + tr_fib S = sum T (4 - n_fib) + 2Pff + Pm", Z(4*rho + trf - sum((4-t[1])*Ts[t] for t in types) - 2*Pff - Pm))

# ---- GA9-1/2: exact LP solved independently by full vertex enumeration (3 equality rows), Fractions only.
# variables: T+ (cost 0), T- (cost 1) for each type, Pff, Pm, Pss (cost 0), all >= 0. Rows: rho, tr_Sigma, tr_fib.
cols = []
for t in types: cols.append(((Fr(1), Fr(-t[0]), Fr(-t[1])), Fr(0), ("T+",)+t))
for t in types: cols.append(((Fr(-1), Fr(t[0]), Fr(t[1])), Fr(1), ("T-",)+t))
cols += [((Fr(1,2), Fr(-1), Fr(0)), Fr(0), ("Pff",)), ((Fr(1,2), Fr(0), Fr(-1)), Fr(0), ("Pm",)), ((Fr(1,2), Fr(1), Fr(-2)), Fr(0), ("Pss",))]
def solve3(A, bb):
    M = [list(A[i]) + [bb[i]] for i in range(3)]
    for c_ in range(3):
        piv = next((r_ for r_ in range(c_, 3) if M[r_][c_] != 0), None)
        if piv is None: return None
        M[c_], M[piv] = M[piv], M[c_]
        for r_ in range(3):
            if r_ != c_ and M[r_][c_] != 0:
                fct = M[r_][c_] / M[c_][c_]; M[r_] = [M[r_][k] - fct*M[c_][k] for k in range(4)]
    return [M[i][3]/M[i][i] for i in range(3)]
def lp_min(bb):
    best = None
    for J in itertools.combinations(range(len(cols)), 3):
        A = [[cols[j][0][r_] for j in J] for r_ in range(3)]
        xs = solve3(A, bb)
        if xs is None or any(v < 0 for v in xs): continue
        val = sum(cols[j][1]*xs[k] for k, j in enumerate(J))
        if best is None or val < best: best = val
    return best
def dual_ok(y):   # A^T y <= c for every column => weak-duality lower bound b.y (LP bounded below)
    return all(sum(col[0][r_]*y[r_] for r_ in range(3)) <= col[1] for col in cols)
wS_UV, wF_UV, wS_IR, wF_IR = Fr(-1), Fr(-6,5), Fr(-4,3), Fr(-4,3)    # J1 end-face inputs (CONDITIONAL)
bU = (Fr(1), 2*wS_UV, 4*wF_UV); bI = (Fr(1), 2*wS_IR, 4*wF_IR)
yIR = (Fr(-1), Fr(0), Fr(-1,4)); yUV = (Fr(0), Fr(0), Fr(1,4))
bdot = lambda bb, y: sum(bb[i]*y[i] for i in range(3))
mU, mI = lp_min(bU), lp_min(bI)
chk("PJ2 GA9-1 (IR-kept, per unit rho_req>0): vertex-enumeration LP minimum of total negative tension = 1/5 (UV end), 1/3 (IR end); NL dual y=(-1,0,-1/4) feasible with b.y equal",
    mU == Fr(1,5) and mI == Fr(1,3) and dual_ok(yIR) and bdot(bU, yIR) == Fr(1,5) and bdot(bI, yIR) == Fr(1,3)
    and mU == -(1 + wF_UV) and mI == -(1 + wF_IR))
bU2 = tuple(-v for v in bU); bI2 = tuple(-v for v in bI)
mU2, mI2 = lp_min(bU2), lp_min(bI2)
chk("PJ3 GA9-2 (UV-kept, per unit |rho_req|): LP minimum = 6/5 (UV end), 4/3 (IR end) = |w_fib|; NL dual y=(0,0,1/4) feasible with b.y equal",
    mU2 == Fr(6,5) and mI2 == Fr(4,3) and dual_ok(yUV) and bdot(bU2, yUV) == Fr(6,5) and bdot(bI2, yUV) == Fr(4,3))
# boundedness/ sanity: LP restricted to positive-tension + YM columns only is infeasible at both ends, both pairings (=> negative tension is necessary within the model)
def feasible_pos_only(bb):
    for J in itertools.combinations([j for j, c_ in enumerate(cols) if c_[2][0] != "T-"], 3):
        A = [[cols[j][0][r_] for j in J] for r_ in range(3)]
        xs = solve3(A, bb)
        if xs is not None and all(v >= 0 for v in xs): return True
    return False
chk("PJ4 within the model, no nonnegative combination of positive-tension types + magnetic YM meets any of the four end-face demands (vertex check; Farkas via the duals above)",
    not any(feasible_pos_only(bb) for bb in (bU, bI, bU2, bI2)))
# ---- §1 end-face demands S(k,k) = (1 + w_j) rho_req
chk("PJ5 §1: 1 + w = -1/5 (UV fib), 0 (UV Sigma), -1/3 (IR fib and Sigma)", 1 + wF_UV == Fr(-1,5) and 1 + wS_UV == 0 and 1 + wF_IR == Fr(-1,3) and 1 + wS_IR == Fr(-1,3))

# ---- J4 Lambda NEC-neutral: S = -Lambda h ; h(k,k) = 0 for null k = t + e, any unit e (general e, reduced mod |e|^2 = 1)
Lam = sp.Symbol("Lambda", real=True); ev = sp.Matrix([0] + list(sp.symbols("e1:10", real=True)))
kvec = sp.Matrix([1] + [0]*9) + ev
nrm = sum(ev[i]**2 for i in range(1,10))
chk("PJ6 J4: S(k,k) = -Lambda eta(k,k) = -Lambda(|e|^2 - 1) = 0 on |e| = 1, for every spatial unit e (not only basis vectors)",
    Z((kvec.T*(-Lam*eta)*kvec)[0] + Lam*(nrm - 1)))

# ---- J8/J9 Israel algebra with a GENERAL symmetric Y6 block of K (off-diagonals allowed), Poincare block k eta on (t,x1..x3), K_tj = 0
kap2, k = sp.symbols("kappa2 k", real=True)
K = sp.zeros(10, 10)
for i in range(4): K[i, i] = k*eta[i, i]
for i, j in itertools.combinations_with_replacement(range(4, 10), 2):
    v = sp.Symbol(f"K{i}_{j}", real=True); K[i, j] = v; K[j, i] = v
Ktr = (eta.inv()*K).trace()
S = -(2/kap2)*(K - eta*Ktr)
evY = sp.Matrix([0]*4 + list(sp.symbols("u4:10", real=True)))
kY = sp.Matrix([1] + [0]*9) + evY
nY = sum(evY[i]**2 for i in range(4, 10))
KYY = (evY.T*K*evY)[0]
chk("PJ7 J8: rho = S_tt = (2/kappa^2)(k - K) ; tr_fib S + 4 rho = -(2/kappa^2) sum_f (K_ff - k)",
    Z(S[0,0] - (2/kap2)*(k - Ktr)) and Z(sum(S[i,i] for i in FIB) + 4*S[0,0] + (2/kap2)*sum(K[i,i] - k for i in FIB)))
chk("PJ8 J9 general: for k = t + e, e any Y6 unit vector: S(k,k) = -(2/kappa^2)(K(e,e) - k) (mod |e|^2 = 1); so NEC sources need max eig(K|Y6) <= k_t",
    Z((kY.T*S*kY)[0] + (2/kap2)*(KYY - k) - (2/kap2)*Ktr*(nY - 1)))

# ---- J5/J6 exponent arithmetic. Monomial l^A N^B stored as (A, B); L = l N^(1/3).
def mul(*ms): return (sum(m[0] for m in ms), sum(m[1] for m in ms))
def pw(m, p): return (m[0]*p, m[1]*p)
l = (Fr(1), Fr(0)); N = (Fr(0), Fr(1)); L = (Fr(1), Fr(1,3)); one = (Fr(0), Fr(0))
inv_TM5 = pw(l, 6)
req = mul(pw(l, -9), pw(L, -1), pw(L, 4), inv_TM5)
wall = lambda kk: mul(pw(l, 2*kk - 10), pw(L, -2*kk), pw(L, 4), inv_TM5)
chk("PJ9 J5: requirement ~ N^1 ; 2k-derivative wall term ~ N^((4-2k)/3) for k = 0..4 (relative N^((1-2k)/3))",
    req == N and all(wall(kk) == (Fr(0), Fr(4 - 2*kk, 3)) for kk in range(5)))
G = mul(pw(l, 3), N, pw(L, -4))
smooth = mul(pw(l, -3), G, pw(L, -6), pw(L, 4), inv_TM5)
delta = mul(pw(l, -3), G, pw(mul(pw(l, -1), pw(L, -1)), 3), pw(L, 4), inv_TM5)
chk("PJ10 J6: G ~ L^-1 ; C^X8 delta-stress ~ N^-1 (smooth R), N^0 (delta(0) ~ 1/l_P each factor); relative to requirement N^-2, N^-1 (given those scaling premises only)",
    mul(G, L) == one and smooth == (Fr(0), Fr(-1)) and delta == one and mul(smooth, pw(req, -1)) == (Fr(0), Fr(-2)) and mul(delta, pw(req, -1)) == (Fr(0), Fr(-1)))

# ---- S4-1 representative transgression, independent matrix (Pauli) realization of su(2), 4D flat chart
ys = sp.symbols("y1:5", real=True); epv = sp.Symbol("epsv", real=True)
Tg = [-sp.I/2*sp.Matrix([[0,1],[1,0]]), -sp.I/2*sp.Matrix([[0,-sp.I],[sp.I,0]]), -sp.I/2*sp.Matrix([[1,0],[0,-1]])]
Ac = [[sp.Function(f"B{m}_{i}")(*ys) for i in range(3)] for m in range(4)]
dAc = [[sp.Function(f"dB{m}_{i}")(*ys) for i in range(3)] for m in range(4)]
Am = lambda AA, m: sum((AA[m][i]*Tg[i] for i in range(3)), sp.zeros(2,2))
def Fm(AA, m, nu):
    return sp.Matrix(2,2, lambda r_, c_: sp.diff(Am(AA,nu)[r_,c_], ys[m]) - sp.diff(Am(AA,m)[r_,c_], ys[nu])) + Am(AA,m)*Am(AA,nu) - Am(AA,nu)*Am(AA,m)
Ae = [[Ac[m][i] + epv*dAc[m][i] for i in range(3)] for m in range(4)]
perms = [(pm, sp.LeviCivita(*pm)) for pm in itertools.permutations(range(4)) if sp.LeviCivita(*pm) != 0]
Fe = {(m,nu): Fm(Ae, m, nu) for m in range(4) for nu in range(4)}
F0 = {(m,nu): Fm(Ac, m, nu) for m in range(4) for nu in range(4)}
Pe = sum(sg*(Fe[(a_,b_)]*Fe[(c_,d_)]).trace() for (a_,b_,c_,d_), sg in perms)
dP = sp.diff(Pe, epv).subs(epv, 0)
dAm = lambda m: sum((dAc[m][i]*Tg[i] for i in range(3)), sp.zeros(2,2))
Y3 = sum(sg*sp.diff((F0[(a_,b_)]*dAm(d_)).trace(), ys[c_]) for (a_,b_,c_,d_), sg in perms)
chk("PJ11 S4-1 rep. (independent Pauli-matrix realization): delta[eps tr F F] = 4 d_c[eps tr(F_ab dA_d)]", Z(dP - 4*Y3))

print(f"{sum(res)}/{len(res)} PASS")
print("ALL PASS" if all(res) else "SOME FAIL")
raise SystemExit(0 if all(res) else 1)
