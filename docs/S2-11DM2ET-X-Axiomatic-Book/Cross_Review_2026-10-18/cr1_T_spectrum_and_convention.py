# Cross-review check 1 (s=7): (a) T-spectrum multiset predicted by the tensor model of Tensor-Pattern-Closure
# vs the S-Eigenvalues list; V42 raw residues vs true local exponents.  (b) S vs S^{-1} convention on stored matrices.
from fractions import Fraction as Fr
from collections import Counter
import numpy as np
SEIG = "0:1, 3/70:2, 1/14:1, 1/10:1, 19/140:4, 1/7:1, 6/35:2, 13/70:2, 31/140:4, 17/70:2, 1/4:2, 2/7:1, 27/70:2, 11/28:2, 2/5:1, 59/140:4, 33/70:2, 1/2:1, 15/28:2, 19/35:2, 4/7:1, 3/5:1, 9/14:1, 13/20:2, 47/70:2, 24/35:2, 26/35:2, 11/14:1, 111/140:4, 23/28:2, 17/20:2, 31/35:2, 9/10:1, 131/140:4, 34/35:2, 139/140:4"
seig = Counter({Fr(k): int(v) for k, v in (x.strip().split(':') for x in SEIG.split(','))})
# local T exponents (Tensor-Pattern-Closure): T_p = diag e(2x^2/p); T2: 00<->01 swap (eig +1,-1), 10 -> i, 11 -> i
def weil_halves(p):
    ev = Counter(); od = Counter()
    for x in range(p):
        r = Fr(2*x*x % p, p)
        if x == 0: ev[r] += 1
        elif x < p - x: ev[r] += 1; od[r] += 1
    return ev, od
W5p, W5m = weil_halves(5); W7p, W7m = weil_halves(7)
A3 = Counter({Fr(0): 1, Fr(1, 2): 1, Fr(1, 4): 1}); B1 = Counter({Fr(1, 4): 1})
def tens(*cs):
    out = Counter({Fr(0): 1})
    for c in cs:
        new = Counter()
        for a, m in out.items():
            for b, n in c.items(): new[(a + b) % 1] += m*n
        out = new
    return out
pieces = {'V_Eis=A3xW5+xW7+': tens(A3, W5p, W7p), 'V_cusp=B1xW5-xW7-': tens(B1, W5m, W7m),
          'B1xW5+xW7+': tens(B1, W5p, W7p), 'A3xW5-xW7-': tens(A3, W5m, W7m)}
W = Counter()
for c in pieces.values(): W += c
lines = []
lines.append(f"dims: " + ", ".join(f"{k}={sum(v.values())}" for k, v in pieces.items()) + f"; total {sum(W.values())}")
lines.append(f"(a) tensor-model T multiset on Fix(P) == S-Eigenvalues list: {W == seig}")
lines.append(f"    V_Eis simple with 36 distinct values: {all(m == 1 for m in pieces['V_Eis=A3xW5+xW7+'].values()) and len(pieces['V_Eis=A3xW5+xW7+']) == 36}")
lines.append(f"    V_cusp values (x140): {sorted(int(r*140) for r in pieces['V_cusp=B1xW5-xW7-'])}")
# V42 raw residues a mod p vs true local exponents (x4=3a mod 4, x5=2a mod 5, x7=6a mod 7)
cusp = [19, 31, 59, 111, 131, 139]
lines.append(f"    V42 raw residues for V_cusp: mod4 {sorted({a%4 for a in cusp})}, mod5 {sorted({a%5 for a in cusp})}, mod7 {sorted({a%7 for a in cusp})}")
lines.append(f"    true local exps for V_cusp:  x4 {sorted({3*a%4 for a in cusp})}, x5 {sorted({2*a%5 for a in cusp})}, x7 {sorted({6*a%7 for a in cusp})}")
lines.append(f"    quadratic residue check: 2 is a square mod 7: {any(x*x%7==2 for x in range(7))}; 2 square mod 5: {any(x*x%5==2 for x in range(5))}; 3 square mod 7: {any(x*x%7==3 for x in range(7))}")
# (b) conventions on stored matrices
base = '../2026-10-18-s8-s11/'
for s in (7, 8, 11):
    S = np.load(base + f'S_{s}.npy'); T = np.load(base + f'T_{s}.npy'); P = np.load(base + f'P_{s}.npy'); I = np.eye(len(S))
    Si = np.linalg.inv(S)
    n = lambda X: np.linalg.norm(X)
    lines.append(f"(b) s={s}: |S^2-P|={n(S@S-P):.1e} |(ST)^3-I|={n(np.linalg.matrix_power(S@T,3)-I):.1e} |(ST)^3-S^2|={n(np.linalg.matrix_power(S@T,3)-S@S):.1e} "
                 f"|(S^-1 T)^3 - S^-2|={n(np.linalg.matrix_power(Si@T,3)-Si@Si):.1e} |P-I|={n(P-I):.1e}")
print("\n".join(lines)); open('cr1_T_spectrum_and_convention.txt', 'w').write("\n".join(lines) + "\n")
