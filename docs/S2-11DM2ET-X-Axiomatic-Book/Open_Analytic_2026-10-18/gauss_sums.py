# Normalised area Gauss sums G_+- = (1/(P^2 m)) sum_{p in Pi} e(x Q_+-(p)) at x = 1/2 and 1/3 (exact enumeration, float output).
import math, cmath, json
from fractions import Fraction as Fr
def G(s, a, N):
    g = math.gcd(24, s-8); m = 3*s//g; b = (s-8)//g; P = 2*N; Gp = Gm = 0
    for n in range(P*m):
        kmin = math.ceil(Fr(b*n, m))
        for k in range(kmin, kmin+P+1):
            al = Fr(k - Fr(b*n, m), P)
            if not (0 <= al < 1): continue
            Qp = n*n + s*n*k + s*k*(k+1)//2; Qm = n*n + s*n*k + s*k*(k-1)//2
            Gp += cmath.exp(2j*math.pi*a*(Qp % N)/N); Gm += cmath.exp(2j*math.pi*a*(Qm % N)/N)
    return [round(Gp.real/(P*P*m), 12), round(Gp.imag/(P*P*m), 12)], [round(Gm.real/(P*P*m), 12), round(Gm.imag/(P*P*m), 12)]
out = {}
for s in list(range(5, 41)) + [48, 56, 64, 80, 96]:
    out[s] = dict(x_half=G(s, 1, 2), x_third=G(s, 1, 3))
    print(s, out[s])
json.dump(out, open('gauss_sums.json', 'w'), indent=1)
