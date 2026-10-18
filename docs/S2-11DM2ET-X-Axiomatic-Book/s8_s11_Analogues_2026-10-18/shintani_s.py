# Generalised Shintani-cone check (step 3) for s in {7,8,11}: F_r=[r, gamma r) for several r, exact 2D Euler-Maclaurin
# coefficients of sum_{nu in F_r cap (a+Z^2)} e^{-t Q2(nu)}: t^-1 (=Res term, numeric), t^-1/2, t^0 (=zeta_E(0)), t^1/2, t^1 (-> zeta_E(-1)).
from fractions import Fraction as Fr
import sympy as sp, math, sys
out=[]
for s in [7,8,11]:
    a=(Fr(s,2*(s-2)),Fr(-1,s-2)); g=((-1,-s),(2,2*s-1))
    Q2=lambda v:v[0]**2+s*v[0]*v[1]+Fr(s,2)*v[1]**2
    Bf=lambda u,v:Q2((u[0]+v[0],u[1]+v[1]))-Q2(u)-Q2(v)
    gv=lambda v:(g[0][0]*v[0]+g[0][1]*v[1],g[1][0]*v[0]+g[1][1]*v[1])
    def classes(r1,r2):
        det=r1[0]*r2[1]-r1[1]*r2[0]; cl=set()
        for n1 in range(-abs(det)-2,abs(det)+3):
            for n2 in range(-abs(det)-2,abs(det)+3):
                v=(a[0]+n1,a[1]+n2)
                S=Fr(v[0]*r2[1]-v[1]*r2[0])/det; T=Fr(r1[0]*v[1]-r1[1]*v[0])/det
                s0=S-math.floor(S); t0=T-math.floor(T)
                if s0==0: s0=Fr(1)
                cl.add((s0,t0))
        return cl,abs(det)
    B=lambda k,x:sp.bernoulli(k,sp.Rational(x.numerator,x.denominator))
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
        # t^-1 coefficient: (#classes/det... ) = (1/det)*int over cone of e^{-Q} dA / ... = area integral: (1/2)*int_0^1 dm/Qcone(1-m? ) -> use formula
        # int_{cone(r1,r2)} e^{-tQ} dx = (1/t) * (1/2) * |det(r1,r2)| * int_0^inf du / Q(r1+u r2) ; lattice covolume 1
        I=sp.Rational(1,2)*det*sp.integrate(1/(A11+2*A12*sp.Symbol('u')+A22*sp.Symbol('u')**2),(sp.Symbol('u'),0,sp.oo))
        return det,len(cl),sp.nsimplify(sp.simplify(h)),sp.simplify(c0),sp.nsimplify(sp.simplify(hh)),sp.simplify(-c1),sp.simplify(I)
    for r in [(1,0),(1,1),(2,1),(1,2),(3,1)]:
        if Q2(r)<=0: continue
        det,ncl,h,z0,hh,zm1,I=coeffs(r)
        out.append(f"s={s} cone [r,gamma r), r={r}: |det|={det}, classes={ncl}: t^-1 coeff={I} ~ {sp.N(I,15)}; t^-1/2={h}; zeta_E(0)={z0}; t^1/2={hh}; zeta_E(-1)={zm1}")
        print(out[-1],flush=True)
open("shintani_s.txt","w").write("\n".join(out)+"\n")
