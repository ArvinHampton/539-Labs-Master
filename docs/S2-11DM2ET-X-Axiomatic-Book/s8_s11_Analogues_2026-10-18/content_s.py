# Step (4): exact ray-class content of every component u_{al,be} of the family, and the Eisenstein/cusp split.
#  For nu in the gamma^2-fundamental domains of S+, S-=-S+, T+, T-=-T+ (weight 1/2), X = D nu, beta_X=(2X1+sX2)+c X2 sqrt(D0),
#  (beta_X) = C * B with C supported on primes | m, B coprime to m.  Key = (sign of Q, C, class of B in Cl_m^+).
#  Per component: total weight per ideal must depend only on the key (checked), unseen keys must be provably empty (checked);
#  then sigma-symmetrise and expand in characters chi of Cl_m^+: sigma-invariant -> Eisenstein (genus), non-invariant pure type -> cusp,
#  mixed type must vanish.  Ranks give the Eis/cusp dimensions inside the P-invariant space.
import cypari2, numpy as np, math, sys, itertools, json, pickle, cmath
from fractions import Fraction as Fr
from collections import defaultdict
from family_s import Family
pari=cypari2.Pari(); pari.allocatemem(3*10**9)
s=int(sys.argv[1]); Qmax=float(sys.argv[2]); mspec=sys.argv[3]   # mspec like "2:8,3:2" exponents of the prime(s) above p
CF={7:(35,1),8:(3,4),11:(11,3)}; D0,c=CF[s]
F=Family(s); D=F.D; A=F.A
K=pari(f'bnfinit(x^2-{D0},1)'); w=pari('Mod(x,x^2-%d)'%D0)
sig=pari.nfgaloisconj(K)[1] if str(pari.nfgaloisconj(K)[0])==str(pari('x')) else pari.nfgaloisconj(K)[0]
mod=pari.idealhnf(K,1); Ps=[]
for tok in mspec.split(','):
    p,e=map(int,tok.split(':'))
    for P in pari.idealprimedec(K,p): Ps.append(P); mod=pari.idealmul(K,mod,pari.idealpow(K,P,e))
bnr=pari.bnrinit(K,[mod,[1,1]],1); cyc=[int(z) for z in pari('(b)->b.cyc')(bnr)]; h=int(pari('(b)->b.no')(bnr))
print(f"s={s} D={D} m={mspec} Cl_m^+ cyc={cyc} order {h}",flush=True)
G1=F.G
def cone_mask(X,r1,r2):
    det=r1[0]*r2[1]-r1[1]*r2[0]
    sv=(X[:,0]*r2[1]-X[:,1]*r2[0])*np.sign(det); tv=(r1[0]*X[:,1]-r1[1]*X[:,0])*np.sign(det)
    return (sv>0)&(tv>=0)
e1=np.array([1,0]); f=np.array([1,-1])
# domain [r, gamma r) for gamma (not gamma^2); the gamma^2 domain = this U gamma(this), and gamma nu gives the same ideal (unit multiple).
sel=None
if len(sys.argv)>4 and sys.argv[4]!='all':
    sel=[int(z) for z in sys.argv[4].split(',')]
    alset={F.LABELS[i][0] for i in sel}
