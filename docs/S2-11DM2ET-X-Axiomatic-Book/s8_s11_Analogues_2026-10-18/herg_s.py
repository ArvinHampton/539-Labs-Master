# Step (5): the s=7 Herglotz template for general s.
#  E_L(tau) (S+ cone of coset a) = sum_{C-part c} sum_chi Fhat_c(chi) theta^{coprime}_chi(lambda_c tau), lambda_c = N(d')N(c)/(4D^2);
#  sigma-invariant chi = psi o N  =>  theta = G_{a,b}, a = psi*1_{(.,P)=1}, b = psi*chi_D*1_{(.,P)=1}  (Lambert double series);
#  Herglotz:  Psi_Eis(z) = sum_c sum_{chi Eis} 2 Fhat_c(chi) R_chi(z),  R(z) = sum_m a(m) sum_{s=1}^{Nb} rho_s digamma(s/Nb + lambda_c m / z).
import cypari2, numpy as np, math, cmath, itertools, sys, pickle
from fractions import Fraction as Fr
from scipy.special import digamma, zeta as hzeta
import sympy
pari=cypari2.Pari(); pari.allocatemem(10**9)
CFG={7:(35,1,[(2,1),(5,1)]),8:(3,4,[(2,2),(3,1)]),11:(11,3,[(2,1),(3,2)])}
def setup(s):
    D0,c,pe=CFG[s]; d=2*(s-2)
    K=pari(f'bnfinit(x^2-{D0},1)'); w=pari('Mod(x,x^2-%d)'%D0); dK=int(pari('(K)->K.disc')(K))
    sig=[g for g in pari.nfgaloisconj(K) if str(g)!='x'][0]
    mod=pari.idealhnf(K,1); Ps=[]
    for p,e in pe:
        for P in pari.idealprimedec(K,p): Ps.append(P); mod=pari.idealmul(K,mod,pari.idealpow(K,P,e))
    bnr=pari.bnrinit(K,[mod,[1,1]],1); cyc=[int(z) for z in pari('(b)->b.cyc')(bnr)]; h=math.prod(cyc)
    cl=lambda J: tuple(int(z) for z in pari.bnrisprincipal(bnr,J,0))
    a=(Fr(s,2*(s-2)),Fr(-1,s-2)); X0=(int(d*a[0]),int(d*a[1])); beta=lambda X1,X2:(2*X1+s*X2)+c*X2*w
    Dp=pari.idealhnf(K,beta(*X0))
    for gg in (beta(d,0),beta(0,d)): Dp=pari.idealadd(K,Dp,gg)
    NDp=int(pari.idealnorm(K,Dp))
    hits={}
    for n in range(-40,41):
        for k in range(0,41):
            X1=d*n+X0[0]; X2=d*k+X0[1]
            if not (X2>=0 and 2*X1+X2>0): continue
            J=pari.idealdiv(K,beta(X1,X2),Dp); Cp=[]; Jp=J
            for P in Ps:
                v=int(pari.idealval(K,J,P)); Cp.append(v)
                if v: Jp=pari.idealdiv(K,Jp,pari.idealpow(K,P,v))
            hits.setdefault(tuple(Cp),set()).add(cl(Jp))
    NP=[int(pari.idealnorm(K,P)) for P in Ps]
    gens=pari('(b)->b.gen')(bnr)
    Sg=np.array([[int(z) for z in cl(pari.nfgaloisapply(K,sig,g))] for g in gens]).T
    allc=list(itertools.product(*[range(m) for m in cyc]))
    sgc=lambda x: tuple(int(v)%m for v,m in zip(Sg@np.array(x),cyc))
    ev=lambda ch,x: cmath.exp(2j*math.pi*sum(cc*v/m for cc,v,m in zip(ch,x,cyc)))
    E1=[tuple(int(i==j) for i in range(len(cyc))) for j in range(len(cyc))]
    inv=lambda ch: all(abs(ev(ch,sgc(e))-ev(ch,e))<1e-9 for e in E1)
    Nm=int(pari.idealnorm(K,mod)); dd=cl(pari.idealhnf(K,1-1000*Nm)); dpm=cl(pari.idealhnf(K,1+1000*Nm*w))
    # content per C-part of the sigma-symmetrised indicator
    content={}
    for Cp,S in hits.items():
        Fs={x:0.0 for x in allc}
        for x in S: Fs[x]+=0.5; Fs[sgc(x)]+=0.5
        lam=Fr(NDp*math.prod(n**v for n,v in zip(NP,Cp)),4*d*d)
        content[Cp]=(lam,{ch:sum(Fs[x]*ev(ch,x).conjugate() for x in allc)/h for ch in allc})
    # Dirichlet psi for sigma-invariant chi
    m0=int(pari.idealhnf(K,mod)[0][0]) if False else int(pari('(K,m)->idealhnf(K,m)[1,1]')(K,mod))
    M=2*m0
    G=pari.znstar(M,1); zcyc=[int(z) for z in pari('(G)->G.cyc')(G)]
    primes=[]
    for p in sympy.primerange(2,1500):
        for P in pari.idealprimedec(K,p):
            if any(int(pari.idealval(K,P,Q))>0 for Q in Ps): continue
            primes.append((int(pari.idealnorm(K,P)),cl(P)))
    def psi_val(zc,n):
        if math.gcd(n,M)!=1: return 0
        return complex(pari.chareval(G,zc,n,[-1,0])) if False else cmath.exp(2j*math.pi*float(pari.chareval(G,zc,n)))
    zchars=list(itertools.product(*[range(m) for m in zcyc]))
    psiv={zc:{n:psi_val(list(zc),n) for n in set(nn for nn,_ in primes)} for zc in zchars}
    kron=lambda n: int(pari.kronecker(dK,n))
    def find_psi(ch):
        out=[]
        for zc in zchars:
            if all(abs(psiv[zc][nn]-ev(ch,x))<1e-9 for nn,x in primes): out.append(zc)
        return out
    return dict(K=K,dK=dK,M=M,G=G,cyc=cyc,content=content,inv=inv,ev=ev,dd=dd,dpm=dpm,find_psi=find_psi,allc=allc,Ps=Ps,NP=NP,bnr=bnr,hits=hits,NDp=NDp,kron=kron,zcyc=zcyc)
