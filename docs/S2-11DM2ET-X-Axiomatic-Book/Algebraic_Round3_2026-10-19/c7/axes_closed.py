# Category A: exact small-t expansion of H^axes_s(e^{-t}) = P - Caxis - Cthird (x=0), symbolic in s = 2 w^2 (w = sqrt(s/2)).
# Uses Zagier's 2-D quadrant Euler-Maclaurin lemma (as proved/used in Analytic-CatB-Push asym_engine) for P and Cthird,
# and the exact 1-D expansions of the unary Gaussian sums in Caxis.  eps = sqrt(t); c[e] = coeff of eps^e.
import sympy as sp, json, sys, pickle
w=sp.symbols('w',positive=True); s=2*w**2; lam=s/2; X,Y,mu=sp.symbols('X Y mu',positive=True)
K=int(sys.argv[1]) if len(sys.argv)>1 else 13
spi=sp.sqrt(sp.pi)
def B(r,a): return sp.bernoulli(r,a) if not (r==1) else (sp.Rational(-1,2) if a==0 else sp.Rational(1,2))
def gX(j): return sp.gamma(sp.Rational(j+1,2))/2                      # int_0^oo X^j e^{-X^2}
def gY(j): return sp.gamma(sp.Rational(j+1,2))/(2*(s/2)**sp.Rational(j+1,2))   # int_0^oo Y^j e^{-(s/2)Y^2}
def coefY(m):   # [Y^m] e^{-sXY-(s/2)Y^2}  (poly in X)
    return sp.expand(sum((-s*X)**a*(-s/2)**((m-a)//2)/(sp.factorial(a)*sp.factorial((m-a)//2)) for a in range(m+1) if (m-a)%2==0))
def coefX(n):   # [X^n] e^{-X^2-sXY} (poly in Y)
    return sp.expand(sum((-s*Y)**a*(-1)**((n-a)//2)/(sp.factorial(a)*sp.factorial((n-a)//2)) for a in range(n+1) if (n-a)%2==0))
def intX(poly):  # int_0^oo poly(X) e^{-X^2}
    p=sp.Poly(poly,X); return sum(c*gX(m[0]) for m,c in zip(p.monoms(),p.coeffs()))
def intY(poly):
    p=sp.Poly(poly,Y); return sum(c*gY(m[0]) for m,c in zip(p.monoms(),p.coeffs()))
qmu=1+s*mu+(s/2)*mu**2
def J(i):        # int_0^oo mu^i / q(1,mu)^{(i+2)/2}, i odd: antiderivative R/q^{i/2}
    r=sp.symbols(f'r0:{i+1}'); R=sum(r[j]*mu**j for j in range(i+1))
    eq=sp.Poly(sp.expand(sp.diff(R,mu)*qmu-sp.Rational(i,2)*R*sp.diff(qmu,mu)-mu**i),mu).all_coeffs()
    sol=sp.solve(eq,r,dict=True)[0]
    return sp.simplify(sol[r[i]]/(s/2)**sp.Rational(i,2)-sol[r[0]])
c={e:sp.Integer(0) for e in range(-2,K+1)}
for sign,sig,al in ((1,1,0),(-1,-1,1)):          # +P (alpha=beta=0, +lam k), -Cthird (alpha=beta=1, -lam k)
    for i in range(0,K+3):
        pref=sign*(-sig*lam)**i/sp.factorial(i)      # G_i = pref * Y^i e^{-q}
        if i%2==1 and i-2<=K:
            c[i-2]+=pref*sp.gamma(sp.Rational(i+2,2))/2*J(i)
        for m in range(0,K+2-i):                     # edge along X (Y=0): derivative in Y of Y^i e^{-q}
            e=i+m-1
            if e>K: break
            # d^m/dY^m [Y^i e^{-q}] at Y=0 = m! [Y^{m-i}] e^{-q} (if m>=i)
            if m>=i:
                d=sp.factorial(m)*coefY(m-i)
                c[e]+=-pref*B(m+1,al)/sp.factorial(m+1)*intX(d)
        for n in range(0,K+2-i):                     # edge along Y (X=0): d^n/dX^n [Y^i e^{-q}] at X=0
            e=i+n-1
            if e>K: break
            d=sp.factorial(n)*sp.expand(Y**i*coefX(n))
            c[e]+=-pref*B(n+1,al)/sp.factorial(n+1)*intY(d)
        for n in range(0,K+1-i):                     # corner
            for m in range(0,K+1-i-n):
                e=i+n+m
                if m<i: continue
                cy=coefY(m-i); d=sp.factorial(n)*sp.factorial(m)*sp.Poly(cy,X).coeff_monomial(X**n) if cy!=0 else 0
                if d==0: continue
                c[e]+=pref*B(n+1,al)*B(m+1,al)/(sp.factorial(n+1)*sp.factorial(m+1))*d
# - Caxis ~ -(1/2) sqrt(pi) eps^{-1} - (1/2) sqrt(2 pi/s) eps^{-1} e^{eps^2 s/8}
c[-1]-=spi/2
for j in range(0,(K+1)//2+1):
    e=2*j-1
    if e<=K: c[e]-=sp.sqrt(2*sp.pi/s)/2*(s/8)**j/sp.factorial(j)
res={}
for e in range(-2,K+1):
    v=sp.factor(sp.simplify(c[e]/(2*w*spi)))     # normalised by sqrt(2 pi s) = 2 w sqrt(pi)
    c[e]=sp.simplify(c[e]); res[e]=v
    print(e, 'c/sqrt(2pi s) =', v, flush=True)
pickle.dump({'c':c,'norm':res},open(f'axes_closed_K{K}.pkl','wb'))
json.dump({str(e):str(v) for e,v in res.items()},open(f'axes_closed_K{K}.json','w'),indent=1)
