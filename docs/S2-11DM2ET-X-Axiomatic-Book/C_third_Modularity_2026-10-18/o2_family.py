# Input for Theorem O2: closed form G(1/m) = e(7*inv20_m/m) * (35/m) / m  for gcd(m,70)=1  (inv20_m = 20^{-1} mod m),
# hence G(1/m) = e(7/(20m)) * P(m mod 140)/m with P periodic, while |cx+1| = (3+140n)/3 along x_n = 1/(3+140n) = gamma0^n(1/3).
import numpy as np, cmath, math
from sympy import jacobi_symbol
def G(h, m):
    n, k = np.meshgrid(np.arange(2*m, dtype=np.int64), np.arange(2*m, dtype=np.int64), indexing='ij')
    Q = n*n + 7*n*k + (7*k*(k+1))//2
    return complex(np.exp(2j*np.pi*((h*Q) % m)/m).mean())
out = []; bad = 0
for m in [3, 9, 11, 13, 17, 19, 23, 27, 29, 31, 33, 37, 41, 143, 283, 423, 563]:
    if math.gcd(m, 70) != 1: continue
    closed = cmath.exp(2j*math.pi*7*pow(20, -1, m)/m)*int(jacobi_symbol(35, m))/m
    g = G(1, m); d = abs(g - closed); bad += int(float(d) > 1e-10)
    Pm = g*m*cmath.exp(-2j*math.pi*7/(20*m))          # should depend only on m mod 140
    out.append(f"m={m:4d} (m mod 140 = {m%140:3d}): G(1/m)={g:.10f}  closed form diff {d:.1e}  P = m e(-7/(20m)) G(1/m) = {Pm:.10f}")
out.append(f"mismatches: {bad}")
print("\n".join(out)); open('o2_family.txt','w').write("\n".join(out)+"\n")
