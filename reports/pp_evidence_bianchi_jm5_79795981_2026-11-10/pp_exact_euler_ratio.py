# PP exact: Euler (Gauss-Bonnet) density of the MN2 squashed fibre S^4 vs rho_J, cohomogeneity-one reduction.
# DISCOVERY ONLY (uses sp.simplify to find the closed form). Grounds for PP grades are pp_exact_gb_verify.py (sp.cancel on rational functions).
# Fibre metric (V2 lines 236-243): g_fib = (1/4) D^(-2/3) h, h = sum_k X_k^-1 (dmu_k^2 + mu_k^2 dphi_k^2), X0=X2=p, X1=p/2 (C1).
# Coordinates: y=(mu0, mu2 e^{i phi2}) = cos(th) n, n in S^2 (psi,chi); z = mu1 e^{i phi1} = sin(th) e^{i phi}; s = mu1^2 = sin^2 th.
import sympy as sp
th,ps,ch,ph=sp.symbols('theta psi chi phi',real=True); p=sp.symbols('p',positive=True)
X=[th,ps,ch,ph]; C=sp.cos(th)**2
D=p/2*(1+C); F=D**sp.Rational(-2,3)/4
g=sp.diag(F*(1+C)/p, F*sp.cos(th)**2/p, F*sp.cos(th)**2*sp.sin(ps)**2/p, F*2*sp.sin(th)**2/p)
n=4; gi=g.inv()
Gam=[[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
def Rup(a,b,c,d):  # R^a_{bcd}
    return sp.diff(Gam[a][d][b],X[c])-sp.diff(Gam[a][c][b],X[d])+sum(Gam[a][c][e]*Gam[e][d][b]-Gam[a][d][e]*Gam[e][c][b] for e in range(n))
R={}
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                R[(a,b,c,d)]=sp.simplify(Rup(a,b,c,d))
# diagonal metric: lower and contract
Rl={k: g[k[0],k[0]]*v for k,v in R.items()}
Rm2=sp.simplify(sum(v**2/(g[a,a]*g[b,b]*g[c,c]*g[d,d]) for (a,b,c,d),v in Rl.items()))
Ric=sp.Matrix(n,n,lambda b,d: sum(R[(a,b,a,d)] for a in range(n)))
Ric=Ric.applyfunc(sp.simplify)
Ric2=sp.simplify(sum(Ric[a,b]**2/(g[a,a]*g[b,b]) for a in range(n) for b in range(n)))
Rs=sp.simplify(sum(Ric[a,a]/g[a,a] for a in range(n)))
GB=sp.simplify(Rm2-4*Ric2+Rs**2)   # E = GB/(32 pi^2) per unit volume
cc=sp.symbols('c',positive=True)
GBc=sp.simplify(GB.subs(sp.sin(th)**2,1-sp.cos(th)**2).subs(sp.cos(th),sp.sqrt(cc)))
print("GB(c) =",sp.factor(GBc))
U=-p**2*(3+cc); Dc=p/2*(1+cc)
# ratio per unit j:  Rj = (E/2)/rho_vol,  rho_vol = 9760 |U| D^(-7/6)/pi^2  (|int G4_fib| = pi^2 exactly, C6)
Rj=sp.simplify(GBc/(64*9760*(-U))*Dc**sp.Rational(7,6))
print("Rj(c) =",sp.factor(Rj))
print("Rj(0) =",sp.nsimplify(sp.simplify(Rj.subs(cc,0))), " =", sp.N(Rj.subs(cc,0),20), " 1/Rj(0) =", sp.N(1/Rj.subs(cc,0),20))
print("Rj(1) =",sp.simplify(Rj.subs(cc,1)), " =", sp.N(Rj.subs(cc,1),20))
import pickle; pass
