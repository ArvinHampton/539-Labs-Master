# S-law rev8 l.274; T-law l.276: u_{a,b}(w+1)=e(-Q(a)-B(a,w_c)) u_{a,a+b+w_c}(w). Labels: alpha mod Z^2, beta mod L' (2a, w_c-a in L').
# Label matrices: row i = expansion of u_i after the transform. |.|^2 entries. Does not read the residual law.
import json, numpy as np, sympy as sp
from fractions import Fraction as F
from math import lcm
G=[[2,7],[7,7]]; a=(F(7,10),F(-1,5)); wc=(F(1,10),F(-1,35))
Bf=lambda x,y:sum(x[i]*G[i][j]*y[j] for i in range(2) for j in range(2)); Qf=lambda x:Bf(x,x)/2
Ai=[[F(-1,5),F(1,5)],[F(1,5),F(-2,35)]]; md=lambda v:(v[0]%1,v[1]%1)
Lp=set()
for x in range(70):
  for y in range(70): Lp.add(md((Ai[0][0]*x+Ai[0][1]*y,Ai[1][0]*x+Ai[1][1]*y)))
Lp=sorted(Lp); al=sorted(set(Lp)|{md((p[0]+a[0],p[1]+a[1])) for p in Lp}); assert len(Lp)==35 and len(al)==70
coset=lambda x: 0 if md(x) in Lp else 1
assert coset((wc[0]-a[0],wc[1]-a[1]))==0 and coset((2*a[0],2*a[1]))==0
betas=[(F(0),F(0)),(-a[0],-a[1])]
labels=[(A,s) for A in al for s in (0,1)]; idx={L:i for i,L in enumerate(labels)}
S=np.zeros((140,140)); Tm=np.zeros((140,140))
for (A,s),i in idx.items():
  b=betas[s]
  for p in Lp: S[i,idx[(md((p[0]-b[0],p[1]-b[1])),coset(A))]]+=1/35
  Tm[i,idx[(A,(coset(A)+s+1)%2)]]=1     # beta' = alpha+beta+w_c mod L', w_c ≡ a
tp=[(Qf(A)+Bf(A,wc))%1 for A,s in labels]; NT=lcm(*[t.denominator for t in tp]); fib=[int(NT*t)%8 for t in tp]
def analyse(M,name):
  # closed communicating classes
  R=((M>0)|np.eye(140,dtype=bool))
  for _ in range(9): R=(R.astype(np.int64)@R.astype(np.int64))>0
  comm=[];seen=set()
  for i in range(140):
    if i in seen: continue
    c=[j for j in range(140) if R[i,j] and R[j,i]]; seen|=set(c); comm.append(c)
  closed=[c for c in comm if all(not R[i,j] or j in c for i in c for j in range(140))]
  res={'doubly_stochastic':bool(np.allclose(M.sum(0),1)),'row_stochastic':bool(np.allclose(M.sum(1),1)),'n_closed':len(closed),'classes':[]}
  for c in closed:
    sub=M[np.ix_(c,c)]
    w,v=np.linalg.eig(sub.T); k=np.argmin(abs(w-1)); pi=np.real(v[:,k]); pi/=pi.sum()
    push=[F(0)]*8
    for i,pv in zip(c,pi): push[fib[i]]+=F(pv).limit_denominator(10**6)
    cs=sorted(set((coset(labels[i][0]),labels[i][1]) for i in c))
    res['classes'].append(dict(size=len(c),coset_types=[list(x) for x in cs],pi_uniform=bool(np.allclose(pi,1/len(c))),push_T=[str(x) for x in push]))
  res['any_mass_on_2_6']=any(F(cl['push_T'][2])!=0 or F(cl['push_T'][6])!=0 for cl in res['classes'])
  return res
out={'NT':NT,'ST':analyse(S@Tm,'ST'),'TS':analyse(Tm@S,'TS'),'ST3_check_|ST|^2':None}
uni=[F(0)]*8
for f in fib: uni[f]+=F(1,140)
out['uniform_push_T']=[str(x) for x in uni]
print(json.dumps(out,indent=1)); json.dump(out,open('data/explore.json','w'),indent=1)
