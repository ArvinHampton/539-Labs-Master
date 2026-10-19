# copy of Analytic-CatB-Push/asym_engine.py expansion() with a free second edge u2=(m,b) (m>0, primitive)
# Open-Analytic, item 1/2: full small-t expansion of H_s(e(x) e^{-t}) for rational x = a/N via the PROVED quadrant
# Euler-Maclaurin (Zagier) lemma (see 2026-10-18-Open-Analytic.md, sec. 2).  No F1 citation is used.
#   H_s(q) = sum_{nu in cone} w(nu) (q^{Q+(nu)} - q^{Q-(nu)}),  Q+-(n,k) = n^2 + s n k + s k(k+-1)/2,
#   cone = {n >= 0, 3 s k >= (s-8) n}, weight 1/2 on both edges (origin contributes 0).
# Decomposition: u1 = (0,1), u2 = (m,b) (m = 3s/g, b = (s-8)/g, g = gcd(24,s-8));  P = 2N (P = 1 if x = 0);  U_i = P u_i.
#   Z^2 cap cone = disjoint union over p in Pi (half-open parallelogram of U1,U2) of p + N0 U1 + N0 U2;  e(x Q+-) is constant
#   on each piece.  Each piece: sum_{j,k>=0} F(eps(j+al), eps(k+be)),  eps = sqrt t,  F(X,Y) = exp(-q(X,Y) -+ eps lam l(X,Y)).
#   Zagier 2-D:  ~ eps^-2 I  - eps^-1 sum_m Bt_{m+1}(be)/(m+1)! eps^m int dX d_Y^m F(X,0)
#                 - sum_n Bt_{n+1}(al)/(n+1)! eps^{n-1} int dY d_X^n F(0,Y) + sum_{n,m} Bt Bt eps^{n+m} d_X^n d_Y^m F(0,0),
#   where Bt_{r}(c) = B_r(c), except Bt_1(0) = 0 (half weight on the edge).
import sympy as sp, mpmath as mp, sys, json, math
from fractions import Fraction as Fr
mp.mp.dps = 70
X, Y = sp.symbols('X Y', real=True)
def bern(r, c):
    if r == 1 and c == 0: return sp.Integer(0)
    return sp.bernoulli(r, sp.Rational(c))
def expansion(s, a=0, N=1, K=7, u2=None):
    """coefficients c[e] of eps^e (e = -2..K) of H_s(e(a/N) e^{-t}), eps = sqrt(t); returned as mpc."""
    g = math.gcd(24, s - 8); m = 3*s//g; b = (s - 8)//g; lam = sp.Rational(s, 2)
    if u2 is not None: m, b = u2
    P = 1 if a % N == 0 else 2*N
    U1 = (0, P); U2 = (P*m, P*b)
    nvec = X*U1[0] + Y*U2[0]; kvec = X*U1[1] + Y*U2[1]
    q = sp.expand(nvec**2 + s*nvec*kvec + sp.Rational(s, 2)*kvec**2); l = sp.expand(kvec)
    # pieces
    pieces = []
    for n in range(0, P*m):
        be = Fr(n, P*m)
        kmin = math.ceil(Fr(b*n, m)); 
        for k in range(kmin, kmin + P + 1):
            al = Fr(k - Fr(b*n, m), P)
            if not (0 <= al < 1): continue
            Qp = n*n + s*n*k + s*k*(k+1)//2; Qm = n*n + s*n*k + s*k*(k-1)//2
            pieces.append((al, be, Qp, Qm))
    assert len(pieces) == P*P*m, (len(pieces), P*P*m)
    ph = lambda Qv: mp.expj(2*mp.pi*mp.mpf(a)*(Qv % N)/N) if N > 1 else mp.mpc(1)
    imax = K + 2
    # Gauss-type sums with Bernoulli weights
    from collections import defaultdict
    Sal = defaultdict(lambda: mp.mpc(0)); Sbe = defaultdict(lambda: mp.mpc(0)); Sab = defaultdict(lambda: mp.mpc(0)); S0 = {1: mp.mpc(0), -1: mp.mpc(0)}
    for al, be, Qp, Qm in pieces:
        for sg, Qv in ((1, Qp), (-1, Qm)):
            f = ph(Qv); S0[sg] += f
            for r in range(1, imax + 3):
                Sal[(sg, r)] += f*mp.mpf(sp.Rational(bern(r, al)))
                Sbe[(sg, r)] += f*mp.mpf(sp.Rational(bern(r, be)))
            for r1 in range(1, imax + 3):
                for r2 in range(1, imax + 3 - r1 + 1):
                    Sab[(sg, r1, r2)] += f*mp.mpf(sp.Rational(bern(r1, al)))*mp.mpf(sp.Rational(bern(r2, be)))
    c = defaultdict(lambda: mp.mpc(0))
    E = sp.exp(-q)
    qx0 = q.subs(Y, 0); q0y = q.subs(X, 0)
    for i in range(0, imax + 1):
        for sg in (1, -1):
            # F = sum_i (-sg lam eps l)^i / i! e^{-q};   H gets sign +1 for Q+, -1 for Q-  -> overall factor sg
            pref = sg*(-sg*lam)**i/sp.factorial(i)
            G = l**i*E
            # area: eps^{i-2}
            e = i - 2
            if e <= K:
                # int int l^i e^{-q} over quadrant = Gamma((i+2)/2)/2 * int_0^inf l(1,mu)^i / q(1,mu)^{(i+2)/2} dmu
                lf = sp.lambdify(Y, l.subs(X, 1), 'mpmath'); qf = sp.lambdify(Y, q.subs(X, 1), 'mpmath')
                I = mp.gamma(mp.mpf(i + 2)/2)/2*mp.quad(lambda mu: lf(mu)**i/qf(mu)**(mp.mpf(i + 2)/2), [0, 1, mp.inf])
                c[e] += mp.mpf(sp.Rational(pref))*I*S0[sg]
            # edges
            for r in range(0, K + 2 - i):
                e = i - 1 + r
                if e > K: break
                dY = sp.diff(G, Y, r).subs(Y, 0); dX = sp.diff(G, X, r).subs(X, 0)
                IY = sp.integrate(sp.expand(dY), (X, 0, sp.oo)); IX = sp.integrate(sp.expand(dX), (Y, 0, sp.oo))
                c[e] += -mp.mpf(sp.Rational(pref))/mp.factorial(r + 1)*(mp.mpf(sp.N(IY, 50))*Sbe[(sg, r + 1)] + mp.mpf(sp.N(IX, 50))*Sal[(sg, r + 1)])
            # corners
            for n1 in range(0, K + 1 - i):
                for n2 in range(0, K + 1 - i - n1):
                    e = i + n1 + n2
                    d = sp.diff(G, X, n1, Y, n2).subs({X: 0, Y: 0}) if (n1 or n2) else G.subs({X: 0, Y: 0})
                    if d == 0: continue
                    c[e] += mp.mpf(sp.Rational(pref))*mp.mpf(sp.Rational(d))/(mp.factorial(n1 + 1)*mp.factorial(n2 + 1))*Sab[(sg, n1 + 1, n2 + 1)]
    return {e: c[e] for e in range(-2, K + 1)}
