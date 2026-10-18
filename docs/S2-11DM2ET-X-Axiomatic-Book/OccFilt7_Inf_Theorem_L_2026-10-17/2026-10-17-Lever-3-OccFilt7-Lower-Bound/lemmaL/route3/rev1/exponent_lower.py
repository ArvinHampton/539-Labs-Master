"""Sharper c_minus: inf over u-boxes and over 40 alpha-sub-boxes of [0.438,0.438+14/sqrt(D0)] of F_low."""
import math, json
from mpmath import iv
from tails import Phi1, I, ONE
iv.prec=60; D0=8890003; sD=math.sqrt(D0); K=40
subs=[I([0.438+14/sD*i/K,0.438+14/sD*(i+1)/K]) for i in range(K)]
cminus=10; u=0.02
while u<10:
    if 0.5<=u<=0.75: ub=u+0.0005; q=1200
    else: ub=(u*1.01 if u>0.1 else u+0.001); q=200
    U=I([u,ub]); P=Phi1(U,q)
    cminus=min(cminus,min(float((A*P+(ONE-A**2)*U/(7*A)).a) for A in subs)); u=ub
cminus=min(cminus,0.48)
print('c_minus =',cminus)
d=json.load(open('exponent.json')); d['c_minus_sharp']=cminus; json.dump(d,open('exponent.json','w'),indent=1)
