import mpmath as mp, cmath, math
from hp_check import H, GEN
from complex_check import Psi
Hs={k:H(k) for k in GEN}; w={k:mp.expjpi(-mp.mpf(2*k[0])/8)/8 for k in GEN}
out=[]
for z in [1+0.6j,2+1j]:
    r=mp.fsum(w[k]*Hs[k].R(mp.mpc(z),420) for k in GEN); p=Psi(z)
    out.append(f"z={z}: Psi(q-series, double)={p:.15f}  Herglotz(34 digits)={mp.nstr(r,20)}  |diff|={abs(p-complex(r)):.1e}")
    print(out[-1],flush=True)
open("complex_hp.txt","w").write("\n".join(out)+"\n")
