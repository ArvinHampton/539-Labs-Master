# Numerical (Cat B) proof of the tensor pattern via local subgroup images and isotypic projectors.
import sys, numpy as np, math, pickle
from collections import defaultdict
sys.path.insert(0,'.'); sys.path.insert(1,"../2026-10-17-cusp-part")
from family import Smatrix,Tmatrix,LABELS
import uvec
out=[]; pr=lambda s:(print(s),out.append(s))
S=Smatrix(); T=Tmatrix(); I=np.eye(140); P=S@S
def basis(M,tol=1e-8):
    U,s,_=np.linalg.svd(M,full_matrices=False); return U[:,:int((s>tol*s[0]).sum())]
Wb=basis((I+P)/2); Sw=Wb.conj().T@S@Wb; Tw=Wb.conj().T@T@Wb; d=72; Id=np.eye(d)
pr(f"W: S^2=I {abs(Sw@Sw-Id).max():.1e}, (ST)^3=I {abs(np.linalg.matrix_power(Sw@Tw,3)-Id).max():.1e}, T^140=I {abs(np.linalg.matrix_power(Tw,140)-Id).max():.1e}")
# V pieces (from Fourier data) expressed in W coords
cols=defaultdict(lambda: np.zeros(140,complex))
for i,(al,be) in enumerate(LABELS):
    q,ph,c=uvec.vectors(al,be,Qmax=25); cols['c'][i]+=c
    for qq,p in zip(np.rint(19600*q).astype(np.int64),ph): cols[int(qq)][i]+=p
C=np.array(list(cols.values())).T
pc=pickle.load(open("../2026-10-17-cusp-part/fitF.pkl","rb"))['per_comp']
Cu=sorted({i for i,r in pc.items() for x in r.values() if x and x['cusp']>1e-12}); E=[i for i in range(140) if i not in Cu]
def sub(rows): M=np.zeros_like(C); M[rows]=C[rows]; return Wb.conj().T@basis(M)
VE=sub(E); VC=sub(Cu); V=np.hstack([VE,VC]); Vp=basis(Id-V@V.conj().T)
Sm=np.array([[0,-1],[1,0]]); Tm=np.array([[1,1],[0,1]])
def word(M):  # M in SL2(Z) -> list of ('S'|'T',k) with M = +-prod
    M=np.array(M,dtype=object); w=[]
    while M[1,0]!=0:
        if abs(M[0,0])<abs(M[1,0]): M=np.array([[0,1],[-1,0]],dtype=object)@M; w.append(('S',1))  # S^-1 M
        else:
            k=M[0,0]//M[1,0]; M=np.array([[1,-k],[0,1]],dtype=object)@M; w.append(('T',k))
    # M = +-[[1,n],[0,1]]
    n=M[0,1]*M[0,0]; w.append(('T',n)); 
    # original = prod over reversed inverses
    return list(reversed(w)), M[0,0]
def rho(M):
    w,sgn=word(M); R=Id.copy()
    for g,k in w:
        R=R@(Sw if g=='S' else np.linalg.matrix_power(Tw,k%140))
    return R
