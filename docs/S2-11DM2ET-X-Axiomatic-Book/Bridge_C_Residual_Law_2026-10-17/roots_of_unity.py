# Radial behaviour at q = e^{2 pi i x} e^{-t}: predicted leading term G(x) I / t versus direct sums,
# and comparison with Master's 'sample markers' (rho = 0.995).
import numpy as np, math, cmath
from fractions import Fraction as Fr
I = math.log(6+math.sqrt(35))/(2*math.sqrt(35))
def W(which, n, k):
    sg=np.sign
    if which=="P":  return ((n>=0)&(k>=0)).astype(float)
    if which=="H":  return 0.5*(sg(5*n)-sg(-n-21*k))
    if which=="C":  return ((n>=0)&(k>=0)).astype(float)-0.5*(sg(5*n)-sg(-n-21*k))
    if which=="Ct": return ((n<=-1)&(k<=-1)).astype(float)
def radial(which, x, t):
    nmax=int(math.sqrt(60/t))+5
    n=np.arange(-nmax,nmax+1)[:,None].astype(float); k=np.arange(-nmax,nmax+1)[None,:].astype(float)
    Q=n*n+7*n*k+3.5*k*(k+1); w=W(which,n,k); Q=np.where(w!=0,Q,0.0)
    # Q is an integer; reduce phase exactly
    ph=np.exp(2j*math.pi*((Q*x.numerator) % x.denominator)/x.denominator)
    return complex((w*ph*np.exp(-t*Q)).sum())
def G(x):
    m=x.denominator; L=2*m
    s=0
    for n in range(L):
        for k in range(L):
            Q=n*n+7*n*k+7*k*(k+1)//2
            s+=cmath.exp(2j*math.pi*(Q*x.numerator % m)/m)
    return s/L**2
samples={Fr(1,7):-18.2+7.8j, Fr(3,7):0.3-1.8j, Fr(5,7):2.1-9.0j, Fr(1,1):20.7+2.9j}
rho=0.995; t0=-math.log(rho)
print(f"I = {I:.15f};  rho = 0.995 -> t = {t0:.7f};  I/t = {I/t0:.4f}\n")
print("x     G(x) (exact mean of e(xQ_s))      G*I/t at rho      C(rho e(x)) direct        C_third(rho e(x))       Master sample   |sample|")
for x,smp in samples.items():
    g=G(x); c=radial("C",x,t0); ct=radial("Ct",x,t0)
    print(f"{str(x):5} {g.real:+.6f}{g.imag:+.6f}i   {abs(g*I/t0):8.3f}   {c.real:+9.3f}{c.imag:+9.3f}i   {ct.real:+9.3f}{ct.imag:+9.3f}i   {smp}  {abs(smp):6.2f}")
print("\nConvergence of t*C(e(x)e^{-t}) to G(x)*I (C, C_third, H_s):")
for x in samples:
    g=G(x)
    for t in [0.01,0.0025,0.000625]:
        c=radial("C",x,t); ct=radial("Ct",x,t); h=radial("H",x,t)
        print(f" x={str(x):4} t={t:<9} t*C={t*c:.5f}  t*C_third={t*ct:.5f}  t*H_s={t*h:.5f}   G*I={g*I:.5f}")
print("\nGauss-sum check: for x=h/7, G = (h/7) i/sqrt7 :", [(h, G(Fr(h,7)), 1j/math.sqrt(7)) for h in (1,3,5)])
