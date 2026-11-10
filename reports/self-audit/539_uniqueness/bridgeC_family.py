# Tests, for integer s, the Bridge C structural identity (s04_rq.tex:39-44, eq. Edef):
#   E_s := R_s + Cthird_s + sum_{n>=1} q^{n^2}  ==  sum_{v: v+a in F} q^{Q_s(v)},  F=[r, gamma r) fundamental cone,
# and hence 2P_s = E_s + 1 + theta3 - Theta_hol,s, with P_s = sum_{n,k>=0} q^{Q_s} (s01_intro.tex:3, s04_rq.tex:6-16).
# Also: P_s - (theta pieces) nonzero ("residual produced"), the Baker leading coefficient, and dim V = s(s-1) (s12_dims.tex:8).
from fractions import Fraction as Fr
import math,sys,json
def series(s,M):
  h=Fr(s,2)
  P=[0]*(M+1); R=[0]*(M+1); Ct=[0]*(M+1); Sq=[0]*(M+1)
  K=int(2*math.sqrt(M))+5
  for n in range(0,M+1):
    if n*n>M: break
    for k in range(0,M+1):
      e=n*n+s*n*k+h*k*(k+1)
      if e>M: break
      assert e.denominator==1; P[int(e)]+=1
      if k>=1: R[int(e)]+=1
  for n in range(1,M+1):
    if n*n>M: break
    Sq[n*n]+=1
    for k in range(1,M+1):
      e=n*n+s*n*k+h*k*(k-1)
      if e>M: break
      Ct[int(e)]+=1
  E=[R[i]+Ct[i]+Sq[i] for i in range(M+1)]
  return P,R,Ct,Sq,E
def cone_sum(s,M,r):
  a=(Fr(s,2*(s-2)),Fr(-1,s-2)); c0=Fr(s,4*(s-2))
  g=((-1,-s),(2,2*s-1))
  gr=(g[0][0]*r[0]+g[0][1]*r[1],g[1][0]*r[0]+g[1][1]*r[1])
  det=r[0]*gr[1]-r[1]*gr[0]
  out=[0]*(M+1)
  K=int(2*math.sqrt(M))+3 if r==(1,0) else int((2*s+1)*math.sqrt(M))+3
  B=K
  Q=lambda x:x[0]**2+s*x[0]*x[1]+Fr(s,2)*x[1]**2
  for n in range(-B,B+1):
    for k in range(-2,K+1):
      x=(n+a[0],k+a[1])
      al=Fr(x[0]*gr[1]-x[1]*gr[0],det); be=Fr(r[0]*x[1]-r[1]*x[0],det)
      if al>0 and be>=0:
        e=Q(x)+c0
        if e<=M: assert e.denominator==1; out[int(e)]+=1
  return out,B
def run(s,M):
  P,R,Ct,Sq,E=series(s,M)
  res={}
  for r in ([(1,0),(1,1)] if s<=60 else [(1,0)]):
    cs,B=cone_sum(s,M,r); res[str(r)]=(cs==E)
  theta3=[0]*(M+1); theta3[0]=1
  for n in range(1,M+1):
    if n*n<=M: theta3[n*n]+=2
  Thol=[Ct[i]+Sq[i]-R[i] for i in range(M+1)]
  ident=all(2*P[i]==E[i]+(1 if i==0 else 0)+theta3[i]-Thol[i] for i in range(M+1))
  resid_nonzero=any(R[i]!=0 for i in range(M+1))  # P_s minus its unary theta row
  lead=math.acosh(s-1)/(2*math.sqrt(s*(s-2)))
  return dict(s=s,M=M,cone_identity=res,two_P_identity=ident,residual_R_nonzero=resid_nonzero,
              nonsquare_radicand=int(math.isqrt(s*(s-2)))**2!=s*(s-2),Baker_lead_coeff=lead,orbit_bound_dimV=s*(s-1) if s%2 else (s//2)*(s//2+1))
if __name__=='__main__':
  ss=list(range(5,31))+[49,98,121,147,169,245,363,539,3481]
  out=[]
  for s in ss:
    M=800 if s<=60 else 1500
    d=run(s,M); out.append(d); print(json.dumps(d)); sys.stdout.flush()
  json.dump(out,open('bridgeC_family.json','w'),indent=1)
