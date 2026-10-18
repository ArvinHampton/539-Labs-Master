# Cat B cross-checks of R4 ingredients against exact data (d <= 40000), and of the local CLT at n=900 (float).
import math, numpy as np
from tails import _phi1f, argmin_u
D=40000; M=D//7+1; nmax=math.isqrt(D)
import bisect
AG=[i/400 for i in range(1,401)]; UG=[argmin_u(a) for a in AG]; PG=[_phi1f(x) for x in UG]
p=[1]+[0]*M; worst=-1e9; worstT2=1e9; cnt=0
for n in range(1,nmax+1):
    for m in range(n,M+1): p[m]-=p[m-n]
    # T1/T2 at several u
    for u in (0.3,0.6,1.0,2.0):
        t=u/n; r=math.exp(-t)
        logA=sum(math.log1p(r**j) for j in range(1,n+1,2))+sum(-math.log1p(-r**(2*k)) for k in range(n//2+1,n+1))
        g=-math.log1p(-math.exp(-u)); P=n*_phi1f(u,2000)
        assert P-0.5*math.log(2)-g-1e-9 <= logA <= P+math.log(2)+g+1e-9, (n,u)
    for m in range(0,(D-n*n)//7+1):
        a=abs(p[m]);
        if a==0: continue
        d=n*n+7*m; al=n/math.sqrt(d); i=min(399,max(0,round(al*400)-1)); u=UG[i]
        F=al*PG[i]+(1-al*al)*u/(7*al)
        bound=math.sqrt(d)*F+math.log(2)-math.log1p(-math.exp(-u))
        worst=max(worst, math.log(a)-bound); cnt+=1
    if n%50==0: print('n',n,'max(log a - Chernoff bound) so far',worst,flush=True)
print('T1/T2 hold for n<=200, u in {0.3,0.6,1,2}; Chernoff+T1 max excess (must be <=0):',worst,'over',cnt,'coefficients')
# local CLT at n=900, u=0.6 (float, tilted DP)
n=900;u=0.6;t=u/n;Mx=int(0.9*n*n)
P=np.zeros(Mx+1);P[0]=1
for j in range(1,n+1,2):
    q=1/(1+math.exp(j*t)); Q=P*(1-q); Q[j:]+=P[:-j]*q; P=Q
for k in range(n//2+1,n+1):
    w=math.exp(-2*k*t); s=2*k; Q=(1-w)*P
    for b in range(s,Mx+1,s): Q[b:b+s]+=w*Q[b-s:b][:len(Q[b:b+s])]
    P=Q
from clt import constants
idx=np.arange(Mx+1); mu=(idx*P).sum(); var=((idx-mu)**2*P).sum(); print('mass',P.sum(),'mu/n^2',mu/n**2,'var/n^3',var/n**3)
C=constants(u,u,900,0.5); print('rigorous M',C['M_lo'],C['M_hi'],'S',C['S_lo'],C['S_hi'])
gx=np.exp(-(idx-mu)**2/(2*var))/math.sqrt(2*math.pi*var)
print('local CLT n=900 u=0.6: max|P-g|*sqrt(2pi)sigma =',np.abs(P-gx).max()*math.sqrt(2*math.pi*var),' rigorous delta bound ~0.15')
