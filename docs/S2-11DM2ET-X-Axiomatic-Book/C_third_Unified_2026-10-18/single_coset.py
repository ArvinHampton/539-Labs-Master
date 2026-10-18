# Path C (s = 7): single-coset cone-weight representation of C_third and the odd/even (Zwegers / Maass) split.
# Coordinates: nu = v + a in a + Z^2, a = (7/10, -1/5), Q(nu) = nu1^2 + 7 nu1 nu2 + 7/2 nu2^2, Q(nu) + 7/20 = Q_s(v).
# Cones (open; no coset point of +-a + Z^2 lies on the rays used): Q1 = {nu1>0, nu2>0}; F = {nu2>0, 2nu1+nu2>0} = [e1, gamma e1);
#   F' = F \ Q1 = {nu1<0, nu2>0, 2nu1+nu2>0}.
import numpy as np, math, sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
B = int(4*math.isqrt(N) + 60)
def ser(e, w=None):
    e = np.asarray(e).ravel(); w = np.ones_like(e) if w is None else np.asarray(w).ravel()
    m = (e >= 0) & (e <= N)
    return np.bincount(e[m], weights=w[m], minlength=N+1).astype(np.int64)
n, k = np.meshgrid(np.arange(-B, B+1), np.arange(-B, B+1), indexing='ij')
d = np.load('../2026-10-18-C_third-modularity/series.npz') if False else None
# reference series (rebuilt exactly as in 2026-10-18-C_third-modularity/series.py)
Qm = (2*n*n + 14*n*k + 7*k*(k-1))//2
Ct = ser(Qm[(n >= 1) & (k >= 1)])
r = np.arange(-B, B+1); th3 = ser(r*r); one = np.zeros(N+1, np.int64); one[0] = 1
TH = ser(Qm[(n >= 1) & (k >= 0)]) - ser(Qm[(n <= 0) & (k <= -1)])
def cone_sum(sign, region):
    # coset sign*a + Z^2 : 10 nu = (10n + 7 sign, 10k - 2 sign); exponent Q(nu) + 7/20 = (X^2 + 7XY + 3.5Y^2 + 35)/100
    X, Y = 10*n + 7*sign, 10*k - 2*sign
    num = 2*X*X + 14*X*Y + 7*Y*Y + 70
    assert (num % 200 == 0).all()
    e = num//200
    m = region(X, Y)
    return ser(e[m])
Fm = lambda X, Y: (Y > 0) & (2*X + Y > 0)
Q1 = lambda X, Y: (X > 0) & (Y > 0)
mQ1 = lambda X, Y: (X < 0) & (Y < 0)
Fp = lambda X, Y: (X < 0) & (Y > 0) & (2*X + Y > 0)
mF = lambda X, Y: (Y < 0) & (2*X + Y < 0)
E_a, E_ma = cone_sum(1, Fm), cone_sum(-1, Fm)
lines = []
lines.append(f"N = {N}")
lines.append(f"[1] E (q^(7/20) E_L) == unit-cone sum over a+Z^2: (reference identity 2C_third = q^8f + 1 + E used below)")
lhs = 2*Ct - one + th3
w_single = cone_sum(1, Fp) + cone_sum(1, mQ1)
lines.append(f"[2] 2C_third - 1 + theta_3 == q^(7/20) * sum_(a+Z^2) w(nu) q^Q(nu), w = 1_F' + 1_(-Q1) >= 0: {bool((lhs == w_single).all())}")
lines.append(f"    and == q^(7/20)[1_F + 1_(-Q1) - 1_(Q1)] form: {bool((lhs == E_a + cone_sum(1, mQ1) - cone_sum(1, Q1)).all())}")
lines.append(f"    Theta_hol == q^(7/20)[E^(-Q1)_a - E^(Q1)_a]: {bool((TH == cone_sum(1, mQ1) - cone_sum(1, Q1)).all())}")
Dodd = E_a - E_ma
lines.append(f"[3] odd part of E_L: E^F_a - E^F_(-a): identically zero to q^{N}: {bool((Dodd == 0).all())}; nonzero count {int((Dodd != 0).sum())}; first {[(int(i), int(Dodd[i])) for i in np.nonzero(Dodd)[0][:10]]}")
lines.append(f"    E^F_(-a) == E^F_a under nu -> R nu?  (checked via [3])")
# coefficient-level: w is a single coset, single degree-0 piecewise-constant weight
lines.append(f"[4] coefficient sanity: w-series nonnegative: {bool((w_single >= 0).all())}; first exponents {[int(i) for i in np.nonzero(w_single)[0][:12]]}")
open('single_coset.txt', 'w').write("\n".join(lines) + "\n"); print("\n".join(lines))
np.savez('single_coset.npz', E_a=E_a, E_ma=E_ma, Dodd=Dodd, w=w_single)
