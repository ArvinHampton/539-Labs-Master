# exact atomic sums at x = a/N in Q(zeta_N) (vector of coefficients on zeta^e), normalised: S0/(P^2 m), TEb[r] m^{r-1}, TEa[r] m^{r-1}
import math, json, sys
from fractions import Fraction as Fr
from atomic_sums import bern
def atomic(s, a, N, R=7, sg='+'):
    g = math.gcd(24, s-8); m = 3*s//g; b = (s-8)//g; P = 2*N
    acc = {'S0': [Fr(0)]*N}
    for key in ['Eb%d' % r for r in range(1, R+1)] + ['Ea%d' % r for r in range(1, R+1)]: acc[key] = [Fr(0)]*N
    for n in range(P*m):
        be = Fr(n, P*m); kmin = math.ceil(Fr(b*n, m))
        for k in range(kmin, kmin+P+1):
            al = Fr(k - Fr(b*n, m), P)
            if not (0 <= al < 1): continue
            Q = n*n + s*n*k + (s*k*(k+1)//2 if sg == '+' else s*k*(k-1)//2)
            e = (a*Q) % N
            acc['S0'][e] += 1
            for r in range(1, R+1):
                acc['Eb%d' % r][e] += bern(r, be); acc['Ea%d' % r][e] += bern(r, al)
    out = {'S0': [str(v/(P*P*m)) for v in acc['S0']]}
    for r in range(1, R+1):
        out['Eb%d' % r] = [str(v*m**(r-1)) for v in acc['Eb%d' % r]]
        out['Ea%d' % r] = [str(v*m**(r-1)) for v in acc['Ea%d' % r]]
    return dict(s=s, g=g, m=m, b=b, **out)
if __name__ == "__main__":
    a, N = (int(z) for z in sys.argv[1].split('/')); ss = [int(z) for z in sys.argv[2:]]
    res = []
    for s in ss:
        r = atomic(s, a, N); res.append(r); print(json.dumps(r), flush=True)
    json.dump(res, open('atomic_%d-%d.json' % (a, N), 'w'), indent=0)
