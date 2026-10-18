# Independent audit helpers (written from scratch; nothing imported from the audited folder).
# Characters, Gauss sums, rho, digamma-form R_chi, Lambert series G_chi, T_chi, lattice sums E_L, E_R.
import mpmath as mp, math
from sympy import jacobi_symbol
from functools import lru_cache
mp.mp.dps = 36
# ---- characters mod 20: psi = chi5^e5 * chi_{-4}^s4 ; chi5(2)=i (quartic char mod 5)
IND5 = {1:0, 2:1, 4:2, 3:3}
def chi5(n, e):
    n %= 5
    return 0 if n == 0 else [1, 1j, -1, -1j][(e*IND5[n]) % 4]
def chim4(n):
    n %= 4
    return {1:1, 3:-1}.get(n, 0)
# (j,l) -> (e5, s4), the table of the Cusp-Part report (I1 input); w_chi = e(-j/8)/16
GEN = {(0,0):(0,0),(0,1):(0,1),(2,0):(3,1),(2,1):(3,0),(4,0):(2,0),(4,1):(2,1),(6,0):(1,1),(6,1):(1,0)}
def psi(key, n):
    e5, s4 = GEN[key]
    v = chi5(n, e5) * (chim4(n) if s4 else 1)
    return v
def chi140(n):
    n %= 140
    if math.gcd(n, 140) != 1: return 0
    return int(jacobi_symbol(35, n))      # Kronecker (140/n) = (35/n) for odd n
