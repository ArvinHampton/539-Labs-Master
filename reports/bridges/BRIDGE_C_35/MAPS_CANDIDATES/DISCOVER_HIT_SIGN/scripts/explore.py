# DISCOVER_HIT_SIGN exploration (pre-PREREG). Lifted T3 chain on Z/M restricted to u!=0 mod 4 (Lemma V). No seeds.
import sympy as sp, json
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
def run(M):
    S=[r for r in range(M) if r%4]; ix={r:i for i,r in enumerate(S)}; n=len(S)
    P=sp.zeros(n,n)
    for r in range(3*M):
        if (r%M)%4: P[ix[r%M],ix[T3(r)%M]]+=sp.Rational(1,3)
    v=(P.T-sp.eye(n)).nullspace()[0]; v=v/sum(v)
    H=[i for i,r in enumerate(S) if r%9==3]; N=[i for i in range(n) if i not in H]
    Q=P.extract(N,N); F=P.extract(H,H)+P.extract(H,N)*(sp.eye(len(N))-Q).inv()*P.extract(N,H)
    fb=lambda i:((S[i]-21)//9)%8; w=[v[i] for i in H]; out={}
    # 2-adic facts on fibres 1,5
    fac={f:sorted({S[i]%8 for i in H if fb(i)==f}) for f in range(8)}
    G=sp.eye(len(H))
    for k in range(1,5):
        G=G*F; K=[[sp.Integer(0)]*8 for _ in range(8)]; W=[sp.Integer(0)]*8
        for x,i in enumerate(H):
            W[fb(i)]+=w[x]
            for y,j in enumerate(H): K[fb(i)][fb(j)]+=w[x]*G[x,y]
        out['K%d'%k]=[[str(sp.nsimplify(K[a][b]/W[a])) if W[a] else '-' for b in range(8)] for a in range(8)]
        out['J%d'%k]=[[str(sp.nsimplify(K[a][b])) for b in range(8)] for a in range(8)]  # joint law of (hit n, hit n+k)
    # induced chain on {1,5}-hits; sign s = chi4(u/2): u=2m, s=(-1)^((m-1)/2)
    I=[x for x,i in enumerate(H) if fb(H[x]) in (1,5)]; O=[x for x in range(len(H)) if x not in I]
    Fi=F.extract(I,I)+F.extract(I,O)*(sp.eye(len(O))-F.extract(O,O)).inv()*F.extract(O,I)
    sg=[ (-1)**(((S[H[x]]//2)-1)//2) for x in I]
    sgf={f:sorted({sg[a] for a,x in enumerate(I) if fb(H[x])==f}) for f in (1,5)}
    wi=sp.Matrix([w[x] for x in I]); wi=wi/sum(wi); sv=sp.Matrix(sg)
    out['sign_by_fibre']=sgf; out['mod8_by_fibre']=fac; out['sign_mean']=str(sp.nsimplify((wi.T*sv)[0]))
    G=sp.eye(len(I)); ac=[]
    for k in range(1,5):
        G=G*Fi; ac.append(str(sp.nsimplify((sp.diag(*wi)*G*sv).T*sv if False else sum(wi[a]*sg[a]*(G*sv)[a] for a in range(len(I))))))
    out['sign_autocorr_lag1to4']=ac
    return out
res={M:run(M) for M in (72,288)}
for M in res: print(M,json.dumps(res[M]),flush=True)
print('stable',res[72]==res[288])
json.dump(res,open('data/explore.json','w'),indent=1)
