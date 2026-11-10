# Written label family (rev8 tex l.134-143, l.272): alpha in ({0,a}+L')/Z^2, beta in {0,-a}; 140 labels.
# L'=A^{-1}Z^2, A^{-1}=[[-1/5,1/5],[1/5,-2/35]], a=(7/10,-1/5). Unary theta (partIII_shadow l.115): u in alpha1+Z, exponent 5u^2/2.
# Does not read the residual law.
import json
from fractions import Fraction as F
from math import lcm
Ai=[[F(-1,5),F(1,5)],[F(1,5),F(-2,35)]]
a=(F(7,10),F(-1,5))
al=set()
for x in range(70):
  for y in range(70):
    v=(Ai[0][0]*x+Ai[0][1]*y, Ai[1][0]*x+Ai[1][1]*y)
    for s in (0,1):
      w=((v[0]+s*a[0])%1,(v[1]+s*a[1])%1); al.add(w)
al=sorted(al); assert len(al)==70, len(al)
labels=[(A,b) for A in al for b in (0,1)]; assert len(labels)==140
# minimal integer scale N making 5u^2/2 integral for all u in alpha1+Z over the family
dens=set(A[0].denominator for A in al)
N=1
for d in dens:
  N=lcm(N,(F(5,2)/d**2).denominator*1)  # exponent 5(x/d)^2/2 = 5x^2/(2d^2)
N=lcm(*[ (F(5,2)*F(1,d*d)).denominator for d in dens]) if dens else 1
def mass(alpha1,scale):
  d=alpha1.denominator; r=alpha1.numerator
  c=[F(0)]*8; per=8*d
  # u=(r+d n)/d ; integer exponent = scale*5*(r+dn)^2/(2 d^2); n mod 8*... uniform
  P=16
  for n in range(P):
    e=F(scale*5,2)*(alpha1+n)**2; assert e.denominator==1
    c[int(e)%8]+=F(1,P)
  return c
def pool(sub,scale):
  t=[F(0)]*8
  for A,b in sub:
    m=mass(A[0],scale); t=[x+y/len(sub) for x,y in zip(t,m)]
  return t
out={'N_min_scale':N,'alpha1_set':sorted(set(str(A[0]) for A in al)),'n_labels':len(labels)}
out['POOL_ALL140_Nmin']=pool(labels,N)
cusp=[L for L in labels if L[1]==1 and 70*L[0][0] in (7,21,49,63)]
out['n_beta-a_70a1_in_7_21_49_63']=len(cusp)
out['POOL_70a1set_beta-a_Nmin']=pool(cusp,N)
for A in sorted(set(A[0] for A in al)):
  out['per_alpha1_'+str(A)]=mass(A,N)
print('label alphas:',[(str(A[0]),str(A[1])) for A in al])
out={k:([str(x) for x in v] if isinstance(v,list) and v and isinstance(v[0],F) else v) for k,v in out.items()}
print(json.dumps(out,indent=1)); json.dump(out,open('data/explore.json','w'),indent=1)
