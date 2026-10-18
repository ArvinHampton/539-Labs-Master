# psi(x) at rationals: exact Bernoulli/kappa value vs the Herglotz (Eisenstein) closed form.  s=8: full agreement expected;
# s=11: the difference is psi_cusp(x) (the non-Eisenstein part of the cocycle at the rational boundary point).
import sys, math
from fractions import Fraction as Fr
from kappa_s import Kappa
import herg_s
s=int(sys.argv[1]); K=Kappa(s); S,terms=herg_s.build(s,verbose=False); HE=herg_s.herglotz_eis(S,terms)
xs=[Fr(1),Fr(2),Fr(1,2),Fr(1,3),Fr(3,2),Fr(2,3),Fr(3,4),Fr(5,3)]
lines=[]
for x in xs:
    ex=K.psi(x); he=HE(float(x))
    lines.append(f"s={s} x={x}: psi_exact(kappa)={ex:.13f}  Herglotz_Eis={he:.13f}  diff={ex-he:.13f} |diff|={abs(ex-he):.2e}")
    print(lines[-1],flush=True)
open(f"rational_check_{s}.txt","w").write("\n".join(lines)+"\n")
