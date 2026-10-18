# Symbolic facts used in item 3a/3b: R^T A R = A, det R = -1, R e1 = e1, R gamma R = gamma^{-1}, R a + a in Z^2, gamma a - a in Z^2.
import sympy as sp
s = sp.symbols('s', integer=True)
A = sp.Matrix([[2, s], [s, s]]); R = sp.Matrix([[1, s], [0, -1]]); G = sp.Matrix([[-1, -s], [2, 2*s-1]])
a = sp.Matrix([s/(2*(s-2)), -1/(s-2)])
print('R^T A R - A =', sp.simplify(R.T*A*R - A).tolist(), ' det R =', R.det(), ' R e1 =', (R*sp.Matrix([1, 0])).T.tolist())
print('R G R - G^-1 =', sp.simplify(R*G*R - G.inv()).tolist())
print('R a + a =', sp.simplify(R*a + a).T.tolist(), '  G a - a =', sp.simplify(G*a - a).T.tolist())
