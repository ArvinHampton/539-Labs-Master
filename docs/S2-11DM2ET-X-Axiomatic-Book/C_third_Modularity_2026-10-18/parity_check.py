# Numerical confirmation of (a) the C_third radial expansion s/t + h t^{-1/2} + c and (b) the PARITY LEMMA:
# q^8 f = Theta_hol - theta_3 has only half-integer powers of t in its radial expansion at rationals
# (fit D(t) = q^8 f(e(x)e^{-t}) against t^{-1/2}, t^0, t^{1/2}, t^1, t^{3/2}).
import numpy as np, math, cmath, sys
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
from radial import Cthird_exp
def series_vals(x, t, which):
    B = int(math.sqrt(60/t)) + 40
    n, k = np.meshgrid(np.arange(-B, B+1), np.arange(-B, B+1), indexing='ij')
    if which == 'C':
        m = (n >= 1) & (k >= 1); e = (n*n + 7*n*k + (7*k*(k-1))//2)[m]
        return np.sum(np.exp((2j*np.pi*float(x) - t)*e.astype(float)))
    sgr = np.where(n >= 0, 1, -1); sgs = np.where(k >= 0, 1, -1); same = sgr == sgs
    e = (8 + n*(n-1) + 7*n*k + (7*k*(k-1))//2 + 10*n + 14*k)
    m = same & (e < 60/t)
    xx = Fr(x); ph = np.exp(2j*np.pi*((xx.numerator*e[m]) % xx.denominator)/xx.denominator)
    return np.sum(sgr[m]*ph*np.exp(-t*e[m].astype(float)))
out = []
for x in (Fr(0), Fr(1, 2), Fr(1, 3), Fr(1, 7), Fr(1, 5)):
    s, h, c = Cthird_exp(x)
    ts = [0.004, 0.002, 0.001, 0.0005]
    rem = [series_vals(x, t, 'C') - (s/t + h/math.sqrt(t) + c) for t in ts]
    out.append(f"x={x}: C_third remainder after s/t + h t^-1/2 + c at t={ts}: " + ", ".join(f"{abs(r):.2e}" for r in rem) + "  (should scale like t^{1/2})")
    ts2 = np.array([0.02, 0.014, 0.01, 0.007, 0.005, 0.0035, 0.0025, 0.0018])
    vals = np.array([series_vals(x, t, 'F') for t in ts2])
    Amat = np.stack([ts2**-0.5, ts2**0, ts2**0.5, ts2**1, ts2**1.5, ts2**2], axis=1)
    coef, *_ = np.linalg.lstsq(Amat.astype(complex), vals, rcond=None)
    out.append(f"   q^8 f fit coefficients [t^-1/2, t^0, t^1/2, t^1, t^3/2, t^2]: " + ", ".join(f"{abs(cc):.2e}" for cc in coef) + f";  predicted t^-1/2 coeff |2h_C - h_E| = {abs(2*h):.6f}")
print("\n".join(out)); open('parity_check.txt', 'w').write("\n".join(out)+"\n")
