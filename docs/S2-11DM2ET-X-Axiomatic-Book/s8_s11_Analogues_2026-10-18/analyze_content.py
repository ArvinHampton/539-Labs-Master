# Character analysis of content_{s}.pkl: Eisenstein (sigma-invariant chi) / cusp (non-invariant, pure type) / mixed-type content
# for every component; ranks inside the family; the list of cusp characters with type and conductor.
import cypari2, numpy as np, pickle, sys, itertools, math, cmath, json
from family_s import Family
pari=cypari2.Pari(); pari.allocatemem(2*10**9)
s=int(sys.argv[1]); import glob
pk=[pickle.load(open(fn,"rb")) for fn in sorted(glob.glob(f"content_{s}_{sys.argv[2] if len(sys.argv)>2 else ''}*.pkl"))]
dat=dict(pk[0]); dat['res']={}; dat['cov']={}
for d in pk:
    assert d['mspec']==pk[0]['mspec']
    for li,Fk in d['res'].items():
        cv=d['cov'][li] if isinstance(d['cov'],dict) else d['cov'][list(d['res'].keys()).index(li)]
        if li not in dat['cov'] or cv>dat['cov'][li]: dat['res'][li]=Fk; dat['cov'][li]=cv
print("merged",len(pk),"runs; coverage min",min(dat['cov'].values()))
CF={7:35,8:3,11:11}; D0=CF[s]
K=pari(f'bnfinit(x^2-{D0},1)')
sig=[g for g in pari.nfgaloisconj(K) if str(g)!='x'][0]
mod=pari.idealhnf(K,1)
for tok in dat['mspec'].split(','):
    p,e=map(int,tok.split(':'))
    for P in pari.idealprimedec(K,p): mod=pari.idealmul(K,mod,pari.idealpow(K,P,e))
bnr=pari.bnrinit(K,[mod,[1,1]],1); cyc=[int(z) for z in pari('(b)->b.cyc')(bnr)]; assert cyc==dat['cyc']
gens=pari('(b)->b.gen')(bnr); h=math.prod(cyc)
Sg=np.array([[int(z) for z in pari.bnrisprincipal(bnr,pari.nfgaloisapply(K,sig,g),0)] for g in gens]).T  # columns = sigma(gen_i)
Nm=int(pari.idealnorm(K,mod)); w=pari('Mod(x,x^2-%d)'%D0)
def cls_of(alpha): return np.array([int(z) for z in pari.bnrisprincipal(bnr,pari.idealhnf(K,alpha),0)])
dmm=cls_of(1-Nm*1000); dpm=cls_of(1+Nm*1000*w)   # totally negative / signs (+,-) under embedding sqrt->+sqrt
allcls=list(itertools.product(*[range(m) for m in cyc])); cidx={cl:i for i,cl in enumerate(allcls)}
CL=np.array(allcls)
chars=list(itertools.product(*[range(m) for m in cyc])); CH=np.array(chars)
cycv=np.array(cyc)
ev=lambda ch,x: np.exp(2j*np.pi*np.sum(np.array(ch)*np.array(x)/cycv))
# chi(x) matrix
Mchi=np.exp(2j*np.pi*(CH/cycv)@CL.T)            # [chi, class]
sigcls=np.array([cidx[tuple(int(z)%m for z,m in zip(Sg@np.array(cl),cyc))] for cl in allcls])
inv=np.array([np.allclose(Mchi[i],Mchi[i][sigcls]) for i in range(len(chars))])
tmm=np.array([ev(ch,dmm) for ch in chars]); tpm=np.array([ev(ch,dpm) for ch in chars])
pure=np.abs(tmm-1)<1e-9; typ11=pure&(np.abs(tpm+1)<1e-9)
cusp=pure&~inv; eis=inv; mixed=~pure
print(f"s={s}: Cl_m^+={cyc} (m={dat['mspec']}); chars: sigma-inv {eis.sum()} (of which mixed {np.sum(eis&mixed)}), cusp-type (pure, non-inv) {cusp.sum()}, mixed non-inv {np.sum(mixed&~inv)}")
F=Family(s); res=dat['res']
rowsE=[];rowsC=[];rowsM=[]; summary=[]
cusp_used=np.zeros(len(chars))
for li in range(F.N):
    Fk=res[li]; vE=[];vC=[];vM=[]
    for sg in (0,1):
        for Cp in sorted({kk[1] for kk in Fk}):
            Fv=np.array([Fk.get((sg,Cp,cl),0.0) for cl in allcls],complex)
            Fs=(Fv+Fv[sigcls])/2
            Fh=(Mchi.conj()@Fs)/h
            vE.append(Fh[eis]); vC.append(Fh[cusp]); vM.append(Fh[mixed&~inv])
            cusp_used+=np.abs(Fh)*cusp
    vE=np.concatenate(vE+[np.zeros(0)]); vC=np.concatenate(vC+[np.zeros(0)]); vM=np.concatenate(vM+[np.zeros(0)])
    rowsE.append(vE); rowsC.append(vC); rowsM.append(vM)
    summary.append((np.linalg.norm(vE),np.linalg.norm(vC),np.linalg.norm(vM)))
