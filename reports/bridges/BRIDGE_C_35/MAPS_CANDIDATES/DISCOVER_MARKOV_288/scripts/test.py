import hashlib, json
from fractions import Fraction as F
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
rho=[F(1,32),F(8,32),F(3,32),0,F(7,32),F(8,32),F(5,32),0]
A=[F(1,32),F(5,24),F(3,32),0,F(7,32),F(7,24),F(5,32),0]
B=[F(1,32),F(7,24),F(3,32),0,F(7,32),F(5,24),F(5,32),0]
OPEN=[0,1,2,4,5,6]
cnt=[0]*8; pa=[0]*8; pb=[0]*8; nh=0
for s in range(3000):
    u=int.from_bytes(hashlib.sha3_512(b'fresh-%d'%s).digest(),'big'); prev=None
    for _ in range(539):
        u=T3(u)
        if u%9==3:
            f=((u-21)//9)%8; cnt[f]+=1; nh+=1
            if prev is not None and prev in OPEN and f in OPEN:
                (pb if prev in (1,5) else pa)[f]+=1
            prev=f
def chi(c,p):
    n=sum(c[i] for i in OPEN); z=sum(p[i] for i in OPEN)
    return float(sum((c[i]-n*p[i]/z)**2/(n*p[i]/z) for i in OPEN))
r=dict(steps=3000*539,hits=nh,counts=cnt,pairsA=pa,pairsB=pb,
 T1=chi(cnt,rho),T2=(cnt[3]+cnt[7])/nh,T3a=chi(pa,A),T3b=chi(pb,B),T4=chi(pb,rho))
r['pass']=dict(T1=r['T1']<=20.52,T2=r['T2']<=1e-3,T3a=r['T3a']<=20.52,T3b=r['T3b']<=20.52,T4=r['T4']>20.52)
print(json.dumps(r)); json.dump(r,open('data/test.json','w'),indent=1)
