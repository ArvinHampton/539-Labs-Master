# Independent Shintani cone decompositions of the gamma-fundamental domain of S+ for the coset a+Z^2:
#   F_r = [r, gamma r)  (r incl.), non-unimodular cone; lattice points split into |det(r,gamma r)| classes
#   nu = (s0+i) r + (t0+j) gamma r,  s0 in (0,1], t0 in [0,1).  Exact EM coefficients (Bernoulli) give zeta_E(0), zeta_E(-1).
from fractions import Fraction as Fr
import sympy as sp, math, numpy as np
a=(Fr(7,10),Fr(-1,5)); g=((-1,-7),(2,13))
def Q2(v): return v[0]**2+7*v[0]*v[1]+Fr(7,2)*v[1]**2
def Bf(u,v): return Q2((u[0]+v[0],u[1]+v[1]))-Q2(u)-Q2(v)
def gv(v): return (g[0][0]*v[0]+g[0][1]*v[1],g[1][0]*v[0]+g[1][1]*v[1])
def classes(r1,r2):
    det=r1[0]*r2[1]-r1[1]*r2[0]; cl=set()
    for n1 in range(-abs(det)-2,abs(det)+3):
        for n2 in range(-abs(det)-2,abs(det)+3):
            v=(a[0]+n1,a[1]+n2)
            s=Fr(v[0]*r2[1]-v[1]*r2[0],1)/det; t=Fr(r1[0]*v[1]-r1[1]*v[0],1)/det
            s0=s-math.floor(s); t0=t-math.floor(t)
            if s0==0: s0=Fr(1)
            cl.add((s0,t0))
    return cl,abs(det)
def B(k,x): return sp.bernoulli(k,sp.Rational(x.numerator,x.denominator))
def coeffs(r1):
    r2=gv(r1); cl,det=classes(r1,r2)
    A11=sp.Rational(Q2(r1)); A22=sp.Rational(Q2(r2)); A12=sp.Rational(Bf(r1,r2))/2
    c0=0;c1=0;h=0;hh=0
    for su,sw in cl:
        Bu=lambda k:B(k,su); Bw=lambda k:B(k,sw)
        h += -Bw(1)*sp.sqrt(sp.pi)/(2*sp.sqrt(A11)) - Bu(1)*sp.sqrt(sp.pi)/(2*sp.sqrt(A22))
        c0+= Bw(2)*A12/(2*A11)+Bu(2)*A12/(2*A22)+Bu(1)*Bw(1)
        hh+= -Bw(3)/6*sp.sqrt(sp.pi)*(A12**2/A11**sp.Rational(3,2)-A22/sp.sqrt(A11)) - Bu(3)/6*sp.sqrt(sp.pi)*(A12**2/A22**sp.Rational(3,2)-A11/sp.sqrt(A22))
        c1+= -Bw(4)/24*(-4*A12**3/A11**2+6*A12*A22/A11) - Bu(4)/24*(-4*A12**3/A22**2+6*A12*A11/A22) \
             + Bu(1)*Bw(3)/6*(-2*A22) + Bu(3)*Bw(1)/6*(-2*A11) + Bu(2)*Bw(2)/4*(-2*A12)
    return det,len(cl),sp.nsimplify(sp.simplify(h)),sp.simplify(c0),sp.nsimplify(sp.simplify(hh)),sp.simplify(-c1)
out=[]
for r in [(1,0),(1,1),(1,2),(2,1),(3,2)]:
    if Q2(r)<=0: continue
    det,ncl,h,z0,hh,zm1=coeffs(r)
    out.append(f"cone [r, gamma r), r={r}: |det|={det}, classes={ncl}: t^-1/2 coeff={h}, zeta_E(0)={z0}, t^1/2 coeff={hh}, zeta_E(-1)={zm1}  => zeta(-1,K)=20*zeta_E(-1)={20*zm1}")
print("\n".join(out)); open("shintani_check.txt","w").write("\n".join(out)+"\n")
