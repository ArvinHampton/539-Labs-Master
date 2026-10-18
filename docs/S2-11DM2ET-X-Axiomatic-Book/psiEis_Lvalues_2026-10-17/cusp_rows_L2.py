# (B, general rationals with denominators built from 2,5,7): kappa_c(h/k) = sum_{chi'} Ghat(chi') L_{m'}(0,chi'),
# G(cls') = F_c(cls' mod m) * e(h N(cls')/(140k)), on Cl_{m'}^+ with m' = m * (extra powers of p2,p5,p7) so that N mod 140k is a class function.
import numpy as np, pickle, itertools, cmath, math, sys, json
from fractions import Fraction as fr
import cypari2; pari=cypari2.Pari(); pari.allocatemem(2*10**9); pari.set_real_precision(38); gp=lambda s: pari(s)
from family import LABELS
import kappa_all
CS=json.load(open('component_split.json'))
F=pickle.load(open("fitF.pkl","rb")); pc=F['per_comp']; cyc0=F['cyc']
C=sorted({i for i,rec in pc.items() for s,r in rec.items() if r and r['cusp']>1e-12})
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; P7=idealprimedec(bnf,7)[1]')
gp('m0=idealmul(bnf,idealmul(bnf,idealpow(bnf,P2,3),P5),P7); bnr0=bnrinit(bnf,[m0,[1,1]],1)')
def Fhat(i): return {tuple(e['chi']):float(fr(e['abs']))*cmath.exp(2j*math.pi*float(fr(e['phase_turns']))) for e in CS[str(i)]['data']['1']['cusp_coeffs']}
def setup(e2,e5,e7,K):
    gp(f'm1=idealmul(bnf,idealmul(bnf,idealpow(bnf,P2,{e2}),idealpow(bnf,P5,{e5})),idealpow(bnf,P7,{e7})); bnr1=bnrinit(bnf,[m1,[1,1]],1); Mp=bnrmap(bnr1,bnr0)')
    cyc=[int(t) for t in gp('bnr1.cyc')]
    Mp=[[int(gp(f'Mp[1][{a+1},{b+1}]')) for b in range(len(cyc))] for a in range(3)]
    gp('Li=ideallist(bnf,40000)')
    ncls=int(np.prod(cyc)); normcls={}
    for n in range(1,40001):
        if math.gcd(n,70)!=1: continue
        for c in gp(f'apply(I->bnrisprincipal(bnr1,I,0),Li[{n}])'):
            c=tuple(int(t) for t in c)
            if c in normcls: assert normcls[c]==n%K
            normcls[c]=n%K
        if len(normcls)==ncls: break
    assert len(normcls)==ncls, (len(normcls),ncls)
    return cyc,Mp,normcls
def kappa_rows(x,e2,e5,e7):
    h,k=x.numerator,x.denominator; K=140*k
    cyc,Mp,normcls=setup(e2,e5,e7,K); classes=list(normcls)
    img={c:tuple(sum(Mp[a][b]*c[b] for b in range(len(cyc)))%cyc0[a] for a in range(3)) for c in classes}
    def ev0(chi,c): return cmath.exp(2j*math.pi*float(sum(fr(chi[a]*c[a],cyc0[a]) for a in range(3))))
    G={}
    for i in C:
        Fh=Fhat(i)
        G[i]=np.array([sum(Fh[chi]*ev0(chi,img[c]) for chi in Fh)*cmath.exp(2j*math.pi*normcls[c]*h/K) for c in classes])
    # character table of Cl_{m1}: chi' values on classes
    chars=list(itertools.product(*[range(cc) for cc in cyc]))
    E=np.exp(2j*np.pi*np.array([[float(sum(fr(ch[a]*c[a],cyc[a]) for a in range(len(cyc)))) for c in classes] for ch in chars]))
    Gh={i:E.conj()@G[i]/len(classes) for i in C}
    need=set()
    for i in C: need|={j for j in range(len(chars)) if abs(Gh[i][j])>1e-12}
    L0={}
    for j in sorted(need):
        ch=list(chars[j])
        gp(f'chi={ch}; Cd=bnrconductor(bnr1,chi)')
        inf=[int(t) for t in gp('Cd[2]')]
        if inf!=[1,1]: L0[j]=0.0; continue      # L(0)=0 unless totally odd (Gamma_R(s) pole)
        gp('bC=bnrinit(bnf,Cd,1); M2=bnrmap(bnr1,bC); L=lfuncreate([bnr1,chi])')
        cycC=[int(t) for t in gp('bC.cyc')]; M2=[[int(gp(f'M2[1][{a+1},{b+1}]')) for b in range(len(cyc))] for a in range(len(cycC))]
        chiC=next(cand for cand in itertools.product(*[range(cc) for cc in cycC]) if all((fr(ch[b],cyc[b])-sum(fr(cand[a]*M2[a][b],cycC[a]) for a in range(len(cycC))))%1==0 for b in range(len(cyc))))
        fac=1
        for P in ("P2","P5","P7"):
            if int(gp(f'idealval(bnf,Cd[1],{P})'))==0:
                cP=[int(t) for t in gp(f'bnrisprincipal(bC,{P},0)')]
                fac*=1-cmath.exp(2j*math.pi*float(sum(fr(chiC[a]*cP[a],cycC[a]) for a in range(len(cycC)))))
        L0[j]=complex(gp('lfun(L,0)'))*fac
    kap=np.array([sum(Gh[i][j]*L0[j] for j in need) for i in C])
    return kap, len(chars), len(need)
if __name__=="__main__":
    S=np.load("../2026-10-17-psi-conditions/S_matrix.npy"); ph=np.load("../2026-10-17-psi-conditions/phi_rows.npy")
    Sc=S[np.ix_(C,C)]; out=[]
    tests=[(fr(2),2,(fr(-1,2),(5,1,1)),(fr(2),(3,1,1))),(fr(7,4),4,(fr(-4,7),(3,1,3)),(fr(7,4),(7,1,1)))]
    for x,idx,(xa,ma),(xb,mb) in tests:
        ka,n1,u1=kappa_rows(xa,*ma); kb,n2,u2=kappa_rows(xb,*mb)
        ea=np.array([kappa_all.fcoef(LABELS[i],xa)[2] for i in C]); eb=np.array([kappa_all.fcoef(LABELS[i],xb)[2] for i in C])
        Phi=ka-abs(float(x))*Sc@kb
        out.append(f"x={x}: kappa({xa}) via {u1}/{n1} chars: dev {np.abs(ka-ea).max():.2e}; kappa({xb}) via {u2}/{n2} chars: dev {np.abs(kb-eb).max():.2e}; Phi_c(x) vs phi_rows: max dev {np.abs(Phi-ph[{2:2,4:4}[idx],C]).max():.2e}; Phi_73={Phi[C.index(73)]:.12f}")
        print(out[-1],flush=True)
    open("cusp_rows_L2.txt","w").write("\n".join(out)+"\n")
