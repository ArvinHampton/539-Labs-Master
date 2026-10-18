from collections import defaultdict
N=501
def mul(a,b,n=N):
    c=[0]*n
    for i,x in enumerate(a[:n]):
        if x:
            for j in range(n-i):
                if b[j]: c[i+j]+=x*b[j]
    return c
def inv(a,n=N):
    b=[0]*n; b[0]=1
    for k in range(1,n): b[k]=-sum(a[i]*b[k-i] for i in range(1,k+1) if a[i])
    return b
def poch(n,base,sign,M=N):
    r=[1]+[0]*(M-1)
    for j in range(1,n+1):
        f=[1]+[0]*(M-1)
        if base*j<M: f[base*j]+=sign
        r=mul(r,f,M)
    return r
def g(s,M):
    out=[0]*M; n=0
    while n*n<M:
        t=inv(poch(n,s,+1,M),M)
        for i in range(M-n*n): out[n*n+i]+=t[i]
        n+=1
    return out
# --- Calibration s=1: HM (0.3)
M=201
lhs=mul(g(1,M),poch(400,1,-1,M),M)  # (q)_inf truncated
rhs=[0]*M
n=0
while (5*n*n+n)//2-n*n<M:
    for j in range(-n,n+1):
        e=(5*n*n+n)//2-j*j
        for ee,sg in ((e,1),(e+4*n+2,-1)):
            if 0<=ee<M: rhs[ee]+=sg*(-1)**j
    n+=1
print("s=1 HM(0.3) match to q^200:",lhs==rhs)
# --- Calibration s=2: HM (4.5) phi(q)=2m(q,-q^3,-1)+2q J12^3/(J4 J_{3,12})
# m(x,Q,z)=1/j(z;Q) sum_r (-1)^r Q^{C(r,2)} z^r/(1-Q^{r-1}xz); x=q,Q=-q^3,z=-1
def Qpow(e): # (-q^3)^e -> (sign, qexp)
    return ((-1)**e, 3*e)
S=defaultdict(int)
for r in range(-40,41):
    sg,ex=Qpow(r*(r-1)//2)  # (-1)^r z^r = 1
    # 1/(1+Q^{r-1} q)
    us,ue=Qpow(r-1); ue+=1
    if ue>0:
        for k in range(0,M):
            if ex+k*ue>=M: break
            S[ex+k*ue]+=sg*((-us)**k)
    else:  # 1/(1+u)=sum_{k>=1}(-1)^{k-1}u^{-k}
        for k in range(1,M):
            e2=ex-k*ue
            if e2>=M: break
            S[e2]+=sg*((-1)**(k-1))*(us**k)
assert min(S)>=0
Sser=[S[i] for i in range(M)]
# j(-1;Q)=sum (-1)^n Q^{C(n,2)} (-1)^n = sum Q^{C(n,2)}
jz=[0]*M
for r in range(-40,41):
    sg,ex=Qpow(r*(r-1)//2)
    if ex<M: jz[ex]+=sg
mser=mul(Sser,inv(jz,M),M)
def J(a,m,M):  # j(q^a;q^m) as series via triple product sum
    s=[0]*M
    for nn in range(-60,61):
        e=m*nn*(nn-1)//2+a*nn
        if 0<=e<M: s[e]+=(-1)**nn
    return s
J12=poch(400,12,-1,M); J4=poch(400,4,-1,M)
th=mul(mul(mul(J12,J12,M),J12,M),inv(mul(J4,J(3,12,M),M),M),M)
phi=[2*x for x in mser]
for i in range(M-1): phi[i+1]+=2*th[i]
print("s=2 HM(4.5) match to q^200:",phi==g(2,M))
# s=2 Bailey alpha closed form check printed elsewhere
# --- Lever 2: C_third
M=501
def Qm(n,k): return n*n+7*n*k+(7*k*(k-1))//2
Ct=[0]*M
for n in range(1,M):
    for k in range(1,M):
        e=Qm(n,k)
        if e>=M: break
        Ct[e]+=1
print("C_third first degrees:",[i for i,x in enumerate(Ct) if x][:12])
# HM f_{a,b,c}(x,y,q)=sum_{sg r=sg s} sg(r)(-1)^{r+s}x^r y^s q^{aC(r,2)+brs+cC(s,2)}
def f(a,b,c,xe,xs,ye,ys,M,R=80):
    out=[0]*(M+50); 
    for r in range(-R,R):
        for s_ in range(-R,R):
            if (r>=0)!=(s_>=0): continue
            e=a*r*(r-1)//2+b*r*s_+c*s_*(s_-1)//2+xe*r+ye*s_
            if 0<=e<M+50:
                out[e]+=(1 if r>=0 else -1)*(-1)**(r+s_)*xs**(r%2 if xs==-1 else 1)*ys**(s_%2 if ys==-1 else 1)
            elif e<0: raise Exception("neg exp")
    return out
F=f(2,7,7,10,-1,14,-1,M)
lhs=[0]*M
for i in range(M-8): lhs[i+8]=F[i]
Pp=[0]*M
for n in range(0,M):
    for k in range(0,M):
        e=n*n+7*n*k+7*k*(k+1)//2
        if e>=M: break
        Pp[e]+=1
print("q^8 f_{2,7,7}(-q^10,-q^14,q) == C_third - sum_{n,k>=0} q^{Q_plus} to q^500:",lhs==[a-b for a,b in zip(Ct,Pp)])
