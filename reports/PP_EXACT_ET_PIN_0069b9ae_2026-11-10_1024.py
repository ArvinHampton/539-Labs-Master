# PP exact re-check of MR2 c2p_ET_pin_lift (0069b9ae). Gaussian-integer matrices as (Re, Im) int64 pairs; equality by np.array_equal only.
import numpy as np, itertools
N=256
def mul(X,Y): A,B=X; C,D=Y; return (A@C-B@D, A@D+B@C)
def neg(X): return (-X[0],-X[1])
def add(X,Y): return (X[0]+Y[0],X[1]+Y[1])
def eq(X,Y): return np.array_equal(X[0],Y[0]) and np.array_equal(X[1],Y[1])
def kron(X,Y): A,B=X; C,D=Y; return (np.kron(A,C)-np.kron(B,D), np.kron(A,D)+np.kron(B,C))
Z=lambda n: np.zeros((n,n),dtype=np.int64)
s0=(np.eye(2,dtype=np.int64),Z(2)); sx=(np.array([[0,1],[1,0]],dtype=np.int64),Z(2))
sy=(Z(2),np.array([[0,-1],[1,0]],dtype=np.int64)); sz=(np.diag([1,-1]).astype(np.int64),Z(2))
def kr(ms):
    out=(np.ones((1,1),dtype=np.int64),Z(1))
    for m in ms: out=kron(out,m)
    return out
e=[]
for k in range(8):
    e.append(kr([sz]*k+[sx]+[s0]*(7-k))); e.append(kr([sz]*k+[sy]+[s0]*(7-k)))
I=(np.eye(N,dtype=np.int64),Z(N)); O=(Z(N),Z(N))
def sc(c,X): return (c*X[0],c*X[1])
anti=all(eq(add(mul(e[a],e[b]),mul(e[b],e[a])), sc(2*(a==b),I)) for a in range(16) for b in range(16))
print("[X1] {e_a,e_b}=2 delta_ab I, all 16x16 pairs, exact:",anti)
def prod(idx):
    M=I
    for i in idx: M=mul(M,e[i])
    return M
