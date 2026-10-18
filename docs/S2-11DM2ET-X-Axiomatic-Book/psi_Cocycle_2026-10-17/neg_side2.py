# Negative axis: the multiplier must be |x| (Siegel-theta weight (1/2,1/2)), not x.
#   psi_minus(x) := kappa_L(-1/x) - (|x|/sqrt35) sum_p kappa_{p,-a}(x),  x<0
# compared with  Psi^-(z) = E_L(-1/z) + K z E_R(z)  (q-series, y->0) and with the period formula with x -> |x| prefactor.
import math, numpy as np
from fractions import Fraction as Fr
from lz_continuation import Psi
from fastkappa import cone_terms, REPS, a, ma, zero
import psi_period as PP
def psi_minus(x):
    x=Fr(x); kL=cone_terms(a,zero,-1/x)[1]; sk=sum(cone_terms(p,ma,x)[1] for p in REPS)
    return kL-abs(float(x))/math.sqrt(35)*sk
def period_minus(x,D):
    t,wts,TL,TR=D
    return -(1/math.pi)*((abs(x)/math.sqrt(35))*(PP.LOGEPS/2-PP.J(TR,t,wts,x))+PP.J(TL,t,wts,-1/x))
out=[]
for x in (Fr(-1),Fr(-2,5),Fr(-13,4),Fr(-3,7),Fr(-55,89)):
    ex=psi_minus(x); pm=period_minus(float(x),PP.D2)
    qs=[Psi(complex(float(x),y),-1/math.sqrt(35)) for y in (0.05,0.025)]
    out.append(f"x={str(x):7}: psi_minus exact={ex:.13f}  period(|x|)={pm:.13f}  |diff|={abs(ex-pm):.1e}   Psi^-(x+iy), y=.05,.025: {qs[0]:.6f} {qs[1]:.6f}")
print("\n".join(out)); open("neg_side2.txt","w").write("\n".join(out)+"\n")
