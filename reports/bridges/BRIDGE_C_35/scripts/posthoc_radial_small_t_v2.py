# Map B-radial (Category B, floating point): t*C(e(y)e^{-t}) -> RHS of (B), y=-1/x, x in X216 with m<=5.
from common import *
import json, math
I=math.log(6+math.sqrt(35))/(2*math.sqrt(35))
TS=[1e-4,5e-5,2.5e-5,1.25e-5,6.25e-6,3.125e-6]; FLAG={"4/5","6/5","4/3","8/5","9/5","11/5","9/4","12/5","13/5","8/3","11/4"}
X=40/min(TS)
R=int(math.sqrt(X/0.6))+2
pts=[];wts=[]
for n in range(-R,R+1):
    k=np.arange(-R,R+1)
    q=n*n+7*n*k+(7*k*(k+1))//2
    orth=((n>=0)&(k>=0)).astype(float)
    w=0.5*(np.sign(n)+np.sign(n+21*k))
    wt=orth-w; sel=(wt!=0)&(q<=X)
    if sel.any(): pts.append(q[sel]); wts.append(wt[sel])
q=np.concatenate(pts).astype(np.int64); wt=np.concatenate(wts)
assert (q>=0).all()
# check truncation box is adequate: no selected point near box edge
print('points',len(q),'R',R,flush=True)
def K3c(mu,x):  # float value of G_{mu,a}(x) (finite mean)
    m=x.denominator; Lb=4*m
    i,j=np.meshgrid(np.arange(Lb),np.arange(Lb),indexing='ij')
    v0=float(mu[0])+i; v1=float(mu[1])+j
    Qv=0.5*(2*v0*v0+14*v0*v1+7*v1*v1); Bv=v0*(2*a[0]+7*a[1])+v1*(7*a[0]+7*a[1])
    return np.exp(2j*np.pi*(float(x)*Qv+float(Bv[0,0]*0)+ (v0*float(2*a[0]+7*a[1])+v1*float(7*a[0]+7*a[1])))).mean()
def rhs(x):
    acc=sum(np.exp(-2j*np.pi*float(B(mu,(2*a[0],2*a[1]))))*K3c(mu,x) for mu in MU)
    return I*np.exp(-2j*np.pi*7/(20*float(x)))*acc/(float(x)*math.sqrt(35))
out=[]
A=np.array([[1,t**0.5,t,t**1.5] for t in TS])
for x in [x for x in XS if str(x) in FLAG]:
    y=-1/x; num,den=y.numerator,y.denominator
    ph=np.exp(2j*np.pi*((num*(q%den))%den)/den)
    vals=np.array([t*np.sum(wt*ph*np.exp(-t*q)) for t in TS])
    c=np.linalg.lstsq(A,vals,rcond=None)[0]
    pred=rhs(x); lem3=I*Grta_c(y); ref=I/den
    err=abs(c[0]-pred)/ref
    verdict='pass' if err<=0.02 else ('FALSIFY' if err>0.10 else 'inconclusive')
    out.append(dict(x=str(x),y=str(y),c0=[c[0].real,c[0].imag],pred=[pred.real,pred.imag],lemma3_IG=[lem3.real,lem3.imag],
                    err_rel=err,verdict=verdict,raw=[[v.real,v.imag] for v in vals]))
    print(x,y,round(abs(pred),6),round(err,5),verdict,flush=True)
json.dump(dict(I=I,TS=TS,X=X,points=len(q),results=out),open('../data/posthoc_radial_small_t_v2.json','w'),indent=1)