w=prod(range(16))
print("[X2] omega^2 = I exact:",eq(mul(w,w),I),"| tr omega = ",int(np.trace(w[0])),"+",int(np.trace(w[1])),"i (=> chiral projectors (I+-omega)/2 idempotent, rank 128 each)")
L=prod([0,1,2,6])
print("[X3] L=e0e1e2e6: L^2 = I exact:",eq(mul(L,L),I),"| L omega = omega L:",eq(mul(L,w),mul(w,L)))
flip={0,1,2,6}
vec=all(eq(mul(mul(L,e[i]),L), e[i] if i not in flip else neg(e[i])) for i in range(16))
print("[X4] L e_i L^{-1} (L^{-1}=L) = -e_i for i in {x,phi1,phi2,a}, +e_i otherwise, all 16 exact:",vec,"=> Ad_L = df (+) R_a on R^16, hence on so(6), so(10), (6,10)")
biv=all(eq(mul(mul(L,mul(e[i],e[j])),L), mul(e[i],e[j]) if ((i in flip)==(j in flip)) else neg(mul(e[i],e[j]))) for i in range(16) for j in range(i+1,16))
print("[X5] Ad_L on all 120 bivectors e_ie_j = sign(df(+)R_a) exact:",biv)
M6=prod([0,1,2,6,7,8]); M3=prod([0,1,2])
print("[X6] 3-vector compensator e0e1e2e6e7e8: square = -I exact:",eq(mul(M6,M6),neg(I)),"| commutes with omega:",eq(mul(M6,w),mul(w,M6)))
print("[X7] no compensator e0e1e2: odd; anticommutes with omega exact:",eq(mul(M3,w),neg(mul(w,M3))),"(swaps the two 128s; not in Spin(16)); square = -I:",eq(mul(M3,M3),neg(I)))
print("[X8] rule (e_i1..e_ik)^2 = (-1)^{k(k-1)/2} I, k=1..8, exact:",[ (k, eq(mul(prod(range(k)),prod(range(k))), sc((-1)**(k*(k-1)//2),I))) for k in range(1,9)])
print("     => with 3 flipped tangent directions, compensator degree must be = 1 mod 4 (1 minimal; 3 gives -1; 5 also +1)")
# [d] combinatorial re-run (exact by construction)
W=['0','inf','1','i','-1','-i']; B6=frozenset(range(6))
def norm(T):
    T=frozenset(T); return min(T,B6-T,key=lambda s:(len(s),sorted(s)))
J2=sorted({norm(T) for k in (0,2,4,6) for T in itertools.combinations(range(6),k)},key=lambda s:(len(s),sorted(s)))
act=lambda p,T: norm({p[i] for i in T})
g1=(0,1,3,4,5,2); g2=(2,4,1,3,0,5); c=(0,1,2,5,4,3)
comp=lambda a,b: tuple(a[b[i]] for i in range(6)); idp=tuple(range(6))
def closure(gens):
    G={idp}; fr=[idp]
    while fr:
        nw=[]
        for h in fr:
            for g in gens:
                k=comp(g,h)
                if k not in G: G.add(k); nw.append(k)
        fr=nw
    return G
Ap=closure([g1,g2]); Fu=closure([g1,g2,c])
print("[D1] |J2|=",len(J2),"|Ap|=",len(Ap),"|Fu|=",len(Fu),"c in Ap:",c in Ap,"c^2=id:",comp(c,c)==idp)
# g1: x->ix, g2: x->(1+x)/(1-x); check as Mobius maps on W exactly with Gaussian rationals (inf handled)
from fractions import Fraction as F
pts=[None,'inf',(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))]; pts[0]=(F(0),F(0))
def cm(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cdiv(a,b): d=b[0]**2+b[1]**2; return ((a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d)
def mob(z,a,b,cc,d):
    if z=='inf': return 'inf' if cc==(0,0) else cdiv(a,cc)
    num=(a[0]*z[0]-a[1]*z[1]+b[0], a[0]*z[1]+a[1]*z[0]+b[1]); den=(cc[0]*z[0]-cc[1]*z[1]+d[0], cc[0]*z[1]+cc[1]*z[0]+d[1])
    return 'inf' if den==(0,0) else cdiv(num,den)
one=(F(1),F(0)); zero=(F(0),F(0)); ii=(F(0),F(1)); m1=(F(-1),F(0))
g1m=[pts.index(mob(z,ii,zero,zero,one)) for z in pts]
g2m=[pts.index(mob(z,one,one,m1,one)) for z in pts]
cm_=[pts.index(z if z=='inf' else (z[0],-z[1])) for z in pts]
print("[D2] g1 = x->ix:",tuple(g1m)==g1,"| g2 = x->(x+1)/(1-x):",tuple(g2m)==g2,"| c = complex conjugation:",tuple(cm_)==c)
rev=Fu-Ap; left=set(rev); inv=lambda g: tuple(sorted(range(6),key=lambda i:g[i]))
while left:
    p=min(left); cl={comp(comp(g,p),inv(g)) for g in Fu}; left-=cl
    print("  class size",len(cl),"| involutions in class:",all(comp(q,q)==idp for q in cl),"| J2 fixed:",sum(act(p,d)==d for d in J2),"| d0 fixed:",act(p,frozenset())==frozenset())
print("[D3] r=c fixed J2:",[sorted(W[i] for i in d) for d in J2 if act(c,d)==d])
# real point of y^2 = x(x^4-1) fixed by c: x=1,y=0 and x=2,y^2=30>0
print("[D4] c has fixed points on Sigma: x=1 gives y^2 =",1*(1**4-1),"; x=2 gives y^2 =",2*(2**4-1),"> 0 (real y)")