else: alset=set(map(tuple,np.array(F.ALS)))
alset={tuple(int(z) for z in a_) for a_ in alset}
GIm=F.GI
resid=alset|{tuple(int(z)%D for z in GIm@np.array(a_)) for a_ in alset}
by2=defaultdict(list)
for r1_,r2_ in resid: by2[r2_].append(r1_)
M=Qmax*D*D
def rows(r1,r2,sgn):
    th=np.linspace(0,1,2001); V=np.outer(1-th,r1)+np.outer(th,r2); V=V/np.linalg.norm(V,axis=1)[:,None]
    lam=np.min(np.abs(V[:,0]**2+s*V[:,0]*V[:,1]+(s/2)*V[:,1]**2))
    R=int(math.sqrt(M/lam))+2
    out=[]
    for x2 in range(-R,R+1):
        if (sgn*x2)%D not in by2: continue
        res1=np.array(sorted(by2[(sgn*x2)%D]))
        dis1=(s*s-2*s)*x2*x2+4*M
        lo=math.floor((-s*x2-math.sqrt(dis1))/2)-1; hi=math.ceil((-s*x2+math.sqrt(dis1))/2)+1
        dis2=(s*s-2*s)*x2*x2-4*M
        if dis2>0:
            a1=math.ceil((-s*x2-math.sqrt(dis2))/2)+1; b1=math.floor((-s*x2+math.sqrt(dis2))/2)-1
            segs=[(lo,a1),(b1,hi)] if a1<b1 else [(lo,hi)]
        else: segs=[(lo,hi)]
        for p,q in segs:
            # x1 with sgn*x1 mod D in res1
            base=np.arange(p//D-1,q//D+2)*D
            cand=(base[:,None]+((sgn*res1)%D)[None,:]).ravel()
            x1=cand[(cand>=p)&(cand<=q)]
            if len(x1): out.append(np.stack([x1,np.full_like(x1,x2)],1))
    X=np.concatenate(out)
    m=cone_mask(sgn*X,r1,r2); X=X[m]
    Q=(X[:,0]**2+s*X[:,0]*X[:,1]+(s/2)*X[:,1]**2)/(D*D)
    X=X[(np.abs(Q)<=Qmax)&(Q!=0)]
    assert np.max(np.abs(X))<R-1
    return X
Xs=[];regs=[]
for rg,(r1,sgn) in enumerate(((e1,1),(e1,-1),(f,1),(f,-1))):
    Xr=rows(r1,G1@r1,sgn)
    # keep points in some coset al or with gamma X in some coset
    GX=Xr@G1.T
    ok=np.array([((x%D,y%D) in alset) or ((u%D,v%D) in alset) for (x,y),(u,v) in zip(Xr,GX)])
    Xs.append(Xr[ok]); regs.append(np.full(ok.sum(),rg))
X=np.concatenate(Xs); reg=np.concatenate(regs)
Qv=(X[:,0]**2+s*X[:,0]*X[:,1]+(s/2)*X[:,1]**2)/(D*D)
assert np.all((Qv>0)==(reg<2))
GX=X@G1.T
print("points:",len(X),flush=True)
# ideal data per point
cache={}; keys=[]; idl=[]
NP=[int(pari.idealnorm(K,P)) for P in Ps]
beta=lambda X1,X2:(2*X1+s*X2)+c*X2*w
dmap={}; Ndmap={}
for al in F.ALS:
    Dg=pari.idealhnf(K,beta(int(al[0]),int(al[1])))
    for gg in (beta(D,0),beta(0,D)): Dg=pari.idealadd(K,Dg,gg)
    dmap[tuple(al)]=Dg; Ndmap[tuple(al)]=int(pari.idealnorm(K,Dg))
ptN=[]
for x1,x2 in X:
    bt=beta(int(x1),int(x2)); alx=(int(x1)%D,int(x2)%D)
    J=pari.idealdiv(K,pari.idealhnf(K,bt),dmap[alx]); ptN.append(Ndmap[alx]); Cp=[]; Jp=J
    for P in Ps:
        v=int(pari.idealval(K,J,P))
        Cp.append(v)
        if v: Jp=pari.idealdiv(K,Jp,pari.idealpow(K,P,v))
    hk=str(Jp)
    if hk not in cache:
        cl=tuple(int(z) for z in pari.bnrisprincipal(bnr,Jp,0))
        cls=tuple(int(z) for z in pari.bnrisprincipal(bnr,pari.nfgaloisapply(K,sig,Jp),0))
        cache[hk]=(cl,cls,int(pari.idealnorm(K,Jp)))
    keys.append((tuple(Cp),)+cache[hk]); idl.append(hk+str(Cp))
print("ideal data done; distinct B ideals:",len(cache),flush=True)
# class -> index
allcls=list(itertools.product(*[range(m) for m in cyc])); cidx={cl:i for i,cl in enumerate(allcls)}
# minimal norm of ideals coprime to m in each class (for emptiness check)
Lmax=int(sys.argv[6]) if len(sys.argv)>6 else 4000; L=pari.ideallist(K,Lmax); minN={}
for nn in range(1,Lmax+1):
    for J in L[nn-1]:
        if any(int(pari.idealval(K,J,P)) for P in Ps): continue
        cl=tuple(int(z) for z in pari.bnrisprincipal(bnr,J,0))
        if cl not in minN: minN[cl]=nn
print("classes with known min norm:",len(minN),"of",h,flush=True)
Cparts=sorted({kk[0] for kk in keys})
def NC(Cp): return math.prod(n**v for n,v in zip(NP,Cp))
normX=4*D*D*Qv  # = N(beta_X)
maxmin=max(minN.values()) if len(minN)==h else float('inf')
ptN=np.array(ptN); Cps_all=[kk[0] for kk in keys]
print("max over classes of min norm:",maxmin,flush=True)
res={}; bad=0; unver=0; covl=[]
for li,(al,be) in enumerate(F.LABELS):
    if sel is not None and li not in sel: continue
    al=np.array(al); be=np.array(be)
    m1=np.all((X%D)==al,axis=1); m2=np.all((GX%D)==al,axis=1)
    idx=np.nonzero(m1|m2)[0]
    wts=0.5*(m1[idx]*np.exp(2j*np.pi*((X[idx]@A@be)%(D*D))/(D*D)) + m2[idx]*np.exp(2j*np.pi*((GX[idx]@A@be)%(D*D))/(D*D)))
    per=defaultdict(complex); perkey={}
    for t,i in enumerate(idx):
        sg=0 if reg[i]<2 else 1
        kk=(sg,keys[i][0],keys[i][1]); per[(sg,idl[i])]+=wts[t]; perkey[(sg,idl[i])]=(kk,normX[i],keys[i][2])
    Fk={}; maxN={}
    for ii,v in per.items():
        kk,nx,nb=perkey[ii]
        if kk in Fk:
            if abs(Fk[kk]-v)>1e-9: bad+=1
        else: Fk[kk]=v
    # per-component completeness: C-part complete iff every class is reachable within the norm bound
    Nd=Ndmap[tuple(al)]
    compC=[Cp for Cp in set(Cps_all[i] for i in idx) if 4*D*D*Qmax/(Nd*NC(Cp))>=maxmin]
    covl.append(np.mean([Cps_all[i] in compC for i in idx]) if len(idx) else 1.0)
    for sg in (0,1):
        for Cp in compC:
            for cl in allcls: Fk.setdefault((sg,Cp,cl),0.0)
    Fk={kk:v for kk,v in Fk.items() if kk[1] in compC}
    res[li]=Fk
print(f"inconsistent per-ideal weights: {bad};  components with full coverage: {sum(1 for c in covl if c==1.0)}/{len(covl)}; min coverage {min(covl):.3f}",flush=True)
pickle.dump({'s':s,'cyc':cyc,'res':res,'Cparts':sorted(set(Cps_all)),'cov':covl,'mspec':mspec,'Qmax':Qmax},open(f"content_{s}_{sys.argv[5] if len(sys.argv)>5 else 'base'}.pkl","wb"))
