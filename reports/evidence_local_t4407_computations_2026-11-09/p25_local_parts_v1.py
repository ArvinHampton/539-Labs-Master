# Local-derived. t4407 item "2- and 5-parts": p-primary decomposition of the carrier discriminant form D(N2), local Weil
# representations rho_{D_p}, their e0-characters, signatures/Gauss sums, tensor factorization, Gamma0(49) visibility,
# and local root numbers of f=49a1 and Xi=elltwist(49a1,140). Exact arithmetic in Q(zeta_140) (coefficient vectors mod Phi_140).
import math, itertools
from fractions import Fraction as Fr
from sympy import cyclotomic_poly, symbols, Poly, jacobi_symbol, Matrix, QQ
import cypari2; pari=cypari2.Pari()
X=symbols('X'); M=140; PHI=Poly(cyclotomic_poly(M,X),X); DEG=PHI.degree()
red=[]   # x^k mod Phi as coefficient list (len DEG), k<M
for k in range(M):
    r=Poly(X**k,X).rem(PHI).all_coeffs()[::-1]; r=[Fr(int(c)) for c in r]+[Fr(0)]*(DEG-len(r)); red.append(r)
class C:
    __slots__=('v',)
    def __init__(s,v=None): s.v=v if v is not None else [Fr(0)]*DEG
    @staticmethod
    def z(k): return C(list(red[k%M]))
    @staticmethod
    def n(q): c=C(); c.v[0]=Fr(q); return c
    def __add__(s,o): return C([a+b for a,b in zip(s.v,o.v)])
    def __sub__(s,o): return C([a-b for a,b in zip(s.v,o.v)])
    def __mul__(s,o):
        if not isinstance(o,C): return C([a*o for a in s.v])
        prod=[Fr(0)]*(2*DEG)
        for i,a in enumerate(s.v):
            if a:
                for j,b in enumerate(o.v):
                    if b: prod[i+j]+=a*b
        out=[Fr(0)]*DEG
        for k,c in enumerate(prod):
            if c:
                for t,rc in enumerate(red[k] if k<M else red[k%M]): out[t]+=c*rc
        return C(out)
    def iszero(s): return all(a==0 for a in s.v)
    def __eq__(s,o): return (s-o).iszero()
    def conj(s):  # complex conjugation zeta->zeta^-1
        out=C()
        for i,a in enumerate(s.v):
            if a: out=out+C.z(-i)*a
        return out
# --- discriminant form of N2 (Gram [[2,14],[14,28]]) ---
Ginv=[[Fr(28,-140),Fr(-14,-140)],[Fr(-14,-140),Fr(2,-140)]]
els=sorted({((Ginv[0][0]*a+Ginv[0][1]*b)%1,(Ginv[1][0]*a+Ginv[1][1]*b)%1) for a in range(140) for b in range(140)})
def add(x,y): return ((x[0]+y[0])%1,(x[1]+y[1])%1)
def mul(k,x): return ((k*x[0])%1,(k*x[1])%1)
def bil(x,y): return (x[0]*(2*y[0]+14*y[1])+x[1]*(14*y[0]+28*y[1]))%1
def q(x): return (Fr(1,2)*(x[0]*(2*x[0]+14*x[1])+x[1]*(14*x[0]+28*x[1])))%1
def order(x): return math.lcm(x[0].denominator,x[1].denominator)
Dp={p:[x for x in els if order(x) in [p**k for k in range(8)]] for p in (2,5,7)}
print("|D_2|,|D_5|,|D_7| =",[len(Dp[p]) for p in (2,5,7)])
orth=all(bil(x,y)==0 for p in (2,5,7) for r in (2,5,7) if p<r for x in Dp[p] for y in Dp[r])
crt=len({add(add(a,b),c) for a in Dp[2] for b in Dp[5] for c in Dp[7]})==140
print("D = D_2 (+) D_5 (+) D_7 orthogonal:",orth," CRT bijection:",crt)
for p in (2,5,7):
    print(f" D_{p}: elements with q-values:",[(str(x),str(q(x))) for x in Dp[p]], " level =", math.lcm(*[q(x).denominator for x in Dp[p]]))
def gauss(S): 
    g=C()
    for x in S: g=g+C.z(int(q(x)*M))
    return g
def sig_of(S):
    g=gauss(S); n=len(S)
    for s in range(8):   # G = sqrt|D| e(s/8) <=> G^2 = |D| * i^s  (and sign fixed by checking G*e(-s/8) is positive real numerically)
        if (g*g)==C.n(n)*C.z(35*s):
            import cmath
            val=sum(cmath.exp(2j*math.pi*float(q(x))) for x in S)/math.sqrt(n)
            if abs(val-cmath.exp(2j*math.pi*s/8))<1e-9: return s,g
    return None,g
