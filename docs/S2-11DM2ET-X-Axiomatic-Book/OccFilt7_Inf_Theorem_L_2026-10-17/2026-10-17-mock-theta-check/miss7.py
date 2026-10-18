D=3000; M=D//7+1
# phi_n(m) table via incremental product prod 1/(1+x^j)
import math
phi=[1]+[0]*M; tabs=[phi[:]]
nmax=int(math.isqrt(D))
for j in range(1,nmax+1):
    p=tabs[-1][:]
    for m in range(j,M+1): p[m]-=p[m-j]
    tabs.append(p)
g=[sum(tabs[n][(d-n*n)//7] for n in range(nmax+1) if n*n<=d and (d-n*n)%7==0) for d in range(D+1)]
miss=[d for d in range(D+1) if d%7 in (0,1,2,4) and g[d]==0]
print(len(miss),miss)
print("off-class nonzero:",[d for d in range(D+1) if d%7 not in (0,1,2,4) and g[d]!=0][:5])
