# Finite checks used in the obstruction theorems.
import numpy as np, math, cmath, sys, pickle
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
PC = '/workspace/quantum-comp/reports/heavy-daily/2026-10-17-psi-conditions/'
sys.path.insert(0, PC)
from family import LABELS, IDX
S = np.load(PC+'S_matrix.npy'); T = np.load(PC+'T_matrix.npy')
cm = pickle.load(open('/workspace/quantum-comp/reports/heavy-daily/2026-10-18-PARI-free/char_match.pkl', 'rb')); C = set(cm['C'])
out = []; P = lambda s: (print(s, flush=True), out.append(s))
iL = IDX[((49, 56), (0, 0))]
P(f"(a,0) = E_L is label #{iL}; in the PARI-free cusp set: {iL in C}")
supp = set(np.nonzero(np.abs(S[iL]) > 1e-12)[0].tolist())
P(f"S-row of (a,0): {len(supp)} entries, all Eisenstein labels: {not (supp & C)}; T-row Eisenstein: {not (set(np.nonzero(np.abs(T[iL])>1e-12)[0].tolist()) & C)}")
# Eisenstein subspace closed under S, T  =>  every cocycle of E_L involves only Eisenstein rows (no cusp L(0) values)
Eset = sorted(set(range(140)) - C)
P(f"(label-level S is not block-diagonal in general: max|S[cusp,Eis]| = {np.abs(S[np.ix_(sorted(C), Eset)]).max():.2f}; the Eis/cusp split is respected on the functions, PARI-free cert. For the row used here, (a,0), every S-partner is an Eisenstein label.)")
# order of T
M = None; Tp = np.eye(140, dtype=complex)
for n in range(1, 2000):
    Tp = Tp @ T
    if np.abs(Tp - np.eye(140)).max() < 1e-9: M = n; break
P(f"order of the T matrix on the 140-label family: {M}")
Si = np.linalg.inv(S)
for c in (M, 2*M):
    rg = Si @ np.linalg.matrix_power(np.linalg.inv(T), c) @ S
    P(f"rho([[1,0],[{c},1]]) = S^-1 T^-{c} S equals identity: max dev {np.abs(rg-np.eye(140)).max():.1e}")
# Gamma_W law for the C_third singular coefficient I*G(x):  G(gx) |cx+1| e(-7(gx-x)/20) / G(x) == 1 ?
def G(h, m):
    n, k = np.meshgrid(np.arange(2*m), np.arange(2*m), indexing='ij')
    Q = n*n + 7*n*k + (7*k*(k+1))//2
    return complex(np.exp(2j*np.pi*((h*Q) % m)/m).mean())
c = M
ratios = []; phases = []
for (h, m) in [(1, 3), (2, 3), (1, 7), (3, 7), (1, 9), (2, 9), (1, 11), (3, 13), (-1, 3), (-2, 7), (1, 1), (-1, 1), (4, 21)]:
    x = Fr(h, m); gx = x/(c*x+1)
    if math.gcd(gx.denominator, 10) != 1 or math.gcd(m, 10) != 1: continue
    g0 = G(x.numerator, x.denominator); g1v = G(gx.numerator, gx.denominator)
    fac = cmath.exp(-2j*math.pi*float((Fr(7, 20)*(gx-x)) % 1))
    R = g1v*abs(float(c*x+1))*fac/g0
    ratios.append((str(x), R)); phases.append(float((Fr(7, 20)*(gx - x)) % 1))
P(f"C_third singular law under gamma = [[1,0],[{c},1]] (in the kernel of the Weil representation):")
P("   G(gx)|cx+1| e(-7(gx-x)/20)/G(x) = " + ", ".join(f"{x}: {R.real:+.12f}{R.imag:+.1e}i" for x, R in ratios))
P("   => G(gx) = e(7(gx-x)/20) G(x)/|cx+1|; the extra phase e(7(gx-x)/20) takes the values (turns) " + ", ".join(f"{p:.6f}" for p in phases[:8]) + ": not constant, so no constant multiplier.")
# E_L itself (no q^{7/20}): G_a(x) = e(-7x/20) G(x) obeys the clean law G_a(gx) = G_a(x)/|cx+1|
P("   equivalently G_a(gx)|cx+1|/G_a(x) = 1 for G_a := e(-7x/20)G (the E_L singular coefficient): " + ", ".join(f"{(R).real:+.10f}" for _, R in ratios))
# Hypotheses of the neg-side argument: E_L and E_R have real Fourier coefficients
import importlib
P(f"zwegers data: c1=(-1/5,1/5): Q(c1) = {Fr(1,2)*(2*Fr(1,25)+14*Fr(-1,5)*Fr(1,5)+7*Fr(1,25))}; c2=(-1/5,2/35): Q(c2) = {Fr(1,2)*(2*Fr(1,25)+14*Fr(-1,5)*Fr(2,35)+7*Fr(4,1225))}; B(c1,c2) = {Fr(-1,5)*(2*Fr(-1,5)+7*Fr(2,35)) + Fr(1,5)*(7*Fr(-1,5)+7*Fr(2,35))}")
open('obstruction_checks.txt', 'w').write("\n".join(out)+"\n")
