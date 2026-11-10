# Local-derived (t4436, branches a-1/a-2/a-3, b-1/b-2/b-3, c-1/c-2/c-3).
import cypari2, itertools; pari=cypari2.Pari(); pari.allocatemem(2*10**9); pari.set_real_precision(60)
P=lambda s: pari(s)
print("[a] Kronecker symbols at v=23: (140/23) =",P("kronecker(140,23)"),", (-7/23) =",P("kronecker(-7,23)"),", (-20/23) =",P("kronecker(-20,23)"))
print("[a] chi(-1): chi_140 ->",P("kronecker(140,-1)"),", chi_-7 ->",P("kronecker(-7,-1)"))
print("[a-2] quadclassunit(140) [h, cyc, gens, reg]:",P("my(q=quadclassunit(140)); [q.no, q.cyc, q.reg]"), "; log(6+sqrt35) =",P("log(6+sqrt(35))"), "; fundamental unit:",P("quadunit(140)"),"norm",P("norm(quadunit(140))"))
print("[a-2] L(1,chi_140) (lfun) =",P("lfun(lfuncreate(140),1)"))
print("      2*h*log(eps)/sqrt(140) =",P("2*2*log(6+sqrt(35))/sqrt(140)"), " difference:",P("lfun(lfuncreate(140),1)-4*log(6+sqrt(35))/sqrt(140)"))
print("[a-3] L(1,chi_-7) (lfun) =",P("lfun(lfuncreate(-7),1)"), " pi*h/sqrt7 (h=1, w=2) =",P("Pi/sqrt(7)"))
print("[b] Gauss sums: g(chi_140) =",P("sum(a=1,140,kronecker(140,a)*exp(2*Pi*I*a/140))"), " sqrt140 =",P("sqrt(140)"), "; g(chi_-7) =",P("sum(a=1,7,kronecker(-7,a)*exp(2*Pi*I*a/7))"), " i sqrt7 =",P("I*sqrt(7)"))
print("[b] lfuncheckfeq (float, illustration): chi_140:",P("lfuncheckfeq(lfuncreate(140))"),", chi_-7:",P("lfuncheckfeq(lfuncreate(-7))"))
ex=list(range(1,46,2))+[23]
print("[b-2] D24 exponents:",ex," sum(2e+1) =",sum(2*e+1 for e in ex)," = dim so(48) =",48*47//2)
# [c] brute force: number of maximal totally singular subspaces of the split form x1y1+...+xnyn over F_q, and the two families
def count_max_isotropic(n,q):
    dim=2*n
    def Qf(v): return sum(v[i]*v[n+i] for i in range(n))%q
    def Bf(u,v): return sum(u[i]*v[n+i]+u[n+i]*v[i] for i in range(n))%q
    vecs=[v for v in itertools.product(range(q),repeat=dim) if any(v) and Qf(v)==0]
    def rref(rows):
        M=[list(r) for r in rows]; lead=0; R=[]
        for r in range(len(M)):
            pass
        # Gaussian elimination mod q
        M=[list(r) for r in rows]; piv=[]; row=0
        for col in range(dim):
            sel=next((i for i in range(row,len(M)) if M[i][col]%q),None)
            if sel is None: continue
            M[row],M[sel]=M[sel],M[row]; invp=pow(M[row][col],-1,q); M[row]=[(x*invp)%q for x in M[row]]
            for i in range(len(M)):
                if i!=row and M[i][col]%q:
                    f=M[i][col]; M[i]=[(a-f*b)%q for a,b in zip(M[i],M[row])]
            row+=1
            if row==len(M): break
        return tuple(tuple(r) for r in M[:row])
    level={rref([v]) for v in vecs}
    for k in range(2,n+1):
        new=set()
        for U in level:
            for v in vecs:
                if all(Bf(u,v)==0 for u in U):
                    W=rref(list(U)+[v])
                    if len(W)==k: new.add(W)
        level=new
    maxs=list(level)
    U0=rref([tuple(1 if j==i else 0 for j in range(dim)) for i in range(n)])
    def dimint(U,W):
        return len(U)+len(W)-len(rref(list(U)+list(W)))
    fam=[ (n-dimint(U,U0))%2 for U in maxs]
    return len(maxs), fam.count(0), fam.count(1)
from math import prod
for n,q in [(1,23),(2,3),(2,5),(2,7),(2,23),(3,3),(3,5),(4,3)]:
    c,f0,f1=count_max_isotropic(n,q)
    print(f"[c] (n,q)=({n},{q}): #maximal totally singular = {c}; formula prod_(i=0..n-1)(q^i+1) = {prod(q**i+1 for i in range(n))}; families (codim parity vs U0): {f0} + {f1}; one-family formula prod_(i=1..n-1)(q^i+1) = {prod(q**i+1 for i in range(1,n))}")
contour=2*prod(23**i+1 for i in range(1,24)); og=prod(23**i+1 for i in range(24))
print("[c-1] #OG(24,48)(F23) == Codex contour 2*prod_(i=1..23)(23^i+1):", og==contour, "; digits:", len(str(og)))
