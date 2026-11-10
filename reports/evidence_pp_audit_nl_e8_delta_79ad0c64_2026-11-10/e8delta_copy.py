# NL derived proposal - E8 instanton stress vs geometric delta under odd G4 (2026-11-10)
# Exact tests only: every zero test is expand(...) on a polynomial with exact
# coefficients, or exact Rational comparison. No simplify()==0, no allclose.
import sympy as sp
from fractions import Fraction as Fr

def Z(e):
    """exact zero test for polynomial/rational expressions (expand, no simplify)"""
    return sp.expand(e) == 0

ok_all = True
def check(name, cond):
    global ok_all
    ok_all = ok_all and bool(cond)
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")

# 10D wall orthonormal frame: 0=t, 1..3=x, 4,5=Sigma, 6..9=fibre
D = 10
eta = sp.diag(-1, *([1]*9))
WV_X = [1,2,3]; SIG = [4,5]; FIB = [6,7,8,9]; Y6 = SIG+FIB

def stress(F):
    """YM stress per Lie generator (lambda=1): S_ab = F_ac F_b^c - 1/4 h_ab F_cd F^cd.
    tr over generators with positive Killing form = sum of copies, so one generator is general."""
    Fup = eta*F*eta          # F^{ab}
    F2 = sum(F[a,b]*Fup[a,b] for a in range(D) for b in range(D))
    S = sp.zeros(D,D)
    for a in range(D):
        for b in range(D):
            S[a,b] = sum(F[a,c]*F[b,d]*eta[c,d] for c in range(D) for d in range(D)) - sp.Rational(1,4)*eta[a,b]*F2
    return S, F2

# ---- C1: general static magnetic field with legs only on Y6 (Sigma+fibre) ----
F = sp.zeros(D,D); syms = {}
for i,a in enumerate(Y6):
    for b in Y6[i+1:]:
        s = sp.Symbol(f"F{a}{b}", real=True); syms[(a,b)] = s
        F[a,b] = s; F[b,a] = -s
S, F2 = stress(F)
rho = sp.Rational(1,4)*F2
check("C1a x-block S_mu nu = -rho eta_mu nu (t,x)", all(Z(S[m,n] + rho*eta[m,n]) for m in [0]+WV_X for n in [0]+WV_X))
check("C1b trace h^ab S_ab = -6 rho", Z(sum(eta[a,a]*S[a,a] for a in range(D)) + 6*rho))
check("C1c rho = 1/2 sum_{a<b} F_ab^2 >= 0 (sum of squares)", Z(rho - sp.Rational(1,2)*sum(v**2 for v in syms.values())))
# block formulas: S_ab = sum_c F_ac F_bc - rho delta_ab on Y6
check("C1d Y6 blocks S_ab = sum_c F_ac F_bc - rho delta_ab (Sigma, fibre, mixed)",
      all(Z(S[a,b] - (sum(F[a,c]*F[b,c] for c in Y6) - rho*(1 if a==b else 0))) for a in Y6 for b in Y6))
check("C1e x-Y6 and t-Y6 mixed blocks vanish", all(Z(S[m,a]) for m in [0]+WV_X for a in Y6))
# per-direction NEC on Y6 directions and Sigma-minus-x identity
check("C1f S_aa + rho = |F(e_a,.)|^2 >= 0 for every Y6 direction a (w_a >= -1)",
      all(Z(S[a,a] + rho - sum(F[a,c]**2 for c in Y6)) for a in Y6))
check("C1g S^Sigma_Sigma - S^x_x = |F(e_sigma,.)|^2 >= 0", all(Z(S[s,s]-S[1,1] - sum(F[s,c]**2 for c in Y6)) for s in SIG))

# ---- C2: fibre-only self-dual field ----
a_,b_,c_ = sp.symbols("a b c", real=True)
Fsd = sp.zeros(D,D)
def setF(M,i,j,v): M[i,j]=v; M[j,i]=-v
f1,f2,f3,f4 = FIB
setF(Fsd,f1,f2,a_); setF(Fsd,f3,f4,a_)
setF(Fsd,f1,f3,b_); setF(Fsd,f4,f2,b_)
setF(Fsd,f1,f4,c_); setF(Fsd,f2,f3,c_)
Ssd, F2sd = stress(Fsd); rsd = sp.Rational(1,4)*F2sd
check("C2a SD fibre block = 0", all(Z(Ssd[a,b]) for a in FIB for b in FIB))
check("C2b SD mixed blocks = 0", all(Z(Ssd[a,b]) for a in FIB for b in range(D) if b not in FIB))
check("C2c SD worldvolume (t,x,Sigma) block = -rho h", all(Z(Ssd[m,n] + rsd*eta[m,n]) for m in [0]+WV_X+SIG for n in [0]+WV_X+SIG))
# topological density q = (F^F)/vol4 = 2(F12F34 - F13F24 + F14F23)
def qdens(M):
    return 2*(M[f1,f2]*M[f3,f4] - M[f1,f3]*M[f2,f4] + M[f1,f4]*M[f2,f3])
check("C2d SD pointwise saturation rho = q/2 (energy density = topological density)", Z(rsd - qdens(Fsd)/2))
# general fibre-only field: Bogomolny pointwise identity rho - q/2 = 1/4 sum_{a<b}(F - *F)_ab^2
Fg = sp.zeros(D,D); gs = []
for i,a in enumerate(FIB):
    for b in FIB[i+1:]:
        s = sp.Symbol(f"G{a}{b}", real=True); gs.append(s); setF(Fg,a,b,s)
