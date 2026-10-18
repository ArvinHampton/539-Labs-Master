"""
Block inequalities (rigorous, interval arithmetic) for Lemma L.
Block = members n_i = n + off_i with weights w_i (evens on the left side, odds on the right side).
Reference tilt r = e^{-u/n}, u = saddle of the base layer n (mu_n(r) = m_n). For every member:
  a_{n_i}(m_i) = A_{n_i}(r) r^{-m_i} P(S_i = m_i),
normalised by A_n(r) r^{-m_n} / (sqrt(2pi) sigma_n):
  T_i = rho_i * Ptilde_i,  rho_i = (A_{n_i}/A_n)(r) * r^{(n_i^2-n^2)/7} * sigma_n/sigma_i,
  Ptilde_i = sqrt(2pi) sigma_i P(S_i=m_i) in [exp(-x_i^2/(2 sigma_i^2)) - delta, 1 + delta]   (local CLT, clt.py)
  x_i = m_i - mu_{n_i}(r) = -(n_i^2-n^2)/7 - (mu_{n_i}-mu_n)(r).
Step identity: A_{m+1}/A_m = 1/(1 - (-1)^m r^{m+1})  (L1).
Everything is a function of (u, s=1/n), enclosed over boxes u in U, s in [0, 1/n1].
"""
from mpmath import iv
iv.prec = 100
I = iv.mpf; ONE = I(1)

PATTERNS = {
    1: dict(base_par=1, mem=[(0, 1.0, 'O'), (5, 1.0, 'E'), (7, 1.0, 'E'), (12, 1.0, 'O')]),
    2: dict(base_par=1, mem=[(0, 1.0, 'O'), (1, 1.0, 'E'), (7, 1.0, 'E'), (8, 1.0, 'O')]),
    4: dict(base_par=1, mem=[(0, 1.0, 'O'), (3, 1.0, 'E'), (7, 1.0, 'E'), (10, 1.0, 'O')]),
    0: dict(base_par=0, mem=[(-7, 0.5, 'O'), (0, 1.0, 'E'), (7, 0.5, 'O')]),
}

def member_data(off, base_par, u, s):
    """returns (logratioA, dmu/n, dvar/n^2) for member at offset off relative to base:
       logratioA = log(A_{n+off}/A_n)(r); dmu = mu_{n+off}-mu_n; dvar = sigma^2_{n+off}-sigma^2_n."""
    lr = I(0); dmu = I(0); dvar = I(0)
    steps = range(0, off) if off > 0 else range(off, 0)
    for k in steps:            # step m = n+k -> m+1, a = m+1 = n(1+(k+1)s)
        eps = 1 if (base_par + k) % 2 == 0 else -1   # (-1)^m
        a_over_n = ONE + (k+1)*s
        ra = iv.exp(-u*a_over_n)                      # r^a
        den = ONE - eps*ra
        sgn = 1 if off > 0 else -1                    # factor 1/den for forward steps, den for backward
        lr += -sgn*iv.log(den)
        dmu += sgn*eps*a_over_n*ra/den                # (r d/dr) log(1/den) = eps a r^a/den ; divided by n
        dvar += sgn*eps*a_over_n**2*ra/den**2         # (r d/dr)^2 log(1/den) = eps a^2 r^a/den^2 ; /n^2
    return lr, dmu, dvar

def block_ratio(cls, u, n1, S_lo_fn, delta):
    """upper bound of  sum_E w T / sum_O w T  over u (interval), all n>=n1.
       S_lo_fn(uinterval) -> lower bound for sigma^2/n^3 valid on that u-interval (n>=n1-7)."""
    pat = PATTERNS[cls]; s = I([0, (ONE/I(n1-7)).b])
    Sb = S_lo_fn(u)     # base sigma^2 >= n^3 Sb
    num = I(0); den = I(0)
    for off, w, typ in pat['mem']:
        lr, dmu, dvar = member_data(off, pat['base_par'], u, s)
        # r^{(n_i^2-n^2)/7} = exp(-u(2 off + off^2 s)/7)
        lr2 = -u*(2*off + off*off*s)/7
        # sigma_i^2/sigma_n^2 = 1 + dvar*n^2/sigma_n^2 ; |.| <= |dvar| s / Sb
        q = dvar*s/Sb if off != 0 else I(0)
        q = I([min(q.a, 0) if off != 0 else 0, max(q.b, 0) if off != 0 else 0]) if off != 0 else I(0)
        # bound q in interval [-|dvar|s/Sb, |dvar|s/Sb]
        if off != 0:
            mag = I(max(abs(dvar.a), abs(dvar.b)))*s.b/Sb
            q = I([(-mag).a, mag.b])
        sig_ratio = ONE/iv.sqrt(ONE + q)                 # sigma_n/sigma_i
        rho = iv.exp(lr + lr2)*sig_ratio
        # x_i/n = -(2off+off^2 s)/7 - dmu ; x_i^2/(2 sigma_i^2) <= n^2 X^2/(2 n_i^3 S_i) <= X^2 s'/(2 S_i)
        X = -(2*off + off*off*s)/7 - dmu
        X2 = I(max(abs(X.a), abs(X.b)))**2
        ui = u*(ONE + off*s)
        Si = S_lo_fn(ui)
        # n_i >= n-7 -> 1/n_i^3 <= (1/n^3)(1+7/(n-7))^3 ; use s range
        gfac = X2*s.b*(ONE+7*s.b)**3/(2*Si)
        if typ == 'E':
            num += w*rho*(ONE+delta)
        else:
            lo = ONE - gfac - delta
            den += w*rho*lo
    R = num/den
    return R.b

if __name__ == '__main__':
    import sys
    from clt import constants
    n1 = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    delta = I(float(sys.argv[2])) if len(sys.argv) > 2 else I(0.12)
    def S_lo_fn(uint):
        return I(constants(uint.a, uint.b, n1-7, 0.5)['S_lo'])
    for cls in (0, 1, 2, 4):
        worst = 0; wu = None
        uu = 0.2
        while uu < 1.6 - 1e-12:
            u = I([uu, uu+0.05])
            R = block_ratio(cls, u, n1, S_lo_fn, delta)
            if R > worst: worst, wu = R, uu
            uu += 0.05
        print('class', cls, 'max ratio E/O in block:', float(worst), 'at u~', wu)
