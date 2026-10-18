# Cat A symbolic check: N = gamma - (s-1)I satisfies N*A^{-1} = [[0,-1],[1,0]] (so gamma = s-1 on L'/Z^2), N^2 = s(s-2)I, gamma in SO(A).
import sympy as sp
s = sp.symbols('s'); A = sp.Matrix([[2, s], [s, s]]); g = sp.Matrix([[-1, -s], [2, 2*s-1]]); N = g - (s-1)*sp.eye(2)
print('N A^-1 =', sp.simplify(N*A.inv())); print('N^2 =', sp.simplify(N*N)); print('g^T A g - A =', sp.simplify(g.T*A*g - A))
m = sp.symbols('m', positive=True); h = (g + sp.eye(2))/(2*m)
print('s=2m^2: h^2 - gamma =', sp.simplify((h*h - g).subs(s, 2*m**2)), '; h^T A h - A =', sp.simplify((h.T*A*h - A).subs(s, 2*m**2)))
