import sympy as s
def ricci(x,gd):
    n=len(x); g=gd; gi=[1/v for v in g]
    G=lambda a,b,c: (s.diff(g[a],x[c]) if a==b else 0)+(s.diff(g[a],x[b]) if a==c else 0)-(s.diff(g[b],x[a]) if b==c else 0)
    Gam=[[[s.simplify(gi[a]*G(a,b,c)/2) for c in range(n)] for b in range(n)] for a in range(n)]
    R=[]
    for b in range(n):
        v=sum(s.diff(Gam[a][b][b],x[a]) for a in range(n))-sum(s.diff(Gam[a][b][a],x[b]) for a in range(n))\
         +sum(Gam[a][a][d]*Gam[d][b][b]-Gam[a][b][d]*Gam[d][a][b] for a in range(n) for d in range(n))
        R.append(s.simplify(v))
    return R
k,B,r,y=s.symbols('k B r y',positive=True)
def build(A,next_):
    xs=s.symbols('x0:%d'%next_); th=s.symbols('t1:7'); x=list(xs)+[y]+list(th)
    w=s.exp(-2*A); g=[-w]+[w]*(next_-1)+[1]
    sph=1
    for i in range(6):
        g.append(s.exp(2*B)*r**2*sph); sph=sph*s.sin(th[i])**2
    nf=11-next_-1
    g=g[:next_+1]+g[next_+1:next_+1+nf]
    if nf>6: pass
    return x,g,next_,nf
def blocks(A,next_=4):
    x,g,ne,nf=build(A,next_)
    if len(g)<11:  # pad fibre for control C2 with extra flat-ish dims not needed
        pass
    R=ricci(x,g); n=len(x)
    rr=[s.simplify(R[i]/g[i]) for i in range(n)]
    Rs=s.simplify(sum(rr)); Gb=[s.simplify(v-Rs/2) for v in rr]
    return rr,Rs,Gb,ne
K=s.Symbol('K'); kap=5/r**2; Ksub={K:kap*s.exp(-2*B)}
rr,Rs,Gb,ne=blocks(k*y)
P1=all(s.simplify(rr[i]+4*k**2)==0 for i in range(5)) and all(s.simplify(rr[i]-kap*s.exp(-2*B))==0 for i in range(5,11))
P2=s.simplify(Rs-(-20*k**2+6*kap*s.exp(-2*B)))==0 and all(s.simplify(Gb[i]-(6*k**2-3*kap*s.exp(-2*B)))==0 for i in range(5)) and all(s.simplify(Gb[i]-(10*k**2-2*kap*s.exp(-2*B)))==0 for i in range(5,11))
lock={r:s.sqrt(5/(8*k**2))*s.exp(-B)}  # K=kap e^-2B=8k^2
P3=s.simplify(Rs.subs(lock)-28*k**2)==0 and all(s.simplify(Gb[i].subs(lock)+18*k**2)==0 for i in range(5)) and all(s.simplify(Gb[i].subs(lock)+6*k**2)==0 for i in range(5,11))
print("ricci/g",rr[:6],"R",Rs)
rc,_,_,_=blocks(k*y**2); C1=s.simplify(rc[4]+4*k**2)!=0
# C2: 3 ext (x0..x2) + y + 7 fibre would need S^7; use same S^6 + 1 flat fibre dim => 3+1+7=11
x3=list(s.symbols('x0:3'))+[y]+list(s.symbols('t1:7'))+[s.Symbol('z')]
w=s.exp(-2*k*y); g3=[-w,w,w,1]; sph=1; th=x3[4:10]
for i in range(6): g3.append(s.exp(2*B)*r**2*sph); sph*=s.sin(th[i])**2
g3.append(s.exp(2*B)); R3=ricci(x3,g3); r3=[s.simplify(R3[i]/g3[i]) for i in range(11)]
Rs3=s.simplify(sum(r3)); C2=s.simplify(r3[0]-Rs3/2-(6*k**2-3*kap*s.exp(-2*B)))!=0
print("P1",P1,"P2",P2,"P3",P3,"C1(fails as required)",C1,"C2(fails as required)",C2)
print("RESULT","PASS" if all([P1,P2,P3,C1,C2]) else "FAIL")