Sg, F2g = stress(Fg); rg = sp.Rational(1,4)*F2g
star = {(f1,f2):(f3,f4),(f1,f3):(f4,f2),(f1,f4):(f2,f3),(f3,f4):(f1,f2),(f4,f2):(f1,f3),(f2,f3):(f1,f4)}
asd2 = sum((Fg[p]-Fg[star[p]])**2 for p in [(f1,f2),(f1,f3),(f1,f4)])  # each ASD component counted once
check("C2e pointwise Bogomolny: rho - q/2 = 1/2 sum_{3 pairs}(F - *F)^2 >= 0", Z(rg - qdens(Fg)/2 - sp.Rational(1,2)*asd2))
check("C2f general fibre-only field: fibre block traceless", Z(sum(Sg[a,a] for a in FIB)))

# ---- C3: NEC with electric legs, k = t + e_j ----
Fe = sp.zeros(D,D); es=[]
for i in range(D):
    for j in range(i+1,D):
        s = sp.Symbol(f"E{i}_{j}", real=True); es.append(s); setF(Fe,i,j,s)
Se,_ = stress(Fe)
okc3 = True
for j in range(1,D):
    k = sp.zeros(D,1); k[0]=1; k[j]=1
    Skk = (k.T*Se*k)[0,0]
    v = [sum(Fe[a,b]*k[a] for a in range(D)) for b in range(D)]  # v_b = F(k, e_b)
    # v_0 = -v_j  (F(k,k)=0); claimed S(k,k) = sum_{c != 0,j} v_c^2
    okc3 = okc3 and Z(Skk - sum(v[c]**2 for c in range(1,D) if c!=j)) and Z(v[0]+v[j])
check("C3 any field (electric legs allowed): S(k,k) = sum_{c not in {t,j}} F(k,e_c)^2 >= 0", okc3)

# ---- C4: normalisation u and bookkeeping (exact) ----
pi = sp.pi
TM5 = (2*pi)**-5
for lab,lam2 in [("HW printed", (2*pi)**7), ("Conrad/Lu", 2*(2*pi)**7)]:
    u = sp.nsimplify(8*pi**2/(lam2*TM5))
    print(f"   u[{lab}] = {u}")
check("C4a u = 2 (HW printed lambda^2=(2pi)^7), u = 1 (lambda^2 = 2(2pi)^7)",
      sp.nsimplify(8*pi**2/((2*pi)**7*TM5)) == 2 and sp.nsimplify(8*pi**2/(2*(2*pi)**7*TM5)) == 1)
N, n, u, eps = sp.symbols("N n u eps", nonnegative=True)
NM5 = 2*N - n                     # charge: N_M5 + n_inst = 2 N_flux
T = NM5 + u*n + eps               # tension in M5 units (BPS part + non-BPS excess)
check("C4b tension = 2N + (u-1) n + eps (symbolic)", Z(T - (2*N + (u-1)*n + eps)))
check("C4c u=1: tension independent of the split n (dT/dn = 0)", Z(sp.diff(T.subs(u,1), n)))
Nf = 4880; Q = 2*Nf
check("C4d 2 N_flux = 9760", Q == 9760)
# on-record N_req values (CONDITIONAL inputs from NL 1711 AB2 / PP fe0c3d92), Fractions from the printed decimals
rec = {"MN2": Fr("12568.6"), "MN1": Fr("12252.1"), "z=2": Fr("12812.2"), "z=3": Fr("12942.4"), "UV": Fr(10*Nf,3)}
for kk,v in rec.items():
    d = v - Q
    print(f"   {kk}: N_req={float(v):.1f}  Delta_N={float(d):.1f}  ratio={float(v/Q):.4f}  n_needed(u=2,BPS)={float(d):.1f} <= 9760: {d<=Q}")
check("C4e UV: N_req/(2N) = 5/3 exactly and Delta_N = (2/3)*9760", rec["UV"]/Q == Fr(5,3) and rec["UV"]-Q == Fr(2,3)*Q)
check("C4f u=2 BPS split would need n_inst = Delta_N <= 9760 on every listed face", all(v-Q <= Q for v in rec.values()))
# minimal u for which a BPS split can reach Delta_N with n <= 2N: u >= 1 + Delta/(2N)
check("C4g BPS reach needs u >= 1 + Delta_N/(2N); at UV end u >= 5/3", 1 + (rec["UV"]-Q)/Q == Fr(5,3))

# ---- C5: odd-Z2 doubling (downstairs) cancels in the tension/charge ratio ----
Kp, S0, Gp, q0, kap = sp.symbols("Kp S0 Gp q0 kappa", positive=True)
# upstairs: [K] = K+ - K- = 2K+ (Z2), [K] ~ -kappa^2 S ; odd G: [G] = 2G+ ~ q
r_up = (2*Kp)/(2*Gp); r_dn = Kp/Gp
check("C5 Z2 doubling of [K] and of [G_tan] cancels in tension/charge", Z(r_up - r_dn))

# ---- C6: end-face fibre deficit vs any YM+M5 content (exact, given J1 T0 values) ----
wfib_UV = Fr(-6,5); wfib_IR = Fr(-4,3)
check("C6 required w_fib (UV -6/5, IR -4/3) < -1 <= w_a of any YM + positive-tension brane", wfib_UV < -1 and wfib_IR < -1)

print("ALL PASS" if ok_all else "SOME FAIL")