sig={}; G={}
for p in (2,5,7):
    sig[p],G[p]=sig_of(Dp[p]); print(f" Milgram: sig(D_{p}) mod 8 =",sig[p])
sD,GD=sig_of(els); print(" sig(D) mod 8 =",sD," sum of local sigs mod 8 =",sum(sig.values())%8)
def chi140(n):
    n%=140
    return 0 if math.gcd(n,140)!=1 else int(((-1)**((n-1)//2))*int(jacobi_symbol(n,5))*int(jacobi_symbol(n,7)))
gs=C()
for u in range(140): gs=gs+C.z(u)*chi140(u)
print(" G(D) == Gauss sum of chi_140 (=> S_D = g^-1 zeta^-B exactly as in 4a):", GD==gs, "; g^2==140:", (gs*gs)==C.n(140))
print(" prod_p G(D_p) == G(D):", (G[2]*G[5]*G[7])==GD)
# --- local Weil reps rho_p (Bruinier convention S e_g = e(-sig/8)/sqrt|D| sum e(-(g,d)) e_d, T e_g = e(q(g)) e_g) ---
def rep(S_):
    n=len(S_); c=G[[p for p in (2,5,7) if Dp[p]==S_][0]].conj()*Fr(1,n)   # e(-sig/8)/sqrt n = conj(G)/n
    Sm=[[C.z(-int(bil(x,y)*M))*c for y in S_] for x in S_]
    Tm=[C.z(int(q(x)*M)) for x in S_]
    Si=[[Sm[j][i].conj() for j in range(n)] for i in range(n)]   # unitary => inverse = conj transpose
    return Sm,Si,Tm
def mv(A,v): 
    n=len(v); out=[]
    for i in range(n):
        acc=C()
        for j in range(n):
            if not v[j].iszero(): acc=acc+A[i][j]*v[j]
        out.append(acc)
    return out
def word_apply(w,v,R):
    Sm,Si,Tm=R; Ti=[t.conj() for t in Tm]
    for c in reversed(w):
        if c=='S': v=mv(Sm,v)
        elif c=='s': v=mv(Si,v)
        elif c=='T': v=[a*b for a,b in zip(Tm,v)]
        else: v=[a*b for a,b in zip(Ti,v)]
    return v
Lm={'S':((0,-1),(1,0)),'s':((0,1),(-1,0)),'T':((1,1),(0,1)),'t':((1,-1),(0,1))}
inv={'S':'s','s':'S','T':'t','t':'T'}
def mmul(A,B): return ((A[0][0]*B[0][0]+A[0][1]*B[1][0],A[0][0]*B[0][1]+A[0][1]*B[1][1]),(A[1][0]*B[0][0]+A[1][1]*B[1][0],A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def wmat(w):
    Mx=((1,0),(0,1))
    for c in w: Mx=mmul(Mx,Lm[c])
    return Mx
def schreier(Nn):
    units=[u for u in range(1,Nn) if math.gcd(u,Nn)==1] or [1]
    key=lambda c,d: min(((u*c)%Nn,(u*d)%Nn) for u in units)
    reps={key(0,1):''}; Q=['']
    while Q:
        w=Q.pop(0); Mx=wmat(w)
        for x in 'ST':
            M2=mmul(Mx,Lm[x]); k=key(M2[1][0],M2[1][1])
            if k not in reps: reps[k]=w+x; Q.append(w+x)
    gens=[]
    for k,w in reps.items():
        for x in 'ST':
            M2=wmat(w+x); w2=reps[key(M2[1][0],M2[1][1])]; g=w+x+''.join(inv[c] for c in reversed(w2)); Mg=wmat(g)
            assert Mg[1][0]%Nn==0
            if Mg!=((1,0),(0,1)): gens.append((g,Mg))
    return len(reps),gens
loc_chi={2:lambda d:int(jacobi_symbol(-1,1)) if False else (0 if d%2==0 else (-1)**((d-1)//2)), 5:lambda d:int(jacobi_symbol(d%5,5)) if d%5 else 0, 7:lambda d:int(jacobi_symbol(d%7,7)) if d%7 else 0}
names={2:"chi_-4",5:"chi_5=(./5)",7:"chi_-7=(./7)"}
for p in (2,5,7):
    S_=Dp[p]; n=len(S_); R=rep(S_); Sm,Si,Tm=R
    I=[[C.n(1 if i==j else 0) for j in range(n)] for i in range(n)]
    def mm(A,B): return [[sum((A[i][k]*B[k][j] for k in range(n)),C()) for j in range(n)] for i in range(n)]
    def eqm(A,B): return all(A[i][j]==B[i][j] for i in range(n) for j in range(n))
    Tmat=[[Tm[i] if i==j else C() for j in range(n)] for i in range(n)]
    S2=mm(Sm,Sm); ST=mm(Sm,Tmat)
    rel=eqm(mm(Sm,Si),I) and eqm(mm(S2,S2),I) and eqm(mm(mm(ST,ST),ST),S2)
    lev=math.lcm(*[q(x).denominator for x in S_])
    ncos,gens=schreier(lev); i0=S_.index((Fr(0),Fr(0)))
    bad=0
    for g,Mg in gens:
        v=[C.n(1 if i==i0 else 0) for i in range(n)]; v=word_apply(g,v,R)
        tgt=[C.n(loc_chi[p](Mg[1][1]) if i==i0 else 0) for i in range(n)]
        if not all(a==b for a,b in zip(v,tgt)): bad+=1
    mI=[C.n(1 if i==i0 else 0) for i in range(n)]; vZ=mv(S2,mI)
    zchar=[ (vZ[i0]==C.n(s)) for s in (1,-1)]
    print(f"rho_D{p}: dim {n}, level {lev}: S S^-1=I, S^4=I, (ST)^3=S^2 EXACT: {rel} (=> genuine SL2(Z)-rep, factors through SL2(Z/{lev}));"
          f" Gamma0({lev}) [{ncos} cosets, {len(gens)} Schreier gens]: rho(g)e0 = {names[p]}(d) e0 fails on {bad}; rho(-I)e0 = {'+' if zchar[0] else ('-' if zchar[1] else '?')}e0")
# --- Gamma0(49) visibility of the 2,5 part: 1-dim subreps of rho_{D2}(x)rho_{D5} (image of Gamma0(49) in SL2(Z/20) is everything) ---
import numpy as np, cmath
def numrep(S_,p):
    n=len(S_); s=sig[p]
    Sm=np.array([[cmath.exp(-2j*math.pi*(s/8+float(bil(x,y)))) for y in S_] for x in S_])/math.sqrt(n)
    Tm=np.diag([cmath.exp(2j*math.pi*float(q(x))) for x in S_]); return Sm,Tm
S2n,T2n=numrep(Dp[2],2); S5n,T5n=numrep(Dp[5],5)
S25=np.kron(S2n,S5n); T25=np.kron(T2n,T5n)
for k in range(4):
    w=1j**k; A=np.vstack([S25-w*np.eye(20),T25-w*np.eye(20)])  # characters of SL2(Z) of level | 4: T->i^k, S->i^(-3k)=i^k
    sv=np.linalg.svd(A,compute_uv=False); print(f" rho_D2(x)rho_D5: dim of lines with character T->i^{k}, S->i^{k}: {int(sum(sv<1e-9))} (smallest sing. value {sv.min():.3e})")
e0=np.zeros(20); e0[Dp[2].index((Fr(0),Fr(0)))*5+Dp[5].index((Fr(0),Fr(0)))]=1
print(" e0^(2,5) eigenvector of S? |S e0 - <S e0,e0> e0| =", np.linalg.norm(S25@e0-(e0@S25@e0)*e0))
# --- local root numbers (PARI ellrootno(E,p)) and conductor exponents ---
pari("E=ellinit([1,-1,0,-2,-1]); X=ellinit(elltwist(E,140)); Xm=ellinit(elltwist(E,-20))")
print("global rootno: f", pari("ellrootno(E)"), " Xi", pari("ellrootno(X)"), " E^(-20)", pari("ellrootno(Xm)"), " Xi~E^(-20) isogenous:", pari("ellap(X,1009)==ellap(Xm,1009)"))
for p in (2,5,7):
    print(f" p={p}: local eps_p(f)={pari(f'ellrootno(E,{p})')}, eps_p(Xi)={pari(f'ellrootno(X,{p})')}, cond exp f={pari(f'elllocalred(E,{p})[1]')}, Xi={pari(f'elllocalred(X,{p})[1]')}, Frob char poly of f at p (if good): {pari(f'if(ellap(E,{p})!=0||{p}!=7, if({p}==7,\"bad\", Strprintf(\"x^2-(%d)x+%d\", ellap(E,{p}),{p})),\"bad\")')}")
print(" eps_inf = -1 (weight 2). Product check f:", pari("-1*ellrootno(E,2)*ellrootno(E,5)*ellrootno(E,7)"), " Xi:", pari("-1*ellrootno(X,2)*ellrootno(X,5)*ellrootno(X,7)"))
print(" chi_p(-1): chi_-4(-1)=-1, (−1/5)=", int(jacobi_symbol(4,5)), ", (−1/7)=", int(jacobi_symbol(6,7)))
