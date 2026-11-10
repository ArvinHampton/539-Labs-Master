# Local-derived. t4429 fallback (i) step 2: twisted ternary-theta products + formal T(p^2) eigen-solve.
# Generators: B_{a,psi}(tau) * U_{b,M,r}(tau), where
#   B_{a,psi} = sum_{alpha in Z[w]} psi(N alpha) q^{a N alpha},  N = x^2+xy+2y^2 (disc -7), psi = kron(d,.) (d=1 keeps constant 1)
#   U_{b,M,r} = sum_{n in Z, n = +-r mod M} q^{b n^2}
# i.e. theta series of ternary forms a*N(x,y) + b*z^2 with character/congruence conditions.
# Unknowns: rational combination h = sum k_j G_j.  Equations (formal, coefficientwise, n <= N/p^2):
#   c(p^2 n) + kron(D,p)*kron(-n,p)*c(n) + p*c(n/p^2) - lambda_p c(n) = 0   for p in PR, for each D in DLIST.
# Linear algebra mod the prime PM (python-flint nmod_mat); genuine dim = nullity after restricting to an independent generator subset.
# A nonzero kernel is a CANDIDATE only (formal, truncated, mod PM); it must be rechecked exactly (tt_v3+).
import sys, time, json, numpy as np, flint, cypari2
pari=cypari2.Pari(); pari.allocatemem(2*10**8)
TARGET=sys.argv[1]; NN=int(sys.argv[2]); CFG=sys.argv[3]
PM=2**31-1  # prime
t0=time.time()
def kron(a,n): return int(pari.kronecker(a,n))
E={'f':'ellinit("49a1")','g':'elltwist(ellinit("49a1"),-4)','Xi':'elltwist(ellinit("49a1"),140)'}[TARGET]
pari(f"EC={E}")
PR=[3,5,11,13,17,19,23,29,31,37,41,43]
if TARGET=='Xi': pass
lam={p:int(pari(f"ellap(EC,{p})")) for p in PR}
if TARGET=='Xi': PR=[p for p in PR if p!=5]
print("target",TARGET,"conductor",pari("ellglobalred(EC)[1]"),"lambda",lam,flush=True)
# representation numbers of N
r=np.zeros(NN+1,dtype=np.int64)
Y=int((8*NN/7)**0.5)+2
for y in range(-Y,Y+1):
    X=int((4*NN)**0.5)+2
    for x in range(-X,X+1):
        n=x*x+x*y+2*y*y
        if n<=NN: r[n]+=1
cfg=json.loads(open(CFG).read()) if CFG.endswith('.json') else json.loads(CFG)
AS=cfg['a']; DS=cfg['psi']; BS=cfg['b']; MR=cfg['MR']; DLIST=cfg['D']
kr={d:np.array([kron(d,n) for n in range(NN+1)],dtype=np.int64) for d in set(DS)}
def B(a,d):
    v=np.zeros(NN+1,dtype=np.int64); m=NN//a
    w=r[:m+1]*(kr[d][:m+1] if d!=1 else 1)
    v[0:a*m+1:a]=w
    if d!=1: v[0]=0
    return v
def Uterms(b,M,rr):
    out={}
    n=0
    lim=int((NN/b)**0.5)+1
    for n in range(-lim,lim+1):
        if (n-rr)%M==0 or (n+rr)%M==0:
            s=b*n*n
            if s<=NN: out[s]=out.get(s,0)+1
    return out
gens=[];labels=[]
for a in AS:
    for d in DS:
        Bv=B(a,d)
        if not Bv.any(): continue
        for b in BS:
            for (M,rr) in MR:
                v=np.zeros(NN+1,dtype=np.int64)
                for s,c in Uterms(b,M,rr).items(): v[s:]+=c*Bv[:NN+1-s]
                gens.append(v);labels.append((a,d,b,M,rr))
print("raw generators",len(gens),f"[{time.time()-t0:.0f}s]",flush=True)
# independent subset using coefficients n<=NI
NI=min(NN,int(cfg.get('NI',4000)))
G=np.array(gens)  # shape (ng, NN+1)
A=flint.nmod_mat([[int(x)%PM for x in G[:,n]] for n in range(NI+1)],PM)
R,rk=A.rref()
piv=[];row=0
ncol=A.ncols()
for i in range(rk):
    j=next(j for j in range(ncol) if int(R[i,j])!=0); piv.append(j)
print("rank on n<=%d:"%NI,rk,f"[{time.time()-t0:.0f}s]",flush=True)
G=G[piv]; labels=[labels[j] for j in piv]
res={}
for D in DLIST:
    rows=[]
    for p in PR:
        cD=kron(D,p)
        for n in range(1,NN//(p*p)+1):
            vec=G[:,p*p*n]+(cD*kron(-n,p)-lam[p])*G[:,n]
            if n%(p*p)==0: vec=vec+p*G[:,n//(p*p)]
            rows.append([int(x)%PM for x in vec])
    Em=flint.nmod_mat(rows,PM)
    X,nul=Em.nullspace()
    res[D]=nul
    print(f"D={D}: equations {len(rows)}, unknowns {len(piv)}, nullity {nul} [{time.time()-t0:.0f}s]",flush=True)
    if 0<nul<=6:
        for k in range(nul):
            kv=np.array([int(X[i,k]) for i in range(len(piv))],dtype=object)
            kv=[(x if x<PM//2 else x-PM) for x in kv]
            h=[sum(int(kv[i])*int(G[i,n]) for i in range(len(piv)))%PM for n in range(0,60)]
            h=[(x if x<PM//2 else x-PM) for x in h]
            nzl=[(labels[i],kv[i]) for i in range(len(piv)) if kv[i]!=0]
            print(f"  kernel vec {k}: support {len(nzl)} generators; h mod PM (n<60, nonzero only):",{n:h[n] for n in range(60) if h[n]},flush=True)
            print("   support:",nzl[:40],flush=True)
print("SUMMARY",TARGET,NN,res,f"[{time.time()-t0:.0f}s]")
