# Check Lemma A3 consequence E_d <= O*_d := sum_{n odd} a_n((d-(n+1)^2)/7), and ratios E/O*, O*/O (heuristic limit y=0.83983)
import math,sys
D=int(sys.argv[1]);M=D//7+1;nmax=math.isqrt(D)
p=[1]+[0]*M;E=[0]*(D+1);O=[0]*(D+1);Os=[0]*(D+1)
for n in range(nmax+1):
    if n:
        for m in range(n,M+1): p[m]-=p[m-n]
    a=[p[m] if m%2==0 else -p[m] for m in range(M+1)]
    for m in range(0,(D-n*n)//7+1):
        (E if n%2==0 else O)[n*n+7*m]+=a[m]
    if n%2==1:
        for m in range(0,(D-(n+1)**2)//7+1) if (n+1)**2<=D else []:
            Os[(n+1)**2+7*m]+=a[m]
viol=[d for d in range(1,D+1) if E[d]>Os[d]]
print('E_d<=O*_d for all 1<=d<=D:',not viol, viol[:10])
for c in (0,1,2,4):
    bad=[d for d in range(D+1) if d%7==c and O[d]<=Os[d] and O[d]>0]
    print('class',c,'last d with O*_d>=O_d:',bad[-1] if bad else None)
for d in [1000,10000,D-13]:
    print([(dd,round(Os[dd]/O[dd],6),round(E[dd]/Os[dd],6)) for dd in range(d,d+7) if dd%7 in (0,1,2,4)])
