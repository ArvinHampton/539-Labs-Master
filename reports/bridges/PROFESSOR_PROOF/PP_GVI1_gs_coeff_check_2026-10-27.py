import math,sys
M=16000
for s in (7,8,11):
    tot=[0]*(M+1); 
    # term_n = q^{n^2} * prod_{k=1..n} 1/(1+q^{sk})
    P=[0]*(M+1); P[0]=1; n=0
    while n*n<=M:
        if n>0:
            d=s*n
            for i in range(d,M+1): P[i]-=P[i-d]
        for i in range(0,M+1-n*n): tot[i+n*n]+=P[i]
        n+=1
    print("s",s)
    for N in (4000,8000,12000,16000):
        w=tot[N-20:N+1]; mx=max(abs(x) for x in w)
        print(N, "maxabs",mx, "log/sqrtN",(math.log(mx)/math.sqrt(N) if mx>0 else None), "pred beta",math.pi/(2*math.sqrt(6)*s))
