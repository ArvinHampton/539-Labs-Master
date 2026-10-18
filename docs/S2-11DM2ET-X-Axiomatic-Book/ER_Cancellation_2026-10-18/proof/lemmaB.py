# Lemma B (E_R in closed form): coefficient of q^{N/140} in E_R equals (sqrt35/140) sum_chi w_chi sum_{nk=N} bhat(n) acheck(k)
import numpy as np, math, cmath, sys
from collections import defaultdict
import uvec
from herglotz import GEN, psi_fn, chi140
from family import G
e1=(1,0); ge1=tuple(G@np.array(e1))
ma70=(-49,14)
reps=sorted({((-14*u+14*w)%70,(14*u-4*w)%70) for u in range(35) for w in range(35)})
Qmax=float(sys.argv[1]) if len(sys.argv)>1 else 25; Bx=int(sys.argv[2]) if len(sys.argv)>2 else 250
coef=defaultdict(complex)
for p in reps:
    q,ph=uvec.cone_pts(np.array(p),np.array(ma70),e1,ge1,1,Qmax,Bx=Bx)
    for N,v in zip(np.rint(140*q).astype(np.int64),ph):
        assert abs(140*q[0]-round(140*q[0]))<1e-9
        coef[int(N)]+=v
Nmax=int(140*Qmax)
# formula
form=np.zeros(Nmax+1,complex)
for key in GEN:
    ps=psi_fn(*GEN[key]); w=cmath.exp(-2j*math.pi*key[0]/8)/16
    a=[ps(r) if math.gcd(r,10)==1 else 0 for r in range(20)]
    b=[ps(r)*chi140(r) for r in range(140)]
    ach=[sum(a[r]*cmath.exp(2j*math.pi*k*r/20) for r in range(20)) for k in range(20)]
    bh=[sum(b[r]*cmath.exp(2j*math.pi*n*r/140) for r in range(140)) for n in range(140)]
    for n in range(1,Nmax+1):
        for k in range(1,Nmax//n+1):
            form[n*k]+=w*bh[n%140]*ach[k%20]
form*=math.sqrt(35)/140
dev=max(abs(coef.get(N,0)-form[N]) for N in range(1,Nmax+1))
nz=sum(1 for N in range(1,Nmax+1) if abs(form[N])>1e-9)
maximag=max(abs(form[N].imag) for N in range(1,Nmax+1))
out=[f"Qmax={Qmax} (N<= {Nmax}), Bx={Bx}: max|c_R(N/140) - formula| = {dev:.2e};  nonzero coefficients: {nz};  max|Im formula| = {maximag:.1e}",
     ]
first=[(N,coef.get(N,0),form[N]) for N in range(1,Nmax+1) if abs(form[N])>1e-9 or abs(coef.get(N,0))>1e-9][:15]
out.append("first nonzero (N, c_R(N/140), formula): "+"; ".join(f"{N}: {c.real:+.10f}{c.imag:+.1e}i | {f.real:+.10f}{f.imag:+.1e}i" for N,c,f in first))
print("\n".join(out)); open(f"lemmaB_Q{int(Qmax)}.txt","w").write("\n".join(out)+"\n")
