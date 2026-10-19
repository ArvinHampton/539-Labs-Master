# Exact rev6 label operators at s=7 (Y convention = Family.Pmatrix convention: row i = source label, column j(i) = target label).
# Built from the unchanged family_s.py (imported, not copied or edited). Phases returned as Fractions mod 1.
import sys, pickle
sys.path.insert(0,'/workspace/quantum-comp/reports/heavy-daily/2026-10-18-Open-Algebraic')
import numpy as np
from fractions import Fraction as Fr
from family_s import Family
class FamilyX(Family):
    @staticmethod
    def e(fr): return Fr(fr)%1          # exponent instead of complex number
    def reduce(self,al,be):
        al=np.array(al); be=np.array(be)
        for b0 in self.BES:
            mu=be-np.array(b0)
            if self.inLp(mu):
                return self.IDX[(tuple(al%self.D),b0)], self.B(al,mu)%1
        raise ValueError
    def S_exact(self):   # S_lab[i,j] = e(r_ij)/sqrt(35)
        M={}
        for i,(al,be) in enumerate(self.LABELS):
            al=np.array(al); be=np.array(be); pre=self.B(al,be)%1
            for p in self.LP:
                j,ph=self.reduce(p-be,al)
                assert (i,j) not in M, "two terms in one entry"
                M[(i,j)]=(pre+ph)%1
        return M
    def T_exact(self):
        T={}
        for i,(al,be) in enumerate(self.LABELS):
            al=np.array(al); be=np.array(be)
            j,ph=self.reduce(al,al+be+self.WC)
            T[(i,j)]=(-self.Q(al)-self.B(al,self.WC)+ph)%1
        return T
    def P_exact(self):
        P={}
        for i,(al,be) in enumerate(self.LABELS):
            j,ph=self.reduce(-np.array(al),-np.array(be)); P[(i,j)]=ph%1
        return P
if __name__=="__main__":
    F=FamilyX(7); S=F.S_exact(); T=F.T_exact(); P=F.P_exact()
    dens=sorted({x.denominator for x in list(S.values())+list(T.values())+list(P.values())})
    print('N labels',F.N,'S entries',len(S),'T entries',len(T),'denominators',dens)
    pickle.dump({'labels':F.LABELS,'D':F.D,'S':S,'T':T,'P':P},open('rev_s7_exact.pkl','wb'))
    # sanity vs complex family_s
    Fc=Family(7); Sc=Fc.Smatrix(); Tc=Fc.Tmatrix()
    import cmath,math
    Sx=np.zeros((F.N,F.N),complex); Tx=np.zeros((F.N,F.N),complex)
    for (i,j),r in S.items(): Sx[i,j]=cmath.exp(2j*math.pi*float(r))/math.sqrt(35)
    for (i,j),r in T.items(): Tx[i,j]=cmath.exp(2j*math.pi*float(r))
    print('match complex family_s:',np.abs(Sx-Sc).max(),np.abs(Tx-Tc).max())
