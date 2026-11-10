import json, hashlib
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
p=[1,8,3,0,7,8,5,0]; fib=[0]*8; h=0; n=0
for d in range(3000):
    u=int.from_bytes(hashlib.sha3_512(b'mfholdout-%d'%d).digest(),'big')
    for i in range(539):
        u=T3(u); n+=1
        if u%9==3: h+=1; fib[((u-21)//9)%8]+=1
O=[0,1,2,4,5,6]; N=sum(fib[j] for j in O)
chi=sum((fib[j]-N*p[j]/32)**2/(N*p[j]/32) for j in O)
chiu=sum((fib[j]-N/6)**2/(N/6) for j in O)
s37=(fib[3]+fib[7])/h
R=dict(steps=n,hits=h,hitfrac=h/n,counts=fib,measured=[c/h for c in fib],predicted=[x/32 for x in p],
 M1=dict(chi2=chi,verdict='PASS' if chi<=20.52 else 'FAIL'),M2=dict(share37=s37,verdict='PASS' if s37<=1e-3 else 'FAIL'),
 M3=dict(chi2_uniform=chiu,verdict='PASS' if chiu>20.52 else 'FAIL'))
R['overall']='PASS' if all(R[m]['verdict']=='PASS' for m in ('M1','M2','M3')) else ('VACUOUS' if R['M1']['verdict']=='PASS' and R['M3']['verdict']=='FAIL' else 'FAIL')
json.dump(R,open('data/test.json','w'),indent=1); print(json.dumps(R))
