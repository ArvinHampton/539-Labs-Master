# Independent check of odd-prime local factor t = tr_{E0_p} S on C[Z/p^e], q=c x^2/p^e.
# (a) exact trace on W+ via exact Gauss sums in Z[zeta_n] (sympy-free integer cyclotomic arithmetic)
# (b) E0_p = rho-span(delta_0) equals W+ : mod-ell rank (rank mod ell <= true rank <= dim W+)
import sys, math
from sympy import factorint, primerange, isprime, cyclotomic_poly, Poly, symbols, legendre_symbol, jacobi_symbol
X=symbols('X')
def gsum_vec(n,a):  # sum_x zeta_n^{a x^2}, x mod n, as coefficient vector
    v=[0]*n
    for x in range(n): v[(a*x*x)%n]+=1
    return v
def mul(u,v,n):
    w=[0]*n
    for i,a in enumerate(u):
        if a:
            for j,b in enumerate(v):
                if b: w[(i+j)%n]+=a*b
    return w
def reduce(v,n):
    P=Poly(cyclotomic_poly(n,X),X); return Poly(list(reversed(v)),X).rem(P)
def exact_t(p,e,c):
    n=p**e
    G=lambda a: gsum_vec(n,a%n)
    # S = conj(G(c))/n * F, F_xy=e(-2cxy/n);  tr F = G(-2c); conj G(c)=G(-c); tr SZ uses F_{x,-x}: G(2c)
    trS=reduce(mul(G(-c),G(-2*c),n),n); trSZ=reduce(mul(G(-c),G(2*c),n),n)
    num=(trS+trSZ)
    assert num.degree()<=0, (p,e,num)
    val=num.as_expr()
    assert val % (2*n)==0
    return val//(2*n)
def predicted(p,e):
    if e%2==0: return 1
    return jacobi_symbol(2,p) if p%4==1 else 0
def span_rank(p,e,c,ell):
    n=p**e; import numpy as np
    g=pow(2,1,ell)
    # primitive n-th root mod ell
    for h in range(2,ell):
        z=pow(h,(ell-1)//n,ell)
        if all(pow(z,n//r,ell)!=1 for r in factorint(n)): break
    zt=[pow(z,k,ell) for k in range(n)]
    T=np.array([zt[(c*x*x)%n] for x in range(n)],dtype=object)
    F=np.array([[zt[(-2*c*x*y)%n] for y in range(n)] for x in range(n)],dtype=np.int64)
    basis=[];piv=[]
    def addv(v):
        v=v.copy()
        for b,pc in zip(basis,piv):
            if v[pc]: v=(v-v[pc]*b)%ell
        nz=np.nonzero(v)[0]
        if len(nz)==0: return False
        pc=nz[0]; v=(v*pow(int(v[pc]),ell-2,ell))%ell
        for i in range(len(basis)):
            if basis[i][pc]: basis[i]=(basis[i]-basis[i][pc]*v)%ell
        basis.append(v);piv.append(pc);return True
    T=np.array([int(t) for t in T],dtype=np.int64)
    d0=np.zeros(n,dtype=np.int64);d0[0]=1
    queue=[d0];addv(d0)
    while queue:
        v=queue.pop()
        for w in ((F@v)%ell,(T*v)%ell):
            if addv(w): queue.append(basis[-1])
    return len(basis)
if __name__=="__main__":
    bad=0
    for n in range(3,202,2):
        f=factorint(n)
        if len(f)!=1: continue
        (p,e),=f.items()
        nr=next(a for a in range(2,p) if legendre_symbol(a,p)==-1)
        ell=next(l for l in range(4*n*1000+1,10**9,n) if isprime(l))
        for c in (1,nr):
            t=exact_t(p,e,c); r=span_rank(p,e,c,ell)
            ok=(t==predicted(p,e)) and r==(n+1)//2
            bad+=not ok
            print(f"p^e={p}^{e}={n} c={c} t_exact={t} pred={predicted(p,e)} dimE0(mod {ell})={r} dimW+={(n+1)//2} {'OK' if ok else 'FAIL'}")
    print("FAILURES",bad)
