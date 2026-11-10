# Frozen (chmod a-w + sidecar) before the logged run. MR2 2026-11-09. Erratum to stages 1/2 (8ca7b93a, 7491cdb8) per PP eb979fda, fix 8:
# resonant algebra RA-5 general holomorphic-section check (exact sympy). Additive; no network.
import sympy as sp
u,v,k=sp.symbols('u v k',real=True); g=sp.Function('g'); G=sp.symbols('G0:3')
Dk=lambda F: -v**2*(sp.diff(F,u,2)+sp.diff(F,v,2))+sp.I*k*v*sp.diff(F,u)
Lk=lambda F: sp.I*v*sp.diff(F,u)-v*sp.diff(F,v)+k*F/2
def ev(e,arg):
    # sympy applies the chain rule itself: d g(arg) -> Subs(Derivative(g(xi), (xi, n)), xi, arg); replace by independent symbols G_n
    reps={s: G[sum(c for _,c in s.expr.variable_count)] for s in e.atoms(sp.Subs)}
    return sp.simplify(sp.expand(e.subs(reps).subs(g(arg),G[0])))
zh=u+sp.I*v; za=u-sp.I*v
Fh=v**(k/2)*g(zh); Fa=v**(k/2)*g(za)
print(f"[RA-5g] exact: F = v^(k/2) g(u+iv), g holomorphic (G0, G1, G2 = g, g', g''): Delta_k F - (k/2)(1-k/2) F = {ev(Dk(Fh)-(k/2)*(1-k/2)*Fh,zh)};  L_k F = {ev(Lk(Fh),zh)}")
print(f"[RA-5g] control, anti-holomorphic g(u-iv): Delta_k F - (k/2)(1-k/2) F = {ev(Dk(Fa)-(k/2)*(1-k/2)*Fa,za)};  L_k F = {ev(Lk(Fa),za)}  (nonzero expected)")
