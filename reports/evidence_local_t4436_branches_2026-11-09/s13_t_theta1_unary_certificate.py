# Local-derived (t4436, T-theta1). Exact certificates supporting
# FINDINGS_LOCAL_t4436_T_THETA1_UNARY_THETA_2026-11-10_*.md
#
# [K] j(gamma,tau)^2 = chi_{-4}(d)*(c*tau+d) for every Schreier generator of
#     Gamma0(196), at two Gaussian-rational points, using the PP 0f1d3361 /
#     F0-5 cocycle for j (word in T, U, -I; exact Arg tracking). No floating
#     point is used in [K], [C] or [G].
# [C] Kronecker identity chi_{-7} chi_{-4} = chi_28 (checked on a range, and
#     the identity (ab/n)=(a/n)(b/n) is used in the findings).
# [G] Gauss sum G = sum_{k=1}^{6} chi_{-7}(k) zeta_7^k satisfies G^2 = -7
#     exactly in Z[zeta_7]/(Phi_7). The sign under zeta |-> e(1/7) is +i*sqrt(7)
#     by writing G = 2i(sin(2pi/7)+sin(4pi/7)-sin(6pi/7)) with a positive
#     parenthesis (sines on (0,pi)); this is recorded, not float-certified.
# [I], [S] float illustrations of the inversion and slash laws (NOT a proof).
from fractions import Fraction as Fr
import math

