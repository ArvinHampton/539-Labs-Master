# Exact: rho_2 = (e(3/4) S2^{-1}, T2) on theta characteristics {00,01,10,11}; image group paired with SL2(Z/4); characters of A3 (even chars) and B1 (odd char).
from fractions import Fraction as F
import cmath, itertools
exec(open('local2.py').read().split("# Local Weil factors")[0])
def inv2(A):
    R={}
    for i,(j,ph) in A.items(): R[j]=(i,(-ph)%1)
    return R
RS=scal(inv2(S2),F(3,4)); RT=T2
key=lambda A: tuple(sorted((k,v[0],v[1]) for k,v in A.items()))
def m4(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))%4 for j in range(2)) for i in range(2))
Sm=((0,3),(1,0)); Tm=((1,1),(0,1)); Id=((1,0),(0,1))
els={(key(I2),Id):(I2,Id)}; fr=[(I2,Id)]
while fr:
    nf=[]
    for A,M in fr:
        for B,N_ in ((RS,Sm),(RT,Tm)):
            C=mul(A,B); P=m4(M,N_); k=(key(C),P)
            if k not in els: els[k]=(C,P); nf.append((C,P))
    fr=nf
imgs={key(A) for A,_ in els.values()}; mats={M for _,M in els.values()}
out=[f"pair group (rho_2(g), g mod 4): {len(els)} elements; distinct g mod 4: {len(mats)}; distinct rho_2(g): {len(imgs)}  -> rho_2 is a function of g mod 4 iff pairs = #mats: {len(els)==len(mats)}"]
ev=lambda r: cmath.exp(2j*cmath.pi*float(r))
def tr(A,sub): return sum(ev(A[i][1]) for i in sub if A[i][0]==i)
EVEN=[(0,0),(0,1),(1,0)]; ODD=[(1,1)]
# invariance of subspaces
inv_ok=all(RS[i][0] in EVEN and RT[i][0] in EVEN for i in EVEN)
chiA=[tr(A,EVEN) for A,_ in els.values()]; chiB=[tr(A,ODD) for A,_ in els.values()]; n=len(els)
nA=sum(abs(c)**2 for c in chiA)/n; nB=sum(abs(c)**2 for c in chiB)/n; ip=sum(a*b.conjugate() for a,b in zip(chiA,chiB))/n
out.append(f"span(even chars) and span(odd char) invariant: {inv_ok}; <chiA,chiA> = {nA:.12f}, <chiB,chiB> = {nB:.12f}, <chiA,chiB> = {abs(ip):.1e}  (character values are exact Gaussian integers: sums of 4th roots of unity)")
out.append(f"B1: S -> {RS[(1,1)][1]} (turns), T -> {RT[(1,1)][1]} ; A3 T-spectrum: T2 on even chars = swap(00,01) and e(1/4) on 10 -> eigenvalues 1,-1,i")
out.append(f"tr rho_2(S) on A3 = e({RS[(0,0)][1]}) (only 00 fixed) ; on B1 = e({RS[(1,1)][1]})")
print("\n".join(out)); open("rho2.txt","w").write("\n".join(out)+"\n")
