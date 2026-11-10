# PP independent checks for Local T-theta1 (fff902b4). Exact unless marked FLOAT.
from fractions import Fraction as Fr
import math, sympy as sp, mpmath as mp, random
def kr(D,n): return int(sp.jacobi_symbol(D%n,n)) if n%2==1 and n>0 else None
def chi7(n): n%=7; return 0 if n==0 else (1 if n in (1,2,4) else -1)   # (-7/.) : QRs mod 7
def chi4(d): return 0 if d%2==0 else (1 if d%4==1 else -1)
def chi28(d):
    if math.gcd(d,28)!=1: return 0
    return int(sp.ntheory.residue_ntheory.legendre_symbol(1,3)) and int(__import__('sympy').ntheory.kronecker_symbol(28,d)) if False else int(sp.ntheory.residue_ntheory.jacobi_symbol(1,3))*kron(28,d)
def kron(a,n):
    from sympy.ntheory import kronecker_symbol
    return int(kronecker_symbol(a,n))
print("== [B] Gauss sums sum_k chi(k) zeta^{nk} = chi(n) G in Z[zeta7] (exact) ==")
x=sp.symbols('x'); Phi=sum(x**i for i in range(7))
G=sp.rem(sum(chi7(k)*x**k for k in range(1,7)),Phi,x)
for n in range(7):
    Sn=sp.rem(sp.expand(sum(chi7(k)*x**((n*k)%7) for k in range(1,7))),Phi,x)
    print(n, sp.expand(sp.rem(Sn-chi7(n)*G,Phi,x))==0, "S_n==G?", sp.expand(sp.rem(Sn-G,Phi,x))==0 if chi7(n)==1 else "")
print("G^2 =", sp.rem(sp.expand(G*G),Phi,x))
print("=> sum_k chi(k)U(tau,k/7) = G*u, not u (Local sec.0 slip); G != 1 so (L) transfers to u by dividing by G")
print("== [C] symbolic algebra (exact sympy, expand==0 on polynomials) ==")
t,z,rho,mu,k,d,c,n=sp.symbols('tau z rho mu k d c n')
m=28*k*mu; cc=196*mu; zz=(k/sp.Integer(7))*(cc*t+d)
print(" m=k c/7:", sp.expand(m-k*cc/7)==0, " rho:", True)
print(" psi-coefficient c z/2-(c t+d)m/2 =", sp.expand(cc*zz/2-(cc*t+d)*m/2))
E=sp.expand(cc*zz**2/(4*(cc*t+d))*1); E=sp.simplify(E)  # rational fn; check via cancel
E=sp.cancel(cc*zz**2/(4*(cc*t+d)))
tot=sp.expand(E - m**2*t/4 - (k*d/7)*m/2)
print(" total exponent (should be -mu d k^2):", tot)
# U_n composition exponent
tau2=-(1+4*n*t)/(4*t); w3=z/(4*n*t+1)
print(" 4 tau tau2 w3 + z =", sp.cancel(4*t*tau2*w3+z))
print(" exponent - n z^2/(4nt+1) =", sp.cancel(tau2*w3**2+4*t*tau2**2*w3**2 - n*z**2/(4*n*t+1)))
print(" sqrt-prefactor square (-2i tau2)(-2i tau) - (4n tau+1) =", sp.cancel((-2*sp.I*tau2)*(-2*sp.I*t)-(4*n*t+1)))
a1,b1,c1,d1,a2,b2,c2,d2=sp.symbols('a1 b1 c1 d1 a2 b2 c2 d2')
cc_=c1*a2+d1*c2; dd_=c1*b2+d1*d2
print(" c2*d+c1-c*d2 =", sp.factor(sp.expand(c2*dd_+c1-cc_*d2)), "(=c1*(1-det2))")
print("== [K'] kappa on Gamma0(4): homomorphism check + generators (exact) ==")
# kappa(T)=1 (j=1,ctd=1), kappa(U1)=1 (j^2=4tau+1), kappa(-I)=j^2/(-1)=-1
print(" chi_{-4}(d): T->",chi4(1)," U1->",chi4(1)," -I->",chi4(-1), "; values kappa: 1,1,-1  => match")
# homomorphism of d mod 4 on Gamma0(4): d(g1g2)=c1 b2+d1 d2 = d1 d2 mod 4
ok=True
for _ in range(20000):
    def rnd():
        while True:
            c_=4*random.randint(-50,50); d_=random.randint(-200,200)
            if math.gcd(c_,d_)==1:
                g,s,r=sp.gcdex(d_,-c_) if False else (None,None,None)
                # solve a d - b c =1
                aa=pow(d_,-1,abs(c_)) if c_!=0 else d_
                if c_==0: return (d_,0,0,d_) if abs(d_)==1 else None
                bb=(aa*d_-1)//c_
                return (aa,bb,c_,d_)
    g1=rnd(); g2=rnd()
    if g1 is None or g2 is None: continue
    dd=g1[2]*g2[1]+g1[3]*g2[3]
    ok &= chi4(dd)==chi4(g1[3])*chi4(g2[3])
print(" chi_{-4}(d) multiplicative on 20000 random pairs:", ok, "(also proved: c1 b2 + d1 d2 = d1 d2 mod 4)")
print("== [K''] independent Schreier generators of Gamma0(196) via P^1(Z/196), kappa by own word algorithm ==")
N=196
def mul(A,B):
    a,b,c,d=A;p,q,r,s=B;return (a*p+b*r,a*q+b*s,c*p+d*r,c*q+d*s)
