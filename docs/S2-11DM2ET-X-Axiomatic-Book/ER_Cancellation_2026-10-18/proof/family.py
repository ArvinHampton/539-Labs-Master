# The full S/T-closed family of components for A=[[2,7],[7,7]], shift a=(7/10,-1/5):
#   u_{al,be} (Maass, weight 0) and f_{al,be} (positive-frequency q-series) for
#   al in ({0,a}+L')/Z^2 (70 classes), be in {0,-a}  -> 140 labels.
# All coordinates are integers scaled by D=70 (nu = N/70).
import numpy as np, math, cmath, itertools
from fractions import Fraction as Fr
D=70
A=np.array([[2,7],[7,7]])
a70=np.array([49,-14])                 # 70*a
AINV70=np.array([[-14,14],[14,-4]])    # 70*A^{-1}
WC70=np.array([7,-2])                  # 70*(1/10,-1/35)
G=np.array([[-1,-7],[2,13]]); GI=np.array([[13,7],[-2,-1]])
def inLp(v70): return np.all((A@v70)%D==0)          # v in L' = A^{-1}Z^2
def B70(n,b):  return Fr(int(n@A@b),D*D)             # B(nu,be) for nu=n/70, be=b/70
def Q70(n):    return Fr(int(n@A@n),2*D*D)
def e(fr):     return cmath.exp(2j*math.pi*float(fr%1))
# discriminant group L'/Z^2 (35 classes)
LP=sorted({tuple((AINV70@np.array([m1,m2]))%D) for m1 in range(35) for m2 in range(35)})
LP=[np.array(p) for p in LP]
ALS=[tuple(p) for p in LP]+[tuple((p+a70)%D) for p in LP]
BES=[(0,0),tuple(-a70)]
LABELS=[(al,be) for al in ALS for be in BES]
IDX={l:i for i,l in enumerate(LABELS)}
def reduce(al,be):
    """u_{al,be} for arbitrary al (70-scaled, any rep) and be in {0,-a}+L' -> (index, phase)."""
    al=np.array(al); be=np.array(be)
    for b0 in BES:
        mu=be-np.array(b0)
        if inLp(mu):
            ph=B70(al,mu)            # u_{al,b0+mu} = e(B(al,mu)) u_{al,b0}
            return IDX[(tuple(al%D),b0)], e(ph)
    raise ValueError("character not in {0,-a}+L'")
N=len(LABELS)
def Smatrix():
    M=np.zeros((N,N),complex)
    for i,(al,be) in enumerate(LABELS):
        al=np.array(al); be=np.array(be)
        pre=e(B70(al,be))/math.sqrt(35)
        for p in LP:
            j,ph=reduce(p-be, al)      # u_{p-be, al}
            M[i,j]+=pre*ph
    return M
def Tmatrix():
    T=np.zeros((N,N),complex)
    for i,(al,be) in enumerate(LABELS):
        al=np.array(al); be=np.array(be)
        # odd lattice: e(Q(n)) = e(B(n,wc)) with characteristic wc = A^{-1}(0,1/2) = (1/10,-1/35)
        j,ph=reduce(al, al+be+WC70)
        T[i,j]+=e(-Q70(al)-B70(al,WC70))*ph
    return T
def gamma_order():
    k=1
    while True:
        ok=True
        Gk=np.linalg.matrix_power(G,k)
        for al,be in LABELS:
            al=np.array(al); be=np.array(be)
            al2=Gk@al; be2=Gk@be
            if np.any((al2-al)%D) : ok=False;break
            mu=be2-be
            if not inLp(mu) or B70(al,mu)%1!=0: ok=False;break
        if ok: return k
        k+=1
