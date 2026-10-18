# PARI-free ideal/class machinery: classes of prime ideals (by solving norm equations), ideal-class counts by norm,
# and the class of the ideal attached to a lattice vector nu of a component.
import math
from collections import Counter, defaultdict
import rc
def isqrt_exact(n):
    if n < 0: return None
    r = math.isqrt(n); return r if r*r == n else None
def primes_upto(N):
    s = bytearray([1])*(N+1); s[0:2] = b'\x00\x00'
    for i in range(2, math.isqrt(N)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(N+1) if s[i]]
def leg35(p): return pow(35 % p, (p-1)//2, p)
class Ideals:
    def __init__(s, R, Nmax):
        s.R = R; s.Nmax = Nmax
        s.g13 = R.cl(tuple([0]*5), 1); s.g13p = R.add(R.cl(R.i13, 0), R.neg(s.g13))
        s.pcl = {}       # p -> (class of p, class of p') for split p (p = (p, sqrt35 - r)), or ('inert', class of (p))
        for p in primes_upto(Nmax):
            if p in (2, 5, 7): continue
            if leg35(p) == p-1:
                s.pcl[p] = ('inert', R.cl(R.iota(p, 0), 0)); continue
            r = next(x for x in range(p) if (x*x-35) % p == 0)
            if p == 13:
                assert r == 3   # (13, sqrt35-3) = p13' ; p13 = (13, sqrt35+3)
                s.pcl[p] = ('split', s.g13p, s.g13, r); continue
            s.pcl[p] = ('split', s.prime_class(p, r), s.prime_class(p, -r % p), r)
    def prime_class(s, p, r):
        R = s.R
        for b in range(0, 40*math.isqrt(p)+50):
            for N in (p, -p, 13*p, -13*p):
                a0 = isqrt_exact(N + 35*b*b)
                if a0 is None: continue
                for a in (a0, -a0):
                    if (a + b*r) % p: continue
                    i = R.iota(a, b)
                    if abs(N) == p: return R.cl(i, 0)
                    if (a - 3*b) % 13 == 0:      # (mu) = P * p13
                        return R.add(R.cl(i, 0), R.neg(s.g13))
                    assert (a + 3*b) % 13 == 0   # (mu) = P * p13'
                    return R.add(R.cl(i, 0), R.neg(s.g13p))
        raise RuntimeError(p)
    def counts(s):
        """C[n] = Counter(class -> number of ideals of norm n), n <= Nmax coprime to 70"""
        R = s.R; zero = R.cl(tuple([0]*5), 0)
        C = [None]*(s.Nmax+1); C[1] = Counter({zero: 1})
        # multiplicative build via smallest prime factor
        spf = list(range(s.Nmax+1))
        for i in range(2, math.isqrt(s.Nmax)+1):
            if spf[i] == i:
                for j in range(i*i, s.Nmax+1, i):
                    if spf[j] == j: spf[j] = i
        for n in range(2, s.Nmax+1):
            if math.gcd(n, 70) != 1: continue
            p = spf[n]; k = 0; m = n
            while m % p == 0: m //= p; k += 1
            pp = s.pcl[p]
            loc = Counter()
            if pp[0] == 'inert':
                if k % 2: C[n] = Counter(); continue
                x = zero
                for _ in range(k//2): x = R.add(x, pp[1])
                loc[x] += 1
            else:
                for i in range(k+1):
                    x = zero
                    for _ in range(i): x = R.add(x, pp[1])
                    for _ in range(k-i): x = R.add(x, pp[2])
                    loc[x] += 1
            out = Counter()
            for x, u in loc.items():
                for y, v in C[m].items(): out[R.add(x, y)] += u*v
            C[n] = out
        return C
# generators: p2^2=(2), p5^2=(5), p7^2=(7), p2p5=(5+sqrt35), p2p7=(7+sqrt35), p5p7=(sqrt35); p_q * p13 = (mu_q)
PAIR = {frozenset((2, 5)): (5, 1), frozenset((2, 7)): (7, 1), frozenset((5, 7)): (0, 1)}
MU = {2: (3, 1), 5: (10, -1), 7: (7, -2)}
def mul(x, y): return (x[0]*y[0]+35*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def ramified_divisor(g):
    """D (element) and delta in {0,1} with  p2^v2 p5^v5 p7^v7 = (D) p13^{-delta}, i.e. (beta) g^-1 = (beta/D) p13^delta"""
    v = {}
    for q in (2, 5, 7):
        e = 0; h = g
        while h % q == 0: h //= q; e += 1
        v[q] = e
    D = (1, 0); odd = []
    for q in (2, 5, 7):
        for _ in range(v[q]//2): D = mul(D, (q, 0))
        if v[q] % 2: odd.append(q)
    delta = 0
    while len(odd) >= 2:
        q1, q2 = odd[0], odd[1]; odd = odd[2:]; D = mul(D, PAIR[frozenset((q1, q2))])
    if odd:
        D = mul(D, MU[odd[0]]); delta = 1
    return D, delta, v
def class_of_quotient(R, beta, D, delta, g13):
    """class of (beta)/(D) * p13^delta, where beta/D is a unit at 2,5,7"""
    a, b = beta; Dc = (D[0], -D[1]); nD = D[0]*D[0]-35*D[1]*D[1]
    num = mul((a, b), Dc)
    den = nD; r = 1
    for q in (2, 5, 7):
        while den % q == 0: den //= q; r *= q
    assert num[0] % r == 0 and num[1] % r == 0, (beta, D)
    gam = (num[0]//r, num[1]//r)
    x = R.add(R.cl(R.iota(*gam), 0), R.neg(R.cl(R.iota(den, 0), 0)))
    if delta: x = R.add(x, g13)
    return x
