# Function-level check that the cusp/Eisenstein split is SL2(Z)-equivariant: for c in cusp set,
# the Eisenstein-labelled part of (u o S)_c = sum_{c' in E} S[c,c'] u_{c'} must vanish identically (coefficientwise), and vice versa.
import numpy as np, pickle, uvec
from collections import defaultdict
from uvec import vectors
from family import LABELS
_o=uvec.cone_pts; uvec.cone_pts=lambda a,b,r1,r2,s,Q,Bx=40:_o(a,b,r1,r2,s,Q,Bx=200)
d=pickle.load(open("fitF.pkl","rb")); pc=d['per_comp']
C=sorted({i for i,rec in pc.items() for s,r in rec.items() if r and r['cusp']>1e-12}); E=[i for i in range(140) if i not in C]
QM=40
keys={}; rows=[]
for i,(al,be) in enumerate(LABELS):
    q,ph,c=vectors(al,be,Qmax=QM); dd=defaultdict(complex)
    for n,v in zip(np.rint(19600*q).astype(np.int64),ph): dd[int(n)]+=v
    dd[0]+=c
    rows.append(dd); [keys.setdefault(k,len(keys)) for k in dd]
Cf=np.zeros((140,len(keys)),complex)
for i,dd in enumerate(rows):
    for k,v in dd.items(): Cf[i,keys[k]]=v
S=np.load("../2026-10-17-psi-conditions/S_matrix.npy")
a=np.abs(S[np.ix_(C,E)]@Cf[E]).max(); b=np.abs(S[np.ix_(E,C)]@Cf[C]).max()
out=f"|sum_(c' Eis) S[c,c'] u_c'| for c cusp: {a:.1e};  |sum_(c' cusp) S[c,c'] u_c'| for c Eis: {b:.1e}  (coefficientwise, {len(keys)} frequencies, |Q|<={QM}; scale of coefficients ~1)"
print(out); open("equiv_check.txt","w").write(out+"\n")
