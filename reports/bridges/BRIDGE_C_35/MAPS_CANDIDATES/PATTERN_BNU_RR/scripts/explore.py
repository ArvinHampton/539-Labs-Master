# Fibre coords (written, rev8 tex): (A) B(nu,a) [l.896: B(nu,a)=Re theta/10]; (T) T-phase Q(alpha)+B(alpha,w_c) [l.276 T-law].
# Does not read the residual law. Exact Fractions; signed content numeric.
import json, sys, numpy as np
from fractions import Fraction as F
from math import lcm
G=[[2,7],[7,7]]; a=(F(7,10),F(-1,5)); wc=(F(1,10),F(-1,35))
Bf=lambda x,y:sum(x[i]*G[i][j]*y[j] for i in range(2) for j in range(2))
Qf=lambda x:Bf(x,x)/2
Ai=[[F(-1,5),F(1,5)],[F(1,5),F(-2,35)]]; al=set()
for x in range(70):
  for y in range(70):
    v=(Ai[0][0]*x+Ai[0][1]*y,Ai[1][0]*x+Ai[1][1]*y)
    for s in (0,1): al.add(((v[0]+s*a[0])%1,(v[1]+s*a[1])%1))
al=sorted(al); assert len(al)==70
out={}
print('B(e1,a),B(e2,a)=',Bf((1,0),a),Bf((0,1),a))
# (A) N_A = least integer making B(nu,a) integral on all labels
NA=lcm(*[Bf((A[0]+n1,A[1]+n2),a).denominator for A in al for n1 in range(2) for n2 in range(2)])
mA=[F(0)]*8; P=8*NA
for A in al:
  for n1 in range(2):
    for n2 in range(P):
      e=NA*Bf((A[0]+n1,A[1]+n2),a); assert e.denominator==1
      mA[int(e)%8]+=F(2,140*2*P)
out['NA']=NA; out['A_unsigned_pool140']=[str(x) for x in mA]
# signed w content binned by A-fibre (box R)
R=int(sys.argv[1]) if len(sys.argv)>1 else 200
n,k=np.meshgrid(np.arange(-R,R+1),np.arange(-R,R+1),indexing='ij')
w=0.5*(np.sign(5*n)-np.sign(-n-21*k)); pool=np.zeros(8)
for A in al:
  e=NA*(F(7,2)*A[1]); 
  # B(nu,a)=7/2*nu2 (checked above); NA*7/2*(A2+k)
  ek=(np.array(e.numerator//e.denominator if e.denominator==1 else 0)+int(NA*F(7,2))*k)%8
  assert e.denominator==1
  for b in (0,1):
    if b==0: ph=np.ones(w.shape,complex)
    else:
      X=float(A[0])+n; Y=float(A[1])+k
      Bv=-((2*X+7*Y)*0.7+(7*X+7*Y)*(-0.2)); ph=np.exp(2j*np.pi*Bv)
    M=np.array([(w*ph)[ek==i].sum() for i in range(8)])/(2*R+1)**2
    pool+=np.abs(M)/140
out['R']=R; out['A_signed_absnorm']=(pool/pool.sum()).tolist()
# (T) T-phase per label
tp=[(Qf(A)+Bf(A,wc))%1 for A in al]
NT=lcm(*[t.denominator for t in tp]); mT=[F(0)]*8
for t in tp: mT[int(NT*t)%8]+=F(2,140)
out['NT']=NT; out['T_pool140']=[str(x) for x in mT]
out['T_values']=sorted(set(str(t) for t in tp))
print(json.dumps(out,indent=1)); json.dump(out,open(f'data/explore_R{R}.json','w'),indent=1)
