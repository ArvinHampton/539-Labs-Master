import cypari2, numpy as np, math
from fractions import Fraction as Fr
pari=cypari2.Pari(); pari.allocatemem(2*10**9)
CFG={7:(35,1),8:(3,4),11:(11,3)}
for s in (7,8,11):
    D0,c=CFG[s]; d=2*(s-2)
    K=pari(f'bnfinit(x^2-{D0},1)')
    print("s=",s,"field Q(sqrt",D0,") disc",pari(f'{K}.disc') if False else pari.nfdisc(f'x^2-{D0}'),"h=",K.bnf_get_no(),"fu=",pari(f'lift({K}.fu)') if False else pari('lift')(K.bnf_get_fu()))
    w=pari('Mod(x,x^2-%d)'%D0)
    a=(Fr(s,2*(s-2)),Fr(-1,s-2)); X0=(int(d*a[0]),int(d*a[1]))
    def beta(X1,X2): return (2*X1+s*X2)+c*X2*w
    b0=beta(*X0); gens=[b0,beta(d,0),beta(0,d)]
    Dp=pari.idealhnf(K,gens[0])
    for gg in gens[1:]: Dp=pari.idealadd(K,Dp,gg)
    print("  d'=",pari.idealfactor(K,Dp), " N(d')=",pari.idealnorm(K,Dp))
    # points in gamma-cone [e1, g e1)
    g=np.array([[-1,-s],[2,2*s-1]]); gr=g@np.array((1,0))
    facs={}
    for n in range(-60,61):
        for k in range(-60,61):
            X1=d*n+X0[0]; X2=d*k+X0[1]
            if not ((X1*gr[1]-X2*gr[0])>0 and X2>=0): continue
            Q=Fr(X1*X1+s*X1*X2,d*d)+Fr(s*X2*X2,2*d*d)
            if Q>12: continue
            A_=pari.idealdiv(K,beta(X1,X2),Dp)
            f=pari.idealfactor(K,A_)
            ps=tuple(sorted(set(int(pari.idealnorm(K,f[0][i])) for i in range(len(f[0])))))
            facs.setdefault(int(Q*pari.idealnorm(K,Dp)/Q if False else 0),[])
            facs[0].append((float(Q),int(pari.idealnorm(K,A_)),ps,str(pari.nfbasistoalg(K,pari.nfeltsign(K,beta(X1,X2))) if False else '')))
    L=sorted(facs[0])[:14]
    for q,nA,ps,_ in L: print(f"   Q2={q:.4f}  N(a)={nA}  N(a)/Q2={nA/q:.4f}  prime norms dividing a: {ps}")
