# Exact special values of the cone (ray-class) zeta  zeta_E(s) = sum_{nu in F cap (a+Z^2)} Q2(nu)^{-s}
# from the Euler-Maclaurin expansion  sum_F e^{-t Q2} = Res/t + sum_j (-1)^j zeta_E(-j) t^j / j!
# (no half-integer powers).  Q2 = x^2 + s x y + (s/2) y^2 ; a = (s/(2(s-2)), -1/(s-2)); F = C0 u rho2 C0.
from fractions import Fraction as Fr
import math, sympy as sp
def B(k,x): return sp.bernoulli(k, x)
def cones(s):
    s=Fr(s); a1=s/(2*(s-2)); a2=Fr(-1)/(s-2)
    def fr(z): return z-math.floor(z)
    u0=fr(a1) or Fr(1); w0=fr(a2)
    u1=fr(a2+2*a1) or Fr(1); w1=fr(-a1)
    return [((u0,w0),(Fr(1),s/2,s/2)), ((u1,w1),(s/2,s/2,Fr(1)))]
def coeffs(s):
    res={'tm1/2':0,'t0':0,'t1/2':0,'t1':0}
    for (su,sw),(A11,A12,A22) in cones(s):
        su=sp.Rational(su.numerator,su.denominator); sw=sp.Rational(sw.numerator,sw.denominator)
        A11,A12,A22=[sp.Rational(z.numerator,z.denominator) for z in (A11,A12,A22)]
        res['tm1/2']+= -B(1,sw)*sp.sqrt(sp.pi)/(2*sp.sqrt(A11)) - B(1,su)*sp.sqrt(sp.pi)/(2*sp.sqrt(A22))
        res['t0']   += B(2,sw)*A12/(2*A11) + B(2,su)*A12/(2*A22) + B(1,su)*B(1,sw)
        res['t1/2'] += -B(3,sw)/6*sp.sqrt(sp.pi)*(A12**2/A11**sp.Rational(3,2)-A22/sp.sqrt(A11)) \
                       -B(3,su)/6*sp.sqrt(sp.pi)*(A12**2/A22**sp.Rational(3,2)-A11/sp.sqrt(A22))
        res['t1']   += -B(4,sw)/24*(-4*A12**3/A11**2+6*A12*A22/A11) - B(4,su)/24*(-4*A12**3/A22**2+6*A12*A11/A22) \
                       + B(1,su)*B(3,sw)/6*(-2*A22) + B(3,su)*B(1,sw)/6*(-2*A11) + B(2,su)*B(2,sw)/4*(-2*A12)
    return {k:sp.nsimplify(sp.simplify(v)) for k,v in res.items()}
def numeric(s,t):
    # direct sum of e^{-t Q2} over F cap (a+Z^2)
    s=float(s); tot=0.0
    for (su,sw),(A11,A12,A22) in cones(int(s)):
        A11,A12,A22=float(A11),float(A12),float(A22); su=float(su); sw=float(sw)
        import numpy as np
        U=su+np.arange(0,int(math.sqrt(60/t/A11))+3)
        W=sw+np.arange(0,int(math.sqrt(60/t/A22))+3)
        q=A11*U[:,None]**2+2*A12*U[:,None]*W[None,:]+A22*W[None,:]**2
        tot+=np.exp(-t*q).sum()
    return tot
out=[]
for s in (7,8,11):
    c=coeffs(s)
    D=s*s-2*s; ratio=(s+sp.sqrt(D))/(s-sp.sqrt(D))
    I=sp.log(sp.nsimplify(sp.radsimp(ratio)))/(2*sp.sqrt(D))
    out.append(f"s={s}: D={D}, eps-ratio={sp.radsimp(ratio)}, Res=2I={sp.simplify(2*I)}")
    out.append(f"   t^(-1/2): {c['tm1/2']}   t^0 = zeta_E(0) = {c['t0']}   t^(1/2): {sp.simplify(c['t1/2'])}   t^1 = -zeta_E(-1) => zeta_E(-1) = {-c['t1']}")
    for t in (0.02,0.01,0.005):
        num=numeric(s,t); pred=float(2*I)/t+float(c['t0'])+float(c['t1'])*t
        out.append(f"   t={t}: direct={num:.12f}  2I/t+zeta(0)-zeta(-1)t={pred:.12f}  diff={num-pred:.2e}  diff/t^2={(num-pred)/t**2:.4f}")
print("\n".join(out)); open("zeta_values.txt","w").write("\n".join(out)+"\n")
