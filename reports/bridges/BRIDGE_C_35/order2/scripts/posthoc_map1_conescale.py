# POST-HOC diagnostic (not preregistered): Map 1 numerics with the t-grid scaled to the longest cone edge,
# t_max = 0.5/(Q(u1)*(2m)^2) with Q(u1)=297.5, t_j = t_max*2^-j (j=0..5). Row-streamed sums (no storage).
from lib2 import *
import json, sys
I=math.log(6+math.sqrt(35))/(2*math.sqrt(35))
PTS=[Fr(s) for s in sys.argv[1:]] or [Fr(1,2),Fr(1,3),Fr(1,4),Fr(1,6),Fr(1,7)]
out=[]
for x in PTS:
    m=x.denominator; tmax=0.5/(297.5*(2*m)**2); ts=np.array([tmax*2**-j for j in range(6)])
    X=40/ts.min(); R=int(math.sqrt(X/0.6))+3
    acc=np.zeros(6,complex); k=np.arange(-R,R+1)
    for n in range(-R,R+1):
        q7=n*n+7*n*k+(7*k*(k+1))//2
        wt=((n>=0)&(k>=0)).astype(float)-0.5*(np.sign(n)+np.sign(n+21*k))
        sel=(wt!=0)&(q7<=X)
        if n in (-R,R): assert not sel.any()
        if not sel.any(): continue
        qq=q7[sel]; ww=wt[sel]*np.exp(2j*np.pi*((x.numerator*(qq%m))%m)/m)
        E=qq-0.35
        acc+=np.array([np.sum(ww*np.exp(-t*E)) for t in ts])
    acc*=np.exp(-2j*np.pi*7*float(x)/20)
    nn,kk=np.meshgrid(np.arange(2*m),np.arange(2*m),indexing='ij')
    G=np.exp(2j*np.pi*(x.numerator*((nn*nn+7*nn*kk+(7*kk*(kk+1))//2)%m)%m)/m).mean()*np.exp(-2j*np.pi*7*float(x)/20)
    _,A1p=A01_float(a,(Fr(0),Fr(0)),x)
    ys=(ts*acc-I*G)/np.sqrt(ts)
    c=np.linalg.lstsq(np.array([[1,t**0.5,t] for t in ts]),ys,rcond=None)[0]
    err=abs(c[0]-A1p)/max(abs(A1p),0.05)
    out.append(dict(x=str(x),ts=ts.tolist(),A1_pred=[A1p.real,A1p.imag],c1=[c[0].real,c[0].imag],err_rel=err,ys=[[y.real,y.imag] for y in ys]))
    print(x,'pred',np.round(A1p,5),'fit',np.round(c[0],5),'err',round(err,5),flush=True)
json.dump(out,open('../data/posthoc_map1_conescale_%s.json'%('_'.join(str(p).replace('/','-') for p in PTS)),'w'),indent=1)