class Herg:
    def __init__(s_,A,B,Na,Nb,lam,K=14):
        s_.a=np.array([A(n) for n in range(0,40*Na+1)],complex); s_.Na=Na; s_.Nb=Nb; s_.lam=float(lam)
        b=np.array([B(r) for r in range(0,Nb+1)],complex); r=np.arange(1,Nb+1)
        s_.rho=np.array([-(b[1:]*np.exp(2j*np.pi*r*t/Nb)).sum()/(2j*math.pi*Nb) for t in range(1,Nb+1)])
        assert abs(s_.rho.sum())<1e-10 and abs(b[1:].sum())<1e-9
        s_.sN=np.arange(1,Nb+1)/Nb; s_.K=K
        Bp=lambda k,x: float(sympy.bernoulli(k,x))
        s_.beta=[None]+[sum(s_.rho[t-1]*Bp(k,sympy.Rational(t,Nb)) for t in range(1,Nb+1)) for k in range(1,K+1)]
    def R(s_,z,mult=30):
        Na=s_.Na; Mc=Na*mult; m=np.arange(1,Mc+1); X=(s_.lam*m/z).astype(complex)
        val=0
        for i0 in range(0,Mc,2000):
            Xi=X[i0:i0+2000]; val+=(s_.a[1+i0:1+i0+len(Xi)]*(s_.rho[None,:]*digamma(s_.sN[None,:]+Xi[:,None])).sum(1)).sum()
        ar=s_.a[1:Na+1]; rr=np.arange(1,Na+1)
        for k in range(1,s_.K+1):
            if abs(s_.beta[k])<1e-12: continue
            if k==1:
                if abs(ar.sum())>1e-9: raise ValueError("k=1 divergent")
                tail=-(ar*digamma(Mc/Na+rr/Na)).sum()/Na
            else: tail=(ar*hzeta(k,Mc/Na+rr/Na)).sum()/Na**k
            val+=(-1)**(k+1)*s_.beta[k]/k*(z/s_.lam)**k*tail
        return val
def build(s,verbose=True):
    S=setup(s); out=[]; terms=[]
    for Cp,(lam,Fh) in S['content'].items():
        for ch,v in Fh.items():
            if abs(v)<1e-12: continue
            if not S['inv'](ch):
                terms.append(('cusp' if abs(S['ev'](ch,S['dd'])-1)<1e-9 else 'mixed',Cp,lam,ch,v,None)); continue
            cands=S['find_psi'](ch)
            M=S['M']; dK=S['dK']; G=S['G']
            chosen=None
            for zc in cands:
                # need psi*chi_D nonprincipal
                bb=[ (cmath.exp(2j*math.pi*float(pari.chareval(G,list(zc),n))) if math.gcd(n,M)==1 else 0)*S['kron'](n) for n in range(1,math.lcm(M,abs(dK))+1)]
                if abs(sum(bb))<1e-9: chosen=zc; break
            assert chosen is not None, (ch,cands)
            terms.append(('eis',Cp,lam,ch,v,chosen))
    if verbose:
        for t in terms: print("  ",t[0],"C-part",t[1],"lambda",t[2],"chi",t[3],"Fhat",np.round(t[4],5),"psi",t[5])
    return S,terms
def herglotz_eis(S,terms):
    M=S['M']; dK=S['dK']; G=S['G']; Nb=math.lcm(M,abs(dK))
    Hs=[]
    for kind,Cp,lam,ch,v,zc in terms:
        if kind!='eis': continue
        ps=lambda n,zc=zc: (cmath.exp(2j*math.pi*float(pari.chareval(G,list(zc),n))) if math.gcd(n,M)==1 else 0)
        A=lambda n,ps=ps: ps(n)
        B=lambda n,ps=ps: ps(n)*S['kron'](n)
        Hs.append((v,Herg(A,B,M,Nb,lam)))
    return lambda z: sum(2*v*H.R(z) for v,H in Hs)
if __name__=="__main__":
    from psi_q import make
    s=int(sys.argv[1]); S,terms=build(s)
    Psi,_,_=make(s)
    HE=herglotz_eis(S,terms)
    lines=[]
    for z in (1+0.6j,2+1j,0.5+0.8j,1.5+0.5j,0.7+0.3j):
        p=Psi(z); h=HE(z); lines.append(f"s={s} z={z}: Psi(q-series)={p:.14f}  Herglotz_Eis={h:.14f}  diff={abs(p-h):.2e}")
        print(lines[-1],flush=True)
    open(f"herg_{s}.txt","w").write("\n".join(lines)+"\n")
    pickle.dump([(t[0],t[1],str(t[2]),t[3],complex(t[4]),t[5]) for t in terms],open(f"herg_terms_{s}.pkl","wb"))
