"""Checks of corollaries of the proved profile law: (C1) vector law G(gx)=|cx+d|^-1 rho(g) G(x) for random words g,
(C2) Weil-kernel invariance G_{a,0}(x/(140x+1))|140x+1| = G_{a,0}(x)."""
import random, math, numpy as np
from fractions import Fraction as Fr
from profile_law_check import G
import thmF_exact as F
S,T,P=F.S,F.T,F.P
labs=F.LAB
def Gvec(x): return np.array([G(al,be,x) for (al,be) in labs])
out=[]
def pr(*s): print(*s); out.append(" ".join(map(str,s)))
random.seed(3)
worst=0
for trial in range(6):
    word=[random.choice("ST") for _ in range(random.randint(2,4))]
    # matrix of the word acting on x (apply rightmost first) and rho(word)
    M=np.array([[1,0],[0,1]],dtype=object); R=np.eye(140,dtype=complex)
    Sm=np.array([[0,-1],[1,0]],dtype=object); Tm=np.array([[1,1],[0,1]],dtype=object)
    for c in word:
        M=M.dot(Sm if c=="S" else Tm); R=R@(S if c=="S" else T)
    x=random.choice([Fr(1,3),Fr(-2,3),Fr(3,7),Fr(1,9)])
    a_,b_,c_,d_=M[0,0],M[0,1],M[1,0],M[1,1]
    if c_*x+d_==0: continue
    gx=(a_*x+b_)/(c_*x+d_)
    if gx==0: continue
    lhs=Gvec(gx); rhs=R@Gvec(x)/abs(float(c_*x+d_))
    dev=np.abs(lhs-rhs).max(); worst=max(worst,dev)
    pr(f"word {''.join(word)} = [[{a_},{b_}],[{c_},{d_}]], x={x}, gx={gx}: max|G(gx)-rho G(x)/|cx+d|| = {dev:.1e}, max|G(gx)| = {np.abs(lhs).max():.3f}")
pr(f"(C1) max deviation {worst:.1e}")
a=(Fr(7,10),Fr(-1,5)); z=(Fr(0),Fr(0)); w=0
for x in [Fr(1,3),Fr(-1,3),Fr(2,9),Fr(3,7),Fr(-5,3),Fr(1,11)]:
    gx=x/(140*x+1); d=abs(G(a,z,gx)*abs(float(140*x+1))-G(a,z,x)); w=max(w,d)
pr(f"(C2) G_(a,0)(x/(140x+1))|140x+1| = G_(a,0)(x) at 6 rationals: max dev {w:.1e}")
open("profile_corollaries.txt","w").write("\n".join(out)+"\n")
