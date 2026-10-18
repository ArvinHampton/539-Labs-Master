"""AUDIT (Cat B, 40-digit mpmath): closed forms.  F(alpha,u) = alpha*K(u)/u + (1-alpha^2) u/(7 alpha),
K(u) = (pi^2/6 - Li2(e^{-2u}))/4  [derived: Phi1(u) = K(u)/u via Li2(z)+Li2(-z) = Li2(z^2)/2].
c := max_alpha min_u F.  Compare with sqrt((Li2(y^2)+7 ln^2 y)/7), y^7+y^2=1."""
from mpmath import mp, mpf, polylog, pi, exp, log, sqrt, findroot, quad, diff
mp.dps = 40
K = lambda u: (pi**2/6 - polylog(2, exp(-2*u)))/4
Phi1q = lambda u: (quad(lambda y: log(1+exp(-u*y)), [0, 1]) + quad(lambda y: -log(1-exp(-u*y)), [1, 2]))/2
for u in (mpf('0.3'), mpf('0.61'), mpf('1.6')):
    print('Phi1 check u=%s: quad - K/u = %s' % (u, Phi1q(u) - K(u)/u))
F = lambda a, u: a*K(u)/u + (1-a*a)*u/(7*a)
def psi(a):
    u = findroot(lambda u: diff(lambda v: F(a, v), u), mpf('0.6')); return F(a, u), u
a = findroot(lambda a: diff(lambda b: psi(b)[0], a), mpf('0.438'))
c_num, u_s = psi(a)
y = findroot(lambda y: y**7+y**2-1, mpf('0.84'))
c_cf = sqrt((polylog(2, y**2) + 7*log(y)**2)/7)
u0 = -mpf(7)/2*log(y); V = (pi**2/6 - polylog(2, y**7))/4 - u0**2/7
print('alpha* =', a, ' u* =', u_s, ' u0 = -(7/2)ln y =', u0)
print('c (max-min of F) =', c_num); print('c closed form    =', c_cf); print('2 sqrt(V/7)      =', 2*sqrt(V/7))
print('diff =', c_num - c_cf)
print('E/O limit (1-sqrt(1-y^2))/y =', (1-sqrt(1-y**2))/y, ' = (1-y^3.5)/y =', (1-y**mpf(3.5))/y, ' 1/(y/(1-y^3.5)) ok')
