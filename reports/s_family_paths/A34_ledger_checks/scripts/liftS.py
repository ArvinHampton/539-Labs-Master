# Explicit Fourier data of the manuscript theta lift u_{alpha,beta} (rev8 Sec. "The lift") for A_s, s odd.
# u_{al,be}(w) = sqrt(y)[ log(eps) [al in Z^2] + 1/2 sum_{nu in al+Z^2, nu!=0, mod gamma^2} e(B(nu,be)) K0(2pi|Q(nu)|y) e(Q(nu)x) ]
# Integer coordinates x = D*nu.  Q(nu) = x^T A x/(2D^2), B(nu,be) = x^T A be_int / D^2.
import sys, math, numpy as np
from fractions import Fraction as Fr
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/heavy-daily/2026-10-18-Open-Algebraic')
from family_s import Family
import mpmath as mp
mp.mp.dps=50   # domain decisions at 50 digits, margin asserted >1e-20
class Lift:
    def __init__(self,s):
        F=Family(s); self.F=F; self.s=s; self.D=F.D; self.A=F.A.astype(object)
        self.n=s*(s-2); self.sq=mp.sqrt(self.n); self.eps=(s-1)+self.sq
        G=np.array(F.G,dtype=object)
        # gamma preserves Q
        assert (G.T@self.A@G==self.A).all()
        self.G=G
        self.C0=mp.mpf('0.2345')   # domain t in [C0 log eps, (C0+4) log eps): avoids the exact boundary orbits t in Z log eps
    def lpm(self,x1,x2):
        s=self.s; return (x1+(s+self.sq)/2*x2, x1+(s-self.sq)/2*x2)
    def in_domain(self,x1,x2):
        # t = log|l+/l-| in [0, 4 log eps); returns (bool, margin) with mp high precision
        lp,lm=self.lpm(x1,x2); le=mp.log(self.eps); t=mp.log(abs(lp/lm))-self.C0*le; L=4*le
        return (t>=0 and t<L), min(abs(t),abs(L-t))
    def reps_norm(self,K2):
        """all integer x (any residue) with x^T A x = K2, in the gamma^2 fundamental domain. K = D^2 Q(nu) integer."""
        s=self.s; n=self.n; out=[]
        if K2==0: return out
        K=mp.mpf(K2)/2
        # |l+| <= sqrt|K| eps^(2+C0/2), |l-| <= sqrt|K|  (crude, safe)
        R=mp.sqrt(abs(K)); X2=int(mp.floor(R*(self.eps**(2+self.C0)+1)/self.sq))+1
        for x2 in range(-X2,X2+1):
            disc=n*x2*x2+2*K2   # x1 = (-s x2 +- sqrt(disc))/2
            if disc<0: continue
            r=math.isqrt(disc)
            if r*r!=disc: continue
            for sg in ((1,-1) if r else (1,)):
                num=-s*x2+sg*r
                if num%2: continue
                x1=num//2
                ok,mg=self.in_domain(x1,x2)
                assert mg>mp.mpf(10)**-20, ('boundary point',x1,x2)
                if ok: out.append((x1,x2))
        return out
