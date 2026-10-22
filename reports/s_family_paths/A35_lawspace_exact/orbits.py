# A35: exact orbit form of the symmetry relations: each symbol s equals zeta^e * (orbit representative) or is forced to 0.
from symbols import *
from exact_dim import automorphs, inv2, mat
def orbits():
    auts=automorphs(); edges=[]
    for gm in auts:
        gi=inv2(gm)
        for s in range(105):
            al,be=sym_pair(FAM[s//35],s%35); k,e=reduce(mat(gi,al),mat(gi,be)); edges.append((s,k,e))   # G_s = e(e/L) G_k
    # BFS: assign each symbol a (root, phase) with G_s = e(ph/L) G_root ; detect contradictions (=> orbit vanishes)
    rep={}; zero=set()
    adj={}
    for s,k,e in edges: adj.setdefault(s,[]).append((k,e)); adj.setdefault(k,[]).append((s,-e))
    for s0 in range(105):
        if s0 in rep: continue
        rep[s0]=(s0,0); stack=[s0]; bad=False; comp=[s0]
        while stack:
            s=stack.pop(); r,ph=rep[s]
            for k,e in adj.get(s,[]):
                # G_s = e(e) G_k  => G_k = e(-e) G_s = e(ph-e) G_root
                want=(ph-e)%L
                if k not in rep: rep[k]=(s0,want); stack.append(k); comp.append(k)
                elif rep[k][1]!=want: bad=True
        if bad: zero.update(comp)
    roots=sorted({rep[s][0] for s in range(105) if s not in zero})
    return rep,zero,roots,len(auts)
if __name__=='__main__':
    rep,zero,roots,na=orbits()
    print('automorphs',na,'vanishing symbols',len(zero),'surviving orbits',len(roots))
    print('orbit families',[ (FAM[r//35], sum(1 for s in rep if rep[s][0]==r and s not in zero)) for r in roots])
