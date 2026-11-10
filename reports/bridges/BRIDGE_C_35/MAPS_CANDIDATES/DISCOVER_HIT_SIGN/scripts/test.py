import hashlib, json, math
from fractions import Fraction as F
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
rho=[1,8,3,0,7,8,5,0]; OPEN=[0,1,2,4,5,6]
lag={k:{'A':[0]*8,'B':[0]*8} for k in (1,2,3)}
sg=[]; ac=0; npair=0; cond={'B':[0,0],'A':[0,0]}
for s in range(3000):
    u=int.from_bytes(hashlib.sha3_512(b'sign-%d'%s).digest(),'big'); hits=[]
    for _ in range(539):
        u=T3(u)
        if u%9==3: hits.append((((u-21)//9)%8,u))
    fs=[f for f,_ in hits]
    for k in (1,2,3):
        for a,b in zip(fs,fs[k:]):
            if a in OPEN and b in OPEN: lag[k]['B' if a in (1,5) else 'A'][b]+=1
    prevs=None
    for i,(f,u) in enumerate(hits):
        if f in (1,5):
            m=u//2; sv=-1 if (m%4)==3 else 1
            assert u%2==0 and m%2==1 and sv==(-1 if f==1 else 1)
            sg.append(sv)
            if prevs is not None: ac+=prevs*sv; npair+=1
            prevs=sv
            if i>0 and fs[i-1] in OPEN:
                c=cond['B' if fs[i-1] in (1,5) else 'A']; c[0]+=sv; c[1]+=1
def chi(c):
    n=sum(c[i] for i in OPEN); return sum((c[i]-n*rho[i]/32)**2/(n*rho[i]/32) for i in OPEN)
n=len(sg); r={}
r['H1A'],r['H1B']=chi(lag[2]['A']),chi(lag[2]['B'])
r['H2A'],r['H2B']=chi(lag[3]['A']),chi(lag[3]['B'])
r['H3']=chi(lag[1]['B'])
r['S1']=sum(sg)/n; r['S1thr']=4/math.sqrt(n)
r['S2']=ac/npair; r['S2thr']=4/math.sqrt(npair)
mB=cond['B'][0]/cond['B'][1]; mA=cond['A'][0]/cond['A'][1]
sB=math.sqrt((1-mB**2)/cond['B'][1]); sA=math.sqrt((1-mA**2)/cond['A'][1])
r.update(mB=mB,mA=mA,nB=cond['B'][1],nA=cond['A'][1],zB=(mB+1/6)/sB,zA=(mA-1/6)/sA,S4z=(mA-mB)/math.hypot(sA,sB))
r['lag']=lag; r['n_sign']=n
p=dict(H1=r['H1A']<=20.52 and r['H1B']<=20.52,H2=r['H2A']<=20.52 and r['H2B']<=20.52,H3=r['H3']>20.52,
 S1=abs(r['S1'])<=r['S1thr'],S2=abs(r['S2'])<=r['S2thr'],S3=abs(r['zB'])<=4 and abs(r['zA'])<=4,S4=r['S4z']>4)
r['pass']=p; r['overall']='PASS' if all(p.values()) else ('VACUOUS' if all(v for k,v in p.items() if k not in('H3','S4')) else 'FAIL')
print(json.dumps(r)); json.dump(r,open('data/test.json','w'),indent=1)
