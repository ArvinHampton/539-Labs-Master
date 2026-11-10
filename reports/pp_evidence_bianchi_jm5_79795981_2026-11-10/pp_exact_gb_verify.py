# PP exact re-verification of the Gauss-Bonnet closed form, rational-function arithmetic only (sp.cancel zero tests).
# Coordinate W > 0 with 1 + cos^2(th) = W^6 (c = cos^2 th = W^6 - 1, W in [1, 2^(1/6)]); p = 2 K^3 (K > 0), so (p/2)^(-2/3) = K^-2.
# Metric (from h, see pp_exact_euler_ratio.py): F = (1/4)(p/2)^(-2/3)(1+c)^(-2/3) = 1/(4 K^2 W^4);
# dth^2 = dc^2/(4c(1-c)), dc = 6 W^5 dW.
import sympy as sp
W,K=sp.symbols('W K',positive=True); ps,ch,ph=sp.symbols('psi chi phi',real=True)
X=[W,ps,ch,ph]; c=W**6-1; p=2*K**3; F=1/(4*K**2*W**4)
gWW=F*(1+c)/p*(6*W**5)**2/(4*c*(1-c))
g=sp.diag(sp.cancel(gWW), F*c/p, F*c*sp.sin(ps)**2/p, F*2*(1-c)/p)
n=4; gi=sp.diag(*[sp.cancel(1/g[i,i]) for i in range(n)])
Gam=[[[sp.cancel(sum(gi[a,d]*(sp.diff(g[d,b],X[c_])+sp.diff(g[d,c_],X[b])-sp.diff(g[b,c_],X[d])) for d in range(n))/2) for c_ in range(n)] for b in range(n)] for a in range(n)]
def Rup(a,b,c_,d): return sp.cancel(sp.diff(Gam[a][d][b],X[c_])-sp.diff(Gam[a][c_][b],X[d])+sum(Gam[a][c_][e]*Gam[e][d][b]-Gam[a][d][e]*Gam[e][c_][b] for e in range(n)))
R={(a,b,c_,d):Rup(a,b,c_,d) for a in range(n) for b in range(n) for c_ in range(n) for d in range(n)}
Rm2=sp.cancel(sum((g[a,a]*v)**2/(g[a,a]*g[b,b]*g[c_,c_]*g[d,d]) for (a,b,c_,d),v in R.items()))
Ric=[[sp.cancel(sum(R[(a,b,a,d)] for a in range(n))) for d in range(n)] for b in range(n)]
Ric2=sp.cancel(sum(Ric[a][b]**2/(g[a,a]*g[b,b]) for a in range(n) for b in range(n)))
Rs=sp.cancel(sum(Ric[a][a]/g[a,a] for a in range(n)))
GB=sp.cancel(Rm2-4*Ric2+Rs**2)
N=lambda c_: 37*c_**3+93*c_**2-25*c_-225
closed=-64*16*K**10*N(c)/(27*W**28)
print("GB free of psi:", sp.diff(GB,ps)==0 or sp.cancel(sp.diff(GB,ps))==0)
print("cancel(GB - closed) == 0:", sp.cancel(sp.expand_trig(GB-closed))==0)
# polynomial certificate: 75(1+c)^3(c+3) - Nn(c) with Nn = -N = 225+25c-93c^2-37c^3 equals 725c+993c^2+487c^3+75c^4
cs=sp.symbols('c'); print("expand(75(1+c)^3(c+3) + N(c) - (725c+993c^2+487c^3+75c^4)) == 0:", sp.expand(75*(1+cs)**3*(cs+3)+N(cs)-(725*cs+993*cs**2+487*cs**3+75*cs**4))==0)
print("N(c) <= 37+93-225 < 0 on [0,1] (term bound): -N(c) >= 225-130 = 95 > 0")
# exact constants with p = 2^(2/5): p^(5/2) = 2
Rj0=sp.sqrt(2)*2*225/(527040*3); print("Rj(0) =",sp.nsimplify(Rj0)," 1/Rj(0) =",sp.radsimp(1/Rj0), "=", sp.N(1/Rj0,20), "| E-S adverse min 1-Rj(0) =", sp.N(1-Rj0,20))
Rj1=sp.sqrt(2)*2*(225+25-93-37)/(527040*2**sp.Rational(7,2)*4); print("Rj(1) =",sp.nsimplify(Rj1), "=", sp.N(Rj1,20))
