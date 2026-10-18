# Lemma A, per genus character chi:  G_chi(-1/(20z)) - 2 R_chi(z) = T_chi(z) = (z/140) sum_{n,k>=1} bhat(n) acheck(k) e(nkz/140),  z in H
import numpy as np, math, cmath
from herglotz import Herg, GEN, psi_fn, chi140
zs=[0.3+0.5j, 0.6+0.45j, 0.2+0.8j, 1.0+0.9j]
out=[]
for key in GEN:
    ps=psi_fn(*GEN[key]); H=Herg(key)
    a=np.array([ps(r) if math.gcd(r,10)==1 else 0 for r in range(20)]); b=np.array([ps(r)*chi140(r) for r in range(140)])
    ach=np.array([sum(a[r]*cmath.exp(2j*math.pi*k*r/20) for r in range(20)) for k in range(20)])
    bh=np.array([sum(b[r]*cmath.exp(2j*math.pi*n*r/140) for r in range(140)) for n in range(140)])
    Nm=60000
    lam=np.zeros(Nm+1,complex); cT=np.zeros(Nm+1,complex)
    for m in range(1,Nm+1):
        if a[m%20]!=0: lam[m::m][:Nm//m]+=a[m%20]*b[(np.arange(1,Nm//m+1))%140]
    for n in range(1,Nm+1):
        cT[n::n][:Nm//n]+=bh[n%140]*ach[(np.arange(1,Nm//n+1))%20]
    N=np.arange(Nm+1)
    worst=0
    for z in zs:
        tau=-1/(20*z)
        Gv=(lam*np.exp(2j*np.pi*N*tau)).sum()
        Tv=z/140*(cT*np.exp(2j*np.pi*N*z/140)).sum()
        Rv=H.R(z,M=3000)
        worst=max(worst,abs(Gv-2*Rv-Tv))
    out.append(f"chi{key} psi={GEN[key]}: sum_r a(r)={a.sum().real:+.0f}, parity={'even' if ps(19)==1 else 'odd'}: max_z |G(-1/20z) - 2R(z) - T(z)| = {worst:.2e}   (|T| at z0 = {abs(Tv):.3e})")
    print(out[-1],flush=True)
open("lemmaA.txt","w").write("Lemma A check at z = "+str(zs)+" (double precision; Herglotz floor ~1e-12)\n"+"\n".join(out)+"\n")
