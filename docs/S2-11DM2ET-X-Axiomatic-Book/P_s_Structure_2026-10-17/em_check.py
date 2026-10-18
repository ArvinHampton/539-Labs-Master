# Numerical check of the analytic EM coefficients: remainder r(t) = S(t) - c_{-2}/t - c_{-1}/sqrt t - c_0 should be O(sqrt t).
import numpy as np, math
import mpmath as mp
from em import res
I = float(mp.log(6+mp.sqrt(35))/(2*mp.sqrt(35)))
def grid(t):
    nmax=int(math.sqrt(80/t))+5
    n=np.arange(-nmax,nmax+1,dtype=np.float64)[:,None]; k=np.arange(-nmax,nmax+1,dtype=np.float64)[None,:]
    return n,k
def series(which,t):
    n,k=grid(t); sg=np.sign
    Qs=n*n+7*n*k+3.5*k*(k+1)
    if which=="P_s": W=((n>=0)&(k>=0))
    elif which=="R": W=((n>=0)&(k>=1))
    elif which=="C_third": W=((n<=-1)&(k<=-1))
    elif which=="E": W=((n>=0)&(k>=1))|((n<=-1)&(k<=0))
    elif which=="H_s": W=0.5*(sg(5*n)-sg(-n-21*k))
    elif which=="C": W=((n>=0)&(k>=0)).astype(float)-0.5*(sg(5*n)-sg(-n-21*k))
    W=np.asarray(W,dtype=np.float64); Q=np.where(W!=0,Qs,0.0)
    return float(np.sum(W*np.exp(-t*Q)))
lines=[]
for which in ["P_s","R","C_third","E","H_s","C"]:
    c=[float(v) for v in res[which]]
    lines.append(f"{which}: analytic (t^-1, t^-1/2, t^0) = ({c[0]:.12f}, {c[1]:.12f}, {c[2]:.12f})")
    for t in [1e-2,1e-3,1e-4,2.5e-5]:
        s=series(which,t); r=s-c[0]/t-c[1]/math.sqrt(t)-c[2]
        lines.append(f"   t={t:<8g} S={s:.10f}  remainder r={r:+.3e}  r/sqrt(t)={r/math.sqrt(t):+.5f}")
print("\n".join(lines)); open("em_check.txt","w").write("\n".join(lines)+"\n")
