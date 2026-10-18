# Item (d): W_2 = dim span{rho_2(g) delta_0}.  Lower bound: Krylov (float + mod-ell exact).  Upper bound (exact):
# isometries of Delta_2 commute with the Weil rep and fix delta_0, so W_2 <= #O(Delta_2)-orbits on Delta_2.
import sys, json, itertools, cmath, math, numpy as np
from fractions import Fraction as Fr
from family_s import Family
out=[]
for s in map(int,sys.argv[1].split(',')):
    F=Family(s); D=F.D; mo=D
    while mo%2==0: mo//=2
    m2=D//mo; eo=(pow(m2,-1,mo)*m2)%D
    # Delta_2 = 2-power torsion of L'/Z^2 (elements with zero odd part)
    els=sorted({tuple(((1-eo)*np.array(p))%D) for p in F.LP})
    els=[np.array(e) for e in els]; n=len(els); idx={tuple(e):i for i,e in enumerate(els)}
    q=[F.Q(e)%1 for e in els]
    Bm=[[F.B(a,b)%1 for b in els] for a in els]
    # generators: find a minimal generating pair by brute force (group is Z/2^a x Z/2^b)
    order=lambda e: next(k for k in range(1,4*n+1) if np.all((k*e)%D==0))
    g1=max(range(n),key=lambda i:order(els[i]))
    sub={tuple((k*els[g1])%D) for k in range(order(els[g1]))}
    g2=min((i for i in range(n) if tuple(els[i]) not in sub),key=lambda i:order(els[i]),default=None)
    gens=[g1]+([g2] if g2 is not None else [])
    # span check
    def comb(c): 
        v=np.zeros(2,dtype=object)
        for ci,gi in zip(c,gens): v=v+ci*els[gi]
        return tuple(v%D)
    ords=[order(els[g]) for g in gens]
    allc=list(itertools.product(*[range(o) for o in ords]))
    assert len({comb(c) for c in allc})==n
    cidx={comb(c):c for c in allc}
    # isometries: images of gens with matching order/q/B, extended linearly
    isos=[]
    cands=[[j for j in range(n) if order(els[j])==ords[k] and q[j]==q[gens[k]]] for k in range(len(gens))]
    for imgs in itertools.product(*cands):
        if len(gens)==2 and Bm[imgs[0]][imgs[1]]!=Bm[gens[0]][gens[1]]: continue
        perm=[]; ok=True
        for c in allc:
            v=np.zeros(2,dtype=object)
            for ci,j in zip(c,imgs): v=v+ci*els[j]
            perm.append(idx[tuple(v%D)])
        if len(set(perm))!=n: continue
        pi=[0]*n
        for c,j in zip(allc,perm): pi[idx[comb(c)]]=j
        if all(q[pi[i]]==q[i] for i in range(n)): isos.append(pi)
    # orbits
    seen=set(); norb=0
    for i in range(n):
        if i in seen: continue
        norb+=1; st=[i]; seen.add(i)
        while st:
            a=st.pop()
            for pi in isos:
                if pi[a] not in seen: seen.add(pi[a]); st.append(pi[a])
    # Krylov (float) of delta_0 under S,T (Weil rep of Delta_2)
    T=np.diag([cmath.exp(2j*math.pi*float(x)) for x in q])
    S=np.array([[cmath.exp(-2j*math.pi*float(b)) for b in row] for row in Bm])/math.sqrt(n)
    basis=np.zeros((n,0),complex); v0=np.zeros(n,complex); v0[idx[(0,0)]]=1
    frontier=[v0]
    def add(v):
        global basis
        r=v-basis@(basis.conj().T@v)
        if np.linalg.norm(r)>1e-8: basis=np.hstack([basis,(r/np.linalg.norm(r))[:,None]]); return True
        return False
    add(v0)
    while frontier:
        v=frontier.pop()
        for M in (S,T,np.linalg.inv(T)):
            w=M@v
            if add(w): frontier.append(w)
    k=0; t=s//2; vv=2*t*(t-1)
    while vv%2==0: vv//=2; k+=1
    r=dict(s=s,k=k,u_mod8=vv%8,n2=n,group_orders=ords,n_isometries=len(isos),orbit_upper=norb,krylov_float=basis.shape[1],
           formula=2**(k-1)+(4 if k%2==0 else (6 if vv%4==1 else 5)))
    print(json.dumps(r),flush=True); out.append(r)
json.dump(out,open(f"w2_orbits_{sys.argv[1].replace(',','_')}.json","w"),indent=1)
