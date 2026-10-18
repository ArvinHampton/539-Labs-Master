# Path B: q-series closed form of H_s (Theorem-G_s style), Zwegers parameters in s, characteristic correction, shadow data.
# Master definition: H_s = sum_{v in Z^2} w(v) q^{Q_s(v)}, Q_s(n,k) = n^2 + s n k + (s/2) k(k+1),
#   w = (sgn B(c1,v) - sgn B(c2,v))/2, B(c,v) = c^T M v, M = [[2,s],[s,s]], c1 = (-1,1), c2 = (-4,1).
import sympy as sp, math, sys, json
from fractions import Fraction as Fr
from collections import defaultdict
sgn = lambda x: (x > 0) - (x < 0)
def Qs(s, n, k): return n*n + s*n*k + (s*k*(k+1))//2
def box(s, N):
    # Q2 is positive definite on the cone K and -K where w != 0; crude bound via smallest eigen-direction inside the cone
    import numpy as np
    th = np.linspace(0, 2*np.pi, 20001); x, y = np.cos(th), np.sin(th)
    B1 = (s-2)*x; B2 = (s-8)*x - 3*s*y
    w = (np.sign(B1) - np.sign(B2))/2
    q = x*x + s*x*y + s/2*y*y
    mn = q[np.abs(w) > 0].min()
    assert mn > 0
    return int(math.sqrt((N + s)/mn)) + 3
def H_master(s, N):
    B = box(s, N); h = defaultdict(Fr)
    for n in range(-B, B+1):
        for k in range(-B, B+1):
            w = Fr(sgn((s-2)*n) - sgn((s-8)*n - 3*s*k), 2)
            if w == 0: continue
            e = Qs(s, n, k)
            if e <= N: h[e] += w
    return {e: v for e, v in h.items() if v != 0}
def H_closed(s, N):
    # Closed form (proved below by case analysis of w):
    # H_s = sum_{n>=1} sum_{k > (s-8)n/(3s)} (q^{Q_s(n,k)} - q^{Q_s(n,k) - s k})
    #     + 1/2 sum_{k>=1} (q^{s k(k+1)/2} - q^{s k(k-1)/2})
    #     + 1/2 sum_{n>=1, 3s | (s-8)n} (q^{Q_s(n,k_n)} - q^{Q_s(n,k_n) - s k_n}),  k_n = (s-8)n/(3s).
    h = defaultdict(Fr); B = box(s, N)
    for n in range(1, B+1):
        kmin = math.floor(Fr((s-8)*n, 3*s)) + 1
        for k in range(kmin, kmin + 4*B):
            e1 = Qs(s, n, k); e2 = e1 - s*k
            if min(e1, e2) > N and k > 0: break
            if e1 <= N: h[e1] += 1
            if e2 <= N: h[e2] -= 1
        if ((s-8)*n) % (3*s) == 0:
            kn = (s-8)*n//(3*s); e1 = Qs(s, n, kn); e2 = e1 - s*kn
            if e1 <= N: h[e1] += Fr(1, 2)
            if e2 <= N: h[e2] -= Fr(1, 2)
    for k in range(1, B+2):
        if s*k*(k+1)//2 <= N: h[s*k*(k+1)//2] += Fr(1, 2)
        if s*k*(k-1)//2 <= N: h[s*k*(k-1)//2] -= Fr(1, 2)
    return {e: v for e, v in h.items() if v != 0}
def H_zw(s, N):
    # (1/2) q^{c0} theta^{c1,c2}_{a,0}(hol), weights from B(c, nu), nu = v + a; exponents Q(nu) + c0 = Q_s(v)
    B = box(s, N) + 2; h = defaultdict(Fr)
    for n in range(-B, B+1):
        for k in range(-B, B+1):
            b1 = Fr(2*(s-2)*n + s, 2); b2 = Fr(2*((s-8)*n - 3*s*k) + s, 2)    # B(c1,nu), B(c2,nu); B(c_i, a) = s/2
            w = Fr(sgn(b1) - sgn(b2), 2)
            if w == 0: continue
            e = Qs(s, n, k)
            if e <= N: h[e] += w
    return {e: v for e, v in h.items() if v != 0}
