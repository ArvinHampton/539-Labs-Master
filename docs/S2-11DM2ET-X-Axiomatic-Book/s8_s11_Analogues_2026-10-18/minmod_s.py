# Minimal modulus: for which m' = prod P^e * (infinite places) is the multiset {a(nu): nu in F} a union of FULL
# ray classes mod m' (after splitting off the m'-supported part c)?  Report all minimal (finite part, inf) and #classes hit.
import cypari2, numpy as np, math, sys, itertools
from fractions import Fraction as Fr
from collections import defaultdict, Counter
pari=cypari2.Pari(); pari.allocatemem(4*10**9)
CFG={7:(35,1,[(2,4),(5,2)]),8:(3,4,[(2,6),(3,2)]),11:(11,3,[(2,4),(3,2)])}
Nmax=int(sys.argv[1]) if len(sys.argv)>1 else 2000
pp=pari('(P)->P.p')
out=[]
for s in [int(z) for z in sys.argv[2].split(',')]:
    D0,c,pex=CFG[s]; d=2*(s-2)
    K=pari(f'bnfinit(x^2-{D0},1)'); w=pari('Mod(x,x^2-%d)'%D0)
    a=(Fr(s,2*(s-2)),Fr(-1,s-2)); X0=(int(d*a[0]),int(d*a[1]))
    beta=lambda X1,X2:(2*X1+s*X2)+c*X2*w
    Dp=pari.idealhnf(K,beta(*X0))
    for gg in (beta(d,0),beta(0,d)): Dp=pari.idealadd(K,Dp,gg)
    NDp=int(pari.idealnorm(K,Dp))
    g=np.array([[-1,-s],[2,2*s-1]]); gr=g@np.array((1,0))
    Qmax=Fr(Nmax*NDp,4*d*d); B=int(6*math.sqrt(float(Qmax)))+10
    ideals=[]
    for n in range(-B,B+1):
        for k in range(-B,B+1):
            X1=d*n+X0[0]; X2=d*k+X0[1]
            if not ((X1*gr[1]-X2*gr[0])>0 and X2>=0): continue
            Q=Fr(X1*X1+s*X1*X2,d*d)+Fr(s*X2*X2,2*d*d)
            if Q>Qmax: continue
            ideals.append(pari.idealdiv(K,beta(X1,X2),Dp))
    cnt=Counter(int(pari.idealnorm(K,J)) for J in ideals)
    L=pari.ideallist(K,Nmax)
    allid=[(nn,J) for nn in range(1,Nmax+1) for J in L[nn-1]]
    # prime ideals over the primes involved
    primes=[]
    for p,emax in pex:
        for P in pari.idealprimedec(K,p):
            e=int(pari('(P)->P.e')(P)); primes.append((P,emax*e//2 if e==2 else emax//1))
    results=[]
    ranges=[range(0,m+1) for _,m in primes]
    for exps in itertools.product(*ranges):
        mod=pari.idealhnf(K,1)
        for (P,_),e in zip(primes,exps): mod=pari.idealmul(K,mod,pari.idealpow(K,P,e))
        sup=[P for (P,_),e in zip(primes,exps) if e>0]
        for inf in ([0,0],[1,0],[0,1],[1,1]):
            bnr=pari.bnrinit(K,[mod,inf],1)
            h=int(pari('(b)->b.no')(bnr))
            def split(J):
                cp=[]; Jp=J
                for P in sup:
                    v=int(pari.idealval(K,J,P))
                    if v: cp.append((str(P),v)); Jp=pari.idealdiv(K,Jp,pari.idealpow(K,P,v))
                return tuple(cp),Jp
            hit=set()
            for J in ideals:
                cp,Jp=split(J); hit.add((cp,tuple(int(z) for z in pari.bnrisprincipal(bnr,Jp,0))))
            pred=Counter()
            for nn,J in allid:
                cp,Jp=split(J)
                if (cp,tuple(int(z) for z in pari.bnrisprincipal(bnr,Jp,0))) in hit: pred[nn]+=1
            ok=all(pred[n]==cnt[n] for n in range(1,Nmax+1))
            if ok: results.append((int(pari.idealnorm(K,mod)),sum(inf),exps,inf,h,len(hit),Counter(cp for cp,_ in hit)))
    results.sort()
    # keep minimal ones (not divisible by another passing modulus)
    out.append(f"s={s}: Q(sqrt{D0}); primes {[(str(pari('(P)->P.gen')(P)),m) for P,m in primes]}; passing moduli (norm, #inf, exps, inf, |Cl_m^+|, #(c,class) hit, c-parts):")
    for r in results[:12]: out.append("   "+str(r))
    print("\n".join(out),flush=True); out=[]
