hbar=6.582119569e-16 # eV s
import math
Eb=0.100*(1-math.sqrt(2)/2); ts=hbar/Eb
o=[f"E_bind = {Eb*1e3:.2f} meV",f"tau_settle = hbar/E_bind = {ts:.3e} s = {ts*1e15:.1f} fs = {ts*1e18:.0f} as (paper: 22.5 attoseconds)",
f"tau_settle*N_eff*(1+1.3) = {ts*10*2.3*1e15:.0f} fs (paper ~234 as)",
f"Statement formula tau_echo*dE/hbarOmega = 3e-12*0.6/100 = {3e-12*0.006:.2e} s = {3e-12*0.006*1e15:.0f} fs; x10x2.3 = {3e-12*0.006*23*1e15:.0f} fs (paper ~234 as)",
f"9 Maths 21514429: floor(e^3*35) = {math.floor(math.e**3*35)} (paper 4880); 4880/e^3 = {4880/math.e**3:.3f}"]
open('verify_17thm.out','w').write("\n".join(o)); print("\n".join(o))
