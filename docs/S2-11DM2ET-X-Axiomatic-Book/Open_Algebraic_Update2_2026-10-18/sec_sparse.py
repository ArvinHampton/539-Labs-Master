# (+,+) sector split via sparse/monomial maps; no dense NxN arrays. Usage: python3 sec_sparse.py s
import sys, math, random, json, time, resource, numpy as np, flint, sympy
from sympy.ntheory.modular import crt
from vecfam import VF
def mem(): return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6  # GB
s=int(sys.argv[1]); t0=time.time(); v=VF(s); N=v.N; K=v.K; D=v.D
def mapv(Mint):
    a=(v.AL@Mint.T)%D; b=v.BE@Mint.T; return v.reduce(a,b)
gens=[mapv(-np.eye(2,dtype=np.int64)),mapv(v.F.G.astype(np.int64))]
Mx=2*D; ps=[p for p in sympy.factorint(s*(s-2)) if p!=2]
for p in ps:
    pe=p**sympy.multiplicity(p,Mx); u=int(crt([pe,Mx//pe],[pe-1,1])[0]); gens.append(mapv(u*np.eye(2,dtype=np.int64)))
coef=-np.ones(N,dtype=np.int64); orb=-np.ones(N,dtype=np.int64); reps=[]; good=[]
for r0 in range(N):
    if orb[r0]>=0: continue
    o=len(reps); reps.append(r0); orb[r0]=o; coef[r0]=0; st=[r0]; ok=True
    while st:
        i=st.pop()
        for j,ph in gens:
            jj=j[i]; e=(coef[i]+ph[i])%K
            if orb[jj]<0: orb[jj]=o; coef[jj]=e; st.append(jj)
            elif coef[jj]!=e: ok=False
    good.append(ok)
good=np.array(good); sec_orbs=np.nonzero(good)[0]; d=len(sec_orbs)
col=-np.ones(len(reps),dtype=np.int64); col[sec_orbs]=np.arange(d); xcol=col[orb]
print(s,"N",N,"sector dim",d,"t",round(time.time()-t0,1),"maxrss GB",mem(),flush=True)
WC=np.array(v.F.WC,dtype=np.int64); a=v.AL; jT,ph=v.reduce(a,v.AL+v.BE+WC)
eT=(-np.einsum('ni,ij,nj->n',a,v.A,a)-v.B2(a,np.broadcast_to(WC,a.shape))+ph)%K
seen=np.zeros(N,bool); lens=set()
for i in range(N):
    if seen[i]: continue
    c=0;j=i
    while not seen[j]: seen[j]=True; j=jT[j]; c+=1
    lens.add(c)
Kbig=K*math.lcm(*lens); k=1
while not sympy.isprime(k*Kbig+1): k+=1
ell=k*Kbig+1; assert ell<2**62
zeta=pow(sympy.primitive_root(ell),(ell-1)//Kbig,ell); z=pow(zeta,Kbig//K,ell)
B=1<<13; nb=K//B+2
lo=np.array([pow(z,i,ell) for i in range(B)],dtype=object); hi=np.array([pow(z,i*B,ell) for i in range(nb)],dtype=object)
def zv(e): e=np.asarray(e,dtype=np.int64); return (hi[e>>13]*lo[e&(B-1)])%ell
print(s,"K",K,"Kbig",Kbig,"ell",ell,flush=True)
def restrict_row(jcols, exps):
    m=xcol[jcols]>=0; x=jcols[m]; val=zv((exps[m]+coef[x])%K); out=[0]*d
    for c,vv in zip(xcol[x].tolist(),val.tolist()): out[c]=(out[c]+vv)%ell
    return out
LP=np.array(v.F.LP,dtype=np.int64); Srows=[]; Trows=[]
for o in sec_orbs:
    i=reps[o]; al=v.AL[i]; be=v.BE[i]
    jj,phs=v.reduce(LP-be,np.broadcast_to(al,(len(LP),2))); pre=v.B2(al,be)%K
    Srows.append(restrict_row(jj,(phs+pre)%K))
    Trows.append(restrict_row(np.array([jT[i]]),np.array([eT[i]])))
Sd=flint.nmod_mat(Srows,ell); Td=flint.nmod_mat(Trows,ell); del Srows,Trows
print(s,"Sd,Td built t",round(time.time()-t0,1),"maxrss GB",mem(),flush=True)
fac=Td.charpoly().factor()[1]; assert all(f.degree()==1 for f,e in fac)
cols=[]; blocks=[]
Id=flint.nmod_mat(d,d,[int(i==j) for i in range(d) for j in range(d)],ell)
for f,e in fac:
    lam=int(-f[0])%ell
    Y,ny=(Td-Id*lam).nullspace(); assert ny==e
    idx=list(range(len(cols),len(cols)+ny)); blocks.append(idx); cols+=[[int(Y[i,j]) for i in range(d)] for j in range(ny)]
P=flint.nmod_mat(cols,ell).transpose(); del cols; Sp=P.inv()*Sd*P
unk=[(i,j) for idx in blocks for i in idx for j in idx]; nU=len(unk)
print(s,"T-eigendecomp done; unknowns",nU,"t",round(time.time()-t0,1),"maxrss GB",mem(),flush=True)
random.seed(1); rows=[]
I_=np.array([i for i,j in unk]); J_=np.array([j for i,j in unk])
for t in range(nU+40):
    u=flint.nmod_mat(1,d,[random.randrange(ell) for _ in range(d)],ell); w=flint.nmod_mat(d,1,[random.randrange(ell) for _ in range(d)],ell)
    aa=u*Sp; bb=Sp*w
    av=np.array([int(aa[0,i]) for i in range(d)],dtype=object); uv=np.array([int(u[0,i]) for i in range(d)],dtype=object)
    bv=np.array([int(bb[i,0]) for i in range(d)],dtype=object); wv=np.array([int(w[i,0]) for i in range(d)],dtype=object)
    rows.append(((av[I_]*wv[J_]-uv[I_]*bv[J_])%ell).tolist())
NS,cub=flint.nmod_mat(rows,ell).nullspace(); del rows
print(s,"commutant upper bound",cub,"t",round(time.time()-t0,1),"maxrss GB",mem(),flush=True)
res={"s":s,"N":N,"d":d,"ell":int(ell),"Kbig":int(Kbig),"unknowns":nU,"comm_ub":cub}
dims=[]
for c in range(cub):
    X=flint.nmod_mat(d,d,[0]*(d*d),ell)
    for k_,(i,j) in enumerate(unk): X[i,j]=NS[k_,c]
    assert Sp*X==X*Sp, "spurious"
    if X==Id*int(X[0,0]): continue
    for f,e in X.charpoly().factor()[1]:
        assert f.degree()==1; mu=int(-f[0])%ell
        Kx,nk=(X-Id*mu).nullspace(); W=P*Kx
        Wk=flint.nmod_mat(d,nk,[int(W[i,j]) for i in range(d) for j in range(nk)],ell)
        SW=Sd*Wk; TW=Td*Wk
        stack=flint.nmod_mat(d,3*nk,[int(M_[i,j]) for i in range(d) for M_ in (Wk,SW,TW) for j in range(nk)],ell)
        r=stack.rank(); dims.append((nk,r)); print(s,"X-eigenspace dim",nk,"rank[W,SW,TW]",r,flush=True)
    break
res["pieces"]=dims; res["maxrss_GB"]=mem(); res["sec"]=round(time.time()-t0,1)
json.dump(res,open(f"sec_sparse_{s}.json","w"),indent=1); print(res,flush=True)
