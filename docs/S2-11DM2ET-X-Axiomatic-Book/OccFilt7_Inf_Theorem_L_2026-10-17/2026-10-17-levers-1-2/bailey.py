# Bailey-pair inversion relative to a=1: beta_n = sum_r alpha_r/((q)_{n-r}(q)_{n+r})
import sys
N=int(sys.argv[2]) if len(sys.argv)>2 else 400
s=int(sys.argv[1])
def mul(a,b):
    c=[0]*N
    for i,x in enumerate(a):
        if x:
            for j in range(N-i):
                if b[j]: c[i+j]+=x*b[j]
    return c
def inv(a):
    b=[0]*N; b[0]=1
    for n in range(1,N):
        b[n]=-sum(a[k]*b[n-k] for k in range(1,n+1) if a[k])
    return b
one=[1]+[0]*(N-1)
def qp(n,base=1,sign=-1):  # prod_{j=1..n}(1+sign q^{base j})
    r=one[:]
    for j in range(1,n+1):
        f=one[:]
        if base*j<N: f[base*j]+=sign
        r=mul(r,f)
    return r
K=8
qpinv=[inv(qp(m)) for m in range(2*K+1)]
beta=[inv(qp(n,s,+1)) for n in range(K)]
alpha=[]
for n in range(K):
    acc=beta[n][:]
    for r in range(n):
        t=mul(alpha[r],mul(qpinv[n-r],qpinv[n+r]))
        acc=[x-y for x,y in zip(acc,t)]
    alpha.append(mul(acc,qp(2*n)))
for n,a in enumerate(alpha):
    nz=[i for i,x in enumerate(a) if x]
    print(f"s={s} n={n} nnz={len(nz)} maxdeg={max(nz) if nz else None} tailnz(>N-50)={sum(1 for i in nz if i>N-50)} first={[(i,a[i]) for i in nz[:8]]}")
