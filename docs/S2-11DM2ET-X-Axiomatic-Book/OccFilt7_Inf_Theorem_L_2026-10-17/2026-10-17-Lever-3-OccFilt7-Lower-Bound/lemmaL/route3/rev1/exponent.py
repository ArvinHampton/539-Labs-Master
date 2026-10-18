"""Steering (a): rigorous enclosure of the growth exponent.  c_plus >= sup_alpha Psi(alpha) via F_up on alpha-boxes (any u_c);
c_minus <= Psi(alpha*) for alpha* in [0.438,0.438+14/sqrt(D0)] (inf over u-boxes).  Closed form c = sqrt((Li2(y^2)+7 ln^2 y)/7)."""
import math, json
from mpmath import iv, mp
from tails import Phi1, g, argmin_u, I, ONE
iv.prec=60; Q=1200
D0=8890003; sD=math.sqrt(D0)
mp.dps=30; y=mp.findroot(lambda y:y**7+y**2-1,0.84); c=mp.sqrt((mp.polylog(2,y**2)+7*mp.log(y)**2)/7)
print('closed-form c =',c)
# upper: alpha boxes
cplus=-1; G0=-1e9; a=0.005; W=0.0005
while a<1-1e-12:
    b=min(a+W,1.0); uc=argmin_u((a+b)/2); P=Phi1(I(uc),Q); A=I([a,b])
    Fu=(A*P+(ONE-A**2)*I(uc)/(7*A)).b; cplus=max(cplus,float(Fu)); 
    G0=max(G0, float(g(I(uc)).b)+sD*(float(Fu)-0.3990)); a=b
print('c_plus (sup F_up over alpha in [0.005,1]) =',cplus)
print('G0 = max_box [g(u_c) - sqrt(D0)(0.3990 - F_up)] =',G0)
# lower at alpha*
A=I([0.438,0.438+14/sD]); cminus=10
u=0.02
while u<10:
    if 0.5<=u<=0.75: ub=u+0.0005; q=Q
    else: ub=(u*1.01 if u>0.1 else u+0.001); q=200
    val=(A*Phi1(I([u,ub]),q)+(ONE-A**2)*I([u,ub])/(7*A)).a; cminus=min(cminus,float(val)); u=ub
cminus=min(cminus,0.48)
print('c_minus (Psi_low at alpha*) =',cminus)
json.dump(dict(c=float(c),c_plus=cplus,c_minus=cminus,G0=G0,D0=D0),open('exponent.json','w'),indent=1)
