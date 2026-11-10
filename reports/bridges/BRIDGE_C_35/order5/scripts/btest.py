# task (b): mixed law A2(-1/x) in colspan[A2, |x|^1/2 A1, |x| A0] on XSb (359 pts), mpmath dps 30 linear algebra
import sys, pickle, json, glob, time; sys.dont_write_bytecode=True
import mpmath as mp, numpy as np
from fractions import Fraction as Fr
from math import gcd
mp.mp.dps=30
XSb=sorted({Fr(h,m) for m in range(1,25) for h in range(1,25) if gcd(h,m)==1})
D={}
for f in glob.glob('../data/b_chunk_*.pkl'): D.update(pickle.load(open(f,'rb')))
assert sorted(D)==list(range(359)), len(D)
R=359
def col(i,kind):  # kind 0..5 = A0,A1,A2,SA0,SA1,SA2
    return [mp.mpc(*D[r][i][kind]) for r in range(R)]
xs=[mp.mpf(x.numerator)/x.denominator for x in XSb]
def scale(v,w): return [v[r]*xs[r]**w for r in range(R)]
Bcols=[col(i,2) for i in range(105)]+[scale(col(i,1),mp.mpf(1)/2) for i in range(105)]+[scale(col(i,0),1) for i in range(105)]
def nrm(v): return mp.sqrt(mp.fsum(abs(z)**2 for z in v))
def dot(q,v): return mp.fdot([z.conjugate() for z in q],v)
def orth_basis(cols,tol):
    cols=[[z/nrm(c) for z in c] if nrm(c)>0 else c for c in cols]
    res=[list(c) for c in cols]; Qb=[]; piv=[]
    while True:
        ns=[nrm(c) for c in res]; j=max(range(len(res)),key=lambda i: ns[i])
        if ns[j]<tol: return Qb,piv,ns[j]
        q=[z/ns[j] for z in res[j]]
        for _ in range(2):  # reorthogonalise q
            for p in Qb:
                c=dot(p,q); q=[a-c*b for a,b in zip(q,p)]
            nq=nrm(q); q=[z/nq for z in q]
        Qb.append(q); piv.append(ns[j])
        for i in range(len(res)):
            c=dot(q,res[i]); res[i]=[a-c*b for a,b in zip(res[i],q)]
t0=time.time()
Qb,piv,first_rej=orth_basis(Bcols,mp.mpf(10)**-20)
rB=len(Qb); gap=piv[-1]/first_rej if first_rej>0 else mp.inf
print('rank',rB,'last',mp.nstr(piv[-1],5),'first rejected',mp.nstr(first_rej,5),'t',time.time()-t0,flush=True)
def resid(T):
    v=list(T); n0=nrm(v)
    for _ in range(2):
        for p in Qb:
            c=dot(p,v); v=[a-c*b for a,b in zip(v,p)]
    return nrm(v)/n0
eps=[resid(col(i,5)) for i in range(105)]
pos=[resid(scale(col(i,3),2)) for i in range(36)]  # |x|^2 A0(-1/x)
neg=[resid(col(i,3)) for i in range(36)]
out=dict(rows=R,rank_B=rB,rows_over_rank=R/rB,gap=mp.nstr(gap,5),last_pivot=mp.nstr(piv[-1],5),first_rejected=mp.nstr(first_rej,5),
         eps_max=mp.nstr(max(eps),5),eps_min=mp.nstr(min(eps),5),pos_ctrl_max=mp.nstr(max(pos),5),neg_ctrl_min=mp.nstr(min(neg),5))
ctrl=max(pos)<=mp.mpf(10)**-20 and min(neg)>=mp.mpf(10)**-6
valid=ctrl and R>=1.5*rB and gap>=1e8
e=max(eps)
out['controls_pass']=bool(ctrl); out['valid']=bool(valid)
out['verdict']=('void/inconclusive' if not valid else ('law holds' if e<=mp.mpf(10)**-20 else ('law FALSIFIED' if e>=mp.mpf(10)**-6 else 'inconclusive')))
out['eps_all']=[mp.nstr(v,4) for v in eps]
print(json.dumps(out,indent=1)); json.dump(out,open('../data/btest.json','w'),indent=1)
