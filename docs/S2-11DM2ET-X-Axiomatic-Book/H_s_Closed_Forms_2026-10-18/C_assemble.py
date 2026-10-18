# Path B: assemble C = P_s - H_s radial coefficients at x=0 for s>=5, using P_s (2026-10-18-g_s-Closed-Forms/prove_P_Theta) and H_s (H_closed).
import pickle, sympy as sp, math, mpmath as mp
from H_em import al, be2, ga, b, mu
Hd = pickle.load(open('H_closed.pkl', 'rb')); H = Hd['H']
Pd = pickle.load(open('../../2026-10-18-g_s-Closed-Forms/PTh_coeffs.pkl', 'rb'))
sP = [x for x in Pd['P'][-1].free_symbols if x.name == 's'][0]
s, g = sp.symbols('s g', positive=True)
P = {k: v.subs(sP, s) for k, v in Pd['P'].items()}; E = {k: v.subs(sP, s) for k, v in Pd['E'].items()}
C = {k: sp.simplify(P[k] - H[k]) for k in P}
names = {-2: 't^-1', -1: 't^-1/2', 0: 't^0', 1: 't^1/2', 2: 't^1'}
out = ["C = P_s - H_s, radial coefficients at x=0 (s>=5):"]
for k in C: out.append(f"  {names[k]}: {sp.simplify(sp.radsimp(C[k]))}")
out.append("Structural identities:")
for k, nm in ((-2, 'C t^-1 = Res/2 = P t^-1'), (0, 'C t^0 = (1+E_0)/2 = P t^0'), (2, 'C t^1 = E_1/2 = P t^1')):
    rhs = (E[k] + (1 if k == 0 else 0))/2
    ok = sp.simplify(C[k] - rhs) == 0; out.append(f"  [{'PASS' if ok else 'FAIL'}] {nm}")
# angular integrals: closed forms vs mpmath quadrature (independent route)
bad = 0
for sv in [5, 6, 7, 8, 9, 10, 11, 12, 13, 19, 20, 25, 30, 41, 97, 150]:
    gv = math.gcd(24, sv-8); sub = {s: sv, g: gv}
    for j, A in ((1, Hd['A1']), (3, Hd['A3'])):
        f = sp.lambdify(mu, ((1+b*mu)**j/(al+be2*mu+ga*mu**2)**(1+sp.Rational(j, 2))).subs(sub), 'mpmath')
        mp.mp.dps = 30; num = mp.quad(f, [0, 1, 10, mp.inf]); ex = sp.N(A.subs(sub), 30)
        bad += abs(num - ex) > 1e-20
out.append(f"[{'PASS' if bad == 0 else 'FAIL'}] angular integrals ANG1, ANG3: closed form vs 30-digit quadrature at 16 values of s: mismatches {bad}")
out.append("\nTable (numerical values of the closed forms):")
out.append(" s  g | H t^-1/2      H t^1/2     | C t^-1        C t^-1/2      C t^0         C t^1/2       C t^1")
for sv in list(range(5, 21)) + [25, 30, 41]:
    gv = math.gcd(24, sv-8); sub = {s: sv, g: gv}
    row = [float(H[-1].subs(sub)), float(H[1].subs(sub))] + [float(C[k].subs(sub)) for k in (-2, -1, 0, 1, 2)]
    out.append(f"{sv:2d} {gv:2d} | " + "  ".join(f"{x:+.9f}" for x in row))
pickle.dump({'C': C, 'H': H}, open('C_closed.pkl', 'wb'))
open('C_assemble.txt', 'w').write("\n".join(out) + "\n"); print("\n".join(out))
