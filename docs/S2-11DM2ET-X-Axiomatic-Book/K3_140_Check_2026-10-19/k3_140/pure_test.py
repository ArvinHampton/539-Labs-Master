import pickle, numpy as np, sympy as sp, sys
from fractions import Fraction as Fr
sys.path.insert(0,'.')
from intertwine import E,p,N,S_lab_inv,T_rev,mm,inv,r35
R=pickle.load(open('rev_s7_exact.pkl','rb')); IDX={l:i for i,l in enumerate(R['labels'])}
Xp=pickle.load(open('X_explicit.pkl','rb')); A=sp.Matrix([[2,7],[7,7]]); D=70; BES=Xp['BES']
Z=[sp.Matrix([sp.Rational(v) for v in z]) for z in Xp['Z']]; q=[Fr(x) for x in Xp['q']]
mb=sp.Matrix([sp.Rational(BES[1][0],D),sp.Rational(BES[1][1],D)])
TW=np.diag([E(x) for x in q]).astype(np.int64)
SW=np.zeros((N,N),dtype=np.int64); ir=inv(2*r35)
for k,z in enumerate(Z):
    for l,w in enumerate(Z): SW[l,k]=E(-Fr(str((z.T*A*w)[0])))*ir%p
for sgn in (1,-1):
  X=np.zeros((N,N),dtype=np.int64)
  for k,z in enumerate(Z):
    a=tuple(Xp['alpha'][k]); X[IDX[(a,BES[0])],k]=1; X[IDX[(a,BES[1])],k]=E(sgn*Fr(str((z.T*A*mb)[0])))
  print('sign',sgn,'S ok',np.array_equal(mm(X,SW),mm(S_lab_inv,X)),'T ok',np.array_equal(mm(X,TW),mm(T_rev,X)))
