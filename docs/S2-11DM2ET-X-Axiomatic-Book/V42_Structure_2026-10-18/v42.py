import sys, numpy as np, pickle
from collections import defaultdict, Counter
from fractions import Fraction as F
CP="../2026-10-17-cusp-part"; sys.path.insert(0,'.'); sys.path.insert(1,CP)
from family import Smatrix,Tmatrix,LABELS,reduce,IDX,D
import uvec
out=[]; pr=lambda s: (print(s),out.append(s))
S=Smatrix(); T=Tmatrix(); I=np.eye(140); N=140
pr(f"S unitary {abs(S@S.conj().T-I).max():.1e}, T unitary {abs(T@T.conj().T-I).max():.1e}")
# Fourier matrix
cols=defaultdict(lambda: np.zeros(N,complex))
for i,(al,be) in enumerate(LABELS):
    q,ph,c=uvec.vectors(al,be,Qmax=40); cols['c'][i]+=c
    for qq,p in zip(np.rint(19600*q).astype(np.int64),ph): cols[int(qq)][i]+=p
keys=list(cols); C=np.array([cols[k] for k in keys]).T
def basis(M,tol=1e-8):
    U,s,_=np.linalg.svd(M,full_matrices=False); return U[:,:int((s>tol*s[0]).sum())]
V=basis(C); P=S@S; Wb=basis((I+P)/2); Ccomp=basis(Wb-V@(V.conj().T@Wb))
pr(f"dim V {V.shape[1]}, dim W {Wb.shape[1]}, dim W(-)V {Ccomp.shape[1]}; complement invariance S {abs(S@Ccomp-Ccomp@(Ccomp.conj().T@S@Ccomp)).max():.1e} T {abs(T@Ccomp-Ccomp@(Ccomp.conj().T@T@Ccomp)).max():.1e}")
pc=pickle.load(open(f"{CP}/fitF.pkl","rb"))['per_comp']
Cu=sorted({i for i,r in pc.items() for x in r.values() if x and x['cusp']>1e-12}); E=[i for i in range(N) if i not in Cu]
def sub(rows): M=np.zeros_like(C); M[rows]=C[rows]; return basis(M)
spaces={"V_Eis":sub(E),"V_cusp":sub(Cu),"W-V":Ccomp}
# irreducible decomposition via commutant
def commutant(Sr,Tr):
    d=Sr.shape[0]; Id=np.eye(d)
    M=np.vstack([np.kron(Sr,Id)-np.kron(Id,Sr.T),np.kron(Tr,Id)-np.kron(Id,Tr.T)])
    _,s,vh=np.linalg.svd(M); k=int((s<1e-9).sum()); return [vh[-j-1].conj().reshape(d,d) for j in range(k)]
