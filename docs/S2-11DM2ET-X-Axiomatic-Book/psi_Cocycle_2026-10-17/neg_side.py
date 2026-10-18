# Which object is psi at negative x?  Compare Psi(x+iy) (q-series) as y->0 with the exact constant-term psi(x),
# and with the period formula evaluated at complex z (z in H).
import math, numpy as np
from fractions import Fraction as Fr
from lz_continuation import Psi
from fastkappa import psi as psi_exact
import psi_period as PP
K=1/math.sqrt(35)
out=[]
for x in (-1.0,-0.4,1.0):
    out.append(f"x={x}: exact constant-term psi = {psi_exact(Fr(x).limit_denominator(10)):.8f}")
    for y in (0.1,0.05,0.025):
        z=complex(x,y)
        out.append(f"   y={y}: Psi(z) q-series = {Psi(z,K):.8f}   period formula at complex z = {PP.psi_period(z,PP.D2):.8f}")
print("\n".join(out)); open("neg_side.txt","w").write("\n".join(out)+"\n")
