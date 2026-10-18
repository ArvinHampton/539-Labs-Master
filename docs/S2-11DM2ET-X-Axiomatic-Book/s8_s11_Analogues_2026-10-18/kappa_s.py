# Exact Bernoulli (Euler-Maclaurin) t^0 coefficients kappa of the cone sums at rational x, general s (generalises fastkappa.py, s=7):
#   E_{al,be}(e(x)e^{-t}) = 2I G(x)/t + a(x)/sqrt(t) + kappa(x) + O(t^{1/2}),  cone F = C0 u rho2 C0 = [e1, gamma e1).
#   psi(x) = kappa_{a,0}(-1/x) - (x/sqrt|det|) sum_{p in L'/Z^2} kappa_{p,-a}(x).
import numpy as np, math, sys
from fractions import Fraction as Fr
from family_s import Family
SP=math.sqrt(math.pi)
def _B1(u): return u-0.5
def _B2(u): return u*u-u+1.0/6
class Kappa:
    def __init__(self,s):
        self.s=s; F=Family(s); self.F=F; self.D=F.D
        self.a=(Fr(int(F.a[0]),F.D),Fr(int(F.a[1]),F.D)); self.ma=(-self.a[0],-self.a[1])
        self.REPS=[(Fr(int(p[0]),F.D),Fr(int(p[1]),F.D)) for p in F.LP]
        self.sq=math.sqrt(abs(F.det))
    def cone_terms(self,al,be,x):
        s=self.s; D=self.D
        x=Fr(x); h,m=x.numerator,x.denominator; L=4*m
        i=np.arange(L,dtype=np.int64)[:,None]; j=np.arange(L,dtype=np.int64)[None,:]
        tot1=0j; tot0=0j
        for which in (0,1):
            if which==0:
                u0=Fr(al[0])%1; w0=Fr(al[1])%1
                if u0==0: u0=Fr(1)
                U=np.broadcast_to(np.int64(u0*D)+D*i,(L,L)); W=np.broadcast_to(np.int64(w0*D)+D*j,(L,L)); N1,N2=U,W
                A11,A12,A22=1.0,s/2,s/2
            else:
                u0=(Fr(al[1])+2*Fr(al[0]))%1; w0=(-Fr(al[0]))%1
                if u0==0: u0=Fr(1)
                U=np.broadcast_to(np.int64(u0*D)+D*i,(L,L)); W=np.broadcast_to(np.int64(w0*D)+D*j,(L,L)); N1,N2=-W,U+2*W
                A11,A12,A22=s/2,s/2,1.0
            q2num=2*N1*N1+2*s*N1*N2+s*N2*N2          # Q2 = q2num/(2D^2)
            Ab=(2*Fr(be[0])+s*Fr(be[1]), s*Fr(be[0])+s*Fr(be[1]))
            den=2*D*D*m
            b1=Ab[0]/D; b2=Ab[1]/D
            lcmden=int(np.lcm.reduce([den,b1.denominator,b2.denominator]))
            P=((h*q2num)%den*(lcmden//den)+N1*(b1.numerator*(lcmden//b1.denominator))+N2*(b2.numerator*(lcmden//b2.denominator)))%lcmden
            ph=np.exp(2j*np.pi*P/lcmden)
            su=U/(D*L); sw=W/(D*L)
            tot1+=np.sum(ph*(-_B1(sw)*SP/(2*math.sqrt(A11))-_B1(su)*SP/(2*math.sqrt(A22))))/L
            tot0+=np.sum(ph*(_B2(sw)*A12/(2*A11)+_B2(su)*A12/(2*A22)+_B1(su)*_B1(sw)))
        return tot1,tot0
    def psi(self,x):
        x=Fr(x); kL=self.cone_terms(self.a,(0,0),-1/x)[1]
        sk=sum(self.cone_terms(p,self.ma,x)[1] for p in self.REPS)
        return kL-float(x)/self.sq*sk
if __name__=="__main__":
    s=int(sys.argv[1]); K=Kappa(s)
    for x in [Fr(1),Fr(1,3),Fr(2)]: print(x,K.psi(x))
