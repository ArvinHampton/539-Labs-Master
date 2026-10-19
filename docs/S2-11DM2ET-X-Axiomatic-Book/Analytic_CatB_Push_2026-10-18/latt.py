import math
def Qp(s, n, k): return n*n + s*n*k + s*k*(k+1)//2
def lat(s):
    g = math.gcd(24, s-8); m = 3*s//g; b = (s-8)//g
    kw, nw = next((k, n) for n in range(-3*m-3, 3*m+3) for k in [(1 + b*n)//m] if k*m - b*n == 1)
    return g, m, b, nw, kw
def Hcounts(s, a, N):   # H(c), c mod 2N, as exponent count vectors mod N  (y over 2N)
    g, m, b, nw, kw = lat(s); P = 2*N; out = []
    for c in range(P):
        v = [0]*N
        for y in range(P): v[(a*Qp(s, c*nw + y*m, c*kw + y*b)) % N] += 1
        out.append(tuple(v))
    return out
