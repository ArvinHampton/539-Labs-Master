# Map-C3 measurement (PREREG.md sha256 fdd4c2be...a424): P = M^2/35 on V (dim 36) mod p; rank(P-I), rank(P+I).
import sys, json, numpy as np, flint
sys.dont_write_bytecode=True
A35='/workspace/quantum-comp/reports/bridges/_git_v8_unpushed_clone/reports/s_family_paths/A35_lawspace_exact'
sys.path.insert(0,A35)
from symbols import *          # read-only import: S_rows, FAM, L
from exact_dim import automorphs, inv2, mat
from sympy import isprime, primitive_root
Lev=588000
def find_p(k):
    while not isprime(k*Lev+1): k+=1
    return k*Lev+1
def nm(M,p): M=np.asarray(M,dtype=object)%p; return flint.nmod_mat(M.shape[0],M.shape[1],[int(v) for v in M.ravel()],p)
def tolist(F): return np.array([[int(F[i,j]) for j in range(F.ncols())] for i in range(F.nrows())],dtype=object)
out={}
for k0 in (1,7,13):
    p=find_p(k0); g=primitive_root(p); z=pow(g,(p-1)//Lev,p); zL=pow(z,Lev//L,p); E=lambda e: pow(zL,int(e)%L,p)
    rel=[]
    for gm in automorphs():
        gi=inv2(gm)
        for s in range(105):
            al,be=sym_pair(FAM[s//35],s%35); k,e=reduce(mat(gi,al),mat(gi,be)); v=[0]*105; v[s]+=1; v[k]=(v[k]-E(e))%p; rel.append(v)
    Rr,rk=nm(rel,p).rref(); Rb=tolist(Rr)[:rk]
    piv=[next(j for j in range(105) if Rb[i][j]) for i in range(rk)]; nonpiv=[j for j in range(105) if j not in piv]
    GS=np.zeros((105,105),dtype=object)
    for j,d in enumerate(S_rows()):
        for kk,es in d.items():
            for e in es: GS[j][kk]=(GS[j][kk]+E(e))%p
    def red(v):
        v=np.array(v,dtype=object)%p
        for i,c in enumerate(piv):
            if v[c]: v=(v-v[c]*np.array(Rb[i],dtype=object))%p
        return v
    GSV=np.array([red(GS[j])[nonpiv] for j in nonpiv],dtype=object)%p
    I=np.eye(36,dtype=object)
    P=(GSV.dot(GSV)%p)*pow(35,-1,p)%p
    Pfull=(GS.dot(GS)%p)*pow(35,-1,p)%p; I105=np.eye(105,dtype=object)
    r={'p':p,'dimV':len(nonpiv),'P2_eq_I':bool(((P.dot(P)-I)%p==0).all()),
       'rank_P_minus_I':nm(P-I,p).rank(),'rank_P_plus_I':nm(P+I,p).rank(),
       'P105_rank_minus_I':nm(Pfull-I105,p).rank(),'P105_rank_plus_I':nm(Pfull+I105,p).rank()}
    r['dim_V_P_plus']=36-r['rank_P_minus_I']; r['dim_V_P_minus']=36-r['rank_P_plus_I']
    print(json.dumps(r),flush=True); out[str(p)]=r
json.dump(out,open('data/c3.json','w'),indent=1)
