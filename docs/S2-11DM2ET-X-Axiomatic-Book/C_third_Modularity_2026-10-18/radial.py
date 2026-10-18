# Exact radial expansions of C_third and E at rationals x:  S(e(x) e^{-t}) = s(x)/t + h(x) t^{-1/2} + c(x) + O(t^{1/2}).
#   C_third = q^{7/20} * sum_{nu in C0 cap (-a+Z^2)} q^{Q2(nu)} - sum_{n>=1} q^{n^2}     (C0 = open quadrant; checked as series below)
#   E       = q^{7/20} * E_L,  E_L = sum_{nu in F cap (a+Z^2)} q^{Q2(nu)}
# Cone constants: 2-D Euler-Maclaurin on residue classes mod 4m (the formula of psi-conditions/kappa_all.py, which is PARI-free),
# recomputed here for the single quadrant cone (which=0) and for F.  Three routes for Z_x(0) := sum_{a in K} e(x Na/20) Na^{-s}|_{s=0}:
#   (i) lattice EM: kappa_L(x);  (ii) ideal-side Shintani cone sums (exact Fractions);  (iii) genus formula with Hurwitz zeta(0,.) = 1/2 - a.
import numpy as np, math, cmath, sys, pickle
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
sys.path.insert(0, '/workspace/quantum-comp/reports/heavy-daily/2026-10-17-psi-conditions')
sys.path.insert(0, '/workspace/quantum-comp/reports/heavy-daily/2026-10-18-PARI-free')
import kappa_all
from kappa_all import IC, SP
import shintani as sh, cyc24
D = 70
I = math.log(6+math.sqrt(35))/(2*math.sqrt(35))
def EF0(al70, x):
    """(s,h,c) of sum over the open quadrant cone nu1 > 0, nu2 >= 0 of coset al70/70 (no twist)"""
    x = Fr(x); h, m = x.numerator, x.denominator; L = 4*m
    i = np.arange(L, dtype=np.int64)[:, None]; j = np.arange(L, dtype=np.int64)[None, :]
    u0 = al70[0] % D or D; w0 = al70[1] % D
    A11, A12, A22 = 1.0, 3.5, 3.5
    U = np.broadcast_to(u0+D*i, (L, L)).astype(np.int64); W = np.broadcast_to(w0+D*j, (L, L)).astype(np.int64)
    q = 2*U*U + 14*U*W + 7*W*W
    ph = np.exp(2j*np.pi*((h*q) % (9800*m))/(9800*m))
    su = U/(D*L); sw = W/(D*L)
    s = IC[0]*ph.sum()/L**2
    hh = np.sum(ph*(-(sw-0.5)*SP/(2*math.sqrt(A11)) - (su-0.5)*SP/(2*math.sqrt(A22))))/L
    c = np.sum(ph*((sw*sw-sw+1/6)*A12/(2*A11) + (su*su-su+1/6)*A12/(2*A22) + (su-0.5)*(sw-0.5)))
    return complex(s), complex(hh), complex(c)
def g1(x):
    x = Fr(x); h, m = x.numerator, x.denominator
    return sum(cmath.exp(2j*math.pi*((h*r*r) % m)/m) for r in range(m))/m
def ez(y): return cmath.exp(2j*math.pi*float(Fr(y) % 1))
def Cthird_exp(x):
    s0, h0, c0 = EF0((21, 14), x)
    f = ez(Fr(7, 20)*Fr(x))
    return f*s0, f*h0 - SP/2*g1(x), 0.5 + f*(c0 - 0.35*s0)
def E_exp(x):
    s, hh, c = kappa_all.EF(np.array([49, -14]), np.array([0, 0]), x)
    f = ez(Fr(7, 20)*Fr(x))
    return f*s, f*hh, f*(c - 0.35*s), complex(c)        # last: kappa_L(x)
def G(x):      # Gauss mean of Q_s (C_third leading coefficient is I*G)
    x = Fr(x); h, m = x.numerator, x.denominator
    n, k = np.meshgrid(np.arange(2*m), np.arange(2*m), indexing='ij')
    Q = n*n + 7*n*k + (7*k*(k+1))//2
    return complex(np.exp(2j*np.pi*((h*Q) % m)/m).mean())
# (iii) genus/Hurwitz formula for Z_x(0)
hh280 = pickle.load(open('genus_h_280.pkl', 'rb'))
def kron140(n):
    if n % 2 == 0: return 0
    a, m, t = 35 % n, n, 1
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5): t = -t
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3: t = -t
        a %= m
    return t if m == 1 else 0
