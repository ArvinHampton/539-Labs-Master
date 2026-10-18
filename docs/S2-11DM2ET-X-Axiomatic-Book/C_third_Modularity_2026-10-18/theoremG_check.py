# Check of Theorem G (Gauss mean G(h/m) = 0 iff 2|m or 5|m) for all reduced h/m, m <= 60.
import numpy as np, math
def G(h, m):
    n, k = np.meshgrid(np.arange(2*m), np.arange(2*m), indexing='ij')
    Q = n*n + 7*n*k + (7*k*(k+1))//2
    return complex(np.exp(2j*np.pi*((h*Q) % m)/m).mean())
bad = 0; tot = 0; zeros = 0
for m in range(1, 61):
    for h in range(m):
        if math.gcd(h, m) != 1: continue
        tot += 1
        z = abs(G(h, m)) < 1e-9
        zeros += z
        if z != (m % 2 == 0 or m % 5 == 0): bad += 1
s = f"Theorem G check, reduced h/m with m<=60: {tot} rationals, {zeros} zeros, mismatches with (2|m or 5|m): {bad}"
print(s); open('theoremG_check.txt','w').write(s+"\n")
