# Function-space dimension of the cusp part of the family (s=11), from the exact ray-class content (content_11_base.pkl):
#  cusp part of component c = sum_{Cp} sum_{chi cusp} Fhat_c(Cp,chi) theta^{coprime}_chi(lambda tau),  lambda = N(d_al)N(C)/(4D^2);
#  theta^{coprime}_chi = prod_{P | 2*3*11, P not | f_chi} (1 - chi_f(P) V_{N P}) theta^{new}_{chi_f};  newforms fingerprinted by coefficients.
#  Rank over the basis {(newform, type, dilation)} = cusp dimension (lower bound if some components are uncovered).
import cypari2, numpy as np, pickle, itertools, math, cmath, sys, glob
from fractions import Fraction as Fr
from family_s import Family
pari=cypari2.Pari(); pari.allocatemem(2*10**9)
s=int(sys.argv[1]); fn=sys.argv[2]
dat=pickle.load(open(fn,'rb')); cyc=dat['cyc']; mspec=dat['mspec']
CF={7:(35,1),8:(3,4),11:(11,3)}; D0,c=CF[s]; F=Family(s); D=F.D
K=pari(f'bnfinit(x^2-{D0},1)'); w=pari('Mod(x,x^2-%d)'%D0)
sig=[g for g in pari.nfgaloisconj(K) if str(g)!='x'][0]
mod=pari.idealhnf(K,1); Ps=[]
for tok in mspec.split(','):
    p,e=map(int,tok.split(':'))
    for P in pari.idealprimedec(K,p): Ps.append(P); mod=pari.idealmul(K,mod,pari.idealpow(K,P,e))
NP=[int(pari.idealnorm(K,P)) for P in Ps]
bnr=pari.bnrinit(K,[mod,[1,1]],1); assert [int(z) for z in pari('(b)->b.cyc')(bnr)]==cyc
cl=lambda J: tuple(int(z) for z in pari.bnrisprincipal(bnr,J,0))
allc=list(itertools.product(*[range(m) for m in cyc])); h=len(allc); cidx={x:i for i,x in enumerate(allc)}
gens=pari('(b)->b.gen')(bnr); Sg=np.array([[int(z) for z in cl(pari.nfgaloisapply(K,sig,g))] for g in gens]).T
cycv=np.array(cyc); CH=np.array(allc)
Mchi=np.exp(2j*np.pi*(CH/cycv)@CH.T)
sigcls=np.array([cidx[tuple(int(v)%m for v,m in zip(Sg@np.array(x),cyc))] for x in allc])
inv=np.array([np.allclose(Mchi[i],Mchi[i][sigcls]) for i in range(h)])
Nm=int(pari.idealnorm(K,mod)); dd=np.array(cl(pari.idealhnf(K,1-1000*Nm))); dpm=np.array(cl(pari.idealhnf(K,1+1000*Nm*w)))
pure=np.abs(np.exp(2j*np.pi*(CH/cycv)@dd)-1)<1e-9; t11=np.abs(np.exp(2j*np.pi*(CH/cycv)@dpm)+1)<1e-9
cusp=pure&~inv
# ideals up to 400 for fingerprints (all ideals, classes only for those coprime to m)
L=pari.ideallist(K,400)
ideals=[(n,J) for n in range(1,401) for J in L[n-1]]
def coprime(J): return all(int(pari.idealval(K,J,P))==0 for P in Ps)
fp_cache={}
def newform_data(i):
    if i in fp_cache: return fp_cache[i]
    ch=[int(z) for z in CH[i]]; fcond=pari.bnrconductor(bnr,ch)
    bf=pari.bnrinit(K,fcond,1); cf=[int(z) for z in pari('(b)->b.cyc')(bf)]
    mp=pari.bnrmap(bnr,bf)
    chif=[int(z) for z in pari.bnrmap(mp,ch)]
    def val(J):
        if any(int(pari.idealval(K,J,P))>0 for P in pari.idealfactor(K,fcond[0])[0]) if int(pari.idealnorm(K,fcond[0]))>1 else False: return 0
        xv=[int(z) for z in pari.bnrisprincipal(bf,J,0)]
        return cmath.exp(2j*math.pi*sum(a_*b_/m_ for a_,b_,m_ in zip(chif,xv,cf)))
    coef=np.zeros(401,complex)
    for n,J in ideals: coef[n]+=val(J)
    fpr=tuple(np.round(coef[1:120],6))
    chiP=[val(P) for P in Ps]
    fp_cache[i]=(fpr,chiP,int(pari.idealnorm(K,fcond[0])),bool(t11[i]))
    return fp_cache[i]
# per-coset normalisation ideals
beta=lambda X1,X2:(2*X1+s*X2)+c*X2*w
Nd={}
for al in F.ALS:
    Dg=pari.idealhnf(K,beta(int(al[0]),int(al[1])))
    for gg in (beta(D,0),beta(0,D)): Dg=pari.idealadd(K,Dg,gg)
    Nd[tuple(int(z) for z in al)]=int(pari.idealnorm(K,Dg))
rows={}; basis={}; ncov=0
for li,Fk in dat['res'].items():
    if not Fk: continue
    ncov+=1
    al=tuple(int(z) for z in F.LABELS[li][0]); vec={}
    for Cp in sorted({k[1] for k in Fk}):
        Fv=np.array([Fk.get((0,Cp,x),0.0) for x in allc],complex); Fs=(Fv+Fv[sigcls])/2
        Fh=(Mchi.conj()@Fs)/h
        lam=Fr(Nd[al]*math.prod(n**e for n,e in zip(NP,Cp)),4*D*D)
        for i in np.nonzero(cusp&(np.abs(Fh)>1e-10))[0]:
            fpr,chiP,fN,ty=newform_data(i)
            # oldform expansion over primes P|m with chi_f(P) != 0
            S_=[(NP[j],chiP[j]) for j in range(len(Ps)) if abs(chiP[j])>1e-12]
            for T in itertools.product([0,1],repeat=len(S_)):
                coefT=Fh[i]*np.prod([(-S_[j][1]) if T[j] else 1 for j in range(len(S_))])
                mu=lam*math.prod(S_[j][0] for j in range(len(S_)) if T[j])
                key=(fpr,ty,mu)
                if key not in basis: basis[key]=len(basis)
                vec[basis[key]]=vec.get(basis[key],0)+coefT
    rows[li]=vec
M=np.zeros((len(rows),len(basis)),complex)
for r,(li,vec) in enumerate(rows.items()):
    for j,v in vec.items(): M[r,j]=v
x=np.linalg.svd(M,compute_uv=False) if M.size else np.array([0.0])
rk=int(np.sum(x>1e-8*max(x[0],1e-300))) if M.size else 0
nforms=len({(k[0],k[1]) for k in basis})
print(f"s={s}: covered components {ncov}/{F.N}; cusp basis functions (newform,type,dilation) used: {len(basis)}; distinct newforms(by type) {nforms}; cusp function-space rank (lower bound) = {rk}")
from collections import Counter
print("newforms by (conductor norm, type):",dict(Counter((fp_cache_v[2],fp_cache_v[3]) for fp_cache_v in {v[0]+(v[3],):v for v in fp_cache.values()}.values())))
