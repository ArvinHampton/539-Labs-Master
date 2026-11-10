# S-law (rev8 tex l.274): u_{a,b}(-1/w) = e(B(a,b))/sqrt35 * sum_{p in L'/Z^2} u_{p-b, a}(w).
# |coef|^2 = 1/35 on each of 35 targets. Labels: alpha mod Z^2 in {0,a}+L'; beta in {0,-a} (taken mod L'; 2a in L' so a ≡ -a).
# Second index of target = alpha, reduced mod L' to its coset rep {0,-a}. Does not read the residual law.
import json, numpy as np, sympy as sp
from fractions import Fraction as F
from math import lcm
G=[[2,7],[7,7]]; a=(F(7,10),F(-1,5)); wc=(F(1,10),F(-1,35))
Bf=lambda x,y:sum(x[i]*G[i][j]*y[j] for i in range(2) for j in range(2)); Qf=lambda x:Bf(x,x)/2
Ai=[[F(-1,5),F(1,5)],[F(1,5),F(-2,35)]]
md=lambda v:(v[0]%1,v[1]%1)
Lp=set();
for x in range(70):
  for y in range(70): Lp.add(md((Ai[0][0]*x+Ai[0][1]*y,Ai[1][0]*x+Ai[1][1]*y)))
Lp=sorted(Lp); assert len(Lp)==35
al=sorted(set(Lp)|{md((p[0]+a[0],p[1]+a[1])) for p in Lp}); assert len(al)==70
assert md((2*a[0],2*a[1])) in Lp
coset=lambda x: 0 if md(x) in Lp else 1          # 0: L', 1: a+L'
betas=[(F(0),F(0)),(-a[0],-a[1])]
labels=[(A,s) for A in al for s in (0,1)]; idx={L:i for i,L in enumerate(labels)}
T=np.zeros((140,140)); Tq=[[F(0)]*140 for _ in range(140)]
for (A,s),i in idx.items():
  b=betas[s]
  for p in Lp:
    tgt=(md((p[0]-b[0],p[1]-b[1])),coset(A)); j=idx[tgt]
    T[i,j]+=1/35; Tq[i][j]+=F(1,35)
rows=np.allclose(T.sum(1),1); cols=np.allclose(T.sum(0),1)
# irreducibility / period
M=sp.Matrix(140,140,lambda i,j:sp.Rational(Tq[i][j].numerator,Tq[i][j].denominator))
reach=(np.linalg.matrix_power((T>0).astype(int)+np.eye(140,dtype=int),140)>0).all()
# stationary pi exact: solve pi(M-I)=0, sum=1
A=(M.T-sp.eye(140)).col_join(sp.ones(1,140)); bvec=sp.zeros(140,1).col_join(sp.Matrix([1]))
sol=A.solve_least_squares(bvec) if False else None
ns=(M.T-sp.eye(140)).nullspace()
pis=[[x/sum(v) for x in v] for v in ns] if ns else []
pi=pis[0] if len(pis)==1 else None
tp=[(Qf(A)+Bf(A,wc))%1 for A,s in labels]; NT=lcm(*[t.denominator for t in tp])
push=[sp.Integer(0)]*8
if pi:
  for i,t in enumerate(tp): push[int(NT*t)%8]+=pi[i]
out=dict(row_stochastic=bool(rows),doubly_stochastic=bool(cols),irreducible=bool(reach),dim_stationary=len(ns),
 pi_uniform=bool(pi and all(x==sp.Rational(1,140) for x in pi)),NT=NT,push_T=[str(x) for x in push])
print(json.dumps(out,indent=1)); json.dump(out,open('data/explore.json','w'),indent=1)
# closed classes by (coset(alpha), s); per-class uniform stationary (doubly stochastic) pushforward to T-fibre
cls={}
for (A,s),i in idx.items(): cls.setdefault((coset(A),s),[]).append(i)
key=lambda c: tuple(sorted(c)) if c[0]!=c[1] else c
blocks={'(0,0)':cls[(0,0)],'(1,1)':cls[(1,1)],'(0,1)+(1,0)':cls[(0,1)]+cls[(1,0)]}
pc={}
for name,ix in blocks.items():
  sub=T[np.ix_(ix,ix)]; assert np.allclose(sub.sum(1),1)
  ev=np.linalg.matrix_power(sub,64); 
  v=[F(0)]*8
  for i in ix: v[int(NT*tp[i])%8]+=F(1,len(ix))
  pc[name]=dict(size=len(ix),closed=True,uniform_stationary=bool(np.allclose(ev,ev[0])) or 'periodic',push_T=[str(x) for x in v])
uni=[F(0)]*8
for t in tp: uni[int(NT*t)%8]+=F(1,140)
out.update(classes=pc,cesaro_from_uniform_push_T=[str(x) for x in uni])
print(json.dumps(out,indent=1)); json.dump(out,open('data/explore.json','w'),indent=1)
