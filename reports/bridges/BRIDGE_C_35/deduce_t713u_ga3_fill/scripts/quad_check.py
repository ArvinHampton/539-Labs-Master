import sys; sys.path.insert(0,'scripts')
import mpmath as mp, cmath, math
from fractions import Fraction as Fr
import ga3_fill as G
c=G.xi_table(106); mx=0
for x in (1/7,3/7,5/7,1,-1,-1/3,-1/5,-1/7):
    f=lambda t: sum(float(v)*mp.e**(2j*mp.pi*float(nu)*(x+1j*t)) for nu,v in c.items())*(1j*t)**-0.5*1j
    q=-mp.quad(f,[0,0.01,0.1,1,mp.inf]); d=abs(complex(q)-G.I(x,c)); mx=max(mx,d); print(x,complex(q),G.I(x,c),d)
print("max",mx)
