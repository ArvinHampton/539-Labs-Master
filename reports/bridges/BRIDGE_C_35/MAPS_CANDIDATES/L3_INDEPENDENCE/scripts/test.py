import json,sys,hashlib; sys.path.insert(0,'scripts'); from common import *
R={}
for m in (8,64):
    J={}
    for d in range(6000):
        u=int.from_bytes(hashlib.sha3_512(b'l3holdout-%d'%d).digest(),'big')
        for i in range(539):
            u=T3(u)
            if i>=20 and (i-20)%8==0: k=(u%3,u%m); J[k]=J.get(k,0)+1
    R[m]=stats(J,m)
fib=[0]*8;h=0
for d in range(6000):
    u=int.from_bytes(hashlib.sha3_512(b'l3holdout-%d'%d).digest(),'big')
    for i in range(539):
        u=T3(u)
        if i>=20 and u%9==3: h+=1; fib[((u-21)//9)%8]+=1
p=[1,8,3,0,7,8,5,0]; meas=[c/h for c in fib]; N=sum(fib[j] for j in (0,1,2,4,5,6))
chi=sum((fib[j]-N*p[j]/32)**2/(N*p[j]/32) for j in (0,1,2,4,5,6)); md=max(abs(meas[j]-p[j]/32) for j in range(8))
a=R[8]; A={'A1':a['chi_ind']<=29.59,'A2':a['chi_full']<=40.79 and a['tv_full']<=0.006,'A3':a['maxdev_cond']<=0.02,'A4':R[64]['chi_ind']<=142.12,'A5':a['bad_mod4']==0 and R[64]['bad_mod4']==0}
out=dict(mod8=R[8],mod64={k:v for k,v in R[64].items() if k!='m2'},checks=A,L3a='PASS' if all(A.values()) else 'FAIL',
 L3b=dict(hits=h,counts=fib,measured=meas,maxdev=md,chi2=chi,verdict='PASS' if md<=0.005 and chi<=20.52 else 'FAIL'))
json.dump(out,open('data/test.json','w'),indent=1,default=str); print(json.dumps(out,default=str))
