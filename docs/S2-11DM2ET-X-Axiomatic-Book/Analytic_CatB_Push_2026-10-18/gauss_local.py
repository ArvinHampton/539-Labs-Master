# Items (1)-(3) of the 21:49 continuation: CLOSED-FORM local evaluation of the edge Gauss sum H(c) for ANY x = a/N,
# verified EXACTLY in Z[zeta_L] (L = lcm(8, 2N)) against the brute-force definition.
#   H_N(c) = sum_{y mod 2N} e(a f_c(y)/N),  f_c(y) = Q+(c w + y u2) = Q2(u2) y^2 + (c B(w,u2) + s b/2) y + Q+(c w)
#   A2 = 2 Q2(u2) = 2m^2 + 2smb + s b^2,  B2 = 2c B(w,u2) + s b,  C = Q+(c w)      (A2, B2, C integers, A2 = B2 mod 2? no: A2+B2 even)
# Theorem L (CRT): N = 2^k * prod p^e.  H_N(c) = [2 if k = 0] * T_2 * prod_p T_{p^e}, with a/N = sum a_q/q (partial fractions),
#   T_{p^e} = sum_{y mod p^e} e(a_p f(y)/p^e)  (odd p; f mod p^e is p^e-periodic),
#   T_2     = sum_{y mod 2^{k+1}} e(a_2 (A2 y^2 + B2 y + 2C)/2^{k+1})   (k >= 1).
# Lemma R (p-adic reduction, any prime q, modulus q^n, alpha, beta, gamma integers, v = v_q(alpha)):
#   sum_{y mod q^n} e((alpha y^2 + beta y + gamma)/q^n) = q^n [q^n | beta] e(gamma/q^n)                       if v >= n
#     = q^v [q^v | beta] e(gamma/q^n) * sum_{y mod q^{n-v}} e((alpha' y^2 + beta' y)/q^{n-v}),  alpha' = alpha/q^v, beta' = beta/q^v   else
# Base cases (alpha' a unit):  odd q: e(-beta'^2 (4 alpha')^{-1}/q^j) (alpha'/q)^j g_{q^j},  g_{q^j} = q^{j/2} (j even), q^{(j-1)/2} g_q (j odd)
#   q = 2: j = 0: 1;  j = 1: 2[beta' odd];  j >= 2: 0 if beta' odd, else e(-alpha'^{-1}(beta'/2)^2/2^j) (1 + i^{alpha'}) (2/alpha')^j 2^{j/2}.
import math, sys, json, sympy as sp
from sympy import jacobi_symbol, factorint
from latt import lat, Qp
X = sp.Symbol('X')
class Cyc:
    def __init__(self, L): self.L = L; self.phi = sp.Poly(sp.cyclotomic_poly(L, X), X)
    def red(self, d):
        p = sp.Poly(sum(c*X**(e % self.L) for e, c in d.items() if c) or sp.Integer(0), X)
        return tuple(p.rem(self.phi).all_coeffs())
def mul(d1, d2, L):
    o = {}
    for e1, c1 in d1.items():
        for e2, c2 in d2.items(): o[(e1+e2) % L] = o.get((e1+e2) % L, 0) + c1*c2
    return o
def scal(d, k): return {e: c*k for e, c in d.items()}
def zeta(num, den, L): return {(num*(L//den)) % L: 1}      # e(num/den), den | L
def sqrt2(L): return {L//8: 1, (-L//8) % L: 1}
def gauss_q(q, L): return {(L//q*y*y) % L: 0 for y in range(q)} | _gq(q, L)
def _gq(q, L):
    d = {}
    for y in range(q): d[(L//q*y*y) % L] = d.get((L//q*y*y) % L, 0) + 1
    return d
def vq(x, q):
    if x == 0: return 10**9
    v = 0
    while x % q == 0: x //= q; v += 1
    return v
def local(q, n, al, be, ga, L):
    """closed form of sum_{y mod q^n} e((al y^2 + be y + ga)/q^n) as element of Z[zeta_L]"""
    M = q**n; al %= M; be %= M; ga %= M
    v = vq(al, q)
    if v >= n: return scal(zeta(ga, M, L), M) if be % M == 0 else {}
    if be % q**v: return {}
    pre = scal(zeta(ga, M, L), q**v); a1 = al//q**v; b1 = be//q**v; j = n - v; Mj = q**j
    if q != 2:
        if j == 0: return pre
        inv = pow(4*a1, -1, Mj)
        base = zeta(-b1*b1*inv, Mj, L) if True else None
        sym = jacobi_symbol(a1 % q, q)**j
        g = scal(_gq(q, L), q**((j-1)//2)) if j % 2 else {0: q**(j//2)}
        return mul(pre, scal(mul(base, g, L), sym), L)
    if j == 0: return pre
    if j == 1: return scal(pre, 2) if b1 % 2 else {}
    if b1 % 2: return {}
    inv = pow(a1, -1, Mj)
    base = zeta(-inv*(b1//2)**2, Mj, L)
    one_i = {0: 1} ; one_i[(L//4*a1) % L] = one_i.get((L//4*a1) % L, 0) + 1
    sgn = jacobi_symbol(2, a1 % 8 if a1 % 8 else 8)**j if True else 1
    two = {0: 2**(j//2)} if j % 2 == 0 else scal(sqrt2(L), 2**(j//2))
    return mul(pre, scal(mul(mul(base, one_i, L), two, L), sgn), L)
def H_closed(s, a, N, c, L):
    g, m, b, nw, kw = lat(s)
    A2 = 2*m*m + 2*s*m*b + s*b*b
    Bw = 2*nw*m + s*(nw*b + kw*m) + s*kw*b
    B2 = 2*c*Bw + s*b; C = Qp(s, c*nw, c*kw)
    fac = factorint(N); k = fac.pop(2, 0)
    # partial fractions a/N = sum a_q / q^e
    parts = {}
    for q, e in list(fac.items()) + ([(2, k)] if k else []):
        Q = q**e; R = N//Q
        parts[(q, e)] = (a*pow(R, -1, Q)) % Q       # a/N = sum_q a_q/Q mod 1
    out = {0: 2} if k == 0 else {0: 1}
    for (q, e), aq in parts.items():
        if q == 2:
            T = local(2, e + 1, aq*A2, aq*B2, 2*aq*C, L)
        else:
            i2 = pow(2, -1, q**e)
            T = local(q, e, aq*A2*i2, aq*B2*i2, aq*C, L)
        out = mul(out, T, L)
    return out
def H_brute(s, a, N, c, L):
    g, m, b, nw, kw = lat(s); d = {}
    for y in range(2*N):
        ex = (a*Qp(s, c*nw + y*m, c*kw + y*b)) % N
        d[ex*(L//N) % L] = d.get(ex*(L//N) % L, 0) + 1
    return d
if __name__ == "__main__":
    Ns = [int(z) for z in sys.argv[1].split(',')]; smax = int(sys.argv[2])
    res = {}
    for N in Ns:
        L = math.lcm(8, 2*N); C = Cyc(L); bad = 0; tests = 0
        for a in [a for a in range(1, N) if math.gcd(a, N) == 1]:
            for s in range(5, smax):
                for c in range(2*N):
                    tests += 1
                    if C.red(H_closed(s, a, N, c, L)) != C.red(H_brute(s, a, N, c, L)): bad += 1
        res[N] = dict(tests=tests, mismatches=bad); print(N, res[N], flush=True)
    json.dump(res, open('gauss_local_%s.json' % sys.argv[1].replace(',', '-'), 'w'))
