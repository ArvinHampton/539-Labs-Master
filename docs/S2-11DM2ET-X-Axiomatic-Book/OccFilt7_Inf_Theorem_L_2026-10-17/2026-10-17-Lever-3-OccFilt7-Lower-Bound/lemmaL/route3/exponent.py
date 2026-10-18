"""Steering (a): rigorous enclosure of the growth exponent (rev2: mpf intervals throughout, no float() of endpoints).
c_plus >= sup_{alpha in [0.005,1]} Psi(alpha) via F_up on alpha-boxes (any u_c); tiny alpha in (0,0.005] handled analytically.
Closed form c = sqrt((Li2(y^2)+7 ln^2 y)/7)."""
import math, json
from mpmath import iv, mp
from tails import Phi1, g, argmin_u, I, ONE
iv.prec=60; Q=1200
D0=8890003; sD=iv.sqrt(I(D0)); CREF=I('0.3990')
mp.dps=30; y=mp.findroot(lambda y:y**7+y**2-1,0.84); c=mp.sqrt((mp.polylog(2,y**2)+7*mp.log(y)**2)/7)
print('closed-form c =',c)
cplus=None; G0=None; a=I('0.005').a; W=I('0.0005')
while a<1:
    b=min((a+W).b,I(1).a); uc=argmin_u((float(I(a).a)+float(I(b).a))/2); P=Phi1(I(uc),Q); A=I([a,b])
    Fu=(A*P+(ONE-A**2)*I(uc)/(7*A)).b
    cplus=Fu if cplus is None else max(cplus,Fu)
    gb=(g(I(uc)) - sD*(CREF-Fu)).b      # valid bound for d>=D0 only if Fu <= CREF (checked below)
    G0=gb if G0 is None else max(G0,gb); a=b
assert cplus <= CREF.a, 'sup F_up exceeds 0.3990'
# tiny alpha (0,0.005]: F <= 0.0267, g(u) <= log(d/3.5)+1 -> per-term log a_n <= 0.0267 sqrt(d) + log(d/3.5) + 1 + log 2,
# which is <= 0.3990 sqrt(d) + G0 + log 2 for d >= D0 because (0.3990-0.0267) sqrt(D0) > log(D0/3.5)+1 and the gap grows in d.
tiny_ok = ((CREF-I('0.0267'))*sD - iv.log(I(D0)/I('3.5')) - 1).a > 0
print('c_plus (sup F_up over alpha in [0.005,1]) =',cplus)
print('G0 = max_box [g(u_c) - sqrt(D0)(0.3990 - F_up)] =',G0)
print('tiny-alpha branch dominated for d>=D0:',tiny_ok, ' margin', ((CREF-I('0.0267'))*sD - iv.log(I(D0)/I('3.5')) - 1).a)
up=lambda x: math.nextafter(float(x), math.inf) if float(x) < x else float(x)
json.dump(dict(c=float(c),c_plus_up=up(cplus),G0_up=up(G0),tiny_dominated=bool(tiny_ok),D0=D0),open('exponent.json','w'),indent=1)
