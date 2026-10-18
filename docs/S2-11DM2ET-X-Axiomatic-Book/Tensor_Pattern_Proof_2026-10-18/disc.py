# Exact (Fractions): discriminant module L'/Z^2 = Z/35, CRT split into Z/5 + Z/7 and local quadratic forms; exact T-spectrum on W=Fix(P).
from fractions import Fraction as F
import numpy as np, sys
sys.path.insert(0,'.')
from family import LP, Q70, B70, D
out=[]
# generator of L'/Z^2
gens=[p for p in LP if len({tuple((k*p)%D) for k in range(35)})==35]; g=gens[0]
out.append(f"L'/Z^2 cyclic of order 35, generator 70*g = {tuple(g)}; Q(g) = {Q70(g)%1}")
q=Q70(g)%1  # Q(kg) = k^2 q mod 1 (q has denominator 35*? )
out.append(f"Q(k g) = k^2 * {q} mod 1 check: {all((Q70((k*g))-k*k*q)%1==0 for k in range(35))}  (Q mod 1 well-defined: Q(g+n) ...)")
g5=(7*g)%D; g7=(5*g)%D   # orders 5 and 7
q5=Q70(g5)%1; q7=Q70(g7)%1
out.append(f"5-part generator 7g: Q = {q5}  -> form c5 x^2/5 with c5 = {q5*5}; 7-part generator 5g: Q = {q7} -> c7 = {q7*7}; B(g5,g7) = {B70(g5,g7)%1}")
def leg(a,p): return 1 if pow(int(a)%p,(p-1)//2,p)==1 else -1
out.append(f"Legendre: (c5|5) = {leg(q5*5,5)}, (c7|7) = {leg(q7*7,7)}")
print("\n".join(out)); open("disc.txt","w").write("\n".join(out)+"\n")