def gm(x,y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def gdiv(x,y):
    n=y[0]*y[0]+y[1]*y[1]
    return ((x[0]*y[0]+x[1]*y[1])/n, (x[1]*y[0]-x[0]*y[1])/n)
def upper(z):
    return z[1]>0 or (z[1]==0 and z[0]<0)
def mob(M,t):
    a,b,c,d=M
    return gdiv((a*t[0]+b, a*t[1]), (c*t[0]+d, c*t[1]))
def mul(A,B):
    a,b,c,d=A; p,q,r,s=B
    return (a*p+b*r, a*q+b*s, c*p+d*r, c*q+d*s)
def inv(A):
    a,b,c,d=A
    return (d,-b,-c,a)

def word(g):
    a,b,c,d=g
    assert c%4==0 and a*d-b*c==1
    M=g; rec=[]
    while M[2]!=0:
        a,b,c,d=M
        k=round(Fr(-d,c))
        if k:
            M=mul(M,(1,k,0,1)); rec.append(('T',-k))
        a,b,c,d=M
        if c==0:
            break
        k=round(Fr(-c,4*d)); assert k!=0
        M=mul(M,(1,0,4*k,1)); rec.append(('U',-k))
    a,b,c,d=M
    assert c==0 and a==d and a in (1,-1)
    w=[]
    if a==-1:
        w.append(('N',1)); w.append(('T',-b))
    else:
        w.append(('T',b))
    w+=list(reversed(rec))
    P=(1,0,0,1)
    for L,n in w:
        P=mul(P, (-1,0,0,-1) if L=='N' else ((1,n,0,1) if L=='T' else (1,0,4*n,1)))
    assert P==g,(P,g)
    return w

def jfactors(g,t):
    w=word(g); zs=[]; cur=t
    for L,n in reversed(w):
        if L=='U':
            zs.append((4*n*cur[0]+1,4*n*cur[1])); cur=mob((1,0,4*n,1),cur)
        elif L=='T':
            cur=(cur[0]+n,cur[1])
    return zs, cur

def sqrtprod(zs):
    P=(Fr(1),Fr(0)); n=0
    for z in zs:
        Q=gm(P,z)
        if upper(P) and upper(z) and not upper(Q):
            n+=1
        elif (not upper(P)) and (not upper(z)) and upper(Q):
            n-=1
        P=Q
    return P,n

def J(g,t):
    zs,cur=jfactors(g,t)
    assert cur==mob(g,t)
    return sqrtprod(zs)

def schreier(L):
    Lm={'S':(0,-1,1,0),'T':(1,1,0,1)}
    units=[u for u in range(1,L) if math.gcd(u,L)==1]
    def key(c,d):
        return min(((u*c)%L,(u*d)%L) for u in units)
    reps={key(0,1):(1,0,0,1)}; queue=[(1,0,0,1)]
    while queue:
        A=queue.pop(0)
        for ch in 'ST':
            A2=mul(A,Lm[ch]); k=key(A2[2],A2[3])
            if k not in reps:
                reps[k]=A2; queue.append(A2)
    gens=set()
    for k,A in reps.items():
        for ch in 'ST':
            A2=mul(A,Lm[ch]); g=mul(A2,inv(reps[key(A2[2],A2[3])]))
            assert g[2]%L==0
            if g!=(1,0,0,1):
                gens.add(g)
    return len(reps),sorted(gens)

def kronecker(D,n):
    D=int(D); n=int(n)
    if n==0:
        return 1 if abs(D)==1 else 0
    sign=1
    if n<0:
        if D<0:
            sign=-1
        n=-n
    odd,v=n,0
    while odd%2==0:
        odd//=2; v+=1
    res=sign
    if v:
        if D%2==0:
            return 0
        t=(D*D-1)//8
        if v%2==1 and t%2==1:
            res=-res
    def jacobi(a,m):
        a=a%m
        if a<0:
            a+=m
        r=1
        while a!=0:
            while a%2==0:
                a//=2
                if m%8 in (3,5):
                    r=-r
            a,m=m,a
            if a%4==3 and m%4==3:
                r=-r
            a=a%m
        return r if m==1 else 0
    if odd>1:
        res*=jacobi(D,odd)
    return res

# self-checks of the Kronecker implementation
assert kronecker(-4,1)==1 and kronecker(-4,3)==-1 and kronecker(-4,5)==1
assert kronecker(-4,-1)==-1
assert kronecker(-7,1)==1 and kronecker(-7,2)==1
assert kronecker(-7,3)==-1 and kronecker(-7,5)==-1

TAUS=[(Fr(1,3),Fr(2,3)),(Fr(-2,7),Fr(1,5))]

def cert_kappa(L=196):
    idx,gens=schreier(L)
    bad=0
    for g in gens:
        a,b,c,d=g
        want=kronecker(-4,d)
        for t0 in TAUS:
            P,n=J(g,t0)          # j = (-1)^n sqrt(P), so j^2 = P
            ctd=(c*t0[0]+d, c*t0[1])
            ratio=gdiv(P,ctd)
            if ratio!=(Fr(want),Fr(0)):
                bad+=1
                print('MISMATCH',g,'tau',t0,'P',P,'ctd',ctd,'ratio',ratio,'want',want,'wind',n)
                break
    return idx,len(gens),bad

print('=== [K] j^2 = chi_{-4}(d)(c tau+d) on Schreier generators of Gamma0(196) ===')
idx,ng,bad=cert_kappa(196)
print(f'index {idx}, generators {ng}, mismatches at either tau0: {bad}')
assert bad==0

print('=== [C] chi_{-7}(d) * chi_{-4}(d) == chi_28(d) for all d coprime to 196, |d|<=400 ===')
c_bad=0; checked=0
for d in range(-400,401):
    if math.gcd(d,196)==1:
        checked+=1
        v=kronecker(-7,d)*kronecker(-4,d)
        if v!=kronecker(28,d):
            c_bad+=1
            print('char mismatch d=',d,v,kronecker(28,d))
print(f'checked {checked} values, mismatches {c_bad}')
assert c_bad==0

print('=== [G] Gauss sum G(chi_{-7})^2 = -7 exactly in Z[zeta_7] ===')
# Polynomial arithmetic in Z[x]/(Phi_7), Phi_7=1+x+...+x^6, basis 1,x,...,x^5
def red(c):
    c=list(c)
    while len(c)>6:
        ak=c.pop()
        k=len(c)  # this was degree of ak; after pop, len is the degree
        # x^{len(c)} = x^{m} with m>=6: wait we popped the last coeff of degree old_len-1
        # After pop, we need to reduce x^{deg} with deg=len(c) (since 0-index)
        deg=len(c)  # degree of the term we popped is len(c)  (if c had length deg+1)
        # x^6 = -1-x-...-x^5, x^{6+r} = -x^r(1+x+...+x^5)
        r=deg-6
        need=r+6
        while len(c)<need:
            c.append(0)
        for i in range(6):
            c[r+i]-=ak
    while len(c)<6:
        c.append(0)
    if len(c)>6:
        return red(c)
    return c[:6]

def mulp(a,b):
    r=[0]*11
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            r[i+j]+=ai*bj
    return red(r)

def addp(a,b):
    return [a[i]+b[i] for i in range(6)]

G=[0]*6
for k in range(1,7):
    ch=kronecker(-7,k)
    mon=[0]*(k+1); mon[k]=ch
    G=addp(G,red(mon))
G2=mulp(G,G)
print('chi_{-7}(k) for k=1..6:', [kronecker(-7,k) for k in range(1,7)])
print('G coeffs on basis 1,zeta,...,zeta^5:', G)
print('G^2 coeffs:', G2)
print('G^2 == -7 (constant)?', G2==[-7,0,0,0,0,0])
assert G2==[-7,0,0,0,0,0]
# Record the sine identity for the sign (proved in the findings, not here):
# G = (zeta+zeta^2-zeta^3+zeta^4-zeta^5-zeta^6) = 2i(sin(2pi/7)+sin(4pi/7)-sin(6pi/7))
# and the parenthesis is positive, so the standard embedding gives +i*sqrt(7).
print('sign: findings write G = 2i(sin(2pi/7)+sin(4pi/7)-sin(6pi/7)) with positive parenthesis')

print('=== [I] float illustration of inversion (NOT a proof) ===')
import cmath
def u_series(tau, N=400):
    s=0j
    qfac=2j*math.pi
    for n in range(-N,N+1):
        if n==0:
            continue
        ch=kronecker(-7,n)
        if ch==0:
            continue
        s += ch*n*cmath.exp(qfac*n*n*tau)
    return s
def th(tt,N=400):
    s=0j
    qfac=2j*math.pi
    for n in range(-N,N+1):
        s+=cmath.exp(qfac*n*n*tt)
    return s

for tau in [0.1+0.3j, -0.2+0.25j, 0.05+0.4j]:
    lhs=u_series(-1/(196*tau))
    fac=-1j*14*math.sqrt(7)*tau*cmath.sqrt(-2j*tau)
    rhs=fac*u_series(tau)
    rel=abs(lhs-rhs)/(abs(lhs)+1e-30)
    print(f'  tau={tau}: |LHS-RHS|/|LHS|={rel:.3e}; |LHS|={abs(lhs):.6g}')

print('=== [S] float illustration of slash law (NOT a proof) ===')
idx,gens=schreier(196)
sample=[(-1,0,0,-1),(1,1,0,1),(1,-1,0,1),(13,1,-196,-15),(15,1,-196,-13),(-29,-4,196,27)]
tau=0.07+0.23j
for g in sample:
    a,b,c,d=g
    gt=(a*tau+b)/(c*tau+d)
    jv=th(gt)/th(tau)
    lhs=u_series(gt)
    rhs=kronecker(28,d)*(jv**3)*u_series(tau)
    rel=abs(lhs-rhs)/(abs(lhs)+1e-30)
    print(f'  g={g}: Im(g tau)={gt.imag:.6g}; |u(gt)-chi28(d) j^3 u|/|u(gt)|={rel:.3e}')

print('DONE; [K],[C],[G] exact and asserted.')
