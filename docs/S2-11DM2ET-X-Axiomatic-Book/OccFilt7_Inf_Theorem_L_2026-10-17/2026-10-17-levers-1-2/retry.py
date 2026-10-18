# (a) residue split h_j(p)=sum_m p^{7m^2+2mj}/(-p;p)_{7m+j};  (b) Bailey inversion relative to a=q (and a=1 recheck), base q
N=300
def mul(a,b):
    c=[0]*N
    for i,x in enumerate(a):
        if x:
            for j in range(N-i):
                if b[j]: c[i+j]+=x*b[j]
    return c
def inv(a):
    b=[0]*N;b[0]=1
    for n in range(1,N): b[n]=-sum(a[k]*b[n-k] for k in range(1,n+1) if a[k])
    return b
one=[1]+[0]*(N-1)
def qp(n,base,sign,shift=0):  # prod_{j=1..n}(1+sign q^{base*j+shift})
    r=one[:]
    for j in range(1,n+1):
        f=one[:]; e=base*j+shift
        if e<N: f[e]+=sign
        r=mul(r,f)
    return r
for j in range(7):
    h=[0]*N; m=0
    while 7*m*m+2*m*j<N:
        t=inv(qp(7*m+j,1,+1)); e=7*m*m+2*m*j
        for i in range(N-e): h[e+i]+=t[i]
        m+=1
    print(f"h_{j}:",h[:30])
# (b) a=q: beta_n = sum_r alpha_r/((q)_{n-r}(q^2;q)_{n+r})
for s in (1,7):
    K=6
    beta=[inv(qp(n,s,+1)) for n in range(K)]
    al=[]
    for n in range(K):
        acc=beta[n][:]
        for r in range(n):
            t=mul(al[r],inv(mul(qp(n-r,1,-1),qp(n+r,1,-1,1))))
            acc=[x-y for x,y in zip(acc,t)]
        al.append(mul(acc,mul(qp(2*n,1,-1,1),one)))
    print(f"a=q, s={s}:",[ (max([i for i,x in enumerate(a) if x]), sum(1 for x in a if x)) for a in al])
