# Generic S/T-closed family for A_s=[[2,s],[s,s]], shift a=(s/(2(s-2)), -1/(s-2)) (generalises 2026-10-17-psi-conditions/family.py, s=7).
#   labels (al,be): al in ({0,a}+L')/Z^2, be in {0,-a} (be reduced mod L' with phase).  If a in L' (s=8) this collapses to L'/Z^2, be=0.
#   Coordinates are integers scaled by D = lcm(s(s-2), 2(s-2)).
import numpy as np, math, cmath, sys
from fractions import Fraction as Fr
class Family:
    def __init__(self,s):
        self.s=s; det=2*s-s*s; self.det=det
        D=math.lcm(s*(s-2),2*(s-2)); self.D=D
        self.A=np.array([[2,s],[s,s]])
        self.a=np.array([D*s//(2*(s-2)), -D//(s-2)])
        self.AINV=np.array([[s,-s],[-s,2]])*(D//det)   # D*A^{-1}
        assert np.all(self.A@self.AINV==D*np.eye(2,dtype=int))
        # characteristic vector: Q(n) = B(n,wc) mod 1 for n in Z^2 ; wc = A^{-1}(0, s/2 mod 1)
        self.odd = (s%2==1)
        self.WC = (self.AINV@np.array([0,1]))//2 if self.odd else np.array([0,0])
        if self.odd: assert np.all((self.AINV@np.array([0,1]))%2==0)
        self.G=np.array([[-1,-s],[2,2*s-1]]); self.GI=np.array([[2*s-1,s],[-2,-1]])
        LP=sorted({tuple((self.AINV@np.array([m1,m2]))%D) for m1 in range(abs(det)) for m2 in range(abs(det))})
        self.LP=[np.array(p) for p in LP]; assert len(LP)==abs(det)
        self.a_in_Lp=self.inLp(self.a)
        if self.a_in_Lp:
            self.ALS=[tuple(p) for p in self.LP]; self.BES=[(0,0)]
        else:
            self.ALS=[tuple(p) for p in self.LP]+[tuple((p+self.a)%D) for p in self.LP]; self.BES=[(0,0),tuple((-self.a)%D)]
        self.LABELS=[(al,be) for al in self.ALS for be in self.BES]
        self.IDX={l:i for i,l in enumerate(self.LABELS)}; self.N=len(self.LABELS)
    def inLp(self,v): return bool(np.all((self.A@v)%self.D==0))
    def B(self,n,b): return Fr(int(n@self.A@b),self.D*self.D)
    def Q(self,n): return Fr(int(n@self.A@n),2*self.D*self.D)
    @staticmethod
    def e(fr): return cmath.exp(2j*math.pi*float(fr%1))
    def reduce(self,al,be):
        al=np.array(al); be=np.array(be)
        for b0 in self.BES:
            mu=be-np.array(b0)
            if self.inLp(mu):
                return self.IDX[(tuple(al%self.D),b0)], self.e(self.B(al,mu))
        raise ValueError
    def Smatrix(self):
        M=np.zeros((self.N,self.N),complex); r=1/math.sqrt(abs(self.det))
        for i,(al,be) in enumerate(self.LABELS):
            al=np.array(al); be=np.array(be); pre=self.e(self.B(al,be))*r
            for p in self.LP:
                j,ph=self.reduce(p-be,al); M[i,j]+=pre*ph
        return M
    def Tmatrix(self):
        T=np.zeros((self.N,self.N),complex)
        for i,(al,be) in enumerate(self.LABELS):
            al=np.array(al); be=np.array(be)
            j,ph=self.reduce(al,al+be+self.WC)
            T[i,j]+=self.e(-self.Q(al)-self.B(al,self.WC))*ph
        return T
    def Pmatrix(self):
        P=np.zeros((self.N,self.N),complex)
        for i,(al,be) in enumerate(self.LABELS):
            j,ph=self.reduce(-np.array(al),-np.array(be)); P[i,j]+=ph
        return P
    def gamma_order(self):
        k=1
        while True:
            Gk=np.linalg.matrix_power(self.G,k); ok=True
            for al,be in self.LABELS:
                al=np.array(al); be=np.array(be); al2=Gk@al; be2=Gk@be
                if np.any((al2-al)%self.D): ok=False;break
                mu=be2-be
                if not self.inLp(mu) or self.B(al,mu)%1!=0: ok=False;break
            if ok: return k
            k+=1
if __name__=="__main__":
    out=[]
    for s in [int(z) for z in sys.argv[1].split(',')]:
        F=Family(s); S=F.Smatrix(); T=F.Tmatrix(); P=F.Pmatrix(); I=np.eye(F.N)
        ev=np.linalg.eigvals(P); dimP=int(np.sum(np.abs(ev-1)<1e-8))
        # T order
        Tk=T.copy(); k=1
        while not np.allclose(Tk,I,atol=1e-9) and k<5000: Tk=Tk@T; k+=1
        u=np.linalg.norm(S@S.conj().T-I)
        out.append(f"s={s}: D={F.D}, |L'/L|={abs(F.det)}, lattice {'odd, w_c='+str(F.WC)+'/'+str(F.D) if F.odd else 'even, w_c=0'}, a in L'? {F.a_in_Lp}; labels N={F.N} (#al={len(F.ALS)}, #be={len(F.BES)})")
        out.append(f"   S unitary: {u:.1e};  |S^2-P| = {np.linalg.norm(S@S-P):.1e};  |(ST)^3 - I| = {np.linalg.norm(np.linalg.matrix_power(S@T,3)-I):.1e};  |(ST)^3 - S^2| = {np.linalg.norm(np.linalg.matrix_power(S@T,3)-S@S):.1e};  P^2=I: {np.linalg.norm(P@P-I):.1e}")
        out.append(f"   order of T = {k};  P-invariant dimension = {dimP};  gamma acts on labels with order {F.gamma_order()}")
        np.save(f"S_{s}.npy",S); np.save(f"T_{s}.npy",T); np.save(f"P_{s}.npy",P)
        print("\n".join(out[-3:]),flush=True)
    open("family_s_%s.txt"%sys.argv[1].replace(',','_'),"w").write("\n".join(out)+"\n")
