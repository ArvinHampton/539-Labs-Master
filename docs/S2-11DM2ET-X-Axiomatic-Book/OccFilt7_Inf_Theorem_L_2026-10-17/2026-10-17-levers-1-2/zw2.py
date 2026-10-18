import numpy as np
from math import erf,sqrt,pi
from fractions import Fraction as Fr
A=np.array([[2,7],[7,7]],float); Ai=np.linalg.inv(A)
c1=Ai@np.array([1,0]); c2=-Ai@np.array([0,1])
Q=lambda v:0.5*v@A@v; B=lambda u,v:u@A@v
def E(x): return erf(sqrt(pi)*x)
def theta(a,b,t,R):
    s=0j
    for n in range(-R,R+1):
        for k in range(-R,R+1):
            nu=np.array([n,k],float)+a
            rho=E(B(c1,nu)*sqrt(t)/sqrt(-Q(c1)))-E(B(c2,nu)*sqrt(t)/sqrt(-Q(c2)))
            if rho: s+=rho*np.exp(-2*pi*Q(nu)*t+2j*pi*B(nu,b))
    return s
reps={(Fr(7*i-7*j,-35)%1, Fr(-7*i+2*j,-35)%1) for i in range(35) for j in range(35)}
print("exact classes:",len(reps))
a=np.array([-0.7,0.2]); b0=np.zeros(2)
for t,R in ((1.0,45),(1.0,90),(1.3,90)):
    lhs=theta(a,b0,1/t,R)
    rhs=1j/sqrt(35)*t*sum(theta(np.array([float(x),float(y)]),-a,t,R) for x,y in reps)
    print(f"t={t}: LHS={lhs.real:.14f} RHS={rhs.real:+.14f} imag={rhs.imag:.1e} diff={abs(lhs-rhs):.1e}")
