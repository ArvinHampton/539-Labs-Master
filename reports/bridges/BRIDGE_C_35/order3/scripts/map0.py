from lib3 import *
import json
I=math.log(6+math.sqrt(35))/(2*math.sqrt(35))
out=[]
for x in [Fr(1),Fr(1,2),Fr(1,3),Fr(2,3),Fr(1,4),Fr(1,5),Fr(1,6)]:
    m=x.denominator; ts=np.array([2.0**-j*0.5/(297.5*(2*m)**2) for j in range(6)])
    X=40/ts.min(); R=int(math.sqrt(X/0.6))+3; acc=np.zeros(6,complex); k=np.arange(-R,R+1)
    for n in range(-R,R+1):
        q7=n*n+7*n*k+(7*k*(k+1))//2
        wt=((n>=0)&(k>=0)).astype(float)-0.5*(np.sign(n)+np.sign(n+21*k))
        sel=(wt!=0)&(q7<=X)
        if n in (-R,R): assert not sel.any()
        if not sel.any(): continue
        qq=q7[sel]; ww=wt[sel]*np.exp(2j*np.pi*((x.numerator*(qq%m))%m)/m)
        acc+=np.array([np.sum(ww*np.exp(-t*(qq-0.35))) for t in ts])
    acc*=np.exp(-2j*np.pi*7*float(x)/20)
    o=parts(a,(Fr(0),Fr(0)),x); A0,A1=o['A0'],o['A1']
    Mx=np.array([[1,t**0.5,t] for t in ts])
    c=np.linalg.lstsq(Mx,(ts*acc-A0)/np.sqrt(ts),rcond=None)[0]
    c2=np.linalg.lstsq(Mx,acc-A0/ts-A1/np.sqrt(ts),rcond=None)[0]
    ref=max(abs(A1),0.05); err=abs(c[0]-A1)/ref
    v='pass' if err<=1e-3 else ('FALSIFY' if err>1e-2 else 'inconclusive')
    out.append(dict(x=str(x),A1=[A1.real,A1.imag],c1=[c[0].real,c[0].imag],err=err,verdict=v,A2_desc=[c2[0].real,c2[0].imag],
                    parts={k:[o[k].real,o[k].imag] for k in o}))
    print(x,round(err,7),v,'A2~',np.round(c2[0],4),flush=True)
json.dump(out,open('../data/map0.json','w'),indent=1)
