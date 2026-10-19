# C = P_orth - H_s at s=7, c1=(-1,1), c2=(-4,1); exact coefficients (Fractions) to degree N
from fractions import Fraction as F
import json
s=7; N=420
Q=lambda n,k: n*n+s*n*k+(s*k*(k+1))//2   # s k(k+1)/2 integer
A=[[2,s],[s,s]]
B=lambda c,v: c[0]*(A[0][0]*v[0]+A[0][1]*v[1])+c[1]*(A[1][0]*v[0]+A[1][1]*v[1])
sg=lambda x: (x>0)-(x<0)
c1=(-1,1); c2=(-4,1)
C=[F(0)]*N
R=200
for n in range(-R,R+1):
    for k in range(-R,R+1):
        q=Q(n,k)
        if 0<=q<N:
            w=F(sg(B(c1,(n,k)))-sg(B(c2,(n,k))),2)
            orth=1 if (n>=0 and k>=0) else 0
            C[q]+=orth-w
vals=sorted(set(C[:N]))
first_out=[(i,str(C[i])) for i in range(N) if C[i] not in (F(0),F(1),F(3,2))][:8]
print('value set to q^%d:'%(N-1),[str(v) for v in vals]); print('first outside {0,1,3/2}:',first_out)
json.dump({'N':N,'values':[str(v) for v in vals],'first_outside':first_out},open('cvals.json','w'),indent=1)
# cross-check with rev6 Thm A(iv): Cmixed = C - Caxis - Cthird
Ca=[F(0)]*N; Ca[0]=F(3,2)
for n in range(1,N):
    if n*n<N: Ca[n*n]+=1
for k in range(1,N):
    t=s*k*(k+1)//2
    if t<N: Ca[t]+=1
Ct=[F(0)]*N
for n in range(1,N):
    for k in range(1,N):
        e=n*n+s*n*k+(s*k*(k-1))//2
        if e<N: Ct[e]+=1
Cm=[C[i]-Ca[i]-Ct[i] for i in range(N)]
nz=[(i,str(Cm[i])) for i in range(N) if Cm[i]!=0][:6]
print('Cmixed first nonzero:',nz)
print('C at 102:',C[102],'Caxis',Ca[102],'Cthird',Ct[102])
