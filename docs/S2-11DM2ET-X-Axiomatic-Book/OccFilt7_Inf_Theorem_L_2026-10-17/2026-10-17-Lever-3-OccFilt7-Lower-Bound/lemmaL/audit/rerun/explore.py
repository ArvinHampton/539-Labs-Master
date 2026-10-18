# float exploration (Cat B): limit functions in u
import mpmath as mp
def lim(u):
    I=lambda f,a,b: mp.quad(f,[a,b])
    M=(I(lambda x:x/(mp.e**x+1),0,u)+I(lambda x:x/(mp.e**x-1),u,2*u))/(2*u**2)
    s2=(I(lambda x:x**2*mp.e**x/(mp.e**x+1)**2,0,u)+I(lambda x:x**2*mp.e**x/(mp.e**x-1)**2,u,2*u))/(2*u**3)
    sB=I(lambda x:x**2*mp.e**x/(mp.e**x+1)**2,0,u)/(2*u**3)
    # K3 crude (theta0->0): sum j^3 p(1-p)(1-2p) + sum (2k)^3 w(1+w)/(1-w)^3
    k3=(I(lambda x:x**3*mp.e**x*(mp.e**x-1)/(mp.e**x+1)**3,0,u)+I(lambda x:x**3*mp.e**x*(mp.e**x+1)/(mp.e**x-1)**3,u,2*u))/(2*u**4)
    rho=M; alpha=1/mp.sqrt(1+7*rho)
    return rho,alpha,s2,sB,k3, k3/s2**1.5
print(' u    rho    alpha   s2     sB     k3   k3/s2^1.5 (=> K3/sigma^3 ~ this/sqrt(n))')
for u in [0.02,0.05,0.1,0.2,0.3,0.5,0.611,0.8,1,1.5,2,3,4,6]:
    print(u,[mp.nstr(v,4) for v in lim(mp.mpf(u))])
