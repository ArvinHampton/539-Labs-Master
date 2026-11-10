# FROZEN before run (MR2, 2026-11-10). Exact replacements for [S] (numpy allclose) and
# [W2] (simplify == 0) in c2p_ESpm_vertical_spin_delta_2026-11-10_1015.py, per PP 731cef3c
# fix 4. No floats, no simplify==0. Also [R]: exact real-root / sign count, cited only
# as a Gross-Harris 2^{g+k-1} cross-check (fix 6, citation only; no grade).
import sympy as sp
from sympy.physics.quantum import TensorProduct as TP

I = sp.I

# --- [S] Cl(4) exact: lift of diag(1,1,-1,-1) is +/- e3 e4; square = -1; preserves chirality
s0 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.diag(1, -1)
e = [TP(sx, s0), TP(sy, s0), TP(sz, sx), TP(sz, sy)]
ok = all((e[a]*e[b] + e[b]*e[a] - (2 if a == b else 0)*sp.eye(4)).is_zero_matrix
         for a in range(4) for b in range(4))
L = e[2]*e[3]
ch = e[0]*e[1]*e[2]*e[3]
conj = [(L*e[k]*L.inv() - (1 if k < 2 else -1)*e[k]).is_zero_matrix for k in range(4)]
print("[S] Clifford exact:", ok,
      "; (e3 e4)^2 + 1 = 0:", (L*L + sp.eye(4)).is_zero_matrix,
      "; commutes with chirality:", (L*ch - ch*L).is_zero_matrix,
      "; Ad(e3 e4) fixes e1,e2 and negates e3,e4:", conj)

# --- [W2] A = dx/y; F_xy = dAy/dx - dAx/dy is exactly y^{-2}; GB area exactly 4*pi
x = sp.symbols('x', real=True)
y = sp.symbols('y', positive=True)
Ax, Ay = 1/y, 0
F_xy = sp.diff(Ay, x) - sp.diff(Ax, y)
w2_diff = sp.expand(F_xy - y**(-2))
area = (8-2)*sp.pi - 8*(sp.pi/4)
print("[W2] F_xy - y^{-2} (exact expand):", w2_diff,
      "; expand is the zero integer:", w2_diff == 0,
      "; GB area (8-2)pi - 8(pi/4) - 4pi:", sp.expand(area - 4*sp.pi),
      "; |deg L| = area/(2pi):", sp.simplify(area/(2*sp.pi)))

# --- [R] citation-only Gross-Harris cross-check: k = 2 real ovals for c, 2^{g+k-1} = 8
t = sp.symbols('t')
f5 = t**5 - t
rr = sp.real_roots(sp.Poly(f5))
sturm = sp.Poly(f5).count_roots(-10**6, 10**6)
pos = [sp.sign(f5.subs(t, m)) for m in (sp.Rational(-3, 2), sp.Rational(-1, 2), sp.Rational(1, 2), 2)]
print("[R] real branch roots (exact):", rr, "; Sturm count on a large interval:", sturm)
print("[R] sign of x^5-x on (-inf,-1),(-1,0),(0,1),(1,inf):", pos,
      "; ovals k=2 for c (y real: positive intervals (-1,0) and (1,inf)); 2**(g+k-1) =", 2**(2+2-1),
      " (citation only; Gross-Harris; no grade)")