def ee(x): return mp.expjpi(2*x)
class Char:
    def __init__(s, key):
        s.key = key
        s.a = [mp.mpc(psi(key, r)) if math.gcd(r, 10) == 1 else mp.mpc(0) for r in range(20)]
        s.b = [mp.mpc(psi(key, r) * chi140(r)) for r in range(140)]
        s.ach = [mp.fsum(s.a[r]*ee(mp.mpf(k*r)/20) for r in range(20)) for k in range(20)]
        s.bh = [mp.fsum(s.b[r]*ee(mp.mpf(n*r)/140) for r in range(140)) for n in range(140)]
        s.rho = [-s.bh[n]/(2j*mp.pi*140) for n in range(140)]       # rho_n, 140-periodic
        s.eta_a = 1 if abs(s.a[19]-1) < 1e-20 else -1
        s.eta_b = 1 if abs(s.b[139]-1) < 1e-20 else -1
        s.mean = mp.fsum(s.a)
        s.w = ee(-mp.mpf(key[0])/8)/16
        s._beta = {}
    def beta(s, k):    # beta_k = sum_s rho_s B_k(s/140)
        if k not in s._beta:
            s._beta[k] = mp.fsum(s.rho[t % 140]*mp.bernpoly(k, mp.mpf(t)/140) for t in range(1, 141))
        return s._beta[k]
    def phi(s, X):     # sum_{s=1}^{140} rho_s digamma(s/140 + X)
        return mp.fsum(s.rho[t % 140]*mp.digamma(mp.mpf(t)/140 + X) for t in range(1, 141))
    def R(s, z, M=None, K=40):
        """R(z) = sum_{m>=1} a(m) phi(m/(20z)); explicit sum m<=M, tail by the asymptotic
        phi(X) ~ sum_k (-1)^{k+1} beta_k/(k X^k) summed with Hurwitz zeta (k=1: digamma, needs mean(a)=0 or beta_1=0)."""
        z = mp.mpc(z)
        if M is None:
            M = 20*int(math.ceil(30*abs(complex(z))))       # |X_M| >= 30
        assert M % 20 == 0
        val = mp.fsum(s.a[m % 20]*s.phi(mp.mpf(m)/(20*z)) for m in range(1, M+1) if s.a[m % 20] != 0)
        for k in range(1, K+1):
            bk = s.beta(k)
            if abs(bk) < mp.mpf(10)**(-30): continue
            if k == 1:
                assert abs(s.mean) < 1e-25
                tail = -mp.fsum(s.a[r % 20]*mp.digamma(mp.mpf(M+r)/20) for r in range(1, 21))/20
            else:
                tail = mp.fsum(s.a[r % 20]*mp.zeta(k, mp.mpf(M+r)/20) for r in range(1, 21))/mp.mpf(20)**k
            val += (-1)**(k+1)*bk/k*(20*z)**k*tail
        return val
    def G(s, tau, digits=34):
        """G_chi(tau) = sum_{m,k>=1} a(m) b(k) e(mk tau)"""
        tau = mp.mpc(tau); N = int((digits+2)*math.log(10)/(2*math.pi*float(tau.imag)))+2
        lam = [mp.mpc(0)]*(N+1)
        for m in range(1, N+1):
            am = s.a[m % 20]
            if am == 0: continue
            for k in range(1, N//m+1): lam[m*k] += am*s.b[k % 140]
        q = ee(tau)
        return mp.polyval(lam[::-1], q)
    def Tser(s, z, digits=34):
        """(z/140) sum_{n,k>=1} bhat(n) acheck(k) e(nkz/140)"""
        z = mp.mpc(z); N = int((digits+2)*math.log(10)*140/(2*math.pi*float(z.imag)))+2
        c = [mp.mpc(0)]*(N+1)
        for n in range(1, N+1):
            bn = s.bh[n % 140]
            if abs(bn) < 1e-25: continue
            for k in range(1, N//n+1): c[n*k] += bn*s.ach[k % 20]
        q = ee(z/140)
        return z/140*mp.polyval(c[::-1], q)
CH = None
def chars():
    global CH
    if CH is None: CH = {k: Char(k) for k in GEN}
    return CH
# ---- lattice side, from scratch. Gram A=[[2,7],[7,7]], Q(v)=v.Av/2, a=(7/10,-1/5), cone F=[e1, g e1), g e1=(-1,2).
# nu = s*e1 + t*(-1,2): t = nu2/2, s = nu1 + nu2/2 ; F: s>0, t>=0.
def EL_coeffs(Qmax):
    """{20*Q : multiplicity} for nu in F cap (a+Z^2), Q(nu)<=Qmax. Uses 10*nu integer."""
    out = {}
    B = int(4*math.sqrt(Qmax))+3
    for n1 in range(-B, B+1):
        for n2 in range(-B, 2*B+1):
            X = 7 + 10*n1; Y = -2 + 10*n2        # 10*nu
            t2 = Y                                # 20*t = 2*Y/... sign only: t>=0 <=> Y>=0
            s2 = 2*X + Y                           # sign of s
            if not (s2 > 0 and Y >= 0): continue
            q200 = 2*X*X + 14*X*Y + 7*Y*Y          # 200*Q
            if q200 > 200*Qmax: continue
            assert q200 % 10 == 0
            N = q200//10                           # 20*Q
            out[N] = out.get(N, 0) + 1
    return out
def ER_coeffs(Qmax, prec=False):
    """{140*Q : sum e(B(nu,-a))} for nu in F cap L', L' = A^{-1}Z^2, nu = A^{-1}m.  B(nu,-a) = -m.a = -(7 m1 - 2 m2)/10."""
    out = {}
    B = int(30*math.sqrt(Qmax))+5
    for m1 in range(-B, B+1):
        for m2 in range(-B, B+1):
            X = -7*m1 + 7*m2; Y = 7*m1 - 2*m2      # 35*nu
            if not (2*X + Y > 0 and Y >= 0): continue
            # 140*Q = 140 * nu.A.nu/2 = 2*(-7 m1^2 + 14 m1 m2 - 2 m2^2)
            N = 2*(-7*m1*m1 + 14*m1*m2 - 2*m2*m2)
            assert N > 0
            if N > 140*Qmax: continue
            ph = (-(7*m1 - 2*m2)) % 10
            out.setdefault(N, [0]*10)[ph] += 1
    return out
