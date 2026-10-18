# Item 3a, exact check of the key step: for every n, #{nu in (a+Z^2) cap F, Q(nu) = n} = #{nu in (-a+Z^2) cap F, Q(nu) = n},
# F = [e1, gamma e1) (half-open fundamental domain of <gamma> on the positive branch containing e1), with the bijection
# nu -> R nu (R = [[1,s],[0,-1]], R e1 = e1, R a = -a mod Z^2, R gamma R = gamma^{-1}) followed by gamma-reduction.
# Integer arithmetic: X = d*nu with d = 2(s-2), X in X0 + dZ^2, 2d^2 Q(nu) = X^T A X.
import sys, json, math
from collections import Counter
def counts(s, Nmax):
    d = 2*(s-2); A = ((2, s), (s, s)); X0 = (s, -2)          # d*a
    G = ((-1, -s), (2, 2*s-1)); e1 = (1, 0); ge1 = (G[0][0], G[1][0])
    det = lambda u, v: u[0]*v[1] - u[1]*v[0]
    inF = lambda X: det(e1, X) >= 0 and det(X, ge1) > 0 if det(e1, ge1) > 0 else None
    Qx = lambda X: X[0]*X[0]*2 + 2*s*X[0]*X[1] + s*X[1]*X[1]   # = X^T A X = 2 d^2 Q
    out = {}
    for sgn in (1, -1):
        C = Counter(); B = int(math.sqrt(2*d*d*Nmax)) * 8 + 50
        for i in range(-B, B+1):
            for j in range(-B, B+1):
                X = (sgn*X0[0] + d*i, sgn*X0[1] + d*j)
                if not inF(X): continue
                q2 = Qx(X)
                if q2 <= 0 or q2 > 2*d*d*Nmax: continue
                C[q2] += 1
        out[sgn] = C
    keys = set(out[1]) | set(out[-1])
    mism = [k for k in keys if out[1][k] != out[-1][k]]
    return dict(s=s, Nmax=Nmax, n_values=len(keys), total_a=sum(out[1].values()), total_minus_a=sum(out[-1].values()), mismatches=len(mism))
res = [counts(s, 60) for s in (5, 6, 7, 8, 9, 10, 11, 12, 13)]
for r in res: print(json.dumps(r))
json.dump(res, open('weight1_vanish_check.json', 'w'), indent=1)
