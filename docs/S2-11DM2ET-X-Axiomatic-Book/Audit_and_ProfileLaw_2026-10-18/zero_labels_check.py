"""Exact explanation of the identically vanishing lift functions: if gamma maps the coset al+Z^2 to itself and
B(gamma nu, be) = B(nu, be) + 1/2 mod 1 on the coset, then nu -> gamma nu pairs the gamma^2-orbits with opposite phases."""
import thmF_exact as F
from fractions import Fraction as Fr
G=[[-1,-7],[2,13]]
def g(v): return (G[0][0]*v[0]+G[0][1]*v[1], G[1][0]*v[0]+G[1][1]*v[1])
res=[]
for (al,be) in F.LAB:
    if F.md(g(al))!=F.md(al): continue
    # phase shift: B(g nu, be) - B(nu, be) = B(nu, g^{-1} be - be); constant on the coset iff mu = g^{-1}be - be in L'
    Gi=[[13,7],[-2,-1]]
    gib=(Gi[0][0]*be[0]+Gi[0][1]*be[1], Gi[1][0]*be[0]+Gi[1][1]*be[1])
    mu=F.add(gib,F.neg(be))
    if F.inLp(mu) and F.Bf(al,mu)%1==Fr(1,2):
        res.append((tuple(str(c) for c in al),'be=-a' if be!=F.zero else 'be=0'))
lines=[f"labels with gamma-stable coset and phase factor -1 under gamma: {len(res)}"]+[str(r) for r in res]
print("\n".join(lines)); open("zero_labels_check.txt","w").write("\n".join(lines)+"\n")