def tloc(r):  # r=a/140 -> (a mod 4 part, mod 5, mod 7) exponents
    a=int(r*140)%140; return (a*35*3%4 if False else (a*35)%140//35, (a*28)%140//28, (a*20)%140//20)
rng=np.random.default_rng(1); table=[]
for nm,Wsp in spaces.items():
    Sr=Wsp.conj().T@S@Wsp; Tr=Wsp.conj().T@T@Wsp; d=Sr.shape[0]
    K=commutant(Sr,Tr); X=sum(rng.normal()*k for k in K); X=X+X.conj().T
    w,U=np.linalg.eigh(X); groups=[]; 
    for j in range(d):
        if groups and abs(w[j]-groups[-1][0])<1e-6: groups[-1][1].append(j)
        else: groups.append([w[j],[j]])
    pr(f"{nm}: dim {d}, commutant dim {len(K)}, eigen-blocks of random commutant element: {[len(g[1]) for g in groups]}")
    for g in groups:
        Ub=U[:,g[1]]; Si=Ub.conj().T@Sr@Ub; Ti=Ub.conj().T@Tr@Ub
        ev=np.linalg.eigvals(Ti); rs=sorted(F(int(round(np.angle(e)/(2*np.pi)*840))%840,840) for e in ev)
        loc=[tloc(r) for r in rs]; m4=sorted(set(l[0] for l in loc)); m5=sorted(set(l[1] for l in loc)); m7=sorted(set(l[2] for l in loc))
        cnt=Counter(loc); prod=len(m4)*len(m5)*len(m7)==len(rs) and all(v==1 for v in cnt.values())
        table.append((nm,len(rs),round(np.trace(Si).real,9),rs,m4,m5,m7,prod))
for t in table:
    pr(f"  [{t[0]}] dim {t[1]}  trS {t[2]}  T-spectrum {[str(x) for x in t[3]]}  local T-exponents: mod4 {t[4]} (/4), mod5 {t[5]} (/5), mod7 {t[6]} (/7); tensor-product shape: {t[7]}")
# relations kernel
Kr=np.linalg.svd(C.T)[2][V.shape[1]:].conj().T
zero=[i for i in range(N) if abs(C[i]).max()<1e-9]
Pminus=basis((I-P)/2)
pr(f"relations kernel dim {Kr.shape[1]}; labels with u==0: {len(zero)}; dim Fix(P)^perp (P=-1 space, transposed) = {Pminus.shape[1]}")
# P^T anti-invariant vectors are relations? check x with P^T x=-x
Ptm=basis((I-P.T)/2); pr(f"P^T(-1)-eigenspace dim {Ptm.shape[1]}, contained in kernel: resid {abs(Ptm.T@C).max():.1e}")
Kq=basis(Kr-Ptm@np.linalg.lstsq(Ptm,Kr,rcond=None)[0]); pr(f"kernel mod P-relations: dim {Kq.shape[1]}")
# proportional pairs
nz=[i for i in range(N) if i not in zero]; prop=[]
for a in nz:
    for b in nz:
        if b<=a: continue
        r=np.vdot(C[a],C[b])/np.vdot(C[a],C[a])
        if abs(C[b]-r*C[a]).max()<1e-9: prop.append((a,b,complex(np.round(r,6))))
pr(f"proportional label pairs (u_b = c u_a): {len(prop)}; rank of pair relations {np.linalg.matrix_rank(np.array([np.eye(N)[b]-p*np.eye(N)[a] for a,b,p in prop]) if prop else np.zeros((1,N)),1e-8)}")
cl={}; 
for a,b,_ in prop: cl.setdefault(a,{a}).add(b)
grp=Counter(len(v) for k,v in cl.items() if not any(k in w and k!=m for m,w in cl.items()))
# involutions on labels
def labperm(fa,fb):
    M=np.zeros((N,N),complex)
    for i,(al,be) in enumerate(LABELS):
        j,ph=reduce(fa(np.array(al))%D, fb(np.array(be))); M[j,i]=ph
    return M
R=np.array([[1,7],[0,-1]])
invs={"R=[[1,7],[0,-1]] (improper autom., Galois-type)":labperm(lambda a:R@a,lambda b:R@b),
      "beta->-beta":labperm(lambda a:a,lambda b:-b),"alpha->-alpha":labperm(lambda a:-a,lambda b:b)}
for nm,M in invs.items():
    # action on functions: compare rows of C mapped, allowing q->-q and/or conjugation
    j=[keys.index(k) if k=='c' else (keys.index(-k) if -k in cols else None) for k in keys]
    Cneg=np.array([C[:,jj] if jj is not None else np.zeros(N) for jj in j]).T
    tests={"u_g = u":abs(M.T@C-C).max(),"u_g(-wbar) = u":abs(M.T@C-Cneg).max(),"u_g = conj u":abs(M.T@C-C.conj()).max(),"u_g(-wbar)=conj u":abs(M.T@C-Cneg.conj()).max()}
    best=min(tests,key=tests.get)
    pr(f"{nm}: M^2=I {abs(M@M-I).max():.1e}; [M,S] {abs(M@S-S@M).max():.1e}, [M,T] {abs(M@T-T@M).max():.1e}, MSM vs conj S {abs(M@S@M-S.conj()).max():.1e}; function identity best: {best} ({tests[best]:.1e})")
    if abs(M@S-S@M).max()<1e-9 and abs(M@T-T@M).max()<1e-9:
        for sn,Wsp in [("V",V),("V_Eis",spaces['V_Eis']),("V_cusp",spaces['V_cusp']),("W-V",Ccomp)]:
            Mr=Wsp.conj().T@M@Wsp; Sr=Wsp.conj().T@S@Wsp; e=abs(M@Wsp-Wsp@Mr).max()
            pr(f"   on {sn}: invariance {e:.1e}, tr M={np.trace(Mr).real:.6f}, tr MS={np.trace(Mr@Sr).real:.6f}")
# invariant Hermitian forms on V: commutant hermitian part
Sr=V.conj().T@S@V; Tr=V.conj().T@T@V; K=commutant(Sr,Tr)
pr(f"V: commutant dim {len(K)} (= number of independent invariant Hermitian forms, since S,T unitary)")
open("v42.txt","w").write("\n".join(out)+"\n")
pickle.dump(dict(prop=prop,zero=zero),open("rel.pkl","wb"))
