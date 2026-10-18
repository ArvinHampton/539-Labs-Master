"""(d) Independent quick check of the zeta rational-curve theorem and Theorem G_s (own sympy code, no reuse)."""
import sympy as sp, mpmath as mp, math, itertools
out=[]
def pr(*s): print(*s); out.append(" ".join(map(str,s)))
s,n,k,u,v,x,y,Aa,t=sp.symbols('s n k u v x y A t')
# Step 0
a1=s/(2*(s-2)); a2=-1/(s-2); c0=s/(4*(s-2))
Q2=lambda X,Y: X**2+s*X*Y+s*Y**2/2
Qs=n**2+s*n*k+s*k*(k+1)/2
pr("Q_s - Q2(nu) - c0 == 0:", sp.simplify(Qs-Q2(n+a1,k+a2)-c0)==0)
g=sp.Matrix([[-1,-s],[2,2*s-1]])
X,Y=sp.symbols('X Y'); vv=sp.Matrix([X,Y]); gv=g*vv
pr("gamma preserves Q2:", sp.expand(Q2(gv[0],gv[1])-Q2(X,Y))==0, "; det =",sp.simplify(g.det()), "; gamma a - a =", list(sp.simplify(g*sp.Matrix([a1,a2])-sp.Matrix([a1,a2]))))
S_,T_=sp.symbols('S T'); r1=sp.Matrix([1,0]); r2=g*r1; nu=S_*r1+T_*r2
pr("Q2 in (S,T) basis:", sp.factor(sp.expand(Q2(nu[0],nu[1]))), " (expect S^2+2(s-1)ST+T^2)")
pr("involution phi(n,k)=(n,-2n-k-1) preserves Q_s:", sp.expand(Qs.subs(k,-2*n-k-1)-Qs)==0)
# Lemma E brute force
bad=0
for sv in range(3,31):
    d=sp.Rational(1,2*(sv-2))
    for nn in range(-40,41):
        for kk in range(-80,81):
            inR = nn>=0 and kk>=1; inMm = nn<=-1 and kk<=0
            Sval=nn+sp.Rational(kk,2)+sp.Rational(1,2)+d; Tval=sp.Rational(kk,2)-d
            inC = Sval>0 and Tval>=0
            # C must equal R union phi(Mm)
            kp=-2*nn-kk-1; inPhiMm = nn<=-1 and kp<=0
            if inC != (inR or inPhiMm): bad+=1
pr("Lemma E region check s=3..30, |n|<=40,|k|<=80: mismatches =",bad)
# iterated Euler-Maclaurin coefficients, own implementation
F=sp.exp(-(u**2+2*Aa*u*v+v**2))
def Dop(p,q):
    G=F
    G = sp.integrate(G,(u,0,sp.oo)) if p==0 else sp.diff(G,u,p-1).subs(u,0)
    G = sp.integrate(G,(v,0,sp.oo)) if q==0 else sp.diff(G,v,q-1).subs(v,0)
    return sp.simplify(G)
def cp(p,z): return 1 if p==0 else -sp.bernoulli(p,z)/sp.factorial(p)
def coeff(order):   # coefficient of eps^(order-2), order = p+q
    return sp.expand(sum(cp(p,x)*cp(order-p,y)*Dop(p,order-p) for p in range(0,order+1) if not (p==0 and order-p==0)))
c_t0=sp.simplify(coeff(2)); pr("per-class t^0 coefficient:", sp.factor(c_t0), " vs B1B1+(A/2)(B2+B2):", sp.simplify(c_t0-(sp.bernoulli(1,x)*sp.bernoulli(1,y)+Aa/2*(sp.bernoulli(2,x)+sp.bernoulli(2,y))))==0)
c_t1=sp.simplify(coeff(4))
d=1/(2*(s-2)); cls=[(sp.Rational(1,2)+d,1-d),(d,sp.Rational(1,2)-d)]
z0=sp.factor(sp.simplify(sum(c_t0.subs({x:X0,y:Y0}) for X0,Y0 in cls).subs(Aa,s-1)))
z1=sp.factor(sp.simplify(-sum(c_t1.subs({x:X0,y:Y0}) for X0,Y0 in cls).subs(Aa,s-1)))
pr("zeta_E(0;s) =",z0, "; matches (s-4)(s-5)/(12(s-2)):", sp.simplify(z0-(s-4)*(s-5)/(12*(s-2)))==0)
pr("zeta_E(-1;s) =",z1, "; matches quintic/1440(s-2)^2:", sp.simplify(z1-(2*s**5-14*s**4-45*s**3+425*s**2-632*s-96)/(1440*(s-2)**2))==0)
for o in (1,3):
    c=sp.simplify(sum(coeff(o).subs({x:X0,y:Y0}) for X0,Y0 in cls).subs(Aa,s-1))
    pr(f"sum of t^{(o-2)}/2 coefficients over the two classes:", sp.simplify(c))
area=sp.integrate(1/(u**2+2*(s-1)*u+1),(u,0,sp.oo),conds='none')
pr("area term numeric at s=7 vs arccosh(6)/sqrt(35):", sp.N(area.subs(s,7)), sp.N(sp.acosh(6)/sp.sqrt(35)))
pr("values s=7,8,11:", [ (z0.subs(s,sv), z1.subs(s,sv)) for sv in (7,8,11)])
# ---- Theorem G_s: own expansion ----
K=4
lam=sp.series(sp.log(2/(1+sp.exp(-x))),x,0,2*K+2).removeO()
j=sp.symbols('j',integer=True,positive=True)
expo=-t*n**2+sum(lam.coeff(x,m)*(s*t)**m*sp.summation(j**m,(j,1,n)) for m in range(1,2*K+2))
ser=sp.series(sp.exp(expo),t,0,K+1).removeO()
Am=[2]
for m in range(1,4*K+4): Am.append(sum(sp.binomial(m,i)*Am[i] for i in range(m)))
cks=[]
for kk in range(K+1):
    poly=sp.Poly(sp.expand(ser.coeff(t,kk)),n)
    cks.append(sp.expand(sum(cf*Am[deg[0]] for deg,cf in zip(poly.monoms(),poly.coeffs()))))
pr("G_s c_k(s), k=0..4:", cks)
claimed=[2,2*(s-3),5*s**2-44*s+75,(55*s**3-930*s**2+3918*s-4683)/3,(1073*s**4-28864*s**3+214620*s**2-593128*s+545835)/12]
pr("match the paper:", [sp.simplify(a-b)==0 for a,b in zip(cks,claimed)])
mp.mp.dps=40
def gs(sv,tv):
    q=mp.e**(-tv); tot=mp.mpf(0); prod=mp.mpf(1); nn=0
    while True:
        term=q**(nn*nn)/prod; tot+=term
        nn+=1; prod*=(1+q**(sv*nn))
        if term<mp.mpf(10)**-45 and nn>10: break
    return tot
for sv in (3, mp.mpf('7.5')):
    for tv in (mp.mpf('0.002'),mp.mpf('0.001')):
        approx=sum(sp.N(c.subs(s,float(sv)),30)*float(tv)**i for i,c in enumerate(cks))
        pr(f"s={sv} t={tv}: g_s={mp.nstr(gs(sv,tv),20)}  sum_k<=4 c_k t^k={sp.N(approx,20)}  diff={mp.nstr(gs(sv,tv)-mp.mpf(str(approx)),3)} (expect O(t^5))")
open("zeta_gs_check.txt","w").write("\n".join(out)+"\n")
