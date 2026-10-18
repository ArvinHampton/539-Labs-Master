# Exact (integer/Fraction) finite checks used in the label-by-label proof.
import sys, numpy as np
sys.path.insert(0,'../2026-10-18-S-Eigenvalues'); import family as F
print('labels',F.N)
print('common gamma-stabiliser order k =',F.gamma_order())      # exact: gamma^k al = al mod Z^2, gamma^k be - be in L', B(al,.) in Z
# closure: every S-target label (p-be, al) and T-target (al, al+be+wc) reduces into the family (reduce raises otherwise)
for al,be in F.LABELS:
    al=np.array(al); be=np.array(be)
    for p in F.LP: F.reduce(p-be,al)
    F.reduce(al,al+be+F.WC70)
    F.reduce(-al,-be)
print('S/T/parity closure: OK (all targets in {0,a}+L\' x {0,-a}+L\')')
nb=sum(1 for al,be in F.LABELS if al==(0,0)); print('labels with al in Z^2 (b = log eps):',nb)
# T-law characteristic vector: e(Q(n)) = e(B(n,wc)) for n in Z^2, exact
from fractions import Fraction as Fr
ok=all((F.Q70(70*np.array(n))-F.B70(70*np.array(n),F.WC70))%1==0 for n in [(1,0),(0,1),(1,1)])
print('wc characteristic (checked on generators; Q-B is additive mod 1 since B(n,m) in Z):',ok)
