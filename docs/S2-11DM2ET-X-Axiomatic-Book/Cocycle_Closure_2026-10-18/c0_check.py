# Check of the hand derivation C = -pi/2 (report Sec. 1): I_n(z) = int_z^{z+i inf} [sqrt(y)K0(2 pi n y)e(nx), R_z^{1/2}].
# Integrand on w = z + i s (derived in the report): -1/2 (2 pi n f - f') R^{1/2} - 1/4 f R^{-1/2} (2y+s)^{-2},
# f(Y) = sqrt(Y) K0(2 pi n Y), R = (y+s)/(s(2y+s)); the x-dependence is the factor e(nx).
from mpmath import mp, mpf, besselk, sqrt, pi, quad, exp, inf, diff
mp.dps = 30
def I(n, y):
    f = lambda Y: sqrt(Y)*besselk(0, 2*pi*n*Y)
    fp = lambda Y: besselk(0, 2*pi*n*Y)/(2*sqrt(Y)) - sqrt(Y)*2*pi*n*besselk(1, 2*pi*n*Y)
    def g(s):
        R = (y+s)/(s*(2*y+s)); Y = y+s
        return -(2*pi*n*f(Y) - fp(Y))*sqrt(R)/2 - f(Y)/sqrt(R)/(4*(2*y+s)**2)
    return quad(g, [0, mpf(1)/100, 1, inf])
for n in (1, 2):
    for y in (mpf('0.3'), mpf(1), mpf(3)):
        v = I(n, y); print(n, y, v*exp(2*pi*n*y), v*exp(2*pi*n*y)/(-pi/2))
