# Discriminant forms of even binary lattices of det -140 (Gram = 2M, det M = -35), and T-spectrum comparison with rev6.
import pickle, itertools, json, math
from fractions import Fraction as Fr
from collections import Counter
import sympy as sp
R=pickle.load(open('rev_s7_exact.pkl','rb'))
T=R['T']; N=140
nxt={i:j for (i,j) in T}; ph={i:T[(i,j)] for (i,j) in T}
seen=set(); spec=Counter(); cycles=[]
for i0 in range(N):
    if i0 in seen: continue
    cyc=[i0]; seen.add(i0); j=nxt[i0]
    while j!=i0: cyc.append(j); seen.add(j); j=nxt[j]
    th=sum(ph[i] for i in cyc)%1; c=len(cyc); cycles.append(c)
    for t in range(c): spec[((th+t)/c)%1]+=1
rev_spec=spec
print('rev6 T cycle lengths',Counter(cycles))
def disc_form(G):
    G=sp.Matrix(G); Gi=G.inv(); d=abs(G.det())
    # representatives of L'/L: y=Gi*m, m in Z^2 mod G Z^2
    reps={}
    for m1 in range(d):
        for m2 in range(d):
            y=Gi*sp.Matrix([m1,m2]); key=tuple(Fr(int(sp.fraction(v)[0]),int(sp.fraction(v)[1]))%1 for v in y)
            if key not in reps: reps[key]=y
    assert len(reps)==d
    els=[sp.Matrix([sp.Rational(k.numerator,k.denominator) for k in key]) for key in reps]
    q=[Fr(str((y.T*G*y)[0]/2))%1 for y in els]
    return els,q
cands={'N1=2A=[[4,14],[14,14]]':[[4,14],[14,14]],'N2=[[2,14],[14,28]]':[[2,14],[14,28]],
       '2*[[1,0],[0,-35]]':[[2,0],[0,-70]],'2*[[-1,0],[0,35]]':[[-2,0],[0,70]],'2*[[5,0],[0,-7]]':[[10,0],[0,-14]],
       '2*[[-5,0],[0,7]]':[[-10,0],[0,14]],'2*[[1,1],[1,-34]]':[[2,2],[2,-68]],'2*[[-1,1],[1,34]]':[[-2,2],[2,68]],
       '2*[[3,1],[1,-12]]':[[6,2],[2,-24]],'2*[[-3,1],[1,12]]':[[-6,2],[2,24]]}
out={'rev6_T_spectrum_size':len(rev_spec)}
for name,G in cands.items():
    els,q=disc_form(G)
    sp_=Counter(q); spd=Counter([(-x)%1 for x in q])
    out[name]={'matches_rev6_T_spectrum':sp_==rev_spec,'dual_matches':spd==rev_spec,
               'gauss_sum_arg/8':None}
    print(name,'T-spectrum match:',sp_==rev_spec,' dual match:',spd==rev_spec)
json.dump({k:(v if not isinstance(v,dict) else v) for k,v in out.items()},open('lattices.json','w'),indent=1)
pickle.dump(rev_spec,open('rev_spec.pkl','wb'))
