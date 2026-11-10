import sympy as s
def ricci(x,g):
    n=len(x); gi=[1/v for v in g]
    G=lambda a,b,c:(s.diff(g[a],x[c]) if a==b else 0)+(s.diff(g[a],x[b]) if a==c else 0)-(s.diff(g[b],x[a]) if b==c else 0)
    Gam=[[[s.simplify(gi[a]*G(a,b,c)/2) for c in range(n)] for b in range(n)] for a in range(n)]
    return [s.simplify(sum(s.diff(Gam[a][b][b],x[a]) for a in range(n))-sum(s.diff(Gam[a][b][a],x[b]) for a in range(n))+sum(Gam[a][a][d]*Gam[d][b][b]-Gam[a][b][d]*Gam[d][a][b] for a in range(n) for d in range(n))) for b in range(n)]
k,B,r,y=s.symbols('k B r y',positive=True)
th=s.symbols('t1:8'); x=list(s.symbols('x0:3'))+[y]+list(th)
w=s.exp(-2*k*y); g=[-w,w,w,1]; sph=1
for i in range(7): g.append(s.exp(2*B)*r**2*sph); sph*=s.sin(th[i])**2
R=ricci(x,g); rr=[s.simplify(R[i]/g[i]) for i in range(11)]; Rs=s.simplify(sum(rr))
Kv=6/r**2*s.exp(-2*B); Ge=s.simplify(rr[0]-Rs/2); Gf=s.simplify(rr[4]-Rs/2)
c1=s.simplify(Ge-(6*k**2-3*Kv))!=0; c2=s.simplify(Gf-(10*k**2-2*Kv))!=0
print("ricci/g",rr[:5],"R",Rs,"G_ext",s.expand(Ge),"G_fib",s.expand(Gf))
print("C2_ext_fails",c1,"C2_fib_fails",c2,"RESULT","PASS" if (c1 and c2) else "FAIL")
