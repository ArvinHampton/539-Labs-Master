# Map 1 numerical test (Category B) on q^{-7/20}C = S_{a,0}: denominator-scaled t-grid.
from lib2 import *
import json
I=math.log(6+math.sqrt(35))/(2*math.sqrt(35))
TAU=[0.02*2**-j for j in range(6)]
P=[x for x in XS if x.denominator<=10]
Xmax=40/(min(TAU)/100); R=int(math.sqrt(Xmax/0.6))+3
qs=[];ws=[]
for n in range(-R,R+1):
    k=np.arange(-R,R+1); q7=n*n+7*n*k+(7*k*(k+1))//2
    wt=((n>=0)&(k>=0)).astype(float)-0.5*(np.sign(n)+np.sign(n+21*k))
    sel=(wt!=0)&(q7<=Xmax+1)
    if sel.any(): qs.append(q7[sel]); ws.append(wt[sel])
    if n in (-R,R): assert not sel.any(), 'box too small'
q7=np.concatenate(qs).astype(np.int64); wt=np.concatenate(ws); assert (q7>=0).all()
o=np.argsort(q7); q7=q7[o]; wt=wt[o]
print('points',len(q7),flush=True)
def Gfl(x):
    m=x.denominator; n,k=np.meshgrid(np.arange(2*m),np.arange(2*m),indexing='ij')
    return np.exp(2j*np.pi*(x.numerator*((n*n+7*n*k+(7*k*(k+1))//2)%m)%m)/m).mean()*np.exp(-2j*np.pi*7*float(x)/20)
res=[]; npass=nfal=0
for x in P:
    m=x.denominator; ts=[tau/m**2 for tau in TAU]; Xc=40/min(ts); cut=np.searchsorted(q7,Xc,side='right')
    qq=q7[:cut]; ww=wt[:cut]
    ph=np.exp(2j*np.pi*((x.numerator*(qq%m))%m)/m)*np.exp(-2j*np.pi*7*float(x)/20)
    A0=I*Gfl(x); _,A1p=A01_float(a,(Fr(0),Fr(0)),x)
    ys=[]
    for t in ts:
        E=qq-0.35
        S=np.sum(ww*ph*np.exp(-t*E)); ys.append((t*S-A0)/math.sqrt(t))
    Mx=np.array([[1,t**0.5,t] for t in ts]); c=np.linalg.lstsq(Mx,np.array(ys),rcond=None)[0]
    ref=max(abs(A1p),0.05); err=abs(c[0]-A1p)/ref
    v='pass' if err<=0.02 else ('FALSIFY' if err>0.10 else 'inconclusive')
    npass+=v=='pass'; nfal+=v=='FALSIFY'
    res.append(dict(x=str(x),A1_pred=[A1p.real,A1p.imag],c1=[c[0].real,c[0].imag],err_rel=err,verdict=v))
    print(x,round(abs(A1p),6),round(err,5),v,flush=True)
verdict='falsified' if nfal else ('confirmed' if npass>=0.95*len(P) else 'inconclusive')
print('pass',npass,'of',len(P),'falsify',nfal,'->',verdict)
json.dump(dict(TAU=TAU,points=len(P),npass=npass,nfalsify=nfal,verdict=verdict,results=res),open('../data/map1_numeric.json','w'),indent=1)
