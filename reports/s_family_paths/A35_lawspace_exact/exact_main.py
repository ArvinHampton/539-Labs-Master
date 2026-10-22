# A35 exact mod-p certificates: dim V = 36 (lower bound by eval rank, upper bound by symmetry relations),
# quotient rep, SL2 relations, Hom(V,E), Hom(V,W), Hom(V(x)chi^k, C), End(V).
import sys, json, numpy as np, flint
sys.dont_write_bytecode=True
from symbols import *
from exact_dim import automorphs, inv2, mat
from math import gcd
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A32_35_to_rho7')
import exact_hom as EH
from sympy import isprime, primitive_root
from sympy.ntheory import sqrt_mod
Lev=588000
def find_p(k0):
    k=k0
    while not isprime(k*Lev+1): k+=1
    return k*Lev+1
def nm(M,p): M=np.asarray(M,dtype=object)%p; return flint.nmod_mat(M.shape[0],M.shape[1],[int(v) for v in M.ravel()],p)
def tolist(F): return np.array([[int(F[i,j]) for j in range(F.ncols())] for i in range(F.nrows())],dtype=object)
def run(k0):
    p=find_p(k0); g=primitive_root(p); z=pow(g,(p-1)//Lev,p); zL=pow(z,Lev//L,p); z294=pow(z,Lev//29400,p)
    E=lambda e: pow(zL,int(e)%L,p); R={'p':p}
    # symmetry relations
    rel=[]
    for gm in automorphs():
        gi=inv2(gm)
        for s in range(105):
            al,be=sym_pair(FAM[s//35],s%35); k,e=reduce(mat(gi,al),mat(gi,be)); v=[0]*105; v[s]+=1; v[k]=(v[k]-E(e))%p; rel.append(v)
    Rr,rk=nm(rel,p).rref(); Rb=tolist(Rr)[:rk]; R['rel_rank']=rk
    piv=[next(j for j in range(105) if Rb[i][j]) for i in range(rk)]; nonpiv=[j for j in range(105) if j not in piv]
    R['basis_symbols']=[f"{FAM[j//35]}[{j%35}]" for j in nonpiv]
    # eval lower bound
    xs=sorted({Fr(h,m) for m in range(1,7) for h in range(-2*m,2*m) if gcd(h,m)==1})
    def Gp(al,be,x):
        m=x.denominator; Lb=4*m; N=9800*m; zN=pow(z,Lev//N,p)
        tab=[pow(zN,k,p) for k in range(N)] if False else None
        i,j=np.meshgrid(np.arange(Lb),np.arange(Lb),indexing='ij')
        v0=int(al[0]*70)+70*i; v1=int(al[1]*70)+70*j; b0,b1=int(be[0]*70),int(be[1]*70)
        Q2=2*v0*v0+14*v0*v1+7*v1*v1; Bn=v0*(2*b0+7*b1)+v1*(7*b0+7*b1)
        ph=(x.numerator*Q2+2*m*Bn)%N
        cnt=np.bincount(ph.ravel(),minlength=N)
        tot=0; w=1
        nzk=np.nonzero(cnt)[0]
        for k in nzk: tot+=int(cnt[k])*pow(zN,int(k),p)
        return tot*pow(Lb*Lb,-1,p)%p
    ev=[[Gp(*sym_pair(f,i),x) for f in FAM for i in range(35)] for x in xs]
    R['eval_points']=len(xs); R['eval_rank']=nm(ev,p).rank()
    R['relations_annihilate_evals']=bool(((np.array(ev,dtype=object).dot(np.array(Rb,dtype=object).T))%p==0).all())
    # quotient matrices
    def matp(rows):
        M=np.zeros((105,105),dtype=object)
        for j,d in enumerate(rows):
            for k,es in d.items():
                for e in es: M[j][k]=(M[j][k]+E(e))%p
        return M
    GS=matp(S_rows()); MT=matp(T_rows())
    def red(v):
        v=np.array(v,dtype=object)%p
        for i,c in enumerate(piv):
            if v[c]: v=(v-v[c]*np.array(Rb[i],dtype=object))%p
        return v
    # closure check: relations * GS, * MT stay in span
    R['relations_closed_under_S_T']=all(not red(np.array(r,dtype=object).dot(M)%p).any() for r in Rb for M in (GS,MT))
    q=lambda M: np.array([red(M[j])[nonpiv] for j in nonpiv],dtype=object)%p
    GSV,MTV=q(GS),q(MT)
    roots=sqrt_mod(35,p,all_roots=True); ok=[]
    for r in roots:
        SV=(GSV*pow(r,-1,p))%p
        ok.append((r, EH.rels(SV,MTV,p), EH.rels(SV.T%p,MTV.T%p,p)))
    R['sqrt35_relations (M, M^T)']=[(int(a),b,c) for a,b,c in ok]
    good=[(r,b,c) for r,b,c in ok if b or c]; assert len(good)==1, ok
    r,bM,bMT=good[0]; SV=(GSV*pow(r,-1,p))%p
    if not bM: SV,MTV=SV.T%p,MTV.T%p
    R['convention']='M' if bM else 'M^T'
    # rho7 on W, E, C
    F,G7,T7=EH.rho7W(p,z294)
    r7=[rr for rr in sqrt_mod(35,p,all_roots=True) if EH.rels((G7*pow(rr,-1,p))%p,T7,p)]; R['rho7_sqrt35_ok']=len(r7)
    S7=(G7*pow(r7[0],-1,p))%p; R['same_sqrt35_root']=bool(r7[0]==r)
    Cidx=[25,27,29,31,33,35]          # 0-based for orbit indices 26..36 (A32 1-based?) -- verified below
    def block_ok(ci):
        ei=[i for i in range(42) if i not in ci]
        return not (S7[np.ix_(ei,ci)]%p).any() and not (S7[np.ix_(ci,ei)]%p).any() and not (T7[np.ix_(ei,ci)]%p).any() and not (T7[np.ix_(ci,ei)]%p).any()
    for ci in ([25,27,29,31,33,35],[26,28,30,32,34,36]):
        if max(ci)<42 and block_ok(ci): Cidx=ci; break
    else: raise SystemExit('C block not found')
    Eidx=[i for i in range(42) if i not in Cidx]; R['C_indices_0based']=Cidx; R['E_C_block_diagonal']=True
    SE,TE=S7[np.ix_(Eidx,Eidx)]%p,T7[np.ix_(Eidx,Eidx)]%p; SC,TC=S7[np.ix_(Cidx,Cidx)]%p,T7[np.ix_(Cidx,Cidx)]%p
    i4=pow(zL,L//4,p)
    H={}
    H['End(V)']=EH.hom_dim(SV,MTV,SV,MTV,p)
    H['Hom(V,E)']=EH.hom_dim(SV,MTV,SE,TE,p); H['Hom(E,V)']=EH.hom_dim(SE,TE,SV,MTV,p)
    H['Hom(V,W)']=EH.hom_dim(SV,MTV,S7,T7,p)
    for k in range(12):
        cS=pow((p-i4)%p,k,p); cT=pow(z294,k*29400//12,p)
        H[f'Hom(V(x)chi^{k},C)']=EH.hom_dim(SV*cS%p,MTV*cT%p,SC,TC,p)
        H[f'Hom(C,V(x)chi^{k})']=EH.hom_dim(SC,TC,SV*cS%p,MTV*cT%p,p)
        H[f'Hom(V(x)chi^{k},E)']=EH.hom_dim(SV*cS%p,MTV*cT%p,SE,TE,p)
    R['hom']=H
    # explicit mod-p intertwiner X: V->E, and its determinant
    n1=36; I1=np.eye(n1,dtype=object); I2=np.eye(36,dtype=object)
    K=np.vstack([(np.kron(SV.T,I2)-np.kron(I1,SE))%p,(np.kron(MTV.T,I2)-np.kron(I1,TE))%p])
    ns,nul=nm(K,p).nullspace(); X=np.array([int(ns[i,0]) for i in range(36*36)],dtype=object).reshape(36,36,order='F')
    R['intertwiner_det_mod_p_nonzero']=bool(nm(X,p).det()!=0)
    np.save(f'X_modp_{p}.npy',X.astype(np.int64))
    json.dump(dict(p=p,nonpiv=nonpiv,piv=piv,Rb=[[int(v) for v in r] for r in Rb]),open(f'quot_{p}.json','w'))
    return R
if __name__=='__main__':
    out={}
    for k0 in (1,7):
        R=run(k0); out[str(R['p'])]=R; print(json.dumps({k:v for k,v in R.items() if k!='basis_symbols'}),flush=True)
    json.dump(out,open('exact_main.json','w'),indent=1)