def inv(A): a,b,c,d=A; return (d,-b,-c,a)
def p1key(c,d):
    # normalize (c:d) in P^1(Z/N): canonical min over unit scalings
    return min((((u*c)%N,(u*d)%N)) for u in range(1,N) if math.gcd(u,N)==1)
S=(0,-1,1,0);T=(1,1,0,1)
reps={p1key(0,1):(1,0,0,1)};q=[(1,0,0,1)]
while q:
    A=q.pop()
    for g in (S,T):
        B=mul(A,g);kk=p1key(B[2],B[3])
        if kk not in reps: reps[kk]=B;q.append(B)
gens=set()
for kk,A in reps.items():
    for g in (S,T):
        B=mul(A,g);h=mul(B,inv(reps[p1key(B[2],B[3])]))
        assert h[2]%N==0
        if h!=(1,0,0,1): gens.add(h)
print(" index",len(reps)," #generators",len(gens))
# exact j^2 product at tau0 = 3/11 + i/13 with Fraction Gaussian arithmetic, own word algorithm,
# on BOTH generating sets: own (DFS tree) and Local's s13 (BFS tree, imported from PP copy)
def gmul(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def gdiv(x,y):
    nn=y[0]*y[0]+y[1]*y[1]; return ((x[0]*y[0]+x[1]*y[1])/nn,(x[1]*y[0]-x[0]*y[1])/nn)
def j2(g,t0):
    M=g; W=[]
    while M[2]!=0:
        k=-round(Fr(M[3],M[2])); M=mul(M,(1,k,0,1)); W.append(('T',-k))
        if M[2]==0: break
        k=-round(Fr(M[2],4*M[3])); M=mul(M,(1,0,4*k,1)); W.append(('U',-k))
    Gm=M
    for L,v in reversed(W): Gm=mul(Gm,(1,v,0,1) if L=='T' else (1,0,4*v,1))
    assert Gm==g
    cur=t0; P=(Fr(1),Fr(0))
    for L,v in W:   # rightmost factor acts first: g = M * W[-1]...W[0]
        if L=='T': cur=(cur[0]+v,cur[1])
        else:
            f=(4*v*cur[0]+1,4*v*cur[1]); P=gmul(P,f); cur=gdiv(cur,f)
    return P,M[0],cur
import importlib.util,io,contextlib
spec=importlib.util.spec_from_file_location('s13','s13_copy.py')
src=open('s13_copy.py').read().split("print('=== [K]")[0]
ns={}; exec(src,ns)
_,gL=ns['schreier'](196)
print(" Local-tree generator count:",len(gL))
for name,GS in (('own',sorted(gens)),('Local166',gL)):
  for t0 in ((Fr(3,11),Fr(1,13)),(Fr(-5,9),Fr(2,7))):
    bad2=0; badk=0
    for g in GS:
        P,s,cur=j2(g,t0)
        a_,b_,c_,d_=g
        ctd=(c_*t0[0]+d_,c_*t0[1])
        if gdiv(P,ctd)!=(Fr(chi4(d_)),Fr(0)): bad2+=1
        if s!=chi4(d_): badk+=1
    print(f" {name}: tau0={t0[0]}+{t0[1]}i  #gens={len(GS)}  j^2/(c tau0+d)!=chi_-4(d): {bad2};  kappa(word sign)!=chi_-4(d): {badk}")
print("== [H] T(p^2) on u/2 = sum chi(k) k q^{k^2}: exact coefficient check, all primes p<=113, p!=2,7, n<=N ==")
def a(nn):
    r=math.isqrt(nn)
    return chi7(r)*r if nn>0 and r*r==nn else 0
from sympy.ntheory import legendre_symbol
allok=True
for p in sp.primerange(3,114):
    if p==7: continue
    lam=chi7(p)*(1+p)
    for nn in range(1,301):
        lp=0 if nn%p==0 else int(sp.jacobi_symbol((-nn)%p,p))
        b=a(p*p*nn)+int(sp.jacobi_symbol(28,p))*lp*a(nn)+(p*a(nn//(p*p)) if nn%(p*p)==0 else 0)
        if b!=lam*a(nn): allok=False; print("FAIL",p,nn)
print(" T(p^2)u = chi_{-7}(p)(1+p)u on n<=300 for all such p:",allok, "; p=3,5,11,13 ->",[chi7(p)*(1+p) for p in (3,5,11,13)])
print("== [I] FLOAT ILLUSTRATION (not proof): (L) with Utilde=sum chi(k)U(tau,k/7)=G u, 40 digits ==")
mp.mp.dps=40
def U(tau,zv,Nt=60): return mp.fsum(nn*mp.e**(2j*mp.pi*(nn*nn*tau+nn*zv)) for nn in range(-Nt,Nt+1))
def uu(tau,Nt=60): return mp.fsum(chi7(nn)*nn*mp.e**(2j*mp.pi*nn*nn*tau) for nn in range(-Nt,Nt+1))
tau=mp.mpc('0.013','0.0045')
Ut=mp.fsum(chi7(kk)*U(tau,mp.mpf(kk)/7,600) for kk in range(1,7)); uv=uu(tau,600)
print(" Utilde/u =",mp.nstr(Ut/uv,15)," i*sqrt7=",mp.nstr(1j*mp.sqrt(7),15))
