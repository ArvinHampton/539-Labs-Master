# Step (3): exact radial asymptotics at q=e^{-t} of P_s, E_s, Theta_hol for s in {7,8,11}.
#  P_s = sum_{n>=0,k>=0} q^{Q_s(n,k)} = e^{-t c0} * sum_{quadrant (a1+N, (1+a2)+K)} e^{-t Q2} + sum_{n>=0} e^{-t n^2}.
#  2D Euler-Maclaurin (Bernoulli) on the shifted quadrant (same formulas as shintani_s.py with r1=e1, r2=e2, one class).
import sympy as sp, math, mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps=30
out=[]
for s in [7,8,11]:
    a1=sp.Rational(s,2*(s-2)); a2=sp.Rational(-1,s-2); c0=sp.Rational(s,4*(s-2))
    A11=sp.Integer(1); A22=sp.Rational(s,2); A12=sp.Rational(s,2)
    su=a1; sw=1+a2
    B=lambda k,x: sp.bernoulli(k,x)
    h=-B(1,sw)*sp.sqrt(sp.pi)/(2*sp.sqrt(A11))-B(1,su)*sp.sqrt(sp.pi)/(2*sp.sqrt(A22))
    c00=B(2,sw)*A12/(2*A11)+B(2,su)*A12/(2*A22)+B(1,su)*B(1,sw)
    u=sp.Symbol('u',positive=True)
    Iq=sp.simplify(sp.Rational(1,2)*sp.integrate(1/(A11+2*A12*u+A22*u**2),(u,0,sp.oo)))
    tP_m1=Iq; tP_mh=sp.nsimplify(sp.simplify(h+sp.sqrt(sp.pi)/2)); tP_0=sp.simplify(c00-c0*Iq+sp.Rational(1,2))
    # E: t^-1 = 2*Iq... (cone integral), t^0 = zeta_E(0) - c0 * (t^-1 coeff); zeta_E(0) from shintani_s
    zE0={7:sp.Rational(1,10),8:sp.Rational(1,6),11:sp.Rational(7,18)}[s]
    Ires={7:sp.sqrt(35)*sp.log(6+sp.sqrt(35))/35,8:sp.sqrt(3)*sp.log(2+sp.sqrt(3))/6,11:sp.sqrt(11)*sp.log(10+3*sp.sqrt(11))/33}[s]
    tE_m1=Ires; tE_0=zE0-c0*Ires
    # Theta_hol from 2P = E + 1 + theta3 - Theta_hol (theta3 = sqrt(pi/t) + O(t^inf))
    tT_m1=sp.simplify(2*tP_m1-tE_m1); tT_mh=sp.simplify(sp.sqrt(sp.pi)-2*tP_mh); tT_0=sp.simplify(tE_0+1-2*tP_0)
    # numerical confirmation: direct sum of P_s at small t, remainder/sqrt(t) bounded
    def Pnum(t):
        tot=mp.mpf(0); N=int(mp.sqrt(60/t))+5
        for k in range(0,N):
            for n in range(0,N):
                Q=n*n+s*n*k+mp.mpf(s)/2*k*(k+1)
                if Q*t>60: break
                tot+=mp.e**(-t*Q)
        return tot
    rem=[]
    for t in (mp.mpf('0.02'),mp.mpf('0.005')):
        pred=float(tP_m1)/t+float(tP_mh)/mp.sqrt(t)+float(tP_0)
        rem.append((float(t),float((Pnum(t)-pred)/mp.sqrt(t))))
    out.append(f"s={s}: c0={c0}, quadrant offsets ({su},{sw})")
    out.append(f"   P_s:   t^-1: {Iq} = {sp.N(Iq,15)};  t^-1/2: {tP_mh} = {sp.N(tP_mh,15)};  t^0: {sp.simplify(tP_0)} = {sp.N(tP_0,15)}")
    out.append(f"   E_s:   t^-1: {Ires} = {sp.N(Ires,15)} (=2*quadrant: {sp.N(2*Iq-Ires,5)} diff);  t^-1/2: 0;  t^0: {sp.simplify(tE_0)} = {sp.N(tE_0,15)}")
    out.append(f"   Theta_hol: t^-1: {sp.N(tT_m1,5)};  t^-1/2: {sp.simplify(tT_mh)} = {sp.N(tT_mh,15)};  t^0: {sp.N(tT_0,15)}")
    out.append(f"   numeric check P_s: (P - three terms)/sqrt(t) at t=0.02, 0.005: {rem}")
    print("\n".join(out[-5:]),flush=True)
open("asym_s.txt","w").write("\n".join(out)+"\n")
