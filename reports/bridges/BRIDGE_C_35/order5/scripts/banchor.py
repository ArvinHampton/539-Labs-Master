# task (b) t-grid anchor: brute-force S_{a,0} (as order3c mapN) at x=1/8, 3/8 vs mp formula
import sys, json, numpy as np, math; sys.dont_write_bytecode=True
from lib5mp import *
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from symbols import a
x=Fr(sys.argv[1]); m=x.denominator; h=x.numerator
J=8; ts=np.array([2.0**-j*0.5/(297.5*(2*m)**2) for j in range(J)]); tmin=ts[-1]
X=36/tmin; acc=np.zeros(J,complex)
R=int(math.sqrt(X/0.6))+3
for n in range(-R,R+1):
    A_,B_,C_=3.5,7*n+3.5,n*n-X; disc=B_*B_-4*A_*C_
    if disc<0: continue
    k0=math.floor((-B_-math.sqrt(disc))/(2*A_))-1; k1=math.ceil((-B_+math.sqrt(disc))/(2*A_))+1
    k=np.arange(k0,k1+1)
    q7=n*n+7*n*k+(7*k*(k+1))//2
    wt=((n>=0)&(k>=0)).astype(float)-0.5*(np.sign(n)+np.sign(n+21*k))
    sel=(wt!=0)&(q7<=X)
    if not sel.any(): continue
    qq=q7[sel]; ww=wt[sel]*np.exp(2j*np.pi*((h*(qq%m))%m)/m)
    E=np.exp(-tmin*(qq-0.35))
    for j in range(J-1,-1,-1):
        acc[j]+=np.sum(ww*E); E=E*E
acc*=np.exp(-2j*np.pi*7*float(x)/20)
A0,A1,A2=[complex(v) for v in A012mp(a,(Fr(0),Fr(0)),x)]
Mx=np.array([[1,t**0.5,t,t**1.5] for t in ts])
c=np.linalg.lstsq(Mx,acc-A0/ts-A1/np.sqrt(ts),rcond=None)[0]
err=abs(c[0]-A2)/max(1,abs(A2))
out=dict(x=str(x),A2=[A2.real,A2.imag],c0=[c[0].real,c[0].imag],err=err,verdict='pass' if err<=1e-3 else ('FALSIFY' if err>1e-2 else 'inconclusive'),ts=list(ts))
print(json.dumps(out)); json.dump(out,open('../data/banchor_%s.json'%str(x).replace('/','-'),'w'),indent=1)
