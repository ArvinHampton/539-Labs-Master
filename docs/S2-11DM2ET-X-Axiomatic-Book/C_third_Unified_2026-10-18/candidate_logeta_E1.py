# Path C numeric candidate: F = log(eta) * E_{1,chi_-3}  (weight-0 object with logarithmic cocycle  x  weight-1 form).
# Test: radial expansion at rationals x = h/k as t -> 0+.  C_third needs half-integer orders t^{-1/2}, t^{1/2} (Zwegers sector)
# and nonzero regular orders t^0, t^1 (E sector).  Lemma C1 predicts F(x+it) = A t^-2 + B t^-1 log t + C t^-1 + O(exp small).
import mpmath as mp
mp.mp.dps = 30
def chi(d): return [0, 1, -1][d % 3]
NMAX = 40000
a = [mp.mpf(0)]*(NMAX+1)
for dd in range(1, NMAX+1):
    c = chi(dd)
    if c:
        for n in range(dd, NMAX+1, dd): a[n] += c
def E1(tau):
    q = mp.exp(2j*mp.pi*tau); s = mp.mpf(1)/6; qn = 1
    for n in range(1, NMAX+1):
        qn *= q; s += a[n]*qn
        if abs(qn) < mp.mpf(10)**-34: break
    return s
def logeta(tau):
    # log eta = pi i tau/12 - sum_{n} sigma_{-1}(n) q^n  (principal branch along the path, exact series)
    q = mp.exp(2j*mp.pi*tau); s = 2j*mp.pi*tau/24; qn = 1
    for n in range(1, NMAX+1):
        qn *= q; t = qn/n/(1-qn); s -= t
        if abs(qn) < mp.mpf(10)**-34: break
    return s
def fit(x, ts, basis):
    rows = [[f(t) for f in basis] for t in ts]
    ys = [logeta(x+1j*t)*E1(x+1j*t) for t in ts]
    A = mp.matrix(rows); y = mp.matrix(ys)
    sol = mp.lu_solve(A.H*A, A.H*y)
    res = max(abs(y[i]-sum(A[i, j]*sol[j] for j in range(len(basis)))) for i in range(len(ts)))
    return sol, res
basisC1 = [lambda t: t**-2, lambda t: mp.log(t)/t, lambda t: 1/t]
basisX = basisC1 + [lambda t: t**-0.5, lambda t: 1, lambda t: t**0.5, lambda t: t]
names = ["t^-2", "t^-1 log t", "t^-1", "t^-1/2", "t^0", "t^1/2", "t^1"]
for x, k in ((mp.mpf(0), 1), (mp.mpf(1)/3, 3), (mp.mpf(1)/2, 2), (mp.mpf(1)/7, 7)):
    ts = [mp.mpf(1)/((40+6*i)*k*k) for i in range(14)]   # scaled so that k^2 t is small (cusp regime)
    sol, res = fit(x, ts, basisX)
    sol1, res1 = fit(x, ts, basisC1)
    print(f"x={mp.nstr(x,6)}: 7-term fit coefficients:")
    for nm, v in zip(names, sol): print(f"   {nm:11s} {mp.nstr(v, 12)}")
    print(f"   residual 7-term {mp.nstr(res,3)};  3-term (C1 basis only) residual {mp.nstr(res1,3)}")
