# Goal 3: general denominator x = a/N.  Exact checks (integer exponent arithmetic in Z[zeta_N]).
# (P) Periodicity: gamma0, G, eb depend on s mod N' ; H, ea depend on s mod 24 N'   (N' = N for odd N, 2N for even N)
# (G) Gauss evaluation, odd prime p >= 5 with p not dividing a s (s-2)(7s-32):
#     H(c) = 2 * (a Q2(u2) / p) * g_p * zeta^{a [ -g^2 (c+delta)^2 / (2(7s-32)) + c0 ]},  arithmetic mod p,
#     g_p = sum_z zeta^{z^2}, Q2(u2) = s(s-2)(7s-32)/(2g^2), c0 = s/(4(s-2)), delta = det(a_char, u2) normalised by det(w,u2)=1,
#     a_char = (s/(2(s-2)), -1/(s-2)).
import math, sys, json
from sympy import legendre_symbol
def Qp(s, n, k): return n*n + s*n*k + s*k*(k+1)//2
def lat(s):
    g = math.gcd(24, s-8); m = 3*s//g; b = (s-8)//g
    kw, nw = next((k, n) for n in range(-3*m-3, 3*m+3) for k in [(1 + b*n)//m] if k*m - b*n == 1)
    return g, m, b, nw, kw
def Hvec(s, a, N):   # H(c) as exponent-multiset vector in Z[zeta_N]: list over c of length-N count vectors
    g, m, b, nw, kw = lat(s); P = 2*N
    out = []
    for c in range(P):
        v = [0]*N
        for y in range(P): v[(a*Qp(s, c*nw + y*m, c*kw + y*b)) % N] += 1
        out.append(tuple(v))
    return tuple(out)
def Gvec(s, a, N):
    P = 2*N
    return tuple(tuple(sum(1 for k in range(P) if (a*Qp(s, j, k)) % N == e) for e in range(N)) for j in range(P))
def red(v, N):       # reduce count vector modulo the relation sum_e zeta^e = 0 (N prime): subtract min
    if all(N % q for q in range(2, int(N**.5)+1)):
        mn = min(v); return tuple(x - mn for x in v)
    return tuple(v)
res = {}
# (P) periodicity
for (a, N) in [(1, 3), (1, 5), (2, 5), (1, 7), (3, 7), (1, 4), (1, 6), (1, 9)]:
    Np = N if N % 2 else 2*N; L = 24*Np
    badH = [s for s in range(5, 5 + 2*L) if Hvec(s, a, N) != Hvec(s + L, a, N)]
    badG = [s for s in range(5, 5 + 4*Np) if Gvec(s, a, N) != Gvec(s + Np, a, N)]
    # minimal period of H among divisors of L (tested on s = 5 .. 5+2L)
    per = min(d for d in range(1, L+1) if L % d == 0 and all(Hvec(s, a, N) == Hvec(s + d, a, N) for s in range(5, 5 + L)))
    res['%d/%d' % (a, N)] = dict(Nprime=Np, H_period_claim=L, H_mismatch=badH, G_period_claim=Np, G_mismatch=badG, H_minimal_period_observed=per)
    print(a, N, res['%d/%d' % (a, N)], flush=True)
# (G) Gauss evaluation for odd primes
gauss = {}
for p in (5, 7, 11, 13):
    for a in range(1, p):
        nbad = 0; ntest = 0
        for s in range(5, 400):
            if (s*(s-2)*(7*s-32)) % p == 0: continue
            g, m, b, nw, kw = lat(s)
            inv = lambda x: pow(x % p, -1, p)
            Q2u = s*(s-2)*(7*s-32) * inv(2*g*g) % p
            chi = legendre_symbol(a*Q2u % p, p)
            a1 = s*inv(2*(s-2)) % p; a2 = (-1)*inv(s-2) % p
            # det convention: k_w m - b n_w = 1  ->  coordinate c of nu = n_nu*(-b)... solve nu = c w + y u2: c = k_nu*m - b*n_nu
            delta = (a2*m - b*a1) % p
            c0 = s*inv(4*(s-2)) % p
            H = Hvec(s, a, p)
            for c in range(2*p):
                ex = a*((-g*g*inv(2*(7*s-32))*(c + delta)**2) + c0) % p
                # predicted: 2*chi*sum_z zeta^{z^2 + ex}
                v = [0]*p
                for z in range(p): v[(z*z + ex) % p] += 2*chi
                ntest += 1
                if red(tuple(v), p) != red(H[c], p): nbad += 1
        gauss['p=%d,a=%d' % (p, a)] = dict(tests=ntest, mismatches=nbad)
    print(p, {k: v for k, v in gauss.items() if k.startswith('p=%d,' % p)}, flush=True)
json.dump(dict(periodicity=res, gauss_odd_prime=gauss), open('general_N.json', 'w'), indent=1)
