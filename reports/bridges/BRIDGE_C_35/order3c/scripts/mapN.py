# brute-force series S_{a,0} on the preregistered grid, one x per process
import sys, json, numpy as np, math
from fractions import Fraction as Fr
from lib3c import A012, corner_mag, a
x=Fr(sys.argv[1]); m=x.denominator; h=x.numerator
J=8; ts=np.array([2.0**-j*0.5/(297.5*(2*m)**2) for j in range(J)]); tmin=ts[-1]
X=36/tmin; acc=np.zeros(J,complex)
# Q(nu+a)=Q7-7/20, Q7=n^2+7nk+7k(k+1)/2 ; weights from order3 map0 (orthant minus cone weight)
R=int(math.sqrt(X/0.6))+3
for n in range(-R,R+1):
    # k range where Q7<=X : 3.5k^2+(7n+3.5)k+n^2-X<=0
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
assert abs(n)==R
al=a; be=(Fr(0),Fr(0))
A0,A1,A2=A012(al,be,x); _,_,A2bad=A012(al,be,x,corner_sign=-1.0); cm=corner_mag(al,be,x)
Mx=np.array([[1,t**0.5,t,t**1.5] for t in ts])
c=np.linalg.lstsq(Mx,acc-A0/ts-A1/np.sqrt(ts),rcond=None)[0]
err=abs(c[0]-A2)/max(1,abs(A2)); errbad=abs(c[0]-A2bad)/max(1,abs(A2bad))
v='pass' if err<=1e-3 else ('FALSIFY' if err>1e-2 else 'inconclusive')
out=dict(x=str(x),A0=[A0.real,A0.imag],A1=[A1.real,A1.imag],A2=[A2.real,A2.imag],c0=[c[0].real,c[0].imag],err=err,verdict=v,
         A2_flipped=[A2bad.real,A2bad.imag],err_flipped=errbad,corner_mag=cm,X=X)
print(json.dumps(out))
json.dump(out,open('../data/mapN_%s.json'%str(x).replace('/','-'),'w'),indent=1)
