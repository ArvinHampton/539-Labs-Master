# Why 6: character content of the 6 T-eigenvectors of V_cusp, and the structure of the content tensor.
import sys, pickle, numpy as np
sys.path.insert(0,'.'); from family import Smatrix,Tmatrix
d=pickle.load(open("../2026-10-17-cusp-part/fitF.pkl","rb")); pc=d['per_comp']; sg=d['sg']; cyc=d['cyc']
labs=sorted(i for i,r in pc.items() for x in r.values() if x and x['cusp']>1e-12)
chars=sorted({tuple(c) for r in pc.values() for x in r.values() if x for c,_ in x['cusp_chars']})
cols=[(c,s) for c in chars for s in (1,-1)]
M=np.zeros((140,len(cols)),complex)
for i in labs:
    for s,x in pc[i].items():
        if x:
            for c,v in x['cusp_chars']: M[i,cols.index((tuple(c),s))]+=v
out=[]
# test 1: sigma pairs (c,13c) equal content
sig=lambda c:(c[0]*13%24,c[1],c[2])
out.append(f"content(chi o sigma) = content(chi): {max(abs(M[:,cols.index((sig(c),s))]-M[:,cols.index((c,s))]).max() for c,s in cols):.1e}")
# test 2: infinity partner eps: content(c,1,1;sign) = -sign... measure ratio content(c,eps=1)/content(c,eps=0) per sign
for s in (1,-1):
    r=[M[i,cols.index(((c0,1,1),s))]/M[i,cols.index(((c0,0,1),s))] for i in labs for c0 in range(1,24,2) if abs(M[i,cols.index(((c0,0,1),s))])>1e-8]
    out.append(f"sign {s:+d}: content(eps=1)/content(eps=0) in {sorted(set(np.round(r,8)))}")
# reduced form index: c mod 12 (sigma-orbit rep), eps ; T-eigenvectors of V_cusp
S=Smatrix(); T=Tmatrix(); U,s_,_=np.linalg.svd(M,full_matrices=False); Vc=U[:,:6]
w,X=np.linalg.eig(Vc.conj().T@T@Vc)
for k in range(6):
    v=Vc@X[:,k]; cont=v@M if False else M.T@v.conj()  # content of the function sum conj? use coefficient combination
    cont=(v[:,None]*M).sum(0)
    sup=sorted({(c[0]%12,c[1]) for (c,s),x in zip(cols,cont) if abs(x)>1e-6})
    r=np.angle(w[k])/(2*np.pi)%1
    out.append(f"T-eigvec e({round(r*140)}/140): forms (c mod 12, eps) present: {sup}")
print("\n".join(out)); open("cusp6.txt","w").write("\n".join(out)+"\n")
