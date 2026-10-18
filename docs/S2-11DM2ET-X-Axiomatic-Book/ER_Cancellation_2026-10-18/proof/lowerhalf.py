# Continuation check off H: the Green-form period formula (A3 of the psi-Cocycle report, split-path form)
#   Psi(z) = -(1/pi)[ (z/sqrt35)(log eps/2 - J_R(z)) + J_L(-1/z) ]
# evaluated at points with Re z > 0, Im z < 0 (where the q-series do not converge), vs the Herglotz form 2 sum_chi w_chi R_chi(z).
import sys, math, cmath
sys.path.insert(0,'../2026-10-17-psi-cocycle')
import os; here=os.getcwd(); os.chdir('../2026-10-17-psi-cocycle')
import psi_period as P
os.chdir(here)
from herglotz import Herg, GEN
H={k:Herg(k) for k in GEN}; w={k:cmath.exp(-2j*math.pi*k[0]/8)/8 for k in GEN}
out=[]
for z in [1-0.3j, 0.7-0.6j, 2-1j, 1.5+0.4j, 3-2.5j, 0.4-0.1j]:
    p1=P.psi_period(z,P.D1); p2=P.psi_period(z,P.D2)
    r=sum(w[k]*H[k].R(z) for k in GEN)
    out.append(f"z={z}: period formula={p2:.12f} (quad. change {abs(p1-p2):.0e})  Herglotz={r:.12f}  |diff|={abs(p2-r):.1e}")
    print(out[-1],flush=True)
open("lowerhalf.txt","w").write("\n".join(out)+"\n")
