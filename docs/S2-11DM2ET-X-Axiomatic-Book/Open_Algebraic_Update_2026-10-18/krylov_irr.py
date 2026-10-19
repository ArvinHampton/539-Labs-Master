# Item 2 for larger s: irreducibility via cyclic span of eigenvectors of SIMPLE T-eigenvalues in each eps-sector (unitary rho):
# if E = E1 ⊕ E2 then such a vector lies in one summand, so Krylov dims list the invariant pieces containing them.  Floating (B).
import sys, json, numpy as np
exec(open('commutant.py').read().split("    out={")[0].replace("for s in map(int,sys.argv[1].split(',')):","s=int(sys.argv[1])\nif True:"))
out={"s":s,"sectors":[]}
for eps in itertools.product((1,-1),repeat=len(ps)):
    A=np.vstack([Nm-np.eye(N),Gm-np.eye(N)]+[Z[p]-e*np.eye(N) for p,e in zip(ps,eps)])
    _,sv,vh=np.linalg.svd(A); E=vh[np.sum(sv>1e-8):].conj().T; d=E.shape[1]
    if d==0: continue
    SE=E.conj().T@S@E; TE=E.conj().T@T@E
    w,V=np.linalg.eig(TE)
    simple=[i for i in range(d) if np.sum(abs(w-w[i])<1e-6)==1]
    dims=set()
    for i in simple[:12]:
        B=np.zeros((d,0),complex); fr=[V[:,i]]
        def add(v):
            global B
            r=v-B@(B.conj().T@v); nr=np.linalg.norm(r)
            if nr>1e-8: B=np.hstack([B,(r/nr)[:,None]]); return True
            return False
        add(V[:,i])
        while fr:
            v=fr.pop()
            for Mm in (SE,TE):
                u=Mm@v
                if add(u): fr.append(u)
        dims.add(B.shape[1])
    out["sectors"].append({"eps":eps,"dim":d,"n_simple_T_eigs":len(simple),"cyclic_span_dims":sorted(dims)})
    print(out["sectors"][-1],flush=True)
json.dump(out,open(f"krylov_irr_{s}.json","w"),indent=1,default=str)
