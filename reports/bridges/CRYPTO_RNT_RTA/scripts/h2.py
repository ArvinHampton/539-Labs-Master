import json
N=20000; ks=range(60,77); M=N//60+1; NM=int(N**.5)+1
# phi[n][m] coefficients of prod_{j<=n}(1+x^j)^{-1}, m<=M
phi=[]; cur=[1]+[0]*M; phi.append(cur[:])
for j in range(1,NM+1):
    # divide by (1+x^j): c[m]-=c[m-j]
    c=cur[:]
    for m in range(j,M+1): c[m]-=c[m-j]
    cur=c; phi.append(c[:])
res={}
for k in ks:
    g=[0]*(N+1)
    for n in range(NM+1):
        if n*n>N: break
        for m in range(0,(N-n*n)//k+1):
            g[n*n+k*m]+=phi[n][m]
    sq={x*x%k for x in range(k)}
    zeros=[d for d in range(N+1) if d%k in sq and g[d]==0]
    res[k]=dict(Z=len(zeros),zeros=zeros if k in(68,17,67) else zeros[:40],late=[d for d in zeros if d>2000])
print(json.dumps({k:{'Z':v['Z'],'late':v['late'][:50]} for k,v in res.items()}))
json.dump(res,open('logs/h2_full.json','w'))
