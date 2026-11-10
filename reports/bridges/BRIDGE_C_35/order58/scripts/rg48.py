# order58 RG48: discriminant form of companion lattice A (Q=n1^2+7n1n2+7n2^2/2, Gram [[2,7],[7,7]]) vs all definite even binary lattices det 35.
import json,itertools,cmath,math
from fractions import Fraction as F
def dform(G):
    a,b,c=G[0][0],G[0][1],G[1][1]; d=a*c-b*b; D=abs(d)
    inv=[[F(c,d),F(-b,d)],[F(-b,d),F(a,d)]]
    els=set()
    for i in range(D):
        for j in range(D):
            v=(inv[0][0]*i+inv[0][1]*j, inv[1][0]*i+inv[1][1]*j); v=(v[0]%1,v[1]%1); els.add(v)
    def q(v): return (F(a)*v[0]**2+2*b*v[0]*v[1]+c*v[1]**2)/2 %1
    vals=sorted(q(v) for v in els); g=sum(cmath.exp(2j*math.pi*float(x)) for x in vals)/math.sqrt(len(vals))
    return vals,g
A=[[2,7],[7,7]]; vA,gA=dform(A); vmA=sorted((-x)%1 for x in vA)
forms=[]
for a in range(1,40):
  for c in range(a,40):
    for b in range(0,a+1):
      if a*c-b*b==35 and 2*b<=2*a: forms.append([[2*a,b],[b,2*c]]) if False else None
# even Gram [[2a,b],[b,2c]], det 4ac-b^2=35, reduced |b|<=2a<=2c... wait det must equal 35 -> enumerate
forms=[]
for a in range(1,30):
  for c in range(a,30):
    for b in range(-a*2,2*a+1):
      if 4*a*c-b*b==35 and abs(b)<=a*2 and 2*a<=2*c: forms.append([[2*a,b],[b,2*c]])
out=dict(A=dict(gram=A,det=-35,milgram=[gA.real,gA.imag],arg_over_2pi=cmath.phase(gA)/(2*math.pi)),forms=[])
for G in forms:
    v,g=dform(G); out['forms'].append(dict(gram=G,milgram=[g.real,g.imag],same_qvals_as_A=v==vA,same_as_minusA=v==vmA))
out['any_definite_match_qA']=any(f['same_qvals_as_A'] for f in out['forms'])
out['any_definite_match_minus_qA']=any(f['same_as_minusA'] for f in out['forms'])
print(json.dumps(out,indent=1)); json.dump(out,open('../data/rg48.json','w'),indent=1)
