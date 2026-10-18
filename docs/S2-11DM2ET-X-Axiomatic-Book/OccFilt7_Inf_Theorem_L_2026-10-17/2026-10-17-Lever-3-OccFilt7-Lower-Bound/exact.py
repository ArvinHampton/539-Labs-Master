# exact big-integer g_7(d) for d<=D (Python ints); writes data/exact_D.txt.gz  (d g)
import math,sys,gzip
D=int(sys.argv[1]);M=D//7+1;nmax=math.isqrt(D)
p=[1]+[0]*M;g=[0]*(D+1)
for n in range(nmax+1):
    if n:
        for m in range(n,M+1): p[m]-=p[m-n]
    for m in range(0,(D-n*n)//7+1): g[n*n+7*m]+=p[m]
with gzip.open(f'data/exact_{D}.txt.gz','wt') as f:
    for d in range(D+1): f.write(f'{d} {g[d]}\n')
miss=[d for d in range(D+1) if d%7 in (0,1,2,4) and g[d]==0]
print('D',D,'zeros in allowed classes:',len(miss),miss)
