# Twisted Herglotz functions R_chi(z) = sum_{m>=1} a(m) sum_{s=1}^{N} rho_s * digamma(s/N + m/(20 z)),
# from the Mittag-Leffler expansion of the Lambert series G_chi(tau)=sum_{m,k} a(m) b(k) e(mk tau) at tau=-1/(20z).
import numpy as np, math, cmath
from scipy.special import digamma, zeta as hzeta, bernoulli
import cypari2; pari=cypari2.Pari()
N=140
def kron(d,n): return int(pari(f'kronecker({d},{n})'))
def chi5(n,e):
    if n%5==0: return 0
    return 1j**(e*{1:0,2:1,4:2,3:3}[n%5])
GEN={(0,0):(0,0,0),(0,1):(0,1,0),(2,0):(3,1,0),(2,1):(3,0,0),(4,0):(2,0,0),(4,1):(2,1,0),(6,0):(1,1,0),(6,1):(1,0,0)}
def psi_fn(e5,s4,s7):
    return lambda n: chi5(n,e5)*(kron(-4,n) if s4 else 1)*(kron(-7,n) if s7 else 1)
def chi140(n): return kron(140,n) if math.gcd(n,140)==1 else 0
from scipy.special import bernoulli as _b
import sympy
def Bpoly(k,x): return float(sympy.bernoulli(k,x))
class Herg:
    def __init__(s,key,swap=False):
        ps=psi_fn(*GEN[key])
        A=lambda n: ps(n) if math.gcd(n,10)==1 else 0
        B=lambda n: ps(n)*chi140(n)
        if swap: A,B=B,A
        s.Mod=140 if swap else 20
        s.a=np.array([A(n) for n in range(0,4001)],complex)
        b=np.array([B(r) for r in range(0,N+1)],complex)
        r=np.arange(1,N+1)
        s.rho=np.array([-(b[1:]*np.exp(2j*np.pi*r*t/N)).sum()/(2j*math.pi*N) for t in range(1,N+1)])
        s.sN=np.arange(1,N+1)/N
        s.K=14
        s.beta=[None]+[sum(s.rho[t-1]*Bpoly(k,sympy.Rational(t,N)) for t in range(1,N+1)) for k in range(1,s.K+1)]
        Mo=s.Mod; ar=np.array([s.a[r] for r in range(1,Mo+1)])
        s.L={}
        for k in range(1,s.K+1):
            if k==1:
                s.L[1]=-(ar*digamma(np.arange(1,Mo+1)/Mo)).sum()/Mo if abs(ar.sum())<1e-12 else None
            else:
                s.L[k]=(ar*hzeta(k,np.arange(1,Mo+1)/Mo)).sum()/Mo**k
    def f(s,X):   # complex X allowed? scipy digamma supports complex
        return (s.rho[None,:]*digamma(s.sN[None,:]+X[:,None])).sum(1)
    def R(s,z,M=3000):
        m=np.arange(1,M+1); X=m/(20*z)
        val=(s.a[1:M+1]*s.f(X.astype(complex))).sum()
        Mo=s.Mod; assert M%Mo==0; ar=np.array([s.a[r] for r in range(1,Mo+1)]); rr=np.arange(1,Mo+1)
        for k in range(1,s.K+1):
            if abs(s.beta[k])<1e-10: continue
            if k==1:
                if abs(ar.sum())>1e-12: raise ValueError("divergent k=1")
                tail=-(ar*digamma(M/Mo+rr/Mo)).sum()/Mo
            else:
                tail=(ar*hzeta(k,M/Mo+rr/Mo)).sum()/Mo**k
            val+=(-1)**(k+1)*s.beta[k]/k*(20*z)**k*tail
        return val
if __name__=="__main__":
    import fastkappa
    from fractions import Fraction as Fr
    H={k:Herg(k) for k in GEN}
    w={k:cmath.exp(-2j*math.pi*k[0]/8)/16 for k in GEN}
    for x in [Fr(1),Fr(1,3),Fr(2),Fr(3,5),Fr(7,4)]:
        ex=fastkappa.psi(x)
        cand=sum(2*w[k]*H[k].R(float(x)) for k in GEN)
        print(x, ex, cand, ex-cand)
