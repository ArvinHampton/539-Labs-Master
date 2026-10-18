# Lemma A at 34 digits for the trivial genus character (mean of a != 0, the delicate case) and one odd character
import mpmath as mp, math
from hp_check import H, GEN, psi_val, chi140
mp.mp.dps=34
out=[]
for key in [(0,0),(4,1)]:
    h=H(key)
    a=[psi_val(key,r) if math.gcd(r,10)==1 else 0 for r in range(20)]; b=[psi_val(key,r)*chi140(r) for r in range(140)]
    ach=[mp.fsum(a[r]*mp.expjpi(mp.mpf(2*k*r)/20) for r in range(20)) for k in range(20)]
    bh=[mp.fsum(b[r]*mp.expjpi(mp.mpf(2*n*r)/140) for r in range(140)) for n in range(140)]
    for z in [mp.mpc(0.6,0.45), mp.mpc(1.0,0.9)]:
        tau=-1/(20*z); NG=int(80/(2*math.pi*float(tau.imag)))+1; NT=int(80/(2*math.pi*float(z.imag)/140))+1
        lam=[mp.mpc(0)]*(NG+1)
        for m in range(1,NG+1):
            if a[m%20]==0: continue
            for k in range(1,NG//m+1): lam[m*k]+=a[m%20]*b[k%140]
        Gv=mp.fsum(lam[n]*mp.exp(2j*mp.pi*n*tau) for n in range(1,NG+1))
        cT=[mp.mpc(0)]*(NT+1)
        for n in range(1,NT+1):
            for k in range(1,NT//n+1): cT[n*k]+=bh[n%140]*ach[k%20]
        q=mp.exp(2j*mp.pi*z/140)
        Tv=z/140*mp.polyval(cT[::-1],q)
        Rv=h.R(z,420)
        out.append(f"chi{key} z={mp.nstr(z,3)}: G(-1/20z)={mp.nstr(Gv,18)}  2R+T={mp.nstr(2*Rv+Tv,18)}  |diff|={mp.nstr(abs(Gv-2*Rv-Tv),3)}")
        print(out[-1],flush=True)
open("lemmaA_hp.txt","w").write("\n".join(out)+"\n")
