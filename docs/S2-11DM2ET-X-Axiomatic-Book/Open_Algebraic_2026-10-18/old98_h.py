# (e) Second-level square root: at m=7, tr g + 2 = 16 = 4^2, so h = (g+I)/4 satisfies h^2 = g (h in SO(A)(Q)).
# Test where h acts on t-perp/<t> classes (choosing lifts modulo Z^2 + Z t) and the extra orbit collapse.
import sys, json, itertools
from fractions import Fraction as Fr
import numpy as np, sympy as sp
exec(open('old98_g.py').read().split("G=[[-1")[0].replace("s=int(sys.argv[1]); m=int(round((s/2)**.5)); p=int(sys.argv[2])","s=98; m=7; p=7"))
g=sp.Matrix([[0,-m],[sp.Rational(1,m),2*m]]); h=(g+sp.eye(2))/4
A=sp.Matrix([[2,s],[s,s]])
print("h^2==g",h*h==g," h isometry",h.T*A*h==A)
tv=sp.Matrix([sp.Rational(t[0],D),sp.Rational(t[1],D)])
def hact(x):
    # all lifts x/D + Z^2 (mod 4*7 enough) + j t ; return set of classes hit
    hits=set()
    for j in range(p):
        for a in range(28):
            for b in range(28):
                v=sp.Matrix([sp.Rational(x[0],D)+a,sp.Rational(x[1],D)+b])+j*tv
                w=h*v
                if all((wi*D).q==1 for wi in w):
                    z=(int(w[0]*D)%mod[0],int(w[1]*D)%mod[1])
                    if z in cls: hits.add(cls[z])
                    else: hits.add(('out',))
    return hits
res={}
sample=reps
hm={}
for r in sample:
    H=hact(r); hm[r]=H
wd=[r for r in sample if len(hm[r])==1 and ('out',) not in hm[r]]
res=dict(n_classes=len(reps),h_single_valued=len(wd),h_multivalued=sum(1 for r in sample if len(hm[r])>1),h_undefined=sum(1 for r in sample if len(hm[r])==0))
print(res)
json.dump(res,open("old_h_98.json","w"))
