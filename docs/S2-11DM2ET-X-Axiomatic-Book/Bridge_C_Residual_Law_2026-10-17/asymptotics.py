# Radial asymptotics of P_s, C, C_third, H_s, q^8 f as q = e^{-t}, t -> 0+ (high-precision direct sums)
import mpmath as mp, math
mp.mp.dps = 40
Q2 = lambda x,y: x*x + 7*x*y + mp.mpf(7)/2*y*y
# Leading constant I = int_{x,y>=0} e^{-Q2}
I_num = mp.quad(lambda u: 1/(2*Q2(1,u)), [0, mp.inf])
I_cf = mp.log(6+mp.sqrt(35))/(2*mp.sqrt(35))
print("I numeric   =", I_num); print("I closed    = log(6+sqrt35)/(2 sqrt35) =", I_cf, " diff", I_num-I_cf)
# subleading t^{-1/2} constant a = (sqrt(pi)/4)(1 + 1/sqrt(7/2)) - (7/2) J,  J = int Y e^{-Q2}
J = mp.quad(lambda th: mp.sin(th)*mp.sqrt(mp.pi)/4*Q2(mp.cos(th),mp.sin(th))**(-1.5), [0, mp.pi/2])
a_pred = mp.sqrt(mp.pi)/4*(1+1/mp.sqrt(mp.mpf(7)/2)) - mp.mpf(7)/2*J
print("J =", J, "  a_pred (t^{-1/2} coeff of P_s) =", a_pred)

import numpy as np
def series_vals(t, which):
    # direct sums in float64 with log-sum care (terms are positive or signed small)
    nmax = int(math.sqrt(60/t))+5
    n = np.arange(-nmax, nmax+1)[:,None].astype(np.float64); k = np.arange(-nmax, nmax+1)[None,:].astype(np.float64)
    Qs = n*n + 7*n*k + 3.5*k*(k+1)
    sg = np.sign
    if which=="P": W = ((n>=0)&(k>=0)).astype(float)
    if which=="H": W = 0.5*(sg(5*n) - sg(-n-21*k))
    if which=="C": W = ((n>=0)&(k>=0)).astype(float) - 0.5*(sg(5*n) - sg(-n-21*k))
    if which=="Ct":  # C_third = sum_{n,k>=1} q^{Q_s(-n,-k)}
        W = ((n<=-1)&(k<=-1)).astype(float)
    E = np.where(W!=0, Qs, 0.0)
    assert (E[W!=0] >= 0).all()
    return float((W*np.exp(-t*E)).sum())
print()
print(" t        P_s(e^-t)       C(e^-t)        C_third        H_s       t*P_s   (P_s - I/t)*sqrt(t)")
rows=[]
for t in [0.08,0.04,0.02,0.01,0.005,0.0050125,0.0025,0.00125]:
    P=series_vals(t,"P"); C=series_vals(t,"C"); Ct=series_vals(t,"Ct"); H=series_vals(t,"H")
    rows.append((t,P,C,Ct,H))
    print(f"{t:<9} {P:14.6f} {C:14.6f} {Ct:14.6f} {H:12.6f} {t*P:10.6f} {(P-float(I_cf)/t)*math.sqrt(t):12.6f}")
# Richardson-type fit of P_s = I/t + a/sqrt t + b + c sqrt t
ts=[r[0] for r in rows if r[0] not in (0.0050125,)]
Ps=[r[1] for r in rows if r[0] not in (0.0050125,)]
A=np.array([[1/t,1/math.sqrt(t),1,math.sqrt(t),t] for t in ts]); sol=np.linalg.lstsq(A,np.array(Ps),rcond=None)[0]
print("\nfit P_s ~ I/t + a/sqrt(t) + b + c sqrt(t) + d t:", sol, "\n I(closed)=",float(I_cf)," a_pred=",float(a_pred))
for lab,idx in (("C",2),("C_third",3),("H_s",4)):
    ys=[r[idx] for r in rows if r[0]!=0.0050125]
    s2=np.linalg.lstsq(A,np.array(ys),rcond=None)[0]; print(f"fit {lab}: 1/t coeff {s2[0]: .8f}, t^-1/2 coeff {s2[1]: .6f}, const {s2[2]: .5f}")
