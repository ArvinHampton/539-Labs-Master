# Step 1(a): which ray-class cusp characters occur in the 24 cusp labels, and how they pair under sigma.
import pickle, numpy as np
d=pickle.load(open("../2026-10-17-cusp-part/fitF.pkl","rb")); pc=d['per_comp']; cyc=d['cyc']; sg=d['sg']
chars=sorted({tuple(c) for r in pc.values() for x in r.values() if x for c,_ in x['cusp_chars']})
labs=sorted(i for i,r in pc.items() for x in r.values() if x and x['cusp']>1e-12)
cols=[(c,s) for c in chars for s in (1,-1)]
M=np.zeros((len(labs),len(cols)),complex)
for a,i in enumerate(labs):
    for s,x in pc[i].items():
        if x:
            for c,v in x['cusp_chars']: M[a,cols.index((tuple(c),s))]+=v
# chi o sigma: (chi o sigma)(g_i) = chi(sigma g_i) -> exponent vector
def sig(c): return tuple(sum(c[k]*sg[i][k]*cyc[i]//cyc[k] if False else 0 for k in range(3)) for i in range(3))
def chisig(c):
    # chi(sigma(g_i)) = sum_k c_k * sg[i][k]/cyc[k] (turns); express as exponent wrt cyc[i]
    return tuple(int(round(sum(c[k]*sg[i][k]/cyc[k] for k in range(3))*cyc[i]))%cyc[i] for i in range(3))
orbits={frozenset({c,chisig(c)}) for c in chars}
out=[f"cusp characters occurring: {len(chars)}; sigma-orbits (= distinct dihedral theta series / Maass forms): {len(orbits)}; all orbits of size 2: {all(len(o)==2 for o in orbits)}",
     f"rank of label x (char,sign) content matrix: {np.linalg.matrix_rank(M,1e-6)}"]
# Since chi and chi o sigma give the same theta series, merge sigma-pairs and recompute rank
rep={c:min(o) for o in orbits for c in o}
cols2=sorted({(rep[c],s) for c,s in cols}); M2=np.zeros((len(labs),len(cols2)),complex)
for j,(c,s) in enumerate(cols): M2[:,cols2.index((rep[c],s))]+=M[:,j]
out.append(f"rank after merging sigma-pairs (= dim of cusp span in functions): {np.linalg.matrix_rank(M2,1e-6)}; forms with nonzero content: {len({c for (c,s),col in zip(cols2,M2.T) if abs(col).max()>1e-6})}")
print("\n".join(out)); open("cusp_count.txt","w").write("\n".join(out)+"\n")
