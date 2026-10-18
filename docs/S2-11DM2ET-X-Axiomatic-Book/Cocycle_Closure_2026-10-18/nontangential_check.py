# Numerical check (Cat B support) that the radial expansion of E_L (s = 7) holds non-tangentially:
#   E_L(x+h) = A/h + kappa(x) + B h + O(h^2), with the same kappa for every direction h = r e^{i phi}, 0 < phi < pi.
# kappa(x) is the exact Bernoulli value (fastkappa.cone_terms(...)[1]).
import sys, math, cmath, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, '../2026-10-17-psi-cocycle')
from fastkappa import cone_terms, a, zero
s = 7; d = 2*(s-2); X0 = (s, -2)
def nus(Qmax):
    B = int(6*math.sqrt(Qmax)) + 10; out = []
        # nu = (X/d), X = X0 + d*(n,k); cone 2X1+X2>0, X2>=0
    X1 = X0[0] + d*np.arange(-B, B+1)[:, None]; X2 = X0[1] + d*np.arange(0, B+1)[None, :]
    X1, X2 = np.broadcast_arrays(X1, X2)
    m = (2*X1 + X2 > 0) & (X2 >= 0)
    Q = (X1*X1 + s*X1*X2 + s*X2*X2/2)/(d*d)
    Q = Q[m]; return Q[Q <= Qmax]
Qs = nus(120000.0)
def E(z): return np.sum(np.exp(2j*np.pi*z*Qs))
for x in (Fr(1,2), Fr(1,3), Fr(2,5)):
    kap = cone_terms(a, zero, x)[1]
    print('x', x, 'kappa exact', kap)
    for phi in (math.pi/2, math.pi/4, 3*math.pi/4, math.pi/6):
        rs = [0.0012, 0.001, 0.0008, 0.0006, 0.0005]
        hs = [r*cmath.exp(1j*phi) for r in rs]
        M = np.array([[1/h, 1, h, h*h, h**3] for h in hs]); v = np.array([E(float(x) + h) for h in hs])
        A, k, Bc, _, _ = np.linalg.solve(M, v)
        print('  phi=%.3f' % phi, 'kappa_fit', k, '|diff|', abs(k - kap), 'A', A)
