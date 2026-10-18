import numpy as np
from math import erf,sqrt,pi
from fractions import Fraction as Fr
A=np.array([[2,7],[7,7]],float); Ai=np.linalg.inv(A)
c1=Ai@np.array([1,0]); c2=-Ai@np.array([0,1])
Q=lambda v:0.5*v@A@v; B=lambda u,v:u@A@v
print("c1",c1,"c2",c2,"Q(c1)",Q(c1),"Q(c2)",Q(c2),"B(c1,c2)",B(c1,c2))
# (i) holomorphic part identity, exact integers
M=400
def Qm(n,k): return n*n+7*n*k+(7*k*(k-1))//2
H=[0]*M; Ct=[0]*M; F=[0]*M; th=[0]*M
for n in range(-80,80):
    for k in range(-80,80):
        w=(1 if n>=1 else -1)+(1 if k>=0 else -1)
        if w==0: continue
        e=Qm(n,k)
        assert e>=0
        if e<M: H[e]+=w//2
        if n>=1 and k>=1 and e<M: Ct[e]+=1
for r in range(-80,80):
    for s in range(-80,80):
        if (r>=0)!=(s>=0): continue
        e=8+r*(r-1)+7*r*s+7*s*(s-1)//2+10*r+14*s
        if e<M: F[e]+=1 if r>=0 else -1
for n in range(-30,30):
    if n*n<M: th[n*n]+=1
print("Zwegers holomorphic sum == q^8 f_{2,7,7}(-q^10,-q^14,q) + theta3(q) to q^399:",H==[a+b for a,b in zip(F,th)])
# (ii) Cor 2.9(5) numeric check of completed theta at tau=i t
def E(x): return erf(sqrt(pi)*x)
def theta(a,b,t,R=40):
    y=t; s=0j
    for n in range(-R,R+1):
        for k in range(-R,R+1):
            nu=np.array([n,k],float)+a
            rho=E(B(c1,nu)*sqrt(y)/sqrt(-Q(c1)))-E(B(c2,nu)*sqrt(y)/sqrt(-Q(c2)))
            if rho==0: continue
            s+=rho*np.exp(-2*pi*Q(nu)*y+2j*pi*B(nu,b))
    return s
a=np.array([-0.7,0.2]); b0=np.zeros(2)
reps=[]
for i in range(35):
    for j in range(35):
        p=(Ai@np.array([i,j]))%1.0
        if not any(np.allclose(p,q2) for q2 in reps): reps.append(p)
print("classes A^-1Z^2/Z^2:",len(reps))
for t in (0.9,1.3):
    lhs=theta(a,b0,1/t)          # tau=i t -> -1/tau = i/t
    rhs=1j/sqrt(35)*t*sum(theta(p,-a,t) for p in reps)   # (-i tau)^{r/2}=t
    print(f"t={t}: theta_a,0(-1/tau)={lhs:.12f}  RHS={rhs:.12f}")
