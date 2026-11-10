# Exploration 2 (pre-PREREG): next-hit fibre kernel K[a][b] = P(next hit fibre=b | current hit fibre=a), stationary-weighted, exact.
import sympy as sp, json
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
def kernel(M):
    S=[r for r in range(M) if r%4!=0]; idx={r:i for i,r in enumerate(S)}; n=len(S)
    P=sp.zeros(n,n)
    for r in range(3*M):
        a=r%M
        if a%4: P[idx[a],idx[T3(r)%M]]+=sp.Rational(1,3)
    v=(P.T-sp.eye(n)).nullspace()[0]; v=v/sum(v)
    H=[i for i,r in enumerate(S) if r%9==3]; N=[i for i in range(n) if i not in H]
    Q=P.extract(N,N); R=P.extract(N,H); B=P.extract(H,H); C=P.extract(H,N)
    F=B+C*(sp.eye(len(N))-Q).inv()*R   # hit -> next hit
    fb=lambda i:((S[i]-21)//9)%8
    K=[[sp.Integer(0)]*8 for _ in range(8)]; w=[sp.Integer(0)]*8
    for x,i in enumerate(H):
        w[fb(i)]+=v[i]
        for y,j in enumerate(H): K[fb(i)][fb(j)]+=v[i]*F[x,y]
    return [[str(sp.nsimplify(K[a][b]/w[a])) if w[a] else '-' for b in range(8)] for a in range(8)]
out={M:kernel(M) for M in [72,144,288]}
for M,k in out.items(): print(M,k,flush=True)
print('stable72=288',out[72]==out[288],'stable144=288',out[144]==out[288])
json.dump(out,open('data/explore2.json','w'),indent=1)
