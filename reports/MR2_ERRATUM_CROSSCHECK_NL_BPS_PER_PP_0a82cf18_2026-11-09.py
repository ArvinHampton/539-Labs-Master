#!/usr/bin/env python3
# MR2 2026-11-09 erratum checks per PP 0a82cf18: (Z1) w-sector at MN2 from CGR (5.16)+(5.15), exact sympy;
# (B3) phi-independence of T and Delta at fixed (lam, w); (D5) Sigma-row Clifford identity Gamma^{cde}G_{S1 cde} = 6 Gamma^{S2} omega-slash (sign +sigma/2).
import sympy as sp, itertools, random
def P(*s): print(*s, flush=True)
ph, la, w = sp.symbols('phi lambda w', real=True); g = sp.symbols('g', positive=True); l = -1
S_, O_, vp = sp.exp(-(ph+3*la)), sp.exp(3*ph-la-w), la-3*ph-w/2           # CGR (5.15)
V = -g**2*O_**-2*S_**-2*(2*l*sp.exp(2*vp)*O_*S_**3 - sp.Rational(1,2)*sp.exp(4*vp)*l**2 - sp.Rational(1,2)*sp.exp(4*vp)*O_**4
                         + 4*O_*S_**3 + 2*sp.exp(2*vp)*O_**2 + 2*sp.exp(2*vp)*O_**3*S_**3)   # (5.16) at z = 0, V = -Lpot
W3 = g/(2*O_*S_)*(O_**2*sp.exp(2*vp) + 2*O_*S_**3 + l*sp.exp(2*vp) + 2)
X = [ph, la, w]; G = sp.diag(60, 60, 3)
sub = {ph: sp.log(2)/30, la: sp.log(2)/10, w: 0}
P("[Z1] grad V at MN2:", [sp.simplify(sp.diff(V, z).subs(sub)) for z in X])
Lsq = sp.simplify((3/W3.subs(sub))**2); P("[Z1] g^2 L^2 =", sp.simplify(g**2*Lsq), "; V* + 12/L^2 =", sp.simplify(V.subs(sub) + 12/Lsq))
H = sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.diff(V, X[i], X[j]).subs(sub)))
P("[Z1] Hess V mixing entries (phi,w), (lam,w):", H[0,2], H[1,2])
M = (G.inv()*H*Lsq).applyfunc(sp.simplify)
P("[Z1] m^2 L^2 = eig(G^-1 Hess V) L^2:", {sp.nsimplify(k): v for k, v in M.eigenvals().items()}, "; w-entry:", M[2,2])
mu = sp.symbols('mu')
P("[Z1] w second-order exponents mu L from mu^2 - 4 mu - m^2 L^2 = 0 with m^2 = 0:", sp.solve(mu**2 - 4*mu - M[2,2], mu))
HW = sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.diff(W3, X[i], X[j]).subs(sub)))
E = (2*G.inv()*HW*sp.sqrt(Lsq)).applyfunc(sp.simplify)
P("[Z1] W3-flow exponents x L (2 G^-1 Hess W3 L):", {sp.nsimplify(k): v for k, v in E.eigenvals().items()}, "; w-entry:", E[2,2])
P("[Z1] d^3V/dw^3 at MN2:", sp.simplify(sp.diff(V, w, 3).subs(sub)), "; equals -24*2^(2/3) g^2:", sp.simplify(sp.diff(V, w, 3).subs(sub) + 24*2**sp.Rational(2,3)*g**2) == 0)
# B3: T and Delta phi-independent
a1, a2, b1, b2, b3 = sp.symbols('m1:6', real=True)
T = sp.diag(sp.exp(-6*la), sp.exp(-6*la), sp.exp(4*la+w), sp.exp(4*la+w), sp.exp(4*la-2*w))
mvec = sp.Matrix([a1, a2, b1, b2, b3]); Delta = (mvec.T*T*mvec)[0]
P("[B3] det T =", sp.simplify(T.det()), "; d Delta/d phi =", sp.diff(Delta, ph), "; d T/d phi zero:", T.diff(ph).is_zero_matrix,
  "; d Delta/d w =", sp.simplify(sp.diff(Delta, w)), "(nonzero: w enters the x/Sigma warps via Delta^(1/3))")
# D5 sign: Sigma rows. Clifford as in the main script; Sigma = indices 4,5; fibre/internal others 6..9
s0 = sp.eye(2); sx = sp.Matrix([[0,1],[1,0]]); sy = sp.Matrix([[0,-sp.I],[sp.I,0]]); sz = sp.Matrix([[1,0],[0,-1]])
def kron(*ms):
    out = ms[0]
    for m_ in ms[1:]: out = sp.kronecker_product(out, m_)
    return out
Eg = []
for k in range(5):
    Eg.append(kron(*([sz]*k + [sx] + [s0]*(4-k)))); Eg.append(kron(*([sz]*k + [sy] + [s0]*(4-k))))
Eg.append(kron(*[sz]*5)); Gam = [sp.I*Eg[0]] + Eg[1:]
def prod(idx):
    out = sp.eye(32)
    for i in idx: out = out*Gam[i]
    return out
random.seed(3); pairs = list(itertools.combinations(range(6, 10), 2))
for trial in range(3):
    om = {p: random.randint(-4, 4) for p in pairs}
    # G_{4 5 i j} = om_ij; Gamma^{cde} G_{4 cde} summed over all c,d,e = 3! * sum_{(5,i,j) sorted} G_{4 5 i j} Gamma^{5 i j}
    lhs = sp.zeros(32)
    for (i, j), v in om.items(): lhs += 6*v*prod((5, i, j))
    omsl = sp.zeros(32)
    for (i, j), v in om.items(): omsl += v*prod((i, j))
    rhs = 6*Gam[5]*omsl
    P(f"[D5] trial {trial}: Gamma^cde G_(S1 cde) - 6 Gamma^S2 omega-slash = 0: {all(sp.expand(x) == 0 for x in (lhs - rhs))}")
P("[D5] => S1-row with x-row substituted: (k_S - k_x) Gamma_S1 eps = (sigma/12)(6 Gamma^S2 omslash) eps; left-multiply by Gamma^S1: (k_S - k_x) eps = +(sigma/2) Gamma^{S1 S2} omslash eps")
