# finite Gauss-Bernoulli data for x = a/N (proved reductions, see report sec. 1.6):
#   gamma0 = P^-2 sum_{n,k mod P} e(x Q+(n,k));  eb_r = sum_{j<P} G(j) Bt_r(j/P), G(j) = sum_{k<P} e(x Q+(j,k));
#   ea_r = sum_{c<P} H(c) Bt_r(c/P),  H(c) = sum_{y<P} e(x Q+(c w + y u2)),  w = (n_w,k_w) with k_w m - b n_w = 1.
import math, cmath, sympy as sp
def Qp(s, n, k): return n*n + s*n*k + s*k*(k+1)//2
def data(s, a, N, R=9):
    g = math.gcd(24, s-8); m = 3*s//g; b = (s-8)//g; P = 2*N
    # w: k m - b n = 1
    kw, nw = next((k, n) for n in range(-3*m-3, 3*m+3) for k in [(1 + b*n)//m] if k*m - b*n == 1)
    z = sp.exp(2*sp.pi*sp.I*sp.Rational(a, N))
    ph = lambda Q: z**(Q % N)
    gamma0 = sp.nsimplify(sp.expand(sum(ph(Qp(s, n, k)) for n in range(P) for k in range(P))/P**2))
    G = [sp.expand(sum(ph(Qp(s, j, k)) for k in range(P))) for j in range(P)]
    H = [sp.expand(sum(ph(Qp(s, c*nw + y*m, c*kw + y*b)) for y in range(P))) for c in range(P)]
    def Bt(r, u): return sp.Integer(0) if (r == 1 and u == 0) else sp.bernoulli(r, u)
    eb = {r: sp.expand(sum(G[j]*Bt(r, sp.Rational(j, P)) for j in range(P))) for r in range(1, R+1)}
    ea = {r: sp.expand(sum(H[c]*Bt(r, sp.Rational(c, P)) for c in range(P))) for r in range(1, R+1)}
    return dict(g=g, m=m, b=b, gamma0=sp.expand(gamma0), eb=eb, ea=ea, G=G, H=H)
