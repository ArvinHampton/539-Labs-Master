# Vectorised exact-phase evaluation of the E-vector radial coefficients at rational x:
#   E_{al,be}(e(x)e^{-t}) = 2I G(x)/t + a(x)/sqrt(t) + kappa(x) + O(t)
# F = C0 u rho2C0 ; per residue class mod L=4m (Euler-Maclaurin with Bernoulli polynomials).
import numpy as np, math
from fractions import Fraction as Fr
D = 70
A = np.array([[2,7],[7,7]])
def _B1(u): return u-0.5
def _B2(u): return u*u-u+1.0/6
SP = math.sqrt(math.pi)
def comps():
    Ainv=((Fr(-1,5),Fr(1,5)),(Fr(1,5),Fr(-2,35)))
    reps=set()
    for u in range(35):
        for w in range(35):
            reps.add(((Ainv[0][0]*u+Ainv[0][1]*w)%1,(Ainv[1][0]*u+Ainv[1][1]*w)%1))
    return sorted(reps)
REPS = comps()
a = (Fr(7,10),Fr(-1,5)); ma = (Fr(-7,10),Fr(1,5)); zero=(Fr(0),Fr(0))
def cone_terms(al, be, x):
    x = Fr(x); h, m = x.numerator, x.denominator; L = 4*m
    i = np.arange(L, dtype=np.int64)[:,None]; j = np.arange(L, dtype=np.int64)[None,:]
    tot1 = 0j; tot0 = 0j
    for which in (0,1):
        if which==0:
            u0 = Fr(al[0])%1; w0 = Fr(al[1])%1
            if u0==0: u0 = Fr(1)
            U = (u0+0)*D + D*i; W = w0*D + D*j            # 70*u, 70*w  (u in (0,L], w in [0,L))
            U = np.broadcast_to(np.int64(u0*D)+D*i,(L,L)); W = np.broadcast_to(np.int64(w0*D)+D*j,(L,L))
            N1, N2 = U, W
            A11,A12,A22 = 1.0,3.5,3.5
        else:
            u0 = (Fr(al[1])+2*Fr(al[0]))%1; w0 = (-Fr(al[0]))%1
            if u0==0: u0 = Fr(1)
            U = np.broadcast_to(np.int64(u0*D)+D*i,(L,L)); W = np.broadcast_to(np.int64(w0*D)+D*j,(L,L))
            N1, N2 = -W, U+2*W                               # nu = (-Y, X+2Y)
            A11,A12,A22 = 3.5,3.5,1.0
        # phase = x*Q2(nu) + B(nu,be),  Q2 = (2N1^2+14N1N2+7N2^2)/(2*D^2),  B = (N1*(A be)_1 + N2*(A be)_2)/D
        q2num = 2*N1*N1 + 14*N1*N2 + 7*N2*N2                 # /(9800)
        Ab = (2*be[0]+7*be[1], 7*be[0]+7*be[1])               # Fractions, denominators | 10
        den = 9800*m
        ph_num = (h*q2num) % den
        b1 = Fr(Ab[0])/D; b2 = Fr(Ab[1])/D
        lcmden = den*(b1.denominator*b2.denominator)//math.gcd(den, b1.denominator*b2.denominator)
        lcmden = np.lcm.reduce([den, b1.denominator, b2.denominator])
        P = (ph_num*(lcmden//den) + N1*(b1.numerator*(lcmden//b1.denominator)) + N2*(b2.numerator*(lcmden//b2.denominator))) % lcmden
        ph = np.exp(2j*np.pi*P/lcmden)
        su = U/(D*L); sw = W/(D*L)
        tot1 += np.sum(ph*(-_B1(sw)*SP/(2*math.sqrt(A11)) - _B1(su)*SP/(2*math.sqrt(A22))))/L
        tot0 += np.sum(ph*(_B2(sw)*A12/(2*A11) + _B2(su)*A12/(2*A22) + _B1(su)*_B1(sw)))
    return tot1, tot0
def neg(u): return (-u[0],-u[1])
def psi(x):
    x = Fr(x)
    kL = cone_terms(a, zero, -1/x)[1]
    sk = sum(cone_terms(p, ma, x)[1] for p in REPS)
    return kL - float(x)/math.sqrt(35)*sk
if __name__ == "__main__":
    for x in [Fr(1),Fr(1,3),Fr(2,3),Fr(3,7),Fr(2)]:
        print(x, psi(x))
