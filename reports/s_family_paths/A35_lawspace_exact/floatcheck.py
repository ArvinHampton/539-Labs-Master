# A35 (Cat B sanity only): symbol S/T matrices vs direct Gauss means at positive AND negative rationals.
import sys,numpy as np,math
sys.path.insert(0,'../A33_law_vector_chi3'); from law import G
from symbols import *
from math import gcd
def mat(rows,n=105):
    M=np.zeros((n,n),complex)
    for j,d in enumerate(rows):
        for k,es in d.items(): M[j,k]+=sum(np.exp(2j*np.pi*e/L) for e in es)
    return M
MS=mat(S_rows())/math.sqrt(35); MT=mat(T_rows())
def vec(x): return np.array([G(*sym_pair(f,i),x) for f in FAM for i in range(35)])
xs=[Fr(h,m)*s for m in range(1,8) for h in range(1,2*m+1) if gcd(h,m)==1 for s in (1,-1)]
eS=max(np.abs(vec(-1/x)-MS@vec(x)/abs(float(x))).max() for x in xs)
eSsgn=max(np.abs(vec(-1/x)-MS@vec(x)/float(x)).max() for x in xs)
eT=max(np.abs(vec(x+1)-MT@vec(x)).max() for x in xs)
print(len(xs),'S |x| law err',eS,' S signed-x err',eSsgn,' T err',eT)
