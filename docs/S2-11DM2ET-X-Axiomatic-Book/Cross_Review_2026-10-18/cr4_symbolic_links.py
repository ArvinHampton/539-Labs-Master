# Cross-review check 4: symbolic / exact links between quantities in different reports (sympy, exact).
import sympy as sp, math
from math import gcd, isqrt
s = sp.symbols('s', positive=True)
L = []
def chk(name, cond): L.append(f"[{'PASS' if cond else 'FAIL'}] {name}")
M = sp.Matrix([[2, s], [s, s]]); B = lambda x, y: (x.T*M*y)[0]; Q = lambda x: B(x, x)/2
a = sp.Matrix([s/(2*(s-2)), -1/(s-2)]); c0 = s/(4*(s-2))
g = sp.Matrix([[-1, -s], [2, 2*s-1]]); R = sp.Matrix([[1, s], [0, -1]]); Lphi = sp.Matrix([[1, 0], [-2, -1]])
chk("a1+a2 = 1/2 (H_s report) for all s", sp.simplify(a[0]+a[1]-sp.Rational(1, 2)) == 0)
chk("gamma, R_s, phi preserve M", all(sp.simplify(X.T*M*X - M) == sp.zeros(2) for X in (g, R, Lphi)))
chk("R_s a = -a (Lemma R, C_third-Unified)", sp.simplify(R*a + a) == sp.zeros(2, 1))
chk("phi linear part (zeta-curve Lemma E, phi(n,k)=(n,-2n-k-1)) satisfies phi*a - a = (0,-1) in Z^2", sp.simplify(Lphi*a - a) == sp.Matrix([0, -1]))
chk("phi = -gamma*R_s  (so Lemma E's reflection, Lemma R's R_s and V42's R are one improper class)", sp.simplify(Lphi + g*R) == sp.zeros(2))
chk("R_s^2 = I", sp.simplify(R*R) == sp.eye(2))
# phi in v-coordinates equals (n,-2n-k-1):
n, k = sp.symbols('n k')
v = sp.Matrix([n, k]); img = Lphi*(v + a) - a
chk("phi(v) = (n, -2n-k-1)", sp.simplify(img - sp.Matrix([n, -2*n-k-1])) == sp.zeros(2, 1))
c1 = sp.Matrix([-1, 1]); c2 = sp.Matrix([-4, 1])
chk("Q(c1) = -(s-2)/2, Q(c2) = -(7s-32)/2, B(c1,c2) = -4(s-2)", sp.simplify(Q(c1)+(s-2)/2) == 0 and sp.simplify(Q(c2)+(7*s-32)/2) == 0 and sp.simplify(B(c1, c2)+4*(s-2)) == 0)
chk("B(c1,c2) = 8 Q(c1)", sp.simplify(B(c1, c2) - 8*Q(c1)) == 0)
chk("B(c1,c2)^2 - 4Q(c1)Q(c2) = 9 s(s-2) = -9 det M  (Gram det of <c1,c2> = 9 det M; index 3)", sp.expand(B(c1, c2)**2 - 4*Q(c1)*Q(c2) - 9*s*(s-2)) == 0 and abs(sp.Matrix.hstack(c1, c2).det()) == 3)
chk("Delta := 4Q(c1)Q(c2) = (s-2)(7s-32) = 16(s-2)^2 - 9s(s-2)", sp.expand(4*Q(c1)*Q(c2) - (s-2)*(7*s-32)) == 0 and sp.expand((s-2)*(7*s-32) - 16*(s-2)**2 + 9*s*(s-2)) == 0)
Rc1 = R*c1
chk("R_s c1 = (s-1,-1); R_s c1 = -c2 exactly when s = 5 (explains H_5 = 0 and Q(c1)=Q(c2) at s=5)", sp.solve(sp.Eq(Rc1[0], 4), s) == [5] and sp.simplify(Rc1.subs(s, 5) + c2) == sp.zeros(2, 1))
chk("B(c1, nu) depends only on nu1: B(c1,(x,y)) = (s-2)x", sp.simplify(B(c1, sp.Matrix([n, k])) - (s-2)*n) == 0)
# gcd identities (integer s)
chk("gcd(7s-32, s-8) = gcd(24, s-8) = g for s=5..2000 (so g | 7s-32 always)", all(gcd(7*t-32, t-8) == gcd(24, t-8) for t in range(5, 2001)))
chk("gcd(7s-32, s-2) = gcd(18, s-2) and gcd(7s-32, s) = gcd(32, s) for s=5..2000", all(gcd(7*t-32, t-2) == gcd(18, t-2) and gcd(7*t-32, t) == gcd(32, t) for t in range(5, 2001)))
# factor-20: denominator of c0
den = {t: sp.Rational(t, 4*(t-2)).q for t in (7, 8, 11)}
chk(f"denominator of c0 = 4(s-2)/gcd(s,8): {den} equals the reported N(a)/Q2 = 20, 3, 36", den == {7: 20, 8: 3, 11: 36} and all(den[t] == 4*(t-2)//gcd(t, 8) for t in den))
chk("for odd s the factor c_s = 4(s-2) = -B(c1,c2); for s=8 they differ (3 vs 24)", all(4*(t-2)//gcd(t, 8) == 4*(t-2) for t in range(5, 200, 2)))
# residue / unit
x = s - 1
chk("arccosh(s-1) = log(eps_s), eps_s = (s-1)+sqrt(s(s-2)), N(eps_s)=1", sp.simplify((x + sp.sqrt(x**2-1))*(x - sp.sqrt(x**2-1)) - 1) == 0 and sp.expand(x**2 - 1 - s*(s-2)) == 0)
def pell_min(D):
    y = 1
    while True:
        xx = isqrt(D*y*y+1)
        if xx*xx == D*y*y+1: return xx, y
        y += 1
chk("(s-1,1) is the fundamental solution of x^2 - s(s-2)y^2 = 1 (trivially y=1) for s=3..300", all(pell_min(t*(t-2)) == (t-1, 1) for t in range(3, 301)))
chk("even s=2t: fundamental solution of x^2 - t(t-1)y^2 = 1 is (2t-1, 2) for t=3..150 (eps_gamma fundamental in the order of disc s(s-2))", all(pell_min(t*(t-1)) == (2*t-1, 2) for t in range(3, 151)))
# Delta perfect squares, and Q(sqrt Delta) vs Q(sqrt s(s-2))
sq = [t for t in range(5, 10**6) if isqrt((t-2)*(7*t-32))**2 == (t-2)*(7*t-32)]
same_field = [t for t in range(5, 10**6) if isqrt(t*(t-2)**2*(7*t-32))**2 == t*(t-2)**2*(7*t-32)]
L.append(f"[INFO] s in [5,1e6) with Delta=(s-2)(7s-32) a perfect square: {sq[:12]} (count {len(sq)})")
L.append(f"[INFO] s in [5,1e6) with Q(sqrt Delta) = Q(sqrt(s(s-2))) [s(7s-32)·square]: {same_field[:12]} (count {len(same_field)})")
L.append(f"[INFO] 7s-32 = 0 at s = 32/7 (non-integer); s=4: Q(c2)=+2>0 (non-admissible); s=5: 7s-32 = s-2 = 3 (degenerate, H_5=0)")
L.append(f"[INFO] zeta_E(0;s)=(s-4)(s-5)/(12(s-2)) vanishes at s=4,5 = the two integers bracketing 32/7; no mechanism found linking E_s (no c2) to H_s (Cat B coincidence)")
# C_{-1/2}(7)
t7 = 7
P12 = sp.sqrt(sp.pi)*(s**2 - 2*sp.sqrt(2*s))/(4*s*(s-2))
H12 = sp.Rational(1, 2)*sp.sqrt(2*sp.pi*s)*(1/sp.sqrt((s-2)*(7*s-32)) - 1/(s-2))
aC = sp.sqrt(sp.pi)*(833 + 204*sp.sqrt(14) - 14*sp.sqrt(1190))/2380
aH = sp.sqrt(sp.pi)*(sp.sqrt(1190) - 17*sp.sqrt(14))/170
val = sp.N((P12 - H12).subs(s, 7), 30)
chk(f"C_-1/2(7) = P_-1/2 - H_-1/2 = {val} equals rev3 a_C closed form (now proved symbolically, not only PSLQ)", sp.simplify(sp.radsimp((P12-H12).subs(s, 7) - aC)) == 0)
chk("H_-1/2(7) equals rev3 a_H = sqrt(pi)(sqrt1190-17sqrt14)/170", sp.simplify(sp.radsimp(H12.subs(s, 7) - aH)) == 0)
# h_C(0) of C_third vs P_s and Theta_hol columns of g_s report
Th12 = sp.sqrt(sp.pi)*(s**2/2 - 2*s + sp.sqrt(2*s))/(s*(s-2))
hC = (P12 + Th12 - sp.sqrt(sp.pi)).subs(s, 7)
chk("C_third t^-1/2 at x=0 from g_s table (P+Theta-theta3) = -sqrt(pi)(49-2sqrt14)/140 (C_third-Modularity)", sp.simplify(hC + sp.sqrt(sp.pi)*(49 - 2*sp.sqrt(14))/140) == 0)
# dims
chk("odd s: dim Fix(P) = 2(n+1) = 2(s-1)^2 with n = s(s-2)", sp.expand(2*(s*(s-2)+1) - 2*(s-1)**2) == 0)
print("\n".join(L)); open('cr4_symbolic_links.txt', 'w').write("\n".join(L) + "\n")
