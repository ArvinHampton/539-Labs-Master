# Period-integral closed form vs exact Bernoulli-sum psi on the 37 grid rationals of psi_grid.py
# plus 40 random rationals with denominators up to 60 (both signs; |x| multiplier for x<0).
import math, random
from fractions import Fraction as Fr
import psi_period as PP
from neg_side2 import psi_minus, period_minus
from fastkappa import psi as psi_exact
grid=sorted({Fr(p,q) for q in range(1,9) for p in range(1,2*q+1) if Fr(p,q)<=2 and Fr(p,q)>=Fr(1,8)})
grid=[x for x in grid if x.denominator in (1,2,3,4,5,6,7,8)]
out=[f"{len(grid)} grid rationals"]
worst=0
for x in grid:
    d=abs(psi_exact(x)-PP.psi_period(float(x),PP.D2)); worst=max(worst,d)
out.append(f"grid: max |exact - period integral| = {worst:.2e}")
random.seed(1); rs=set()
while len(rs)<40:
    q=random.randint(2,60); p=random.randint(-3*q,3*q)
    if p: rs.add(Fr(p,q))
worst=0; wn=0
for x in sorted(rs):
    if x>0: d=abs(psi_exact(x)-PP.psi_period(float(x),PP.D2))
    else: d=abs(psi_minus(x)-period_minus(float(x),PP.D2))
    worst=max(worst,d)
    if x<0: wn=max(wn,abs(psi_minus(x)-psi_exact(-x).conjugate()))
out.append(f"40 random rationals (denominators<=60, both signs): max |exact - period integral| = {worst:.2e}")
out.append(f"symmetry check psi_minus(-x) = conj(psi(x)) on the negative ones: max dev = {wn:.2e}")
print("\n".join(out)); open("psi_all.txt","w").write("\n".join(out)+"\n")
