# Exact builder: S[i][j] = e(r_ij)/sqrt(35) (single term), T[i] -> (pi(i), t_i), with Fractions mod 1.
import sys; sys.path.insert(0,'.')
import numpy as np
from fractions import Fraction as F
from family import LABELS, LP, BES, IDX, A, D, a70, WC70, inLp, B70, Q70
N=len(LABELS)
def red(al,be):
    al=np.array(al); be=np.array(be)
    for b0 in BES:
        mu=be-np.array(b0)
        if inLp(mu): return IDX[(tuple(al%D),b0)], B70(al,mu)%1
    raise ValueError
def Sexact():
    M={}
    for i,(al,be) in enumerate(LABELS):
        al=np.array(al); be=np.array(be); pre=B70(al,be)
        for p in LP:
            j,ph=red(p-be,al)
            assert (i,j) not in M
            M[(i,j)]=(pre+ph)%1
    return M
def Texact():
    out={}
    for i,(al,be) in enumerate(LABELS):
        al=np.array(al); be=np.array(be)
        j,ph=red(al,al+be+WC70); out[i]=(j,(-Q70(al)-B70(al,WC70)+ph)%1)
    return out
def tonp(Sx,Tx):
    S=np.zeros((N,N),complex); T=np.zeros((N,N),complex)
    for (i,j),r in Sx.items(): S[i,j]=np.exp(2j*np.pi*float(r))/np.sqrt(35)
    for i,(j,r) in Tx.items(): T[i,j]=np.exp(2j*np.pi*float(r))
    return S,T
# CRT coordinates
g=np.array([14,6])
def coords(i):
    al,be=LABELS[i]; al=np.array(al)
    for e in (0,1):
        for x in range(35):
            if np.all((x*g+e*a70-al)%D==0): return (x, e, 0 if be==(0,0) else 1)
    raise ValueError
if __name__=="__main__":
    from family import Smatrix,Tmatrix
    Sx=Sexact(); Tx=Texact(); S,T=tonp(Sx,Tx)
    print("exact builder == family:",abs(S-Smatrix()).max(),abs(T-Tmatrix()).max())
    print("denominators S:",sorted({r.denominator for r in Sx.values()})[-3:],"T:",sorted({r.denominator for _,r in Tx.values()})[-3:])
    C=[coords(i) for i in range(N)]; print("coords bijective:",len(set(C))==N)