def Z_genus(x):
    x = Fr(x); h, m = x.numerator, x.denominator
    L = 280*20*m//math.gcd(280, 20*m)
    d0 = np.arange(1, L+1)
    chi = np.array([kron140(int(v)) for v in d0 % 140]); chi[(d0 % 140) == 0] = 0
    Hm = np.array([float(hh280.get(int(v), 0)) for v in range(280)])
    tot = 0j
    B = 0.5 - d0/L
    nz = np.nonzero(chi)[0]
    for i in nz:
        Nn = (d0[i]*d0) % L
        w = Hm[Nn % 280]*np.exp(2j*np.pi*((h*Nn) % (20*m))/(20*m))
        tot += chi[i]*B[i]*np.sum(w*B)
    return tot
# (ii) ideal-side Shintani: mu' = -mu has signs (+,-): cone ('P','+-'); coset A' = 0 mod 7, A' - 5B' = 3 mod 10; N(a) = |N mu|/7
def Z_shintani(x):
    x = Fr(x); h, m = x.numerator, x.denominator; Mp = 70*m
    a, b, T1, T2, Nv = sh.cone_points('P', '+-', Mp)
    ok = (a % 7 == 0) & ((a - 5*b) % 10 == 3)
    a, b, T1, T2 = a[ok], b[ok], T1[ok], T2[ok]
    Na = np.abs(a*a - 35*b*b)//7
    K = 20*m; key = Na % K
    T1o = T1.astype(object); T2o = T2.astype(object)
    num = 4*T1o*T2o + 12*T1o**2 + 12*T2o**2 - 14*Nv*(T1o+T2o) + 5*Nv*Nv
    tot = 0j; exact = {}
    for r in np.unique(key):
        sel = key == r
        z = Fr(int(np.sum(num[sel])), 4*Nv*Nv)
        exact[int(r)] = z
        tot += float(z)*cmath.exp(2j*math.pi*((h*int(r)) % K)/K)
    return tot, exact
if __name__ == '__main__':
    out = []; P = lambda s: (print(s, flush=True), out.append(s))
    # series sanity of the cone representation of C_third and E (to q^400)
    d = np.load('series.npz'); NN = 400
    # quadrant cone of coset -a: nu = (n - 7/10, k + 1/5), n >= 1, k >= 0  ->  exponent Q_-(n,k) = Q2(nu) + 7/20
    n, k = np.meshgrid(np.arange(1, 80), np.arange(0, 80), indexing='ij'); e = n*n + 7*n*k + (7*k*(k-1))//2
    cone = np.bincount(e[e <= NN].ravel(), minlength=NN+1)
    sq = np.zeros(NN+1, int); sq[[r*r for r in range(1, 21)]] = 1
    P(f"series check: C_third == q^(7/20)*[quadrant cone of -a+Z^2] - sum_(n>=1) q^(n^2) to q^{NN}: {(cone - sq == d['Ct'][:NN+1]).all()}")
    xs = [Fr(0), Fr(1, 2), Fr(1, 3), Fr(1, 4), Fr(1, 5), Fr(2, 5), Fr(1, 7), Fr(3, 7), Fr(1, 10), Fr(3, 10), Fr(2, 3), Fr(5, 7), Fr(1, 6), Fr(1, 9)]
    res = {}
    P("\nx | s_C (=I G?) | h_C | c_C | Z_x(0): lattice kappa_L / Shintani / genus-Hurwitz")
    for x in xs:
        sC, hC, cC = Cthird_exp(x); sE, hE, cE, kL = E_exp(x)
        zs, zex = Z_shintani(x) if x.denominator <= 10 else (float('nan'), None)
        zg = Z_genus(x)
        res[x] = dict(sC=sC, hC=hC, cC=cC, sE=sE, hE=hE, cE=cE, kL=kL, zs=zs, zg=zg, G=G(x))
        P(f"{str(x):>5} | {sC:.12f} (IG {I*G(x):.12f}) | {hC:.12f} | {cC:.12f} | {kL:.12f} / {zs:.12f} / {zg:.12f}")
    P(f"\nx=0 closed forms: c_C(0) = (11-7I)/20 = {(11-7*I)/20:.12f}; h_C(0) = -sqrt(pi)(49-2sqrt14)/140 = {-SP*(49-2*math.sqrt(14))/140:.12f}")
    P("consistency of 2 C_third = q^8 f + 1 + E: s_E = 2 s_C, and kappa_(q^8 f) := 2c_C - 1 - c_E (computed below)")
    for x in xs:
        r = res[x]
        P(f"  x={str(x):>5}: |s_E - 2 s_C| = {abs(r['sE']-2*r['sC']):.1e};  kappa_(q8f)(x) = {2*r['cC']-1-r['cE']:.12f};  h_(q8f) = 2h_C - h_E = {2*r['hC']-r['hE']:.12f}")
    pickle.dump(res, open('radial.pkl', 'wb'))
    open('radial.txt', 'w').write("\n".join(out)+"\n")
