# Does the x-dependent W_7 phase of the earlier residual-law report come from the q^{7/20} shift?
# Test: ratio G(x) / (7^{-1/2} (7x) G(-1/(7x))) * e(-7(x - W7x)/20)  should take finitely many values (Weil-law phases).
import numpy as np, math, cmath
from fractions import Fraction as Fr
def G(x):
    h, m = x.numerator, x.denominator
    n, k = np.meshgrid(np.arange(2*m), np.arange(2*m), indexing='ij')
    Q = n*n + 7*n*k + (7*k*(k+1))//2
    return complex(np.exp(2j*np.pi*((h*Q) % m)/m).mean())
raw = []; corr = []
for m in range(1, 30):
    for h in range(1, 2*m):
        x = Fr(h, m)
        if math.gcd(h, m) != 1: continue
        w = -1/(7*x)
        g1, g2 = G(x), G(w)
        if abs(g1) < 1e-9 or abs(g2) < 1e-9: continue
        r = g1/(7**-0.5*float(7*x)*g2)
        raw.append(round((cmath.phase(r)/(2*math.pi)) % 1, 6))
        c = r*cmath.exp(-2j*math.pi*float((Fr(7, 20)*(x - w)) % 1))
        corr.append(round((cmath.phase(c)/(2*math.pi)) % 1, 6))
out = [f"pairs with G(x), G(W7 x) both nonzero (x = h/m, m < 30, 0 < x < 2): {len(raw)}",
       f"distinct raw phases (turns) of G(x)/(7^-1/2 (7x) G(W7x)): {len(set(raw))}",
       f"distinct phases after removing e(7(x - W7x)/20): {len(set(corr))}: {sorted(set(corr))[:12]}"]
print("\n".join(out)); open('w7_explain.txt', 'w').write("\n".join(out)+"\n")
