# Step (2): E_s as a ray-class generating function.  For nu in F=[e1, gamma e1) cap (a+Z^2):
#   beta(nu) = (2X1+sX2) + c X2 sqrt(D0)  (X = d nu, d = 2(s-2)),  N(beta) = 4 d^2 Q2(nu);
#   frak a(nu) := (beta) * d'^{-1}, d' = gcd ideal of the coset module.
# Decompose frak a = c * a' with c supported on primes | m and a' coprime to m; record (c, class of a' in Cl_m^+ (narrow ray)),
# then check counts against PARI's independent ideal enumeration: for every n <= Nmax,
#   #{nu : N a(nu) = n} == sum_{(c,cls) hit} mu * #{a' in cls : N a' = n/Nc}.
import cypari2, numpy as np, math, sys, json
from fractions import Fraction as Fr
from collections import defaultdict, Counter
pari=cypari2.Pari(); pari.allocatemem(4*10**9)
CFG={7:(35,1,'20'),8:(3,4,'24'),11:(11,3,'36')}
Nmax=int(sys.argv[1]) if len(sys.argv)>1 else 6000
SS=[int(z) for z in sys.argv[2].split(',')] if len(sys.argv)>2 else [7,8,11]
pp=pari('(P)->P.p'); pg=pari('(P)->P.gen[2]')
out=[]; res={}
for s in SS:
    D0,c,mstr=CFG[s]; d=2*(s-2)
    K=pari(f'bnfinit(x^2-{D0},1)')
    w=pari('Mod(x,x^2-%d)'%D0)
    a=(Fr(s,2*(s-2)),Fr(-1,s-2)); X0=(int(d*a[0]),int(d*a[1]))
    def beta(X1,X2): return (2*X1+s*X2)+c*X2*w
    Dp=pari.idealhnf(K,beta(*X0))
    for gg in (beta(d,0),beta(0,d)): Dp=pari.idealadd(K,Dp,gg)
    NDp=int(pari.idealnorm(K,Dp))
    bnr=pari.bnrinit(K,pari(f'[{mstr},[1,1]]'),1)
    cyc=[int(z) for z in pari('(b)->b.cyc')(bnr)]
    mprimes=[int(p) for p in pari.factor(int(mstr))[0]]
    g=np.array([[-1,-s],[2,2*s-1]]); gr=g@np.array((1,0))
    Qmax=Fr(Nmax*NDp,4*d*d)
    B=int(6*math.sqrt(float(Qmax)))+10
    cnt_nu=Counter(); S=Counter(); mult=Counter()
    for n in range(-B,B+1):
        for k in range(-B,B+1):
            X1=d*n+X0[0]; X2=d*k+X0[1]
            if not ((X1*gr[1]-X2*gr[0])>0 and X2>=0): continue
            Q=Fr(X1*X1+s*X1*X2,d*d)+Fr(s*X2*X2,2*d*d)
            if Q>Qmax: continue
            assert abs(n)<B-2 and abs(k)<B-2
            bt=beta(X1,X2); Aid=pari.idealdiv(K,bt,Dp); nA=int(pari.idealnorm(K,Aid))
            assert Fr(nA)==4*d*d*Q/NDp
            cnt_nu[nA]+=1
            f=pari.idealfactor(K,Aid); cpart=[]; Ap=Aid
            for i in range(len(f[0])):
                P=f[0][i]; e=int(f[1][i])
                if int(pp(P)) in mprimes:
                    cpart.append((int(pp(P)),str(pg(P)),e)); Ap=pari.idealdiv(K,Ap,pari.idealpow(K,P,e))
            cl=tuple(int(z) for z in pari.bnrisprincipal(bnr,Ap,0))
            S[(tuple(sorted(cpart)),cl)]+=1
            mult[str(pari.idealhnf(K,Aid))]+=1
    multset=Counter(mult.values())
    L=pari.ideallist(K,Nmax)
    byclass=defaultdict(Counter)
    for nn in range(1,Nmax+1):
        if any(nn%p==0 for p in mprimes): continue
        for J in L[nn-1]:
            byclass[tuple(int(z) for z in pari.bnrisprincipal(bnr,J,0))][nn]+=1
    def Nc(cp):
        r=1
        for p,gstr,e in cp:
            P=[Pp for Pp in pari.idealprimedec(K,p) if str(pg(Pp))==gstr][0]
            r*=int(pari.idealnorm(K,P))**e
        return r
    cparts=Counter()
    for (cp,cl) in S: cparts[cp]+=1
    mu=max(multset); keys=set(S.keys()); pred=Counter()
    for (cp,cl) in keys:
        nc=Nc(cp)
        for nn,v in byclass[cl].items():
            if nn*nc<=Nmax: pred[nn*nc]+=v*mu
    dev=max(abs(pred[n]-cnt_nu[n]) for n in range(1,Nmax+1))
    out.append(f"s={s}: K=Q(sqrt{D0}), d'={pari.idealfactor(K,Dp)} (N d'={NDp}), N(a)={Fr(4*d*d,NDp)}*Q2; modulus m=({mstr})*oo1*oo2, Cl_m^+ = {cyc}")
    out.append(f"   multiplicity of ideals among nu in F: {dict(multset)}; m-parts c occurring (#classes each): {dict(cparts)}")
    out.append(f"   distinct (c,class) hit: {len(keys)}; count check vs PARI ideal enumeration, N a <= {Nmax}, multiplicity {mu}: max|diff| = {dev}")
    res[s]={'cyc':cyc,'keys':[[[list(x) for x in cp],list(cl)] for cp,cl in keys],'mu':mu,'NDp':NDp}
    print("\n".join(out[-3:]),flush=True)
open("rayclass_s_%s.txt"%("_".join(map(str,SS))),"w").write("\n".join(out)+"\n"); json.dump(res,open("rayclass_s_%s.json"%("_".join(map(str,SS))),"w"))