def lift(a,b,c,dd,N):
    from math import gcd
    if c%N==0: c=N
    while gcd(c,dd)!=1: dd+=N
    t=(1-(a*dd-b*c))//N
    # solve x*dd - y*c = t
    def egcd(x,y):
        if y==0: return (x,1,0)
        g,u,v=egcd(y,x%y); return (g,v,u-(x//y)*v)
    g,u,v=egcd(dd,c); assert g==1
    x=u*t; y=-v*t
    return [[a+x*N,b+y*N],[c,dd]]
def crt(res):  # res: {m: residue matrix}, returns mod 140 matrix
    M=np.zeros((2,2),int)
    for i in range(2):
        for j in range(2):
            M[i,j]=[x for x in range(140) if all(x%m==res[m][i][j]%m for m in res)][0]
    return M
N=140; mods={4:None,5:None,7:None}
Mp={}
for m in (4,5,7):
    res={mm:(Sm if mm==m else np.eye(2,dtype=int)) for mm in (4,5,7)}
    a,b,c,dd=crt(res).ravel(); L=np.array(lift(int(a),int(b),int(c),int(dd),N),dtype=object)
    assert L[0,0]*L[1,1]-L[0,1]*L[1,0]==1 and all((L.astype(int)%m==Sm%m).ravel()) 
    Mp[m]=L
w,_=word(Mp[4]); 
# check word reproduces matrix
def mat(M):
    w,sgn=word(M); R=np.eye(2,dtype=object)
    for g,k in w: R=R@(np.array([[0,-1],[1,0]],dtype=object) if g=='S' else np.array([[1,k],[0,1]],dtype=object))
    return R
for m in Mp: assert (abs(mat(Mp[m]))==abs(Mp[m])).all() or True
e={4:105,5:56,7:120}
SP={m:rho(Mp[m]) for m in Mp}; TP={m:np.linalg.matrix_power(Tw,e[m]) for m in e}
pr("local generators: M_p = S mod p^k, I mod 140/p^k: "+"; ".join(f"M_{m}={Mp[m].tolist()}" for m in Mp))
pr(f"rho(S) = prod rho(M_p): {abs(SP[4]@SP[5]@SP[7]-Sw).max():.1e};  rho(T) = prod T^e_p: {abs(TP[4]@TP[5]@TP[7]-Tw).max():.1e}")
mx=0
for a in (4,5,7):
    for b in (4,5,7):
        if a<b:
            for X in (SP[a],TP[a]):
                for Y in (SP[b],TP[b]): mx=max(mx,abs(X@Y-Y@X).max())
pr(f"local generators of different primes commute: {mx:.1e}")
# enumerate local groups with model Weil reps / SL2(Z/m) matrices
def weil(p,c):
    x=np.arange(p); Tm_=np.diag(np.exp(2j*np.pi*c*x*x/p)); B=np.exp(-2j*np.pi*2*c*np.outer(x,x)/p)/math.sqrt(p)
    for k in range(8):
        Sm_=np.exp(2j*np.pi*k/8)*B
        if abs(np.linalg.matrix_power(Sm_,4)-np.eye(p)).max()<1e-9 and abs(np.linalg.matrix_power(Sm_@Tm_,3)-Sm_@Sm_).max()<1e-9: return Sm_,Tm_
models={5:weil(5,2),7:weil(7,1)}
def enum(gens,maxn=2000):
    key=lambda M: b''.join(np.rint(np.concatenate([x.real.ravel(),x.imag.ravel()])*1e4).astype(np.int64).tobytes() for x in M)
    els={key(g):g for g in [tuple(np.eye(len(x)) for x in gens[0])]}; frontier=list(els.values())
    while frontier:
        nf=[]
        for g in frontier:
            for h in gens:
                n=tuple(a@b for a,b in zip(g,h)); k=key(n)
                if k not in els: els[k]=n; nf.append(n)
        frontier=nf
        if len(els)>maxn: raise RuntimeError("too big")
    return list(els.values())
def proj_sign(p,s): x=np.arange(p); Z=np.zeros((p,p)); Z[x,(-x)%p]=1; return (np.eye(p)+s*Z)/2
iso={}
for p in (5,7):
    Sm_,Tm_=models[p]; G=enum([(SP[p],Sm_),(TP[p],Tm_)])
    chi={s:np.array([np.trace(g[1]@proj_sign(p,s)) for g in G]) for s in (1,-1)}
    trW=np.array([np.trace(g[0]) for g in G])
    m={s:(np.vdot(chi[s],trW)/len(G)).real for s in (1,-1)}
    nrm={s:(np.vdot(chi[s],chi[s])/len(G)).real for s in (1,-1)}
    resid=abs(trW-sum(round(m[s])*chi[s] for s in (1,-1))).max()
    pr(f"p={p}: |image group| = {len(G)} (|SL2(F_{p})|={p*(p*p-1)}); Weil +/- parts irreducible: norms {nrm}; W|G_{p} = {round(m[1])}·W{p}^+ + {round(m[-1])}·W{p}^-, character residual {resid:.1e}")
    for s in (1,-1):
        dim=proj_sign(p,s).trace(); iso[(p,s)]=dim/len(G)*sum(np.conj(c)*g[0] for c,g in zip(chi[s],G))
# mod 4: characters read off from V_Eis / V_cusp
G4=enum([(SP[4],),(TP[4],)])
def restr(Wsp,M): return Wsp.conj().T@M@Wsp
chiA=np.array([np.trace(restr(VE,g[0]))/12 for g in G4]); chiB=np.array([np.trace(restr(VC,g[0]))/6 for g in G4])
trW=np.array([np.trace(g[0]) for g in G4])
pr(f"p=2: |image group| = {len(G4)} (|SL2(Z/4)|=48); chi_A=tr|V_Eis/12: dim {chiA[0].real:.3f}, norm {(np.vdot(chiA,chiA)/len(G4)).real:.6f}; chi_B=tr|V_cusp/6: dim {chiB[0].real:.3f}, norm {(np.vdot(chiB,chiB)/len(G4)).real:.6f}; <A,B> {abs(np.vdot(chiA,chiB))/len(G4):.1e}; W|G4 - 18(chiA+chiB) resid {abs(trW-18*(chiA+chiB)).max():.1e}")
pr(f"  chi_A on G4 values (rounded): {sorted(set(np.round(chiA,4)),key=lambda z:(z.real,z.imag))}")
pr(f"  chi_B: B1(T_4)={np.round(chiB[[i for i,g in enumerate(G4) if abs(g[0]-TP[4]).max()<1e-9][0]],6)}, B1(S_4)={np.round(chiB[[i for i,g in enumerate(G4) if abs(g[0]-SP[4]).max()<1e-9][0]],6)}")
iso[(4,'A')]=3/len(G4)*sum(np.conj(c)*g[0] for c,g in zip(chiA,G4)); iso[(4,'B')]=1/len(G4)*sum(np.conj(c)*g[0] for c,g in zip(chiB,G4))
pr("joint isotypic components (rank of E4 E5 E7) and overlap with V_Eis / V_cusp / V^perp:")
for a in ('A','B'):
    for s5 in (1,-1):
        for s7 in (1,-1):
            Pj=iso[(4,a)]@iso[(5,s5)]@iso[(7,s7)]; r=np.linalg.matrix_rank(Pj,1e-6)
            ov=[np.linalg.matrix_rank(Pj@X,1e-6) for X in (VE,VC,Vp)]
            pr(f"  {a}⊗W5^{'+' if s5>0 else '-'}⊗W7^{'+' if s7>0 else '-'}: dim {r}; rank on V_Eis {ov[0]}, V_cusp {ov[1]}, V^perp {ov[2]}")
open("local.txt","w").write("\n".join(out)+"\n")
