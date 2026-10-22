# A35 exact (mod-p certificates): dim V = 36, relations, quotient matrices, SL2 relations.
import json, itertools, flint, sys
from symbols import *
from math import gcd
Lev=117600                                     # 9800*12, divisible by 29400
def find_p(k0):
    from sympy import isprime
    k=k0
    while not isprime(k*Lev+1): k+=1
    return k*Lev+1
def setup(p):
    from sympy import primitive_root
    g=primitive_root(p); return pow(g,(p-1)//Lev,p)   # primitive Lev-th root
def rank(rows,p,n):
    if not rows: return 0
    return flint.nmod_mat(len(rows),n,[int(v)%p for r in rows for v in r],p).rank()
# --- automorphs of A (search) ---
def automorphs(Bd=40):
    out=[]
    for a1,b1,c1,d1 in itertools.product(range(-Bd,Bd+1),repeat=4):
        if abs(a1*d1-b1*c1)!=1: continue
        g=((a1,b1),(c1,d1)); gT=((a1,c1),(b1,d1))
        M=[[sum(gT[i][k]*A[k][l]*g[l][j] for k in range(2) for l in range(2)) for j in range(2)] for i in range(2)]
        if M==[list(r) for r in A]: out.append(g)
    return out
def inv2(g):
    (a1,b1),(c1,d1)=g; det=a1*d1-b1*c1; return ((d1*det,-b1*det),(-c1*det,a1*det))
mat=lambda M,v:(M[0][0]*v[0]+M[0][1]*v[1], M[1][0]*v[0]+M[1][1]*v[1])
if __name__=='__main__':
    res={}
    auts=automorphs(); res['automorphs_found(|entries|<=40)']=[list(map(list,g)) for g in auts]
    # symmetry relations: G_s = G_{g^-1 al, g^-1 be} = e(ph) G_{s'}   (row vector: e_s - e(ph) e_{s'})
    rel=[]   # list of dicts {idx: [exps with sign]} -> stored as (s, s', ph)
    bad=0
    for g in auts:
        gi=inv2(g)
        for s in range(105):
            al,be=sym_pair(FAM[s//35],s%35)
            try: k,e=reduce(mat(gi,al),mat(gi,be))
            except ValueError: bad+=1; continue
            rel.append((s,k,e))
    res['symmetry relations']=len(rel); res['symmetry images outside K2-4']=bad
    Srows=S_rows(); Trows=T_rows()
    out={}
    for k0 in (1,40):
        p=find_p(k0); z=setup(p); zL=pow(z,Lev//L,p)         # primitive L-th root
        E=lambda e: pow(zL,e%L,p)
        # relation vectors mod p
        def relvec(s,k,e):
            v=[0]*105; v[s]=(v[s]+1)%p; v[k]=(v[k]-E(e))%p; return v
        Rv=[relvec(*t) for t in rel]
        def matp(rows):
            M=[[0]*105 for _ in range(105)]
            for j,d in enumerate(rows):
                for k,es in d.items():
                    for e in es: M[j][k]=(M[j][k]+E(e))%p
            return M
        GS=matp(Srows); MT=matp(Trows)          # MS = GS / sqrt35
        def vm(v,M): return [sum(v[j]*M[j][k] for j in range(105) if v[j])%p for k in range(105)]
        # closure of relation span under right mult by GS, MT (scaling irrelevant)
        Mr=flint.nmod_mat(len(Rv),105,[x for r in Rv for x in r],p); Rr,rk=Mr.rref()
        basis=[[int(Rr[i,j]) for j in range(105)] for i in range(rk)]; r0=rk
        while True:
            new=basis+[vm(v,GS) for v in basis]+[vm(v,MT) for v in basis]
            Mr=flint.nmod_mat(len(new),105,[x for r in new for x in r],p); Rr,rk2=Mr.rref()
            basis=[[int(Rr[i,j]) for j in range(105)] for i in range(rk2)]
            if rk2==rk: break
            rk=rk2
        # evaluation matrix: rows = rationals h/m with m | 12, 0<=h<12m... values G mod p
        def Gp(al,be,x):
            m=x.denominator; Lb=4*m; N=9800*m; zN=pow(z,Lev//N,p); tot=0
            for i in range(Lb):
                for j in range(Lb):
                    nu=(al[0]+i,al[1]+j); ph=(x*Q(nu)+B(nu,be))%1; k=ph*N; assert k.denominator==1
                    tot+=pow(zN,int(k),p)
            return tot*pow(Lb*Lb,-1,p)%p
        xs=sorted({Fr(h,m) for m in (1,2,3,4,6,12) for h in range(-m,2*m) if gcd(h,m)==1})
        ev=[[Gp(*sym_pair(f,i),x) for f in FAM for i in range(35)] for x in xs]
        rev=rank(ev,p,105)
        # check every evaluated row is annihilated by relations: ev * R^T == 0
        ann=all(sum(r[j]*b[j] for j in range(105))%p==0 for r in ev for b in basis)
        out[p]=dict(sym_rel_rank=r0,closed_rel_rank=rk,dim_upper=105-rk,eval_points=len(xs),eval_rank=rev,relations_vanish_on_evals=ann)
        print(p,out[p],flush=True)
        if k0==1:
            json.dump(dict(p=p,basis=basis),open('relations_p1.json','w'))
    res['mod_p']={str(k):v for k,v in out.items()}
    json.dump(res,open('exact_dim.json','w'),indent=1)
