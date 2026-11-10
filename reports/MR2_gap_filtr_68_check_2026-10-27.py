from sympy import Matrix, divisor_sigma, GF
from sympy.polys.matrices import DomainMatrix
N=120; p=7
def E(k,c):
    a=[0]*N; a[0]=1
    for n in range(1,N): a[n]=c*divisor_sigma(n,k-1)
    return a
def sc(a,m):  # a(mz)
    b=[0]*N
    for n in range(0,N,m): b[n]=a[n//m]
    return b
def mul(a,b): 
    c=[0]*N
    for i in range(N):
        if a[i]:
            for j in range(N-i): c[i+j]+=a[i]*b[j]
    return c
from fractions import Fraction as F
E2=E(2,-24);E4=E(4,240);E6=E(6,-504)
g=[7*x-y for x,y in zip(sc(E2,7),E2)]  # wt2 Gamma0(7)
B4=[E4,sc(E4,7),mul(g,g)]
# solve a0=0, a1=1 for cusp-ish; dim S4=1 so impose a0=0,a1=1 and a0 at other cusp unknown: use 3 eqns a0=0,a1=1, and Hecke check
M=Matrix([[b[0] for b in B4],[b[1] for b in B4],[b[2] for b in B4]])
# unknown a2: try eigenform condition a4=a2^2-8 ; brute a2 in -5..5
import itertools
for a2 in range(-6,7):
    x=M.solve(Matrix([0,1,a2]))
    f=[sum(x[i]*B4[i][n] for i in range(3)) for n in range(N)]
    if all(v==int(v) for v in f) and f[4]==f[2]**2-8 and f[6]==f[2]*f[3]:
        print("f",f[:12]); break
th3=[(n**3*f[n])%p for n in range(N)]
def inspan(bas,v):
    rows=[[int(b[n])%p for b in bas]+[v[n]%p] for n in range(N)]
    A=Matrix([r[:-1] for r in rows]); Ab=Matrix(rows)
    rk=lambda m: DomainMatrix.from_Matrix(m).convert_to(GF(p)).rank()
    return rk(A),rk(Ab)
print("wt4 rank,aug",inspan(B4,th3))
fz=f
W={2:[g],4:[E4,sc(E4,7),fz,mul(g,g)],6:[E6,sc(E6,7),mul(g,E4),mul(g,sc(E4,7)),mul(g,fz)]}
W8=[mul(a,b) for a in W[4] for b in W[4]]+[mul(g,b) for b in W[6]]
# GAP-FILTR-68: enlarge generators; dim M_k(Gamma0(7)) = 1+2*floor(k/3) (genus 0, 2 cusps, e2=0, e3=2)
def eta_pow(m,e):  # prod (1-q^{mn})^e, q^{m/24} shift handled by caller
    a=[0]*N; a[0]=1
    for n in range(1,N//m+1):
        for _ in range(e):
            for i in range(N-1,m*n-1,-1): a[i]-=a[i-m*n]
    return a
def shift(a,s):
    return [0]*s+a[:N-s]
# eta-quotients with integral q-order, weight 3, character (.|-7): h1=eta^7(z)/eta(7z)? use h=(eta(z)eta(7z))^3 = q^1 * prod
h=shift(mul(eta_pow(1,3),eta_pow(7,3)),1)
u=[0]*N  # eta(z)^7/eta(7z): q^0
inv7=[0]*N; inv7[0]=1
for n in range(1,N//7+1):  # 1/(1-q^{7n}) geometric
    t=inv7[:]
    for i in range(7*n,N): t[i]+=t[i-7*n]
    inv7=t
u=mul(eta_pow(1,7),inv7)
v=[0]*N; inv1=[0]*N; inv1[0]=1
for n in range(1,N):
    t=inv1[:]
    for i in range(n,N): t[i]+=t[i-n]
    inv1=t
v=shift(mul(eta_pow(7,7),inv1),2)  # eta(7z)^7/eta(z), order q^2
W3=[h,u,v]
G6=W[6]+[mul(g,mul(g,g))]+[mul(a,b) for a in W3 for b in W3]
G8=W8+[mul(g,b) for b in G6]+[mul(mul(g,g),b) for b in W[4]]
for k,G in ((6,G6),(8,G8)):
    print("wt",k,"dim",1+2*(k//3),"rank,aug",inspan(G,th3))
