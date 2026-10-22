# Direct check: E = <S,T>-span of delta_0 in C[D], D = A^{-1}Z^2/Z^2, A=[[2,s],[s,s]].
# Computes dim E and tr_E S mod ell (two primes). On E (even, S^2=Z=1) tr_E S is an integer in [-dim,dim],
# so tr=0 mod ell (ell>2 dim) means tr_E S = 0; with tr_W S = 0 (A8c import) this gives tr_C S = 0.
# sqrt|D| sign ambiguity flips the sign of tr only -> irrelevant for vanishing; |tr| is reported.
import sys, numpy as np
from sympy import isprime, factorint, sqrt_mod
def run(s,ell):
    m=s//2; M=m*(m-1); N=4*M  # |det A|
    # D ~= Z^2 / A Z^2 via v -> A^{-1} v.  adj = [[s,-s],[-s,2]], det=-4M. q(v)=v^T A^{-1} v/2 = -(v^T adj v)/(8M)
    # HNF of column lattice of A: columns (2,s),(s,s). Enumerate reps by brute: reps of Z^2/AZ^2 using coset key A^{-1}v mod 1
    adj=np.array([[s,-s],[-s,2]]); reps={}
    for x in range(N):
        for y in range(2*s if False else 1):
            pass
    # Z^2/AZ^2 is generated; take box [0,N)^2 too big; use structure: lattice contains (2,s),(s,s) -> (s-2,0)... use sympy smith-free approach
    from sympy import Matrix
    from sympy.matrices.normalforms import hermite_normal_form
    H=hermite_normal_form(Matrix([[2,s],[s,s]]))  # column-style HNF
    H=np.array(H.tolist(),dtype=object)
    # reps: v=(i,j) with 0<=i<H00 , 0<=j<H11 if upper triangular
    assert H[1][0]==0, H
    reps=[(i,j) for i in range(int(H[0][0])) for j in range(int(H[1][1]))]
    assert len(reps)==N
    L=8*M
    def Bnum(v,w): return -(v[0]*(s*w[0]-s*w[1])+v[1]*(-s*w[0]+2*w[1]))  # B = Bnum/(4M) -> use units of 1/L: 2*Bnum
    z=None
    for h in range(2,ell):
        zz=pow(h,(ell-1)//L,ell)
        if all(pow(zz,L//r,ell)!=1 for r in factorint(L)): z=zz;break
    zt=[pow(z,k,ell) for k in range(L)]
    qv=np.array([zt[(Bnum(v,v))%L] for v in reps],dtype=np.int64)   # e(q)=e(Bnum/(8M))
    r=sqrt_mod(N,ell); inv=pow(int(r),ell-2,ell)
    F=np.array([[zt[(-2*Bnum(v,w))%L] for w in reps] for v in reps],dtype=np.int64)
    F=(F*inv)%ell
    basis=[];piv=[]
    def addv(v):
        for b,pc in zip(basis,piv):
            if v[pc]: v=(v-v[pc]*b)%ell
        nz=np.nonzero(v)[0]
        if len(nz)==0: return False
        pc=nz[0]; v=(v*pow(int(v[pc]),ell-2,ell))%ell
        for i in range(len(basis)):
            if basis[i][pc]: basis[i]=(basis[i]-basis[i][pc]*v)%ell
        basis.append(v);piv.append(pc);return True
    i0=reps.index((0,0)); d0=np.zeros(N,dtype=np.int64); d0[i0]=1
    addv(d0); q=[basis[0]]
    while q:
        v=q.pop()
        for w in ((F@v)%ell,(qv*v)%ell):
            if addv(w): q.append(basis[-1])
    Bm=np.array(basis); P=np.array(piv)
    # reduced row echelon: coordinates of x in basis = x[piv]
    SB=(Bm@F.T)%ell if False else np.array([(F@b)%ell for b in basis])
    tr=int(sum(int(SB[i][P[i]]) for i in range(len(basis)))%ell)
    S2ok=None
    tr=min(tr,ell-tr)
    return len(basis),tr
if __name__=="__main__":
    for s in [int(a) for a in sys.argv[1:]]:
        out=[]
        L=8*(s//2)*(s//2-1); N=L//2; cap=int((9e18/N)**0.5)
        p1=[l for l in range(L+1,cap,L) if isprime(l)]
        assert len(p1)>=2 and p1[-1]>4*N
        for ell in (p1[-1], p1[len(p1)//2]):
            assert ell*ell*N<9e18
            out.append(run(s,ell))
        print(f"s={s} |D|={4*(s//2)*(s//2-1)} dimE,|trE S| per prime: {out}",flush=True)
