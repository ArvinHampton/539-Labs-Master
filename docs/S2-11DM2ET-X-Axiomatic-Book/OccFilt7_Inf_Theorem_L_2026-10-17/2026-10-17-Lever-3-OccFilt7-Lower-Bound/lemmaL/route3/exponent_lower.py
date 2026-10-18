"""Sharper c_minus (rev2): inf over u in [0.5,0.75] (certified range of the central saddle u*) and over 40 alpha-sub-boxes
of [0.438,0.438+14/sqrt(D0)] of F_low.  Interval arithmetic; no claims outside u in [0.5,0.75]."""
import math, json
from mpmath import iv
from tails import Phi1, I, ONE
iv.prec=60; D0=8890003; sD=iv.sqrt(I(D0)); K=40
lo=I('0.438').a; hi=(I('0.438')+14/sD).b
edges=[lo]+[(lo+(hi-lo)*I(i)/K).b for i in range(1,K)]+[hi]
subs=[I([edges[i],edges[i+1]]) for i in range(K)]
cminus=None; u=I('0.5').a; H=I('0.0005')
while u<I('0.75').a:
    ub=min((u+H).b, I('0.75').b); U=I([u,ub]); P=Phi1(U,1200)
    m=min((A*P+(ONE-A**2)*U/(7*A)).a for A in subs)
    cminus=m if cminus is None else min(cminus,m); u=ub
print('c_minus =',cminus)
dn=lambda x: math.nextafter(float(x), -math.inf) if float(x) > x else float(x)
d=json.load(open('exponent.json')); d['c_minus_down']=dn(cminus); json.dump(d,open('exponent.json','w'),indent=1)
