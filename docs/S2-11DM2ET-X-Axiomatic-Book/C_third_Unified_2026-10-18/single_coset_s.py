# Path C, all s >= 5: (i) E^F_a == E^F_{-a} (odd part of the unit-cone sum vanishes; proof: improper automorph R = [[1,s],[0,-1]],
#   R^T M R = M, R a = -a, R F = [e1, R gamma e1) is again a <gamma>-fundamental cone);
# (ii) single-coset identity 2C_third,s - 1 + theta_3 = q^{c0} sum_{a+Z^2} (1_{F'} + 1_{-Q1}) q^{Q}, with C_third,s := P_s + Theta_hol,s - theta_3
#   (the all-s identity of 2026-10-18-g_s-Closed-Forms.md §4), F = cone(e1, gamma e1), gamma e1 = (-1, 2), Q1 = open quadrant, F' = F \ Q1.
import numpy as np, math, sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
def ser(e, w=None, N=N):
    e = np.asarray(e).ravel(); w = np.ones_like(e) if w is None else np.asarray(w).ravel()
    m = (e >= 0) & (e <= N)
    return np.bincount(e[m], weights=w[m], minlength=N+1).astype(np.int64)
out = []
for s in list(range(5, 26)) + [41]:
    B = int(6*math.isqrt(N) + 80)
    n, k = np.meshgrid(np.arange(-B, B+1), np.arange(-B, B+1), indexing='ij')
    Qs = n*n + s*n*k + (s*k*(k+1))//2; Qm = n*n + s*n*k + (s*k*(k-1))//2
    r = np.arange(-B, B+1); th3 = ser(r*r); one = np.zeros(N+1, np.int64); one[0] = 1
    P = ser(Qs[(n >= 0) & (k >= 0)])
    TH = ser(Qm[(n >= 1) & (k >= 0)]) - ser(Qm[(n <= 0) & (k <= -1)])
    Ct = P + TH - th3
    d = 2*(s-2)                       # d*nu = (d n + s*sign, d k - 2*sign)
    def cone(sign, reg):
        X, Y = d*n + s*sign, d*k - 2*sign
        e = Qs if sign == 1 else (n*n + s*n*k + (s*k*(k-1))//2 if False else None)
        # exponent: Q(nu) + c0, computed exactly from X, Y:  (X^2 + s X Y + s Y^2/2)/d^2 + s/(4(s-2))
        num = 2*X*X + 2*s*X*Y + s*Y*Y + 2*d*d*s//(4*(s-2)) if (2*d*d*s) % (4*(s-2)) == 0 else None
        assert num is not None and (num % (2*d*d) == 0).all()
        return ser((num//(2*d*d))[reg(X, Y)])
    F = lambda X, Y: (Y > 0) & (2*X + Y > 0)
    Q1 = lambda X, Y: (X > 0) & (Y > 0); mQ1 = lambda X, Y: (X < 0) & (Y < 0)
    Fp = lambda X, Y: (X < 0) & (Y > 0) & (2*X + Y > 0)
    Ea, Ema = cone(1, F), cone(-1, F)
    ok1 = bool((Ea == Ema).all())
    ok2 = bool((2*Ct - one + th3 == cone(1, Fp) + cone(1, mQ1)).all())
    ok3 = bool((TH == cone(1, mQ1) - cone(1, Q1)).all())
    ok4 = bool((2*P == Ea + one + th3 - TH).all())
    out.append(f"s={s}: E^F_a == E^F_-a: {ok1};  2C_third-1+theta3 == single-coset (1_F' + 1_-Q1): {ok2};  Theta_hol == E^-Q1_a - E^Q1_a: {ok3};  2P = E + 1 + th3 - Theta_hol: {ok4}")
open('single_coset_s.txt', 'w').write(f"N = {N}\n" + "\n".join(out) + "\n"); print("\n".join(out))
