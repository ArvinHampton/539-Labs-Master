import pickle, sympy as sp
from fractions import Fraction as Fr
from collections import Counter
X=pickle.load(open('X_explicit.pkl','rb'))
Z=[sp.Matrix([sp.Rational(v) for v in z]) for z in X['Z']]; A=sp.Matrix([[2,7],[7,7]])
c={tuple(map(int,k.split(','))):Fr(v) for k,v in X['cexp'].items()}
D=70; BES=X['BES']; mbeta=sp.Matrix([sp.Rational(BES[1][0],D),sp.Rational(BES[1][1],D)])
al=[sp.Matrix([sp.Rational(a[0],D),sp.Rational(a[1],D)]) for a in X['alpha']]
res=Counter()
for k,z in enumerate(Z):
    n=z-al[k]                        # integer vector, z = alpha + n
    d=(c[(k,1)]-c[(k,0)])%1
    cand=Fr(str((z.T*A*mbeta)[0]))%1    # B(z,-a)
    res[str((d-cand)%1)]+=1
print('c1-c0 - B(z,-a) distribution:',res)
r0=Counter(); 
for k,z in enumerate(Z):
    n=z-al[k]; r0[(str(c[(k,0)]),tuple(n))]+=0
# c0 vs n=z-alpha (which of the two lifts)
r=Counter()
for k,z in enumerate(Z):
    n=tuple(int(x) for x in (z-al[k])); r[(str(c[(k,0)]),n[1]%2)]+=1
print('c0 by parity of n2:',r)
r=Counter(); r2=Counter()
for k,z in enumerate(Z):
    d=(c[(k,1)]-c[(k,0)])%1
    r[str((d-Fr(str((z.T*A*mbeta)[0])))%1)]+=0
    r2[str((d+Fr(str((z.T*A*mbeta)[0])))%1)]+=1
    # alternative: B(alpha, beta) with alpha the stored label
    r[str((d-Fr(str((al[k].T*A*mbeta)[0])))%1)]+=1
print('c1 - B(alpha_stored, beta_stored):',r); print('c1 + B(z,beta_stored):',r2)
