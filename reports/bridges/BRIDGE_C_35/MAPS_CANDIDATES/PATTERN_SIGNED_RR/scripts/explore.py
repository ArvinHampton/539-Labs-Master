# Signed fibre mass of the 140 written labels (rev8 tex l.134-160, l.272).
# w(v)=1/2(sgn B(c1,v)-sgn B(c2,v)), c1=(-1,1), c2=(-4,1); B(x,y)=x^T G y, G=[[2,7],[7,7]] (Q=1/2 B).
# Point nu=alpha+v, v in Z^2 (as in H_s: nu=v+a). Phase e(B(nu,beta)), beta in {0,-a}. Fibre 140*Q(nu) mod 8.
# Box |v_i|<=R, normalized by (2R+1)^2. Does not read the residual law.
import json, numpy as np
from fractions import Fraction as F
R=int(__import__('sys').argv[1]) if len(__import__('sys').argv)>1 else 300
Ai=[[F(-1,5),F(1,5)],[F(1,5),F(-2,35)]]; a=(F(7,10),F(-1,5)); al=set()
for x in range(70):
  for y in range(70):
    v=(Ai[0][0]*x+Ai[0][1]*y,Ai[1][0]*x+Ai[1][1]*y)
    for s in (0,1): al.add(((v[0]+s*a[0])%1,(v[1]+s*a[1])%1))
al=sorted(al); assert len(al)==70
n,k=np.meshgrid(np.arange(-R,R+1),np.arange(-R,R+1),indexing='ij'); n=n.astype(np.int64);k=k.astype(np.int64)
w=0.5*(np.sign(5*n)-np.sign(-n-21*k))
res={'R':R,'labels':{}}
pool_abs=np.zeros(8); supp=set()
for A in al:
  X=70*int(70*A[0])//70; X0,Y0=int(70*A[0]),int(70*A[1])
  Xn=X0+70*n; Yn=Y0+70*k
  q=2*Xn*Xn+14*Xn*Yn+7*Yn*Yn; assert (q%70==0).all(); f=(q//70)%8
  for b,beta in ((0,(0,0)),(1,(-7,2))):  # 70*(-a) = (-49,14) -> use exact below
    if b==0: ph=np.ones_like(w,dtype=complex)
    else:
      # B(nu,-a)= -(G nu).a ; 70nu=(Xn,Yn); a=(7/10,-1/5)
      Bv=-((2*Xn+7*Yn)*0.7+(7*Xn+7*Yn)*(-0.2))/70.0
      ph=np.exp(2j*np.pi*Bv)
    M=np.array([ (w*ph)[f==i].sum() for i in range(8)])/(2*R+1)**2
    res['labels'][f'{A[0]},{A[1]};b{b}']=[[float(z.real),float(z.imag)] for z in M]
    pool_abs+=np.abs(M)/140
    supp|={i for i in range(8) if (f==i).any() and abs(M[i])>1e-9}
res['POOL_ABS_norm']=(pool_abs/pool_abs.sum()).tolist() if pool_abs.sum()>0 else None
res['POOL_ABS_raw']=pool_abs.tolist(); res['support_signed']=sorted(supp)
print(json.dumps({k:v for k,v in res.items() if k!='labels'},indent=1))
json.dump(res,open(f'data/explore_R{R}.json','w'))
