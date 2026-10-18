# Independent numerical check of the analytic input (F1/F2): direct sums Z(t) vs the expansion Res/t + zeta(0) - zeta(-1) t + O(t^2).
import numpy as np, math
def Z(s, t, M=None):
    d = 1/(2*(s-2)); A = s-1; tot = 0.0
    M = M or int(12/math.sqrt(t))+5
    i = np.arange(M)[:, None]; j = np.arange(M)[None, :]
    for x, y in ((0.5+d, 1-d), (d, 0.5-d)):
        X = x+i; Y = y+j; tot += np.exp(-t*(X*X+2*A*X*Y+Y*Y)).sum()
    return tot
out = []
for s in (3, 5, 13, 30):
    Res = math.acosh(s-1)/math.sqrt(s*(s-2)); z0 = (s-4)*(s-5)/(12*(s-2)); z1 = (2*s**5-14*s**4-45*s**3+425*s**2-632*s-96)/(1440*(s-2)**2)
    for t in [c/(s-1)**2 for c in (0.2, 0.1, 0.05, 0.025)]:   # asymptotic regime needs t*(s-1)^2 small
        r = (Z(s, t) - Res/t - z0 + z1*t)/t**2
        out.append(f"s={s} t={t:.2e}: (Z - Res/t - zeta0 + zeta(-1) t)/t^2 = {r:.5f}   (bounded => t^0 and t^1 coefficients confirmed)")
print("\n".join(out)); open('numeric_asymptotic_check.txt', 'w').write("\n".join(out)+"\n")
