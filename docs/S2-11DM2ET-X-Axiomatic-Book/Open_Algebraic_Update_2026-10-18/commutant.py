# Item 2 (phase-free route): commutant of rho on each eps-sector of U = Fix(N)∩Fix(gamma) in LABEL space.
# Sector E is rho-invariant (N, gamma, Z_p commute with rho).  dim End_rho(E) = sum mult^2 ; idempotents -> piece dims.
# Commutant solved inside T-eigenspace blocks (X commutes with T => block diagonal), then S-commutation.  Floating (B).
import sys, json, cmath, math, itertools, numpy as np, sympy
from sympy.ntheory.modular import crt
from family_s import Family
from even_exact import red
for s in map(int,sys.argv[1].split(',')):
    F=Family(s); D=F.D; S=F.Smatrix(); T=F.Tmatrix(); N=F.N
    def mat(f):
        X=np.zeros((N,N),complex)
        for i,(al,be) in enumerate(F.LABELS):
            j,ph=red(F,f(np.array(al))%D,f(np.array(be))); X[j,i]=cmath.exp(2j*math.pi*float(ph))
        return X
    Nm=mat(lambda v:-v); Gm=mat(lambda v:F.G@v)
    ps=[p for p in sympy.factorint(s*(s-2)) if p!=2]; Mx=2*D
    Z={}
    for p in ps:
        pe=p**sympy.multiplicity(p,Mx); u=int(crt([pe,Mx//pe],[pe-1,1])[0])
        Z[p]=mat(lambda v,u=u:u*v)
    comm_ok=[float(np.abs(Z[p]@S-S@Z[p]).max()) for p in ps]+[float(np.abs(Nm@S-S@Nm).max()),float(np.abs(Gm@S-S@Gm).max())]
    out={"s":s,"max_commutator_with_S":max(comm_ok),"sectors":[]}
    for eps in itertools.product((1,-1),repeat=len(ps)):
        A=np.vstack([Nm-np.eye(N),Gm-np.eye(N)]+[Z[p]-e*np.eye(N) for p,e in zip(ps,eps)])
        _,sv,vh=np.linalg.svd(A); E=vh[np.sum(sv>1e-8):].conj().T
        d=E.shape[1]
        if d==0: continue
        SE=E.conj().T@S@E; TE=E.conj().T@T@E
        w,V=np.linalg.eig(TE); Vi=np.linalg.inv(V); SE2=Vi@SE@V
        # group T-eigenvalues
        keys=[]; blocks=[]
        for i,z in enumerate(w):
            for b,k in enumerate(keys):
                if abs(z-k)<1e-6: blocks[b].append(i); break
            else: keys.append(z); blocks.append([i])
        # unknown X block-diagonal: X[blocks[b], blocks[b]] free
        var=[(i,j) for b in blocks for i in b for j in b]; vi={v:k for k,v in enumerate(var)}
        rows=[]
        # (X SE2 - SE2 X)[a,c] = sum_j X[a,j]SE2[j,c] - sum_j SE2[a,j]X[j,c]
        Mrow=np.zeros((d*d,len(var)),complex)
        for (a,j),k in vi.items():
            for c in range(d): Mrow[a*d+c,k]+=SE2[j,c]
        for (j,c),k in vi.items():
            for a in range(d): Mrow[a*d+c,k]-=SE2[a,j]
        sv2=np.linalg.svd(Mrow,compute_uv=False)
        cdim=int(np.sum(sv2<1e-8*sv2[0]))+max(0,len(var)-len(sv2))
        out["sectors"].append({"eps":eps,"dim":d,"commutant_dim":cdim})
        print(s,eps,"dim",d,"commutant",cdim,flush=True)
    json.dump(out,open(f"commutant_{s}.json","w"),indent=1,default=str)
