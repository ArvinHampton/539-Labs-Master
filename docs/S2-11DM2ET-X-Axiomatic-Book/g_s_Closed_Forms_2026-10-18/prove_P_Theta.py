# Step (4)/(5) support: symbolic 2-D Euler-Maclaurin (cited F1, as in the zeta-curve proof) for the quadrant sum R(q)=sum_{n>=0,k>=1} q^{Q_s},
# general s>=3; then P_s = R + (1+theta3)/2 and Theta_hol = E - 2R through order t^1, using the proved E_s coefficients.
import sympy as sp
s = sp.symbols('s', positive=True); t = sp.symbols('t', positive=True); u, v, x, y, w = sp.symbols('u v x y w', positive=True)
out = []
def check(name, z):
    ok = sp.simplify(z) == 0; out.append(f"[{'PASS' if ok else 'FAIL'}] {name}"); print(out[-1]); return ok
F = sp.exp(-t*(u**2 + s*u*v + s/2*v**2))
edge_u = lambda p: sp.integrate(sp.diff(F, u, p-1).subs(u, 0), (v, 0, sp.oo), conds='none')
edge_v = lambda q: sp.integrate(sp.diff(F, v, q-1).subs(v, 0), (u, 0, sp.oo), conds='none')
corner = lambda p, q: sp.diff(F, u, p-1, v, q-1).subs({u: 0, v: 0})
Pm = 5; B = sp.bernoulli
ex = 0
for p in range(1, Pm+1): ex += -B(p, x)/sp.factorial(p)*edge_u(p)
for q in range(1, Pm+1): ex += -B(q, y)/sp.factorial(q)*edge_v(q)
for p in range(1, Pm+1):
    for q in range(1, Pm+1): ex += B(p, x)*B(q, y)/(sp.factorial(p)*sp.factorial(q))*corner(p, q)
exw = sp.expand(sp.simplify(ex).subs(t, w**2))
coefZ = {j: sp.simplify(exw.coeff(w, j)) for j in (-1, 0, 1, 2)}       # t^{j/2}, j=-1..2 (excluding area t^-1)
X0, Y0 = sp.Rational(1, 2) + 1/(s-2), 1 - 1/(s-2)                      # R offsets: nu=(n+a1, k+a2), n>=0, k>=1
c0 = s/(4*(s-2))
ZR = {j: sp.simplify(coefZ[j].subs({x: X0, y: Y0})) for j in coefZ}
D = s*(s-2); Res = sp.acosh(s-1)/sp.sqrt(D)
ZR[-2] = Res/2                                                        # area term: (1/2) int_0^oo dm/(1+s m+(s/2)m^2) = Res/2 (hand + numeric)
# E (Z-normalised, proved): t^-1 Res, t^-1/2 0, t^0 zeta0, t^1/2 0, t^1 -zeta(-1)
Z0 = (s-4)*(s-5)/(12*(s-2)); Z1 = (2*s**5-14*s**4-45*s**3+425*s**2-632*s-96)/(1440*(s-2)**2)
ZE = {-2: Res, -1: 0, 0: Z0, 1: 0, 2: -Z1}
# convert Z (Q2 sums) -> q^{Q_s} sums: multiply by e^{-t c0} = 1 - c0 t + c0^2 t^2/2
def toq(Z):
    o = {j: 0 for j in (-2, -1, 0, 1, 2)}
    for j, cz in Z.items():
        for m, f in ((0, 1), (2, -c0), (4, c0**2/2)):
            if j + m <= 2: o[j+m] += cz*f
    return {j: sp.simplify(c) for j, c in o.items()}
R = toq(ZR); E = toq(ZE)
P = {j: sp.simplify(R[j] + {-1: sp.sqrt(sp.pi)/2, 0: sp.Rational(1, 2)}.get(j, 0)) for j in R}
Th = {j: sp.simplify(E[j] - 2*R[j]) for j in R}
names = {-2: 't^-1', -1: 't^-1/2', 0: 't^0', 1: 't^1/2', 2: 't^1'}
out.append("\nP_s coefficients (general s>=3):")
for j in P: out.append(f"   {names[j]}: {sp.simplify(sp.radsimp(P[j]))}")
out.append("Theta_hol coefficients:")
for j in Th: out.append(f"   {names[j]}: {sp.simplify(sp.radsimp(Th[j]))}")
out.append("E_s (q^{Q_s}-normalised) coefficients:")
for j in E: out.append(f"   {names[j]}: {sp.factor(E[j])}")
check("P t^-1/2 = sqrt(pi)(s^2 - 2 sqrt(2s))/(4 s (s-2))  [pre-stated guess]", sp.radsimp(P[-1] - sp.sqrt(sp.pi)*(s**2 - 2*sp.sqrt(2*s))/(4*s*(s-2))))
# Parity split (Lemma P) for all s, orders t^-1..t^1: Theta_hol has only half-integer orders
check("Theta_hol t^-1 = 0", Th[-2]); check("Theta_hol t^0 = 0", Th[0]); check("Theta_hol t^1 = 0", Th[2])
check("=> integer orders of P equal those of (1+E)/2: t^0", P[0] - (1 + E[0])/2); check("t^1", P[2] - E[2]/2)
# numeric comparison with earlier per-s report (asym_s.txt, s=7,8,11)
prev = {7: (0.525617204331837, 0.476703062889850, 0.721219442241842), 8: (0.516965706514109, 0.519971166974921, 0.738522437877298), 11: (0.499595517696650, 0.648484272710551, 0.773262815512215)}
for sv, (ph, p0, th) in prev.items():
    d = max(abs(sp.N(P[-1].subs(s, sv)) - ph), abs(sp.N(P[0].subs(s, sv)) - p0), abs(sp.N(Th[-1].subs(s, sv)) - th))
    out.append(f"[{'PASS' if d < 1e-12 else 'FAIL'}] s={sv}: matches 2026-10-18-s8-s11/asym_s.txt (max diff {float(d):.1e})")
import pickle; pickle.dump(dict(P=P, Th=Th, E=E, R=R), open('PTh_coeffs.pkl', 'wb'))
open('prove_P_Theta.txt', 'w').write("\n".join(out) + "\n"); print("\n".join(out[-25:]))
