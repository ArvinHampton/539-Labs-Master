# Second-order test of the vector-valued route.
# For P_{al,be}(tau) = sum_{nu in C0 cap (al+Z^2)} e(B(nu,be)) q^{Q2(nu)},  q = e(x) e^{-t}:
#   P ~ I*G(x)/t + a(x)/sqrt(t) + O(1),  with (exact finite formula, EM on residue classes mod L)
#   a(x) = -(sqrt(pi)/(2L)) sum_c ph_c [ B1(be_c) + B1(al_c)/sqrt(7/2) ],  classes nu0 in (al+Z^2) cap (0,L]^2.
# Weight-1 vector law at order t^{-1/2} would require  a_{a,b}(-1/x) = (sgn x / sqrt35) e(B(a,b)) sum_p a_{b+p,-a}(x).
import cmath, math
from fractions import Fraction as Fr
exec(open('weil_test.py').read().split("out=[")[0])
def B1(u): return float(u) - 0.5
def acoef(al,be,x):
    x=Fr(x); L=4*x.denominator
    s=0
    o0=Fr(al[0])%1; o1=Fr(al[1])%1
    if o0==0: o0=Fr(1)
    if o1==0: o1=Fr(1)
    for i in range(L):
        for j in range(L):
            nu=(o0+i, o1+j)                     # in (0, L]^2
            ph=cmath.exp(2j*math.pi*float((x*Qf(nu)+Bf(nu,be))%1))
            s+=ph*(B1(nu[1]/L) + B1(nu[0]/L)/math.sqrt(3.5))
    return -math.sqrt(math.pi)/(2*L)*s
out=[]
a=(Fr(7,10),Fr(-1,5)); zero=(Fr(0),Fr(0))
for L_x in [Fr(1),Fr(2),Fr(3)]:   # x integer -> trivial phases; consistency of the class formula
    out.append(f"check: a_(a,0)(x={L_x}) = {acoef(a,zero,L_x):.12f}   (EM value for R, t^-1/2 coeff: -0.360609721121)")
worst=0; rows=[]
for (al,be,lab) in [(a,zero,"(a,0)"),(reps[3],neg(a),"(p3,-a)")]:
    for x in [Fr(1),Fr(1,3),Fr(2,3),Fr(1,7),Fr(3,7),Fr(1,2),Fr(3,4),Fr(2,5)]:
        lhs=acoef(al,be,-1/x)
        rhs=cmath.exp(2j*math.pi*float(Bf(al,be)%1))/math.sqrt(35)*sum(acoef(addv(be,p),neg(al),x) for p in reps)
        rows.append(f"order t^-1/2  {lab:9} x={str(x):4}: LHS={lhs.real:+.8f}{lhs.imag:+.8f}i  RHS={rhs.real:+.8f}{rhs.imag:+.8f}i  |LHS|/|RHS|={abs(lhs)/abs(rhs) if abs(rhs)>1e-12 else float('nan'):.5f}")
out+=rows
print("\n".join(out)); open("weil_order2.txt","w").write("\n".join(out)+"\n")