def Delta_lines(s, N):
    # H_s - H_zw = -1/2 sum_{k in Z} q^{s k(k+1)/2}  (c1: line n = 0)
    #            + sum_{v: -s/2 < L(v) < 0} q^{Q_s(v)} + 1/2 sum_{v: L(v) in {0, -s/2}} q^{Q_s(v)},   L(v) = (s-8)n - 3sk
    # each line L = l (l in gZ, g = gcd(24, s-8)) is a full positive-definite unary theta in j along u2 = (3s, s-8)/g.
    B = box(s, N) + 2; h = defaultdict(Fr)
    for k in range(-B, B+1):
        e = s*k*(k+1)//2
        if e <= N: h[e] -= Fr(1, 2)
    Bl = 4*B + 50
    for n in range(-Bl, Bl+1):
        for k in range(-Bl, Bl+1):
            L = (s-8)*n - 3*s*k
            if 2*L < -s or L > 0: continue
            e = Qs(s, n, k)
            if e > N: continue
            h[e] += Fr(1, 2) if (L == 0 or 2*L == -s) else 1
    return {e: v for e, v in h.items() if v != 0}
def add(a, b, sb=1):
    r = defaultdict(Fr, a)
    for e, v in b.items(): r[e] += sb*v
    return {e: v for e, v in r.items() if v != 0}
def params():
    s = sp.symbols('s', positive=True)
    M = sp.Matrix([[2, s], [s, s]]); c1 = sp.Matrix([-1, 1]); c2 = sp.Matrix([-4, 1])
    Q = lambda v: sp.expand((v.T*M*v)[0]/2); Bf = lambda u, v: sp.expand((u.T*M*v)[0])
    a = sp.simplify(M.inv()*sp.Matrix([0, s/2]))
    u1 = sp.Matrix([0, 1]); u2 = sp.Matrix([3*s, s-8])         # B(c_i, u_i) = 0 ; u2 primitive after dividing by g = gcd(24, s-8)
    out = {
      'M': str(M.tolist()), 'det M': str(sp.factor(M.det())), 'a = M^{-1}(0,s/2)': str(list(a)), 'Q(a) = -c0': str(sp.factor(Q(a))),
      'Q(c1)': str(sp.factor(Q(c1))), 'Q(c2)': str(sp.factor(Q(c2))), 'B(c1,c2)': str(sp.factor(Bf(c1, c2))),
      'B(c1,a)': str(sp.simplify(Bf(c1, a))), 'B(c2,a)': str(sp.simplify(Bf(c2, a))),
      'B(c1,u1)': str(Bf(c1, u1)), 'B(c2,u2)': str(sp.simplify(Bf(c2, u2))), 'Q(u1)': str(Q(u1)), 'g^2 Q(u2/g) = Q(u2)': str(sp.factor(Q(u2))),
      '4 Q(c1) Q(c2)': str(sp.factor(4*Q(c1)*Q(c2))), 'Delta = 7s^2-46s+64': str(sp.factor(7*s**2 - 46*s + 64)),
      'check 4Q(c1)Q(c2) == Delta': bool(sp.simplify(4*Q(c1)*Q(c2) - (7*s**2 - 46*s + 64)) == 0),
      'det[c1,u1]': str(sp.Matrix.hstack(c1, u1).det()), 'det[c2,u2]/g': str(sp.factor(sp.Matrix.hstack(c2, u2).det())) + '  (divide by g)',
      'c1-split: nu = x c1 + y u1 with x = -(n+a1), y = k + n + a1 + a2; a1 + a2': str(sp.simplify(a[0] + a[1])),
      'shadow c1: ell = B(c1,nu) in (s-2)(Z + s/(2(s-2))), ell^2/(-4Q(c1))': 'ell^2/(2(s-2))',
      'shadow c2: ell = B(c2,nu) in gZ + s/2, ell^2/(-4Q(c2))': 'ell^2/(2(7s-32))',
    }
    return out
if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
    SS = list(range(5, 31)) + [41]
    lines = []
    for k_, v_ in params().items(): lines.append(f"  {k_}: {v_}")
    ok_all = True
    for s in SS:
        hm = H_master(s, N); hc = H_closed(s, N); hz = H_zw(s, N); dl = Delta_lines(s, N)
        ok1 = hm == hc; ok2 = add(hz, dl) == hm
        ok_all &= ok1 and ok2
        lines.append(f"s={s}: closed-form == Master to q^{N}: {ok1};  H = (1/2)q^c0 theta_hol^Zw + Delta_lines: {ok2};  #nonzero coeffs {len(hm)}; first: {sorted(hm.items())[:6]}")
    lines.append(f"ALL PASS: {ok_all}")
    open('H_zwegers.txt', 'w').write("\n".join(lines) + "\n"); print("\n".join(lines))
