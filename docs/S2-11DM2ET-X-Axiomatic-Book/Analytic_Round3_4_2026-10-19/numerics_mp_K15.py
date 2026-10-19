# Cat B support: direct H_s(e(a/N) e^{-t}) at 60 digits (exact integer coefficient table, mpmath evaluation),
# minus the proved expansion through t^{11/2}; fit the remainder to c13 t^{13/2} + c15 t^{15/2} + c17 t^{17/2} + c19 t^{19/2}  (K = 15).
import sys, math, json, numpy as np, mpmath as mp, sympy as sp
from collections import defaultdict
from hs_coeffs import coeffs
mp.mp.dps = 60
def table(s, Emax):
    # H = sum_cone w(nu) (q^{Q+} - q^{Q-}); weights 1/2 on n = 0 (k > 0) and on the wall 3sk = (s-8)n (n > 0); origin 0
    A = defaultdict(int)   # coefficients times 2
    n = 0
    while n*n <= Emax*1.0 + 1:
        k0 = -((-(s-8)*n) // (3*s))           # ceil((s-8)n/(3s))
        k = k0
        while True:
            Qp = n*n + s*n*k + s*k*(k+1)//2; Qm = Qp - s*k
            if min(Qp, Qm) > Emax and k > 0: break
            wt = 2
            if n == 0: wt = 0 if k == 0 else 1
            elif 3*s*k == (s-8)*n: wt = 1
            if wt:
                if Qp <= Emax: A[Qp] += wt
                if Qm <= Emax: A[Qm] -= wt
            k += 1
        n += 1
    return A
def H(A, a, N, t):
    z = mp.mpf(0)
    for E, c in A.items():
        if c: z += c*mp.expjpi(2*mp.mpf(a)*E/N)*mp.exp(-t*E)
    return z/2
s, a, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); ts = [mp.mpf(x) for x in sys.argv[4].split(',')]
C = coeffs(s, a, N, 15)
Cn = {e: mp.mpc(complex(sp.N(v, 70))) if False else mp.mpmathify(sp.N(v, 70)) for e, v in C.items()}
Emax = int(160/min(ts)) + 10
A = table(s, Emax)
rows = []
for t in ts:
    h = H(A, a, N, t)
    rem = h - sum(Cn[e]*t**(mp.mpf(e)/2) for e in Cn if e <= 11)
    rows.append((t, rem/t**mp.mpf(6.5)))
# least squares in t for rem/t^{11/2} = c11 + c13 t + c15 t^2 + c17 t^3
M = mp.matrix([[t**j for j in range(4)] for t, _ in rows]); y = mp.matrix([r for _, r in rows])
sol = mp.lu_solve(M.T*M, M.T*y)
out = dict(s=s, x='%d/%d' % (a, N), t=[mp.nstr(t, 6) for t in ts],
           c13_fit=mp.nstr(sol[0], 15), c13_exact=mp.nstr(Cn[13], 20), c15_fit=mp.nstr(sol[1], 12), c15_exact=mp.nstr(Cn[15], 20),
           rel_err_c13=mp.nstr(abs(sol[0]-Cn[13])/max(abs(Cn[13]), mp.mpf(10)**-40), 3),
           rel_err_c15=mp.nstr(abs(sol[1]-Cn[15])/max(abs(Cn[15]), mp.mpf(10)**-40), 3))
# second diagnostic: residual after subtracting through t^{13/2}
print(json.dumps(out))
