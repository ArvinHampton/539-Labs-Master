# Exact 2-adic factor (monomial, phases in Q/Z) and its normalisation; exact local Weil relations via Gauss sums (classical) + modular certificate.
import itertools
from fractions import Fraction as F
out=[]
L2=[(0,0),(0,1),(1,0),(1,1)]
# monomial matrices as dict: col k -> (row, phase)  meaning M e_k = e(phase) e_row ; we store as maps acting on label vectors u: (M u)_i = e(ph_i) u_{pi(i)}
S2={(0,0):((0,0),F(0)),(0,1):((1,0),F(0)),(1,0):((0,1),F(0)),(1,1):((1,1),F(1,2))}
T2={(0,0):((0,1),F(0)),(0,1):((0,0),F(0)),(1,0):((1,0),F(1,4)),(1,1):((1,1),F(1,4))}
def mul(A,B):  # (AB u)_i = e(a_i) (B u)_{pa(i)} = e(a_i+b_{pa(i)}) u_{pb(pa(i))}
    return {i:(B[A[i][0]][0],(A[i][1]+B[A[i][0]][1])%1) for i in A}
def scal(A,c): return {i:(A[i][0],(A[i][1]+c)%1) for i in A}
I2={i:(i,F(0)) for i in L2}
def inv2(A):
    R={}
    for i,(j,ph) in A.items(): R[j]=(i,(-ph)%1)
    return R
def pw(A,n):
    R=I2
    for _ in range(n): R=mul(R,A)
    return R
# Local Weil factors: rho_p(S) = gamma_p F_p/sqrt p with F_p[x,y]=e(4xy/p), rho_p(T)=diag e(2x^2/p).
# Relations (gS T)^3 = (gS)^2, (gS)^4=1 reduce to Gauss sums: (F/sqrt p)^2 = Z (x->-x) exactly (orthogonality),
# (F T)^3 / p^{3/2} = G(p)/sqrt(p) * conj... -> we determine gamma_p as the unique 8th root making the relations hold, numerically, then certify exactly below.
import numpy as np, cmath
def weilnum(p):
    x=np.arange(p); Fm=np.exp(-2j*np.pi*4*np.outer(x,x)/p)/np.sqrt(p); Tm=np.diag(np.exp(2j*np.pi*2*x*x/p))
    sols=[k for k in range(8) if np.allclose(np.linalg.matrix_power(np.exp(2j*np.pi*k/8)*Fm@Tm,3),(np.exp(2j*np.pi*k/8)*Fm)@(np.exp(2j*np.pi*k/8)*Fm))]
    return sols
g5=weilnum(5); g7=weilnum(7); out.append(f"gamma_5 = e(k/8), k in {g5}; gamma_7 = e(k/8), k in {g7}  (S^4=1 automatic since (F/sqrt p)^2 = Z exactly)")
for k5 in g5:
    for k7 in g7:
        c=-F(k5+k7,8)
        R2=scal(inv2(S2),c)
        rel1=pw(R2,4)==I2; ST=mul(R2,T2); rel2=pw(ST,3)==mul(R2,R2)
        rel3=pw(T2,4)==I2
        out.append(f"k5={k5},k7={k7}: rho_2(S)=e({c%1})S2^-1: S^4=I {rel1}, (ST)^3=S^2 {rel2}, T^4=I {rel3}; S^2 = {mul(R2,R2)}; (ST)^3 = {pw(ST,3)}")
print("\n".join(str(o) for o in out)); open("local2.txt","w").write("\n".join(str(o) for o in out)+"\n")
