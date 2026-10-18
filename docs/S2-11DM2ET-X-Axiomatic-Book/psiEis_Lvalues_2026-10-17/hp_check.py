# High-precision (32 digits) check:  psi(x) = (1/8) sum_{j even,l} e(-j/8) R_{j,l}(x)
# exact psi(x) from the Bernoulli/kappa formula re-implemented in mpmath (exact phases), R via digamma + asymptotic tail.
import mpmath as mp, math, sys
from fractions import Fraction as Fr
mp.mp.dps=34
import cypari2; pari=cypari2.Pari()
N=140; D=70
def kron(d,n): return int(pari(f'kronecker({d},{n})'))
def chi5(n,e):
    if n%5==0: return mp.mpc(0)
    return mp.mpc(1j)**(e*{1:0,2:1,4:2,3:3}[n%5])
GEN={(0,0):(0,0,0),(0,1):(0,1,0),(2,0):(3,1,0),(2,1):(3,0,0),(4,0):(2,0,0),(4,1):(2,1,0),(6,0):(1,1,0),(6,1):(1,0,0)}
def psi_val(key,n):
    e5,s4,s7=GEN[key]; return chi5(n,e5)*(kron(-4,n) if s4 else 1)*(kron(-7,n) if s7 else 1)
def chi140(n): return kron(140,n) if math.gcd(n,140)==1 else 0
class H:
    def __init__(s,key,K=80):
        s.a=[mp.mpc(0)]+[psi_val(key,n) if math.gcd(n,10)==1 else mp.mpc(0) for n in range(1,21)]
        b=[psi_val(key,r)*chi140(r) for r in range(N+1)]
        s.rho=[None]+[-mp.fsum(b[r]*mp.expjpi(mp.mpf(2*r*t)/N) for r in range(1,N+1))/(2j*mp.pi*N) for t in range(1,N+1)]
        s.K=K
        s.beta=[None]+[mp.fsum(s.rho[t]*mp.bernpoly(k,mp.mpf(t)/N) for t in range(1,N+1)) for k in range(1,K+1)]
        s.mean=mp.fsum(s.a[1:21])
    def A(s,m): return s.a[(m-1)%20+1]
    def R(s,z,M):
        val=mp.mpc(0)
        for m in range(1,M+1):
            am=s.A(m)
            if am==0: continue
            X=mp.mpf(m)/(20*z)
            val+=am*mp.fsum(s.rho[t]*mp.digamma(mp.mpf(t)/N+X) for t in range(1,N+1))
        for k in range(1,s.K+1):
            if abs(s.beta[k])<mp.mpf(10)**(-25): continue
            if k==1:
                assert abs(s.mean)<1e-25
                tail=-mp.fsum(s.a[r]*mp.digamma(mp.mpf(M)/20+mp.mpf(r)/20) for r in range(1,21))/20
            else:
                tail=mp.fsum(s.a[r]*mp.zeta(k,mp.mpf(M)/20+mp.mpf(r)/20) for r in range(1,21))/mp.mpf(20)**k
            val+=(-1)**(k+1)*s.beta[k]/k*(20*z)**k*tail
        return val
# exact kappa in mpmath
A_=((2,7),(7,7))
def B1(u): return u-mp.mpf(1)/2
def B2(u): return u*u-u+mp.mpf(1)/6
def cone_k(al,be,x):
    h,m=x.numerator,x.denominator; L=4*m; tot=mp.mpc(0)
    for which in (0,1):
        if which==0:
            u0=Fr(al[0])%1 or Fr(1); w0=Fr(al[1])%1; A11,A12,A22=mp.mpf(1),mp.mpf(7)/2,mp.mpf(7)/2
        else:
            u0=(Fr(al[1])+2*Fr(al[0]))%1 or Fr(1); w0=(-Fr(al[0]))%1; A11,A12,A22=mp.mpf(7)/2,mp.mpf(7)/2,mp.mpf(1)
        for i in range(L):
            for j in range(L):
                U=u0+i; W=w0+j
                n1,n2=(U,W) if which==0 else (-W,U+2*W)
                ph=Fr(h,m)*(n1*n1+7*n1*n2+Fr(7,2)*n2*n2)+n1*(2*be[0]+7*be[1])+n2*(7*be[0]+7*be[1])
                ph=ph%1
                su=mp.mpf(U.numerator)/U.denominator/L; sw=mp.mpf(W.numerator)/W.denominator/L
                tot+=mp.expjpi(2*mp.mpf(ph.numerator)/ph.denominator)*(B2(sw)*A12/(2*A11)+B2(su)*A12/(2*A22)+B1(su)*B1(sw))
    return tot
def comps():
    Ainv=((Fr(-1,5),Fr(1,5)),(Fr(1,5),Fr(-2,35)))
    return sorted({((Ainv[0][0]*u+Ainv[0][1]*w)%1,(Ainv[1][0]*u+Ainv[1][1]*w)%1) for u in range(35) for w in range(35)})
REPS=comps(); a=(Fr(7,10),Fr(-1,5)); ma=(Fr(-7,10),Fr(1,5)); zero=(Fr(0),Fr(0))
def psi_exact(x):
    return cone_k(a,zero,-1/x)-mp.mpf(x.numerator)/x.denominator/mp.sqrt(35)*mp.fsum(cone_k(p,ma,x) for p in REPS)
if __name__=="__main__":
    part=int(sys.argv[1]); nparts=int(sys.argv[2])
    grid=sorted({Fr(p,q) for q in range(1,9) for p in range(1,2*q+1) if Fr(1,8)<=Fr(p,q)<=2})
    grid=grid[part::nparts]
    Hs={k:H(k) for k in GEN}
    w={k:mp.expjpi(-mp.mpf(2*k[0])/8)/8 for k in GEN}
    out=[]
    for x in grid:
        M=max(140,int(math.ceil(12*20*float(x)/140))*140)
        cand=mp.fsum(w[k]*Hs[k].R(float(x) if False else mp.mpf(x.numerator)/x.denominator,M) for k in GEN)
        ex=psi_exact(x)
        out.append(f"{str(x):6s} exact={mp.nstr(ex,25)}  herglotz={mp.nstr(cand,25)}  |diff|={mp.nstr(abs(ex-cand),3)}")
        print(out[-1],flush=True)
    open(f"hp_check_{part}.txt","w").write("\n".join(out)+"\n")
