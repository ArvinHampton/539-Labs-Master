# (e') exact relation vectors in the s=98 old space (class functions on t-perp/<t>, <gamma,-1>-invariant).
import sys, json, flint
from fractions import Fraction as Fr
from item1_lead import data
s=98; m=7; p=7; Q=float(sys.argv[1])
orb,counts,modes,mod,D,Mx,no=data(s,Q)
src=open('old98_g.py').read()
body=src.split("orb,counts,modes,mod,D,Mx,no=data(s,2)")[1].split("res=dict(")[0]
exec(body)
# class-orbits under <gamma,-1>
co={}; corep=[]
for r in reps:
    if r in co: continue
    st=[r]; co[r]=len(corep); grp=[r]
    while st:
        a=st.pop()
        for b in (gam(a),neg(a)):
            if b not in co: co[b]=len(corep); st.append(b); grp.append(b)
    corep.append(grp)
nc=len(corep)
# Delta orbits inside t-perp -> class orbit
reprO={}
for x,o in orb.items(): reprO.setdefault(o,x)
rows=[[0]*len(modes) for _ in range(nc)]
for o in range(no):
    x=reprO[o]
    if x in cls:
        c=co[cls[x]]
        for j in range(len(modes)): rows[c][j]+=Mx[o][j]
M=flint.fmpz_mat(rows); rk=M.rank()
X,nul=M.transpose().nullspace()
K=[[int(X[i,j]) for i in range(nc)] for j in range(nul)]
# g-relations: e_c - e_{g c}
grel=[]
for c,grp in enumerate(corep):
    d=co[gm[grp[0]]]
    if d!=c:
        v=[0]*nc; v[c]+=1; v[d]-=1; grel.append(v)
G=flint.fmpz_mat(grel) if grel else None
rG=G.rank()
both=flint.fmpz_mat(grel+K).rank()
# are g-relations inside K?  check rows@M == 0
gin=all(all(sum(v[c]*rows[c][j] for c in range(nc))==0 for j in range(len(modes))) for v in grel)
# extra relations: K modulo span(grel): pick K vectors that are g-invariant (v_c = v_{gc})
# project: solve for combos of K that are g-symmetric
gsym=[]
for c,grp in enumerate(corep):
    d=co[gm[grp[0]]]
    if d!=c:
        v=[0]*nc; v[c]=1; v[d]=-1; gsym.append(v)
# condition symmetric: (v_c - v_{gc}) = 0 -> linear constraints on K-combos
C=flint.fmpz_mat([[sum(gs[c]*k[c] for c in range(nc)) for k in K] for gs in gsym])
Y,ny=C.nullspace()
extra=[[sum(int(Y[a,b])*K[a][c] for a in range(len(K))) for c in range(nc)] for b in range(ny)]
info=[]
for v in extra:
    sup=[c for c in range(nc) if v[c]]
    info.append({"support":[{"class_orbit":c,"coef":v[c],"rep":list(map(int,corep[c][0])),"size":len(corep[c]),
                 "q":str(Fr(Qi(corep[c][0]),2*D*D)%1)} for c in sup]})
res=dict(Qmax=Q,n_class_orbits=nc,rank=rk,kernel_dim=nul,g_relations=len(grel),g_rel_rank=rG,g_rel_in_kernel=gin,
         rank_g_plus_K=both,extra_g_symmetric_relations=len(extra),extra=info)
print(json.dumps({k:v for k,v in res.items() if k!='extra'}))
for e in info: print("extra:",[(d['class_orbit'],d['coef'],d['q'],d['size']) for d in e['support']])
json.dump(res,open(f"old98_rel_Q{int(Q)}.json","w"),indent=1,default=str)
