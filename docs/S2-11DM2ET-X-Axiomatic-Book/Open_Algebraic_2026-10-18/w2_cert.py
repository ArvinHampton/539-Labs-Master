# (3) Exact upper certificate for W_2 at k=6: find Y = Fix(O) ∩ W^perp (rho-invariant), get exact basis, verify invariance in Z[zeta_256].
import sys, json, numpy as np, cmath, math, itertools
from fractions import Fraction as Fr
exec(open('w2_orbits.py').read().split("out=[]")[0])
from family_s import Family
s=int(sys.argv[1])
src=open('w2_orbits.py').read().split("for s in map(int,sys.argv[1].split(',')):")[1].split("    k=0; t=s//2")[0]
import textwrap; exec(textwrap.dedent(src))
W=basis; n=len(els)
# orbit indicators
orbs=[]; seen=set()
for i in range(n):
    if i in seen: continue
    o={i}; st=[i]
    while st:
        a=st.pop()
        for pi in isos:
            if pi[a] not in o: o.add(pi[a]); st.append(pi[a])
    seen|=o; orbs.append(sorted(o))
Fx=np.zeros((n,len(orbs)))
for j,o in enumerate(orbs): Fx[o,j]=1
# Y = Fix(O) ∩ W^perp, in orbit coordinates: c with W^H Fx c = 0
Mm=W.conj().T@Fx
_,sv,vh=np.linalg.svd(Mm); null=vh[np.sum(sv>1e-9):].conj().T
print("dim Fix(O)",len(orbs),"dim W",W.shape[1],"dim Y",null.shape[1])
# T-eigen decomposition of Y: group orbits by q
qs=[q[o[0]] for o in orbs]
for qv in sorted(set(qs)):
    J=[j for j in range(len(orbs)) if qs[j]==qv]
    # Y ∩ span(J): solve
    A=np.hstack([null, -np.eye(len(orbs))[:,J]])
    _,sv2,vh2=np.linalg.svd(A); k=np.sum(sv2>1e-9); ns=vh2[k:]
    if len(ns):
        for v in ns:
            c=v[null.shape[1]:]; c=c/c[np.argmax(abs(c))]
            print("q=",qv,"orbits",[ (orbs[J[t]][:3],len(orbs[J[t]])) for t in range(len(J))],"coef",np.round(c,6))
np.save("w2_Y.npy",null); json.dump({"orbs":orbs,"q":[str(x) for x in qs]},open("w2_orbs.json","w"))
# ---- exact verification in Z[zeta_Nn], Nn = lcm of denominators of B (power of 2): zeta^(Nn/2) = -1
z0=idx[(0,0)]; Nn=1
for row in Bm:
    for b in row: Nn=Nn*b.denominator//math.gcd(Nn,b.denominator)
H=Nn//2
Yex=[]
for qv in sorted(set(qs)):
    J=[j for j in range(len(orbs)) if qs[j]==qv]
    A=np.hstack([null,-np.eye(len(orbs))[:,J]]); _,sv2,vh2=np.linalg.svd(A); k=np.sum(sv2>1e-9)
    for v in vh2[k:]:
        c=v[null.shape[1]:]; c=c/c[np.argmax(abs(c))]
        y=np.zeros(n,dtype=int)
        for t,j in enumerate(J): y[orbs[j]]=int(round(c[t].real))
        Yex.append(y)
def elem(e):  # zeta^e as coefficient vector
    v=np.zeros(H,dtype=object); e%=Nn
    if e<H: v[e]+=1
    else: v[e-H]-=1
    return v
ok=True; zero=np.zeros(H,dtype=object)
for y in Yex:
    Sy=[sum((elem(-int(Bm[x][z]*Nn))*int(y[z]) for z in range(n) if y[z]),zero.copy()) for x in range(n)]
    for yj in Yex+[None]:
        pass
    # zero outside union of supports
    sup=set(i for yy in Yex for i in range(n) if yy[i])
    if any(np.any(Sy[x]!=0) for x in range(n) if x not in sup): ok=False
    for yj in Yex:
        sj=[i for i in range(n) if yj[i]]
        ref=Sy[sj[0]]*yj[sj[0]]
        if any(np.any(Sy[i]*yj[i]-ref!=0) for i in sj): ok=False
# also: Y is in Fix(O) by construction (orbit indicators) and orthogonal to delta_0 (0 not in support)
print("exact: Nn=",Nn,"S(Y) ⊂ Y:",ok," delta0 ⟂ Y:",all(y[z0]==0 for y in Yex),
      " Y independent (disjoint T-eigen supports):",np.linalg.matrix_rank(np.array(Yex))==len(Yex))
json.dump({"s":s,"Nn":Nn,"S_invariant_exact":bool(ok),"dimFixO":len(orbs),"dimY":len(Yex),"upper":len(orbs)-len(Yex),
           "Y":[{str(i):int(y[i]) for i in range(n) if y[i]} for y in Yex]},open(f"w2_cert_{s}.json","w"),indent=0)
