# Singular-level S-law for the E-vector at x<0: is it
#   G_{a,0}(-1/x) = (1/(sqrt35 * x))   * sum_{p in L'/Z^2} G_{p,-a}(x)      (holomorphic factor), or
#   G_{a,0}(-1/x) = (1/(sqrt35 * |x|)) * sum_{p in L'/Z^2} G_{p,-a}(x)      (real factor)?
# G_{al,be}(x) = mean over nu in al+Z^2 of e(x Q(nu) + B(nu,be)); Q = nu1^2+7nu1nu2+3.5nu2^2, Gram [[2,7],[7,7]].
# Exact integer arithmetic for phases, numpy for the mean.
import numpy as np
from fractions import Fraction as Fr
D = 70                       # common denominator of all alpha, beta used
def G(al, be, x):
    h, m = x.numerator, x.denominator
    A1, A2 = int(al[0]*D), int(al[1]*D); b1, b2 = int(be[0]*D), int(be[1]*D)
    P = 2*m*D                # period in n (safe)
    n1, n2 = np.meshgrid(np.arange(P, dtype=np.int64), np.arange(P, dtype=np.int64), indexing='ij')
    N1, N2 = A1 + D*n1, A2 + D*n2                     # D*nu
    twoQ = 2*N1*N1 + 14*N1*N2 + 7*N2*N2               # 2 Q(nu) D^2
    Bn = 2*N1*b1 + 7*(N1*b2 + N2*b1) + 7*N2*b2        # B(nu,be) D^2
    M = 2*m*D*D
    ph = (h*twoQ + 2*m*Bn) % M                        # (x Q + B) * M
    return np.exp(2j*np.pi*ph/M).mean()
a = (Fr(7,10), Fr(-1,5)); mina = (-a[0], -a[1]); zero = (Fr(0), Fr(0))
# L'/Z^2 = A^{-1}Z^2/Z^2, A^{-1} = (1/35)[[7,-7],[-7,2]]
Lp = sorted({((Fr(7*u - 7*w, 35)) % 1, (Fr(-7*u + 2*w, 35)) % 1) for u in range(35) for w in range(35)})
assert len(Lp) == 35
lines = []
for x in [Fr(1,3), Fr(-1,3), Fr(2,3), Fr(-2,3), Fr(1,7), Fr(-1,7), Fr(3,7), Fr(-3,7), Fr(1,9), Fr(-4,9), Fr(1,1), Fr(-1,1)]:
    lhs = G(a, zero, -1/x)
    rhs0 = sum(G(p, mina, x) for p in Lp)/np.sqrt(35)
    if abs(rhs0) < 1e-12:
        lines.append(f"x={str(x):>5}: RHS sum = 0, |lhs| = {abs(lhs):.2e}"); continue
    rs, ra = lhs/(rhs0/float(x)), lhs/(rhs0/abs(float(x)))
    lines.append(f"x={str(x):>5}: lhs={lhs.real:+.6f}{lhs.imag:+.6f}i   lhs/RHS(x) = {rs.real:+.6f}{rs.imag:+.6f}i   lhs/RHS(|x|) = {ra.real:+.6f}{ra.imag:+.6f}i")
print("\n".join(lines)); open('sign_law_check.txt','w').write("\n".join(lines)+"\n")
