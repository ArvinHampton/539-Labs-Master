# PARI-free Shintani evaluation of Z(0) = "sum_{a coprime to 70} w(a) N(a)^-s at s = 0" for weights w that depend on
# (ray class of a, N(a) mod K).  Ideals: principal a = (mu), mu in O (mu > 0 at the first place, two sign patterns),
# non-principal a = (mu) p13'^{-1}, mu in p13' = {a + 3b = 0 mod 13}; units: cone [v, eps v) is a fundamental domain mod <eps>.
# For cone generators v1 = v, v2 = eps v:  |N(t1 v1 + t2 v2)| = |N v| (t1^2 + 12 t1 t2 + t2^2), and (2-dim Euler-Maclaurin)
#   zeta_cone(0; x) = B1(x1) B1(x2) + 3 (B2(x1) + B2(x2)),   x1 in (0,1], x2 in [0,1).
import numpy as np, math
from fractions import Fraction as Fr
CONES = {  # (kind, sign pattern) -> omega (cone direction), lattice
    ('P', '++'): ((1, 0), 'O'), ('P', '+-'): ((5, 1), 'O'),          # N(5+sqrt35) = -10, signs (+,-)
    ('N', '++'): ((10, 1), 'p13b'), ('N', '+-'): ((-3, 1), 'p13b'),  # 10+sqrt35 (N=65), -3+sqrt35 (N=-26), both in p13'
}
def cone_points(kind, sp, Mp):
    """all mu = (a,b) in lattice with mu = t1 v1 + t2 eps v1, v1 = Mp*omega, t1 in (0,1], t2 in [0,1).
    Returns a, b, T1num, T2num, Nv  with t_i = T_inum / Nv (Nv > 0)."""
    (p, r), lat = CONES[(kind, sp)]
    p, r = Mp*p, Mp*r
    Nv = p*p - 35*r*r
    # t2 = (b p - a r)/Nv ; t1 = (a (p+6r) - b (35 r + 6 p))/Nv
    vs = [(0, 0), (p, r), (6*p+35*r, p+6*r), (7*p+35*r, p+7*r)]
    bmin = min(v[1] for v in vs); bmax = max(v[1] for v in vs)
    A_l = []; B_l = []
    sN = 1 if Nv > 0 else -1; aN = abs(Nv)
    for b in range(bmin, bmax+1):
        # interval in a from both constraints (as reals), then exact filter
        lo, hi = -math.inf, math.inf
        for (ca, cb, L, H) in ((-r, b*p, 0, aN), (p+6*r, -b*(35*r+6*p), 0, aN)):
            # constraint: L <= sN*(ca*a + cb) <= H
            c = sN*ca; d = sN*cb
            if c == 0:
                if not (L <= d <= H): lo, hi = 1, 0
                continue
            x1 = (L-d)/c; x2 = (H-d)/c
            lo = max(lo, min(x1, x2)); hi = min(hi, max(x1, x2))
        if hi < lo: continue
        a = np.arange(math.floor(lo)-1, math.ceil(hi)+2, dtype=np.int64)
        A_l.append(a); B_l.append(np.full(len(a), b, dtype=np.int64))
    a = np.concatenate(A_l); b = np.concatenate(B_l)
    T2 = sN*(b*p - a*r); T1 = sN*(a*(p+6*r) - b*(35*r+6*p))
    ok = (T2 >= 0) & (T2 < aN) & (T1 > 0) & (T1 <= aN)
    if lat == 'p13b': ok &= ((a + 3*b) % 13 == 0)
    a, b, T1, T2 = a[ok], b[ok], T1[ok], T2[ok]
    return a, b, T1, T2, aN
def kernel_float(T1, T2, Nv):
    t1 = T1/Nv; t2 = T2/Nv
    B1 = lambda t: t-0.5; B2 = lambda t: t*t-t+1/6
    return B1(t1)*B1(t2) + 3*(B2(t1)+B2(t2))
def kernel_exact(t1n, t2n, Nv):
    t1 = Fr(int(t1n), Nv); t2 = Fr(int(t2n), Nv)
    B2 = lambda t: t*t-t+Fr(1, 6)
    return (t1-Fr(1, 2))*(t2-Fr(1, 2)) + 3*(B2(t1)+B2(t2))
def iota_vec(a, b, e2):
    """vectorised iota (G0 coordinates without signs) for units at 2,5,7"""
    L5 = np.array([0, 0, 1, 3, 2]); L7 = np.array([0, 0, 2, 1, 4, 5, 3])
    k5 = L5[a % 5]; k7 = L7[a % 7]
    if e2 == 3:
        tab = np.zeros((2, 4), dtype=np.int64); tab[1, 1] = 0; tab[0, 3] = 1; tab[1, 3] = 2; tab[0, 1] = 3
        k2 = tab[a % 2, (a-b) % 4]
    else:
        k2 = (a % 2 == 0).astype(np.int64)
    return k2, k5, k7
def unit70(a, b): return ((a+b) % 2 == 1) & (a % 5 != 0) & (a % 7 != 0)