S=np.array(summary)
tol=1e-9
cls_E=[i for i in range(F.N) if S[i,0]>tol and S[i,1]<tol]; cls_C=[i for i in range(F.N) if S[i,1]>tol and S[i,0]<tol]
cls_B=[i for i in range(F.N) if S[i,1]>tol and S[i,0]>tol]; cls_0=[i for i in range(F.N) if S[i,1]<tol and S[i,0]<tol]
print(f"   components: pure Eis {len(cls_E)}, pure cusp {len(cls_C)}, both {len(cls_B)}, zero-content {len(cls_0)};  max mixed content {S[:,2].max():.2e}")
import os
if os.path.exists(f"raw_{s}.npy"):
    Mraw=np.load(f"raw_{s}.npy")
    def rk(ii):
        if not ii: return 0
        x=np.linalg.svd(Mraw[ii],compute_uv=False); return int(np.sum(x>1e-8*x[0]))
    rE,rC,rT=rk(cls_E),rk(cls_C),rk(list(range(F.N)))
    print(f"   function-space ranks (raw Fourier matrix): Eis comps {rE}, cusp comps {rC}, Eis+cusp {rk(cls_E+cls_C)}, whole family {rT}")
    Pm=np.load(f"P_{s}.npy"); I=np.eye(F.N)
    lab=lambda ii: int(np.linalg.matrix_rank(((I+Pm)/2)[ii],tol=1e-8)) if ii else 0
    print(f"   label-space (P-invariant) dims: Eis labels {lab(cls_E)}, cusp labels {lab(cls_C)}, all {lab(list(range(F.N)))}")
else: rE=rC=rT=None
iL=F.IDX[(tuple(F.a%F.D),(0,0))]
print(f"   u_L = u_(a,0): |Eis|={S[iL,0]:.3e} |cusp|={S[iL,1]:.3e} |mixed|={S[iL,2]:.1e}")
# u_R = sum_p u_{p,-a}  (for a in L': = sum_p e(B(p,-a)) u_{p,0})
# u_R content: combine label summaries is not linear; report labels involved
labsR=[F.reduce(p,(-F.a)%F.D)[0] for p in F.LP]
print(f"   u_R labels: {len(set(labsR))}, of which pure Eis {len(set(labsR)&set(cls_E))}, cusp {len(set(labsR)&set(cls_C))}, both {len(set(labsR)&set(cls_B))}, zero {len(set(labsR)&set(cls_0))}")
cuspidx=[i for i in range(len(chars)) if cusp[i] and cusp_used[i]>1e-9]
lst=[]
for i in cuspidx:
    ch=list(chars[i]); f=pari.bnrconductor(bnr,ch)
    lst.append((tuple(ch),'(1,1)' if typ11[i] else '(0,0)',str(pari.idealfactor(K,f[0])),int(pari.idealnorm(K,f[0])),str(f[1])))
print(f"   cusp characters with nonzero content: {len(lst)}  (=> {len(lst)//2} dihedral forms if sigma-pairs)")
from collections import Counter
print("   by (type, N(conductor)):",dict(Counter((t,n) for _,t,_,n,_ in lst)))
for r in lst[:60]: print("     ",r)
json.dump({'summary':S.tolist(),'cusp_chars':lst,'ranks':[rE,rC,rT],'cls_E':cls_E,'cls_C':cls_C,'cls_B':cls_B,'cls_0':cls_0},open(f"analysis_{s}.json","w"))
