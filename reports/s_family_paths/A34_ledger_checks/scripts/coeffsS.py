# Exact Fourier coefficients of the lift components: a_{al,be}(m), m = k/Tlevel.
# a_{al,be}(m) = 1/2 sum_{x in Z^2, x = D nu, nu in al+Z^2, x^T A x = 2 D^2 m, x in gamma^2-domain} e(x^T A be / D^2)
# Returned exactly as a dict label-index -> list of phase exponents (Fractions mod 1) [each term weight 1/2].
import sys, math, json, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A9_hecke_family/scripts'); sys.dont_write_bytecode=True
from liftS import Lift
class Coeffs:
    def __init__(self,s,Tlevel):
        self.L=Lift(s); self.F=self.L.F; self.D=self.F.D; self.Lv=Tlevel; self.cache={}
        self.alidx={al:i for i,al in enumerate(self.F.ALS)}
        self.Aint=[[int(v) for v in r] for r in self.F.A]
    def K_of(self,k):
        num=2*self.D*self.D*k; return num//self.Lv if num%self.Lv==0 else None
    def terms(self,k):
        """dict label -> list of exponents (Fraction mod 1); coefficient = 1/2 * sum e(exponent)"""
        if k in self.cache: return self.cache[k]
        out={}
        K2=self.K_of(k) if k else None
        if K2 is not None:
            D=self.D; A=self.Aint
            for (x1,x2) in self.L.reps_norm(K2):
                r=(x1%D,x2%D)
                if r not in self.alidx: continue
                for be in self.F.BES:
                    be=(int(be[0]),int(be[1])); b=(A[0][0]*be[0]+A[0][1]*be[1], A[1][0]*be[0]+A[1][1]*be[1])
                    ph=Fr(x1*b[0]+x2*b[1], D*D)%1
                    out.setdefault(self.F.IDX[(r,tuple(be))],[]).append(ph)
        self.cache[k]=out; return out
    def numeric(self,k):
        v=np.zeros(self.F.N,complex)
        for i,ps in self.terms(k).items(): v[i]=0.5*sum(np.exp(2j*np.pi*float(p)) for p in ps)
        return v
